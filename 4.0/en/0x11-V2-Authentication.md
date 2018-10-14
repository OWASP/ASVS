# V2: Authentication Verification Requirements

## Control Objective

Authentication is the act of establishing, or confirming, something (or someone) as authentic, that is, that claims made by a person or about a device are true, resistant to impersonation (phishing), and prevents recovery or interception of memorized secrets (passwords).

ASVS V2 Authentication, V3 Session Management, and V4 Access Controls have been adapted to be a compliant subset of selected NIST 800-63 controls, focused around typical threats and commonly exploited authentication weaknesses. Previous verification requirements have been retired, de-duped, or in most cases adapted to either be identical or strongly aligned with the intent of NIST 800-63 normative (mandatory) requirements. Logging requirements have been moved to the V8 Error and Logging chapter. TLS requirements have been moved to the V10 Communications Chapter.

NIST 800-63 is a modern, evidence based standard, and represents the best advice available, regardless of applicabilty. The standard is helpful for all organizations all over the world, but is particularly relevant to US agencies and those dealing with US agencies.

Implementers requiring the full set of controls should review the entire standard, especially regarding evidence of identity, identity binding, identity assertion, the deployment and management of multi-factor, biometric and crypto devices, security usability, and a great deal more advanced topics. Full compliance with the ASVS 4.0 is not the same as full compliance with NIST 800-63.

### Selecting an appropriate NIST AAL Level

The Application Security Verification Standard has mapped ASVS L1 to AAL1 requirements, L2 to AAL2, and L3 to AAL3. However, the approach of ASVS Level 1 as "essential" controls may not necessarily be the correct AAL level to verify an application or API. For example, if the application is a Level 3 application or has regulatory requirements to be AAL3, Level 3 should be chosen in Sections V2 and V3 Session Management.

The choice of NIST compliant authentication assertion level (AAL) should be performed as per NIST 800-63 guidelines as set out in *Selecting AAL* in [NIST 800-63 Section 6.2](https://pages.nist.gov/800-63-3/sp800-63-3.html#AAL_CYOA). 

We strongly urge everyone to adopt NIST 800-63, and align any policies, guidelines and standards with it, such as we've done here.

## Authentication Verification Requirements

Legend

Applications can always exceed the current level's requirements. To assist in establishing a baseline, the following is used throughout the standard:

* No check tick or "o" - not required at this level
* "o" - recommended, but not required
* "✓" - required

### V2.1 General Authenticator Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.1.1** | Verify physical authenticators can be suspended or revoked, and this is effective including through Identity Providers and Relying Parties (RPs). | o | ✓ | ✓ | 5.2.1 |
| **2.1.2** | Verify one or more of anti-automation, rate limiting, CAPTCHA, increasing delays, IP address restrictions, risk-based restrictions, is in place and effective to prevent breached credential testing, brute forcing, and account lockout attacks. Verify that no more than 100 failed attempts is possible on a single account. | o | ✓ | ✓ | 5.2.2 / 5.1.1.2|
| **2.1.3** | Verify biometric authenticators are used as one factor of multi-factor authentication (either something you have or something you know). |  | o | ✓ | 5.2.3 |
| **2.1.4** | Verify attestation information is available. For more information, please see NIST 800-63 B &sect; 5.2.4 |  |  | ✓ | 5.2.4 |
| **2.1.5** | Verify impersonation resistance against phishing is in place, such as the use of client-side certificates. |  |  | ✓ | 5.2.5 |
| **2.1.6** | Verify where a verifier and CSP are separate, mutually authenticated TLS must be in place between the verifier and the CSP. |  | o | ✓ | 5.2.6 |
| **2.1.7** | Verify verifier compromise resistance by ensuring sufficient strength of approved public key cryptographic algorithms as per standards such as NIST 800-131A or similar. |  |  | ✓ | 5.2.7 |
| **2.1.8** | Verify replay resistance is present, such as the mandated use of OTP devices, cryptographic authenticators, or lookup codes. |  |  | ✓ | 5.2.8 |
| **2.1.9** | Verify authentication intent by the entry of an OTP token in authentication or high value re-authentication flows, or user initiated action resulting in cryptographic device authentication, such as a button press on a FIDO hardware key. |  | o | ✓ | 5.2.9 |
| **2.1.10** | Verify restricted authenticators - such as email and SMS - are not a preferred recovery mechanism or second factor, and at least one alternative is offered to the user first. If the user selects a restricted authenticator, a meaningful warning covering the potential risks of that restricted authenticator SHOULD be presented to the user, including that the future use of the restricted authenticator may be removed in the future. | ✓ | ✓ | ✓ | 5.2.10 |

In the future, email and SMS restricted authenticators will be removed from NIST 800-63 and thus the ASVS, so they should not be the sole form of credential recovery or second factor authenticator.

### V2.2 Authenticator Lifecycle Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.2.1** | Verify generated memorized secret initial values or activation codes SHOULD be securely randomly generated, SHOULD be at least 6 characters long, and MAY contain letters and numbers. | ✓ | ✓ | ✓ | 5.1.1.2 / A.3 |


### V2.3 Authenticator Recovery Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.3.1** | Verify memorized secret credential recovery does not reveal the current memorized secret and that a system generated new memorized secret is not sent in clear text to the user. Lookup codes or a random, time limited one time reset link should be used instead. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.3.1** | Verify memorized secret hints or knowledge based answers (so called "secret questions") are not present. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.3.2** | Verify memorized secret credential recovery does not reveal the current memorized secret in any way. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.3.4** | Verify forgotten memorized secret and other recovery paths use a TOTP or other soft token, mobile push, or other offline recovery mechanism. The use of email or PSTN verifiers (such as SMS tokens) has been deprecated by NIST and SHOULD NOT be used. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.3.5** | Verify identities cannot cannot be re-bound to a different identity (spoofing). | ✓ | ✓ | ✓ | 5.1.1.2 / A.3 |

### V2.4 Memorized Secrets Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.4.1** | Verify that memorized secrets are at least 8 characters in length. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.2** | Verify that memorized secrets 64 characters or longer are permitted. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.3** | Verify that memorized secrets can contain spaces and truncation is not performed. Consecutive multiple spaces MAY optionally be coalesced. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.4** | Verify that Unicode characters are permitted in memorized secrets. A single Unicode code point is considered a character, so 8 emoji or 64 kanji characters should be valid and permitted. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.5** | Verify users can change their memorized secret, and the change validates the current secret. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.6** | Verify that new or changed memorized secrets are validated against a list of compromised secrets, and if found to be compromised, the user is prompted to choose another secret. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.7** | Verify that a password strength meter is provided to help users set a stronger secret. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.8** | Verify that there are no enforced composition rules limiting the type of characters permitted (i.e. there should be no requirement for upper or lower case or numbers or special characters). | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.9** | Verify that there are no enforced arbitary or periodic credential rotation requirements. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.10** | Verify that the user is required to change their password if the credential has found to be compromised. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.11** | Verify that "paste" functionality, browser password helpers, and external password managers are permitted. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.4.12** | Verify that the user can choose to either temporarily view the masked entered password, or temporarily view the last typed character of the password. | ✓ | ✓ | ✓ | 5.1.1.2 |

### V2.5 Credential Storage Requirements

Architects and developers should adhere to this section when building or refactoring code. This section can only be fully verified using source code review, or through secure unit or integration tests. Penetration testing will not be able to identify any of these issues.

The list of approved one way key derivation functions is detailed in NIST 800-63 B section 5.1.1.2, and in [BSI Kryptographische Verfahren: Empfehlungen und Schlussell&auml;ngen (2018)](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile). The latest national or regional algoritm and key length standards can be chosen in place of these choices.

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.5.1** | Verify that memorized secrets are stored in a form that is resistant to offline attacks. Memorized secrets SHALL be salted and hashed using an approved one-way key derivation function. Key derivation functions take a password, a salt, and a cost factor as inputs then generate a password hash. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.5.2** | Verify that the salt is at least 32 bits in length and be chosen arbitrarily so as to minimize salt value collisions among stored hashes. For each credential, a unique salt value and the resulting hash SHALL be stored. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.5.3** | Verify that if PBKDF2 is used, the iteration count SHOULD be as large as verification server performance will allow, typically at least 10,000 iterations. | ✓ | ✓ | ✓ | 5.1.1.2 |
| **2.5.4** | Verify that an additional iteration of a key derivation function using a salt value that is secret and known only to the verifier. This salt value, if used, SHALL be generated by an approved random bit generator [SP 800-90Ar1] and provide at least the minimum security strength specified in the latest revision of SP 800-131A. The secret salt value SHALL be stored separately from the hashed memorized secrets (e.g., in a specialized device like a hardware security module). | o | ✓ | ✓ | 5.1.1.2 |

### Lookup Code Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.x.1 | Verify that look-up secret authenticators use an approved random bit generator [SP 800-90Ar1] to generate the list of secrets. Look-up secrets SHALL have at least 20 bits of entropy. | ✓ | ✓ | ✓ | 5.1.2.1 |
 | 2.x.2 | Verify that look-up secrets are delivered securely, and not over a clear text channel (SMS, email, etc) | ✓ | ✓ | ✓ | 5.1.2.1 |

### Out of Band Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.x.1 | Verify that look-up secret authenticators use an approved random bit generator [SP 800-90Ar1] to generate the list of secrets. Look-up secrets SHALL have at least 20 bits of entropy. | ✓ | ✓ | ✓ | 5.1.2.1 |
 | 2.x.2 | Verify that look-up secrets are delivered securely, and not over a clear text channel (SMS, email, etc) | ✓ | ✓ | ✓ | 5.1.2.1 |

### Single Factor OTP Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.x.1 | Verify that look-up secret authenticators use an approved random bit generator [SP 800-90Ar1] to generate the list of secrets. Look-up secrets SHALL have at least 20 bits of entropy. | ✓ | ✓ | ✓ | 5.1.2.1 |
 | 2.x.2 | Verify that look-up secrets are delivered securely, and not over a clear text channel (SMS, email, etc) | ✓ | ✓ | ✓ | 5.1.2.1 |

### Multi-factor OTP Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.28** | Verify hardware-based authenticators and verifiers SHOULD resist relevant side-channel (e.g., timing and power-consumption analysis) attacks. Relevant side-channel attacks SHALL be determined by a risk assessment performed by the CSP. |  |  | ✓ | 4.3.2 |
| **2.34** | Verify that users can change their MFA enrollment. | | √ | √ | TBA |

### Cryptographic Software and Devices


### Service Authentication Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| **2.21** | Integration secrets SHOULD NOT rely on unchanging memorized secrets, such as API keys or shared privileged accounts. If memorized secrets are required, the credential should not be a default account, and stored with sufficient protection to prevent offline recovery attacks, including local system access. | Software | OS assisted | HSM | 5.1.1.1 |
| **2.29** | Verify memorized secrets, integrations with databases and third party systems, seeds and internal secrets, and API keys are managed securely and not included in the source code or stored within source code repositories. Such storage SHOULD resist offline attacks. The use of a software secure key store (L1), hardware trusted platform module (TPM), or hardware security module (L3) is recommended for memorized secret storage. |  Software | OS assisted | HSM | TBA |



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
