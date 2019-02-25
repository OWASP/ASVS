# V6: Stored Cryptography Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* All cryptographic modules fail in a secure manner and that errors are handled correctly.
* A suitable random number generator is used.
* Access to keys is managed in a secure way.

## 6.1 Data Classification

The most important asset is the data processed, stored or transmitted by an application. Always perform a privacy impact assessment to correctly classify the data protection needs of any stored data.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.1.1** | Verify that regulated private data is stored encrypted while at rest, such as personally identifiable information (PII), sensitive personal information, or data assessed likely to be subject to EU's GDPR. |  | ✓ | ✓ | 311 |
| **6.1.2** | Verify that regulated health data is stored encrypted while at rest, such as medical records, medical device details, or de-anonymized research records. |  | ✓ | ✓ | 311 |
| **6.1.3** | Verify that regulated financial data is stored encrypted while at rest, such as financial accounts, defaults or credit history, tax records, pay history, beneficiaries, or de-anonymized market or research records. |  | ✓ | ✓ | 311 |

## 6.2 Algorithms

Recent advances in cryptography mean that previously safe algorithms and key lengths are no longer safe or sufficient to protect data. Therefore, it should be possible to change algorithms.

Although this section is not easily penetration tested, developers should consider this entire section as mandatory even though L1 is missing from most of the items.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.2.1** | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable Padding Oracle attacks. | ✓ | ✓ | ✓ | 310 |
| **6.2.2** | Verify that industry proven or government approved cryptographic algorithms, modes, and libraries are used, instead of custom coded cryptography. ([C8](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering)) | | ✓ | ✓ | 327 |
| **6.2.3** | Verify that encryption initialization vector, cipher configuration, and block modes are configured securely using the latest advice. |  | ✓ | ✓ | 326 |
| **6.2.4** | Verify that random number, encryption or hashing algorithms, key lengths, rounds, ciphers or modes, can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks. ([C8](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering)) | | ✓ | ✓ | 326 |

## 6.3 Random Values

True pseudo-random number generation (PRNG) is incredibly difficult to get right. Generally, good sources of entropy within a system will be quickly depleted if over-used, but sources with less randomness can lead to predictable keys and secrets.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.3.1** | Verify that all random numbers, random file names, and random strings are generated using the cryptographic module's approved random number generator when these random values are intended to be not guessable by an attacker. |  | ✓ | ✓ | 338 |
| **6.3.2** | Verify that random GUIDs are created using the GUID v4 algorithm, and a cryptographically-secure pseudo-random number generator (CSPRNG). GUIDs created using other pseudo-random number generators may be predictable. |  | ✓ | ✓ | 338 |
| **6.3.3** | Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances. |  |  | ✓ | 338 |

## 6.4 Secret Management

Although this section is not easily penetration tested, developers should consider this entire section as mandatory even though L1 is missing from most of the items.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.4.1** | Verify that a secrets management solution such as a key vault is used to securely create, store, control access to and destroy secrets. ([C8](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering)) | | ✓ | ✓ | 798 |
| **6.4.2** | Verify that key material is not exposed to the application but instead uses an isolated security module like a vault for cryptographic operations. ([C8](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering)) | | ✓ | ✓ | 320 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Testing for weak Cryptography](https://www.owasp.org/index.php/Testing_for_weak_Cryptography)
* [OWASP Cheat Sheet: Cryptographic Storage](https://www.owasp.org/index.php/Cryptographic_Storage_Cheat_Sheet)
* [FIPS 140-2](https://csrc.nist.gov/publications/detail/fips/140/2/final)
