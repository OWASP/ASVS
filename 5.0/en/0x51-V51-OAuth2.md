# V51 OAuth and OIDC

## Control Objective

OAuth2 (referred to as OAuth in this chapter) is an industry standard framework for obtaining API authorizations. For example, using OAuth, a client application can obtain access to APIs (server resources) on the user's behalf, where the user has delegated authorization to the application.

By itself, OAuth is not designed for user authentication. The OpenID Connect (OIDC) framework extends OAuth by adding a user identity layer on top of OAuth. Where OIDC provides support for e.g. standardized user information, Single-Sign On (SSO) and session management. As OIDC is an extension of OAuth, the OAuth requirements in this chapter also apply to OIDC.

The following roles are defined in OAuth:

* The OAuth client is the application that attempts to obtain an authorization for some server resources (e.g., by calling an API using the issued access token). The OAuth client is often a server-side application.
    * A confidential client is a client that is capable of maintaining the confidentiality of their credentials, to authenticate itself with the authorization server.
    * A public client does not have client credentials (is not capable of maintaining the confidentiality) and does not authenticate itself with the authorization server.
* The OAuth resource server (RS) is the server API exposing resources to OAuth clients.
* The OAuth authorization server (AS) is a server application which issues access tokens to Oauth clients. These access tokens represents authorizations for OAuth clients to access RS resources, either on behalf of an end-user or on the OAuth client's own behalf. The AS is often a separate application, but (if appropriate) it may be integrated in a suitable RS.
* The resource owner (RO) is an end-user which uses AS to grant to the client the authorizations to access RS on his behalf.

The following roles are defined in OIDC:

* The relying party (RP) is the client application requesting end-user authentication through the OpenID Provider. It assumes the role of an OAuth client.
* The OpenID provider (OP) is the identity provider (IdP) providing authentication to the relying party. It often assumes the role of an OAuth AS, but it is common with federated scenarios where the OAuth AS and OP are different server applications.

OAuth and OIDC were initially designed for third-party applications. Nowadays, they are often used by first-party applications as well. However, when used in first-party scenarios e. g. authentication and session management, the protocol adds some complexity which may introduce new security challenges.

OAuth and OIDC can be used for many kinds of applications, but the focus for ASVS and the requirements in this chapter is on web applications and APIs.

Since OAuth and OIDC can be considered to be logic on top of web technologies, general requirements from other chapters always apply and this chapter can not be taken out of context.

This chapter addresses best current practices for OAuth2 and OIDC aligned with specifications found at <https://oauth.net/2/> and <https://openid.net/developers/specs/>. Even if RFCs are considered to be mature, they are being updated frequently. Thus, it is important to align with the latest versions when applying the requirements in this chapter. See the references sections for more details.

Given the complexity of the area, it is vitally important for a secure OAuth or OIDC solution to use well-known industry standard authorization servers and apply the recommended security configuration.

Terminology is defined in Appendix A - Glossary and aligns with OAuth RFCs and OIDC specifications. Note that in this chapter OIDC terminology is only used for OIDC-specific requirements, otherwise OAuth terminology is used.

For the context of OAuth and OIDC the term token in this chapter refers to:

* Access tokens, shall only be consumed by RS and can either be reference tokens, validated using introspection, or self-contained tokens, validated using some key material.
* Refresh tokens, shall only be consumed by the authorization server who issued the token.
* OIDC ID Tokens, shall only be consumed by the client who issued the authorization flow (as a proof of user authentication).

Other kinds of tokens, like logout tokens, are not in the scope for this chapter.

The risk levels for some of the requirements in this chapter depend on whether the client is a confidential client or regarded as a public client. Since using strong client authentication mitigates many attack vectors, a few requirements might be relaxed when using a confidential client for L1 applications.

## V51.1 Generic OAuth and OIDC security

The requirements cover generic architectural requirements that apply to all applications using OAuth or OIDC, such as main architectural patterns available when building browser-based JavaScript applications that rely on OAuth or OIDC for accessing protected resources.

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.1.1** | [ADDED] Verify that tokens are only sent to components that strictly need them. For example, avoid having access or refresh tokens accessible for the frontend when they are only needed by the backend. | ✓ | ✓ | ✓ |
| **51.1.2** | [ADDED] Verify that the client only accepts values from the authorization server (such as the authorization code or ID token) if these values result from an authorization flow that was initiated by the same user agent session and transaction. This requires that client-generated secrets, such as the proof key for code exchange (PKCE) 'code_verifier', 'state' or OIDC 'nonce' are not guessable, are specific to the transaction, and are securely bound to both the client and the user agent session in which the transaction was started. | ✓ | ✓ | ✓ |

## V51.2 OAuth Client

The requirements cover responsibilities for OAuth client applications. The client can be for example a web server backend (often acting as a Backend For Frontend, BFF), a backend service integration, or a frontend Single Page Application (SPA, aka browser-based application).

In general backend clients are regarded as confidential clients and frontend clients are regarded as public clients. However, native application running on the end user device can be regarded as confidential when using OAuth dynamic client registration.

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.2.1** | [ADDED] Verify that, if the OAuth Client can interact with more than one authorization server, it has a defense against mix-up attacks. For example, it could require that the authorization server returns the 'iss' parameter value and validate it in the authorization response and the token response. | ✓ | ✓ | ✓ |
| **51.2.2** | [ADDED] Verify that, if the code flow is used, the OAuth Client has protection against cross-site request forgery (CSRF) attacks which trigger token requests, either by using proof key for code exchange (PKCE) functionality or checking the 'state' parameter that was sent in the authorization request. | ✓ | ✓ | ✓ |
| **51.2.3** | [ADDED] Verify that the OAuth Client only requests the required scopes (or other authorization parameters) in requests to the authorization server. | ✓ | ✓ | ✓ |

## V51.3 OAuth Resource Server

In the context of ASVS and this chapter, the resource server is an API. To provide secure access the resource server must:

* Validate the access token, according to token format and protocol specifications
* If valid, enforce authorization decisions based on information from the access token and granted permissions. For example, the resource server needs to verify that the client (acting on behalf of RO) is authorized to access the requested resource.

Thus the requirements listed here are OAuth or OIDC specific and should be performed after token integrity validation and before accepting the delegated authorization information from the token.

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.3.1** | [ADDED] Verify that the resource server prevents the use of stolen access tokens or replay of access tokens (from unauthorized parties) by requiring sender-constrained access tokens, either Mutual TLS for OAuth 2 or OAuth 2 Demonstration of Proof of Possession (DPoP). | | | ✓ |
| **51.3.2** | [ADDED] Verify that the resource server only accepts access tokens that are intended for use with that service (audience). The audience may be included in a structured access token (such as the 'aud' claim in JWT) or it can be checked using the token introspection endpoint. | ✓ | ✓ | ✓ |
| **51.3.3** | [ADDED] Verify that the resource server enforces authorization decisions based on claims from the access token that define delegated authorization. If claims such as 'sub', 'scope', and 'authorization_details' are present, they should be part of the decision. | ✓ | ✓ | ✓ |
| **51.3.4** | [ADDED] Verify that if an access control decision requires identifying a unique user from an access token (JWT or related token introspection response), the resource server identifies the user from claims that can not be reassigned to other users. Typically it means using a combination of 'iss' and 'sub' claims. | ✓ | ✓ | ✓ |

## V51.4 OAuth Authorization Server

These requirements cover responsibilities for OAuth authorization servers, including OpenID providers.

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.4.1** | [ADDED] Verify that, if the authorization server returns the authorization code, it can be used only once for a token request. | ✓ | ✓ | ✓ |
| **51.4.2** | [ADDED] Verify that the authorization code is short-lived. The maximum lifetime can be 10 minutes for L1 and L2 applications and 1 minute for L3 applications. | ✓ | ✓ | ✓ |
| **51.4.3** | [ADDED] Verify that, if the code grant is used, the authorization server mitigates authorization code interception attacks by requiring proof key for code exchange (PKCE). For authorization requests, the authorization server must require a valid 'code_challenge' value and must not accept 'code_challenge_method' value 'plain'. For a token request, it must require validation of the 'code_verifier' parameter. | ✓ | ✓ | ✓ |
| **51.4.4** | [ADDED] Verify that the authorization server mitigates refresh token replay attacks for public clients, preferably using sender-constrained refresh tokens (i.e., Demonstrating Proof of Possession (DPoP) or Certificate-Bound Access Tokens (mTLS)). For L1 applications only, refresh token rotation may be used instead. If refresh token rotation is used, verify that the authorization server invalidates the refresh token after usage and revokes all refresh tokens for that authorization if an already used and invalidated refresh token is provided. | ✓ | ✓ | ✓ |
| **51.4.5** | [ADDED] Verify that for a given client, the authorization server only allows the usage of grants that this client needs to use. Note that the grants 'token' (Implicit flow) and 'password' (Resource Owner Password Credentials flow) must no longer be used. | | ✓ | ✓ |
| **51.4.6** | [ADDED] Verify that the authorization server validates redirect URIs based on a client-specific allowlist of pre-registered URIs using exact string comparison. | ✓ | ✓ | ✓ |
| **51.4.7** | [ADDED] Verify that confidential client is authenticated for client-to-authorized server backchannel requests such as token requests, pushed authorization requests (PAR), token revocation requests, and token introspection requests. | ✓ | ✓ | ✓ |
| **51.4.8** | [ADDED] Verify that the authorization server configuration only assigns the required scopes to the OAuth Client. | ✓ | ✓ | ✓ |
| **51.4.9** | [ADDED] Verify that grant type 'code' is always used together with pushed authorization requests (PAR). | | | ✓ |
| **51.4.10** | [ADDED] Verify that the client is confidential and the authorization server requires the use of strong client authentication methods (based on public-key cryptography and resistant to replay attacks), i.e., 'mTLS' or 'private-key-jwt'. | | | ✓ |
| **51.4.11** | [ADDED] Verify that the authorization server issues only sender-constrained (Proof-of-Possession) access tokens, either using mTLS certificate binding or Demonstration of Proof of Possession (DPoP). | | | ✓ |
| **51.4.12** | [ADDED] Verify that for a given client, the authorization server only allows the 'response_mode' value that this client needs to use. For example by having the authorization server validate this value against the expected values or by using pushed authorization request (PAR) or JWT-secured authorization request (JAR). | ✓ | ✓ | ✓ |
| **51.4.13** | [ADDED] Verify that refresh tokens have an absolute expiration, including if sliding refresh token expiration is applied. | ✓ | ✓ | ✓ |
| **51.4.14** | [MODIFIED, MOVED FROM 3.5.1] Verify that refresh tokens and reference access tokens can be revoked by an authorized user. It can be achieved by using the authorization server user interface, or by a client that is using authorization server APIs for revocation. | | ✓ | ✓ |
| **51.4.15** | [ADDED] Verify that, for a server-side client (which is not executed on the end-user device), the authorization server ensures that the 'authorization_details' parameter value is from the client backend and that the user has not tampered with it. For example by requiring the usage of pushed authorization request (PAR) or JWT-secured authorization request (JAR). | | | ✓ |

## V51.5 OIDC Client

As the OIDC Relying Party acts as an OAuth client, the requirements from the section "OAuth Client" apply as well. Note that if using the 'id-token' flow (not the 'code' flow), then no access tokens are issued and requirements for OAuth clients are not applicable.

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.5.1** | [ADDED] Verify that the Client (as the relying party) mitigates ID token replay attacks. For example, by ensuring that the 'nonce' claim in the ID token matches the 'nonce' value sent in the authentication request to the OpenID provider (in OAuth2 refereed to as the authorization request sent to the authorization server). | ✓ | ✓ | ✓ |
| **51.5.2** | [ADDED] Verify that the Client uniquely identifies the user from ID token claims, usually the 'sub' claim, which cannot be reassigned to other users (for the scope of an identity provider). | ✓ | ✓ | ✓ |
| **51.5.3** | [ADDED] Verify that the client rejects attempts by a malicious authorization server to impersonate another authorization server through authorization server metadata. The client must reject authorization server metadata if the issuer URL in the authorization server metadata does not exactly match the pre-configured issuer URL expected by client. | ✓ | ✓ | ✓ |
| **51.5.4** | [ADDED] Verify that the client validates that the ID token is intended to be used for that client (audience) by checking that the 'aud' claim from the token is equal to the 'client_id' value for the client. | ✓ | ✓ | ✓ |

## V51.6 OpenID Provider

As OpenID Providers act as OAuth Authorization servers, the requirements from the section "OAuth Authorization Server" apply as well. Note that if using the id-token flow (not the code flow), no access tokens are issued and many of the requirements for OAuth AS are not applicable.

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.6.1** | [ADDED] Verify that the OpenID Provider only allows values 'code', 'ciba', 'id-token', or 'id-token code' for response mode. Note that 'code' is preferred over 'id-token code' (the OIDC Hybrid flow), and 'token' (any Implicit flow) must not be used. | | ✓ | ✓ |

## V51.7 Consent Management

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.7.1** | [ADDED] Verify that the authorization server ensures that the user consents to each authorization request. If the identity of the client cannot be assured, the authorization server must always explicitly prompt the user for consent. | | ✓ | ✓ |
| **51.7.2** | [ADDED] Verify that when the authorization server prompts for user consent, it presents sufficient and clear information about what is being consented to. When applicable this should include the nature of the requested authorizations (typically based on scope, resource server, rich authorization requests (RAR) authorization details), the identity of the authorized application and the lifetime of these authorizations. | | ✓ | ✓ |
| **51.7.3** | [ADDED] Verify that the user can review, modify and revoke consents which the user has granted through the authorization server. | | ✓ | ✓ |

## References

For more information on OAuth, please see:

* [oauth.net](https://oauth.net/)
* [OWASP Cheat Sheet: OAuth 2.0 Protocol Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

For OAuth-related requirements in ASVS following published and in draft status RFC-s are used:

* [RFC6749 The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
* [RFC6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)
* [RFC6819 OAuth 2.0 Threat Model and Security Considerations](https://datatracker.ietf.org/doc/html/rfc6819)
* [RFC7636 Proof Key for Code Exchange by OAuth Public Clients](https://datatracker.ietf.org/doc/html/rfc7636)
* [RFC9068 JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
* [RFC8628 OAuth 2.0 Device Authorization Grant](https://datatracker.ietf.org/doc/html/rfc8628)
* [RFC8707 Resource Indicators for OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc8707)
* [RFC9126 OAuth 2.0 Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126)
* [RFC9207 OAuth 2.0 Authorization Server Issuer Identification](https://datatracker.ietf.org/doc/html/rfc9207)
* [RFC9396 OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)
* [RFC9449 OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)
* [draft OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics)<!-- recheck on release -->
* [draft OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)<!-- recheck on release -->
* [draft The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-11)<!-- recheck on release -->

For more information on OpenID Connect, please see:

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.bitbucket.io/fapi/fapi-2_0-security-profile.html)<!-- recheck on release -->
