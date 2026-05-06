# Perubahan Dibandingkan dengan v4.x

## Pengantar

Pengguna yang sudah familiar dengan standar versi 4.x mungkin akan merasa terbantu dengan meninjau perubahan-perubahan utama yang diperkenalkan dalam versi 5.0, termasuk pembaruan dalam konten, cakupan, dan filosofi yang mendasarinya.

Dari 286 persyaratan dalam versi 4.0.3, hanya 11 yang tetap tidak berubah, sementara 15 mengalami penyesuaian tata bahasa kecil tanpa mengubah maknanya. Secara total, 109 persyaratan (38%) tidak lagi menjadi persyaratan terpisah dalam versi 5.0, dengan 50 di antaranya dihapus, 28 dihapus karena duplikat, dan 31 digabungkan ke dalam persyaratan lain. Sisanya telah direvisi dalam beberapa hal. Bahkan persyaratan yang tidak dimodifikasi secara substansial memiliki pengenal yang berbeda karena penataan ulang atau restrukturisasi.

Untuk mempermudah adopsi versi 5.0, dokumen pemetaan disediakan untuk membantu pengguna melacak bagaimana persyaratan dari versi 4.x sesuai dengan persyaratan di versi 5.0. Pemetaan ini tidak terikat pada versi rilis dan dapat diperbarui atau diklarifikasi sesuai kebutuhan.

## Filosofi Persyaratan

### Cakupan dan Fokus

Versi 4.x mencakup persyaratan yang tidak sesuai dengan ruang lingkup standar yang dimaksud; persyaratan tersebut telah dihapus. Persyaratan yang tidak memenuhi kriteria ruang lingkup untuk versi 5.0 atau tidak dapat diverifikasi juga telah dikecualikan.

### Penekanan pada Tujuan Keamanan di Atas Mekanisme

Pada versi 4.x, banyak persyaratan berfokus pada mekanisme spesifik daripada tujuan keamanan yang mendasar. Pada versi 5.0, persyaratan berpusat pada tujuan keamanan, hanya merujuk pada mekanisme tertentu ketika itu adalah satu-satunya solusi praktis, atau menyediakannya sebagai contoh atau panduan tambahan.

Pendekatan ini mengakui bahwa mungkin ada beberapa metode untuk mencapai tujuan keamanan tertentu, dan menghindari preskriptifitas yang tidak perlu yang dapat membatasi fleksibilitas organisasi.

Selain itu, persyaratan yang membahas masalah keamanan yang sama telah dikonsolidasikan jika sesuai.

### Keputusan Keamanan yang Terdokumentasi

Meskipun konsep keputusan keamanan yang terdokumentasi mungkin terlihat baru dalam versi 5.0, ini merupakan evolusi dari persyaratan sebelumnya yang terkait dengan penerapan kebijakan dan pemodelan ancaman dalam versi 4.0. Sebelumnya, beberapa persyaratan secara implisit menuntut analisis untuk menginformasikan implementasi kontrol keamanan, seperti menentukan koneksi jaringan yang diizinkan.

Untuk memastikan bahwa informasi yang diperlukan tersedia untuk implementasi dan verifikasi, harapan-harapan ini sekarang secara eksplisit didefinisikan sebagai persyaratan dokumentasi, sehingga menjadi jelas, dapat ditindaklanjuti, dan dapat diverifikasi.

## Perubahan Struktur dan Bab Baru

Beberapa bab dalam versi 5.0 memperkenalkan konten yang sepenuhnya baru:

* OAuth dan OIDC – Mengingat adopsi luas protokol ini untuk delegasi akses dan single sign-on, persyaratan khusus telah ditambahkan untuk mengatasi beragam skenario yang mungkin dihadapi pengembang. Area ini pada akhirnya dapat berkembang menjadi standar mandiri, serupa dengan perlakuan terhadap persyaratan Mobile dan IoT pada versi sebelumnya.
* WebRTC – Seiring meningkatnya popularitas teknologi ini, pertimbangan dan tantangan keamanannya yang unik kini dibahas dalam bagian khusus.

Upaya juga telah dilakukan untuk memastikan bahwa bab dan bagian disusun berdasarkan serangkaian persyaratan terkait yang koheren.

Restrukturisasi ini telah menyebabkan terciptanya bab-bab tambahan:

* Token Mandiri – Sebelumnya dikelompokkan dalam manajemen sesi, token mandiri kini diakui sebagai mekanisme yang berbeda dan elemen dasar untuk komunikasi tanpa status (seperti dalam OAuth dan OIDC). Karena implikasi keamanannya yang unik, token ini dibahas dalam bab khusus, dengan beberapa persyaratan baru yang diperkenalkan dalam versi 5.x.
* Keamanan Antarmuka Web – Dengan meningkatnya kompleksitas aplikasi berbasis browser dan munculnya arsitektur berbasis API saja, persyaratan keamanan antarmuka web telah dipisahkan ke dalam bab tersendiri.
* Pengkodean dan Arsitektur yang Aman – Persyaratan baru yang membahas praktik keamanan umum yang tidak sesuai dengan bab-bab yang ada telah dikelompokkan di sini.

Perubahan organisasi lainnya dalam versi 5.0 dilakukan untuk memperjelas maksud. Misalnya, persyaratan validasi input dipindahkan bersama logika bisnis, mencerminkan peran mereka dalam menegakkan aturan bisnis, daripada dikelompokkan dengan sanitasi dan pengkodean.

Bab Arsitektur V1 sebelumnya telah dihapus. Bagian awalnya berisi persyaratan yang berada di luar cakupan, sementara bagian selanjutnya telah didistribusikan kembali ke bab-bab yang relevan, dengan persyaratan yang dihilangkan duplikatnya dan diklarifikasi seperlunya.

## Penghapusan Pemetaan Langsung ke Standar Lain

Pemetaan langsung ke standar lain telah dihapus dari bagian utama standar ini. Tujuannya adalah untuk mempersiapkan pemetaan dengan proyek OWASP Common Requirement Enumeration (CRE), yang pada gilirannya akan menghubungkan ASVS dengan berbagai proyek OWASP dan standar eksternal.

Pemetaan langsung ke CWE dan NIST tidak lagi dipelihara, seperti yang dijelaskan di bawah ini.

### Mengurangi Keterkaitan dengan Pedoman Identitas Digital NIST

Pedoman [Identitas Digital NIST (SP 800-63)](https://pages.nist.gov/800-63-3/) telah lama berfungsi sebagai referensi untuk kontrol otentikasi dan otorisasi. Pada versi 4.x, bab-bab tertentu diselaraskan secara erat dengan struktur dan terminologi NIST.

Meskipun pedoman ini tetap menjadi referensi penting, penyelarasan yang ketat menimbulkan tantangan, termasuk terminologi yang kurang dikenal secara luas, duplikasi persyaratan serupa, dan pemetaan yang tidak lengkap. Versi 5.0 beralih dari pendekatan ini untuk meningkatkan kejelasan dan relevansi.

### Menjauh dari Enumerasi Kelemahan Umum (CWE)

[Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) menyediakan taksonomi yang berguna untuk kelemahan keamanan perangkat lunak. Namun, tantangan seperti CWE yang hanya berdasarkan kategori, kesulitan dalam memetakan persyaratan ke satu CWE, dan adanya pemetaan yang tidak tepat pada versi 4.x telah menyebabkan keputusan untuk menghentikan pemetaan CWE langsung pada versi 5.0.

## Memikirkan Kembali Definisi Level

Versi 4.x mendeskripsikan level-level tersebut sebagai L1 ("Minimum"), L2 ("Standar"), dan L3 ("Lanjutan"), dengan implikasi bahwa semua aplikasi yang menangani data sensitif setidaknya harus memenuhi level L2.

Versi 5.0 mengatasi beberapa masalah dengan pendekatan ini yang dijelaskan dalam paragraf-paragraf berikut.

Secara praktis, sementara versi 4.x menggunakan tanda centang untuk indikator level, versi 5.x menggunakan angka sederhana pada semua format standar termasuk markdown, PDF, DOCX, CSV, JSON, dan XML. Untuk kompatibilitas mundur, versi lama dari output CSV, JSON, dan XML yang masih menggunakan tanda centang juga dihasilkan.

### Tingkat Pemula yang Lebih Mudah

Umpan balik menunjukkan bahwa banyaknya persyaratan Level 1 (~120), ditambah dengan penunjukannya sebagai level "minimum" yang tidak cukup baik untuk sebagian besar aplikasi, menghambat adopsi. Versi 5.0 bertujuan untuk menurunkan hambatan ini dengan mendefinisikan Level 1 terutama di sekitar persyaratan pertahanan lapisan pertama, sehingga menghasilkan persyaratan yang lebih jelas dan lebih sedikit pada level tersebut. Untuk menunjukkan hal ini secara numerik, dalam v4.0.3 terdapat 128 persyaratan L1 dari total 278 persyaratan, yang mewakili 46%. Dalam 5.0.0 terdapat 70 persyaratan L1 dari total 345 persyaratan, yang mewakili 20%.

### Kekeliruan Keterujian

Faktor kunci dalam memilih kontrol untuk Level 1 di versi 4.x adalah kesesuaiannya untuk penilaian melalui pengujian penetrasi eksternal "kotak hitam". Namun, pendekatan ini tidak sepenuhnya selaras dengan tujuan Level 1 sebagai rangkaian kontrol keamanan minimum. Beberapa pengguna berpendapat bahwa Level 1 tidak cukup untuk mengamankan aplikasi, sementara yang lain menganggapnya terlalu sulit untuk diuji.

Mengandalkan kemampuan uji sebagai kriteria bersifat relatif dan, terkadang, menyesatkan. Fakta bahwa suatu persyaratan dapat diuji tidak menjamin bahwa persyaratan tersebut dapat diuji secara otomatis atau langsung. Terlebih lagi, persyaratan yang paling mudah diuji tidak selalu merupakan persyaratan yang memiliki dampak keamanan terbesar atau yang paling mudah diimplementasikan.

Oleh karena itu, dalam versi 5.0, keputusan level dibuat terutama berdasarkan pengurangan risiko dan juga dengan mempertimbangkan upaya implementasi.

### Bukan Hanya Soal Risiko

Penggunaan tingkatan preskriptif berbasis risiko yang mewajibkan tingkat tertentu untuk aplikasi tertentu telah terbukti terlalu kaku. Dalam praktiknya, prioritas dan implementasi kontrol keamanan bergantung pada banyak faktor, termasuk pengurangan risiko dan upaya yang dibutuhkan untuk implementasi.

Oleh karena itu, organisasi didorong untuk mencapai tingkat yang mereka rasa pantas dicapai berdasarkan kematangan mereka dan pesan yang ingin mereka sampaikan kepada pengguna mereka.
