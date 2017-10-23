# V2: Authentication Verification Requirements

## Control Objective

Authentication is the act of establishing, or confirming, something (or someone) as authentic, that is, that claims made by or about the thing are true. Ensure that a verified application satisfies the following high level requirements:

* Verifies the digital identity of the sender of a communication.
* •	Ensures that only those authorised are able to authenticate and credentials are transported in a secure manner.

## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **2.1** | Verify all pages and resources are protected by server-side authentication, except those specifically intended to be public. | ✓ | ✓ | ✓ | 3.1 |
| **2.2** | Verify that the application does not automatically fill in credentials – either as hidden fields, URL arguments, Ajax requests, or in forms, as this implies plain text, reversible or de-cryptable password storage. Random time limited nonces are acceptable as stand ins, such as to protect change password forms or forgot password forms. | ✓ | ✓ | ✓ | 3.1 |
| **2.6** | Verify all authentication controls fail securely to ensure attackers cannot log in. | ✓ | ✓ | ✓ | 1.0 |
| **2.7** | Verify password entry fields allow, or encourage, the use of passphrases, and do not prevent long passphrases or highly complex passwords being entered. | ✓ | ✓ | ✓ | 3.0.1 |
| **2.8** | Verify all identity functions (e.g. forgot password, change password, change email, manage 2FA token, etc.) have the security controls, as the primary authentication mechanism (e.g. login form). | ✓ | ✓ | ✓ | 2.0 |
| **2.9** | Verify that the changing password functionality includes the old password, the new password, and a password confirmation. | ✓ | ✓ | ✓ | 1.0 |
| **2.12** | Verify that all authentication decisions can be logged, without storing sensitive session identifiers or passwords. This should include requests with relevant metadata needed for security investigations.  |  | ✓ | ✓ | 3.0.1 |
| **2.13** | Verify that account passwords are one way hashed with a salt, and there is sufficient work factor to defeat brute force and password hash recovery attacks. |  | ✓ | ✓ | 3.0.1 |
| **2.16** | Verify that all application data is transmitted over an encrypted channel (e.g. TLS). | ✓ | ✓ | ✓ | 3.1 |
| **2.17** | Verify that the forgotten password function and other recovery paths do not reveal the current password and that the new password is not sent in clear text to the user. A one time password reset link should be used instead. | ✓ | ✓ | ✓ | 2.0 |
| **2.18** | Verify that information enumeration is not possible via login, password reset, or forgot account functionality.  |  | ✓ | ✓ | 2.0 |
| **2.19** | Verify there are no default passwords in use for the application framework or any components used by the application (such as “admin/password”). | ✓ | ✓ | ✓ | 2.0 |
| **2.20** | Verify that anti-automation is in place to prevent breached credential testing, brute forcing, and account lockout attacks. |  | ✓ | ✓ | 3.0.1 |
| **2.21** | Verify that all authentication credentials for accessing services external to the application are encrypted and stored in a protected location.  |  | ✓ | ✓ | 2.0 |
| **2.22** | Verify that forgotten password and other recovery paths use a TOTP or other soft token, mobile push, or other offline recovery mechanism. The use of SMS has been deprecated by NIST and should not be used. |  | ✓ | ✓ | 3.0.1 |
| **2.23** | Verify that account lockout is divided into soft and hard lock status, and these are not mutually exclusive. If an account is temporarily soft locked out due to a brute force attack, this should not reset the hard lock status. |  | ✓ | ✓ | 3.0 |
| **2.24** | Verify that if secret questions are required, the questions do not violate privacy laws and are sufficiently strong to protect accounts from malicious recovery. | ✓ | ✓ | ✓ | 3.0.1 |
| **2.25** | Verify that high value applications can be configured to disallow the use of a configurable number of previous passwords. |  | ✓ | ✓ | 3.1 |
| **2.26** | Verify that sensitive operations (e.g. change password, change email address, add new biller, etc.) require re-authentication (e.g. password or 2FA token). This is in addition to CSRF measures, not instead. |  | ✓ | ✓ | 3.0.1 |
| **2.27** | Verify that measures are in place to block the use of commonly chosen passwords and weak pass-phrases. |  | ✓ | ✓ | 3.0 |
| **2.28** | Verify that all authentication challenges, whether successful or failed, should respond in the same average response time. |  |  | ✓ | 3.0 |
| **2.29** | Verify that secrets, API keys, and passwords are not included in the source code, or online source code repositories. |  | ✓ | ✓ | 3.0 |
| **2.31** | Verify that users can enrol and use TOTP verification, two-factor, biometric (Touch ID or similar), or equivalent multi-factor authentication mechanism that provides protection against single factor credential disclosure. |  | ✓ | ✓ | 3.1 |
| **2.32** | Verify that access to administrative interfaces are strictly controlled and not accessible to untrusted parties. | ✓ | ✓ | ✓ | 3.0 |
| **2.33** | Verify that the application is compatible with browser based and third party password managers, unless prohibited by risk based policy. | ✓ | ✓ | ✓ | 3.1 |



## References

For more information, see also:

* [OWASP Testing Guide 4.0: Testing for Authentication](https://www.owasp.org/index.php/Testing_for_authentication)
* [Password storage cheat sheet](https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet)
* [Forgot password cheat sheet](https://www.owasp.org/index.php/Forgot_Password_Cheat_Sheet)
* [Choosing and Using Security Questions at](https://www.owasp.org/index.php/Choosing_and_Using_Security_Questions_Cheat_Sheet)
