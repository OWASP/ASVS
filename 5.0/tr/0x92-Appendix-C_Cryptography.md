# Ek C: Kriptografi Standartları

“Kriptografi” bölümü sadece en iyi uygulamaları tanımlamanın ötesine geçmektedir. Kriptografi ilkelerinin daha iyi anlaşılmasını ve daha esnek, modern güvenlik yöntemlerinin benimsenmesini teşvik etmeyi amaçlamaktadır. Bu ek, “Kriptografi” bölümünde ana hatlarıyla belirtilen kapsayıcı standartları tamamlayan her bir gereklilikle ilgili ayrıntılı teknik bilgi sağlamaktadır.

Bu ek, farklı kriptografik mekanizmalar için onay seviyesini tanımlar:

* Onaylanmış (A) mekanizmalar uygulamalarda kullanılabilir.
* Eski (Legacy) mekanizmalar (L) uygulamalarda kullanılmamalıdır, ancak yine de yalnızca mevcut eski uygulamalar veya kodlarla uyumluluk için kullanılabilir. Bu tür mekanizmaların kullanımı şu anda kendi başına bir güvenlik açığı olarak kabul edilmese de, mümkün olan en kısa sürede daha güvenli ve geleceğe dönük mekanizmalarla değiştirilmelidir.
* İzin verilmeyen (Disallowed) mekanizmalar (D) şu anda bozuk kabul edildikleri veya yeterli güvenlik sağlamadıkları için kullanılmamalıdır.

Bu liste, belirli bir uygulama bağlamında, aşağıdakiler de dahil olmak üzere çeşitli nedenlerle geçersiz kılınabilir:

* kriptografi alanındaki yeni gelişmeler;
* yönetmeliklere uygunluk.

## Kriptografik Envanter ve Dokümantasyon

Bu bölüm V11.1 Kriptografik Envanter
ve Dokümantasyon için ek bilgi sağlamaktadır.

Algoritmalar, anahtarlar ve sertifikalar gibi tüm kriptografik varlıkların düzenli olarak keşfedildiğinden, envanterinin çıkarıldığından ve değerlendirildiğinden emin olmak önemlidir. Seviye 3 için bu, bir uygulamada kriptografi kullanımını keşfetmek için statik ve dinamik tarama kullanımını içermelidir. SAST ve DAST gibi araçlar bu konuda yardımcı olabilir, ancak daha geniş bir kapsam elde etmek için özel araçlara ihtiyaç duyulması mümkündür. Ücretsiz araç örnekleri şunları içerir:

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

## Kriptografik Parametrelerin Eşdeğer Güçleri

Çeşitli kriptografik sistemler için göreceli güvenlik güçleri bu tabloda yer almaktadır: [NIST SP 800-57 Kısım 1, syf.71](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)

| Güvenlik Gücü | Simetrik Anahtar Algoritmaları | Sonlu Alan | Tamsayı Çarpanlarına Ayırma | Eliptik Eğri (Elliptic Curve) |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA   | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

Uygulama örnekleri şunlardır:

* Sonlu Alan Kriptografisi (Finite Field Cryptography): DSA, FFDH, MQV
* Tamsayı Çarpanlarına Ayırma Kriptografisi (Integer Factorization Cryptography): RSA
* Eliptik Eğri Kriptografisi (Elliptic Curve Cryptography): ECDSA, EdDSA, ECDH, MQV

Not: Bu bölümde kuantum bilgisayarlarının var olmadığı varsayılmaktadır. Eğer böyle bir bilgisayar var olsaydı, son 3 sütun için yapılan tahminler artık geçerli olmazdı.

## Rastgele Değerler

Bu bölümde V11.5 Rastgele Değerler
için ek bilgi sağlanmaktadır.

| İsim | Sürüm/Referans | Notlar | Durum |
|:---|:----|:----|:-:|
| `/dev/random` | Linux 4.8+ [(Oct 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3), , iOS, Android ve diğer Linux tabanlı POSIX işletim sistemlerinde de bulunur. [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) temel alınmıştır. | ChaCha20 akışını kullanır. iOS [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) ve Android [`Secure Random`](https://developer.android.com/reference/java/security/SecureRandom) içinde her biri için sağlanan doğru ayarlarla bulunur.| A |
| `/dev/urandom` | Linux çekirdeğinin rastgele veri sağlamak için özel dosyası | Donanım rastgeleliğinden gelen yüksek kaliteli, entropi kaynakları sağlar | A |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) gibi yaygın uygulamalarda kullanıldığı gibi, [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers) tarafından ayarlanır. | A |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2), [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) ve [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) sürümlerinde mevcuttur. | Doğrudan çekirdeğin entropi kaynağından basit ve minimal bir API ile güvenli rastgele baytlar sağlar. Daha moderndir ve eski API'lerle ilişkili tuzaklardan kaçınır. | A |

HMAC-DRBG veya Hash-DRBG ile kullanılan temel hash fonksiyonu, bu kullanım için onaylanmış olmalıdır.

## Şifre (Cipher) Algoritmaları

Bu bölüm V11.3 Şifreleme Algoritmaları
için ek bilgi sağlar.

Onaylanan şifre algoritmaları tercih sırasına göre listelenmiştir.

| Simetrik Anahtar Algoritmaları | Referans | Durum |
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

### AES Şifre Modları

AES gibi blok şifreler farklı işlem modları ile kullanılabilir. Elektronik kod kitabı (Electronic codebook - ECB) gibi birçok işlem modu güvensizdir ve kullanılmamalıdır. Galois/Counter Modu (Galois/Counter Mode - GCM) ve şifre blok zincirleme mesaj kimlik doğrulama kodlu Sayaç (CCM) işlem modları, kimliği doğrulanmış şifreleme sağlar ve modern uygulamalarda kullanılmalıdır.

Onaylanan modlar tercih sırasına göre listelenmiştir.

| Mod | Kimliği Doğrulanmış | Referans | Durum | Kısıtlama |
|--|--|--|--|--|
| GCM | Evet | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A | |
| CCM | Evet | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A | |
| CBC | Hayır | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | L | |
| CCM-8 | Evet | | D | |
| ECB | Hayır | | D | |
| CFB | Hayır | | D | |
| OFB | Hayır | | D | |
| CTR | Hayır | | D | |

Notlar:

* Tüm şifrelenmiş mesajların kimliği doğrulanmalıdır. CBC modunun herhangi bir kullanımı için, mesajı doğrulamak üzere ilişkili bir karma MAC algoritması olmalıdır. Genel olarak bu, Encrypt-Then-Hash yönteminde uygulanmalıdır (ancak TLS 1.2 bunun yerine Hash-Then-Encrypt kullanır). Eğer bu garanti edilemiyorsa, CBC kullanılmamalıdır. MAC algoritması olmadan şifrelemeye izin verilen tek uygulama disk şifrelemedir.
* Eğer CBC kullanıldıysa, padding doğrulanmasının sabit zamanda gerçekleştirildiği garanti edilmelidir.
* CCM-8 kullanıldığında, MAC etiketi yalnızca 64 bit güvenliğe sahiptir. Bu, en az 128 bit güvenlik gerektiren gereksinim 6.2.9 ile uyumlu değildir.
* Disk şifrelemenin ASVS için kapsam dışı olduğu düşünülmektedir. Bu nedenle bu ekte disk şifreleme için onaylanmış herhangi bir yöntem listelenmemiştir. Bu kullanım için, kimlik doğrulama olmadan şifreleme genellikle kabul edilir ve XTS, XEX ve LRW modları tipik olarak kullanılır.

### Anahtar Sarma (Key Wrapping)

Kriptografik anahtar sarma (ve buna karşılık gelen anahtar açma), mevcut bir anahtarı ek bir şifreleme mekanizması kullanarak kapsülleyerek (yani sararak) koruma yöntemidir. Böylece orijinal anahtar, örneğin bir aktarım sırasında açıkça ortaya çıkmaz. Orijinal anahtarı korumak için kullanılan bu ek anahtar sarma anahtarı (wrap key) olarak adlandırılır.

Bu işlem, güvenilmez olduğu düşünülen yerlerdeki anahtarları korumak veya hassas anahtarları güvenilmeyen ağlar üzerinden ya da uygulamalar içinde göndermek istendiğinde gerçekleştirilebilir.
Ancak, bir sarma/açma prosedürüne girişmeden önce orijinal anahtarın doğasını (örn. kimliği ve amacı) anlamaya ciddi önem verilmelidir, çünkü bunun hem kaynak hem de hedef sistemler/uygulamalar için güvenlik ve özellikle de bir anahtarın işlevinin (örn. imzalama) denetim izlerini ve uygun anahtar depolamayı içerebilecek uyumluluk açısından yansımaları olabilir.

Özellikle, [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) uyarınca ve kuantum tehdidine karşı ileriye dönük hükümler göz önünde bulundurularak, anahtar sarma için AES-256 kullanılmalıdır. AES kullanan şifre modları tercih sırasına göre şunlardır:

| Anahtar Sarma | Referans | Durum |
|--|--|--|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |

Kullanım durumu gerektiriyorsa AES-192 ve AES-128 kullanılabilir. Ancak bunun sebebi ve amacı, kuruluşun kriptografi envanterinde belgelenmelidir.

### Kimlik Doğrulamalı Şifreleme

Disk şifreleme haricinde, şifrelenmiş veriler bir çeşit kimliği doğrulanmış şifreleme (authenticated encryption - AE) şeması kullanılarak, genellikle ilişkili verilerle kimliği doğrulanmış şifreleme (authenticated encryption with associated data - AEAD) şeması kullanılarak yetkisiz değişikliklere karşı korunmalıdır.

Uygulama tercihen onaylı bir AEAD şeması kullanmalıdır. Alternatif olarak onaylı bir şifreleme şeması ile onaylı bir MAC algoritmasını bir Encrypt-then-MAC yapısıyla birleştirebilir.

MAC-then-encrypt'e eski uygulamalarla uyumluluk için hala izin verilmektedir. TLS v1.2'de eski şifre takımları ile kullanılır.

| AEAD mekanizması | Referans | Durum |
|---|---------|:-:|
|AES-GCM | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A |
|AES-CCM  | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A |
|ChaCha-Poly1305 | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539) | A |
|AEGIS-256 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128L| [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|Encrypt-then-MAC | | A |
|MAC-then-encrypt | | L |

## Hash Fonksiyonları

Bu bölümde V11.4 Hashing ve Hash Tabanlı Fonksiyonlar
için ek bilgiler sağlanmaktadır.

### Genel Kullanım Durumları için Hash Fonksiyonları

Aşağıdaki tabloda, dijital imzalar gibi genel kriptografik kullanım durumlarında onaylanan hash fonksiyonları listelenmektedir:

* Onaylanan hash fonksiyonları güçlü çakışma (collision) direnci sağlar ve yüksek güvenlikli uygulamalar için uygundur.
* Bu algoritmalardan bazıları uygun kriptografik anahtar yönetimi ile kullanıldığında saldırılara karşı güçlü direnç sunar ve bu nedenle HMAC, KDF ve RBG işlevleri için ek olarak onaylanmıştır.
* 254 bitten daha az çıktıya sahip hash fonksiyonların çakışma direnci yetersizdir ve dijital imza veya çakışma direnci gerektiren diğer uygulamalar için kullanılmamalıdır. Diğer kullanımlar için, sadece eski sistemlerle uyumluluk ve doğrulama için kullanılabilirler, ancak yeni tasarımlarda kullanılmamalıdırlar.

| Hash fonksiyonu | Referans | Durum | Kısıtlamalar |
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
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | HMAC, KDF, RBG, dijital imzalar için uygun değildir. |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | HMAC, KDF, RBG, dijital imzalar için uygun değildir. |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | L | HMAC, KDF, RBG, dijital imzalar için uygun değildir. |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L | HMAC, KDF, RBG, dijital imzalar için uygun değildir. |
| CRC (herhangi bir uzunluk) |  | D |  |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) | D | |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D | |

### Parola Saklama için Hash Fonksiyonları

Güvenli parola hashleme için özel hash fonksiyonları kullanılmalıdır. Bu yavaş hash algoritmaları, parola kırmanın hesaplama zorluğunu artırarak kaba kuvvet ve sözlük saldırılarını azaltır.

| KDF | Referans | Gerekli Parametreler | Durum |
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

Parola depolama için onaylı parola tabanlı anahtar türetme işlevleri kullanılabilir.

## Anahtar Türetme İşlevleri (Key Derivation Functions - KDF)

### Genel Anahtar Türetme Fonksiyonları

| KDF              | Referanslar                                                                                     | Durum |
| ---------------- | -------- |:-:|
| HKDF             | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                           | A      |
| TLS 1.2 PRF      | [RFC 5248](https://www.rfc-editor.org/info/rfc5248)                                           | L      |
| MD5-based KDFs   | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                           | D      |
| SHA-1-based KDFs | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | D      |

### Parola Tabanlı Anahtar Türetme İşlevleri

| KDF | Referans | Gerekli Parametreler | Durum |
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

## Anahtar Değişim Mekanizmaları (Key Exchange Mechanisms - KEX)

Bu bölümde V11.6 Açık Anahtar Kriptografisi
için ek bilgi sağlanmaktadır.

### KEX Şemaları

Tüm anahtar değişimi şemaları için 112 bit veya üzeri bir güvenlik gücü sağlanmalıdır ve bunların uygulanması aşağıdaki tablodaki parametre seçeneklerini takip etmelidir.

| Şema | Etki Alanı Parametreleri | İleriye Yönelik Gizlilik | Durum |
|--|--|--|:-:|
| Finite Field Diffie-Hellman (FFDH) | L >= 3072 & N >= 256 | Evet | A |
| Elliptic Curve Diffie-Hellman (ECDH) | f >= 256-383 | Evet | A |
| Encrypted key transport with RSA-PKCS#1 v1.5 | | Hayır | D |

Parametreler aşağıdaki gibidir:

* k, RSA anahtarları için anahtar boyutudur.
* L açık anahtarın boyutu ve N sonlu alan kriptografisi için özel anahtarın boyutudur.
* f, ECC için anahtar boyutları aralığıdır.

Herhangi bir yeni uygulama [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) & [B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) ve [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final) ile uyumlu OLMAYAN herhangi bir şema kullanılmamalıdır. Özellikle, IKEv1 üretimde kullanılmamalıdır.

### Diffie-Hellman Grupları

Aşağıdaki gruplar Diffie-Hellman anahtar değişimi uygulamaları için onaylanmıştır. Güvenlik güçleri [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final), Ek D ve [NIST SP 800-57 Bölüm 1 Rev.5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)'de belgelenmiştir.

| Group            | Status |
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

## Mesaj Kimlik Doğrulama Kodları (Message Authentication Codes - MAC)

Mesaj Kimlik Doğrulama Kodları (MAC), bir mesajın bütünlüğünü ve gerçekliğini doğrulamak için kullanılan kriptografik yapılardır. Bir MAC, girdi olarak bir mesaj ve gizli bir anahtar alır ve sabit boyutlu bir etiket (MAC değeri) üretir. MAC'ler güvenli iletişim protokollerinde (örneğin TLS/SSL) taraflar arasında değiş tokuş edilen mesajların gerçek ve bozulmamış olmasını sağlamak için yaygın olarak kullanılır.

| MAC Algoritması | Referans                                                                                | Durum |
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

## Dijital İmzalar

İmza şemaları [NIST SP 800-57 Bölüm 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) uyarınca onaylanmış anahtar boyutlarını ve parametrelerini kullanmalıdır.

| İmza Algoritması               | Referans                                                   | Durum  |
| ------------------------------ | ---------------------------------------------              | :-:    |
| EdDSA (Ed25519, Ed448)         | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)        | A      |
| XEdDSA (Curve25519, Curve448)  | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)   | A      |
| ECDSA (P-256, P-384, P-521)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)  | A      |
| RSA-RSSA-PSS                   | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | A      |
| RSA-SSA-PKCS#1 v1.5            | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | D      |
| DSA (any key size)             | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)  | D      |

## Kuantum Sonrası Şifreleme Standartları

Kuantum sonrası kriptografi (PQC) uygulamaları [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd), [FIPS-204](https://csrc.nist.gov/pubs/fips/204/ipd) ve [FIPS-205](https://csrc.nist.gov/pubs/fips/205/ipd) standartlarını takip etmelidir. Şu anda, bu standartlar için çok fazla güçlendirilmiş kod örneği veya referans uygulaması mevcut değildir. Daha fazla ayrıntı için, [Kuantum sonrası şifreleme standartlarının ilk üçüne ilişkin NIST duyurusu (Ağustos 2024)](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) adresine bakın.

Önerilen [mlkem768x25519](https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/03/) kuantum sonrası hibrit TLS anahtar anlaşma yöntemi [Firefox sürüm 132](https://www.mozilla.org/en-US/firefox/132.0/releasenotes/) ve [Chrome sürüm 131](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html) gibi büyük tarayıcılar tarafından desteklenmektedir. Kriptografik test ortamlarında veya endüstri veya devlet onaylı kütüphanelerde mevcut olduğunda kullanılabilir.
