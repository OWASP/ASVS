## V3.8 OAuth 2.0 Protocol

This section describes and summarizes the [best current security practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics#name-best-practices) for OAuth 2.0 as derived from its [RFC 6750](https://www.rfc-editor.org/info/rfc6750) and [6749](https://www.rfc-editor.org/info/rfc6749) for every OAuth implementor. OAuth became the standard for API protection and the basis for federated login using OpenID Connect. OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It enables clients to verify the identity of the end-user based on the authentication performed by an authorization server, as well as to obtain basic profile information about the end-user in an interoperable and REST-like manner.

There are various different personas in the OAuth process, described in more detail in the terminology section below. The requirements in this chapter are structured based on those personas as requirements for one persona may not be relevant for a different persona.

## Terminology

* Access tokens - provides an abstraction, replacing different authorization constructs (e.g., username and password, assertion) for a single token understood by the resource server. This abstraction enables issuing access tokens valid for a short time period, as well as removing the resource server's need to understand a wide range of authentication schemes.
* Refresh tokens - are credentials used to obtain access tokens. These are issued to the client by the authorization server and are used to obtain a new access token when the current access token becomes invalid or expires, or to obtain additional access tokens with identical or narrower scope (access tokens may have a shorter lifetime and fewer permissions than authorized by the resource owner).
* Client - generally refers to an application making protected resource requests on behalf of the resource owner and with its authorization. The term "client" does not imply any particular implementation characteristics (e.g., whether the application executes on a server, a desktop, or other devices).
* Authorization Server (AS) - refers to the server issuing access tokens to the client after successfully authenticating the resource owner and obtaining authorization.
* Resource Owner (RO) - refers to an entity capable of granting access to a protected resource. When the resource owner is a person, it is referred to as an end-user.
* Resource Server (RS) - refers to the server hosting the protected resources, capable of accepting and responding to protected resource requests using access tokens.

## OAuth 2.0 Basics

In OpenID Connect flows, the "nonce" parameter provides CSRF protection. Otherwise, one-time user CSRF tokens carried in the "state" parameter that are securely bound to the user agent must be used for CSRF protection.

### PKCE - Proof Key for Code Exchange Mechanism / Authorization Code Grant

OAuth 2.0 public clients utilizing the Authorization Code Grant are susceptible to the authorization code interception attack. Proof Key for Code Exchange (PKCE, pronounced "pixy") is the technique used to mitigate against the threat of authorization code interception attack.

Originally, PKCE is intended to be used solely focused on securing native apps, but then it became a deployed OAuth feature. It does not only protect against authorization code injection attacks, but also protects authorization codes created for public clients as PKCE ensures that the attacker cannot redeem a stolen authorization code at the token endpoint of the authorization server without knowledge of the code_verifier.

### Token Replay Prevention

Preventing token replay attacks is of essential importance in using and implementing OAuth 2.0.

### Access Token Privilege Restriction

Restricting token privileges ensures a Client is granted the proper access to a specific resource.

### Resource Owner Password Credentials Grant

Aside from this grant type can leak credentials in more places than just the Authorization Server, adapting the Resource Owner password credentials grant to two-factor authentication, authentication with cryptographic credentials (e.g. WebCrypto, WebAuthn) and authentication processes that require multiple steps can be hard or impossible.

## V51.1 Authorization Server

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.1.1** | [ADDED] Verify that the Authorization Server supports CSRF protection either using the mechanism provided by PKCE, the "nonce" parameter or the "state" parameter. | ✓ | ✓ | ✓ |
| **51.1.2** | [ADDED] Verify that the replay of authorization codes into the authorization response is prevented either by using the PKCE flow or alternatively the OpenID Connect "nonce" parameter and the respective Claim in the ID Token. The PKCE challenge or OpenID Connect "nonce" must be transaction-specific and securely bound to the client and the user agent in which the transaction was started.  | ✓ | ✓ | ✓ |
| **51.1.3** | [ADDED] Verify that Authorization Servers are mitigating PKCE Downgrade Attacks by ensuring a token request containing a "code_verifier" parameter is accepted only if a "code_challenge" parameter was present in the authorization request. | ✓ | ✓ | ✓ |
| **51.1.4** | [ADDED] Verify that refresh tokens are sender-constrained or use refresh token rotation. | ✓ | ✓ | ✓ |
| **51.1.5** | [ADDED] Verify that the Authorization Server publishes the element "code_challenge_methods_supported" in their Authorization Server metadata containing the supported PKCE challenge methods. | ✓ | ✓ | ✓ |

## V51.2 OAuth Client

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.2.1** | [ADDED] Verify that when an OAuth Client can interact with more than one Authorization Server, Clients should verify that the issuer "iss" parameter value is what it expected from the authorization response to prevent against mix-up attacks. [reference link for Mix-up attacks: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-18#mix_up] In the absence of "iss" parameter, Clients may instead use distinct redirect URIs to identify authorization endpoints and token endpoints.  | ✓ | ✓ | ✓ |
| **51.2.2** | [ADDED] Verify that the Client is using the PKCE flow or alternatively the OpenID Connect "nonce" parameter and the respective Claim in the ID Token. The PKCE challenge or OpenID Connect "nonce" must be transaction-specific and securely bound to the client and the user agent in which the transaction was started.  | ✓ | ✓ | ✓ |
| **51.2.3** | [ADDED] Verify that if a Client sends a valid PKCE "code_challenge" parameter in the authorization request, the Authorization Server enforces the correct usage of "code_verifier" at the token endpoint. | ✓ | ✓ | ✓ |
| **51.2.4** | [ADDED] Verify that Clients are utilizing the parameters "scope" and "resource", respectively to determine the Resource Server they want to access. | ✓ | ✓ | ✓ |
| **51.2.5** | [ADDED] Verify that Clients are utilizing the parameters "scope" and "authorization_details" to determine the requested/related resources and/or actions the access token are restricted to. | ✓ | ✓ | ✓ |

## V51.3 Resource Server

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.3.1** | [ADDED] Verify that Resource Servers are using mechanisms for sender-constraining access tokens to prevent token replay, such as Mutual TLS for OAuth 2.0 or OAuth Demonstration of Proof of Possession (DPoP).  | ✓ | ✓ | ✓ |
| **51.3.2** | [ADDED] Verify that access tokens are restricted to certain Resource Servers (audience restriction), preferably to a single Resource Server. Every Resource Server is obliged to verify, for every request, whether the access token sent with that request was meant to be used for that particular Resource Server. If not, the Resource Server must refuse to serve the respective request. | ✓ | ✓ | ✓ |
| **51.3.3** | [ADDED] Verify that access tokens are restricted to certain resources and actions on Resource Servers or resources. Every Resource Server is obliged to verify, for every request, whether the access token sent with that request was meant to be used for that particular action on the particular resource. If not, the Resource Server must refuse to serve the respective request. | ✓ | ✓ | ✓ |

## V51.4 Resource Owner

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **51.4.1** | [ADDED] Verify that the Resource Owner password credentials grant is not used. This grant type insecurely exposes the credentials of the Resource Owner to the client, increasing the attack surface of the application.  | ✓ | ✓ | ✓ |

## Mapping

This mapping shows which OAuth 2.0 requirements belongs to which OAuth-specific subsection from the original requirements structure that was proposed here: https://github.com/OWASP/ASVS/blob/5375e96bc99c47fe7b3430407cd469d0f9896180/5.0/en/0x12-V3-Session-management.md#v38-oauth-20-protocol

| Section | Requirements |
| :--- | :--- |
| OAuth 2.0 Essential Basics | 51.1.1, 51.1.2 |
| PCKE | 51.1.3, 51.1.4, 51.1.5, 51.3.1 |
| Token Replay | 51.2.1, 51.2.2 |
| Access Restriction | 51.2.3, 51.2.4 |
| Resource Owner | 51.2.5 |

## OAuth 2.0 References

* Original RFC: https://www.rfc-editor.org/info/rfc6750 & : https://www.rfc-editor.org/info/rfc6749
* OAuth 2.0 Best Practices: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics#name-best-practices
* Mix-up attacks: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-18#mix_up
* RFC9207 [I-D.ietf-oauth-iss-auth-resp]: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-18#section-2.1-4
* & [I-D.ietf-oauth-iss-auth-resp]: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-iss-auth-resp-00
* Other Countermeasures for Mix-up attacks: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-18#section-2.1-6

## References

For more information, see also:

* [OAuth 2.0 RFC](https://www.rfc-editor.org/info/rfc6749)
* [OAuth RFC](https://www.rfc-editor.org/info/rfc6750)
* [OAuth 2.0 Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics#name-best-practices)
