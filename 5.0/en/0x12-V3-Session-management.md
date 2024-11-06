# V3 Session Management

## Control Objective

One of the core components of any web-based application or stateful API is the mechanism by which it controls and maintains the state for a user or device interacting with it. Session management changes a stateless protocol to stateful, which is critical for differentiating different users or devices.

Ensure that a verified application satisfies the following high-level session management requirements:

* Sessions are unique to each individual and cannot be guessed or shared.
* Sessions are invalidated when no longer required and timed out during periods of inactivity.

As previously noted, these requirements have been adapted to be a compliant subset of selected NIST SP 800-63B controls, focused on common threats and commonly exploited authentication weaknesses. Previous verification requirements have been retired, de-duped, or in most cases adapted to be strongly aligned with the intent of mandatory [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) requirements.

## V1.3 Session Management Documentation

Session management mechanisms give applications the ability to correlate user and device interactions over time, even when using otherwise stateless communication protocols. Modern applications may utilize multiple session identifiers or tokens with distinct characteristics and purposes. A secure session management system is one that optimally prevents attackers from obtaining, utilizing, or otherwise abusing a victim's session.

There is no single pattern that suits all applications. Therefore, it is infeasible to define universal boundaries and limits that suit all cases. A risk analysis with documented security decisions related to session handling must be conducted as a prerequisite to implementation and testing. This ensures that the session management system is tailored to the specific requirements of the application. Regardless of whether a stateful or "stateless" session mechanism is chosen, the analysis must be complete and documented to demonstrate that the selected solution is capable of satisfying all relevant security requirements.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.3.1** | [ADDED] Verify that the user's session inactivity period and maximum session lifetime before reauthentication are documented, appropriate in combination with other controls, and that documentation includes justification for any deviations from NIST SP 800-63B reauthentication requirements. | ✓ | ✓ | ✓ | |
| **1.3.2** | [ADDED] Verify that the documentation defines how many concurrent (parallel) sessions are allowed for one account as well as the intended behaviours and actions to be taken when the maximum number of active sessions is reached. | ✓ | ✓ | ✓ | |

## V3.1 Fundamental Session Management Security

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.1.1** | [DELETED, MERGED TO 8.3.1] | | | | | |
| **3.1.2** | [ADDED] Verify that the application performs all session token verification using a trusted, back-end service. | ✓ | ✓ | ✓ | 603 | |
| **3.1.3** | [MODIFIED, MOVED FROM 3.5.2, LEVEL L2 > L1] Verify that the application uses either cryptographically secured or random session tokens for session management. Static API secrets and keys should be avoided. | ✓ | ✓ | ✓ | 798 | 7.1 |
| **3.1.4** | [MODIFIED, MOVED FROM 3.2.2, MERGED FROM 3.2.4] Verify that if random tokens are used to represent user sessions, they are unique and generated using a cryptographically secure pseudo-random number generator (CSPRNG) and possess at least 128 bits of entropy. | ✓ | ✓ | ✓ | | |

## V3.2 Session Binding

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.2.1** | [MODIFIED] Verify the application generates a new session token on user authentication, including re-authentication, and terminates the current session token. | ✓ | ✓ | ✓ | 384 | 7.1 |
| **3.2.2** | [MOVED TO 3.1.4] | | | | | |
| **3.2.3** | [DELETED, MERGED TO 8.2.2] | | | | | |
| **3.2.4** | [DELETED, MERGED TO 3.1.4] | | | | | |
| **3.2.5** | [ADDED] Verify that creating a session for the application requires the user's consent and that the application is protected against a CSRF-style attack where a new application session for the user is created via SSO without user interaction. | | ✓ | ✓ | | |

TLS or another secure transport channel is mandatory for session management. This is covered in the Communications Security chapter.

## V3.3 Session Timeout

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.3.1** | [MOVED TO 3.8.1] | | | | | |
| **3.3.2** | [MODIFIED, SPLIT TO 3.3.5] Verify that there is an absolute maximum session lifetime such that re-authentication is enforced according to risk analysis and documented security decisions. | ✓ | ✓ | ✓ | | |
| **3.3.3** | [MOVED TO 3.8.2] | | | | | |
| **3.3.4** | [MOVED TO 3.8.3] | | | | | |
| **3.3.5** | [ADDED, SPLIT FROM 3.3.2] Verify that there is an inactivity timeout such that re-authentication is enforced according to risk analysis and documented security decisions. | ✓ | ✓ | ✓ | 613 | 7.2 |

## V3.4 Cookie-based Session Management

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.4.1** | Verify that cookie-based session tokens have the 'Secure' attribute set. | ✓ | ✓ | ✓ | 614 | 7.1.1 |
| **3.4.2** | [MODIFIED] Verify that cookie-based session tokens are not readable by client-side scripts. The session token cookie should have the 'HttpOnly' attribute set and the session token value should only be transferred to the client via the Set-Cookie header field. | ✓ | ✓ | ✓ | 1004 | 7.1.1 |
| **3.4.3** | Verify that cookie-based session tokens utilize the 'SameSite' attribute to limit exposure to cross-site request forgery attacks. | ✓ | ✓ | ✓ | 1275 | 7.1.1 |
| **3.4.4** | Verify that cookie-based session tokens use the "__Host-" prefix so cookies are only sent to the host that initially set the cookie. | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.5** | [DELETED, DEPRECATED BY 50.1.1] | | | | | |

## V3.5 Token-based Session Management

Token-based session management includes JWT, OAuth, SAML, and API keys. Of these, API keys are known to be weak and should not be used in new code. JWTs and SAML tokens are examples of stateless session tokens. All checks noted below should be enforced by a trusted, back-end service as noted above.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.5.1** | [GRAMMAR] Verify that the application allows users to revoke OAuth tokens that form trust relationships with linked applications. | | ✓ | ✓ | 290 | 7.1.2 |
| **3.5.2** | [MOVED TO 3.1.3] | | | | | |
| **3.5.3** | [MODIFIED, LEVEL L2 > L1] Verify that stateless tokens use a digital signature or MAC to protect against tampering, which is checked before accepting the token's contents. | ✓ | ✓ | ✓ | 345 | |
| **3.5.4** | [ADDED] Verify that stateless tokens are checked for expiration before processing them further. | ✓ | ✓ | ✓ | 613 | |
| **3.5.5** | [ADDED] Verify that only algorithms on an allowlist can be used to create and verify cryptographically secured tokens, for a given context. The allowlist should include the permitted algorithms, ideally only either symmetric or asymmetric algorithms, and should not include the 'None' algorithm. If both symmetric and asymmetric are needed, additional controls should prevent key confusion. | ✓ | ✓ | ✓ | 757 | |
| **3.5.6** | [ADDED] Verify that other, security-sensitive attributes of a stateless token are being verified. For example, in a JWT this may include issuer, subject, and audience. | ✓ | ✓ | ✓ | 287 | |

## V3.6 Federated Re-authentication

This section relates to those writing Relying Party (RP) or Credential Service Provider (CSP) code. If relying on code implementing these features, ensure that these issues are handled correctly.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.6.1** | Verify that Relying Parties (RPs) specify the maximum authentication time to Credential Service Providers (CSPs) and that CSPs re-authenticate the user if they haven't used a session within that period. | | | ✓ | 613 | 7.2.1 |
| **3.6.2** | Verify that Credential Service Providers (CSPs) inform Relying Parties (RPs) of the last authentication event, to allow RPs to determine if they need to re-authenticate the user. | | | ✓ | 613 | 7.2.1 |

## V3.7 Defenses Against Session Abuse

This section provides requirements to mitigate the risk posed by active sessions that are either hijacked or abused through vectors such as cross-site attacks.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.7.1** | [MODIFIED] Verify that the application requires re-authentication or secondary verification before allowing highly sensitive transactions or modifications to sensitive account attributes such as authentication settings. | ✓ | ✓ | ✓ | 306 | |

## V3.8 Session Termination

Session termination may be handled either by the application itself or by the SSO provider if the SSO provider is handling session management instead of the application. It may be necessary to decide whether the SSO provider is in scope when considering the requirements in this section as some may be controlled by the provider.

Session termination should result in requiring re-authentication and be effective across the application, federated login (if present), and any relying parties.

For stateful session mechanisms, this should just require invalidating the session at the backend. If a stateless session mechanism with signed tokens is being used, a way to revoke these tokens will be needed.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.8.1** | [MODIFIED, MOVED FROM 3.3.1] Verify that logout and expiration terminate the user's session, such that the back button or a downstream relying party cannot resume an authenticated session. | ✓ | ✓ | ✓ | 613 | 7.1 |
| **3.8.2** | [MODIFIED, LEVEL L2 > L1, MOVED FROM 3.3.3] Verify that the application gives the option to terminate all other active sessions after a successful change or removal of any authentication factor (including password change via reset or recovery and, if present, an MFA settings update). | ✓ | ✓ | ✓ | 613 | |
| **3.8.3** | [MODIFIED, MOVED FROM 3.3.4] Verify that users are able to view and (having re-entered login credentials) terminate any or all currently active sessions. | | ✓ | ✓ | 613 | 7.1 |
| **3.8.4** | [ADDED] Verify that all pages that require authentication have easy and visible access to logout functionality. | | ✓ | ✓ | | |
| **3.8.5** | [ADDED] Verify that the application terminates all active sessions when a user account is disabled or deleted (such as an employee leaving the company). | ✓ | ✓ | ✓ | 613 | |
| **3.8.6** | [ADDED] Verify that application administrators are able to terminate active sessions for an individual user or for all users. | ✓ | ✓ | ✓ | 613 | 7.1 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
