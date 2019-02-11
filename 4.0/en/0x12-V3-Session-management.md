# V3: Session Management Verification Requirements

## Control Objective

One of the core components of any web-based application or API is the mechanism by which it controls and maintains the state for a user or device interacting with it. Session management changes a stateless protocol to stateful, which is critical for differentiating different users or devices.

Ensure that a verified application satisfies the following high-level session management requirements:

* Sessions are unique to each individual and cannot be guessed or shared.
* Sessions are invalidated when no longer required and timed out during periods of inactivity.

As previously noted, these requirements have been adapted to be a compliant subset of selected NIST 800-63b controls, focused around common threats and commonly exploited authentication weaknesses. Previous verification requirements have been retired, de-duped, or in most cases adapted to be strongly aligned with the intent of mandatory [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.htmlx) requirements.

## Security Verification Requirements

### V3.1 Fundamental Session Management Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: | :---: |
| **3.1.1** | Verify that the session token is never disclosed in URLs, error messages, or logs. This includes verifying that the application does not support URL rewriting of session cookies. |  | ✓ | ✓ | - | 598 | tbd |

### V3.2 Session Binding Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: | :---: |
| **3.2.1** | Verify that session tokens are created or generated after authentication, not before. | ✓ | ✓ | ✓ | 7.1 | 384 | tbd |
| **3.2.2** | Verify that session tokens are created using approved cryptographic algorithms with at least 64 bits of entropy. | ✓ | ✓ | ✓ | 7.1 | 331 | tbd |
| **3.2.3** | Verify that session tokens are not stored in insecure local storage, such as HTML 5 local storage. | ✓ | ✓ | ✓ | 7.1 | 539 | tbd |
| **3.2.4** | Verify that active session functionality exists, which allows users to either selectively or completely log out all active devices / sessions. |  | ✓ | ✓ | 7.1 | 613 | tbd |

TLS or another secure transport channel is mandatory for session management. This is covered off in the Communications Security chapter.

### V3.3 Session Logout and Timeout Requirements

Session timeouts have been aligned with NIST 800-63, which permits much longer session timeouts than traditionally permitted. This reflects modern common industry practice but is backed by increasing timeouts when multi-factor or stronger authenticators are used.

L1 in this context is IAL1/AAL1, L2 is IAL2/AAL3, L3 is IAL3/AAL3. For IAL2/AAL2 and IAL3/AAL3, the shorter idle timeout is, the lower bound of idle times for being logged out or re-authenticated to resume the session.

| # | Description | L1 | L2 | L3 | NIST &sect; | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: | :---: |
| **3.3.1** | Verify that logout invalidates or erases any client- or server-side session storage, such that the back button or a downstream relying party does not resume an authenticated session, including across relying parties. | ✓ | ✓ | ✓ | 7.1 | 613 | tbd |
| **3.3.2** | Verify that absolute or idle timeouts invalidates or erases any client- or server-side session storage. |  | ✓ | ✓ | 7.1 | 613 | tbd |
| **3.3.3 | If authenticators permit users to remain logged in, verify that re-authentication occurs periodically both when actively used or after an idle period. | 30 days | 12 hours or 30 minutes of inactivity, 2FA optional | 12 hours or 15 minutes of inactivity, with 2FA | 7.2 | 613 | tbd |
| **3.3.4** | Verify that the user can terminate all other active sessions after a successful change password process, and this is effective across the application, federated login (if present) and any relying parties. |  | ✓ | ✓ | - | 613 | tbd |

### V3.4 Cookie-based Session Management

| # | Description | L1 | L2 | L3 | NIST &sect; | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: | :---: |
| **3.4.1** | Verify that cookie-based session IDs have the 'Secure' attribute. | ✓ | ✓ | ✓ | 7.1.1 | 614 | tbd |
| **3.4.2** | Verify that cookie-based session IDs have the 'HttpOnly' attributes. | ✓ | ✓ | ✓ | 7.1.1 | 1004 | tbd |
| **3.4.3** | Verify that cookie-based session IDs have minimum practical hostnames, domain and path attributes, along with the 'SameSite' attribute. | ✓ | ✓ | ✓ | 7.1.1 | 16 | tbd |
| **3.4.4** | Verify that cookie-based session IDs are set to expire soon after the default session timeout period. | ✓ | ✓ | ✓ | 7.1.1 | 613 | tbd |

### V3.5 Token-based Session Management

Token-based session management includes JWT, OAuth, SAML, and API keys. Of these, API keys are known to be weak and should not be used in new code.

| # | Description | L1 | L2 | L3 | NIST &sect; | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: | :---: |
| **3.5.1** | Verify that OAuth and refresh tokens on their own are not interpreted as the presence of the subscriber. |  | ✓ | ✓ | 7.1.2 | 290 | tbd |
| **3.5.2** | Verify that single factor, static API secrets and keys are not used, except with legacy implementations. |  | ✓ | ✓ | - | 798 | tbd |
| **3.5.3** | Verify that stateless session tokens, which contain sensitive session data, are digitally signed or encrypted and regularly verified in a timely fashion to protect against tampering, enveloping, replay, null cipher and key substitution attacks. |  | ✓ | ✓ | - | 345 | tbd |

### V3.6 Re-authentication from a Federation or Assertion

This section relates to those writing relying party (RP) or credential service provider (CSP) code. If relying on code implementing these features, ensure that these issues are handled correctly.

| # | Description | L1 | L2 | L3 | NIST &sect; | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: | :---: |
| **3.6.1** | Verify that relying parties specify the maximum authentication time to CSPs and that CSPs re-authenticate the subscriber if they haven't used a session within that period. |  | | ✓ | 7.2.1 | 613 | tbd |
| **3.6.2** | Verify that CSPs inform relying parties of the last authentication event, to allow RPs to determine if they need to re-authenticate the subscriber. |  |  | ✓ | 7.2.1 | 613 tbd |

### V3.7 Defenses Against Session Management Exploits

There are a small number of session management attacks, some related to the user experience (UX) of sessions. Previously, based on ISO 27002 requirements, the ASVS has required blocking multiple simultaneous sessions. Blocking simultaneous sessions is no longer appropriate, not only as modern users have many devices or the app is an API without a browser session, but in most of these implementations, the last authenticator wins, which is often the attacker. This section provides leading guidance on deterring, delaying and detecting session management attacks using code.

#### Description of the half-open Attack

In early 2018, several financial institutions were compromised using what the attackers called "half-open attacks". This term has stuck in the industry. The attackers struck multiple institutions with different proprietary code bases, and indeed it seems different code bases within the same institutions. The half-open attack is exploiting a design pattern flaw commonly found in many existing authentication, session management and access control systems.

Attackers start a half-open attack by attempting to lock, reset, or recover a credential. A popular session management design pattern re-uses user profile session objects/models between unauthenticated, half-authenticated (password resets, forgot username), and fully authenticated code. This design pattern populates a valid session object or token containing the victim's profile, including password hashes and roles. If access control checks in controllers or routers does not correctly verify that the user is fully logged in, the attacker will be able to act as the user. Attacks could include changing the user's password to a known value, update the email address to perform a valid password reset, disable multi-factor authentication or enroll a new MFA device, reveal or change API keys, and so on.

| # | Description | L1 | L2 | L3 | NIST &sect; | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.7.1** | Verify that all post-reset, post-registration, and post-authentication high value or administrative functionality verifies the user session is both fully logged in and has a valid post-authentication role before permitting any changes or transactions, especially in relation to user profile updates, password changes, MFA enrollment, and administrative functionality.  | ✓ | ✓ | ✓ | - | 778 | tbd |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Session Management Testing](https://www.owasp.org/index.php/Testing_for_Session_Management)
* [OWASP Session Management Cheat Sheet](https://www.owasp.org/index.php/Session_Management_Cheat_Sheet)