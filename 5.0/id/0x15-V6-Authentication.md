# V6 Athentication

## Objektif Kontrol

Athentication adalah proses menetapkan atau mengonfirmasi keaslian suatu individu atau perangkat [cite: 1]. Ini melibatkan verifikasi klaim yang dibuat oleh seseorang atau tentang sebuah perangkat, memastikan ketahanan terhadap peniruan (impersonation), dan mencegah pemulihan atau pencegatan sandi (password) [cite: 1].

[NIST SP 800-63](https://pages.nist.gov/800-63-3/) adalah standar modern berbasis bukti yang berharga bagi organisasi di seluruh dunia, tetapi secara khusus relevan bagi agensi AS dan mereka yang berinteraksi dengan agensi AS [cite: 1].

Meskipun banyak dari persyaratan dalam bab ini didasarkan pada bagian kedua dari standar tersebut (dikenal sebagai NIST SP 800-63B "Digital Identity Guidelines - Authentication and Lifecycle Management"), bab ini berfokus pada ancaman umum dan kelemahan Athentication yang sering dieksploitasi [cite: 1]. Bab ini tidak mencoba untuk secara komprehensif mencakup setiap poin dalam standar [cite: 1]. Untuk kasus di mana kepatuhan penuh terhadap NIST SP 800-63 diperlukan, silakan merujuk ke NIST SP 800-63 [cite: 1].

Selain itu, terminologi NIST SP 800-63 terkadang dapat berbeda, dan bab ini sering menggunakan terminologi yang lebih umum dipahami untuk meningkatkan kejelasan [cite: 1].

Fitur umum dari aplikasi yang lebih canggih adalah kemampuan untuk mengadaptasi tahapan Athentication yang diperlukan berdasarkan berbagai faktor risiko [cite: 1]. Fitur ini dibahas dalam bab "Otorisasi" (Authorization), karena mekanisme ini juga perlu dipertimbangkan untuk keputusan otorisasi [cite: 1].

## V6.1 Dokumentasi Athentication

Bagian ini berisi persyaratan yang merinci dokumentasi Athentication yang harus dikelola untuk sebuah aplikasi [cite: 1]. Hal ini sangat penting untuk mengimplementasikan dan menilai bagaimana kontrol Athentication yang relevan harus dikonfigurasi [cite: 1].

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **6.1.1** | Pastikan bahwa dokumentasi aplikasi mendefinisikan bagaimana kontrol seperti rate limiting, anti-automation, dan adaptive response, digunakan untuk bertahan dari serangan seperti credential stuffing dan password brute force [cite: 1]. Dokumentasi harus memperjelas bagaimana kontrol ini dikonfigurasi dan mencegah penguncian akun yang berbahaya (malicious account lockout) [cite: 1]. | 1 |
| **6.1.2** | Pastikan bahwa daftar kata-kata spesifik konteks didokumentasikan untuk mencegah penggunaannya dalam password [cite: 1]. Daftar tersebut dapat mencakup permutasi nama organisasi, nama produk, pengenal sistem (system identifiers), nama sandi proyek, nama departemen atau peran, dan sejenisnya [cite: 1]. | 2 |
| **6.1.3** | Pastikan bahwa, jika aplikasi mencakup beberapa jalur Athentication, semuanya didokumentasikan bersama dengan kontrol keamanan dan kekuatan Athentication yang harus diterapkan secara konsisten di seluruh jalur tersebut [cite: 1]. | 2 |

## V6.2 Keamanan Password

Password, yang disebut "Memorized Secrets" oleh NIST SP 800-63, mencakup password, passphrase, PIN, pola buka kunci (unlock patterns), dan memilih gambar anak kucing yang tepat atau elemen gambar lainnya [cite: 1]. Mereka umumnya dianggap sebagai "sesuatu yang Anda ketahui" (something you know) dan sering digunakan sebagai mekanisme single-factor authentication [cite: 1].

Oleh karena itu, bagian ini berisi persyaratan untuk memastikan bahwa password dibuat dan ditangani dengan aman [cite: 1]. Sebagian besar persyaratan adalah L1 karena mereka paling penting pada level tersebut [cite: 1]. Dari L2 dan seterusnya, mekanisme multi-factor authentication (MFA) diwajibkan, di mana password mungkin menjadi salah satu dari faktor-faktor tersebut [cite: 1].

Persyaratan di bagian ini sebagian besar terkait dengan [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) dari [Panduan NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) [cite: 1].

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **6.2.1** | Pastikan bahwa password yang diatur pengguna memiliki panjang setidaknya 8 karakter, meskipun minimal 15 karakter sangat direkomendasikan [cite: 1]. | 1 |
| **6.2.2** | Pastikan bahwa pengguna dapat mengubah password mereka [cite: 1]. | 1 |
| **6.2.3** | Pastikan bahwa fungsionalitas perubahan password memerlukan password pengguna saat ini dan yang baru [cite: 1]. | 1 |
| **6.2.4** | Pastikan bahwa password yang dikirimkan selama pendaftaran akun atau perubahan password diperiksa terhadap sekumpulan, setidaknya, 3000 password teratas yang cocok dengan kebijakan password aplikasi, mis. panjang minimum [cite: 1]. | 1 |
| **6.2.5** | Pastikan bahwa password dari komposisi apa pun dapat digunakan, tanpa aturan yang membatasi jenis karakter yang diizinkan [cite: 1]. Tidak boleh ada persyaratan untuk jumlah minimum karakter huruf besar atau kecil, angka, atau karakter khusus [cite: 1]. | 1 |
| **6.2.6** | Pastikan bahwa kolom input password menggunakan type=password untuk menutupi (mask) entri [cite: 1]. Aplikasi dapat mengizinkan pengguna untuk sementara melihat seluruh password yang ditutupi, atau karakter terakhir yang diketik dari password [cite: 1]. | 1 |
| **6.2.7** | Pastikan bahwa fungsi "paste", browser password helpers, dan external password managers diizinkan [cite: 1]. | 1 |
| **6.2.8** | Pastikan bahwa aplikasi memverifikasi password pengguna persis seperti yang diterima dari pengguna, tanpa modifikasi apa pun seperti pemotongan (truncation) atau transformasi huruf (case transformation) [cite: 1]. | 1 |
| **6.2.9** | Pastikan bahwa password dengan panjang setidaknya 64 karakter diizinkan [cite: 1]. | 2 |
| **6.2.10** | Pastikan bahwa password pengguna tetap valid sampai diketahui telah disusupi (compromised) atau pengguna memutarnya (rotates) [cite: 1]. Aplikasi tidak boleh mensyaratkan rotasi kredensial berkala [cite: 1]. | 2 |
| **6.2.11** | Pastikan bahwa daftar kata-kata spesifik konteks yang didokumentasikan digunakan untuk mencegah pembuatan password yang mudah ditebak [cite: 1]. | 2 |
| **6.2.12** | Pastikan bahwa password yang dikirimkan selama pendaftaran akun atau perubahan password diperiksa terhadap sekumpulan password yang bocor (breached passwords) [cite: 1]. | 2 |

## V6.3 Keamanan Athentication Umum

Bagian ini berisi persyaratan umum untuk keamanan mekanisme Athentication serta menetapkan ekspektasi yang berbeda untuk berbagai level [cite: 1]. Aplikasi L2 harus memaksa penggunaan multi-factor authentication (MFA) [cite: 1]. Aplikasi L3 harus menggunakan hardware-based authentication, yang dilakukan di lingkungan eksekusi yang dibuktikan dan dipercaya (Trusted Execution Environment - TEE) [cite: 1]. Ini bisa termasuk device-bound passkeys, autentikator eIDAS Level of Assurance (LoA) High, autentikator dengan jaminan NIST Authenticator Assurance Level 3 (AAL3), atau mekanisme yang setara [cite: 1].

Meskipun ini adalah sikap yang relatif agresif terhadap MFA, sangat penting untuk meningkatkan standar di seputar ini untuk melindungi pengguna, dan setiap upaya untuk melonggarkan persyaratan ini harus disertai dengan rencana yang jelas tentang bagaimana risiko seputar Athentication akan dimitigasi, dengan mempertimbangkan panduan dan penelitian NIST mengenai topik ini [cite: 1].

Perhatikan bahwa pada saat rilis, NIST SP 800-63 menganggap email [tidak dapat diterima](https://pages.nist.gov/800-63-FAQ/#q-b11) sebagai mekanisme Athentication ([salinan arsip](https://web.archive.org/web/20250330115328/https://pages.nist.gov/800-63-FAQ/#q-b11)) [cite: 1].

Persyaratan di bagian ini berkaitan dengan berbagai bagian dari [Panduan NIST](https://pages.nist.gov/800-63-3/sp800-63b.html), termasuk: [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling), dan [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding) [cite: 1].

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **6.3.1** | Pastikan bahwa kontrol untuk mencegah serangan seperti credential stuffing dan password brute force diimplementasikan sesuai dengan dokumentasi keamanan aplikasi [cite: 1]. | 1 |
| **6.3.2** | Pastikan bahwa akun pengguna default (misalnya, "root", "admin", atau "sa") tidak ada di dalam aplikasi atau dinonaktifkan [cite: 1]. | 1 |
| **6.3.3** | Pastikan bahwa mekanisme multi-factor authentication (MFA) atau kombinasi mekanisme single-factor authentication harus digunakan untuk mengakses aplikasi [cite: 1]. Untuk L3, salah satu faktor harus berupa mekanisme hardware-based authentication yang memberikan ketahanan terhadap kompromi dan peniruan (impersonation resistance) terhadap serangan phishing sekaligus memverifikasi niat untuk mengAthentication dengan mewajibkan tindakan yang dimulai oleh pengguna (seperti menekan tombol pada FIDO hardware key atau ponsel) [cite: 1]. Melonggarkan salah satu pertimbangan dalam persyaratan ini memerlukan alasan yang didokumentasikan sepenuhnya dan serangkaian kontrol mitigasi yang komprehensif [cite: 1]. | 2 |
| **6.3.4** | Pastikan bahwa, jika aplikasi mencakup beberapa jalur Athentication, tidak ada jalur yang tidak didokumentasikan dan kontrol keamanan serta kekuatan Athentication diterapkan secara konsisten [cite: 1]. | 2 |
| **6.3.5** | Pastikan bahwa pengguna diberi tahu tentang upaya Athentication yang mencurigakan (berhasil atau tidak berhasil) [cite: 1]. Ini dapat mencakup upaya Athentication dari lokasi atau klien yang tidak biasa, Athentication yang berhasil sebagian (hanya satu dari beberapa faktor), upaya Athentication setelah periode tidak aktif yang lama, atau Athentication yang berhasil setelah beberapa upaya gagal [cite: 1]. | 3 |
| **6.3.6** | Pastikan bahwa email tidak digunakan sebagai mekanisme single-factor atau multi-factor authentication [cite: 1]. | 3 |
| **6.3.7** | Pastikan bahwa pengguna diberi tahu setelah pembaruan detail Athentication, seperti pengaturan ulang kredensial (credential resets) atau modifikasi username atau alamat email [cite: 1]. | 3 |
| **6.3.8** | Pastikan bahwa pengguna yang valid tidak dapat disimpulkan dari tantangan Athentication yang gagal, seperti dengan mendasarkan pada pesan kesalahan, kode respons HTTP, atau waktu respons yang berbeda [cite: 1]. Fungsionalitas pendaftaran dan lupa password (forgot password) juga harus memiliki perlindungan ini [cite: 1]. | 3 |

## V6.4 Siklus Hidup dan Pemulihan Faktor Athentication

Faktor Athentication dapat mencakup password, soft tokens, hardware tokens, dan perangkat biometrik [cite: 1]. Menangani siklus hidup mekanisme ini dengan aman sangat penting untuk keamanan aplikasi, dan bagian ini mencakup persyaratan yang terkait dengan hal tersebut [cite: 1].

Persyaratan di bagian ini sebagian besar terkait dengan [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) atau [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) dari [Panduan NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) [cite: 1].

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **6.4.1** | Pastikan bahwa password awal atau kode aktivasi yang dihasilkan sistem dibuat secara acak dengan aman (securely randomly generated), mengikuti kebijakan password yang ada, dan kedaluwarsa setelah periode waktu yang singkat atau setelah pertama kali digunakan [cite: 1]. Rahasia awal ini tidak boleh diizinkan menjadi password jangka panjang [cite: 1]. | 1 |
| **6.4.2** | Pastikan bahwa petunjuk password (password hints) atau knowledge-based authentication (disebut "pertanyaan rahasia") tidak digunakan [cite: 1]. | 1 |
| **6.4.3** | Pastikan bahwa proses yang aman untuk mengatur ulang password yang terlupakan diimplementasikan, yang tidak mengabaikan (bypass) mekanisme multi-factor authentication yang diaktifkan [cite: 1]. | 2 |
| **6.4.4** | Pastikan bahwa jika suatu faktor multi-factor authentication hilang, bukti pembuktian identitas (identity proofing) dilakukan pada tingkat yang sama seperti saat pendaftaran (enrollment) [cite: 1]. | 2 |
| **6.4.5** | Pastikan bahwa instruksi perpanjangan untuk mekanisme Athentication yang kedaluwarsa dikirim dengan waktu yang cukup untuk dilakukan sebelum mekanisme Athentication yang lama kedaluwarsa, mengatur pengingat otomatis jika perlu [cite: 1]. | 3 |
| **6.4.6** | Pastikan bahwa pengguna administratif dapat memulai proses pengaturan ulang password untuk pengguna, tetapi ini tidak mengizinkan mereka untuk mengubah atau memilih password pengguna [cite: 1]. Hal ini mencegah situasi di mana mereka mengetahui password pengguna [cite: 1]. | 3 |

## V6.5 Persyaratan Umum Multi-factor Authentication

Bagian ini memberikan panduan umum yang relevan untuk berbagai metode multi-factor authentication (MFA) yang berbeda [cite: 1].

Mekanismenya meliputi:

* Lookup Secrets [cite: 1]
* Time based One-time Passwords (TOTPs) [cite: 1]
* Mekanisme Out-of-Band [cite: 1]

Lookup secrets adalah daftar kode rahasia yang dibuat sebelumnya, mirip dengan Transaction Authorization Numbers (TAN), kode pemulihan media sosial, atau kisi (grid) yang berisi sekumpulan nilai acak [cite: 1]. Jenis mekanisme Athentication ini dianggap sebagai "sesuatu yang Anda miliki" (something you have) karena kode tersebut sengaja dibuat agar tidak mudah diingat sehingga perlu disimpan di suatu tempat [cite: 1].

Time based One-time Passwords (TOTPs) adalah token fisik atau perangkat lunak (soft tokens) yang menampilkan tantangan pseudo-acak (pseudo-random one-time challenge) yang terus berubah [cite: 1]. Jenis mekanisme Athentication ini dianggap sebagai "sesuatu yang Anda miliki" (something you have) [cite: 1]. TOTP multi-factor mirip dengan TOTP single-factor, namun memerlukan kode PIN yang valid, pembukaan kunci biometrik (biometric unlocking), penyisipan USB atau pemasangan NFC, atau beberapa nilai tambahan (seperti kalkulator penandatanganan transaksi) untuk dimasukkan guna membuat One-time Password (OTP) akhir [cite: 1].

Detail mengenai mekanisme out-of-band akan diberikan pada bagian berikutnya [cite: 1].

Persyaratan di bagian ini sebagian besar terkait dengan [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators), dan [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) dari [Panduan NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) [cite: 1].

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **6.5.1** | Pastikan bahwa lookup secrets, permintaan atau kode Athentication out-of-band, dan time-based one-time passwords (TOTPs) hanya dapat berhasil digunakan sekali [cite: 1]. | 2 |
| **6.5.2** | Pastikan bahwa, saat disimpan di backend aplikasi, lookup secrets dengan entropi kurang dari 112 bit (19 karakter alfanumerik acak atau 34 digit acak) di-hash dengan algoritma hashing penyimpanan password yang disetujui yang menggabungkan salt acak 32-bit [cite: 1]. Fungsi hash standar dapat digunakan jika rahasia tersebut memiliki entropi 112 bit atau lebih [cite: 1]. | 2 |
| **6.5.3** | Pastikan bahwa lookup secrets, kode Athentication out-of-band, dan seed time-based one-time password (TOTP), dihasilkan menggunakan Cryptographically Secure Pseudorandom Number Generator (CSPRNG) untuk menghindari nilai yang dapat ditebak [cite: 1]. | 2 |
| **6.5.4** | Pastikan bahwa lookup secrets dan kode Athentication out-of-band memiliki entropi minimal 20 bit (biasanya 4 karakter alfanumerik acak atau 6 digit acak sudah cukup) [cite: 1]. | 2 |
| **6.5.5** | Pastikan bahwa permintaan, kode, atau token Athentication out-of-band, serta time-based one-time passwords (TOTPs) memiliki masa pakai yang ditentukan [cite: 1]. Permintaan out-of-band harus memiliki masa pakai maksimal 10 menit dan untuk TOTP masa pakai maksimal 30 detik [cite: 1]. | 2 |
| **6.5.6** | Pastikan bahwa setiap faktor Athentication (termasuk physical devices) dapat dicabut jika terjadi pencurian atau kehilangan lainnya [cite: 1]. | 3 |
| **6.5.7** | Pastikan bahwa mekanisme Athentication biometrik hanya digunakan sebagai faktor sekunder (secondary factors) bersama dengan sesuatu yang Anda miliki (something you have) atau sesuatu yang Anda ketahui (something you know) [cite: 1]. | 3 |
| **6.5.8** | Pastikan bahwa time-based one-time passwords (TOTPs) diperiksa berdasarkan sumber waktu dari layanan tepercaya (trusted service) dan bukan dari waktu yang tidak tepercaya atau yang disediakan klien [cite: 1]. | 3 |

## V6.6 Mekanisme Athentication Out-of-Band

Hal ini biasanya melibatkan server Athentication yang berkomunikasi dengan perangkat fisik melalui saluran sekunder yang aman [cite: 1]. Misalnya, mengirimkan push notifications ke perangkat seluler [cite: 1]. Jenis mekanisme Athentication ini dianggap sebagai "sesuatu yang Anda miliki" (something you have) [cite: 1].

Mekanisme Athentication out-of-band yang tidak aman seperti e-mail dan VOIP tidak diizinkan [cite: 1]. Athentication PSTN dan SMS saat ini dianggap sebagai ["restricted" authentication mechanisms](https://pages.nist.gov/800-63-FAQ/#q-b01) oleh NIST dan harus dihentikan penggunaannya demi Time based One-time Passwords (TOTPs), mekanisme kriptografi, atau sejenisnya [cite: 1]. NIST SP 800-63B [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network) menyarankan untuk menangani risiko device swap, penggantian SIM (SIM change), porting nomor, atau perilaku abnormal lainnya, jika Athentication out-of-band telepon atau SMS mutlak harus didukung [cite: 1]. Meskipun bagian ASVS ini tidak mewajibkan hal ini sebagai persyaratan, tidak mengambil tindakan pencegahan ini untuk aplikasi L2 yang sensitif atau aplikasi L3 harus dilihat sebagai bendera merah (red flag) yang signifikan [cite: 1].

Perhatikan bahwa NIST baru-baru ini juga memberikan panduan yang [tidak menyarankan penggunaan push notifications](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/#fig-3) [cite: 1]. Walaupun bagian ASVS ini tidak melakukannya, penting untuk menyadari risiko "push bombing" [cite: 1].

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **6.6.1** | Pastikan bahwa mekanisme Athentication menggunakan Public Switched Telephone Network (PSTN) untuk mengirimkan One-time Passwords (OTPs) melalui telepon atau SMS hanya ditawarkan ketika nomor telepon telah divalidasi sebelumnya, metode alternatif yang lebih kuat (seperti Time based One-time Passwords) juga ditawarkan, dan layanan tersebut memberikan informasi tentang risiko keamanannya kepada pengguna [cite: 1]. Untuk aplikasi L3, telepon dan SMS tidak boleh tersedia sebagai opsi [cite: 1]. | 2 |
| **6.6.2** | Pastikan bahwa permintaan, kode, atau token Athentication out-of-band terikat pada permintaan Athentication asli yang menghasilkannya dan tidak dapat digunakan untuk permintaan sebelumnya atau sesudahnya [cite: 1]. | 2 |
| **6.6.3** | Pastikan bahwa mekanisme Athentication out-of-band berbasis kode dilindungi dari serangan brute force dengan menggunakan rate limiting [cite: 1]. Pertimbangkan juga untuk menggunakan kode dengan entropi setidaknya 64 bit [cite: 1]. | 2 |
| **6.6.4** | Pastikan bahwa, jika push notifications digunakan untuk multi-factor authentication, rate limiting digunakan untuk mencegah serangan push bombing [cite: 1]. Pencocokan nomor (number matching) juga dapat memitigasi risiko ini [cite: 1]. | 3 |

## V6.7 Mekanisme Athentication Kriptografi

Mekanisme Athentication kriptografi mencakup smart cards atau FIDO keys, di mana pengguna harus menyambungkan atau memasangkan perangkat kriptografi ke komputer untuk menyelesaikan Athentication [cite: 1]. Server Athentication akan mengirimkan tantangan (challenge nonce) ke perangkat atau perangkat lunak kriptografi, dan perangkat atau perangkat lunak tersebut menghitung respons berdasarkan kunci kriptografi yang disimpan dengan aman [cite: 1]. Persyaratan di bagian ini memberikan panduan khusus implementasi untuk mekanisme ini, dengan panduan tentang algoritma kriptografi yang tercakup dalam bab "Kriptografi" [cite: 1].

Di mana shared atau secret keys digunakan untuk Athentication kriptografi, ini harus disimpan menggunakan mekanisme yang sama seperti rahasia sistem lainnya, sebagaimana didokumentasikan dalam bagian "Manajemen Rahasia" (Secret Management) di bab "Konfigurasi" [cite: 1].

Persyaratan di bagian ini sebagian besar terkait dengan [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) dari [Panduan NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) [cite: 1].

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **6.7.1** | Pastikan bahwa sertifikat yang digunakan untuk memverifikasi asersi Athentication kriptografi disimpan dengan cara yang melindunginya dari modifikasi [cite: 1]. | 3 |
| **6.7.2** | Pastikan bahwa challenge nonce memiliki panjang setidaknya 64 bit, dan secara statistik unik atau unik selama masa pakai perangkat kriptografi tersebut [cite: 1]. | 3 |

## V6.8 Athentication dengan Identity Provider

Identity Providers (IdPs) menyediakan identitas federasi (federated identity) untuk pengguna [cite: 1]. Pengguna sering kali akan memiliki lebih dari satu identitas di beberapa IdP, seperti identitas perusahaan yang menggunakan Azure AD, Okta, Ping Identity, atau Google, atau identitas konsumen yang menggunakan Facebook, Twitter, Google, atau WeChat, untuk menyebutkan beberapa alternatif umum [cite: 1]. Daftar ini bukan dukungan terhadap perusahaan atau layanan tersebut, melainkan sekadar dorongan bagi pengembang untuk mempertimbangkan kenyataan bahwa banyak pengguna memiliki banyak identitas yang telah mapan [cite: 1]. Organisasi harus mempertimbangkan untuk mengintegrasikan identitas pengguna yang ada, sesuai dengan profil risiko dari kekuatan pembuktian identitas (identity proofing) IdP [cite: 1]. Misalnya, kecil kemungkinannya organisasi pemerintah akan menerima identitas media sosial sebagai login untuk sistem yang sensitif, karena mudah untuk membuat identitas palsu atau sekali pakai, sedangkan perusahaan game seluler mungkin perlu berintegrasi dengan platform media sosial besar untuk menumbuhkan basis pemain aktif mereka [cite: 1].

Penggunaan external identity providers yang aman membutuhkan konfigurasi dan verifikasi yang hati-hati untuk mencegah identity spoofing atau forged assertions [cite: 1]. Bagian ini menyediakan persyaratan untuk mengatasi risiko tersebut [cite: 1].

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **6.8.1** | Pastikan bahwa, jika aplikasi mendukung beberapa identity providers (IdPs), identitas pengguna tidak dapat dipalsukan (spoofed) melalui identity provider lain yang didukung (mis. dengan menggunakan user identifier yang sama) [cite: 1]. Mitigasi standar adalah aplikasi mendaftarkan dan mengidentifikasi pengguna menggunakan kombinasi IdP ID (berfungsi sebagai namespace) dan ID pengguna di IdP [cite: 1]. | 2 |
| **6.8.2** | Pastikan bahwa keberadaan dan integritas tanda tangan digital pada asersi Athentication (misalnya pada JWTs atau SAML assertions) selalu divalidasi, menolak setiap asersi yang tidak ditandatangani atau memiliki tanda tangan tidak valid [cite: 1]. | 2 |
| **6.8.3** | Pastikan bahwa SAML assertions diproses secara unik dan digunakan hanya sekali dalam periode validitas untuk mencegah replay attacks [cite: 1]. | 2 |
| **6.8.4** | Pastikan bahwa, jika sebuah aplikasi menggunakan Identity Provider (IdP) terpisah dan mengharapkan kekuatan Athentication, metode, atau kebaruan spesifik untuk fungsi tertentu, aplikasi memverifikasi ini menggunakan informasi yang dikembalikan oleh IdP [cite: 1]. Misalnya, jika OIDC digunakan, ini mungkin dicapai dengan memvalidasi klaim ID Token seperti 'acr', 'amr', dan 'auth_time' (jika ada) [cite: 1]. Jika IdP tidak memberikan informasi ini, aplikasi harus memiliki pendekatan fallback yang didokumentasikan yang mengasumsikan bahwa mekanisme Athentication kekuatan minimum telah digunakan (misalnya, single-factor authentication menggunakan username dan password) [cite: 1]. | 2 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [NIST SP 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf) [cite: 1]
* [NIST SP 800-63B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf) [cite: 1]
* [NIST SP 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/) [cite: 1]
* [OWASP Web Security Testing Guide: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/04-Authentication_Testing) [cite: 1]
* [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) [cite: 1]
* [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) [cite: 1]
* [OWASP Choosing and Using Security Questions Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html) [cite: 1]
* [CISA Guidance on "Number Matching"](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf) [cite: 1]
* [Details on the FIDO Alliance](https://fidoalliance.org/) [cite: 1]
v6_Athentication_terjemahan.md
Menampilkan v6_Athentication_terjemahan.md.