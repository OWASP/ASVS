# V13 Configuration

## Tujuan Kontrol

Konfigurasi default aplikasi harus aman untuk digunakan di Internet.

Bab ini menyediakan panduan mengenai berbagai konfigurasi yang diperlukan untuk mencapai hal tersebut, termasuk konfigurasi yang diterapkan selama development, build, dan deployment.

Topik yang dibahas mencakup pencegahan kebocoran data, pengelolaan komunikasi antar komponen secara aman, dan perlindungan secrets.

## V13.1 Dokumentasi Konfigurasi

Bagian ini menguraikan persyaratan dokumentasi mengenai bagaimana aplikasi berkomunikasi dengan layanan internal dan eksternal, serta teknik untuk mencegah hilangnya ketersediaan (availability) akibat layanan yang tidak dapat diakses. Bagian ini juga membahas dokumentasi yang terkait dengan secrets.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **13.1.1** | Verifikasi bahwa semua kebutuhan komunikasi untuk aplikasi terdokumentasi. Hal ini harus mencakup layanan eksternal yang diandalkan oleh aplikasi dan kasus-kasus di mana pengguna akhir mungkin dapat memberikan sebuah lokasi eksternal yang kemudian akan dihubungi oleh aplikasi. | 2 |
| **13.1.2** | Verifikasi bahwa untuk setiap layanan yang digunakan aplikasi, dokumentasi mendefinisikan jumlah maksimum koneksi paralel (concurrent) (misalnya, batas connection pool) dan bagaimana perilaku aplikasi ketika batas tersebut tercapai, termasuk mekanisme fallback atau recovery apa pun, guna mencegah kondisi denial of service. | 3 |
| **13.1.3** | Verifikasi bahwa dokumentasi aplikasi mendefinisikan strategi manajemen resource untuk setiap sistem atau layanan eksternal yang digunakannya (misalnya, database, file handles, thread, koneksi HTTP). Hal ini harus mencakup prosedur pelepasan resource (resource-release), pengaturan timeout, penanganan kegagalan, dan jika logika retry diterapkan, penentuan batas retry, delay, dan algoritma back-off. Untuk operasi request-response HTTP yang bersifat sinkron, dokumentasi harus mewajibkan timeout yang singkat dan menonaktifkan retry atau membatasi retry secara ketat guna mencegah keterlambatan yang berantai (cascading delays) dan habisnya resource. | 3 |
| **13.1.4** | Verifikasi bahwa dokumentasi aplikasi mendefinisikan secrets yang krusial bagi keamanan aplikasi serta jadwal rotasinya, berdasarkan model ancaman (threat model) organisasi dan kebutuhan bisnis. | 3 |

## V13.2 Konfigurasi Komunikasi Backend

Aplikasi berinteraksi dengan berbagai layanan, termasuk API, database, atau komponen lainnya. Komponen-komponen ini dapat dianggap internal bagi aplikasi namun tidak termasuk dalam mekanisme access control standar aplikasi, atau dapat sepenuhnya bersifat eksternal. Dalam kedua kasus tersebut, aplikasi perlu dikonfigurasi untuk berinteraksi secara aman dengan komponen-komponen ini dan, jika diperlukan, melindungi konfigurasi tersebut.

Catatan: Bab "Secure Communication" menyediakan panduan untuk enkripsi data yang sedang ditransmisikan (in transit).

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **13.2.1** | Verifikasi bahwa komunikasi antar komponen aplikasi backend yang tidak mendukung mekanisme session pengguna standar aplikasi, termasuk API, middleware, dan data layer, telah diautentikasi. Autentikasi harus menggunakan akun layanan (service accounts) individual, token jangka pendek, atau autentikasi berbasis sertifikat, dan bukan kredensial yang tidak berubah seperti password, API key, atau akun bersama (shared accounts) dengan akses istimewa (privileged access). | 2 |
| **13.2.2** | Verifikasi bahwa komunikasi antar komponen aplikasi backend, termasuk layanan lokal atau sistem operasi, API, middleware, dan data layer, dilakukan dengan akun yang diberikan hak akses (privilege) minimal yang diperlukan. | 2 |
| **13.2.3** | Verifikasi bahwa jika sebuah kredensial harus digunakan untuk autentikasi layanan, kredensial yang digunakan oleh consumer bukan merupakan kredensial default (misalnya, root/root atau admin/admin). | 2 |
| **13.2.4** | Verifikasi bahwa sebuah allowlist digunakan untuk mendefinisikan resource atau sistem eksternal yang diizinkan untuk dihubungi oleh aplikasi (misalnya, untuk outbound requests, pemuatan data, atau akses file). Allowlist ini dapat diterapkan pada application layer, web server, firewall, atau kombinasi dari beberapa lapisan yang berbeda. | 2 |
| **13.2.5** | Verifikasi bahwa web server atau application server dikonfigurasi dengan sebuah allowlist resource atau sistem yang dapat dikirimi request atau tempat pemuatan data atau file oleh server tersebut. | 2 |
| **13.2.6** | Verifikasi bahwa ketika aplikasi terhubung ke layanan terpisah, aplikasi tersebut mengikuti konfigurasi terdokumentasi untuk setiap koneksi, seperti jumlah maksimum koneksi paralel, perilaku ketika jumlah maksimum koneksi yang diizinkan tercapai, timeout koneksi, dan strategi retry. | 3 |

## V13.3 Manajemen Secret

Manajemen secret merupakan tugas konfigurasi yang esensial untuk memastikan perlindungan data yang digunakan dalam aplikasi. Persyaratan spesifik untuk cryptography dapat ditemukan pada bab "Cryptography", namun bagian ini berfokus pada aspek pengelolaan dan penanganan secrets.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **13.3.1** | Verifikasi bahwa sebuah solusi secrets management, seperti sebuah key vault, digunakan untuk membuat, menyimpan, mengontrol akses ke, dan menghapus secrets backend secara aman. Hal ini dapat mencakup password, key material, integrasi dengan database dan sistem pihak ketiga, key dan seed untuk token berbasis waktu, secrets internal lainnya, dan API key. Secrets tidak boleh disertakan dalam kode sumber aplikasi atau disertakan dalam build artifacts. Untuk aplikasi L3, hal ini harus melibatkan sebuah solusi yang didukung oleh perangkat keras (hardware-backed) seperti HSM. | 2 |
| **13.3.2** | Verifikasi bahwa akses terhadap aset secret mematuhi prinsip least privilege. | 2 |
| **13.3.3** | Verifikasi bahwa semua operasi kriptografi dilakukan menggunakan sebuah modul keamanan yang terisolasi (seperti sebuah vault atau hardware security module) guna mengelola dan melindungi key material secara aman dari paparan di luar modul keamanan tersebut. | 3 |
| **13.3.4** | Verifikasi bahwa secrets dikonfigurasi untuk kedaluwarsa dan dirotasi berdasarkan dokumentasi aplikasi. | 3 |

## V13.4 Kebocoran Informasi yang Tidak Diinginkan

Konfigurasi produksi harus diperkuat (hardened) guna menghindari terungkapnya data yang tidak diperlukan. Banyak dari masalah ini jarang dinilai sebagai risiko signifikan, namun sering kali dirangkai (chained) dengan kerentanan lainnya. Jika masalah-masalah ini tidak muncul secara default, hal tersebut akan meningkatkan tingkat kesulitan (raises the bar) untuk menyerang sebuah aplikasi.

Misalnya, menyembunyikan versi komponen server-side tidak menghilangkan kebutuhan untuk melakukan patch pada semua komponen, dan menonaktifkan folder listing tidak menghilangkan kebutuhan untuk menggunakan kontrol authorization atau menjauhkan file dari folder publik, namun hal tersebut meningkatkan tingkat kesulitan bagi penyerang.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **13.4.1** | Verifikasi bahwa aplikasi di-deploy tanpa metadata source control apa pun, termasuk folder .git atau .svn, atau dengan cara sedemikian rupa sehingga folder-folder ini tidak dapat diakses baik secara eksternal maupun oleh aplikasi itu sendiri. | 1 |
| **13.4.2** | Verifikasi bahwa mode debug dinonaktifkan untuk semua komponen pada environment produksi guna mencegah terekspornya fitur debugging dan kebocoran informasi. | 2 |
| **13.4.3** | Verifikasi bahwa web server tidak mengekspor directory listing kepada client kecuali memang secara eksplisit dimaksudkan demikian. | 2 |
| **13.4.4** | Verifikasi bahwa penggunaan metode HTTP TRACE tidak didukung pada environment produksi, guna menghindari potensi kebocoran informasi. | 2 |
| **13.4.5** | Verifikasi bahwa dokumentasi (seperti untuk API internal) dan endpoint monitoring tidak terekspos kecuali memang secara eksplisit dimaksudkan demikian. | 2 |
| **13.4.6** | Verifikasi bahwa aplikasi tidak mengekspor informasi versi terperinci dari komponen backend. | 3 |
| **13.4.7** | Verifikasi bahwa web tier dikonfigurasi untuk hanya menyajikan file dengan ekstensi file tertentu guna mencegah kebocoran informasi, konfigurasi, dan kode sumber yang tidak disengaja. | 3 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP Web Security Testing Guide: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing)
