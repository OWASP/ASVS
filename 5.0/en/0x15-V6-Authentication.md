# V6 Authentication

## Control Objective

Authentication is the process of establishing or confirming the authenticity of an individual or device. It involves verifying claims made by a person or about a device, ensuring resistance to impersonation, and preventing the recovery or interception of passwords.

[NIST SP 800-63](https://pages.nist.gov/800-63-3/) is a modern, evidence-based standard, and represents the best advice available, regardless of applicability. The standard is helpful for all organizations all over the world but is particularly relevant to US agencies and those dealing with US agencies.

For this chapter, it was useful to refer to the second section of the NIST standard known as NIST SP 800-63B "Digital Identity Guidelines - Authentication and Lifecycle Management" when preparing requirements.

However, NIST SP 800-63 terminology can sometimes be different and we have therefore tried to use more commonly understood terminology where possible, to make the chapter clearer.

This means that whilst this chapter aligns to a subset of selected NIST SP 800-63B controls, we have focused on common threats and frequently exploited authentication weaknesses. For cases where full NIST SP 800-63 compliance is necessary, please refer to NIST SP 800-63.

## V6.1 Authentication Documentation

This section contains requirements detailing the authentication documentation that should be maintained for an application. This will be crucial to implement and assess how the relevant authentication controls should be configured.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **6.1.1** | [ADDED, SPLIT FROM 2.2.1] Verify that application documentation defines how controls such as rate limiting, anti-automation, and adaptive response, are used to defend against attacks such as credential stuffing and password brute force. The documentation should make clear how these controls are configured and prevent malicious account lockout. | 1 | v5.0.be-1.2.6 |
| **6.1.2** | [ADDED] Verify that a list of context specific words are documented in order to prevent their use in passwords. | 2 | v5.0.be-1.2.5 |
| **6.1.3** | [MODIFIED, SPLIT TO 2.2.11, COVERS 1.2.3] Verify that, if the application includes multiple authentication pathways, these are all documented together with the security controls and authentication strength which should be consistently enforced across them. | 2 | v5.0.be-1.2.4 |

## V6.2 Password Security

Passwords, called "Memorized Secrets" by NIST SP 800-63, include passwords, PINs, unlock patterns, pick the correct kitten or another image element, and passphrases. They are generally considered "something you know", and often used as single-factor authentication mechanism. From L2 onwards, multi-factor authentication mechanisms are required, where passwords may be one of those factors.

As such, this section contains requirements for making sure that passwords are created and handled securely.

The requirements in this section mostly relate to [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **6.2.1** | [MODIFIED] Verify that user set passwords are at least 8 characters in length although a minimum of 15 characters is strongly recommended. | 1 | v5.0.be-2.1.1 |
| **6.2.2** | [GRAMMAR] Verify that users can change their password. | 1 | v5.0.be-2.1.5 |
| **6.2.3** | Verify that password change functionality requires the user's current and new password. | 1 | v5.0.be-2.1.6 |
| **6.2.4** | [MODIFIED, SPLIT TO 2.1.13] Verify that passwords submitted during account registration or password change are checked against an available set of, at least, the top 3000 passwords which match the application's password policy, e.g. minimum length. | 1 | v5.0.be-2.1.7 |
| **6.2.5** | Verify that there are no password composition rules limiting the type of characters permitted. There should be no requirement for upper or lower case or numbers or special characters. | 1 | v5.0.be-2.1.9 |
| **6.2.6** | [MODIFIED] Verify that password input fields use type=password to mask the entry. Applications may allow the user to temporarily view the entire masked password, or the last typed character of the password. | 1 | v5.0.be-2.1.12 |
| **6.2.7** | Verify that "paste" functionality, browser password helpers, and external password managers are permitted. | 1 | v5.0.be-2.1.11 |
| **6.2.8** | [MODIFIED] Verify that the application verifies the user's password exactly as received from the user, without any modifications such as truncation or case transformation. | 2 | v5.0.be-2.1.3 |
| **6.2.9** | [MODIFIED] Verify that passwords of at least 64 characters are permitted. | 2 | v5.0.be-2.1.2 |
| **6.2.10** | [MODIFIED, LEVEL L1 > L2] Verify that a user's password stays valid until it is discovered to be compromised or the user rotates it. The application must not require periodic credential rotation. | 2 | v5.0.be-2.1.10 |
| **6.2.11** | [ADDED] Verify that the documented list of context specific words is used to prevent easy to guess passwords being created. | 2 | v5.0.be-2.1.14 |
| **6.2.12** | [ADDED, SPLIT FROM 2.1.7, LEVEL L1 > L3] Verify that passwords submitted during account registration or password changes are checked against a set of breached passwords. | 3 | v5.0.be-2.1.13 |

Possible sources of frequently used passwords for requirement 2.1.7 include:

* <https://github.com/danielmiessler/SecLists/tree/master/Passwords>
* <https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt>

## V6.3 General Authentication Security

This section contains general requirements for the security of authentication mechanisms as well as setting out the different expectations for levels including requiring multi-factor for L2 and supporting hardware-based mechanisms for L3.

Note that NIST SP 800-63 considers email as [not acceptable](https://pages.nist.gov/800-63-FAQ/#q-b11) as an authentication mechanism.

The requirements in this section relate to a variety of sections of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html), including: [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling), and [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding).

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **6.3.1** | [MODIFIED, SPLIT TO 1.2.6] Verify that controls to prevent attacks such as credential stuffing and password brute force are implemented according to the application's security documentation. | 1 | v5.0.be-2.2.1 |
| **6.3.2** | [ADDED, SPLIT FROM 2.2.4] Verify that the application requires users to either use a multi-factor authentication mechanism or a combination of single-factor authentication mechanisms. | 2 | v5.0.be-2.2.9 |
| **6.3.3** | [ADDED, SPLIT FROM 1.2.4] Verify that, if the application includes multiple authentication pathways, there are no undocumented pathways and that security controls and authentication strength are enforced consistently. | 2 | v5.0.be-2.2.11 |
| **6.3.4** | [ADDED, SPLIT FROM 2.2.3] Verify that users are notified of suspicious authentication attempts. This may include successful or unsuccessful authentication from an unusual location or client, partially successful authentication with only one of multiple factors, successful or unsuccessful authentication after a long period of inactivity or successful authentication after several unsuccessful attempts. | 3 | v5.0.be-2.2.10 |
| **6.3.5** | [MODIFIED] Verify that email is not used as either a single-factor or multi-factor authentication mechanism. | 3 | v5.0.be-2.2.2 |
| **6.3.6** | [MODIFIED, SPLIT TO 2.2.10, COVERS 2.5.5] Verify that users are notified after updates to authentication details, such as credential resets or modification of the username or email address. | 3 | v5.0.be-2.2.3 |
| **6.3.7** | [MODIFIED, SPLIT TO 2.2.9, MERGED FROM 2.2.7, 2.3.2] Verify that a hardware-based authentication mechanism is supported that provides impersonation resistance against phishing attacks (such as WebAuthn) and verifies intent to authenticate by requiring a user-initiated action (such as a button press on a FIDO hardware key). | 3 | v5.0.be-2.2.4 |
| **6.3.8** | [ADDED] Verify that valid users cannot be deduced from failed authentication challenges, such as by basing on error messages, HTTP response codes, or different response times. Registration and forgot password functionality should also have this protection. | 3 | v5.0.be-2.2.8 |

## V6.4 Authentication Factor Lifecycle and Recovery

Authentication factors may include passwords, soft tokens, hardware tokens, and biometric devices. Securely handling the lifecycle of these mechanisms is critical to the security of an application and this section includes requirements related to this.

The requirements in this section mostly relate to [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) or [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **6.4.1** | [MODIFIED, MOVED FROM 2.3.1] Verify that system generated initial passwords or activation codes are securely randomly generated, follow the existing password policy, and expire after a short period of time or after they are initially used. These initial secrets must not be permitted to become the long term password. | 1 | v5.0.be-2.5.8 |
| **6.4.2** | [GRAMMAR] Verify that password hints or knowledge-based authentication (so-called "secret questions") are not present. | 1 | v5.0.be-2.5.2 |
| **6.4.3** | [MODIFIED] Verify that a secure process for resetting a forgotten password is implemented, that does not bypass any enabled multi-factor authentication mechanisms. | 2 | v5.0.be-2.5.6 |
| **6.4.4** | [GRAMMAR, LEVEL L2 > L1] Verify that if OTP or other multi-factor authentication factors are lost, that evidence of identity proofing is performed at the same level as during enrollment. | 2 | v5.0.be-2.5.7 |
| **6.4.5** | [MODIFIED, MOVED FROM 2.3.3] Verify that renewal instructions for authentication mechanisms which expire are sent with enough time to be carried out before the old authentication mechanism expires, configuring automated reminders if necessary. | 3 | v5.0.be-2.5.9 |
| **6.4.6** | [ADDED] Verify that administrative users can initiate the password reset process for the user, but that this does not allow them to change or choose the user's password. This prevents a situation where they know the user's password. | 3 | v5.0.be-2.5.10 |

## V6.5 General Multi-factor authentication requirements

This section provides general guidance that will be relevant to various different multi-factor authentication methods.

The mechanisms include:

* Lookup Secrets
* Time based One-time Passwords (TOTPs)
* Out-of-Band mechanisms

Lookup secrets are pre-generated lists of secret codes, similar to Transaction Authorization Numbers (TAN), social media recovery codes, or a grid containing a set of random values. This type of authentication mechanism is considered "something you have" since the codes are random so you need to have stored them somewhere.

Time based One-time Passwords (TOTPs) are physical or soft tokens that display a continually changing pseudo-random one-time challenge. This type of authentication mechanism is considered "something you have". Multi-factor TOTPs are similar to single-factor TOTPs, but require a valid PIN code, biometric unlocking, USB insertion or NFC pairing or some additional value (such as transaction signing calculators) to be entered to create the final OTP.

More details on out-of-band mechanisms will be provided in a subsequent section.

The requirements in these sections mostly relate to [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators), and [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **6.5.1** | [MODIFIED, MERGED FROM 2.8.4, SPLIT FROM 2.7.3, COVERS 2.2.6] Verify that lookup secrets, out-of-band authentication requests or codes, and time-based, one-time passwords (TOTPs) are only usable once. | 2 | v5.0.be-2.6.1 |
| **6.5.2** | [MODIFIED, SPLIT TO 2.6.4] Verify that, when being stored in the application's backend, lookup secrets with less than 112 bits of entropy (19 random alphanumeric characters or 34 random digits) are hashed with an approved password storage hashing algorithm that incorporates a 32-bit random salt. A standard hash function can be used if the secret has 112 bits of entropy or more. | 2 | v5.0.be-2.6.2 |
| **6.5.3** | [MODIFIED, MERGED FROM 2.8.3, SPLIT FROM 2.7.6] Verify that lookup secrets, out-of-band authentication code, and time-based, one-time password seeds, are generated using a Cryptographically Secure Pseudorandom Number Generator (CSPRNG) to avoid predictable values. | 2 | v5.0.be-2.6.3 |
| **6.5.4** | [ADDED, SPLIT FROM 2.6.2, 2.7.6] Verify that lookup secrets and out-of-band authentication codes have a minimum of 20 bits of entropy (typically 4 random alphanumeric characters or 6 random digits is sufficient). | 2 | v5.0.be-2.6.4 |
| **6.5.5** | [MODIFIED, MOVED FROM 2.7.2, MERGED FROM 2.8.1] Verify that out-of-band authentication requests, codes, or tokens, as well as time-based, one-time passwords (TOTPs) have a defined lifetime. For out of band this should be 10 minutes and for TOTP this should be as short as possible, usually 30 seconds. | 2 | v5.0.be-2.6.5 |
| **6.5.6** | [MODIFIED, MOVED FROM 2.8.6, LEVEL L2 > L3] Verify that any authentication factor (including physical devices) can be revoked in case of theft or other loss. | 3 | v5.0.be-2.6.6 |
| **6.5.7** | [MODIFIED, MOVED FROM 2.8.7, LEVEL L2 > L3] Verify that biometric authentication mechanisms are only used as secondary factors together with either something you have or something you know. | 3 | v5.0.be-2.6.7 |
| **6.5.8** | [ADDED] Verify that time-based OTPs are checked based on a time source from a trusted service and not from an untrusted or client provided time. | 3 | v5.0.be-2.6.8 |

## V6.6 Out-of-Band authentication mechanisms

This will generally involve the authentication server communicating with a physical device over a secure secondary channel. Examples include push notifications to mobile devices and One-time Passwords (OTPs) sent to a user via SMS. This type of authentication mechanism is considered "something you have".

Unsafe out-of-band authentication mechanisms such as e-mail and VOIP are not permitted. PSTN and SMS authentication are currently considered to be ["restricted" authentication mechanisms](https://pages.nist.gov/800-63-FAQ/#q-b01) by NIST and should be deprecated in favor of push notifications or similar. If you need to use telephone or SMS out-of-band authentication, please see NIST SP 800-63B [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network).

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **6.6.1** | [MODIFIED] Verify that authentication mechanisms using the Public Switched Telephone Network (PSTN) to deliver One-time Passwords (OTPs) via phone or SMS are offered only when alternate stronger methods (such as push notifications) are also offered and when the service provides information on their security risks to users. For L3 applications, phone and SMS must not be available as options. | 2 | v5.0.be-2.7.1 |
| **6.6.2** | [MODIFIED, SPLIT TO 2.6.1] Verify that out-of-band authentication requests, codes, or tokens are only usable for the original authentication request for which they were generated and not a previous or subsequent one. | 2 | v5.0.be-2.7.3 |
| **6.6.3** | [ADDED] Verify that a code based out-of-band authentication mechanism is protected against brute force attacks by using either rate limiting or a code with at least 64 bits of entropy. | 2 | v5.0.be-2.7.7 |
| **6.6.4** | [ADDED] Verify that, where push notifications are used for multi-factor authentication, rate limiting or number matching is used to prevent push bombing attacks. | 3 | v5.0.be-2.7.8 |

## V6.7 Cryptographic authentication mechanism

Cryptographic authentication mechanisms include smart cards or FIDO keys, where the user has to plug in or pair the cryptographic device to the computer to complete authentication. The authentication server will send a challenge nonce to the cryptographic device or software, and the device or software calculates a response based upon a securely stored cryptographic key. The requirements in this section provide implementation specific guidance for these mechanisms with guidance on cryptographic algorithms being covered in the "Cryptography" chapter.

Where shared or secret keys are used for cryptographic authentication, these should be stored using the same mechanisms as other system secrets, as documented in the "Secret Management" section in the "Configuration" chapter.

The requirements in this section mostly relate to [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **6.7.1** | [MODIFIED, SPLIT TO 14.8.1, LEVEL L2 > L3] Verify that the certificates used to verify cryptographic authentication assertions are stored in a way protects them from modification. | 3 | v5.0.be-2.9.1 |
| **6.7.2** | [LEVEL L2 > L3] Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device. | 3 | v5.0.be-2.9.2 |

## V6.8 Authentication with an Identity Provider

Identity Providers (IdPs) provide federated identity for users. Users will often have more than one identity with multiple IdPs, such as an enterprise identity using Azure AD, Okta, Ping Identity or Google, or consumer identity using Facebook, Twitter, Google, or WeChat, to name just a few common alternatives. This list is not an endorsement of these companies or services, but simply an encouragement for developers to consider the reality that many users have many established identities. Organizations should consider integrating with existing user identities, as per the risk profile of the IdPs's strength of identity proofing. For example, it is unlikely a government organization would accept a social media identity as a login for sensitive systems, as it is easy to create fake or throw away identities, whereas a mobile game company may well need to integrate with major social media platforms to grow their active player base.

Secure use of external identity providers requires careful configuration and verification to prevent identity spoofing or forged assertions. This section provides requirements to address these risks.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **6.8.1** | [ADDED] Verify that, if the application supports multiple identity providers (IdPs), the user's identity cannot be spoofed via another supported identity provider (eg. by using the same user identifier). Usually, the application should register and identify the user using a combination of the IdP ID (serving as a namespace) and the user's ID in the IdP. | 2 | v5.0.be-2.11.1 |
| **6.8.2** | [ADDED] Verify that the presence and integrity of digital signatures on authentication assertions (for example on JWTs or SAML assertions) are always validated, rejecting any assertions that are unsigned or have invalid signatures. | 2 | v5.0.be-2.11.2 |
| **6.8.3** | [ADDED] Verify that SAML assertions are uniquely processed and used only once within the validity period to prevent replay attacks. | 2 | v5.0.be-2.11.3 |

## References

For more information, see also:

* [NIST SP 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST SP 800-63A - Enrollment and Identity Proofing](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST SP 800-63B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST SP 800-63C - Federation and Assertions](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST SP 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [OWASP Cheat Sheet - Password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Forgot password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Choosing and using security questions](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
* [CISA Guidance on "Number Matching"](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
