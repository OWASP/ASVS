# V7 Session Management

## Tujuan Kontrol

Mekanisme session management memungkinkan aplikasi untuk mengaitkan interaksi pengguna dan perangkat dari waktu ke waktu, bahkan ketika menggunakan protokol komunikasi yang stateless (seperti HTTP). Aplikasi modern dapat menggunakan beberapa session token dengan karakteristik dan tujuan yang berbeda. Sistem session management yang aman adalah sistem yang mencegah penyerang memperoleh, memanfaatkan, atau menyalahgunakan sesi milik korban. Aplikasi yang mengelola sesi harus memastikan bahwa persyaratan tingkat tinggi berikut mengenai session management terpenuhi:

* Sesi bersifat unik untuk setiap individu dan tidak dapat ditebak atau dibagikan.
* Sesi menjadi tidak valid ketika sudah tidak diperlukan lagi dan mengalami timeout selama periode tidak aktif.

Banyak persyaratan dalam bab ini terkait dengan kontrol terpilih dari [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/), yang berfokus pada ancaman umum dan kelemahan autentikasi yang sering dieksploitasi.

Perlu dicatat bahwa persyaratan untuk detail implementasi spesifik dari mekanisme session management tertentu dapat ditemukan di tempat lain:

* HTTP Cookies merupakan mekanisme umum untuk mengamankan session token. Persyaratan keamanan spesifik untuk cookie dapat ditemukan pada bab "Web Frontend Security".
* Self-contained tokens sering digunakan sebagai cara untuk mempertahankan sesi. Persyaratan keamanan spesifik dapat ditemukan pada bab "Self-contained Tokens".

## V7.1 Dokumentasi Session Management

Tidak ada satu pola yang cocok untuk semua aplikasi. Oleh karena itu, tidak memungkinkan untuk mendefinisikan batasan dan limit universal yang cocok untuk semua kasus. Sebuah analisis risiko dengan keputusan keamanan yang terdokumentasi terkait penanganan sesi harus dilakukan sebagai prasyarat sebelum implementasi dan pengujian. Hal ini memastikan bahwa sistem session management disesuaikan dengan kebutuhan spesifik aplikasi.

Terlepas dari apakah mekanisme sesi yang dipilih bersifat stateful atau "stateless", analisis tersebut harus lengkap dan terdokumentasi untuk menunjukkan bahwa solusi yang dipilih mampu memenuhi semua persyaratan keamanan yang relevan. Interaksi dengan mekanisme Single Sign-on (SSO) yang digunakan juga harus dipertimbangkan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **7.1.1** | Verifikasi bahwa inactivity timeout sesi pengguna dan absolute maximum session lifetime terdokumentasi, sesuai jika dikombinasikan dengan kontrol lainnya, dan bahwa dokumentasi tersebut mencakup justifikasi untuk setiap penyimpangan dari persyaratan re-authentication pada NIST SP 800-63B. | 2 |
| **7.1.2** | Verifikasi bahwa dokumentasi mendefinisikan berapa banyak sesi paralel (concurrent) yang diizinkan untuk satu akun serta perilaku dan tindakan yang dimaksudkan ketika jumlah maksimum sesi aktif tercapai. | 2 |
| **7.1.3** | Verifikasi bahwa semua sistem yang membuat dan mengelola sesi pengguna sebagai bagian dari ekosistem federated identity management (seperti sistem SSO) terdokumentasi beserta kontrol untuk mengoordinasikan session lifetime, terminasi, dan kondisi lain apa pun yang memerlukan re-authentication. | 2 |

## V7.2 Keamanan Dasar Session Management

Bagian ini memenuhi persyaratan mendasar dari sesi yang aman dengan memverifikasi bahwa session token dihasilkan dan divalidasi secara aman.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **7.2.1** | Verifikasi bahwa aplikasi melakukan seluruh verifikasi session token menggunakan layanan backend yang tepercaya. | 1 |
| **7.2.2** | Verifikasi bahwa aplikasi menggunakan self-contained token atau reference token yang dihasilkan secara dinamis untuk session management, yaitu tidak menggunakan API secrets dan keys yang statis. | 1 |
| **7.2.3** | Verifikasi bahwa jika reference token digunakan untuk merepresentasikan sesi pengguna, token tersebut bersifat unik dan dihasilkan menggunakan cryptographically secure pseudo-random number generator (CSPRNG) serta memiliki entropi minimal 128 bit. | 1 |
| **7.2.4** | Verifikasi bahwa aplikasi menghasilkan session token baru pada saat autentikasi pengguna, termasuk re-authentication, dan menghentikan session token yang sedang berlaku (current). | 1 |

## V7.3 Session Timeout

Mekanisme session timeout berfungsi untuk meminimalkan jendela peluang (window of opportunity) terjadinya session hijacking dan bentuk penyalahgunaan sesi lainnya. Timeout harus memenuhi keputusan keamanan yang terdokumentasi.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **7.3.1** | Verifikasi bahwa terdapat inactivity timeout sedemikian rupa sehingga re-authentication diberlakukan sesuai dengan analisis risiko dan keputusan keamanan yang terdokumentasi. | 2 |
| **7.3.2** | Verifikasi bahwa terdapat absolute maximum session lifetime sedemikian rupa sehingga re-authentication diberlakukan sesuai dengan analisis risiko dan keputusan keamanan yang terdokumentasi. | 2 |

## V7.4 Terminasi Sesi

Terminasi sesi dapat ditangani baik oleh aplikasi itu sendiri maupun oleh penyedia SSO jika penyedia SSO yang menangani session management, bukan aplikasi. Mungkin perlu ditentukan apakah penyedia SSO termasuk dalam scope saat mempertimbangkan persyaratan pada bagian ini, karena beberapa hal mungkin dikendalikan oleh penyedia tersebut.

Terminasi sesi harus mengakibatkan diperlukannya re-authentication dan efektif di seluruh aplikasi, federated login (jika ada), dan pihak-pihak terkait (relying parties) lainnya.

Untuk mekanisme sesi stateful, terminasi umumnya melibatkan invalidasi sesi pada backend. Dalam kasus self-contained token, langkah tambahan diperlukan untuk mencabut (revoke) atau memblokir token tersebut, karena jika tidak, token tersebut dapat tetap valid hingga masa berlakunya habis (expiration).

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **7.4.1** | Verifikasi bahwa ketika terminasi sesi dipicu (seperti logout atau expiration), aplikasi melarang penggunaan sesi tersebut lebih lanjut. Untuk reference token atau sesi stateful, hal ini berarti melakukan invalidasi terhadap data sesi pada backend aplikasi. Aplikasi yang menggunakan self-contained token memerlukan solusi seperti mempertahankan daftar token yang telah dihentikan, melarang token yang dibuat sebelum tanggal dan waktu tertentu per pengguna, atau melakukan rotasi signing key per pengguna. | 1 |
| **7.4.2** | Verifikasi bahwa aplikasi menghentikan semua sesi aktif ketika sebuah akun pengguna dinonaktifkan atau dihapus (seperti seorang karyawan yang keluar dari perusahaan). | 1 |
| **7.4.3** | Verifikasi bahwa aplikasi memberikan opsi untuk menghentikan semua sesi aktif lainnya setelah keberhasilan perubahan atau penghapusan faktor autentikasi apa pun (termasuk perubahan password melalui reset atau recovery dan, jika ada, pembaruan pengaturan MFA). | 2 |
| **7.4.4** | Verifikasi bahwa semua halaman yang memerlukan autentikasi memiliki akses yang mudah dan terlihat jelas ke fungsionalitas logout. | 2 |
| **7.4.5** | Verifikasi bahwa administrator aplikasi mampu menghentikan sesi aktif untuk pengguna tertentu atau untuk semua pengguna. | 2 |

## V7.5 Pertahanan Terhadap Penyalahgunaan Sesi

Bagian ini menyediakan persyaratan untuk memitigasi risiko yang ditimbulkan oleh sesi aktif yang dibajak (hijacked) atau disalahgunakan melalui vektor yang bergantung pada keberadaan dan kemampuan sesi pengguna aktif. Misalnya, menggunakan eksekusi konten berbahaya untuk memaksa browser korban yang telah terautentikasi melakukan suatu tindakan menggunakan sesi milik korban.

Perlu dicatat bahwa panduan spesifik per level pada bab "Authentication" harus dipertimbangkan saat menerapkan persyaratan pada bagian ini.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **7.5.1** | Verifikasi bahwa aplikasi mewajibkan re-authentication penuh sebelum mengizinkan modifikasi terhadap atribut akun yang sensitif yang dapat memengaruhi autentikasi, seperti alamat email, nomor telepon, konfigurasi MFA, atau informasi lain yang digunakan dalam account recovery. | 2 |
| **7.5.2** | Verifikasi bahwa pengguna dapat melihat dan (setelah melakukan autentikasi ulang dengan setidaknya satu faktor) menghentikan sebagian atau seluruh sesi yang sedang aktif saat ini. | 2 |
| **7.5.3** | Verifikasi bahwa aplikasi mewajibkan autentikasi lebih lanjut dengan setidaknya satu faktor atau verifikasi sekunder sebelum melakukan transaksi atau operasi yang sangat sensitif. | 3 |

## V7.6 Federated Re-authentication

Bagian ini terkait dengan pihak yang menulis kode Relying Party (RP) atau Identity Provider (IdP). Persyaratan ini diturunkan dari [NIST SP 800-63C](https://pages.nist.gov/800-63-4/sp800-63c.html) untuk Federation & Assertions.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **7.6.1** | Verifikasi bahwa session lifetime dan terminasi antara Relying Parties (RP) dan Identity Providers (IdP) berperilaku sebagaimana yang terdokumentasi, mewajibkan re-authentication sesuai kebutuhan seperti ketika waktu maksimum antar peristiwa autentikasi IdP tercapai. | 2 |
| **7.6.2** | Verifikasi bahwa pembuatan sesi memerlukan persetujuan pengguna atau tindakan eksplisit, mencegah pembuatan sesi aplikasi baru tanpa interaksi pengguna. | 2 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP Web Security Testing Guide: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/06-Session_Management_Testing)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)