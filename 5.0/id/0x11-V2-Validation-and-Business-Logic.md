# V2 Validation dan Business Logic

## Tujuan Kontrol

Bab ini bertujuan untuk memastikan bahwa aplikasi yang diverifikasi memenuhi tujuan tingkat tinggi berikut:

* Input yang diterima oleh aplikasi sesuai dengan ekspektasi bisnis atau fungsional.
* Alur business logic bersifat sekuensial, diproses secara berurutan, dan tidak dapat dilewati (bypassed).
* Business logic mencakup batasan dan kontrol untuk mendeteksi serta mencegah serangan otomatis, seperti transfer dana kecil yang dilakukan terus-menerus atau menambahkan satu juta teman satu per satu.
* Alur business logic yang bernilai tinggi telah mempertimbangkan abuse case dan pelaku jahat (malicious actors), serta memiliki perlindungan terhadap serangan spoofing, tampering, information disclosure, dan elevation of privilege.

## V2.1 Dokumentasi Validation dan Business Logic

Dokumentasi validation dan business logic harus secara jelas mendefinisikan batasan business logic, aturan validasi, dan konsistensi kontekstual dari kombinasi item data, sehingga jelas apa yang perlu diimplementasikan dalam aplikasi.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **2.1.1** | Verifikasi bahwa dokumentasi aplikasi mendefinisikan aturan input validation untuk cara memeriksa validitas item data terhadap struktur yang diharapkan. Ini dapat berupa format data umum seperti nomor kartu kredit, alamat email, nomor telepon, atau dapat berupa format data internal. | 1 |
| **2.1.2** | Verifikasi bahwa dokumentasi aplikasi mendefinisikan cara memvalidasi konsistensi logis dan kontekstual dari kombinasi item data, seperti memeriksa bahwa nama kelurahan/kecamatan dan kode pos saling cocok. | 2 |
| **2.1.3** | Verifikasi bahwa ekspektasi untuk batasan dan validasi business logic didokumentasikan, baik per pengguna maupun secara global di seluruh aplikasi. | 2 |

## V2.2 Input Validation

Kontrol input validation yang efektif menegakkan ekspektasi bisnis atau fungsional terkait jenis data yang diharapkan diterima oleh aplikasi. Hal ini memastikan kualitas data yang baik dan mengurangi attack surface. Namun, hal ini tidak menghilangkan atau menggantikan kebutuhan untuk menggunakan encoding, parameterization, atau sanitization yang tepat saat data tersebut digunakan pada komponen lain atau saat disajikan sebagai output.

Dalam konteks ini, "input" dapat berasal dari berbagai sumber, termasuk HTML form fields, REST requests, parameter URL, HTTP header fields, cookies, file pada disk, database, dan API eksternal.

Sebuah kontrol business logic dapat memeriksa bahwa input tertentu adalah angka kurang dari 100. Sebuah ekspektasi fungsional dapat memeriksa bahwa suatu angka berada di bawah ambang batas tertentu, karena angka tersebut mengontrol berapa kali sebuah loop tertentu akan dijalankan, dan angka yang tinggi dapat mengakibatkan pemrosesan berlebihan serta potensi kondisi denial of service.

Meskipun schema validation tidak diwajibkan secara eksplisit, ini bisa menjadi mekanisme paling efektif untuk cakupan validasi penuh terhadap HTTP API atau interface lain yang menggunakan JSON atau XML.

Perhatikan poin-poin berikut mengenai Schema Validation:

* "Published version" dari spesifikasi JSON Schema validation dianggap sudah siap untuk produksi (production-ready), namun secara ketat belum bisa dikatakan "stabil". Saat menggunakan JSON Schema validation, pastikan tidak ada celah dengan panduan pada persyaratan di bawah ini.
* Pustaka JSON Schema validation apa pun yang digunakan juga harus dipantau dan diperbarui jika diperlukan setelah standar tersebut diresmikan.
* DTD validation tidak boleh digunakan, dan evaluasi DTD pada framework harus dinonaktifkan, guna menghindari masalah serangan XXE terhadap DTD.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **2.2.1** | Verifikasi bahwa input divalidasi untuk menegakkan ekspektasi bisnis atau fungsional terhadap input tersebut. Hal ini harus menggunakan positive validation terhadap allow list nilai, pola, dan rentang, atau berdasarkan perbandingan input dengan struktur yang diharapkan dan batasan logis sesuai aturan yang telah ditentukan sebelumnya. Untuk L1, hal ini dapat difokuskan pada input yang digunakan untuk membuat keputusan bisnis atau keamanan tertentu. Untuk L2 ke atas, hal ini harus berlaku untuk semua input. | 1 |
| **2.2.2** | Verifikasi bahwa aplikasi dirancang untuk menegakkan input validation pada trusted service layer. Meskipun client-side validation meningkatkan usability dan harus didorong penggunaannya, hal ini tidak boleh diandalkan sebagai kontrol keamanan. | 1 |
| **2.2.3** | Verifikasi bahwa aplikasi memastikan kombinasi item data yang saling terkait masuk akal (reasonable) sesuai dengan aturan yang telah ditentukan sebelumnya. | 2 |

## V2.3 Keamanan Business Logic

Bagian ini membahas persyaratan utama untuk memastikan bahwa aplikasi menegakkan proses business logic dengan cara yang benar dan tidak rentan terhadap serangan yang mengeksploitasi logika dan alur aplikasi.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **2.3.1** | Verifikasi bahwa aplikasi hanya akan memproses alur business logic untuk pengguna yang sama sesuai urutan langkah sekuensial yang diharapkan dan tanpa melewatkan langkah apa pun. | 1 |
| **2.3.2** | Verifikasi bahwa batasan business logic diimplementasikan sesuai dokumentasi aplikasi untuk menghindari kelemahan business logic dieksploitasi. | 2 |
| **2.3.3** | Verifikasi bahwa transactions digunakan pada level business logic sedemikian rupa sehingga sebuah operasi business logic berhasil dilakukan secara keseluruhan atau dikembalikan (rolled back) ke keadaan benar sebelumnya. | 2 |
| **2.3.4** | Verifikasi bahwa mekanisme locking pada level business logic digunakan untuk memastikan resource dengan kuantitas terbatas (seperti kursi teater atau slot pengiriman) tidak dapat dipesan ganda (double-booked) dengan memanipulasi logika aplikasi. | 2 |
| **2.3.5** | Verifikasi bahwa alur business logic yang bernilai tinggi memerlukan persetujuan multi-user (multi-user approval) untuk mencegah tindakan yang tidak sah atau tidak disengaja. Hal ini dapat mencakup, namun tidak terbatas pada, transfer uang dalam jumlah besar, persetujuan kontrak, akses ke informasi rahasia, atau safety override dalam proses manufaktur. | 3 |

## V2.4 Anti-automation

Bagian ini mencakup kontrol anti-automation untuk memastikan bahwa interaksi yang menyerupai interaksi manusia diperlukan dan permintaan otomatis yang berlebihan dapat dicegah.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **2.4.1** | Verifikasi bahwa kontrol anti-automation diterapkan untuk melindungi dari pemanggilan fungsi aplikasi secara berlebihan yang dapat menyebabkan data exfiltration, pembuatan data sampah (garbage-data), habisnya quota, pelanggaran rate-limit, denial-of-service, atau penggunaan berlebihan terhadap resource yang mahal. | 2 |
| **2.4.2** | Verifikasi bahwa alur business logic memerlukan timing yang realistis layaknya manusia, guna mencegah pengiriman transaksi yang berlangsung terlalu cepat. | 3 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP Web Security Testing Guide: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Web Security Testing Guide: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README)
* Anti-automation dapat dicapai dengan berbagai cara, termasuk penggunaan [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [JSON Schema](https://json-schema.org/specification.html)