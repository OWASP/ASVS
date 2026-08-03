# V14 Data Protection

## Tujuan Kontrol

Aplikasi tidak dapat memperhitungkan seluruh pola penggunaan dan perilaku pengguna, sehingga perlu menerapkan kontrol untuk membatasi akses tidak sah terhadap data sensitif pada perangkat client.

Bab ini mencakup persyaratan yang terkait dengan mendefinisikan data apa yang perlu dilindungi, bagaimana data tersebut harus dilindungi, serta mekanisme spesifik yang perlu diterapkan atau jebakan (pitfalls) yang perlu dihindari.

Pertimbangan lain untuk perlindungan data adalah ekstraksi massal (bulk extraction), modifikasi, atau penggunaan yang berlebihan. Persyaratan setiap sistem kemungkinan akan sangat berbeda-beda, sehingga penentuan apa yang dianggap "tidak wajar" (abnormal) harus mempertimbangkan model ancaman (threat model) dan risiko bisnis. Dari sudut pandang ASVS, pendeteksian masalah-masalah ini ditangani pada bab "Security Logging and Error Handling", dan penentuan batasan ditangani pada bab "Validation and Business Logic".

## V14.1 Dokumentasi Perlindungan Data

Prasyarat utama untuk dapat melindungi data adalah mengategorikan data apa yang harus dianggap sensitif. Kemungkinan akan terdapat beberapa tingkat sensitivitas yang berbeda, dan untuk setiap tingkat, kontrol yang diperlukan untuk melindungi data pada tingkat tersebut akan berbeda-beda.

Terdapat berbagai regulasi dan undang-undang privasi yang memengaruhi bagaimana aplikasi harus melakukan pendekatan terhadap penyimpanan, penggunaan, dan transmisi informasi pribadi yang sensitif. Bagian ini tidak lagi berupaya menduplikasi jenis-jenis undang-undang perlindungan data atau privasi tersebut, melainkan berfokus pada pertimbangan teknis utama untuk melindungi data sensitif. Silakan berkonsultasi dengan hukum dan regulasi setempat, serta berkonsultasi dengan spesialis privasi atau pengacara yang berkualifikasi sesuai kebutuhan.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **14.1.1** | Verifikasi bahwa semua data sensitif yang dibuat dan diproses oleh aplikasi telah diidentifikasi dan diklasifikasikan ke dalam tingkat perlindungan (protection levels). Hal ini mencakup data yang hanya di-encode dan karenanya mudah di-decode, seperti string Base64 atau plaintext payload di dalam sebuah JWT. Tingkat perlindungan perlu mempertimbangkan regulasi dan standar perlindungan data serta privasi yang wajib dipatuhi oleh aplikasi. | 2 |
| **14.1.2** | Verifikasi bahwa semua tingkat perlindungan data sensitif memiliki serangkaian persyaratan perlindungan yang terdokumentasi. Hal ini harus mencakup (namun tidak terbatas pada) persyaratan yang terkait dengan enkripsi secara umum, verifikasi integritas, retensi, bagaimana data tersebut dicatat (logged), kontrol akses terhadap data sensitif dalam log, enkripsi pada level database, privasi dan teknologi peningkat privasi (privacy-enhancing technologies) yang akan digunakan, serta persyaratan kerahasiaan lainnya. | 2 |

## V14.2 Perlindungan Data Secara Umum

Bagian ini berisi berbagai persyaratan praktis yang terkait dengan perlindungan data. Sebagian besar bersifat spesifik terhadap masalah tertentu seperti kebocoran data yang tidak disengaja, namun juga terdapat persyaratan umum untuk menerapkan kontrol perlindungan berdasarkan tingkat perlindungan yang dibutuhkan untuk setiap item data.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **14.2.1** | Verifikasi bahwa data sensitif hanya dikirimkan ke server melalui HTTP message body atau header fields, dan bahwa URL serta query string tidak mengandung informasi sensitif, seperti sebuah API key atau session token. | 1 |
| **14.2.2** | Verifikasi bahwa aplikasi mencegah data sensitif di-cache pada komponen server, seperti load balancer dan application cache, atau memastikan bahwa data tersebut dihapus (purged) secara aman setelah digunakan. | 2 |
| **14.2.3** | Verifikasi bahwa data sensitif yang telah didefinisikan tidak dikirimkan ke pihak yang tidak tepercaya (misalnya, user trackers) guna mencegah pengumpulan data yang tidak diinginkan di luar kendali aplikasi. | 2 |
| **14.2.4** | Verifikasi bahwa kontrol terhadap data sensitif yang terkait dengan enkripsi, verifikasi integritas, retensi, bagaimana data tersebut dicatat (logged), kontrol akses terhadap data sensitif dalam log, serta privasi dan teknologi peningkat privasi, diterapkan sebagaimana didefinisikan dalam dokumentasi untuk tingkat perlindungan data tertentu. | 2 |
| **14.2.5** | Verifikasi bahwa mekanisme caching dikonfigurasi untuk hanya menyimpan cache response yang memiliki content type yang sesuai untuk resource tersebut dan tidak mengandung konten dinamis yang sensitif. Web server harus mengembalikan response 404 atau 302 ketika sebuah file yang tidak ada diakses, alih-alih mengembalikan file lain yang valid. Hal ini seharusnya mencegah serangan Web Cache Deception. | 3 |
| **14.2.6** | Verifikasi bahwa aplikasi hanya mengembalikan data sensitif minimal yang diperlukan untuk fungsionalitas aplikasi. Misalnya, hanya mengembalikan sebagian digit dari sebuah nomor kartu kredit, bukan nomor lengkapnya. Jika data lengkap memang diperlukan, data tersebut harus disamarkan (masked) pada user interface kecuali pengguna secara khusus melihatnya. | 3 |
| **14.2.7** | Verifikasi bahwa informasi sensitif tunduk pada klasifikasi retensi data, memastikan bahwa data yang sudah usang atau tidak diperlukan dihapus secara otomatis, sesuai jadwal yang telah ditentukan, atau sesuai kebutuhan situasi. | 3 |
| **14.2.8** | Verifikasi bahwa informasi sensitif dihapus dari metadata file yang dikirimkan oleh pengguna, kecuali penyimpanan telah disetujui (consented) oleh pengguna tersebut. | 3 |

## V14.3 Perlindungan Data di Sisi Client

Bagian ini berisi persyaratan untuk mencegah kebocoran data dengan cara tertentu pada sisi client atau user agent dari sebuah aplikasi.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **14.3.1** | Verifikasi bahwa data yang terautentikasi dihapus dari penyimpanan client, seperti browser DOM, setelah client atau sesi dihentikan. HTTP response header field 'Clear-Site-Data' dapat membantu hal ini, namun sisi client juga harus mampu membersihkan data tersebut jika koneksi ke server tidak tersedia saat sesi dihentikan. | 1 |
| **14.3.2** | Verifikasi bahwa aplikasi mengatur HTTP response header fields anti-caching yang memadai (yaitu, Cache-Control: no-store) sehingga data sensitif tidak di-cache pada browser. | 2 |
| **14.3.3** | Verifikasi bahwa data yang disimpan pada browser storage (seperti localStorage, sessionStorage, IndexedDB, atau cookies) tidak mengandung data sensitif, dengan pengecualian untuk session token. | 2 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* [Pertimbangkan menggunakan situs Security Headers untuk memeriksa header fields keamanan dan anti-caching](https://securityheaders.com/)
* [Dokumentasi mengenai header anti-caching oleh Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [Australian Privacy Principle 11 - Security of personal information](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-11-app-11-security-of-personal-information)
* [Ikhtisar European Union General Data Protection Regulation (GDPR)](https://www.edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://www.edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
* [Informasi mengenai header "Clear-Site-Data"](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data)
* [White paper mengenai Web Cache Deception](https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack-wp.pdf)