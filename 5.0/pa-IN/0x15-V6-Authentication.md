<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x15-V6-Authentication.md -->
<!-- Translator: GeeksikhSecurity -->

# V6 Authentication
# V6 ਪ੍ਰਮਾਣੀਕਰਨ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

Authentication is the process of establishing or confirming the authenticity of an individual or device. It involves verifying claims made by a person or about a device, ensuring resistance to impersonation, and preventing the recovery or interception of passwords.

ਪ੍ਰਮਾਣੀਕਰਨ (Authentication) ਕਿਸੇ ਵਿਅਕਤੀ ਜਾਂ ਡਿਵਾਈਸ ਦੀ ਪ੍ਰਮਾਣਿਕਤਾ ਨੂੰ ਸਥਾਪਿਤ ਕਰਨ ਜਾਂ ਉਸ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਹੈ। ਇਸ ਵਿੱਚ ਕਿਸੇ ਵਿਅਕਤੀ ਦੁਆਰਾ ਕੀਤੇ ਗਏ ਜਾਂ ਕਿਸੇ ਡਿਵਾਈਸ ਬਾਰੇ ਕੀਤੇ ਗਏ ਦਾਅਵਿਆਂ ਦੀ ਤਸਦੀਕ ਕਰਨਾ, ਪਛਾਣ-ਨਕਲ (impersonation) ਪ੍ਰਤੀ ਰੋਧਕਤਾ ਯਕੀਨੀ ਬਣਾਉਣਾ, ਅਤੇ ਪਾਸਵਰਡਾਂ ਦੀ ਰਿਕਵਰੀ ਜਾਂ ਉਹਨਾਂ ਨੂੰ ਰਾਹ ਵਿੱਚ ਫੜੇ ਜਾਣ (interception) ਨੂੰ ਰੋਕਣਾ ਸ਼ਾਮਲ ਹੈ।

[NIST SP 800-63](https://pages.nist.gov/800-63-3/) is a modern, evidence-based standard that is valuable for organizations worldwide, but is particularly relevant to US agencies and those interacting with US agencies.

[NIST SP 800-63](https://pages.nist.gov/800-63-3/) ਇੱਕ ਆਧੁਨਿਕ, ਸਬੂਤ-ਆਧਾਰਿਤ ਮਿਆਰ ਹੈ ਜੋ ਦੁਨੀਆ ਭਰ ਦੀਆਂ ਸੰਸਥਾਵਾਂ ਲਈ ਕੀਮਤੀ ਹੈ, ਪਰ ਅਮਰੀਕੀ ਏਜੰਸੀਆਂ ਅਤੇ ਅਮਰੀਕੀ ਏਜੰਸੀਆਂ ਨਾਲ ਆਪਸੀ ਤਾਲਮੇਲ ਕਰਨ ਵਾਲਿਆਂ ਲਈ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ਢੁਕਵਾਂ ਹੈ।

While many of the requirements in this chapter are based on the second section of the standard (known as NIST SP 800-63B "Digital Identity Guidelines - Authentication and Lifecycle Management"), the chapter focuses on common threats and frequently exploited authentication weaknesses. It does not attempt to comprehensively cover every point in the standard. For cases where full NIST SP 800-63 compliance is necessary, please refer to NIST SP 800-63.

ਭਾਵੇਂ ਇਸ ਅਧਿਆਇ ਦੀਆਂ ਬਹੁਤ ਸਾਰੀਆਂ ਲੋੜਾਂ ਮਿਆਰ ਦੇ ਦੂਜੇ ਭਾਗ (ਜਿਸ ਨੂੰ NIST SP 800-63B "Digital Identity Guidelines - Authentication and Lifecycle Management" ਵਜੋਂ ਜਾਣਿਆ ਜਾਂਦਾ ਹੈ) 'ਤੇ ਆਧਾਰਿਤ ਹਨ, ਇਹ ਅਧਿਆਇ ਆਮ ਖ਼ਤਰਿਆਂ ਅਤੇ ਅਕਸਰ ਸ਼ੋਸ਼ਣ ਕੀਤੀਆਂ ਜਾਣ ਵਾਲੀਆਂ ਪ੍ਰਮਾਣੀਕਰਨ ਕਮਜ਼ੋਰੀਆਂ 'ਤੇ ਕੇਂਦ੍ਰਿਤ ਹੈ। ਇਹ ਮਿਆਰ ਦੇ ਹਰ ਨੁਕਤੇ ਨੂੰ ਵਿਆਪਕ ਰੂਪ ਵਿੱਚ ਕਵਰ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਨਹੀਂ ਕਰਦਾ। ਜਿਨ੍ਹਾਂ ਮਾਮਲਿਆਂ ਵਿੱਚ NIST SP 800-63 ਦੀ ਪੂਰੀ ਪਾਲਣਾ ਜ਼ਰੂਰੀ ਹੈ, ਕਿਰਪਾ ਕਰਕੇ NIST SP 800-63 ਵੇਖੋ।

Additionally, NIST SP 800-63 terminology may sometimes differ, and this chapter often uses more commonly understood terminology to improve clarity.

ਇਸ ਤੋਂ ਇਲਾਵਾ, NIST SP 800-63 ਦੀ ਸ਼ਬਦਾਵਲੀ ਕਈ ਵਾਰ ਵੱਖਰੀ ਹੋ ਸਕਦੀ ਹੈ, ਅਤੇ ਸਪੱਸ਼ਟਤਾ ਵਧਾਉਣ ਲਈ ਇਹ ਅਧਿਆਇ ਅਕਸਰ ਵਧੇਰੇ ਆਮ ਤੌਰ 'ਤੇ ਸਮਝੀ ਜਾਣ ਵਾਲੀ ਸ਼ਬਦਾਵਲੀ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ।

A common feature of more advanced applications is the ability to adapt authentication stages required based on various risk factors. This feature is covered in the "Authorization" chapter, since these mechanisms also need to be considered for authorization decisions.

ਵਧੇਰੇ ਉੱਨਤ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੀ ਇੱਕ ਆਮ ਵਿਸ਼ੇਸ਼ਤਾ ਵੱਖ-ਵੱਖ ਜੋਖਮ ਕਾਰਕਾਂ (risk factors) ਦੇ ਆਧਾਰ 'ਤੇ ਲੋੜੀਂਦੇ ਪ੍ਰਮਾਣੀਕਰਨ ਪੜਾਵਾਂ ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਉਣ ਦੀ ਯੋਗਤਾ ਹੈ। ਇਹ ਵਿਸ਼ੇਸ਼ਤਾ "ਅਧਿਕਾਰੀਕਰਨ" (Authorization) ਅਧਿਆਇ ਵਿੱਚ ਕਵਰ ਕੀਤੀ ਗਈ ਹੈ, ਕਿਉਂਕਿ ਇਹਨਾਂ ਪ੍ਰਣਾਲੀਆਂ ਨੂੰ ਅਧਿਕਾਰੀਕਰਨ ਫ਼ੈਸਲਿਆਂ ਲਈ ਵੀ ਵਿਚਾਰਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

## V6.1 Authentication Documentation
## V6.1 ਪ੍ਰਮਾਣੀਕਰਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

This section contains requirements detailing the authentication documentation that should be maintained for an application. This is crucial for implementing and assessing how the relevant authentication controls should be configured.

ਇਸ ਭਾਗ ਵਿੱਚ ਉਹ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ ਜੋ ਕਿਸੇ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਬਣਾਈ ਰੱਖੇ ਜਾਣ ਵਾਲੇ ਪ੍ਰਮਾਣੀਕਰਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਦਾ ਵੇਰਵਾ ਦਿੰਦੀਆਂ ਹਨ। ਇਹ ਲਾਗੂ ਕਰਨ ਅਤੇ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਸੰਬੰਧਿਤ ਪ੍ਰਮਾਣੀਕਰਨ ਨਿਯੰਤਰਣਾਂ ਨੂੰ ਕਿਵੇਂ ਕੌਨਫ਼ਿਗਰ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **6.1.1** | Verify that application documentation defines how controls such as rate limiting, anti-automation, and adaptive response, are used to defend against attacks such as credential stuffing and password brute force. The documentation must make clear how these controls are configured and prevent malicious account lockout. | 1 |
| **6.1.2** | Verify that a list of context-specific words is documented in order to prevent their use in passwords. The list could include permutations of organization names, product names, system identifiers, project codenames, department or role names, and similar. | 2 |
| **6.1.3** | Verify that, if the application includes multiple authentication pathways, these are all documented together with the security controls and authentication strength which must be consistently enforced across them. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **6.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਕਿ ਦਰ ਸੀਮਾ (rate limiting), ਸਵੈਚਾਲਨ-ਵਿਰੋਧੀ (anti-automation), ਅਤੇ ਅਨੁਕੂਲਿਤ ਪ੍ਰਤੀਕਿਰਿਆ (adaptive response) ਵਰਗੇ ਨਿਯੰਤਰਣਾਂ ਦੀ ਵਰਤੋਂ ਕ੍ਰੀਡੈਂਸ਼ੀਅਲ ਸਟਫ਼ਿੰਗ (credential stuffing) ਅਤੇ ਪਾਸਵਰਡ ਬਰੂਟ ਫੋਰਸ ਵਰਗੇ ਹਮਲਿਆਂ ਤੋਂ ਬਚਾਅ ਲਈ ਕਿਵੇਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਨੂੰ ਸਪੱਸ਼ਟ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਇਹ ਨਿਯੰਤਰਣ ਕਿਵੇਂ ਕੌਨਫ਼ਿਗਰ ਕੀਤੇ ਗਏ ਹਨ ਅਤੇ ਦੁਰਭਾਵਨਾਪੂਰਨ ਖਾਤਾ ਤਾਲਾਬੰਦੀ (account lockout) ਨੂੰ ਕਿਵੇਂ ਰੋਕਦੇ ਹਨ। | 1 |
| **6.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੰਦਰਭ-ਖ਼ਾਸ ਸ਼ਬਦਾਂ ਦੀ ਇੱਕ ਸੂਚੀ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਵਿੱਚ ਦਰਜ ਹੈ ਤਾਂ ਜੋ ਪਾਸਵਰਡਾਂ ਵਿੱਚ ਉਹਨਾਂ ਦੀ ਵਰਤੋਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। ਇਸ ਸੂਚੀ ਵਿੱਚ ਸੰਸਥਾ ਦੇ ਨਾਂ, ਉਤਪਾਦ ਦੇ ਨਾਂ, ਸਿਸਟਮ ਪਛਾਣਕਰਤਾ, ਪ੍ਰੋਜੈਕਟ ਕੋਡਨਾਂ, ਵਿਭਾਗ ਜਾਂ ਭੂਮਿਕਾ ਦੇ ਨਾਂ, ਅਤੇ ਇਸੇ ਤਰ੍ਹਾਂ ਦੇ ਹੋਰ ਸ਼ਬਦਾਂ ਦੇ ਕ੍ਰਮ-ਪਰਿਵਰਤਨ (permutations) ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ। | 2 |
| **6.1.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਕਈ ਪ੍ਰਮਾਣੀਕਰਨ ਮਾਰਗ ਸ਼ਾਮਲ ਹਨ, ਤਾਂ ਇਹ ਸਾਰੇ ਉਹਨਾਂ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣਾਂ ਅਤੇ ਪ੍ਰਮਾਣੀਕਰਨ ਤਾਕਤ ਦੇ ਨਾਲ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਵਿੱਚ ਦਰਜ ਹਨ ਜੋ ਇਹਨਾਂ ਸਾਰਿਆਂ ਵਿੱਚ ਇਕਸਾਰ ਤੌਰ 'ਤੇ ਲਾਗੂ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ। | 2 |

## V6.2 Password Security
## V6.2 ਪਾਸਵਰਡ ਸੁਰੱਖਿਆ

Passwords, called "Memorized Secrets" by NIST SP 800-63, include passwords, passphrases, PINs, unlock patterns, and picking the correct kitten or another image element. They are generally considered "something you know" and are often used as a single-factor authentication mechanism.

ਪਾਸਵਰਡ, ਜਿਨ੍ਹਾਂ ਨੂੰ NIST SP 800-63 ਦੁਆਰਾ "Memorized Secrets" (ਯਾਦ ਰੱਖੇ ਭੇਦ) ਕਿਹਾ ਜਾਂਦਾ ਹੈ, ਵਿੱਚ ਪਾਸਵਰਡ, ਪਾਸਫ਼੍ਰੇਜ਼, PIN, ਅਨਲੌਕ ਪੈਟਰਨ, ਅਤੇ ਸਹੀ ਬਿੱਲੀ ਦੇ ਬੱਚੇ ਜਾਂ ਕਿਸੇ ਹੋਰ ਚਿੱਤਰ ਤੱਤ ਨੂੰ ਚੁਣਨਾ ਸ਼ਾਮਲ ਹੈ। ਇਹਨਾਂ ਨੂੰ ਆਮ ਤੌਰ 'ਤੇ "ਕੁਝ ਜੋ ਤੁਸੀਂ ਜਾਣਦੇ ਹੋ" ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਇਹ ਅਕਸਰ ਇੱਕ ਇੱਕ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ (single-factor authentication) ਪ੍ਰਣਾਲੀ ਵਜੋਂ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।

As such, this section contains requirements for making sure that passwords are created and handled securely. Most of the requirements are L1 as they are most important at that level. From L2 onwards, multi-factor authentication mechanisms are required, where passwords may be one of those factors.

ਇਸ ਲਈ, ਇਸ ਭਾਗ ਵਿੱਚ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ ਕਿ ਪਾਸਵਰਡ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਬਣਾਏ ਅਤੇ ਸੰਭਾਲੇ ਜਾਣ। ਜ਼ਿਆਦਾਤਰ ਲੋੜਾਂ L1 ਹਨ ਕਿਉਂਕਿ ਉਹ ਉਸ ਪੱਧਰ 'ਤੇ ਸਭ ਤੋਂ ਮਹੱਤਵਪੂਰਨ ਹਨ। L2 ਤੋਂ ਅੱਗੇ, ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ (multi-factor authentication) ਪ੍ਰਣਾਲੀਆਂ ਲੋੜੀਂਦੀਆਂ ਹਨ, ਜਿੱਥੇ ਪਾਸਵਰਡ ਉਹਨਾਂ ਕਾਰਕਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੋ ਸਕਦੇ ਹਨ।

The requirements in this section mostly relate to [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

ਇਸ ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ ਜ਼ਿਆਦਾਤਰ [NIST ਦੇ ਮਾਰਗਦਰਸ਼ਨ](https://pages.nist.gov/800-63-3/sp800-63b.html) ਦੇ [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) ਨਾਲ ਸੰਬੰਧਿਤ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **6.2.1** | Verify that user set passwords are at least 8 characters in length although a minimum of 15 characters is strongly recommended. | 1 |
| **6.2.2** | Verify that users can change their password. | 1 |
| **6.2.3** | Verify that password change functionality requires the user's current and new password. | 1 |
| **6.2.4** | Verify that passwords submitted during account registration or password change are checked against an available set of, at least, the top 3000 passwords which match the application's password policy, e.g. minimum length. | 1 |
| **6.2.5** | Verify that passwords of any composition can be used, without rules limiting the type of characters permitted. There must be no requirement for a minimum number of upper or lower case characters, numbers, or special characters. | 1 |
| **6.2.6** | Verify that password input fields use type=password to mask the entry. Applications may allow the user to temporarily view the entire masked password, or the last typed character of the password. | 1 |
| **6.2.7** | Verify that "paste" functionality, browser password helpers, and external password managers are permitted. | 1 |
| **6.2.8** | Verify that the application verifies the user's password exactly as received from the user, without any modifications such as truncation or case transformation. | 1 |
| **6.2.9** | Verify that passwords of at least 64 characters are permitted. | 2 |
| **6.2.10** | Verify that a user's password stays valid until it is discovered to be compromised or the user rotates it. The application must not require periodic credential rotation. | 2 |
| **6.2.11** | Verify that the documented list of context specific words is used to prevent easy to guess passwords being created. | 2 |
| **6.2.12** | Verify that passwords submitted during account registration or password changes are checked against a set of breached passwords. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **6.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਸੈੱਟ ਕੀਤੇ ਪਾਸਵਰਡ ਘੱਟੋ-ਘੱਟ 8 ਅੱਖਰ ਲੰਬੇ ਹਨ, ਹਾਲਾਂਕਿ ਘੱਟੋ-ਘੱਟ 15 ਅੱਖਰਾਂ ਦੀ ਜ਼ੋਰਦਾਰ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 1 |
| **6.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਪਭੋਗਤਾ ਆਪਣਾ ਪਾਸਵਰਡ ਬਦਲ ਸਕਦੇ ਹਨ। | 1 |
| **6.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪਾਸਵਰਡ ਬਦਲਣ ਦੀ ਕਾਰਜਸ਼ੀਲਤਾ ਲਈ ਉਪਭੋਗਤਾ ਦਾ ਮੌਜੂਦਾ ਅਤੇ ਨਵਾਂ ਪਾਸਵਰਡ ਲੋੜੀਂਦਾ ਹੈ। | 1 |
| **6.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਖਾਤਾ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਜਾਂ ਪਾਸਵਰਡ ਬਦਲਣ ਦੌਰਾਨ ਜਮ੍ਹਾਂ ਕੀਤੇ ਪਾਸਵਰਡਾਂ ਦੀ ਜਾਂਚ ਘੱਟੋ-ਘੱਟ ਉਹਨਾਂ ਸਿਖਰਲੇ 3000 ਪਾਸਵਰਡਾਂ ਦੇ ਉਪਲਬਧ ਸਮੂਹ ਦੇ ਵਿਰੁੱਧ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਪਾਸਵਰਡ ਨੀਤੀ, ਜਿਵੇਂ ਕਿ ਘੱਟੋ-ਘੱਟ ਲੰਬਾਈ, ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ। | 1 |
| **6.2.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਿਸੇ ਵੀ ਬਣਤਰ ਦੇ ਪਾਸਵਰਡ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ, ਬਿਨਾਂ ਅਜਿਹੇ ਨਿਯਮਾਂ ਦੇ ਜੋ ਇਜਾਜ਼ਤ ਪ੍ਰਾਪਤ ਅੱਖਰਾਂ ਦੀ ਕਿਸਮ ਨੂੰ ਸੀਮਤ ਕਰਦੇ ਹੋਣ। ਵੱਡੇ ਜਾਂ ਛੋਟੇ ਅੱਖਰਾਂ, ਅੰਕਾਂ, ਜਾਂ ਵਿਸ਼ੇਸ਼ ਅੱਖਰਾਂ ਦੀ ਘੱਟੋ-ਘੱਟ ਗਿਣਤੀ ਦੀ ਕੋਈ ਲੋੜ ਨਹੀਂ ਹੋਣੀ ਚਾਹੀਦੀ। | 1 |
| **6.2.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪਾਸਵਰਡ ਇਨਪੁੱਟ ਖੇਤਰ ਦਾਖ਼ਲੇ ਨੂੰ ਲੁਕਾਉਣ (mask) ਲਈ type=password ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ। ਐਪਲੀਕੇਸ਼ਨਾਂ ਉਪਭੋਗਤਾ ਨੂੰ ਪੂਰੇ ਲੁਕਾਏ ਹੋਏ ਪਾਸਵਰਡ, ਜਾਂ ਪਾਸਵਰਡ ਦੇ ਆਖ਼ਰੀ ਟਾਈਪ ਕੀਤੇ ਅੱਖਰ, ਨੂੰ ਅਸਥਾਈ ਤੌਰ 'ਤੇ ਵੇਖਣ ਦੀ ਇਜਾਜ਼ਤ ਦੇ ਸਕਦੀਆਂ ਹਨ। | 1 |
| **6.2.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ "ਪੇਸਟ" ਕਾਰਜਸ਼ੀਲਤਾ, ਬ੍ਰਾਊਜ਼ਰ ਪਾਸਵਰਡ ਸਹਾਇਕਾਂ, ਅਤੇ ਬਾਹਰੀ ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਕਾਂ ਦੀ ਇਜਾਜ਼ਤ ਹੈ। | 1 |
| **6.2.8** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਉਪਭੋਗਤਾ ਦੇ ਪਾਸਵਰਡ ਦੀ ਤਸਦੀਕ ਬਿਲਕੁਲ ਉਸੇ ਰੂਪ ਵਿੱਚ ਕਰਦੀ ਹੈ ਜਿਵੇਂ ਉਹ ਉਪਭੋਗਤਾ ਤੋਂ ਪ੍ਰਾਪਤ ਹੋਇਆ ਹੈ, ਬਿਨਾਂ ਕਿਸੇ ਸੋਧ ਦੇ ਜਿਵੇਂ ਕਿ ਕੱਟ-ਛਾਂਟ (truncation) ਜਾਂ ਵੱਡੇ-ਛੋਟੇ ਅੱਖਰਾਂ ਦਾ ਰੂਪਾਂਤਰਨ। | 1 |
| **6.2.9** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਘੱਟੋ-ਘੱਟ 64 ਅੱਖਰਾਂ ਦੇ ਪਾਸਵਰਡਾਂ ਦੀ ਇਜਾਜ਼ਤ ਹੈ। | 2 |
| **6.2.10** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਪਭੋਗਤਾ ਦਾ ਪਾਸਵਰਡ ਉਦੋਂ ਤੱਕ ਜਾਇਜ਼ ਰਹਿੰਦਾ ਹੈ ਜਦੋਂ ਤੱਕ ਇਹ ਪਤਾ ਨਹੀਂ ਲੱਗਦਾ ਕਿ ਇਸ ਦਾ ਸਮਝੌਤਾ ਹੋ ਗਿਆ ਹੈ (compromised) ਜਾਂ ਉਪਭੋਗਤਾ ਇਸ ਨੂੰ ਬਦਲ ਨਹੀਂ ਦਿੰਦਾ। ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਸਮੇਂ-ਸਮੇਂ 'ਤੇ ਪ੍ਰਮਾਣ-ਪੱਤਰ ਬਦਲਣ (credential rotation) ਦੀ ਲੋੜ ਨਹੀਂ ਰੱਖਣੀ ਚਾਹੀਦੀ। | 2 |
| **6.2.11** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੰਦਰਭ-ਖ਼ਾਸ ਸ਼ਬਦਾਂ ਦੀ ਦਸਤਾਵੇਜ਼ੀ ਸੂਚੀ ਦੀ ਵਰਤੋਂ ਆਸਾਨੀ ਨਾਲ ਅਨੁਮਾਨ ਲਗਾਏ ਜਾ ਸਕਣ ਵਾਲੇ ਪਾਸਵਰਡਾਂ ਨੂੰ ਬਣਾਏ ਜਾਣ ਤੋਂ ਰੋਕਣ ਲਈ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 2 |
| **6.2.12** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਖਾਤਾ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਜਾਂ ਪਾਸਵਰਡ ਬਦਲਣ ਦੌਰਾਨ ਜਮ੍ਹਾਂ ਕੀਤੇ ਪਾਸਵਰਡਾਂ ਦੀ ਜਾਂਚ ਲੀਕ ਹੋਏ (breached) ਪਾਸਵਰਡਾਂ ਦੇ ਸਮੂਹ ਦੇ ਵਿਰੁੱਧ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 2 |

## V6.3 General Authentication Security
## V6.3 ਆਮ ਪ੍ਰਮਾਣੀਕਰਨ ਸੁਰੱਖਿਆ

This section contains general requirements for the security of authentication mechanisms as well as setting out the different expectations for levels. L2 applications must force the use of multi-factor authentication (MFA). L3 applications must use hardware-based authentication, performed in an attested and trusted execution environment (TEE). This could include device-bound passkeys, eIDAS Level of Assurance (LoA) High enforced authenticators, authenticators with NIST Authenticator Assurance Level 3 (AAL3) assurance, or an equivalent mechanism.

ਇਸ ਭਾਗ ਵਿੱਚ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਸੁਰੱਖਿਆ ਲਈ ਆਮ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ ਅਤੇ ਨਾਲ ਹੀ ਪੱਧਰਾਂ ਲਈ ਵੱਖ-ਵੱਖ ਉਮੀਦਾਂ ਵੀ ਨਿਰਧਾਰਿਤ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ। L2 ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ (MFA) ਦੀ ਵਰਤੋਂ ਲਾਜ਼ਮੀ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ। L3 ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਹਾਰਡਵੇਅਰ-ਆਧਾਰਿਤ ਪ੍ਰਮਾਣੀਕਰਨ ਵਰਤਣਾ ਚਾਹੀਦਾ ਹੈ, ਜੋ ਇੱਕ ਤਸਦੀਕਸ਼ੁਦਾ (attested) ਅਤੇ ਭਰੋਸੇਯੋਗ ਐਗਜ਼ੀਕਿਊਸ਼ਨ ਵਾਤਾਵਰਣ (trusted execution environment, TEE) ਵਿੱਚ ਕੀਤਾ ਜਾਂਦਾ ਹੋਵੇ। ਇਸ ਵਿੱਚ ਡਿਵਾਈਸ-ਬੱਧ ਪਾਸਕੀਆਂ, eIDAS Level of Assurance (LoA) High ਲਾਗੂ ਕੀਤੇ ਪ੍ਰਮਾਣਕ (authenticators), NIST Authenticator Assurance Level 3 (AAL3) ਭਰੋਸੇ ਵਾਲੇ ਪ੍ਰਮਾਣਕ, ਜਾਂ ਕੋਈ ਬਰਾਬਰ ਦੀ ਪ੍ਰਣਾਲੀ ਸ਼ਾਮਲ ਹੋ ਸਕਦੀ ਹੈ।

While this is a relatively aggressive stance on MFA, it is critical to raise the bar around this to protect users, and any attempt to relax these requirements should be accompanied by a clear plan on how the risks around authentication will be mitigated, taking into account NIST's guidance and research on the topic.

ਭਾਵੇਂ MFA ਬਾਰੇ ਇਹ ਮੁਕਾਬਲਤਨ ਸਖ਼ਤ ਰੁਖ਼ ਹੈ, ਉਪਭੋਗਤਾਵਾਂ ਦੀ ਸੁਰੱਖਿਆ ਲਈ ਇਸ ਸੰਬੰਧੀ ਮਿਆਰ ਉੱਚਾ ਚੁੱਕਣਾ ਬਹੁਤ ਜ਼ਰੂਰੀ ਹੈ, ਅਤੇ ਇਹਨਾਂ ਲੋੜਾਂ ਵਿੱਚ ਢਿੱਲ ਦੇਣ ਦੀ ਕਿਸੇ ਵੀ ਕੋਸ਼ਿਸ਼ ਦੇ ਨਾਲ ਇੱਕ ਸਪੱਸ਼ਟ ਯੋਜਨਾ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ ਕਿ ਪ੍ਰਮਾਣੀਕਰਨ ਸੰਬੰਧੀ ਜੋਖਮਾਂ ਨੂੰ ਕਿਵੇਂ ਘਟਾਇਆ ਜਾਵੇਗਾ, ਜਿਸ ਵਿੱਚ ਇਸ ਵਿਸ਼ੇ 'ਤੇ NIST ਦੇ ਮਾਰਗਦਰਸ਼ਨ ਅਤੇ ਖੋਜ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਿਆ ਜਾਵੇ।

Note that at the time of release, NIST SP 800-63 considers email as [not acceptable](https://pages.nist.gov/800-63-FAQ/#q-b11) as an authentication mechanism ([archived copy](https://web.archive.org/web/20250330115328/https://pages.nist.gov/800-63-FAQ/#q-b11)).

ਧਿਆਨ ਦਿਓ ਕਿ ਰਿਲੀਜ਼ ਦੇ ਸਮੇਂ, NIST SP 800-63 ਈਮੇਲ ਨੂੰ ਇੱਕ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਵਜੋਂ [ਸਵੀਕਾਰਯੋਗ ਨਹੀਂ](https://pages.nist.gov/800-63-FAQ/#q-b11) ਮੰਨਦਾ ਹੈ ([ਪੁਰਾਲੇਖ ਕਾਪੀ](https://web.archive.org/web/20250330115328/https://pages.nist.gov/800-63-FAQ/#q-b11))।

The requirements in this section relate to a variety of sections of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html), including: [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling), and [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding).

ਇਸ ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ [NIST ਦੇ ਮਾਰਗਦਰਸ਼ਨ](https://pages.nist.gov/800-63-3/sp800-63b.html) ਦੇ ਕਈ ਭਾਗਾਂ ਨਾਲ ਸੰਬੰਧਿਤ ਹਨ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ: [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling), ਅਤੇ [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding)।

| # | Description | Level |
| :---: | :--- | :---: |
| **6.3.1** | Verify that controls to prevent attacks such as credential stuffing and password brute force are implemented according to the application's security documentation. | 1 |
| **6.3.2** | Verify that default user accounts (e.g., "root", "admin", or "sa") are not present in the application or are disabled. | 1 |
| **6.3.3** | Verify that either a multi-factor authentication mechanism or a combination of single-factor authentication mechanisms, must be used in order to access the application. For L3, one of the factors must be a hardware-based authentication mechanism which provides compromise and impersonation resistance against phishing attacks while verifying the intent to authenticate by requiring a user-initiated action (such as a button press on a FIDO hardware key or a mobile phone). Relaxing any of the considerations in this requirement requires a fully documented rationale and a comprehensive set of mitigating controls. | 2 |
| **6.3.4** | Verify that, if the application includes multiple authentication pathways, there are no undocumented pathways and that security controls and authentication strength are enforced consistently. | 2 |
| **6.3.5** | Verify that users are notified of suspicious authentication attempts (successful or unsuccessful). This may include authentication attempts from an unusual location or client, partially successful authentication (only one of multiple factors), an authentication attempt after a long period of inactivity or a successful authentication after several unsuccessful attempts. | 3 |
| **6.3.6** | Verify that email is not used as either a single-factor or multi-factor authentication mechanism. | 3 |
| **6.3.7** | Verify that users are notified after updates to authentication details, such as credential resets or modification of the username or email address. | 3 |
| **6.3.8** | Verify that valid users cannot be deduced from failed authentication challenges, such as by basing on error messages, HTTP response codes, or different response times. Registration and forgot password functionality must also have this protection. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **6.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕ੍ਰੀਡੈਂਸ਼ੀਅਲ ਸਟਫ਼ਿੰਗ ਅਤੇ ਪਾਸਵਰਡ ਬਰੂਟ ਫੋਰਸ ਵਰਗੇ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਨਿਯੰਤਰਣ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਸੁਰੱਖਿਆ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਦੇ ਅਨੁਸਾਰ ਲਾਗੂ ਕੀਤੇ ਗਏ ਹਨ। | 1 |
| **6.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਡਿਫ਼ਾਲਟ ਉਪਭੋਗਤਾ ਖਾਤੇ (ਜਿਵੇਂ ਕਿ "root", "admin", ਜਾਂ "sa") ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਮੌਜੂਦ ਨਹੀਂ ਹਨ ਜਾਂ ਅਯੋਗ ਕੀਤੇ ਗਏ ਹਨ। | 1 |
| **6.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਤੱਕ ਪਹੁੰਚ ਕਰਨ ਲਈ ਜਾਂ ਤਾਂ ਇੱਕ ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਜਾਂ ਇੱਕ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀਆਂ ਦਾ ਸੁਮੇਲ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਵਰਤਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। L3 ਲਈ, ਕਾਰਕਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹਾਰਡਵੇਅਰ-ਆਧਾਰਿਤ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ ਜੋ ਫ਼ਿਸ਼ਿੰਗ ਹਮਲਿਆਂ ਦੇ ਵਿਰੁੱਧ ਸਮਝੌਤਾ ਅਤੇ ਪਛਾਣ-ਨਕਲ ਪ੍ਰਤੀ ਰੋਧਕਤਾ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ, ਅਤੇ ਨਾਲ ਹੀ ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਸ਼ੁਰੂ ਕੀਤੀ ਕਾਰਵਾਈ (ਜਿਵੇਂ ਕਿ FIDO ਹਾਰਡਵੇਅਰ ਕੁੰਜੀ ਜਾਂ ਮੋਬਾਈਲ ਫ਼ੋਨ 'ਤੇ ਬਟਨ ਦਬਾਉਣਾ) ਦੀ ਲੋੜ ਰੱਖ ਕੇ ਪ੍ਰਮਾਣੀਕਰਨ ਦੇ ਇਰਾਦੇ ਦੀ ਤਸਦੀਕ ਕਰਦੀ ਹੈ। ਇਸ ਲੋੜ ਦੇ ਕਿਸੇ ਵੀ ਵਿਚਾਰ ਵਿੱਚ ਢਿੱਲ ਦੇਣ ਲਈ ਇੱਕ ਪੂਰੀ ਤਰ੍ਹਾਂ ਦਸਤਾਵੇਜ਼ੀ ਤਰਕ ਅਤੇ ਘਟਾਉ ਨਿਯੰਤਰਣਾਂ ਦੇ ਇੱਕ ਵਿਆਪਕ ਸਮੂਹ ਦੀ ਲੋੜ ਹੈ। | 2 |
| **6.3.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਕਈ ਪ੍ਰਮਾਣੀਕਰਨ ਮਾਰਗ ਸ਼ਾਮਲ ਹਨ, ਤਾਂ ਕੋਈ ਵੀ ਗ਼ੈਰ-ਦਸਤਾਵੇਜ਼ੀ ਮਾਰਗ ਨਹੀਂ ਹੈ ਅਤੇ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਅਤੇ ਪ੍ਰਮਾਣੀਕਰਨ ਤਾਕਤ ਇਕਸਾਰ ਤੌਰ 'ਤੇ ਲਾਗੂ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। | 2 |
| **6.3.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਸ਼ੱਕੀ ਪ੍ਰਮਾਣੀਕਰਨ ਕੋਸ਼ਿਸ਼ਾਂ (ਸਫਲ ਜਾਂ ਅਸਫਲ) ਬਾਰੇ ਸੂਚਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਕਿਸੇ ਅਸਧਾਰਨ ਟਿਕਾਣੇ ਜਾਂ ਕਲਾਇੰਟ ਤੋਂ ਪ੍ਰਮਾਣੀਕਰਨ ਕੋਸ਼ਿਸ਼ਾਂ, ਅੰਸ਼ਕ ਤੌਰ 'ਤੇ ਸਫਲ ਪ੍ਰਮਾਣੀਕਰਨ (ਕਈ ਕਾਰਕਾਂ ਵਿੱਚੋਂ ਸਿਰਫ਼ ਇੱਕ), ਲੰਬੇ ਸਮੇਂ ਦੀ ਨਿਸ਼ਕਿਰਿਆ ਤੋਂ ਬਾਅਦ ਪ੍ਰਮਾਣੀਕਰਨ ਕੋਸ਼ਿਸ਼ ਜਾਂ ਕਈ ਅਸਫਲ ਕੋਸ਼ਿਸ਼ਾਂ ਤੋਂ ਬਾਅਦ ਸਫਲ ਪ੍ਰਮਾਣੀਕਰਨ ਸ਼ਾਮਲ ਹੋ ਸਕਦਾ ਹੈ। | 3 |
| **6.3.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਈਮੇਲ ਨੂੰ ਨਾ ਤਾਂ ਇੱਕ-ਕਾਰਕ ਅਤੇ ਨਾ ਹੀ ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਵਜੋਂ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। | 3 |
| **6.3.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰਮਾਣੀਕਰਨ ਵੇਰਵਿਆਂ ਵਿੱਚ ਅੱਪਡੇਟ ਤੋਂ ਬਾਅਦ, ਜਿਵੇਂ ਕਿ ਪ੍ਰਮਾਣ-ਪੱਤਰ ਰੀਸੈੱਟ ਜਾਂ ਉਪਭੋਗਤਾ ਨਾਂ ਜਾਂ ਈਮੇਲ ਪਤੇ ਵਿੱਚ ਸੋਧ, ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਸੂਚਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। | 3 |
| **6.3.8** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਅਸਫਲ ਪ੍ਰਮਾਣੀਕਰਨ ਚੁਣੌਤੀਆਂ ਤੋਂ ਜਾਇਜ਼ ਉਪਭੋਗਤਾਵਾਂ ਦਾ ਅਨੁਮਾਨ ਨਹੀਂ ਲਗਾਇਆ ਜਾ ਸਕਦਾ, ਜਿਵੇਂ ਕਿ ਗਲਤੀ ਸੁਨੇਹਿਆਂ, HTTP ਜਵਾਬ ਕੋਡਾਂ, ਜਾਂ ਵੱਖ-ਵੱਖ ਜਵਾਬ ਸਮਿਆਂ ਦੇ ਆਧਾਰ 'ਤੇ। ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਅਤੇ ਪਾਸਵਰਡ ਭੁੱਲ ਜਾਣ ਦੀ ਕਾਰਜਸ਼ੀਲਤਾ ਵਿੱਚ ਵੀ ਇਹ ਸੁਰੱਖਿਆ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ। | 3 |

## V6.4 Authentication Factor Lifecycle and Recovery
## V6.4 ਪ੍ਰਮਾਣੀਕਰਨ ਕਾਰਕ ਜੀਵਨ-ਚੱਕਰ ਅਤੇ ਰਿਕਵਰੀ

Authentication factors may include passwords, soft tokens, hardware tokens, and biometric devices. Securely handling the lifecycle of these mechanisms is critical to the security of an application, and this section includes requirements related to this.

ਪ੍ਰਮਾਣੀਕਰਨ ਕਾਰਕਾਂ ਵਿੱਚ ਪਾਸਵਰਡ, ਸਾਫ਼ਟ ਟੋਕਨ, ਹਾਰਡਵੇਅਰ ਟੋਕਨ, ਅਤੇ ਬਾਇਓਮੈਟ੍ਰਿਕ (biometric) ਡਿਵਾਈਸਾਂ ਸ਼ਾਮਲ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਹਨਾਂ ਪ੍ਰਣਾਲੀਆਂ ਦੇ ਜੀਵਨ-ਚੱਕਰ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਸੰਭਾਲਣਾ ਕਿਸੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਸੁਰੱਖਿਆ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ, ਅਤੇ ਇਸ ਭਾਗ ਵਿੱਚ ਇਸ ਨਾਲ ਸੰਬੰਧਿਤ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ।

The requirements in this section mostly relate to [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) or [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

ਇਸ ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ ਜ਼ਿਆਦਾਤਰ [NIST ਦੇ ਮਾਰਗਦਰਸ਼ਨ](https://pages.nist.gov/800-63-3/sp800-63b.html) ਦੇ [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) ਜਾਂ [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) ਨਾਲ ਸੰਬੰਧਿਤ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **6.4.1** | Verify that system generated initial passwords or activation codes are securely randomly generated, follow the existing password policy, and expire after a short period of time or after they are initially used. These initial secrets must not be permitted to become the long term password. | 1 |
| **6.4.2** | Verify that password hints or knowledge-based authentication (so-called "secret questions") are not present. | 1 |
| **6.4.3** | Verify that a secure process for resetting a forgotten password is implemented, that does not bypass any enabled multi-factor authentication mechanisms. | 2 |
| **6.4.4** | Verify that if a multi-factor authentication factor is lost, evidence of identity proofing is performed at the same level as during enrollment. | 2 |
| **6.4.5** | Verify that renewal instructions for authentication mechanisms which expire are sent with enough time to be carried out before the old authentication mechanism expires, configuring automated reminders if necessary. | 3 |
| **6.4.6** | Verify that administrative users can initiate the password reset process for the user, but that this does not allow them to change or choose the user's password. This prevents a situation where they know the user's password. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **6.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਿਸਟਮ ਦੁਆਰਾ ਪੈਦਾ ਕੀਤੇ ਸ਼ੁਰੂਆਤੀ ਪਾਸਵਰਡ ਜਾਂ ਸਰਗਰਮੀ ਕੋਡ (activation codes) ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਬੇਤਰਤੀਬ ਤੌਰ 'ਤੇ ਪੈਦਾ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਮੌਜੂਦਾ ਪਾਸਵਰਡ ਨੀਤੀ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹਨ, ਅਤੇ ਥੋੜ੍ਹੇ ਸਮੇਂ ਬਾਅਦ ਜਾਂ ਪਹਿਲੀ ਵਾਰ ਵਰਤੇ ਜਾਣ ਤੋਂ ਬਾਅਦ ਮਿਆਦ ਪੁੱਗ ਜਾਂਦੇ ਹਨ। ਇਹਨਾਂ ਸ਼ੁਰੂਆਤੀ ਭੇਦਾਂ ਨੂੰ ਲੰਬੇ ਸਮੇਂ ਦਾ ਪਾਸਵਰਡ ਬਣਨ ਦੀ ਇਜਾਜ਼ਤ ਨਹੀਂ ਹੋਣੀ ਚਾਹੀਦੀ। | 1 |
| **6.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪਾਸਵਰਡ ਸੰਕੇਤ (password hints) ਜਾਂ ਗਿਆਨ-ਆਧਾਰਿਤ ਪ੍ਰਮਾਣੀਕਰਨ (ਅਖੌਤੀ "ਗੁਪਤ ਸਵਾਲ") ਮੌਜੂਦ ਨਹੀਂ ਹਨ। | 1 |
| **6.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਭੁੱਲੇ ਹੋਏ ਪਾਸਵਰਡ ਨੂੰ ਰੀਸੈੱਟ ਕਰਨ ਲਈ ਇੱਕ ਸੁਰੱਖਿਅਤ ਪ੍ਰਕਿਰਿਆ ਲਾਗੂ ਕੀਤੀ ਗਈ ਹੈ, ਜੋ ਕਿਸੇ ਵੀ ਸਮਰੱਥ ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਨੂੰ ਬਾਈਪਾਸ ਨਹੀਂ ਕਰਦੀ। | 2 |
| **6.4.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜੇ ਕੋਈ ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ ਕਾਰਕ ਗੁਆਚ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਪਛਾਣ ਸਬੂਤੀਕਰਨ (identity proofing) ਦਾ ਸਬੂਤ ਉਸੇ ਪੱਧਰ 'ਤੇ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜਿਵੇਂ ਨਾਮਾਂਕਣ (enrollment) ਦੌਰਾਨ ਕੀਤਾ ਗਿਆ ਸੀ। | 2 |
| **6.4.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਮਿਆਦ ਪੁੱਗਣ ਵਾਲੀਆਂ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀਆਂ ਲਈ ਨਵੀਨੀਕਰਨ ਹਦਾਇਤਾਂ ਇੰਨੇ ਸਮੇਂ ਨਾਲ ਭੇਜੀਆਂ ਜਾਂਦੀਆਂ ਹਨ ਕਿ ਪੁਰਾਣੀ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਦੀ ਮਿਆਦ ਪੁੱਗਣ ਤੋਂ ਪਹਿਲਾਂ ਉਹਨਾਂ 'ਤੇ ਅਮਲ ਕੀਤਾ ਜਾ ਸਕੇ, ਅਤੇ ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ ਸਵੈਚਾਲਿਤ ਯਾਦ-ਦਹਾਨੀਆਂ ਕੌਨਫ਼ਿਗਰ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ। | 3 |
| **6.4.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰਸ਼ਾਸਕੀ ਉਪਭੋਗਤਾ ਉਪਭੋਗਤਾ ਲਈ ਪਾਸਵਰਡ ਰੀਸੈੱਟ ਪ੍ਰਕਿਰਿਆ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹਨ, ਪਰ ਇਹ ਉਹਨਾਂ ਨੂੰ ਉਪਭੋਗਤਾ ਦਾ ਪਾਸਵਰਡ ਬਦਲਣ ਜਾਂ ਚੁਣਨ ਦੀ ਇਜਾਜ਼ਤ ਨਹੀਂ ਦਿੰਦੀ। ਇਹ ਅਜਿਹੀ ਸਥਿਤੀ ਨੂੰ ਰੋਕਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਉਹ ਉਪਭੋਗਤਾ ਦਾ ਪਾਸਵਰਡ ਜਾਣਦੇ ਹੋਣ। | 3 |

## V6.5 General Multi-factor authentication requirements
## V6.5 ਆਮ ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ ਲੋੜਾਂ

This section provides general guidance that will be relevant to various different multi-factor authentication methods.

ਇਹ ਭਾਗ ਆਮ ਮਾਰਗਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਵੱਖ-ਵੱਖ ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ ਵਿਧੀਆਂ ਲਈ ਢੁਕਵਾਂ ਹੋਵੇਗਾ।

The mechanisms include:

ਇਹਨਾਂ ਪ੍ਰਣਾਲੀਆਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

* Lookup Secrets
* Time based One-time Passwords (TOTPs)
* Out-of-Band mechanisms

* ਲੁੱਕਅੱਪ ਭੇਦ (Lookup Secrets)
* ਸਮਾਂ-ਆਧਾਰਿਤ ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡ (Time based One-time Passwords, TOTP)
* ਆਊਟ-ਆਫ਼-ਬੈਂਡ (Out-of-Band) ਪ੍ਰਣਾਲੀਆਂ

Lookup secrets are pre-generated lists of secret codes, similar to Transaction Authorization Numbers (TAN), social media recovery codes, or a grid containing a set of random values. This type of authentication mechanism is considered "something you have" because the codes are deliberately not memorable so will need to be stored somewhere.

ਲੁੱਕਅੱਪ ਭੇਦ ਗੁਪਤ ਕੋਡਾਂ ਦੀਆਂ ਪਹਿਲਾਂ ਤੋਂ ਪੈਦਾ ਕੀਤੀਆਂ ਸੂਚੀਆਂ ਹਨ, ਜੋ ਲੈਣ-ਦੇਣ ਅਧਿਕਾਰੀਕਰਨ ਨੰਬਰਾਂ (Transaction Authorization Numbers, TAN), ਸੋਸ਼ਲ ਮੀਡੀਆ ਰਿਕਵਰੀ ਕੋਡਾਂ, ਜਾਂ ਬੇਤਰਤੀਬ ਮੁੱਲਾਂ ਦੇ ਸਮੂਹ ਵਾਲੇ ਗਰਿੱਡ ਵਰਗੀਆਂ ਹਨ। ਇਸ ਕਿਸਮ ਦੀ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਨੂੰ "ਕੁਝ ਜੋ ਤੁਹਾਡੇ ਕੋਲ ਹੈ" ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ ਕਿਉਂਕਿ ਇਹ ਕੋਡ ਜਾਣ-ਬੁੱਝ ਕੇ ਯਾਦ ਰੱਖਣ ਯੋਗ ਨਹੀਂ ਹੁੰਦੇ, ਇਸ ਲਈ ਇਹਨਾਂ ਨੂੰ ਕਿਤੇ ਸਟੋਰ ਕਰਨ ਦੀ ਲੋੜ ਪਵੇਗੀ।

Time based One-time Passwords (TOTPs) are physical or soft tokens that display a continually changing pseudo-random one-time challenge. This type of authentication mechanism is considered "something you have". Multi-factor TOTPs are similar to single-factor TOTPs, but require a valid PIN code, biometric unlocking, USB insertion or NFC pairing, or some additional value (such as transaction signing calculators) to be entered to create the final One-time Password (OTP).

ਸਮਾਂ-ਆਧਾਰਿਤ ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡ (TOTP) ਭੌਤਿਕ ਜਾਂ ਸਾਫ਼ਟ ਟੋਕਨ ਹਨ ਜੋ ਲਗਾਤਾਰ ਬਦਲਦੀ ਰਹਿਣ ਵਾਲੀ ਛਦਮ-ਬੇਤਰਤੀਬ (pseudo-random) ਇੱਕ-ਵਾਰੀ ਚੁਣੌਤੀ ਦਿਖਾਉਂਦੇ ਹਨ। ਇਸ ਕਿਸਮ ਦੀ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਨੂੰ "ਕੁਝ ਜੋ ਤੁਹਾਡੇ ਕੋਲ ਹੈ" ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ। ਬਹੁ-ਕਾਰਕ TOTP ਇੱਕ-ਕਾਰਕ TOTP ਵਰਗੇ ਹੀ ਹਨ, ਪਰ ਅੰਤਿਮ ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡ (OTP) ਬਣਾਉਣ ਲਈ ਇੱਕ ਜਾਇਜ਼ PIN ਕੋਡ, ਬਾਇਓਮੈਟ੍ਰਿਕ ਅਨਲੌਕਿੰਗ, USB ਲਗਾਉਣ ਜਾਂ NFC ਜੋੜੀ ਬਣਾਉਣ (pairing), ਜਾਂ ਕੋਈ ਵਾਧੂ ਮੁੱਲ (ਜਿਵੇਂ ਕਿ ਲੈਣ-ਦੇਣ ਦਸਤਖ਼ਤ ਕੈਲਕੁਲੇਟਰ) ਦਾਖ਼ਲ ਕੀਤੇ ਜਾਣ ਦੀ ਲੋੜ ਰੱਖਦੇ ਹਨ।

Details on out-of-band mechanisms will be provided in the next section.

ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਪ੍ਰਣਾਲੀਆਂ ਬਾਰੇ ਵੇਰਵੇ ਅਗਲੇ ਭਾਗ ਵਿੱਚ ਦਿੱਤੇ ਜਾਣਗੇ।

The requirements in these sections mostly relate to [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators), and [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

ਇਹਨਾਂ ਭਾਗਾਂ ਦੀਆਂ ਲੋੜਾਂ ਜ਼ਿਆਦਾਤਰ [NIST ਦੇ ਮਾਰਗਦਰਸ਼ਨ](https://pages.nist.gov/800-63-3/sp800-63b.html) ਦੇ [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators), ਅਤੇ [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) ਨਾਲ ਸੰਬੰਧਿਤ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **6.5.1** | Verify that lookup secrets, out-of-band authentication requests or codes, and time-based one-time passwords (TOTPs) are only successfully usable once. | 2 |
| **6.5.2** | Verify that, when being stored in the application's backend, lookup secrets with less than 112 bits of entropy (19 random alphanumeric characters or 34 random digits) are hashed with an approved password storage hashing algorithm that incorporates a 32-bit random salt. A standard hash function can be used if the secret has 112 bits of entropy or more. | 2 |
| **6.5.3** | Verify that lookup secrets, out-of-band authentication code, and time-based one-time password seeds, are generated using a Cryptographically Secure Pseudorandom Number Generator (CSPRNG) to avoid predictable values. | 2 |
| **6.5.4** | Verify that lookup secrets and out-of-band authentication codes have a minimum of 20 bits of entropy (typically 4 random alphanumeric characters or 6 random digits is sufficient). | 2 |
| **6.5.5** | Verify that out-of-band authentication requests, codes, or tokens, as well as time-based one-time passwords (TOTPs) have a defined lifetime. Out of band requests must have a maximum lifetime of 10 minutes and for TOTP a maximum lifetime of 30 seconds. | 2 |
| **6.5.6** | Verify that any authentication factor (including physical devices) can be revoked in case of theft or other loss. | 3 |
| **6.5.7** | Verify that biometric authentication mechanisms are only used as secondary factors together with either something you have or something you know. | 3 |
| **6.5.8** | Verify that time-based one-time passwords (TOTPs) are checked based on a time source from a trusted service and not from an untrusted or client provided time. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **6.5.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਲੁੱਕਅੱਪ ਭੇਦ, ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਪ੍ਰਮਾਣੀਕਰਨ ਬੇਨਤੀਆਂ ਜਾਂ ਕੋਡ, ਅਤੇ ਸਮਾਂ-ਆਧਾਰਿਤ ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡ (TOTP) ਸਿਰਫ਼ ਇੱਕ ਵਾਰ ਹੀ ਸਫਲਤਾਪੂਰਵਕ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ। | 2 |
| **6.5.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਬੈਕਐਂਡ ਵਿੱਚ ਸਟੋਰ ਕੀਤੇ ਜਾਣ ਸਮੇਂ, 112 ਬਿੱਟ ਤੋਂ ਘੱਟ ਐਂਟਰੋਪੀ (entropy) ਵਾਲੇ ਲੁੱਕਅੱਪ ਭੇਦਾਂ (19 ਬੇਤਰਤੀਬ ਅੱਖਰ-ਅੰਕ ਜਾਂ 34 ਬੇਤਰਤੀਬ ਅੰਕ) ਨੂੰ ਇੱਕ ਪ੍ਰਵਾਨਿਤ ਪਾਸਵਰਡ ਸਟੋਰੇਜ ਹੈਸ਼ਿੰਗ ਐਲਗੋਰਿਦਮ ਨਾਲ ਹੈਸ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ 32-ਬਿੱਟ ਬੇਤਰਤੀਬ ਸਾਲਟ (salt) ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ। ਜੇ ਭੇਦ ਵਿੱਚ 112 ਬਿੱਟ ਜਾਂ ਵੱਧ ਐਂਟਰੋਪੀ ਹੈ ਤਾਂ ਇੱਕ ਮਿਆਰੀ ਹੈਸ਼ ਫੰਕਸ਼ਨ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। | 2 |
| **6.5.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਲੁੱਕਅੱਪ ਭੇਦ, ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਪ੍ਰਮਾਣੀਕਰਨ ਕੋਡ, ਅਤੇ ਸਮਾਂ-ਆਧਾਰਿਤ ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡ ਸੀਡ (seeds), ਅਨੁਮਾਨਯੋਗ ਮੁੱਲਾਂ ਤੋਂ ਬਚਣ ਲਈ ਇੱਕ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਤੌਰ 'ਤੇ ਸੁਰੱਖਿਅਤ ਛਦਮ-ਬੇਤਰਤੀਬ ਨੰਬਰ ਜਨਰੇਟਰ (Cryptographically Secure Pseudorandom Number Generator, CSPRNG) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪੈਦਾ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। | 2 |
| **6.5.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਲੁੱਕਅੱਪ ਭੇਦਾਂ ਅਤੇ ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਪ੍ਰਮਾਣੀਕਰਨ ਕੋਡਾਂ ਵਿੱਚ ਘੱਟੋ-ਘੱਟ 20 ਬਿੱਟ ਐਂਟਰੋਪੀ ਹੈ (ਆਮ ਤੌਰ 'ਤੇ 4 ਬੇਤਰਤੀਬ ਅੱਖਰ-ਅੰਕ ਜਾਂ 6 ਬੇਤਰਤੀਬ ਅੰਕ ਕਾਫ਼ੀ ਹਨ)। | 2 |
| **6.5.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਪ੍ਰਮਾਣੀਕਰਨ ਬੇਨਤੀਆਂ, ਕੋਡਾਂ, ਜਾਂ ਟੋਕਨਾਂ, ਅਤੇ ਨਾਲ ਹੀ ਸਮਾਂ-ਆਧਾਰਿਤ ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡਾਂ (TOTP) ਦਾ ਇੱਕ ਪਰਿਭਾਸ਼ਿਤ ਜੀਵਨਕਾਲ ਹੈ। ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਬੇਨਤੀਆਂ ਦਾ ਵੱਧ ਤੋਂ ਵੱਧ ਜੀਵਨਕਾਲ 10 ਮਿੰਟ ਅਤੇ TOTP ਲਈ ਵੱਧ ਤੋਂ ਵੱਧ ਜੀਵਨਕਾਲ 30 ਸਕਿੰਟ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। | 2 |
| **6.5.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਚੋਰੀ ਜਾਂ ਹੋਰ ਨੁਕਸਾਨ ਦੀ ਸੂਰਤ ਵਿੱਚ ਕਿਸੇ ਵੀ ਪ੍ਰਮਾਣੀਕਰਨ ਕਾਰਕ (ਭੌਤਿਕ ਡਿਵਾਈਸਾਂ ਸਮੇਤ) ਨੂੰ ਰੱਦ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। | 3 |
| **6.5.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਬਾਇਓਮੈਟ੍ਰਿਕ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀਆਂ ਸਿਰਫ਼ ਸੈਕੰਡਰੀ ਕਾਰਕਾਂ ਵਜੋਂ ਵਰਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ, ਜਾਂ ਤਾਂ "ਕੁਝ ਜੋ ਤੁਹਾਡੇ ਕੋਲ ਹੈ" ਜਾਂ "ਕੁਝ ਜੋ ਤੁਸੀਂ ਜਾਣਦੇ ਹੋ" ਦੇ ਨਾਲ ਮਿਲ ਕੇ। | 3 |
| **6.5.8** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਮਾਂ-ਆਧਾਰਿਤ ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡਾਂ (TOTP) ਦੀ ਜਾਂਚ ਇੱਕ ਭਰੋਸੇਯੋਗ ਸੇਵਾ ਤੋਂ ਪ੍ਰਾਪਤ ਸਮਾਂ ਸਰੋਤ ਦੇ ਆਧਾਰ 'ਤੇ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਨਾ ਕਿ ਕਿਸੇ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਜਾਂ ਕਲਾਇੰਟ ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤੇ ਸਮੇਂ ਦੇ ਆਧਾਰ 'ਤੇ। | 3 |

## V6.6 Out-of-Band authentication mechanisms
## V6.6 ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀਆਂ

This usually involves the authentication server communicating with a physical device over a secure secondary channel. For example, sending push notifications to mobile devices. This type of authentication mechanism is considered "something you have".

ਇਸ ਵਿੱਚ ਆਮ ਤੌਰ 'ਤੇ ਪ੍ਰਮਾਣੀਕਰਨ ਸਰਵਰ ਦਾ ਇੱਕ ਸੁਰੱਖਿਅਤ ਸੈਕੰਡਰੀ ਚੈਨਲ ਰਾਹੀਂ ਕਿਸੇ ਭੌਤਿਕ ਡਿਵਾਈਸ ਨਾਲ ਸੰਚਾਰ ਕਰਨਾ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਮੋਬਾਈਲ ਡਿਵਾਈਸਾਂ ਨੂੰ ਪੁਸ਼ ਸੂਚਨਾਵਾਂ (push notifications) ਭੇਜਣਾ। ਇਸ ਕਿਸਮ ਦੀ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਨੂੰ "ਕੁਝ ਜੋ ਤੁਹਾਡੇ ਕੋਲ ਹੈ" ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ।

Unsafe out-of-band authentication mechanisms such as e-mail and VOIP are not permitted. PSTN and SMS authentication are currently considered to be ["restricted" authentication mechanisms](https://pages.nist.gov/800-63-FAQ/#q-b01) by NIST and should be deprecated in favor of Time based One-time Passwords (TOTPs), a cryptographic mechanism, or similar. NIST SP 800-63B [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network) recommends addressing the risks of device swap, SIM change, number porting, or other abnormal behavior, if telephone or SMS out-of-band authentication absolutely has to be supported. While this ASVS section does not mandate this as a requirement, not taking these precautions for a sensitive L2 app or an L3 app should be seen as a significant red flag.

ਈਮੇਲ ਅਤੇ VOIP ਵਰਗੀਆਂ ਅਸੁਰੱਖਿਅਤ ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਇਜਾਜ਼ਤ ਨਹੀਂ ਹੈ। PSTN ਅਤੇ SMS ਪ੍ਰਮਾਣੀਕਰਨ ਨੂੰ ਇਸ ਸਮੇਂ NIST ਦੁਆਰਾ ["ਪ੍ਰਤਿਬੰਧਿਤ" (restricted) ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀਆਂ](https://pages.nist.gov/800-63-FAQ/#q-b01) ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਇਹਨਾਂ ਨੂੰ ਸਮਾਂ-ਆਧਾਰਿਤ ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡਾਂ (TOTP), ਕਿਸੇ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਪ੍ਰਣਾਲੀ, ਜਾਂ ਇਸੇ ਤਰ੍ਹਾਂ ਦੀ ਕਿਸੇ ਹੋਰ ਪ੍ਰਣਾਲੀ ਨੂੰ ਤਰਜੀਹ ਦਿੰਦੇ ਹੋਏ ਅਪ੍ਰਚਲਿਤ (deprecate) ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। NIST SP 800-63B [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network) ਸਿਫ਼ਾਰਸ਼ ਕਰਦਾ ਹੈ ਕਿ, ਜੇ ਟੈਲੀਫ਼ੋਨ ਜਾਂ SMS ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਪ੍ਰਮਾਣੀਕਰਨ ਦਾ ਸਮਰਥਨ ਕਰਨਾ ਬਿਲਕੁਲ ਲਾਜ਼ਮੀ ਹੀ ਹੋਵੇ, ਤਾਂ ਡਿਵਾਈਸ ਦੀ ਅਦਲਾ-ਬਦਲੀ, SIM ਬਦਲਣ, ਨੰਬਰ ਪੋਰਟਿੰਗ (number porting), ਜਾਂ ਹੋਰ ਅਸਧਾਰਨ ਵਿਹਾਰ ਦੇ ਜੋਖਮਾਂ ਨਾਲ ਨਜਿੱਠਿਆ ਜਾਵੇ। ਭਾਵੇਂ ASVS ਦਾ ਇਹ ਭਾਗ ਇਸ ਨੂੰ ਇੱਕ ਲੋੜ ਵਜੋਂ ਲਾਜ਼ਮੀ ਨਹੀਂ ਕਰਦਾ, ਕਿਸੇ ਸੰਵੇਦਨਸ਼ੀਲ L2 ਐਪ ਜਾਂ L3 ਐਪ ਲਈ ਇਹ ਸਾਵਧਾਨੀਆਂ ਨਾ ਵਰਤਣ ਨੂੰ ਇੱਕ ਗੰਭੀਰ ਚੇਤਾਵਨੀ ਸੰਕੇਤ (red flag) ਵਜੋਂ ਵੇਖਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

Note that NIST has also recently provided guidance which [discourages the use of push notifications](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/#fig-3). While this ASVS section does not do so, it is important to be aware of the risks of "push bombing".

ਧਿਆਨ ਦਿਓ ਕਿ NIST ਨੇ ਹਾਲ ਹੀ ਵਿੱਚ ਅਜਿਹਾ ਮਾਰਗਦਰਸ਼ਨ ਵੀ ਪ੍ਰਦਾਨ ਕੀਤਾ ਹੈ ਜੋ [ਪੁਸ਼ ਸੂਚਨਾਵਾਂ ਦੀ ਵਰਤੋਂ ਨੂੰ ਨਿਰਉਤਸ਼ਾਹਿਤ ਕਰਦਾ ਹੈ](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/#fig-3)। ਭਾਵੇਂ ASVS ਦਾ ਇਹ ਭਾਗ ਅਜਿਹਾ ਨਹੀਂ ਕਰਦਾ, "ਪੁਸ਼ ਬੌਂਬਿੰਗ" (push bombing) ਦੇ ਜੋਖਮਾਂ ਤੋਂ ਜਾਣੂ ਹੋਣਾ ਮਹੱਤਵਪੂਰਨ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **6.6.1** | Verify that authentication mechanisms using the Public Switched Telephone Network (PSTN) to deliver One-time Passwords (OTPs) via phone or SMS are offered only when the phone number has previously been validated, alternate stronger methods (such as Time based One-time Passwords) are also offered, and the service provides information on their security risks to users. For L3 applications, phone and SMS must not be available as options. | 2 |
| **6.6.2** | Verify that out-of-band authentication requests, codes, or tokens are bound to the original authentication request for which they were generated and are not usable for a previous or subsequent one. | 2 |
| **6.6.3** | Verify that a code based out-of-band authentication mechanism is protected against brute force attacks by using rate limiting. Consider also using a code with at least 64 bits of entropy. | 2 |
| **6.6.4** | Verify that, where push notifications are used for multi-factor authentication, rate limiting is used to prevent push bombing attacks. Number matching may also mitigate this risk. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **6.6.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਫ਼ੋਨ ਜਾਂ SMS ਰਾਹੀਂ ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡ (OTP) ਪਹੁੰਚਾਉਣ ਲਈ ਜਨਤਕ ਸਵਿੱਚਡ ਟੈਲੀਫ਼ੋਨ ਨੈੱਟਵਰਕ (Public Switched Telephone Network, PSTN) ਦੀ ਵਰਤੋਂ ਕਰਨ ਵਾਲੀਆਂ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀਆਂ ਸਿਰਫ਼ ਉਦੋਂ ਹੀ ਪੇਸ਼ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ ਜਦੋਂ ਫ਼ੋਨ ਨੰਬਰ ਨੂੰ ਪਹਿਲਾਂ ਪ੍ਰਮਾਣਿਤ ਕੀਤਾ ਜਾ ਚੁੱਕਾ ਹੋਵੇ, ਬਦਲਵੀਆਂ ਵਧੇਰੇ ਮਜ਼ਬੂਤ ਵਿਧੀਆਂ (ਜਿਵੇਂ ਕਿ ਸਮਾਂ-ਆਧਾਰਿਤ ਇੱਕ-ਵਾਰੀ ਪਾਸਵਰਡ) ਵੀ ਪੇਸ਼ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹੋਣ, ਅਤੇ ਸੇਵਾ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਇਹਨਾਂ ਦੇ ਸੁਰੱਖਿਆ ਜੋਖਮਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੋਵੇ। L3 ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ, ਫ਼ੋਨ ਅਤੇ SMS ਵਿਕਲਪਾਂ ਵਜੋਂ ਉਪਲਬਧ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ। | 2 |
| **6.6.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਪ੍ਰਮਾਣੀਕਰਨ ਬੇਨਤੀਆਂ, ਕੋਡ, ਜਾਂ ਟੋਕਨ ਉਸ ਮੂਲ ਪ੍ਰਮਾਣੀਕਰਨ ਬੇਨਤੀ ਨਾਲ ਬੱਧ ਹਨ ਜਿਸ ਲਈ ਉਹ ਪੈਦਾ ਕੀਤੇ ਗਏ ਸਨ, ਅਤੇ ਕਿਸੇ ਪਿਛਲੀ ਜਾਂ ਅਗਲੀ ਬੇਨਤੀ ਲਈ ਵਰਤਣਯੋਗ ਨਹੀਂ ਹਨ। | 2 |
| **6.6.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕੋਡ-ਆਧਾਰਿਤ ਆਊਟ-ਆਫ਼-ਬੈਂਡ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਦਰ ਸੀਮਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬਰੂਟ ਫੋਰਸ ਹਮਲਿਆਂ ਤੋਂ ਸੁਰੱਖਿਅਤ ਹੈ। ਘੱਟੋ-ਘੱਟ 64 ਬਿੱਟ ਐਂਟਰੋਪੀ ਵਾਲਾ ਕੋਡ ਵਰਤਣ 'ਤੇ ਵੀ ਵਿਚਾਰ ਕਰੋ। | 2 |
| **6.6.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜਿੱਥੇ ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ ਲਈ ਪੁਸ਼ ਸੂਚਨਾਵਾਂ ਵਰਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ, ਉੱਥੇ ਪੁਸ਼ ਬੌਂਬਿੰਗ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਦਰ ਸੀਮਾ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਨੰਬਰ ਮਿਲਾਨ (number matching) ਵੀ ਇਸ ਜੋਖਮ ਨੂੰ ਘਟਾ ਸਕਦਾ ਹੈ। | 3 |

## V6.7 Cryptographic authentication mechanism
## V6.7 ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ

Cryptographic authentication mechanisms include smart cards or FIDO keys, where the user has to plug in or pair the cryptographic device to the computer to complete authentication. The authentication server will send a challenge nonce to the cryptographic device or software, and the device or software calculates a response based upon a securely stored cryptographic key. The requirements in this section provide implementation-specific guidance for these mechanisms, with guidance on cryptographic algorithms being covered in the "Cryptography" chapter.

ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀਆਂ ਵਿੱਚ ਸਮਾਰਟ ਕਾਰਡ ਜਾਂ FIDO ਕੁੰਜੀਆਂ ਸ਼ਾਮਲ ਹਨ, ਜਿੱਥੇ ਪ੍ਰਮਾਣੀਕਰਨ ਪੂਰਾ ਕਰਨ ਲਈ ਉਪਭੋਗਤਾ ਨੂੰ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਡਿਵਾਈਸ ਨੂੰ ਕੰਪਿਊਟਰ ਨਾਲ ਲਗਾਉਣਾ ਜਾਂ ਜੋੜੀ ਬਣਾਉਣੀ (pair) ਪੈਂਦੀ ਹੈ। ਪ੍ਰਮਾਣੀਕਰਨ ਸਰਵਰ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਡਿਵਾਈਸ ਜਾਂ ਸਾਫ਼ਟਵੇਅਰ ਨੂੰ ਇੱਕ ਚੁਣੌਤੀ ਨੌਂਸ (challenge nonce) ਭੇਜੇਗਾ, ਅਤੇ ਡਿਵਾਈਸ ਜਾਂ ਸਾਫ਼ਟਵੇਅਰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਸਟੋਰ ਕੀਤੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕੁੰਜੀ ਦੇ ਆਧਾਰ 'ਤੇ ਇੱਕ ਜਵਾਬ ਦੀ ਗਣਨਾ ਕਰਦਾ ਹੈ। ਇਸ ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ ਇਹਨਾਂ ਪ੍ਰਣਾਲੀਆਂ ਲਈ ਲਾਗੂਕਰਨ-ਖ਼ਾਸ ਮਾਰਗਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦੀਆਂ ਹਨ, ਜਦੋਂ ਕਿ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਐਲਗੋਰਿਦਮਾਂ ਬਾਰੇ ਮਾਰਗਦਰਸ਼ਨ "ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ" (Cryptography) ਅਧਿਆਇ ਵਿੱਚ ਕਵਰ ਕੀਤਾ ਗਿਆ ਹੈ।

Where shared or secret keys are used for cryptographic authentication, these should be stored using the same mechanisms as other system secrets, as documented in the "Secret Management" section in the "Configuration" chapter.

ਜਿੱਥੇ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਪ੍ਰਮਾਣੀਕਰਨ ਲਈ ਸਾਂਝੀਆਂ ਜਾਂ ਗੁਪਤ ਕੁੰਜੀਆਂ ਵਰਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ, ਉੱਥੇ ਇਹਨਾਂ ਨੂੰ ਹੋਰ ਸਿਸਟਮ ਭੇਦਾਂ ਵਾਂਗ ਹੀ ਉਹਨਾਂ ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਟੋਰ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ "ਸੰਰਚਨਾ" (Configuration) ਅਧਿਆਇ ਦੇ "ਭੇਦ ਪ੍ਰਬੰਧਨ" (Secret Management) ਭਾਗ ਵਿੱਚ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਵਿੱਚ ਦਰਜ ਹੈ।

The requirements in this section mostly relate to [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

ਇਸ ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ ਜ਼ਿਆਦਾਤਰ [NIST ਦੇ ਮਾਰਗਦਰਸ਼ਨ](https://pages.nist.gov/800-63-3/sp800-63b.html) ਦੇ [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) ਨਾਲ ਸੰਬੰਧਿਤ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **6.7.1** | Verify that the certificates used to verify cryptographic authentication assertions are stored in a way protects them from modification. | 3 |
| **6.7.2** | Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **6.7.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਪ੍ਰਮਾਣੀਕਰਨ ਅਸਰਸ਼ਨਾਂ (assertions) ਦੀ ਤਸਦੀਕ ਕਰਨ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਸਰਟੀਫ਼ਿਕੇਟ ਇਸ ਤਰੀਕੇ ਨਾਲ ਸਟੋਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਜੋ ਉਹਨਾਂ ਨੂੰ ਸੋਧ ਤੋਂ ਸੁਰੱਖਿਅਤ ਰੱਖਦਾ ਹੈ। | 3 |
| **6.7.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਚੁਣੌਤੀ ਨੌਂਸ ਘੱਟੋ-ਘੱਟ 64 ਬਿੱਟ ਲੰਬਾ ਹੈ, ਅਤੇ ਅੰਕੜਾ-ਵਿਗਿਆਨਕ ਤੌਰ 'ਤੇ ਵਿਲੱਖਣ ਹੈ ਜਾਂ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਡਿਵਾਈਸ ਦੇ ਪੂਰੇ ਜੀਵਨਕਾਲ ਦੌਰਾਨ ਵਿਲੱਖਣ ਹੈ। | 3 |

## V6.8 Authentication with an Identity Provider
## V6.8 ਪਛਾਣ ਪ੍ਰਦਾਤਾ ਨਾਲ ਪ੍ਰਮਾਣੀਕਰਨ

Identity Providers (IdPs) provide federated identity for users. Users will often have more than one identity with multiple IdPs, such as an enterprise identity using Azure AD, Okta, Ping Identity, or Google, or consumer identity using Facebook, Twitter, Google, or WeChat, to name just a few common alternatives. This list is not an endorsement of these companies or services, but simply an encouragement for developers to consider the reality that many users have many established identities. Organizations should consider integrating with existing user identities, as per the risk profile of the IdP's strength of identity proofing. For example, it is unlikely a government organization would accept a social media identity as a login for sensitive systems, as it is easy to create fake or throwaway identities, whereas a mobile game company may well need to integrate with major social media platforms to grow their active player base.

ਪਛਾਣ ਪ੍ਰਦਾਤਾ (Identity Providers, IdP) ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਸੰਘੀ ਪਛਾਣ (federated identity) ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ। ਉਪਭੋਗਤਾਵਾਂ ਕੋਲ ਅਕਸਰ ਕਈ IdP ਨਾਲ ਇੱਕ ਤੋਂ ਵੱਧ ਪਛਾਣਾਂ ਹੁੰਦੀਆਂ ਹਨ, ਜਿਵੇਂ ਕਿ Azure AD, Okta, Ping Identity, ਜਾਂ Google ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਇੱਕ ਸੰਸਥਾਗਤ (enterprise) ਪਛਾਣ, ਜਾਂ Facebook, Twitter, Google, ਜਾਂ WeChat ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਇੱਕ ਖਪਤਕਾਰ ਪਛਾਣ — ਕੁਝ ਕੁ ਆਮ ਬਦਲਾਂ ਦਾ ਨਾਂ ਲੈਣ ਲਈ। ਇਹ ਸੂਚੀ ਇਹਨਾਂ ਕੰਪਨੀਆਂ ਜਾਂ ਸੇਵਾਵਾਂ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਨਹੀਂ ਹੈ, ਸਗੋਂ ਵਿਕਾਸਕਾਰਾਂ ਲਈ ਇਸ ਹਕੀਕਤ 'ਤੇ ਵਿਚਾਰ ਕਰਨ ਦਾ ਸਿਰਫ਼ ਇੱਕ ਉਤਸ਼ਾਹ ਹੈ ਕਿ ਬਹੁਤ ਸਾਰੇ ਉਪਭੋਗਤਾਵਾਂ ਕੋਲ ਬਹੁਤ ਸਾਰੀਆਂ ਸਥਾਪਿਤ ਪਛਾਣਾਂ ਹਨ। ਸੰਸਥਾਵਾਂ ਨੂੰ IdP ਦੀ ਪਛਾਣ ਸਬੂਤੀਕਰਨ ਦੀ ਤਾਕਤ ਦੇ ਜੋਖਮ ਪ੍ਰੋਫ਼ਾਈਲ ਦੇ ਅਨੁਸਾਰ, ਮੌਜੂਦਾ ਉਪਭੋਗਤਾ ਪਛਾਣਾਂ ਨਾਲ ਏਕੀਕਰਨ ਕਰਨ 'ਤੇ ਵਿਚਾਰ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਇਸ ਦੀ ਸੰਭਾਵਨਾ ਘੱਟ ਹੈ ਕਿ ਕੋਈ ਸਰਕਾਰੀ ਸੰਸਥਾ ਸੰਵੇਦਨਸ਼ੀਲ ਸਿਸਟਮਾਂ ਲਈ ਲੌਗਇਨ ਵਜੋਂ ਸੋਸ਼ਲ ਮੀਡੀਆ ਪਛਾਣ ਨੂੰ ਸਵੀਕਾਰ ਕਰੇਗੀ, ਕਿਉਂਕਿ ਜਾਅਲੀ ਜਾਂ ਅਸਥਾਈ (throwaway) ਪਛਾਣਾਂ ਬਣਾਉਣਾ ਆਸਾਨ ਹੈ, ਜਦੋਂ ਕਿ ਕਿਸੇ ਮੋਬਾਈਲ ਗੇਮ ਕੰਪਨੀ ਨੂੰ ਆਪਣੇ ਸਰਗਰਮ ਖਿਡਾਰੀ ਆਧਾਰ ਨੂੰ ਵਧਾਉਣ ਲਈ ਮੁੱਖ ਸੋਸ਼ਲ ਮੀਡੀਆ ਪਲੇਟਫ਼ਾਰਮਾਂ ਨਾਲ ਏਕੀਕਰਨ ਦੀ ਸੱਚਮੁੱਚ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ।

Secure use of external identity providers requires careful configuration and verification to prevent identity spoofing or forged assertions. This section provides requirements to address these risks.

ਬਾਹਰੀ ਪਛਾਣ ਪ੍ਰਦਾਤਾਵਾਂ ਦੀ ਸੁਰੱਖਿਅਤ ਵਰਤੋਂ ਲਈ ਪਛਾਣ ਸਪੂਫ਼ਿੰਗ (identity spoofing) ਜਾਂ ਜਾਅਲੀ ਅਸਰਸ਼ਨਾਂ ਨੂੰ ਰੋਕਣ ਵਾਸਤੇ ਸਾਵਧਾਨ ਸੰਰਚਨਾ ਅਤੇ ਤਸਦੀਕ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਇਹ ਭਾਗ ਇਹਨਾਂ ਜੋਖਮਾਂ ਨਾਲ ਨਜਿੱਠਣ ਲਈ ਲੋੜਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **6.8.1** | Verify that, if the application supports multiple identity providers (IdPs), the user's identity cannot be spoofed via another supported identity provider (eg. by using the same user identifier). The standard mitigation would be for the application to register and identify the user using a combination of the IdP ID (serving as a namespace) and the user's ID in the IdP. | 2 |
| **6.8.2** | Verify that the presence and integrity of digital signatures on authentication assertions (for example on JWTs or SAML assertions) are always validated, rejecting any assertions that are unsigned or have invalid signatures. | 2 |
| **6.8.3** | Verify that SAML assertions are uniquely processed and used only once within the validity period to prevent replay attacks. | 2 |
| **6.8.4** | Verify that, if an application uses a separate Identity Provider (IdP) and expects specific authentication strength, methods, or recentness for specific functions, the application verifies this using the information returned by the IdP. For example, if OIDC is used, this might be achieved by validating ID Token claims such as 'acr', 'amr', and 'auth_time' (if present). If the IdP does not provide this information, the application must have a documented fallback approach that assumes that the minimum strength authentication mechanism was used (for example, single-factor authentication using username and password). | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **6.8.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ ਐਪਲੀਕੇਸ਼ਨ ਕਈ ਪਛਾਣ ਪ੍ਰਦਾਤਾਵਾਂ (IdP) ਦਾ ਸਮਰਥਨ ਕਰਦੀ ਹੈ, ਤਾਂ ਉਪਭੋਗਤਾ ਦੀ ਪਛਾਣ ਕਿਸੇ ਹੋਰ ਸਮਰਥਿਤ ਪਛਾਣ ਪ੍ਰਦਾਤਾ ਰਾਹੀਂ ਸਪੂਫ਼ ਨਹੀਂ ਕੀਤੀ ਜਾ ਸਕਦੀ (ਜਿਵੇਂ ਕਿ ਉਹੀ ਉਪਭੋਗਤਾ ਪਛਾਣਕਰਤਾ ਵਰਤ ਕੇ)। ਮਿਆਰੀ ਘਟਾਉ ਇਹ ਹੋਵੇਗਾ ਕਿ ਐਪਲੀਕੇਸ਼ਨ IdP ID (ਜੋ ਨੇਮਸਪੇਸ ਵਜੋਂ ਕੰਮ ਕਰਦੀ ਹੈ) ਅਤੇ IdP ਵਿੱਚ ਉਪਭੋਗਤਾ ਦੀ ID ਦੇ ਸੁਮੇਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਉਪਭੋਗਤਾ ਨੂੰ ਰਜਿਸਟਰ ਅਤੇ ਪਛਾਣ ਕਰੇ। | 2 |
| **6.8.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰਮਾਣੀਕਰਨ ਅਸਰਸ਼ਨਾਂ (ਉਦਾਹਰਨ ਲਈ JWT ਜਾਂ SAML ਅਸਰਸ਼ਨਾਂ) 'ਤੇ ਡਿਜ਼ੀਟਲ ਦਸਤਖ਼ਤਾਂ ਦੀ ਮੌਜੂਦਗੀ ਅਤੇ ਅਖੰਡਤਾ (integrity) ਨੂੰ ਹਮੇਸ਼ਾ ਪ੍ਰਮਾਣਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਕਿਸੇ ਵੀ ਅਜਿਹੀ ਅਸਰਸ਼ਨ ਨੂੰ ਰੱਦ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜੋ ਦਸਤਖ਼ਤ-ਰਹਿਤ ਹੈ ਜਾਂ ਜਿਸ ਦੇ ਦਸਤਖ਼ਤ ਜਾਇਜ਼ ਨਹੀਂ ਹਨ। | 2 |
| **6.8.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਰੀਪਲੇ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ SAML ਅਸਰਸ਼ਨਾਂ ਨੂੰ ਵਿਲੱਖਣ ਤੌਰ 'ਤੇ ਪ੍ਰੋਸੈੱਸ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਜਾਇਜ਼ਤਾ ਮਿਆਦ (validity period) ਦੇ ਅੰਦਰ ਸਿਰਫ਼ ਇੱਕ ਵਾਰ ਹੀ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। | 2 |
| **6.8.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ ਕੋਈ ਐਪਲੀਕੇਸ਼ਨ ਇੱਕ ਵੱਖਰੇ ਪਛਾਣ ਪ੍ਰਦਾਤਾ (IdP) ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ ਅਤੇ ਖ਼ਾਸ ਫੰਕਸ਼ਨਾਂ ਲਈ ਖ਼ਾਸ ਪ੍ਰਮਾਣੀਕਰਨ ਤਾਕਤ, ਵਿਧੀਆਂ, ਜਾਂ ਤਾਜ਼ਗੀ (recentness) ਦੀ ਉਮੀਦ ਰੱਖਦੀ ਹੈ, ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ IdP ਦੁਆਰਾ ਵਾਪਸ ਭੇਜੀ ਗਈ ਜਾਣਕਾਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸ ਦੀ ਤਸਦੀਕ ਕਰਦੀ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਜੇ OIDC ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਇਹ ID Token ਦੇ ਦਾਅਵਿਆਂ (claims) ਜਿਵੇਂ ਕਿ 'acr', 'amr', ਅਤੇ 'auth_time' (ਜੇ ਮੌਜੂਦ ਹੋਣ) ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਕੇ ਹਾਸਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਜੇ IdP ਇਹ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਨਹੀਂ ਕਰਦਾ, ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ ਕੋਲ ਇੱਕ ਦਸਤਾਵੇਜ਼ੀ ਫ਼ਾਲਬੈਕ (fallback) ਪਹੁੰਚ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ ਜੋ ਇਹ ਮੰਨਦੀ ਹੈ ਕਿ ਘੱਟੋ-ਘੱਟ ਤਾਕਤ ਵਾਲੀ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਣਾਲੀ ਵਰਤੀ ਗਈ ਸੀ (ਉਦਾਹਰਨ ਲਈ, ਉਪਭੋਗਤਾ ਨਾਂ ਅਤੇ ਪਾਸਵਰਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ)। | 2 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [NIST SP 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST SP 800-63B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST SP 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Web Security Testing Guide: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/04-Authentication_Testing)
* [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Choosing and Using Security Questions Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
* [CISA Guidance on "Number Matching"](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
* [Details on the FIDO Alliance](https://fidoalliance.org/)
