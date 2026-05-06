# V7 Manajemen Sesi

## Tujuan Kontrol

Mekanisme manajemen sesi memungkinkan aplikasi untuk menghubungkan interaksi pengguna dan perangkat dari waktu ke waktu, bahkan ketika menggunakan protokol komunikasi stateless (seperti HTTP). Aplikasi modern dapat menggunakan beberapa token sesi dengan karakteristik dan tujuan yang berbeda. Sistem manajemen sesi yang aman adalah sistem yang mencegah penyerang mendapatkan, memanfaatkan, atau menyalahgunakan sesi korban. Aplikasi yang memelihara sesi harus memastikan bahwa persyaratan manajemen sesi tingkat tinggi berikut ini terpenuhi:

* Sesi bersifat unik untuk setiap individu dan tidak dapat ditebak atau dibagikan.
* Sesi dinyatakan tidak berlaku ketika tidak lagi diperlukan dan di-timeout selama periode tidak aktif.

Banyak persyaratan dalam bab ini berkaitan dengan kontrol [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/) yang dipilih, dengan fokus pada ancaman umum dan kelemahan autentikasi yang sering dieksploitasi.

Perhatikan bahwa persyaratan untuk detail implementasi spesifik dari mekanisme manajemen sesi tertentu dapat ditemukan di tempat lain:

* HTTP Cookies adalah mekanisme umum untuk mengamankan token sesi. Persyaratan keamanan spesifik untuk cookies dapat ditemukan di bab "Web Frontend Security".
* Self-contained tokens sering digunakan sebagai cara untuk memelihara sesi. Persyaratan keamanan spesifik dapat ditemukan di bab "Self-contained Tokens".

## V7.1 Dokumentasi Manajemen Sesi

Tidak ada pola tunggal yang cocok untuk semua aplikasi. Oleh karena itu, tidaklah layak untuk menetapkan batasan dan limit universal yang sesuai untuk semua kasus. Analisis risiko dengan keputusan keamanan yang terdokumentasi terkait penanganan sesi harus dilakukan sebagai prasyarat sebelum implementasi dan pengujian. Ini memastikan bahwa sistem manajemen sesi disesuaikan dengan kebutuhan spesifik aplikasi.

Terlepas dari apakah mekanisme sesi stateful atau "stateless" yang dipilih, analisis harus lengkap dan terdokumentasi untuk menunjukkan bahwa solusi yang dipilih mampu memenuhi semua persyaratan keamanan yang relevan. Interaksi dengan mekanisme Single Sign-on (SSO) yang digunakan juga harus dipertimbangkan.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **7.1.1** | Verifikasi bahwa session inactivity timeout dan masa berlaku sesi maksimum absolut pengguna telah terdokumentasi, sesuai jika dikombinasikan dengan kontrol lainnya, dan dokumentasi tersebut mencakup justifikasi untuk setiap penyimpangan dari persyaratan autentikasi ulang NIST SP 800-63B. | 2 |
| **7.1.2** | Verifikasi bahwa dokumentasi menetapkan berapa banyak sesi konkuren (paralel) yang diizinkan untuk satu akun serta perilaku dan tindakan yang dimaksudkan untuk diambil ketika jumlah maksimum sesi aktif tercapai. | 2 |
| **7.1.3** | Verifikasi bahwa semua sistem yang membuat dan mengelola sesi pengguna sebagai bagian dari ekosistem federated identity management (seperti sistem SSO) didokumentasikan bersama dengan kontrol untuk mengoordinasikan masa berlaku sesi, penghentian sesi, dan kondisi lain apa pun yang memerlukan autentikasi ulang. | 2 |

## V7.2 Keamanan Manajemen Sesi Fundamental

Bagian ini memenuhi persyaratan esensial sesi yang aman dengan memverifikasi bahwa token sesi dibuat dan divalidasi secara aman.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **7.2.1** | Verifikasi bahwa aplikasi melakukan semua verifikasi token sesi menggunakan layanan backend yang tepercaya. | 1 |
| **7.2.2** | Verifikasi bahwa aplikasi menggunakan self-contained tokens atau reference tokens yang dibuat secara dinamis untuk manajemen sesi, yaitu tidak menggunakan API secrets dan kunci statis. | 1 |
| **7.2.3** | Verifikasi bahwa jika reference tokens digunakan untuk merepresentasikan sesi pengguna, token tersebut bersifat unik dan dibuat menggunakan cryptographically secure pseudo-random number generator (CSPRNG) serta memiliki setidaknya 128 bit entropi. | 1 |
| **7.2.4** | Verifikasi bahwa aplikasi membuat token sesi baru pada saat autentikasi pengguna, termasuk autentikasi ulang, dan mengakhiri token sesi yang sedang berjalan. | 1 |

## V7.3 Waktu Habis Sesi

Mekanisme session timeout berfungsi untuk meminimalkan jendela peluang bagi session hijacking dan bentuk penyalahgunaan sesi lainnya. Timeout harus memenuhi keputusan keamanan yang terdokumentasi.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **7.3.1** | Verifikasi bahwa terdapat inactivity timeout sehingga autentikasi ulang diterapkan sesuai dengan analisis risiko dan keputusan keamanan yang terdokumentasi. | 2 |
| **7.3.2** | Verifikasi bahwa terdapat masa berlaku sesi maksimum absolut sehingga autentikasi ulang diterapkan sesuai dengan analisis risiko dan keputusan keamanan yang terdokumentasi.. | 2 |

## V7.4 Pengakhiran Sesi

Pengakhiran sesi dapat ditangani baik oleh aplikasi itu sendiri maupun oleh penyedia SSO jika penyedia SSO menangani manajemen sesi alih-alih aplikasi. Mungkin perlu diputuskan apakah penyedia SSO termasuk dalam ruang lingkup saat mempertimbangkan persyaratan di bagian ini karena beberapa di antaranya mungkin dikendalikan oleh penyedia tersebut.

Pengakhiran sesi seharusnya mengakibatkan perlunya autentikasi ulang dan berlaku efektif di seluruh aplikasi, login federasi (jika ada), dan semua relying party.

Untuk mekanisme sesi stateful, pengakhiran biasanya melibatkan invalidasi sesi di backend. Dalam kasus self-contained tokens, langkah-langkah tambahan diperlukan untuk mencabut atau memblokir token-token ini, karena jika tidak, token tersebut mungkin tetap valid hingga masa berlakunya habis.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **7.4.1** | Verifikasi bahwa ketika pengakhiran sesi dipicu (seperti logout atau kedaluwarsa), aplikasi tidak mengizinkan penggunaan sesi lebih lanjut. Untuk reference tokens atau sesi stateful, ini berarti menginvalidasi data sesi di backend aplikasi. Aplikasi yang menggunakan self-contained tokens memerlukan solusi seperti memelihara daftar token yang diakhiri, tidak mengizinkan token yang dibuat sebelum tanggal dan waktu per pengguna, atau merotasi signing key per pengguna. | 1 |
| **7.4.2** | Verifikasi bahwa aplikasi mengakhiri semua sesi aktif ketika akun pengguna dinonaktifkan atau dihapus (seperti karyawan yang meninggalkan perusahaan). | 1 |
| **7.4.3** | Verifikasi bahwa aplikasi memberikan opsi untuk mengakhiri semua sesi aktif lainnya setelah berhasil mengubah atau menghapus faktor autentikasi apa pun (termasuk penggantian kata sandi melalui reset atau recovery dan, jika ada, pembaruan pengaturan MFA). | 2 |
| **7.4.4** | Verifikasi bahwa semua halaman yang memerlukan autentikasi memiliki akses yang mudah dan terlihat ke fungsionalitas logout. | 2 |
| **7.4.5** | Verifikasi bahwa administrator aplikasi dapat mengakhiri sesi aktif untuk seorang pengguna individual atau untuk semua pengguna. | 2 |

## V7.5 Upaya Pencegahan Penyalahgunaan Sesi

Bagian ini menyediakan persyaratan untuk memitigasi risiko yang ditimbulkan oleh sesi aktif yang dibajak atau disalahgunakan melalui vektor yang mengandalkan keberadaan dan kapabilitas sesi pengguna yang aktif. Sebagai contoh, menggunakan eksekusi konten berbahaya untuk memaksa browser korban yang terautentikasi melakukan suatu tindakan menggunakan sesi korban.

Perhatikan bahwa panduan spesifik level di bab "Authentication" harus dipertimbangkan saat mempertimbangkan persyaratan di bagian ini.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **7.5.1** | Verifikasi bahwa aplikasi memerlukan autentikasi ulang penuh sebelum mengizinkan modifikasi pada atribut akun sensitif yang dapat memengaruhi autentikasi seperti alamat email, nomor telepon, konfigurasi MFA, atau informasi lain yang digunakan dalam pemulihan akun. | 2 |
| **7.5.2** | Verifikasi bahwa pengguna dapat melihat dan (setelah mengautentikasi ulang dengan setidaknya satu faktor) mengakhiri sebagian atau semua sesi yang sedang aktif. | 2 |
| **7.5.3** | Verifikasi bahwa aplikasi memerlukan autentikasi lebih lanjut dengan setidaknya satu faktor atau verifikasi sekunder sebelum melakukan transaksi atau operasi yang sangat sensitif. | 3 |

## V7.6 Otentikasi Ulang Terintegrasi

Bagian ini berkaitan dengan mereka yang menulis kode Relying Party (RP) atau Identity Provider (IdP). Persyaratan ini berasal dari [NIST SP 800-63C](https://pages.nist.gov/800-63-4/sp800-63c.html) untuk Federation & Assertions.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **7.6.1** | Verifikasi bahwa masa berlaku sesi dan pengakhiran sesi antara Relying Parties (RPs) dan Identity Providers (IdPs) berperilaku sesuai yang didokumentasikan, memerlukan autentikasi ulang seperlunya seperti ketika waktu maksimum antara peristiwa autentikasi IdP tercapai. | 2 |
| **7.6.2** | Verifikasi bahwa pembuatan sesi memerlukan persetujuan pengguna atau tindakan eksplisit, mencegah pembuatan sesi aplikasi baru tanpa interaksi pengguna. | 2 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP Web Security Testing Guide: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/06-Session_Management_Testing)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
