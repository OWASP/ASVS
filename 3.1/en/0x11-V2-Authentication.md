# V2: Authentication Verification Requirements

## Control Objective

Authentication is the act of establishing, or confirming, something (or someone) as authentic, that is, that claims made by a person or about a device are true, resistant to impersonation, and prevents recovery or interception of memorized secrets (passwords).

NIST 800-63 is a modern, evidence based standard, and represents the best advice available in 2018. The standard is extremely helpful for all organizations all over the world, but is particularly relevant to US agencies and those dealing with US agencies. Implementers requiring the full set of controls should review the entire standard, especially regarding evidence of identity, identity binding, identity assertion, the deployment and management of multi-factor, biometric and crypto devices, security usability, and a great deal more advanced topics.

Verifications below are selected to address modern authentication threats such as credential stuffing, phishing, breached, weak or default memorized secrets, but by necessity are not a complete set of controls. If you require full NIST 800-63 compliance, please use this list as unit or integration tests to demonstrate a sampling of essential controls. Full compliance with the ASVS 3.1 is not the same as full compliance with NIST 800-63.

ASVS V2 Authentication, V3 Session Management, and V4 Access Controls has been adapted to be a compliant subset of selected NIST 800-63 B controls, focused around commonly exploited authentication weaknesses. Previous verification requirements have been retired, de-duped, or in most cases adapted to either be identical or strongly aligned with the intent of NIST 800-63 normative (mandatory) requirements. New NIST 800-63 verifications are enumerated from V2.40 onwards.

Authentication Access Levels (AAL) replace L1 .. L3 in these chapters. You should use NIST 800-63 &sect; 6.2 to determine the correct authentication assurance level (AAL) for your application. In some cases, AAL1 weakens L1 controls as documented in previous versions of ASVS. If you wish to retain those controls, choose AAL2 or AAL3 instead as per the risk of your application.

We strongly urge everyone to adopt NIST 800-63, and align any policies, guidelines and standards with it, such as we've done here.

## Authentication Verification Requirements

| # | Description | AAL1 | AAL2 | AAL3 | Since | NIST &sect; |
| --- | --- | --- | --- | -- | -- | -- |
| **2.1** | Verify authenticators are resistant to compromise, such as enforcing authentication decisions on a trusted device or service. | ✓  | ✓ | ✓ | 3.1 | 5.2.7 |
| **2.2** | Verify authenticators CANNOT store or return plain text memorized secrets, either as hidden or visible form fields, query parameters, cookie values, HTTP headers, emails, or SMS messages. | ✓ | ✓ | ✓ | 3.1 | 5.1.1 |
| **2.6** | Verify authentication controls fail securely to ensure attackers cannot log in by inducing errors or exceptions. | ✓ | ✓ | ✓ | 1.0 | Implicit |
| **2.7** | Verifiers SHALL require memorized secrets to be at least 8 characters in length. Verifiers SHOULD permit memorized secrets at least 64 characters in length. | ✓ | ✓ | ✓ | 3.1 | 5.1.1.2 |
| **2.8** | Verify all identity proofing functions (registration, login, credential reset, MFA device enrollment, lookup code entry, and so on) are secured by equivalent security controls. | ✓ | ✓ | ✓ | 3.1 | Implicit |
| **2.9** | Verify change memorized secret includes the old secret, the new secret and confirmation secret, and if used by the user, a valid multi-factor authentication challenge. | ✓ | ✓ | ✓ | 3.1 | N/A |
| **2.12** | Verify all authentication decisions are logged, without storing sensitive session identifiers or memorized secrets. This should include requests with relevant metadata needed for security investigations.  |  | ✓ | ✓ | 3.1 | N/A |
| **2.13** | Verifiers SHALL store memorized secrets in a form that is resistant to offline attacks. Memorized secrets SHALL be salted and hashed using a suitable one way key derivation function. Key derivation functions take a memorized secret, a salt, and a cost factor as inputs, and then generate a memorized secret.  | ✓ | ✓ | ✓ | 3.1 | 5.1.1.1 |
| **2.16** | Verify communication between the claimant and verifier (the primary channel in the case of an out-of-band authenticator) SHALL be via an authenticated protected channel to provide confidentiality of the authenticator output and resistance to man in the middle attacks. | ✓ | ✓ | ✓ | 3.1 | TBA |
| **2.17** | Verify memorized secret credential recovery, does not reveal the current memorized secret and that a system generated new memorized secret is not sent in clear text to the user. Lookup codes or a random, time limited one time reset link should be used instead. | ✓ | ✓ | ✓ | 3.1 | TBA |
| **2.18** | Verify credential or profile enumeration is not possible via registration, login, credential reset functionality.  |  | ✓ | ✓ | 3.1 | N/A |
| **2.19** | Removed. Default and weak memorized secrets are now covered by 2.27. | ✓ | ✓ | ✓ | 2.0 | TBA |
| **2.20** | Verify anti-automation or rate limiting is in place and effective to prevent breached credential testing, brute forcing, and account lockout attacks. |  | ✓ | ✓ | 3.1 | 5.2.2 |
| **2.21** | Integration memorized secrets SHOULD NOT rely on unchanging memorized secrets, such as API keys or shared privileged accounts. If memorized secrets are required, the credential should not be a default account, and stored with sufficient protection to prevent offline recovery attacks, including local system access. | Software | OS assisted | HSM | 3.1 | 5.1.1.1 |
| **2.22** | Verify forgotten memorized secret and other recovery paths use a TOTP or other soft token, mobile push, or other offline recovery mechanism. The use of PSTN verifiers (such as SMS tokens) has been deprecated by NIST and SHOULD NOT be used. |  | ✓ | ✓ | 3.1 | TBA |
| **2.23** | Verify the authenticator permits at least 10 attempts before soft lock out, particularly where longer memorized secrets are required. Including meaningful feedback on the number of attempts left. | ✓ | ✓ | ✓ | 3.1 | TBA |
| **2.24** | Removed. Shared knowledge questions/answers MUST NOT be present. | ✓ | ✓ | ✓ | 3.1 | TBA |
| **2.25** | Removed. Password history SHOULD NOT be enforced. |  ✓ | ✓ | ✓ | 3.1 | TBA |
| **2.26** | Verify if authenticators permit users to remain logged in, that re-authentication occurs periodically both when actively used or after an idle period. | 30 days | 12 hours or 30 minutes of inactivity, 2FA optional | 12 hours or 15 minutes of inactivity, with 2FA | 3.1 | 4.5 |
| **2.27** | Verify authenticators prevent the use of breached, weak, default, common memorized secrets (PINS, memorized secrets and pass-phrases). |  ✓ | ✓ | ✓ | 3.1 | 5.1.1 |
| **2.28** | Verify hardware-based authenticators and verifiers SHOULD resist relevant side-channel (e.g., timing and power-consumption analysis) attacks. Relevant side-channel attacks SHALL be determined by a risk assessment performed by the CSP. |  |  | ✓ | 3.1 | 4.3.2 |
| **2.29** | Verify memorized secrets, integrations with databases and third party systems, seeds and internal secrets, and API keys are managed securely and not included in the source code or stored within source code repositories. Such storage SHOULD resist offline attacks. The use of a software secure key store (L1), hardware trusted platform module (TPM), or hardware security module (L3) is recommended for memorized secret storage. |  Software | OS assisted | HSM | 3.1 | TBA |
| **2.32** | Verify administrative interfaces use appropriate multi-factor authentication to prevent unauthorized use. | ✓ | ✓ | ✓ | 3.1 | TBA |
| **2.33** | Verify the application allows paste into memorized secret fields, can show the memorized secret at the user's request, potentially show the last typed character for a second or two, and is compatible with browser based and third party credential managers. | ✓ | ✓ | ✓ | 3.1 | TBA |
| **2.34** | Verify that users can change their memorized secret or MFA enrollment. | SFA | | | 3.1 | TBA |
| **2.41** | Verify the permitted authenticator types TBA | SFA | | | 3.1 | TBA |
| **2.42** | Verify encryption of memorized secrets complies uses with FIPS 140 approved algorithms and verification levels. Key length SHALL comply with NIST 800-131A, with a minimum key length of 112 bits. Salts SHALL be securely randomly generated, and be no less than 32 bits in length. | Level 1 | Level 1 | Level 2 Overall | 3.1 | TBA |
| **2.43** | Verify the authentication system is man-in-the-middle resistant, such as mandatory use of TLS certificates | ✓ | ✓ | ✓ | 3.1 | TBA |
| **2.44** | Verify the authentication system is impersonation resistant, such as anti-phishing countermeasures or mutual authentication TLS connections. |  |  | ✓ | 3.1 | 5.2.3 |
| **2.45** | Verify the authentication system is compromise resistant, such as memorized secret breaches and/or client device reputation, and other controls. | | | ✓ | 3.1 | 5.2.7 |
| **2.46** | Verify the authentication system is replay resistant, such as ensuring session or bearer tokens cannot be easily be captured or replayed by attackers. | | | ✓ | 3.1 | 5.2.28 |
| **2.4x** | Verify the authentication system explicitly challenges the user on each authentication request. | ✓ | ✓ | ✓ | 3.1 | 5.2.9 |
| **2.47** | Verify authentication challenges SHOULD be rate limited. | ✓ | ✓ | ✓ | 3.1 | 5.2.2 |
| **2.48** | Verify memorized secret activation SHOULD be securely randomly generated, SHOULD be at least 6 characters long, and MAY contain letters and numbers. | ✓ | ✓ | ✓ | 3.1 | 5.1.1.2 / A.3 |
| **2.49** | Verify identities cannot cannot be re-bound to a different identity (spoofing). | ✓ | ✓ | ✓ | 3.1 | 5.1.1.2 / A.3 |
| **2.50** | Verify Replay resistance. | ✓ | ✓ | ✓ | 3.1 | 5.1.1.2 / A.3 |

Authentication intent
Record retention policy
Privacy controls

## Optional requirement

For US Government agencies and advanced verifiers, NIST 800-63 requires the following

| # | Description | AAL1 | AAL2 | AAL3 | Since | NIST &sect; |
| --- | --- | --- | --- | -- | -- | -- |
| **2.50** | Verify security controls adhere to the indicated NIST 800-53 baseline or equivalent. | Low | Moderate | High | 3.1 |  TBA |

Privacy compliance 9.4

## Glossary of terms

| Term | Meaning |
| -- | -- |

| CSP | Credential Service Provider, also called an Identity Provider |
| Authenticator | |
| Verifier | "An entity that verifies the claimant's identity by verifying the claimant's possession and control of one or two authenticators using an authentication protocol. To do this, the verifier may also need to validate credentials that link the authenticator(s) to the subscriber's identifier and check their status" |
| OTP | One time password |
| SFA | Single factor authenticator, such as something you know (memorized secrets, passwords, pass phrases, PINs), something you are (biometrics, fingerprint, face scans), or something you have (OTP tokens, cryptographic device such as a smart card),  |
| MFA | Multi factor authenticator, which includes two or more single factors |

## References

For more information, see also:

* [NIST 800-63 - TBA](TBA)
* [NIST 800-63 A - Digital Identity and Authentication Lifecycle](TBA)
* [NIST 800-63 B - TBA](TBA)
* [NIST 800-63 C - TBA](TBA)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://www.owasp.org/index.php/Testing_for_authentication)
* [Password storage cheat sheet](https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet)
* [Forgot password cheat sheet](https://www.owasp.org/index.php/Forgot_Password_Cheat_Sheet)
* [Choosing and Using Security Questions at](https://www.owasp.org/index.php/Choosing_and_Using_Security_Questions_Cheat_Sheet)
