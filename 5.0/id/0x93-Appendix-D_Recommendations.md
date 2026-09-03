# Lampiran D: Rekomendasi

## Pendahuluan

Saat mempersiapkan versi 5.0 dari Standar Verifikasi Keamanan Aplikasi (ASVS), menjadi jelas bahwa ada sejumlah item yang sudah ada dan yang baru diusulkan yang seharusnya tidak dimasukkan sebagai persyaratan dalam versi 5.0. Hal ini mungkin karena item-item tersebut tidak termasuk dalam ruang lingkup ASVS sesuai dengan definisi untuk versi 5.0, atau alternatifnya, dirasa bahwa meskipun merupakan ide yang bagus, item-item tersebut tidak dapat dijadikan wajib.

Karena tidak ingin kehilangan semua item ini sepenuhnya, beberapa di antaranya telah disertakan dalam lampiran ini.

## Mekanisme yang direkomendasikan dan termasuk dalam cakupan

Berikut ini adalah hal-hal yang termasuk dalam ruang lingkup ASVS. Hal-hal ini tidak boleh diwajibkan, tetapi sangat disarankan untuk mempertimbangkannya sebagai bagian dari aplikasi yang aman.

* Sebaiknya disediakan alat pengukur kekuatan kata sandi untuk membantu pengguna membuat kata sandi yang lebih kuat.
* Buat file security.txt yang dapat diakses publik di direktori root atau .well-known dari aplikasi yang secara jelas mendefinisikan tautan atau alamat email bagi orang-orang untuk menghubungi pemilik tentang masalah keamanan.
* Validasi input sisi klien harus diterapkan sebagai tambahan validasi pada lapisan layanan tepercaya karena ini memberikan peluang bagus untuk menemukan kapan seseorang telah melewati kontrol sisi klien dalam upaya menyerang aplikasi.
* Cegah halaman yang tidak sengaja dapat diakses dan berisi informasi sensitif agar tidak muncul di mesin pencari dengan menggunakan file robots.txt, header respons X-Robots-Tag, atau tag meta robots.html.
* Saat menggunakan GraphQL, terapkan logika otorisasi pada lapisan logika bisnis, bukan pada lapisan GraphQL atau resolver, untuk menghindari keharusan menangani otorisasi pada setiap antarmuka secara terpisah.

Referensi:

* [Informasi selengkapnya tentang security.txt termasuk tautan ke RFC](https://securitytxt.org/)

## Prinsip-prinsip Keamanan Perangkat Lunak

Berikut ini adalah beberapa poin yang sebelumnya ada di ASVS tetapi sebenarnya bukan persyaratan. Lebih tepatnya, ini adalah prinsip-prinsip yang perlu dipertimbangkan saat menerapkan kontrol keamanan yang, jika diikuti, akan menghasilkan kontrol yang lebih kuat. Prinsip-prinsip tersebut meliputi:

* Kontrol keamanan harus terpusat, sederhana (efisiensi desain), terbukti aman, dan dapat digunakan kembali. Hal ini harus menghindari kontrol yang duplikat, hilang, atau tidak efektif.
* Sebisa mungkin, gunakan implementasi kontrol keamanan yang telah ditulis dan diuji dengan baik sebelumnya, daripada mengandalkan implementasi kontrol dari awal.
* Idealnya, mekanisme kontrol akses tunggal harus digunakan untuk mengakses data dan sumber daya yang dilindungi. Semua permintaan harus melewati mekanisme tunggal ini untuk menghindari penyalinan dan penempelan atau jalur alternatif yang tidak aman.
* Kontrol akses berbasis atribut atau fitur adalah pola yang direkomendasikan di mana kode memeriksa otorisasi pengguna untuk suatu fitur atau item data, bukan hanya peran mereka. Izin tetap harus dialokasikan menggunakan peran.

## Proses Keamanan Perangkat Lunak

Terdapat sejumlah proses keamanan yang dihapus dari ASVS 5.0 tetapi masih merupakan ide yang bagus. Proyek OWASP SAMM dapat menjadi sumber yang baik untuk mengetahui cara mengimplementasikan proses-proses ini secara efektif. Item-item yang sebelumnya ada di ASVS meliputi:

* Verifikasi penggunaan siklus pengembangan perangkat lunak yang aman yang menangani keamanan di semua tahapan pengembangan.
* Verifikasi penggunaan pemodelan ancaman untuk setiap perubahan desain atau perencanaan sprint guna mengidentifikasi ancaman, merencanakan tindakan penanggulangan, memfasilitasi respons risiko yang tepat, dan memandu pengujian keamanan.
* Pastikan bahwa semua user story dan fitur mengandung batasan keamanan fungsional, seperti "Sebagai pengguna, saya harus dapat melihat dan mengedit profil saya. Saya tidak boleh dapat melihat atau mengedit profil orang lain."
* Pastikan ketersediaan daftar periksa pengkodean yang aman, persyaratan keamanan, pedoman, atau kebijakan bagi semua pengembang dan penguji.
* Verifikasi bahwa terdapat proses berkelanjutan untuk memastikan bahwa kode sumber aplikasi bebas dari pintu belakang (backdoor), kode berbahaya (misalnya, serangan salami, bom logika, bom waktu), dan fitur yang tidak terdokumentasi atau tersembunyi (misalnya, Easter egg, alat debugging yang tidak aman). Mematuhi bagian ini tidak mungkin dilakukan tanpa akses penuh ke kode sumber, termasuk pustaka pihak ketiga, dan oleh karena itu mungkin hanya cocok untuk aplikasi yang membutuhkan tingkat keamanan tertinggi.
* Pastikan mekanisme telah tersedia untuk mendeteksi dan menanggapi penyimpangan konfigurasi di lingkungan yang telah diimplementasikan. Hal ini dapat mencakup penggunaan infrastruktur yang tidak dapat diubah, penerapan ulang otomatis dari basis data yang aman, atau alat deteksi penyimpangan yang membandingkan kondisi saat ini dengan konfigurasi yang telah disetujui.
* Pastikan bahwa pengerasan konfigurasi dilakukan pada semua produk, pustaka, kerangka kerja, dan layanan pihak ketiga sesuai dengan rekomendasi masing-masing.

Referensi:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/securityengineering/sdl/)
