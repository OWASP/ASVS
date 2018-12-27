# V2: Authentication Verification Requirements

## Control Objective

Authentication is the act of establishing, or confirming, someone (or something) as authentic and that claims made by a person or about a device are correct, resistant to impersonation, and prevent recovery or interception of passwords.

ASVS V2 Authentication, V3 Session Management, and V4 Access Controls have been adapted to be a compliant subset of selected NIST 800-63 controls, focused around common threats and commonly exploited authentication weaknesses. Previous verification requirements have been retired, de-duped, or in most cases adapted to be strongly aligned with the intent of mandatory NIST 800-63 requirements.

NIST 800-63 is a modern, evidence-based standard, and represents the best advice available, regardless of applicability. The standard is helpful for all organizations all over the world but is particularly relevant to US agencies and those dealing with US agencies.

Implementers requiring the full set of controls should review the entire standard, especially regarding evidence of identity, identity binding, identity assertion, the deployment and management of multi-factor, biometric and crypto devices, security usability, and more.

 NB: We use the term "password" when NIST uses "memorized secret" throughout this standard.

### Selecting an appropriate NIST AAL Level

The Application Security Verification Standard has mapped ASVS L1 to AAL1 requirements, L2 to AAL2, and L3 to AAL3. However, the approach of ASVS Level 1 as "essential" controls may not necessarily be the correct AAL level to verify an application or API. For example, if the application is a Level 3 application or has regulatory requirements to be AAL3, Level 3 should be chosen in Sections V2 and V3 Session Management.

The choice of NIST compliant authentication assertion level (AAL) should be performed as per NIST 800-63 guidelines as set out in *Selecting AAL* in [NIST 800-63 Section 6.2](https://pages.nist.gov/800-63-3/sp800-63-3.html#AAL_CYOA). 

## Warning

While we strongly urge everyone to adopt NIST 800-63, full compliance with the ASVS 4.0 is not the same as full compliance with NIST 800-63.

## Authentication Verification Requirements

Legend

Applications can always exceed the current level's requirements. The following keys are used throughout this standard:

* No check tick or "o" - not required at this level
* "o" - recommended, but not required
* "✓" - required

### V2.1 General Authenticator Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.1.1 | Verify revocability of physical authenticators in case of theft or other loss. Ensure that revocation is immediately effective across all Identity Providers and Relying Parties. | o | ✓ | ✓ | 5.2.1 |
| 2.1.2 | Verify that one or more anti-automation controls--including rate limiting, CAPTCHA, increasing delays, IP address restrictions, risk-based restrictions--are in place and effective to mitigate breached credential testing, brute force, and account lockout attacks. Verify that no more than 100 failed attempts is possible on a single account. | ✓ | ✓ | ✓ | 5.2.2 / 5.1.1.2|
| 2.1.3 | Verify that biometric authenticators are limited to use only as secondary factors in conjunction with either something you have and something you know. |  | o | ✓ | 5.2.3 |
| 2.1.5 | Verify impersonation resistance against phishing, such as the use of multi-factor authentication, cryptographic devices with intent (such as connected keys with a push to authenticate), or at higher AAL levels, client-side certificates. |  | o | ✓ | 5.2.5 |
| 2.1.6 | Verify that in cases where a verifier and CSP are separate, mutually authenticated TLS is in place between the two endpoints. |  | o | ✓ | 5.2.6 |
| 2.1.8 | Verify replay resistance through the mandated use of OTP devices, cryptographic authenticators, or lookup codes. |  | o | ✓ | 5.2.8 |
| 2.1.9 | Verify intent to authenticate by requiring the entry of an OTP token or user-initiated action such as a button press on a FIDO hardware key. |  | o | ✓ | 5.2.9 |
| 2.1.10 | Verify that restricted authenticators--such as email and SMS--are not a preferred recovery mechanism or second factor, and at least one alternative is offered to the user first. If the user selects a restricted authenticator, a meaningful warning covering the potential risks of that restricted authenticator SHOULD be presented to the user, including that the future use of the restricted authenticator may be removed in the future. | ✓ | ✓ | ✓ | 5.2.10 |

NIST considers email and SMS as "restricted" plain text authentication channels. As restricted authenticators, they will be removed from NIST 800-63 and thus the ASVS at some point the future. Authenticator agility is essential to future-proof applications. Refactor application verifiers to allow additional authenticators as per user preferences, as well as allowing retiring deprecated or unsafe authenticators in an orderly fashion.  

### V2.2 Authenticator Lifecycle Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.2.1 | Verify system generated initial passwords or activation codes SHOULD be securely randomly generated, SHOULD be at least 6 characters long, and MAY contain letters and numbers. | ✓ | ✓ | ✓ | 5.1.1.2 / A.3 |
| 2.2.2 | Verify that enrollment and use of subscriber-provided authentication devices are supported, such as a U2F or FIDO tokens. | ✓ | ✓ | ✓ | 6.1.3 |
| 2.2.3 | Verify that renewal instructions are sent with sufficient time to renew time bound authenticators. | ✓ | ✓ | ✓ | 6.1.4 |

There are additional requirements in section 6.2 for US agencies that are out of scope for the ASVS. 

### V2.3 Authenticator Recovery Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.3.1 | Verify that a system generated activation or recovery password is not sent in clear text to the user. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.3.2 | Verify password hints or knowledge-based answers (so-called "secret questions") are not present. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.3.3 | Verify password credential recovery does not reveal the current password in any way. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.3.4 | Verify forgotten password, and other recovery paths use a TOTP or other soft token, mobile push, or another offline recovery mechanism. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.3.5 | Verify identities cannot be re-bound to a different identity (spoofing), and shared accounts are not present ("root", "admin", or "sa"). | ✓ | ✓ | ✓ | 5.1.1.2 / A.3 |
| 2.3.6 | Verify that if one or more multi-factor authentication factors are lost, that identity proofing and binding is performed at the same level as during enrollment. Once replaced, the verifier MAY use a single factor to re-bind the account to the new factor. | ✓ | ✓ | ✓ | 6.1.2.3 |
| 2.3.7 | Verify that if an authentication factor is changed or replaced, that the user is notified of this event. | ✓ | ✓ | ✓ | 6.1.2.3 |

The use of email or PSTN verifiers (such as SMS tokens) has been deprecated by NIST and SHOULD NOT be used.

### V2.4 Memorized Secrets Authenticator Requirements

Memorized secrets are passwords, PINs, unlock patterns, pick the correct kitten or another image element, and passphrases. They are generally considered "something you know", and often used as single factor authenticators. There are significant challenges to the continued use of single-factor authentication, including billions of valid usernames and passwords disclosed on the Internet, default or weak passwords, rainbow tables and ordered dictionaries of the most common passwords.

Memorized secrets are not sufficient to protect against today's threats. The ASVS has long required multi-factor authentication. We have not relaxed this point of view. NIST 800-63 recommends but does not require multi-factor authentication at IAL1/AAL1. The ASVS Leadership Team strongly feels that it is essential to start the process of universal multi-factor authentication, as it defeats the most common attacks against passwords. Therefore, we have set multi-factor authentication as a baseline L1 requirement.

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.4.1 | Verify that passwords are at least 8 characters in length. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.2 | Verify that passwords 64 characters or longer are permitted. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.3 | Verify that passwords can contain spaces and truncation is not performed. Consecutive multiple spaces MAY optionally be coalesced. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.4 | Verify that Unicode characters are permitted in passwords. A single Unicode code point is considered a character, so 8 emoji or 64 kanji characters should be valid and permitted. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.5 | Verify users can change their password, and the change validates the current secret. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.6 | Verify that new or changed passwords are validated against a list of compromised secrets, and if found to be compromised, the user is prompted to choose another secret. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.7 | Verify that a password strength meter is provided to help users set a stronger secret. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.8 | Verify that there are no password composition rules limiting the type of characters permitted. There should be no requirement for upper or lower case or numbers or special characters. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.9 | Verify that there are no arbitrary or periodic credential rotation requirements. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.10 | Verify that the user is required to change their password if the credential has found to be compromised. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.11 | Verify that "paste" functionality, browser password helpers, and external password managers are permitted. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.4.12 | Verify that the user can choose to either temporarily view the masked entered password, or temporarily view the last typed character of the password. | ✓ | ✓ | ✓ | 5.1.1.2 |

### V2.5 Credential Storage Requirements

Architects and developers should adhere to this section when building or refactoring code. This section can only be fully verified using source code review or through  secure unit or integration tests. Penetration testing cannot identify any of these issues.

The list of approved one-way key derivation functions is detailed in NIST 800-63 B section 5.1.1.2, and in [BSI Kryptographische Verfahren: Empfehlungen und Schlussell&auml;ngen (2018)](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile). The latest national or regional algorithm and key length standards can be chosen in place of these choices.

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.5.1 | Verify that passwords are stored in a form that is resistant to offline attacks. Passwords SHALL be salted and hashed using an approved one-way key derivation or password hashing function. Key derivation and password hashing functions take a password, and a cost factor as inputs then generate a password hash. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.5.2 | Verify that the salt is at least 32 bits in length and be chosen arbitrarily to minimize salt value collisions among stored hashes. For each credential, a unique salt value and the resulting hash SHALL be stored. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.5.3 | Verify that if PBKDF2 is used, the iteration count SHOULD be as large as verification server performance will allow, typically at least 100,000 iterations. | ✓ | ✓ | ✓ | 5.1.1.2 |
| 2.5.4 | Verify that if bcrypt is used, the work factor SHOULD be as large as verification server performance will allow, typically at least 13. | ✓ | ✓ | ✓ |  |
| 2.5.5 | Verify that an additional iteration of a key derivation function using a salt value that is secret and known only to the verifier. This salt value, if used, SHALL be generated by an approved random bit generator [SP 800-90Ar1] and provide at least the minimum security strength specified in the latest revision of SP 800-131A. The secret salt value SHALL be stored separately from the hashed passwords (e.g., in a specialized device like a hardware security module). | o | ✓ | ✓ | 5.1.1.2 |

### V2.6 Look-up Secret Verifier Requirements

Look up secrets are pre-generated lists of secret codes, similar to Transaction Authorization Numbers (TAN), Google Recovery Codes, or a grid containing a set of random values. These are distributed securely to users. These lookup codes are used once, and once all used, the lookup secret list is discarded. This type of authenticator is considered "something you have".

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.6.1 | Verify that lookup secrets can be used only once. | o | ✓ | ✓ | 5.1.2.2 |
| 2.6.2 | Verify that lookup secrets have sufficient randomness (112 bits of entropy), or if less than 112 bits of entropy, salted with a unique and random 32-bit salt and hashed with an approved one-way hash. | o | ✓ | ✓ | 5.1.2.2 |
| 2.6.3 | Verify that lookup secrets are resistant to offline attacks, such as predictable values. | o | ✓ | ✓ | 5.1.2.2 |
| 2.6.4 | Verify that lookup secrets are rate limited, particularly when using less than 64 bits of entropy. | o | ✓ | ✓ | 5.1.2.2 |

### V2.7 Out of Band Verifier Requirements

Out of band authenticators are physical devices that can communicate with the verifier over a secure secondary channel. Examples include push notifications to mobile devices. This type of authenticator is considered "something you have". When a user wishes to authenticate, the verifying application sends a message to the out of band authenticator via a connection to the authenticator directly or indirectly through a third party service. The message contains an authentication key (typically a random six digit number or a modal approval dialog). The verifying application waits to receive the authentication key through the primary channel and compares the hash of the received value to the hash of the original authentication key. If they match, the out of band verifier can assume that the user has authenticated.

The ASVS assumes that only a few developers will be developing new out of band authenticators, such as push notifications, and thus the following ASVS controls apply to verifiers, such as authentication API, applications, and single sign-on implementations. If developing a new out of band authenticator, please refer to NIST 800-63B &sect; 5.1.3.1.

Unsafe out of band authenticators such as e-mail and VOIP is not permitted. PSTN and SMS authentication are currently restricted and should be deprecated in favor of push notifications or similar. If you need to use telephone or SMS out of band authentication, please see &sect; 5.1.3.3.

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.7.1 | Verify that prohibited unencrypted out of band authenticators, such as e-mail or VOIP, is not in use. | ✓ | ✓ | ✓ | 5.1.3.1 |
| 2.7.2 | Verify that restricted out of band authenticators, such as SMS or PSTN, are not offered by default, and stronger alternatives such as push notifications are offered first. | ✓ | ✓ | ✓ | 5.1.3.2 |
| 2.7.3 | Verify that the out of band authenticator and verifier communicates over a secure independent channel. | ✓ | ✓ | ✓ | 5.1.3.2 |
| 2.7.4 | Verify that the out of band verifier retains only a hashed version of the authentication key. | ✓ | ✓ | ✓ | 5.1.3.2 |
| 2.7.5 | Verify that the out of band verifier rejects out of band authentication attempts after 10 minutes. | ✓ | ✓ | ✓ | 5.1.3.2 |
| 2.7.6 | Verify that the out of band verifier authentication keys is only usable once, and only for the original authentication request. | ✓ | ✓ | ✓ | 5.1.3.2 |
| 2.7.7 | Verify that the authentication key is generated by a secure random number generator, containing at least 20 bits of entropy (typically a six digital random number is sufficient). | ✓ | ✓ | ✓ | 5.1.3.2 |
| 2.7.8 | Verify that rate limiting is in place if the authentication secret uses less than 64 bits of entropy (typically all numeric authenticators). | ✓ | ✓ | ✓ | 5.1.3.2 |

### V2.8 Single Factor OTP Requirements

Single factor one time passwords are physical or soft tokens that display a continually changing pseudo-random one time challenge. These devices make phishing (impersonation) difficult, but not impossible. This type of authenticator is considered "something you have".

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.8.1 | Verify that symmetric keys used to verify submitted codes is highly protected, such as using an HSM or OS based key storage. | o | ✓ | ✓ | 5.1.4.2 |
| 2.8.2 | Verify that approved cryptographic algorithms are used in the generation, seeding, and verification. | o | ✓ | ✓ | 5.1.4.2 |
| 2.8.3 | Verify that time-based tokens have a defined lifetime before needing re-seeding or replacement. | o | o | ✓ | 5.1.4.2 |
| 2.8.4 | Verify that time-based OTP can be used only once within the validity period. | ✓ | ✓ | ✓ | 5.1.4.2 |
| 2.8.5 | Verify that rate limiting is in place if the authentication secret uses less than 64 bits of entropy (typically all numeric OTP authenticators). | o | ✓ | ✓ | 5.1.4.2 |


### V2.9 Multi-factor OTP Verifier Requirements

Multi-factor tokens are similar to single factor OTP tokens, but require a valid PIN code, biometric unlocking, USB insertion or NFC pairing or some additional value (such as transaction signing calculators) to be entered to create the final OTP. 

In the context of this section, the claimant should be read as the person or organization who enrolled the OTP device. Claimants may not necessarily be the person in possession of the OTP device. 

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.9.1 | Verify that symmetric keys used to verify submitted codes is highly protected, such as using an HSM or OS based key storage. | o | ✓ | ✓ | 5.1.5.2 |
| 2.9.2 | Verify that approved cryptographic algorithms are used in the generation, seeding, and verification. | o | ✓ | ✓ | 5.1.5.2 |
| 2.9.3 | Verify that MFA OTP device is a multi-factor device. Otherwise, the device should be treated as a single factor OTP device. | o | o | ✓ | 5.1.5.2 |
| 2.9.4 | Verify that time-based OTPs have a defined lifetime before needing re-seeding or replacement. | o | o | ✓ | 5.1.5.2 |
| 2.9.5 | Verify that time-based OTP can be used only once within the validity period. | o | ✓ | ✓ | 5.1.5.2 |
| 2.9.6 | Verify that if a time-based OTP is re-used during the validity period, a warning is presented to the claimant, and optionally the user or the existing session. | o | ✓ | ✓ | 5.1.5.2 |
| 2.9.7 | Verify that rate limiting is in place if the authentication secret uses less than 64 bits of entropy (typically all numeric OTP authenticators). | o | ✓ | ✓ | 5.1.5.2 |

### V2.10 Cryptographic Software and Devices Verifier Requirements

Cryptographic security keys are smart cards or FIDO keys, where the user has to plug in or pair the cryptographic device to the computer to complete authentication. Verifiers send a challenge nonce to the cryptographic devices or software, and the device or software calculates a response based upon a securely stored cryptographic key. 

The requirements for single factor cryptographic devices and software, and multi-factor cryptographic devices and software are the same, as verification of the cryptographic authenticator proves possession of the authentication factor. 

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.10.1 | Verify that cryptographic keys used in verification are stored securely and protected against disclosure, such as using a TPM or HSM, or an OS service that can use this secure storage. | ✓ | ✓ | ✓ | 5.1.7.2 |
| 2.10.2 | Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device. | ✓ | ✓ | ✓ | 5.1.7.2 |
| 2.10.3 | Verify that approved cryptographic algorithms are used in the generation, seeding, and verification. | o | ✓ | ✓ | 5.1.7.2 |

### V2.11 Service Authentication Requirements

| # | Description | L1 | L2 | L3 | NIST &sect; |
| --- | --- | --- | --- | -- | -- |
| 2.11.1 | Integration secrets SHOULD NOT rely on unchanging passwords, such as API keys or shared privileged accounts. If passwords are required, the credential should not be a default account and stored with sufficient protection to prevent offline recovery attacks, including local system access. | Software | OS assisted | HSM | 5.1.1.1 |
| 2.11.2 | Verify passwords, integrations with databases and third-party systems, seeds and internal secrets, and API keys are managed securely and not included in the source code or stored within source code repositories. Such storage SHOULD resist offline attacks. The use of a secure software key store (L1), hardware trusted platform module (TPM), or a hardware security module (L3) is recommended for password storage. |  Software | OS assisted | HSM | TBA |

### Additional US Agency Requirements

US Agencies have mandatory requirements concerning NIST 800-63. The Application Security Verification Standard has always been about the 80% of controls that apply to nearly 100% of apps, and not the last 20% of advanced controls or those that have limited applicability. As such, the ASVS is a strict subset of NIST 800-63, especially for IAL1/2 and AAL1/2 classifications, but is not sufficiently comprehensive, particularly concerning IAL3/AAL3 classifications. 

We strongly urge US government agencies to review and implement NIST 800-63 in its entirety.

## Glossary of terms

| Term | Meaning |
| -- | -- |
| CSP | Credential Service Provider also called an Identity Provider |
| Authenticator | TBA |
| Verifier | "An entity that verifies the claimant's identity by verifying the claimant's possession and control of one or two authenticators using an authentication protocol. To do this, the verifier may also need to validate credentials that link the authenticator(s) to the subscriber's identifier and check their status" |
| OTP | One-time password |
| SFA | Single factor authenticators, such as something you know (memorized secrets, passwords, passphrases, PINs), something you are (biometrics, fingerprint, face scans), or something you have (OTP tokens, a cryptographic device such as a smart card),  |
| MFA | Multi factor authenticator, which includes two or more single factors |

## References

For more information, see also:

* [NIST 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST 800-63 A - Enrollment and Identity Proofing](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST 800-63 B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST 800-63 C - Federation and Assertions](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://www.owasp.org/index.php/Testing_for_authentication)
* [OWASP Cheat Sheet - Password storage](https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet)
* [OWASP Cheat Sheet - Forgot password](https://www.owasp.org/index.php/Forgot_Password_Cheat_Sheet)
* [OWASP Cheat Sheet - Choosing and using security questions](https://www.owasp.org/index.php/Choosing_and_Using_Security_Questions_Cheat_Sheet)

