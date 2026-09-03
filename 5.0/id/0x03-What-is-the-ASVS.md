# Apa itu ASVS?

Application Security Verification Standard (ASVS) mendefinisikan persyaratan keamanan untuk aplikasi dan layanan web, serta merupakan sumber daya yang berharga bagi siapa saja yang bertujuan untuk merancang, mengembangkan, dan memelihara aplikasi yang aman atau mengevaluasi keamanannya.

Bab ini menguraikan aspek-aspek esensial dari penggunaan ASVS, termasuk cakupannya, struktur level berbasis prioritas, dan kasus penggunaan (_use cases_) utama untuk standar ini.

## Cakupan ASVS

Cakupan (_scope_) dari ASVS didefinisikan oleh namanya: Application, Security, Verification, dan Standard. ASVS menetapkan persyaratan mana yang dimasukkan atau dikecualikan, dengan tujuan utama untuk mengidentifikasi prinsip-prinsip keamanan yang harus dicapai. Cakupan ini juga mempertimbangkan persyaratan dokumentasi, yang berfungsi sebagai fondasi bagi persyaratan implementasi.

Tidak ada yang namanya cakupan bagi penyerang (_attacker_). Oleh karena itu, persyaratan ASVS harus dievaluasi bersamaan dengan panduan untuk aspek-aspek lain dari siklus hidup aplikasi, termasuk proses CI/CD, _hosting_, dan aktivitas operasional.

### Aplikasi (Application)

ASVS mendefinisikan "aplikasi" sebagai produk perangkat lunak yang sedang dikembangkan, di mana kontrol keamanan harus diintegrasikan ke dalamnya. ASVS tidak menetapkan aktivitas siklus hidup pengembangan atau mendikte bagaimana aplikasi harus dibangun melalui _pipeline_ CI/CD; melainkan menentukan hasil keamanan yang harus dicapai dalam produk itu sendiri.

Komponen yang melayani, mengubah, atau memvalidasi lalu lintas HTTP, seperti Web Application Firewall (WAF), _load balancer_, atau _proxy_, dapat dianggap sebagai bagian dari aplikasi untuk tujuan spesifik tersebut, karena beberapa kontrol keamanan bergantung langsung padanya atau dapat diimplementasikan melaluinya. Komponen-komponen ini harus dipertimbangkan untuk persyaratan yang berkaitan dengan respons yang di-cache, _rate limiting_, atau pembatasan koneksi masuk dan keluar berdasarkan sumber dan tujuan.

Sebaliknya, ASVS umumnya mengecualikan persyaratan yang tidak relevan secara langsung dengan aplikasi atau di mana konfigurasinya berada di luar tanggung jawab aplikasi. Sebagai contoh, masalah DNS biasanya dikelola oleh tim atau fungsi yang terpisah.

Demikian pula, meskipun aplikasi bertanggung jawab atas cara mengonsumsi input dan menghasilkan output, jika proses eksternal berinteraksi dengan aplikasi atau datanya, proses tersebut dianggap di luar cakupan (_out of scope_) ASVS. Misalnya, pencadangan (_backup_) aplikasi atau datanya biasanya merupakan tanggung jawab proses eksternal dan tidak dikontrol oleh aplikasi atau pengembangnya.

### Keamanan (Security)

Setiap persyaratan harus memiliki dampak yang terbukti terhadap keamanan. Absennya suatu persyaratan harus mengakibatkan aplikasi menjadi kurang aman, dan mengimplementasikan persyaratan tersebut harus mengurangi kemungkinan atau dampak dari risiko keamanan.

Semua pertimbangan lainnya, seperti aspek fungsional, gaya penulisan kode (_code style_), atau persyaratan kebijakan, berada di luar cakupan.

### Verifikasi (Verification)

Persyaratan harus dapat diverifikasi (_verifiable_), dan verifikasi tersebut harus menghasilkan keputusan "gagal" (_fail_) atau "lulus" (_pass_).

### Standar (Standard)

ASVS dirancang untuk menjadi kumpulan persyaratan keamanan yang diimplementasikan untuk mematuhi standar. Ini berarti bahwa persyaratan dibatasi untuk mendefinisikan tujuan keamanan yang ingin dicapai. Informasi relevan lainnya dapat dibangun di atas ASVS atau dihubungkan melalui pemetaan (_mappings_).

Secara khusus, OWASP memiliki banyak proyek, dan ASVS secara sengaja menghindari tumpang tindih dengan konten di proyek lain. Sebagai contoh, pengembang mungkin memiliki pertanyaan, "bagaimana cara mengimplementasikan persyaratan tertentu dalam teknologi atau lingkungan spesifik saya," dan ini harus dicakup oleh proyek _Cheat Sheet Series_. Verifikator mungkin memiliki pertanyaan "bagaimana cara menguji persyaratan ini di lingkungan ini," dan ini harus dicakup oleh proyek _Web Security Testing Guide_.

Meskipun ASVS tidak hanya ditujukan untuk digunakan oleh pakar keamanan, standar ini tetap mengharapkan pembaca memiliki pengetahuan teknis untuk memahami kontennya atau memiliki kemampuan untuk meneliti konsep-konsep tertentu.

### Persyaratan (Requirement)

Kata _requirement_ (persyaratan) digunakan secara khusus dalam ASVS karena menggambarkan apa yang harus dicapai untuk memenuhinya. ASVS hanya berisi persyaratan wajib (_must_) dan tidak berisi rekomendasi (_should_) sebagai kondisi utama.

Dengan kata lain, rekomendasi, baik yang hanya berupa salah satu dari banyak opsi untuk menyelesaikan masalah atau pertimbangan gaya penulisan kode, tidak memenuhi definisi untuk menjadi sebuah persyaratan.

Persyaratan ASVS dimaksudkan untuk menangani prinsip-prinsip keamanan tertentu tanpa terlalu spesifik pada implementasi atau teknologi, sekaligus memberikan penjelasan mandiri tentang mengapa persyaratan itu ada. Ini juga berarti persyaratan tidak dibangun di sekitar metode verifikasi atau implementasi tertentu.

### Keputusan Keamanan yang Terdokumentasi

Dalam keamanan perangkat lunak, merencanakan desain keamanan dan mekanisme yang akan digunakan sejak awal akan mengarah pada implementasi yang lebih konsisten dan andal pada produk atau fitur yang selesai dibuat.

Selain itu, untuk persyaratan tertentu, implementasinya akan rumit dan sangat spesifik dengan kebutuhan aplikasi. Contoh umumnya meliputi hak akses (_permissions_), validasi input, dan kontrol perlindungan di sekitar berbagai tingkat data sensitif.

Untuk mengatasi hal ini, daripada membuat pernyataan umum seperti "semua data harus dienkripsi" atau mencoba mencakup setiap kemungkinan kasus penggunaan dalam satu persyaratan, persyaratan dokumentasi dimasukkan untuk mewajibkan agar pendekatan dan konfigurasi pengembang aplikasi terhadap jenis kontrol ini didokumentasikan. Dokumentasi ini kemudian dapat ditinjau kesesuaiannya dan implementasi aktualnya dapat dibandingkan dengan dokumentasi untuk menilai apakah implementasi sesuai dengan ekspektasi.

Persyaratan ini dimaksudkan untuk mendokumentasikan keputusan yang telah diambil oleh organisasi pengembang aplikasi mengenai cara mengimplementasikan persyaratan keamanan tertentu.

Persyaratan dokumentasi selalu berada di bagian pertama dari suatu bab (meskipun tidak setiap bab memilikinya) dan selalu memiliki persyaratan implementasi terkait di mana keputusan yang didokumentasikan tersebut harus benar-benar diterapkan. Poin di sini adalah bahwa memverifikasi keberadaan dokumentasi dan memverifikasi implementasi aktualnya adalah dua aktivitas yang terpisah.

Ada dua pendorong utama dimasukannya persyaratan ini. Pendorong pertama adalah bahwa persyaratan keamanan sering kali melibatkan penegakan aturan, misal: jenis file apa yang diizinkan untuk diunggah, kontrol bisnis apa yang harus ditegakkan, karakter apa saja yang diizinkan untuk kolom tertentu. Aturan-aturan ini akan berbeda untuk setiap aplikasi, dan oleh karena itu, ASVS tidak dapat mendefinisikan secara preskriptif bagaimana aturan tersebut seharusnya, begitu pula _cheat sheet_ atau respons yang lebih detail tidak dapat membantu dalam kasus ini. Demikian pula, tanpa keputusan ini didokumentasikan, verifikasi persyaratan yang mengimplementasikan keputusan tersebut tidak akan mungkin dilakukan.

Pendorong kedua adalah untuk persyaratan tertentu, penting untuk memberikan fleksibilitas kepada pengembang aplikasi mengenai cara mengatasi tantangan keamanan tertentu. Misalnya, dalam versi ASVS sebelumnya, aturan _session timeout_ sangat preskriptif. Secara praktis, banyak aplikasi (terutama yang berhadapan langsung dengan konsumen) memiliki aturan yang jauh lebih longgar dan memilih untuk mengimplementasikan kontrol mitigasi lainnya. Oleh karena itu, persyaratan dokumentasi secara eksplisit memberikan fleksibilitas di seputar hal ini.

Jelas, tidak diharapkan bahwa masing-masing pengembang individu yang membuat dan mendokumentasikan keputusan ini, melainkan organisasi secara keseluruhan yang mengambil keputusan tersebut dan menyampaikannya kepada pengembang yang kemudian mematuhinya.

Menyediakan spesifikasi dan desain fitur baru kepada pengembang adalah bagian standar dari pengembangan perangkat lunak. Demikian pula, pengembang diharapkan menggunakan komponen umum dan mekanisme _user interface_ yang ada alih-alih membuat keputusan sendiri setiap saat. Dengan demikian, memperluas hal ini ke ranah keamanan seharusnya tidak dipandang sebagai hal yang mengejutkan atau kontroversial.

Ada juga fleksibilitas tentang cara mencapai hal ini. Keputusan keamanan dapat didokumentasikan dalam dokumen tertulis yang dirujuk oleh pengembang. Atau, keputusan keamanan dapat didokumentasikan dan diimplementasikan dalam pustaka kode umum (_common code library_) yang diwajibkan untuk digunakan oleh semua pengembang. Dalam kedua kasus tersebut, hasil yang diinginkan tetap tercapai.

## Tingkat Verifikasi Keamanan Aplikasi (Application Security Verification Levels)

ASVS mendefinisikan tiga tingkat verifikasi keamanan, di mana setiap tingkat meningkat dalam kedalaman dan kompleksitasnya. Tujuan umumnya adalah agar organisasi memulai dari tingkat pertama untuk mengatasi masalah keamanan yang paling krusial, lalu naik ke tingkat yang lebih tinggi sesuai dengan kebutuhan organisasi dan aplikasi. Tingkat ini dapat ditampilkan sebagai L1, L2, dan L3 dalam dokumen dan teks persyaratan.

Setiap level ASVS menunjukkan persyaratan keamanan yang wajib dicapai pada level tersebut, dengan sisa persyaratan di level yang lebih tinggi berfungsi sebagai rekomendasi.

Untuk menghindari persyaratan duplikat atau persyaratan yang tidak lagi relevan pada level yang lebih tinggi, beberapa persyaratan berlaku untuk level tertentu tetapi memiliki kondisi yang lebih ketat untuk level di atasnya.

### Evaluasi Level

Level-level ini didefinisikan berdasarkan evaluasi prioritas dari setiap persyaratan yang berpatokan pada pengalaman implementasi dan pengujian keamanan. Fokus utamanya adalah membandingkan pengurangan risiko (_risk reduction_) dengan upaya untuk mengimplementasikan persyaratan tersebut (_effort to implement_). Faktor kunci lainnya adalah menjaga ambang batas masuk (_barrier to entry_) tetap rendah.

Pengurangan risiko mempertimbangkan sejauh mana persyaratan tersebut mengurangi tingkat risiko keamanan dalam aplikasi, dengan memperhitungkan faktor dampak klasik _Confidentiality_, _Integrity_, dan _Availability_, serta mempertimbangkan apakah ini merupakan lapisan pertahanan utama (_primary layer of defense_) atau pertahanan berlapis (_defense in depth_).

Diskusi ketat di sekitar kriteria dan keputusan tingkat telah menghasilkan alokasi yang seharusnya berlaku untuk sebagian besar kasus, sambil menerima bahwa hal ini mungkin tidak 100% cocok untuk setiap situasi. Ini berarti dalam kasus tertentu, organisasi mungkin ingin memprioritaskan persyaratan dari level yang lebih tinggi lebih awal berdasarkan pertimbangan risiko spesifik mereka sendiri.

Jenis persyaratan di setiap level dapat dikarakterisasikan sebagai berikut:

### Level 1

Tingkat ini berisi persyaratan minimum yang harus dipertimbangkan saat mengamankan aplikasi dan mewakili titik awal yang sangat penting. Tingkat ini berisi sekitar 20% dari seluruh persyaratan ASVS. Tujuan dari tingkat ini adalah memiliki persyaratan sesedikit mungkin untuk menurunkan ambang batas masuk.

Persyaratan ini umumnya kritis atau mendasar, sebagai pertahanan lapisan pertama untuk mencegah serangan umum yang tidak memerlukan kerentanan atau prakondisi lain agar dapat dieksploitasi.

Selain persyaratan pertahanan lapisan pertama, beberapa persyaratan memiliki dampak yang lebih kecil pada level yang lebih tinggi, seperti persyaratan yang berkaitan dengan kata sandi. Persyaratan tersebut lebih penting untuk Level 1, karena pada level yang lebih tinggi, persyaratan otentikasi multi-faktor (_multi-factor authentication_) menjadi lebih relevan.

Level 1 tidak selalu dapat diuji dengan _penetration test_ oleh penguji eksternal tanpa akses internal ke dokumentasi atau kode (seperti pengujian _black box_), meskipun jumlah persyaratan yang lebih sedikit seharusnya membuatnya lebih mudah untuk diverifikasi.

### Level 2

Sebagian besar aplikasi harus berusaha mencapai tingkat keamanan ini. Sekitar 50% persyaratan dalam ASVS berada di L2, yang berarti aplikasi perlu mengimplementasikan sekitar 70% dari seluruh persyaratan ASVS (semua persyaratan L1 dan L2) agar sesuai dengan L2.

Persyaratan ini umumnya berkaitan dengan serangan yang kurang umum atau perlindungan yang lebih rumit terhadap serangan umum. Persyaratan ini mungkin masih berupa pertahanan lapisan pertama, atau mungkin memerlukan prakondisi tertentu agar serangan berhasil.

### Level 3

Tingkat ini harus menjadi target bagi aplikasi yang ingin menunjukkan tingkat keamanan tertinggi dan menyediakan sisa ~30% persyaratan terakhir yang harus dipenuhi.

Persyaratan pada bagian ini umumnya merupakan mekanisme pertahanan berlapis (_defense-in-depth_) atau kontrol lain yang berguna tetapi sulit diimplementasikan.

### Level Mana yang Harus Dicapai

Level berbasis prioritas dimaksudkan untuk memberikan gambaran tentang kematangan keamanan aplikasi (_application security maturity_) dari organisasi dan aplikasi tersebut. Daripada ASVS mendikte secara kaku level apa yang harus dicapai oleh suatu aplikasi, organisasi harus menganalisis risikonya dan memutuskan level mana yang menurut mereka sesuai, tergantung pada sensitivitas aplikasi dan ekspektasi dari pengguna aplikasi.

Sebagai contoh, _startup_ tahap awal yang hanya mengumpulkan data sensitif secara terbatas dapat memutuskan untuk berfokus pada Level 1 untuk target keamanan awalnya, tetapi sebuah bank mungkin akan kesulitan membenarkan tingkat di bawah Level 3 kepada nasabahnya untuk aplikasi perbankan _online_ mereka.

## Cara Menggunakan ASVS

### Struktur ASVS

ASVS terdiri dari total sekitar 350 persyaratan yang dibagi menjadi 17 bab, di mana masing-masing bab dibagi lagi menjadi beberapa bagian.

Tujuan dari pembagian bab dan bagian ini adalah untuk mempermudah pemeliharaan atau penyaringan bab dan bagian berdasarkan apa yang relevan untuk aplikasi. Misalnya, untuk API _machine-to-machine_, persyaratan dalam bab V3 yang terkait dengan _web frontend_ tidak akan relevan. Jika tidak ada penggunaan OAuth atau WebRTC, bab-bab tersebut juga dapat diabaikan.

### Strategi Rilis

Rilis ASVS mengikuti pola "Major.Minor.Patch" dan nomor-nomor tersebut memberikan informasi tentang apa yang telah berubah dalam rilis tersebut:

* **Major release** - Restrukturisasi penuh, hampir semuanya dapat berubah, termasuk nomor persyaratan. Reevaluasi kepatuhan akan diperlukan (misalnya, 4.0.3 -> 5.0.0).
* **Minor release** - Persyaratan dapat ditambahkan atau dihapus, tetapi penomoran secara keseluruhan akan tetap sama. Reevaluasi kepatuhan akan diperlukan, tetapi seharusnya lebih mudah (misalnya, 5.0.0 -> 5.1.0).
* **Patch release** - Persyaratan dapat dihapus (misalnya, jika duplikat atau usang) atau dibuat lebih longgar, tetapi aplikasi yang mematuhi rilis sebelumnya juga akan mematuhi rilis _patch_ ini (misalnya, 5.0.0 -> 5.0.1).

Hal-hal di atas secara khusus berkaitan dengan persyaratan dalam ASVS. Perubahan pada teks sekitarnya dan konten lain seperti lampiran tidak dianggap sebagai perubahan besar (_breaking change_).

### Fleksibilitas dalam ASVS

Beberapa poin yang dijelaskan di atas, seperti persyaratan dokumentasi dan mekanisme level, memberikan kemampuan untuk menggunakan ASVS secara lebih fleksibel dan spesifik sesuai kebutuhan organisasi.

Selain itu, organisasi sangat didorong untuk membuat _fork_ khusus organisasi atau domain yang menyesuaikan persyaratan berdasarkan karakteristik spesifik dan tingkat risiko aplikasi mereka. Namun, penting untuk menjaga keterlacakan (_traceability_) sehingga memenuhi persyaratan 4.1.1 berarti hal yang sama di semua versi.

Ideally, setiap organisasi harus membuat ASVS tersendiri yang disesuaikan, dengan mengabaikan bagian yang tidak relevan (misalnya GraphQL, WebSockets, SOAP, jika tidak digunakan). Versi atau suplemen ASVS khusus organisasi juga merupakan tempat yang baik untuk menyediakan panduan implementasi internal, yang merinci pustaka (_libraries_) atau sumber daya yang digunakan saat mematuhi persyaratan.

### Cara Merujuk Persyaratan ASVS

Setiap persyaratan memiliki pengenal (_identifier_) dalam format `<bab>.<bagian>.<persyaratan>`, di mana setiap elemen berupa angka. Contohnya, `1.11.3`.

* Nilai `<bab>` sesuai dengan bab asal persyaratan tersebut; contohnya, semua persyaratan `1.#.#` berasal dari bab 'Encoding and Sanitization'.
* Nilai `<bagian>` sesuai dengan bagian dalam bab tersebut di mana persyaratan muncul; contohnya: semua persyaratan `1.2.#` berada di bagian 'Injection Prevention' pada bab 'Encoding and Sanitization'.
* Nilai `<persyaratan>` mengidentifikasi persyaratan spesifik dalam bab dan bagian tersebut, misalnya `1.2.5` yang pada versi 5.0.0 dari standar ini berbunyi:

> Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding.

Karena pengenal dapat berubah antar versi standar, lebih disukai jika dokumen, laporan, atau alat lain menggunakan format berikut: `v<versi>-<bab>.<bagian>.<persyaratan>`, di mana 'versi' adalah tag versi ASVS. Contohnya: `v5.0.0-1.2.5` akan dipahami sebagai persyaratan ke-5 dalam bagian 'Injection Prevention' dari bab 'Encoding and Sanitization' pada versi 5.0.0. (Ini dapat diringkas sebagai `v<versi>-<pengenal_persyaratan>`.)

_Catatan: Huruf `v` yang mendahului nomor versi dalam format ini harus selalu menggunakan huruf kecil._

Jika pengenal digunakan tanpa menyertakan elemen `v<versi>`, maka dianggap merujuk pada konten Application Security Verification Standard terbaru. Seiring berkembang dan berubahnya standar, hal ini dapat menimbulkan masalah, itulah sebabnya penulis atau pengembang harus menyertakan elemen versi.

Daftar persyaratan ASVS disediakan dalam format CSV, JSON, dan format lain yang dapat berguna untuk referensi atau penggunaan terprogram.

### Melakukan Fork pada ASVS

Organisasi dapat memperoleh manfaat dari mengadopsi ASVS dengan memilih salah satu dari tiga level atau dengan membuat _fork_ khusus domain yang menyesuaikan persyaratan per tingkat risiko aplikasi. Jenis _fork_ ini sangat didorong, asalkan mempertahankan keterlacakan (_traceability_) sehingga memenuhi persyaratan 4.1.1 berarti hal yang sama di semua versi.

Ideally, setiap organisasi harus membuat ASVS tersendiri yang disesuaikan, dengan mengabaikan bagian yang tidak relevan (misalnya GraphQL, Websockets, SOAP, jika tidak digunakan). Proses _forking_ harus dimulai dengan ASVS Level 1 sebagai tolok ukur (_baseline_), lalu meningkat ke Level 2 atau 3 berdasarkan risiko aplikasi.

## Kasus Penggunaan (Use Cases) ASVS

ASVS dapat digunakan untuk menilai keamanan aplikasi dan ini dijelaskan lebih mendalam di bab berikutnya. Namun, beberapa potensi penggunaan lain untuk ASVS (atau versi _fork_) telah diidentifikasi:

### Sebagai Panduan Arsitektur Keamanan Terperinci

Salah satu penggunaan ASVS yang paling umum adalah sebagai sumber daya bagi _security architect_. Sumber daya yang tersedia tentang cara membangun arsitektur aplikasi yang aman sangat terbatas, terutama untuk aplikasi modern. ASVS dapat digunakan untuk mengisi celah tersebut dengan memungkinkan _security architect_ memilih kontrol yang lebih baik untuk masalah umum, seperti pola perlindungan data dan strategi validasi input. Persyaratan arsitektur dan dokumentasi akan sangat berguna untuk tujuan ini.

### Sebagai Referensi Secure Coding Khusus

ASVS dapat digunakan sebagai dasar untuk menyiapkan referensi pengodean aman (_secure coding reference_) selama pengembangan aplikasi, membantu pengembang memastikan mereka tetap mempertimbangkan keamanan saat membuat perangkat lunak. Meskipun ASVS dapat menjadi basisnya, organisasi harus menyiapkan panduan spesifik mereka sendiri yang jelas dan terpadu, dan idealnya disiapkan berdasarkan arahan dari _security engineer_ atau _security architect_. Sebagai ekstensi dari hal ini, organisasi didorong untuk menyiapkan mekanisme keamanan dan pustaka (_libraries_) yang disetujui yang dapat dirujuk dalam panduan dan digunakan oleh pengembang.

### Sebagai Panduan untuk Pengujian Otomatis (Unit & Integration Tests)

ASVS dirancang agar sangat dapat diuji (_testable_). Beberapa verifikasi bersifat teknis sedangkan persyaratan lain (seperti persyaratan arsitektur dan dokumentasi) mungkin memerlukan peninjauan dokumentasi atau arsitektur. Dengan membangun _unit test_ dan _integration test_ yang menguji serta melakukan _fuzzing_ untuk kasus-kasus penyalahgunaan (_abuse cases_) yang spesifik dan relevan terkait dengan persyaratan teknis, akan lebih mudah untuk memastikan bahwa kontrol tersebut beroperasi dengan benar pada setiap _build_. Misalnya, pengujian tambahan dapat dibuat untuk _test suite_ kontroler _login_, menguji parameter _username_ untuk _default username_ umum, _account enumeration_, _brute force_, _LDAP/SQL injection_, dan _XSS_. Demikian pula, pengujian pada parameter _password_ harus mencakup kata sandi umum, panjang kata sandi, _null byte injection_, penghapusan parameter, _XSS_, dan lainnya.

### Untuk Pelatihan Pengembangan Aman (Secure Development Training)

ASVS juga dapat digunakan untuk mendefinisikan karakteristik perangkat lunak yang aman. Banyak kursus "secure coding" hanya berupa kursus _ethical hacking_ yang diberi sedikit tip pengodean. Ini mungkin tidak membantu pengembang untuk menulis kode yang lebih aman. Sebaliknya, kursus pengembangan aman dapat menggunakan ASVS dengan fokus kuat pada mekanisme positif yang ditemukan dalam ASVS, daripada Top 10 hal negatif yang tidak boleh dilakukan. Struktur ASVS juga memberikan alur logika yang teratur untuk mempelajari berbagai topik saat mengamankan aplikasi.

### Sebagai Kerangka Kerja Pengadaan Perangkat Lunak Aman

ASVS adalah kerangka kerja yang sangat baik untuk membantu pengadaan perangkat lunak aman atau pengadaan layanan pengembangan kustom. Pembeli hanya perlu menetapkan persyaratan bahwa perangkat lunak yang ingin mereka beli harus dikembangkan pada ASVS Level X, dan meminta penjual membuktikan bahwa perangkat lunak tersebut memenuhi ASVS Level X.

## Menerapkan ASVS dalam Praktik

Ancaman yang berbeda memiliki motivasi yang berbeda pula. Beberapa industri memiliki aset informasi/teknologi yang unik serta persyaratan kepatuhan regulasi khusus domain.

Organisasi sangat didorong untuk melihat secara mendalam karakteristik risiko unik mereka berdasarkan sifat bisnis mereka, dan berdasarkan risiko serta persyaratan bisnis tersebut, tentukan level ASVS yang sesuai.
