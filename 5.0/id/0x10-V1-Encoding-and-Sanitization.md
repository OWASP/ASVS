# V1 Encoding dan Sanitization

## Tujuan Kontrol

Bab ini membahas kelemahan keamanan aplikasi web yang paling umum terkait dengan pemrosesan data tidak tepercaya (untrusted data) secara tidak aman. Kelemahan semacam ini dapat mengakibatkan berbagai kerentanan teknis, di mana data tidak tepercaya diinterpretasikan sesuai dengan aturan sintaks dari interpreter yang relevan.

Untuk aplikasi web modern, selalu lebih baik menggunakan API yang lebih aman, seperti parameterized queries, auto-escaping, atau templating frameworks. Jika tidak, output encoding, escaping, atau sanitization yang dilakukan dengan cermat menjadi krusial bagi keamanan aplikasi.

Input validation berfungsi sebagai mekanisme defense-in-depth untuk melindungi dari konten yang tidak terduga atau berbahaya. Namun, karena tujuan utamanya adalah memastikan bahwa konten yang masuk sesuai dengan ekspektasi fungsional dan bisnis, persyaratan terkait hal ini dapat ditemukan pada bab "Validation and Business Logic".

## V1.1 Arsitektur Encoding dan Sanitization

Pada bagian di bawah ini, disediakan persyaratan yang spesifik terhadap sintaks atau interpreter untuk memproses konten tidak aman secara aman guna menghindari kerentanan keamanan. Persyaratan dalam bagian ini mencakup urutan pemrosesan yang harus dilakukan dan di mana pemrosesan tersebut harus terjadi. Persyaratan ini juga bertujuan untuk memastikan bahwa setiap kali data disimpan, data tersebut tetap dalam bentuk aslinya dan tidak disimpan dalam bentuk yang sudah di-encode atau di-escape (misalnya, HTML encoding), untuk mencegah masalah double encoding.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **1.1.1** | Verifikasi bahwa input di-decode atau di-unescape ke dalam bentuk kanonik hanya satu kali, hanya di-decode ketika data yang di-encode dalam bentuk tersebut memang diharapkan, dan hal ini dilakukan sebelum pemrosesan input lebih lanjut, misalnya tidak dilakukan setelah input validation atau sanitization. | 2 |
| **1.1.2** | Verifikasi bahwa aplikasi melakukan output encoding dan escaping baik sebagai langkah terakhir sebelum digunakan oleh interpreter yang dituju, atau dilakukan oleh interpreter itu sendiri. | 2 |

## V1.2 Pencegahan Injection

Output encoding atau escaping, yang dilakukan dekat atau berdekatan dengan konteks yang berpotensi berbahaya, sangat krusial bagi keamanan aplikasi apa pun. Biasanya, output encoding dan escaping tidak disimpan (persisted), melainkan digunakan untuk membuat output aman untuk digunakan segera pada interpreter yang sesuai. Melakukan hal ini terlalu dini dapat mengakibatkan konten menjadi malformed atau membuat encoding maupun escaping menjadi tidak efektif.

Dalam banyak kasus, pustaka perangkat lunak menyertakan fungsi yang aman atau lebih aman yang melakukan hal ini secara otomatis, meskipun tetap perlu dipastikan bahwa fungsi tersebut sesuai untuk konteks yang digunakan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **1.2.1** | Verifikasi bahwa output encoding untuk HTTP response, dokumen HTML, atau dokumen XML relevan dengan konteks yang dibutuhkan, seperti melakukan encoding pada karakter yang relevan untuk elemen HTML, atribut HTML, komentar HTML, CSS, atau HTTP header fields, guna menghindari perubahan pada struktur pesan atau dokumen. | 1 |
| **1.2.2** | Verifikasi bahwa ketika membangun URL secara dinamis, data tidak tepercaya di-encode sesuai dengan konteksnya (misalnya, URL encoding atau base64url encoding untuk parameter query atau path). Pastikan hanya protokol URL yang aman yang diizinkan (misalnya, larang javascript: atau data:). | 1 |
| **1.2.3** | Verifikasi bahwa output encoding atau escaping digunakan saat membangun konten JavaScript secara dinamis (termasuk JSON), guna menghindari perubahan pada struktur pesan atau dokumen (untuk menghindari JavaScript dan JSON injection). | 1 |
| **1.2.4** | Verifikasi bahwa pemilihan data atau query database (misalnya, SQL, HQL, NoSQL, Cypher) menggunakan parameterized queries, ORM, entity frameworks, atau dilindungi dengan cara lain dari SQL Injection dan serangan database injection lainnya. Hal ini juga relevan saat menulis stored procedures. | 1 |
| **1.2.5** | Verifikasi bahwa aplikasi terlindungi dari OS command injection dan bahwa pemanggilan sistem operasi menggunakan parameterized OS queries atau menggunakan contextual command line output encoding. | 1 |
| **1.2.6** | Verifikasi bahwa aplikasi terlindungi dari kerentanan LDAP injection, atau bahwa kontrol keamanan khusus untuk mencegah LDAP injection telah diterapkan. | 2 |
| **1.2.7** | Verifikasi bahwa aplikasi terlindungi dari serangan XPath injection dengan menggunakan query parameterization atau precompiled queries. | 2 |
| **1.2.8** | Verifikasi bahwa LaTeX processors dikonfigurasi secara aman (seperti tidak menggunakan flag "--shell-escape") dan sebuah allowlist perintah digunakan untuk mencegah serangan LaTeX injection. | 2 |
| **1.2.9** | Verifikasi bahwa aplikasi melakukan escape terhadap karakter khusus dalam regular expressions (biasanya menggunakan backslash) untuk mencegah karakter tersebut disalahartikan sebagai metacharacters. | 2 |
| **1.2.10** | Verifikasi bahwa aplikasi terlindungi dari CSV and Formula Injection. Aplikasi harus mengikuti aturan escaping yang didefinisikan dalam RFC 4180 bagian 2.6 dan 2.7 saat mengekspor konten CSV. Selain itu, saat mengekspor ke CSV atau format spreadsheet lain (seperti XLS, XLSX, atau ODF), karakter khusus (termasuk '=', '+', '-', '@', '\t' (tab), dan '\0' (null character)) harus di-escape dengan tanda kutip tunggal jika muncul sebagai karakter pertama dalam nilai suatu field. | 3 |

Catatan: Menggunakan parameterized queries atau melakukan escaping SQL tidak selalu cukup. Bagian query seperti nama tabel dan nama kolom (termasuk nama kolom pada "ORDER BY") tidak dapat di-escape. Menyertakan data yang berasal dari pengguna dan sudah di-escape pada bagian-bagian ini dapat mengakibatkan query gagal atau terjadinya SQL injection.

## V1.3 Sanitization

Perlindungan ideal terhadap penggunaan konten tidak tepercaya dalam konteks yang tidak aman adalah dengan menggunakan context-specific encoding atau escaping, yang mempertahankan makna semantik yang sama dari konten tidak aman tersebut namun membuatnya aman untuk digunakan pada konteks tertentu, sebagaimana dibahas lebih rinci pada bagian sebelumnya.

Jika hal ini tidak memungkinkan, sanitization menjadi diperlukan, yaitu dengan menghapus karakter atau konten yang berpotensi berbahaya. Dalam beberapa kasus, hal ini dapat mengubah makna semantik dari input, namun demi alasan keamanan, mungkin tidak ada alternatif lain.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **1.3.1** | Verifikasi bahwa semua input HTML tidak tepercaya dari WYSIWYG editor atau sejenisnya di-sanitize menggunakan pustaka atau fitur framework HTML sanitization yang terkenal dan aman. | 1 |
| **1.3.2** | Verifikasi bahwa aplikasi menghindari penggunaan eval() atau fitur dynamic code execution lainnya seperti Spring Expression Language (SpEL). Jika tidak ada alternatif lain, input pengguna yang disertakan harus di-sanitize sebelum dieksekusi. | 1 |
| **1.3.3** | Verifikasi bahwa data yang diteruskan ke konteks yang berpotensi berbahaya di-sanitize terlebih dahulu untuk menerapkan langkah-langkah keamanan, seperti hanya mengizinkan karakter yang aman untuk konteks tersebut dan memotong (trimming) input yang terlalu panjang. | 2 |
| **1.3.4** | Verifikasi bahwa konten Scalable Vector Graphics (SVG) scriptable yang disediakan pengguna divalidasi atau di-sanitize agar hanya berisi tag dan atribut (seperti untuk menggambar grafik) yang aman bagi aplikasi, misalnya, tidak mengandung script dan foreignObject. | 2 |
| **1.3.5** | Verifikasi bahwa aplikasi melakukan sanitize atau menonaktifkan konten scriptable atau expression template language yang disediakan pengguna, seperti Markdown, CSS atau XSL stylesheets, BBCode, atau sejenisnya. | 2 |
| **1.3.6** | Verifikasi bahwa aplikasi terlindungi dari serangan Server-side Request Forgery (SSRF), dengan memvalidasi data tidak tepercaya terhadap allowlist protokol, domain, path, dan port, serta melakukan sanitize terhadap karakter yang berpotensi berbahaya sebelum menggunakan data tersebut untuk memanggil layanan lain. | 2 |
| **1.3.7** | Verifikasi bahwa aplikasi terlindungi dari serangan template injection dengan tidak mengizinkan template dibangun berdasarkan input tidak tepercaya. Jika tidak ada alternatif lain, input tidak tepercaya yang disertakan secara dinamis selama pembuatan template harus di-sanitize atau divalidasi secara ketat. | 2 |
| **1.3.8** | Verifikasi bahwa aplikasi melakukan sanitize secara tepat terhadap input tidak tepercaya sebelum digunakan dalam query Java Naming and Directory Interface (JNDI) dan bahwa JNDI dikonfigurasi secara aman untuk mencegah serangan JNDI injection. | 2 |
| **1.3.9** | Verifikasi bahwa aplikasi melakukan sanitize terhadap konten sebelum dikirim ke memcache untuk mencegah serangan injection. | 2 |
| **1.3.10** | Verifikasi bahwa format strings yang berpotensi diinterpretasikan dengan cara yang tidak terduga atau berbahaya saat digunakan telah di-sanitize sebelum diproses. | 2 |
| **1.3.11** | Verifikasi bahwa aplikasi melakukan sanitize terhadap input pengguna sebelum diteruskan ke sistem mail untuk melindungi dari SMTP atau IMAP injection. | 2 |
| **1.3.12** | Verifikasi bahwa regular expressions bebas dari elemen yang menyebabkan exponential backtracking, dan pastikan input tidak tepercaya di-sanitize untuk memitigasi serangan ReDoS atau Runaway Regex. | 3 |

## V1.4 Memory, String, dan Unmanaged Code

Persyaratan berikut membahas risiko yang terkait dengan penggunaan memory yang tidak aman, yang umumnya berlaku ketika aplikasi menggunakan bahasa sistem (systems language) atau unmanaged code.

Dalam beberapa kasus, hal ini dapat dicapai dengan mengatur compiler flags yang mengaktifkan perlindungan dan peringatan terhadap buffer overflow, termasuk stack randomization dan data execution prevention, serta menghentikan proses build jika ditemukan operasi pointer, memory, format string, integer, atau string yang tidak aman.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **1.4.1** | Verifikasi bahwa aplikasi menggunakan string yang memory-safe, memory copy, dan pointer arithmetic yang lebih aman untuk mendeteksi atau mencegah stack, buffer, atau heap overflow. | 2 |
| **1.4.2** | Verifikasi bahwa teknik validasi sign, range, dan input digunakan untuk mencegah integer overflow. | 2 |
| **1.4.3** | Verifikasi bahwa memory dan resource yang dialokasikan secara dinamis dibebaskan (released), dan bahwa referensi atau pointer ke memory yang telah dibebaskan dihapus atau diatur ke null untuk mencegah dangling pointers dan kerentanan use-after-free. | 2 |

## V1.5 Safe Deserialization

Konversi data dari representasi yang disimpan atau ditransmisikan menjadi objek aplikasi yang sesungguhnya (deserialization) secara historis telah menjadi penyebab berbagai kerentanan code injection. Penting untuk melakukan proses ini dengan hati-hati dan aman guna menghindari jenis masalah tersebut.

Secara khusus, metode deserialization tertentu telah diidentifikasi oleh dokumentasi bahasa pemrograman atau framework sebagai tidak aman dan tidak dapat dibuat aman jika digunakan dengan data tidak tepercaya. Untuk setiap mekanisme yang digunakan, uji tuntas (due diligence) yang cermat harus dilakukan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **1.5.1** | Verifikasi bahwa aplikasi mengonfigurasi XML parser untuk menggunakan konfigurasi yang restriktif dan bahwa fitur tidak aman seperti resolving external entities dinonaktifkan untuk mencegah serangan XML eXternal Entity (XXE). | 1 |
| **1.5.2** | Verifikasi bahwa deserialization terhadap data tidak tepercaya menerapkan penanganan input yang aman, seperti menggunakan allowlist tipe objek atau membatasi tipe objek yang didefinisikan oleh client, untuk mencegah serangan deserialization. Mekanisme deserialization yang secara eksplisit didefinisikan sebagai tidak aman tidak boleh digunakan dengan input tidak tepercaya. | 2 |
| **1.5.3** | Verifikasi bahwa parser yang berbeda-beda digunakan dalam aplikasi untuk tipe data yang sama (misalnya, JSON parser, XML parser, URL parser), melakukan parsing dengan cara yang konsisten dan menggunakan mekanisme character encoding yang sama untuk menghindari masalah seperti kerentanan JSON Interoperability atau perbedaan perilaku URI atau file parsing yang dapat dieksploitasi dalam serangan Remote File Inclusion (RFI) atau Server-side Request Forgery (SSRF). | 3 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
* [OWASP Web Security Testing Guide: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [RFC4180 - Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180#section-2)

Untuk informasi lebih lanjut, khususnya mengenai masalah deserialization atau parsing, silakan lihat:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai - A New Era of SSRF Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)