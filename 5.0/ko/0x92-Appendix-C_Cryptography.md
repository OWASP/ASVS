# 부록 C: 암호 기법 표준

"암호 기법" 장은 단순히 모범 사례를 정의하는 것을 넘어선다. 이 장은 암호학 원리에 대한 이해를 향상시키고, 보다 견고하고 현대적인 보안 방법의 채택을 장려하는 것을 목표로 한다. 이 부록에서는 각 요구 사항에 대한 상세한 기술 정보를 제공하며, "암호 기법" 장에 설명된 전반적인 표준을 보완한다.

이 부록은 다양한 암호화 메커니즘(mechanism)에 대한 승인 수준을 정의한다:

* 승인된 메커니즘(A)은 애플리케이션에서 사용할 수 있다.
* 기존 메커니즘(L)은 애플리케이션에서 사용해서는 안 되지만, 기존 애플리케이션이나 코드와의 호환성을 위해 제한적으로 사용될 수 있다. 이러한 메커니즘의 사용은 현재 본질적으로 취약점으로 간주하지는 않지만, 가능한 한 빠른 시일 내에 더 안전하고 미래 지향적인 메커니즘으로 대체되어야 한다.
* 허용되지 않은 메커니즘(D)은 현재 취약한 것으로 간주되거나 충분한 보안을 제공하지 않으므로 사용해서는 안 된다.

이 목록은 특정 애플리케이션의 맥락에서 여러 가지 이유로 재정의 될 수 있으며, 예를 들어 다음과 같다:

* 암호학 분야의 새로운 발전;
* 규제 준수.

## 암호 자산 목록 및 문서화

이 문단은 V11.1 암호 목록 및 문서화에 대한
추가 정보를 제공한다.

알고리즘, 키, 인증서와 같은 암호 자산은 정기적으로 발견되고, 목록화되며, 평가되어야 한다. 3단계에서는 애플리케이션에서 암호 기법의 사용을 식별하기 위해 정적 및 동적 스캐닝을 포함해야 한다. SAST 및 DAST와 같은 도구는 이에 도움이 될 수 있으나, 더 포괄적인 범위를 위해서는 전용 도구가 필요할 수 있다. 프리웨어 도구의 예시는 다음과 같다:

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

## 암호 매개변수의 동등 강도

다양한 암호 시스템의 상대적 보안 강도는 이 표에 제시되어 있다. (출처: [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), p.71):

| 보안 강도 | 대칭키 알고리즘 | 유한체 | 소인수 분해 | 타원 곡선 |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA   | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

애플리케이션 예시:

* 유한체 암호 기법: DSA, FFDH, MQV
* 소인수 분해 암호 기법: RSA
* 타원 곡선 암호 기법: ECDSA, EdDSA, ECDH, MQV

참고: 이 문단은 양자컴퓨터가 존재하지 않는다고 가정한다. 만약 그러한 컴퓨터가 존재한다면, 마지막 3개 열의 추정치는 더 이상 유효하지 않게 된다.

## 무작위 값

이 문단은 V11.5 무작위 값에 대한
추가 정보를 제공한다.

| 이름 | 버전/참조 | 비고 | 상태 |
|:---|:----|:----|:-:|
| `/dev/random` | Linux 4.8+ [(Oct 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3), iOS, Android, 그리고 다른 Linux 기반 POSIX 운영체제에서도 사용된다. [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539)를 기반으로 한다. | ChaCha20 스트림을 활용한다. iOS의 [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) 및 Android의 [`Secure Random`](https://developer.android.com/reference/java/security/SecureRandom)에서 각각 올바른 설정이 적용된 상태로 제공된다. | A |
| `/dev/urandom` | 무작위 데이터를 제공하는 Linux 커널의 특수 파일 | 하드웨어 난수를 통해 고품질의 엔트로피 소스를 제공한다. | A |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | 일반적인 구현에서 사용되며, 예를 들어 [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers)로 설정된 [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom)이 사용된다. | A |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2)은 [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) 및 [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web)에서 지원한다. | 단순하고 최소화된 API를 통해 커널의 엔트로피 소스에서 보안 무작위 바이트를 직접 제공한다. 이는 보다 최신 방식이며, 기존 API와 관련된 문제점을 피할 수 있다. | A |

HMAC-DRBG 또는 Hash-DRBG와 함께 사용되는 기반 해시 함수는 반드시 해당 용도로 승인되어야 한다.

## 암호 알고리즘

이 문단은 V11.3 암호화 알고리즘에 대한
추가 정보를 제공한다.

승인된 암호 알고리즘은 선호도 순서로 제시되어 있다.

| 대칭키 알고리즘 | 참조 | 상태 |
| ------ | ------ |:-:|
| AES-256 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | A |
| Salsa20 | [Salsa 20 specification](https://cr.yp.to/snuffle/spec.pdf) | A |
| XChaCha20 | [XChaCha20 Draft](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-xchacha-03) | A |
| XSalsa20 | [Extending the Salsa20 nonce](https://cr.yp.to/snuffle/xsalsa-20110204.pdf) | A |
| ChaCha20 | [RFC 8439](https://www.rfc-editor.org/info/rfc8439) | A |
| AES-192 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | A |
| AES-128 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | L |
| 2TDEA | | D |
| TDEA (3DES/3DEA) | | D |
| IDEA | | D |
| RC4 | | D |
| Blowfish| | D |
| ARC4 | | D |
| DES | | D |

### AES 암호 모드

AES와 같은 블록 암호는 다양한 운용 모드와 함께 사용할 수 있다. 전자 코드북(Electronic codebook; ECB)와 같은 많은 운용 모드는 안전하지 않으며, 사용해서는 안 된다. 갈루아/카운터 모드(Galois/Counter Mode; GCM)와 CBC-MAC을 사용하는 카운터 모드(Counter with Cipher Block Chaining Message Authentication Code; CCM)는 인증 암호화를 제공하며, 최신 애플리케이션에서 사용하는 것이 권장된다.

승인된 모드는 선호도 순서로 제시되어 있다.

| 모드 | 인증 여부 | 참조 | 상태 | 제한 사항 |
|--|--|--|--|--|
| GCM | 예 | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A | |
| CCM | 예 | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A | |
| CBC | 아니오 | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | L | |
| CCM-8 | 예 | | D | |
| ECB | 아니오 | | D | |
| CFB | 아니오 | | D | |
| OFB | 아니오 | | D | |
| CTR | 아니오 | | D | |

비고:

* 모든 암호화된 메시지는 반드시 인증되어야 한다. CBC 모드를 사용하는 모든 경우에 반드시 메시지 무결성을 검증하기 위한 해시 기반 MAC 알고리즘을 함께 사용해야 한다. 일반적으로 반드시 암호화 후 해싱 방식(Encrypt-Then-Hash)을 적용해야 한다. (단, TLS 1.2는 해시 후 암호화 방식(Hash-Then-Encrypt)을 사용한다.) 이것이 보장되지 않는다면, CBC를 절대 사용해서는 안 된다. MAC 알고리즘 없이 암호화가 허용되는 애플리케이션은 디스크 암호화로 한정된다.
* CBC 모드를 사용하는 경우, 패딩 검증이 상수 시간(constant time)으로 수행되도록 보장해야 한다.
* CCM-8을 사용할 경우, MAC 태그의 보안 강도는 64비트에 불과하다. 이는 최소 128비트 이상의 보안 강도를 요구하는 요구사항 6.2.9를 준수하지 않는다.
* 디스크 암호화는 ASVS의 적용 범위에 포함되지 않는다. 따라서 이 부록에서는 디스크 암호화를 위한 승인된 방법을 제시하지 않는다. 이러한 용도의 경우, 인증 없는 암호화가 일반적으로 허용되며 XTS, XEX, LRW 모드가 주로 사용된다.

### 키 래핑

암호 키 래핑(cryptographic key wrap, 및 해당 언래핑)은 기존 키를 추가적인 암호화 메커니즘으로 캡슐화(즉, 래핑)하여 전송 과정 등에서 직접적으로 노출되지 않도록 보호하는 방법이다. 기존 키를 보호하기 위해 사용되는 이 추가 키를 래핑 키(wrap key)라고 한다.

이 작업은 신뢰할 수 없는 것으로 간주되는 환경에서 키를 보호하거나, 민감한 키를 신뢰할 수 없는 네트워크나 애플리케이션 내에서 전송해야 하는 경우에 수행될 수 있다.
그러나 래핑/언래핑 절차를 수행하기 전에 원래 키의 속성(예: 키의 식별 정보 및 용도)을 충분히 이해하는 것을 신중히 고려해야 하며, 이는 보안 측면뿐 아니라 특히 컴플라이언스 측면에서 원본 및 대상 시스템 또는 애플리케이션 모두에 영향을 미칠 수 있고, 컴플라이언스 요구사항에는 키 기능(예: 서명)에 대한 감사 추적(audit trail)과 적절한 키 저장 방식이 포함될 수 있다.

특히, 키 래핑에는 [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final)를 준수하고 양자 위협에 대비한 향후 권고 사항을 고려하여 반드시 AES-256을 사용해야 한다. AES를 사용하는 암호 모드는 선호도 순서로 제시되어 있다:

| 키 래핑 | 참조 | 상태 |
|--|--|:-:|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |

AES-192와 AES-128은 사용 사례에서 필요할 경우 사용할 수 있지만, 그 사용 사유는 해당 엔터티의 암호 인벤토리(cryptography inventory)에 반드시 문서화해야 한다.

### 인증 암호화

디스크 암호화를 제외하고, 암호화된 데이터는 인증 암호화(AE) 방식, 일반적으로는 연관 데이터가 있는 인증 암호화(AEAD) 방식을 사용하여 무단 변경으로부터 반드시 보호해야 한다.

애플리케이션은 승인된 AEAD 방식을 사용하는 것이 바람직하다. 대안으로, 승인된 암호화 방식과 승인된 MAC 알고리즘을 결합하여 암호화 후 MAC(Encrypt-then-MAC) 구조를 사용할 수도 있다.

MAC 후 암호화는 방식은 레거시 애플리케이션과의 호환성을 위해 여전히 허용된다. 이 방식은 TLS 1.2에서 구식 암호 제품군(cipher suites)과 함께 사용된다.

| AEAD 메커니즘 | 참조 | 상태 |
|---|---------|:-:|
|AES-GCM | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A |
|AES-CCM  | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A |
|ChaCha-Poly1305 | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539) | A |
|AEGIS-256 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128L| [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|Encrypt-then-MAC | | A |
|MAC-then-encrypt | | L |

## 해시 함수

이 문단은 V11.4 해싱과 해시 기반 함수에 대한
추가 정보를 제공한다.

### 범용 해시 함수

다음 표는 디지털 서명과 같은 일반적인 암호 사용 사례에서 승인된 해시 함수를 제시한다.

* 승인된 해시 함수는 강력한 충돌 저항성을 제공하며, 높은 보안 수준을 요구하는 애플리케이션에 적합하다.
* 이들 알고리즘 중 일부는 적절한 암호 키 관리와 함께 사용될 경우 강력한 공격 저항성을 제공하므로, HMAC, KDF, RBG 기능에도 추가적으로 승인된다.
* 출력 길이가 254비트 미만인 해시 함수는 충돌 저항성이 불충분하므로 디지털 서명 또는 충돌 저항성이 필요한 다른 애플리케이션에 사용해서는 안 된다. 다른 용도의 경우, 호환성 및 검증을 위해서만 레거시 시스템에서 제한적으로 사용할 수 있지만, 새로운 설계에서는 사용해서는 안 된다.

| 해시 함수 | 참조 | 상태 | 제한 사항 |
| ------ | ----------- |:-:| ---------- |
| SHA3-512 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-512 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA3-384 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-384 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA3-256 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-512/256 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA-256 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHAKE256 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| BLAKE2s | [BLAKE2: simpler, smaller, fast as MD5](https://eprint.iacr.org/2013/322) | A | |
| BLAKE2b | [BLAKE2: simpler, smaller, fast as MD5](https://eprint.iacr.org/2013/322) | A | |
| BLAKE3 | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf) | A | |
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | HMAC, KDF, RBG, 디지털 서명에 적합하지 않다. |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | HMAC, KDF, RBG, 디지털 서명에 적합하지 않다. |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | L | HMAC, KDF, RBG, 디지털 서명에 적합하지 않다. |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L | HMAC, KDF, RBG, 디지털 서명에 적합하지 않다. |
| CRC (길이 무관) |  | D |  |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) | D | |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D | |

### 비밀번호 저장을 위한 해시 함수

안전한 비밀번호 해싱을 위해서는 전용 해시 함수를 반드시 사용해야 한다. 이러한 느린 해싱(slow-hashing) 알고리즘은 비밀번호 크래킹의 연산 난이도를 높여 무차별 대입 공격과 사전 대입 공격을 완화한다.

| KDF | 참조 | 필수 매개변수 | 상태 |
| ---------- | --------- | ------------ |:-:|
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
|          |                                                     | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
|          |                                                     | t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A |
| scrypt   | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
|          |                                                     | p = 2: N ≥ 2^16 (64 MiB), r = 8  | A |
|          |                                                     | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8  | A |
| bcrypt | [A Future-Adaptable Password Scheme](https://www.researchgate.net/publication/2519476_A_Future-Adaptable_Password_Scheme) | cost ≥ 10 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 1,300,000 | L |

승인된 비밀번호 기반 키 유도 함수 (Password-based Key Derivation Function; PBKDF)는 비밀번호 저장에 사용할 수 있다.

## 키 유도 함수 (Key Derivation Functions; KDFs)

### 범용 키 유도 함수

| KDF              | 참조                                                                                     | 상태 |
| ---------------- | -------- |:-:|
| HKDF             | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                           | A      |
| TLS 1.2 PRF      | [RFC 5248](https://www.rfc-editor.org/info/rfc5248)                                           | L      |
| MD5 기반 KDFs   | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                           | D      |
| SHA-1 기반 KDFs | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | D      |

### 비밀번호 기반 키 유도 함수

| KDF | 참조 | 필수 매개변수 | 상태 |
| ---------- | --------- | ------------ |:-:|
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
|          |                                                     | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
|          |                                                     | t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A |
| scrypt   | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
|          |                                                     | p = 2: N ≥ 2^16 (64 MiB), r = 8  | A |
|          |                                                     | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8  | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 1,300,000 | L |

## 키 교환 메커니즘

이 문단은 V11.6 공개 키 암호에 대한
추가 정보를 제공한다.

### 키 교환 체계

모든 키 교환 체계에서 최소 112비트 이상의 보안 강도를 반드시 보장해야 하며, 구현 시 아래 표의 매개변수 선택을 따라야 한다.

| 체계 | 도메인 매개변수 | 순방향 보안 | 상태 |
|--|--|--|:-:|
| 유한체 디피-헬만(Finite Field Diffie-Hellman; FFDH) | L >= 3072 & N >= 256 | 예 | A |
| 타원 곡선 디피-헬만(Elliptic Curve Diffie-Hellman; ECDH) | f >= 256-383 | 예 | A |
| RSA-PKCS#1 v1.5 기반 암호화 키 전송 | | 아니오 | D |

다음은 매개변수 정의이다:

* k는 RSA 키의 크기이다.
* L은 유한체 암호 기법에서 공개 키의 크기이며, N은 개인 키의 크기이다.
* f는ECC에서 키 크기의 범위이다.

새로운 구현에서는 [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final), [NIST SP 800-56B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final), [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final) 표준을 준수하지 않는 어떤 체계도 사용해서는 안 된다. 특히, IKEv1은 운영 환경에서 사용해서는 안 된다.

### 디피-헬만 그룹

다음 그룹들은 디피-헬만 키 교환 구현 시 승인된 그룹이다. 보안 강도에 대한 상세 내용은 [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) 부록 D 및 [NIST SP 800-57 Part 1 Rev.5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)에 문서화되어 있다.

| 그룹            | 상태 |
|------------------|:------:|
| P-224, secp224r1 | A      |
| P-256, secp256r1 | A      |
| P-384, secp384r1 | A      |
| P-521, secp521r1 | A      |
| K-233, sect233k1 | A      |
| K-283, sect283k1 | A      |
| K-409, sect409k1 | A      |
| K-571, sect571k1 | A      |
| B-233, sect233r1 | A      |
| B-283, sect283r1 | A      |
| B-409, sect409r1 | A      |
| B-571, sect571r1 | A      |
| Curve448         | A      |
| Curve25519       | A      |
| MODP-2048        | A      |
| MODP-3072        | A      |
| MODP-4096        | A      |
| MODP-6144        | A      |
| MODP-8192        | A      |
| ffdhe2048        | A      |
| ffdhe3072        | A      |
| ffdhe4096        | A      |
| ffdhe6144        | A      |
| ffdhe8192        | A      |

## 메시지 인증 코드(Message Authentication Codes; MAC)

메시지 인증 코드(MAC)는 메시지의 무결성과 진위 여부를 검증하기 위해 사용되는 암호학적 구성 요소이다. MAC은 메시지와 비밀 키를 입력으로 받아 고정 길이의 태그(MAC 값)를 생성한다. MAC는 TLS, SSL 등과 같은 보안 통신 프로토콜에서 널리 사용되며, 통신 당사자 간에 교환되는 메시지가 인증되었고 변경되지 않았음을 보장한다.

| MAC 알고리즘 | 참조                                                                                 | 상태 |
| ----------    | --------------- |:-:|
| HMAC-SHA-256  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-384  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-512  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| KMAC128       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A |
| KMAC256       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A |
| BLAKE3 (keyed_hash mode) | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf)  | A |
| AES-CMAC      | [RFC 4493](https://datatracker.ietf.org/doc/html/rfc4493) & [NIST SP 800-38B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf) | A |
| AES-GMAC      | [NIST SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)            | A |
| Poly1305-AES  | [The Poly1305-AES message-authentication code](https://cr.yp.to/mac/poly1305-20050329.pdf)                  | A |
| HMAC-SHA-1    | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | L |
| HMAC-MD5      | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                | D      |

## 디지털 서명

서명 체계는 반드시 [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)에서 승인한 키 크기와 매개변수를 사용해야 한다.

| 서명 알고리즘            | 참조                                                  | 상태 |
| ------------------------------ | ---------------------------------------------              | :-:    |
| EdDSA (Ed25519, Ed448)         | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)        | A      |
| XEdDSA (Curve25519, Curve448)  | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)   | A      |
| ECDSA (P-256, P-384, P-521)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)  | A      |
| RSA-RSSA-PSS                   | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | A      |
| RSA-SSA-PKCS#1 v1.5            | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | D      |
| DSA (키 길이 무관)                | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)  | D      |

## 양자 내성 암호 표준

양자 내성 암호(Post-quantum cryptography; PQC) 구현은 [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd), [FIPS-204](https://csrc.nist.gov/pubs/fips/204/ipd), [FIPS-205](https://csrc.nist.gov/pubs/fips/205/ipd)를 준수해야 한다. 현재 이들 표준에 대해 보안이 강화된 코드 예제나 참조 구현은 아직 많지 않다. 자세한 내용은 [NIST announcement of the first three finalized post-quantum encryption standards (August 2024)](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)을 참조하라.

제안된 [mlkem768x25519](https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/03/) 양자 내성 하이브리드 TLS 키 합의 방식은 [Firefox release 132](https://www.mozilla.org/en-US/firefox/132.0/releasenotes/)와 [Chrome release 131](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html)과 같은 주요 브라우저에서 지원된다. 이 방식은 암호화 테스트 환경에서 사용하거나, 산업계 또는 정부에서 승인한 라이브러리에서 사용할 수 있다.
