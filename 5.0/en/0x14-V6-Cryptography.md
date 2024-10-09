# V6 Stored Cryptography

## Control Objective

## Control Objective

Ensure that the application adopts a proactive, adaptive, and holistic approach to cryptographic security by:

- Implementing robust cryptographic systems that fail securely, adapt to evolving threats, and are future-proof.
- Utilizing cryptographic mechanisms that are both secure and aligned with industry best practices.
- Maintaining a secure cryptographic key management system with appropriate access controls and auditing.
- Regularly evaluating the cryptographic landscape to assess new risks and adapt algorithms accordingly.
- Discovering and managing cryptographic use cases throughout the application's lifecycle to ensure that all cryptographic assets are accounted for and secured.

## V6.1 Data Classification and Cryptographic Inventory

The most important asset is the data processed, stored, or transmitted by an application. Always perform a privacy impact assessment to classify the data protection needs of any stored data correctly. In addition, ensure that all cryptographic assets, such as algorithms, keys, and certificates, are regularly discovered, inventoried, and assessed.

|     #     | Description                                                                                                                                                                                                                                                                                         | L1  | L2  | L3  | CWE |
| :-------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-: |
| **6.1.1** | Verify that regulated data, such as private, health, and financial, is stored encrypted while at rest with at least 112-bit encryption, ideally 256-bit, such as Personally Identifiable Information (PII), sensitive personal information, or data assessed likely to be subject to the EU's GDPR. |     |  ✓  |  ✓  | 311 |
| **6.1.2** | Verify that a cryptographic inventory performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application.                                                                                                                              |     |  ✓  |  ✓  | 311 |
| **6.1.3** | Verify that cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations.                                                                                                                     |     |  ✓  |  ✓  | 311 |
| **6.1.4** | Verify that regulated health data is stored encrypted while at rest, such as medical records, medical device details, or de-anonymized research records.                                                                                                                                            |     |  ✓  |  ✓  | 311 |
| **6.1.5** | Verify that regulated financial data is stored encrypted while at rest, such as financial accounts, defaults or credit history, tax records, pay history, beneficiaries, or de-anonymized market or research records.                                                                               |     |  ✓  |  ✓  | 311 |

## V6.2 Algorithms

Recent advances in cryptography mean that previously safe algorithms and key lengths are no longer safe or sufficient to protect data. Therefore, it should be possible to change algorithms.

Although this section is not easily penetration tested, developers should consider this entire section as mandatory even though L1 is missing from most of the items.

|     #     | Description                                                                                                                                                                                                          | L1  | L2  | L3  | CWE |
| :-------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-: |
| **6.2.1** | All cryptographic modules must fail securely to prevent vulnerabilities like Padding Oracle attacks.                                                                                                                 |  ✓  |  ✓  |  ✓  | 310 |
| **6.2.2** | Verify that industry proven or government approved cryptographic algorithms, modes, and libraries are used, instead of custom coded cryptography.                                                                    |     |  ✓  |  ✓  | 327 |
| **6.2.3** | Verify that random number, encryption or hashing algorithms, key lengths, rounds, ciphers or modes, can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks.                  |     |  ✓  |  ✓  | 326 |
| **6.2.4** | Verify that insecure block modes (e.g., ECB) and weak padding schemes (e.g., PKCS#1 v1.5) are not used.                                                                                                              |     |  ✓  |  ✓  | 326 |
| **6.2.5** | Verify that insecure ciphers, including Triple-DES and Blowfish, are not used but secure modes** like AES with GCM are.                                                                                |  ✓  |  ✓  |  ✓  | 326 |
| **6.2.6** | Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key/data-element pair. The method of generation must be appropriate for the algorithm being used. |     |     |  ✓  | 326 |
| **6.2.7** | Verify that encrypted data is authenticated via signatures, authenticated cipher modes, or HMAC to ensure that ciphertext is not altered by an unauthorized party.                                                   |     |     |  ✓  | 326 |
| **6.2.8** | Verify that all cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information.                                               |     |     |  ✓  | 385 |

## V6.3 Hashing and Hash-based Functions

Cryptographic hashes are used in a wide variety of cryptographic protocols, such as digital signatures, HMAC, key derivation functions (KDF), random bit generation, and password storage. The security of the cryptographic system is only as strong as the underlying hash functions used. This section outlines the requirements for using secure hash functions in cryptographic operations.

|     #     | Description                                                                                                                                                                                          | L1  | L2  | L3  | CWE |
| :-------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-: |
| **6.8.1** | Verify that only approved hash functions are used for general cryptographic use cases, including digital signatures, HMAC, KDF, and random bit generation. Approved hash functions are listed below. |     |  ✓  |  ✓  | 916 |
| **6.8.2** | Verify that slow hashing functions are used for password storage, with appropriate parameter settings as outlined below.                                                                             |     |  ✓  |  ✓  | 916 |
| **6.8.3** | Verify that cryptographic systems avoid the use of disallowed hash functions, such as MD5, SHA-1, or any other insecure hash functions, for any cryptographic purpose.                               |  ✓  |  ✓  |  ✓  | 327 |
| **6.8.4** | Verify that hash functions used in digital signatures are collision resistant and have appropriate bit-lengths to avoid attacks, such as collision or pre-image attacks.                             |  ✓  |  ✓  |  ✓  | 916 |
| **6.8.5** | Verify that hash functions used in HMAC, KDF, and random bit generation are derived from those with proper entropy seeding for random bit generation.                                                |     |  ✓  |  ✓  | 916 |

### Approved Hash Functions for General Use Cases

The following hash functions are approved for use in general cryptographic use cases such as digital signatures, HMAC, key derivation functions (KDF), and random bit generation (RBG). These functions provide strong collision resistance and are suitable for high-security applications.

| Hash functions | Reference                                                      |
| -------------- | -------------------------------------------------------------- |
| SHA3-512       | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |
| SHA-512        | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA3-384       | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |
| SHA-384        | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA3-256       | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |
| SHA-512/256    | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA-256        | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHAKE256       | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |

### Approved Hash Functions specifically for HMAC, KDF, and Random Bit Generation (RBG)

The following hash functions are recommended for use with HMAC, KDF, and RBG operations. These hashes offer strong resistance to attacks when used with proper cryptographic key management.

| Hash functions | Reference                                                      |
| -------------- | -------------------------------------------------------------- |
| SHA3-512       | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |
| SHA3-384       | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |
| SHA3-256       | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |
| SHA-512        | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA-384        | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA-256        | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| KMAC256        | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) |
| KMAC128        | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) |
| SHAKE256       | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |

### Approved Hash Functions for Password Storage

The following hash functions are specifically recommended for secure password storage. These slow-hashing algorithms mitigate brute-force and dictionary attacks by increasing the computational difficulty of password cracking.

| Hash Function | Reference                                                                                                                      | Required Parameter Sets                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| argon2\*\*    | [RFC 9106](https://www.rfc-editor.org/info/rfc9106)                                                                            | Recommended parameter sets as listed in the internal cryptographic standard. |
| scrypt        | [RFC 7914](https://www.rfc-editor.org/info/rfc7914)                                                                            | Recommended parameter sets as listed in the internal cryptographic standard. |
| bcrypt        | --                                                                                                                             | At least 10 rounds.                                                          |
| PBKDF2_SHA512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 210,000 iterations                                                           |
| PBKDF2_SHA256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 600,000 iterations                                                           |

### Disallowed Hash Functions

The following hash functions MUST NOT be used in any cryptographic operation generating new material due to known weaknesses and vulnerabilities, they MAY only be used for verification of existing material.

| Hash functions   | Reference                                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------- |
| CRC (any length) | --                                                                                                        |
| MD4              | [RFC 1320](https://www.rfc-editor.org/info/rfc1320)                                                       |
| MD5              | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                                       |
| SHA-1            | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) |

### Disallowed Hash Functions for Digital Signatures

For digital signature implementations, the following hash functions MUST NOT be used due to insufficient collision resistance:

| Hash functions | Reference                                                      |
| -------------- | -------------------------------------------------------------- |
| SHA-224        | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA-512/224    | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA3-224       | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |

## V6.4 Random Values

Cryptographically secure Pseudo-random Number Generation (CSPRNG) is incredibly difficult to get right. Generally, good sources of entropy within a system will be quickly depleted if over-used, but sources with less randomness can lead to predictable keys and secrets.

|     #     | Description                                                                                                 | L1  | L2  | L3  | CWE |
| :-------: | :---------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-: |
| **6.3.1** | All random numbers and strings intended to be non-guessable must be generated using a CSPRNG.               |     |  ✓  |  ✓  | 338 |
| **6.3.2** | GUIDs must be created using the GUID v4 algorithm with CSPRNG.                                              |     |  ✓  |  ✓  | 338 |
| **6.3.3** | Random number generation must work properly under heavy system load, or the system must degrade gracefully. |     |     |  ✓  | 338 |

## V6.5 Secret Management

Although this section is not easily penetration tested, developers should consider this entire section as mandatory even though L1 is missing from most of the items.

|     #     | Description                                                                                                                                                      | L1  | L2  | L3  | CWE |
| :-------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-: |
| **6.4.1** | A secrets management solution, such as a key vault, must be used to securely create, store, and control access to secrets (e.g., credentials, service accounts). |     |  ✓  |  ✓  | 798 |
| **6.4.2** | Key material must not be exposed to the application and should be stored and managed within an isolated security module.                                         |     |  ✓  |  ✓  | 320 |
| **6.4.3** | Verify that cryptographic keys and secrets be managed using approved key management systems with proper auditing and access controls.                |     |  ✓  |  ✓  | 320 |
| **6.4.4** | Verify that a function exists for the secure destruction of secrets, ensuring that secrets are irrecoverable when no longer needed.                              |     |  ✓  |  ✓  | 320 |

## V6.6 Key Exchange Mechanisms

There exists a need for approved key exchange mechanisms, such as Diffie-Hellman and Elliptic Curve Diffie-Hellman (ECDH) to ensure that the cryptosystem remains secure against modern threats.

|     #     | Description                                                                                                                                                                                                                                                                                                    | L1  | L2  | L3  | CWE |
| :-------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-: |
| **6.5.1** | Verify that industry-proven cryptographic algorithms, such as Diffie-Hellman groups, with a focus on ensuring that key exchange mechanisms use secure parameters to prevent man-in-the-middle attacks or cryptographic breaks, are used for key exchanges to prevent attacks on the key establishment process. |     |  ✓  |  ✓  | 798 |

## V6.7 In-Use Data Cryptography

Protecting data while it is being processed is paramount. Techniques such as full memory encryption, encryption of data in transit, and ensuring data is encrypted as quickly as possible after use is recommended.

|     #     | Description                                                                                                                                                                    | L1  | L2  | L3  | CWE |
| :-------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-: |
| **6.6.1** | Verify that full memory encryption is in use that protects sensitive data while it is in use, preventing access by unauthorized users or processes.                            |     |  ✓  |  ✓  | 798 |
| **6.6.2** | Verify that data minimization ensures the minimal amount of data is exposed during processing, and ensure that data is encrypted immediately after use or as soon as feasible. |     |  ✓  |  ✓  | 798 |

## V6.8 Post-Quantum Cryptography (PQC)

The need to future-proof cryptographic systems in preparation for the eventual rise of quantum computing is critical. Post-Quantum Cryptography (PQC) focuses on developing cryptographic systems that are resistant to quantum attacks, which could break current encryption methods such as RSA and ECC.

|     #     | Description                                                                                                                                                                                                                                 | L1  | L2  | L3  | CWE |
| :-------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-: | :-: | :-: | :-: |
| **6.7.1** | Verify that Quantum-Safe Algorithms, or quantum-resistant algorithms, such as lattice-based, hash-based, code-based, or multivariate cryptographic schemes, as replacements for vulnerable classical algorithms like RSA and ECC, are used. |     |  ✓  |  ✓  | 798 |
| **6.7.2** | Verify that cryptographic systems are designed to allow for seamless upgrades to post-quantum cryptography, enabling the transition once PQC standards are fully established.                                                               |     |  ✓  |  ✓  | 798 |
| **6.7.3** | Regularly monitor advancements in the field of post-quantum cryptography and align with emerging industry standards to remain prepared for quantum threats.                                                                                 |     |  ✓  |  ✓  | 798 |
