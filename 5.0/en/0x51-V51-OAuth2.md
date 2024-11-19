# V51 OAuth and OIDC

## Control Objective

OAuth2 has become industry standard for delegating API authorization and also the basis for end-user authentication using OpenID Connect (OIDC), where OIDC is an identity layer on top of OAuth2. Thus, all OAuth2 verifications in this chapter also apply to OIDC, while OAuth2 can be used without OIDC verifications.

OAuth was initially made for third-party access delegation but it is often nowadays used as a first-party solution, including as a replacement for session management. Due to the complexity, it may introduce the risk of overengineering and causing new security challenges.

OAuth and OIDC are logic on top of web technologies and therefore general requirements from other chapters always apply and this chapter can not be taken out of context.
This chapter addresses best current practices for OAuth2 and OIDC aligned with specifications found at <https://oauth.net/2/> and <https://openid.net/developers/specs/>. Even if RFCs are considered to be mature, they are being updated frequently. Thus, it is important to align with the latest versions when applying the requirements in this chapter, see the references sections for more details.

Given the complexity of the area, it is vitally important for a secure OAuth or OIDC solution to use well-known industry standard authorization servers and apply the recommended security configuration.

## V51.1 Generic OAuth and OIDC security

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.1.1** | [ADDED] Verify that tokens are only sent to components that strictly need them. For example, avoid having access or refresh tokens accessible for the frontend when they are only needed by the backend. | ✓ | ✓ | ✓ |
| **51.1.2** | [ADDED] Verify that the client only accepts values from the authorization server (such as the authorization code or ID token) if these values result from an authorization flow that was initiated by the same user agent session and transaction. This requires that client-generated secrets, such as the proof key for code exchange (PKCE) 'code_verifier', 'state' or OIDC 'nonce' are not guessable, are specific to the transaction, and are securely bound to both the client and the user agent session in which the transaction was started. | ✓ | ✓ | ✓ |

## V51.2 OAuth Authorization Server

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.2.1** | [ADDED] Verify that, if the authorization server returns the authorization code, it can be used only once for a token request. | ✓ | ✓ | ✓ |
| **51.2.2** | [ADDED] Verify that the authorization code is short-lived. The maximum lifetime can be 10 minutes for L1 and L2 applications and 1 minute for L3 applications. | ✓ | ✓ | ✓ |
| **51.2.3** | [ADDED] Verify that, if the code grant is used, the authorization server mitigates authorization code interception attacks by requiring proof key for code exchange (PKCE). For authorization requests, the authorization server must require a valid 'code_challenge' value and must not accept 'code_challenge_method' value 'plain'. For a token request, it must require validation of the 'code_verifier' parameter. | ✓ | ✓ | ✓ |
| **51.2.4** | [ADDED] Verify that the authorization server mitigates refresh token replay attacks for public clients, preferably using sender-constrained refresh tokens (i.e. Demonstrating Proof of Possession (DPoP) or Certificate-Bound Access Tokens (mTLS)). For L1 applications only, refresh token rotation may be used instead. If refresh token rotation is used, verify that the authorization server invalidates the refresh token after usage and revokes all refresh tokens for that authorization if an already used and invalidated refresh token is provided. | ✓ | ✓ | ✓ |
| **51.2.5** | [ADDED] Verify that for a given client, the authorization server only allows the usage of grants that this client needs to use. Note that the grants 'token' (Implicit flow) and 'password' (Resource Owner Password Credentials flow) should no longer be used. | ✓ | ✓ | ✓ |
| **51.2.6** | [ADDED] Verify that the authorization server validates redirect URIs based on a client-specific allowlist of pre-registered URIs using exact string comparison. | ✓ | ✓ | ✓ |
| **51.2.7** | [ADDED] Verify that confidential client is authenticated for client-to-authorized server backchannel requests such as token requests, pushed authorization requests (PAR), token revocation requests, and token introspection requests. | ✓ | ✓ | ✓ |
| **51.2.8** | [ADDED] Verify that the authorization server configuration only assigns the required scopes to the OAuth Client. | ✓ | ✓ | ✓ |
| **51.2.9** | [ADDED] Verify that grant type 'code' is always used together with pushed authorization requests (PAR). | | | ✓ |
| **51.2.10** | [ADDED] Verify that the client is confidential and the authorization server requires the use of strong client authentication methods (based on public-key cryptography and resistant to replay attacks), i. e. 'mTLS' or 'private-key-jwt'. | | | ✓ |
| **51.2.11** | [ADDED] Verify that the authorization server issues only sender-constrained (Proof-of-Posession) access tokens, either using mTLS certificate binding or Demonstration of Proof of Possession (DPoP). | | | ✓ |
| **51.2.12** | [ADDED] Verify that for a given client, the authorization server only allows the 'response_mode' value that this client needs to use. For example by having the authorization server validate this value against the expected values or by using pushed authorization request (PAR) or JWT-secured authorization request (JAR). | ✓ | ✓ | ✓ |
| **51.2.13** | [ADDED] Verify that refresh tokens have an absolute expiration, including if sliding refresh token expiration is applied. | ✓ | ✓ | ✓ |
| **51.2.14** | [MODIFIED, MOVED FROM 3.5.1] Verify that refresh tokens and reference access tokens can be revoked by an authorized user. It can be achieved by using the authorization server user interface, or by a client that is using authorization server APIs for revocation. | | ✓ | ✓ |
| **51.2.15** | [ADDED] Verify that, for a server-side client (which is not executed on the end-user device), the authorization server ensures that the 'authorization_details' parameter value is from the client backend and that the user has not tampered with it. For example by requiring the usage of pushed authorization request (PAR) or JWT-secured authorization request (JAR). | | | ✓ |

## V51.3 OAuth Client

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.3.1** | [ADDED] Verify that, if the OAuth Client can interact with more than one authorization server, it has a defense against mix-up attacks. For example, it could require that the authorization server returns the 'iss' parameter value and validate it in the authorization response and the token response. | ✓ | ✓ | ✓ |
| **51.3.2** | [ADDED] Verify that, if the code flow is used, the OAuth Client has protection against cross-site request forgery (CSRF) attacks which trigger token requests, either by using proof key for code exchange (PKCE) functionality or checking the 'state' parameter that was sent in the authorization request. | ✓ | ✓ | ✓ |
| **51.3.3** | [ADDED] Verify that the OAuth Client only requests the required scopes (or other authorization parameters) in requests to the authorization server. | ✓ | ✓ | ✓ |

## V51.4 OAuth Resource Server

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.4.1** | [ADDED] Verify that the resource server prevents the use of stolen access tokens or replay of access tokens (from unauthorized parties) by requiring sender-constrained access tokens, either Mutual TLS for OAuth 2 or OAuth 2 Demonstration of Proof of Possession (DPoP). | | | ✓ |
| **51.4.2** | [ADDED] Verify that the resource server ensures that the access token is intended to be used with that server (audience). For an access token in JWT format or when using a JWT from token introspection, this can be done by checking the 'aud' claim. | ✓ | ✓ | ✓ |
| **51.4.3** | [ADDED] Verify that access tokens are restricted to certain resources and actions on resource servers or resources. Every Resource Server is obliged to verify, for every request, whether the access token sent with that request was meant to be used for that particular action on the particular resource. If not, the resource server must refuse to serve the respective request. | ✓ | ✓ | ✓ |
| **51.4.4** | [ADDED] Verify that if an access control decision requires identifying a unique user from an access token (JWT or related token introspection response), the resource server identifies the user from claims that can not be reassigned to other users. Typically it means using a combination of 'iss' and 'sub' claims. | ✓ | ✓ | ✓ |

## V51.5 OIDC Client

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.5.1** | [ADDED] Verify that the Client (as the relying party) mitigates ID token replay attacks. For example, by ensuring that the 'nonce' claim in the ID token matches the 'nonce' value sent in the authentication request to the OpenID provider (in OAuth2 refereed to as the authorization request sent to the authorization server). | ✓ | ✓ | ✓ |
| **51.5.2** | [ADDED] Verify that the Client uniquely identifies the user from ID token claims, usually the 'sub' claim, which cannot be reassigned to other users (for the scope of an identity provider). | ✓ | ✓ | ✓ |
| **51.5.3** | [ADDED] Verify that the client rejects attempts by a malicious authorization server to impersonate another authorization server through authorization server metadata. The client must reject authorization server metadata if the issuer URL in the authorization server metadata does not exactly match the pre-configured issuer URL expected by client. | ✓ | ✓ | ✓ |
| **51.5.4** | [ADDED] Verify that the client validates that the ID token is intended to be used for that client (audience) by checking that the 'aud' claim from the token is equal to the 'client_id' value for the client. | ✓ | ✓ | ✓ |

## V51.5 OIDC OpenID Provider

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.6.1** | [ADDED] Verify that the OpenID Provider only allows values 'code', 'ciba', 'id-token', or 'id-token code' for response mode. Note that 'code' is preferred over 'id-token code' (the OIDC Hybrid flow), and 'token' (any Implicit flow) should not be used. | ✓ | ✓ | ✓ |

## Terminology

This chapter uses the terms "Access tokens", "Refresh tokens", "Client", "Authorization Server", "Resource Owner", and "Resource Server" as defined by OAuth 2.0 RFC 6749. As such this chapter defines the following terms:

### Access tokens

Access tokens provide an abstraction, replacing different authorization constructs (e.g., username and password, assertion) for a single token understood by the resource server. This abstraction enables issuing access tokens valid for a short time period, as well as removing the resource server's need to understand a wide range of authentication schemes.

### Refresh tokens

Refresh tokens are credentials used to obtain access tokens. These are issued to the client by the authorization server and are used to obtain a new access token when the current access token becomes invalid or expires, or to obtain additional access tokens with identical or narrower scope (access tokens may have a shorter lifetime and fewer permissions than authorized by the resource owner).

### Client

A Client generally refers to an application making protected resource requests on behalf of the resource owner and with its authorization. The term "client" does not imply any particular implementation characteristics (e.g., whether the application executes on a server, a desktop, or other devices).

### Authorization Server (AS)

The Authorization Server refers to the server or entity issuing access tokens to the client after successfully authenticating the resource owner and obtaining authorization.

### Resource Owner (RO)

The Resource Owner refers to an entity capable of granting access to a protected resource. When the resource owner is a person, it is referred to as an end-user.

### Resource Server (RS)

The Resource Server refers to the server hosting the protected resources, capable of accepting and responding to protected resource requests using access tokens.

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
