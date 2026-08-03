# Penilaian dan Sertifikasi

## Sikap OWASP Terhadap Sertifikasi ASVS dan Trust Mark

OWASP, sebagai organisasi nirlaba yang netral vendor, tidak menyertifikasi vendor, verifikator, atau perangkat lunak apa pun. Jaminan (*assurance*), *trust mark*, atau sertifikasi apa pun yang mengklaim kepatuhan ASVS tidak didukung secara resmi oleh OWASP, sehingga organisasi harus berhati-hati terhadap klaim pihak ketiga mengenai sertifikasi ASVS.

Organisasi dapat menawarkan layanan jaminan (*assurance services*), asalkan mereka tidak mengklaim sertifikasi resmi dari OWASP.

## Cara Memverifikasi Kepatuhan ASVS

ASVS sengaja dibuat tidak preskriptif mengenai cara tepat memverifikasi kepatuhan pada tingkat panduan pengujian. Namun, penting untuk menyoroti beberapa poin kunci.

### Pelaporan Verifikasi

Laporan *penetration testing* tradisional biasanya melaporkan masalah "berdasarkan pengecualian" (*by exception*), yang hanya mencantumkan kegagalan. Namun, laporan sertifikasi ASVS harus mencakup cakupan (*scope*), ringkasan dari semua persyaratan yang diperiksa, persyaratan di mana pengecualian dicatat, serta panduan tentang penyelesaian masalah. Beberapa persyaratan mungkin tidak berlaku (misalnya, manajemen sesi pada API *stateless*), dan hal ini harus dicatat dalam laporan.

### Cakupan Verifikasi

Organisasi yang mengembangkan aplikasi umumnya tidak akan mengimplementasikan semua persyaratan, karena beberapa mungkin tidak relevan atau kurang signifikan berdasarkan fungsionalitas aplikasi tersebut. Verifikator harus memperjelas cakupan verifikasi, termasuk Level mana yang ingin dicapai oleh organisasi dan persyaratan mana saja yang dilingkupi. Hal ini harus dilihat dari perspektif apa saja yang dimasukkan, alih-alih apa yang tidak dimasukkan. Mereka juga harus memberikan pandangan/pendapat mengenai alasan mengecualikan persyaratan yang belum diimplementasikan.

Hal ini memungkinkan konsumen laporan verifikasi untuk memahami konteks verifikasi dan membuat keputusan yang tepat mengenai tingkat kepercayaan yang dapat mereka berikan pada aplikasi tersebut.

Organisasi penilai dapat memilih metode pengujian mereka sendiri, tetapi harus mengungkapkannya dalam laporan dan metode ini idealnya dapat diulang (*repeatable*). Berbagai metode, seperti *manual penetration test* atau analisis *source code*, dapat digunakan untuk memverifikasi aspek-aspek seperti validasi input, tergantung pada aplikasi dan persyaratannya.

### Mekanisme Verifikasi

Terdapat sejumlah teknik berbeda yang mungkin diperlukan untuk memverifikasi persyaratan ASVS tertentu. Selain *penetration testing* (menggunakan kredensial yang valid untuk mendapatkan cakupan aplikasi secara penuh), memverifikasi persyaratan ASVS dapat memerlukan akses ke dokumentasi, *source code*, konfigurasi, dan orang-orang yang terlibat dalam proses pengembangan. Terutama untuk memverifikasi persyaratan Level 2 dan Level 3. Sudah menjadi praktik standar untuk menyediakan bukti temuan yang kuat dengan dokumentasi terperinci, yang dapat mencakup lembar kerja (*work papers*), tangkapan layar, skrip, dan *log* pengujian. Hanya menjalankan alat otomatis tanpa pengujian menyeluruh tidaklah cukup untuk sertifikasi, karena setiap persyaratan harus diuji secara terverifikasi.

Penggunaan otomatisasi untuk memverifikasi persyaratan ASVS adalah topik yang terus-menerus menarik perhatian. Oleh karena itu, penting untuk memperjelas beberapa poin terkait pengujian otomatis dan *black box*.

#### Peran Alat Pengujian Keamanan Otomatis (Automated Security Testing Tools)

Ketika alat pengujian keamanan otomatis seperti *Dynamic and Static Application Security Testing* (DAST dan SAST) diimplementasikan dengan benar dalam *build pipeline*, alat tersebut mungkin dapat mengidentifikasi beberapa masalah keamanan yang seharusnya tidak pernah ada. Namun, tanpa konfigurasi dan penyesuaian (*tuning*) yang cermat, alat-alat ini tidak akan memberikan cakupan yang diperlukan, dan tingkat *noise* akan mencegah masalah keamanan yang sebenarnya untuk diidentifikasi dan dimitigasi.

Meskipun hal ini dapat memberikan cakupan untuk beberapa persyaratan teknis yang lebih dasar dan lugas seperti yang berkaitan dengan *output encoding* atau sanitasi, sangat penting untuk dicatat bahwa alat-alat ini tidak akan mampu sepenuhnya memverifikasi banyak persyaratan ASVS yang lebih rumit atau yang berkaitan dengan logika bisnis dan kontrol akses.

Untuk persyaratan yang kurang sederhana, kemungkinan otomatisasi masih dapat dimanfaatkan, tetapi verifikasi khusus aplikasi perlu ditulis untuk mencapainya. Ini mungkin mirip dengan *unit test* dan *integration test* yang mungkin sudah digunakan oleh organisasi. Oleh karena itu, infrastruktur otomatisasi pengujian yang ada dapat digunakan untuk menulis pengujian khusus ASVS ini. Meskipun hal ini memerlukan investasi jangka pendek, manfaat jangka panjang dari kemampuan memverifikasi persyaratan ASVS ini secara terus-menerus akan sangat signifikan.

Singkatnya, dapat diuji menggunakan otomatisasi != menjalankan alat siap pakai (*off the shelf tool*).

#### Peran Penetration Testing

Meskipun L1 dalam versi 4.0 dioptimalkan untuk pengujian *black box* (tanpa dokumentasi dan tanpa *source code*), bahkan saat itu standar sudah menegaskan bahwa hal tersebut bukanlah aktivitas jaminan (*assurance*) yang efektif dan sangat tidak dianjurkan.

Pengujian tanpa akses ke informasi tambahan yang diperlukan adalah mekanisme yang tidak efisien dan tidak efektif untuk verifikasi keamanan, karena kehilangan kesempatan untuk meninjau *source code*, mengidentifikasi ancaman dan kontrol yang hilang, serta melakukan pengujian yang jauh lebih menyeluruh dalam jangka waktu yang lebih singkat.

Sangat disarankan untuk melakukan *penetration testing* berbasis dokumentasi atau *source code* (*hybrid*), yang memiliki akses penuh ke pengembang aplikasi dan dokumentasi aplikasi, daripada *penetration testing* tradisional. Hal ini tentu sangat diperlukan untuk memverifikasi banyak persyaratan ASVS.