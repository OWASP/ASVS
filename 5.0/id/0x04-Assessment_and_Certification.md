# Penilaian dan Sertifikasi

## Sikap OWASP Terkait Sertifikasi dan Tanda Kepercayaan ASVS

OWASP, sebagai organisasi nirlaba yang netral terhadap vendor, tidak memberikan sertifikasi kepada vendor, pihak verifikator, atau perangkat lunak mana pun. Setiap jaminan, tanda kepercayaan, atau sertifikasi yang mengklaim kepatuhan terhadap ASVS tidak secara resmi didukung oleh OWASP; oleh karena itu, organisasi disarankan untuk berhati-hati terhadap klaim pihak ketiga mengenai sertifikasi ASVS.

Organisasi dapat menawarkan layanan jaminan, asalkan mereka tidak mengklaim memiliki sertifikasi resmi OWASP.

## Cara Memverifikasi Kepatuhan ASVS

ASVS sengaja tidak memberikan petunjuk pasti tentang bagaimana memverifikasi kepatuhan pada tingkat panduan pengujian. Namun, penting untuk menyoroti beberapa poin kunci.

### Laporan Verifikasi

Laporan pengujian penetrasi konvensional biasanya melaporkan masalah "berdasarkan pengecualian", dengan hanya mencantumkan kegagalan. Namun, laporan sertifikasi ASVS harus mencakup ruang lingkup, ringkasan seluruh persyaratan yang telah diperiksa, persyaratan di mana pengecualian ditemukan, serta panduan untuk mengatasi masalah tersebut. Beberapa persyaratan mungkin tidak berlaku (misalnya, manajemen sesi pada API stateless), dan hal ini harus dicantumkan dalam laporan.

### Ruang Lingkup Verifikasi

Sebuah organisasi yang mengembangkan aplikasi umumnya tidak akan menerapkan semua persyaratan, karena beberapa di antaranya mungkin tidak relevan atau kurang signifikan berdasarkan fungsionalitas aplikasi tersebut. Pihak verifikator harus menjelaskan ruang lingkup verifikasi secara jelas, termasuk Tingkat mana yang ingin dicapai oleh organisasi tersebut dan persyaratan mana saja yang dimasukkan. Penjelasan ini harus didasarkan pada apa yang dimasukkan, bukan apa yang tidak dimasukkan. Mereka juga harus memberikan pendapat mengenai alasan pengecualian terhadap persyaratan yang belum diterapkan.

Hal ini diharapkan dapat membantu pembaca laporan verifikasi memahami konteks verifikasi tersebut dan mengambil keputusan yang tepat mengenai tingkat kepercayaan yang dapat mereka berikan terhadap aplikasi tersebut.

Lembaga sertifikasi dapat memilih metode pengujian yang akan digunakan, namun harus mencantumkannya dalam laporan, dan metode tersebut sebaiknya dapat diulang. Berbagai metode, seperti pengujian penetrasi manual atau analisis kode sumber, dapat digunakan untuk memverifikasi aspek-aspek seperti validasi input, tergantung pada aplikasi dan persyaratannya.

### Mekanisme Verifikasi

Terdapat sejumlah teknik berbeda yang mungkin diperlukan untuk memverifikasi persyaratan ASVS tertentu. Selain pengujian penetrasi (menggunakan kredensial yang sah untuk menjangkau seluruh aplikasi), verifikasi persyaratan ASVS mungkin memerlukan akses ke dokumentasi, kode sumber, konfigurasi, serta pihak-pihak yang terlibat dalam proses pengembangan. Terutama untuk memverifikasi persyaratan L2 dan L3. Merupakan praktik standar untuk menyediakan bukti temuan yang kuat dengan dokumentasi terperinci, yang dapat mencakup dokumen kerja, tangkapan layar, skrip, dan log pengujian. Hanya menjalankan alat otomatis tanpa pengujian menyeluruh tidak cukup untuk sertifikasi, karena setiap persyaratan harus diuji secara terverifikasi.

Penggunaan otomatisasi untuk memverifikasi persyaratan ASVS merupakan topik yang selalu menarik perhatian. Oleh karena itu, penting untuk menjelaskan beberapa hal terkait pengujian otomatis dan pengujian kotak hitam.

#### Peran Alat Pengujian Keamanan Otomatis

Ketika alat pengujian keamanan otomatis seperti Dynamic Application Security Testing (DAST) dan Static Application Security Testing (SAST) diterapkan dengan benar dalam alur kerja pengembangan, alat-alat tersebut berpotensi mengidentifikasi beberapa masalah keamanan yang seharusnya tidak pernah terjadi. Namun, tanpa konfigurasi dan penyempurnaan yang cermat, alat-alat tersebut tidak akan memberikan cakupan yang diperlukan, dan tingginya tingkat "noise" akan menghalangi identifikasi serta penanganan masalah keamanan yang sesungguhnya.

Meskipun hal ini mungkin dapat memenuhi beberapa persyaratan teknis yang lebih mendasar dan sederhana, seperti yang berkaitan dengan pengkodean keluaran atau sanitasi, penting untuk dicatat bahwa alat-alat ini tidak akan mampu sepenuhnya memverifikasi banyak persyaratan ASVS yang lebih rumit atau yang berkaitan dengan logika bisnis dan kontrol akses.

Untuk persyaratan yang tidak terlalu sederhana, otomatisasi kemungkinan besar masih dapat diterapkan, namun untuk mewujudkannya, perlu ditulis verifikasi khusus aplikasi (ASVS). Verifikasi ini mungkin mirip dengan uji unit dan uji integrasi yang mungkin sudah digunakan oleh organisasi. Oleh karena itu, infrastruktur otomatisasi pengujian yang sudah ada ini mungkin dapat dimanfaatkan untuk menulis uji ASVS tersebut. Meskipun hal ini memerlukan investasi jangka pendek, manfaat jangka panjangnya—yaitu kemampuan untuk terus memverifikasi persyaratan ASVS ini—akan sangat signifikan.

Singkatnya, dapat diuji secara otomatis ≠ menggunakan alat siap pakai.

#### Peran Uji Penetrasi

Meskipun L1 pada versi 4.0 telah dioptimalkan untuk pelaksanaan pengujian "black box" (tanpa dokumentasi dan tanpa kode sumber), standar tersebut tetap menegaskan bahwa hal itu bukanlah kegiatan jaminan kualitas yang efektif dan harus secara aktif dihindari.

Pengujian tanpa akses ke informasi tambahan yang diperlukan merupakan mekanisme verifikasi keamanan yang tidak efisien dan tidak efektif, karena hal ini mengabaikan peluang untuk meninjau sumber kode, mengidentifikasi ancaman dan kontrol yang terlewatkan, serta melakukan pengujian yang jauh lebih menyeluruh dalam waktu yang lebih singkat.

Sangat disarankan untuk melakukan pengujian penetrasi berbasis dokumentasi atau kode sumber (hibrida), yang memiliki akses penuh kepada pengembang aplikasi dan dokumentasi aplikasi, daripada pengujian penetrasi tradisional. Hal ini tentu saja diperlukan untuk memverifikasi banyak persyaratan ASVS.
