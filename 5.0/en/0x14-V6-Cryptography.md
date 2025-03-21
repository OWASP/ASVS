# V6 Cryptography

## Control Objective

The objective of V6 is to define best practices for the general use of cryptography but also to instill a fundamental understanding of cryptographic principles and inspire a shift toward more resilient and modern approaches. It encourages doing the following:

* Implementing robust cryptographic systems that fail securely, adapt to evolving threats, and are future-proof.
* Utilizing cryptographic mechanisms that are both secure and aligned with industry best practices.
* Maintaining a secure cryptographic key management system with appropriate access controls and auditing.
* Regularly evaluating the cryptographic landscape to assess new risks and adapt algorithms accordingly.
* Discovering and managing cryptographic use cases throughout the application's lifecycle to ensure that all cryptographic assets are accounted for and secured.

In addition to outlining general principles and best practices, this document also provides more in-depth technical information about the requirements in [Appendix V](./0x97-Appendix-V_Cryptography.md).

Requirements which use cryptography to solve a separate problem, such as secrets management or communications security, will be in different parts of the standard.

## V1.6 Cryptographic Inventory and Documentation

Applications need to be designed with strong cryptographic architecture to protect data assets as per their classification. Encrypting everything is wasteful, not encrypting anything is legally negligent. A balance must be struck, usually during architectural or high-level design, design sprints or architectural spikes. Designing cryptography as you go or retrofitting it will inevitably cost much more to implement securely than simply building it in from the start.

Architectural requirements are intrinsic to the entire code base, and thus difficult to unit or integration test. Architectural requirements require consideration in coding standards, throughout the coding phase, and should be reviewed during security architecture, peer or code reviews, or retrospectives.

It is also important to ensure that all cryptographic assets, such as algorithms, keys, and certificates, are regularly discovered, inventoried, and assessed. For Level 3, this should include the use of static and dynamic scanning to discover the use of cryptography in an application. Tools such as SAST and DAST may help with this but it is possible that dedicated tools would be needed to get more comprehensive coverage. Freeware examples of tools include:

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **1.6.1** | Verify that there is an explicit policy for management of cryptographic keys and that a cryptographic key lifecycle follows a key management standard such as NIST SP 800-57. | 2 | 320 |
| **1.6.2** | [DELETED, MERGED TO 14.8.1] | | |
| **1.6.3** | [DELETED, MERGED TO 6.2.4] | | |
| **1.6.4** | [MODIFIED] Verify that a cryptographic inventory is performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application. It should also document where keys can and cannot be used in the system and also the types of data which can and cannot be protected using the keys. | 2 | 320 |
| **1.6.5** | [ADDED] Verify that cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations. | 3 | 320 |

## V6.1 Data Classification

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **6.1.1** | [DELETED, MERGED TO 1.8.1] | | |
| **6.1.2** | [DELETED, MERGED TO 1.8.1] | | |
| **6.1.3** | [DELETED, COVERED BY 1.8.1] | | |

## V6.2 Algorithms

Recent advances in cryptography mean that previously safe algorithms and key lengths are no longer safe or sufficient to protect data. Therefore, it should be possible to change algorithms.

Although this section is not easily penetration tested, developers should consider this entire section as mandatory even though L1 is missing from most of the items.

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **6.2.1** | [MODIFIED] Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable vulnerabilities, such as Padding Oracle attacks. | 1 | 310 |
| **6.2.2** | [MODIFIED, SPLIT TO 6.5.1, 6.5.2, 6.5.4, 6.6.1, 6.7.2] Verify that industry-validated implementations (including libraries and hardware-accelerated implementations) are used for cryptographic operations. | 2 | 327 |
| **6.2.3** | [DELETED, COVERED BY 6.5.1, 6.5.2, 6.6.1] | | |
| **6.2.4** | [MODIFIED, MERGED FROM 1.6.3] Verify that the application is designed with crypto agility such that random number, authenticated encryption, MAC, or hashing algorithms, key lengths, rounds, ciphers or modes can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks. Similarly, it must also be possible to replace keys and passwords and re-encrypt data. This should allow for seamless upgrades to post-quantum cryptography (PQC), once high-assurance implementations of approved PQC schemes or standards are widely available. | 2 | 320 |
| **6.2.5** | [SPLIT TO 6.5.1, 6.5.2, 6.6.1] | | |
| **6.2.6** | [MOVED TO 6.5.3] | | |
| **6.2.7** | [MOVED TO 6.5.4] | | |
| **6.2.8** | Verify that all cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information. | 3 | 385 |
| **6.2.9** | [ADDED] Verify that all cryptographic primitives utilize a minimum of 128-bits of security based on the algorithm, key size, and configuration. For example, a 256-bit ECC key provides roughly 128 bits of security where RSA requires a 3072-bit key to achieve 128 bits of security. | 1 | 311 |

## V6.3 Random Values

Cryptographically secure Pseudo-random Number Generation (CSPRNG) is incredibly difficult to get right. Generally, good sources of entropy within a system will be quickly depleted if over-used, but sources with less randomness can lead to predictable keys and secrets.

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **6.3.1** | [GRAMMAR, COVERS 6.3.2, LEVEL L2 > L1] Verify that all random numbers and strings which are intended to be non-guessable must be generated using a cryptographically-secure pseudo-random number generator (CSPRNG) and have at least 128 bits of entropy. Note that UUIDs do not respect this condition. | 1 | 338 |
| **6.3.2** | [DELETED, COVERED BY 6.3.1] | | |
| **6.3.3** | [GRAMMAR, LEVEL L3 > L1] Verify that random number generation continues to work securely, even under heavy system load, or that the system degrades gracefully. | 1 | 338 |

## V6.4 Secret Management

Although this section is not easily penetration tested, developers should consider this entire section as mandatory even though L1 is missing from most of the items.

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **6.4.1** | [MOVED TO 14.8.1] | | |
| **6.4.2** | [MOVED TO 14.8.2] | | |

## V6.5 Encryption Algorithms

Authenticated encryption algorithms built on AES and CHACHA20 form the backbone of modern cryptographic practice.

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **6.5.1** | [ADDED, SPLIT FROM 6.2.2, 6.2.5, COVERS 6.2.3] Verify that insecure block modes (e.g., ECB) and weak padding schemes (e.g., PKCS#1 v1.5) are not used. | 2 | 326 |
| **6.5.2** | [ADDED, SPLIT FROM 6.2.2, 6.2.5, COVERS 6.2.3, LEVEL L2 > L1] Verify that only secure, authenticated ciphers and modes such as AES with GCM are used. | 1 | 326 |
| **6.5.3** | [MODIFIED, MOVED FROM 6.2.6, LEVEL L2 > L3] Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key and data-element pair. The method of generation must be appropriate for the algorithm being used. | 3 | 326 |
| **6.5.4** | [MODIFIED, SPLIT FROM 6.2.2, MOVED FROM 6.2.7] Verify that encrypted data is protected against unauthorized modification preferably by using an approved authenticated encryption method or by combining an approved encryption method with an approved MAC algorithm. | 3 | 326 |
| **6.5.5** | [ADDED] Verify that any combination of an encryption algorithm and a MAC algorithm is operating in encrypt-then-MAC mode. | 3 | 326 |

## V6.6 Hashing and Hash-based Functions

Cryptographic hashes are used in a wide variety of cryptographic protocols, such as digital signatures, HMAC, key derivation functions (KDF), random bit generation, and password storage. The security of the cryptographic system is only as strong as the underlying hash functions used. This section outlines the requirements for using secure hash functions in cryptographic operations.

For password stroage, as well as the cryptography appendix, the [OWASP Password Storage Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms) will also provide useful context and guidance.

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **6.6.1** | [ADDED, SPLIT FROM 6.2.2, 6.2.5, COVERS 6.2.3] Verify that only approved hash functions are used for general cryptographic use cases, including digital signatures, HMAC, KDF, and random bit generation. Disallowed hash functions, such as MD5, must not be used for any cryptographic purpose. | 2 | |
| **6.6.2** | [MODIFIED, MOVED FROM 2.4.1, MERGED FROM 2.4.3, 2.4.4, COVERS 2.5.3] Verify that passwords are stored using an approved, computationally intensive, hashing algorithm with parameter settings configured based on current guidance. The settings should balance security and performance to make brute-force attacks more challenging. | 2 | |
| **6.6.3** | [ADDED] Verify that hash functions used in digital signatures, as part of data authentication or data integrity are collision resistant and have appropriate bit-lengths. If collision resistance is required, the output length must be at least 256 bits. If only resistance to second pre-image attacks is required, the output length must be at least 128 bits. | 1 | |

## V6.7 Public Key Cryptography

Public Key Cryptography will be used where it is not possible or not desirable to share a secret key between multiple parties.

As part of this, there exists a need for approved key exchange mechanisms, such as Diffie-Hellman and Elliptic Curve Diffie-Hellman (ECDH) to ensure that the cryptosystem remains secure against modern threats.

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **6.7.1** | [ADDED] Verify that industry-proven cryptographic algorithms are used for key exchange (such as Diffie-Hellman) with a focus on ensuring that key exchange mechanisms use secure parameters. This should prevent attacks on the key establishment process which could lead to adversary-in-the-middle attacks or cryptographic breaks. | 2 | |
| **6.7.2** | [MODIFIED, MOVED FROM 2.9.3, SPLIT FROM 6.2.2] Verify that only approved cryptographic algorithms and modes of operation are used for key generation and seeding, and digital signature generation and verification. | 2 | 327 |

## V6.8 In-Use Data Cryptography

Protecting data while it is being processed is paramount. Techniques such as full memory encryption, encryption of data in transit, and ensuring data is encrypted as quickly as possible after use is recommended.

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **6.8.1** | [ADDED] Verify that full memory encryption is in use that protects sensitive data while it is in use, preventing access by unauthorized users or processes. | 3 | |
| **6.8.2** | [ADDED] Verify that data minimization ensures the minimal amount of data is exposed during processing, and ensure that data is encrypted immediately after use or as soon as feasible. | 2 | |

## V6.9 Post-Quantum Cryptography (PQC)

The need to future-proof cryptographic systems in preparation for the eventual rise of quantum computing is critical. Post-Quantum Cryptography (PQC) focuses on developing cryptographic systems that are resistant to quantum attacks, which could break current encryption methods such as RSA and ECC. Please see the Appendix for the latest information on available PQC primitives.

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **6.9.1** | [ADDED] Verify that a cryptographic inventory is maintained and includes a documented transformation plan or mapping that outlines the migration path from current cryptographic algorithms and systems to those that use post-quantum cryptography. | 2 | |
| **6.9.2** | [ADDED] Verify that advancements in the field of post-quantum cryptography are being monitored in order to ensure that the application is aligned with emerging industry standards, and remains prepared for quantum threats. | 2 | |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Testing for Weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/README.html)
* [OWASP Cheat Sheet: Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
