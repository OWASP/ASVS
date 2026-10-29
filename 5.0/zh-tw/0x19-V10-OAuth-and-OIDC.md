# V10 OAuth 和 OIDC

## 控制目標

OAuth 2.0（本章簡稱 OAuth）是用於委派授權的產業標準框架。使用者授權後，用戶端應用便可以代表使用者存取 API 等伺服器端資源。

OAuth 本身並不是使用者身分驗證協議。OpenID Connect（OIDC）在 OAuth 之上增加了身分層，提供標準化使用者資訊、單一登入（SSO）和工作階段管理等功能。由於 OIDC 建立在 OAuth 之上，本章針對 OAuth 的要求也適用於 OIDC。

OAuth 定義了以下角色：

* OAuth 用戶端是嘗試獲取伺服器資源存取權限的應用（例如使用已簽發的存取權杖呼叫 API）。OAuth 用戶端通常是伺服器端應用。
    * 機密用戶端能夠妥善保管用於向授權伺服器證明自身身分的身分驗證資訊。
    * 公共用戶端無法安全保管這類身分驗證資訊。因此，它不能使用 `client_id` 和 `client_secret` 等參數證明自身身分，只能通過 `client_id` 標明自己是哪一個用戶端。
* OAuth 資源伺服器（RS）是向 OAuth 用戶端暴露資源的伺服器 API。
* OAuth 授權伺服器（AS）是向 OAuth 用戶端簽發存取權杖的伺服器應用。這些存取權杖允許 OAuth 用戶端代表最終使用者，或代表 OAuth 用戶端自身，存取 RS 資源。AS 通常是獨立應用，但在合適情況下也可以整合到合適的 RS 中。
* 資源所有者（RO）是最終使用者，他們授權 OAuth 用戶端代表自己獲取對資源伺服器上托管資源的有限存取權限。資源所有者通過與授權伺服器互動來同意這種委派授權。

OIDC 定義了以下角色：

* 在 OIDC 中，接入 OIDC 登入並請求身分驗證服務確認使用者身分的應用稱為「依賴方」（Relying Party，RP）。它在 OAuth 流程中同時承擔用戶端角色。
* OpenID Provider（OP）是能夠身分驗證最終使用者並向 RP 提供 OIDC 聲明的 OAuth AS。OP 可以是身分提供方（IdP），但在聯合場景中，OP 和最終使用者進行身分驗證的身分提供方可能是不同的伺服器應用。

OAuth 和 OIDC 最初面向第三方應用設計，如今也經常用於第一方應用。但在第一方場景中把它們用於身分驗證和工作階段管理，會增加系統複雜度，並可能帶來新的安全問題。

OAuth 和 OIDC 可用於多種類型的應用，但 ASVS 以及本章要求的重點是 Web 應用和 API。

OAuth 和 OIDC 建立在 Web 技術之上，因此其他章節的通用要求始終適用。不能脫離整份標準，孤立地理解或驗證本章。

本章採用 OAuth 2.0 和 OIDC 當前的最佳實務，並與 <https://oauth.net/2/> 和 <https://openid.net/developers/specs/> 發佈的規範保持一致。相關 RFC 即使已經成熟，仍會持續更新，因此，實施本章要求時，與最新版本保持一致十分重要。更多資訊見參考資料。

鑒於該領域的複雜性，要建置安全的 OAuth 或 OIDC 解決方案，使用知名且符合產業標準的授權伺服器並採用推薦的安全組態至關重要。

本章使用的術語與 OAuth RFC 和 OIDC 規範一致，但請注意，OIDC 術語只用於 OIDC 特定要求；其他情況下使用 OAuth 術語。

在 OAuth 和 OIDC 語境中，本章中的「權杖」指：

* 存取權杖只能由資源伺服器（RS）使用。它可以是通過權杖內省進行驗證的引用權杖，也可以是使用相應金鑰材料進行驗證的自包含權杖。
* 刷新權杖只能由簽發該權杖的授權伺服器接收並使用。
* OIDC ID Token 只能由觸發相應授權流程的用戶端接收並使用。

本章部分要求的等級取決於用戶端屬於機密用戶端還是公共用戶端。強用戶端身分驗證能夠降低多種攻擊風險，因此 L1 應用使用機密用戶端時，可以適當放寬少數要求。

## V10.1 通用 OAuth 和 OIDC 安全

本節覆蓋適用於所有使用 OAuth 或 OIDC 的應用的通用架構要求。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **10.1.1** | 驗證權杖只發送給確實需要使用它的元件。例如，基於瀏覽器的 JavaScript 應用採用 BFF（Backend for Frontend）模式時，存取權杖和刷新權杖只能由後端存取。 | 2 |
| **10.1.2** | 驗證用戶端只接受由同一使用者代理工作階段發起的同一次授權流程所產生的授權伺服器傳回值，例如授權碼或 ID Token。為此，用戶端生成的 `code_verifier`、`state`、OIDC `nonce` 等秘密值必須不可猜測、僅用於該次授權流程，並與用戶端以及發起該流程的使用者代理工作階段安全綁定。 | 2 |

## V10.2 OAuth 用戶端

本節詳細說明 OAuth 用戶端應用需要承擔的安全責任。OAuth 用戶端可以實作為執行在伺服器端的 Web 後端（通常充當 BFF）、用於服務間整合的後端服務，或者執行在瀏覽器中的單頁應用（SPA，也稱基於瀏覽器的應用）。

一般而言，後端用戶端被視為機密用戶端，前端用戶端被視為公共用戶端。不過，執行在最終使用者裝置上的原生應用在使用 OAuth 動態用戶端註冊時，也可以被視為機密用戶端。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **10.2.1** | 驗證 OAuth 用戶端使用授權碼流程時，能夠防範由瀏覽器請求偽造（通常稱為 CSRF）觸發的權杖請求。可以使用授權碼交換證明金鑰（PKCE），也可以檢查授權請求中發送的 `state` 參數。 | 2 |
| **10.2.2** | 驗證 OAuth 用戶端需要與多個授權伺服器互動時，能夠防範授權伺服器混淆攻擊。例如，可以要求授權伺服器傳回 `iss` 參數，並在授權回應和權杖回應中檢查該參數。 | 2 |
| **10.2.3** | 驗證 OAuth 用戶端向授權伺服器發起請求時，只請求所需的 scope（或其他授權參數）。 | 3 |

## V10.3 OAuth 資源伺服器

在 ASVS 和本章語境中，資源伺服器是一個 API。為提供安全存取，資源伺服器必須：

* 根據權杖格式和相關協議規範驗證存取權杖。例如，可以在本地驗證 JWT，或者通過 OAuth 權杖內省端點向授權伺服器查詢權杖狀態和屬性。
* 如果權杖有效，則基於存取權杖中的資訊和已授予權限執行授權決策。例如，資源伺服器需要驗證用戶端（代表 RO 行事）是否被授權存取所請求的資源。

因此，以下 OAuth 和 OIDC 專用檢查應在確認權杖有效之後、根據權杖內容作出授權決定之前執行。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **10.3.1** | 驗證資源伺服器在接受存取權杖前，會確認該權杖的預期接收方（受眾）包含本資源伺服器。受眾資訊可以記錄在結構化存取權杖中，例如 JWT 的 `aud` 聲明；也可以通過權杖內省端點傳回的資訊確認。 | 2 |
| **10.3.2** | 驗證資源伺服器依據存取權杖中描述委派權限的聲明作出授權決定。權杖含有 `sub`、`scope`、`authorization_details` 等聲明時，必須把這些聲明納入決策。 | 2 |
| **10.3.3** | 驗證存取控制決策需要從存取權杖（JWT 或相關權杖內省回應）識別唯一使用者時，資源伺服器只採用不會被重新分配給其他使用者的聲明。通常應組合使用 `iss` 和 `sub`。 | 2 |
| **10.3.4** | 驗證資源伺服器對身分驗證強度、身分驗證方式或身分驗證時效性有特定要求時，會確認存取權杖滿足這些條件。例如，可以分別檢查 OIDC 的 `acr`、`amr` 和 `auth_time` 聲明（如有）。 | 2 |
| **10.3.5** | 驗證資源伺服器要求使用發送方約束存取權杖，防止被盜存取權杖被使用，或存取權杖被未授權方重放。可以採用 OAuth 2.0 雙向 TLS，或 OAuth 2.0 持有證明（DPoP）。 | 3 |

## V10.4 OAuth 授權伺服器

這些要求詳細說明 OAuth 授權伺服器的職責，包括 OpenID Provider。

用戶端身分驗證可以使用 `self_signed_tls_client_auth`，但必須滿足 [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705) [第 2.2 節](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut)規定的前提條件。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **10.4.1** | 驗證授權伺服器為每個用戶端維護預先註冊的重定向 URI 允許列表，並通過精確字串比較來檢查重定向 URI。 | 1 |
| **10.4.2** | 驗證授權伺服器在授權回應中傳回授權碼時，該授權碼只能用於一次權杖請求。當第二次有效請求使用已用於簽發存取權杖的授權碼時，授權伺服器必須拒絕該權杖請求，並撤銷與該授權碼相關的所有已簽發權杖。 | 1 |
| **10.4.3** | 驗證授權碼的有效期足夠短。L1 和 L2 應用最長為 10 分鐘，L3 應用最長為 1 分鐘。 | 1 |
| **10.4.4** | 驗證授權伺服器只為每個用戶端啟用其實際需要的授權類型。不得再使用 `token`（隱式流程）或 `password`（資源所有者密碼身分驗證資訊流程）授權。 | 1 |
| **10.4.5** | 驗證授權伺服器採取措施緩解針對公共用戶端的刷新權杖重放攻擊，優先使用發送方約束刷新權杖，即採用持有證明（DPoP）或使用雙向 TLS（mTLS）的憑證綁定存取權杖。L1 和 L2 應用可以使用刷新權杖輪替。採用輪替時，授權伺服器必須在刷新權杖使用後使其失效；如果收到已使用且已失效的刷新權杖，必須撤銷該授權對應的所有刷新權杖。 | 1 |
| **10.4.6** | 驗證在使用授權碼流程時，授權伺服器強制採用 PKCE（Proof Key for Code Exchange）機制，以防範授權碼截獲攻擊。授權伺服器必須要求授權請求包含有效的 `code_challenge`，且不得接受值為 `plain` 的 `code_challenge_method`；對於權杖請求，必須要求驗證 `code_verifier` 參數。 | 2 |
| **10.4.7** | 驗證授權伺服器允許未經身分驗證的動態用戶端註冊時，採取措施降低惡意用戶端風險。伺服器必須驗證已註冊 URI 等用戶端元資料，取得使用者同意，並在處理不可信用戶端的授權請求之前向使用者發出警告。 | 2 |
| **10.4.8** | 驗證刷新權杖設有絕對失效時間，即使同時採用滑動過期機制也不例外。 | 2 |
| **10.4.9** | 驗證已授權使用者可以通過授權伺服器的使用者界面撤銷刷新權杖和引用存取權杖，以降低惡意用戶端或權杖被盜帶來的風險。 | 2 |
| **10.4.10** | 驗證機密用戶端向授權伺服器發送後通道請求時會經過用戶端身分驗證，例如權杖請求、推送授權請求（PAR）和權杖撤銷請求。 | 2 |
| **10.4.11** | 驗證授權伺服器組態只向 OAuth 用戶端分配所需的 scope。 | 2 |
| **10.4.12** | 驗證授權伺服器只允許每個用戶端使用其實際需要的 `response_mode` 值。可以把該值與預期值進行比較，也可以通過推送授權請求（PAR）或 JWT 安全授權請求（JAR）加以限制。 | 3 |
| **10.4.13** | 驗證使用 `code` 授權類型時，始終同時採用推送授權請求（PAR）。 | 3 |
| **10.4.14** | 驗證授權伺服器只簽發發送方約束（持有證明）存取權杖，採用基於雙向 TLS（mTLS）的憑證綁定存取權杖，或採用 DPoP 綁定存取權杖。 | 3 |
| **10.4.15** | 驗證對於執行在伺服器而非最終使用者裝置上的 OAuth 用戶端，授權伺服器必須確認 `authorization_details` 參數由該伺服器上的用戶端程序提供，並且未被使用者篡改。可以通過強制使用推送授權請求（PAR）或 JWT 安全授權請求（JAR）來滿足此要求。 | 3 |
| **10.4.16** | 驗證用戶端屬於機密用戶端，並且授權伺服器強制使用基於公開金鑰密碼學、能夠抵抗重放攻擊的強用戶端身分驗證方式，例如雙向 TLS（`tls_client_auth`、`self_signed_tls_client_auth`）或私密金鑰 JWT（`private_key_jwt`）。 | 3 |

## V10.5 OIDC 用戶端

本節適用於接入 OIDC 登入的應用，也就是 OIDC 規範所稱的「依賴方」（RP）。由於這類應用在 OAuth 流程中同時承擔用戶端角色，因此「OAuth 用戶端」小節中的要求也適用於它。

注意，「身分驗證」章節中的「使用身分提供方進行身分驗證」小節也包含相關通用要求。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **10.5.1** | 驗證接入 OIDC 登入的應用能夠防範 ID Token 重放。例如，檢查 ID Token 中的 `nonce` 是否與發送給 OpenID Provider 的身分驗證請求中的 `nonce` 完全一致；在 OAuth 2.0 中，這類請求稱為發送給授權伺服器的授權請求。 | 2 |
| **10.5.2** | 驗證用戶端根據 ID Token 中不會被重新分配給其他使用者的聲明來唯一識別使用者，通常使用相應身分提供方範圍內的 `sub` 聲明。 | 2 |
| **10.5.3** | 驗證用戶端能夠阻止惡意授權伺服器通過元資料冒充其他授權伺服器。如果元資料中的簽發方 URL 與用戶端預先組態的預期 URL 不完全一致，用戶端必須拒絕該元資料。 | 2 |
| **10.5.4** | 驗證用戶端檢查 ID Token 的 `aud` 聲明是否等於自身的 `client_id`，以確認該權杖確實以本用戶端為受眾。 | 2 |
| **10.5.5** | 驗證使用 OIDC 後通道登出時，依賴方採取措施緩解登出流程中通過強制登出造成的拒絕服務和跨 JWT 混淆。用戶端必須驗證登出權杖的類型正確且值為 `logout+jwt`，包含成員名稱正確的 `event` 聲明，並且不包含 `nonce` 聲明。此外，建議設定較短的有效期，例如 2 分鐘。 | 2 |

## V10.6 OpenID Provider

由於 OpenID Provider 充當 OAuth 授權伺服器，「OAuth 授權伺服器」小節中的要求同樣適用。

注意，如果使用 ID Token 流程（而不是授權碼流程），不會簽發存取權杖，許多 OAuth AS 要求並不適用。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **10.6.1** | 驗證 OpenID Provider 只允許 response mode 使用 `code`、`ciba`、`id_token` 或 `id_token code`。應優先採用 `code`，而不是 `id_token code`（OIDC 混合流程）；不得使用 `token` 等任何隱式流程。 | 2 |
| **10.6.2** | 驗證 OpenID Provider 採取措施緩解通過強制登出造成的拒絕服務，例如取得最終使用者的明確確認，或者驗證由依賴方發起的登出請求中提供的 `id_token_hint` 等參數（如有）。 | 2 |

## V10.7 同意管理

本節要求授權伺服器正確取得並驗證使用者同意。否則，攻擊者可能通過欺騙或社會工程手段，在使用者不知情的情況下取得權限。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **10.7.1** | 驗證授權伺服器確保使用者同意每一次授權請求。無法確認用戶端身分時，必須每次都明確詢問使用者是否同意。 | 2 |
| **10.7.2** | 驗證授權伺服器徵求同意時，向使用者提供充分、清晰的資訊，說明其同意的授權內容。適用時，應說明所請求權限的性質（通常由 scope、資源伺服器和富授權請求（RAR）詳情決定）、獲得授權的應用身分，以及授權的有效期。 | 2 |
| **10.7.3** | 驗證使用者可以查看、修改和撤銷自己通過授權伺服器作出的授權同意。 | 2 |

## 參考資料

關於 OAuth 的更多資訊，請參見：

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

ASVS 中 OAuth 相關要求使用了以下已發佈和草案狀態的 RFC：

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

關於 OpenID Connect 的更多資訊，請參見：

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
