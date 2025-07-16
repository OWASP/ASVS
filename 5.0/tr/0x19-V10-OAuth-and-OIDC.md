# V10 OAuth ve OIDC

## Kontrol Amacı

OAuth2 (bu bölümde kısaca OAuth olarak anılacaktır), yetki devri için endüstri standardı bir çerçevedir. Örneğin, OAuth kullanılarak bir istemci uygulama, kullanıcı tarafından yetkilendirildiği sürece, o kullanıcı adına API’lere (sunucu kaynaklarına) erişim sağlayabilir.

OAuth tek başına kullanıcı kimlik doğrulaması amacıyla tasarlanmamıştır. OpenID Connect (OIDC) çerçevesi, OAuth üzerine bir kullanıcı kimliği katmanı ekleyerek bu eksikliği tamamlar. OIDC, standartlaştırılmış kullanıcı bilgileri, Single Sign-On (SSO) ve oturum yönetimi gibi özellikleri destekler. OIDC, OAuth'un bir uzantısı olduğundan, bu bölümdeki OAuth gereksinimleri aynı zamanda OIDC için de geçerlidir.

OAuth çerçevesinde aşağıdaki roller tanımlanır:

* OAuth istemcisi, sunucu kaynaklarına erişim sağlamaya çalışan uygulamadır (örneğin, verilen access token’ı kullanarak bir API çağrısı yapar). Genellikle bu, sunucu taraflı bir uygulamadır.
    * Gizli istemci (confidential client), authorization server ile kimlik doğrulama sırasında kullandığı kimlik bilgilerini gizli tutabilecek kapasitede olan istemcidir.
    * Genel istemci (public client), authorization server ile kimlik doğrulama sırasında kullandığı kimlik bilgilerini gizli tutamayacak durumdadır. Bu nedenle kendini yalnızca bir client_id ile tanıtır, client_id ve client_secret gibi bilgilerle kimlik doğrulaması yapmaz.
* OAuth kaynak sunucusu (resource server – RS), OAuth istemcilerine kaynakları sunan API’dir.
* OAuth yetkilendirme sunucusu (authorization server – AS), access token üreten sunucu uygulamasıdır. Bu token’lar sayesinde OAuth istemcisi, son kullanıcı adına veya kendi adına RS üzerindeki kaynaklara erişim sağlayabilir. AS genellikle ayrı bir uygulama olsa da, uygun görüldüğünde RS ile entegre olabilir.
* Kaynak sahibi (resource owner – RO), OAuth istemcilerinin kendi adına, kaynak sunucusu üzerinde kısıtlı erişim elde etmesine izin veren son kullanıcıdır. Yetkilendirme sürecine AS üzerinden katılım sağlar.

OIDC çerçevesinde aşağıdaki roller tanımlanır:

* Güvenen taraf (relying party – RP), son kullanıcının kimlik doğrulamasını OpenID Provider üzerinden gerçekleştirmek isteyen istemci uygulamadır. Aynı zamanda bir OAuth istemcisidir.
* OpenID Provider (OP), son kullanıcıyı kimlik doğrulama yeteneğine sahip olan ve RP'ye OIDC claim’lerini sağlayan bir OAuth yetkilendirme sunucusudur. OP çoğu zaman bir kimlik sağlayıcı (IdP) olur; ancak federasyon senaryolarında OP ve gerçek kimlik sağlayıcı farklı uygulamalar olabilir.

OAuth ve OIDC başlangıçta üçüncü taraf uygulamalar için tasarlanmıştı. Ancak günümüzde ilk taraf uygulamalar tarafından da yaygın şekilde kullanılmaktadır. Bu kullanım senaryolarında, özellikle kimlik doğrulama ve oturum yönetimi amacıyla kullanıldığında protokol belirli bir karmaşıklık ekler ve bu durum bazı yeni güvenlik riskleri yaratabilir.

OAuth ve OIDC birçok farklı uygulama tipiyle kullanılabilir; ancak ASVS ve bu bölümdeki gereksinimler özellikle web uygulamaları ve API’ler için tasarlanmıştır.

OAuth ve OIDC, web teknolojilerinin üzerine kurulu mantıksal protokoller olduklarından, bu bölümdeki gereksinimler diğer bölümlerden bağımsız değerlendirilemez; genel güvenlik gereksinimleri geçerliliğini korur.

Bu bölüm, <https://oauth.net/2/> ve <https://openid.net/developers/specs/> üzerindeki spesifikasyonlarla uyumlu şekilde OAuth2 ve OIDC için güncel en iyi uygulamaları ele alır. RFC’ler olgun belgeler olarak görülse de, sık sık güncellenmektedir. Bu nedenle uygulamada, ilgili gereksinimlerin en güncel versiyonlarla uyumlu şekilde ele alınması önemlidir. Ayrıntılar için bölümün referans kısmına bakınız.

Bu alanın karmaşıklığı göz önünde bulundurulduğunda, güvenli bir OAuth veya OIDC çözümünün, tanınmış ve endüstri standardı yetkilendirme sunucularını kullanması ve önerilen güvenlik yapılandırmalarını uygulaması son derece önemlidir.

Bu bölümde kullanılan terimler, OAuth ve OIDC spesifikasyonlarındaki tanımlarla uyumludur. Ancak OIDC’ye özel gereksinimler dışında, genellikle OAuth terminolojisi tercih edilmiştir.

Bu bölümde geçen "token" terimi, aşağıdaki anlamlarda kullanılmıştır:

* Access token'ları sadece RS tarafından kullanılır. Bunlar ya introspection ile doğrulanan bir reference token olabilir ya da belirli bir anahtar malzemesiyle doğrulanan bir self-contained token olabilir.
* Refresh token'ları, yalnızca onu üreten authorization server tarafından kullanılabilir.
* OIDC ID Token'ları sadece authorization flow’u tetikleyen istemci tarafından kullanılabilir.

Bu bölümdeki bazı gereksinimlerin risk seviyesi, istemcinin gizli istemci mi yoksa açık istemci mi olduğuna göre değişiklik gösterebilir. Güçlü istemci kimlik doğrulaması, birçok saldırı vektörünü etkisiz hale getirebildiği için, L1 uygulamalarında bazı gereksinimler gizli istemci kullanıldığında esnetilebilir.


## V10.1 Generic OAuth and OIDC Security

Bu bölüm, OAuth veya OIDC kullanan tüm uygulamalara uygulanabilen genel mimari gereksinimleri kapsar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **10.1.1** | 	Token'ların yalnızca kesinlikle ihtiyaç duyan bileşenlere gönderildiği doğrulanmalıdır. Örneğin, tarayıcı tabanlı JavaScript uygulamaları için bir backend-for-frontend modeli kullanıldığında, access ve refresh token'lara yalnızca backend'in erişebilmesi gerekir. | 2 |
| **10.1.2** | Authorization server'dan gelen değerler (örneğin authorization code veya ID Token gibi) yalnızca aynı user agent oturumu ve işlemi tarafından başlatılmış bir yetkilendirme akışının sonucuysa kabul edildiği doğrulanmalıdır. Bu, client tarafından oluşturulan secret’ların 'proof key for code exchange' (PKCE) ‘code_verifier’, ‘state’ veya OIDC ‘nonce’ gibi tahmin edilemez, işleme özgü ve hem client’a hem de işlem başlatılan user agent oturumuna güvenli bir şekilde bağlı olmasını gerektirir. | 2 |

## V10.2 OAuth İstemcisi

Bu gereksinimler, OAuth istemci uygulamaları için sorumlulukları detaylandırır. Client örneğin bir web sunucusu backend’i (genellikle Backend For Frontend olarak hareket eden), bir backend servis entegrasyonu veya bir frontend Single Page Application (SPA, yani tarayıcı tabanlı uygulama) olabilir.

Genel olarak backend istemciler gizli istemci olarak, frontend istemciler ise açık istemci olarak değerlendirilir. Ancak, son kullanıcı cihazında çalışan native uygulamalar, 'OAuth dynamic client registration' kullanıldığında gizli olarak kabul edilebilir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **10.2.1** | Code flow kullanılıyorsa, OAuth client’ın token taleplerini tetikleyen CSRF saldırılarına karşı korumaya sahip olduğu doğrulanmalıdır. Bu genellikle PKCE kullanılarak veya authorization isteğinde gönderilen ‘state’ parametresinin kontrolü ile sağlanır. | 2 |
| **10.2.2** | OAuth istemcisi birden fazla AS ile etkileşime girebiliyorsa, mix-up saldırılarına karşı korumaya sahip olduğu doğrulanmalıdır. Örneğin, authorization server’ın 'iss' parametresini döndürmesi zorunlu kılınabilir ve bu parametrenin hem authorization yanıtında hem de token yanıtında doğrulanması gerekir. | 2 |
| **10.2.3** | OAuth istemcisinin authorization server’a yaptığı taleplerde yalnızca gerekli scope’ları (veya diğer yetkilendirme parametrelerini) talep ettiği doğrulanmalıdır. | 3 |

## V10.3 OAuth Resource Server

ASVS ve bu bölüm bağlamında resource server (RS) bir API’dir. Güvenli erişim sağlamak için RS şunları yapmalıdır:

* Access token’ı, token formatı ve ilgili protokol spesifikasyonlarına göre doğrulamalıdır; örneğin JWT doğrulaması veya OAuth token introspection.
* Geçerliyse, access token’dan alınan bilgiler ve verilmiş izinlere göre yetkilendirme kararları uygulamalıdır. Örneğin, resource server’ın client’ın (RO adına hareket eden) istenen kaynağa erişme yetkisine sahip olduğunu doğrulaması gerekir.

Bu nedenle burada listelenen gereksinimler, OAuth veya OIDC’ye özeldir ve token doğrulaması yapıldıktan sonra, token içeriğine dayalı yetkilendirme gerçekleştirilmeden önce uygulanmalıdır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **10.3.1** | RS'nin yalnızca bu servisle kullanılmak üzere tasarlanmış access token’ları kabul ettiği doğrulanmalıdır (audience kontrolü). Audience bilgisi yapılandırılmış token’larda (örneğin JWT içindeki ‘aud’ claim’i) yer alabilir veya token introspection endpoint aracılığıyla kontrol edilebilir. | 2 |
| **10.3.2** | Verify that the resource server enforces authorization decisions based on claims from the access token that define delegated authorization. If claims such as 'sub', 'scope', and 'authorization_details' are present, they must be part of the decision. | 2 |
| **10.3.3** | Verify that if an access control decision requires identifying a unique user from an access token (JWT or related token introspection response), the resource server identifies the user from claims that cannot be reassigned to other users. Typically, it means using a combination of 'iss' and 'sub' claims. | 2 |
| **10.3.4** | Verify that, if the resource server requires specific authentication strength, methods, or recentness, it verifies that the presented access token satisfies these constraints. For example, if present, using the OIDC 'acr', 'amr' and 'auth_time' claims respectively. | 2 |
| **10.3.5** | Verify that the resource server prevents the use of stolen access tokens or replay of access tokens (from unauthorized parties) by requiring sender-constrained access tokens, either Mutual TLS for OAuth 2 or OAuth 2 Demonstration of Proof of Possession (DPoP). | 3 |

## V10.4 OAuth Authorization Server

These requirements detail the responsibilities for OAuth authorization servers, including OpenID Providers.

For client authentication, the 'self_signed_tls_client_auth' method is allowed with the prerequisites required by [section 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) of [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705).

| # | Description | Level |
| :---: | :--- | :---: |
| **10.4.1** | Verify that the authorization server validates redirect URIs based on a client-specific allowlist of pre-registered URIs using exact string comparison. | 1 |
| **10.4.2** | Verify that, if the authorization server returns the authorization code in the authorization response, it can be used only once for a token request. For the second valid request with an authorization code that has already been used to issue an access token, the authorization server must reject a token request and revoke any issued tokens related to the authorization code. | 1 |
| **10.4.3** | Verify that the authorization code is short-lived. The maximum lifetime can be up to 10 minutes for L1 and L2 applications and up to 1 minute for L3 applications. | 1 |
| **10.4.4** | Verify that for a given client, the authorization server only allows the usage of grants that this client needs to use. Note that the grants 'token' (Implicit flow) and 'password' (Resource Owner Password Credentials flow) must no longer be used. | 1 |
| **10.4.5** | Verify that the authorization server mitigates refresh token replay attacks for public clients, preferably using sender-constrained refresh tokens, i.e., Demonstrating Proof of Possession (DPoP) or Certificate-Bound Access Tokens using mutual TLS (mTLS). For L1 and L2 applications, refresh token rotation may be used. If refresh token rotation is used, the authorization server must invalidate the refresh token after usage, and revoke all refresh tokens for that authorization if an already used and invalidated refresh token is provided. | 1 |
| **10.4.6** | Verify that, if the code grant is used, the authorization server mitigates authorization code interception attacks by requiring proof key for code exchange (PKCE). For authorization requests, the authorization server must require a valid 'code_challenge' value and must not accept a 'code_challenge_method' value of 'plain'. For a token request, it must require validation of the 'code_verifier' parameter. | 2 |
| **10.4.7** | Verify that if the authorization server supports unauthenticated dynamic client registration, it mitigates the risk of malicious client applications. It must validate client metadata such as any registered URIs, ensure the user's consent, and warn the user before processing an authorization request with an untrusted client application. | 2 |
| **10.4.8** | Verify that refresh tokens have an absolute expiration, including if sliding refresh token expiration is applied. | 2 |
| **10.4.9** | Verify that refresh tokens and reference access tokens can be revoked by an authorized user using the authorization server user interface, to mitigate the risk of malicious clients or stolen tokens. | 2 |
| **10.4.10** | Verify that confidential client is authenticated for client-to-authorized server backchannel requests such as token requests, pushed authorization requests (PAR), and token revocation requests. | 2 |
| **10.4.11** | Verify that the authorization server configuration only assigns the required scopes to the OAuth client. | 2 |
| **10.4.12** | Verify that for a given client, the authorization server only allows the 'response_mode' value that this client needs to use. For example, by having the authorization server validate this value against the expected values or by using pushed authorization request (PAR) or JWT-secured Authorization Request (JAR). | 3 |
| **10.4.13** | Verify that grant type 'code' is always used together with pushed authorization requests (PAR). | 3 |
| **10.4.14** | Verify that the authorization server issues only sender-constrained (Proof-of-Possession) access tokens, either with certificate-bound access tokens using mutual TLS (mTLS) or DPoP-bound access tokens (Demonstration of Proof of Possession). | 3 |
| **10.4.15** | Verify that, for a server-side client (which is not executed on the end-user device), the authorization server ensures that the 'authorization_details' parameter value is from the client backend and that the user has not tampered with it. For example, by requiring the usage of pushed authorization request (PAR) or JWT-secured Authorization Request (JAR). | 3 |
| **10.4.16** | Verify that the client is confidential and the authorization server requires the use of strong client authentication methods (based on public-key cryptography and resistant to replay attacks), such as mutual TLS ('tls_client_auth', 'self_signed_tls_client_auth') or private key JWT ('private_key_jwt'). | 3 |

## V10.5 OIDC Client

As the OIDC relying party acts as an OAuth client, the requirements from the section "OAuth Client" apply as well.

Note that the "Authentication with an Identity Provider" section in the "Authentication" chapter also contains relevant general requirements.

| # | Description | Level |
| :---: | :--- | :---: |
| **10.5.1** | Verify that the client (as the relying party) mitigates ID Token replay attacks. For example, by ensuring that the 'nonce' claim in the ID Token matches the 'nonce' value sent in the authentication request to the OpenID Provider (in OAuth2 refereed to as the authorization request sent to the authorization server). | 2 |
| **10.5.2** | Verify that the client uniquely identifies the user from ID Token claims, usually the 'sub' claim, which cannot be reassigned to other users (for the scope of an identity provider). | 2 |
| **10.5.3** | Verify that the client rejects attempts by a malicious authorization server to impersonate another authorization server through authorization server metadata. The client must reject authorization server metadata if the issuer URL in the authorization server metadata does not exactly match the pre-configured issuer URL expected by the client. | 2 |
| **10.5.4** | Verify that the client validates that the ID Token is intended to be used for that client (audience) by checking that the 'aud' claim from the token is equal to the 'client_id' value for the client. | 2 |
| **10.5.5** | Verify that, when using OIDC back-channel logout, the relying party mitigates denial of service through forced logout and cross-JWT confusion in the logout flow. The client must verify that the logout token is correctly typed with a value of 'logout+jwt', contains the 'event' claim with the correct member name, and does not contain a 'nonce' claim. Note that it is also recommended to have a short expiration (e.g., 2 minutes). | 2 |

## V10.6 OpenID Provider

As OpenID Providers act as OAuth authorization servers, the requirements from the section "OAuth Authorization Server" apply as well.

Note that if using the ID Token flow (not the code flow), no access tokens are issued, and many of the requirements for OAuth AS are not applicable.

| # | Description | Level |
| :---: | :--- | :---: |
| **10.6.1** | Verify that the OpenID Provider only allows values 'code', 'ciba', 'id_token', or 'id_token code' for response mode. Note that 'code' is preferred over 'id_token code' (the OIDC Hybrid flow), and 'token' (any Implicit flow) must not be used. | 2 |
| **10.6.2** | Verify that the OpenID Provider mitigates denial of service through forced logout. By obtaining explicit confirmation from the end-user or, if present, validating parameters in the logout request (initiated by the relying party), such as the 'id_token_hint'. | 2 |

## V10.7 Consent Management

These requirements cover the verification of the user's consent by the authorization server. Without proper user consent verification, a malicious actor may obtain permissions on the user's behalf through spoofing or social-engineering.

| # | Description | Level |
| :---: | :--- | :---: |
| **10.7.1** | Verify that the authorization server ensures that the user consents to each authorization request. If the identity of the client cannot be assured, the authorization server must always explicitly prompt the user for consent. | 2 |
| **10.7.2** | Verify that when the authorization server prompts for user consent, it presents sufficient and clear information about what is being consented to. When applicable, this should include the nature of the requested authorizations (typically based on scope, resource server, Rich Authorization Requests (RAR) authorization details), the identity of the authorized application, and the lifetime of these authorizations. | 2 |
| **10.7.3** | Verify that the user can review, modify, and revoke consents which the user has granted through the authorization server. | 2 |

## References

For more information on OAuth, please see:

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

For OAuth-related requirements in ASVS following published and in draft status RFC-s are used:

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

For more information on OpenID Connect, please see:

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
