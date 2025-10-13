# Приложение C: Стандарты криптографии

Глава «Криптография» выходит за рамки простого описания передовых практик. Она направлена ​​на углубление понимания принципов криптографии и поощрение внедрения более надёжных и современных методов безопасности. В этом приложении представлена ​​подробная техническая информация по каждому требованию, дополняющая общие стандарты, изложенные в главе «Криптография».

В этом приложении определяются уровни допустимости различных криптографических механизмов:

* Допустимые механизмы (A) могут использоваться в приложениях.
* Устаревшие механизмы (L) не должны использоваться в приложениях, но могут использоваться только для обеспечения совместимости с существующими устаревшими приложениями или кодом. Хотя использование таких механизмов в настоящее время само по себе не считается уязвимостью, их следует как можно скорее заменить более безопасными и перспективными механизмами.
* Запрещенные механизмы (D) не должны использоваться, поскольку в настоящее время они считаются ненадежными или не обеспечивают достаточной безопасности.

Этот список может быть переопределен в контексте конкретного приложения по разным причинам, включая:

* новые разработки в области криптографии;
* соблюдение нормативных требований.

## Инвентаризация и документирование криптографии

В этом разделе представлена ​​дополнительная информация
для V11.1 «Инвентаризация и документирование криптографии».

Важно обеспечить регулярное обнаружение, инвентаризацию и оценку всех криптографических активов, таких как алгоритмы, ключи и сертификаты. Для уровня 3 это должно включать статическое и динамическое сканирование для обнаружения использования криптографии в приложении. Такие инструменты, как SAST и DAST, могут помочь в этом, но для более полного охвата могут потребоваться специализированные инструменты. Примеры бесплатных инструментов:

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

## Эквивалентная стойкость криптографических параметров

Относительные уровни безопасности различных криптографических систем приведены в следующей таблице (из [NIST SP 800-57 Часть 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), стр.71):

| Количество бит стойкости | Симметричные алгоритмы | Конечное поле | Целочисленная факторизация | Эллиптическая кривая |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA   | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

Примеры применения:

* Криптография на конечных полях: DSA, FFDH, MQV
* Криптография на целочисленной факторизации: RSA
* Криптография на эллиптических кривых: ECDSA, EdDSA, ECDH, MQV

Примечание: в этом разделе предполагается, что квантового компьютера не существует; если бы такой компьютер существовал, оценки для последних трех столбцов стали бы недействительными.

## Случайные значения

В этом разделе представлена ​​дополнительная информация
для V11.5 «Случайные значения».

| Имя | Версия/Ссылка | Примечания | Статус |
|:-:|:-:|:-:|:-:|
| `/dev/random` | Linux 4.8+ [(Окт 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3), также встречается в iOS, Android и других операционных системах POSIX на базе Linux. Основан на [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) | Использование ChaCha20. Найдено в iOS [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) и Android [`Secure Random`](https://developer.android.com/reference/java/security/SecureRandom) с правильными настройками, предоставленными для каждого. | A |
| `/dev/urandom` | Специальный файл ядра Linux для предоставления случайных данных | Обеспечивает высококачественный источник энтропии на основе аппаратной случайности. | A |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | Используется в распространенных реализациях, таких как [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) при установке [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers). | A |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2), доступный в [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) и [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) | Обеспечивает безопасный доступ к случайным байтам непосредственно из источника энтропии ядра с помощью простого и минималистичного API. Он более современный и позволяет избежать ошибок, связанных со старыми API. | A |

Базовая хэш-функция, используемая с HMAC-DRBG или Hash-DRBG, должна быть допустима для такого применения.

## Алгоритмы шифрования

В этом разделе представлена ​​дополнительная информация
для V11.3 «Алгоритмы шифрования».

Допустимые алгоритмы шифрования перечислены в порядке предпочтения.

| Симметричные алгоритмы | Ссылка | Статус |
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

### Режимы шифрования AES

Блочные шифры, такие как AES, могут использоваться в различных режимах работы. Многие режимы работы, такие как Electronic codebook (ECB), небезопасны и не должны использоваться. Режимы работы Galois/Counter Mode (GCM) и «Счётчик с кодом аутентификации сообщений цепочки блоков шифра» (CCM) обеспечивают аутентифицированное шифрование и должны использоваться в современных приложениях.

Допустимые режимы перечислены в порядке предпочтения.

| Режим | Поддержка аутентификации | Ссылка | Статус | Ограничение |
|--|--|--|--|--|
| GCM | Yes | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A | |
| CCM | Yes | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A | |
| CBC | No | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | L | |
| CCM-8 | Yes | | D | |
| ECB | No | | D | |
| CFB | No | | D | |
| OFB | No | | D | |
| CTR | No | | D | |

Примечания:

* Все зашифрованные сообщения должны быть аутентифицированы. Для ЛЮБОГО использования режима CBC ОБЯЗАТЕЛЬНО должен быть соответствующий алгоритм хеширования MAC для проверки сообщения. Как правило, он ДОЛЖЕН применяться в методе «Шифрование-затем-хеширование» (но в TLS 1.2 вместо этого используется «Хеширование-затем-шифрование»). Если это невозможно гарантировать, то CBC НЕ ДОЛЖЕН использоваться. Единственной опцией, где разрешено шифрование без алгоритма MAC, является шифрование диска.
* При использовании CBC должно быть гарантировано, что проверка заполнения выполняется за константное время.
* При использовании CCM-8 тег MAC имеет только 64 бита стойкости. Это не соответствует требованию 6.2.9, которое требует не менее 128 бит стойкости.
* Шифрование диска считается выходящим за рамки ASVS. Поэтому в данном приложении не перечислены какие-либо утверждённые методы шифрования диска. В этом случае обычно допускается шифрование без аутентификации, и обычно используются режимы XTS, XEX и LRW.

### Шифрование ключей

Шифрование ключей (и соответствующее расшифрование ключей) — это метод защиты существующего ключа путём его инкапсуляции с использованием дополнительного механизма шифрования, чтобы исходный ключ не был явно раскрыт, например, во время передачи. Этот дополнительный ключ, используемый для защиты исходного ключа, называется ключом обёртывания (wrap key).

В частности, для шифрования ключей ОБЯЗАТЕЛЬНО должен использоваться алгоритм AES-256, соответствующий [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) и с учётом перспективных мер защиты от квантовых угроз. Режимы шифрования с использованием AES применяются в следующем порядке предпочтения:

| Шифрование ключа | Ссылка | Статус |
|--|--|--|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |

AES-192 и AES-128 МОГУТ использоваться, если того требует сценарий использования, но обоснование этого ДОЛЖНО быть задокументировано в реестре криптографии организации.

### Аутентифицированное шифрование

За исключением шифрования диска, зашифрованные данные должны быть защищены от несанкционированного изменения с использованием какой-либо схемы аутентифицированного шифрования (AE), обычно с использованием схемы аутентифицированного шифрования с соответствующими данными (AEAD).

Предпочтительно, чтобы приложение использовало утверждённую схему AEAD. В качестве альтернативы, оно может комбинировать утверждённую схему шифрования и утверждённый алгоритм MAC с конструкцией Encrypt-then-MAC.

MAC-then-encrypt по-прежнему разрешен для совместимости со старыми приложениями. Он используется в TLS версии 1.2 со старыми наборами шифров.

| Схема AEAD | Ссылка | Статус
|--------------------------|---------|-----|
|AES-GCM | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A
|AES-CCM  | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A
|ChaCha-Poly1305 | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539) | A
|AEGIS-256 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A
|AEGIS-128 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A
|AEGIS-128L| [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A
|Encrypt-then-MAC | | A
|MAC-then-encrypt | | L

## Хэш-функции

В этом разделе представлена ​​дополнительная информация
для V11.4 «Хеширование и функции на основе хеширования».

### Основные случаи использования хэш функций

В следующей таблице перечислены хэш-функции, допустимые для основных случаев использования криптографии, таких как цифровые подписи:

* Допустимые хеш-функции обеспечивают высокую устойчивость к коллизиям и подходят для приложений с высоким уровнем безопасности.
* Некоторые из этих алгоритмов обеспечивают высокую устойчивость к атакам при использовании с надлежащим управлением криптографическими ключами, поэтому они дополнительно допустимы для функций HMAC, KDF и RBG.
* Хэш-функции с длиной выходного значения менее 254 бит обладают недостаточной устойчивостью к коллизиям и не должны использоваться для цифровой подписи или других приложений, требующих устойчивости к коллизиям. В других случаях они могут использоваться ТОЛЬКО для обеспечения совместимости и верификации с устаревшими системами, но не должны использоваться в новых разработках.

| Хэш-функция | Ссылка | Статус | Ограничения |
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
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Not suitable for HMAC, KDF, RBG, digital signatures |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Not suitable for HMAC, KDF, RBG, digital signatures |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | L | Not suitable for HMAC, KDF, RBG, digital signatures |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L | Not suitable for HMAC, KDF, RBG, digital signatures |
| CRC (any length) |  | D |  |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) | D | |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D | |

### Хэш-функции для хранения паролей

Для безопасного хеширования паролей необходимо использовать специальные хеш-функции. Эти медленные алгоритмы хеширования снижают риск атак методом перебора и перебора по словарю, увеличивая вычислительную сложность взлома паролей.

| KDF | Ссылка | Обязательные параметры | Статус |
| --- | --------- | ------------------- | ------ |
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1<br>t = 2: m ≥ 19456 (19 MiB), p = 1<br>t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A |
| scrypt | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8<br>p = 2: N ≥ 2^16 (64 MiB), r = 8<br>p ≥ 3: N ≥ 2^15 (32 MiB), r = 8 | A |
| bcrypt | [A Future-Adaptable Password Scheme](https://www.researchgate.net/publication/2519476_A_Future-Adaptable_Password_Scheme) | cost ≥ 10 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 1,300,000 | L |

Для хранения паролей можно использовать допустимые функции формирования ключей на основе паролей.

## Функции формирования ключа (KDFs)

### Основные функции формирования ключа

| KDF              | Ссылка                                                                                        | Статус |
| ---------------- | --------------------------------------------------------------------------------------------- | ------ |
| HKDF             | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                           | A      |
| TLS 1.2 PRF      | [RFC 5248](https://www.rfc-editor.org/info/rfc5248)                                           | L      |
| MD5-based KDFs   | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                           | D      |
| SHA-1-based KDFs | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | D      |

### Функции формирования ключа на основе пароля

| KDF | Ссылка | Обязательные параметры | Статус |
| --- | --------- | ------------------- | ------ |
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1<br>t = 2: m ≥ 19456 (19 MiB), p = 1<br>t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A |
| scrypt | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8<br>p = 2: N ≥ 2^16 (64 MiB), r = 8<br>p ≥ 3: N ≥ 2^15 (32 MiB), r = 8 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 1,300,000 | L |

## Механизмы обмена ключами

В этом разделе представлена ​​дополнительная информация
для V11.6 «Криптография с публичным ключом».

### Схемы KEX

Для всех схем обмена ключами ДОЛЖНА быть обеспечена стойкость в 112 бит или выше, а их реализация ДОЛЖНА соответствовать выбору параметров, представленному в следующей таблице.

| Схема | Параметры | Прямая секретность | Статус |
|--|--|--|--|
| Диффи-Хеллман на конечных полях (FFDH) | L >= 3072 & N >= 256 | Yes | A |
| Диффи-Хеллман на эллиптических кривых (ECDH) | f >= 256-383 | Yes | A |
| Передача зашифрованного ключа с помощью RSA-PKCS#1 v1.5 | | No | D |

Где следующие параметры:

* k — длина ключа для RSA.
* L — длина открытого ключа, а N — длина закрытого ключа для криптографии на конечном поле.
* f — диапазон длин ключей для ECC.

Любая новая реализация НЕ ДОЛЖНА использовать схему, НЕ соответствующую [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) & [B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) и [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final). В частности, IKEv1 НЕ ДОЛЖЕН использоваться в промышленной среде.

### Группы Диффи-Хеллмана

Следующие группы допустимы для реализации обмена ключами Диффи-Хеллмана. Уровни безопасности описаны в [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final), Приложение D, и [NIST SP 800-57 Часть 1, Ред. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Группа           | Статус |
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

## Коды аутентификации сообщений (MAC)

Коды аутентификации сообщений (MAC) — это криптографические конструкции, используемые для проверки целостности и подлинности сообщения. MAC принимает сообщение и секретный ключ в качестве входных данных и создаёт тег фиксированного размера (значение MAC). MAC широко используется в протоколах защищённой связи (например, TLS/SSL) для обеспечения подлинности и целостности сообщений, которыми обмениваются стороны.

| Алгоритм MAC  | Ссылка                                                                                    | Статус | Ограничения  |
| --------------| ----------------------------------------------------------------------------------------- | -------| ------------ |
| HMAC-SHA-256  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A | |
| HMAC-SHA-384  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A | |
| HMAC-SHA-512  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A | |
| KMAC128       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A | |
| KMAC256       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A | |
| BLAKE3 (keyed_hash mode) | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf)  | A | |
| AES-CMAC      | [RFC 4493](https://datatracker.ietf.org/doc/html/rfc4493) & [NIST SP 800-38B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf) | A | |
| AES-GMAC      | [NIST SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)            | A | |
| Poly1305-AES  | [The Poly1305-AES message-authentication code](https://cr.yp.to/mac/poly1305-20050329.pdf)                  | A | |
| HMAC-SHA-1    | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | L | |
| HMAC-MD5      | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                | D      | |

## Цифровые подписи

Схемы подписи ДОЛЖНЫ использовать утвержденные размеры ключей и параметры согласно [NIST SP 800-57 Часть 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Алгоритм подписи               | Ссылка                                                     | Статус |
| ------------------------------ | ---------------------------------------------------------- | ------ |
| EdDSA (Ed25519, Ed448)         | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)        | A      |
| XEdDSA (Curve25519, Curve448)  | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)   | A      |
| ECDSA (P-256, P-384, P-521)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)  | A      |
| RSA-RSSA-PSS                   | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | A      |
| RSA-SSA-PKCS#1 v1.5            | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | D      |
| DSA (any key size)             | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)  | D      |

## Стандарты постквантового шифрования

Реализации постквантовой криптографии (PQC) должны соответствовать стандартам [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd), [FIPS-204](https://csrc.nist.gov/pubs/fips/204/ipd) и [FIPS-205](https://csrc.nist.gov/pubs/fips/205/ipd). В настоящее время для этих стандартов доступно не так много примеров эталонных реализаций. Подробнее см. [объявление NIST о первых трёх финализированных постквантовых стандартах шифрования (август 2024 г.)](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards).

Предлагаемый постквантовый гибридный метод согласования ключей TLS [mlkem768x25519](https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/03/) поддерживается основными браузерами, такими как [Firefox версии 132](https://www.mozilla.org/en-US/firefox/132.0/releasenotes/) и [Chrome версии 131](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html). Он может использоваться в средах тестирования криптографии или при наличии в библиотеках, допустимых отраслевыми или государственными органами.
