<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x19-V10-OAuth-and-OIDC.md -->
<!-- Translator: GeeksikhSecurity -->

# V10 OAuth and OIDC
# V10 OAuth ਅਤੇ OIDC

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

OAuth2 (referred to as OAuth in this chapter) is an industry-standard framework for delegated authorization. For example, using OAuth, a client application can obtain access to APIs (server resources) on a user's behalf, provided the user has authorized the client application to do so.

OAuth2 (ਇਸ ਅਧਿਆਇ ਵਿੱਚ OAuth ਕਿਹਾ ਗਿਆ ਹੈ) ਸੌਂਪੇ ਗਏ ਅਧਿਕਾਰੀਕਰਨ (delegated authorization) ਲਈ ਇੱਕ ਉਦਯੋਗ-ਮਿਆਰੀ ਫ੍ਰੇਮਵਰਕ ਹੈ। ਉਦਾਹਰਨ ਲਈ, OAuth ਦੀ ਵਰਤੋਂ ਕਰਕੇ, ਇੱਕ client ਐਪਲੀਕੇਸ਼ਨ ਉਪਭੋਗਤਾ ਦੀ ਤਰਫ਼ੋਂ API (ਸਰਵਰ ਸਰੋਤਾਂ) ਤੱਕ ਪਹੁੰਚ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੀ ਹੈ, ਬਸ਼ਰਤੇ ਕਿ ਉਪਭੋਗਤਾ ਨੇ client ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਅਜਿਹਾ ਕਰਨ ਲਈ ਅਧਿਕਾਰਤ ਕੀਤਾ ਹੋਵੇ।

By itself, OAuth is not designed for user authentication. The OpenID Connect (OIDC) framework extends OAuth by adding a user identity layer on top of OAuth. OIDC provides support for features including standardized user information, Single Sign-On (SSO), and session management. As OIDC is an extension of OAuth, the OAuth requirements in this chapter also apply to OIDC.

ਆਪਣੇ ਆਪ ਵਿੱਚ, OAuth ਉਪਭੋਗਤਾ ਪ੍ਰਮਾਣੀਕਰਨ (authentication) ਲਈ ਡਿਜ਼ਾਈਨ ਨਹੀਂ ਕੀਤਾ ਗਿਆ। OpenID Connect (OIDC) ਫ੍ਰੇਮਵਰਕ OAuth ਦੇ ਉੱਪਰ ਇੱਕ ਉਪਭੋਗਤਾ ਪਛਾਣ ਪਰਤ ਜੋੜ ਕੇ OAuth ਦਾ ਵਿਸਤਾਰ ਕਰਦਾ ਹੈ। OIDC ਮਿਆਰੀਕ੍ਰਿਤ ਉਪਭੋਗਤਾ ਜਾਣਕਾਰੀ, ਸਿੰਗਲ ਸਾਈਨ-ਔਨ (Single Sign-On, SSO), ਅਤੇ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਸਮੇਤ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਲਈ ਸਮਰਥਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਕਿਉਂਕਿ OIDC OAuth ਦਾ ਇੱਕ ਵਿਸਤਾਰ ਹੈ, ਇਸ ਅਧਿਆਇ ਦੀਆਂ OAuth ਲੋੜਾਂ OIDC 'ਤੇ ਵੀ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ।

The following roles are defined in OAuth:

OAuth ਵਿੱਚ ਹੇਠ ਲਿਖੀਆਂ ਭੂਮਿਕਾਵਾਂ ਪਰਿਭਾਸ਼ਿਤ ਹਨ:

* The OAuth client is the application that attempts to obtain access to server resources (e.g., by calling an API using the issued access token). The OAuth client is often a server-side application.
    * A confidential client is a client capable of maintaining the confidentiality of the credentials it uses to authenticate itself with the authorization server.
    * A public client is not capable of maintaining the confidentiality of credentials for authenticating with the authorization server. Therefore, instead of authenticating itself (e.g., using 'client_id' and 'client_secret' parameters), it only identifies itself (using a 'client_id' parameter).
* The OAuth resource server (RS) is the server API exposing resources to OAuth clients.
* The OAuth authorization server (AS) is a server application that issues access tokens to OAuth clients. These access tokens allow OAuth clients to access RS resources, either on behalf of an end-user or on the OAuth client's own behalf. The AS is often a separate application, but (if appropriate) it may be integrated into a suitable RS.
* The resource owner (RO) is the end-user who authorizes OAuth clients to obtain limited access to resources hosted on the resource server on their behalf. The resource owner consents to this delegated authorization by interacting with the authorization server.

* OAuth client ਉਹ ਐਪਲੀਕੇਸ਼ਨ ਹੈ ਜੋ ਸਰਵਰ ਸਰੋਤਾਂ ਤੱਕ ਪਹੁੰਚ ਪ੍ਰਾਪਤ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੀ ਹੈ (ਜਿਵੇਂ, ਜਾਰੀ ਕੀਤੇ access token (ਪਹੁੰਚ ਟੋਕਨ) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਿਸੇ API ਨੂੰ ਕਾਲ ਕਰਕੇ)। OAuth client ਅਕਸਰ ਇੱਕ ਸਰਵਰ-ਸਾਈਡ ਐਪਲੀਕੇਸ਼ਨ ਹੁੰਦੀ ਹੈ।
    * ਇੱਕ confidential client (ਗੁਪਤ client) ਉਹ client ਹੈ ਜੋ ਉਹਨਾਂ ਪ੍ਰਮਾਣ-ਪੱਤਰਾਂ ਦੀ ਗੁਪਤਤਾ ਕਾਇਮ ਰੱਖਣ ਦੇ ਸਮਰੱਥ ਹੈ ਜਿਨ੍ਹਾਂ ਦੀ ਵਰਤੋਂ ਉਹ authorization server (ਅਧਿਕਾਰੀਕਰਨ ਸਰਵਰ) ਨਾਲ ਆਪਣਾ ਪ੍ਰਮਾਣੀਕਰਨ ਕਰਨ ਲਈ ਕਰਦਾ ਹੈ।
    * ਇੱਕ public client (ਜਨਤਕ client) authorization server ਨਾਲ ਪ੍ਰਮਾਣੀਕਰਨ ਲਈ ਪ੍ਰਮਾਣ-ਪੱਤਰਾਂ ਦੀ ਗੁਪਤਤਾ ਕਾਇਮ ਰੱਖਣ ਦੇ ਸਮਰੱਥ ਨਹੀਂ ਹੁੰਦਾ। ਇਸ ਲਈ, ਆਪਣਾ ਪ੍ਰਮਾਣੀਕਰਨ ਕਰਨ ਦੀ ਬਜਾਏ (ਜਿਵੇਂ, 'client_id' ਅਤੇ 'client_secret' ਪੈਰਾਮੀਟਰਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ), ਇਹ ਸਿਰਫ਼ ਆਪਣੀ ਪਛਾਣ ਦੱਸਦਾ ਹੈ ('client_id' ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ)।
* OAuth resource server (RS — ਸਰੋਤ ਸਰਵਰ) ਉਹ ਸਰਵਰ API ਹੈ ਜੋ OAuth clients ਨੂੰ ਸਰੋਤ ਉਜਾਗਰ ਕਰਦਾ ਹੈ।
* OAuth authorization server (AS — ਅਧਿਕਾਰੀਕਰਨ ਸਰਵਰ) ਇੱਕ ਸਰਵਰ ਐਪਲੀਕੇਸ਼ਨ ਹੈ ਜੋ OAuth clients ਨੂੰ access tokens ਜਾਰੀ ਕਰਦੀ ਹੈ। ਇਹ access tokens OAuth clients ਨੂੰ RS ਸਰੋਤਾਂ ਤੱਕ ਪਹੁੰਚ ਦੀ ਇਜਾਜ਼ਤ ਦਿੰਦੇ ਹਨ, ਜਾਂ ਤਾਂ ਕਿਸੇ ਅੰਤਮ-ਉਪਭੋਗਤਾ ਦੀ ਤਰਫ਼ੋਂ ਜਾਂ OAuth client ਦੀ ਆਪਣੀ ਤਰਫ਼ੋਂ। AS ਅਕਸਰ ਇੱਕ ਵੱਖਰੀ ਐਪਲੀਕੇਸ਼ਨ ਹੁੰਦਾ ਹੈ, ਪਰ (ਜੇ ਢੁਕਵਾਂ ਹੋਵੇ) ਇਸ ਨੂੰ ਕਿਸੇ ਢੁਕਵੇਂ RS ਵਿੱਚ ਏਕੀਕ੍ਰਿਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।
* resource owner (RO — ਸਰੋਤ ਮਾਲਕ) ਉਹ ਅੰਤਮ-ਉਪਭੋਗਤਾ ਹੈ ਜੋ OAuth clients ਨੂੰ ਆਪਣੀ ਤਰਫ਼ੋਂ resource server 'ਤੇ ਹੋਸਟ ਕੀਤੇ ਸਰੋਤਾਂ ਤੱਕ ਸੀਮਤ ਪਹੁੰਚ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਅਧਿਕਾਰਤ ਕਰਦਾ ਹੈ। resource owner authorization server ਨਾਲ ਅੰਤਰਕਿਰਿਆ ਕਰਕੇ ਇਸ ਸੌਂਪੇ ਗਏ ਅਧਿਕਾਰੀਕਰਨ ਲਈ ਸਹਿਮਤੀ (consent) ਦਿੰਦਾ ਹੈ।

The following roles are defined in OIDC:

OIDC ਵਿੱਚ ਹੇਠ ਲਿਖੀਆਂ ਭੂਮਿਕਾਵਾਂ ਪਰਿਭਾਸ਼ਿਤ ਹਨ:

* The relying party (RP) is the client application requesting end-user authentication through the OpenID Provider. It assumes the role of an OAuth client.
* The OpenID Provider (OP) is an OAuth AS that is capable of authenticating the end-user and provides OIDC claims to an RP. The OP may be the identity provider (IdP), but in federated scenarios, the OP and the identity provider (where the end-user authenticates) may be different server applications.

* ਨਿਰਭਰ ਧਿਰ (relying party, RP) ਉਹ client ਐਪਲੀਕੇਸ਼ਨ ਹੈ ਜੋ OpenID Provider ਰਾਹੀਂ ਅੰਤਮ-ਉਪਭੋਗਤਾ ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਬੇਨਤੀ ਕਰਦੀ ਹੈ। ਇਹ ਇੱਕ OAuth client ਦੀ ਭੂਮਿਕਾ ਨਿਭਾਉਂਦੀ ਹੈ।
* OpenID Provider (OP — OpenID ਪ੍ਰਦਾਤਾ) ਇੱਕ ਅਜਿਹਾ OAuth AS ਹੈ ਜੋ ਅੰਤਮ-ਉਪਭੋਗਤਾ ਦਾ ਪ੍ਰਮਾਣੀਕਰਨ ਕਰਨ ਦੇ ਸਮਰੱਥ ਹੈ ਅਤੇ ਕਿਸੇ RP ਨੂੰ OIDC ਦਾਅਵੇ (claims) ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। OP ਪਛਾਣ ਪ੍ਰਦਾਤਾ (identity provider, IdP) ਹੋ ਸਕਦਾ ਹੈ, ਪਰ ਸੰਘੀ (federated) ਦ੍ਰਿਸ਼ਾਂ ਵਿੱਚ, OP ਅਤੇ ਪਛਾਣ ਪ੍ਰਦਾਤਾ (ਜਿੱਥੇ ਅੰਤਮ-ਉਪਭੋਗਤਾ ਪ੍ਰਮਾਣੀਕਰਨ ਕਰਦਾ ਹੈ) ਵੱਖ-ਵੱਖ ਸਰਵਰ ਐਪਲੀਕੇਸ਼ਨਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ।

OAuth and OIDC were initially designed for third-party applications. Today, they are often used by first-party applications as well. However, when used in first-party scenarios, such as authentication and session management, the protocol adds some complexity, which may introduce new security challenges.

OAuth ਅਤੇ OIDC ਨੂੰ ਸ਼ੁਰੂ ਵਿੱਚ ਤੀਜੀ-ਧਿਰ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਸੀ। ਅੱਜ, ਇਹ ਅਕਸਰ ਪਹਿਲੀ-ਧਿਰ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੁਆਰਾ ਵੀ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਹਾਲਾਂਕਿ, ਜਦੋਂ ਪਹਿਲੀ-ਧਿਰ ਦ੍ਰਿਸ਼ਾਂ ਵਿੱਚ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਪ੍ਰਮਾਣੀਕਰਨ ਅਤੇ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ, ਤਾਂ ਪ੍ਰੋਟੋਕਾਲ ਕੁਝ ਜਟਿਲਤਾ ਜੋੜਦਾ ਹੈ, ਜੋ ਨਵੀਆਂ ਸੁਰੱਖਿਆ ਚੁਣੌਤੀਆਂ ਪੈਦਾ ਕਰ ਸਕਦੀ ਹੈ।

OAuth and OIDC can be used for many types of applications, but the focus for ASVS and the requirements in this chapter is on web applications and APIs.

OAuth ਅਤੇ OIDC ਕਈ ਕਿਸਮਾਂ ਦੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ, ਪਰ ASVS ਅਤੇ ਇਸ ਅਧਿਆਇ ਦੀਆਂ ਲੋੜਾਂ ਦਾ ਕੇਂਦਰ-ਬਿੰਦੂ ਵੈੱਬ ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਤੇ API ਹਨ।

Since OAuth and OIDC can be considered logic on top of web technologies, general requirements from other chapters always apply, and this chapter cannot be taken out of context.

ਕਿਉਂਕਿ OAuth ਅਤੇ OIDC ਨੂੰ ਵੈੱਬ ਤਕਨਾਲੋਜੀਆਂ ਦੇ ਉੱਪਰ ਤਰਕ ਮੰਨਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਦੂਜੇ ਅਧਿਆਵਾਂ ਦੀਆਂ ਆਮ ਲੋੜਾਂ ਹਮੇਸ਼ਾ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ, ਅਤੇ ਇਸ ਅਧਿਆਇ ਨੂੰ ਸੰਦਰਭ ਤੋਂ ਬਾਹਰ ਨਹੀਂ ਲਿਆ ਜਾ ਸਕਦਾ।

This chapter addresses best current practices for OAuth2 and OIDC aligned with specifications found at <https://oauth.net/2/> and <https://openid.net/developers/specs/>. Even if RFCs are considered mature, they are updated frequently. Thus, it is important to align with the latest versions when applying the requirements in this chapter. See the references section for more details.

ਇਹ ਅਧਿਆਇ OAuth2 ਅਤੇ OIDC ਲਈ ਸਭ ਤੋਂ ਚੰਗੇ ਮੌਜੂਦਾ ਅਮਲਾਂ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਦਾ ਹੈ, ਜੋ <https://oauth.net/2/> ਅਤੇ <https://openid.net/developers/specs/> 'ਤੇ ਮਿਲਣ ਵਾਲੀਆਂ ਸਪੈਸੀਫ਼ਿਕੇਸ਼ਨਾਂ (specifications) ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ। ਭਾਵੇਂ RFC ਨੂੰ ਪਰਿਪੱਕ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ, ਉਹ ਅਕਸਰ ਅੱਪਡੇਟ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। ਇਸ ਲਈ, ਇਸ ਅਧਿਆਇ ਦੀਆਂ ਲੋੜਾਂ ਲਾਗੂ ਕਰਦੇ ਸਮੇਂ ਨਵੀਨਤਮ ਸੰਸਕਰਣਾਂ ਨਾਲ ਮੇਲ ਰੱਖਣਾ ਮਹੱਤਵਪੂਰਨ ਹੈ। ਹੋਰ ਵੇਰਵਿਆਂ ਲਈ ਹਵਾਲੇ ਭਾਗ ਵੇਖੋ।

Given the complexity of the area, it is vitally important for a secure OAuth or OIDC solution to use well-known industry-standard authorization servers and apply the recommended security configuration.

ਇਸ ਖੇਤਰ ਦੀ ਜਟਿਲਤਾ ਨੂੰ ਦੇਖਦਿਆਂ, ਇੱਕ ਸੁਰੱਖਿਅਤ OAuth ਜਾਂ OIDC ਹੱਲ ਲਈ ਇਹ ਬੇਹੱਦ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਪ੍ਰਸਿੱਧ ਉਦਯੋਗ-ਮਿਆਰੀ authorization servers ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਵੇ ਅਤੇ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਸੁਰੱਖਿਆ ਸੰਰਚਨਾ ਲਾਗੂ ਕੀਤੀ ਜਾਵੇ।

Terminology used in this chapter aligns with OAuth RFCs and OIDC specifications, but note that OIDC terminology is only used for OIDC-specific requirements; otherwise, OAuth terminology is used.

ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਵਰਤੀ ਗਈ ਸ਼ਬਦਾਵਲੀ OAuth RFC ਅਤੇ OIDC ਸਪੈਸੀਫ਼ਿਕੇਸ਼ਨਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦੀ ਹੈ, ਪਰ ਧਿਆਨ ਦਿਓ ਕਿ OIDC ਸ਼ਬਦਾਵਲੀ ਸਿਰਫ਼ OIDC-ਵਿਸ਼ੇਸ਼ ਲੋੜਾਂ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ; ਨਹੀਂ ਤਾਂ, OAuth ਸ਼ਬਦਾਵਲੀ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।

In the context of OAuth and OIDC, the term "token" in this chapter refers to:

OAuth ਅਤੇ OIDC ਦੇ ਸੰਦਰਭ ਵਿੱਚ, ਇਸ ਅਧਿਆਇ ਵਿੱਚ "ਟੋਕਨ" (token) ਸ਼ਬਦ ਦਾ ਮਤਲਬ ਹੈ:

* Access tokens, which shall only be consumed by the RS and can either be reference tokens that are validated using introspection or self-contained tokens that are validated using some key material.
* Refresh tokens, which shall only be consumed by the authorization server that issued the token.
* OIDC ID Tokens, which shall only be consumed by the client that triggered the authorization flow.

* Access tokens, ਜੋ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਸਿਰਫ਼ RS ਦੁਆਰਾ ਹੀ ਖਪਤ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ ਅਤੇ ਜੋ ਜਾਂ ਤਾਂ ਹਵਾਲਾ ਟੋਕਨ (reference tokens) ਹੋ ਸਕਦੇ ਹਨ ਜੋ introspection ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰਮਾਣਿਤ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਜਾਂ ਸਵੈ-ਨਿਰਭਰ ਟੋਕਨ (self-contained tokens) ਜੋ ਕਿਸੇ key material ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰਮਾਣਿਤ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
* Refresh tokens (ਨਵਿਆਉਣ ਟੋਕਨ), ਜੋ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਸਿਰਫ਼ ਉਸ authorization server ਦੁਆਰਾ ਹੀ ਖਪਤ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ ਜਿਸ ਨੇ ਟੋਕਨ ਜਾਰੀ ਕੀਤਾ ਹੈ।
* OIDC ID Tokens (ਪਛਾਣ ਟੋਕਨ), ਜੋ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਸਿਰਫ਼ ਉਸ client ਦੁਆਰਾ ਹੀ ਖਪਤ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ ਜਿਸ ਨੇ ਅਧਿਕਾਰੀਕਰਨ ਪ੍ਰਵਾਹ (authorization flow) ਸ਼ੁਰੂ ਕੀਤਾ ਸੀ।

The risk levels for some of the requirements in this chapter depend on whether the client is a confidential client or regarded as a public client. Since using strong client authentication mitigates many attack vectors, a few requirements might be relaxed when using a confidential client for L1 applications.

ਇਸ ਅਧਿਆਇ ਦੀਆਂ ਕੁਝ ਲੋੜਾਂ ਲਈ ਜੋਖਮ ਪੱਧਰ ਇਸ ਗੱਲ 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ ਕਿ client ਇੱਕ confidential client ਹੈ ਜਾਂ ਇਸ ਨੂੰ public client ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ। ਕਿਉਂਕਿ ਮਜ਼ਬੂਤ client ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਵਰਤੋਂ ਕਈ ਹਮਲਾ ਵੈਕਟਰਾਂ (attack vectors) ਨੂੰ ਘਟਾਉਂਦੀ ਹੈ, L1 ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ confidential client ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਸਮੇਂ ਕੁਝ ਲੋੜਾਂ ਢਿੱਲੀਆਂ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।

## V10.1 Generic OAuth and OIDC Security
## V10.1 ਆਮ OAuth ਅਤੇ OIDC ਸੁਰੱਖਿਆ

This section covers generic architectural requirements that apply to all applications using OAuth or OIDC.

ਇਹ ਭਾਗ ਉਹਨਾਂ ਆਮ ਆਰਕੀਟੈਕਚਰ-ਸੰਬੰਧੀ ਲੋੜਾਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ ਜੋ OAuth ਜਾਂ OIDC ਵਰਤਣ ਵਾਲੀਆਂ ਸਾਰੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ 'ਤੇ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **10.1.1** | Verify that tokens are only sent to components that strictly need them. For example, when using a backend-for-frontend pattern for browser-based JavaScript applications, access and refresh tokens shall only be accessible for the backend. | 2 |
| **10.1.2** | Verify that the client only accepts values from the authorization server (such as the authorization code or ID Token) if these values result from an authorization flow that was initiated by the same user agent session and transaction. This requires that client-generated secrets, such as the proof key for code exchange (PKCE) 'code_verifier', 'state' or OIDC 'nonce', are not guessable, are specific to the transaction, and are securely bound to both the client and the user agent session in which the transaction was started. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **10.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਟੋਕਨ ਸਿਰਫ਼ ਉਹਨਾਂ ਹਿੱਸਿਆਂ ਨੂੰ ਹੀ ਭੇਜੇ ਜਾਂਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਉਹਨਾਂ ਦੀ ਸਖ਼ਤ ਲੋੜ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਬ੍ਰਾਊਜ਼ਰ-ਆਧਾਰਿਤ JavaScript ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ backend-for-frontend ਪੈਟਰਨ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਸਮੇਂ, access ਅਤੇ refresh tokens ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਸਿਰਫ਼ ਬੈਕਐਂਡ ਲਈ ਹੀ ਪਹੁੰਚਯੋਗ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ। | 2 |
| **10.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ client authorization server ਤੋਂ ਮੁੱਲ (ਜਿਵੇਂ ਕਿ authorization code ਜਾਂ ID Token) ਸਿਰਫ਼ ਤਾਂ ਹੀ ਸਵੀਕਾਰ ਕਰਦਾ ਹੈ ਜੇ ਇਹ ਮੁੱਲ ਉਸੇ ਯੂਜ਼ਰ ਏਜੰਟ (user agent) ਸੈਸ਼ਨ ਅਤੇ ਟ੍ਰਾਂਜ਼ੈਕਸ਼ਨ ਦੁਆਰਾ ਸ਼ੁਰੂ ਕੀਤੇ ਅਧਿਕਾਰੀਕਰਨ ਪ੍ਰਵਾਹ ਦਾ ਨਤੀਜਾ ਹਨ। ਇਸ ਲਈ ਜ਼ਰੂਰੀ ਹੈ ਕਿ client ਦੁਆਰਾ ਪੈਦਾ ਕੀਤੇ ਭੇਦ, ਜਿਵੇਂ ਕਿ proof key for code exchange (PKCE) 'code_verifier', 'state' ਜਾਂ OIDC 'nonce', ਅੰਦਾਜ਼ਾ ਲਗਾਉਣ ਯੋਗ ਨਾ ਹੋਣ, ਟ੍ਰਾਂਜ਼ੈਕਸ਼ਨ ਲਈ ਵਿਸ਼ੇਸ਼ ਹੋਣ, ਅਤੇ client ਅਤੇ ਉਸ ਯੂਜ਼ਰ ਏਜੰਟ ਸੈਸ਼ਨ ਦੋਵਾਂ ਨਾਲ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਬੰਨ੍ਹੇ ਹੋਏ ਹੋਣ ਜਿਸ ਵਿੱਚ ਟ੍ਰਾਂਜ਼ੈਕਸ਼ਨ ਸ਼ੁਰੂ ਕੀਤੀ ਗਈ ਸੀ। | 2 |

## V10.2 OAuth Client
## V10.2 OAuth Client (ਓਅਥ ਕਲਾਇੰਟ)

These requirements detail the responsibilities for OAuth client applications. The client can be, for example, a web server backend (often acting as a Backend For Frontend, BFF), a backend service integration, or a frontend Single Page Application (SPA, aka browser-based application).

ਇਹ ਲੋੜਾਂ OAuth client ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੀਆਂ ਜ਼ਿੰਮੇਵਾਰੀਆਂ ਦਾ ਵੇਰਵਾ ਦਿੰਦੀਆਂ ਹਨ। client, ਉਦਾਹਰਨ ਲਈ, ਇੱਕ ਵੈੱਬ ਸਰਵਰ ਬੈਕਐਂਡ (ਜੋ ਅਕਸਰ Backend For Frontend, BFF ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ), ਇੱਕ ਬੈਕਐਂਡ ਸੇਵਾ ਏਕੀਕਰਨ, ਜਾਂ ਇੱਕ ਫਰੰਟਐਂਡ Single Page Application (SPA — ਇੱਕ-ਪੰਨਾ ਐਪਲੀਕੇਸ਼ਨ, ਜਿਸ ਨੂੰ ਬ੍ਰਾਊਜ਼ਰ-ਆਧਾਰਿਤ ਐਪਲੀਕੇਸ਼ਨ ਵੀ ਕਿਹਾ ਜਾਂਦਾ ਹੈ) ਹੋ ਸਕਦਾ ਹੈ।

In general, backend clients are regarded as confidential clients and frontend clients are regarded as public clients. However, native applications running on the end-user device can be regarded as confidential when using OAuth dynamic client registration.

ਆਮ ਤੌਰ 'ਤੇ, ਬੈਕਐਂਡ clients ਨੂੰ confidential clients ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਫਰੰਟਐਂਡ clients ਨੂੰ public clients ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ। ਹਾਲਾਂਕਿ, ਅੰਤਮ-ਉਪਭੋਗਤਾ ਦੀ ਡਿਵਾਈਸ 'ਤੇ ਚੱਲਣ ਵਾਲੀਆਂ ਨੇਟਿਵ (native) ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ OAuth ਗਤੀਸ਼ੀਲ client ਰਜਿਸਟ੍ਰੇਸ਼ਨ (dynamic client registration) ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਸਮੇਂ confidential ਮੰਨਿਆ ਜਾ ਸਕਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **10.2.1** | Verify that, if the code flow is used, the OAuth client has protection against browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF), which trigger token requests, either by using proof key for code exchange (PKCE) functionality or checking the 'state' parameter that was sent in the authorization request. | 2 |
| **10.2.2** | Verify that, if the OAuth client can interact with more than one authorization server, it has a defense against mix-up attacks. For example, it could require that the authorization server return the 'iss' parameter value and validate it in the authorization response and the token response. | 2 |
| **10.2.3** | Verify that the OAuth client only requests the required scopes (or other authorization parameters) in requests to the authorization server. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **10.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ code flow ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਤਾਂ OAuth client ਕੋਲ ਬ੍ਰਾਊਜ਼ਰ-ਆਧਾਰਿਤ ਬੇਨਤੀ ਜਾਅਲਸਾਜ਼ੀ ਹਮਲਿਆਂ, ਜਿਨ੍ਹਾਂ ਨੂੰ ਆਮ ਤੌਰ 'ਤੇ ਕਰਾਸ-ਸਾਈਟ ਬੇਨਤੀ ਜਾਅਲਸਾਜ਼ੀ (CSRF) ਕਿਹਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਜੋ ਟੋਕਨ ਬੇਨਤੀਆਂ ਨੂੰ ਸ਼ੁਰੂ ਕਰਦੇ ਹਨ, ਦੇ ਵਿਰੁੱਧ ਸੁਰੱਖਿਆ ਹੈ, ਜਾਂ ਤਾਂ proof key for code exchange (PKCE) ਕਾਰਜਸ਼ੀਲਤਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਾਂ ਅਧਿਕਾਰੀਕਰਨ ਬੇਨਤੀ ਵਿੱਚ ਭੇਜੇ ਗਏ 'state' ਪੈਰਾਮੀਟਰ ਦੀ ਜਾਂਚ ਕਰਕੇ। | 2 |
| **10.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ OAuth client ਇੱਕ ਤੋਂ ਵੱਧ authorization server ਨਾਲ ਅੰਤਰਕਿਰਿਆ ਕਰ ਸਕਦਾ ਹੈ, ਤਾਂ ਇਸ ਕੋਲ mix-up ਹਮਲਿਆਂ (ਸਰਵਰਾਂ ਦੇ ਰਲ਼-ਗੱਡ ਹੋਣ ਵਾਲੇ ਹਮਲਿਆਂ) ਦੇ ਵਿਰੁੱਧ ਰੱਖਿਆ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਇਹ ਮੰਗ ਕਰ ਸਕਦਾ ਹੈ ਕਿ authorization server 'iss' ਪੈਰਾਮੀਟਰ ਮੁੱਲ ਵਾਪਸ ਕਰੇ ਅਤੇ ਅਧਿਕਾਰੀਕਰਨ ਜਵਾਬ ਅਤੇ ਟੋਕਨ ਜਵਾਬ ਵਿੱਚ ਇਸ ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰੇ। | 2 |
| **10.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ OAuth client authorization server ਨੂੰ ਬੇਨਤੀਆਂ ਵਿੱਚ ਸਿਰਫ਼ ਲੋੜੀਂਦੇ scopes (ਜਾਂ ਹੋਰ ਅਧਿਕਾਰੀਕਰਨ ਪੈਰਾਮੀਟਰਾਂ) ਦੀ ਹੀ ਬੇਨਤੀ ਕਰਦਾ ਹੈ। | 3 |

## V10.3 OAuth Resource Server
## V10.3 OAuth Resource Server (ਓਅਥ ਸਰੋਤ ਸਰਵਰ)

In the context of ASVS and this chapter, the resource server is an API. To provide secure access, the resource server must:

ASVS ਅਤੇ ਇਸ ਅਧਿਆਇ ਦੇ ਸੰਦਰਭ ਵਿੱਚ, resource server ਇੱਕ API ਹੈ। ਸੁਰੱਖਿਅਤ ਪਹੁੰਚ ਪ੍ਰਦਾਨ ਕਰਨ ਲਈ, resource server ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ:

* Validate the access token, according to the token format and relevant protocol specifications, e.g., JWT-validation or OAuth token introspection.
* If valid, enforce authorization decisions based on the information from the access token and permissions which have been granted. For example, the resource server needs to verify that the client (acting on behalf of RO) is authorized to access the requested resource.

* access token ਨੂੰ ਟੋਕਨ ਫਾਰਮੈਟ ਅਤੇ ਸੰਬੰਧਤ ਪ੍ਰੋਟੋਕਾਲ ਸਪੈਸੀਫ਼ਿਕੇਸ਼ਨਾਂ ਦੇ ਅਨੁਸਾਰ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ, ਜਿਵੇਂ, JWT-ਪ੍ਰਮਾਣਿਕਤਾ ਜਾਂ OAuth token introspection।
* ਜੇ ਜਾਇਜ਼ ਹੈ, ਤਾਂ access token ਦੀ ਜਾਣਕਾਰੀ ਅਤੇ ਦਿੱਤੀਆਂ ਗਈਆਂ ਇਜਾਜ਼ਤਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਅਧਿਕਾਰੀਕਰਨ ਫ਼ੈਸਲੇ ਲਾਗੂ ਕਰਨੇ ਚਾਹੀਦੇ ਹਨ। ਉਦਾਹਰਨ ਲਈ, resource server ਨੂੰ ਇਹ ਤਸਦੀਕ ਕਰਨ ਦੀ ਲੋੜ ਹੈ ਕਿ client (RO ਦੀ ਤਰਫ਼ੋਂ ਕੰਮ ਕਰਦਾ ਹੋਇਆ) ਬੇਨਤੀ ਕੀਤੇ ਸਰੋਤ ਤੱਕ ਪਹੁੰਚ ਲਈ ਅਧਿਕਾਰਤ ਹੈ।

Therefore, the requirements listed here are OAuth or OIDC specific and should be performed after token validation and before performing authorization based on information from the token.

ਇਸ ਲਈ, ਇੱਥੇ ਸੂਚੀਬੱਧ ਲੋੜਾਂ OAuth ਜਾਂ OIDC ਵਿਸ਼ੇਸ਼ ਹਨ ਅਤੇ ਇਹਨਾਂ ਨੂੰ ਟੋਕਨ ਪ੍ਰਮਾਣਿਕਤਾ ਤੋਂ ਬਾਅਦ ਅਤੇ ਟੋਕਨ ਦੀ ਜਾਣਕਾਰੀ ਦੇ ਆਧਾਰ 'ਤੇ ਅਧਿਕਾਰੀਕਰਨ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਪੂਰਾ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **10.3.1** | Verify that the resource server only accepts access tokens that are intended for use with that service (audience). The audience may be included in a structured access token (such as the 'aud' claim in JWT), or it can be checked using the token introspection endpoint. | 2 |
| **10.3.2** | Verify that the resource server enforces authorization decisions based on claims from the access token that define delegated authorization. If claims such as 'sub', 'scope', and 'authorization_details' are present, they must be part of the decision. | 2 |
| **10.3.3** | Verify that if an access control decision requires identifying a unique user from an access token (JWT or related token introspection response), the resource server identifies the user from claims that cannot be reassigned to other users. Typically, it means using a combination of 'iss' and 'sub' claims. | 2 |
| **10.3.4** | Verify that, if the resource server requires specific authentication strength, methods, or recentness, it verifies that the presented access token satisfies these constraints. For example, if present, using the OIDC 'acr', 'amr' and 'auth_time' claims respectively. | 2 |
| **10.3.5** | Verify that the resource server prevents the use of stolen access tokens or replay of access tokens (from unauthorized parties) by requiring sender-constrained access tokens, either Mutual TLS for OAuth 2 or OAuth 2 Demonstration of Proof of Possession (DPoP). | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **10.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ resource server ਸਿਰਫ਼ ਉਹਨਾਂ access tokens ਨੂੰ ਹੀ ਸਵੀਕਾਰ ਕਰਦਾ ਹੈ ਜੋ ਉਸ ਸੇਵਾ ਨਾਲ ਵਰਤੋਂ ਲਈ ਹਨ (audience)। audience ਨੂੰ ਇੱਕ ਸੰਰਚਿਤ access token ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ (ਜਿਵੇਂ ਕਿ JWT ਵਿੱਚ 'aud' ਦਾਅਵਾ), ਜਾਂ ਇਸ ਦੀ ਜਾਂਚ token introspection ਅੰਤ-ਬਿੰਦੂ (endpoint) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। | 2 |
| **10.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ resource server access token ਦੇ ਉਹਨਾਂ ਦਾਅਵਿਆਂ ਦੇ ਆਧਾਰ 'ਤੇ ਅਧਿਕਾਰੀਕਰਨ ਫ਼ੈਸਲੇ ਲਾਗੂ ਕਰਦਾ ਹੈ ਜੋ ਸੌਂਪੇ ਗਏ ਅਧਿਕਾਰੀਕਰਨ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਨ। ਜੇ 'sub', 'scope', ਅਤੇ 'authorization_details' ਵਰਗੇ ਦਾਅਵੇ ਮੌਜੂਦ ਹਨ, ਤਾਂ ਉਹ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਫ਼ੈਸਲੇ ਦਾ ਹਿੱਸਾ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ। | 2 |
| **10.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜੇ ਕਿਸੇ ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਫ਼ੈਸਲੇ ਲਈ access token (JWT ਜਾਂ ਸੰਬੰਧਤ token introspection ਜਵਾਬ) ਤੋਂ ਇੱਕ ਵਿਲੱਖਣ ਉਪਭੋਗਤਾ ਦੀ ਪਛਾਣ ਕਰਨ ਦੀ ਲੋੜ ਹੈ, ਤਾਂ resource server ਉਪਭੋਗਤਾ ਦੀ ਪਛਾਣ ਉਹਨਾਂ ਦਾਅਵਿਆਂ ਤੋਂ ਕਰਦਾ ਹੈ ਜੋ ਹੋਰ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਮੁੜ-ਨਿਰਧਾਰਤ ਨਹੀਂ ਕੀਤੇ ਜਾ ਸਕਦੇ। ਆਮ ਤੌਰ 'ਤੇ, ਇਸ ਦਾ ਮਤਲਬ 'iss' ਅਤੇ 'sub' ਦਾਅਵਿਆਂ ਦੇ ਸੁਮੇਲ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਹੈ। | 2 |
| **10.3.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ resource server ਨੂੰ ਖ਼ਾਸ ਪ੍ਰਮਾਣੀਕਰਨ ਤਾਕਤ, ਵਿਧੀਆਂ, ਜਾਂ ਤਾਜ਼ਗੀ (recentness) ਦੀ ਲੋੜ ਹੈ, ਤਾਂ ਇਹ ਤਸਦੀਕ ਕਰਦਾ ਹੈ ਕਿ ਪੇਸ਼ ਕੀਤਾ access token ਇਹਨਾਂ ਪਾਬੰਦੀਆਂ ਨੂੰ ਪੂਰਾ ਕਰਦਾ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਜੇ ਮੌਜੂਦ ਹੋਣ, ਤਾਂ ਕ੍ਰਮਵਾਰ OIDC 'acr', 'amr' ਅਤੇ 'auth_time' ਦਾਅਵਿਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ। | 2 |
| **10.3.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ resource server ਭੇਜਣਹਾਰ-ਬੰਨ੍ਹੇ (sender-constrained) access tokens ਦੀ ਮੰਗ ਕਰਕੇ ਚੋਰੀ ਕੀਤੇ access tokens ਦੀ ਵਰਤੋਂ ਜਾਂ (ਅਣਅਧਿਕਾਰਤ ਧਿਰਾਂ ਵੱਲੋਂ) access tokens ਦੇ ਰੀਪਲੇ ਨੂੰ ਰੋਕਦਾ ਹੈ, ਜਾਂ ਤਾਂ Mutual TLS for OAuth 2 ਜਾਂ OAuth 2 Demonstration of Proof of Possession (DPoP) ਰਾਹੀਂ। | 3 |

## V10.4 OAuth Authorization Server
## V10.4 OAuth Authorization Server (ਓਅਥ ਅਧਿਕਾਰੀਕਰਨ ਸਰਵਰ)

These requirements detail the responsibilities for OAuth authorization servers, including OpenID Providers.

ਇਹ ਲੋੜਾਂ OAuth authorization servers, OpenID Providers ਸਮੇਤ, ਦੀਆਂ ਜ਼ਿੰਮੇਵਾਰੀਆਂ ਦਾ ਵੇਰਵਾ ਦਿੰਦੀਆਂ ਹਨ।

For client authentication, the 'self_signed_tls_client_auth' method is allowed with the prerequisites required by [section 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) of [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705).

client ਪ੍ਰਮਾਣੀਕਰਨ ਲਈ, 'self_signed_tls_client_auth' ਵਿਧੀ ਦੀ ਇਜਾਜ਼ਤ [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705) ਦੇ [ਭਾਗ 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) ਦੁਆਰਾ ਲੋੜੀਂਦੀਆਂ ਪੂਰਵ-ਸ਼ਰਤਾਂ ਨਾਲ ਹੈ।

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

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **10.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ authorization server ਪਹਿਲਾਂ ਤੋਂ ਰਜਿਸਟਰ ਕੀਤੇ URI ਦੀ client-ਵਿਸ਼ੇਸ਼ allowlist ਦੇ ਆਧਾਰ 'ਤੇ ਸਟੀਕ ਸਟ੍ਰਿੰਗ ਤੁਲਨਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ redirect URIs ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਦਾ ਹੈ। | 1 |
| **10.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ authorization server ਅਧਿਕਾਰੀਕਰਨ ਜਵਾਬ ਵਿੱਚ authorization code ਵਾਪਸ ਕਰਦਾ ਹੈ, ਤਾਂ ਇਸ ਨੂੰ ਟੋਕਨ ਬੇਨਤੀ ਲਈ ਸਿਰਫ਼ ਇੱਕ ਵਾਰ ਹੀ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਅਜਿਹੇ authorization code ਨਾਲ ਦੂਜੀ ਜਾਇਜ਼ ਬੇਨਤੀ ਲਈ ਜੋ ਪਹਿਲਾਂ ਹੀ access token ਜਾਰੀ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਚੁੱਕਾ ਹੈ, authorization server ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਟੋਕਨ ਬੇਨਤੀ ਨੂੰ ਅਸਵੀਕਾਰ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ ਉਸ authorization code ਨਾਲ ਸੰਬੰਧਤ ਕੋਈ ਵੀ ਜਾਰੀ ਕੀਤੇ ਟੋਕਨ ਰੱਦ (revoke) ਕਰਨੇ ਚਾਹੀਦੇ ਹਨ। | 1 |
| **10.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ authorization code ਛੋਟੀ ਮਿਆਦ ਵਾਲਾ (short-lived) ਹੈ। ਵੱਧ ਤੋਂ ਵੱਧ ਜੀਵਨਕਾਲ L1 ਅਤੇ L2 ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ 10 ਮਿੰਟ ਤੱਕ ਅਤੇ L3 ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ 1 ਮਿੰਟ ਤੱਕ ਹੋ ਸਕਦਾ ਹੈ। | 1 |
| **10.4.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਿਸੇ ਦਿੱਤੇ client ਲਈ, authorization server ਸਿਰਫ਼ ਉਹਨਾਂ grants (ਅਧਿਕਾਰੀਕਰਨ ਪ੍ਰਵਾਹ ਦੀਆਂ ਕਿਸਮਾਂ) ਦੀ ਵਰਤੋਂ ਦੀ ਹੀ ਇਜਾਜ਼ਤ ਦਿੰਦਾ ਹੈ ਜਿਨ੍ਹਾਂ ਦੀ ਇਸ client ਨੂੰ ਵਰਤੋਂ ਕਰਨ ਦੀ ਲੋੜ ਹੈ। ਧਿਆਨ ਦਿਓ ਕਿ 'token' (Implicit flow) ਅਤੇ 'password' (Resource Owner Password Credentials flow) grants ਹੁਣ ਨਹੀਂ ਵਰਤੇ ਜਾਣੇ ਚਾਹੀਦੇ। | 1 |
| **10.4.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ authorization server public clients ਲਈ refresh token ਰੀਪਲੇ ਹਮਲਿਆਂ ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ, ਤਰਜੀਹੀ ਤੌਰ 'ਤੇ ਭੇਜਣਹਾਰ-ਬੰਨ੍ਹੇ refresh tokens ਦੀ ਵਰਤੋਂ ਕਰਕੇ, ਭਾਵ, Demonstrating Proof of Possession (DPoP) ਜਾਂ mutual TLS (mTLS) ਦੀ ਵਰਤੋਂ ਕਰਨ ਵਾਲੇ Certificate-Bound Access Tokens। L1 ਅਤੇ L2 ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ, refresh token ਰੋਟੇਸ਼ਨ (rotation) ਵਰਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਜੇ refresh token ਰੋਟੇਸ਼ਨ ਵਰਤੀ ਜਾਂਦੀ ਹੈ, ਤਾਂ authorization server ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਵਰਤੋਂ ਤੋਂ ਬਾਅਦ refresh token ਨੂੰ ਅਵੈਧ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ, ਅਤੇ ਜੇ ਪਹਿਲਾਂ ਹੀ ਵਰਤਿਆ ਅਤੇ ਅਵੈਧ ਕੀਤਾ refresh token ਪ੍ਰਦਾਨ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਤਾਂ ਉਸ ਅਧਿਕਾਰੀਕਰਨ ਲਈ ਸਾਰੇ refresh tokens ਰੱਦ ਕਰਨੇ ਚਾਹੀਦੇ ਹਨ। | 1 |
| **10.4.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ code grant ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਤਾਂ authorization server proof key for code exchange (PKCE) ਦੀ ਮੰਗ ਕਰਕੇ authorization code ਇੰਟਰਸੈਪਸ਼ਨ (interception) ਹਮਲਿਆਂ ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ। ਅਧਿਕਾਰੀਕਰਨ ਬੇਨਤੀਆਂ ਲਈ, authorization server ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਇੱਕ ਜਾਇਜ਼ 'code_challenge' ਮੁੱਲ ਦੀ ਮੰਗ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ ਅਤੇ 'plain' ਦੇ 'code_challenge_method' ਮੁੱਲ ਨੂੰ ਸਵੀਕਾਰ ਨਹੀਂ ਕਰਨਾ ਚਾਹੀਦਾ। ਟੋਕਨ ਬੇਨਤੀ ਲਈ, ਇਸ ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ 'code_verifier' ਪੈਰਾਮੀਟਰ ਦੀ ਪ੍ਰਮਾਣਿਕਤਾ ਦੀ ਮੰਗ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ। | 2 |
| **10.4.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜੇ authorization server ਬਿਨਾਂ ਪ੍ਰਮਾਣੀਕਰਨ ਦੇ ਗਤੀਸ਼ੀਲ client ਰਜਿਸਟ੍ਰੇਸ਼ਨ (unauthenticated dynamic client registration) ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ, ਤਾਂ ਇਹ ਖ਼ਤਰਨਾਕ client ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਜੋਖਮ ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ। ਇਸ ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ client ਮੈਟਾਡਾਟਾ, ਜਿਵੇਂ ਕਿ ਕੋਈ ਵੀ ਰਜਿਸਟਰ ਕੀਤੇ URI, ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ, ਉਪਭੋਗਤਾ ਦੀ ਸਹਿਮਤੀ ਯਕੀਨੀ ਬਣਾਉਣੀ ਚਾਹੀਦੀ ਹੈ, ਅਤੇ ਕਿਸੇ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ client ਐਪਲੀਕੇਸ਼ਨ ਨਾਲ ਅਧਿਕਾਰੀਕਰਨ ਬੇਨਤੀ ਨੂੰ ਪ੍ਰੋਸੈੱਸ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਉਪਭੋਗਤਾ ਨੂੰ ਚੇਤਾਵਨੀ ਦੇਣੀ ਚਾਹੀਦੀ ਹੈ। | 2 |
| **10.4.8** | ਤਸਦੀਕ ਕਰੋ ਕਿ refresh tokens ਦੀ ਇੱਕ ਨਿਰਪੇਖ ਮਿਆਦ-ਸਮਾਪਤੀ (absolute expiration) ਹੈ, ਭਾਵੇਂ ਸਲਾਈਡਿੰਗ (sliding) refresh token ਮਿਆਦ-ਸਮਾਪਤੀ ਲਾਗੂ ਕੀਤੀ ਗਈ ਹੋਵੇ। | 2 |
| **10.4.9** | ਤਸਦੀਕ ਕਰੋ ਕਿ refresh tokens ਅਤੇ ਹਵਾਲਾ access tokens ਨੂੰ ਇੱਕ ਅਧਿਕਾਰਤ ਉਪਭੋਗਤਾ ਦੁਆਰਾ authorization server ਦੇ ਉਪਭੋਗਤਾ ਇੰਟਰਫ਼ੇਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਰੱਦ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਤਾਂ ਜੋ ਖ਼ਤਰਨਾਕ clients ਜਾਂ ਚੋਰੀ ਕੀਤੇ ਟੋਕਨਾਂ ਦੇ ਜੋਖਮ ਨੂੰ ਘਟਾਇਆ ਜਾ ਸਕੇ। | 2 |
| **10.4.10** | ਤਸਦੀਕ ਕਰੋ ਕਿ confidential client ਦਾ client-ਤੋਂ-authorization server ਬੈਕ-ਚੈਨਲ (backchannel) ਬੇਨਤੀਆਂ, ਜਿਵੇਂ ਕਿ ਟੋਕਨ ਬੇਨਤੀਆਂ, pushed authorization requests (PAR), ਅਤੇ ਟੋਕਨ ਰੱਦ ਕਰਨ ਦੀਆਂ ਬੇਨਤੀਆਂ, ਲਈ ਪ੍ਰਮਾਣੀਕਰਨ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। | 2 |
| **10.4.11** | ਤਸਦੀਕ ਕਰੋ ਕਿ authorization server ਸੰਰਚਨਾ OAuth client ਨੂੰ ਸਿਰਫ਼ ਲੋੜੀਂਦੇ scopes ਹੀ ਨਿਰਧਾਰਤ ਕਰਦੀ ਹੈ। | 2 |
| **10.4.12** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਿਸੇ ਦਿੱਤੇ client ਲਈ, authorization server ਸਿਰਫ਼ ਉਸ 'response_mode' ਮੁੱਲ ਦੀ ਹੀ ਇਜਾਜ਼ਤ ਦਿੰਦਾ ਹੈ ਜਿਸ ਦੀ ਇਸ client ਨੂੰ ਵਰਤੋਂ ਕਰਨ ਦੀ ਲੋੜ ਹੈ। ਉਦਾਹਰਨ ਲਈ, authorization server ਦੁਆਰਾ ਇਸ ਮੁੱਲ ਨੂੰ ਉਮੀਦ ਕੀਤੇ ਮੁੱਲਾਂ ਦੇ ਵਿਰੁੱਧ ਪ੍ਰਮਾਣਿਤ ਕਰਵਾ ਕੇ ਜਾਂ pushed authorization request (PAR) ਜਾਂ JWT-secured Authorization Request (JAR) ਦੀ ਵਰਤੋਂ ਕਰਕੇ। | 3 |
| **10.4.13** | ਤਸਦੀਕ ਕਰੋ ਕਿ grant type 'code' ਹਮੇਸ਼ਾ pushed authorization requests (PAR) ਦੇ ਨਾਲ ਮਿਲ ਕੇ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। | 3 |
| **10.4.14** | ਤਸਦੀਕ ਕਰੋ ਕਿ authorization server ਸਿਰਫ਼ ਭੇਜਣਹਾਰ-ਬੰਨ੍ਹੇ (Proof-of-Possession) access tokens ਹੀ ਜਾਰੀ ਕਰਦਾ ਹੈ, ਜਾਂ ਤਾਂ mutual TLS (mTLS) ਦੀ ਵਰਤੋਂ ਕਰਨ ਵਾਲੇ ਸਰਟੀਫ਼ਿਕੇਟ-ਬੰਨ੍ਹੇ (certificate-bound) access tokens ਨਾਲ ਜਾਂ DPoP-ਬੰਨ੍ਹੇ access tokens (Demonstration of Proof of Possession) ਨਾਲ। | 3 |
| **10.4.15** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਇੱਕ ਸਰਵਰ-ਸਾਈਡ client (ਜੋ ਅੰਤਮ-ਉਪਭੋਗਤਾ ਦੀ ਡਿਵਾਈਸ 'ਤੇ ਨਹੀਂ ਚਲਾਇਆ ਜਾਂਦਾ) ਲਈ, authorization server ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ 'authorization_details' ਪੈਰਾਮੀਟਰ ਮੁੱਲ client ਬੈਕਐਂਡ ਤੋਂ ਹੈ ਅਤੇ ਉਪਭੋਗਤਾ ਨੇ ਇਸ ਨਾਲ ਛੇੜਛਾੜ ਨਹੀਂ ਕੀਤੀ। ਉਦਾਹਰਨ ਲਈ, pushed authorization request (PAR) ਜਾਂ JWT-secured Authorization Request (JAR) ਦੀ ਵਰਤੋਂ ਦੀ ਮੰਗ ਕਰਕੇ। | 3 |
| **10.4.16** | ਤਸਦੀਕ ਕਰੋ ਕਿ client confidential ਹੈ ਅਤੇ authorization server ਮਜ਼ਬੂਤ client ਪ੍ਰਮਾਣੀਕਰਨ ਵਿਧੀਆਂ (ਜਨਤਕ-ਕੁੰਜੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ 'ਤੇ ਆਧਾਰਿਤ ਅਤੇ ਰੀਪਲੇ ਹਮਲਿਆਂ ਪ੍ਰਤੀ ਰੋਧਕ) ਦੀ ਵਰਤੋਂ ਦੀ ਮੰਗ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ mutual TLS ('tls_client_auth', 'self_signed_tls_client_auth') ਜਾਂ private key JWT ('private_key_jwt')। | 3 |

## V10.5 OIDC Client
## V10.5 OIDC Client (ਓ.ਆਈ.ਡੀ.ਸੀ. ਕਲਾਇੰਟ)

As the OIDC relying party acts as an OAuth client, the requirements from the section "OAuth Client" apply as well.

ਕਿਉਂਕਿ OIDC ਨਿਰਭਰ ਧਿਰ ਇੱਕ OAuth client ਵਜੋਂ ਕੰਮ ਕਰਦੀ ਹੈ, "OAuth Client" ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ ਵੀ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ।

Note that the "Authentication with an Identity Provider" section in the "Authentication" chapter also contains relevant general requirements.

ਧਿਆਨ ਦਿਓ ਕਿ "ਪ੍ਰਮਾਣੀਕਰਨ" (Authentication) ਅਧਿਆਇ ਦੇ "ਪਛਾਣ ਪ੍ਰਦਾਤਾ ਨਾਲ ਪ੍ਰਮਾਣੀਕਰਨ" (Authentication with an Identity Provider) ਭਾਗ ਵਿੱਚ ਵੀ ਸੰਬੰਧਤ ਆਮ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **10.5.1** | Verify that the client (as the relying party) mitigates ID Token replay attacks. For example, by ensuring that the 'nonce' claim in the ID Token matches the 'nonce' value sent in the authentication request to the OpenID Provider (in OAuth2 refereed to as the authorization request sent to the authorization server). | 2 |
| **10.5.2** | Verify that the client uniquely identifies the user from ID Token claims, usually the 'sub' claim, which cannot be reassigned to other users (for the scope of an identity provider). | 2 |
| **10.5.3** | Verify that the client rejects attempts by a malicious authorization server to impersonate another authorization server through authorization server metadata. The client must reject authorization server metadata if the issuer URL in the authorization server metadata does not exactly match the pre-configured issuer URL expected by the client. | 2 |
| **10.5.4** | Verify that the client validates that the ID Token is intended to be used for that client (audience) by checking that the 'aud' claim from the token is equal to the 'client_id' value for the client. | 2 |
| **10.5.5** | Verify that, when using OIDC back-channel logout, the relying party mitigates denial of service through forced logout and cross-JWT confusion in the logout flow. The client must verify that the logout token is correctly typed with a value of 'logout+jwt', contains the 'event' claim with the correct member name, and does not contain a 'nonce' claim. Note that it is also recommended to have a short expiration (e.g., 2 minutes). | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **10.5.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ client (ਨਿਰਭਰ ਧਿਰ ਵਜੋਂ) ID Token ਰੀਪਲੇ ਹਮਲਿਆਂ ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਇਹ ਯਕੀਨੀ ਬਣਾ ਕੇ ਕਿ ID Token ਵਿੱਚ 'nonce' ਦਾਅਵਾ OpenID Provider ਨੂੰ ਪ੍ਰਮਾਣੀਕਰਨ ਬੇਨਤੀ ਵਿੱਚ ਭੇਜੇ ਗਏ 'nonce' ਮੁੱਲ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ (OAuth2 ਵਿੱਚ ਇਸ ਨੂੰ authorization server ਨੂੰ ਭੇਜੀ ਗਈ ਅਧਿਕਾਰੀਕਰਨ ਬੇਨਤੀ ਕਿਹਾ ਜਾਂਦਾ ਹੈ)। | 2 |
| **10.5.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ client ID Token ਦਾਅਵਿਆਂ ਤੋਂ, ਆਮ ਤੌਰ 'ਤੇ 'sub' ਦਾਅਵੇ ਤੋਂ, ਉਪਭੋਗਤਾ ਦੀ ਵਿਲੱਖਣ ਤੌਰ 'ਤੇ ਪਛਾਣ ਕਰਦਾ ਹੈ, ਜਿਸ ਨੂੰ (ਕਿਸੇ ਪਛਾਣ ਪ੍ਰਦਾਤਾ ਦੇ ਘੇਰੇ ਵਿੱਚ) ਹੋਰ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਮੁੜ-ਨਿਰਧਾਰਤ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ। | 2 |
| **10.5.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ client ਕਿਸੇ ਖ਼ਤਰਨਾਕ authorization server ਦੁਆਰਾ authorization server ਮੈਟਾਡਾਟਾ ਰਾਹੀਂ ਕਿਸੇ ਹੋਰ authorization server ਦੀ ਪਛਾਣ-ਨਕਲ (impersonation) ਕਰਨ ਦੀਆਂ ਕੋਸ਼ਿਸ਼ਾਂ ਨੂੰ ਅਸਵੀਕਾਰ ਕਰਦਾ ਹੈ। ਜੇ authorization server ਮੈਟਾਡਾਟਾ ਵਿੱਚ ਜਾਰੀਕਰਤਾ (issuer) URL client ਦੁਆਰਾ ਉਮੀਦ ਕੀਤੇ ਪਹਿਲਾਂ ਤੋਂ ਸੰਰਚਿਤ ਜਾਰੀਕਰਤਾ URL ਨਾਲ ਸਟੀਕ ਤੌਰ 'ਤੇ ਮੇਲ ਨਹੀਂ ਖਾਂਦਾ, ਤਾਂ client ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ authorization server ਮੈਟਾਡਾਟਾ ਨੂੰ ਅਸਵੀਕਾਰ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ। | 2 |
| **10.5.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ client ਇਹ ਜਾਂਚ ਕਰਕੇ ਕਿ ਟੋਕਨ ਦਾ 'aud' ਦਾਅਵਾ client ਦੇ 'client_id' ਮੁੱਲ ਦੇ ਬਰਾਬਰ ਹੈ, ਇਹ ਪ੍ਰਮਾਣਿਤ ਕਰਦਾ ਹੈ ਕਿ ID Token ਉਸ client (audience) ਲਈ ਵਰਤੇ ਜਾਣ ਲਈ ਹੈ। | 2 |
| **10.5.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ, OIDC ਬੈਕ-ਚੈਨਲ ਲੌਗਆਊਟ (back-channel logout) ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਸਮੇਂ, ਨਿਰਭਰ ਧਿਰ ਲੌਗਆਊਟ ਪ੍ਰਵਾਹ ਵਿੱਚ ਜ਼ਬਰਦਸਤੀ ਲੌਗਆਊਟ ਰਾਹੀਂ ਸੇਵਾ-ਇਨਕਾਰ ਅਤੇ ਕਰਾਸ-JWT ਉਲਝਣ (cross-JWT confusion) ਨੂੰ ਘਟਾਉਂਦੀ ਹੈ। client ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਤਸਦੀਕ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਕਿ logout token 'logout+jwt' ਮੁੱਲ ਨਾਲ ਸਹੀ ਤਰ੍ਹਾਂ ਟਾਈਪ ਕੀਤਾ ਗਿਆ ਹੈ, ਸਹੀ ਮੈਂਬਰ ਨਾਮ ਨਾਲ 'event' ਦਾਅਵਾ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ, ਅਤੇ 'nonce' ਦਾਅਵਾ ਸ਼ਾਮਲ ਨਹੀਂ ਕਰਦਾ। ਧਿਆਨ ਦਿਓ ਕਿ ਇੱਕ ਛੋਟੀ ਮਿਆਦ-ਸਮਾਪਤੀ (ਜਿਵੇਂ, 2 ਮਿੰਟ) ਰੱਖਣ ਦੀ ਵੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 2 |

## V10.6 OpenID Provider
## V10.6 OpenID Provider (ਓਪਨਆਈਡੀ ਪ੍ਰਦਾਤਾ)

As OpenID Providers act as OAuth authorization servers, the requirements from the section "OAuth Authorization Server" apply as well.

ਕਿਉਂਕਿ OpenID Providers OAuth authorization servers ਵਜੋਂ ਕੰਮ ਕਰਦੇ ਹਨ, "OAuth Authorization Server" ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ ਵੀ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ।

Note that if using the ID Token flow (not the code flow), no access tokens are issued, and many of the requirements for OAuth AS are not applicable.

ਧਿਆਨ ਦਿਓ ਕਿ ਜੇ ID Token flow (code flow ਨਹੀਂ) ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਕੋਈ access tokens ਜਾਰੀ ਨਹੀਂ ਕੀਤੇ ਜਾਂਦੇ, ਅਤੇ OAuth AS ਲਈ ਬਹੁਤ ਸਾਰੀਆਂ ਲੋੜਾਂ ਲਾਗੂ ਨਹੀਂ ਹੁੰਦੀਆਂ।

| # | Description | Level |
| :---: | :--- | :---: |
| **10.6.1** | Verify that the OpenID Provider only allows values 'code', 'ciba', 'id_token', or 'id_token code' for response mode. Note that 'code' is preferred over 'id_token code' (the OIDC Hybrid flow), and 'token' (any Implicit flow) must not be used. | 2 |
| **10.6.2** | Verify that the OpenID Provider mitigates denial of service through forced logout. By obtaining explicit confirmation from the end-user or, if present, validating parameters in the logout request (initiated by the relying party), such as the 'id_token_hint'. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **10.6.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ OpenID Provider response mode ਲਈ ਸਿਰਫ਼ 'code', 'ciba', 'id_token', ਜਾਂ 'id_token code' ਮੁੱਲਾਂ ਦੀ ਹੀ ਇਜਾਜ਼ਤ ਦਿੰਦਾ ਹੈ। ਧਿਆਨ ਦਿਓ ਕਿ 'code' ਨੂੰ 'id_token code' (OIDC Hybrid flow) ਨਾਲੋਂ ਤਰਜੀਹ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ, ਅਤੇ 'token' (ਕੋਈ ਵੀ Implicit flow) ਨਹੀਂ ਵਰਤਿਆ ਜਾਣਾ ਚਾਹੀਦਾ। | 2 |
| **10.6.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ OpenID Provider ਜ਼ਬਰਦਸਤੀ ਲੌਗਆਊਟ ਰਾਹੀਂ ਸੇਵਾ-ਇਨਕਾਰ ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ। ਅੰਤਮ-ਉਪਭੋਗਤਾ ਤੋਂ ਸਪੱਸ਼ਟ ਪੁਸ਼ਟੀ ਪ੍ਰਾਪਤ ਕਰਕੇ ਜਾਂ, ਜੇ ਮੌਜੂਦ ਹੋਣ, ਤਾਂ (ਨਿਰਭਰ ਧਿਰ ਦੁਆਰਾ ਸ਼ੁਰੂ ਕੀਤੀ) ਲੌਗਆਊਟ ਬੇਨਤੀ ਵਿੱਚ ਪੈਰਾਮੀਟਰਾਂ, ਜਿਵੇਂ ਕਿ 'id_token_hint', ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਕੇ। | 2 |

## V10.7 Consent Management
## V10.7 ਸਹਿਮਤੀ ਪ੍ਰਬੰਧਨ

These requirements cover the verification of the user's consent by the authorization server. Without proper user consent verification, a malicious actor may obtain permissions on the user's behalf through spoofing or social-engineering.

ਇਹ ਲੋੜਾਂ authorization server ਦੁਆਰਾ ਉਪਭੋਗਤਾ ਦੀ ਸਹਿਮਤੀ ਦੀ ਤਸਦੀਕ ਨੂੰ ਕਵਰ ਕਰਦੀਆਂ ਹਨ। ਸਹੀ ਉਪਭੋਗਤਾ ਸਹਿਮਤੀ ਤਸਦੀਕ ਤੋਂ ਬਿਨਾਂ, ਕੋਈ ਖ਼ਤਰਨਾਕ ਕਰਤਾ (malicious actor) ਸਪੂਫ਼ਿੰਗ ਜਾਂ ਸੋਸ਼ਲ ਇੰਜੀਨੀਅਰਿੰਗ ਰਾਹੀਂ ਉਪਭੋਗਤਾ ਦੀ ਤਰਫ਼ੋਂ ਇਜਾਜ਼ਤਾਂ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **10.7.1** | Verify that the authorization server ensures that the user consents to each authorization request. If the identity of the client cannot be assured, the authorization server must always explicitly prompt the user for consent. | 2 |
| **10.7.2** | Verify that when the authorization server prompts for user consent, it presents sufficient and clear information about what is being consented to. When applicable, this should include the nature of the requested authorizations (typically based on scope, resource server, Rich Authorization Requests (RAR) authorization details), the identity of the authorized application, and the lifetime of these authorizations. | 2 |
| **10.7.3** | Verify that the user can review, modify, and revoke consents which the user has granted through the authorization server. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **10.7.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ authorization server ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਉਪਭੋਗਤਾ ਹਰੇਕ ਅਧਿਕਾਰੀਕਰਨ ਬੇਨਤੀ ਲਈ ਸਹਿਮਤੀ ਦਿੰਦਾ ਹੈ। ਜੇ client ਦੀ ਪਛਾਣ ਦਾ ਭਰੋਸਾ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ, ਤਾਂ authorization server ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਹਮੇਸ਼ਾ ਉਪਭੋਗਤਾ ਤੋਂ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਸਹਿਮਤੀ ਮੰਗਣੀ ਚਾਹੀਦੀ ਹੈ। | 2 |
| **10.7.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਦੋਂ authorization server ਉਪਭੋਗਤਾ ਸਹਿਮਤੀ ਮੰਗਦਾ ਹੈ, ਤਾਂ ਇਹ ਇਸ ਬਾਰੇ ਕਾਫ਼ੀ ਅਤੇ ਸਪੱਸ਼ਟ ਜਾਣਕਾਰੀ ਪੇਸ਼ ਕਰਦਾ ਹੈ ਕਿ ਕਿਸ ਗੱਲ ਲਈ ਸਹਿਮਤੀ ਦਿੱਤੀ ਜਾ ਰਹੀ ਹੈ। ਜਿੱਥੇ ਲਾਗੂ ਹੋਵੇ, ਇਸ ਵਿੱਚ ਬੇਨਤੀ ਕੀਤੇ ਅਧਿਕਾਰੀਕਰਨਾਂ ਦਾ ਸੁਭਾਅ (ਆਮ ਤੌਰ 'ਤੇ scope, resource server, Rich Authorization Requests (RAR) authorization details 'ਤੇ ਆਧਾਰਿਤ), ਅਧਿਕਾਰਤ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਪਛਾਣ, ਅਤੇ ਇਹਨਾਂ ਅਧਿਕਾਰੀਕਰਨਾਂ ਦਾ ਜੀਵਨਕਾਲ ਸ਼ਾਮਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। | 2 |
| **10.7.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਪਭੋਗਤਾ ਉਹਨਾਂ ਸਹਿਮਤੀਆਂ ਦੀ ਸਮੀਖਿਆ ਕਰ ਸਕਦਾ ਹੈ, ਉਹਨਾਂ ਨੂੰ ਸੋਧ ਸਕਦਾ ਹੈ, ਅਤੇ ਰੱਦ ਕਰ ਸਕਦਾ ਹੈ ਜੋ ਉਪਭੋਗਤਾ ਨੇ authorization server ਰਾਹੀਂ ਦਿੱਤੀਆਂ ਹਨ। | 2 |

## References
## ਹਵਾਲੇ

For more information on OAuth, please see:

OAuth ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਕਿਰਪਾ ਕਰਕੇ ਵੇਖੋ:

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

For OAuth-related requirements in ASVS following published and in draft status RFC-s are used:

ASVS ਵਿੱਚ OAuth-ਸੰਬੰਧੀ ਲੋੜਾਂ ਲਈ ਹੇਠ ਲਿਖੇ ਪ੍ਰਕਾਸ਼ਿਤ ਅਤੇ ਡਰਾਫ਼ਟ ਸਥਿਤੀ ਵਾਲੇ RFC ਵਰਤੇ ਗਏ ਹਨ:

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

OpenID Connect ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਕਿਰਪਾ ਕਰਕੇ ਵੇਖੋ:

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
