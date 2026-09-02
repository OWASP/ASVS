# Lampiran C: Standar Kriptografi

Bab "Kriptografi" bergerak lebih jauh dari sekadar mendefinisikan _best practices_. Bab ini bertujuan untuk meningkatkan pemahaman tentang prinsip-prinsip kriptografi dan mendorong adopsi metode keamanan yang lebih tangguh dan modern. Lampiran ini menyediakan informasi teknis terperinci mengenai setiap persyaratan, melengkapi standar menyeluruh yang diuraikan dalam bab "Kriptografi".

Lampiran ini mendefinisikan tingkat persetujuan untuk berbagai mekanisme kriptografi:

* Mekanisme Approved/Disetujui (A) dapat digunakan dalam aplikasi.
* Mekanisme Legacy/Warisan (L) tidak boleh digunakan dalam aplikasi baru, tetapi mungkin masih digunakan hanya untuk kompatibilitas dengan aplikasi atau kode _legacy_ yang ada. Meskipun penggunaan mekanisme ini saat ini tidak dianggap sebagai kerentanan dengan sendirinya, mekanisme tersebut harus digantikan oleh mekanisme yang lebih aman dan _future-proof_ sesegera mungkin.
* Mekanisme Disallowed/Dilarang (D) tidak boleh digunakan karena saat ini dianggap rusak atau tidak memberikan keamanan yang memadai.

Daftar ini dapat digantikan (_overridden_) dalam konteks aplikasi tertentu karena berbagai alasan termasuk:

* Perkembangan baru di bidang kriptografi;
* Kepatuhan terhadap regulasi (_compliance_).

## Inventarisasi dan Dokumentasi Kriptografi

Bagian ini menyediakan informasi tambahan untuk V11.1 Inventarisasi dan Dokumentasi Kriptografi.

Penting untuk memastikan bahwa semua aset kriptografi, seperti algoritma, kunci, dan sertifikat, secara teratur ditemukan, diinventarisasi, dan dievaluasi. Untuk Level 3, ini harus mencakup penggunaan pemindaian statis dan dinamis untuk menemukan penggunaan kriptografi dalam aplikasi. _Tools_ seperti SAST dan DAST dapat membantu dalam hal ini, tetapi mungkin diperlukan _tools_ khusus untuk mendapatkan cakupan yang lebih komprehensif. Contoh _tools_ gratis (_freeware_) meliputi:

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

## Kekuatan Setara dari Parameter Kriptografi

Kekuatan keamanan relatif untuk berbagai sistem kriptografi ada dalam tabel ini (dari [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), hal. 71):

| Security Strength | Symmetric Key Algorithms | Finite Field | Integer Factorisation | Elliptic Curve |
| -- | -- | -- | -- | -- |
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

Contoh aplikasi:

* Finite Field Cryptography: DSA, FFDH, MQV
* Integer Factorisation Cryptography: RSA
* Elliptic Curve Cryptography: ECDSA, EdDSA, ECDH, MQV

Catatan: Bagian ini mengasumsikan bahwa belum ada komputer kuantum; jika komputer tersebut ada, estimasi untuk 3 kolom terakhir tidak lagi berlaku.

## Nilai Acak (Random Values)

Bagian ini menyediakan informasi tambahan untuk V11.5 Nilai Acak (_Random Values_).

| Nama | Versi/Referensi | Catatan | Status |
| :--- | :---- | :---- | :-: |
| `/dev/random` | Linux 4.8+ [(Okt 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3), juga ditemukan pada iOS, Android, dan sistem operasi POSIX berbasis Linux lainnya. Berdasarkan [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) | Menggunakan stream ChaCha20. Ditemukan di iOS [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) dan Android [`Secure Random`](https://developer.android.com/reference/java/security/SecureRandom) dengan pengaturan yang benar yang diberikan pada masing-masing OS. | A |
| `/dev/urandom` | File khusus kernel Linux untuk menyediakan data acak | Menyediakan sumber entropi berkualitas tinggi dari acak perangkat keras (_hardware randomness_) | A |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | Seperti yang digunakan dalam implementasi umum, seperti [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) yang diatur oleh [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers). | A |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2), tersedia di [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) dan [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) | Menyediakan byte acak yang aman langsung dari sumber entropi kernel dengan API yang sederhana dan minimalis. Metode ini lebih modern dan menghindari masalah yang terkait dengan API lama. | A |

Fungsi hash mendasar yang digunakan dengan HMAC-DRBG atau Hash-DRBG harus disetujui untuk penggunaan ini.

## Algoritma Cipher

Bagian ini menyediakan informasi tambahan untuk V11.3 Algoritma Enkripsi.

Algoritma cipher yang disetujui (_Approved_) terdaftar berdasarkan urutan preferensi.

| Algoritma Kunci Simetris | Referensi | Status |
| ------ | ------ | :-: |
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
| Blowfish | | D |
| ARC4 | | D |
| DES | | D |

### Mode Cipher AES

Block cipher, seperti AES, dapat digunakan dengan mode operasi yang berbeda. Banyak mode operasi, seperti Electronic Codebook (ECB), tidak aman dan tidak boleh digunakan. Mode operasi Galois/Counter Mode (GCM) dan Counter with cipher block chaining message authentication code (CCM) menyediakan enkripsi terotentikasi (_authenticated encryption_) dan harus digunakan dalam aplikasi modern.

Mode yang disetujui (_Approved_) terdaftar berdasarkan urutan preferensi.

| Mode | Terotentikasi | Referensi | Status | Pembatasan |
| -- | -- | -- | :-: | -- |
| GCM | Ya | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A | |
| CCM | Ya | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A | |
| CBC | Tidak | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | L | |
| CCM-8 | Ya | | D | |
| ECB | Tidak | | D | |
| CFB | Tidak | | D | |
| OFB | Tidak | | D | |
| CTR | Tidak | | D | |

Catatan:

* Semua pesan yang dienkripsi harus diotentikasi. Untuk SETIAP penggunaan mode CBC, HARUS ada algoritma MAC hashing terkait untuk memvalidasi pesan. Secara umum, ini HARUS diterapkan dalam metode Encrypt-Then-Hash (tetapi TLS 1.2 menggunakan Hash-Then-Encrypt sebagai gantinya). Jika hal ini tidak dapat dijamin, maka CBC TIDAK BOLEH digunakan. Satu-satunya aplikasi di mana enkripsi tanpa algoritma MAC diizinkan adalah enkripsi disk.
* Jika CBC digunakan, harus dijamin bahwa verifikasi _padding_ dilakukan dalam waktu konstan (_constant time_).
* Saat menggunakan CCM-8, tag MAC hanya memiliki keamanan 64 bit. Ini tidak sesuai dengan persyaratan 6.2.9 yang memerlukan keamanan setidaknya 128 bit.
* Enkripsi disk dianggap di luar cakupan ASVS. Oleh karena itu, lampiran ini tidak mencantumkan metode yang disetujui untuk enkripsi disk. Untuk penggunaan ini, enkripsi tanpa otentikasi biasanya diterima dan mode XTS, XEX, serta LRW biasanya digunakan.

### Key Wrapping

Cryptographic key wrap (dan unwrap kunci terkait) adalah metode untuk melindungi kunci yang ada dengan mengapsulkan (misalnya, membungkus/wrapping) kunci tersebut menggunakan mekanisme enkripsi tambahan sehingga kunci asli tidak terekspos secara jelas, misalnya selama transfer. Kunci tambahan yang digunakan untuk melindungi kunci asli ini disebut sebagai _wrap key_.

Operasi ini dapat dilakukan ketika ingin melindungi kunci di tempat-tempat yang dianggap tidak terpercaya, atau untuk mengirimkan kunci sensitif melalui jaringan yang tidak terpercaya atau di dalam aplikasi.
Namun, pertimbangan serius harus diberikan untuk memahami sifat (seperti identitas dan tujuan) dari kunci asli sebelum melakukan prosedur wrap/unwrap karena hal ini dapat berimplikasi pada sistem/aplikasi sumber dan target dalam hal keamanan dan terutama kepatuhan yang mungkin mencakup jejak audit (_audit trails_) dari fungsi kunci (seperti penandatanganan) serta penyimpanan kunci yang tepat.

Secara khusus, AES-256 HARUS digunakan untuk _key wrapping_, mengikuti [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) dan mempertimbangkan ketentuan jangka panjang terhadap ancaman kuantum. Mode cipher yang menggunakan AES adalah sebagai berikut, berdasarkan urutan preferensi:

| Key Wrapping | Referensi | Status |
| -- | -- | :-: |
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |

AES-192 dan AES-128 BOLEH digunakan jika kasus penggunaan menghendakinya, tetapi alasannya HARUS didokumentasikan dalam inventarisasi kriptografi entitas.

### Enkripsi Terotentikasi (Authenticated Encryption)

Dengan pengecualian enkripsi disk, data terenkripsi harus dilindungi dari modifikasi tanpa izin menggunakan beberapa bentuk skema Authenticated Encryption (AE), biasanya menggunakan skema Authenticated Encryption with Associated Data (AEAD).

Aplikasi sebaiknya menggunakan skema AEAD yang disetujui. Secara alternatif, aplikasi dapat menggabungkan skema cipher yang disetujui dan algoritma MAC yang disetujui dengan konstruksi Encrypt-then-MAC.

MAC-then-encrypt masih diizinkan untuk kompatibilitas dengan aplikasi _legacy_. Ini digunakan dalam TLS v1.2 dengan _cipher suites_ lama.

| Mekanisme AEAD | Referensi | Status |
| --- | --------- | :-: |
| AES-GCM | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A |
| AES-CCM | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A |
| ChaCha-Poly1305 | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539) | A |
| AEGIS-256 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
| AEGIS-128 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
| AEGIS-128L | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
| Encrypt-then-MAC | | A |
| MAC-then-encrypt | | L |

## Fungsi Hash

Bagian ini menyediakan informasi tambahan untuk V11.4 Hashing dan Fungsi Berbasis Hash.

### Fungsi Hash untuk Kasus Penggunaan Umum

Tabel berikut mencantumkan fungsi hash yang disetujui dalam kasus penggunaan kriptografi umum seperti tanda tangan digital:

* Fungsi hash yang disetujui memberikan resistensi kolisi (_collision resistance_) yang kuat dan cocok untuk aplikasi keamanan tinggi.
* Beberapa dari algoritma ini menawarkan resistensi yang kuat terhadap serangan jika digunakan dengan manajemen kunci kriptografi yang tepat, sehingga secara tambahan disetujui untuk fungsi HMAC, KDF, dan RBG.
* Fungsi hash dengan output kurang dari 254 bit memiliki resistensi kolisi yang tidak memadai dan tidak boleh digunakan untuk tanda tangan digital atau aplikasi lain yang memerlukan resistensi kolisi. Untuk penggunaan lain, fungsi tersebut mungkin digunakan untuk kompatibilitas dan verifikasi HANYA dengan sistem _legacy_, tetapi tidak boleh digunakan dalam desain baru.

| Fungsi Hash | Referensi | Status | Pembatasan |
| ------ | ----------- | :-: | ---------- |
| SHA3-512 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-512 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA3-384 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-384 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA3-256 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-512/256 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA-256 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHAKE256 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| BLAKE2s | [BLAKE2: simpler, smaller, fast as MD5](https://eprint.iacr.org/2013/322) | A | |
| BLAKE2b | [BLAKE2: simpler, smaller, fast as MD5](https://eprint.iacr.org/2013/322) | A | |
| BLAKE3 | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf) | A | |
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Tidak cocok untuk HMAC, KDF, RBG, tanda tangan digital |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Tidak cocok untuk HMAC, KDF, RBG, tanda tangan digital |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | L | Tidak cocok untuk HMAC, KDF, RBG, tanda tangan digital |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L | Tidak cocok untuk HMAC, KDF, RBG, tanda tangan digital |
| CRC (panjang apa pun) | | D | |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) | D | |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D | |

### Fungsi Hash untuk Penyimpanan Kata Sandi

Untuk hashing kata sandi yang aman, fungsi hash khusus harus digunakan. Algoritma _slow-hashing_ ini memitigasi serangan _brute-force_ dan _dictionary attack_ dengan meningkatkan kesulitan komputasi dalam pembongkaran kata sandi (_password cracking_).

| KDF | Referensi | Parameter yang Diperlukan | Status |
| ---------- | --------- | ------------ | :-: |
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
| | | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
| | | t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A |
| scrypt | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
| | | p = 2: N ≥ 2^16 (64 MiB), r = 8 | A |
| | | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8 | A |
| bcrypt | [A Future-Adaptable Password Scheme](https://www.researchgate.net/publication/2519476_A_Future-Adaptable_Password_Scheme) | cost ≥ 10 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 1,300,000 | L |

Fungsi derivasi kunci berbasis kata sandi yang disetujui dapat digunakan untuk penyimpanan kata sandi.

## Key Derivation Functions (KDFs)

### Key Derivation Functions Umum

| KDF              | Referensi                                                                                     | Status |
| ---------------- | -------- |:-:|
| HKDF             | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                           | A      |
| TLS 1.2 PRF      | [RFC 5248](https://www.rfc-editor.org/info/rfc5248)                                           | L      |
| MD5-based KDFs   | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                           | D      |
| SHA-1-based KDFs | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | D      |

### Key Derivation Functions Berbasis Kata Sandi

| KDF | Referensi | Parameter yang Diperlukan | Status |
| ---------- | --------- | ------------ | :-: |
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
| | | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
| scrypt | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
| | | p = 2: N ≥ 2^16 (64 MiB), r = 8 | A |
| | | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 1,300,000 | L |

## Mekanisme Pertukaran Kunci (Key Exchange)

Bagian ini menyediakan informasi tambahan untuk V11.6 Kriptografi Kunci Publik.

### Skema KEX

Kekuatan keamanan 112 bit atau lebih tinggi HARUS dipastikan untuk semua skema Pertukaran Kunci (_Key Exchange_), dan implementasinya HARUS mengikuti pilihan parameter dalam tabel berikut.

| Skema | Parameter Domain | Forward Secrecy | Status |
| -- | -- | -- | :-: |
| Finite Field Diffie-Hellman (FFDH) | L >= 3072 & N >= 256 | Ya | A |
| Elliptic Curve Diffie-Hellman (ECDH) | f >= 256-383 | Ya | A |
| Encrypted key transport dengan RSA-PKCS#1 v1.5 | | Tidak | D |

Di mana parameter berikut adalah:

* k adalah ukuran kunci untuk kunci RSA.
* L adalah ukuran kunci publik dan N adalah ukuran kunci privat untuk kriptografi finite field.
* f adalah rentang ukuran kunci untuk ECC.

Setiap implementasi baru TIDAK BOLEH menggunakan skema apa pun yang TIDAK patuh terhadap [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) & [B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) dan [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final). Secara khusus, IKEv1 TIDAK BOLEH digunakan dalam lingkungan produksi.

### Grup Diffie-Hellman

Grup berikut disetujui untuk implementasi pertukaran kunci Diffie-Hellman. Kekuatan keamanan didokumentasikan dalam [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final), Lampiran D, dan [NIST SP 800-57 Part 1 Rev.5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Grup             | Status |
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

## Message Authentication Codes (MAC)

Message Authentication Codes (MAC) adalah konstruksi kriptografi yang digunakan untuk memverifikasi integritas dan keaslian (_authenticity_) suatu pesan. MAC menerima pesan dan kunci rahasia sebagai input dan menghasilkan tag berukuran tetap (nilai MAC). MAC banyak digunakan dalam protokol komunikasi aman (misalnya TLS/SSL) untuk memastikan bahwa pesan yang dipertukarkan antar pihak adalah otentik dan utuh.

| Algoritma MAC | Referensi | Status |
| ---------- | --------------- | :-: |
| HMAC-SHA-256 | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-384 | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-512 | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| KMAC128 | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) | A |
| KMAC256 | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) | A |
| BLAKE3 (keyed_hash mode) | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf) | A |
| AES-CMAC | [RFC 4493](https://datatracker.ietf.org/doc/html/rfc4493) & [NIST SP 800-38B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf) | A |
| AES-GMAC | [NIST SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf) | A |
| Poly1305-AES | [The Poly1305-AES message-authentication code](https://cr.yp.to/mac/poly1305-20050329.pdf) | A |
| HMAC-SHA-1 | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | L |
| HMAC-MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D |

## Tanda Tangan Digital (Digital Signatures)

Skema tanda tangan HARUS menggunakan ukuran kunci dan parameter yang disetujui sesuai [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Algoritma Tanda Tangan        | Referensi                                                  | Status |
| ------------------------------ | ---------------------------------------------              | :-:    |
| EdDSA (Ed25519, Ed448)         | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)        | A      |
| XEdDSA (Curve25519, Curve448)  | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)   | A      |
| ECDSA (P-256, P-384, P-521)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)  | A      |
| RSA-RSSA-PSS                   | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | A      |
| RSA-SSA-PKCS#1 v1.5            | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | D      |
| DSA (ukuran kunci apa pun)     | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)  | D      |

## Standar Enkripsi Pasca-Kuantum (Post-Quantum Encryption)

Implementasi PQC harus sejalan dengan [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd)/[204](https://csrc.nist.gov/pubs/fips/204/ipd)/[205](https://csrc.nist.gov/pubs/fips/205/ipd) karena sejauh ini masih minim kode yang diperkuat (_hardened code_) maupun referensi implementasi. https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards

Metode _key agreement_ TLS hibrida pasca-kuantum yang diusulkan [mlkem768x25519](https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/03/) telah didukung oleh peramban-peramban utama seperti [Firefox release 132](https://www.mozilla.org/en-US/firefox/132.0/releasenotes/) dan [Chrome release 131](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html). Metode ini dapat digunakan dalam lingkungan pengujian kriptografi atau ketika tersedia dalam pustaka (_libraries_) yang disetujui oleh industri atau pemerintah.
