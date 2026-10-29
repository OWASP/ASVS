# 附錄 C：密碼學標準

「密碼學」章節不僅定義了最佳實務，還旨在幫助讀者深入理解密碼學原理，並推動採用更具韌性的現代安全方法。本附錄針對各項要求提供詳細的技術說明，作為「密碼學」章節總體標準的補充。

本附錄將密碼機制分為以下使用級別：

* 可用（A）：本標準認可，可在應用中使用。
* 遺留（L）：不應在應用中使用，僅可用於相容現有的遺留應用或程式碼。目前使用此類機制本身不被視為弱點，但應盡快替換為更安全、能夠適應未來需求的機制。
* 禁止（D）：不得使用，因為這類機制目前已被攻破，或無法提供足夠的安全性。

在具體應用中，可能需要基於多種原因調整此清單，包括：

* 密碼學領域出現新的發展；
* 滿足法規要求。

## 密碼資產清單和文件

本節提供補充說明，
適用於 V11.1 密碼資產清單和文件。

應定期發現、盤點和評估演算法、金鑰及憑證等所有密碼學資產。對於第 3 級，還應通過靜態和動態掃描，識別應用中的密碼學使用情況。SAST 和 DAST 工具可以提供幫助，但要實作更全面的覆蓋，可能還需要使用專用工具。可免費使用的工具示例包括：

* [CryptoMon：使用 eBPF、以 Python 編寫的網路密碼學監控工具](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge：根據 CodeQL 輸出生成完整的 CBOM](https://github.com/Santandersecurityresearch/cryptobom-forge)

## 密碼學參數的等效安全強度

下表列出了不同密碼學系統的相對安全強度（摘自 [NIST SP 800-57 第 1 部分](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)第 71 頁）：

| 安全強度 | 對稱金鑰演算法 | 有限域 | 整數分解 | 橢圓曲線 |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA   | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

應用示例：

* 有限域密碼學：DSA、FFDH、MQV
* 整數分解密碼學：RSA
* 橢圓曲線密碼學：ECDSA、EdDSA、ECDH、MQV

注意：本節以不存在可用的量子電腦為前提。如果此類電腦成為現實，後三列的估算將不再有效。

## 隨機值

本節提供補充說明，
適用於 V11.5 隨機值。

| 名稱 | 版本/參考資料 | 說明 | 狀態 |
|:-:|:-:|:-:|:-:|
| `/dev/random` | Linux 4.8+ [（2016 年 10 月）](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3)，也存在於 iOS、Android 和其他基於 Linux 的 POSIX 作業系統中。基於 [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) | 使用 ChaCha20 流。在正確組態的情況下，可通過 iOS 的 [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) 和 Android 的 [`SecureRandom`](https://developer.android.com/reference/java/security/SecureRandom) 使用。 | A |
| `/dev/urandom` | Linux 核心中用於提供隨機資料的特殊檔案 | 由硬體隨機源提供高品質熵 | A |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | 已用於常見實作，例如通過 [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers) 組態的 [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom)。 | A |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2)，也可用於 [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) 和 [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) | 通過簡潔的 API 直接從核心熵源獲取安全隨機位元組。該介面較為現代，可避免舊式 API 的常見問題。 | A |

HMAC-DRBG 或 Hash-DRBG 使用的底層雜湊函數必須是本標準認可用於此用途的函數。

## 加密演算法

本節提供補充說明，
適用於 V11.3 加密演算法。

下表按優先順序列出本標準認可的加密演算法。

| 對稱金鑰演算法 | 參考資料 | 狀態 |
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

AES 等區塊密碼可採用不同的工作模式。電子密碼本（ECB）等許多模式並不安全，嚴禁使用。伽羅瓦/計數器模式（GCM）和帶 CBC-MAC 的計數器模式（CCM）可提供具驗證性的加密，應在現代應用中使用。

下表按優先順序列出本標準認可的工作模式。

| 模式 | 是否提供訊息鑑別 | 參考資料 | 狀態 | 限制 |
|--|--|--|--|--|
| GCM | 是 | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A | |
| CCM | 是 | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A | |
| CBC | 否 | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | L | |
| CCM-8 | 是 | | D | |
| ECB | 否 | | D | |
| CFB | 否 | | D | |
| OFB | 否 | | D | |
| CTR | 否 | | D | |

說明：

* 所有加密訊息都必須經過訊息鑑別。使用任何 CBC 模式時，都必須同時使用基於雜湊的 MAC 演算法驗證訊息。通常必須採用先加密後雜湊（Encrypt-Then-Hash）的方式，但 TLS 1.2 使用先雜湊後加密（Hash-Then-Encrypt）。如果無法滿足這一要求，則不得使用 CBC。僅磁碟加密允許在不使用 MAC 演算法的情況下進行加密。
* 使用 CBC 時，必須確保以恆定時間完成填補驗證。
* 使用 CCM-8 時，MAC 標籤僅提供 64 位元安全強度，不符合要求 11.2.3 中至少 128 位元安全強度的規定。
* 磁碟加密不在 ASVS 的範圍內，因此本附錄未列出本標準認可的磁碟加密方法。此類場景通常允許使用不具驗證性的加密，並普遍採用 XTS、XEX 和 LRW 模式。

### 金鑰封裝

密碼學金鑰封裝（以及相應的金鑰解封）是指使用額外的加密機制封裝現有金鑰，使原始金鑰在傳輸等過程中不會直接暴露。用於保護原始金鑰的附加金鑰稱為封裝金鑰。

當需要在不可信位置保護金鑰，或通過不可信網路及應用內部傳輸敏感金鑰時，可以使用此操作。
不過，在決定執行封裝或解封前，應認真考慮並理解原始金鑰的屬性，例如身分和用途。這項操作可能影響源系統、目標系統或應用的安全性，尤其會影響合規性，包括金鑰功能（如簽章）的稽核記錄以及適當的金鑰儲存方式。

金鑰封裝必須使用 AES-256，並遵循 [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final)，同時為未來的量子運算威脅做好準備。下表按優先順序列出基於 AES 的加密模式：

| 金鑰封裝 | 參考資料 | 狀態 |
|--|--|--|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |

如果使用場景確有需要，可以使用 AES-192 和 AES-128，但必須在組織的密碼學清單中記錄使用理由。

### 具驗證性的加密

除磁碟加密外，加密資料必須使用某種具驗證性的加密（AE）方案防止未經授權的篡改，通常採用帶關聯資料的具驗證性的加密（AEAD）方案。

應用應優先使用本標準認可的 AEAD 方案，也可以將本標準認可的加密方案與本標準認可的 MAC 演算法組合，並採用先加密後計算 MAC（Encrypt-then-MAC）的結構。

為相容遺留應用，仍允許使用先計算 MAC 後加密（MAC-then-encrypt）。TLS v1.2 的舊密碼套件採用了這種方式。

| AEAD 機制 | 參考資料 | 狀態 |
|--------------------------|---------|-----|
|AES-GCM | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A |
|AES-CCM  | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A |
|ChaCha-Poly1305 | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539) | A |
|AEGIS-256 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128L| [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|Encrypt-then-MAC | | A |
|MAC-then-encrypt | | L |

## 雜湊函數

本節提供補充說明，
適用於 V11.4 雜湊和基於雜湊的函數。

### 通用場景下的雜湊函數

下表列出了本標準認可用於數位簽章等通用密碼學場景的雜湊函數：

* 本標準認可的雜湊函數具有較強的抗碰撞能力，適用於高安全性應用。
* 其中部分演算法配合適當的密碼學金鑰管理時具有較強的抗攻擊能力，因此本標準也認可將其用於 HMAC、KDF 和 RBG。
* 輸出長度不足 254 位元的雜湊函數無法提供足夠的抗碰撞能力，不得用於數位簽章或其他要求抗碰撞能力的場景。在其他場景中，這類函數只能用於遺留系統的相容和驗證，不得用於新的設計。

| 雜湊函數 | 參考資料 | 狀態 | 限制 |
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
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | 不適用於 HMAC、KDF、RBG 和數位簽章 |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | 不適用於 HMAC、KDF、RBG 和數位簽章 |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | L | 不適用於 HMAC、KDF、RBG 和數位簽章 |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L | 不適用於 HMAC、KDF、RBG 和數位簽章 |
| CRC（任意長度） |  | D |  |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) | D | |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D | |

### 用於密碼儲存的雜湊函數

為安全地對密碼進行雜湊處理，必須使用專用的雜湊函數。這類慢速雜湊演算法會增加破解密碼所需的計算量，從而降低暴力破解和字典攻擊的風險。

| KDF | 參考資料 | 參數要求 | 狀態 |
| --- | --------- | ------------------- | ------ |
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
| | | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
| | | t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A |
| scrypt | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
| | | p = 2: N ≥ 2^16 (64 MiB), r = 8 | A |
| | | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8 | A |
| bcrypt | [一種面向未來、可調整的密碼方案](https://www.researchgate.net/publication/2519476_A_Future-Adaptable_Password_Scheme) | cost ≥ 10 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次數 ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次數 ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次數 ≥ 1,300,000 | L |

本標準認可的基於密碼的金鑰衍生函數可用於儲存密碼。

## 金鑰衍生函數（KDF）

### 通用金鑰衍生函數

| KDF              | 參考資料                                                                                      | 狀態 |
| ---------------- | --------------------------------------------------------------------------------------------- | ------ |
| HKDF             | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                           | A      |
| TLS 1.2 PRF      | [RFC 5248](https://www.rfc-editor.org/info/rfc5248)                                           | L      |
| 基於 MD5 的 KDF  | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                           | D      |
| 基於 SHA-1 的 KDF | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | D      |

### 基於密碼的金鑰衍生函數

| KDF | 參考資料 | 參數要求 | 狀態 |
| --- | --------- | ------------------- | ------ |
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
| | | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
| scrypt | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
| | | p = 2: N ≥ 2^16 (64 MiB), r = 8 | A |
| | | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次數 ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次數 ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final)，[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | 迭代次數 ≥ 1,300,000 | L |

## 金鑰交換機制

本節提供補充說明，
適用於 V11.6 公開金鑰密碼學。

### 金鑰交換方案

所有金鑰交換方案必須達到至少 112 位元的安全強度，並按照下表選擇實作參數。

| 方案 | 域參數 | 前向保密 | 狀態 |
|--|--|--|--|
| 有限域 Diffie-Hellman（FFDH） | L >= 3072 & N >= 256 | 是 | A |
| 橢圓曲線 Diffie-Hellman（ECDH） | f >= 256-383 | 是 | A |
| 使用 RSA-PKCS#1 v1.5 的加密金鑰傳輸 | | 否 | D |

其中，各參數含義如下：

* k 表示 RSA 金鑰的長度。
* 在有限域密碼學中，L 表示公開金鑰長度，N 表示私密金鑰長度。
* f 表示 ECC 金鑰長度的範圍。

任何新實作都不得使用不符合 [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final)、[NIST SP 800-56B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) 和 [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final) 的方案。尤其不得在正式環境中使用 IKEv1。

### Diffie-Hellman 群

本標準認可使用以下群實作 Diffie-Hellman 金鑰交換。各群的安全強度記錄在 [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) 附錄 D 和 [NIST SP 800-57 第 1 部分修訂版 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)中。

| 群               | 狀態 |
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

## 訊息鑑別碼（MAC）

訊息鑑別碼（MAC）是一種用於驗證訊息完整性和真實性的密碼學結構。MAC 以訊息和秘密金鑰作為輸入，生成固定長度的標籤，即 MAC 值。MAC 廣泛用於 TLS/SSL 等安全通訊通訊協定，以確保通訊雙方交換的訊息真實且未被篡改。

| MAC 演算法 | 參考資料                                                                                       | 狀態 |
| --------------| ----------------------------------------------------------------------------------------- | -------|
| HMAC-SHA-256  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-384  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-512  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| KMAC128       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A |
| KMAC256       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A |
| BLAKE3（keyed_hash 模式） | [BLAKE3：一個可在各種環境中高效執行的函數](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf)  | A |
| AES-CMAC      | [RFC 4493](https://datatracker.ietf.org/doc/html/rfc4493) & [NIST SP 800-38B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf) | A |
| AES-GMAC      | [NIST SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)            | A |
| Poly1305-AES  | [The Poly1305-AES message-authentication code](https://cr.yp.to/mac/poly1305-20050329.pdf)                  | A |
| HMAC-SHA-1    | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | L |
| HMAC-MD5      | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                | D      |

## 數位簽章

簽章方案必須使用 [NIST SP 800-57 第 1 部分](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)認可的金鑰長度和參數。

| 簽章演算法                       | 參考資料                                                   | 狀態 |
| ------------------------------ | ---------------------------------------------------------- | ------ |
| EdDSA (Ed25519, Ed448)         | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)        | A      |
| XEdDSA (Curve25519, Curve448)  | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)   | A      |
| ECDSA (P-256, P-384, P-521)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)  | A      |
| RSA-RSSA-PSS                   | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | A      |
| RSA-SSA-PKCS#1 v1.5            | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | D      |
| DSA（任意金鑰長度）            | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)  | D      |

## 後量子加密標準

後量子密碼學（PQC）實作應遵循 [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd)、[FIPS-204](https://csrc.nist.gov/pubs/fips/204/ipd) 和 [FIPS-205](https://csrc.nist.gov/pubs/fips/205/ipd)。目前，這些標準可用的加固程式碼示例或參考實作還不多。更多詳情見：[NIST 關於首批三項最終版後量子加密標準的公告（2024 年 8 月）](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)。

擬議的後量子混合 TLS 金鑰協商方法 [mlkem768x25519](https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/03/) 已獲得 [Firefox 132](https://www.mozilla.org/en-US/firefox/132.0/releasenotes/) 和 [Chrome 131](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html) 等主流瀏覽器支援。該方法可用於密碼學測試環境，也可在業界或政府批准的密碼學函式庫提供支援時使用。
