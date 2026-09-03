# V11 Cryptography

## Tujuan Kontrol

Tujuan bab ini adalah untuk mendefinisikan praktik terbaik untuk penggunaan cryptography secara umum, serta menanamkan pemahaman mendasar mengenai prinsip-prinsip kriptografi dan mendorong pergeseran menuju pendekatan yang lebih tangguh dan modern. Bab ini mendorong hal-hal berikut:

* Menerapkan sistem kriptografi yang tangguh, yang gagal secara aman (fail securely), beradaptasi terhadap ancaman yang terus berkembang, dan tahan terhadap perkembangan di masa depan (future-proof).
* Memanfaatkan mekanisme kriptografi yang aman sekaligus selaras dengan praktik terbaik industri.
* Mempertahankan sistem manajemen kunci kriptografi yang aman dengan kontrol akses dan audit yang sesuai.
* Secara berkala mengevaluasi lanskap kriptografi untuk menilai risiko baru dan menyesuaikan algoritma yang digunakan.
* Menemukan dan mengelola kasus penggunaan kriptografi di sepanjang siklus hidup aplikasi guna memastikan bahwa semua aset kriptografi terdata dan terlindungi.

Selain menguraikan prinsip umum dan praktik terbaik, dokumen ini juga menyediakan informasi teknis yang lebih mendalam mengenai persyaratan pada Appendix C - Cryptography Standards. Hal ini mencakup algoritma dan mode yang dianggap "disetujui" (approved) untuk tujuan persyaratan pada bab ini.

Persyaratan yang menggunakan cryptography untuk menyelesaikan masalah yang berbeda, seperti secrets management atau communications security, akan berada pada bagian standar yang berbeda.

## V11.1 Inventaris dan Dokumentasi Kriptografi

Aplikasi perlu dirancang dengan arsitektur kriptografi yang kuat untuk melindungi aset data sesuai dengan klasifikasinya. Mengenkripsi segalanya adalah tindakan yang boros; tidak mengenkripsi apa pun adalah kelalaian secara hukum. Sebuah keseimbangan harus dicapai, biasanya selama tahap desain arsitektur atau desain tingkat tinggi, design sprint, atau architectural spike. Merancang cryptography secara "on the fly" atau menambahkannya belakangan (retrofitting) pasti akan memakan biaya jauh lebih besar untuk diimplementasikan secara aman dibandingkan langsung membangunnya sejak awal.

Penting untuk memastikan bahwa semua aset kriptografi secara rutin ditemukan, diinventarisasi, dan dinilai. Silakan lihat appendix untuk informasi lebih lanjut mengenai bagaimana hal ini dapat dilakukan.

Kebutuhan untuk membuat sistem kriptografi tahan di masa depan (future-proof) terhadap kemunculan quantum computing juga sangat krusial. Post-Quantum Cryptography (PQC) merujuk pada algoritma kriptografi yang dirancang untuk tetap aman terhadap serangan oleh quantum computer, yang diperkirakan akan dapat memecahkan algoritma yang banyak digunakan seperti RSA dan elliptic curve cryptography (ECC).

Silakan lihat appendix untuk panduan terkini mengenai primitif dan standar PQC yang telah diverifikasi (vetted).

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **11.1.1** | Verifikasi bahwa terdapat kebijakan terdokumentasi untuk manajemen kunci kriptografi dan sebuah siklus hidup kunci kriptografi yang mengikuti standar manajemen kunci seperti NIST SP 800-57. Hal ini harus mencakup memastikan bahwa kunci tidak dibagikan secara berlebihan (misalnya, dengan lebih dari dua entitas untuk shared secrets dan lebih dari satu entitas untuk private keys). | 2 |
| **11.1.2** | Verifikasi bahwa sebuah inventaris kriptografi dilakukan, dipelihara, diperbarui secara berkala, dan mencakup semua kunci kriptografi, algoritma, serta sertifikat yang digunakan oleh aplikasi. Inventaris tersebut juga harus mendokumentasikan di mana kunci dapat dan tidak dapat digunakan dalam sistem, serta jenis data yang dapat dan tidak dapat dilindungi menggunakan kunci tersebut. | 2 |
| **11.1.3** | Verifikasi bahwa mekanisme cryptographic discovery diterapkan untuk mengidentifikasi seluruh penggunaan cryptography dalam sistem, termasuk operasi enkripsi, hashing, dan signing. | 3 |
| **11.1.4** | Verifikasi bahwa sebuah inventaris kriptografi dipelihara. Hal ini harus mencakup sebuah rencana terdokumentasi yang menguraikan jalur migrasi menuju standar kriptografi baru, seperti post-quantum cryptography, guna mengantisipasi ancaman di masa depan. | 3 |

## V11.2 Implementasi Cryptography yang Aman

Bagian ini mendefinisikan persyaratan untuk pemilihan, implementasi, dan pengelolaan berkelanjutan terhadap algoritma kriptografi inti untuk sebuah aplikasi. Tujuannya adalah untuk memastikan bahwa hanya primitif kriptografi yang tangguh dan diterima secara industri yang digunakan, selaras dengan standar terkini (misalnya, NIST, ISO/IEC) dan praktik terbaik. Organisasi harus memastikan bahwa setiap komponen kriptografi dipilih berdasarkan bukti yang telah ditinjau sejawat (peer-reviewed) dan pengujian keamanan praktis.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **11.2.1** | Verifikasi bahwa implementasi yang telah tervalidasi secara industri (termasuk pustaka dan implementasi yang dipercepat oleh perangkat keras) digunakan untuk operasi kriptografi. | 2 |
| **11.2.2** | Verifikasi bahwa aplikasi dirancang dengan crypto agility sedemikian rupa sehingga algoritma random number, authenticated encryption, MAC, atau hashing, panjang kunci, rounds, cipher, dan mode dapat dikonfigurasi ulang, ditingkatkan (upgraded), atau diganti kapan saja, guna melindungi dari pembobolan (breaks) kriptografi. Demikian pula, harus dimungkinkan juga untuk mengganti kunci dan password serta melakukan re-enkripsi data. Hal ini akan memungkinkan peningkatan (upgrade) yang mulus menuju post-quantum cryptography (PQC), setelah implementasi dengan jaminan tinggi (high-assurance) dari skema atau standar PQC yang disetujui tersedia secara luas. | 2 |
| **11.2.3** | Verifikasi bahwa semua primitif kriptografi menggunakan tingkat keamanan minimal 128-bit berdasarkan algoritma, ukuran kunci, dan konfigurasi. Misalnya, sebuah kunci ECC 256-bit memberikan tingkat keamanan kira-kira 128 bit, sedangkan RSA memerlukan kunci 3072-bit untuk mencapai tingkat keamanan 128 bit. | 2 |
| **11.2.4** | Verifikasi bahwa semua operasi kriptografi bersifat constant-time, tanpa operasi 'short-circuit' pada perbandingan, kalkulasi, atau return, guna menghindari kebocoran informasi. | 3 |
| **11.2.5** | Verifikasi bahwa semua modul kriptografi gagal secara aman (fail securely), dan error ditangani dengan cara yang tidak memungkinkan terjadinya kerentanan, seperti serangan Padding Oracle. | 3 |

## V11.3 Algoritma Enkripsi

Algoritma authenticated encryption yang dibangun di atas AES dan CHACHA20 menjadi tulang punggung praktik kriptografi modern.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **11.3.1** | Verifikasi bahwa block mode yang tidak aman (misalnya, ECB) dan skema padding yang lemah (misalnya, PKCS#1 v1.5) tidak digunakan. | 1 |
| **11.3.2** | Verifikasi bahwa hanya cipher dan mode yang disetujui, seperti AES dengan GCM, yang digunakan. | 1 |
| **11.3.3** | Verifikasi bahwa data yang terenkripsi dilindungi dari modifikasi yang tidak sah, sebaiknya dengan menggunakan metode authenticated encryption yang disetujui atau dengan mengombinasikan metode enkripsi yang disetujui dengan algoritma MAC yang disetujui. | 2 |
| **11.3.4** | Verifikasi bahwa nonces, initialization vectors, dan angka sekali pakai (single-use numbers) lainnya tidak digunakan untuk lebih dari satu pasangan kunci enkripsi dan elemen data. Metode pembuatannya harus sesuai untuk algoritma yang digunakan. | 3 |
| **11.3.5** | Verifikasi bahwa kombinasi apa pun antara algoritma enkripsi dan algoritma MAC beroperasi dalam mode encrypt-then-MAC. | 3 |

## V11.4 Hashing dan Fungsi Berbasis Hash

Cryptographic hash digunakan dalam berbagai macam protokol kriptografi, seperti digital signatures, HMAC, key derivation functions (KDF), pembuatan bit acak (random bit generation), dan penyimpanan password. Keamanan sistem kriptografi hanya sekuat fungsi hash yang mendasarinya. Bagian ini menguraikan persyaratan untuk menggunakan fungsi hash yang aman dalam operasi kriptografi.

Untuk penyimpanan password, serta appendix kriptografi, [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms) juga akan memberikan konteks dan panduan yang berguna.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **11.4.1** | Verifikasi bahwa hanya fungsi hash yang disetujui yang digunakan untuk kasus penggunaan kriptografi secara umum, termasuk digital signatures, HMAC, KDF, dan random bit generation. Fungsi hash yang tidak diizinkan, seperti MD5, tidak boleh digunakan untuk tujuan kriptografi apa pun. | 1 |
| **11.4.2** | Verifikasi bahwa password disimpan menggunakan sebuah key derivation function yang disetujui dan membutuhkan komputasi intensif (juga dikenal sebagai "fungsi hashing password"), dengan pengaturan parameter yang dikonfigurasi berdasarkan panduan terkini. Pengaturan tersebut harus menyeimbangkan antara keamanan dan performa agar serangan brute-force cukup sulit dilakukan sesuai tingkat keamanan yang dibutuhkan. | 2 |
| **11.4.3** | Verifikasi bahwa fungsi hash yang digunakan pada digital signatures, sebagai bagian dari autentikasi data atau integritas data, tahan terhadap collision (collision resistant) dan memiliki panjang bit yang sesuai. Jika ketahanan terhadap collision dibutuhkan, panjang output harus minimal 256 bit. Jika hanya ketahanan terhadap serangan second pre-image yang dibutuhkan, panjang output harus minimal 128 bit. | 2 |
| **11.4.4** | Verifikasi bahwa aplikasi menggunakan key derivation function yang disetujui dengan parameter key stretching saat menurunkan (deriving) secret key dari password. Parameter yang digunakan harus menyeimbangkan antara keamanan dan performa untuk mencegah serangan brute-force membobol kunci kriptografi yang dihasilkan. | 2 |

## V11.5 Nilai Acak (Random Values)

Cryptographically secure Pseudo-random Number Generation (CSPRNG) sangat sulit untuk dilakukan dengan benar. Umumnya, sumber entropi yang baik dalam sebuah sistem akan cepat habis jika digunakan secara berlebihan, namun sumber dengan tingkat keacakan yang lebih rendah dapat mengakibatkan kunci dan secret yang dapat diprediksi.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **11.5.1** | Verifikasi bahwa semua angka dan string acak yang dimaksudkan untuk tidak dapat ditebak (non-guessable) harus dihasilkan menggunakan cryptographically secure pseudo-random number generator (CSPRNG) dan memiliki entropi minimal 128 bit. Perlu dicatat bahwa UUID tidak memenuhi kondisi ini. | 2 |
| **11.5.2** | Verifikasi bahwa mekanisme random number generation yang digunakan dirancang untuk bekerja secara aman, bahkan di bawah permintaan yang tinggi (heavy demand). | 3 |

## V11.6 Public Key Cryptography

Public Key Cryptography digunakan pada kondisi di mana tidak memungkinkan atau tidak diinginkan untuk membagikan sebuah secret key antar beberapa pihak.

Sebagai bagian dari hal ini, terdapat kebutuhan akan mekanisme key exchange yang disetujui, seperti Diffie-Hellman dan Elliptic Curve Diffie-Hellman (ECDH), guna memastikan bahwa sistem kriptografi tetap aman terhadap ancaman modern. Bab "Secure Communication" menyediakan persyaratan untuk TLS, sehingga persyaratan pada bagian ini dimaksudkan untuk situasi di mana Public Key Cryptography digunakan pada kasus penggunaan selain TLS.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **11.6.1** | Verifikasi bahwa hanya algoritma kriptografi dan mode operasi yang disetujui yang digunakan untuk pembuatan dan seeding kunci, serta pembuatan dan verifikasi digital signature. Algoritma pembuatan kunci tidak boleh menghasilkan kunci yang tidak aman dan rentan terhadap serangan yang telah diketahui, misalnya, kunci RSA yang rentan terhadap Fermat factorization. | 2 |
| **11.6.2** | Verifikasi bahwa algoritma kriptografi yang disetujui digunakan untuk key exchange (seperti Diffie-Hellman) dengan fokus untuk memastikan bahwa mekanisme key exchange menggunakan parameter yang aman. Hal ini akan mencegah serangan terhadap proses key establishment yang dapat mengakibatkan serangan adversary-in-the-middle atau pembobolan kriptografi. | 3 |

## V11.7 Kriptografi Data yang Sedang Digunakan (In-Use)

Melindungi data selagi sedang diproses sangatlah penting. Teknik seperti full memory encryption, enkripsi data yang sedang ditransmisikan (in transit), dan memastikan data dienkripsi secepat mungkin setelah digunakan sangat direkomendasikan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **11.7.1** | Verifikasi bahwa full memory encryption digunakan untuk melindungi data sensitif selagi sedang digunakan, mencegah akses oleh pengguna atau proses yang tidak berwenang. | 3 |
| **11.7.2** | Verifikasi bahwa data minimization memastikan hanya jumlah data minimal yang terekspos selama pemrosesan, dan pastikan data dienkripsi segera setelah digunakan atau sesegera mungkin. | 3 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP Web Security Testing Guide: Testing for Weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography)
* [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
