# V12 Secure Communication

## Tujuan Kontrol

Bab ini mencakup persyaratan yang terkait dengan mekanisme spesifik yang harus diterapkan untuk melindungi data yang sedang ditransmisikan (in transit), baik antara client pengguna akhir dan backend service, maupun antara layanan internal dan backend service.

Konsep umum yang didorong oleh bab ini meliputi:

* Memastikan bahwa komunikasi dienkripsi secara eksternal, dan idealnya juga secara internal.
* Mengonfigurasi mekanisme enkripsi menggunakan panduan terkini, termasuk algoritma dan cipher yang direkomendasikan.
* Memastikan bahwa komunikasi tidak diintersep oleh pihak yang tidak berwenang melalui penggunaan sertifikat yang ditandatangani (signed certificates).

Selain menguraikan prinsip umum dan praktik terbaik, ASVS juga menyediakan informasi teknis yang lebih mendalam mengenai kekuatan kriptografi pada Appendix C - Cryptography Standards.

## V12.1 Panduan Umum Keamanan TLS

Bagian ini menyediakan panduan awal mengenai cara mengamankan komunikasi TLS. Alat (tools) yang selalu diperbarui harus digunakan untuk meninjau konfigurasi TLS secara berkelanjutan.

Meskipun penggunaan sertifikat TLS wildcard tidak secara inheren tidak aman, kompromi terhadap sebuah sertifikat yang digunakan di seluruh environment yang dimiliki (misalnya, produksi, staging, development, dan test) dapat mengakibatkan kompromi terhadap postur keamanan aplikasi yang menggunakannya. Perlindungan, pengelolaan yang tepat, serta penggunaan sertifikat TLS terpisah pada environment yang berbeda-beda harus diterapkan jika memungkinkan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **12.1.1** | Verifikasi bahwa hanya versi terbaru protokol TLS yang direkomendasikan yang diaktifkan, seperti TLS 1.2 dan TLS 1.3. Versi terbaru dari protokol TLS harus menjadi opsi yang diutamakan (preferred). | 1 |
| **12.1.2** | Verifikasi bahwa hanya cipher suite yang direkomendasikan yang diaktifkan, dengan cipher suite terkuat diatur sebagai yang diutamakan (preferred). Aplikasi L3 hanya boleh mendukung cipher suite yang menyediakan forward secrecy. | 2 |
| **12.1.3** | Verifikasi bahwa aplikasi memvalidasi bahwa sertifikat client mTLS tepercaya sebelum menggunakan identitas sertifikat tersebut untuk authentication atau authorization. | 2 |
| **12.1.4** | Verifikasi bahwa mekanisme pencabutan sertifikat (certificate revocation) yang tepat, seperti Online Certificate Status Protocol (OCSP) Stapling, diaktifkan dan dikonfigurasi. | 3 |
| **12.1.5** | Verifikasi bahwa Encrypted Client Hello (ECH) diaktifkan pada pengaturan TLS aplikasi guna mencegah terekspornya metadata sensitif, seperti Server Name Indication (SNI), selama proses TLS handshake. | 3 |

## V12.2 Komunikasi HTTPS dengan Layanan yang Menghadap Eksternal

Pastikan seluruh lalu lintas HTTP menuju layanan yang menghadap eksternal (external-facing) yang diekspos oleh aplikasi dikirimkan secara terenkripsi, dengan sertifikat yang tepercaya secara publik.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **12.2.1** | Verifikasi bahwa TLS digunakan untuk seluruh konektivitas antara client dan layanan berbasis HTTP yang menghadap eksternal, dan tidak berpindah kembali (fall back) ke komunikasi yang tidak aman atau tidak terenkripsi. | 1 |
| **12.2.2** | Verifikasi bahwa layanan yang menghadap eksternal menggunakan sertifikat TLS yang tepercaya secara publik. | 1 |

## V12.3 Keamanan Komunikasi Umum Antar Layanan (Service to Service)

Komunikasi server (baik internal maupun eksternal) melibatkan lebih dari sekadar HTTP. Koneksi menuju dan dari sistem lain juga harus aman, idealnya menggunakan TLS.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **12.3.1** | Verifikasi bahwa sebuah protokol terenkripsi seperti TLS digunakan untuk seluruh koneksi masuk (inbound) dan keluar (outbound) menuju dan dari aplikasi, termasuk sistem monitoring, alat manajemen, remote access dan SSH, middleware, database, mainframe, sistem partner, atau API eksternal. Server tidak boleh berpindah kembali (fall back) ke protokol yang tidak aman atau tidak terenkripsi. | 2 |
| **12.3.2** | Verifikasi bahwa client TLS memvalidasi sertifikat yang diterima sebelum berkomunikasi dengan server TLS. | 2 |
| **12.3.3** | Verifikasi bahwa TLS atau mekanisme transport encryption lain yang sesuai digunakan untuk seluruh konektivitas antara layanan internal berbasis HTTP dalam aplikasi, dan tidak berpindah kembali (fall back) ke komunikasi yang tidak aman atau tidak terenkripsi. | 2 |
| **12.3.4** | Verifikasi bahwa koneksi TLS antar layanan internal menggunakan sertifikat yang tepercaya. Ketika sertifikat yang dihasilkan secara internal atau self-signed digunakan, layanan yang mengonsumsi (consuming service) harus dikonfigurasi untuk hanya mempercayai CA internal tertentu dan sertifikat self-signed tertentu. | 2 |
| **12.3.5** | Verifikasi bahwa layanan yang berkomunikasi secara internal dalam suatu sistem (intra-service communications) menggunakan strong authentication untuk memastikan bahwa setiap endpoint terverifikasi. Metode strong authentication, seperti TLS client authentication, harus diterapkan untuk memastikan identitas, menggunakan public-key infrastructure dan mekanisme yang tahan terhadap serangan replay. Untuk arsitektur microservice, pertimbangkan penggunaan sebuah service mesh untuk menyederhanakan pengelolaan sertifikat dan meningkatkan keamanan. | 3 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP - Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
* [Panduan konfigurasi Server Side TLS dari Mozilla](https://wiki.mozilla.org/Security/Server_Side_TLS)
* [Alat dari Mozilla untuk menghasilkan konfigurasi TLS yang telah dikenal baik](https://ssl-config.mozilla.org/).
* [O-Saft - Proyek OWASP untuk memvalidasi konfigurasi TLS](https://owasp.org/www-project-o-saft/)
