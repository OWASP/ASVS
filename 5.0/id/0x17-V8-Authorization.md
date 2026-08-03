# V8 Authorization

## Tujuan Kontrol

Authorization memastikan bahwa akses hanya diberikan kepada consumer yang diizinkan (pengguna, server, dan client lainnya). Untuk menegakkan Principle of Least Privilege (POLP), aplikasi yang diverifikasi harus memenuhi persyaratan tingkat tinggi berikut:

* Mendokumentasikan aturan authorization, termasuk faktor pengambilan keputusan dan konteks lingkungan (environmental contexts).
* Consumer hanya boleh memiliki akses terhadap resource yang diizinkan oleh entitlement yang telah ditentukan bagi mereka.

## V8.1 Dokumentasi Authorization

Dokumentasi authorization yang komprehensif sangat penting untuk memastikan bahwa keputusan keamanan diterapkan secara konsisten, dapat diaudit, dan selaras dengan kebijakan organisasi. Hal ini mengurangi risiko akses tidak sah dengan membuat persyaratan keamanan menjadi jelas dan dapat ditindaklanjuti bagi developer, administrator, dan tester.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **8.1.1** | Verifikasi bahwa dokumentasi authorization mendefinisikan aturan untuk membatasi akses pada level fungsi (function-level) dan akses spesifik terhadap data berdasarkan permission consumer dan atribut resource. | 1 |
| **8.1.2** | Verifikasi bahwa dokumentasi authorization mendefinisikan aturan untuk pembatasan akses pada level field (baik untuk read maupun write) berdasarkan permission consumer dan atribut resource. Perlu dicatat bahwa aturan ini mungkin bergantung pada nilai atribut lain dari objek data terkait, seperti state atau status. | 2 |
| **8.1.3** | Verifikasi bahwa dokumentasi aplikasi mendefinisikan atribut lingkungan dan kontekstual (termasuk namun tidak terbatas pada, waktu dalam sehari, lokasi pengguna, alamat IP, atau perangkat) yang digunakan dalam aplikasi untuk membuat keputusan keamanan, termasuk yang berkaitan dengan authentication dan authorization. | 3 |
| **8.1.4** | Verifikasi bahwa dokumentasi authentication dan authorization mendefinisikan bagaimana faktor lingkungan dan kontekstual digunakan dalam pengambilan keputusan, selain authorization pada level fungsi, data spesifik, dan level field. Hal ini harus mencakup atribut yang dievaluasi, ambang batas (thresholds) risiko, dan tindakan yang diambil (misalnya, allow, challenge, deny, step-up authentication). | 3 |

## V8.2 Desain Authorization Umum

Menerapkan kontrol authorization yang terperinci pada level fungsi, data, dan field memastikan bahwa consumer hanya dapat mengakses apa yang secara eksplisit telah diberikan kepada mereka.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **8.2.1** | Verifikasi bahwa aplikasi memastikan akses pada level fungsi dibatasi hanya untuk consumer dengan permission eksplisit. | 1 |
| **8.2.2** | Verifikasi bahwa aplikasi memastikan akses spesifik terhadap data dibatasi hanya untuk consumer dengan permission eksplisit terhadap item data tertentu guna memitigasi insecure direct object reference (IDOR) dan broken object level authorization (BOLA). | 1 |
| **8.2.3** | Verifikasi bahwa aplikasi memastikan akses pada level field dibatasi hanya untuk consumer dengan permission eksplisit terhadap field tertentu guna memitigasi broken object property level authorization (BOPLA). | 2 |
| **8.2.4** | Verifikasi bahwa kontrol keamanan adaptif berdasarkan atribut lingkungan dan kontekstual consumer (seperti waktu dalam sehari, lokasi, alamat IP, atau perangkat) diterapkan untuk keputusan authentication dan authorization, sebagaimana didefinisikan dalam dokumentasi aplikasi. Kontrol ini harus diterapkan baik ketika consumer mencoba memulai sesi baru maupun selama sesi yang sedang berlangsung. | 3 |

## V8.3 Authorization Level Operasi

Penerapan segera (immediate) terhadap perubahan authorization pada tier arsitektur aplikasi yang sesuai sangat penting untuk mencegah tindakan tidak sah, terutama pada lingkungan yang dinamis.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **8.3.1** | Verifikasi bahwa aplikasi menegakkan aturan authorization pada trusted service layer dan tidak mengandalkan kontrol yang dapat dimanipulasi oleh consumer yang tidak tepercaya, seperti client-side JavaScript. | 1 |
| **8.3.2** | Verifikasi bahwa perubahan pada nilai yang menjadi dasar keputusan authorization diterapkan secara langsung (immediate). Jika perubahan tidak dapat diterapkan secara langsung (seperti ketika mengandalkan data pada self-contained token), harus ada kontrol mitigasi untuk memberikan peringatan ketika seorang consumer melakukan suatu tindakan pada saat mereka sudah tidak lagi berwenang untuk melakukannya, serta mengembalikan (revert) perubahan tersebut. Perlu dicatat bahwa alternatif ini tidak memitigasi kebocoran informasi (information leakage). | 3 |
| **8.3.3** | Verifikasi bahwa akses terhadap sebuah objek didasarkan pada permission dari subjek asal (originating subject, misalnya consumer), bukan pada permission dari perantara atau layanan mana pun yang bertindak atas nama mereka. Misalnya, jika seorang consumer memanggil sebuah web service menggunakan self-contained token untuk autentikasi, dan layanan tersebut kemudian meminta data dari layanan lain, layanan kedua tersebut harus menggunakan token milik consumer, bukan token machine-to-machine dari layanan pertama, untuk membuat keputusan permission. | 3 |

## V8.4 Pertimbangan Authorization Lainnya

Pertimbangan tambahan untuk authorization, khususnya untuk interface administratif dan lingkungan multi-tenant, membantu mencegah akses tidak sah.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **8.4.1** | Verifikasi bahwa aplikasi multi-tenant menggunakan kontrol cross-tenant untuk memastikan operasi consumer tidak akan pernah memengaruhi tenant lain yang tidak memiliki permission untuk berinteraksi dengan mereka. | 2 |
| **8.4.2** | Verifikasi bahwa akses ke interface administratif menerapkan beberapa lapisan keamanan, termasuk verifikasi identitas consumer secara berkelanjutan, penilaian postur keamanan perangkat (device security posture assessment), dan analisis risiko kontekstual, guna memastikan bahwa lokasi jaringan atau endpoint tepercaya bukan satu-satunya faktor untuk authorization, meskipun faktor-faktor tersebut dapat mengurangi kemungkinan akses tidak sah. | 3 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP Web Security Testing Guide: Authorization](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/05-Authorization_Testing)
* [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)