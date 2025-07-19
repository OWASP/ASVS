# V11 암호화

## 제어 목표

The objective of this chapter is to define best practices for the general use of cryptography, as well as to instill a fundamental understanding of cryptographic principles and inspire a shift toward more resilient and modern approaches. It encourages the following:
이 챕터의 목표는 암호화의 일반적인 사용에 대한 **모범 사례**를 정의하고, 암호화 원리에 대한 **근본적인 이해**를 확립하여 더욱 **견고하고 현대적인 접근 방식**으로 전환하도록 장려하는 것이다. 본 챕터는 다음을 권장한다.

* Implementing robust cryptographic systems that fail securely, adapt to evolving threats, and are future-proof.
* Utilizing cryptographic mechanisms that are both secure and aligned with industry best practices.
* Maintaining a secure cryptographic key management system with appropriate access controls and auditing.
* Regularly evaluating the cryptographic landscape to assess new risks and adapt algorithms accordingly.
* Discovering and managing cryptographic use cases throughout the application's lifecycle to ensure that all cryptographic assets are accounted for and secured.
* **안전하게 실패**하고, 진화하는 위협에 적응하며, 미래에도 사용할 수 있는 **강력한 암호화 시스템을 구현**한다.
* 안전하고 **업계 모범 사례에 부합**하는 암호화 메커니즘을 활용한다.
* **적절한 접근 제어 및 감사 기능**을 갖춘 안전한 암호화 키 관리 시스템을 유지한다.
* 새로운 위험을 평가하고 그에 따라 알고리즘을 조정하기 위해 **암호화 환경을 정기적으로 평가**한다.
* 애플리케이션 수명 주기 전반에 걸쳐 암호화 사용 사례를 발견하고 관리하여 **모든 암호화 자산이 파악되고 보호**되도록 한다.

In addition to outlining general principles and best practices, this document also provides more in-depth technical information about the requirements in Appendix C - Cryptography Standards. This includes algorithms and modes that are considered "approved" for the purposes of the requirements in this chapter.
이 문서는 일반적인 원칙 및 모범 사례를 설명하는 것 외에도, 부록 C - 암호화 표준의 요구 사항에 대한 보다 **심층적인 기술 정보**를 제공한다. 여기에는 이 챕터의 요구 사항 목적에 따라 "승인된" 것으로 간주되는 알고리즘 및 모드가 포함된다.

Requirements that use cryptography to solve a separate problem, such as secrets management or communications security, will be in different parts of the standard.
비밀 관리 또는 통신 보안과 같이 별도의 문제를 해결하기 위해 암호화를 사용하는 요구 사항은 표준의 다른 부분에 기술될 것이다.

## V11.1 Cryptographic Inventory and Documentation
## V11.1 암호화 인벤토리 및 문서화

Applications need to be designed with strong cryptographic architecture to protect data assets according to their classification. Encrypting everything is wasteful; not encrypting anything is legally negligent. A balance must be struck, usually during architectural or high-level design, design sprints, or architectural spikes. Designing cryptography "on the fly" or retrofitting it will inevitably cost much more to implement securely than simply building it in from the start.
애플리케이션은 데이터 분류에 따라 데이터 자산을 보호하기 위한 **강력한 암호화 아키텍처**로 설계되어야 한다. 모든 것을 암호화하는 것은 낭비이며, 아무것도 암호화하지 않는 것은 법적으로 태만한 것이다. 일반적으로 아키텍처 또는 고수준 설계, 설계 스프린트 또는 아키텍처 스파이크 중에 균형을 이루어야 한다. "즉흥적으로" 암호화를 설계하거나 나중에 적용하는 것은 처음부터 구축하는 것보다 안전하게 구현하는 데 훨씬 더 많은 비용이 소요될 수 있다.

It is important to ensure that all cryptographic assets are regularly discovered, inventoried, and assessed. Please see the appendix for more information on how this can be done.
모든 암호화 자산이 **정기적으로 발견, 인벤토리화 및 평가**되도록 하는 것이 중요하다. 수행 방법에 대한 자세한 내용은 부록을 참조해야 한다.

The need to future-proof cryptographic systems against the eventual rise of quantum computing is also critical. Post-Quantum Cryptography (PQC) refers to cryptographic algorithms designed to remain secure against attacks by quantum computers, which are expected to break widely used algorithms such as RSA and elliptic curve cryptography (ECC).
**양자 컴퓨팅**의 궁극적인 부상에 대비하여 암호화 시스템의 미래를 보장해야 하는 필요성 또한 중요하다. **양자 내성 암호(Post-Quantum Cryptography; PQC)**는 RSA 및 타원 곡선 암호(Elliptic Curve Cryptography; ECC)와 같이 널리 사용되는 알고리즘을 깨뜨릴 것으로 예상되는 양자 컴퓨터의 공격에 대해 보안을 유지하도록 설계된 암호화 알고리즘을 의미한다.

Please see the appendix for current guidance on vetted PQC primitives and standards.
검증된 PQC 기본 요소 및 표준에 대한 현재 지침은 부록을 참조해야 한다.

| # | Description | Level |
| :---: | :--- | :---: |
| **11.1.1** | Verify that there is a documented policy for management of cryptographic keys and a cryptographic key lifecycle that follows a key management standard such as NIST SP 800-57. This should include ensuring that keys are not overshared (for example, with more than two entities for shared secrets and more than one entity for private keys). | 2 |
| **11.1.1** | 암호화 키 관리를 위한 **문서화된 정책**과 **NIST SP 800-57**과 같은 키 관리 표준을 따르는 암호화 키 수명 주기가 있는지 **검증**해야 한다. 여기에는 키가 과도하게 공유되지 않도록 하는 것이 포함된다(예: 공유 비밀의 경우 두 개를 초과하는 엔터티와 개인 키의 경우 한 개를 초과하는 엔터티에 공유되지 않도록). | 2 |
| **11.1.2** | Verify that a cryptographic inventory is performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application. It must also document where keys can and cannot be used in the system, and the types of data that can and cannot be protected using the keys. | 2 |
| **11.1.2** | 암호화 인벤토리가 수행되고, 유지 관리되고, 정기적으로 업데이트되며, 애플리케이션에서 사용되는 모든 **암호화 키, 알고리즘 및 인증서**를 포함하는지 **검증**해야 한다. 또한 시스템에서 키를 사용할 수 있는 위치와 사용할 수 없는 위치, 그리고 키를 사용하여 보호할 수 있는 데이터 유형과 보호할 수 없는 데이터 유형을 문서화해야 한다. | 2 |
| **11.1.3** | Verify that cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations. | 3 |
| **11.1.3** | 암호화, 해싱 및 서명 작업을 포함하여 시스템의 모든 암호화 인스턴스를 식별하기 위해 **암호화 발견 메커니즘**이 사용되는지 **검증**해야 한다. | 3 |
| **11.1.4** | Verify that a cryptographic inventory is maintained. This must include a documented plan that outlines the migration path to new cryptographic standards, such as post-quantum cryptography, in order to react to future threats. | 3 |
| **11.1.4** | 암호화 인벤토리가 유지 관리되는지 **검증**해야 한다. 여기에는 미래의 위협에 대응하기 위해 **양자 내성 암호**와 같은 새로운 암호화 표준으로의 **마이그레이션 경로**를 설명하는 문서화된 계획이 포함되어야 한다. | 3 |

## V11.2 Secure Cryptography Implementation
## V11.2 안전한 암호화 구현

This section defines the requirements for the selection, implementation, and ongoing management of core cryptographic algorithms for an application. The objective is to ensure that only robust, industry-accepted cryptographic primitives are deployed, in alignment with current standards (e.g., NIST, ISO/IEC) and best practices. Organizations must ensure that each cryptographic component is selected based on peer-reviewed evidence and practical security testing.
이 섹션은 애플리케이션의 핵심 암호화 알고리즘 선택, 구현 및 지속적인 관리에 대한 요구 사항을 정의한다. 목표는 현재 표준(예: NIST, ISO/IEC) 및 모범 사례에 맞춰 **강력하고 업계에서 인정하는 암호화 기본 요소**만 배포되도록 하는 것이다. 조직은 각 암호화 구성 요소가 **동료 검토된 증거** 및 실제 보안 테스트를 기반으로 선택되도록 해야 한다.

| # | Description | Level |
| :---: | :--- | :---: |
| **11.2.1** | Verify that industry-validated implementations (including libraries and hardware-accelerated implementations) are used for cryptographic operations. | 2 |
| **11.2.1** | 암호화 작업에 **업계에서 검증된 구현**(라이브러리 및 하드웨어 가속 구현 포함)이 사용되는지 **검증**해야 한다. | 2 |
| **11.2.2** | Verify that the application is designed with crypto agility such that random number, authenticated encryption, MAC, or hashing algorithms, key lengths, rounds, ciphers and modes can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks. Similarly, it must also be possible to replace keys and passwords and re-encrypt data. This will allow for seamless upgrades to post-quantum cryptography (PQC), once high-assurance implementations of approved PQC schemes or standards are widely available. | 2 |
| **11.2.2** | 난수, 인증 암호화, MAC, 또는 해싱 알고리즘, 키 길이, 라운드, 암호 및 모드를 언제든지 재구성, 업그레이드 또는 교체하여 암호화 해독으로부터 보호할 수 있도록 애플리케이션이 **암호화 유연성(crypto agility)**을 갖추고 설계되었는지 **검증**해야 한다. 마찬가지로, 키와 비밀번호를 교체하고 데이터를 다시 암호화하는 것도 가능해야 한다. 이를 통해 승인된 PQC 체계 또는 표준의 고신뢰 구현이 널리 사용 가능해지면 **양자 내성 암호(PQC)**로 원활하게 업그레이드할 수 있다. | 2 |
| **11.2.3** | Verify that all cryptographic primitives utilize a minimum of 128-bits of security based on the algorithm, key size, and configuration. For example, a 256-bit ECC key provides roughly 128 bits of security where RSA requires a 3072-bit key to achieve 128 bits of security. | 2 |
| **11.2.3** | 모든 암호화 기본 요소가 알고리즘, 키 크기 및 구성에 따라 **최소 128비트의 보안**을 사용하는지 **검증**해야 한다. 예를 들어, 256비트 ECC 키는 대략 128비트의 보안을 제공하는 반면, RSA는 128비트의 보안을 달성하기 위해 3072비트 키를 필요로 한다. | 2 |
| **11.2.4** | Verify that all cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information. | 3 |
| **11.2.4** | 모든 암호화 작업이 정보를 유출하는 것을 방지하기 위해 비교, 계산 또는 반환 시 '단락' 작업 없이 **상수 시간(constant-time)**으로 수행되는지 **검증**해야 한다. | 3 |
| **11.2.5** | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable vulnerabilities, such as Padding Oracle attacks. | 3 |
| **11.2.5** | 모든 암호화 모듈이 **안전하게 실패**하고, 패딩 오라클 공격(Padding Oracle attacks)과 같은 취약점을 허용하지 않는 방식으로 오류가 처리되는지 **검증**해야 한다. | 3 |

## V11.3 Encryption Algorithms
## V11.3 암호화 알고리즘

Authenticated encryption algorithms built on AES and CHACHA20 form the backbone of modern cryptographic practice.
AES 및 CHACHA20을 기반으로 구축된 **인증 암호화 알고리즘**은 현대 암호화 관행의 근간을 이룬다.

| # | Description | Level |
| :---: | :--- | :---: |
| **11.3.1** | Verify that insecure block modes (e.g., ECB) and weak padding schemes (e.g., PKCS#1 v1.5) are not used. | 1 |
| **11.3.1** | 안전하지 않은 블록 모드(예: ECB) 및 약한 패딩 체계(예: PKCS#1 v1.5)가 사용되지 않는지 **검증**해야 한다. | 1 |
| **11.3.2** | Verify that only approved ciphers and modes such as AES with GCM are used. | 1 |
| **11.3.2** | GCM을 사용하는 AES와 같이 **승인된 암호 및 모드**만 사용되는지 **검증**해야 한다. | 1 |
| **11.3.3** | Verify that encrypted data is protected against unauthorized modification preferably by using an approved authenticated encryption method or by combining an approved encryption method with an approved MAC algorithm. | 2 |
| **11.3.3** | 암호화된 데이터가 승인된 인증 암호화 방법 또는 승인된 암호화 방법과 승인된 MAC 알고리즘을 결합하여 **무단 수정으로부터 보호**되는지 **검증**해야 한다. | 2 |
| **11.3.4** | Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key and data-element pair. The method of generation must be appropriate for the algorithm being used. | 3 |
| **11.3.4** | **논스(nonces), 초기화 벡터** 및 기타 단일 사용 번호가 둘 이상의 암호화 키 및 데이터 요소 쌍에 사용되지 않는지 **검증**해야 한다. 생성 방법은 사용되는 알고리즘에 적합해야 한다. | 3 |
| **11.3.5** | Verify that any combination of an encryption algorithm and a MAC algorithm is operating in encrypt-then-MAC mode. | 3 |
| **11.3.5** | 암호화 알고리즘과 MAC 알고리즘의 모든 조합이 **Encrypt-then-MAC 모드**에서 작동하는지 **검증**해야 한다. | 3 |

## V11.4 Hashing and Hash-based Functions
## V11.4 해싱 및 해시 기반 함수

Cryptographic hashes are used in a wide variety of cryptographic protocols, such as digital signatures, HMAC, key derivation functions (KDF), random bit generation, and password storage. The security of the cryptographic system is only as strong as the underlying hash functions used. This section outlines the requirements for using secure hash functions in cryptographic operations.
암호화 해시는 디지털 서명, HMAC, 키 유도 함수(KDF), 무작위 비트 생성 및 비밀번호 저장과 같은 다양한 암호화 프로토콜에서 사용된다. 암호화 시스템의 보안은 사용되는 기본 해시 함수의 강도에 달려 있다. 이 섹션에서는 암호화 작업에서 **안전한 해시 함수**를 사용하는 요구 사항을 설명한다.

For password storage, as well as the cryptography appendix, the [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms) will also provide useful context and guidance.
비밀번호 저장 및 암호화 부록의 경우, [OWASP 비밀번호 저장 치트 시트](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms)도 유용한 맥락과 지침을 제공할 것이다.

| # | Description | Level |
| :---: | :--- | :---: |
| **11.4.1** | Verify that only approved hash functions are used for general cryptographic use cases, including digital signatures, HMAC, KDF, and random bit generation. Disallowed hash functions, such as MD5, must not be used for any cryptographic purpose. | 1 |
| **11.4.1** | 디지털 서명, HMAC, KDF 및 무작위 비트 생성을 포함한 일반적인 암호화 사용 사례에 **승인된 해시 함수**만 사용되는지 **검증**해야 한다. MD5와 같이 허용되지 않는 해시 함수는 어떤 암호화 목적으로도 사용해서는 안 된다. | 1 |
| **11.4.2** | Verify that passwords are stored using an approved, computationally intensive, key derivation function (also known as a "password hashing function"), with parameter settings configured based on current guidance. The settings should balance security and performance to make brute-force attacks sufficiently challenging for the required level of security. | 2 |
| **11.4.2** | 비밀번호가 승인된, **계산 집약적인 키 유도 함수**("비밀번호 해싱 함수"라고도 함)를 사용하여 저장되고, 파라미터 설정이 현재 지침에 따라 구성되었는지 **검증**해야 한다. 설정은 필요한 보안 수준에 대한 **무차별 대입 공격**을 충분히 어렵게 만들기 위해 보안과 성능의 균형을 이루어야 한다. | 2 |
| **11.4.3** | Verify that hash functions used in digital signatures, as part of data authentication or data integrity are collision resistant and have appropriate bit-lengths. If collision resistance is required, the output length must be at least 256 bits. If only resistance to second pre-image attacks is required, the output length must be at least 128 bits. | 2 |
| **11.4.3** | 데이터 인증 또는 데이터 무결성의 일부로 디지털 서명에 사용되는 해시 함수가 **충돌 저항성**을 가지며 적절한 비트 길이를 갖는지 **검증**해야 한다. 충돌 저항성이 필요한 경우, 출력 길이는 **최소 256비트**여야 한다. 두 번째 역상 공격에 대한 저항성만 필요한 경우, 출력 길이는 **최소 128비트**여야 한다. | 2 |
| **11.4.4** | Verify that the application uses approved key derivation functions with key stretching parameters when deriving secret keys from passwords. The parameters in use must balance security and performance to prevent brute-force attacks from compromising the resulting cryptographic key. | 2 |
| **11.4.4** | 비밀번호로부터 비밀 키를 유도할 때 애플리케이션이 **키 스트레칭 파라미터**를 사용하여 승인된 키 유도 함수를 사용하는지 **검증**해야 한다. 사용 중인 파라미터는 결과적인 암호화 키를 손상시키는 무차별 대입 공격을 방지하기 위해 보안과 성능의 균형을 이루어야 한다. | 2 |

## V11.5 Random Values
## V11.5 무작위 값

Cryptographically secure Pseudo-random Number Generation (CSPRNG) is incredibly difficult to get right. Generally, good sources of entropy within a system will be quickly depleted if over-used, but sources with less randomness can lead to predictable keys and secrets.
**암호학적으로 안전한 의사 난수 생성(CSPRNG)**은 올바르게 구현하기가 매우 어렵다. 일반적으로 시스템 내의 좋은 엔트로피 소스는 과도하게 사용될 경우 빠르게 고갈되지만, 무작위성이 적은 소스는 예측 가능한 키와 비밀로 이어질 수 있다.

| # | Description | Level |
| :---: | :--- | :---: |
| **11.5.1** | Verify that all random numbers and strings which are intended to be non-guessable must be generated using a cryptographically secure pseudo-random number generator (CSPRNG) and have at least 128 bits of entropy. Note that UUIDs do not respect this condition. | 2 |
| **11.5.1** | 예측 불가능해야 하는 모든 난수 및 문자열이 **암호학적으로 안전한 의사 난수 생성기(CSPRNG)**를 사용하여 생성되고 **최소 128비트의 엔트로피**를 갖는지 **검증**해야 한다. UUID는 이 조건을 충족하지 않는다. | 2 |
| **11.5.2** | Verify that the random number generation mechanism in use is designed to work securely, even under heavy demand. | 3 |
| **11.5.2** | 사용 중인 난수 생성 메커니즘이 과도한 수요 상황에서도 **안전하게 작동**하도록 설계되었는지 **검증**해야 한다. | 3 |

## V11.6 Public Key Cryptography
## V11.6 공개 키 암호화

Public Key Cryptography will be used where it is not possible or not desirable to share a secret key between multiple parties.
공개 키 암호화는 여러 당사자 간에 비밀 키를 공유하는 것이 불가능하거나 바람직하지 않은 경우에 사용될 것이다.

As part of this, there exists a need for approved key exchange mechanisms, such as Diffie-Hellman and Elliptic Curve Diffie-Hellman (ECDH) to ensure that the cryptosystem remains secure against modern threats. The "Secure Communication" chapter provides requirements for TLS so the requirements in this section are intended for situations where Public Key Cryptography is being used in use cases other than TLS.
이의 일부로, 디피-헬만(Diffie-Hellman) 및 타원 곡선 디피-헬만(Elliptic Curve Diffie-Hellman; ECDH)과 같은 **승인된 키 교환 메커니즘**이 필요하여 암호화 시스템이 현대 위협에 대해 안전하게 유지되도록 한다. "안전한 통신" 챕터는 TLS에 대한 요구 사항을 제공하므로 이 섹션의 요구 사항은 TLS 이외의 사용 사례에서 공개 키 암호화가 사용되는 상황을 위한 것이다.

| # | Description | Level |
| :---: | :--- | :---: |
| **11.6.1** | Verify that only approved cryptographic algorithms and modes of operation are used for key generation and seeding, and digital signature generation and verification. Key generation algorithms must not generate insecure keys vulnerable to known attacks, for example, RSA keys which are vulnerable to Fermat factorization. | 2 |
| **11.6.1** | 키 생성 및 시딩, 디지털 서명 생성 및 검증에 **승인된 암호화 알고리즘 및 작동 모드**만 사용되는지 **검증**해야 한다. 키 생성 알고리즘은 알려진 공격에 취약한 안전하지 않은 키(예: 페르마 인수분해(Fermat factorization)에 취약한 RSA 키)를 생성해서는 안 된다. | 2 |
| **11.6.2** | Verify that approved cryptographic algorithms are used for key exchange (such as Diffie-Hellman) with a focus on ensuring that key exchange mechanisms use secure parameters. This will prevent attacks on the key establishment process which could lead to adversary-in-the-middle attacks or cryptographic breaks. | 3 |
| **11.6.2** | 키 교환(예: 디피-헬만)에 **승인된 암호화 알고리즘**이 사용되는지 **검증**하고, 키 교환 메커니즘이 **안전한 파라미터**를 사용하도록 하는 데 중점을 두어야 한다. 이는 중간자 공격(adversary-in-the-middle attacks) 또는 암호화 해독으로 이어질 수 있는 키 설정 프로세스에 대한 공격을 방지할 것이다. | 3 |

## V11.7 In-Use Data Cryptography
## V11.7 사용 중 데이터 암호화

Protecting data while it is being processed is paramount. Techniques such as full memory encryption, encryption of data in transit, and ensuring data is encrypted as quickly as possible after use is recommended.
데이터가 처리되는 동안 데이터를 보호하는 것이 가장 중요하다. **전체 메모리 암호화, 전송 중 데이터 암호화** 및 사용 후 가능한 한 빨리 데이터가 암호화되도록 하는 기술이 권장된다.

| # | Description | Level |
| :---: | :--- | :---: |
| **11.7.1** | Verify that full memory encryption is in use that protects sensitive data while it is in use, preventing access by unauthorized users or processes. | 3 |
| **11.7.1** | 사용 중인 민감한 데이터를 보호하고 무단 사용자 또는 프로세스의 접근을 방지하기 위해 **전체 메모리 암호화**가 사용되는지 **검증**해야 한다. | 3 |
| **11.7.2** | Verify that data minimization ensures the minimal amount of data is exposed during processing, and ensure that data is encrypted immediately after use or as soon as feasible. | 3 |
| **11.7.2** | **데이터 최소화**가 처리 중에 노출되는 데이터의 양을 최소화하고, 사용 직후 또는 가능한 한 빨리 데이터가 암호화되도록 보장하는지 **검증**해야 한다. | 3 |

## 참조

더 많은 정보는 다음을 참조한다:

* [OWASP 웹 보안 테스팅 가이드: 취약한 암호화 테스트](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography)
* [OWASP 암호화 저장 치트 시트](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
