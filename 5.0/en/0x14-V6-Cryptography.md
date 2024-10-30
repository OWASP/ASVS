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
| **6.1.1** | Verify that regulated data, such as private, health, and financial, is stored encrypted while at rest with at least 112-bit encryption, ideally 128-bit, such as Personally Identifiable Information (PII), sensitive personal information, or data assessed likely to be subject to the EU's GDPR. |     |  ✓  |  ✓  | 326 |
| **6.1.2** | Verify that a cryptographic inventory performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application.                                                                                                                              |     |  ✓  |  ✓  | 311 |
| **6.1.3** | Verify that cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations.                                                                                                                     |     |  ✓  |  ✓  | 311 |
| **6.1.4** | Verify that regulated health data is stored encrypted while at rest, such as medical records, medical device details, or de-anonymized research records.                                                                                                                                            |     |  ✓  |  ✓  | 311 |
| **6.1.5** | Verify that regulated financial data is stored encrypted while at rest, such as financial accounts, defaults or credit history, tax records, pay history, beneficiaries, or de-anonymized market or research records.                                                                               |     |  ✓  |  ✓  | 311 |

## V6.2 General Requirements for Cryptographic Algorithms

Recent advances in cryptography mean that previously safe algorithms and key lengths are no longer safe or sufficient to protect data. Therefore, it should be possible to change algorithms.

Although this section is not easily penetration tested, developers should consider this entire section as mandatory even though L1 is missing from most of the items.

|     #     | Description                                                                                                                                                                                                          | L1  | L2  | L3  | CWE |
| :-------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-: |
| **6.2.1** | All cryptographic primitives MUST utilize a minimum of 128-bits of security, with exceptions only made for equipment or applications approaching end of life, where the requirement is at least 112-bits of security for all cryptography. |  ✓  |  ✓  |  ✓  | 311 |
| **6.2.2** | All cryptographic modules must fail securely to prevent vulnerabilities like Padding Oracle attacks.                                                                                                                 |  ✓  |  ✓  |  ✓  | 310 |
| **6.2.3** | Verify that industry proven or government approved cryptographic algorithms, modes, and libraries are used, instead of custom coded cryptography.                                                                    |     |  ✓  |  ✓  | 327 |
| **6.2.4** | Verify that random number, encryption or hashing algorithms, key lengths, rounds, ciphers or modes, can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks.                  |     |  ✓  |  ✓  | 326 |
| **6.2.5** | Verify that all cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information.                                               |     |     |  ✓  | 385 |

### Equivalent Strenghts of Cryptographic Parameters

The relative security strengths for various cryptographic systems are in this table (from [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), p.71):

| Security Strength | Symmetric Key Algorithms | Finite Field Cryptography (DSA, DH, MQV) | Integer Factorisation Cryptography (RSA) | Elliptic Curve Cryptography (ECDSA, EdDSA, DH, MQV) |
|--|--|--|--|--|
| <= 80 | 2TDEA   | L = 1024 <br> N = 160  | k = 1024  | f = 160-223 |
| 112   | 3TDEA\*  | L = 2048 <br> N = 224  | k = 2048  | f = 224-255 |
| 128   | AES-128 | L = 3072 <br> N = 256  | k = 3072  | f = 256-383 |
| 192   | AES-192 | L = 7680 <br> N = 384  | k = 7680  | f = 384-511 |
| 256   | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

## V6.3 Cipher Algorithms

Cipher algorithms such as AES and CHACHA20 form the backbone of modern cryptographic practice.

|     #     | Description                                                                                                                                                                                                          | L1  | L2  | L3  | CWE |
| :-------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-: |
| **6.2.4** | Verify that insecure block modes (e.g., ECB) and weak padding schemes (e.g., PKCS#1 v1.5) are not used.                                                                                                              |     |  ✓  |  ✓  | 326 |
| **6.2.5** | Verify that insecure ciphers, including Triple-DES and Blowfish, are not used but secure ciphers and modes** such as AES with GCM are.                                                                                |  ✓  |  ✓  |  ✓  | 326 |
| **6.2.6** | Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key/data-element pair. The method of generation must be appropriate for the algorithm being used. |     |     |  ✓  | 326 |
| **6.2.7** | Verify that encrypted data is authenticated via signatures, authenticated cipher modes, or HMAC to ensure that ciphertext is not altered by an unauthorized party.                                                   |     |     |  ✓  | 326 |
| **6.2.8** | Verify that any authenticated signatures are operating in encrypt-then-MAC or encrypt-then-hash modes as required. party.                                                   |     |     |  ✓  | 326 |

### Approved Ciphers

Implementations MUST choose from the ciphers in this list, in order of preference:

| Symmetric Key Algorithms | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| AES-256 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) |     |  ✓  |  ✓  |
| ChaCha20-Poly1305 | [RFC 8439](https://www.rfc-editor.org/info/rfc8439) |     |  ✓  |  ✓  |
| AES-192 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) |     |  ✓  |  ✓  |
| AES-128 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) |  ✓  |  ✓  |  ✓  |

Any other cipher options MUST NOT be used.

### Disallowed Ciphers

The following is a list of _explicitly unauthorized_ ciphers. Whilst anything not on the above list must be approved with documented reasons, the following are explicitly banned and MUST NOT be used:

| Symmetric Key Algorithms |
|--|
| 2TDEA   | 
| 3TDEA (3DES)   |
| IDEA    |
| RC4     |
| Blowfish|
| ARC4    |
| DES     |

### AES Cipher Modes

Modern ciphers make use of various modes, particularly AES  for various purposes. We describe the requirements on AES Cipher Modes here.

#### Approved Cipher Modes for General Use Cases

Implementations MUST choose from the following block modes, in order of preference, EXCEPT where the function is encrypted data storage (see next subsection):

| AES Encryption Mode | Authenticated?* | Reference | L1 | L2 | L3 |
|--|--|--|--|--|--|
| GCM | Yes | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) |  ✓  |  ✓  |  ✓  |
| CCM | Yes | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) |  ✓  |  ✓  |  ✓  |
| CCM-8** | Yes | [RFC 6655](https://www.rfc-editor.org/info/rfc6655) |  ✓  |  ✓  |  ✓  |
| CBC | No | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) |  ✓  |  ✓  |  ✓  |

* All encrypted messages must be authenticated. Given this, for ANY use of CBC mode there MUST be an associated hashing function or MAC to validate the message. This MUST be applied in the 'Encrypt-Then-Hash' or 'ETH' method. If this cannot be guaranteed, then CBC MUST NOT be used.

**CCM-8 is included in regard to TLS cipher suites (see [TLS](https://github.com/santander-group-cyber-cto/CryptographyStandard/blob/main/Implementations/TLS/README.md) section). 

#### Recommendations for Approved Cipher Modes for General Use Cases

Out of the given approved block modes, implementations SHOULD use the ciphers in this list, in order of preference:

| AES Encryption Mode | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| GCM | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) |  ✓  |  ✓  |  ✓  |
| CCM | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) |  ✓  |  ✓  |  ✓  |

#### Approved Cipher Modes ONLY for Data Storage (block encryption on disk)

Implementations of disk-level block encryption MUST choose from the following list, in order of preference:

| AES Disk Encryption Mode | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| XTS | [NIST SP 800-38E](https://csrc.nist.gov/pubs/sp/800/38/e/final) |  ✓  |  ✓  |  ✓  |
| XEX | [Rogaway 2004](https://doi.org/10.1007/978-3-540-30539-2_2) |  ✓  |  ✓  |  ✓  |
| LRW | [Liskov, Rivest, and Wagner 2005](https://doi.org/10.1007/s00145-010-9073-y) |  ✓  |  ✓  |  ✓  |

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
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) |  ✓  |  ✓  |  ✓  |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) |  ✓  |  ✓  |  ✓  |

AES-192 and AES-128 MAY be used if the use case demands it, but its motivation MUST be documented in the entity's cryptography inventory. Any other method for key wrapping MUST NOT be used.

## V6.3a Hashing and Hash-based Functions

Cryptographic hashes are used in a wide variety of cryptographic protocols, such as digital signatures, HMAC, key derivation functions (KDF), random bit generation, and password storage. The security of the cryptographic system is only as strong as the underlying hash functions used. This section outlines the requirements for using secure hash functions in cryptographic operations.

|     #     | Description                                                                                                                                                                                          | L1  | L2  | L3  | CWE |
| :-------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-: |
| **6.8.1** | Verify that only approved hash functions are used for general cryptographic use cases, including digital signatures, HMAC, KDF, and random bit generation. Approved hash functions are listed below. |     |  ✓  |  ✓  | 916 |
| **6.8.2** | Verify that slow hashing functions are used for password storage, with appropriate parameter settings as outlined below.                                                                             |     |  ✓  |  ✓  | 916 |
| **6.8.3** | Verify that cryptographic systems avoid the use of disallowed hash functions, such as MD5, SHA-1, or any other insecure hash functions, for any cryptographic purpose.                               |  ✓  |  ✓  |  ✓  | 327 |
| **6.8.4** | Verify that hash functions used in digital signatures are collision resistant and have appropriate bit-lengths to avoid attacks, such as collision or pre-image attacks.                             |  ✓  |  ✓  |  ✓  | 916 |
| **6.8.5** | Verify that hash functions used in HMAC, KDF, and random bit generation are derived from those with proper entropy seeding for random bit generation.                                                |     |  ✓  |  ✓  | 916 |

### Approved Hash Functions for General Use Cases

The following hash functions are approved for use in general cryptographic use cases such as digital signatures, HMAC, key derivation functions (KDF), and random bit generation (RBG). These functions provide strong collision resistance and are suitable for high-security applications. Some of these algorithms offer strong resistance to attacks when used with proper cryptographic key management, and so are additionally approved for HMAC, KDF, and RBG functions.

| Hash functions | Suitable for<br>HMAC/KDF/RBG? |Reference                                                      | L1 | L2 | L3 |
| -------------- | ----------------------------- |-------------------------------------------------------------- |--|--|--|
| SHA3-512       | Y                             |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |     |  ✓  |  ✓  |
| SHA-512        | Y                             |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |     |  ✓  |  ✓  |
| SHA3-384       | Y                             |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |     |  ✓  |  ✓  |
| SHA-384        | Y                             |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |     |  ✓  |  ✓  |
| SHA3-256       | Y                             |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |     |  ✓  |  ✓  |
| SHA-512/256    | Y                             |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |     |  ✓  |  ✓  |
| SHA-256        | Y                             |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |  ✓  |  ✓  |  ✓  |
| KMAC256        | N                             |[NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) |  ✓  |  ✓  |  ✓  |
| KMAC128        | N                             |[NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) |  ✓  |  ✓  |  ✓  |
| SHAKE256       | Y                             |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)          |  ✓  |  ✓  |  ✓  |

### Approved Hash Functions for Password Storage

The following hash functions are specifically recommended for secure password storage. These slow-hashing algorithms mitigate brute-force and dictionary attacks by increasing the computational difficulty of password cracking.

| Hash Function | Reference                                                                                                                      | Required Parameter Sets                                                      | L1 | L2 | L3 |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | --|--|--|
| argon2    | [RFC 9106](https://www.rfc-editor.org/info/rfc9106)                                                                            | TODO |    |  ✓  |  ✓  |
| scrypt        | [RFC 7914](https://www.rfc-editor.org/info/rfc7914)                                                                            | TODO |    |  ✓  |  ✓  |
| bcrypt        | --                                                                                                                             | At least 10 rounds.                                                          |    |  ✓  |  ✓  |
| PBKDF2_SHA512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 210,000 iterations                                                           |  ✓  |  ✓  |  ✓  |
| PBKDF2_SHA256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 600,000 iterations                                                           |  ✓  |  ✓  |  ✓  |

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

### Approved RNG Methods and Algorithms

| Name | Version/Reference | Notes | L1 | L2 | L3 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| `/dev/random` | Linux 4.8+ [(Oct 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3), also found in iOS, Android, and other Linux-based POSIX operating systems. Based on [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) | Utilizing ChaCha20 stream. Found in iOS [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) and Android [`Secure Random`](https://developer.android.com/reference/java/security/SecureRandom) with the correct settings provided to each. | ✓ | ✓ | ✓ |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | As used in common implementations, such as [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) set by [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers). | ✓ | ✓ | ✓ |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) |  | ✓ | ✓ | ✓ |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) |  | ✓ | ✓ | ✓ |

### Disallowed Hashes for RBG

The following SHOULD NOT be used for RBG (according to [NIST SP-800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)):

| Hash functions | Reference |
|--|--|
| SHA3-224    | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA-224     | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| KMAC128     | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) |

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

### Approved KEX Schemes

A security strength of 112 bits or above MUST be ensured for all Key Exchange schemes, and their implementation MUST follow the parameter choices in the next table.

| Scheme | Domain Parameters |
|--|--|
| RSA | k >= 2048 |
| Diffie-Hellman (DH) | (L, N) parameters: <br>L >= 2048 & N >= 224 |
| Elliptic Curve <br>Diffie-Hellman (ECDH) | f >= 224 |

Where the following parameters are:

* k is the key size for RSA keys.
* L is the size of the public key and N is the size of the private key for finite field cryptography.
* f is the range of key sizes for ECC.

### Approved DH groups

The following groups are approved and MUST be used for implementations of Diffie-Hellman KEX. IKEv2 groups are provided for reference ([NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final)). Equivalent groups might be used in other protocols. Other groups MUST NOT be used. This list is ordered STRONGEST to WEAKEST. Security strengths are documented in [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final), Appendix D, and [NIST SP 800-57 Part 1 Rev.5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Group | Scheme | Parameters | Security bits | L1 | L2 | L3 |
|--|--|--|--|--|--|--|
| 21 | ECC | 521-bit random ECP group | 260 |    |    |  ✓  |
| 32 | ECC | Curve448 | 224 |    |    |  ✓  |
| 18 | MODP | 8192-bit MODP Group | 192 < 200 |    |  ✓  |  ✓  |
| 20 | ECC | 384-bit random ECP group | 192 |    |  ✓  |  ✓  |
| 17 | MODP | 6144-bit MODP Group | 128 < 176 |  ✓  |  ✓  |  ✓  |
| 16 | MODP | 4096-bit MODP Group | 128 < 152 |  ✓  |  ✓  |  ✓  |
| 31 | ECC | Curve25519 | 128 |  ✓  |  ✓  |  ✓  |
| 19 | ECC | 256-bit random ECP group | 128 |  ✓  |  ✓  |  ✓  |
| 15 | MODP | 3072-bit MODP Group | 128 |  ✓  |  ✓  |  ✓  |
| 14 | MODP | 2048-bit MODP Group | 112 |  ✓  |  ✓  |  ✓  |

A complete list of IKE Groups is available by [IANA](https://www.iana.org/assignments/ikev2-parameters/ikev2-parameters.xhtml) under "Transform Type 4 - Key Exchange Method Transform IDs". Further recommendations on IKE specifically can be found on the [IPSec](https://github.com/santander-group-cyber-cto/CryptographyStandard/blob/main/Implementations/IPSec/README.md) section.

### Disallowed KEX Schemes

Any new implementation MUST NOT use any scheme that is NOT compliant with [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) & [B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) and [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final).

Specifically, IKEv1 MUST NOT be used in production.

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
