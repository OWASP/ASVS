# V5 File Handling

## Tujuan Kontrol

Penggunaan file dapat menghadirkan berbagai risiko bagi aplikasi, termasuk denial of service, akses tidak sah, dan habisnya kapasitas penyimpanan (storage exhaustion). Bab ini mencakup persyaratan untuk mengatasi risiko-risiko tersebut.

## V5.1 Dokumentasi Penanganan File

Bagian ini mencakup persyaratan untuk mendokumentasikan karakteristik file yang diharapkan diterima oleh aplikasi, sebagai prasyarat yang diperlukan untuk mengembangkan dan memverifikasi pemeriksaan keamanan yang relevan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **5.1.1** | Verifikasi bahwa dokumentasi mendefinisikan jenis file yang diizinkan, ekstensi file yang diharapkan, dan ukuran maksimum (termasuk ukuran setelah unpacked) untuk setiap fitur upload. Selain itu, pastikan dokumentasi tersebut menentukan bagaimana file dibuat aman bagi pengguna akhir untuk diunduh dan diproses, seperti bagaimana perilaku aplikasi ketika sebuah file berbahaya terdeteksi. | 2 |

## V5.2 Upload File dan Konten

Fungsionalitas upload file merupakan sumber utama file yang tidak tepercaya. Bagian ini menjelaskan persyaratan untuk memastikan bahwa keberadaan, volume, atau konten dari file-file tersebut tidak dapat membahayakan aplikasi.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **5.2.1** | Verifikasi bahwa aplikasi hanya akan menerima file dengan ukuran yang dapat diproses tanpa menyebabkan penurunan performa atau serangan denial of service. | 1 |
| **5.2.2** | Verifikasi bahwa saat aplikasi menerima sebuah file, baik secara mandiri maupun di dalam sebuah archive seperti file zip, aplikasi memeriksa apakah ekstensi file sesuai dengan ekstensi file yang diharapkan dan memvalidasi bahwa isi file tersebut sesuai dengan tipe yang direpresentasikan oleh ekstensi tersebut. Hal ini mencakup, namun tidak terbatas pada, pemeriksaan 'magic bytes' awal, melakukan image re-writing, dan menggunakan pustaka khusus untuk validasi konten file. Untuk L1, hal ini dapat difokuskan hanya pada file yang digunakan untuk membuat keputusan bisnis atau keamanan tertentu. Untuk L2 ke atas, hal ini harus berlaku untuk semua file yang diterima. | 1 |
| **5.2.3** | Verifikasi bahwa aplikasi memeriksa file terkompresi (misalnya, zip, gz, docx, odt) terhadap ukuran maksimum yang diizinkan setelah dekompresi (uncompressed) dan terhadap jumlah maksimum file sebelum melakukan dekompresi file tersebut. | 2 |
| **5.2.4** | Verifikasi bahwa kuota ukuran file dan jumlah maksimum file per pengguna diterapkan untuk memastikan bahwa satu pengguna tidak dapat memenuhi storage dengan terlalu banyak file, atau file yang berukuran sangat besar. | 3 |
| **5.2.5** | Verifikasi bahwa aplikasi tidak mengizinkan pengunggahan file terkompresi yang berisi symlink kecuali hal ini memang secara khusus diperlukan (dalam hal ini perlu diterapkan allowlist untuk file-file yang dapat di-symlink). | 3 |
| **5.2.6** | Verifikasi bahwa aplikasi menolak gambar yang diunggah dengan ukuran pixel lebih besar dari maksimum yang diizinkan, untuk mencegah serangan pixel flood. | 3 |

## V5.3 Penyimpanan File

Bagian ini mencakup persyaratan untuk mencegah file dieksekusi secara tidak sah setelah diunggah, untuk mendeteksi konten berbahaya, dan untuk menghindari data tidak tepercaya digunakan untuk mengontrol di mana file disimpan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **5.3.1** | Verifikasi bahwa file yang diunggah atau dihasilkan dari input tidak tepercaya dan disimpan pada folder publik, tidak dieksekusi sebagai kode program server-side ketika diakses secara langsung melalui HTTP request. | 1 |
| **5.3.2** | Verifikasi bahwa saat aplikasi membuat file paths untuk operasi file, aplikasi menggunakan data yang dihasilkan secara internal atau data tepercaya, bukan nama file yang dikirimkan oleh pengguna; atau jika nama file atau metadata file yang dikirimkan pengguna harus digunakan, validasi dan sanitization yang ketat harus diterapkan. Hal ini bertujuan untuk melindungi dari serangan path traversal, local atau remote file inclusion (LFI, RFI), dan server-side request forgery (SSRF). | 1 |
| **5.3.3** | Verifikasi bahwa pemrosesan file di sisi server, seperti dekompresi file, mengabaikan informasi path yang disediakan oleh pengguna untuk mencegah kerentanan seperti zip slip. | 3 |

## V5.4 Download File

Bagian ini berisi persyaratan untuk memitigasi risiko saat menyajikan file untuk diunduh, termasuk serangan path traversal dan injection. Hal ini juga mencakup memastikan bahwa file tersebut tidak mengandung konten berbahaya.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **5.4.1** | Verifikasi bahwa aplikasi memvalidasi atau mengabaikan nama file yang dikirimkan oleh pengguna, termasuk pada JSON, JSONP, atau parameter URL, dan menentukan sebuah nama file pada Content-Disposition header field dalam response. | 2 |
| **5.4.2** | Verifikasi bahwa nama file yang disajikan (misalnya, pada HTTP response header fields atau lampiran email) di-encode atau di-sanitize (misalnya, mengikuti RFC 6266) untuk menjaga struktur dokumen dan mencegah serangan injection. | 2 |
| **5.4.3** | Verifikasi bahwa file yang diperoleh dari sumber tidak tepercaya dipindai oleh antivirus scanner untuk mencegah penyajian konten berbahaya yang telah dikenal. | 2 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
* [Contoh penggunaan symlink untuk pembacaan file secara sewenang-wenang (arbitrary file read)](https://hackerone.com/reports/1439593)
* [Penjelasan mengenai "Magic Bytes" dari Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures)