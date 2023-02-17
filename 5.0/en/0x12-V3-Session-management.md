# V3 Session Management

## Control Objective

One of the core components of any web-based application or stateful API is the mechanism by which it controls and maintains the state for a user or device interacting with it. Session management changes a stateless protocol to stateful, which is critical for differentiating different users or devices.

Ensure that a verified application satisfies the following high-level session management requirements:

* Sessions are unique to each individual and cannot be guessed or shared.
* Sessions are invalidated when no longer required and timed out during periods of inactivity.

As previously noted, these requirements have been adapted to be a compliant subset of selected NIST SP 800-63B controls, focused around common threats and commonly exploited authentication weaknesses. Previous verification requirements have been retired, de-duped, or in most cases adapted to be strongly aligned with the intent of mandatory [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) requirements.

## V3.1 Fundamental Session Management Security

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.1.1** | [DELETED, MERGED TO 8.3.1] | | | | | |
| **3.1.2** | [ADDED] Verify that the application performs all session token verification using a trusted, back-end service. | ✓ | ✓ | ✓ | 603 | |
| **3.1.3** | [MODIFIED, MOVED FROM 3.5.2, LEVEL L2 > L1] Verify that the application uses either cryptographically signed or opaque tokens for session management. Static API secrets and keys should be avoided. | ✓ | ✓ | ✓ | 798 | 7.1 |

## V3.2 Session Binding

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.2.1** | [MODIFIED] Verify the application generates a new session token on user authentication, including re-authentication, and terminates the current session token. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 384 | 7.1 |
| **3.2.2** | [MODIFIED] Verify that opaque session tokens possess at least 128 bits of entropy. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 331 | 7.1 |
| **3.2.3** | [DELETED, MERGED TO 8.2.2] | | | | | |
| **3.2.4** | [MODIFIED] Verify that opaque session tokens are generated using a secure random function. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 330 | 7.1 |

TLS or another secure transport channel is mandatory for session management. This is covered in the Communications Security chapter.

## V3.3 Session Termination

Session timeouts have been aligned with NIST SP 800-63, which permits much longer session timeouts than traditionally permitted by security standards. Organizations should review the table below, and if a longer time out is desirable based on the application's risk, the NIST value should be the upper bounds of session idle timeouts.

L1 in this context is IAL1/AAL1, L2 is IAL2/AAL3, L3 is IAL3/AAL3. For IAL2/AAL2 and IAL3/AAL3, the shorter idle timeout is, the lower bound of idle times for being logged out or re-authenticated to resume the session.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.3.1** | [MODIFIED] Verify that logout and expiration invalidate the session token, such that the back button or a downstream relying party cannot resume an authenticated session. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 613 | 7.1 |
| **3.3.2** | [MODIFIED, SPLIT TO 3.3.7] Verify that there is an absolute maximum session lifetime such that re-authentication is required at least every 30 days for L1 applications or every 12 hours for L2 and L3 applications. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 613 | 7.2 |
| **3.3.3** | [MODIFIED, LEVEL L2 > L1] Verify that the application gives the option to terminate all other active sessions after a successful change or removal of any authentication factor (including password change via reset or recovery and, if present, an MFA settings update). This must be effective across the application, federated login (if present), and any relying parties. | ✓ | ✓ | ✓ | 613 | |
| **3.3.4** | Verify that users are able to view and (having re-entered login credentials) log out of any or all currently active sessions and devices. | | ✓ | ✓ | 613 | 7.1 |
| **3.3.5** | [ADDED] Verify that all pages that require authentication have easy and visible access to logout functionality. | ✓ | ✓ | ✓ | | |
| **3.3.6** | [ADDED] Verify that all active sessions are revoked when a user account is disabled or deleted (such as an employee leaving the company). | ✓ | ✓ | ✓ | 613 | |
| **3.3.7** | [ADDED, SPLIT FROM 3.3.2] Verify that re-authentication is required after 30 minutes of inactivity for L2 applications or after 15 minutes of inactivity for L3 applications. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 613 | 7.2 |

## V3.4 Cookie-based Session Management

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.4.1** | Verify that cookie-based session tokens have the 'Secure' attribute set. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 614 | 7.1.1 |
| **3.4.2** | [MODIFIED] Verify that cookie-based session tokens are not readable by client-side scripts. The session token cookie should have the 'HttpOnly' attribute set and the session token value should only be transferred to the client via the Set-Cookie header. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1004 | 7.1.1 |
| **3.4.3** | Verify that cookie-based session tokens utilize the 'SameSite' attribute to limit exposure to cross-site request forgery attacks. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1275 | 7.1.1 |
| **3.4.4** | Verify that cookie-based session tokens use the "__Host-" prefix so cookies are only sent to the host that initially set the cookie. | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.5** | [GRAMMAR] Verify that if the application is published under a domain name with other applications that set or use session cookies that might disclose the session cookies, it sets the path attribute in cookie-based session tokens using the most precise path possible. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |

## V3.5 Token-based Session Management

Token-based session management includes JWT, OAuth, SAML, and API keys. Of these, API keys are known to be weak and should not be used in new code. JWTs and SAML tokens are examples of stateless session tokens. All checks noted below should be enforced by a trusted, back-end service as noted above.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.5.1** | [GRAMMAR] Verify that the application allows users to revoke OAuth tokens that form trust relationships with linked applications. | | ✓ | ✓ | 290 | 7.1.2 |
| **3.5.2** | [MOVED TO 3.1.3] | | | | | |
| **3.5.3** | [MODIFIED, LEVEL L2 > L1] Verify that stateless session tokens make use of a digital signature to protect against tampering and this is checked before processing it further. | ✓ | ✓ | ✓ | 345 | |
| **3.5.4** | [ADDED] Verify that stateless tokens are checked for expiration before processing them further. | ✓ | ✓ | ✓ | 613 | |
| **3.5.5** | [ADDED] Verify that only allow-listed signing algorithms are allowed for a stateless token. | ✓ | ✓ | ✓ | 757 | |
| **3.5.6** | [ADDED] Verify that other, security-sensitive attributes of a stateless token are being verified. For example, in a JWT this may include issuer, subject, and audience. | ✓ | ✓ | ✓ | 287 | |
| **3.5.7** | [ADDED] Verify that all active stateless tokens, which are being relied upon for access control decisions, are revoked when admins change the entitlements or roles of the user. | ✓ | ✓ | ✓ | 613 | |

## V3.6 Federated Re-authentication

This section relates to those writing Relying Party (RP) or Credential Service Provider (CSP) code. If relying on code implementing these features, ensure that these issues are handled correctly.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.6.1** | Verify that Relying Parties (RPs) specify the maximum authentication time to Credential Service Providers (CSPs) and that CSPs re-authenticate the user if they haven't used a session within that period. | | | ✓ | 613 | 7.2.1 |
| **3.6.2** | Verify that Credential Service Providers (CSPs) inform Relying Parties (RPs) of the last authentication event, to allow RPs to determine if they need to re-authenticate the user. | | | ✓ | 613 | 7.2.1 |

## V3.7 Defenses Against Session Management Exploits

There are a small number of session management attacks, some related to the user experience (UX) of sessions. Previously, based on ISO 27002 requirements, the ASVS has required blocking multiple simultaneous sessions. Blocking simultaneous sessions is no longer appropriate, not only as modern users have many devices or the app is an API without a browser session, but in most of these implementations, the last authenticator wins, which is often the attacker. This section provides leading guidance on deterring, delaying and detecting session management attacks using code.

### Description of the half-open Attack

In early 2018, several financial institutions were compromised using what the attackers called "half-open attacks". This term has stuck in the industry. The attackers struck multiple institutions with different proprietary code bases, and indeed it seems different code bases within the same institutions. The half-open attack is exploiting a design pattern flaw commonly found in many existing authentication, session management and access control systems.

Attackers start a half-open attack by attempting to lock, reset, or recover a credential. A popular session management design pattern re-uses user profile session objects/models between unauthenticated, half-authenticated (password resets, forgot username), and fully authenticated code. This design pattern populates a valid session object or token containing the victim's profile, including password hashes and roles. If access control checks in controllers or routers do not correctly verify that the user is fully logged in, the attacker will be able to act as the user. Attacks could include changing the user's password to a known value, updating the email address to perform a valid password reset, disabling multi-factor authentication or enrolling a new MFA device, revealing or changing API keys, and so on.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.7.1** | [MODIFIED] Verify that the application requires re-authentication or secondary verification before allowing highly sensitive transactions or modifications to account profile or authentication settings. | ✓ | ✓ | ✓ | 306 | |



## V3.8 OAuth 2.0 Protocol

This section describes the best current security practices for OAuth 2.0 as derived from its RFC. OAuth became the standard for API protection and the basis for federated login using OpenID Connect. OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It enables clients to verify the identity of the end-user based on the authentication performed by an authorization server, as well as to obtain basic profile information about the end-user in an interoperable and REST-like manner. 

## Terminology: 

* Access tokens - provides an abstraction, replacing different authorization constructs (e.g., username and password, assertion) for a single token understood by the resource server. This abstraction enables issuing access tokens valid for a short time period, as well as removing the resource server's need to understand a wide range of authentication schemes. 
* Refresh tokens - are credentials used to obtain access tokens. These are issued to the client by the authorization server and are used to obtain a new access token when the current access token becomes invalid or expires, or to obtain additional access tokens with identical or narrower scope (access tokens may have a shorter lifetime and fewer permissions than authorized by the resource owner). 
* Client - generally refers to an application making protected resource requests on behalf of the resource owner and with its authorization. The term "client" does not imply any particular implementation characteristics (e.g., whether the application executes on a server, a desktop, or other devices). 
* Authorization Server (AS) - refers to the server issuing access tokens to the client after successfully authenticating the resource owner and obtaining authorization.
* Resource Owner (RO) - refers to an entity capable of granting access to a protected resource. When the resource owner is a person, it is referred to as an end-user. 
* Resource Server (RS) - refers to the server hosting the protected resources, capable of accepting and responding to protected resource requests using access tokens. 


## OAuth 2.0 Essential Basics

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **3.8.1** | [ADDED] Verify that Clients and Authorization Server must not expose URLs that forward the user's browser to arbitrary URIs obtained from a query parameter ("open redirectors") which can enable exfiltration of authorization codes and access tokens.  | ✓ | ✓ | ✓ |
| **3.8.2** | [ADDED] Verify Clients have ensured that the Authorization Server supports PKCE may rely on the CRSF protection provided by PKCE. In OpenID Connect flows, the "nonce" parameter provides CSRF protection. Otherwise, one-time user CSRF tokens carried in the "state" parameter that are securely bound to the user agent must be used for CSRF protection.  | ✓ | ✓ | ✓ |
| **3.8.3** | [ADDED] Verify that when an OAuth Client can interact with more than one Authorization Server, Clients should use the issuer "iss" parameter as a countermeasure, or alternatively based on an "iss" value in the authorization response (such as the "iss" Claim in the ID Token in OpenID) | ✓ | ✓ | ✓ |
| **3.8.4** | [ADDED] Verify that when the other countermeasure options for OAuth clients interacting with more than one Authorization Servers are absent, Clients may instead use distinct redirect URIs to identify authorization endpoints and token endpoints.  | ✓ | ✓ | ✓ |
| **3.8.5** | [ADDED] Verify that an Authorization Server avoids forwarding or redirecting a request potentially containing user credentials accidentally.  | ✓ | ✓ | ✓ |


## PKCE - Proof Key for Code Exchange Mechanism

OAuth 2.0 public clients utilizing the Authorization Code Grant are susceptible to the authorization code interception attack. Proof Key for Code Exchange (PCKE, pronounced "pixy") is the technique used to mitigate against the threat of authorization code interception attack. 

Originally, PKCE is intended to be used solely focused on securing native apps, but then it became a deployed OAuth feature. It does not only protect against authorization code injection attacks, but also protects authorization codes created for public clients as PKCE ensures that the attacker cannot redeem a stolen authorization code at the token endpoint of the authorization server without knowledge of the code_verifier. 

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **3.8.6** | [ADDED] Verify that Clients are preventing injection (replay) of authorization codes into the authorization response by using PKCE flow. Additionally, clients may use the OpenID Connect "nonce" parameter and the respective Claim in the ID Token instead. The PKCE challenge or OpenID Connect "nonce" must be transaction-specific and securely bound to the client and the user agent in which the transaction was started.  | ✓ | ✓ | ✓ |
| **3.8.7** | [ADDED] Verify that when using PKCE, Clients should use PKCE code challenge methods that do not expose the PKCE verifier in the authorization request. Otherwise, attackers that can read the authorization request can break the security provided by the PKCE. Authorization servers must support PKCE.  | ✓ | ✓ | ✓ |
| **3.8.8** | [ADDED] Verify that if a Client sends a valid PKCE "code_challenge" parameter in the authorization request, the authorization server enforces the correct usage of "code_verifier" at the token endpoint. | ✓ | ✓ | ✓ |
| **3.8.9** | [ADDED] Verify that Authorization Servers are mitigating PKCE Downgrade Attacks by ensuring a token request containing a "code_verifier" parameter is accepted only if a "code_challenge" parameter was present in the authorization request. | ✓ | ✓ | ✓ |


## Implicit Grant

The implicit grant is a simplified authorization code flow optimized for clients implemented in a browser using a scripting language such as JavaScript. In the implicit flow, instead of issuing the client an authorization code, the client is issued an access token directly (as the result of the resource owner authorization). The grant type is implicit, as no intermediate credentials (such as authorization code) are issued (and later used to obtain an access token). 

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **3.8.10** | [ADDED] Verify that Clients are using the response type "code" (aka authorization code grant type) or any other response type that causes the authorization server to issue access tokens in the token response, such as the "code id_token" response type. This allows the Authorization Server to detect replay attempts by attackers and generally reduces the attack surface since access tokens are not exposed in the URLs. It also allows the Authorization Server to sender-contrain the issued tokens.  | ✓ | ✓ | ✓ |


## Token Replay Prevention 

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **3.8.11** | [ADDED] Verify that Authorization and Resource Servers are using mechanisms for sender-constraining access tokens to prevent token replay, such as Mutual TLS for OAuth 2.0 or OAuth Demonstration of Proof of Possession (DPoP).  | ✓ | ✓ | ✓ |
| **3.8.12** | [ADDED]  Verify that refresh tokens are sender-constrained or use refresh token rotation. | ✓ | ✓ | ✓ |


## Access Token Privilege Restriction

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **3.8.13** | [ADDED] Verify that the privileges associated with an access token should be restricted to the minimum required for the particular application or use case. This prevents clients from exceeding the priviliges authorized by the Resource Owner. It also prevents users from exceeding their privileges authorized by the respective security policy. Privilege restrictions also help to reduce the impact of access token leakage.  | ✓ | ✓ | ✓ |
| **3.8.14** | [ADDED] Verify that access tokens are restricted to certain Resource Servers (audience restriction), preferably to a single Resource Server. The Authorization Server should associate the access token with certain Resource Servers and every Resource Server is obliged to verify, for every request, whether the access token sent with that request was meant to be used for that particular Resource Server. If not, the Resource Server must refuse to serve the respective request. Clients and Authorization Servers may utilize the parameters "scope" and "resource", respectively to determine the Resource Server they want to access.  | ✓ | ✓ | ✓ |
| **3.8.15** | [ADDED] Verify that access tokens are restricted to certain resources and actions on Resource Servers or resources. The Authorization Server should associate the access token with the respective resource and actions and every Resource Server is obliged to verify, for every request, whether the access token sent with that request was meant to be used for that particular action on the particular resource. If not, the Resource Server must refuse to serve the respective request. Clients and Authorization Servers may utilized the parameters "scope" and "authorization_details" to determine those resources and/or actions. | ✓ | ✓ | ✓ |


## Resource Owner Password Credentials Grant

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **3.8.16** | [ADDED] Verify that the Resource Owner password credentials grant is not used. This grant type insecurely exposes the credentials of the Resource Owner to the client, increasing the attack surface of the application.  | ✓ | ✓ | ✓ |


## Client Authentication

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **3.8.17** | [ADDED] Verify that Authorization Servers are using client authentication if possible. It is recommended to use asymmetric (public-key based) methods for client authentication such as mTLS or "private_key_jwt" (OpenID Connect). When asymmetric methods for client authentication are used, Authorization Servers do not need to store sensitive symmetric keys, making these methods more robust against a number of attacks.  | ✓ | ✓ | ✓ |


## Other Recommendations

| # | Description | L1 | L2 | L3 |
| :---: | :--- | :---: | :---: | :---: |
| **3.8.18** | [ADDED] Verify that Authorization Servers do not allow clients to influence their "client_id" or "sub" value or any other Claim that can cause confusion with a genuine Resource Owner. It is recommended to use end-to-end TLS.  | ✓ | ✓ | ✓ |
| **3.8.19** | [ADDED] Verify that Authorization responses are not transmitted over unencrypted network connections. Authorization Servers must not allow redirect URIs that use the "http" scheme except for native clients that use Loopback Interface Redirection.  | ✓ | ✓ | ✓ |



## References

For more information, see also:

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OAuth 2.0 RFC](https://www.rfc-editor.org/info/rfc6749)
* [OAuth RFC](https://www.rfc-editor.org/info/rfc6750)
* [OAuth 2.0 Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics#name-best-practices)
