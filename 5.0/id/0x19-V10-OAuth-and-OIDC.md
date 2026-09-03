# V10 OAuth dan OIDC

## Tujuan Kontrol

OAuth2 (disebut sebagai OAuth dalam bab ini) adalah framework standar industri untuk delegated authorization. Misalnya, dengan menggunakan OAuth, sebuah aplikasi client dapat memperoleh akses ke API (server resources) atas nama pengguna, asalkan pengguna tersebut telah mengizinkan aplikasi client untuk melakukannya.

Dengan sendirinya, OAuth tidak dirancang untuk autentikasi pengguna. Framework OpenID Connect (OIDC) memperluas OAuth dengan menambahkan sebuah lapisan identitas pengguna di atas OAuth. OIDC menyediakan dukungan untuk fitur-fitur termasuk informasi pengguna yang terstandardisasi, Single Sign-On (SSO), dan session management. Karena OIDC merupakan perluasan dari OAuth, persyaratan OAuth pada bab ini juga berlaku untuk OIDC.

Peran-peran berikut didefinisikan dalam OAuth:

* OAuth client adalah aplikasi yang berupaya memperoleh akses ke server resources (misalnya, dengan memanggil sebuah API menggunakan access token yang diterbitkan). OAuth client sering kali berupa aplikasi server-side.
    * Confidential client adalah client yang mampu menjaga kerahasiaan kredensial yang digunakannya untuk mengautentikasi dirinya sendiri dengan authorization server.
    * Public client tidak mampu menjaga kerahasiaan kredensial untuk mengautentikasi dengan authorization server. Oleh karena itu, alih-alih mengautentikasi dirinya sendiri (misalnya, menggunakan parameter 'client_id' dan 'client_secret'), client tersebut hanya mengidentifikasi dirinya (menggunakan parameter 'client_id').
* OAuth resource server (RS) adalah server API yang mengekspos resource kepada OAuth client.
* OAuth authorization server (AS) adalah aplikasi server yang menerbitkan access token kepada OAuth client. Access token ini memungkinkan OAuth client mengakses resource RS, baik atas nama pengguna akhir (end-user) maupun atas nama OAuth client itu sendiri. AS sering kali merupakan aplikasi terpisah, namun (jika sesuai) dapat diintegrasikan ke dalam RS yang sesuai.
* Resource owner (RO) adalah pengguna akhir yang mengizinkan OAuth client untuk memperoleh akses terbatas ke resource yang di-hosting pada resource server atas nama mereka. Resource owner menyetujui delegated authorization ini dengan berinteraksi dengan authorization server.

Peran-peran berikut didefinisikan dalam OIDC:

* Relying party (RP) adalah aplikasi client yang meminta autentikasi pengguna akhir melalui OpenID Provider. RP berperan sebagai OAuth client.
* OpenID Provider (OP) adalah sebuah OAuth AS yang mampu mengautentikasi pengguna akhir dan menyediakan OIDC claims kepada RP. OP dapat merupakan identity provider (IdP), namun dalam skenario federated, OP dan identity provider (tempat pengguna akhir melakukan autentikasi) dapat merupakan aplikasi server yang berbeda.

OAuth dan OIDC awalnya dirancang untuk aplikasi pihak ketiga (third-party). Saat ini, keduanya juga sering digunakan oleh aplikasi pihak pertama (first-party). Namun, ketika digunakan dalam skenario pihak pertama, seperti authentication dan session management, protokol tersebut menambahkan kompleksitas tertentu, yang dapat menimbulkan tantangan keamanan baru.

OAuth dan OIDC dapat digunakan untuk berbagai jenis aplikasi, namun fokus untuk ASVS dan persyaratan pada bab ini adalah pada aplikasi web dan API.

Karena OAuth dan OIDC dapat dianggap sebagai logika di atas teknologi web, persyaratan umum dari bab-bab lain selalu berlaku, dan bab ini tidak dapat dipisahkan dari konteksnya.

Bab ini membahas praktik terbaik terkini (best current practices) untuk OAuth2 dan OIDC yang selaras dengan spesifikasi yang terdapat pada <https://oauth.net/2/> dan <https://openid.net/developers/specs/>. Meskipun RFC dianggap sudah matang (mature), RFC tersebut sering diperbarui. Oleh karena itu, penting untuk menyelaraskan dengan versi terbaru saat menerapkan persyaratan pada bab ini. Lihat bagian referensi untuk detail lebih lanjut.

Mengingat kompleksitas area ini, sangat penting bagi solusi OAuth atau OIDC yang aman untuk menggunakan authorization server yang sudah dikenal dan menjadi standar industri serta menerapkan konfigurasi keamanan yang direkomendasikan.

Terminologi yang digunakan dalam bab ini selaras dengan RFC OAuth dan spesifikasi OIDC, namun perlu dicatat bahwa terminologi OIDC hanya digunakan untuk persyaratan yang spesifik terhadap OIDC; selain itu, terminologi OAuth yang digunakan.

Dalam konteks OAuth dan OIDC, istilah "token" pada bab ini merujuk pada:

* Access token, yang hanya boleh dikonsumsi oleh RS dan dapat berupa reference token yang divalidasi menggunakan introspection atau self-contained token yang divalidasi menggunakan key material tertentu.
* Refresh token, yang hanya boleh dikonsumsi oleh authorization server yang menerbitkan token tersebut.
* OIDC ID Token, yang hanya boleh dikonsumsi oleh client yang memicu authorization flow.

Level risiko untuk beberapa persyaratan pada bab ini bergantung pada apakah client tersebut merupakan confidential client atau dianggap sebagai public client. Karena penggunaan client authentication yang kuat dapat memitigasi banyak attack vector, beberapa persyaratan mungkin dilonggarkan saat menggunakan confidential client untuk aplikasi L1.

## V10.1 Keamanan Umum OAuth dan OIDC

Bagian ini membahas persyaratan arsitektur umum yang berlaku untuk semua aplikasi yang menggunakan OAuth atau OIDC.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **10.1.1** | Verifikasi bahwa token hanya dikirimkan ke komponen yang benar-benar memerlukannya. Misalnya, saat menggunakan pola backend-for-frontend untuk aplikasi JavaScript berbasis browser, access token dan refresh token hanya boleh dapat diakses oleh backend. | 2 |
| **10.1.2** | Verifikasi bahwa client hanya menerima nilai dari authorization server (seperti authorization code atau ID Token) jika nilai tersebut berasal dari sebuah authorization flow yang diinisiasi oleh user agent session dan transaksi yang sama. Hal ini mensyaratkan bahwa secret yang dihasilkan oleh client, seperti proof key for code exchange (PKCE) 'code_verifier', 'state', atau OIDC 'nonce', tidak dapat ditebak, bersifat spesifik terhadap transaksi tersebut, dan terikat secara aman baik pada client maupun pada user agent session tempat transaksi tersebut dimulai. | 2 |

## V10.2 OAuth Client

Persyaratan ini merinci tanggung jawab untuk aplikasi OAuth client. Client dapat berupa, misalnya, sebuah backend web server (sering bertindak sebagai Backend For Frontend, BFF), sebuah integrasi backend service, atau sebuah frontend Single Page Application (SPA, dikenal juga sebagai aplikasi berbasis browser).

Secara umum, backend client dianggap sebagai confidential client dan frontend client dianggap sebagai public client. Namun, aplikasi native yang berjalan pada perangkat pengguna akhir dapat dianggap sebagai confidential ketika menggunakan OAuth dynamic client registration.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **10.2.1** | Verifikasi bahwa, jika code flow digunakan, OAuth client memiliki perlindungan terhadap serangan browser-based request forgery, yang umum dikenal sebagai cross-site request forgery (CSRF), yang memicu token requests, baik dengan menggunakan fungsionalitas proof key for code exchange (PKCE) atau dengan memeriksa parameter 'state' yang dikirimkan pada authorization request. | 2 |
| **10.2.2** | Verifikasi bahwa, jika OAuth client dapat berinteraksi dengan lebih dari satu authorization server, client tersebut memiliki pertahanan terhadap mix-up attacks. Misalnya, dapat dilakukan dengan mewajibkan authorization server mengembalikan nilai parameter 'iss' dan memvalidasinya pada authorization response dan token response. | 2 |
| **10.2.3** | Verifikasi bahwa OAuth client hanya meminta scopes (atau parameter authorization lainnya) yang diperlukan pada request ke authorization server. | 3 |

## V10.3 OAuth Resource Server

Dalam konteks ASVS dan bab ini, resource server adalah sebuah API. Untuk menyediakan akses yang aman, resource server harus:

* Memvalidasi access token, sesuai dengan format token dan spesifikasi protokol yang relevan, misalnya, JWT-validation atau OAuth token introspection.
* Jika valid, menegakkan keputusan authorization berdasarkan informasi dari access token dan permission yang telah diberikan. Misalnya, resource server perlu memverifikasi bahwa client (yang bertindak atas nama RO) berwenang untuk mengakses resource yang diminta.

Oleh karena itu, persyaratan yang tercantum di sini bersifat spesifik terhadap OAuth atau OIDC dan harus dilakukan setelah validasi token dan sebelum melakukan authorization berdasarkan informasi dari token tersebut.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **10.3.1** | Verifikasi bahwa resource server hanya menerima access token yang dimaksudkan untuk digunakan dengan layanan tersebut (audience). Audience dapat disertakan dalam access token yang terstruktur (seperti claim 'aud' pada JWT), atau dapat diperiksa menggunakan token introspection endpoint. | 2 |
| **10.3.2** | Verifikasi bahwa resource server menegakkan keputusan authorization berdasarkan claims dari access token yang mendefinisikan delegated authorization. Jika claims seperti 'sub', 'scope', dan 'authorization_details' ada, claims tersebut harus menjadi bagian dari keputusan tersebut. | 2 |
| **10.3.3** | Verifikasi bahwa jika sebuah keputusan access control mensyaratkan identifikasi pengguna unik dari sebuah access token (JWT atau token introspection response terkait), resource server mengidentifikasi pengguna dari claims yang tidak dapat dipindahtangankan (reassigned) ke pengguna lain. Umumnya, hal ini berarti menggunakan kombinasi claims 'iss' dan 'sub'. | 2 |
| **10.3.4** | Verifikasi bahwa, jika resource server mensyaratkan kekuatan, metode, atau kebaruan (recentness) autentikasi tertentu, resource server tersebut memverifikasi bahwa access token yang dipresentasikan memenuhi batasan-batasan tersebut. Misalnya, jika ada, dengan menggunakan claims OIDC 'acr', 'amr', dan 'auth_time' secara berurutan. | 2 |
| **10.3.5** | Verifikasi bahwa resource server mencegah penggunaan access token yang dicuri atau replay access token (dari pihak yang tidak berwenang) dengan mewajibkan sender-constrained access token, baik Mutual TLS untuk OAuth 2 maupun OAuth 2 Demonstration of Proof of Possession (DPoP). | 3 |

## V10.4 OAuth Authorization Server

Persyaratan ini merinci tanggung jawab untuk OAuth authorization server, termasuk OpenID Provider.

Untuk client authentication, metode 'self_signed_tls_client_auth' diizinkan dengan prasyarat yang disyaratkan oleh [bagian 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) dari [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705).

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **10.4.1** | Verifikasi bahwa authorization server memvalidasi redirect URI berdasarkan sebuah allowlist yang spesifik terhadap client dari URI yang telah didaftarkan sebelumnya (pre-registered) menggunakan exact string comparison. | 1 |
| **10.4.2** | Verifikasi bahwa, jika authorization server mengembalikan authorization code pada authorization response, code tersebut hanya dapat digunakan sekali untuk sebuah token request. Untuk request kedua yang valid dengan sebuah authorization code yang telah digunakan sebelumnya untuk menerbitkan access token, authorization server harus menolak token request tersebut dan mencabut (revoke) semua token yang diterbitkan terkait dengan authorization code tersebut. | 1 |
| **10.4.3** | Verifikasi bahwa authorization code memiliki masa berlaku yang singkat (short-lived). Masa berlaku maksimum dapat mencapai 10 menit untuk aplikasi L1 dan L2 serta hingga 1 menit untuk aplikasi L3. | 1 |
| **10.4.4** | Verifikasi bahwa untuk client tertentu, authorization server hanya mengizinkan penggunaan grant yang memang perlu digunakan oleh client tersebut. Perlu dicatat bahwa grant 'token' (Implicit flow) dan 'password' (Resource Owner Password Credentials flow) sudah tidak boleh digunakan lagi. | 1 |
| **10.4.5** | Verifikasi bahwa authorization server memitigasi serangan refresh token replay untuk public client, sebaiknya menggunakan sender-constrained refresh token, yaitu Demonstrating Proof of Possession (DPoP) atau Certificate-Bound Access Token menggunakan mutual TLS (mTLS). Untuk aplikasi L1 dan L2, refresh token rotation dapat digunakan. Jika refresh token rotation digunakan, authorization server harus melakukan invalidasi terhadap refresh token setelah digunakan, dan mencabut semua refresh token untuk authorization tersebut jika sebuah refresh token yang sudah digunakan dan tidak valid diberikan kembali. | 1 |
| **10.4.6** | Verifikasi bahwa, jika code grant digunakan, authorization server memitigasi serangan authorization code interception dengan mewajibkan proof key for code exchange (PKCE). Untuk authorization request, authorization server harus mewajibkan nilai 'code_challenge' yang valid dan tidak boleh menerima nilai 'code_challenge_method' 'plain'. Untuk token request, authorization server harus mewajibkan validasi parameter 'code_verifier'. | 2 |
| **10.4.7** | Verifikasi bahwa jika authorization server mendukung unauthenticated dynamic client registration, authorization server tersebut memitigasi risiko aplikasi client yang berbahaya. Authorization server harus memvalidasi metadata client seperti URI mana pun yang telah didaftarkan, memastikan persetujuan pengguna, dan memberikan peringatan kepada pengguna sebelum memproses sebuah authorization request dengan aplikasi client yang tidak tepercaya. | 2 |
| **10.4.8** | Verifikasi bahwa refresh token memiliki masa kedaluwarsa mutlak (absolute expiration), termasuk jika sliding refresh token expiration diterapkan. | 2 |
| **10.4.9** | Verifikasi bahwa refresh token dan reference access token dapat dicabut (revoked) oleh pengguna yang berwenang melalui user interface authorization server, guna memitigasi risiko client yang berbahaya atau token yang dicuri. | 2 |
| **10.4.10** | Verifikasi bahwa confidential client diautentikasi untuk client-to-authorized server backchannel requests seperti token requests, pushed authorization requests (PAR), dan token revocation requests. | 2 |
| **10.4.11** | Verifikasi bahwa konfigurasi authorization server hanya memberikan scopes yang diperlukan kepada OAuth client. | 2 |
| **10.4.12** | Verifikasi bahwa untuk client tertentu, authorization server hanya mengizinkan nilai 'response_mode' yang memang perlu digunakan oleh client tersebut. Misalnya, dengan membuat authorization server memvalidasi nilai ini terhadap nilai yang diharapkan atau dengan menggunakan pushed authorization request (PAR) atau JWT-secured Authorization Request (JAR). | 3 |
| **10.4.13** | Verifikasi bahwa grant type 'code' selalu digunakan bersama dengan pushed authorization requests (PAR). | 3 |
| **10.4.14** | Verifikasi bahwa authorization server hanya menerbitkan sender-constrained (Proof-of-Possession) access token, baik menggunakan certificate-bound access token dengan mutual TLS (mTLS) maupun DPoP-bound access token (Demonstration of Proof of Possession). | 3 |
| **10.4.15** | Verifikasi bahwa, untuk sebuah server-side client (yang tidak dieksekusi pada perangkat pengguna akhir), authorization server memastikan bahwa nilai parameter 'authorization_details' berasal dari backend client dan bahwa pengguna tidak telah memanipulasinya (tampered with). Misalnya, dengan mewajibkan penggunaan pushed authorization request (PAR) atau JWT-secured Authorization Request (JAR). | 3 |
| **10.4.16** | Verifikasi bahwa client bersifat confidential dan authorization server mewajibkan penggunaan metode client authentication yang kuat (berbasis kriptografi kunci publik dan tahan terhadap serangan replay), seperti mutual TLS ('tls_client_auth', 'self_signed_tls_client_auth') atau private key JWT ('private_key_jwt'). | 3 |

## V10.5 OIDC Client

Karena OIDC relying party bertindak sebagai sebuah OAuth client, persyaratan dari bagian "OAuth Client" juga berlaku.

Perlu dicatat bahwa bagian "Authentication with an Identity Provider" pada bab "Authentication" juga memuat persyaratan umum yang relevan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **10.5.1** | Verifikasi bahwa client (sebagai relying party) memitigasi serangan ID Token replay. Misalnya, dengan memastikan bahwa claim 'nonce' pada ID Token sesuai dengan nilai 'nonce' yang dikirimkan pada authentication request ke OpenID Provider (dalam OAuth2 disebut sebagai authorization request yang dikirimkan ke authorization server). | 2 |
| **10.5.2** | Verifikasi bahwa client mengidentifikasi pengguna secara unik dari claims pada ID Token, biasanya claim 'sub', yang tidak dapat dipindahtangankan (reassigned) ke pengguna lain (dalam scope sebuah identity provider). | 2 |
| **10.5.3** | Verifikasi bahwa client menolak upaya authorization server yang berbahaya untuk menyamar sebagai authorization server lain melalui metadata authorization server. Client harus menolak metadata authorization server jika URL issuer pada metadata authorization server tersebut tidak sama persis dengan URL issuer yang telah dikonfigurasi sebelumnya (pre-configured) dan diharapkan oleh client. | 2 |
| **10.5.4** | Verifikasi bahwa client memvalidasi bahwa ID Token memang dimaksudkan untuk digunakan oleh client tersebut (audience) dengan memeriksa bahwa claim 'aud' dari token sesuai dengan nilai 'client_id' untuk client tersebut. | 2 |
| **10.5.5** | Verifikasi bahwa, saat menggunakan OIDC back-channel logout, relying party memitigasi denial of service melalui forced logout dan cross-JWT confusion pada alur logout. Client harus memverifikasi bahwa logout token memiliki tipe yang benar dengan nilai 'logout+jwt', mengandung claim 'event' dengan nama member yang benar, dan tidak mengandung claim 'nonce'. Perlu dicatat bahwa juga direkomendasikan untuk memiliki masa kedaluwarsa yang singkat (misalnya, 2 menit). | 2 |

## V10.6 OpenID Provider

Karena OpenID Provider bertindak sebagai OAuth authorization server, persyaratan dari bagian "OAuth Authorization Server" juga berlaku.

Perlu dicatat bahwa jika menggunakan ID Token flow (bukan code flow), tidak ada access token yang diterbitkan, dan banyak persyaratan untuk OAuth AS tidak berlaku.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **10.6.1** | Verifikasi bahwa OpenID Provider hanya mengizinkan nilai 'code', 'ciba', 'id_token', atau 'id_token code' untuk response mode. Perlu dicatat bahwa 'code' lebih diutamakan daripada 'id_token code' (OIDC Hybrid flow), dan 'token' (Implicit flow apa pun) tidak boleh digunakan. | 2 |
| **10.6.2** | Verifikasi bahwa OpenID Provider memitigasi denial of service melalui forced logout. Dengan memperoleh konfirmasi eksplisit dari pengguna akhir atau, jika ada, memvalidasi parameter pada logout request (yang diinisiasi oleh relying party), seperti 'id_token_hint'. | 2 |

## V10.7 Manajemen Consent

Persyaratan ini membahas verifikasi consent pengguna oleh authorization server. Tanpa verifikasi consent pengguna yang tepat, pelaku jahat dapat memperoleh permission atas nama pengguna melalui spoofing atau social-engineering.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **10.7.1** | Verifikasi bahwa authorization server memastikan pengguna menyetujui (consent) setiap authorization request. Jika identitas client tidak dapat dipastikan, authorization server harus selalu secara eksplisit meminta consent kepada pengguna. | 2 |
| **10.7.2** | Verifikasi bahwa saat authorization server meminta consent pengguna, authorization server tersebut menyajikan informasi yang cukup dan jelas mengenai apa yang sedang disetujui. Jika berlaku, hal ini harus mencakup sifat dari authorization yang diminta (biasanya berdasarkan scope, resource server, detail authorization Rich Authorization Requests (RAR)), identitas aplikasi yang diberi wewenang, dan masa berlaku dari authorization tersebut. | 2 |
| **10.7.3** | Verifikasi bahwa pengguna dapat meninjau, mengubah, dan mencabut consent yang telah diberikan pengguna melalui authorization server. | 2 |

## Referensi

Untuk informasi lebih lanjut mengenai OAuth, silakan lihat:

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

Untuk persyaratan terkait OAuth pada ASVS, RFC berikut yang telah dipublikasikan maupun yang masih berstatus draft digunakan:

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

Untuk informasi lebih lanjut mengenai OpenID Connect, silakan lihat:

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
