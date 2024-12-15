# V3 Session Management

## Control Objective

Session management mechanisms allow applications to correlate user and device interactions over time, even when using stateless communication protocols (such as HTTP). Modern applications may use multiple session identifiers or tokens with distinct characteristics and purposes. A secure session management system is one that prevents attackers from obtaining, utilizing, or otherwise abusing a victim's session. Applications maintaining sessions must ensure that the following high-level session management requirements are satisfied:

* Sessions are unique to each individual and cannot be guessed or shared.
* Sessions are invalidated when no longer required and timed out during periods of inactivity.

Many of the requirements in this chapter relate to selected [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/) controls, focused on common threats and commonly exploited authentication weaknesses.

Note that requirements for specific implementation details of certain session management mechanisms can be found in other:

* HTTP Cookies are a common mechanism for securing session identifiers and specific security requirements for cookies can be found in the "Web Frontend Security" chapter.
* Self-contained tokens are frequently used as a way of maintaining sessions. Specific security requirements can be found in the "Self-contained Tokens" chapter.

## V1.3 Session Management Documentation

There is no single pattern that suits all applications. Therefore, it is infeasible to define universal boundaries and limits that suit all cases. A risk analysis with documented security decisions related to session handling must be conducted as a prerequisite to implementation and testing. This ensures that the session management system is tailored to the specific requirements of the application. Regardless of whether a stateful or "stateless" session mechanism is chosen, the analysis must be complete and documented to demonstrate that the selected solution is capable of satisfying all relevant security requirements.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.3.1** | [ADDED] Verify that the user's session inactivity period and maximum session lifetime before reauthentication are documented, appropriate in combination with other controls, and that documentation includes justification for any deviations from NIST SP 800-63B reauthentication requirements. | ✓ | ✓ | ✓ | |
| **1.3.2** | [ADDED] Verify that the documentation defines how many concurrent (parallel) sessions are allowed for one account as well as the intended behaviours and actions to be taken when the maximum number of active sessions is reached. | ✓ | ✓ | ✓ | |
| **1.3.3** | [ADDED] Verify that all systems that create and manage user sessions as part of a federated identity management ecosystem (such as SSO systems) are documented along with controls to coordinate session lifetimes, termination, and any other condition that should require re-authentication. | ✓ | ✓ | ✓ | |

## V3.1 Fundamental Session Management Security

This section satisfies the essential requirements of secure sessions by verifying that session tokens are securely generated, managed, and validated.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **3.1.1** | [DELETED, MERGED TO 8.3.1] | | | | |
| **3.1.2** | [ADDED] Verify that the application performs all session token verification using a trusted, back-end service. | ✓ | ✓ | ✓ | 603 |
| **3.1.3** | [MODIFIED, MOVED FROM 3.5.2, LEVEL L2 > L1] Verify that the application uses either self-contained or reference tokens for session management. Static API secrets and keys should be avoided. | ✓ | ✓ | ✓ | 798 |
| **3.1.4** | [MODIFIED, MOVED FROM 3.2.2, MERGED FROM 3.2.4] Verify that if reference tokens are used to represent user sessions, they are unique and generated using a cryptographically secure pseudo-random number generator (CSPRNG) and possess at least 128 bits of entropy. | ✓ | ✓ | ✓ | |
| **3.1.5** | [MODIFIED, MOVED FROM 3.2.1] Verify the application generates a new session token on user authentication, including re-authentication, and terminates the current session token. | ✓ | ✓ | ✓ | |

## V3.2 Session Binding

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **3.2.1** | [MOVED TO 3.1.5] | | | | |
| **3.2.2** | [MOVED TO 3.1.4] | | | | |
| **3.2.3** | [DELETED, MERGED TO 8.2.2] | | | | |
| **3.2.4** | [DELETED, MERGED TO 3.1.4] | | | | |

## V3.3 Session Timeout

Session timeout mechanisms serve to minimize the window of opportunity for session hijacking and other forms of session abuse. Timeouts must satisfy documented requirements.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **3.3.1** | [MOVED TO 3.8.1] | | | | |
| **3.3.2** | [MODIFIED, SPLIT TO 3.3.5] Verify that there is an absolute maximum session lifetime such that re-authentication is enforced according to risk analysis and documented security decisions. | ✓ | ✓ | ✓ | |
| **3.3.3** | [MOVED TO 3.8.2] | | | | |
| **3.3.4** | [MOVED TO 3.7.2] | | | | |
| **3.3.5** | [ADDED, SPLIT FROM 3.3.2] Verify that there is an inactivity timeout such that re-authentication is enforced according to risk analysis and documented security decisions. | ✓ | ✓ | ✓ | 613 |

## V3.4 Cookie-based Session Management

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **3.4.1** | [MOVED TO 50.2.1] | | | | |
| **3.4.2** | [MOVED TO 50.2.2] | | | | |
| **3.4.3** | [MOVED TO 50.2.3] | | | | |
| **3.4.4** | [MOVED TO 50.2.4] | | | | |
| **3.4.5** | [DELETED, DEPRECATED BY 50.1.1] | | | | |

## V3.5 Token-based Session Management

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **3.5.1** | [MOVED TO 51.4.14] | | | | |
| **3.5.2** | [MOVED TO 3.1.3] | | | | |
| **3.5.3** | [MOVED TO 52.1.1] | | | | |

## V3.6 Federated Re-authentication

This section relates to those writing Relying Party (RP) or Credential Service Provider (CSP) code. These requirements are derived from the [NIST SP 800-63C](https://pages.nist.gov/800-63-4/sp800-63c.html) for Federation & Assertions.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **3.6.1** | [MODIFIED, MERGED FROM 3.6.2] Verify that session lifetime and termination between Relying Parties (RPs) and Credential Service Providers (CSPs) behave as documented, requiring re-authentication as necessary such as when the maximum time between CSP authentication events is reached. | | | ✓ | 613 |
| **3.6.2** | [DELETED, MERGED TO 3.6.1] | | | | |
| **3.6.3** | [ADDED] Verify that creation of a session requires either the user's consent or an explicit action, preventing the creation of new application sessions without user interaction. | | ✓ | ✓ | |

## V3.7 Defenses Against Session Abuse

This section provides requirements to mitigate the risk posed by active sessions that are either hijacked or abused through vectors such as cross-site request forgery (CSRF) and other cross-site attacks, which rely on the existence and capabilities of active user sessions.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **3.7.1** | [MODIFIED] Verify that the application requires re-authentication or secondary verification before allowing highly sensitive transactions or modifications to sensitive account attributes such as authentication settings. | ✓ | ✓ | ✓ | 306 |
| **3.7.2** | [MODIFIED, MOVED FROM 3.3.4] Verify that users are able to view and (having re-entered login credentials) terminate any or all currently active sessions. | | ✓ | ✓ | |

## V3.8 Session Termination

Session termination may be handled either by the application itself or by the SSO provider if the SSO provider is handling session management instead of the application. It may be necessary to decide whether the SSO provider is in scope when considering the requirements in this section as some may be controlled by the provider.

Session termination should result in requiring re-authentication and be effective across the application, federated login (if present), and any relying parties.

For stateful session mechanisms, termination typically involves invalidating the session on the backend. In the case of self-contained tokens, additional measures are required to revoke or block these tokens, as they may otherwise remain valid until expiration.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **3.8.1** | [MODIFIED, MOVED FROM 3.3.1] Verify that logout and expiration terminate the user's session, such that the back button or a downstream relying party cannot resume an authenticated session. | ✓ | ✓ | ✓ | 613 |
| **3.8.2** | [MODIFIED, LEVEL L2 > L1, MOVED FROM 3.3.3] Verify that the application gives the option to terminate all other active sessions after a successful change or removal of any authentication factor (including password change via reset or recovery and, if present, an MFA settings update). | ✓ | ✓ | ✓ | 613 |
| **3.8.3** | [ADDED] Verify that all pages that require authentication have easy and visible access to logout functionality. | | ✓ | ✓ | |
| **3.8.4** | [ADDED] Verify that the application terminates all active sessions when a user account is disabled or deleted (such as an employee leaving the company). | ✓ | ✓ | ✓ | 613 |
| **3.8.5** | [ADDED] Verify that application administrators are able to terminate active sessions for an individual user or for all users. | ✓ | ✓ | ✓ | 613 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
