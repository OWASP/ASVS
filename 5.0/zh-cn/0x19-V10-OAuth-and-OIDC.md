# V10 OAuth 和 OIDC

## 控制目标

OAuth 2.0（本章简称 OAuth）是用于委派授权的行业标准框架。用户授权后，客户端应用便可以代表用户访问 API 等服务端资源。

OAuth 本身并不是用户认证协议。OpenID Connect（OIDC）在 OAuth 之上增加了身份层，提供标准化用户信息、单点登录（SSO）和会话管理等功能。由于 OIDC 建立在 OAuth 之上，本章针对 OAuth 的要求也适用于 OIDC。

OAuth 定义了以下角色：

* OAuth 客户端是尝试获取服务器资源访问权限的应用（例如使用已签发的访问令牌调用 API）。OAuth 客户端通常是服务端应用。
    * 机密客户端能够妥善保管用于向授权服务器证明自身身份的凭据。
    * 公共客户端无法安全保管这类凭据。因此，它不能使用 `client_id` 和 `client_secret` 等参数证明自身身份，只能通过 `client_id` 标明自己是哪一个客户端。
* OAuth 资源服务器（RS）是向 OAuth 客户端暴露资源的服务器 API。
* OAuth 授权服务器（AS）是向 OAuth 客户端签发访问令牌的服务器应用。这些访问令牌允许 OAuth 客户端代表最终用户，或代表 OAuth 客户端自身，访问 RS 资源。AS 通常是独立应用，但在合适情况下也可以集成到合适的 RS 中。
* 资源所有者（RO）是最终用户，他们授权 OAuth 客户端代表自己获取对资源服务器上托管资源的有限访问权限。资源所有者通过与授权服务器交互来同意这种委派授权。

OIDC 定义了以下角色：

* 在 OIDC 中，接入 OIDC 登录并请求身份认证服务确认用户身份的应用称为“依赖方”（Relying Party，RP）。它在 OAuth 流程中同时承担客户端角色。
* OpenID Provider（OP）是能够认证最终用户并向 RP 提供 OIDC 声明的 OAuth AS。OP 可以是身份提供方（IdP），但在联合场景中，OP 和最终用户进行认证的身份提供方可能是不同的服务器应用。

OAuth 和 OIDC 最初面向第三方应用设计，如今也经常用于第一方应用。但在第一方场景中把它们用于认证和会话管理，会增加系统复杂度，并可能带来新的安全问题。

OAuth 和 OIDC 可用于多种类型的应用，但 ASVS 以及本章要求的重点是 Web 应用和 API。

OAuth 和 OIDC 建立在 Web 技术之上，因此其他章节的通用要求始终适用。不能脱离整份标准，孤立地理解或验证本章。

本章采用 OAuth 2.0 和 OIDC 当前的最佳实践，并与 <https://oauth.net/2/> 和 <https://openid.net/developers/specs/> 发布的规范保持一致。相关 RFC 即使已经成熟，仍会持续更新，因此，实施本章要求时，与最新版本保持一致十分重要。更多信息见参考资料。

鉴于该领域的复杂性，要构建安全的 OAuth 或 OIDC 解决方案，使用知名且符合行业标准的授权服务器并采用推荐的安全配置至关重要。

本章使用的术语与 OAuth RFC 和 OIDC 规范一致，但请注意，OIDC 术语只用于 OIDC 特定要求；其他情况下使用 OAuth 术语。

在 OAuth 和 OIDC 语境中，本章中的“令牌”指：

* 访问令牌只能由资源服务器（RS）使用。它可以是通过令牌内省进行验证的引用令牌，也可以是使用相应密钥材料进行验证的自包含令牌。
* 刷新令牌只能由签发该令牌的授权服务器接收并使用。
* OIDC ID Token 只能由触发相应授权流程的客户端接收并使用。

本章部分要求的等级取决于客户端属于机密客户端还是公共客户端。强客户端认证能够降低多种攻击风险，因此 L1 应用使用机密客户端时，可以适当放宽少数要求。

## V10.1 通用 OAuth 和 OIDC 安全

本节覆盖适用于所有使用 OAuth 或 OIDC 的应用的通用架构要求。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **10.1.1** | 验证令牌只发送给确实需要使用它的组件。例如，基于浏览器的 JavaScript 应用采用 BFF（Backend for Frontend）模式时，访问令牌和刷新令牌只能由后端访问。 | 2 |
| **10.1.2** | 验证客户端只接受由同一用户代理会话发起的同一次授权流程所产生的授权服务器返回值，例如授权码或 ID Token。为此，客户端生成的 `code_verifier`、`state`、OIDC `nonce` 等秘密值必须不可猜测、仅用于该次授权流程，并与客户端以及发起该流程的用户代理会话安全绑定。 | 2 |

## V10.2 OAuth 客户端

本节详细说明 OAuth 客户端应用需要承担的安全责任。OAuth 客户端可以实现为运行在服务端的 Web 后端（通常充当 BFF）、用于服务间集成的后端服务，或者运行在浏览器中的单页应用（SPA，也称基于浏览器的应用）。

一般而言，后端客户端被视为机密客户端，前端客户端被视为公共客户端。不过，运行在最终用户设备上的原生应用在使用 OAuth 动态客户端注册时，也可以被视为机密客户端。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **10.2.1** | 验证 OAuth 客户端使用授权码流程时，能够防范由浏览器请求伪造（通常称为 CSRF）触发的令牌请求。可以使用授权码交换证明密钥（PKCE），也可以检查授权请求中发送的 `state` 参数。 | 2 |
| **10.2.2** | 验证 OAuth 客户端需要与多个授权服务器交互时，能够防范授权服务器混淆攻击。例如，可以要求授权服务器返回 `iss` 参数，并在授权响应和令牌响应中检查该参数。 | 2 |
| **10.2.3** | 验证 OAuth 客户端向授权服务器发起请求时，只请求所需的 scope（或其他授权参数）。 | 3 |

## V10.3 OAuth 资源服务器

在 ASVS 和本章语境中，资源服务器是一个 API。为提供安全访问，资源服务器必须：

* 根据令牌格式和相关协议规范验证访问令牌。例如，可以在本地验证 JWT，或者通过 OAuth 令牌内省端点向授权服务器查询令牌状态和属性。
* 如果令牌有效，则基于访问令牌中的信息和已授予权限执行授权决策。例如，资源服务器需要验证客户端（代表 RO 行事）是否被授权访问所请求的资源。

因此，以下 OAuth 和 OIDC 专用检查应在确认令牌有效之后、根据令牌内容作出授权决定之前执行。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **10.3.1** | 验证资源服务器在接受访问令牌前，会确认该令牌的预期接收方（受众）包含本资源服务器。受众信息可以记录在结构化访问令牌中，例如 JWT 的 `aud` 声明；也可以通过令牌内省端点返回的信息确认。 | 2 |
| **10.3.2** | 验证资源服务器依据访问令牌中描述委派权限的声明作出授权决定。令牌含有 `sub`、`scope`、`authorization_details` 等声明时，必须把这些声明纳入决策。 | 2 |
| **10.3.3** | 验证访问控制决策需要从访问令牌（JWT 或相关令牌内省响应）识别唯一用户时，资源服务器只采用不会被重新分配给其他用户的声明。通常应组合使用 `iss` 和 `sub`。 | 2 |
| **10.3.4** | 验证资源服务器对认证强度、认证方式或认证时效性有特定要求时，会确认访问令牌满足这些条件。例如，可以分别检查 OIDC 的 `acr`、`amr` 和 `auth_time` 声明（如有）。 | 2 |
| **10.3.5** | 验证资源服务器要求使用发送方约束访问令牌，防止被盗访问令牌被使用，或访问令牌被未授权方重放。可以采用 OAuth 2.0 双向 TLS，或 OAuth 2.0 持有证明（DPoP）。 | 3 |

## V10.4 OAuth 授权服务器

这些要求详细说明 OAuth 授权服务器的职责，包括 OpenID Provider。

客户端认证可以使用 `self_signed_tls_client_auth`，但必须满足 [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705) [第 2.2 节](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut)规定的前提条件。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **10.4.1** | 验证授权服务器为每个客户端维护预先注册的重定向 URI 允许列表，并通过精确字符串比较来检查重定向 URI。 | 1 |
| **10.4.2** | 验证授权服务器在授权响应中返回授权码时，该授权码只能用于一次令牌请求。当第二次有效请求使用已用于签发访问令牌的授权码时，授权服务器必须拒绝该令牌请求，并撤销与该授权码相关的所有已签发令牌。 | 1 |
| **10.4.3** | 验证授权码的有效期足够短。L1 和 L2 应用最长为 10 分钟，L3 应用最长为 1 分钟。 | 1 |
| **10.4.4** | 验证授权服务器只为每个客户端启用其实际需要的授权类型。不得再使用 `token`（隐式流程）或 `password`（资源所有者密码凭据流程）授权。 | 1 |
| **10.4.5** | 验证授权服务器采取措施缓解针对公共客户端的刷新令牌重放攻击，优先使用发送方约束刷新令牌，即采用持有证明（DPoP）或使用双向 TLS（mTLS）的证书绑定访问令牌。L1 和 L2 应用可以使用刷新令牌轮换。采用轮换时，授权服务器必须在刷新令牌使用后使其失效；如果收到已使用且已失效的刷新令牌，必须撤销该授权对应的所有刷新令牌。 | 1 |
| **10.4.6** | 验证在使用授权码流程时，授权服务器强制采用 PKCE（Proof Key for Code Exchange）机制，以防范授权码截获攻击。授权服务器必须要求授权请求包含有效的 `code_challenge`，且不得接受值为 `plain` 的 `code_challenge_method`；对于令牌请求，必须要求验证 `code_verifier` 参数。 | 2 |
| **10.4.7** | 验证授权服务器允许未经认证的动态客户端注册时，采取措施降低恶意客户端风险。服务器必须验证已注册 URI 等客户端元数据，取得用户同意，并在处理不可信客户端的授权请求之前向用户发出警告。 | 2 |
| **10.4.8** | 验证刷新令牌设有绝对失效时间，即使同时采用滑动过期机制也不例外。 | 2 |
| **10.4.9** | 验证已授权用户可以通过授权服务器的用户界面撤销刷新令牌和引用访问令牌，以降低恶意客户端或令牌被盗带来的风险。 | 2 |
| **10.4.10** | 验证机密客户端向授权服务器发送后通道请求时会经过客户端认证，例如令牌请求、推送授权请求（PAR）和令牌撤销请求。 | 2 |
| **10.4.11** | 验证授权服务器配置只向 OAuth 客户端分配所需的 scope。 | 2 |
| **10.4.12** | 验证授权服务器只允许每个客户端使用其实际需要的 `response_mode` 值。可以把该值与预期值进行比较，也可以通过推送授权请求（PAR）或 JWT 安全授权请求（JAR）加以限制。 | 3 |
| **10.4.13** | 验证使用 `code` 授权类型时，始终同时采用推送授权请求（PAR）。 | 3 |
| **10.4.14** | 验证授权服务器只签发发送方约束（持有证明）访问令牌，采用基于双向 TLS（mTLS）的证书绑定访问令牌，或采用 DPoP 绑定访问令牌。 | 3 |
| **10.4.15** | 验证对于运行在服务器而非最终用户设备上的 OAuth 客户端，授权服务器必须确认 `authorization_details` 参数由该服务器上的客户端程序提供，并且未被用户篡改。可以通过强制使用推送授权请求（PAR）或 JWT 安全授权请求（JAR）来满足此要求。 | 3 |
| **10.4.16** | 验证客户端属于机密客户端，并且授权服务器强制使用基于公钥密码学、能够抵抗重放攻击的强客户端认证方式，例如双向 TLS（`tls_client_auth`、`self_signed_tls_client_auth`）或私钥 JWT（`private_key_jwt`）。 | 3 |

## V10.5 OIDC 客户端

本节适用于接入 OIDC 登录的应用，也就是 OIDC 规范所称的“依赖方”（RP）。由于这类应用在 OAuth 流程中同时承担客户端角色，因此“OAuth 客户端”小节中的要求也适用于它。

注意，“认证”章节中的“使用身份提供方进行认证”小节也包含相关通用要求。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **10.5.1** | 验证接入 OIDC 登录的应用能够防范 ID Token 重放。例如，检查 ID Token 中的 `nonce` 是否与发送给 OpenID Provider 的认证请求中的 `nonce` 完全一致；在 OAuth 2.0 中，这类请求称为发送给授权服务器的授权请求。 | 2 |
| **10.5.2** | 验证客户端根据 ID Token 中不会被重新分配给其他用户的声明来唯一识别用户，通常使用相应身份提供方范围内的 `sub` 声明。 | 2 |
| **10.5.3** | 验证客户端能够阻止恶意授权服务器通过元数据冒充其他授权服务器。如果元数据中的签发方 URL 与客户端预先配置的预期 URL 不完全一致，客户端必须拒绝该元数据。 | 2 |
| **10.5.4** | 验证客户端检查 ID Token 的 `aud` 声明是否等于自身的 `client_id`，以确认该令牌确实以本客户端为受众。 | 2 |
| **10.5.5** | 验证使用 OIDC 后通道注销时，依赖方采取措施缓解注销流程中通过强制注销造成的拒绝服务和跨 JWT 混淆。客户端必须验证注销令牌的类型正确且值为 `logout+jwt`，包含成员名称正确的 `event` 声明，并且不包含 `nonce` 声明。此外，建议设置较短的有效期，例如 2 分钟。 | 2 |

## V10.6 OpenID Provider

由于 OpenID Provider 充当 OAuth 授权服务器，“OAuth 授权服务器”小节中的要求同样适用。

注意，如果使用 ID Token 流程（而不是授权码流程），不会签发访问令牌，许多 OAuth AS 要求并不适用。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **10.6.1** | 验证 OpenID Provider 只允许 response mode 使用 `code`、`ciba`、`id_token` 或 `id_token code`。应优先采用 `code`，而不是 `id_token code`（OIDC 混合流程）；不得使用 `token` 等任何隐式流程。 | 2 |
| **10.6.2** | 验证 OpenID Provider 采取措施缓解通过强制注销造成的拒绝服务，例如取得最终用户的明确确认，或者验证由依赖方发起的注销请求中提供的 `id_token_hint` 等参数（如有）。 | 2 |

## V10.7 同意管理

本节要求授权服务器正确取得并验证用户同意。否则，攻击者可能通过欺骗或社会工程手段，在用户不知情的情况下取得权限。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **10.7.1** | 验证授权服务器确保用户同意每一次授权请求。无法确认客户端身份时，必须每次都明确询问用户是否同意。 | 2 |
| **10.7.2** | 验证授权服务器征求同意时，向用户提供充分、清晰的信息，说明其同意的授权内容。适用时，应说明所请求权限的性质（通常由 scope、资源服务器和富授权请求（RAR）详情决定）、获得授权的应用身份，以及授权的有效期。 | 2 |
| **10.7.3** | 验证用户可以查看、修改和撤销自己通过授权服务器作出的授权同意。 | 2 |

## 参考资料

关于 OAuth 的更多信息，请参见：

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

ASVS 中 OAuth 相关要求使用了以下已发布和草案状态的 RFC：

* [RFC6749 The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
* [RFC6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)
* [RFC6819 OAuth 2.0 Threat Model and Security Considerations](https://datatracker.ietf.org/doc/html/rfc6819)
* [RFC7636 Proof Key for Code Exchange by OAuth Public Clients](https://datatracker.ietf.org/doc/html/rfc7636)
* [RFC7591 OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591)
* [RFC8628 OAuth 2.0 Device Authorization Grant](https://datatracker.ietf.org/doc/html/rfc8628)
* [RFC8707 Resource Indicators for OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc8707)
* [RFC9068 JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
* [RFC9126 OAuth 2.0 Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126)
* [RFC9207 OAuth 2.0 Authorization Server Issuer Identification](https://datatracker.ietf.org/doc/html/rfc9207)
* [RFC9396 OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)
* [RFC9449 OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)
* [RFC9700 Best Current Practice for OAuth 2.0 Security](https://datatracker.ietf.org/doc/html/rfc9700)
* [draft OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)<!-- recheck on release -->
* [draft The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12)<!-- recheck on release -->

关于 OpenID Connect 的更多信息，请参见：

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
