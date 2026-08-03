# V16 Security Logging dan Error Handling

## Tujuan Kontrol

Security log berbeda dari log error atau performa dan digunakan untuk mencatat kejadian (events) yang relevan dengan keamanan, seperti keputusan otentikasi, keputusan kontrol akses, serta upaya untuk melompati (bypass) kontrol keamanan seperti validasi input atau validasi logika bisnis. Tujuannya adalah untuk mendukung deteksi, respons, dan investigasi dengan menyediakan data terstruktur yang ber-signal tinggi (high-signal) untuk alat analisis seperti SIEM.

Log tidak boleh mencakup data pribadi yang sensitif kecuali diwajibkan secara hukum, dan setiap data yang dicatat harus dilindungi sebagai aset bernilai tinggi. Logging tidak boleh mengompromikan privasi atau keamanan sistem. Aplikasi juga harus mengalami kegagalan secara aman (fail securely), menghindari pengungkapan informasi atau gangguan yang tidak perlu.

Untuk panduan implementasi terperinci, lihat OWASP Cheat Sheets di bagian referensi.

## V16.1 Dokumentasi Security Logging

Bagian ini memastikan inventarisasi logging yang jelas dan lengkap di seluruh stack aplikasi. Hal ini sangat penting untuk pemantauan keamanan yang efektif, respons insiden, dan kepatuhan (compliance).

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **16.1.1** | Verifikasi bahwa terdapat inventaris yang mendokumentasikan logging yang dilakukan pada setiap lapisan technology stack aplikasi, event apa saja yang dicatat, format log, lokasi penyimpanan log tersebut, bagaimana log digunakan, bagaimana akses ke log dikontrol, dan berapa lama log disimpan. | 2 |

## V16.2 General Logging

Bagian ini memberikan persyaratan untuk memastikan bahwa security log terstruktur secara konsisten dan berisi metadata yang diharapkan. Tujuannya adalah membuat log dapat dibaca oleh mesin (machine-readable) dan dapat dianalisis di seluruh sistem dan tools terdistribusi.

Secara alami, event keamanan sering kali melibatkan data sensitif. Jika data tersebut dicatat tanpa pertimbangan, log itu sendiri akan menjadi terklasifikasi dan oleh karena itu tunduk pada persyaratan enkripsi, kebijakan retensi yang lebih ketat, serta potensi pengungkapan selama audit.

Oleh karena itu, sangat penting untuk mencatat hanya apa yang diperlukan dan memperlakukan data log dengan tingkat kepedulian yang sama seperti aset sensitif lainnya.

Persyaratan di bawah ini menetapkan fondasi dasar untuk metadata logging, sinkronisasi, format, dan kontrol.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **16.2.1** | Verifikasi bahwa setiap entry log mencakup metadata yang diperlukan (seperti kapan, di mana, siapa, apa) yang memungkinkan investigasi mendalam terhadap garis waktu (timeline) saat terjadi suatu event. | 2 |
| **16.2.2** | Verifikasi bahwa sumber waktu untuk semua komponen logging tersinkronisasi, dan timestamp pada metadata event keamanan menggunakan UTC atau menyertakan offset zona waktu yang eksplisit. UTC direkomendasikan untuk memastikan konsistensi di seluruh sistem terdistribusi dan mencegah kebingungan selama transisi daylight saving time. | 2 |
| **16.2.3** | Verifikasi bahwa aplikasi hanya menyimpan atau menyiarkan (broadcast) log ke file dan layanan yang terdokumentasi dalam inventaris log. | 2 |
| **16.2.4** | Verifikasi bahwa log dapat dibaca dan dikorelasikan oleh pemroses log (log processor) yang digunakan, sebaiknya dengan menggunakan format logging umum. | 2 |
| **16.2.5** | Verifikasi bahwa saat mencatat data sensitif, aplikasi menerapkan logging berdasarkan tingkat perlindungan data tersebut. Sebagai contoh, data tertentu seperti kredensial atau rincian pembayaran mungkin tidak diizinkan untuk dicatat. Data lain seperti token sesi hanya boleh dicatat dengan di-hash atau di-masking, baik secara penuh maupun sebagian. | 2 |

## V16.3 Security Events

Bagian ini mendefinisikan persyaratan untuk mencatat event yang relevan dengan keamanan di dalam aplikasi. Menangkap event ini sangat penting untuk mendeteksi perilaku mencurigakan, mendukung investigasi, dan memenuhi kewajiban kepatuhan.

Bagian ini menguraikan jenis event yang harus dicatat tetapi tidak mencoba memberikan rincian yang meyeluruh. Setiap aplikasi memiliki faktor risiko dan konteks operasional yang unik.

Harap dicatat bahwa meskipun ASVS mencakup pencatatan event keamanan dalam cakupannya, pengalihan peringatan (*alerting*) dan korelasi (misalnya aturan SIEM atau infrastruktur pemantauan) dianggap di luar cakupan dan ditangani oleh sistem operasional dan pemantauan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **16.3.1** | Verifikasi bahwa semua operasi otentikasi dicatat, termasuk percobaan yang berhasil dan yang gagal. Metadata tambahan, seperti jenis otentikasi atau faktor yang digunakan, juga harus dikumpulkan. | 2 |
| **16.3.2** | Verifikasi bahwa percobaan otorisasi yang gagal dicatat. Untuk L3, ini harus mencakup pencatatan semua keputusan otorisasi, termasuk mencatat saat data sensitif diakses (tanpa mencatat data sensitif itu sendiri). | 2 |
| **16.3.3** | Verifikasi bahwa aplikasi mencatat event keamanan yang didefinisikan dalam dokumentasi dan juga mencatat upaya untuk melompati (*bypass*) kontrol keamanan, seperti validasi input, logika bisnis, dan anti-otomatisasi. | 2 |
| **16.3.4** | Verifikasi bahwa aplikasi mencatat error yang tidak terduga dan kegagalan kontrol keamanan seperti kegagalan backend TLS. | 2 |

## V16.4 Log Protection

Log adalah artefak forensik yang berharga dan harus dilindungi. Jika log dapat diubah atau dihapus dengan mudah, log tersebut kehilangan integritasnya dan menjadi tidak dapat diandalkan untuk investigasi insiden atau proses hukum. Log dapat mengekspos perilaku internal aplikasi atau metadata sensitif, menjadikannya target yang menarik bagi penyerang.

Bagian ini mendefinisikan persyaratan untuk memastikan bahwa log dilindungi dari akses yang tidak sah, manipulasi, dan pengungkapan, serta ditransmisikan dan disimpan secara aman di dalam sistem yang aman dan terisolasi.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **16.4.1** | Verifikasi bahwa semua komponen logging melakukan encode data dengan tepat untuk mencegah log injection. | 2 |
| **16.4.2** | Verifikasi bahwa log dilindungi dari akses yang tidak sah dan tidak dapat diubah. | 2 |
| **16.4.3** | Verifikasi bahwa log ditransmisikan secara aman ke sistem terpisah secara logis untuk analisis, deteksi, alerting, dan eskalasi. Tujuannya adalah untuk memastikan bahwa jika aplikasi dibobol, log tidak ikut terkompromikan. | 2 |

## V16.5 Error Handling

Bagian ini mendefinisikan persyaratan untuk memastikan bahwa aplikasi mengalami kegagalan secara baik (*graceful*) dan aman tanpa mengungkapkan rincian internal yang sensitif.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **16.5.1** | Verifikasi bahwa pesan generik dikembalikan ke pengguna/konsumen saat terjadi error yang tidak terduga atau sensitif terhadap keamanan, memastikan tidak ada paparan data sistem internal yang sensitif seperti stack trace, query, secret key, dan token. | 2 |
| **16.5.2** | Verifikasi bahwa aplikasi tetap beroperasi secara aman ketika akses sumber daya eksternal gagal, misalnya dengan menggunakan pola seperti circuit breaker atau pemulihan secara bertahap (*graceful degradation*). | 2 |
| **16.5.3** | Verifikasi bahwa aplikasi mengalami kegagalan secara *graceful* dan aman, termasuk saat terjadi pengecualian (*exception*), mencegah kondisi *fail-open* seperti memproses transaksi meskipun terjadi error akibat logika validasi. | 2 |
| **16.5.4** | Verifikasi bahwa error handler "last resort" (upaya terakhir) telah ditentukan untuk menangkap semua pengecualian (*unhandled exceptions*). Ini bertujuan untuk menghindari kehilangan rincian error yang harus masuk ke file log dan memastikan bahwa error tidak menjatuhkan seluruh proses aplikasi, yang mengakibatkan hilangnya ketersediaan (*availability*). | 3 |

Catatan: Bahasa tertentu, (termasuk Swift, Go, dan melalui praktik desain umum, banyak bahasa fungsional,) tidak mendukung *exceptions* atau *last-resort event handlers*. Dalam hal ini, arsitek dan pengembang harus menggunakan pola, bahasa, atau cara yang ramah *framework* untuk memastikan bahwa aplikasi dapat menangani event luar biasa, tidak terduga, atau terkait keamanan secara aman.

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP Web Security Testing Guide: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
* [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
* [OWASP Application Logging Vocabulary Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html)