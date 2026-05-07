# V8 Otorisasi

## Tujuan Kontrol

Otorisasi memastikan bahwa akses hanya diberikan kepada konsumen yang diizinkan (pengguna, server, dan klien lainnya). Untuk menegakkan *Principle of Least Privilege* (POLP), aplikasi yang diverifikasi harus memenuhi persyaratan tingkat tinggi berikut:

* Dokumentasikan aturan otorisasi, termasuk faktor pengambilan keputusan dan konteks lingkungan.
* Konsumen seharusnya hanya memiliki akses ke sumber daya yang diizinkan oleh hak yang ditetapkan untuk mereka.

## V8.1 Dokumentasi Otorisasi

Dokumentasi otorisasi yang komprehensif sangat penting untuk memastikan bahwa keputusan keamanan diterapkan secara konsisten, dapat diaudit, dan selaras dengan kebijakan organisasi. Ini mengurangi risiko akses tidak sah dengan membuat persyaratan keamanan menjadi jelas dan dapat ditindaklanjuti oleh pengembang, administrator, dan penguji.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **8.1.1** | Verifikasi bahwa dokumentasi otorisasi mendefinisikan aturan untuk membatasi akses function-level dan data-specific berdasarkan izin konsumen dan atribut sumber daya. | 1 |
| **8.1.2** | Verifikasi bahwa dokumentasi otorisasi mendefinisikan aturan untuk pembatasan akses field-level (baik baca maupun tulis) berdasarkan izin konsumen dan atribut sumber daya. Perhatikan bahwa aturan ini mungkin bergantung pada nilai atribut lain dari objek data yang relevan, seperti state atau status. | 2 |
| **8.1.3** | Verifikasi bahwa dokumentasi aplikasi mendefinisikan atribut lingkungan dan kontekstual (termasuk namun tidak terbatas pada, waktu, lokasi pengguna, alamat IP, atau perangkat) yang digunakan dalam aplikasi untuk membuat keputusan keamanan, termasuk yang berkaitan dengan autentikasi dan otorisasi. | 3 |
| **8.1.4** | Verifikasi bahwa dokumentasi autentikasi dan otorisasi mendefinisikan bagaimana faktor lingkungan dan kontekstual digunakan dalam pengambilan keputusan, selain otorisasi function-level, data-specific, dan field-level. Ini harus mencakup atribut yang dievaluasi, ambang batas risiko, dan tindakan yang diambil (misalnya, izinkan, tantang, tolak, step-up authentication). | 3 |

## V8.2 Desain Otorisasi Umum

Menerapkan kontrol otorisasi granular pada level fungsi, data, dan field memastikan bahwa konsumen hanya dapat mengakses apa yang telah secara eksplisit diberikan kepada mereka.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **8.2.1** | Verifikasi bahwa aplikasi memastikan akses function-level dibatasi hanya untuk konsumen dengan izin eksplisit. | 1 |
| **8.2.2** | Verifikasi bahwa aplikasi memastikan akses data-specific dibatasi hanya untuk konsumen dengan izin eksplisit ke item data tertentu untuk memitigasi insecure direct object reference (IDOR) dan broken object level authorization (BOLA). | 1 |
| **8.2.3** | Verifikasi bahwa aplikasi memastikan akses field-level dibatasi hanya untuk konsumen dengan izin eksplisit ke field tertentu untuk memitigasi broken object property level authorization (BOPLA). | 2 |
| **8.2.4** | Verifikasi bahwa kontrol keamanan adaptif berdasarkan atribut lingkungan dan kontekstual konsumen (seperti waktu, lokasi, alamat IP, atau perangkat) diimplementasikan untuk keputusan autentikasi dan otorisasi, seperti yang didefinisikan dalam dokumentasi aplikasi. Kontrol ini harus diterapkan ketika konsumen mencoba memulai sesi baru dan juga selama sesi berlangsung. | 3 |

## V8.3 Otorisasi Tingkat Operasi

Penerapan segera perubahan otorisasi di tier yang sesuai dalam arsitektur aplikasi sangat penting untuk mencegah tindakan yang tidak sah, terutama dalam lingkungan yang dinamis.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **8.3.1** | Verifikasi bahwa aplikasi menegakkan aturan otorisasi di lapisan layanan tepercaya dan tidak bergantung pada kontrol yang dapat dimanipulasi oleh konsumen yang tidak tepercaya, seperti JavaScript sisi klien. | 1 |
| **8.3.2** | Verifikasi bahwa perubahan pada nilai yang menjadi dasar keputusan otorisasi diterapkan segera. Jika perubahan tidak dapat diterapkan segera, (seperti ketika bergantung pada data di self-contained tokens), harus ada kontrol mitigasi untuk memberi peringatan ketika konsumen melakukan tindakan saat mereka tidak lagi berwenang untuk melakukannya dan mengembalikan perubahan tersebut. Perhatikan bahwa alternatif ini tidak akan memitigasi kebocoran informasi. | 3 |
| **8.3.3** | Verifikasi bahwa akses ke suatu objek didasarkan pada izin subjek asal (misalnya konsumen), bukan pada izin perantara atau layanan apa pun yang bertindak atas nama mereka. Sebagai contoh, jika konsumen memanggil layanan web menggunakan self-contained token untuk autentikasi, dan layanan tersebut kemudian meminta data dari layanan lain, layanan kedua akan menggunakan token konsumen, bukan token machine-to-machine dari layanan pertama, untuk membuat keputusan izin. | 3 |

## V8.4 Pertimbangan Otorisasi Lainnya

Pertimbangan tambahan untuk otorisasi, khususnya untuk antarmuka administratif dan lingkungan multi-tenant, membantu mencegah akses tanpa izin.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **8.4.1** | Pastikan bahwa aplikasi multi-tenant menggunakan kontrol lintas-tenant untuk menjamin bahwa operasi konsumen tidak akan pernah memengaruhi tenant yang tidak memiliki izin untuk berinteraksi dengannya. | 2 |
| **8.4.2** | Pastikan bahwa akses ke antarmuka administratif menggabungkan beberapa lapisan keamanan, termasuk *continuous consumer identity verification*, penilaian *device security posture*, dan *contextual risk analysis*, untuk memastikan bahwa lokasi jaringan atau *trusted endpoints* bukan merupakan satu-satunya faktor otorisasi meskipun hal tersebut dapat mengurangi kemungkinan akses yang tidak sah. | 3 |

## Referensi

Untuk informasi selengkapnya, lihat juga:

* [OWASP Web Security Testing Guide: Authorization](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/05-Authorization_Testing)
* [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
