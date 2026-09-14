# Załącznik C: Standardy kryptograficzne

Rozdział „Kryptografia” wykracza poza samo definiowanie najlepszych praktyk. Jego celem jest pogłębienie zrozumienia zasad kryptografii oraz zachęcenie do przyjmowania bardziej odpornych, nowoczesnych metod bezpieczeństwa. Niniejszy załącznik dostarcza szczegółowych informacji technicznych dotyczących poszczególnych wymagań, uzupełniając nadrzędne standardy przedstawione w rozdziale „Kryptografia”.

Załącznik definiuje poziomy dopuszczenia różnych mechanizmów kryptograficznych:

* Mechanizmy zatwierdzone (A, approved) mogą być używane w aplikacjach.
* Mechanizmy przestarzałe (L, legacy) nie powinny być używane w aplikacjach, ale mogą być nadal stosowane wyłącznie dla zgodności z istniejącymi starszymi aplikacjami lub kodem. Choć użycie tych mechanizmów nie jest obecnie uznawane za podatność samo w sobie, powinny one zostać jak najszybciej zastąpione mechanizmami bezpieczniejszymi i przyszłościowymi.
* Mechanizmy niedozwolone (D, disallowed) nie mogą być używane, ponieważ są obecnie uznawane za złamane lub nie zapewniają wystarczającego bezpieczeństwa.

Lista ta może zostać nadpisana w kontekście danej aplikacji z różnych powodów, w tym:

* nowych postępów w dziedzinie kryptografii;
* zgodności z regulacjami.

## Inwentarz kryptograficzny i dokumentacja

Ta sekcja dostarcza dodatkowych informacji dla V11.1 Inwentarz kryptograficzny i dokumentacja.

Ważne jest zapewnienie, że wszystkie zasoby kryptograficzne — takie jak algorytmy, klucze i certyfikaty — są regularnie wykrywane, inwentaryzowane i oceniane. Dla poziomu 3 powinno to obejmować użycie skanowania statycznego i dynamicznego do wykrywania użycia kryptografii w aplikacji. Pomocne mogą być narzędzia takie jak SAST i DAST, ale możliwe, że dla pełniejszego pokrycia potrzebne będą narzędzia dedykowane. Darmowe przykłady narzędzi obejmują:

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

## Równoważne siły parametrów kryptograficznych

Względne siły bezpieczeństwa różnych systemów kryptograficznych przedstawia poniższa tabela (z [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), s. 71):

| Siła bezpieczeństwa | Algorytmy klucza symetrycznego | Ciało skończone | Faktoryzacja liczb całkowitych | Krzywa eliptyczna |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA   | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

Przykłady zastosowań:

* Kryptografia ciał skończonych: DSA, FFDH, MQV
* Kryptografia faktoryzacji liczb całkowitych: RSA
* Kryptografia krzywych eliptycznych: ECDSA, EdDSA, ECDH, MQV

Uwaga: ta sekcja zakłada, że nie istnieje komputer kwantowy; gdyby taki komputer istniał, szacunki w trzech ostatnich kolumnach przestałyby być aktualne.

## Wartości losowe

Ta sekcja dostarcza dodatkowych informacji dla V11.5 Wartości losowe.

| Nazwa | Wersja/odniesienie | Uwagi | Status |
|:---|:----|:----|:-:|
| `/dev/random` | Linux 4.8+ [(październik 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3), obecny również w iOS, Androidzie i innych systemach POSIX opartych na Linuksie. Oparty na [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) | Wykorzystuje strumień ChaCha20. Obecny w iOS w [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) oraz w Androidzie w [`Secure Random`](https://developer.android.com/reference/java/security/SecureRandom), przy poprawnych ustawieniach każdego z nich. | A |
| `/dev/urandom` | Specjalny plik jądra Linuksa dostarczający dane losowe | Zapewnia wysokiej jakości źródła entropii z losowości sprzętowej | A |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | Stosowany w popularnych implementacjach, takich jak [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) ustawiany przez [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers). | A |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2), dostępny w [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) oraz [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) | Dostarcza bezpieczne losowe bajty bezpośrednio ze źródła entropii jądra, z prostym i minimalnym API. Jest nowocześniejszy i unika pułapek związanych ze starszymi API. | A |

Bazowa funkcja skrótu używana z HMAC-DRBG lub Hash-DRBG musi być zatwierdzona do tego zastosowania.

## Algorytmy szyfrów

Ta sekcja dostarcza dodatkowych informacji dla V11.3 Algorytmy szyfrowania.

Zatwierdzone algorytmy szyfrów wymieniono w kolejności preferencji.

| Algorytmy klucza symetrycznego | Odniesienie | Status |
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

### Tryby szyfrowania AES

Szyfry blokowe, takie jak AES, mogą być używane w różnych trybach działania. Wiele trybów działania, takich jak Electronic codebook (ECB), jest niebezpiecznych i nie może być używanych. Tryby Galois/Counter Mode (GCM) oraz Counter with cipher block chaining message authentication code (CCM) zapewniają szyfrowanie uwierzytelnione i powinny być stosowane w nowoczesnych aplikacjach.

Zatwierdzone tryby wymieniono w kolejności preferencji.

| Tryb | Uwierzytelniony | Odniesienie | Status | Ograniczenie |
|--|--|--|:-:|--|
| GCM | Tak | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A | |
| CCM | Tak | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A | |
| CBC | Nie | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | L | |
| CCM-8 | Tak | | D | |
| ECB | Nie | | D | |
| CFB | Nie | | D | |
| OFB | Nie | | D | |
| CTR | Nie | | D | |

Uwagi:

* Wszystkie zaszyfrowane komunikaty muszą być uwierzytelnione. Dla KAŻDEGO użycia trybu CBC MUSI istnieć powiązany algorytm MAC oparty na funkcji skrótu, walidujący komunikat. Zasadniczo MUSI to być stosowane w metodzie Encrypt-Then-Hash (choć TLS 1.2 używa zamiast tego Hash-Then-Encrypt). Jeśli nie można tego zagwarantować, CBC NIE MOŻE być używany. Jedynym zastosowaniem, w którym dozwolone jest szyfrowanie bez algorytmu MAC, jest szyfrowanie dysków.
* Jeśli używany jest CBC, należy zagwarantować, że weryfikacja dopełnienia jest wykonywana w czasie stałym.
* Przy stosowaniu CCM-8 znacznik MAC ma jedynie 64 bity bezpieczeństwa. Nie spełnia to wymagania 11.2.3, które wymaga co najmniej 128 bitów bezpieczeństwa.
* Szyfrowanie dysków jest uznawane za pozostające poza zakresem ASVS. Dlatego niniejszy załącznik nie wymienia żadnej zatwierdzonej metody szyfrowania dysków. Dla tego zastosowania szyfrowanie bez uwierzytelniania jest zwykle akceptowane i typowo stosowane są tryby XTS, XEX oraz LRW.

### Opakowywanie kluczy

Kryptograficzne opakowywanie klucza (key wrap, i odpowiadające mu odpakowywanie, key unwrap) to metoda ochrony istniejącego klucza poprzez jego enkapsulację (tj. opakowanie) z użyciem dodatkowego mechanizmu szyfrowania, tak aby oryginalny klucz nie był jawnie eksponowany, np. podczas transferu. Dodatkowy klucz używany do ochrony oryginalnego klucza nazywany jest kluczem opakowującym (wrap key).

Operacja ta może być wykonywana, gdy pożądana jest ochrona kluczy w miejscach uznanych za niegodne zaufania albo przesyłanie wrażliwych kluczy przez niezaufane sieci lub wewnątrz aplikacji.
Należy jednak poważnie rozważyć zrozumienie natury (np. tożsamości i przeznaczenia) oryginalnego klucza przed przystąpieniem do procedury opakowania/odpakowania, ponieważ może to mieć konsekwencje dla systemów/aplikacji źródłowych i docelowych w zakresie bezpieczeństwa, a zwłaszcza zgodności — co może obejmować ślady audytowe funkcji klucza (np. podpisywania) oraz właściwe przechowywanie kluczy.

W szczególności do opakowywania kluczy MUSI być używany AES-256, zgodnie z [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) i z uwzględnieniem perspektywicznych zabezpieczeń przed zagrożeniem kwantowym. Tryby szyfrowania używające AES są następujące, w kolejności preferencji:

| Opakowywanie kluczy | Odniesienie | Status |
|--|--|:-:|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |

AES-192 i AES-128 MOGĄ być używane, jeśli wymaga tego przypadek użycia, ale motywacja MUSI zostać udokumentowana w inwentarzu kryptograficznym podmiotu.

### Szyfrowanie uwierzytelnione

Z wyjątkiem szyfrowania dysków zaszyfrowane dane muszą być chronione przed nieautoryzowaną modyfikacją z użyciem jakiejś formy schematu szyfrowania uwierzytelnionego (AE), zwykle schematu szyfrowania uwierzytelnionego z danymi powiązanymi (AEAD).

Aplikacja powinna preferencyjnie używać zatwierdzonego schematu AEAD. Alternatywnie może łączyć zatwierdzony schemat szyfru i zatwierdzony algorytm MAC w konstrukcji Encrypt-then-MAC.

MAC-then-encrypt jest nadal dozwolony dla zgodności ze starszymi aplikacjami. Jest używany w TLS v1.2 ze starymi zestawami szyfrów.

| Mechanizm AEAD | Odniesienie | Status |
|---|---------|:-:|
|AES-GCM | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A |
|AES-CCM  | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A |
|ChaCha-Poly1305 | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539) | A |
|AEGIS-256 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128L| [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|Encrypt-then-MAC | | A |
|MAC-then-encrypt | | L |

## Funkcje skrótu

Ta sekcja dostarcza dodatkowych informacji dla V11.4 Haszowanie i funkcje oparte na skrótach.

### Funkcje skrótu do ogólnych przypadków użycia

Poniższa tabela wymienia funkcje skrótu zatwierdzone do ogólnych kryptograficznych przypadków użycia, takich jak podpisy cyfrowe:

* Zatwierdzone funkcje skrótu zapewniają silną odporność na kolizje i są odpowiednie dla aplikacji o wysokich wymaganiach bezpieczeństwa.
* Niektóre z tych algorytmów oferują silną odporność na ataki przy właściwym zarządzaniu kluczami kryptograficznymi, dlatego są dodatkowo zatwierdzone dla funkcji HMAC, KDF i RBG.
* Funkcje skrótu o długości wyjścia mniejszej niż 254 bity mają niewystarczającą odporność na kolizje i nie mogą być używane do podpisów cyfrowych ani innych zastosowań wymagających odporności na kolizje. W pozostałych zastosowaniach mogą być używane WYŁĄCZNIE dla zgodności i weryfikacji ze starszymi systemami, ale nie mogą być używane w nowych projektach.

| Funkcja skrótu | Odniesienie | Status | Ograniczenia |
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
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Nieodpowiednia dla HMAC, KDF, RBG, podpisów cyfrowych |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Nieodpowiednia dla HMAC, KDF, RBG, podpisów cyfrowych |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | L | Nieodpowiednia dla HMAC, KDF, RBG, podpisów cyfrowych |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L | Nieodpowiednia dla HMAC, KDF, RBG, podpisów cyfrowych |
| CRC (dowolna długość) |  | D |  |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) | D | |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D | |

### Funkcje skrótu do przechowywania haseł

Do bezpiecznego haszowania haseł muszą być używane dedykowane funkcje skrótu. Te wolne algorytmy haszowania ograniczają ataki siłowe i słownikowe, zwiększając trudność obliczeniową łamania haseł.

| KDF        | Odniesienie | Wymagane parametry | Status |
| ---------- | --------- | ------------ |:-:|
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
|          |                                                     | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
|          |                                                     | t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A |
| scrypt   | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
|          |                                                     | p = 2: N ≥ 2^16 (64 MiB), r = 8  | A |
|          |                                                     | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8  | A |
| bcrypt | [A Future-Adaptable Password Scheme](https://www.researchgate.net/publication/2519476_A_Future-Adaptable_Password_Scheme) | cost ≥ 10 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iteracje ≥ 210 000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iteracje ≥ 600 000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iteracje ≥ 1 300 000 | L |

Zatwierdzone funkcje wyprowadzania klucza oparte na hasłach mogą być używane do przechowywania haseł.

## Funkcje wyprowadzania klucza (KDF)

### Ogólne funkcje wyprowadzania klucza

| KDF              | Odniesienie                                                                                     | Status |
| ---------------- | -------- |:-:|
| HKDF             | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                           | A      |
| TLS 1.2 PRF      | [RFC 5248](https://www.rfc-editor.org/info/rfc5248)                                           | L      |
| KDF oparte na MD5   | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                           | D      |
| KDF oparte na SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | D      |

### Funkcje wyprowadzania klucza oparte na hasłach

| KDF        | Odniesienie | Wymagane parametry | Status |
| ---------- | --------- | ------------ |:-:|
| argon2id   | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
|            |                                                     | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
| scrypt     | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
|            |                                                     | p = 2: N ≥ 2^16 (64 MiB), r = 8  | A |
|            |                                                     | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8  | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iteracje ≥ 210 000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iteracje ≥ 600 000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iteracje ≥ 1 300 000 | L |

## Mechanizmy wymiany kluczy

Ta sekcja dostarcza dodatkowych informacji dla V11.6 Kryptografia klucza publicznego.

### Schematy KEX

Dla wszystkich schematów wymiany kluczy MUSI być zapewniona siła bezpieczeństwa 112 bitów lub wyższa, a ich implementacja MUSI przestrzegać doboru parametrów z poniższej tabeli.

| Schemat | Parametry dziedziny | Utajnianie z wyprzedzeniem |Status |
|--|--|--|:-:|
| Finite Field Diffie-Hellman (FFDH) | L >= 3072 & N >= 256 | Tak | A |
| Elliptic Curve Diffie-Hellman (ECDH) | f >= 256-383 | Tak | A |
| Szyfrowany transport klucza z RSA-PKCS#1 v1.5 | | Nie | D |

Gdzie poszczególne parametry oznaczają:

* k — rozmiar klucza dla kluczy RSA.
* L — rozmiar klucza publicznego, a N — rozmiar klucza prywatnego dla kryptografii ciał skończonych.
* f — zakres rozmiarów kluczy dla ECC.

Żadna nowa implementacja NIE MOŻE używać schematu NIEZGODNEGO z [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) i [B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) oraz [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final). W szczególności IKEv1 NIE MOŻE być używany w środowisku produkcyjnym.

### Grupy Diffiego-Hellmana

Następujące grupy są zatwierdzone dla implementacji wymiany kluczy Diffiego-Hellmana. Siły bezpieczeństwa są udokumentowane w [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final), Załącznik D, oraz [NIST SP 800-57 Part 1 Rev.5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Grupa            | Status |
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

## Kody uwierzytelniania wiadomości (MAC)

Kody uwierzytelniania wiadomości (MAC) to konstrukcje kryptograficzne służące weryfikacji integralności i autentyczności komunikatu. MAC przyjmuje na wejściu komunikat i klucz tajny, a produkuje znacznik o stałym rozmiarze (wartość MAC). MAC są szeroko stosowane w protokołach bezpiecznej komunikacji (np. TLS/SSL), aby zapewnić, że komunikaty wymieniane między stronami są autentyczne i nienaruszone.

| Algorytm MAC | Odniesienie                                                                                 | Status |
| ----------    | --------------- |:-:|
| HMAC-SHA-256  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-384  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-512  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| KMAC128       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A |
| KMAC256       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A |
| BLAKE3 (tryb keyed_hash) | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf)  | A |
| AES-CMAC      | [RFC 4493](https://datatracker.ietf.org/doc/html/rfc4493) & [NIST SP 800-38B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf) | A |
| AES-GMAC      | [NIST SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)            | A |
| Poly1305-AES  | [The Poly1305-AES message-authentication code](https://cr.yp.to/mac/poly1305-20050329.pdf)                  | A |
| HMAC-SHA-1    | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | L |
| HMAC-MD5      | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                | D      |

## Podpisy cyfrowe

Schematy podpisów MUSZĄ używać zatwierdzonych rozmiarów kluczy i parametrów zgodnie z [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Algorytm podpisu            | Odniesienie                                                  | Status |
| ------------------------------ | ---------------------------------------------              | :-:    |
| EdDSA (Ed25519, Ed448)         | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)        | A      |
| XEdDSA (Curve25519, Curve448)  | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)   | A      |
| ECDSA (P-256, P-384, P-521)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)  | A      |
| RSA-RSSA-PSS                   | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | A      |
| RSA-SSA-PKCS#1 v1.5            | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | D      |
| DSA (dowolny rozmiar klucza)   | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)  | D      |

## Postkwantowe standardy szyfrowania

Implementacje kryptografii postkwantowej (PQC) powinny być zgodne z [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd), [FIPS-204](https://csrc.nist.gov/pubs/fips/204/ipd) oraz [FIPS-205](https://csrc.nist.gov/pubs/fips/205/ipd). W chwili obecnej nie ma wielu utwardzonych przykładów kodu ani implementacji referencyjnych dla tych standardów. Więcej szczegółów w [ogłoszeniu NIST o pierwszych trzech sfinalizowanych postkwantowych standardach szyfrowania (sierpień 2024)](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards).

Proponowana postkwantowa hybrydowa metoda uzgadniania klucza TLS [mlkem768x25519](https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/03/) jest wspierana przez główne przeglądarki, takie jak [Firefox w wydaniu 132](https://www.mozilla.org/en-US/firefox/132.0/releasenotes/) i [Chrome w wydaniu 131](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html). Może być stosowana w kryptograficznych środowiskach testowych albo gdy jest dostępna w bibliotekach zatwierdzonych branżowo lub rządowo.
