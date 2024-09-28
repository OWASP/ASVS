# V51 OAuth and OIDC

This chapter describes and summarizes the [best current security practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics#name-best-practices) for OAuth 2.0 as derived from its [RFC 6750](https://www.rfc-editor.org/info/rfc6750) and [6749](https://www.rfc-editor.org/info/rfc6749) for every OAuth implementor. OAuth became the standard for API protection and the basis for federated login using OpenID Connect. OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It enables clients to verify the identity of the end-user based on the authentication performed by an authorization server, as well as to obtain basic profile information about the end-user in an interoperable and REST-like manner.

There are various different personas in the OAuth process, described in more detail in the terminology section below. The requirements in this chapter are structured based on those personas as requirements for one persona may not be relevant for a different persona.

## V51.1 Generic OAuth and OIDC security

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.1.1** | [ADDED] Verify that tokens (such as ID tokens, access tokens and refresh tokens) can only be used for their intended purpose. For example, ID tokens can only be used to prove user authentication for the client. | ✓ | ✓ | ✓ |
| **51.1.2** | [ADDED] Verify that tokens are only sent to components that strictly need them. For example, avoid having access or refresh tokens accessible for the frontend when they are only needed by the backend. | ✓ | ✓ | ✓ |

## V51.2 OAuth Authorization Server

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.2.1** | [ADDED] Verify that, if the authorization server returns the authorization code, it can be used only once for a token request and it is only valid for up to 10 minutes. | ✓ | ✓ | ✓ |
| **51.2.2** | [ADDED] Verify that the replay of authorization codes into the authorization response is prevented either by using the PKCE flow or alternatively the OpenID Connect "nonce" parameter and the respective Claim in the ID Token. The PKCE challenge or OpenID Connect "nonce" must be transaction-specific and securely bound to the client and the user agent in which the transaction was started. | ✓ | ✓ | ✓ |
| **51.2.3** | [ADDED] Verify that, if the code grant is used, the authorization server mitigates authorization code interception attacks by requiring PKCE. For authorization requests, the authorization server must require a valid code_challenge value and must not accept code_challenge_method 'plain'. For a token request, it must require validation of the "code_verifier" parameter. | ✓ | ✓ | ✓ |
| **51.2.4** | [ADDED] Verify that refresh tokens are sender-constrained or use refresh token rotation to prevent token replay attacks. Refresh token rotation prevents usage in the event of a compromised refresh token. Sender-constrained refresh tokens cryptographically binds the refresh token to a particular Client. | ✓ | ✓ | ✓ |
| **51.2.5** | [ADDED] Verify that for a given client, the authorization server only allows the usage of grants that this client needs to use. Note that the grants 'token' (Implicit flow) and 'password' (Resource Owner Password Credentials flow) should no longer be used. | ✓ | ✓ | ✓ |
| **51.2.6** | [ADDED] Verify that the authorization server validates redirect URIs based on a client-specific allowlist of pre-registered URIs using exact string comparison. | ✓ | ✓ | ✓ |
| **51.2.7** | [ADDED] Verify that confidential client is authenticated for client-to-authorized server backchannel requests such as token requests, PAR requests, token revocation requests, and token introspection requests. | ✓ | ✓ | ✓ |
| **51.2.8** | [ADDED] Verify that grant type 'code' is always used together with pushed authorization requests (PAR). | | | ✓ |

## V51.3 OAuth Client

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.3.1** | [ADDED] Verify that when an OAuth Client can interact with more than one authorization server, Clients should verify that the issuer "iss" parameter value is what it expected from the authorization response to prevent against mix-up attacks. In the absence of an "iss" parameter, Clients may instead use distinct redirect URIs to identify authorization endpoints and token endpoints. | ✓ | ✓ | ✓ |
| **51.3.2** | [ADDED] Verify that the Client is using the PKCE flow or alternatively the OpenID Connect "nonce" parameter and the respective Claim in the ID Token. | ✓ | ✓ | ✓ |
| **51.3.3** | [ADDED] Verify that Clients are utilizing the "scope" and "resource" parameters, respectively to determine the resource server they want to access. | ✓ | ✓ | ✓ |
| **51.3.4** | [ADDED] Verify that Clients are utilizing the "scope" and "authorization_details" parameters to determine the related resources and actions the access token are restricted to. | ✓ | ✓ | ✓ |
| **51.3.5** | [ADDED] Verify that, if the code flow is used, the OAuth Client has protection against CSRF attacks which trigger token requests, either by using PKCE functionality or checking the state parameter that was sent in the authorization request. | ✓ | ✓ | ✓ |

## V51.4 OAuth Resource Server

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.4.1** | [ADDED] Verify that resource servers implement sender-constrained access token mechanisms to mitigate token replay risks. This is achieved by mandating Mutual TLS for OAuth 2.0 or OAuth Demonstration of Proof of Possession (DPoP), using the client secret provided at client registration. | ✓ | ✓ | ✓ |
| **51.4.2** | [ADDED] Verify that access tokens are restricted to certain resource servers (audience restriction), preferably to a single resource server. Every resource server is obliged to verify, for every request, whether the access token sent with that request was meant to be used for that particular resource server. If not, the resource server must refuse to serve the respective request. | ✓ | ✓ | ✓ |
| **51.5.3** | [ADDED] Verify that access tokens are restricted to certain resources and actions on resource servers or resources. Every Resource Server is obliged to verify, for every request, whether the access token sent with that request was meant to be used for that particular action on the particular resource. If not, the resource server must refuse to serve the respective request. | ✓ | ✓ | ✓ |

## V51.5 OIDC Client

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.5.1** | [ADDED] Verify that the Client (as the Relying Party) mitigates ID Token replay attacks. For example, by ensuring that the nonce claim in the ID Token matches the nonce value sent in the Authentication Request to the OpenID Provider (in OAuth2 refereed to as the Authorization request sent to the Authorization Server). | ✓ | ✓ | ✓ |

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

## OAuth 2.0 Basics

In OpenID Connect flows, the "nonce" parameter provides CSRF protection. Otherwise, one-time user CSRF tokens carried in the "state" parameter that are securely bound to the user agent must be used for CSRF protection.

### PKCE - Proof Key for Code Exchange Mechanism / Authorization Code Grant

OAuth 2.0 public clients utilizing the Authorization Code Grant are susceptible to the authorization code interception attack. Proof Key for Code Exchange (PKCE, pronounced "pixy") is the technique used to mitigate against the threat of authorization code interception attack.

Originally, PKCE is intended to be used solely focused on securing native apps, but then it became a deployed OAuth feature. It does not only protect against authorization code injection attacks, but also protects authorization codes created for public clients as PKCE ensures that the attacker cannot redeem a stolen authorization code at the token endpoint of the authorization server without knowledge of the code_verifier.

The PKCE challenge or OpenID Connect "nonce" must be transaction-specific and securely bound to the client and the user agent in which the transaction was started.

### Token Replay Prevention

Preventing token replay attacks is of essential importance in using and implementing OAuth 2.0.

### Access Token Privilege Restriction

Restricting token privileges ensures a Client is granted the proper access to a specific resource.

### Resource Owner Password Credentials Grant

Aside from this grant type can leak credentials in more places than just the Authorization Server, adapting the Resource Owner password credentials grant to two-factor authentication, authentication with cryptographic credentials (e.g. WebCrypto, WebAuthn), and authentication processes that require multiple steps can be hard or impossible. This grant type is not recommended in general due to security concerns. Instead, use the authorization code grant with PKCE. This grant type is omitted from the OAuth 2.1 specification.

## OAuth 2.0 References

For more information, see also:

* RFC 6749 - The OAuth 2.0 Authorization Framework: <https://www.rfc-editor.org/info/rfc6749>
* RFC 6750 - The OAuth 2.0 Authorization Framework: Bearer Token Usage: <https://www.rfc-editor.org/info/rfc6750>
* OAuth 2.0 Best Practices: <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics#name-best-practices>
* Mix-up attacks: <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-18#mix_up>
* RFC9207 - OAuth 2.0 Authorization Server Issuer Identifier in Authorization Response: <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-iss-auth-resp-00>
* Other Countermeasures for Mix-up attacks: <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-18#section-2.1-6>
