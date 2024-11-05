# V6 Stored Cryptography

## Control Objective

The objective of V6 is not only to define best practices but also to instill a fundamental understanding of cryptographic principles and inspire a shift toward more resilient and modern approaches by doing the following:

- Implementing robust cryptographic systems that fail securely, adapt to evolving threats, and are future-proof.
- Utilizing cryptographic mechanisms that are both secure and aligned with industry best practices.
- Maintaining a secure cryptographic key management system with appropriate access controls and auditing.
- Regularly evaluating the cryptographic landscape to assess new risks and adapt algorithms accordingly.
- Discovering and managing cryptographic use cases throughout the application's lifecycle to ensure that all cryptographic assets are accounted for and secured.

## V6.1 Data Classification

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **6.1.1** | [DELETED, MERGED TO 1.8.1] | | | | |
| **6.1.2** | [DELETED, MERGED TO 1.8.1] | | | | |
| **6.1.3** | [DELETED, DUPLICATE OF 1.8.1] | | | | |

## V6.2 Algorithms

Recent advances in cryptography mean that previously safe algorithms and key lengths are no longer safe or sufficient to protect data. Therefore, it should be possible to change algorithms.

Although this section is not easily penetration tested, developers should consider this entire section as mandatory even though L1 is missing from most of the items.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **6.2.1** | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable Padding Oracle attacks. | ✓ | ✓ | ✓ | 310 |
| **6.2.2** | Verify that industry proven or government approved cryptographic algorithms, modes, and libraries are used, instead of custom coded cryptography. | | ✓ | ✓ | 327 |
| **6.2.3** | [DELETED, DUPLICATE OF 6.2.5] | | | | |
| **6.2.4** | Verify that random number, encryption or hashing algorithms, key lengths, rounds, ciphers or modes, can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks. | | ✓ | ✓ | 326 |
| **6.2.5** | [MODIFIED] Verify that known insecure block modes (i.e. ECB, etc.), padding modes (i.e. PKCS#1 v1.5, etc.), ciphers with small block sizes (i.e. Triple-DES, Blowfish, etc.), and weak hashing algorithms (i.e. MD5, SHA1, etc.) are not used. | | ✓ | ✓ | 326 |
| **6.2.6** | [MODIFIED, LEVEL L2 > L3] Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key/data-element pair. The method of generation must be appropriate for the algorithm being used. | | | ✓ | 326 |
| **6.2.7** | Verify that encrypted data is authenticated via signatures, authenticated cipher modes, or HMAC to ensure that ciphertext is not altered by an unauthorized party. | | | ✓ | 326 |
| **6.2.8** | Verify that all cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information. | | | ✓ | 385 |
| **6.2.9** | [ADDED] All cryptographic primitives MUST utilize a minimum of 128-bits of security, with exceptions only made for equipment or applications approaching end of life, where the requirement is at least 112-bits of security for all cryptography. | ✓ | ✓ | ✓ | 311 |

### Equivalent Strenghts of Cryptographic Parameters

The relative security strengths for various cryptographic systems are in this table (from [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), p.71):

| Security Strength | Symmetric Key Algorithms | Finite Field Cryptography (DSA, DH, MQV) | Integer Factorisation Cryptography (RSA) | Elliptic Curve Cryptography (ECDSA, EdDSA, DH, MQV) |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA\* | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

## V6.3 Random Values

Cryptographically secure Pseudo-random Number Generation (CSPRNG) is incredibly difficult to get right. Generally, good sources of entropy within a system will be quickly depleted if over-used, but sources with less randomness can lead to predictable keys and secrets.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **6.3.1** | [MODIFIED] Verify that all random numbers, random file names, and random strings are generated using a cryptographically-secure pseudo-random number generator (CSPRNG) when these random values are intended to be not guessable by an attacker. | | ✓ | ✓ | 338 |
| **6.3.2** | [MODIFIED] Verify that GUIDs are created with an implementation of the GUID v4 algorithm which utilizes a cryptographically-secure pseudo-random number generator (CSPRNG). GUIDs created using other algorithm versions or using insufficiently secure pseudo-random number generators may be predictable. | | ✓ | ✓ | 338 |
| **6.3.3** | Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances. | | | ✓ | 338 |

## V6.4 Secret Management

Although this section is not easily penetration tested, developers should consider this entire section as mandatory even though L1 is missing from most of the items.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **6.4.1** | [MODIFIED, MERGED FROM 2.10.4] Verify that a secrets management solution such as a key vault is used to securely create, store, control access to, and destroy back-end secrets, such as passwords, integrations with databases and third-party systems, seeds and internal secrets, and API keys. Secrets must not be included in source code or be received as CI/CD variables. For a L3 application, this should involved a hardware-backed solution such as an HSM. | | ✓ | ✓ | 798 |
| **6.4.2** | [MODIFIED] Verify that key material is not exposed to the application (neither the front-end nor the back-end) but instead uses an isolated security module like a vault for cryptographic operations. | | ✓ | ✓ | 320 |

## V6.6 Cipher Algorithms

Cipher algorithms such as AES and CHACHA20 form the backbone of modern cryptographic practice.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **6.2.4** | [ADDED] Verify that insecure block modes (e.g., ECB) and weak padding schemes (e.g., PKCS#1 v1.5) are not used. | | ✓ | ✓ | 326 |
| **6.2.5** | [ADDED] Verify that insecure ciphers, including Triple-DES and Blowfish, are not used but secure ciphers and modes** such as AES with GCM are. | ✓ | ✓ | ✓ | 326 |
| **6.2.6** | [ADDED] Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key/data-element pair. The method of generation must be appropriate for the algorithm being used. | | | ✓ | 326 |
| **6.2.7** | [ADDED] Verify that encrypted data is authenticated via signatures, authenticated cipher modes, or HMAC to ensure that ciphertext is not altered by an unauthorized party. | | | ✓ | 326 |
| **6.2.8** | [ADDED] Verify that any authenticated signatures are operating in encrypt-then-MAC or encrypt-then-hash modes as required. party. | | | ✓ | 326 |

### Approved Ciphers

Implementations MUST choose from the ciphers in this list, in order of preference:

| Symmetric Key Algorithms | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| AES-256 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | | ✓ | ✓ |
| ChaCha20-Poly1305 | [RFC 8439](https://www.rfc-editor.org/info/rfc8439) | | ✓ | ✓ |
| AES-192 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | | ✓ | ✓ |
| AES-128 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | ✓ | ✓ | ✓ |

Any other cipher options MUST NOT be used.

### Disallowed Ciphers

The following is a list of _explicitly unauthorized_ ciphers. Whilst anything not on the above list must be approved with documented reasons, the following are explicitly banned and MUST NOT be used:

| Symmetric Key Algorithms |
|--|
| 2TDEA |
| 3TDEA (3DES) |
| IDEA |
| RC4 |
| Blowfish|
| ARC4 |
| DES |

### AES Cipher Modes

Modern ciphers make use of various modes, particularly AES for various purposes. We describe the requirements on AES Cipher Modes here.

#### Approved Cipher Modes for General Use Cases

Implementations MUST choose from the following block modes, in order of preference, EXCEPT where the function is encrypted data storage (see next subsection):

| AES Encryption Mode | Authenticated?* | Reference | L1 | L2 | L3 |
|--|--|--|--|--|--|
| GCM | Yes | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | ✓ | ✓ | ✓ |
| CCM | Yes | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | ✓ | ✓ | ✓ |
| CCM-8** | Yes | [RFC 6655](https://www.rfc-editor.org/info/rfc6655) | ✓ | ✓ | ✓ |
| CBC | No | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | ✓ | ✓ | ✓ |

* All encrypted messages must be authenticated. Given this, for ANY use of CBC mode there MUST be an associated hashing function or MAC to validate the message. This MUST be applied in the 'Encrypt-Then-Hash' or 'ETH' method. If this cannot be guaranteed, then CBC MUST NOT be used.

\*\*CCM-8 is included in regard to TLS cipher suites (see [TLS](https://github.com/santander-group-cyber-cto/CryptographyStandard/blob/main/Implementations/TLS/README.md) section).

#### Recommendations for Approved Cipher Modes for General Use Cases

Out of the given approved block modes, implementations SHOULD use the ciphers in this list, in order of preference:

| AES Encryption Mode | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| GCM | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | ✓ | ✓ | ✓ |
| CCM | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | ✓ | ✓ | ✓ |

#### Approved Cipher Modes ONLY for Data Storage (block encryption on disk)

Implementations of disk-level block encryption MUST choose from the following list, in order of preference:

| AES Disk Encryption Mode | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| XTS | [NIST SP 800-38E](https://csrc.nist.gov/pubs/sp/800/38/e/final) | ✓ | ✓ | ✓ |
| XEX | [Rogaway 2004](https://doi.org/10.1007/978-3-540-30539-2_2) | ✓ | ✓ | ✓ |
| LRW | [Liskov, Rivest, and Wagner 2005](https://doi.org/10.1007/s00145-010-9073-y) | ✓ | ✓ | ✓ |

#### Disallowed Cipher Modes

The following cipher modes MUST NOT be used for any use case:

| Encryption Mode |
|--|
| ECB |
| CFB |
| OFB |
| CTR |

### Key Wrapping

ONLY AES-256 MUST be used for key wrapping, following [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) and considering forward-looking provisions against the quantum threat. Cipher modes using AES are the following, in order of preference:

| Key Wrapping | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | ✓ | ✓ | ✓ |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | ✓ | ✓ | ✓ |

AES-192 and AES-128 MAY be used if the use case demands it, but its motivation MUST be documented in the entity's cryptography inventory. Any other method for key wrapping MUST NOT be used.


## References

For more information, see also:

* [OWASP Testing Guide 4.0: Testing for Weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/README.html)
* [OWASP Cheat Sheet: Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
