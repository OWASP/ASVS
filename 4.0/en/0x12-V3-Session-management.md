# V3: Session Management Verification Requirements

## Control Objective

One of the core components of any web-based application or API is the mechanism by which it controls and maintains the state for a user or device interacting with it. Session management changes a stateless protocol to stateful, which is critical for differentiating different users or devices.

Ensure that a verified application satisfies the following high-level session management requirements:

* Sessions are unique to each individual and cannot be guessed or shared.
* Sessions are invalidated when no longer required and timed out during periods of inactivity.

As previously noted, these requirements have been adapted to be a compliant subset of selected NIST 800-63b controls, focused around common threats and commonly exploited authentication weaknesses. Previous verification requirements have been retired, de-duped, or in most cases adapted to be strongly aligned with the intent of mandatory [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.htmlx) requirements.

## Security Verification Requirements

### V3.1 Fundamental Session Management Requirements

| # | Description | L1 | L2 | L3 | CWE | NIST &sect; |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.1.1** | Verify the application never reveals session tokens as GET parameters in URLs, in error messages, or in log files.  | ✓ | ✓ | ✓ | 598 |  |

### V3.2 Session Binding Requirements

| # | Description | L1 | L2 | L3 | CWE | NIST &sect; |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.2.1** | Verify the application generates a new session token on user authentication. | ✓ | ✓ | ✓ | 384 | 7.1 |
| **3.2.2** | Verify that session tokens use approved cryptographic algorithms with at least 64 bits of entropy. | ✓ | ✓ | ✓ | 331 | 7.1 |
| **3.2.3** | Verify the application does not store session tokens using insecure methods such as HTML 5 local storage. | ✓ | ✓ | ✓ | 539 | 7.1 |

TLS or another secure transport channel is mandatory for session management. This is covered off in the Communications Security chapter.

### V3.3 Session Logout and Timeout Requirements

Session timeouts have been aligned with NIST 800-63, which permits much longer session timeouts than traditionally permitted. This reflects modern common industry practice but is backed by increasing timeouts when multi-factor or stronger authenticators are used.

L1 in this context is IAL1/AAL1, L2 is IAL2/AAL3, L3 is IAL3/AAL3. For IAL2/AAL2 and IAL3/AAL3, the shorter idle timeout is, the lower bound of idle times for being logged out or re-authenticated to resume the session.

| # | Description | L1 | L2 | L3 | CWE | NIST &sect; |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.3.1** | Verify that logout and expiration invalidate the session token, such that the back button or a downstream relying party does not resume an authenticated session, including across relying parties. | ✓ | ✓ | ✓ | 613 | 7.1 |
| **3.3.2** | If authenticators permit users to remain logged in, verify that re-authentication occurs periodically both when actively used or after an idle period. | 30 days | 12 hours or 30 minutes of inactivity, 2FA optional | 12 hours or 15 minutes of inactivity, with 2FA | 613 | 7.2 |
| **3.3.3** | Verify that the application terminates all other active sessions after a successful password change, and that this is effective across the application, federated login, (if present) and any relying parties. |  | ✓ | ✓ | 613 | |
| **3.3.4** | Verify that users are able to view and log out of any or all currently active sessions and devices. |  | ✓ | ✓ | 613 | 7.1 |

### V3.4 Cookie-based Session Management

| # | Description | L1 | L2 | L3 | CWE | NIST &sect; |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.4.1** | Verify that cookie-based session tokens have the 'Secure' attribute set. | ✓ | ✓ | ✓ | 614 | 7.1.1 |
| **3.4.2** | Verify that cookie-based session tokens have the 'HttpOnly' attribute set. | ✓ | ✓ | ✓ | 1004 | 7.1.1 |
| **3.4.3** | Verify that cookie-based session tokens utilize the 'SameSite' attribute to limit exposure to cross-site request forgery attacks. | ✓ | ✓ | ✓ | 16 |7.1.1 |
| **3.4.4** | Verify that cookie-based session tokens limit the 'path' attribute to the most precise path possible. | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.5** | Verify that cookie-based session tokens utilize the 'host' attribute. If the 'host' attribute is missing ensure the 'domain' attribute is set and is as precise as possible. | ✓ | ✓ | ✓ | 16 | 7.1.1 |

### V3.5 Token-based Session Management

Token-based session management includes JWT, OAuth, SAML, and API keys. Of these, API keys are known to be weak and should not be used in new code.

| # | Description | L1 | L2 | L3 | CWE | NIST &sect; |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.5.1** | Verify the application does not treat OAuth and refresh tokens &mdash; on their own &mdash; as the presence of the subscriber and allows users to terminate trust relationships with linked applications.  |  | ✓ | ✓ | 290 | 7.1.2 |
| **3.5.2** | Verify the application uses session tokens rather than static API secrets and keys, except with legacy implementations. |  | ✓ | ✓ | 798 | |
| **3.5.3** | Verify that stateless session tokens use digital signatures, encryption, and other countermeasures to protect against tampering, enveloping, replay, null cipher, and key substitution attacks. |  | ✓ | ✓ | 345 | |

### V3.6 Re-authentication from a Federation or Assertion

This section relates to those writing relying party (RP) or credential service provider (CSP) code. If relying on code implementing these features, ensure that these issues are handled correctly.

| # | Description | L1 | L2 | L3 | CWE | NIST &sect; |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.6.1** | Verify that relying parties specify the maximum authentication time to CSPs and that CSPs re-authenticate the subscriber if they haven't used a session within that period. |  | | ✓ | 613 | 7.2.1 |
| **3.6.2** | Verify that CSPs inform relying parties of the last authentication event, to allow RPs to determine if they need to re-authenticate the user. |  |  | ✓ | 613| 7.2.1 |

### V3.7 Defenses Against Session Management Exploits

There are a small number of session management attacks, some related to the user experience (UX) of sessions. Previously, based on ISO 27002 requirements, the ASVS has required blocking multiple simultaneous sessions. Blocking simultaneous sessions is no longer appropriate, not only as modern users have many devices or the app is an API without a browser session, but in most of these implementations, the last authenticator wins, which is often the attacker. This section provides leading guidance on deterring, delaying and detecting session management attacks using code.

#### Description of the half-open Attack

In early 2018, several financial institutions were compromised using what the attackers called "half-open attacks". This term has stuck in the industry. The attackers struck multiple institutions with different proprietary code bases, and indeed it seems different code bases within the same institutions. The half-open attack is exploiting a design pattern flaw commonly found in many existing authentication, session management and access control systems.

Attackers start a half-open attack by attempting to lock, reset, or recover a credential. A popular session management design pattern re-uses user profile session objects/models between unauthenticated, half-authenticated (password resets, forgot username), and fully authenticated code. This design pattern populates a valid session object or token containing the victim's profile, including password hashes and roles. If access control checks in controllers or routers does not correctly verify that the user is fully logged in, the attacker will be able to act as the user. Attacks could include changing the user's password to a known value, update the email address to perform a valid password reset, disable multi-factor authentication or enroll a new MFA device, reveal or change API keys, and so on.

| # | Description | L1 | L2 | L3 | CWE | NIST &sect; |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.7.1** | Verify the application ensures a valid login session or requires re-authentication or secondary verification before allowing any sensitive transactions or account modifications.   | ✓ | ✓ | ✓ | 778 | |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Session Management Testing](https://www.owasp.org/index.php/Testing_for_Session_Management)
* [OWASP Session Management Cheat Sheet](https://www.owasp.org/index.php/Session_Management_Cheat_Sheet)
