# V15 Secure Coding dan Architecture

## Tujuan Kontrol

Banyak persyaratan ASVS yang terkait dengan area keamanan tertentu, seperti authentication atau authorization, atau berkaitan dengan jenis fungsionalitas aplikasi tertentu, seperti logging atau file handling.

Bab ini menyediakan persyaratan keamanan umum yang perlu dipertimbangkan saat merancang dan mengembangkan aplikasi. Persyaratan ini tidak hanya berfokus pada arsitektur yang bersih (clean architecture) dan kualitas kode, tetapi juga pada praktik arsitektur dan coding tertentu yang diperlukan untuk keamanan aplikasi.

## V15.1 Dokumentasi Secure Coding dan Arsitektur

Banyak persyaratan untuk membangun arsitektur yang aman dan dapat dipertahankan (defensible) bergantung pada dokumentasi yang jelas mengenai keputusan yang dibuat terkait implementasi kontrol keamanan tertentu dan komponen yang digunakan dalam aplikasi.

Bagian ini menguraikan persyaratan dokumentasi, termasuk mengidentifikasi komponen yang dianggap mengandung "dangerous functionality" atau merupakan "risky component".

Sebuah komponen dengan "dangerous functionality" dapat berupa komponen yang dikembangkan secara internal atau komponen pihak ketiga yang melakukan operasi seperti deserialization terhadap data tidak tepercaya, parsing raw file atau data biner, dynamic code execution, atau manipulasi memory secara langsung. Kerentanan pada jenis operasi ini menimbulkan risiko tinggi terhadap kompromi aplikasi dan berpotensi mengekspos infrastruktur yang mendasarinya.

Sebuah "risky component" adalah sebuah pustaka pihak ketiga (yaitu, tidak dikembangkan secara internal) yang tidak memiliki atau memiliki kontrol keamanan yang buruk seputar proses pengembangan atau fungsionalitasnya. Contohnya mencakup komponen yang kurang terpelihara (poorly maintained), tidak lagi didukung (unsupported), berada pada tahap end-of-life, atau memiliki riwayat kerentanan yang signifikan.

Bagian ini juga menekankan pentingnya mendefinisikan jangka waktu yang sesuai untuk mengatasi kerentanan pada komponen pihak ketiga.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **15.1.1** | Verifikasi bahwa dokumentasi aplikasi mendefinisikan jangka waktu remediasi berbasis risiko untuk versi komponen pihak ketiga yang memiliki kerentanan dan untuk pembaruan pustaka secara umum, guna meminimalkan risiko dari komponen-komponen tersebut. | 1 |
| **15.1.2** | Verifikasi bahwa sebuah katalog inventaris, seperti software bill of materials (SBOM), dipelihara untuk semua pustaka pihak ketiga yang digunakan, termasuk memverifikasi bahwa komponen-komponen tersebut berasal dari repository yang telah ditentukan sebelumnya, tepercaya, dan terus terpelihara. | 2 |
| **15.1.3** | Verifikasi bahwa dokumentasi aplikasi mengidentifikasi fungsionalitas yang memakan waktu lama atau memerlukan resource besar. Hal ini harus mencakup cara mencegah hilangnya ketersediaan (availability) akibat penggunaan berlebihan terhadap fungsionalitas ini dan cara menghindari situasi di mana pembuatan sebuah response memakan waktu lebih lama daripada timeout consumer. Pertahanan yang mungkin dapat mencakup pemrosesan asinkron, penggunaan queue, dan pembatasan proses paralel per pengguna dan per aplikasi. | 2 |
| **15.1.4** | Verifikasi bahwa dokumentasi aplikasi menyoroti pustaka pihak ketiga yang dianggap sebagai "risky component". | 3 |
| **15.1.5** | Verifikasi bahwa dokumentasi aplikasi menyoroti bagian-bagian aplikasi di mana "dangerous functionality" digunakan. | 3 |

## V15.2 Arsitektur Keamanan dan Dependensi

Bagian ini mencakup persyaratan untuk menangani dependensi dan komponen yang berisiko, usang, atau tidak aman melalui dependency management.

Bagian ini juga mencakup penggunaan teknik pada level arsitektur seperti sandboxing, encapsulation, containerization, dan network isolation untuk mengurangi dampak penggunaan "dangerous operations" atau "risky component" (sebagaimana didefinisikan pada bagian sebelumnya) serta mencegah hilangnya ketersediaan (availability) akibat penggunaan berlebihan terhadap fungsionalitas yang memerlukan resource besar.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **15.2.1** | Verifikasi bahwa aplikasi hanya mengandung komponen yang belum melanggar jangka waktu pembaruan dan remediasi yang terdokumentasi. | 1 |
| **15.2.2** | Verifikasi bahwa aplikasi telah menerapkan pertahanan terhadap hilangnya ketersediaan (availability) akibat fungsionalitas yang memakan waktu lama atau memerlukan resource besar, berdasarkan keputusan keamanan dan strategi terdokumentasi untuk hal ini. | 2 |
| **15.2.3** | Verifikasi bahwa environment produksi hanya mencakup fungsionalitas yang diperlukan agar aplikasi dapat berfungsi, dan tidak mengekspor fungsionalitas yang tidak diperlukan seperti kode test, contoh cuplikan kode (sample snippets), dan fungsionalitas development. | 2 |
| **15.2.4** | Verifikasi bahwa komponen pihak ketiga beserta seluruh dependensi transitifnya disertakan dari repository yang diharapkan, baik yang dimiliki secara internal maupun sumber eksternal, dan bahwa tidak ada risiko serangan dependency confusion. | 3 |
| **15.2.5** | Verifikasi bahwa aplikasi menerapkan perlindungan tambahan pada bagian-bagian aplikasi yang terdokumentasi mengandung "dangerous functionality" atau menggunakan pustaka pihak ketiga yang dianggap sebagai "risky component". Hal ini dapat mencakup teknik seperti sandboxing, encapsulation, containerization, atau network level isolation untuk menghambat dan mencegah penyerang yang telah mengompromikan satu bagian aplikasi agar tidak dapat berpindah (pivoting) ke bagian lain dalam aplikasi. | 3 |

## V15.3 Defensive Coding

Bagian ini membahas jenis-jenis kerentanan, termasuk type juggling, prototype pollution, dan lainnya, yang muncul akibat penggunaan pola coding yang tidak aman pada bahasa tertentu. Beberapa mungkin tidak relevan untuk semua bahasa, sementara yang lain memiliki perbaikan yang spesifik terhadap bahasa tertentu atau terkait dengan bagaimana suatu bahasa atau framework tertentu menangani sebuah fitur seperti HTTP parameter. Bagian ini juga mempertimbangkan risiko tidak melakukan validasi kriptografis terhadap pembaruan aplikasi.

Bagian ini juga mempertimbangkan risiko yang terkait dengan penggunaan objek untuk merepresentasikan item data serta menerima dan mengembalikan data tersebut melalui API eksternal. Dalam hal ini, aplikasi harus memastikan bahwa field data yang seharusnya tidak dapat ditulis (writable) tidak dimodifikasi oleh input pengguna (mass assignment) dan bahwa API tersebut selektif mengenai field data mana yang dikembalikan. Jika akses field bergantung pada permission pengguna, hal ini harus dipertimbangkan dalam konteks persyaratan field-level access control pada bab Authorization.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **15.3.1** | Verifikasi bahwa aplikasi hanya mengembalikan subset field yang diperlukan dari sebuah objek data. Misalnya, aplikasi tidak boleh mengembalikan seluruh objek data, karena beberapa field individual seharusnya tidak dapat diakses oleh pengguna. | 1 |
| **15.3.2** | Verifikasi bahwa ketika backend aplikasi melakukan pemanggilan ke URL eksternal, aplikasi tersebut dikonfigurasi untuk tidak mengikuti redirect kecuali hal tersebut memang merupakan fungsionalitas yang dimaksudkan. | 2 |
| **15.3.3** | Verifikasi bahwa aplikasi memiliki penanggulangan (countermeasures) untuk melindungi dari serangan mass assignment dengan membatasi field yang diizinkan per controller dan action, misalnya, tidak memungkinkan untuk menyisipkan atau memperbarui nilai sebuah field ketika hal tersebut tidak dimaksudkan menjadi bagian dari action tersebut. | 2 |
| **15.3.4** | Verifikasi bahwa semua komponen proxying dan middleware meneruskan alamat IP asli pengguna secara benar menggunakan field data tepercaya yang tidak dapat dimanipulasi oleh pengguna akhir, dan aplikasi serta web server menggunakan nilai yang benar ini untuk logging dan keputusan keamanan seperti rate limiting, dengan mempertimbangkan bahwa bahkan alamat IP asli mungkin tidak dapat diandalkan akibat IP dinamis, VPN, atau firewall perusahaan. | 2 |
| **15.3.5** | Verifikasi bahwa aplikasi secara eksplisit memastikan bahwa variabel memiliki tipe yang benar dan melakukan operasi strict equality dan comparator. Hal ini untuk menghindari kerentanan type juggling atau type confusion yang disebabkan oleh kode aplikasi yang membuat asumsi mengenai tipe sebuah variabel. | 2 |
| **15.3.6** | Verifikasi bahwa kode JavaScript ditulis dengan cara yang mencegah prototype pollution, misalnya, dengan menggunakan Set() atau Map() alih-alih object literal. | 2 |
| **15.3.7** | Verifikasi bahwa aplikasi memiliki pertahanan terhadap serangan HTTP parameter pollution, terutama jika application framework tidak membedakan sumber dari request parameter (query string, body parameters, cookies, atau header fields). | 2 |

## V15.4 Concurrency yang Aman

Masalah concurrency seperti race conditions, kerentanan time-of-check to time-of-use (TOCTOU), deadlock, livelock, thread starvation, dan sinkronisasi yang tidak tepat dapat mengakibatkan perilaku yang tidak dapat diprediksi dan risiko keamanan. Bagian ini mencakup berbagai teknik dan strategi untuk membantu memitigasi risiko-risiko tersebut.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **15.4.1** | Verifikasi bahwa objek bersama (shared objects) dalam kode multi-threaded (seperti cache, file, atau objek in-memory yang diakses oleh beberapa thread) diakses secara aman dengan menggunakan tipe yang thread-safe dan mekanisme sinkronisasi seperti locks atau semaphores guna menghindari race conditions dan kerusakan data. | 3 |
| **15.4.2** | Verifikasi bahwa pemeriksaan terhadap state sebuah resource, seperti keberadaannya atau permission-nya, dan tindakan yang bergantung padanya dilakukan sebagai satu operasi atomik guna mencegah race conditions time-of-check to time-of-use (TOCTOU). Misalnya, memeriksa apakah sebuah file ada sebelum membukanya, atau memverifikasi akses pengguna sebelum memberikannya. | 3 |
| **15.4.3** | Verifikasi bahwa locks digunakan secara konsisten guna menghindari thread yang terjebak (stuck), baik karena saling menunggu satu sama lain maupun melakukan retry tanpa henti, dan bahwa logika locking tetap berada dalam kode yang bertanggung jawab mengelola resource tersebut guna memastikan lock tidak dapat dimodifikasi secara tidak sengaja atau secara jahat oleh class atau kode eksternal. | 3 |
| **15.4.4** | Verifikasi bahwa kebijakan alokasi resource mencegah thread starvation dengan memastikan akses yang adil terhadap resource, seperti dengan memanfaatkan thread pool, yang memungkinkan thread dengan prioritas lebih rendah untuk tetap berjalan dalam jangka waktu yang wajar. | 3 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP Prototype Pollution Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [OWASP CycloneDX Bill of Materials Specification](https://owasp.org/www-project-cyclonedx/)
* [OWASP Web Security Testing Guide: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution)