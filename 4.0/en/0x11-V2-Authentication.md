# V2: Authentication Verification Requirements

## Control Objective

Authentication is the act of establishing, or confirming, something (or someone) as authentic, that is, that claims made by a person or about a device are true, resistant to impersonation (phishing), and prevents recovery or interception of memorized secrets (passwords).

ASVS V2 Authentication, V3 Session Management, and V4 Access Controls have been adapted to be a compliant subset of selected NIST 800-63 controls, focused around typical threats and commonly exploited authentication weaknesses. Previous verification requirements have been retired, de-duped, or in most cases adapted to either be identical or strongly aligned with the intent of NIST 800-63 normative (mandatory) requirements. Logging requirements have been moved to the V8 Error and Logging chapter. TLS requirements have been moved to the V10 Communications Chapter.

NIST 800-63 is a modern, evidence based standard, and represents the best advice available, regardless of applicabilty. The standard is helpful for all organizations all over the world, but is particularly relevant to US agencies and those dealing with US agencies.

Implementers requiring the full set of controls should review the entire standard, especially regarding evidence of identity, identity binding, identity assertion, the deployment and management of multi-factor, biometric and crypto devices, security usability, and a great deal more advanced topics. Full compliance with the ASVS 4.0 is not the same as full compliance with NIST 800-63.

### Selecting an appropriate ASVS Level

The Application Security Verification Standard has mapped ASVS L1 to AAL1 requirements, L2 to AAL2, and L3 to AAL3. However, the approach of ASVS Level 1 as "essential" controls may not necessarily be the correct AAL level to verify an application or API. For example, if the application is a Level 3 application or has regulatory requirements to be AAL3, Level 3 should be chosen in Sections V2 and V3 Session Management. 

The choice of NIST compliant authentication assertion level (AAL) should be performed as per NIST 800-63 guidelines as set out in *Selecting AAL* in [NIST 800-63 Section 6.2](https://pages.nist.gov/800-63-3/sp800-63-3.html#AAL_CYOA). 

We strongly urge everyone to adopt NIST 800-63, and align any policies, guidelines and standards with it, such as we've done here.

## Authentication Verification Requirements

### V2.1 Fundamental Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.1.1** | Verify authenticators are resistant to compromise, such as enforcing authentication decisions on a trusted device or service. | ✓  | ✓ | ✓ | 5.2.7 |
| **2.1.2** | Verify authentication controls fail securely to ensure attackers cannot log in by inducing errors or exceptions. | ✓ | ✓ | ✓ | ASVS |
| **2.1.3** | Verify all identity proofing functions (registration, login, credential reset, MFA device enrollment, lookup code entry, and so on) are equally effective security controls. | ✓ | ✓ | ✓ | ASVS |

| **2.1.5** | Verify anti-automation or rate limiting is in place and effective to prevent breached credential testing, brute forcing, and account lockout attacks. |  | ✓ | ✓ | 5.2.2 |

### V2.2 Authenticator Binding Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.2.1** | Verify memorized secret activation codes SHOULD be securely randomly generated, SHOULD be at least 6 characters long, and MAY contain letters and numbers. | ✓ | ✓ | ✓ | 5.1.1.2 / A.3 |


### V2.3 Authenticator Recovery Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.3.1** | Verify memorized secret credential recovery, does not reveal the current memorized secret and that a system generated new memorized secret is not sent in clear text to the user. Lookup codes or a random, time limited one time reset link should be used instead. | ✓ | ✓ | ✓ | 5.1.1 |
| **2.3.2** | Verify memorized secret credential recovery, does not reveal the current memorized secret in any way. Stronger recovery mechanisms including multi-factor challenge, impersonation resistance, presence . |  | ✓ | ✓ | 5.1.1 |
| **2.3.4** | Verify forgotten memorized secret and other recovery paths use a TOTP or other soft token, mobile push, or other offline recovery mechanism. The use of PSTN verifiers (such as SMS tokens) has been deprecated by NIST and SHOULD NOT be used. |  | ✓ | ✓ | TBA |
| **2.3.5** | Verify identities cannot cannot be re-bound to a different identity (spoofing). | ✓ | ✓ | ✓ | 5.1.1.2 / A.3 |

### V2.4 Memorized Secrets Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.13** | Verifiers SHALL store memorized secrets in a form that is resistant to offline attacks. Memorized secrets SHALL be salted and hashed using a suitable one way key derivation function. Key derivation functions take a memorized secret, a salt, and a cost factor as inputs, and then generate a memorized secret.  | ✓ | ✓ | ✓ | 5.1.1.1 |
| **2.7** | Verifiers SHALL require memorized secrets to be at least 8 characters in length. Verifiers SHOULD permit memorized secrets at least 64 characters in length. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.9** | Verify users can change their stored memorized secret. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.x.x | Verify memorized secret change validates the current secret, and if used by the user, the credential change validates a multi-factor authentication challenge. | ✓ | ✓ | ✓ | N/A |
| **2.24** | Verify the application does not rely on knowledge-based or secret questions for authentication. | ✓ | ✓ | ✓ | TBA |
| **2.25** | Verify the application does not enforce a password history as a substitute for poor password policy. |  ✓ | ✓ | ✓ | TBA |
| **2.27** | Verify authenticators prevent the use of breached, weak, default, common memorized secrets (PINS, memorized secrets and pass-phrases). |  ✓ | ✓ | ✓ | 5.1.1 |
| **2.33** | Verify authenticators allows paste into memorized secret fields, and is compatible with browser based and third party credential managers. | ✓ | ✓ | ✓ | TBA |


### Lookup Code Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.x.1 | Verify that look-up secret authenticators use an approved random bit generator [SP 800-90Ar1] to generate the list of secrets. Look-up secrets SHALL have at least 20 bits of entropy. | ✓ | ✓ | ✓ | 5.1.2.1 |
 | 2.x.2 | Verify that look-up secrets are delivered securely, and not over a clear text channel (SMS, email, etc) | ✓ | ✓ | ✓ | 5.1.2.1 |

### Multi-factor Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.28** | Verify hardware-based authenticators and verifiers SHOULD resist relevant side-channel (e.g., timing and power-consumption analysis) attacks. Relevant side-channel attacks SHALL be determined by a risk assessment performed by the CSP. |  |  | ✓ | 4.3.2 |
| **2.34** | Verify that users can change their MFA enrollment. | | √ | √ | TBA |

### Service Authentication Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.21** | Integration  secrets SHOULD NOT rely on unchanging memorized secrets, such as API keys or shared privileged accounts. If memorized secrets are required, the credential should not be a default account, and stored with sufficient protection to prevent offline recovery attacks, including local system access. | Software | OS assisted | HSM | 5.1.1.1 |
| **2.29** | Verify memorized secrets, integrations with databases and third party systems, seeds and internal secrets, and API keys are managed securely and not included in the source code or stored within source code repositories. Such storage SHOULD resist offline attacks. The use of a software secure key store (L1), hardware trusted platform module (TPM), or hardware security module (L3) is recommended for memorized secret storage. |  Software | OS assisted | HSM | TBA |

### Credential Storage Requirements
| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.42** | Verifiers SHALL store memorized secrets in a form that is resistant to offline attacks. Memorized secrets SHALL be salted and hashed using a suitable one-way key derivation function. Key derivation functions take a password, a salt, and a cost factor as inputs then generate a password hash. | ✓ | ✓ | ✓ | TBA |
| **2.42** | The salt SHALL be at least 32 bits in length and be chosen arbitrarily so as to minimize salt value collisions among stored hashes. Both the salt value and the resulting hash SHALL be stored for each subscriber using a memorized secret authenticator.. | ✓ | ✓ | ✓ | TBA |
| **2.42** | Verify that if PBKDF2 is used, the cost factor is an iteration count: the more times the PBKDF2 function is iterated, the longer it takes to compute the password hash. Therefore, the iteration count SHOULD be as large as verification server performance will allow, typically at least 10,000 iterations. | ✓ | ✓ | ✓ | TBA |
| **2.42** | Verify that an additional iteration of a key derivation function using a salt value that is secret and known only to the verifier. This salt value, if used, SHALL be generated by an approved random bit generator [SP 800-90Ar1] and provide at least the minimum security strength specified in the latest revision of SP 800-131A (112 bits as of the date of this publication). The secret salt value SHALL be stored separately from the hashed memorized secrets (e.g., in a specialized device like a hardware security module).  |  |  | ✓ | TBA |


### US Agency Requirements

US Agencies have mandatory requirements in relation to NIST 800-63. We have sought to include only the most relevant of the mandatory requirements here that would suit a Level 3 application. There are additional requirements that US government agencies should consider as part of their compliance requirements against NIST 800-63 itself, rather than the Application Security Verification Standard.

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.50** | Verify security controls adhere to the indicated NIST 800-53 baseline or equivalent. | Low | Moderate | High |  TBA |
| **2.45** | Verify the authentication system is compromise resistant, such as memorized secret breaches and/or client device reputation, and other controls. | | | ✓ | 5.2.7 |
| **2.46** | Verify the authentication system is replay resistant, such as ensuring session or bearer tokens cannot be easily be captured or replayed by attackers. | | | ✓ | 5.2.28 |
| **2.4x** | Verify the authentication system explicitly challenges the user on each authentication request. | ✓ | ✓ | ✓ | 5.2.9 |


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

* [NIST 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST 800-63 A - Enrollment and Identity Proofing](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST 800-63 B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST 800-63 C - Federation and Assertions](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://www.owasp.org/index.php/Testing_for_authentication)
* [Password storage cheat sheet](https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet)
* [Forgot password cheat sheet](https://www.owasp.org/index.php/Forgot_Password_Cheat_Sheet)
* [Choosing and Using Security Questions at](https://www.owasp.org/index.php/Choosing_and_Using_Security_Questions_Cheat_Sheet)
