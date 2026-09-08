# الملحق ج: معايير التشفير

يتجاوز فصل "التشفير" مجرّد تحديد الممارسات الفضلى. فهو يهدف إلى تعزيز فهم مبادئ التشفير والتشجيع على تبنّي طرائق أمنية أكثر صمودًا وحداثة. ويوفّر هذا الملحق معلومات تقنية مفصّلة عن كل متطلب، مكمّلًا المعايير الشاملة المبيّنة في فصل "التشفير".

يحدّد هذا الملحق مستوى الاعتماد لآليات التشفير المختلفة:

* الآليات المعتمدة (A) يمكن استخدامها في التطبيقات.
* الآليات القديمة (L) لا ينبغي استخدامها في التطبيقات لكن قد تبقى مستخدمة للتوافق مع التطبيقات أو الشيفرات القديمة القائمة فقط. ومع أن استخدام هذه الآليات لا يُعدّ حاليًا ثغرة في حد ذاته، فينبغي استبدالها بآليات أكثر أمانًا وأصمد للمستقبل في أسرع وقت ممكن.
* الآليات الممنوعة (D) يجب ألا تُستخدم لأنها تُعدّ حاليًا مكسورة أو لا توفّر أمانًا كافيًا.

وقد تُتجاوز هذه القائمة في سياق تطبيق معيّن لأسباب متنوعة منها:

* التطورات الجديدة في مجال التشفير؛
* الامتثال للتنظيمات.

## جرد التشفير وتوثيقه

يوفّر هذا القسم معلومات إضافية
عن V11.1 جرد التشفير وتوثيقه.

من المهم التأكد من أن جميع الأصول التشفيرية، مثل الخوارزميات والمفاتيح والشهادات، تُستكشف وتُجرد وتُقيَّم بانتظام. وبالنسبة إلى المستوى 3، ينبغي أن يشمل ذلك استخدام الفحص الساكن والديناميكي لاستكشاف استخدام التشفير في التطبيق. وقد تساعد أدوات مثل SAST وDAST في ذلك، لكن من المحتمل أن تكون هناك حاجة إلى أدوات مخصّصة للحصول على تغطية أشمل. ومن أمثلة الأدوات المجانية:

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

## القوى المكافئة لمعاملات التشفير

ترد القوى الأمنية النسبية لأنظمة تشفير متنوعة في هذا الجدول (من [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)، ص. 71):

| القوة الأمنية | خوارزميات المفتاح المتناظر | الحقل المنتهي | تحليل الأعداد الصحيحة إلى عوامل | المنحنى الإهليلجي |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA   | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

أمثلة على التطبيقات:

* تشفير الحقل المنتهي: DSA وFFDH وMQV
* تشفير تحليل الأعداد الصحيحة إلى عوامل: RSA
* تشفير المنحنيات الإهليلجية: ECDSA وEdDSA وECDH وMQV

ملاحظة: يفترض هذا القسم عدم وجود حاسوب كمومي؛ فإذا وُجد مثل هذا الحاسوب، فلن تبقى التقديرات في الأعمدة الثلاثة الأخيرة صالحة.

## القيم العشوائية

يوفّر هذا القسم معلومات إضافية
عن V11.5 القيم العشوائية.

| الاسم | الإصدار/المرجع | ملاحظات | الحالة |
|:---|:----|:----|:-:|
| `/dev/random` | Linux 4.8+ [(Oct 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3), also found in iOS, Android, and other Linux-based POSIX operating systems. Based on [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) | Utilizing ChaCha20 stream. Found in iOS [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) and Android [`Secure Random`](https://developer.android.com/reference/java/security/SecureRandom) with the correct settings provided to each. | A |
| `/dev/urandom` | Linux kernel's special file for providing random data | Provides high-quality, entropy sources from hardware randomness | A |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | As used in common implementations, such as [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) set by [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers). | A |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2), available in [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) and [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) | Provides secure random bytes directly from the kernel's entropy source with a straightforward and minimal API. It’s more modern and avoids pitfalls associated with older APIs. | A |

يجب أن تكون دالة التلبيد الأساسية المستخدمة مع HMAC-DRBG أو Hash-DRBG معتمدة لهذا الاستخدام.

## خوارزميات التشفير

يوفّر هذا القسم معلومات إضافية
عن V11.3 خوارزميات التشفير.

خوارزميات التشفير المعتمدة مدرجة بترتيب التفضيل.

| خوارزميات المفتاح المتناظر | المرجع | الحالة |
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

### أنماط تشفير AES

يمكن استخدام تشفيرات الكتل، مثل AES، مع أنماط تشغيل مختلفة. وكثير من أنماط التشغيل، مثل كتاب الشيفرة الإلكتروني (ECB)، غير آمن ويجب ألا يُستخدم. أما نمط جالوا/العدّاد (GCM) ونمط العدّاد مع رمز مصادقة رسالة تسلسل كتل التشفير (CCM) فيوفّران تشفيرًا مصادَقًا عليه وينبغي استخدامهما في التطبيقات الحديثة.

الأنماط المعتمدة مدرجة بترتيب التفضيل.

| النمط | مصادَق عليه | المرجع | الحالة | القيد |
|--|--|--|:-:|--|
| GCM | Yes | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A | |
| CCM | Yes | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A | |
| CBC | No | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | L | |
| CCM-8 | Yes | | D | |
| ECB | No | | D | |
| CFB | No | | D | |
| OFB | No | | D | |
| CTR | No | | D | |

ملاحظات:

* يجب أن تكون جميع الرسائل المشفّرة مصادَقًا عليها. ولأي استخدام لنمط CBC يجب أن تكون هناك خوارزمية MAC تلبيدية مرتبطة به للتحقق من الرسالة. وعمومًا، يجب تطبيق ذلك بطريقة التشفير ثم التلبيد (لكن TLS 1.2 يستخدم التلبيد ثم التشفير بدلًا من ذلك). وإذا لم يكن من الممكن ضمان ذلك، فيجب ألا يُستخدم CBC. والتطبيق الوحيد الذي يُسمح فيه بالتشفير دون خوارزمية MAC هو تشفير الأقراص.
* في حال استخدام CBC، يجب ضمان أن التحقق من الحشو يُنفَّذ في زمن ثابت.
* عند استخدام CCM-8، لا تمتلك وسيمة MAC سوى 64 بتًا من الأمان. وهذا لا يتوافق مع المتطلب 6.2.9 الذي يقتضي 128 بتًا من الأمان على الأقل.
* يُعدّ تشفير الأقراص خارج نطاق معيار التحقق من أمان التطبيقات. ولذلك لا يُدرج هذا الملحق أي طريقة معتمدة لتشفير الأقراص. ولهذا الاستخدام، يُقبل عادةً التشفير دون مصادقة وتُستخدم عادةً الأنماط XTS وXEX وLRW.

### تغليف المفاتيح

تغليف المفاتيح التشفيري (وما يقابله من فك التغليف) طريقة لحماية مفتاح قائم بتغليفه (أي تطويقه) باستخدام آلية تشفير إضافية بحيث لا يكون المفتاح الأصلي مكشوفًا بجلاء، مثلًا أثناء النقل. ويُشار إلى هذا المفتاح الإضافي المستخدم لحماية المفتاح الأصلي بمفتاح التغليف.

وقد تُنفَّذ هذه العملية عندما يكون من المرغوب حماية المفاتيح في أماكن تُعدّ غير موثوقة، أو إرسال مفاتيح حساسة عبر شبكات غير موثوقة أو داخل التطبيقات.
لكن ينبغي إيلاء اعتبار جدّي لفهم طبيعة المفتاح الأصلي (مثل هويته والغرض منه) قبل الإقدام على إجراء تغليف/فك تغليف، إذ قد تكون لذلك تبعات على الأنظمة أو التطبيقات المصدر والهدف على حد سواء من حيث الأمان، وخصوصًا الامتثال، الذي قد يشمل مسارات تدقيق لوظيفة المفتاح (مثل التوقيع) وكذلك التخزين الملائم للمفاتيح.

وعلى وجه التحديد، يجب استخدام AES-256 لتغليف المفاتيح، وفقًا لـ [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) ومع مراعاة الأحكام الاستشرافية ضد التهديد الكمومي. وأنماط التشفير التي تستخدم AES هي التالية، بترتيب التفضيل:

| تغليف المفاتيح | المرجع | الحالة |
|--|--|:-:|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |

ويمكن استخدام AES-192 وAES-128 إذا اقتضت حالة الاستخدام ذلك، لكن يجب توثيق مبرّر ذلك في جرد التشفير الخاص بالجهة.

### التشفير المصادَق عليه

باستثناء تشفير الأقراص، يجب حماية البيانات المشفّرة من التعديل غير المصرَّح به باستخدام صورة ما من مخططات التشفير المصادَق عليه (AE)، وعادةً باستخدام مخطط التشفير المصادَق عليه مع البيانات المرتبطة (AEAD).

وينبغي للتطبيق أن يستخدم مخطط AEAD معتمدًا تفضيلًا. وقد يجمع بدلًا من ذلك بين مخطط تشفير معتمد وخوارزمية MAC معتمدة ببنية التشفير ثم MAC.

ولا يزال التلبيد ثم التشفير مسموحًا به للتوافق مع التطبيقات القديمة. وهو مستخدم في TLS v1.2 مع مجموعات التشفير القديمة.

| آلية AEAD | المرجع | الحالة |
|---|---------|:-:|
|AES-GCM | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A |
|AES-CCM  | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A |
|ChaCha-Poly1305 | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539) | A |
|AEGIS-256 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128L| [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|Encrypt-then-MAC | | A |
|MAC-then-encrypt | | L |

## دوالّ التلبيد

يوفّر هذا القسم معلومات إضافية
عن V11.4 التلبيد والدوالّ المبنية على التلبيد.

### دوالّ التلبيد لحالات الاستخدام العامة

يسرد الجدول التالي دوالّ التلبيد المعتمدة في حالات الاستخدام التشفيري العامة مثل التوقيعات الرقمية:

* توفّر دوالّ التلبيد المعتمدة مقاومة قوية للتصادم وهي ملائمة للتطبيقات عالية الأمان.
* توفّر بعض هذه الخوارزميات مقاومة قوية للهجمات عند استخدامها مع إدارة سليمة لمفاتيح التشفير، ولذلك فهي معتمدة إضافةً إلى ذلك لدوالّ HMAC وKDF وRBG.
* دوالّ التلبيد التي يقل طول مخرَجها عن 254 بتًا لا تمتلك مقاومة كافية للتصادم ويجب ألا تُستخدم للتوقيع الرقمي أو غيره من التطبيقات التي تقتضي مقاومة التصادم. أما للاستخدامات الأخرى، فقد تُستخدم للتوافق والتحقق مع الأنظمة القديمة فقط، لكن يجب ألا تُستخدم في التصاميم الجديدة.

| دالة التلبيد | المرجع | الحالة | القيود |
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
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Not suitable for HMAC, KDF, RBG, digital signatures |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Not suitable for HMAC, KDF, RBG, digital signatures |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | L | Not suitable for HMAC, KDF, RBG, digital signatures |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L | Not suitable for HMAC, KDF, RBG, digital signatures |
| CRC (any length) |  | D |  |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) | D | |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D | |

### دوالّ التلبيد لتخزين كلمات المرور

لتلبيد كلمات المرور بأمان، يجب استخدام دوالّ تلبيد مخصّصة. وتخفّف خوارزميات التلبيد البطيء هذه من هجمات القوة الغاشمة وهجمات القواميس بزيادة الصعوبة الحسابية لكسر كلمات المرور.

| KDF        | المرجع | المعاملات المطلوبة | الحالة |
| ---------- | --------- | ------------ |:-:|
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m >= 47104 (46 MiB), p = 1 | A |
|          |                                                     | t = 2: m >= 19456 (19 MiB), p = 1 | A |
|          |                                                     | t >= 3: m >= 12288 (12 MiB), p = 1 | A |
| scrypt   | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N >= 2^17 (128 MiB), r = 8 | A |
|          |                                                     | p = 2: N >= 2^16 (64 MiB), r = 8  | A |
|          |                                                     | p >= 3: N >= 2^15 (32 MiB), r = 8  | A |
| bcrypt | [A Future-Adaptable Password Scheme](https://www.researchgate.net/publication/2519476_A_Future-Adaptable_Password_Scheme) | cost >= 10 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations >= 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations >= 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations >= 1,300,000 | L |

ويمكن استخدام دوالّ اشتقاق المفاتيح المعتمدة القائمة على كلمات المرور لتخزين كلمات المرور.

## دوالّ اشتقاق المفاتيح (KDFs)

### دوالّ اشتقاق المفاتيح العامة

| KDF              | المرجع                                                                                        | الحالة |
| ---------------- | -------- |:-:|
| HKDF             | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                           | A      |
| TLS 1.2 PRF      | [RFC 5248](https://www.rfc-editor.org/info/rfc5248)                                           | L      |
| MD5-based KDFs   | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                           | D      |
| SHA-1-based KDFs | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | D      |

### دوالّ اشتقاق المفاتيح القائمة على كلمات المرور

| KDF        | المرجع | المعاملات المطلوبة | الحالة |
| ---------- | --------- | ------------ |:-:|
| argon2id   | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m >= 47104 (46 MiB), p = 1 | A |
|            |                                                     | t = 2: m >= 19456 (19 MiB), p = 1 | A |
| scrypt     | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N >= 2^17 (128 MiB), r = 8 | A |
|            |                                                     | p = 2: N >= 2^16 (64 MiB), r = 8  | A |
|            |                                                     | p >= 3: N >= 2^15 (32 MiB), r = 8  | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations >= 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations >= 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations >= 1,300,000 | L |

## آليات تبادل المفاتيح

يوفّر هذا القسم معلومات إضافية
عن V11.6 تشفير المفتاح العام.

### مخططات تبادل المفاتيح

يجب ضمان قوة أمنية قدرها 112 بتًا أو أكثر لجميع مخططات تبادل المفاتيح، ويجب أن يتّبع تنفيذها اختيارات المعاملات الواردة في الجدول التالي.

| المخطط | معاملات المجال | السرّية التامة للتوجيه |الحالة |
|--|--|--|:-:|
| Finite Field Diffie-Hellman (FFDH) | L >= 3072 & N >= 256 | Yes | A |
| Elliptic Curve Diffie-Hellman (ECDH) | f >= 256-383 | Yes | A |
| Encrypted key transport with RSA-PKCS#1 v1.5 | | No | D |

حيث المعاملات التالية هي:

* k هو حجم المفتاح لمفاتيح RSA.
* L هو حجم المفتاح العام وN هو حجم المفتاح الخاص لتشفير الحقل المنتهي.
* f هو نطاق أحجام المفاتيح لتشفير المنحنيات الإهليلجية (ECC).

ويجب ألا يستخدم أي تنفيذ جديد أي مخطط غير متوافق مع [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) و[B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) و[NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final). وعلى وجه التحديد، يجب ألا يُستخدم IKEv1 في الإنتاج.

### مجموعات ديفي-هيلمان

المجموعات التالية معتمدة لتنفيذات تبادل المفاتيح بطريقة ديفي-هيلمان. والقوى الأمنية موثّقة في [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final)، الملحق د، وفي [NIST SP 800-57 Part 1 Rev.5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| المجموعة         | الحالة |
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

## رموز مصادقة الرسائل (MAC)

رموز مصادقة الرسائل (MACs) بِنى تشفيرية تُستخدم للتحقق من سلامة الرسالة وأصالتها. ويأخذ رمز MAC رسالة ومفتاحًا سرّيًا كمدخلات وينتج وسيمة ثابتة الحجم (قيمة MAC). وتُستخدم رموز MAC على نطاق واسع في بروتوكولات الاتصال الآمن (مثل TLS/SSL) لضمان أن الرسائل المتبادلة بين الأطراف أصيلة وسليمة.

| خوارزمية MAC | المرجع                                                                                    | الحالة |
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

## التوقيعات الرقمية

يجب أن تستخدم مخططات التوقيع أحجام مفاتيح ومعاملات معتمدة وفق [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| خوارزمية التوقيع               | المرجع                                                     | الحالة |
| ------------------------------ | ---------------------------------------------              | :-:    |
| EdDSA (Ed25519, Ed448)         | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)        | A      |
| XEdDSA (Curve25519, Curve448)  | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)   | A      |
| ECDSA (P-256, P-384, P-521)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)  | A      |
| RSA-RSSA-PSS                   | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | A      |
| RSA-SSA-PKCS#1 v1.5            | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | D      |
| DSA (any key size)             | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)  | D      |

## معايير التشفير ما بعد الكمومي

يجب أن تكون تنفيذات التشفير ما بعد الكمومي متوافقة مع [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd)/[204](https://csrc.nist.gov/pubs/fips/204/ipd)/[205](https://csrc.nist.gov/pubs/fips/205/ipd) إذ لا يوجد بعد سوى قدر ضئيل من الشيفرات المحصّنة أو المراجع التنفيذية. https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards

طريقة اتفاق المفاتيح الهجينة ما بعد الكمومية المقترحة [mlkem768x25519](https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/03/) لـ TLS مدعومة من متصفحات رئيسية مثل [Firefox release 132](https://www.mozilla.org/en-US/firefox/132.0/releasenotes/) و[Chrome release 131](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html). ويمكن استخدامها في بيئات الاختبار التشفيري أو عند توافرها في مكتبات معتمدة صناعيًا أو حكوميًا.
