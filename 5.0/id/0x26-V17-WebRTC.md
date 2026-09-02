# V17 WebRTC

## Tujuan Kontrol

Web Real-Time Communication (WebRTC) memungkinkan pertukaran suara, video, dan data secara _real-time_ dalam aplikasi modern. Seiring dengan peningkatan adopsinya, mengamankan infrastruktur WebRTC menjadi sangat krusial. Bagian ini menyediakan persyaratan keamanan bagi para pemangku kepentingan yang mengembangkang, meng-host, atau mengintegrasikan sistem WebRTC.

Pasar WebRTC secara garis besar dapat dikategorikan menjadi tiga segmen:

1. Product Developers: Vendor _proprietary_ dan _open-source_ yang membuat dan menyuplai produk serta solusi WebRTC. Fokus mereka adalah mengembangkan teknologi WebRTC yang tangguh dan aman yang dapat digunakan oleh pihak lain.

2. Communication Platforms as a Service (CPaaS): Penyedia yang menawarkan API, SDK, serta infrastruktur atau platform yang diperlukan untuk mengaktifkan fungsionalitas WebRTC. Penyedia CPaaS dapat menggunakan produk dari kategori pertama atau mengembangkan perangkat lunak WebRTC mereka sendiri untuk menawarkan layanan ini.

3. Service Providers: Organisasi yang memanfaatkan produk dari pengembang produk atau penyedia CPaaS, atau mengembangkan solusi WebRTC mereka sendiri. Mereka membuat dan mengimplementasikan aplikasi untuk konferensi _online_, layanan kesehatan, _e-learning_, dan domain lainnya di mana komunikasi _real-time_ sangat penting.

Persyaratan keamanan yang diuraikan di sini utamanya difokuskan pada Pengembang Produk, CPaaS, dan Penyedia Layanan yang:

* Memanfaatkan solusi _open-source_ untuk membangun aplikasi WebRTC mereka.
* Menggunakan produk WebRTC komersial sebagai bagian dari infrastruktur mereka.
* Menggunakan solusi WebRTC yang dikembangkan secara internal atau mengintegrasikan berbagai komponen menjadi satu penawaran layanan yang kohesif.

Penting untuk dicatat bahwa persyaratan keamanan ini tidak berlaku bagi pengembang yang secara eksklusif menggunakan SDK dan API yang disediakan oleh vendor CPaaS. Bagi pengembang tersebut, penyedia CPaaS biasanya bertanggung jawab atas sebagian besar masalah keamanan yang mendasari platform mereka, dan standar keamanan generik seperti ASVS mungkin tidak sepenuhnya memenuhi kebutuhan mereka.

## V17.1 TURN Server

Bagian ini mendefinisikan persyaratan keamanan untuk sistem yang mengoperasikan server TURN (Traversal Using Relays around NAT) milik mereka sendiri. Server TURN membantu meneruskan (_relay_) media dalam lingkungan jaringan yang terbatas, tetapi dapat menimbulkan risiko jika salah dikonfigurasi. Kontrol ini berfokus pada penyaringan alamat yang aman dan perlindungan terhadap kehabisan sumber daya (_resource exhaustion_).

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **17.1.1** | Verifikasi bahwa layanan Traversal Using Relays around NAT (TURN) hanya mengizinkan akses ke alamat IP yang tidak dipesan untuk tujuan khusus (misalnya, jaringan internal, _broadcast_, _loopback_). Perhatikan bahwa ini berlaku untuk alamat IPv4 dan IPv6. | 2 |
| **17.1.2** | Verifikasi bahwa layanan Traversal Using Relays around NAT (TURN) tidak rentan terhadap kehabisan sumber daya (_resource exhaustion_) ketika pengguna yang sah mencoba membuka sejumlah besar _port_ pada server TURN. | 3 |

## V17.2 Media

Persyaratan ini hanya berlaku untuk sistem yang meng-host server media WebRTC milik mereka sendiri, seperti Selective Forwarding Units (SFUs), Multipoint Control Units (MCUs), server perekaman, atau server gateway. Server media menangani dan mendistribusikan _stream_ media, menjadikan keamanannya sangat krusial untuk melindungi komunikasi antar _peer_. Mengamankan _stream_ media sangat penting dalam aplikasi WebRTC untuk mencegah penyadapan (_eavesdropping_), manipulasi data (_tampering_), dan serangan _Denial-of-Service_ (DoS) yang dapat mengompromikan privasi pengguna dan kualitas komunikasi.

Secara khusus, sangat penting untuk mengimplementasikan perlindungan terhadap _flood attack_ seperti _rate limiting_, memvalidasi _timestamp_, menggunakan jam yang tersinkronisasi untuk mencocokkan interval _real-time_, dan mengelola _buffer_ untuk mencegah _overflow_ serta menjaga pewaktuan yang tepat. Jika paket untuk sesi media tertentu tiba terlalu cepat, paket berlebih harus dibuang (_dropped_). Penting juga untuk melindungi sistem dari paket yang rusak (_malformed_) dengan menerapkan validasi input, menangani _integer overflow_ secara aman, mencegah _buffer overflow_, dan menggunakan teknik penanganan error yang tangguh lainnya.

Sistem yang hanya mengandalkan komunikasi media _peer-to-peer_ antar peramban web, tanpa keterlibatan server media perantara, dikecualikan dari persyaratan keamanan terkait media khusus ini.

Bagian ini mengacu pada penggunaan Datagram Transport Layer Security (DTLS) dalam konteks WebRTC. Persyaratan yang berkaitan dengan kepemilikan kebijakan terdokumentasi untuk pengelolaan kunci kriptografi dapat ditemukan pada bab "Kriptografi". Informasi tentang metode kriptografi yang disetujui dapat ditemukan dalam Lampiran Kriptografi ASVS atau dalam dokumen seperti NIST SP 800-52 Rev. 2 atau BSI TR-02102-2 (Versi 2025-01).

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **17.2.1** | Verifikasi bahwa kunci untuk sertifikat Datagram Transport Layer Security (DTLS) dikelola dan dilindungi berdasarkan kebijakan terdokumentasi untuk pengelolaan kunci kriptografi. | 2 |
| **17.2.2** | Verifikasi bahwa server media dikonfigurasi untuk menggunakan dan mendukung _cipher suites_ Datagram Transport Layer Security (DTLS) yang disetujui serta _protection profile_ yang aman untuk DTLS Extension dalam menetapkan kunci bagi Secure Real-time Transport Protocol (DTLS-SRTP). | 2 |
| **17.2.3** | Verifikasi bahwa otentikasi Secure Real-time Transport Protocol (SRTP) diperiksa pada server media untuk mencegah serangan injeksi Real-time Transport Protocol (RTP) yang dapat menyebabkan kondisi _Denial of Service_ atau penyisipan media audio atau video ke dalam _stream_ media. | 2 |
| **17.2.4** | Verifikasi bahwa server media mampu melanjutkan pemrosesan lalu lintas media yang masuk ketika menemui paket Secure Real-time Transport Protocol (SRTP) yang cacat (_malformed_). | 2 |
| **17.2.5** | Verifikasi bahwa server media mampu melanjutkan pemrosesan lalu lintas media yang masuk selama terjadinya lonjakan paket (_flood_) Secure Real-time Transport Protocol (SRTP) dari pengguna yang sah. | 3 |
| **17.2.6** | Verifikasi bahwa server media tidak rentan terhadap kerentanan _Race Condition_ "ClientHello" pada Datagram Transport Layer Security (DTLS) dengan memeriksa apakah server media secara publik diketahui rentan atau dengan melakukan pengujian _race condition_. | 3 |
| **17.2.7** | Verifikasi bahwa setiap mekanisme perekaman audio atau video yang terkait dengan server media mampu melanjutkan pemrosesan lalu lintas media yang masuk selama terjadinya lonjakan paket (_flood_) Secure Real-time Transport Protocol (SRTP) dari pengguna yang sah. | 3 |
| **17.2.8** | Verifikasi bahwa sertifikat Datagram Transport Layer Security (DTLS) diperiksa terhadap atribut _fingerprint_ Session Description Protocol (SDP), dan menghentikan _stream_ media jika pemeriksaan gagal, untuk memastikan keaslian (_authenticity_) dari _stream_ media. | 3 |

## V17.3 Signaling

Bagian ini mendefinisikan persyaratan untuk sistem yang mengoperasikan server _signaling_ WebRTC milik mereka sendiri. _Signaling_ mengoordinasikan komunikasi _peer-to-peer_ dan harus tangguh terhadap serangan yang dapat mengganggu pembuatan atau kontrol sesi.

Untuk memastikan _signaling_ yang aman, sistem harus menangani input yang cacat (_malformed_) dengan baik (_gracefully_) dan tetap tersedia di bawah beban kerja yang tinggi.

| # | Deskripsi | Level |
| :---: | :--- | :---: |
| **17.3.1** | Verifikasi bahwa server _signaling_ mampu melanjutkan pemrosesan pesan _signaling_ masuk yang sah selama serangan _flood_. Hal ini harus dicapai dengan mengimplementasikan _rate limiting_ pada tingkat _signaling_. | 2 |
| **17.3.2** | Verifikasi bahwa server _signaling_ mampu melanjutkan pemrosesan pesan _signaling_ yang sah ketika menemui pesan _signaling_ yang cacat (_malformed_) yang dapat menyebabkan kondisi _Denial of Service_. Ini dapat mencakup pengimplementasian validasi input, penanganan _integer overflow_ secara aman, pencegahan _buffer overflow_, dan penggunaan teknik penanganan error yang tangguh lainnya. | 2 |

## Referensi

Untuk informasi lebih lanjut, lihat juga:

* WebRTC DTLS ClientHello DoS didokumentasikan paling baik pada [postingan blog Enable Security yang ditujukan untuk profesional keamanan](https://www.enablesecurity.com/blog/novel-dos-vulnerability-affecting-webrtc-media-servers/) dan [white paper terkait yang ditujukan untuk pengembang WebRTC](https://www.enablesecurity.com/blog/webrtc-hello-race-conditions-paper/)
* [RFC 3550 - RTP: A Transport Protocol for Real-Time Applications](https://www.rfc-editor.org/rfc/rfc3550)
* [RFC 3711 - The Secure Real-time Transport Protocol (SRTP)](https://datatracker.ietf.org/doc/html/rfc3711)
* [RFC 5764 - Datagram Transport Layer Security (DTLS) Extension to Establish Keys for the Secure Real-time Transport Protocol (SRTP))](https://datatracker.ietf.org/doc/html/rfc5764)
* [RFC 8825 - Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/info/rfc8825)
* [RFC 8826 - Security Considerations for WebRTC](https://www.rfc-editor.org/info/rfc8826)
* [RFC 8827 - WebRTC Security Architecture](https://www.rfc-editor.org/info/rfc8827)
* [DTLS-SRTP Protection Profiles](https://www.iana.org/assignments/srtp-protection/srtp-protection.xhtml)
