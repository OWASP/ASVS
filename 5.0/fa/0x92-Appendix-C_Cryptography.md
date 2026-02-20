# Appendix C: Cryptography Standards

فصل «رمزنگاری» فراتر از ارائه‌ی ساده‌ی بهترین رویه‌ها عمل می‌کند. این فصل با هدف افزایش درک اصول رمزنگاری و تشویق به به‌کارگیری روش‌های امنیتی مدرن‌تر و مقاوم‌تر تدوین شده است. این پیوست، اطلاعات فنی تفصیلی مربوط به هر یک از الزامات را ارائه می‌دهد و استانداردهای کلی مطرح‌شده در فصل «رمزنگاری» را تکمیل می‌کند.

این پیوست سطح تأیید را برای مکانیزم‌های مختلف رمزنگاری تعریف می‌کند:

* مکانیزم‌های تأییدشده (A) می‌توانند در برنامه‌ها استفاده شوند.
* مکانیزم‌های قدیمی (L) نباید در برنامه‌ها استفاده شوند، اما ممکن است فقط برای سازگاری با برنامه‌ها یا کدهای قدیمی موجود به کار روند. اگرچه استفاده از این مکانیزم‌ها در حال حاضر به خودی خود آسیب‌پذیری محسوب نمی‌شود، اما باید هرچه سریع‌تر با مکانیزم‌های امن‌تر و آینده‌نگر جایگزین شوند.
* مکانیزم‌های غیرمجاز (D) نباید استفاده شوند زیرا در حال حاضر شکسته محسوب می‌شوند یا امنیت کافی ارائه نمی‌کنند.

این فهرست ممکن است در زمینه یک برنامه خاص به دلایل مختلف لغو شود، از جمله:

* تحولات جدید در حوزه رمزنگاری؛
* رعایت مقررات و قوانین.

## Cryptographic Inventory and Documentation

این بخش اطلاعات تکمیلی را برای V11.1 موجودی و مستندسازی رمزنگاری ارائه می‌دهد.

مهم است که تمام دارایی‌های رمزنگاری، مانند الگوریتم‌ها، کلیدها و گواهی‌نامه‌ها، به‌طور منظم شناسایی، فهرست‌بندی و ارزیابی شوند. برای سطح ۳، این باید شامل استفاده از اسکن ایستا و پویا برای شناسایی استفاده از رمزنگاری در یک برنامه باشد. ابزارهایی مانند SAST و DAST می‌توانند در این زمینه کمک کنند، اما ممکن است ابزارهای اختصاصی برای پوشش جامع‌تر مورد نیاز باشند. نمونه‌های رایگان از این ابزارها عبارتند از:

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

## Equivalent Strengths of Cryptographic Parameters

قدرت‌های امنیتی نسبی برای سیستم‌های مختلف رمزنگاری در این جدول آمده است  (از [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), صفحه71):

| Security Strength | Symmetric Key Algorithms | Finite Field           | Integer Factorization | Elliptic Curve |
| ----------------- | ------------------------ | ---------------------- | --------------------- | -------------- |
| <= 80             | 2TDEA                    | L = 1024 <br> N = 160  | k = 1024              | f = 160-223    |
| 112               | 3TDEA                    | L = 2048 <br> N = 224  | k = 2048              | f = 224-255    |
| 128               | AES-128                  | L = 3072 <br> N = 256  | k = 3072              | f = 256-383    |
| 192               | AES-192                  | L = 7680 <br> N = 384  | k = 7680              | f = 384-511    |
| 256               | AES-256                  | L = 15360 <br> N = 512 | k = 15360             | f = 512+       |

نمونه‌ای از برنامه‌ها:

* رمزنگاری میدان محدود (Finite Field Cryptography):  DSA، FFDH، MQV
* رمزنگاری تجزیه عدد صحیح (Integer Factorization Cryptography):  RSA
* رمزنگاری منحنی بیضوی (Elliptic Curve Cryptography):  ECDSA، EdDSA، ECDH، MQV

توجه: این بخش فرض می‌کند که هیچ کامپیوتر کوانتومی وجود ندارد؛ اگر چنین کامپیوتری وجود داشته باشد، برآوردهای سه ستون آخر دیگر معتبر نخواهند بود.

## Random Values

این بخش اطلاعات تکمیلی برای 5 Random Values را ارائه می‌دهد.

| Name           | Version/Reference                                                                                                                                                                                                                                                                                             | Notes                                                                                                                                                                                                                                                                                                                  | Status |
|:--------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------:|
| `/dev/random`  | لینوکس 4.8 به بعد [(اکتبر 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3)، همچنین در iOS، Android و سایر سیستم‌عامل‌های POSIX مبتنی بر لینوکس یافت می‌شود. مبتنی بر[ RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539). | با استفاده از جریان ChaCha20. در iOS [(SecRandomCopyBytes)](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) و [Android Secure Random](https://developer.android.com/reference/java/security/SecureRandom) با تنظیمات صحیح مربوط به هرکدام یافت می‌شود.                    | A      |
| `/dev/urandom` | فایل ویژه هسته لینوکس برای ارائه داده‌های تصادفی                                                                                                                                                                                                                                                              | منابع آنتروپی با کیفیت بالا را از تصادفی‌بودن سخت‌افزاری فراهم می‌کند                                                                                                                                                                                                                                                  | A      |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf)                                                                                                                                                                                                                 | همان‌طور که در پیاده‌سازی‌های رایج استفاده می‌شود، مانند [API ویندوز CNG و تابع BCryptGenRandom](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) که توسط [BCRYPT_RNG_ALGORITHM](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers) تنظیم شده است. | A      |
| `HMAC-DRBG`    | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf)                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                        | A      |
| `Hash-DRBG`    | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf)                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                        | A      |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2)، در [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) و [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) در دسترس است.                                                                              | بایت‌های تصادفی امن را مستقیماً از منبع آنتروپی کرنل فراهم می‌کند و دارای یک رابط برنامه‌نویسی ساده و کم‌حجم است. این روش مدرن‌تر است و از مشکلات و محدودیت‌های مرتبط با APIهای قدیمی اجتناب می‌کند.                                                                                                                   | A      |

تابع هش زیربنایی که در HMAC-DRBG یا Hash-DRBG استفاده می‌شود، باید برای این کاربرد تأیید شده باشد.

## Cipher Algorithms

این بخش اطلاعات تکمیلی برای الگوریتم‌های رمزنگاری را ارائه می‌دهد.

الگوریتم‌های رمزنگاری تأیید شده به ترتیب اولویت فهرست شده‌اند.

| Symmetric Key Algorithms | Reference                                                                           | Status |
| ------------------------ | ----------------------------------------------------------------------------------- | ------ |
| AES-256                  | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final)                               | A      |
| Salsa20                  | [Salsa 20 specification](https://cr.yp.to/snuffle/spec.pdf)                         | A      |
| XChaCha20                | [XChaCha20 Draft](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-xchacha-03) | A      |
| XSalsa20                 | [Extending the Salsa20 nonce](https://cr.yp.to/snuffle/xsalsa-20110204.pdf)         | A      |
| ChaCha20                 | [RFC 8439](https://www.rfc-editor.org/info/rfc8439)                                 | A      |
| AES-192                  | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final)                               | A      |
| AES-128                  | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final)                               | L      |
| 2TDEA                    |                                                                                     | D      |
| TDEA (3DES/3DEA)         |                                                                                     | D      |
| IDEA                     |                                                                                     | D      |
| RC4                      |                                                                                     | D      |
| Blowfish                 |                                                                                     | D      |
| ARC4                     |                                                                                     | D      |
| DES                      |                                                                                     | D      |

### AES Cipher Modes

رمزنگاری‌های بلوکی، مانند AES، می‌توانند با حالت‌های مختلف عملیاتی استفاده شوند. بسیاری از حالت‌های عملیاتی، مانند Electronic Codebook (ECB)، ناامن هستند و نباید استفاده شوند. حالت‌های عملیاتی Galois/Counter Mode (GCM) و Counter with Cipher Block Chaining Message Authentication Code (CCM) رمزنگاری تأیید شده (Authenticated Encryption) ارائه می‌دهند و باید در برنامه‌های مدرن استفاده شوند.

حالت‌های تأیید شده به ترتیب اولویت فهرست شده‌اند.

| Mode  | Authenticated | Reference                                                            | Status | Restriction |
| ----- | ------------- | -------------------------------------------------------------------- | ------ | ----------- |
| GCM   | Yes           | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final)      | A      |             |
| CCM   | Yes           | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A      |             |
| CBC   | No            | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final)      | L      |             |
| CCM-8 | Yes           |                                                                      | D      |             |
| ECB   | No            |                                                                      | D      |             |
| CFB   | No            |                                                                      | D      |             |
| OFB   | No            |                                                                      | D      |             |
| CTR   | No            |                                                                      | D      |             |

یادداشت‌ها:

* تمام پیام‌های رمزنگاری‌شده باید احراز هویت شوند. برای هر استفاده‌ای از حالت CBC، حتماً باید یک الگوریتم هش MAC مرتبط برای اعتبارسنجی پیام وجود داشته باشد. به طور کلی، این باید با روش Encrypt-Then-Hash اعمال شود (اما TLS 1.2 به جای آن از روش Hash-Then-Encrypt استفاده می‌کند). اگر این تضمین امکان‌پذیر نباشد، نباید از CBC استفاده شود. تنها کاربردی که در آن رمزنگاری بدون الگوریتم MAC مجاز است، رمزنگاری دیسک است.
* اگر از حالت CBC استفاده شود، باید تضمین شود که بررسی پدینگ (Padding) در زمان ثابت انجام می‌شود.
* هنگام استفاده از CCM-8، برچسب MAC تنها ۶۴ بیت امنیت ارائه می‌دهد. این با الزامات بند ۶.۲.۹ که حداقل ۱۲۸ بیت امنیت را نیاز دارد، مطابقت ندارد.
* رمزنگاری دیسک خارج از محدوده ASVS در نظر گرفته شده است. بنابراین، این ضمیمه هیچ روش تأیید شده‌ای برای رمزنگاری دیسک فهرست نمی‌کند. برای این کاربرد، معمولاً رمزنگاری بدون احراز هویت پذیرفته می‌شود و حالت‌های XTS، XEX و LRW معمولاً استفاده می‌شوند.

### Key Wrapping

بسته‌بندی کلید رمزنگاری (و باز کردن بسته‌ی مربوطه) روشی برای محافظت از یک کلید موجود است که با محصور کردن (یعنی بسته‌بندی) آن و استفاده از یک مکانیزم رمزنگاری اضافی انجام می‌شود تا کلید اصلی به‌طور آشکار در معرض دید قرار نگیرد، مثلاً هنگام انتقال. کلید اضافی که برای محافظت از کلید اصلی استفاده می‌شود، کلید بسته‌بندی (wrap key) نامیده می‌شود.

این عملیات ممکن است زمانی انجام شود که بخواهیم کلیدها را در مکان‌هایی که قابل اعتماد نیستند محافظت کنیم، یا کلیدهای حساس را از طریق شبکه‌های غیرقابل اعتماد یا درون برنامه‌ها ارسال کنیم.
 با این حال، باید با دقت به ماهیت کلید اصلی (مانند هویت و هدف آن) قبل از انجام فرآیند بسته‌بندی/بازکردن بسته توجه شود، زیرا این می‌تواند برای سیستم‌ها یا برنامه‌های مبدأ و مقصد پیامدهایی در زمینه امنیت و به ویژه تطابق قانونی داشته باشد، که ممکن است شامل مسیرهای حسابرسی عملکرد کلید (مانند امضا) و همچنین ذخیره‌سازی مناسب کلید باشد.

به‌طور مشخص، برای بسته‌بندی کلید باید از AES-256 استفاده شود، مطابق با [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) و با در نظر گرفتن تمهیدات آینده‌نگر در برابر تهدید کوانتومی. حالت‌های رمزنگاری استفاده‌شده با AES به ترتیب اولویت به شرح زیر هستند:

| Key Wrapping | Reference                                                       | Status |
| ------------ | --------------------------------------------------------------- | ------ |
| KW           | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A      |
| KWP          | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A      |

در صورتی که مورد استفاده نیاز داشته باشد، می‌توان از AES-192 و AES-128 نیز استفاده کرد، اما دلیل استفاده از آن‌ها باید در فهرست رمزنگاری موجود در سازمان مستندسازی شود.

### Authenticated Encryption

به استثنای رمزنگاری دیسک، داده‌های رمزنگاری‌شده باید در برابر تغییرات غیرمجاز با استفاده از نوعی از طرح رمزنگاری احراز هویت‌شده (AE) محافظت شوند، که معمولاً از طرح رمزنگاری احراز هویت‌شده با داده‌های مرتبط (AEAD) استفاده می‌شود.

بهتر است برنامه از یک طرح AEAD تأیید شده استفاده کند. به طور جایگزین، می‌تواند یک طرح رمزنگاری تأیید شده و یک الگوریتم MAC تأیید شده را با ساختار Encrypt-then-MAC ترکیب کند.

روش MAC-then-encrypt همچنان برای سازگاری با برنامه‌های قدیمی مجاز است. این روش در TLS نسخه ۱.۲ با مجموعه‌های رمزنگاری قدیمی استفاده می‌شود.

| AEAD mechanism   | Reference                                                                                                    | Status |
| ---------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| AES-GCM          | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final)                                                   | A      |
| AES-CCM          | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final)                                              | A      |
| ChaCha-Poly1305  | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539)                                                    | A      |
| AEGIS-256        | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A      |
| AEGIS-128        | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A      |
| AEGIS-128L       | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A      |
| Encrypt-then-MAC |                                                                                                              | A      |
| MAC-then-encrypt |                                                                                                              | L      |

## Hash Functions

این بخش اطلاعات تکمیلی در مورد هش کردن و توابع مبتنی بر هش را ارائه می‌دهد.

### Hash Functions for General Use Cases

جدول زیر توابع هش تأیید شده برای کاربردهای عمومی رمزنگاری، مانند امضاهای دیجیتال، را فهرست می‌کند:

* توابع هش تأیید شده مقاومت بالایی در برابر برخورد (collision) دارند و برای برنامه‌های با امنیت بالا مناسب هستند.
* برخی از این الگوریتم‌ها وقتی همراه با مدیریت صحیح کلیدهای رمزنگاری استفاده شوند، مقاومت بالایی در برابر حملات ارائه می‌دهند و بنابراین برای توابع HMAC، KDF و RBG نیز تأیید شده‌اند.
* توابع هش با خروجی کمتر از ۲۵۴ بیت مقاومت کافی در برابر برخورد (collision) ندارند و نباید برای امضاهای دیجیتال یا سایر کاربردهایی که نیاز به مقاومت در برابر برخورد دارند، استفاده شوند. برای سایر کاربردها، ممکن است تنها برای سازگاری و اعتبارسنجی با سیستم‌های قدیمی استفاده شوند، اما نباید در طراحی‌های جدید به کار روند.

| Hash function    | Reference                                                                                                 | Status | Restrictions                                     |
| ---------------- | --------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------------------ |
| SHA3-512         | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)                                                     | A      |                                                  |
| SHA-512          | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)                                            | A      |                                                  |
| SHA3-384         | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)                                                     | A      |                                                  |
| SHA-384          | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)                                            | A      |                                                  |
| SHA3-256         | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)                                                     | A      |                                                  |
| SHA-512/256      | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)                                            | A      |                                                  |
| SHA-256          | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)                                            | A      |                                                  |
| SHAKE256         | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)                                                     | A      |                                                  |
| BLAKE2s          | [BLAKE2: simpler, smaller, fast as MD5](https://eprint.iacr.org/2013/322)                                 | A      |                                                  |
| BLAKE2b          | [BLAKE2: simpler, smaller, fast as MD5](https://eprint.iacr.org/2013/322)                                 | A      |                                                  |
| BLAKE3           | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf) | A      |                                                  |
| SHA-224          | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)                                            | L      | مناسب برای HMAC، KDF، RBG و امضاهای دیجیتال نیست |
| SHA-512/224      | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)                                            | L      | مناسب برای HMAC، KDF، RBG و امضاهای دیجیتال نیست |
| SHA3-224         | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)                                                     | L      | مناسب برای HMAC، KDF، RBG و امضاهای دیجیتال نیست |
| SHA-1            | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L      | مناسب برای HMAC، KDF، RBG و امضاهای دیجیتال نیست |
| CRC (any length) |                                                                                                           | D      |                                                  |
| MD4              | [RFC 1320](https://www.rfc-editor.org/info/rfc1320)                                                       | D      |                                                  |
| MD5              | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                                       | D      |                                                  |

### Hash Functions for Password Storage

برای هش کردن امن گذرواژه‌ها، باید از توابع هش مخصوص استفاده شود. این الگوریتم‌های هش کند، با افزایش سختی محاسباتی شکستن گذرواژه، حملات جستجوی فراگیر (brute-force) و دیکشنری را کاهش می‌دهند.

| KDF                 | Reference                                                                                                                      | Required Parameters                                                                                      | Status |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ------ |
| argon2id            | [RFC 9106](https://www.rfc-editor.org/info/rfc9106)                                                                            | t = 1: m ≥ 47104 (46 MiB), p = 1<br>t = 2: m ≥ 19456 (19 MiB), p = 1<br>t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A      |
| scrypt              | [RFC 7914](https://www.rfc-editor.org/info/rfc7914)                                                                            | p = 1: N ≥ 2^17 (128 MiB), r = 8<br>p = 2: N ≥ 2^16 (64 MiB), r = 8<br>p ≥ 3: N ≥ 2^15 (32 MiB), r = 8   | A      |
| bcrypt              | [A Future-Adaptable Password Scheme](https://www.researchgate.net/publication/2519476_A_Future-Adaptable_Password_Scheme)      | cost ≥ 10                                                                                                | A      |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 210,000                                                                                     | A      |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 600,000                                                                                     | A      |
| PBKDF2-HMAC-SHA-1   | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 1,300,000                                                                                   | L      |

توابع استخراج کلید مبتنی بر گذرواژه (Password-Based Key Derivation Functions) تأیید شده می‌توانند برای ذخیره‌سازی گذرواژه استفاده شوند.

## Key Derivation Functions (KDFs)

### General Key Derivation Functions

| KDF              | Reference                                                                                                 | Status |
| ---------------- | --------------------------------------------------------------------------------------------------------- | ------ |
| HKDF             | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                                       | A      |
| TLS 1.2 PRF      | [RFC 5248](https://www.rfc-editor.org/info/rfc5248)                                                       | L      |
| MD5-based KDFs   | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                                       | D      |
| SHA-1-based KDFs | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | D      |

### Password-based Key Derivation Functions

| KDF                 | Reference                                                                                                                      | Required Parameters                                                                                      | Status |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ------ |
| argon2id            | [RFC 9106](https://www.rfc-editor.org/info/rfc9106)                                                                            | t = 1: m ≥ 47104 (46 MiB), p = 1<br>t = 2: m ≥ 19456 (19 MiB), p = 1<br>t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A      |
| scrypt              | [RFC 7914](https://www.rfc-editor.org/info/rfc7914)                                                                            | p = 1: N ≥ 2^17 (128 MiB), r = 8<br>p = 2: N ≥ 2^16 (64 MiB), r = 8<br>p ≥ 3: N ≥ 2^15 (32 MiB), r = 8   | A      |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 210,000                                                                                     | A      |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 600,000                                                                                     | A      |
| PBKDF2-HMAC-SHA-1   | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 1,300,000                                                                                   | L      |

## Key Exchange Mechanisms

این بخش اطلاعات تکمیلی رمزنگاری کلید عمومی را ارائه می‌دهد.

### KEX Schemes

برای همه طرح‌های تبادل کلید باید قدرت امنیتی ۱۱۲ بیت یا بیشتر تضمین شود و پیاده‌سازی آن‌ها باید از انتخاب پارامترهای موجود در جدول زیر پیروی کند.

| Scheme                                       | Domain Parameters    | Forward Secrecy | Status |
| -------------------------------------------- | -------------------- | --------------- | ------ |
| Finite Field Diffie-Hellman (FFDH)           | L >= 3072 & N >= 256 | Yes             | A      |
| Elliptic Curve Diffie-Hellman (ECDH)         | f >= 256-383         | Yes             | A      |
| Encrypted key transport with RSA-PKCS#1 v1.5 |                      | No              | D      |

که پارامترهای زیر عبارتند از:

* k اندازه کلید برای کلیدهای RSA است.
* L اندازه کلید عمومی و N اندازه کلید خصوصی برای رمزنگاری بر مبنای میدان محدود است.
* f محدوده اندازه‌های کلید برای ECC است.

هیچ پیاده‌سازی جدیدی نباید از طرحی استفاده کند که با استانداردهای [NIST SP 800-56A & B](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) و [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final) مطابقت نداشته باشد. به طور مشخص، IKEv1 نباید در محیط‌های تولیدی استفاده شود.

### Diffie-Hellman groups

گروه‌های زیر برای پیاده‌سازی Diffie-Hellman تأیید شده‌اند. قدرت‌های امنیتی در ضمیمه D استاندارد [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) و [بخش ۱ نسخه ۵ استاندارد NIST SP 800-57](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) مستند شده‌اند.

| Group            | Status |
| ---------------- | ------ |
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

## Message Authentication Codes (MAC)

کدهای احراز هویت پیام (MAC) سازه‌های رمزنگاری هستند که برای بررسی صحت و اصالت یک پیام استفاده می‌شوند. یک MAC یک پیام و یک کلید مخفی را به عنوان ورودی می‌گیرد و یک برچسب با اندازه ثابت (مقدار MAC) تولید می‌کند. MACها به طور گسترده در پروتکل‌های ارتباطی امن (مانند TLS/SSL) استفاده می‌شوند تا اطمینان حاصل شود که پیام‌های تبادل‌شده بین طرفین معتبر و دست‌نخورده هستند.

| MAC Algorithm            | Reference                                                                                                                                                | Status | Restrictions |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------ |
| HMAC-SHA-256             | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final)                                          | A      |              |
| HMAC-SHA-384             | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final)                                          | A      |              |
| HMAC-SHA-512             | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final)                                          | A      |              |
| KMAC128                  | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                                                                                           | A      |              |
| KMAC256                  | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                                                                                           | A      |              |
| BLAKE3 (keyed_hash mode) | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf)                                                | A      |              |
| AES-CMAC                 | [RFC 4493](https://datatracker.ietf.org/doc/html/rfc4493) & [NIST SP 800-38B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf) | A      |              |
| AES-GMAC                 | [NIST SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)                                                         | A      |              |
| Poly1305-AES             | [The Poly1305-AES message-authentication code](https://cr.yp.to/mac/poly1305-20050329.pdf)                                                               | A      |              |
| HMAC-SHA-1               | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final)                                          | L      |              |
| HMAC-MD5                 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                                                                                      | D      |              |

## Digital Signatures

طرح‌های امضا باید از اندازه‌ها و پارامترهای کلید تأیید شده مطابق با [NIST SP 800-57 بخش ۱](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) استفاده کنند.

| Signature Algorithm           | Reference                                                 | Status |
| ----------------------------- | --------------------------------------------------------- | ------ |
| EdDSA (Ed25519, Ed448)        | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)       | A      |
| XEdDSA (Curve25519, Curve448) | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)  | A      |
| ECDSA (P-256, P-384, P-521)   | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final) | A      |
| RSA-RSSA-PSS                  | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)       | A      |
| RSA-SSA-PKCS#1 v1.5           | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)       | D      |
| DSA (any key size)            | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final) | D      |

## Post-Quantum Encryption Standards

پیاده‌سازی‌های رمزنگاری پساکوانتومی (PQC) باید از استانداردهای [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd)، [FIPS-204](https://csrc.nist.gov/pubs/fips/204/ipd) و [FIPS-205](https://csrc.nist.gov/pubs/fips/205/ipd) پیروی کنند. در حال حاضر، نمونه‌های کد مقاوم یا پیاده‌سازی‌های مرجع زیادی برای این استانداردها در دسترس نیست. برای جزئیات بیشتر، به [اعلامیه NIST درباره سه استاندارد نهایی‌شده رمزنگاری پساکوانتومی (اوت ۲۰۲۴) مراجعه کنید.](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)

روش پیشنهادی [mlkem768x25519](https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/03/) برای توافق کلید هیبریدی TLS پساکوانتومی توسط مرورگرهای اصلی مانند [Firefox نسخه ۱۳۲](https://www.mozilla.org/en-US/firefox/132.0/releasenotes/) و [Chrome نسخه ۱۳۱](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html) پشتیبانی می‌شود. این روش می‌تواند در محیط‌های آزمایشی رمزنگاری یا زمانی که در کتابخانه‌های تأیید شده توسط صنعت یا دولت در دسترس است، استفاده شود.
