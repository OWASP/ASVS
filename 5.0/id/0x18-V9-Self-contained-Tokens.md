# V9 Self-contained Tokens

## Tujuan Kontrol

Konsep self-contained token disebutkan dalam RFC 6749 OAuth 2.0 asli dari tahun 2012. Istilah ini merujuk pada sebuah token yang berisi data atau claims yang akan diandalkan oleh layanan penerima untuk membuat keputusan keamanan. Hal ini perlu dibedakan dari token sederhana yang hanya berisi sebuah identifier, yang digunakan oleh layanan penerima untuk mencari data secara lokal. Contoh paling umum dari self-contained token adalah JSON Web Tokens (JWT) dan SAML assertions.

Penggunaan self-contained token telah menjadi sangat luas, bahkan di luar OAuth dan OIDC. Pada saat yang sama, keamanan mekanisme ini bergantung pada kemampuan untuk memvalidasi integritas token dan memastikan bahwa token tersebut valid untuk konteks tertentu. Terdapat banyak jebakan (pitfalls) dalam proses ini, dan bab ini menyediakan detail spesifik mengenai mekanisme yang harus dimiliki oleh aplikasi untuk mencegahnya.

## V9.1 Sumber dan Integritas Token

Bagian ini mencakup persyaratan untuk memastikan bahwa token telah dihasilkan oleh pihak tepercaya dan tidak telah dimanipulasi (tampered with).

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **9.1.1** | Verifikasi bahwa self-contained token divalidasi menggunakan digital signature atau MAC-nya untuk melindungi dari manipulasi (tampering) sebelum menerima isi token tersebut. | 1 |
| **9.1.2** | Verifikasi bahwa hanya algoritma yang terdapat pada allowlist yang dapat digunakan untuk membuat dan memverifikasi self-contained token, untuk konteks tertentu. Allowlist tersebut harus mencakup algoritma yang diizinkan, idealnya hanya algoritma simetris atau asimetris saja, dan tidak boleh mencakup algoritma 'None'. Jika baik algoritma simetris maupun asimetris harus didukung, kontrol tambahan diperlukan untuk mencegah key confusion. | 1 |
| **9.1.3** | Verifikasi bahwa key material yang digunakan untuk memvalidasi self-contained token berasal dari sumber tepercaya yang telah dikonfigurasi sebelumnya (pre-configured) untuk token issuer tersebut, guna mencegah penyerang menentukan sumber dan key yang tidak tepercaya. Untuk JWT dan struktur JWS lainnya, header seperti 'jku', 'x5u', dan 'jwk' harus divalidasi terhadap allowlist sumber tepercaya. | 1 |

## V9.2 Konten Token

Sebelum membuat keputusan keamanan berdasarkan konten dari sebuah self-contained token, perlu dilakukan validasi bahwa token tersebut telah dipresentasikan dalam masa berlakunya (validity period) dan bahwa token tersebut memang dimaksudkan untuk digunakan oleh layanan penerima serta untuk tujuan token tersebut dipresentasikan. Hal ini membantu menghindari penggunaan silang (cross-usage) yang tidak aman antar layanan yang berbeda atau dengan jenis token yang berbeda dari issuer yang sama.

Persyaratan spesifik untuk OAuth dan OIDC dibahas pada bab tersendiri.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **9.2.1** | Verifikasi bahwa, jika sebuah rentang waktu validitas (validity time span) terdapat pada data token, token dan isinya hanya diterima jika waktu verifikasi berada dalam rentang waktu validitas tersebut. Misalnya, untuk JWT, claims 'nbf' dan 'exp' harus diverifikasi. | 1 |
| **9.2.2** | Verifikasi bahwa layanan yang menerima sebuah token memvalidasi bahwa token tersebut memiliki tipe yang benar dan dimaksudkan untuk tujuan yang sesuai sebelum menerima isi token tersebut. Misalnya, hanya access token yang dapat diterima untuk keputusan authorization dan hanya ID Token yang dapat digunakan untuk membuktikan autentikasi pengguna. | 2 |
| **9.2.3** | Verifikasi bahwa layanan hanya menerima token yang dimaksudkan untuk digunakan dengan layanan tersebut (audience). Untuk JWT, hal ini dapat dicapai dengan memvalidasi claim 'aud' terhadap allowlist yang didefinisikan pada layanan tersebut. | 2 |
| **9.2.4** | Verifikasi bahwa, jika sebuah token issuer menggunakan private key yang sama untuk menerbitkan token bagi audience yang berbeda-beda, token yang diterbitkan tersebut mengandung sebuah audience restriction yang secara unik mengidentifikasi audience yang dituju. Hal ini akan mencegah sebuah token digunakan kembali dengan audience yang tidak dimaksudkan. Jika audience identifier disediakan secara dinamis (dynamically provisioned), token issuer harus memvalidasi audience tersebut guna memastikan bahwa hal ini tidak mengakibatkan audience impersonation. | 2 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP JSON Web Token Cheat Sheet for Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) (namun memiliki panduan umum yang berguna)