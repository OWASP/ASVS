# Appendix V: Cryptography

V6 goes beyond simply defining best practices. It aims to enhance understanding of cryptography principles and encourage the adoption of more resilient, modern security methods. This appendix provides detailed technical information regarding each requirement, complementing the overarching standards outlined in V6

## Algorithms (V6.2)

### Equivalent Strenghts of Cryptographic Parameters

The relative security strengths for various cryptographic systems are in this table (from [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), p.71):

| Security Strength | Symmetric Key Algorithms | Finite Field Cryptography (DSA, DH, MQV) | Integer Factorisation Cryptography (RSA) | Elliptic Curve Cryptography (ECDSA, EdDSA, DH, MQV) |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA\* | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

## Random Values (V6.3)

### Approved RNG Methods and Algorithms

| Name | Version/Reference | Notes | L1 | L2 | L3 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| `/dev/random` | Linux 4.8+ [(Oct 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3), also found in iOS, Android, and other Linux-based POSIX operating systems. Based on [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) | Utilizing ChaCha20 stream. Found in iOS [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) and Android [`Secure Random`](https://developer.android.com/reference/java/security/SecureRandom) with the correct settings provided to each. | ✓ | ✓ | ✓ |
| `/dev/urandom` | Linux kernel's special file for providing random data | Provides high-quality, entropy sources from hardware randomness | ✓ | ✓ | ✓ |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | As used in common implementations, such as [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) set by [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers). | ✓ | ✓ | ✓ |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | ✓ | ✓ | ✓ |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | ✓ | ✓ | ✓ |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2), available in [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) and [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) | Provides secure random bytes directly from the kernel's entropy source with a straightforward and minimal API. It’s more modern and avoids pitfalls associated with older APIs. | ✓ | ✓ | ✓ |

### Disallowed Hashes for RBG

The following SHOULD NOT be used for RBG (according to [NIST SP-800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)):

| Hash functions | Reference |
|--|--|
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| KMAC128 | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) |

## Cipher Algorithms (V6.5)

### Approved Ciphers

The following ciphers are approved and listed in order of preference:

| Symmetric Key Algorithms | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| AES-256 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | | ✓ | ✓ |
| ChaCha20 | [RFC 8439](https://www.rfc-editor.org/info/rfc8439) | | ✓ | ✓ |
| AES-192 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | | ✓ | ✓ |
| AES-128 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | ✓ | ✓ | ✓ |

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

The following modes are approved except where the function is encrypted data storage (see next subsection)
and are listed in order of preference:

| AES Encryption Mode | Authenticated?* | Reference | L1 | L2 | L3 |
|--|--|--|--|--|--|
| GCM | Yes | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | ✓ | ✓ | ✓ |
| CCM | Yes | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | ✓ | ✓ | ✓ |
| CCM-8** | Yes | [RFC 6655](https://www.rfc-editor.org/info/rfc6655) | ✓ | ✓ | ✓ |
| CBC | No | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | ✓ | ✓ | ✓ |

* All encrypted messages must be authenticated. Given this, for ANY use of CBC mode there MUST be an associated hashing function or MAC to validate the message. This MUST be applied in the 'Encrypt-Then-Hash' or 'ETH' method. If this cannot be guaranteed, then CBC MUST NOT be used.

#### Recommendations for Approved Cipher Modes for General Use Cases

Out of the given approved block modes, implementations SHOULD use the ciphers in this list, in order of preference:

| AES Encryption Mode | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| GCM | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | ✓ | ✓ | ✓ |
| CCM | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | ✓ | ✓ | ✓ |

#### Approved Cipher Modes ONLY for Data Storage (block encryption on disk)

The following disk-level block encryption modes are approved and are listed in order of preference:

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

Cryptographic key wrap (and corresponding key unwrap) is a method of protecting an existing key by encapsulating (i.e. wrapping) it by employing an additional encryption mechanism so that the original key is not obviously exposed, e.g. during a transfer. This additional key used to protect the original key is referred to as the the wrap key.

This operation may be performed when it is desirable to protect keys in places deemed untrustworthy, or to send sensitive keys over untrusted networks or within applications.
However, serious consideration should be given to understanding the nature (e.g. the identity and the purpose) of the original key prior to committing to a wrap/unwrap procedure as this may have repercussions for both source and target systems/applications in terms of security and especially compliance which may include audit trails of a key's function (e.g. signing) as well as appropriate key storage.

ONLY AES-256 MUST be used for key wrapping, following [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) and considering forward-looking provisions against the quantum threat. Cipher modes using AES are the following, in order of preference:

| Key Wrapping | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | ✓ | ✓ | ✓ |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | ✓ | ✓ | ✓ |

AES-192 and AES-128 MAY be used if the use case demands it, but its motivation MUST be documented in the entity's cryptography inventory.

## Hashing and Hash-based Functions (V6.6)

### Approved Hash Functions for General Use Cases

The following hash functions are approved for use in general cryptographic use cases such as digital signatures, HMAC, key derivation functions (KDF), and random bit generation (RBG). These functions provide strong collision resistance and are suitable for high-security applications. Some of these algorithms offer strong resistance to attacks when used with proper cryptographic key management, and so are additionally approved for HMAC, KDF, and RBG functions.

| Hash functions | Suitable for HMAC/KDF/RBG? | Reference | L1 | L2 | L3 |
| -------------- | ----------------------------- |-------------------------------------------------------------- |--|--|--|
| SHA3-512 | Y |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | | ✓ | ✓ |
| SHA-512 | Y |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | | ✓ | ✓ |
| SHA3-384 | Y |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | | ✓ | ✓ |
| SHA-384 | Y |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | | ✓ | ✓ |
| SHA3-256 | Y |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | | ✓ | ✓ |
| SHA-512/256 | Y |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | | ✓ | ✓ |
| SHA-256 | Y |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | ✓ | ✓ | ✓ |
| KMAC256 | N |[NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) | ✓ | ✓ | ✓ |
| KMAC128 | N |[NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) | ✓ | ✓ | ✓ |
| SHAKE256 | Y |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | ✓ | ✓ | ✓ |

### Approved Hash Functions for Password Storage

The following hash functions are specifically recommended for secure password storage. These slow-hashing algorithms mitigate brute-force and dictionary attacks by increasing the computational difficulty of password cracking.

| Hash Function | Reference | Required Parameter Sets | L1 | L2 | L3 |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | --|--|--|
| argon2 | RFC 9106 | Argon2ID: Memory Cost 19MB, Time Cost 2, Parallelism 1 | | ✓ | ✓ |
| scrypt | RFC 7914 | 2^15 r = 8 p = 1 | | ✓ | ✓ |
| bcrypt | -- | At least 10 rounds. | | ✓ | ✓ |
| PBKDF2_SHA512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 210,000 iterations | ✓ | ✓ | ✓ |
| PBKDF2_SHA256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 600,000 iterations | ✓ | ✓ | ✓ |

### Disallowed Hash Functions

The following hash functions MUST NOT be used in any cryptographic operation generating new material due to known weaknesses and vulnerabilities, they MAY only be used for verification of existing material.

| Hash functions | Reference |
| ---------------- | --------------------------------------------------------------------------------------------------------- |
| CRC (any length) | -- |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) |

### Disallowed Hash Functions for Digital Signatures

For digital signature implementations, the following hash functions MUST NOT be used due to insufficient collision resistance:

| Hash functions | Reference |
| -------------- | -------------------------------------------------------------- |
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) |

## Key Exchange Mechanisms (V6.7)

### Approved KEX Schemes

A security strength of 112 bits or above MUST be ensured for all Key Exchange schemes, and their implementation MUST follow the parameter choices in the next table.

| Scheme | Domain Parameters |
|--|--|
| RSA | k >= 2048 |
| Diffie-Hellman (DH) | L >= 2048 & N >= 224 |
| Elliptic Curve Diffie-Hellman (ECDH) | f >= 224 |

Where the following parameters are:

* k is the key size for RSA keys.
* L is the size of the public key and N is the size of the private key for finite field cryptography.
* f is the range of key sizes for ECC.

### Approved DH groups

The following groups are approved and MUST be used for implementations of Diffie-Hellman KEX. IKEv2 groups are provided for reference ([NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final)). Equivalent groups might be used in other protocols. This list is ordered STRONGEST to WEAKEST. Security strengths are documented in [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final), Appendix D, and [NIST SP 800-57 Part 1 Rev.5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Group | Scheme | Parameters | Security bits | L1 | L2 | L3 |
|--|--|--|--|--|--|--|
| 21 | ECC | 521-bit random ECP group | 260 | | | ✓ |
| 32 | ECC | Curve448 | 224 | | | ✓ |
| 18 | MODP | 8192-bit MODP Group | 192 < 200 | | ✓ | ✓ |
| 20 | ECC | 384-bit random ECP group | 192 | | ✓ | ✓ |
| 17 | MODP | 6144-bit MODP Group | 128 < 176 | ✓ | ✓ | ✓ |
| 16 | MODP | 4096-bit MODP Group | 128 < 152 | ✓ | ✓ | ✓ |
| 31 | ECC | Curve25519 | 128 | ✓ | ✓ | ✓ |
| 19 | ECC | 256-bit random ECP group | 128 | ✓ | ✓ | ✓ |
| 15 | MODP | 3072-bit MODP Group | 128 | ✓ | ✓ | ✓ |
| 14 | MODP | 2048-bit MODP Group | 112 | ✓ | ✓ | ✓ |

### Disallowed KEX Schemes

Any new implementation MUST NOT use any scheme that is NOT compliant with [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) & [B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) and [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final).

Specifically, IKEv1 MUST NOT be used in production.

## Message Authentication Codes (MAC)

Message Authentication Codes (MACs) are cryptographic constructs used to verify the integrity and authenticity of a message. A MAC takes a message and a secret key as inputs and produces a fixed-size tag (the MAC value). MACs are widely used in secure communication protocols (e.g., TLS/SSL) to ensure that messages exchanged between parties are authentic and intact.

### Approved MAC Algorithms

The following MAC algorithms are approved for use in securing messages by providing integrity and authenticity guarantees. Implementations MUST use only authenticated encryption modes or separately applied HMAC to ensure the security of messages:

| MAC Algorithm     | Reference                                                                                 | Suitable for General Use? | L1 | L2 | L3 |
| ----------------- | ----------------------------------------------------------------------------------------- | ------------------------- |----|----|----|
| HMAC-SHA-256      | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | ✓                       | ✓  | ✓  | ✓  |
| HMAC-SHA-384      | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | ✓                       |    | ✓  | ✓  |
| HMAC-SHA-512      | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | ✓                       |    | ✓  | ✓  |
| KMAC128           | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | ✓                       | ✓  | ✓  | ✓  |
| KMAC256           | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | ✓                       | ✓  | ✓  | ✓  |

### Disallowed MAC Algorithms

The following algorithms are explicitly banned and MUST NOT be used due to known vulnerabilities or insufficient security strength:

| MAC Algorithm    | Reference                                                                          |
| ---------------- | ---------------------------------------------------------------------------------- |
| MD5-based HMAC   | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                |
| SHA-1-based HMAC | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) |

## Digital Signatures

### Approved Digital Signature Algorithms

The following digital signature algorithms are approved for use in ensuring data authenticity and integrity. Signature schemes MUST use approved key sizes and parameters per [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final):

| Signature Algorithm        | Reference                                                                          | Suitable for General Use? | L1 | L2 | L3 |
| -------------------------- | ---------------------------------------------------------------------------------- | ------------------------- |----|----|----|
| EdDSA (Ed25519, Ed448)     | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)                                | ✓                         | ✓  | ✓  | ✓  |
| ECDSA (P-256, P-384, P-521)| [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)                         | ✓                         | ✓  | ✓  | ✓  |
| RSA-PSS                    | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)                                | ✓                         | ✓  | ✓  | ✓  |

### Disallowed Digital Signature Algorithms

The following digital signature algorithms MUST NOT be used due to known weaknesses or insufficient security strength:

| Signature Algorithm | Reference                                                                          |
| ------------------- | ---------------------------------------------------------------------------------- |
| RSA PKCS#1 v1.5     | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)                                |
| DSA (any key size)  | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)                          |

## Key Derivation Functions (KDFs)

### Approved KDFs

Key derivation functions transform a keying material into keys suitable for specific cryptographic operations. The following KDFs are approved and MUST be used based on the application’s needs and security context:

| KDF         | Reference                                                                                     | Suitable for General Use? | L1 | L2 | L3 |
| ----------- | --------------------------------------------------------------------------------------------- | ------------------------- |----|----|----|
| argon2id    | [RFC 9106](https://www.rfc-editor.org/info/rfc9106)                                          | ✓                       |    | ✓  | ✓  |
| scrypt      | [RFC 7914](https://www.rfc-editor.org/info/rfc7914)                                          | ✓                       |    | ✓  | ✓  |
| PBKDF2      | [RFC 8018](https://www.rfc-editor.org/info/rfc8018) & [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final) | ✓                       | ✓  | ✓  | ✓  |
| HKDF        | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                          | ✓                       | ✓  | ✓  | ✓  |

### Disallowed KDFs

The following KDFs are explicitly banned and MUST NOT be used due to insufficient security properties or known weaknesses:

| KDF            | Reference                                                                          |
| -------------- | ---------------------------------------------------------------------------------- |
| MD5-based KDFs | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                |
| SHA-1-based KDFs | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) |

### Post-Quantum Encryption Standards

PQC implementations must be inline with [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd)/[204](https://csrc.nist.gov/pubs/fips/204/ipd)/[205](https://csrc.nist.gov/pubs/fips/205/ipd) as there isn't any hardened code nor implementation reference yet. https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards
