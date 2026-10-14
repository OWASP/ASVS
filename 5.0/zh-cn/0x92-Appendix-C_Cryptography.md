# 附录 C：密码学标准

“密码学”章节不仅定义了最佳实践，还旨在帮助读者深入理解密码学原理，并推动采用更具韧性的现代安全方法。本附录针对各项要求提供详细的技术说明，作为“密码学”章节总体标准的补充。

本附录将密码机制分为以下使用级别：

* 可用（A）：本标准认可，可在应用中使用。
* 遗留（L）：不应在应用中使用，仅可用于兼容现有的遗留应用或代码。目前使用此类机制本身不被视为漏洞，但应尽快替换为更安全、能够适应未来需求的机制。
* 禁止（D）：不得使用，因为这类机制目前已被攻破，或无法提供足够的安全性。

在具体应用中，可能需要基于多种原因调整此列表，包括：

* 密码学领域出现新的发展；
* 满足法规要求。

## 密码资产清单和文档

本节为 V11.1
密码资产清单和文档提供补充说明。

应定期发现、盘点和评估算法、密钥及证书等所有密码学资产。对于第 3 级，还应通过静态和动态扫描，识别应用中的密码学使用情况。SAST 和 DAST 工具可以提供帮助，但要实现更全面的覆盖，可能还需要使用专用工具。可免费使用的工具示例包括：

* [CryptoMon：使用 eBPF、以 Python 编写的网络密码学监控工具](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge：根据 CodeQL 输出生成完整的 CBOM](https://github.com/Santandersecurityresearch/cryptobom-forge)

## 密码学参数的等效安全强度

下表列出了不同密码学系统的相对安全强度（摘自 [NIST SP 800-57 第 1 部分](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)第 71 页）：

| 安全强度 | 对称密钥算法 | 有限域 | 整数分解 | 椭圆曲线 |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA   | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

应用示例：

* 有限域密码学：DSA、FFDH、MQV
* 整数分解密码学：RSA
* 椭圆曲线密码学：ECDSA、EdDSA、ECDH、MQV

注意：本节以不存在可用的量子计算机为前提。如果此类计算机成为现实，后三列的估算将不再有效。

## 随机值

本节为 V11.5
随机值提供补充说明。

| 名称 | 版本/参考资料 | 说明 | 状态 |
|:-:|:-:|:-:|:-:|
| `/dev/random` | Linux 4.8+ [（2016 年 10 月）](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3)，也存在于 iOS、Android 和其他基于 Linux 的 POSIX 操作系统中。基于 [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) | 使用 ChaCha20 流。在正确配置的情况下，可通过 iOS 的 [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) 和 Android 的 [`SecureRandom`](https://developer.android.com/reference/java/security/SecureRandom) 使用。 | A |
| `/dev/urandom` | Linux 内核中用于提供随机数据的特殊文件 | 由硬件随机源提供高质量熵 | A |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | 已用于常见实现，例如通过 [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers) 配置的 [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom)。 | A |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2)，也可用于 [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) 和 [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) | 通过简洁的 API 直接从内核熵源获取安全随机字节。该接口较为现代，可避免旧式 API 的常见问题。 | A |

HMAC-DRBG 或 Hash-DRBG 使用的底层哈希函数必须是本标准认可用于此用途的函数。

## 加密算法

本节为 V11.3
加密算法提供补充说明。

下表按优先顺序列出本标准认可的加密算法。

| 对称密钥算法 | 参考资料 | 状态 |
|--|--|--|
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

### AES 加密模式

AES 等分组密码可采用不同的工作模式。电子密码本（ECB）等许多模式并不安全，严禁使用。伽罗瓦/计数器模式（GCM）和带 CBC-MAC 的计数器模式（CCM）可提供认证加密，应在现代应用中使用。

下表按优先顺序列出本标准认可的工作模式。

| 模式 | 是否认证 | 参考资料 | 状态 | 限制 |
|--|--|--|--|--|
| GCM | 是 | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A | |
| CCM | 是 | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A | |
| CBC | 否 | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | L | |
| CCM-8 | 是 | | D | |
| ECB | 否 | | D | |
| CFB | 否 | | D | |
| OFB | 否 | | D | |
| CTR | 否 | | D | |

说明：

* 所有加密消息都必须经过认证。使用任何 CBC 模式时，都必须同时使用基于哈希的 MAC 算法验证消息。通常必须采用先加密后哈希（Encrypt-Then-Hash）的方式，但 TLS 1.2 使用先哈希后加密（Hash-Then-Encrypt）。如果无法满足这一要求，则不得使用 CBC。仅磁盘加密允许在不使用 MAC 算法的情况下进行加密。
* 使用 CBC 时，必须确保以恒定时间完成填充验证。
* 使用 CCM-8 时，MAC 标签仅提供 64 位安全强度，不符合要求 6.2.9 中至少 128 位安全强度的规定。
* 磁盘加密不在 ASVS 的范围内，因此本附录未列出本标准认可的磁盘加密方法。此类场景通常允许使用不带认证的加密，并普遍采用 XTS、XEX 和 LRW 模式。

### 密钥封装

密码学密钥封装（以及相应的密钥解封）是指使用额外的加密机制封装现有密钥，使原始密钥在传输等过程中不会直接暴露。用于保护原始密钥的附加密钥称为封装密钥。

当需要在不可信位置保护密钥，或通过不可信网络及应用内部传输敏感密钥时，可以使用此操作。
不过，在决定执行封装或解封前，应认真考虑并理解原始密钥的属性，例如身份和用途。这项操作可能影响源系统、目标系统或应用的安全性，尤其会影响合规性，包括密钥功能（如签名）的审计记录以及适当的密钥存储方式。

密钥封装必须使用 AES-256，并遵循 [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final)，同时为未来的量子计算威胁做好准备。下表按优先顺序列出基于 AES 的加密模式：

| 密钥封装 | 参考资料 | 状态 |
|--|--|--|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |

如果使用场景确有需要，可以使用 AES-192 和 AES-128，但必须在组织的密码学清单中记录使用理由。

### 认证加密

除磁盘加密外，加密数据必须使用某种认证加密（AE）方案防止未经授权的篡改，通常采用带关联数据的认证加密（AEAD）方案。

应用应优先使用本标准认可的 AEAD 方案，也可以将本标准认可的加密方案与本标准认可的 MAC 算法组合，并采用先加密后计算 MAC（Encrypt-then-MAC）的结构。

为兼容遗留应用，仍允许使用先计算 MAC 后加密（MAC-then-encrypt）。TLS v1.2 的旧密码套件采用了这种方式。

| AEAD 机制 | 参考资料 | 状态 |
|--------------------------|---------|-----|
|AES-GCM | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A |
|AES-CCM  | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A |
|ChaCha-Poly1305 | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539) | A |
|AEGIS-256 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128L| [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|Encrypt-then-MAC | | A |
|MAC-then-encrypt | | L |

## 哈希函数

本节为 V11.4
哈希和基于哈希的函数提供补充说明。

### 通用场景下的哈希函数

下表列出了本标准认可用于数字签名等通用密码学场景的哈希函数：

* 本标准认可的哈希函数具有较强的抗碰撞能力，适用于高安全性应用。
* 其中部分算法配合适当的密码学密钥管理时具有较强的抗攻击能力，因此本标准也认可将其用于 HMAC、KDF 和 RBG。
* 输出长度不足 254 位的哈希函数无法提供足够的抗碰撞能力，不得用于数字签名或其他要求抗碰撞能力的场景。在其他场景中，这类函数只能用于遗留系统的兼容和验证，不得用于新的设计。

| 哈希函数 | 参考资料 | 状态 | 限制 |
| -------------- | ------------------------------------------------------------- |--|--|
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
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | 不适用于 HMAC、KDF、RBG 和数字签名 |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | 不适用于 HMAC、KDF、RBG 和数字签名 |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | L | 不适用于 HMAC、KDF、RBG 和数字签名 |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L | 不适用于 HMAC、KDF、RBG 和数字签名 |
| CRC（任意长度） |  | D |  |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) | D | |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D | |

### 用于密码存储的哈希函数

为安全地对密码进行哈希处理，必须使用专用的哈希函数。这类慢速哈希算法会增加破解密码所需的计算量，从而降低暴力破解和字典攻击的风险。

| KDF | 参考资料 | 参数要求 | 状态 |
| --- | --------- | ------------------- | ------ |
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
| | | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
| | | t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A |
| scrypt | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
| | | p = 2: N ≥ 2^16 (64 MiB), r = 8 | A |
| | | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8 | A |
| bcrypt | [一种面向未来、可调整的密码方案](https://www.researchgate.net/publication/2519476_A_Future-Adaptable_Password_Scheme) | cost ≥ 10 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次数 ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次数 ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次数 ≥ 1,300,000 | L |

本标准认可的基于密码的密钥派生函数可用于存储密码。

## 密钥派生函数（KDF）

### 通用密钥派生函数

| KDF              | 参考资料                                                                                      | 状态 |
| ---------------- | --------------------------------------------------------------------------------------------- | ------ |
| HKDF             | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                           | A      |
| TLS 1.2 PRF      | [RFC 5248](https://www.rfc-editor.org/info/rfc5248)                                           | L      |
| 基于 MD5 的 KDF  | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                           | D      |
| 基于 SHA-1 的 KDF | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | D      |

### 基于密码的密钥派生函数

| KDF | 参考资料 | 参数要求 | 状态 |
| --- | --------- | ------------------- | ------ |
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
| | | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
| scrypt | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
| | | p = 2: N ≥ 2^16 (64 MiB), r = 8 | A |
| | | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次数 ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次数 ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次数 ≥ 1,300,000 | L |

## 密钥交换机制

本节为 V11.6
公钥密码学提供补充说明。

### 密钥交换方案

所有密钥交换方案必须达到至少 112 位的安全强度，并按照下表选择实现参数。

| 方案 | 域参数 | 前向保密 | 状态 |
|--|--|--|--|
| 有限域 Diffie-Hellman（FFDH） | L >= 3072 & N >= 256 | 是 | A |
| 椭圆曲线 Diffie-Hellman（ECDH） | f >= 256-383 | 是 | A |
| 使用 RSA-PKCS#1 v1.5 的加密密钥传输 | | 否 | D |

其中，各参数含义如下：

* k 表示 RSA 密钥的长度。
* 在有限域密码学中，L 表示公钥长度，N 表示私钥长度。
* f 表示 ECC 密钥长度的范围。

任何新实现都不得使用不符合 [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final)、[NIST SP 800-56B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) 和 [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final) 的方案。尤其不得在生产环境中使用 IKEv1。

### Diffie-Hellman 群

本标准认可使用以下群实现 Diffie-Hellman 密钥交换。各群的安全强度记录在 [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) 附录 D 和 [NIST SP 800-57 第 1 部分修订版 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)中。

| 群               | 状态 |
|------------------|--------|
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

## 消息认证码（MAC）

消息认证码（MAC）是一种用于验证消息完整性和真实性的密码学结构。MAC 以消息和秘密密钥作为输入，生成固定长度的标签，即 MAC 值。MAC 广泛用于 TLS/SSL 等安全通信协议，以确保通信双方交换的消息真实且未被篡改。

| MAC 算法 | 参考资料                                                                                       | 状态 |
| --------------| ----------------------------------------------------------------------------------------- | -------|
| HMAC-SHA-256  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-384  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-512  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| KMAC128       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A |
| KMAC256       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A |
| BLAKE3（keyed_hash 模式） | [BLAKE3：一个可在各种环境中高效运行的函数](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf)  | A |
| AES-CMAC      | [RFC 4493](https://datatracker.ietf.org/doc/html/rfc4493) & [NIST SP 800-38B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf) | A |
| AES-GMAC      | [NIST SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)            | A |
| Poly1305-AES  | [The Poly1305-AES message-authentication code](https://cr.yp.to/mac/poly1305-20050329.pdf)                  | A |
| HMAC-SHA-1    | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | L |
| HMAC-MD5      | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                | D      |

## 数字签名

签名方案必须使用 [NIST SP 800-57 第 1 部分](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)认可的密钥长度和参数。

| 签名算法                       | 参考资料                                                   | 状态 |
| ------------------------------ | ---------------------------------------------------------- | ------ |
| EdDSA (Ed25519, Ed448)         | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)        | A      |
| XEdDSA (Curve25519, Curve448)  | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)   | A      |
| ECDSA (P-256, P-384, P-521)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)  | A      |
| RSA-RSSA-PSS                   | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | A      |
| RSA-SSA-PKCS#1 v1.5            | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | D      |
| DSA（任意密钥长度）            | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)  | D      |

## 后量子加密标准

由于目前经过安全加固的代码和实现参考仍然很少，PQC 实现必须符合 [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd)、[FIPS-204](https://csrc.nist.gov/pubs/fips/204/ipd) 和 [FIPS-205](https://csrc.nist.gov/pubs/fips/205/ipd)。另见：https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards

拟议的后量子混合 TLS 密钥协商方法 [mlkem768x25519](https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/03/) 已获得 [Firefox 132](https://www.mozilla.org/en-US/firefox/132.0/releasenotes/) 和 [Chrome 131](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html) 等主流浏览器支持。该方法可用于密码学测试环境，也可在业界或政府批准的密码库提供支持时使用。
