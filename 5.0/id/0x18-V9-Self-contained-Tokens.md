# V9 Self-contained Tokens

## Tujuan Kontrol

Konsep **self-contained token** disebutkan dalam RFC 6749 OAuth 2.0 asli dari tahun 2012. Istilah ini merujuk pada sebuah token yang berisi data atau *claims* yang akan diandalkan oleh layanan penerima untuk membuat keputusan keamanan. Hal ini harus dibedakan dari token sederhana yang hanya berisi sebuah pengenal (*identifier*), yang digunakan oleh layanan penerima untuk mencari data secara lokal. Contoh paling umum dari *self-contained tokens* adalah *JSON Web Tokens (JWTs)* dan *SAML assertions*.

Penggunaan **self-contained tokens** telah menjadi sangat luas, bahkan di luar OAuth dan OIDC. Pada saat yang sama, keamanan mekanisme ini bergantung pada kemampuan untuk memvalidasi integritas token dan memastikan bahwa token tersebut valid untuk konteks tertentu. Terdapat banyak celah (*pitfalls*) dalam proses ini, dan bab ini memberikan rincian spesifik mengenai mekanisme yang harus diterapkan oleh aplikasi untuk mencegah hal tersebut.

## V9.1 Sumber dan integritas token

Bagian ini mencakup persyaratan untuk memastikan bahwa token telah dibuat oleh pihak yang tepercaya dan belum dimodifikasi oleh pihak yang tidak berwenang.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **9.1.1** | Pastikan bahwa **self-contained tokens** divalidasi menggunakan tanda tangan digital atau MAC untuk melindungi dari modifikasi sebelum menerima konten token tersebut. | 1 |
| **9.1.2** | Pastikan bahwa hanya algoritma dalam *allowlist* yang dapat digunakan untuk membuat dan memvalidasi **self-contained tokens**, untuk konteks tertentu. *Allowlist* tersebut harus mencakup algoritma yang diizinkan, idealnya hanya algoritma simetris atau asimetris saja, dan tidak boleh menyertakan algoritma '**None**'. Jika algoritma simetris dan asimetris harus didukung secara bersamaan, diperlukan kontrol tambahan untuk mencegah terjadinya *key confusion*. | 1 |
| **9.1.3** | Pastikan bahwa materi kunci yang digunakan untuk memvalidasi **self-contained tokens** berasal dari sumber yang telah dikonfigurasi sebelumnya secara tepercaya (*trusted pre-configured sources*) untuk penerbit token, guna mencegah penyerang menentukan sumber dan kunci yang tidak tepercaya. Untuk **JWTs** dan struktur **JWS** lainnya, *header* seperti '**jku**', '**x5u**', dan '**jwk**' harus divalidasi terhadap *allowlist* dari sumber yang tepercaya. | 1 |

## V9.2 Konten token

Sebelum membuat keputusan keamanan berdasarkan konten dari sebuah **self-contained token**, perlu dilakukan validasi bahwa token tersebut diberikan dalam masa berlakunya (*validity period*) dan memang ditujukan untuk digunakan oleh layanan penerima serta untuk tujuan awal token tersebut diberikan. Hal ini membantu menghindari penggunaan silang yang tidak aman (*insecure cross-usage*) antar layanan yang berbeda atau dengan jenis token yang berbeda dari penerbit yang sama.

Persyaratan khusus untuk OAuth dan OIDC dibahas dalam bab khusus.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **9.2.1** | Pastikan bahwa jika rentang waktu validitas ada di dalam data token, token dan isinya hanya diterima jika waktu verifikasi berada dalam rentang waktu validitas ini. Sebagai contoh, untuk **JWTs**, *claims* '**nbf**' (*not before*) dan '**exp**' (*expiration*) harus diverifikasi. | 1 |
| **9.2.2** | Pastikan bahwa layanan yang menerima token memvalidasi bahwa token tersebut adalah tipe yang benar dan dimaksudkan untuk tujuan yang sesuai sebelum menerima konten token. Sebagai contoh, hanya **access tokens** yang dapat diterima untuk keputusan otorisasi dan hanya **ID Tokens** yang dapat digunakan untuk membuktikan autentikasi pengguna. | 2 |
| **9.2.3** | Pastikan bahwa layanan hanya menerima token yang memang ditujukan untuk digunakan pada layanan tersebut (**audience**). Untuk **JWTs**, hal ini dapat dicapai dengan memvalidasi *claim* '**aud**' terhadap *allowlist* yang didefinisikan di dalam layanan. | 2 |
| **9.2.4** | Pastikan bahwa jika penerbit token menggunakan *private key* yang sama untuk menerbitkan token ke **audience** yang berbeda, token yang diterbitkan harus berisi batasan *audience* yang secara unik mengidentifikasi *audience* yang dituju. Hal ini akan mencegah token digunakan kembali pada *audience* yang tidak dimaksudkan. Jika pengenal *audience* disediakan secara dinamis, penerbit token harus memvalidasi *audience* tersebut untuk memastikan tidak terjadi *audience impersonation*. | 2 |

## Referensi

Untuk informasi selengkapnya, lihat juga:

* [CheatSheet Singkat OWASP JSON Web Token untuk Java](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) (tetapi memiliki panduan umum yang bermanfaat.)
