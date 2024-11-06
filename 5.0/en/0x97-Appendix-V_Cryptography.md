# Appendix V: Cryptography

V6 goes beyond simply defining best practices. It aims to enhance understanding of cryptography principles and encourage the adoption of more resilient, modern security methods. This appendix provides detailed technical information regarding each requirement, complementing the overarching standards outlined in V6. 

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

Implementations MUST choose from the ciphers in this list, in order of preference:

| Symmetric Key Algorithms | Reference | L1 | L2 | L3 |
|--|--|--|--|--|
| AES-256 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | | ✓ | ✓ |
| ChaCha20 | [RFC 8439](https://www.rfc-editor.org/info/rfc8439) | | ✓ | ✓ |
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

## Hashing and Hash-based Functions (V6.6)

### Approved Hash Functions for General Use Cases

The following hash functions are approved for use in general cryptographic use cases such as digital signatures, HMAC, key derivation functions (KDF), and random bit generation (RBG). These functions provide strong collision resistance and are suitable for high-security applications. Some of these algorithms offer strong resistance to attacks when used with proper cryptographic key management, and so are additionally approved for HMAC, KDF, and RBG functions.

| Hash functions | Suitable for<br>HMAC/KDF/RBG? |Reference | L1 | L2 | L3 |
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

A complete list of IKE Groups is available by [IANA](https://www.iana.org/assignments/ikev2-parameters/ikev2-parameters.xhtml) under "Transform Type 4 - Key Exchange Method Transform IDs". Further recommendations on IKE specifically can be found on the [IPSec](https://github.com/santander-group-cyber-cto/CryptographyStandard/blob/main/Implementations/IPSec/README.md) section.

### Disallowed KEX Schemes

Any new implementation MUST NOT use any scheme that is NOT compliant with [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) & [B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) and [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final).

Specifically, IKEv1 MUST NOT be used in production.
