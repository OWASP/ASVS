# V6 Otentikasi

## Tujuan Kontrol

Autentikasi adalah proses untuk menetapkan atau mengkonfirmasi keaslian individu atau perangkat. Proses ini melibatkan verifikasi klaim yang dibuat oleh seseorang atau tentang suatu perangkat, memastikan ketahanan terhadap peniruan identitas, dan mencegah pemulihan atau penyadapan kata sandi.

[NIST SP 800-63](https://pages.nist.gov/800-63-3/) adalah standar modern berbasis bukti yang berharga bagi organisasi di seluruh dunia, tetapi sangat relevan bagi lembaga-lembaga AS dan mereka yang berinteraksi dengan lembaga-lembaga AS.

Meskipun banyak persyaratan dalam bab ini didasarkan pada bagian kedua standar (yang dikenal sebagai NIST SP 800-63B "Pedoman Identitas Digital - Otentikasi dan Manajemen Siklus Hidup"), bab ini berfokus pada ancaman umum dan kelemahan otentikasi yang sering dieksploitasi. Bab ini tidak berupaya untuk mencakup secara komprehensif setiap poin dalam standar tersebut. Untuk kasus di mana kepatuhan penuh terhadap NIST SP 800-63 diperlukan, silakan merujuk ke NIST SP 800-63.

Selain itu, terminologi NIST SP 800-63 terkadang dapat berbeda, dan bab ini sering menggunakan terminologi yang lebih umum dipahami untuk meningkatkan kejelasan.

Salah satu fitur umum dari aplikasi yang lebih canggih adalah kemampuan untuk menyesuaikan tahapan otentikasi yang dibutuhkan berdasarkan berbagai faktor risiko. Fitur ini dibahas dalam bab "Otorisasi", karena mekanisme ini juga perlu dipertimbangkan dalam pengambilan keputusan otorisasi.

## V6.1 Dokumentasi Otentikasi

Bagian ini berisi persyaratan yang merinci dokumentasi otentikasi yang harus dipelihara untuk suatu aplikasi. Hal ini sangat penting untuk mengimplementasikan dan menilai bagaimana kontrol otentikasi yang relevan harus dikonfigurasi.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **6.1.1** | Pastikan dokumentasi aplikasi mendefinisikan bagaimana kontrol seperti pembatasan laju (rate limiting), anti-otomatisasi, dan respons adaptif digunakan untuk melindungi dari serangan seperti credential stuffing dan brute force kata sandi. Dokumentasi harus menjelaskan dengan jelas bagaimana kontrol ini dikonfigurasi dan mencegah penguncian akun yang berbahaya. | 1 |
| **6.1.2** | Pastikan daftar kata-kata spesifik konteks didokumentasikan untuk mencegah penggunaannya dalam kata sandi. Daftar tersebut dapat mencakup berbagai kombinasi nama organisasi, nama produk, pengenal sistem, kode nama proyek, nama departemen atau peran, dan sejenisnya. | 2 |
| **6.1.3** | Pastikan bahwa, jika aplikasi mencakup beberapa jalur otentikasi, semuanya didokumentasikan bersama dengan kontrol keamanan dan kekuatan otentikasi yang harus diterapkan secara konsisten di seluruh jalur tersebut. | 2 |

## V6.2 Keamanan Kata Sandi

Kata sandi, yang disebut "Rahasia yang Dihafal" oleh NIST SP 800-63, mencakup kata sandi, frasa sandi, PIN, pola pembuka kunci, dan memilih gambar anak kucing atau elemen gambar lainnya yang tepat. Secara umum, kata sandi dianggap sebagai "sesuatu yang Anda ketahui" dan sering digunakan sebagai mekanisme otentikasi satu faktor.

Oleh karena itu, bagian ini berisi persyaratan untuk memastikan bahwa kata sandi dibuat dan ditangani dengan aman. Sebagian besar persyaratan adalah L1 karena paling penting pada level tersebut. Mulai dari L2 dan seterusnya, mekanisme otentikasi multi-faktor diperlukan, di mana kata sandi dapat menjadi salah satu faktor tersebut.

Persyaratan di bagian ini sebagian besar berkaitan dengan [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) dari [Pedoman NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **6.2.1** | Pastikan kata sandi yang dibuat pengguna minimal terdiri dari 8 karakter, meskipun minimal 15 karakter sangat disarankan. | 1 |
| **6.2.2** | Pastikan pengguna dapat mengubah kata sandi mereka. | 1 |
| **6.2.3** | Pastikan fungsi perubahan kata sandi memerlukan kata sandi pengguna saat ini dan kata sandi baru. | 1 |
| **6.2.4** | Pastikan bahwa kata sandi yang dikirimkan selama pendaftaran akun atau perubahan kata sandi diperiksa terhadap kumpulan kata sandi yang tersedia, setidaknya, 3000 kata sandi teratas yang sesuai dengan kebijakan kata sandi aplikasi, misalnya panjang minimum. | 1 |
| **6.2.5** | Pastikan bahwa kata sandi dengan komposisi apa pun dapat digunakan, tanpa aturan yang membatasi jenis karakter yang diizinkan. Tidak boleh ada persyaratan jumlah minimum karakter huruf besar atau kecil, angka, atau karakter khusus. | 1 |
| **6.2.6** | Pastikan kolom input kata sandi menggunakan type=password untuk menyembunyikan entri. Aplikasi mungkin mengizinkan pengguna untuk sementara melihat seluruh kata sandi yang disembunyikan, atau karakter terakhir yang diketik dari kata sandi. | 1 |
| **6.2.7** | Pastikan fungsi "tempel", fitur bantuan kata sandi peramban, dan pengelola kata sandi eksternal diizinkan. | 1 |
| **6.2.8** | Pastikan bahwa aplikasi memverifikasi kata sandi pengguna persis seperti yang diterima dari pengguna, tanpa modifikasi apa pun seperti pemotongan atau perubahan huruf besar/kecil. | 1 |
| **6.2.9** | Pastikan bahwa kata sandi minimal 64 karakter diperbolehkan. | 2 |
| **6.2.10** | Pastikan bahwa kata sandi pengguna tetap valid hingga ditemukan telah disalahgunakan atau pengguna menggantinya. Aplikasi tidak boleh mewajibkan penggantian kredensial secara berkala. | 2 |
| **6.2.11** | Pastikan bahwa daftar kata-kata spesifik konteks yang didokumentasikan digunakan untuk mencegah pembuatan kata sandi yang mudah ditebak. | 2 |
| **6.2.12** | Pastikan bahwa kata sandi yang dimasukkan selama pendaftaran akun atau perubahan kata sandi diperiksa terhadap serangkaian kata sandi yang telah dibobol. | 2 |

## V6.3 Keamanan Otentikasi Umum

Bagian ini berisi persyaratan umum untuk keamanan mekanisme otentikasi serta menetapkan berbagai harapan untuk setiap level. Aplikasi L2 harus mewajibkan penggunaan otentikasi multi-faktor (MFA). Aplikasi L3 harus menggunakan otentikasi berbasis perangkat keras, yang dilakukan dalam lingkungan eksekusi yang teruji dan tepercaya (TEE). Ini dapat mencakup kata sandi yang terikat pada perangkat, otentikator yang menerapkan Tingkat Jaminan (LoA) Tinggi eIDAS, otentikator dengan jaminan Tingkat Jaminan Otentikator NIST Level 3 (AAL3), atau mekanisme yang setara.

Meskipun ini merupakan sikap yang relatif agresif terhadap MFA, sangat penting untuk meningkatkan standar di sekitarnya guna melindungi pengguna, dan setiap upaya untuk melonggarkan persyaratan ini harus disertai dengan rencana yang jelas tentang bagaimana risiko seputar otentikasi akan dimitigasi, dengan mempertimbangkan panduan dan penelitian NIST tentang topik tersebut.

Perlu dicatat bahwa pada saat dirilis, NIST SP 800-63 menganggap email sebagai [tidak dapat diterima](https://pages.nist.gov/800-63-FAQ/#q-b11) sebagai mekanisme otentikasi ([salinan arsip](https://web.archive.org/web/20250330115328/https://pages.nist.gov/800-63-FAQ/#q-b11)).

Persyaratan di bagian ini berkaitan dengan berbagai bagian dari [Panduan NIST](https://pages.nist.gov/800-63-3/sp800-63b.html), termasuk: [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling), dan [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding).

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **6.3.1** | Pastikan bahwa kontrol untuk mencegah serangan seperti credential stuffing dan password brute force diimplementasikan sesuai dengan dokumentasi keamanan aplikasi. | 1 |
| **6.3.2** | Pastikan bahwa akun pengguna default (misalnya, "root", "admin", atau "sa") tidak ada di aplikasi atau dinonaktifkan. | 1 |
| **6.3.3** | Pastikan bahwa mekanisme otentikasi multi-faktor atau kombinasi mekanisme otentikasi satu faktor harus digunakan untuk mengakses aplikasi. Untuk L3, salah satu faktornya harus berupa mekanisme otentikasi berbasis perangkat keras yang memberikan ketahanan terhadap peretasan dan peniruan identitas terhadap serangan phishing, sekaligus memverifikasi niat untuk melakukan otentikasi dengan mensyaratkan tindakan yang diprakarsai pengguna (seperti menekan tombol pada kunci perangkat keras FIDO atau telepon seluler). Melonggarkan salah satu pertimbangan dalam persyaratan ini memerlukan penjelasan yang terdokumentasi lengkap dan serangkaian kontrol mitigasi yang komprehensif. | 2 |
| **6.3.4** | Pastikan bahwa, jika aplikasi mencakup beberapa jalur otentikasi, tidak ada jalur yang tidak terdokumentasi dan bahwa kontrol keamanan serta kekuatan otentikasi diterapkan secara konsisten. | 2 |
| **6.3.5** | Pastikan pengguna diberi tahu tentang upaya otentikasi yang mencurigakan (berhasil atau tidak berhasil). Ini mungkin termasuk upaya otentikasi dari lokasi atau klien yang tidak biasa, otentikasi yang sebagian berhasil (hanya satu dari beberapa faktor), upaya otentikasi setelah periode tidak aktif yang lama, atau otentikasi yang berhasil setelah beberapa upaya yang tidak berhasil. | 3 |
| **6.3.6** | Pastikan bahwa email tidak digunakan sebagai mekanisme otentikasi satu faktor atau multi-faktor. | 3 |
| **6.3.7** | Pastikan pengguna mendapat pemberitahuan setelah terjadi pembaruan pada detail otentikasi, seperti pengaturan ulang kredensial atau perubahan nama pengguna atau alamat email. | 3 |
| **6.3.8** | Pastikan bahwa pengguna yang sah tidak dapat diidentifikasi berdasarkan kegagalan proses otentikasi, misalnya dengan menganalisis pesan kesalahan, kode respons HTTP, atau perbedaan waktu respons. Fitur pendaftaran dan pemulihan kata sandi juga harus dilengkapi dengan perlindungan ini. | 3 |

## V6.4 Siklus Hidup dan Pemulihan Faktor Otentikasi

Faktor otentikasi dapat mencakup kata sandi, token lunak, token perangkat keras, dan perangkat biometrik. Pengelolaan siklus hidup mekanisme-mekanisme ini secara aman sangat penting bagi keamanan suatu aplikasi, dan bagian ini memuat persyaratan yang berkaitan dengan hal tersebut.

Persyaratan di bagian ini sebagian besar berkaitan dengan [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) atau [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) dari [Pedoman NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **6.4.1** | Pastikan bahwa kata sandi awal atau kode aktivasi yang dihasilkan sistem dibuat secara acak dan aman, mengikuti kebijakan kata sandi yang ada, dan kedaluwarsa setelah jangka waktu singkat atau setelah pertama kali digunakan. Rahasia awal ini tidak boleh diizinkan untuk menjadi kata sandi jangka panjang. | 1 |
| **6.4.2** | Pastikan tidak ada petunjuk kata sandi atau otentikasi berbasis pengetahuan (yang disebut "pertanyaan rahasia"). | 1 |
| **6.4.3** | Pastikan bahwa proses yang aman untuk mengatur ulang kata sandi yang terlupakan telah diterapkan, dan tidak melewati mekanisme otentikasi multi-faktor yang diaktifkan. | 2 |
| **6.4.4** | Pastikan bahwa jika salah satu faktor otentikasi multi-faktor hilang, proses verifikasi identitas dilakukan dengan standar yang sama seperti saat pendaftaran. | 2 |
| **6.4.5** | Pastikan bahwa petunjuk perpanjangan untuk mekanisme otentikasi yang akan kedaluwarsa dikirimkan dengan waktu yang cukup agar dapat dilaksanakan sebelum mekanisme otentikasi lama tersebut kedaluwarsa, serta atur pengingat otomatis jika diperlukan. | 3 |
| **6.4.6** | Pastikan bahwa pengguna administratif dapat memulai proses reset kata sandi untuk pengguna tersebut, namun hal ini tidak memungkinkan mereka untuk mengubah atau menentukan kata sandi pengguna tersebut. Hal ini mencegah terjadinya situasi di mana mereka mengetahui kata sandi pengguna tersebut. | 3 |

## V6.5 Persyaratan umum untuk otentikasi multi-faktor

Bagian ini memberikan panduan umum yang berlaku untuk berbagai metode otentikasi multi-faktor.

Mekanisme-mekanisme tersebut meliputi:

* Pencarian Rahasia
* Time based One-time Passwords (TOTPs)
* Mekanisme Out-of-Band

Kode rahasia pencarian adalah daftar kode rahasia yang telah dibuat sebelumnya, mirip dengan *Transaction Authorization Numbers* (TAN), kode pemulihan media sosial, atau kisi yang berisi serangkaian nilai acak. Mekanisme otentikasi jenis ini dianggap sebagai "sesuatu yang Anda miliki" karena kode-kode tersebut sengaja dibuat tidak mudah diingat sehingga perlu disimpan di suatu tempat.

Time based One-time Passwords (TOTPs) adalah token fisik atau digital yang menampilkan kode tantangan sekali pakai pseudo-acak yang terus berubah. Mekanisme otentikasi jenis ini dikategorikan sebagai "sesuatu yang Anda miliki". TOTP multi-faktor mirip dengan TOTP satu faktor, tetapi memerlukan kode PIN yang valid, pembukaan kunci biometrik, penyisipan USB atau pemasangan NFC, atau nilai tambahan (seperti kalkulator penandatanganan transaksi) yang harus dimasukkan untuk menghasilkan *One-time Password* (OTP) akhir.

Rincian mengenai mekanisme *out-of-band* akan diberikan di bagian selanjutnya.

Persyaratan di bagian ini sebagian besar berkaitan dengan [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators), dan [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) dari [Panduan NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **6.5.1** | Pastikan bahwa rahasia pencarian, permintaan atau kode autentikasi *out-of-band*, dan *time-based one-time passwords* (TOTP) hanya dapat digunakan dengan sukses satu kali. | 2 |
| **6.5.2** | Pastikan bahwa, saat disimpan di backend aplikasi, rahasia pencarian (lookup secrets) dengan entropi kurang dari 112 bit (19 karakter alfanumerik acak atau 34 digit acak) di-hash menggunakan algoritma hashing penyimpanan kata sandi yang disetujui dan dilengkapi dengan salt acak berukuran 32 bit. Fungsi hash standar dapat digunakan jika rahasia tersebut memiliki entropi 112 bit atau lebih. | 2 |
| **6.5.3** | Verifikasi bahwa rahasia pencarian, kode otentikasi *out-of-band*, dan seed *time-based one-time password*, dihasilkan menggunakan Generator Angka Pseudorandom yang Aman secara Kriptografis (CSPRNG) untuk menghindari nilai yang dapat diprediksi. | 2 |
| **6.5.4** | Pastikan bahwa rahasia pencarian dan kode otentikasi *out-of-band* memiliki entropi minimal 20 bit (biasanya 4 karakter alfanumerik acak atau 6 digit acak sudah cukup). | 2 |
| **6.5.5** | Pastikan bahwa permintaan autentikasi di luar jalur komunikasi (out-of-band), kode, atau token, serta kata sandi satu kali berbasis waktu (TOTP) memiliki masa berlaku yang ditentukan. Permintaan di luar jalur komunikasi harus memiliki masa berlaku maksimum 10 menit dan untuk TOTP masa berlaku maksimum 30 detik. | 2 |
| **6.5.6** | Pastikan bahwa setiap faktor otentikasi (termasuk perangkat fisik) dapat dicabut jika terjadi pencurian atau kehilangan lainnya. | 3 |
| **6.5.7** | Pastikan bahwa mekanisme otentikasi biometrik hanya digunakan sebagai faktor sekunder bersama dengan sesuatu yang Anda miliki atau sesuatu yang Anda ketahui. | 3 |
| **6.5.8** | Pastikan bahwa *time-based one-time passwords* (TOTPs) diperiksa berdasarkan sumber waktu dari layanan tepercaya dan bukan dari sumber waktu yang tidak tepercaya atau yang disediakan oleh klien. | 3 |

## V6.6 Mekanisme otentikasi Out-of-Band

Hal ini biasanya melibatkan server otentikasi yang berkomunikasi dengan perangkat fisik melalui saluran sekunder yang aman. Misalnya, mengirimkan notifikasi push ke perangkat seluler. Jenis mekanisme otentikasi ini dianggap sebagai "sesuatu yang Anda miliki".

Mekanisme otentikasi di luar jalur yang tidak aman seperti email dan VOIP tidak diizinkan. Otentikasi PSTN dan SMS saat ini dianggap sebagai [mekanisme otentikasi "terbatas"](https://pages.nist.gov/800-63-FAQ/#q-b01) oleh NIST dan harus dihentikan penggunaannya dan digantikan dengan Time based One-time Passwords (TOTPs), mekanisme kriptografi, atau yang serupa. NIST SP 800-63B [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network) merekomendasikan untuk mengatasi risiko pertukaran perangkat, perubahan SIM, pemindahan nomor, atau perilaku abnormal lainnya, jika otentikasi di luar jalur melalui telepon atau SMS benar-benar harus didukung. Meskipun bagian ASVS ini tidak mewajibkan hal ini sebagai persyaratan, tidak mengambil tindakan pencegahan ini untuk aplikasi L2 atau aplikasi L3 yang sensitif harus dianggap sebagai tanda bahaya yang signifikan.

Perlu dicatat bahwa NIST juga baru-baru ini memberikan panduan yang [tidak menganjurkan penggunaan notifikasi push](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/#fig-3). Meskipun bagian ASVS ini tidak membahas hal tersebut, penting untuk menyadari risiko "push bombing".

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **6.6.1** | Verifikasi bahwa mekanisme autentikasi yang menggunakan Public Switched Telephone Network (PSTN) untuk mengirimkan One-time Passwords (OTPs) melalui panggilan telepon atau SMS hanya ditawarkan jika nomor telepon tersebut telah divalidasi sebelumnya, metode alternatif yang lebih kuat (seperti Time-based One-time Passwords) juga ditawarkan, dan layanan memberikan informasi mengenai risiko keamanannya kepada pengguna. Untuk aplikasi L3, panggilan telepon dan SMS tidak boleh tersedia sebagai opsi. | 2 |
| **6.6.2** | Verifikasi bahwa permintaan autentikasi out-of-band, kode, atau token terikat pada permintaan autentikasi asli yang untuknya mereka dibuat, dan tidak dapat digunakan untuk permintaan sebelumnya atau permintaan berikutnya. | 2 |
| **6.6.3** | Verifikasi bahwa mekanisme autentikasi out-of-band berbasis kode dilindungi dari serangan brute force dengan menggunakan rate limiting. Pertimbangkan juga untuk menggunakan kode dengan setidaknya 64 bit entropi. | 2 |
| **6.6.4** | Verifikasi bahwa, ketika push notification digunakan untuk multi-factor authentication, rate limiting digunakan untuk mencegah serangan push bombing. Pencocokan angka juga dapat memitigasi risiko ini. | 3 |

## V6.7 Mekanisme otentikasi kriptografi

Mekanisme otentikasi kriptografi mencakup kartu pintar atau kunci FIDO, di mana pengguna harus mencolokkan atau memasangkan perangkat kriptografi ke komputer untuk menyelesaikan otentikasi. Server otentikasi akan mengirimkan nonce tantangan ke perangkat atau perangkat lunak kriptografi, dan perangkat atau perangkat lunak tersebut menghitung respons berdasarkan kunci kriptografi yang disimpan dengan aman. Persyaratan dalam bagian ini memberikan panduan spesifik implementasi untuk mekanisme ini, dengan panduan tentang algoritma kriptografi yang dibahas dalam bab "Kriptografi".

Apabila kunci bersama atau kunci rahasia digunakan untuk otentikasi kriptografi, kunci-kunci ini harus disimpan menggunakan mekanisme yang sama seperti rahasia sistem lainnya, sebagaimana didokumentasikan dalam bagian "Secret Management" di bab "Configuration".

Persyaratan di bagian ini sebagian besar berkaitan dengan [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **6.7.1** | Verifikasi bahwa sertifikat yang digunakan untuk memverifikasi asersi autentikasi kriptografis disimpan dengan cara yang melindunginya dari modifikasi. | 3 |
| **6.7.2** | Verifikasi bahwa *challenge nonce* memiliki panjang setidaknya 64 bit, dan unik secara statistik atau unik sepanjang masa pakai perangkat kriptografis. | 3 |

## V6.8 Autentikasi dengan Penyedia Identitas

Identity Providers (IdPs) menyediakan identitas federasi bagi pengguna. Pengguna sering kali memiliki lebih dari satu identitas di berbagai IdP, seperti identitas perusahaan menggunakan Azure AD, Okta, Ping Identity, atau Google, atau identitas konsumen menggunakan Facebook, Twitter, Google, atau WeChat, untuk menyebut beberapa alternatif umum. Daftar ini bukan merupakan dukungan terhadap perusahaan atau layanan tersebut, melainkan sekadar dorongan bagi pengembang untuk mempertimbangkan kenyataan bahwa banyak pengguna telah memiliki banyak identitas. Organisasi sebaiknya mempertimbangkan untuk berintegrasi dengan identitas pengguna yang sudah ada, sesuai dengan profil risiko dari kekuatan identity proofing IdP tersebut. Sebagai contoh, kecil kemungkinan sebuah organisasi pemerintahan akan menerima identitas media sosial sebagai login untuk sistem sensitif, karena mudah untuk membuat identitas palsu atau sementara, sementara perusahaan gim seluler mungkin sangat perlu berintegrasi dengan platform media sosial utama untuk mengembangkan basis pemain aktif mereka.

Penggunaan external identity providers secara aman memerlukan konfigurasi dan verifikasi yang cermat untuk mencegah pemalsuan identitas atau asersi palsu. Bagian ini menyediakan persyaratan untuk menangani risiko-risiko tersebut.

| # | Deskripsi | Tingkat |
| :---: | :--- | :---: |
| **6.8.1** | Verifikasi bahwa, jika aplikasi mendukung beberapa identity providers (IdPs), identitas pengguna tidak dapat dipalsukan melalui identity provider lain yang didukung (misalnya dengan menggunakan pengenal pengguna yang sama). Mitigasi standarnya adalah aplikasi mendaftarkan dan mengidentifikasi pengguna menggunakan kombinasi IdP ID (yang berfungsi sebagai namespace) dan ID pengguna di IdP tersebut. | 2 |
| **6.8.2** | Verifikasi bahwa keberadaan dan integritas digital signature pada asersi autentikasi (misalnya pada JWT atau asersi SAML) selalu divalidasi, menolak segala asersi yang tidak ditandatangani atau memiliki signature yang tidak valid. | 2 |
| **6.8.3** | Verifikasi bahwa asersi SAML diproses secara unik dan hanya digunakan sekali dalam masa berlaku untuk mencegah serangan replay. | 2 |
| **6.8.4** | Verifikasi bahwa, jika aplikasi menggunakan Identity Provider (IdP) terpisah dan mengharapkan kekuatan, metode, atau kebaruan autentikasi tertentu untuk fungsi tertentu, aplikasi memverifikasi ini menggunakan informasi yang dikembalikan oleh IdP. Sebagai contoh, jika OIDC digunakan, ini dapat dicapai dengan memvalidasi klaim ID Token seperti 'acr', 'amr', dan 'auth_time' (jika tersedia). Jika IdP tidak menyediakan informasi ini, aplikasi harus memiliki pendekatan fallback yang terdokumentasi yang mengasumsikan bahwa mekanisme autentikasi dengan kekuatan minimum telah digunakan (misalnya, single-factor authentication menggunakan nama pengguna dan kata sandi). | 2 |

## Referensi

Untuk informasi selengkapnya, lihat juga:

* [NIST SP 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST SP 800-63B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST SP 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Web Security Testing Guide: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/04-Authentication_Testing)
* [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Choosing and Using Security Questions Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
* [CISA Guidance on "Number Matching"](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
* [Details on the FIDO Alliance](https://fidoalliance.org/)
