# V3 Web Frontend Security

## Tujuan Kontrol

Kategori ini berfokus pada persyaratan yang dirancang untuk melindungi dari serangan yang dilakukan melalui web frontend. Persyaratan ini tidak berlaku untuk solusi machine-to-machine.

## V3.1 Dokumentasi Web Frontend Security

Bagian ini menjelaskan fitur keamanan browser yang harus ditentukan dalam dokumentasi aplikasi.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **3.1.1** | Verifikasi bahwa dokumentasi aplikasi menyatakan fitur keamanan yang diharapkan didukung oleh browser yang digunakan untuk mengakses aplikasi (seperti HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), dan mekanisme keamanan HTTP relevan lainnya). Dokumentasi tersebut juga harus mendefinisikan bagaimana aplikasi harus berperilaku jika beberapa fitur ini tidak tersedia (seperti memberi peringatan kepada pengguna atau memblokir akses). | 3 |

## V3.2 Interpretasi Konten yang Tidak Diinginkan

Me-render konten atau fungsionalitas dalam konteks yang salah dapat mengakibatkan konten berbahaya dieksekusi atau ditampilkan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **3.2.1** | Verifikasi bahwa kontrol keamanan diterapkan untuk mencegah browser me-render konten atau fungsionalitas dalam HTTP responses pada konteks yang salah (misalnya, ketika sebuah API, file yang diunggah pengguna, atau resource lain diminta secara langsung). Kontrol yang mungkin dapat mencakup: tidak menyajikan konten kecuali HTTP request header fields (seperti Sec-Fetch-\*) menunjukkan bahwa itu adalah konteks yang benar, menggunakan sandbox directive pada Content-Security-Policy header field, atau menggunakan attachment disposition type pada Content-Disposition header field. | 1 |
| **3.2.2** | Verifikasi bahwa konten yang dimaksudkan untuk ditampilkan sebagai teks, bukan di-render sebagai HTML, ditangani menggunakan fungsi rendering yang aman (seperti createTextNode atau textContent) untuk mencegah eksekusi konten yang tidak diinginkan seperti HTML atau JavaScript. | 1 |
| **3.2.3** | Verifikasi bahwa aplikasi menghindari DOM clobbering ketika menggunakan client-side JavaScript dengan menerapkan deklarasi variabel secara eksplisit, melakukan strict type checking, menghindari penyimpanan variabel global pada objek document, dan menerapkan namespace isolation. | 3 |

## V3.3 Konfigurasi Cookie

Bagian ini menjelaskan persyaratan untuk mengonfigurasi cookie yang sensitif secara aman guna memberikan tingkat jaminan yang lebih tinggi bahwa cookie tersebut dibuat oleh aplikasi itu sendiri, serta mencegah isinya bocor atau dimodifikasi secara tidak sah.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **3.3.1** | Verifikasi bahwa cookie memiliki atribut 'Secure' yang diatur, dan jika prefix '\__Host-' tidak digunakan untuk nama cookie, maka prefix '__Secure-' harus digunakan untuk nama cookie tersebut. | 1 |
| **3.3.2** | Verifikasi bahwa nilai atribut 'SameSite' pada setiap cookie diatur sesuai dengan tujuan cookie tersebut, untuk membatasi paparan terhadap user interface redress attacks dan browser-based request forgery attacks, yang umum dikenal sebagai cross-site request forgery (CSRF). | 2 |
| **3.3.3** | Verifikasi bahwa cookie memiliki prefix '__Host-' untuk nama cookie, kecuali jika cookie tersebut memang dirancang secara eksplisit untuk dibagikan dengan host lain. | 2 |
| **3.3.4** | Verifikasi bahwa jika nilai suatu cookie tidak dimaksudkan untuk dapat diakses oleh client-side scripts (seperti session token), cookie tersebut harus memiliki atribut 'HttpOnly' yang diatur dan nilai yang sama (misalnya session token) hanya boleh dikirimkan ke client melalui 'Set-Cookie' header field. | 2 |
| **3.3.5** | Verifikasi bahwa saat aplikasi menulis sebuah cookie, panjang gabungan nama dan nilai cookie tidak melebihi 4096 byte. Cookie yang terlalu besar tidak akan disimpan oleh browser dan karenanya tidak akan dikirimkan bersama request, sehingga mencegah pengguna menggunakan fungsionalitas aplikasi yang bergantung pada cookie tersebut. | 3 |

## V3.4 Header Mekanisme Keamanan Browser

Bagian ini menjelaskan header keamanan mana yang harus diatur pada HTTP responses untuk mengaktifkan fitur keamanan dan pembatasan browser saat menangani response dari aplikasi.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **3.4.1** | Verifikasi bahwa Strict-Transport-Security header field disertakan pada semua response untuk menegakkan kebijakan HTTP Strict Transport Security (HSTS). Sebuah maximum age minimal 1 tahun harus didefinisikan, dan untuk L2 ke atas, kebijakan tersebut juga harus berlaku untuk semua subdomain. | 1 |
| **3.4.2** | Verifikasi bahwa Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header field bernilai tetap (fixed value) yang ditentukan oleh aplikasi, atau jika nilai Origin HTTP request header field digunakan, nilai tersebut divalidasi terhadap allowlist origin tepercaya. Ketika 'Access-Control-Allow-Origin: *' perlu digunakan, verifikasi bahwa response tersebut tidak menyertakan informasi sensitif apa pun. | 1 |
| **3.4.3** | Verifikasi bahwa HTTP responses menyertakan Content-Security-Policy response header field yang mendefinisikan directives untuk memastikan browser hanya memuat dan menjalankan konten atau resource yang tepercaya, guna membatasi eksekusi JavaScript berbahaya. Minimal, sebuah kebijakan global harus digunakan yang mencakup directives object-src 'none' dan base-uri 'none' serta mendefinisikan allowlist atau menggunakan nonces atau hashes. Untuk aplikasi L3, sebuah kebijakan per-response dengan nonces atau hashes harus didefinisikan. | 2 |
| **3.4.4** | Verifikasi bahwa semua HTTP responses mengandung 'X-Content-Type-Options: nosniff' header field. Hal ini menginstruksikan browser untuk tidak menggunakan content sniffing dan MIME type guessing terhadap response tertentu, dan mewajibkan nilai Content-Type header field pada response tersebut sesuai dengan resource tujuan. Misalnya, response terhadap sebuah permintaan style hanya diterima jika Content-Type pada response tersebut adalah 'text/css'. Hal ini juga mengaktifkan penggunaan fungsionalitas Cross-Origin Read Blocking (CORB) oleh browser. | 2 |
| **3.4.5** | Verifikasi bahwa aplikasi mengatur sebuah referrer policy untuk mencegah kebocoran data teknis yang sensitif ke layanan pihak ketiga melalui 'Referer' HTTP request header field. Hal ini dapat dilakukan dengan menggunakan Referrer-Policy HTTP response header field atau melalui atribut elemen HTML. Data sensitif dapat mencakup data path dan query pada URL, dan untuk aplikasi internal non-publik juga termasuk hostname. | 2 |
| **3.4.6** | Verifikasi bahwa aplikasi web menggunakan frame-ancestors directive pada Content-Security-Policy header field untuk setiap HTTP response guna memastikan aplikasi tidak dapat di-embed secara default dan bahwa embedding resource tertentu hanya diizinkan jika diperlukan. Perlu dicatat bahwa X-Frame-Options header field, meskipun masih didukung oleh browser, sudah usang (obsolete) dan tidak boleh diandalkan. | 2 |
| **3.4.7** | Verifikasi bahwa Content-Security-Policy header field menentukan lokasi untuk melaporkan pelanggaran (violations). | 3 |
| **3.4.8** | Verifikasi bahwa semua HTTP responses yang memicu rendering dokumen (seperti response dengan Content-Type text/html), menyertakan Cross‑Origin‑Opener‑Policy header field dengan directive same-origin atau directive same-origin-allow-popups sesuai kebutuhan. Hal ini mencegah serangan yang menyalahgunakan shared access terhadap Window objects, seperti tabnabbing dan frame counting. | 3 |

## V3.5 Pemisahan Origin Browser

Saat menerima permintaan terhadap fungsionalitas sensitif pada sisi server, aplikasi perlu memastikan bahwa permintaan tersebut diinisiasi oleh aplikasi itu sendiri atau oleh pihak tepercaya dan bukan dipalsukan (forged) oleh penyerang.

Fungsionalitas sensitif dalam konteks ini dapat mencakup penerimaan form posts untuk pengguna yang telah maupun belum terautentikasi (seperti permintaan autentikasi), operasi yang mengubah state, atau fungsionalitas yang memerlukan resource besar (seperti data export).

Perlindungan utama di sini adalah kebijakan keamanan browser seperti Same Origin Policy untuk JavaScript dan juga logika SameSite untuk cookie. Perlindungan umum lainnya adalah mekanisme CORS preflight. Mekanisme ini sangat penting untuk endpoint yang dirancang untuk dipanggil dari origin yang berbeda, namun juga dapat menjadi mekanisme pencegahan request forgery yang berguna untuk endpoint yang tidak dirancang untuk dipanggil dari origin yang berbeda.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **3.5.1** | Verifikasi bahwa, jika aplikasi tidak mengandalkan mekanisme CORS preflight untuk mencegah cross-origin requests yang tidak diizinkan menggunakan fungsionalitas sensitif, request tersebut divalidasi untuk memastikan bahwa request tersebut berasal dari aplikasi itu sendiri. Hal ini dapat dilakukan dengan menggunakan dan memvalidasi anti-forgery tokens atau mewajibkan HTTP header fields tambahan yang bukan merupakan CORS-safelisted request-header fields. Hal ini bertujuan untuk melindungi dari browser-based request forgery attacks, yang umum dikenal sebagai cross-site request forgery (CSRF). | 1 |
| **3.5.2** | Verifikasi bahwa, jika aplikasi mengandalkan mekanisme CORS preflight untuk mencegah penggunaan cross-origin yang tidak diizinkan terhadap fungsionalitas sensitif, tidak mungkin untuk memanggil fungsionalitas tersebut dengan request yang tidak memicu CORS-preflight request. Hal ini mungkin memerlukan pemeriksaan nilai 'Origin' dan 'Content-Type' request header fields atau menggunakan header field tambahan yang bukan merupakan CORS-safelisted header-field. | 1 |
| **3.5.3** | Verifikasi bahwa HTTP requests terhadap fungsionalitas sensitif menggunakan metode HTTP yang sesuai seperti POST, PUT, PATCH, atau DELETE, dan bukan metode yang didefinisikan oleh spesifikasi HTTP sebagai "safe" seperti HEAD, OPTIONS, atau GET. Sebagai alternatif, validasi ketat terhadap Sec-Fetch-* request header fields dapat digunakan untuk memastikan bahwa request tidak berasal dari pemanggilan cross-origin yang tidak sesuai, navigation request, atau resource load (seperti image source) yang seharusnya tidak diharapkan. | 1 |
| **3.5.4** | Verifikasi bahwa aplikasi yang terpisah di-hosting pada hostname yang berbeda untuk memanfaatkan pembatasan yang disediakan oleh same-origin policy, termasuk bagaimana dokumen atau script yang dimuat oleh satu origin dapat berinteraksi dengan resource dari origin dan hostname lain serta pembatasan cookie berbasis hostname. | 2 |
| **3.5.5** | Verifikasi bahwa pesan yang diterima oleh interface postMessage dibuang (discarded) jika origin dari pesan tersebut tidak tepercaya, atau jika sintaks pesan tersebut tidak valid. | 2 |
| **3.5.6** | Verifikasi bahwa fungsionalitas JSONP tidak diaktifkan di bagian mana pun dalam aplikasi untuk menghindari serangan Cross-Site Script Inclusion (XSSI). | 3 |
| **3.5.7** | Verifikasi bahwa data yang memerlukan otorisasi tidak disertakan dalam response resource script, seperti file JavaScript, untuk mencegah serangan Cross-Site Script Inclusion (XSSI). | 3 |
| **3.5.8** | Verifikasi bahwa resource yang memerlukan autentikasi (seperti gambar, video, script, dan dokumen lainnya) hanya dapat dimuat atau di-embed atas nama pengguna ketika memang dimaksudkan demikian. Hal ini dapat dicapai dengan validasi ketat terhadap Sec-Fetch-* HTTP request header fields untuk memastikan bahwa request tidak berasal dari pemanggilan cross-origin yang tidak sesuai, atau dengan mengatur Cross-Origin-Resource-Policy HTTP response header field yang bersifat restriktif untuk menginstruksikan browser memblokir konten yang dikembalikan. | 3 |

## V3.6 Integritas Resource Eksternal

Bagian ini memberikan panduan untuk hosting konten yang aman pada situs pihak ketiga.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **3.6.1** | Verifikasi bahwa client-side assets, seperti pustaka JavaScript, CSS, atau web fonts, hanya di-hosting secara eksternal (misalnya, pada sebuah Content Delivery Network) jika resource tersebut bersifat statis dan memiliki versi (versioned) serta Subresource Integrity (SRI) digunakan untuk memvalidasi integritas asset tersebut. Jika hal ini tidak memungkinkan, harus ada keputusan keamanan yang terdokumentasi untuk menjustifikasi hal tersebut pada setiap resource. | 3 |

## V3.7 Pertimbangan Keamanan Browser Lainnya

Bagian ini mencakup berbagai kontrol keamanan lain dan fitur keamanan browser modern yang diperlukan untuk keamanan browser sisi client.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **3.7.1** | Verifikasi bahwa aplikasi hanya menggunakan teknologi client-side yang masih didukung dan dianggap aman. Contoh teknologi yang tidak memenuhi persyaratan ini antara lain NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, atau client-side Java applets. | 2 |
| **3.7.2** | Verifikasi bahwa aplikasi hanya akan secara otomatis mengarahkan (redirect) pengguna ke hostname atau domain yang berbeda (yang tidak dikendalikan oleh aplikasi) apabila tujuan tersebut terdapat pada sebuah allowlist. | 2 |
| **3.7.3** | Verifikasi bahwa aplikasi menampilkan notifikasi ketika pengguna diarahkan (redirect) ke URL di luar kendali aplikasi, dengan opsi untuk membatalkan navigasi tersebut. | 3 |
| **3.7.4** | Verifikasi bahwa top-level domain aplikasi (misalnya, site.tld) ditambahkan ke public preload list untuk HTTP Strict Transport Security (HSTS). Hal ini memastikan bahwa penggunaan TLS untuk aplikasi tertanam langsung pada browser-browser utama, alih-alih hanya mengandalkan Strict-Transport-Security response header field. | 3 |
| **3.7.5** | Verifikasi bahwa aplikasi berperilaku sesuai dengan yang didokumentasikan (seperti memberi peringatan kepada pengguna atau memblokir akses) jika browser yang digunakan untuk mengakses aplikasi tidak mendukung fitur keamanan yang diharapkan. | 3 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
* [OWASP DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)