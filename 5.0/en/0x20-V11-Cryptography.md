# V11 Cryptography

## Control Objective

The objective of V6 is to define best practices for the general use of cryptography but also to instill a fundamental understanding of cryptographic principles and inspire a shift toward more resilient and modern approaches. It encourages doing the following:

* Implementing robust cryptographic systems that fail securely, adapt to evolving threats, and are future-proof.
* Utilizing cryptographic mechanisms that are both secure and aligned with industry best practices.
* Maintaining a secure cryptographic key management system with appropriate access controls and auditing.
* Regularly evaluating the cryptographic landscape to assess new risks and adapt algorithms accordingly.
* Discovering and managing cryptographic use cases throughout the application's lifecycle to ensure that all cryptographic assets are accounted for and secured.

In addition to outlining general principles and best practices, this document also provides more in-depth technical information about the requirements in [Appendix V](./0x97-Appendix-V_Cryptography.md).

Requirements which use cryptography to solve a separate problem, such as secrets management or communications security, will be in different parts of the standard.

## V11.1 Cryptographic Inventory and Documentation

Applications need to be designed with strong cryptographic architecture to protect data assets as per their classification. Encrypting everything is wasteful, not encrypting anything is legally negligent. A balance must be struck, usually during architectural or high-level design, design sprints or architectural spikes. Designing cryptography as you go or retrofitting it will inevitably cost much more to implement securely than simply building it in from the start.

Architectural requirements are intrinsic to the entire code base, and thus difficult to unit or integration test. Architectural requirements require consideration in coding standards, throughout the coding phase, and should be reviewed during security architecture, peer or code reviews, or retrospectives.

It is also important to ensure that all cryptographic assets, such as algorithms, keys, and certificates, are regularly discovered, inventoried, and assessed. For Level 3, this should include the use of static and dynamic scanning to discover the use of cryptography in an application. Tools such as SAST and DAST may help with this but it is possible that dedicated tools would be needed to get more comprehensive coverage. Freeware examples of tools include:

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.1.1** | Verify that there is an explicit policy for management of cryptographic keys and that a cryptographic key lifecycle follows a key management standard such as NIST SP 800-57. | 2 | v5.0.be-1.6.1 |
| **11.1.2** | [MODIFIED] Verify that a cryptographic inventory is performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application. It should also document where keys can and cannot be used in the system and also the types of data which can and cannot be protected using the keys. | 2 | v5.0.be-1.6.4 |
| **11.1.3** | [ADDED] Verify that cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations. | 3 | v5.0.be-1.6.5 |

## V11.2 Secure Cryptography Implementation

This section defines the requirements for the selection, implementation, and ongoing management of core cryptographic algorithms for an application. The objective is to ensure that only robust, industry-accepted cryptographic primitives are deployed, in alignment with current standards (e.g., NIST, ISO/IEC) and best practices. Organizations must ensure that each cryptographic component is selected based on peer-reviewed evidence and practical security testing.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.2.1** | [MODIFIED, SPLIT TO 6.5.1, 6.5.2, 6.5.4, 6.6.1, 6.7.2] Verify that industry-validated implementations (including libraries and hardware-accelerated implementations) are used for cryptographic operations. | 2 | v5.0.be-6.2.2 |
| **11.2.2** | [MODIFIED, MERGED FROM 1.6.3] Verify that the application is designed with crypto agility such that random number, authenticated encryption, MAC, or hashing algorithms, key lengths, rounds, ciphers or modes can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks. Similarly, it must also be possible to replace keys and passwords and re-encrypt data. This should allow for seamless upgrades to post-quantum cryptography (PQC), once high-assurance implementations of approved PQC schemes or standards are widely available. | 2 | v5.0.be-6.2.4 |
| **11.2.3** | [ADDED] Verify that all cryptographic primitives utilize a minimum of 128-bits of security based on the algorithm, key size, and configuration. For example, a 256-bit ECC key provides roughly 128 bits of security where RSA requires a 3072-bit key to achieve 128 bits of security. | 2 | v5.0.be-6.2.9 |
| **11.2.4** | Verify that all cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information. | 3 | v5.0.be-6.2.8 |
| **11.2.5** | [MODIFIED] Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable vulnerabilities, such as Padding Oracle attacks. | 3 | v5.0.be-6.2.1 |

## V11.3 Encryption Algorithms

Authenticated encryption algorithms built on AES and CHACHA20 form the backbone of modern cryptographic practice.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.3.1** | [ADDED, SPLIT FROM 6.2.2, 6.2.5, COVERS 6.2.3] Verify that insecure block modes (e.g., ECB) and weak padding schemes (e.g., PKCS#1 v1.5) are not used. | 1 | v5.0.be-6.5.1 |
| **11.3.2** | [ADDED, SPLIT FROM 6.2.2, 6.2.5, COVERS 6.2.3, LEVEL L2 > L1] Verify that only secure, authenticated ciphers and modes such as AES with GCM are used. | 1 | v5.0.be-6.5.2 |
| **11.3.3** | [MODIFIED, SPLIT FROM 6.2.2, MOVED FROM 6.2.7] Verify that encrypted data is protected against unauthorized modification preferably by using an approved authenticated encryption method or by combining an approved encryption method with an approved MAC algorithm. | 2 | v5.0.be-6.5.4 |
| **11.3.4** | [MODIFIED, MOVED FROM 6.2.6, LEVEL L2 > L3] Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key and data-element pair. The method of generation must be appropriate for the algorithm being used. | 3 | v5.0.be-6.5.3 |
| **11.3.5** | [ADDED] Verify that any combination of an encryption algorithm and a MAC algorithm is operating in encrypt-then-MAC mode. | 3 | v5.0.be-6.5.5 |

## V11.4 Hashing and Hash-based Functions

Cryptographic hashes are used in a wide variety of cryptographic protocols, such as digital signatures, HMAC, key derivation functions (KDF), random bit generation, and password storage. The security of the cryptographic system is only as strong as the underlying hash functions used. This section outlines the requirements for using secure hash functions in cryptographic operations.

For password storage, as well as the cryptography appendix, the [OWASP Password Storage Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms) will also provide useful context and guidance.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.4.1** | [ADDED, SPLIT FROM 6.2.2, 6.2.5, COVERS 6.2.3] Verify that only approved hash functions are used for general cryptographic use cases, including digital signatures, HMAC, KDF, and random bit generation. Disallowed hash functions, such as MD5, must not be used for any cryptographic purpose. | 1 | v5.0.be-6.6.1 |
| **11.4.2** | [MODIFIED, MOVED FROM 2.4.1, MERGED FROM 2.4.3, 2.4.4, COVERS 2.5.3] Verify that passwords are stored using an approved, computationally intensive, hashing algorithm with parameter settings configured based on current guidance. The settings should balance security and performance to make brute-force attacks more challenging. | 2 | v5.0.be-6.6.2 |
| **11.4.3** | [ADDED] Verify that hash functions used in digital signatures, as part of data authentication or data integrity are collision resistant and have appropriate bit-lengths. If collision resistance is required, the output length must be at least 256 bits. If only resistance to second pre-image attacks is required, the output length must be at least 128 bits. | 2 | v5.0.be-6.6.3 |

## V11.5 Random Values

Cryptographically secure Pseudo-random Number Generation (CSPRNG) is incredibly difficult to get right. Generally, good sources of entropy within a system will be quickly depleted if over-used, but sources with less randomness can lead to predictable keys and secrets.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.5.1** | [GRAMMAR, COVERS 6.3.2, LEVEL L2 > L1] Verify that all random numbers and strings which are intended to be non-guessable must be generated using a cryptographically-secure pseudo-random number generator (CSPRNG) and have at least 128 bits of entropy. Note that UUIDs do not respect this condition. | 2 | v5.0.be-6.3.1 |
| **11.5.2** | [GRAMMAR, LEVEL L3 > L1] Verify that random number generation continues to work securely, even under heavy system load, or that the system degrades gracefully. | 3 | v5.0.be-6.3.3 |

## V11.6 Public Key Cryptography

Public Key Cryptography will be used where it is not possible or not desirable to share a secret key between multiple parties.

As part of this, there exists a need for approved key exchange mechanisms, such as Diffie-Hellman and Elliptic Curve Diffie-Hellman (ECDH) to ensure that the cryptosystem remains secure against modern threats.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.6.1** | [MODIFIED, MOVED FROM 2.9.3, SPLIT FROM 6.2.2] Verify that only approved cryptographic algorithms and modes of operation are used for key generation and seeding, and digital signature generation and verification. | 2 | v5.0.be-6.7.2 |
| **11.6.2** | [ADDED] Verify that industry-proven cryptographic algorithms are used for key exchange (such as Diffie-Hellman) with a focus on ensuring that key exchange mechanisms use secure parameters. This should prevent attacks on the key establishment process which could lead to adversary-in-the-middle attacks or cryptographic breaks. | 3 | v5.0.be-6.7.1 |

## V11.7 In-Use Data Cryptography

Protecting data while it is being processed is paramount. Techniques such as full memory encryption, encryption of data in transit, and ensuring data is encrypted as quickly as possible after use is recommended.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.7.1** | [ADDED] Verify that full memory encryption is in use that protects sensitive data while it is in use, preventing access by unauthorized users or processes. | 3 | v5.0.be-6.8.1 |
| **11.7.2** | [ADDED] Verify that data minimization ensures the minimal amount of data is exposed during processing, and ensure that data is encrypted immediately after use or as soon as feasible. | 3 | v5.0.be-6.8.2 |

## V11.8 Post-Quantum Cryptography (PQC)

The need to future-proof cryptographic systems in preparation for the eventual rise of quantum computing is critical. Post-Quantum Cryptography (PQC) focuses on developing cryptographic systems that are resistant to quantum attacks, which could break current encryption methods such as RSA and ECC. Please see the Appendix for the latest information on available PQC primitives.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.8.1** | [ADDED] Verify that a cryptographic inventory is maintained and includes a documented transformation plan or mapping that outlines the migration path from current cryptographic algorithms and systems to those that use post-quantum cryptography. | 3 | v5.0.be-6.9.1 |
| **11.8.2** | [ADDED] Verify that advancements in the field of post-quantum cryptography are being monitored in order to ensure that the application is aligned with emerging industry standards, and remains prepared for quantum threats. | 3 | v5.0.be-6.9.2 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Testing for Weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/README.html)
* [OWASP Cheat Sheet: Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
