# V10 OAuth dan OIDC

## Tujuan Kontrol

OAuth2 (disebut sebagai OAuth dalam bab ini) adalah kerangka kerja standar industri untuk *delegated authorization*. Sebagai contoh, dengan menggunakan OAuth, sebuah aplikasi klien dapat memperoleh akses ke API (*server resources*) atas nama pengguna, asalkan pengguna tersebut telah memberikan otorisasi kepada aplikasi klien untuk melakukannya.

Secara mandiri, OAuth tidak dirancang untuk autentikasi pengguna. Kerangka kerja *OpenID Connect (OIDC)* memperluas OAuth dengan menambahkan lapisan identitas pengguna di atas OAuth. OIDC memberikan dukungan untuk fitur-fitur termasuk informasi pengguna yang terstandarisasi, *Single Sign-On (SSO)*, dan manajemen sesi. Karena OIDC adalah ekstensi dari OAuth, persyaratan OAuth dalam bab ini juga berlaku untuk OIDC.

Peran-peran berikut didefinisikan dalam OAuth:

* Klien OAuth adalah aplikasi yang mencoba untuk mendapatkan akses ke *server resources* (misalnya, dengan memanggil API menggunakan *access token* yang telah diterbitkan). Klien OAuth sering kali berupa aplikasi berbasis *server-side*.
    * *Confidential client* adalah klien yang mampu menjaga kerahasiaan kredensial yang digunakannya untuk melakukan autentikasi ke *authorization server*.
    * *Public client* tidak mampu menjaga kerahasiaan kredensial untuk autentikasi ke *authorization server*. Oleh karena itu, alih-alih melakukan autentikasi (misalnya, menggunakan parameter '*client_id*' dan '*client_secret*'), klien ini hanya mengidentifikasi dirinya sendiri (menggunakan parameter '*client_id*').   
* *OAuth resource server* (*RS*) adalah API server yang mengekspos sumber daya ke *OAuth clients*.
* *OAuth authorization server* (*AS*) adalah sebuah aplikasi server yang menerbitkan *access tokens* kepada *OAuth clients*. *Access tokens* ini memungkinkan *OAuth clients* untuk mengakses sumber daya *RS*, baik atas nama *end-user* maupun atas nama *OAuth client* itu sendiri. *AS* sering kali merupakan aplikasi yang terpisah, namun (jika sesuai) dapat juga diintegrasikan ke dalam *RS* yang memadai.
* *Resource owner* (*RO*) adalah *end-user* yang memberikan otorisasi kepada *OAuth clients* untuk memperoleh akses terbatas ke sumber daya yang dihosting di *resource server* atas nama mereka. *Resource owner* memberikan persetujuan untuk *delegated authorization* ini dengan berinteraksi dengan *authorization server*.

Peran-peran berikut didefinisikan dalam OIDC:

* *Relying party* (*RP*) adalah aplikasi klien yang meminta autentikasi *end-user* melalui *OpenID Provider*. *RP* mengambil peran sebagai *OAuth client*.
* *OpenID Provider* (*OP*) adalah *OAuth AS* yang mampu melakukan autentikasi *end-user* dan memberikan *OIDC claims* kepada *RP*. *OP* bisa jadi merupakan *identity provider* (*IdP*), namun dalam skenario federasi, *OP* dan *identity provider* (tempat *end-user* melakukan autentikasi) bisa saja merupakan aplikasi server yang berbeda.

*OAuth* dan *OIDC* pada awalnya dirancang untuk aplikasi pihak ketiga (*third-party applications*). Saat ini, keduanya juga sering digunakan oleh aplikasi pihak pertama (*first-party applications*). Namun, ketika digunakan dalam skenario pihak pertama, seperti untuk autentikasi dan manajemen sesi, protokol tersebut menambah kompleksitas tertentu yang mungkin menghadirkan tantangan keamanan baru.

*OAuth* dan *OIDC* dapat digunakan untuk berbagai jenis aplikasi, namun fokus untuk *ASVS* dan persyaratan dalam bab ini adalah pada aplikasi web dan *APIs*.

Karena *OAuth* dan *OIDC* dapat dianggap sebagai logika di atas teknologi web, persyaratan umum dari bab-bab lain selalu berlaku, dan bab ini tidak dapat dipisahkan dari konteks tersebut.

Bab ini membahas praktik terbaik saat ini untuk *OAuth2* dan *OIDC* yang selaras dengan spesifikasi yang ditemukan di <https://oauth.net/2/> dan <https://openid.net/developers/specs/>. Meskipun *RFC* dianggap sudah matang, mereka sering diperbarui. Oleh karena itu, penting untuk menyelaraskan dengan versi terbaru saat menerapkan persyaratan dalam bab ini. Lihat bagian referensi untuk rincian lebih lanjut.

Mengingat kompleksitas di bidang ini, sangatlah penting bagi solusi *OAuth* atau *OIDC* yang aman untuk menggunakan server otorisasi standar industri yang sudah dikenal luas dan menerapkan konfigurasi keamanan yang direkomendasikan.

Terminologi yang digunakan dalam bab ini selaras dengan *OAuth RFCs* dan spesifikasi *OIDC*, namun perlu dicatat bahwa terminologi *OIDC* hanya digunakan untuk persyaratan khusus *OIDC*; jika tidak, maka terminologi *OAuth* yang digunakan.

Dalam konteks *OAuth* dan *OIDC*, istilah *token* dalam bab ini merujuk pada:

* *Access tokens*, yang hanya boleh dikonsumsi oleh *RS* dan dapat berupa *reference tokens* yang divalidasi menggunakan *introspection* atau *self-contained tokens* yang divalidasi menggunakan beberapa materi kunci.
* *Refresh tokens*, yang hanya boleh dikonsumsi oleh *authorization server* yang menerbitkan token tersebut.
* *OIDC ID Tokens*, yang hanya boleh dikonsumsi oleh klien yang memicu *authorization flow*.

Tingkat risiko untuk beberapa persyaratan dalam bab ini bergantung pada apakah klien tersebut merupakan *confidential client* atau dianggap sebagai *public client*. Karena penggunaan *strong client authentication* memitigasi banyak vektor serangan, beberapa persyaratan mungkin diperlonggar ketika menggunakan *confidential client* untuk aplikasi *L1*.

## V10.1 Keamanan OAuth dan OIDC Generik

Bagian ini mencakup persyaratan arsitektur umum yang berlaku untuk semua aplikasi yang menggunakan *OAuth* atau *OIDC*.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **10.1.1** | Pastikan bahwa token hanya dikirim ke komponen yang benar-benar membutuhkannya. Misalnya, saat menggunakan pola backend-for-frontend untuk aplikasi JavaScript berbasis browser, token akses dan refresh hanya boleh diakses oleh backend. | 2 |
| **10.1.2** | Pastikan bahwa klien hanya menerima nilai dari *authorization server* (seperti *authorization code* atau *ID Token*) jika nilai-nilai tersebut merupakan hasil dari *authorization flow* yang dimulai oleh sesi *user agent* dan transaksi yang sama. Hal ini mengharuskan rahasia yang dihasilkan klien, seperti *code_verifier* pada *proof key for code exchange* (*PKCE*), *state*, atau *nonce* pada *OIDC*, tidak dapat ditebak, bersifat spesifik untuk transaksi tersebut, dan terikat secara aman baik pada klien maupun sesi *user agent* tempat transaksi dimulai. | 2 |

## V10.2 OAuth Client

Persyaratan ini merinci tanggung jawab untuk aplikasi *OAuth client*. Klien tersebut dapat berupa, misalnya, *web server backend* (yang sering kali bertindak sebagai *Backend For Frontend*, *BFF*), integrasi layanan *backend*, atau *frontend Single Page Application* (*SPA*, yang juga dikenal sebagai aplikasi berbasis *browser*).

Secara umum, klien *backend* dianggap sebagai *confidential clients* dan klien *frontend* dianggap sebagai *public clients*. Namun, aplikasi natif yang berjalan pada perangkat *end-user* dapat dianggap sebagai *confidential* ketika menggunakan *OAuth dynamic client registration*.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **10.2.1** | Pastikan bahwa, jika *code flow* digunakan, *OAuth client* memiliki perlindungan terhadap serangan pemalsuan permintaan berbasis *browser*, yang umumnya dikenal sebagai *cross-site request forgery* (*CSRF*), yang memicu permintaan token, baik dengan menggunakan fungsionalitas *proof key for code exchange* (*PKCE*) atau dengan memeriksa parameter *state* yang dikirimkan dalam *authorization request*. | 2 |
| **10.2.2** | Pastikan bahwa, jika *OAuth client* dapat berinteraksi dengan lebih dari satu *authorization server*, klien tersebut memiliki pertahanan terhadap *mix-up attacks*. Sebagai contoh, klien dapat mewajibkan *authorization server* untuk mengembalikan nilai parameter `iss` (*issuer*) dan memvalidasinya dalam *authorization response* serta *token response* | 2 |
| **10.2.3** |Pastikan bahwa OAuth client hanya meminta scopes (atau parameter otorisasi lainnya) yang benar-benar diperlukan dalam setiap permintaan ke authorization server. | 3 |

## V10.3 OAuth Resource Server

Dalam konteks ASVS dan bab ini, *resource server* adalah sebuah API. Untuk menyediakan akses yang aman, *resource server* harus:

* Memvalidasi *access token*, sesuai dengan format token dan spesifikasi protokol yang relevan, misalnya, validasi JWT atau *OAuth token introspection*.
* Jika valid, menegakkan keputusan otorisasi berdasarkan informasi dari *access token* dan izin yang telah diberikan. Sebagai contoh, *resource server* perlu memverifikasi bahwa klien (yang bertindak atas nama *RO*) memiliki wewenang untuk mengakses sumber daya yang diminta.

Oleh karena itu, persyaratan yang tercantum di sini bersifat khusus untuk OAuth atau OIDC dan harus dilakukan setelah validasi token dan sebelum melakukan otorisasi berdasarkan informasi dari token tersebut.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **10.3.1** | Pastikan bahwa *resource server* hanya menerima *access tokens* yang ditujukan untuk digunakan dengan layanan tersebut (*audience*). *Audience* dapat dicantumkan dalam *access token* yang terstruktur (seperti *claim* 'aud' dalam *JWT*), atau dapat diperiksa menggunakan *endpoint token introspection*. | 2 |
| **10.3.2** | Pastikan bahwa *resource server* menegakkan keputusan otorisasi berdasarkan *claims* dari *access token* yang mendefinisikan delegasi otorisasi. Jika *claims* seperti 'sub', 'scope', dan 'authorization_details' ada, maka hal tersebut harus menjadi bagian dari pengambilan keputusan. | 2 |
| **10.3.3** | Pastikan bahwa jika keputusan kontrol akses memerlukan identifikasi pengguna yang unik dari sebuah *access token* (*JWT* atau respons *token introspection* terkait), *resource server* mengidentifikasi pengguna dari *claims* yang tidak dapat dialihkan ke pengguna lain. Biasanya, hal ini berarti menggunakan kombinasi dari *claims* 'iss' (*issuer*) dan 'sub' (*subject*). | 2 |
| **10.3.4** | Pastikan bahwa jika *resource server* memerlukan kekuatan autentikasi, metode, atau kebaruan tertentu, ia memverifikasi bahwa *access token* yang disajikan memenuhi batasan tersebut. Sebagai contoh, jika tersedia, masing-masing menggunakan *claims* OIDC 'acr', 'amr', dan 'auth_time'. | 2 |
| **10.3.5** | Pastikan bahwa *resource server* mencegah penggunaan *access tokens* yang dicuri atau *replay* (pengulangan) *access tokens* (dari pihak yang tidak berwenang) dengan mewajibkan *sender-constrained access tokens*, baik menggunakan *Mutual TLS* untuk *OAuth 2* atau *OAuth 2 Demonstration of Proof of Possession* (*DPoP*). | 3 |

## V10.4 OAuth Authorization Server

Persyaratan ini merinci tanggung jawab untuk server otorisasi OAuth, termasuk Penyedia OpenID.

Untuk otentikasi klien, metode 'self_signed_tls_client_auth' diperbolehkan dengan prasyarat yang dibutuhkan oleh [section 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) dari [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705).

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **10.4.1** | Pastikan bahwa *authorization server* memvalidasi *redirect URIs* berdasarkan *allowlist* khusus klien dari URI yang telah didaftarkan sebelumnya menggunakan perbandingan string yang tepat (*exact string comparison*). | 1 |
| **10.4.2** | Pastikan bahwa, jika *authorization server* mengembalikan *authorization code* dalam *authorization response*, kode tersebut hanya dapat digunakan satu kali untuk *token request*. Untuk permintaan valid kedua dengan *authorization code* yang sudah pernah digunakan untuk menerbitkan *access token*, *authorization server* harus menolak permintaan token tersebut dan mencabut semua token yang telah diterbitkan sebelumnya yang berkaitan dengan *authorization code* tersebut. | 1 |
| **10.4.3** | Pastikan bahwa *authorization code* bersifat berumur pendek (*short-lived*). Masa berlaku maksimum dapat mencapai 10 menit untuk aplikasi L1 dan L2, serta maksimum 1 menit untuk aplikasi L3. | 1 |
| **10.4.4** | Pastikan bahwa untuk klien tertentu, *authorization server* hanya mengizinkan penggunaan *grants* yang memang perlu digunakan oleh klien tersebut. Perhatikan bahwa *grants* 'token' (*Implicit flow*) dan 'password' (*Resource Owner Password Credentials flow*) tidak boleh lagi digunakan. | 1 |
| **10.4.5** | Pastikan bahwa *authorization server* memitigasi serangan *refresh token replay* untuk *public clients*, lebih baik menggunakan *sender-constrained refresh tokens*, yaitu *Demonstrating Proof of Possession* (DPoP) atau *Certificate-Bound Access Tokens* menggunakan *mutual TLS* (mTLS). Untuk aplikasi L1 dan L2, *refresh token rotation* dapat digunakan. Jika *refresh token rotation* digunakan, *authorization server* harus membatalkan *refresh token* setelah digunakan, dan mencabut semua *refresh token* untuk otorisasi tersebut jika *refresh token* yang sudah digunakan dan dibatalkan diberikan kembali. | 1 |
| **10.4.6** | Pastikan bahwa, jika *code grant* digunakan, *authorization server* memitigasi serangan intersepsi *authorization code* dengan mewajibkan *proof key for code exchange* (PKCE). Untuk *authorization requests*, *authorization server* harus mewajibkan nilai 'code_challenge' yang valid dan tidak boleh menerima nilai 'code_challenge_method' berupa 'plain'. Untuk *token request*, server harus mewajibkan validasi parameter 'code_verifier'. | 2 |
| **10.4.7** | Pastikan bahwa jika *authorization server* mendukung pendaftaran klien dinamis tanpa autentikasi (*unauthenticated dynamic client registration*), server tersebut memitigasi risiko aplikasi klien yang berbahaya. Server harus memvalidasi metadata klien seperti setiap URI yang didaftarkan, memastikan persetujuan pengguna, dan memperingatkan pengguna sebelum memproses *authorization request* dengan aplikasi klien yang tidak tepercaya. | 2 |
| **10.4.8** | Pastikan bahwa *refresh tokens* memiliki kedaluwarsa absolut, termasuk jika masa kedaluwarsa *refresh token* yang bergeser (*sliding expiration*) diterapkan. | 2 |
| **10.4.9** | Pastikan bahwa *refresh tokens* dan *reference access tokens* dapat dicabut oleh pengguna yang berwenang menggunakan antarmuka pengguna *authorization server*, untuk memitigasi risiko klien berbahaya atau token yang dicuri. | 2 |
| **10.4.10** | Pastikan bahwa *confidential client* diautentikasi untuk permintaan *backchannel* antara klien ke *authorization server*, seperti *token requests*, *pushed authorization requests* (PAR), dan *token revocation requests*. | 2 |
| **10.4.11** | Pastikan bahwa konfigurasi *authorization server* hanya menetapkan *scopes* yang diperlukan kepada klien OAuth. | 2 |
| **10.4.12** | Pastikan bahwa untuk klien tertentu, *authorization server* hanya mengizinkan nilai 'response_mode' yang memang perlu digunakan oleh klien tersebut. Sebagai contoh, dengan meminta *authorization server* memvalidasi nilai ini terhadap nilai yang diharapkan atau dengan menggunakan *pushed authorization request* (PAR) atau *JWT-secured Authorization Request* (JAR). | 3 |
| **10.4.13** | Pastikan bahwa *grant type* 'code' selalu digunakan bersama dengan *pushed authorization requests* (PAR). | 3 |
| **10.4.14** | Pastikan bahwa *authorization server* hanya menerbitkan *access tokens* yang terikat pada pengirim (*sender-constrained*/*Proof-of-Possession*), baik dengan *certificate-bound access tokens* menggunakan *mutual TLS* (mTLS) atau *DPoP-bound access tokens* (*Demonstration of Proof of Possession*). | 3 |
| **10.4.15** | Pastikan bahwa, untuk *server-side client* (yang tidak dieksekusi di perangkat pengguna akhir), *authorization server* memastikan bahwa nilai parameter 'authorization_details' berasal dari *backend* klien dan pengguna tidak merusaknya. Sebagai contoh, dengan mewajibkan penggunaan *pushed authorization request* (PAR) atau *JWT-secured Authorization Request* (JAR). | 3 |
| **10.4.16** | Pastikan bahwa klien bersifat rahasia (*confidential*) dan *authorization server* mewajibkan penggunaan metode autentikasi klien yang kuat (berbasis kriptografi kunci publik dan tahan terhadap serangan *replay*), seperti *mutual TLS* ('tls_client_auth', 'self_signed_tls_client_auth') atau *private key JWT* ('private_key_jwt'). | 3 |

## V10.5 OIDC Client

Karena pihak yang mengandalkan OIDC bertindak sebagai klien OAuth, persyaratan dari bagian "Klien OAuth" juga berlaku.

Perlu dicatat bahwa bagian "Autentikasi dengan Penyedia Identitas" dalam bab "Autentikasi" juga berisi persyaratan umum yang relevan.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **10.5.1** | Pastikan bahwa klien (sebagai *relying party*) memitigasi serangan *ID Token replay*. Sebagai contoh, dengan memastikan bahwa *claim* 'nonce' di dalam *ID Token* cocok dengan nilai 'nonce' yang dikirimkan dalam *authentication request* ke *OpenID Provider* (dalam *OAuth2* disebut sebagai *authorization request* yang dikirimkan ke *authorization server*). | 2 |
| **10.5.2** | Pastikan bahwa klien mengidentifikasi pengguna secara unik dari *claims* dalam *ID Token*, biasanya melalui *claim* 'sub', yang tidak dapat dialokasikan kembali ke pengguna lain (dalam cakupan *identity provider* tersebut). | 2 |
| **10.5.3** | Pastikan bahwa klien menolak upaya oleh *authorization server* yang berbahaya untuk meniru *authorization server* lain melalui metadata *authorization server*. Klien harus menolak metadata *authorization server* jika URL *issuer* dalam metadata tersebut tidak cocok secara persis dengan URL *issuer* yang telah dikonfigurasi sebelumnya dan diharapkan oleh klien. | 2 |
| **10.5.4** | Pastikan bahwa klien memvalidasi bahwa *ID Token* memang ditujukan untuk digunakan oleh klien tersebut (*audience*) dengan memeriksa apakah *claim* 'aud' dari token tersebut sama dengan nilai 'client_id' milik klien. | 2 |
| **10.5.5** | Pastikan bahwa, saat menggunakan *OIDC back-channel logout*, *relying party* memitigasi serangan *denial of service* melalui *forced logout* dan kebingungan antar-JWT (*cross-JWT confusion*) dalam alur *logout*. Klien harus memverifikasi bahwa *logout token* memiliki tipe yang benar dengan nilai 'logout+jwt', berisi *claim* 'event' dengan nama anggota yang tepat, dan tidak mengandung *claim* 'nonce'. Perlu dicatat bahwa sangat disarankan juga untuk memiliki masa kedaluwarsa yang pendek (misalnya, 2 menit). | 2 |

## V10.6 Penyedia OpenID

Karena *OpenID Provider* bertindak sebagai *OAuth authorization server*, persyaratan dari bagian "*OAuth Authorization Server*" juga berlaku di sini.

Perlu dicatat bahwa jika menggunakan alur *ID Token* (bukan *code flow*), tidak ada *access tokens* yang diterbitkan, sehingga banyak persyaratan untuk *OAuth Authorization Server* (AS) menjadi tidak relevan.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **10.6.1** | Pastikan bahwa *OpenID Provider* hanya mengizinkan nilai 'code', 'ciba', 'id_token', atau 'id_token code' untuk *response mode*. Perlu dicatat bahwa 'code' lebih disukai daripada 'id_token code' (*OIDC Hybrid flow*), dan 'token' (*Implicit flow* apa pun) tidak boleh digunakan. | 2 |
| **10.6.2** | Pastikan bahwa *OpenID Provider* memitigasi serangan *denial of service* melalui *forced logout*. Hal ini dilakukan dengan mendapatkan konfirmasi eksplisit dari pengguna akhir atau, jika tersedia, memvalidasi parameter dalam *logout request* (yang diinisiasi oleh *relying party*), seperti 'id_token_hint'. | 2 |

## V10.7 Manajemen Persetujuan

Persyaratan ini mencakup verifikasi persetujuan pengguna oleh *authorization server*. Tanpa verifikasi persetujuan pengguna yang tepat, aktor jahat dapat memperoleh izin atas nama pengguna melalui teknik *spoofing* atau rekayasa sosial (*social engineering*).

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **10.7.1** | Pastikan bahwa *authorization server* memastikan pengguna menyetujui setiap permintaan otorisasi. Jika identitas klien tidak dapat dipastikan, *authorization server* harus selalu secara eksplisit meminta persetujuan dari pengguna. | 2 |
| **10.7.2** | Pastikan bahwa ketika *authorization server* meminta persetujuan pengguna, server tersebut menyajikan informasi yang cukup dan jelas mengenai apa yang sedang disetujui. Jika memungkinkan, hal ini harus mencakup sifat dari otorisasi yang diminta (biasanya berdasarkan *scope*, *resource server*, atau rincian otorisasi *Rich Authorization Requests* (RAR)), identitas aplikasi yang diberi wewenang, serta masa berlaku dari otorisasi tersebut. | 2 |
| **10.7.3** | Pastikan bahwa pengguna dapat meninjau, mengubah, dan mencabut persetujuan (*consents*) yang telah mereka berikan melalui *authorization server*. | 2 |

## Referensi

Untuk informasi lebih lanjut mengenai OAuth, silakan lihat:

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

Untuk persyaratan terkait OAuth di ASVS, RFC yang telah diterbitkan dan yang masih dalam tahap draf digunakan:

* [RFC6749 The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
* [RFC6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)
* [RFC6819 OAuth 2.0 Threat Model and Security Considerations](https://datatracker.ietf.org/doc/html/rfc6819)
* [RFC7636 Proof Key for Code Exchange by OAuth Public Clients](https://datatracker.ietf.org/doc/html/rfc7636)
* [RFC7591 OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591)
* [RFC8628 OAuth 2.0 Device Authorization Grant](https://datatracker.ietf.org/doc/html/rfc8628)
* [RFC8707 Resource Indicators for OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc8707)
* [RFC9068 JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
* [RFC9126 OAuth 2.0 Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126)
* [RFC9207 OAuth 2.0 Authorization Server Issuer Identification](https://datatracker.ietf.org/doc/html/rfc9207)
* [RFC9396 OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)
* [RFC9449 OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)
* [RFC9700 Best Current Practice for OAuth 2.0 Security](https://datatracker.ietf.org/doc/html/rfc9700)
* [draft OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)<!-- recheck on release -->
* [draft The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12)<!-- recheck on release -->

Untuk informasi lebih lanjut mengenai *OpenID Connect*, silakan lihat:

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
