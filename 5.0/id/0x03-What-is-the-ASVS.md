# Apa itu ASVS?

Standar Verifikasi Keamanan Aplikasi (ASVS) menetapkan persyaratan keamanan untuk aplikasi dan layanan web, serta merupakan sumber daya yang berharga bagi siapa pun yang ingin merancang, mengembangkan, dan memelihara aplikasi yang aman atau mengevaluasi keamanannya.

Bab ini menguraikan aspek-aspek penting dalam penggunaan ASVS, termasuk ruang lingkupnya, struktur tingkatan berbasis prioritasnya, serta kasus penggunaan utama standar tersebut.

## Ruang Lingkup ASVS

Ruang lingkup ASVS ditentukan oleh namanya: Aplikasi, Keamanan, Verifikasi, dan Standar. Ruang lingkup ini menetapkan persyaratan mana yang dimasukkan atau dikecualikan, dengan tujuan utama untuk mengidentifikasi prinsip-prinsip keamanan yang harus dipenuhi. Ruang lingkup ini juga mencakup persyaratan dokumentasi, yang berfungsi sebagai landasan bagi persyaratan implementasi.

Tidak ada yang namanya ruang lingkup bagi penyerang. Oleh karena itu, persyaratan ASVS harus dievaluasi bersamaan dengan pedoman untuk aspek-aspek lain dalam siklus hidup aplikasi, termasuk proses CI/CD, hosting, dan kegiatan operasional.

### Aplikasi

ASVS mendefinisikan “aplikasi” sebagai produk perangkat lunak yang sedang dikembangkan, di mana pengendalian keamanan harus diintegrasikan. ASVS tidak mengatur aktivitas siklus hidup pengembangan atau menentukan cara aplikasi harus dibangun melalui jalur CI/CD; sebaliknya, ASVS menetapkan hasil keamanan yang harus dicapai dalam produk itu sendiri.

Komponen yang menangani, memodifikasi, atau memvalidasi lalu lintas HTTP, seperti Web Application Firewalls (WAF), load balancer, atau proxy, dapat dianggap sebagai bagian dari aplikasi untuk tujuan-tujuan spesifik tersebut, karena beberapa kontrol keamanan bergantung langsung pada komponen-komponen tersebut atau dapat diimplementasikan melalui mereka. Komponen-komponen ini perlu dipertimbangkan dalam persyaratan yang berkaitan dengan respons yang disimpan dalam cache, pembatasan laju, atau pembatasan koneksi masuk dan keluar berdasarkan sumber dan tujuan.

Sebaliknya, ASVS umumnya tidak memasukkan persyaratan yang tidak secara langsung berkaitan dengan aplikasi atau yang konfigurasinya berada di luar lingkup tanggung jawab aplikasi. Misalnya, masalah DNS biasanya ditangani oleh tim atau unit kerja yang terpisah.

Demikian pula, meskipun aplikasi bertanggung jawab atas bagaimana ia menggunakan input dan menghasilkan output, jika sebuah proses eksternal berinteraksi dengan aplikasi atau datanya, hal itu dianggap berada di luar cakupan ASVS. Misalnya, mencadangkan aplikasi atau datanya biasanya merupakan tanggung jawab proses eksternal dan tidak dikendalikan oleh aplikasi atau pengembangnya.

### Keamanan

Setiap persyaratan harus memiliki dampak yang dapat dibuktikan terhadap keamanan. Ketiadaan suatu persyaratan harus mengakibatkan aplikasi menjadi kurang aman, dan penerapan persyaratan tersebut harus mengurangi baik kemungkinan maupun dampak dari risiko keamanan.

Pertimbangan lain apa pun, seperti aspek fungsional, gaya penulisan kode, atau persyaratan kebijakan, tidak termasuk dalam cakupan ini.

### Verifikasi

Persyaratan tersebut harus dapat diverifikasi, dan hasil verifikasi harus berupa keputusan “gagal” atau “lulus”.

### Standar

ASVS dirancang sebagai kumpulan persyaratan keamanan yang harus diterapkan untuk memenuhi standar tersebut. Artinya, persyaratan tersebut terbatas pada penetapan tujuan keamanan yang ingin dicapai. Informasi terkait lainnya dapat dikembangkan berdasarkan ASVS atau dihubungkan melalui pemetaan.

Secara khusus, OWASP memiliki banyak proyek, dan ASVS secara sengaja menghindari tumpang tindih dengan konten di proyek-proyek lain. Misalnya, pengembang mungkin memiliki pertanyaan, “bagaimana cara menerapkan persyaratan tertentu dalam teknologi atau lingkungan saya,” dan hal ini seharusnya dibahas dalam proyek Cheat Sheet Series. Sementara itu, penguji mungkin memiliki pertanyaan, “bagaimana cara menguji persyaratan ini dalam lingkungan ini,” dan hal ini seharusnya dibahas dalam proyek Web Security Testing Guide.

Meskipun ASVS tidak hanya ditujukan untuk para ahli keamanan, buku ini mengharuskan pembaca memiliki pengetahuan teknis untuk memahami isinya atau kemampuan untuk meneliti konsep-konsep tertentu.

### Persyaratan

Istilah "persyaratan" digunakan secara khusus dalam ASVS karena istilah tersebut menggambarkan hal-hal yang harus dipenuhi untuk memenuhi ketentuan tersebut. ASVS hanya memuat persyaratan (harus) dan tidak memuat rekomendasi (sebaiknya) sebagai syarat utama.

Dengan kata lain, rekomendasi—baik yang hanya merupakan salah satu dari banyak opsi yang mungkin untuk memecahkan suatu masalah maupun pertimbangan gaya penulisan kode—tidak memenuhi definisi sebagai suatu persyaratan.

Persyaratan ASVS dirancang untuk mencakup prinsip-prinsip keamanan tertentu tanpa terlalu terikat pada metode implementasi atau teknologi tertentu, sekaligus secara jelas menjelaskan alasan keberadaannya. Hal ini juga berarti bahwa persyaratan tersebut tidak didasarkan pada metode verifikasi atau implementasi tertentu.

### Keputusan keamanan yang terdokumentasi

Dalam keamanan perangkat lunak, merencanakan desain keamanan dan mekanisme yang akan digunakan sejak awal akan menghasilkan implementasi yang lebih konsisten dan andal pada produk atau fitur yang telah jadi.

Selain itu, untuk persyaratan tertentu, implementasinya akan menjadi rumit dan sangat spesifik sesuai dengan kebutuhan aplikasi. Contoh umum meliputi izin akses, validasi masukan, dan kontrol perlindungan terhadap berbagai tingkat data sensitif.

Untuk mengatasi hal ini, alih-alih membuat pernyataan umum seperti "semua data harus dienkripsi" atau mencoba mencakup setiap kemungkinan skenario penggunaan dalam suatu persyaratan, telah dimasukkan persyaratan dokumentasi yang mewajibkan agar pendekatan dan konfigurasi yang diterapkan oleh pengembang aplikasi terhadap jenis-jenis pengendalian tersebut harus didokumentasikan. Hal ini kemudian dapat ditinjau untuk memastikan kesesuaiannya, dan implementasi yang sebenarnya dapat dibandingkan dengan dokumentasi tersebut guna menilai apakah implementasi tersebut sesuai dengan harapan.

Persyaratan ini dimaksudkan untuk mendokumentasikan keputusan yang telah diambil oleh organisasi pengembang aplikasi terkait cara menerapkan persyaratan keamanan tertentu.

Persyaratan dokumentasi selalu tercantum pada bagian pertama suatu bab (meskipun tidak semua bab memilikinya) dan selalu disertai dengan persyaratan implementasi terkait, di mana keputusan yang didokumentasikan tersebut harus benar-benar diterapkan. Intinya di sini adalah bahwa memverifikasi keberadaan dokumentasi dan memastikan implementasi yang sebenarnya merupakan dua kegiatan yang terpisah.

Ada dua faktor utama yang mendasari dimasukkannya persyaratan-persyaratan ini. Faktor pertama adalah bahwa persyaratan keamanan sering kali melibatkan penerapan aturan, misalnya jenis file apa saja yang boleh diunggah, kontrol bisnis apa saja yang harus diterapkan, serta karakter apa saja yang diperbolehkan untuk bidang tertentu. Aturan-aturan ini akan berbeda untuk setiap aplikasi, dan oleh karena itu, ASVS tidak dapat secara preskriptif menentukan seperti apa aturan tersebut seharusnya, dan lembar panduan singkat atau tanggapan yang lebih terperinci pun tidak akan membantu dalam hal ini. Demikian pula, tanpa dokumentasi keputusan-keputusan ini, tidak akan mungkin untuk melakukan verifikasi terhadap persyaratan yang mengimplementasikan keputusan-keputusan tersebut.

Faktor pendorong kedua adalah bahwa untuk persyaratan tertentu, penting untuk memberikan keleluasaan dalam pengembangan aplikasi terkait cara menangani tantangan keamanan tertentu. Misalnya, pada versi ASVS sebelumnya, aturan batas waktu sesi sangat ketat. Dalam praktiknya, banyak aplikasi, terutama yang berorientasi pada konsumen, menerapkan aturan yang jauh lebih longgar dan lebih memilih untuk menerapkan langkah-langkah mitigasi lain sebagai gantinya. Oleh karena itu, persyaratan dokumentasi secara eksplisit memberikan keleluasaan dalam hal ini.

Jelaslah bahwa pengembang individu tidak diharapkan untuk membuat dan mendokumentasikan keputusan-keputusan tersebut; sebaliknya, organisasi secara keseluruhan lah yang akan mengambil keputusan-keputusan tersebut dan memastikan bahwa keputusan-keputusan itu dikomunikasikan kepada para pengembang, yang kemudian akan memastikan untuk mematuhinya.

Memberikan spesifikasi dan desain fitur serta fungsionalitas baru kepada para pengembang merupakan bagian standar dari pengembangan perangkat lunak. Demikian pula, para pengembang diharapkan menggunakan komponen dan mekanisme antarmuka pengguna yang umum, alih-alih membuat keputusan sendiri setiap kali. Oleh karena itu, memperluas hal ini ke bidang keamanan seharusnya tidak dianggap mengejutkan atau kontroversial.

Ada juga fleksibilitas dalam hal cara mencapai hal ini. Keputusan keamanan dapat didokumentasikan dalam sebuah dokumen tertulis, yang diharapkan dapat dijadikan acuan oleh para pengembang. Atau, keputusan keamanan dapat didokumentasikan dan diimplementasikan dalam pustaka kode umum yang wajib digunakan oleh semua pengembang. Dalam kedua kasus tersebut, hasil yang diinginkan tetap tercapai.

## Tingkat Verifikasi Keamanan Aplikasi

ASVS menetapkan tiga tingkatan verifikasi keamanan, dengan setiap tingkatan memiliki tingkat kedalaman dan kompleksitas yang semakin tinggi. Tujuan umumnya adalah agar organisasi memulai dari tingkatan pertama untuk menangani masalah keamanan yang paling kritis, kemudian naik ke tingkatan yang lebih tinggi sesuai dengan kebutuhan organisasi dan aplikasi. Tingkatan-tingkatan tersebut dapat disebut sebagai L1, L2, dan L3 dalam dokumen dan teks persyaratan.

Setiap tingkat ASVS menunjukkan persyaratan keamanan yang harus dipenuhi pada tingkat tersebut, sedangkan persyaratan pada tingkat yang lebih tinggi disajikan sebagai rekomendasi.

Untuk menghindari persyaratan yang tumpang tindih atau persyaratan yang tidak lagi relevan pada tingkat yang lebih tinggi, beberapa persyaratan berlaku untuk tingkat tertentu namun memiliki ketentuan yang lebih ketat pada tingkat yang lebih tinggi.

### Tingkat penilaian

Tingkat-tingkat tersebut ditentukan melalui evaluasi berbasis prioritas terhadap setiap persyaratan, yang didasarkan pada pengalaman dalam menerapkan dan menguji persyaratan keamanan. Fokus utamanya adalah membandingkan pengurangan risiko dengan upaya yang diperlukan untuk menerapkan persyaratan tersebut. Faktor penting lainnya adalah menjaga agar hambatan untuk memulai tetap rendah.

Pengurangan risiko mempertimbangkan sejauh mana persyaratan tersebut menurunkan tingkat risiko keamanan dalam aplikasi, dengan memperhitungkan faktor-faktor dampak klasik berupa Kerahasiaan, Integritas, dan Ketersediaan, serta mempertimbangkan apakah hal ini merupakan lapisan pertahanan utama atau apakah hal ini dapat dikategorikan sebagai pertahanan berlapis.

Diskusi mendalam mengenai kriteria dan keputusan penetapan tingkatan tersebut telah menghasilkan alokasi yang seharusnya berlaku untuk sebagian besar kasus, meskipun diakui bahwa hal ini mungkin tidak sepenuhnya sesuai untuk setiap situasi. Artinya, dalam kasus tertentu, organisasi mungkin ingin memprioritaskan persyaratan dari tingkatan yang lebih tinggi lebih awal berdasarkan pertimbangan risiko spesifik mereka sendiri.

Jenis-jenis persyaratan pada setiap tingkat dapat digambarkan sebagai berikut.

### Tingkat 1

Tingkat ini mencakup persyaratan minimum yang perlu dipertimbangkan dalam mengamankan suatu aplikasi dan merupakan titik awal yang sangat penting. Tingkat ini mencakup sekitar 20% dari persyaratan ASVS. Tujuan dari tingkat ini adalah untuk meminimalkan jumlah persyaratan, guna mengurangi hambatan untuk memulai.

Persyaratan-persyaratan ini umumnya bersifat kritis atau mendasar, yaitu persyaratan pertahanan tingkat pertama untuk mencegah serangan umum yang tidak memerlukan kerentanan atau prasyarat lain agar dapat dieksploitasi.

Selain persyaratan lapisan pertahanan pertama, ada beberapa persyaratan yang dampaknya lebih kecil pada tingkat yang lebih tinggi, seperti persyaratan yang berkaitan dengan kata sandi. Persyaratan tersebut lebih penting untuk Tingkat 1, karena pada tingkat yang lebih tinggi, persyaratan otentikasi multi-faktor mulai berlaku.

Tingkat 1 belum tentu dapat diuji penetrasi oleh penguji eksternal yang tidak memiliki akses internal ke dokumentasi atau kode (seperti pengujian “black box”), meskipun jumlah persyaratan yang lebih sedikit seharusnya membuatnya lebih mudah untuk diverifikasi.

### Tingkat 2

Sebagian besar aplikasi seharusnya berupaya mencapai tingkat keamanan ini. Sekitar 50% dari persyaratan dalam ASVS termasuk dalam kategori L2, yang berarti sebuah aplikasi harus menerapkan sekitar 70% dari persyaratan dalam ASVS (seluruh persyaratan L1 dan L2) agar memenuhi standar L2.

Persyaratan ini umumnya berkaitan dengan serangan yang kurang umum atau langkah-langkah perlindungan yang lebih rumit terhadap serangan yang umum. Persyaratan tersebut mungkin masih berfungsi sebagai lapisan pertahanan pertama, atau mungkin memerlukan prasyarat tertentu agar serangan tersebut berhasil.

### Tingkat 3

Tingkat ini seharusnya menjadi target bagi aplikasi yang ingin menunjukkan tingkat keamanan tertinggi, dan mencakup sekitar 30% persyaratan terakhir yang harus dipenuhi.

Persyaratan dalam bagian ini umumnya berupa mekanisme pertahanan berlapis atau pengendalian lain yang bermanfaat namun sulit diterapkan.

### Tingkat mana yang ingin dicapai

Tingkat-tingkat yang didasarkan pada prioritas ini dimaksudkan untuk menggambarkan tingkat kematangan keamanan aplikasi organisasi dan aplikasi itu sendiri. Alih-alih ASVS secara tegas menentukan tingkat mana yang harus dicapai oleh suatu aplikasi, organisasi sebaiknya menganalisis risikonya dan memutuskan tingkat mana yang menurutnya sesuai, tergantung pada tingkat sensitivitas aplikasi dan, tentu saja, ekspektasi para pengguna aplikasi tersebut.

Misalnya, sebuah perusahaan rintisan yang masih dalam tahap awal dan hanya mengumpulkan data sensitif dalam jumlah terbatas mungkin memutuskan untuk berfokus pada Tingkat 1 sebagai sasaran keamanan awalnya, tetapi sebuah bank mungkin akan kesulitan meyakinkan pelanggannya bahwa aplikasi perbankan daringnya layak menggunakan tingkat keamanan di bawah Tingkat 3.

## Cara menggunakan ASVS

### Struktur ASVS

ASVS terdiri dari total sekitar 350 persyaratan yang dibagi ke dalam 17 bab, yang masing-masing dibagi lagi ke dalam beberapa bagian.

Tujuan dari pembagian bab dan bagian ini adalah untuk mempermudah pemilihan atau penyaringan bab dan bagian berdasarkan hal-hal yang relevan bagi penerapan tertentu. Misalnya, untuk API machine-to-machine, persyaratan dalam Bab V3 yang berkaitan dengan antarmuka web tidak akan relevan. Jika OAuth atau WebRTC tidak digunakan, maka bab-bab tersebut juga dapat diabaikan.

### Strategi Peluncuran

Rilis ASVS mengikuti pola "Major.Minor.Patch", dan angka-angka tersebut memberikan informasi mengenai perubahan yang terjadi dalam rilis tersebut. Pada rilis major, angka pertama yang berubah; pada rilis minor, angka kedua yang berubah; dan pada rilis patch, angka ketiga yang berubah.

* Rilis besar (Major) - Perombakan menyeluruh; hampir semua hal mungkin telah berubah, termasuk nomor persyaratan. Diperlukan evaluasi ulang untuk memastikan kepatuhan (misalnya, 4.0.3 -> 5.0.0).
* Rilis minor — Persyaratan mungkin ditambahkan atau dihapus, tetapi penomoran versi secara keseluruhan akan tetap sama. Penilaian ulang terhadap kepatuhan akan diperlukan, tetapi seharusnya lebih mudah (misalnya, 5.0.0 -> 5.1.0).
* Rilis tambalan (Patch) - Persyaratan mungkin dihapus (misalnya, jika merupakan duplikat atau sudah usang) atau dibuat lebih longgar, tetapi aplikasi yang telah memenuhi persyaratan pada rilis sebelumnya juga akan memenuhi persyaratan pada rilis tambalan tersebut (misalnya, 5.0.0 -> 5.0.1).

Hal di atas secara khusus berkaitan dengan persyaratan dalam ASVS. Perubahan pada teks di sekitarnya dan konten lain seperti lampiran tidak akan dianggap sebagai perubahan yang berdampak signifikan.

### Fleksibilitas dengan ASVS

Beberapa poin yang dijelaskan di atas, seperti persyaratan dokumentasi dan mekanisme tingkatan, memungkinkan penggunaan ASVS secara lebih fleksibel dan disesuaikan dengan kebutuhan organisasi.

Selain itu, organisasi sangat dianjurkan untuk membuat cabang (fork) yang disesuaikan dengan organisasi atau domain tertentu, yang menyesuaikan persyaratan berdasarkan karakteristik dan tingkat risiko spesifik dari aplikasi mereka. Namun, penting untuk menjaga keterlacakan sehingga pemenuhan persyaratan 4.1.1 memiliki arti yang sama di seluruh versi.

Idealnya, setiap organisasi sebaiknya menyusun ASVS yang disesuaikan dengan kebutuhannya sendiri, dengan menghilangkan bagian-bagian yang tidak relevan (misalnya, GraphQL, WebSockets, SOAP, jika tidak digunakan). Versi atau lampiran ASVS khusus organisasi juga merupakan wadah yang tepat untuk memberikan panduan implementasi khusus organisasi, yang merinci pustaka atau sumber daya yang harus digunakan dalam memenuhi persyaratan.

### Cara Merujuk pada Persyaratan ASVS

Setiap persyaratan memiliki pengenal dalam format `<chapter>.<section>.<requirement>`, di mana setiap elemen berupa angka. Misalnya, `1.11.3`.

* Nilai `<chapter>` menunjukkan bab asal persyaratan tersebut; misalnya, semua persyaratan `1.#.#` berasal dari bab ‘Pengkodean dan Pembersihan’.
* Nilai `<section>` mengacu pada bagian dalam bab tersebut di mana persyaratan tersebut tercantum, misalnya: semua persyaratan `1.2.#` terdapat dalam bagian ‘Pencegahan Injeksi’ pada bab ‘Pengkodean dan Sanitasi’.
* Nilai `<requirement>` mengidentifikasi persyaratan spesifik dalam bab dan bagian tersebut, misalnya, `1.2.5` yang pada versi 5.0.0 standar ini berbunyi:

> Pastikan bahwa aplikasi tersebut terlindungi dari serangan injeksi perintah sistem operasi (OS Command Injection) dan bahwa panggilan sistem (system calls) operasi menggunakan kueri sistem operasi yang diparameterkan atau mengenkode keluaran baris perintah sesuai konteks.

Karena pengenal (identifier) dapat berubah antar versi standar, disarankan agar dokumen, laporan, atau alat lain menggunakan format berikut: `v<version>-<chapter>.<section>.<requirement>`, di mana: 'version' adalah tag versi ASVS. Misalnya: `v5.0.0-1.2.5` akan diartikan secara spesifik sebagai persyaratan ke-5 dalam bagian 'Pencegahan Injeksi' dari bab 'Pengkodean dan Sanitasi' pada versi 5.0.0. (Hal ini dapat diringkas sebagai `v<version>-<requirement_identifier>`.)

Catatan: Huruf `v` yang mendahului nomor versi dalam format tersebut harus selalu ditulis dengan huruf kecil.

Jika identifier digunakan tanpa menyertakan elemen `v<version>`, maka identifier tersebut dianggap merujuk pada konten Standar Verifikasi Keamanan Aplikasi terbaru. Seiring berkembangnya standar ini, hal tersebut dapat menimbulkan masalah; oleh karena itu, penulis atau pengembang disarankan untuk menyertakan elemen version.

Daftar persyaratan ASVS tersedia dalam format CSV, JSON, dan format lain yang mungkin berguna sebagai referensi atau untuk keperluan pemrograman.

### Membuat fork dari ASVS

Organisasi dapat memperoleh manfaat dari penerapan ASVS dengan memilih salah satu dari tiga tingkatan tersebut atau dengan membuat cabang khusus bidang yang menyesuaikan persyaratan sesuai dengan tingkat risiko aplikasi. Pembuatan cabang semacam ini dianjurkan, asalkan tetap menjaga keterlacakan sehingga pemenuhan persyaratan 4.1.1 memiliki arti yang sama di seluruh versi.

Idealnya, setiap organisasi sebaiknya menyusun ASVS yang disesuaikan dengan kebutuhannya sendiri, dengan menghilangkan bagian-bagian yang tidak relevan (misalnya, GraphQL, WebSockets, SOAP, jika tidak digunakan). Pembuatan cabang (forking) sebaiknya dimulai dengan ASVS Level 1 sebagai acuan dasar, kemudian ditingkatkan ke Level 2 atau 3 sesuai dengan tingkat risiko aplikasi.

## Contoh penerapan ASVS

ASVS dapat digunakan untuk mengevaluasi keamanan suatu aplikasi, dan hal ini akan dibahas lebih mendalam pada bab berikutnya. Namun, telah diidentifikasi beberapa kegunaan potensial lainnya untuk ASVS (atau versi fork-nya).

### Panduan Arsitektur Keamanan yang Terperinci

Salah satu kegunaan yang paling umum dari Standar Verifikasi Keamanan Aplikasi (ASVS) adalah sebagai sumber daya bagi para arsitek keamanan. Sumber daya yang tersedia mengenai cara membangun arsitektur aplikasi yang aman masih terbatas, terutama untuk aplikasi modern. ASVS dapat digunakan untuk mengisi kekosongan tersebut dengan memungkinkan para arsitek keamanan memilih kontrol yang lebih baik untuk mengatasi masalah umum, seperti pola perlindungan data dan strategi validasi input. Persyaratan arsitektur dan dokumentasi akan sangat berguna dalam hal ini.

### Sebagai Panduan Pemrograman Aman yang Khusus

ASVS dapat digunakan sebagai landasan untuk menyusun pedoman penulisan kode yang aman selama pengembangan aplikasi, sehingga membantu pengembang memastikan bahwa mereka tetap memperhatikan aspek keamanan saat membuat perangkat lunak. Meskipun ASVS dapat dijadikan landasan, organisasi sebaiknya menyusun pedoman khusus mereka sendiri yang jelas dan terpadu, dan idealnya disusun berdasarkan masukan dari insinyur keamanan atau arsitek keamanan. Sebagai kelanjutan dari hal ini, organisasi didorong untuk, sejauh mungkin, menyiapkan mekanisme dan pustaka keamanan yang telah disetujui yang dapat dirujuk dalam panduan tersebut dan digunakan oleh pengembang.

### Sebagai Panduan untuk Pengujian Unit dan Integrasi Otomatis

ASVS dirancang agar sangat mudah diuji. Beberapa verifikasi bersifat teknis, sedangkan persyaratan lain (seperti persyaratan arsitektur dan dokumentasi) mungkin memerlukan tinjauan dokumentasi atau arsitektur. Dengan membuat uji unit dan integrasi yang menguji dan melakukan fuzzing terhadap kasus penyalahgunaan tertentu dan relevan yang terkait dengan persyaratan yang dapat diverifikasi secara teknis, seharusnya lebih mudah untuk memeriksa apakah kontrol-kontrol ini beroperasi dengan benar pada setiap build. Misalnya, pengujian tambahan dapat dibuat untuk rangkaian pengujian pengontrol login, yang menguji parameter nama pengguna untuk nama pengguna default umum, enumerasi akun, brute forcing, injeksi LDAP dan SQL, serta XSS. Demikian pula, pengujian pada parameter kata sandi harus mencakup kata sandi umum, panjang kata sandi, injeksi byte null, penghapusan parameter, XSS, dan lainnya.

### Untuk Pelatihan Pengembangan yang Aman

ASVS juga dapat digunakan untuk mendefinisikan karakteristik perangkat lunak yang aman. Banyak kursus _secure coding_ hanyalah kursus peretasan etis yang diselingi sedikit tips pengkodean. Hal ini belum tentu membantu pengembang menulis kode yang lebih aman. Sebaliknya, kursus pengembangan aman dapat menggunakan ASVS dengan fokus yang kuat pada mekanisme positif yang terdapat dalam ASVS, alih-alih 10 hal negatif yang harus dihindari. Struktur ASVS juga menyediakan kerangka logis untuk membahas berbagai topik saat mengamankan sebuah aplikasi.

### Sebagai Kerangka Kerja untuk Mengarahkan Pengadaan Perangkat Lunak yang Aman

ASVS merupakan kerangka kerja yang sangat baik untuk membantu proses pengadaan perangkat lunak yang aman atau pengadaan layanan pengembangan khusus. Pembeli cukup menetapkan persyaratan bahwa perangkat lunak yang ingin mereka peroleh harus dikembangkan sesuai dengan tingkat ASVS X, dan meminta penjual untuk membuktikan bahwa perangkat lunak tersebut memenuhi tingkat ASVS X.

## Penerapan ASVS dalam Praktik

Ancaman yang berbeda memiliki motivasi yang berbeda pula. Beberapa industri memiliki aset informasi dan teknologi yang unik serta persyaratan kepatuhan regulasi yang spesifik sesuai bidangnya.

Organisasi sangat dianjurkan untuk menganalisis secara mendalam karakteristik risiko unik mereka berdasarkan sifat bisnisnya, dan berdasarkan risiko serta persyaratan bisnis tersebut, menentukan tingkat ASVS yang sesuai.
