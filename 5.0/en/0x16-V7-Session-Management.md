# V7 Session Management

## Control Objective

Session management mechanisms allow applications to correlate user and device interactions over time, even when using stateless communication protocols (such as HTTP). Modern applications may use multiple session tokens with distinct characteristics and purposes. A secure session management system is one that prevents attackers from obtaining, utilizing, or otherwise abusing a victim's session. Applications maintaining sessions must ensure that the following high-level session management requirements are satisfied:

* Sessions are unique to each individual and cannot be guessed or shared.
* Sessions are invalidated when no longer required and timed out during periods of inactivity.

Many of the requirements in this chapter relate to selected [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/) controls, focused on common threats and commonly exploited authentication weaknesses.

Note that requirements for specific implementation details of certain session management mechanisms can be elsewhere:

* HTTP Cookies are a common mechanism for securing session tokens. Specific security requirements for cookies can be found in the "Web Frontend Security" chapter.
* Self-contained tokens are frequently used as a way of maintaining sessions. Specific security requirements can be found in the "Self-contained Tokens" chapter.

## V7.1 Session Management Documentation

There is no single pattern that suits all applications. Therefore, it is infeasible to define universal boundaries and limits that suit all cases. A risk analysis with documented security decisions related to session handling must be conducted as a prerequisite to implementation and testing. This ensures that the session management system is tailored to the specific requirements of the application.

Regardless of whether a stateful or "stateless" session mechanism is chosen, the analysis must be complete and documented to demonstrate that the selected solution is capable of satisfying all relevant security requirements. Interaction with any Single Sign-on (SSO) mechanisms in use should also be considered.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.1.1** | Verify that the user's session inactivity period and maximum session lifetime before re-authentication are documented, appropriate in combination with other controls, and that documentation includes justification for any deviations from NIST SP 800-63B re-authentication requirements. | 2 | v5.0.be-1.3.1 |
| **7.1.2** | Verify that the documentation defines how many concurrent (parallel) sessions are allowed for one account as well as the intended behaviours and actions to be taken when the maximum number of active sessions is reached. | 2 | v5.0.be-1.3.2 |
| **7.1.3** | Verify that all systems that create and manage user sessions as part of a federated identity management ecosystem (such as SSO systems) are documented along with controls to coordinate session lifetimes, termination, and any other conditions that require re-authentication. | 2 | v5.0.be-1.3.3 |

## V7.2 Fundamental Session Management Security

This section satisfies the essential requirements of secure sessions by verifying that session tokens are securely generated and validated.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.2.1** | Verify that the application performs all session token verification using a trusted, backend service. | 1 | v5.0.be-3.1.2 |
| **7.2.2** | Verify that the application uses either self-contained or reference tokens that are dynamically generated for session management, i.e. not using static API secrets and keys. | 1 | v5.0.be-3.1.3 |
| **7.2.3** | Verify that if reference tokens are used to represent user sessions, they are unique and generated using a cryptographically secure pseudo-random number generator (CSPRNG) and possess at least 128 bits of entropy. | 1 | v5.0.be-3.1.4 |
| **7.2.4** | Verify that the application generates a new session token on user authentication, including re-authentication, and terminates the current session token. | 1 | v5.0.be-3.1.5 |

## V7.3 Session Timeout

Session timeout mechanisms serve to minimize the window of opportunity for session hijacking and other forms of session abuse. Timeouts must satisfy documented security decisions.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.3.1** | Verify that there is an inactivity timeout such that re-authentication is enforced according to risk analysis and documented security decisions. | 2 | v5.0.be-3.3.5 |
| **7.3.2** | Verify that there is an absolute maximum session lifetime such that re-authentication is enforced according to risk analysis and documented security decisions. | 2 | v5.0.be-3.3.2 |

## V7.4 Session Termination

Session termination may be handled either by the application itself or by the SSO provider if the SSO provider is handling session management instead of the application. It may be necessary to decide whether the SSO provider is in scope when considering the requirements in this section as some may be controlled by the provider.

Session termination should result in requiring re-authentication and be effective across the application, federated login (if present), and any relying parties.

For stateful session mechanisms, termination typically involves invalidating the session on the backend. In the case of self-contained tokens, additional measures are required to revoke or block these tokens, as they may otherwise remain valid until expiration.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.4.1** | Verify that logout and expiration terminate the user's session, such that the back button or a downstream relying party cannot resume an authenticated session. | 1 | v5.0.be-3.8.1 |
| **7.4.2** | Verify that the application terminates all active sessions when a user account is disabled or deleted (such as an employee leaving the company). | 1 | v5.0.be-3.8.4 |
| **7.4.3** | Verify that the application gives the option to terminate all other active sessions after a successful change or removal of any authentication factor (including password change via reset or recovery and, if present, an MFA settings update). | 2 | v5.0.be-3.8.2 |
| **7.4.4** | Verify that all pages that require authentication have easy and visible access to logout functionality. | 2 | v5.0.be-3.8.3 |
| **7.4.5** | Verify that application administrators are able to terminate active sessions for an individual user or for all users. | 2 | v5.0.be-3.8.5 |

## V7.5 Defenses Against Session Abuse

This section provides requirements to mitigate the risk posed by active sessions that are either hijacked or abused through vectors that rely on the existence and capabilities of active user sessions. For example, using malicious content execution to force an authenticated victim browser to perform an action using the victim's session.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.5.1** | Verify that the application requires re-authentication before allowing modifications to sensitive account attributes which may affect authentication such as email address, phone number, MFA configuration, or other information used in account recovery. | 2 | v5.0.be-3.7.1 |
| **7.5.2** | Verify that users are able to view and (having re-entered login credentials) terminate any or all currently active sessions. | 2 | v5.0.be-3.7.2 |
| **7.5.3** | Verify that the application requires re-authentication or secondary verification before performing highly sensitive transactions or operations. | 3 | v5.0.be-3.7.3 |

## V7.6 Federated Re-authentication

This section relates to those writing Relying Party (RP) or Identity Provider (IdP) code. These requirements are derived from the [NIST SP 800-63C](https://pages.nist.gov/800-63-4/sp800-63c.html) for Federation & Assertions.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.6.1** | Verify that session lifetime and termination between Relying Parties (RPs) and Identity Providers (IdPs) behave as documented, requiring re-authentication as necessary such as when the maximum time between IdP authentication events is reached. | 2 | v5.0.be-3.6.1 |
| **7.6.2** | Verify that creation of a session requires either the user's consent or an explicit action, preventing the creation of new application sessions without user interaction. | 2 | v5.0.be-3.6.3 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
