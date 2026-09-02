# V4 API dan Web Service

## Tujuan Kontrol

Beberapa pertimbangan berlaku secara khusus untuk aplikasi yang mengekspos API untuk digunakan oleh web browser atau consumer lainnya (umumnya menggunakan JSON, XML, atau GraphQL). Bab ini membahas konfigurasi dan mekanisme keamanan relevan yang harus diterapkan.

Perlu dicatat bahwa hal-hal terkait authentication, session management, dan input validation dari bab lain juga berlaku untuk API, sehingga bab ini tidak dapat dipisahkan dari konteksnya atau diuji secara terpisah.

## V4.1 Keamanan Web Service Umum

Bagian ini membahas pertimbangan keamanan web service secara umum dan, oleh karena itu, praktik-praktik dasar kebersihan (hygiene) web service.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **4.1.1** | Verifikasi bahwa setiap HTTP response dengan message body memiliki Content-Type header field yang sesuai dengan konten sebenarnya dari response tersebut, termasuk parameter charset untuk menentukan character encoding yang aman (misalnya, UTF-8, ISO-8859-1) sesuai dengan IANA Media Types, seperti "text/", "/+xml" dan "/xml". | 1 |
| **4.1.2** | Verifikasi bahwa hanya endpoint yang menghadap pengguna (user-facing, dimaksudkan untuk akses manual melalui web browser) yang secara otomatis melakukan redirect dari HTTP ke HTTPS, sedangkan layanan atau endpoint lainnya tidak menerapkan transparent redirects. Hal ini untuk menghindari situasi di mana client secara keliru mengirimkan HTTP request yang tidak terenkripsi, namun karena request tersebut secara otomatis diarahkan ke HTTPS, kebocoran data sensitif menjadi tidak terdeteksi. | 2 |
| **4.1.3** | Verifikasi bahwa HTTP header field apa pun yang digunakan oleh aplikasi dan diatur oleh lapisan perantara (intermediary layer), seperti load balancer, web proxy, atau layanan backend-for-frontend, tidak dapat di-override oleh pengguna akhir. Contoh header dapat mencakup X-Real-IP, X-Forwarded-*, atau X-User-ID. | 2 |
| **4.1.4** | Verifikasi bahwa hanya metode HTTP yang secara eksplisit didukung oleh aplikasi atau API-nya (termasuk OPTIONS selama preflight requests) yang dapat digunakan dan metode yang tidak digunakan diblokir. | 3 |
| **4.1.5** | Verifikasi bahwa per-message digital signatures digunakan untuk memberikan jaminan tambahan di atas perlindungan transport untuk request atau transaksi yang sangat sensitif atau yang melintasi sejumlah sistem. | 3 |

## V4.2 Validasi Struktur Pesan HTTP

Bagian ini menjelaskan bagaimana struktur dan header fields dari sebuah pesan HTTP harus divalidasi untuk mencegah serangan seperti request smuggling, response splitting, header injection, dan denial of service melalui pesan HTTP yang terlalu panjang.

Persyaratan ini relevan untuk pemrosesan dan pembuatan pesan HTTP secara umum, namun menjadi sangat penting terutama saat mengonversi pesan HTTP antar versi HTTP yang berbeda.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **4.2.1** | Verifikasi bahwa semua komponen aplikasi (termasuk load balancer, firewall, dan application server) menentukan batasan pesan HTTP yang masuk menggunakan mekanisme yang sesuai untuk versi HTTP tersebut guna mencegah HTTP request smuggling. Pada HTTP/1.x, jika sebuah Transfer-Encoding header field ada, Content-Length header harus diabaikan sesuai RFC 2616. Saat menggunakan HTTP/2 atau HTTP/3, jika sebuah Content-Length header field ada, penerima harus memastikan bahwa nilai tersebut konsisten dengan panjang DATA frames. | 2 |
| **4.2.2** | Verifikasi bahwa saat membuat pesan HTTP, Content-Length header field tidak bertentangan dengan panjang konten sebagaimana ditentukan oleh framing protokol HTTP, guna mencegah serangan request smuggling. | 3 |
| **4.2.3** | Verifikasi bahwa aplikasi tidak mengirim maupun menerima pesan HTTP/2 atau HTTP/3 dengan connection-specific header fields seperti Transfer-Encoding guna mencegah serangan response splitting dan header injection. | 3 |
| **4.2.4** | Verifikasi bahwa aplikasi hanya menerima request HTTP/2 dan HTTP/3 yang header fields dan nilainya tidak mengandung urutan CR (\r), LF (\n), atau CRLF (\r\n), guna mencegah serangan header injection. | 3 |
| **4.2.5** | Verifikasi bahwa, jika aplikasi (backend atau frontend) membangun dan mengirim request, aplikasi tersebut menggunakan validation, sanitization, atau mekanisme lain untuk menghindari pembuatan URI (seperti untuk pemanggilan API) atau HTTP request header fields (seperti Authorization atau Cookie) yang terlalu panjang untuk diterima oleh komponen penerima. Hal ini dapat menyebabkan denial of service, seperti saat mengirimkan request yang terlalu panjang (misalnya, cookie header field yang panjang), yang mengakibatkan server selalu merespons dengan status error. | 3 |

## V4.3 GraphQL

GraphQL semakin umum digunakan sebagai cara untuk membuat client yang kaya data (data-rich) yang tidak terikat erat dengan berbagai layanan backend. Bagian ini membahas pertimbangan keamanan untuk GraphQL.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **4.3.1** | Verifikasi bahwa query allowlist, depth limiting, amount limiting, atau query cost analysis digunakan untuk mencegah GraphQL atau data layer expression Denial of Service (DoS) akibat query yang mahal (expensive) dan bersarang (nested). | 2 |
| **4.3.2** | Verifikasi bahwa GraphQL introspection queries dinonaktifkan pada environment produksi, kecuali jika GraphQL API tersebut memang dimaksudkan untuk digunakan oleh pihak lain. | 2 |

## V4.4 WebSocket

WebSocket adalah protokol komunikasi yang menyediakan saluran komunikasi dua arah secara simultan melalui satu koneksi TCP tunggal. Protokol ini distandarkan oleh IETF sebagai RFC 6455 pada tahun 2011 dan berbeda dari HTTP, meskipun dirancang untuk bekerja melalui port HTTP 443 dan 80.

Bagian ini menyediakan persyaratan keamanan utama untuk mencegah serangan yang terkait dengan keamanan komunikasi dan session management yang secara khusus mengeksploitasi saluran komunikasi real-time ini.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **4.4.1** | Verifikasi bahwa WebSocket over TLS (WSS) digunakan untuk semua koneksi WebSocket. | 1 |
| **4.4.2** | Verifikasi bahwa, selama initial HTTP WebSocket handshake, Origin header field diperiksa terhadap daftar origin yang diizinkan untuk aplikasi tersebut. | 2 |
| **4.4.3** | Verifikasi bahwa, jika session management standar aplikasi tidak dapat digunakan, token khusus (dedicated tokens) digunakan untuk hal ini, yang sesuai dengan persyaratan keamanan Session Management yang relevan. | 2 |
| **4.4.4** | Verifikasi bahwa token session management WebSocket khusus pada awalnya diperoleh atau divalidasi melalui sesi HTTPS yang telah terautentikasi sebelumnya, saat mengalihkan sesi HTTPS yang ada ke saluran WebSocket. | 2 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* Sumber daya mengenai GraphQL Authorization dari [graphql.org](https://graphql.org/learn/authorization/) dan [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods).
* [OWASP Web Security Testing Guide: GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [OWASP Web Security Testing Guide: Testing WebSockets](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)
