# Perubahan Dibandingkan dengan v4.x

## Pengantar

Pengguna yang sudah terbiasa dengan versi 4.x dari standar ini mungkin merasa terbantu untuk meninjau perubahan kunci yang diperkenalkan pada versi 5.0, termasuk pembaruan dalam konten, cakupan (_scope_), dan filosofi dasar.

Dari 286 persyaratan dalam versi 4.0.3, hanya 11 yang tetap tidak berubah, sementara 15 telah mengalami penyesuaian tata bahasa minor tanpa mengubah maknanya. Secara total, 109 persyaratan (38%) tidak lagi menjadi persyaratan terpisah di versi 5.0, dengan rincian: 50 persyaratan dihapus, 28 dihapus karena duplikat, dan 31 digabungkan ke dalam persyaratan lain. Sisanya telah direvisi sedemikian rupa. Bahkan persyaratan yang tidak diubah secara substansial memiliki pengenal (_identifier_) yang berbeda karena adanya pengurutan ulang atau restrukturisasi.

Untuk memfasilitasi adopsi versi 5.0, dokumen pemetaan (_mapping documents_) telah disediakan untuk membantu pengguna menelusuri bagaimana persyaratan dari versi 4.x sesuai dengan persyaratan di versi 5.0. Pemetaan ini tidak terikat pada pemetaan versi rilis dan dapat diperbarui atau diperjelas sesuai kebutuhan.

## Filosofi Persyaratan

### Cakupan dan Fokus

Versi 4.x mencakup persyaratan yang tidak selaras dengan cakupan yang dimaksudkan dari standar ini; persyaratan tersebut telah dihapus. Persyaratan yang tidak memenuhi kriteria cakupan untuk 5.0 atau tidak dapat diverifikasi (_verifiable_) juga telah dikeluarkannya.

### Penekanan pada Tujuan Keamanan Dibandingkan Mekanisme

Dalam versi 4.x, banyak persyaratan berfokus pada mekanisme tertentu alih-alih tujuan keamanan yang mendasarinya. Dalam versi 5.0, persyaratan berpusat pada tujuan keamanan (_security goals_), merujuk pada mekanisme tertentu hanya jika mekanisme tersebut merupakan satu-satunya solusi praktis, atau menyediakannya sebagai contoh atau panduan tambahan.

Pendekatan ini menyadari bahwa beberapa metode mungkin ada untuk mencapai tujuan keamanan tertentu, dan menghindari sifat preskriptif yang tidak perlu yang dapat membatasi fleksibilitas organisasi.

Selain itu, persyaratan yang menangani masalah keamanan yang sama telah dikonsolidasikan jika sesuai.

### Keputusan Keamanan yang Terdokumentasi

Meskipun konsep keputusan keamanan yang terdokumentasi mungkin tampak baru di versi 5.0, konsep ini merupakan evolusi dari persyaratan terdahulu terkait penerapan kebijakan dan pemodelan ancaman (_threat modeling_) di versi 4.0. Sebelumnya, beberapa persyaratan secara tersirat menuntut analisis untuk menginformasikan implementasi kontrol keamanan, seperti menentukan koneksi jaringan yang diizinkan.

Untuk memastikan bahwa informasi yang diperlukan tersedia untuk implementasi dan verifikasi, ekspektasi ini sekarang didefinisikan secara eksplisit sebagai persyaratan dokumentasi, menjadikannya jelas, dapat ditindaklanjuti, dan dapat diverifikasi.

## Perubahan Struktural dan Bab-Bab Baru

Beberapa bab dalam versi 5.0 memperkenalkan konten yang sama sekali baru:

* OAuth dan OIDC – Mengingat adopsi yang luas dari protokol-protokol ini untuk delegasi akses dan _single sign-on_, persyaratan khusus telah ditambahkan untuk menangani berbagai skenario yang mungkin ditemui oleh pengembang. Area ini pada akhirnya mungkin berkembang menjadi standar berdiri sendiri, mirip dengan penanganan persyaratan _Mobile_ dan _IoT_ pada versi sebelumnya.
* WebRTC – Seiring meningkatnya popularitas teknologi ini, pertimbangan dan tantangan keamanan uniknya kini ditangani dalam bagian khusus.

Upaya juga telah dilakukan untuk memastikan bahwa bab dan bagian diatur di sekitar kumpulan persyaratan terkait yang kohesif.

Restrukturisasi ini telah menyebabkan terciptanya bab-bab tambahan:

* Self-contained Tokens – Sebelumnya dikelompokkan di bawah manajemen sesi (_session management_), _self-contained tokens_ kini diakui sebagai mekanisme terpisah dan elemen mendasar untuk komunikasi _stateless_ (seperti dalam OAuth dan OIDC). Karena implikasi keamanannya yang unik, topik ini ditangani dalam bab khusus, dengan beberapa persyaratan baru diperkenalkan pada versi 5.x.
* Web Frontend Security – Dengan meningkatnya kompleksitas aplikasi berbasis peramban dan berkembangnya arsitektur _API-only_, persyaratan keamanan _frontend_ telah dipisahkan ke dalam bab mereka sendiri.
* Secure Coding and Architecture – Persyaratan baru yang menangani praktik keamanan umum yang tidak cocok di dalam bab-bab yang ada telah dikelompokkan di sini.

Perubahan organisasional lainnya di versi 5.0 dibuat untuk memperjelas maksud. Sebagai contoh, persyaratan validasi input dipindahkan berdampingan dengan logika bisnis, mencerminkan peran mereka dalam menegakkan aturan bisnis, alih-alih dikelompokkan dengan sanitasi dan _encoding_.

Bab V1 Architecture sebelumnya telah dihapus. Bagian awalnya berisi persyaratan yang berada di luar cakupan (_out of scope_), sementara bagian selanjutnya telah didistribusikan ulang ke bab-bab yang relevan, dengan persyaratan yang terduplikasi dan diperjelas seperlunya.

## Penghapusan Pemetaan Langsung ke Standar Lain

Pemetaan langsung ke standar lain telah dihapus dari bagian utama standar ini. Tujuannya adalah menyiapkan pemetaan dengan proyek OWASP Common Requirement Enumeration (CRE), yang pada gilirannya akan menghubungkan ASVS ke berbagai proyek OWASP dan standar eksternal.

Pemetaan langsung ke CWE dan NIST tidak lagi dipertahankan, seperti yang dijelaskan di bawah ini.

### Pengurangan Keterkaitan dengan NIST Digital Identity Guidelines

NIST [Digital Identity Guidelines (SP 800-63)](https://pages.nist.gov/800-63-3/) telah lama berfungsi sebagai referensi untuk kontrol otentikasi dan otorisasi. Dalam versi 4.x, bab-bab tertentu sangat selaras dengan struktur dan terminologi NIST.

Meskipun panduan ini tetap menjadi referensi penting, keselarasan yang ketat menimbulkan tantangan, termasuk terminologi yang kurang dikenal secara luas, duplikasi persyaratan serupa, dan pemetaan yang tidak lengkap. Versi 5.0 beralih dari pendekatan ini untuk meningkatkan kejelasan dan relevansi.

### Beralih dari Common Weakness Enumeration (CWE)

[Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) menyediakan taksonomi yang berguna tentang kelemahan keamanan perangkat lunak. Namun, tantangan seperti CWE yang hanya berupa kategori, kesulitan dalam memetakan persyaratan ke satu CWE, dan adanya pemetaan yang tidak presisi pada versi 4.x telah menyebabkan keputusan untuk menghentikan pemetaan CWE langsung pada versi 5.0.

## Memikirkan Ulang Definisi Level

Versi 4.x menggambarkan tingkat/level sebagai L1 ("Minimum"), L2 ("Standar"), dan L3 ("Lanjutan"), dengan implikasi bahwa semua aplikasi yang menangani data sensitif harus memenuhi setidaknya L2.

Versi 5.0 menangani beberapa masalah dengan pendekatan ini yang dijelaskan dalam paragraf berikut.

Secara praktis, di mana versi 4.x menggunakan tanda centang (_tick marks_) sebagai indikator level, versi 5.x menggunakan angka sederhana pada semua format standar termasuk Markdown, PDF, DOCX, CSV, JSON, dan XML. Untuk kompatibilitas mundur (_backwards compatibility_), output CSV, JSON, dan XML versi _legacy_ yang masih menggunakan tanda centang juga tetap dihasilkan.

### Level Masuk yang Lebih Mudah

Umpan balik menunjukkan bahwa sejumlah besar persyaratan Level 1 (~120), dikombinasikan dengan sebutan sebagai level "minimum" yang dianggap tidak cukup baik untuk sebagian besar aplikasi, menyurutkan niat untuk melakukan adopsi. Versi 5.0 bertujuan untuk menurunkan hambatan ini dengan mendefinisikan Level 1 utamanya di sekitar persyaratan pertahanan lapisan pertama (_first-layer defense_), yang menghasilkan persyaratan yang lebih jelas dan lebih sedikit pada level tersebut. Untuk menunjukkannya secara numerik, pada v4.0.3 terdapat 128 persyaratan L1 dari total 278 persyaratan, mewakili 46%. Pada 5.0.0 terdapat 70 persyaratan L1 dari total 345 persyaratan, mewakili 20%.

### Kekeliruan Pemikiran tentang Kemampuan Pengujian (Testability)

Faktor kunci dalam memilih kontrol untuk Level 1 pada versi 4.x adalah kesesuaian mereka untuk penilaian melalui pengujian penetrasi eksternal _black box_. Namun, pendekatan ini tidak sepenuhnya selaras dengan maksud Level 1 sebagai kumpulan kontrol keamanan minimum. Beberapa pengguna berpendapat bahwa Level 1 tidak cukup untuk mengamankan aplikasi, sementara yang lain menganggapnya terlalu sulit untuk diuji.

Mengandalkan kemampuan pengujian (_testability_) sebagai kriteria adalah hal yang relatif dan terkadang menyesatkan. Fakta bahwa suatu persyaratan dapat diuji tidak menjamin bahwa persyaratan tersebut dapat diuji secara otomatis atau dengan cara yang sederhana. Selain itu, persyaratan yang paling mudah diuji tidak selalu merupakan persyaratan dengan dampak keamanan terbesar atau yang paling mudah diimplementasikan.

Dengan demikian, dalam versi 5.0, keputusan level dibuat terutama berdasarkan pengurangan risiko dan juga mengingat upaya yang diperlukan untuk mengimplementasikannya.

### Tidak Hanya Tentang Risiko

Penggunaan level berbasis risiko yang preskriptif yang mewajibkan level tertentu untuk aplikasi tertentu telah terbukti terlalu kaku. Dalam praktiknya, prioritisasi dan implementasi kontrol keamanan bergantung pada banyak faktor, termasuk pengurangan risiko dan upaya yang diperlukan untuk implementasi.

Oleh karena itu, organisasi didorong untuk mencapai level yang mereka merasa harus dicapai berdasarkan kematangan (_maturity_) mereka dan pesan yang ingin mereka sampaikan kepada pengguna mereka.
