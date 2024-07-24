# V2 Authentication

## Control Objective

Authentication is the process of establishing or confirming the authenticity of an individual or device. It involves verifying claims made by a person or about a device, ensuring resistance to impersonation, and preventing the recovery or interception of passwords.

When the ASVS was initially released, the combination of username and password was the most common form of authentication, except in high-security systems. Multi-factor Authentication (MFA) was commonly accepted in security circles but rarely required elsewhere. As the number of password breaches increased, the idea that usernames are somehow confidential and passwords unknown, rendered many security controls untenable. For example, NIST SP 800-63 considers usernames and Knowledge Based Authentication (KBA) as public information, email as [not allowed](https://pages.nist.gov/800-63-FAQ/#q-b11), SMS as a ["restricted" authenticator type](https://pages.nist.gov/800-63-FAQ/#q-b01), and passwords as pre-breached. This reality renders knowledge-based authenticators, SMS and email recovery, and password-related controls such as history, complexity, and rotation, ineffective. These controls have always been less than helpful, often forcing users to come up with weak passwords every few months, but with the release of over 5 billion username and password breaches, it's time to move on.

Of all the chapters in the ASVS, the authentication and session management chapters have changed the most. Adoption of effective, evidence-based leading practice will be challenging for many, and that's perfectly okay. We have to start the transition to a post-password future now.

## NIST SP 800-63 - Modern, evidence-based authentication standard

[NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) is a modern, evidence-based standard, and represents the best advice available, regardless of applicability. The standard is helpful for all organizations all over the world but is particularly relevant to US agencies and those dealing with US agencies.

NIST SP 800-63 terminology can be a little confusing at first, especially if you're only used to username + password authentication. Advancements in modern authentication are necessary, so we have to introduce terminology that will become commonplace in the future, but we do understand the difficulty in understanding until the industry settles on these new terms. We have provided a glossary at the end of this chapter to assist. We have rephrased many requirements to satisfy the intent of the requirement, rather than the letter of the requirement. For example, the ASVS uses the term "password" while NIST uses "memorized secret" throughout this standard.

The V2 Authentication and V3 Session Management chapters in the ASVS, and to a lesser extent the V4 Access Control chapter, have been adapted to align as a compliant subset of selected NIST SP 800-63B controls. This adaptation focuses on common threats and frequently exploited authentication weaknesses. For cases where full NIST SP 800-63 compliance is necessary, please refer to NIST SP 800-63.

### Selecting an appropriate NIST AAL Level

The Application Security Verification Standard has tried to map ASVS L1 to NIST AAL1 requirements, L2 to AAL2, and L3 to AAL3. However, the approach of ASVS Level 1 as "essential" controls may not necessarily be the correct AAL level to verify an application or API. For example, if the application is a Level 3 application or has regulatory requirements to be AAL3, Level 3 should be chosen in chapters V2 and V3 Session Management. The choice of NIST-compliant Authentication Assertion Level (AAL) should be performed as per NIST SP 800-63B guidelines as set out in *Selecting AAL* in [NIST SP 800-63B Section 6.2](https://pages.nist.gov/800-63-3/sp800-63-3.html#AAL_CYOA).

## V2.1 Password Security

Passwords, called "Memorized Secrets" by NIST SP 800-63, include passwords, PINs, unlock patterns, pick the correct kitten or another image element, and passphrases. They are generally considered "something you know", and often used as single-factor authenticators. There are significant challenges to the continued use of single-factor authentication, including billions of valid usernames and passwords disclosed on the Internet, default or weak passwords, rainbow tables and ordered dictionaries of the most common passwords.

Applications should strongly encourage users to enroll in multi-factor authentication and should allow users to re-use tokens they already possess, such as FIDO or U2F tokens, or link to a credential service provider that provides multi-factor authentication.

Credential Service Providers (CSPs) provide federated identity for users. Users will often have more than one identity with multiple CSPs, such as an enterprise identity using Azure AD, Okta, Ping Identity or Google, or consumer identity using Facebook, Twitter, Google, or WeChat, to name just a few common alternatives. This list is not an endorsement of these companies or services, but simply an encouragement for developers to consider the reality that many users have many established identities. Organizations should consider integrating with existing user identities, as per the risk profile of the CSP's strength of identity proofing. For example, it is unlikely a government organization would accept a social media identity as a login for sensitive systems, as it is easy to create fake or throw away identities, whereas a mobile game company may well need to integrate with major social media platforms to grow their active player base.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.1.1** | [MODIFIED] Verify that user set passwords are at least 8 characters in length. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.2** | [MODIFIED, SPLIT TO 2.4.6] Verify that passwords of at least 64 characters are permitted. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.3** | [MODIFIED] Verify that the application verifies the user's password exactly as received from the user, without any modifications such as truncation or case transformation. | ✓ | ✓ | ✓ | | 5.1.1.2 |
| **2.1.4** | Verify that any printable Unicode character, including language neutral characters such as spaces and Emojis are permitted in passwords. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.5** | Verify users can change their password. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.6** | Verify that password change functionality requires the user's current and new password. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.7** | [MODIFIED, SPLIT TO 2.1.14] Verify that passwords submitted during account registration or password change are checked against an available set of, at least, the top 3000 passwords. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.8** | [DELETED, INSUFFICIENT IMPACT] | | | | | |
| **2.1.9** | Verify that there are no password composition rules limiting the type of characters permitted. There should be no requirement for upper or lower case or numbers or special characters. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.10** | [MODIFIED, SPLIT TO 2.1.13, LEVEL L1 > L2] Verify that the application does not require periodic credential rotation. | | ✓ | ✓ | | 5.1.1.2 |
| **2.1.11** | Verify that "paste" functionality, browser password helpers, and external password managers are permitted. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.12** | [MODIFIED] Verify that password input fields use type=password to mask the entry. Applications may allow the user to temporarily view the entire masked password, or the last typed character of the password. | ✓ | ✓ | ✓ | 549 | 5.1.1.2 |
| **2.1.13** | [ADDED, SPLIT FROM 2.1.10, LEVEL L1 > L2] Verify that the application does not keep a password history. | | ✓ | ✓ | | 5.1.1.2 |
| **2.1.14** | [ADDED, SPLIT FROM 2.1.7, LEVEL L1 > L3] Verify that passwords submitted during account registration or password changes are checked against a set of breached passwords. | | | ✓ | | 5.1.1.2 |
| **2.1.15** | [ADDED] Verify that the documented list of context specific words is used to prevent easy to guess passwords being created. | | ✓ | ✓ | 521 | 5.1.1.2 |

Possible sources of frequently used passwords for requirement 2.1.7 include:

* <https://github.com/danielmiessler/SecLists/tree/master/Passwords>
* <https://www.ncsc.gov.uk/blog-post/passwords-passwords-everywhere>

## V2.2 General Authenticator Security

Authenticator agility is essential to future-proof applications. Refactor application verifiers to allow additional authenticators as per user preferences, as well as retiring deprecated or unsafe authenticators in an orderly fashion.

NIST considers SMS as ["restricted" authenticator types](https://pages.nist.gov/800-63-FAQ/#q-b01), and they are likely to be removed from NIST SP 800-63, and consequently from the ASVS, in the future. Applications should plan a roadmap that does not require the use of SMS.

As noted above, NIST SP 800-63 considers email as [not acceptable](https://pages.nist.gov/800-63-FAQ/#q-b11) as an authenticator.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.2.1** | [MODIFIED] Verify that anti-automation controls are effective at mitigating breached credential testing, brute force, and account lockout attacks. Such controls include blocking the most common breached passwords, soft lockouts, rate limiting, CAPTCHA, ever increasing delays between attempts, IP address restrictions, or risk-based restrictions such as location, first login on a device, recent attempts to unlock the account, or similar. More than 5 failed authentication attempts per hour for a single account should trigger some sort of reaction or alert. | ✓ | ✓ | ✓ | 307 | 5.2.2 / 5.1.1.2 / 5.1.4.2 / 5.1.5.2 |
| **2.2.2** | [MODIFIED, SPLIT TO 2.2.12] Verify that restricted authenticators (those using PSTN to deliver OTPs via phone or SMS) are offered only when alternate stronger methods are also offered and when the service provides information on their security risks to users. | ✓ | ✓ | ✓ | 304 | 5.2.10 |
| **2.2.3** | [MODIFIED, SPLIT TO 2.2.10] Verify that users are notified after updates to authentication details, such as credential resets or modification of the username or email address. | ✓ | ✓ | ✓ | 778 | 6.1.2 |
| **2.2.4** | [MODIFIED, SPLIT TO 2.2.9] Verify that a hardware-based authenticator and an authenticator that provides verifier impersonation resistance against phishing attacks (such as WebAuthn) are used. | | | ✓ | 308 | 4.3.1 |
| **2.2.5** | Verify that where a Credential Service Provider (CSP) and the application verifying authentication are separated, mutually authenticated TLS is in place between the two endpoints. | | | ✓ | 319 | 5.2.6 |
| **2.2.6** | Verify replay resistance through the mandated use of One-time Passwords (OTP) devices, cryptographic authenticators, or lookup codes. | | | ✓ | 308 | 5.2.8 |
| **2.2.7** | Verify intent to authenticate by requiring the entry of an OTP token or user-initiated action such as a button press on a FIDO hardware key. | | | ✓ | 308 | 5.2.9 |
| **2.2.8** | [ADDED] Verify that valid users cannot be deduced from failed authentication challenges, such as based on error messages, HTTP response codes, or different response times. Registration and forgot password functionality should also have this protection. | | | ✓ | | |
| **2.2.9** | [ADDED, SPLIT FROM 2.2.4] Verify that multi-factor authentication is required, that is, the application uses either a multi-factor authenticator or a combination of single-factor authenticators. | | ✓ | ✓ | 308 | 4.2.1 |
| **2.2.10** | [ADDED, SPLIT FROM 2.2.3] Verify that users are notified of suspicious authentication attempts. Suspicious authentication attempts may include successful or unsuccessful authentication from an unusual location or client, partially successful authentication with only one of multiple factors, successful or unsuccessful authentication after a long period of inactivity or successful authentication after several unsuccessful attempts. | | ✓ | ✓ | 778 | |
| **2.2.11** | [ADDED, SPLIT FROM 1.2.4] Verify that, if the application includes multiple authentication pathways, there are no undocumented pathways and that security controls and authentication strength are enforced consistently. | | ✓ | ✓ | 306 | |
| **2.2.12** | [ADDED, SPLIT FROM 2.2.2] Verify that email is not used as either a single-factor or multi-factor authentication mechanism. | ✓ | ✓ | ✓ | 1390 | |

## V2.3 Authenticator Lifecycle

Authenticators are passwords, soft tokens, hardware tokens, and biometric devices. The lifecycle of authenticators is critical to the security of an application - if anyone can self-register an account with no evidence of identity, there can be little trust in the identity assertion. For social media sites like Reddit, that's perfectly okay. For banking systems, a greater focus on the registration and issuance of credentials and devices is critical to the security of the application.

Note: Passwords are not to have a maximum lifetime or be subject to password rotation. Passwords should be checked for being breached, not regularly replaced.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.3.1** | [MODIFIED] Verify system generated initial passwords or activation codes are securely randomly generated, at least 6 characters long, may contain letters and numbers, expire after a short period of time, and are single-use. These initial secrets must not be permitted to become the long term password. | ✓ | ✓ | ✓ | 330 | 5.1.1.2 / A.3 |
| **2.3.2** | Verify that enrollment and use of user-provided authentication devices are supported, such as a U2F or FIDO tokens. | | ✓ | ✓ | 308 | 6.1.3 |
| **2.3.3** | [MODIFIED] Verify that automated reminders are configured and acted on to ensure that renewal instructions for time-bound authenticators are sent with enough time to be carried out before the old authenticator expires. | | ✓ | ✓ | 287 | 6.1.4 |
| **2.3.4** | [ADDED] System administrators should not be able to change or choose any user's password, but rather only be able to initiate the password reset process for the user. | ✓ | ✓ | ✓ | 620 | |

## V2.4 Credential Storage

Architects and developers should adhere to this section when building or refactoring code.

The current list of approved password hashing algorithms is detailed in NIST SP 800-63B section 5.1.1.2, and in the [OWASP Password Storage Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms). Pay careful attention to the configuration guidance to be aware of any implementation challenges or limits with each algorithm.

In particular, note that since these algorithms are intentionally compute-intensive, there have been cases in the past where providing a very long password leads to a denial of service condition. It is therefore very important to protect against this.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.4.1** | [MODIFIED, MERGED FROM 2.4.3, 2.4.4] Verify that user passwords are stored using an approved password hashing algorithm that is securely configured according to current guidance. | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.2** | [DELETED, INCORRECT] | | | | | |
| **2.4.3** | [DELETED, MERGED TO 2.4.1] | | | | | |
| **2.4.4** | [DELETED, MERGED TO 2.4.1] | | | | | |
| **2.4.5** | [DELETED, INCORRECT] | | | | | |
| **2.4.6** | [ADDED, SPLIT FROM 2.1.2] Verify that the application is protected against a denial of service attack caused by processing an overly long password. | | ✓ | ✓ | | |

Where US standards are mentioned, a regional or local standard can be used in place of or in addition to the US standard as required.

## V2.5 Credential Recovery

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.5.1** | [DELETED, INCORRECT] | | | | | |
| **2.5.2** | Verify password hints or knowledge-based authentication (so-called "secret questions") are not present. | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.3** | [DELETED, DUPLICATE OF 2.4.1] | | | | | |
| **2.5.4** | [MODIFIED] Verify that default user accounts (e.g. "root", "admin", or "sa") are not present in the application or are disabled. | ✓ | ✓ | ✓ | 798 | |
| **2.5.5** | [DELETED, DUPLICATE OF 2.2.3] | | | | | |
| **2.5.6** | Verify forgotten password, and other recovery paths use a secure recovery mechanism, such as time-based OTP (TOTP) or other soft token, mobile push, or another offline recovery mechanism. | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.7** | [LEVEL L2 > L1] Verify that if OTP or multi-factor authentication factors are lost, that evidence of identity proofing is performed at the same level as during enrollment. | ✓ | ✓ | ✓ | 308 | 6.1.2.3 |

## V2.6 Lookup Secret Verifier

Lookup secrets are pre-generated lists of secret codes, similar to Transaction Authorization Numbers (TAN), social media recovery codes, or a grid containing a set of random values. These are distributed securely to users. These lookup codes are single-use. Once all are utilized, the lookup secret list is discarded. This type of authenticator is considered "something you have".

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.6.1** | Verify that lookup secrets can be used only once. | | ✓ | ✓ | 308 | 5.1.2.2 |
| **2.6.2** | [MODIFIED, SPLIT TO 2.6.4] Verify that lookup secrets stored at the back-end with less than 112 bits of entropy (19 random alphanumeric characters or 34 random digits) are hashed with an approved password storage hashing algorithm that incorporates a 32-bit random salt. A standard hash function can be used if the secret has 112 bits of entropy or more. | | ✓ | ✓ | 330 | 5.1.2.2 |
| **2.6.3** | [MODIFIED] Verify that lookup secrets are generated using a Cryptographically Secure Pseudorandom Number Generator (CSPRNG) to avoid predictable values. | | ✓ | ✓ | 310 | 5.1.2.2 |
| **2.6.4** | [ADDED, SPLIT FROM 2.6.2] Verify that lookup secrets have a minimum of 20 bits of entropy (typically 4 random alphanumeric characters or 6 random digits is sufficient). | | ✓ | ✓ | 330 | 5.1.2.1 |

## V2.7 Out-of-Band Verifier

In the past, a common out-of-band verifier would have been an email or SMS containing a password reset link. Attackers use this weak mechanism to reset accounts they don't yet control, such as taking over a person's email account and re-using any discovered reset links. There are better ways to handle out-of-band verification.

Secure out-of-band authenticators are physical devices that can communicate with the verifier over a secure secondary channel. Examples include push notifications to mobile devices. This type of authenticator is considered "something you have". When a user wishes to authenticate, the verifying application sends a message to the out-of-band authenticator via a connection to the authenticator directly or indirectly through a third-party service. The message includes an authentication code, typically a random six-digit number, or features a modal approval dialog. The verifying application waits to receive the authentication code through the primary channel and compares the hash of the received value to the hash of the original authentication code. If they match, the out-of-band verifier can assume that the user has authenticated.

The ASVS assumes that only a few developers will be developing new out-of-band authenticators, such as push notifications, and thus the following ASVS controls apply to verifiers, such as authentication API, applications, and single sign-on implementations. If developing a new out-of-band authenticator, please refer to NIST SP 800-63B &sect; 5.1.3.1.

Unsafe out-of-band authenticators such as e-mail and VOIP are not permitted. PSTN and SMS authentication are currently "restricted" by NIST and should be deprecated in favor of push notifications or similar. If you need to use telephone or SMS out-of-band authentication, please see NIST SP 800-63B &sect; 5.1.3.3.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.7.1** | [GRAMMAR] Verify that cleartext out-of-band (NIST "restricted") authenticators, such as SMS or PSTN, are not offered by default, and stronger alternatives such as push notifications are offered first. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.2** | [MODIFIED] Verify that the out-of-band verifier expires out-of-band authentication requests, codes, or tokens within 10 minutes. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.3** | [GRAMMAR] Verify that the out-of-band verifier authentication requests, codes, or tokens are only usable once, and only for the original authentication request. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.4** | [GRAMMAR] Verify that the out-of-band authenticator and verifier communicates over a secure independent channel. | ✓ | ✓ | ✓ | 523 | 5.1.3.2 |
| **2.7.5** | [GRAMMAR] Verify that the out-of-band verifier retains only a hashed version of the authentication code. | | ✓ | ✓ | 256 | 5.1.3.2 |
| **2.7.6** | [MODIFIED] Verify that the initial authentication code is generated by a secure random number generator, containing at least 20 bits of entropy (typically 4 random alphanumeric characters or 6 random digits is sufficient). | | ✓ | ✓ | 310 | 5.1.3.2 |
| **2.7.7** | [ADDED] Verify that the initial authentication code is protected against brute force attacks by using either rate limiting or a code with at least 64 bits of entropy. | | ✓ | ✓ | 307 | 5.1.3.2 |

## V2.8 One-Time Verifier

Single-factor One-time Passwords (OTPs) are physical or soft tokens that display a continually changing pseudo-random one-time challenge. These devices make phishing (impersonation) difficult, but not impossible. This type of authenticator is considered "something you have". Multi-factor tokens are similar to single-factor OTPs, but require a valid PIN code, biometric unlocking, USB insertion or NFC pairing or some additional value (such as transaction signing calculators) to be entered to create the final OTP.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.8.1** | Verify that time-based OTPs have a defined lifetime before expiring. | ✓ | ✓ | ✓ | 613 | 5.1.4.2 / 5.1.5.2 |
| **2.8.2** | Verify that symmetric keys used to verify submitted OTPs are highly protected, such as by using a hardware security module or secure operating system based key storage. | | ✓ | ✓ | 320 | 5.1.4.2 / 5.1.5.2 |
| **2.8.3** | Verify that approved cryptographic algorithms are used in the generation, seeding, and verification of OTPs. | | ✓ | ✓ | 326 | 5.1.4.2 / 5.1.5.2 |
| **2.8.4** | Verify that time-based OTP can be used only once within the validity period. | | ✓ | ✓ | 287 | 5.1.4.2 / 5.1.5.2 |
| **2.8.5** | Verify that if a time-based multi-factor OTP token is re-used during the validity period, it is logged and rejected with secure notifications being sent to the holder of the device. | | ✓ | ✓ | 287 | 5.1.5.2 |
| **2.8.6** | Verify physical single-factor OTP generator can be revoked in case of theft or other loss. Ensure that revocation is immediately effective across logged in sessions, regardless of location. | | ✓ | ✓ | 613 | 5.2.1 |
| **2.8.7** | [MODIFIED, LEVEL L2 > L3] Verify that biometric authenticators are only used as secondary factors together with either something you have or something you know. | | | ✓ | 308 | 5.2.3 |
| **2.8.8** | [ADDED] Ensure that generation of the time-based multi-factor OTP token is based on the server's system time and not the client's machine. | | | ✓ | 367 | 5.1.4.2 / 5.1.5.2 |

## V2.9 Cryptographic Verifier

Cryptographic security keys are smart cards or FIDO keys, where the user has to plug in or pair the cryptographic device to the computer to complete authentication. Verifiers send a challenge nonce to the cryptographic devices or software, and the device or software calculates a response based upon a securely stored cryptographic key.

The requirements for single-factor cryptographic devices and software, and multi-factor cryptographic devices and software are the same, as verification of the cryptographic authenticator proves possession of the authentication factor.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.9.1** | Verify that cryptographic keys used in verification are stored securely and protected against disclosure, such as using a Trusted Platform Module (TPM) or Hardware Security Module (HSM), or an OS service that can use this secure storage. | | ✓ | ✓ | 320 | 5.1.7.2 |
| **2.9.2** | Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device. | | ✓ | ✓ | 330 | 5.1.7.2 |
| **2.9.3** | [MODIFIED] Verify that approved cryptographic algorithms are used in the generation, seeding, and verification of the cryptographic keys. | | ✓ | ✓ | 327 | 5.1.7.2 |

## V2.10 Service Authentication

This section is not penetration testable, so does not have any L1 requirements.

Secrets can be securely stored by using services offered by the framework, the operating system, or hardware. For example, the Java Key Store, Keychain Access and AWS Secrets Manager are services that can help store secrets securely. For optimal security, a hardware solution such as a Hardware Security Module or Trusted Platform Module should be used. To conform to level 2, secrets must be stored in a secured service offered by the framework or operating system. For level 3, secrets must be stored in a hardware-assisted service.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.10.1** | Verify that intra-service secrets do not rely on unchanging credentials such as passwords, API keys or shared accounts with privileged access. | | ✓ | ✓ | 287 | |
| **2.10.2** | [GRAMMAR] Verify that if a credential has to be used for service authentication, the credential being used by the consumer is not a default credential (e.g. root/root or admin/admin are default in some services during installation). | | ✓ | ✓ | 255 | |
| **2.10.3** | [DELETED, DUPLICATE OF 2.10.4] | | | | | |
| **2.10.4** | [GRAMMAR] Verify passwords, integrations with databases and third-party systems, seeds and internal secrets, and API keys are managed securely and not included in the source code or stored within source code repositories. Such storage should resist offline attacks. The use of a secure software key store (L1), hardware TPM, or an HSM (L3) is recommended for password storage. | | ✓ | ✓ | 798 | |

## Additional US Agency Requirements

US Agencies have mandatory requirements concerning NIST SP 800-63. The Application Security Verification Standard has always been about the 80% of controls that apply to nearly 100% of apps, and not the last 20% of advanced controls or those that have limited applicability. As such, the ASVS is a strict subset of NIST SP 800-63, especially for IAL1/2 and AAL1/2 classifications, but is not sufficiently comprehensive, particularly concerning IAL3/AAL3 classifications.

We strongly urge US government agencies to review and implement NIST SP 800-63 in its entirety.

## Glossary of terms

| Term | Meaning |
| -- | -- |
| CSP | Credential Service Provider also called an Identity Provider. |
| Authenticator | Code that authenticates a password, token, MFA, federated assertion, and so on. |
| Verifier | "An entity that verifies the claimant's identity by verifying the claimant's possession and control of one or two authenticators using an authentication protocol. To do this, the verifier may also need to validate credentials that link the authenticator(s) to the subscriber's identifier and check their status". |
| OTP | One-time password. |
| SFA | Single-factor authenticators, such as something you know (memorized secrets, passwords, passphrases, PINs), something you are (biometrics, fingerprint, face scans), or something you have (OTP tokens, a cryptographic device such as a smart card). |
| MFA | Multi-factor authentication, which includes two or more single factors. |

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
