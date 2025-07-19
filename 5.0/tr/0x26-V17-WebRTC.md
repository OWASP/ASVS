# V17 WebRTC

## Kontrol Amacı

Web Gerçek Zamanlı İletişim (WebRTC), modern uygulamalarda gerçek zamanlı ses, görüntü ve veri alışverişini mümkün kılar. Kullanım yaygınlaştıkça, WebRTC altyapısının güvenliğinin sağlanması kritik hâle gelir. Bu bölüm, WebRTC sistemlerini geliştiren, barındıran veya entegre eden paydaşlar için güvenlik gereksinimlerini tanımlar.

WebRTC pazarı genel olarak üç kategoriye ayrılabilir:

1. Ürün Geliştiriciler: WebRTC ürün ve çözümlerini geliştiren ve sağlayan özel veya açık kaynak tedarikçileri. Odak noktaları, başkaları tarafından da kullanılabilecek sağlam ve güvenli WebRTC teknolojileri geliştirmektir.

2. Hizmet Olarak İletişim Platformları (Communication Platforms as a Service - CPaaS): WebRTC işlevlerini mümkün kılmak için API, SDK ve altyapı/platform sağlayan hizmet sağlayıcılarıdır. CPaaS sağlayıcıları, birinci kategorideki ürünleri kullanabilir veya kendi WebRTC yazılımlarını geliştirerek bu hizmetleri sunabilirler.

3. Hizmet Sağlayıcılar: Ürün geliştiricilerden veya CPaaS sağlayıcılarından alınan ürünleri kullanan ya da kendi WebRTC çözümlerini geliştiren kuruluşlardır. Bu sağlayıcılar çevrim içi konferans, sağlık, online eğitim gibi alanlarda gerçek zamanlı iletişimin kritik olduğu uygulamalar geliştirirler.

Bu bölümdeki güvenlik gereksinimleri, özellikle aşağıdaki gibi sistemleri kullanan Ürün Geliştiriciler, CPaaS’ler ve Hizmet Sağlayıcıları için geçerlidir:

* WebRTC uygulamalarını oluşturmak için açık kaynak çözümler kullananlar,
* Altyapılarının bir parçası olarak ticari WebRTC ürünlerini kullananlar,
* Kendi WebRTC çözümlerini geliştiren ya da çeşitli bileşenleri birleştirerek entegre hizmet sunanlar.

Not: Bu güvenlik gereksinimleri yalnızca CPaaS sağlayıcılarının sunduğu SDK ve API'leri doğrudan kullanan geliştiricileri kapsamaz. Bu tür durumlarda, güvenlikten büyük ölçüde CPaaS sağlayıcısı sorumlu olur ve ASVS gibi genel güvenlik standartları her zaman tam olarak geçerli olmayabilir.

## V17.1 TURN Sunucusu

Bu bölüm, kendi TURN (Traversal Using Relays around NAT) sunucusunu işleten sistemler için güvenlik gereksinimlerini tanımlar. TURN sunucuları, kısıtlayıcı ağ ortamlarında medya iletimini sağlamak için kullanılır, ancak yanlış yapılandırıldıklarında güvenlik riski oluşturabilirler. Bu gereksinimler, güvenli IP filtrelemesi ve kaynak tüketimine karşı korumaları ele alır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **17.1.1** | TURN hizmetinin yalnızca özel amaçlar için ayrılmamış IP adreslerine (ör. iç ağlar, yayın adresleri, loopback) erişime izin verdiği doğrulanmalıdır. Bu gereksinim hem IPv4 hem de IPv6 adresleri için geçerlidir. | 2 |
| **17.1.2** | TURN hizmetinin, meşru kullanıcıların sunucuda çok sayıda bağlantı noktası açmaya çalışması durumunda kaynak tüketimi saldırılarına karşı dayanıklı olduğu doğrulanmalıdır. | 3 |

## V17.2 Medya

Bu gereksinimler yalnızca kendi WebRTC medya sunucularını (ör. SFU, MCU, kayıt sunucuları veya geçit sunucuları) barındıran sistemler için geçerlidir. Medya sunucuları, medya akışlarını işler ve dağıtır, bu da iletişim güvenliğini sağlamada kritik rol oynar. Medya akışlarını korumak dinlemeyi, kurcalamayı veya hizmet reddi (DoS) saldırılarını önlemek açısından önemlidir.

Özellikle, hız sınırlama, zaman damgalarını doğrulama, gerçek zamanlı aralıkları eşleştirmek için senkronize saatler kullanma ve taşmayı önlemek ve uygun zamanlamayı korumak için arabellekleri (buffer) yönetme gibi flood saldırılarına karşı korumalar uygulamak gerekir. Belirli bir medya oturumu için paketler çok hızlı gelirse, fazla paketler düşürülmelidir. Girdi doğrulaması uygulayarak, tamsayı taşmalarını (integer overflow) güvenli bir şekilde ele alarak, arabellek taşmalarını (buffer overflow) önleyerek ve diğer sağlam hata işleme tekniklerini kullanarak sistemi hatalı biçimlendirilmiş paketlerden korumak da önemlidir.

Sadece peer-to-peer medya iletişimi kullanan sistemler bu medya gereksinimlerinin kapsamı dışındadır.

DTLS (Datagram Transport Layer Security) kullanımıyla ilgili gereksinimler burada yer alır. Kriptografik anahtarların yönetimi için bir politika oluşturulması "Kriptografi" bölümünde ele alınır. Onaylı şifreleme yöntemleri için ASVS’nin Kriptografi Ek’i veya NIST SP 800‑52 Rev. 2, BSI TR‑02102‑2 (2025‑01) gibi belgeler referans alınabilir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **17.2.1** | 	DTLS sertifikası anahtarının, belgelenmiş kriptografik anahtar yönetim politikasına uygun şekilde yönetildiği ve korunduğu doğrulanmalıdır. | 2 |
| **17.2.2** | Medya sunucusunun onaylı DTLS şifre takımlarını (cipher suites) ve Güvenli Gerçek Zamanlı Aktarım Protokolü (Secure Real-time Transport Protocol - SRTP) için anahtarlar oluşturmaya yönelik DTLS Uzantısı için güvenli bir koruma profilini kullanacak ve destekleyecek şekilde yapılandırıldığı (DTLS-SRTP) doğrulanmalıdır. | 2 |
| **17.2.3** | Real-time Transport Protocol (RTP) injection saldırılarının bir hizmet reddi durumuna veya medya akışlarına ses veya video medyası eklenmesine yol açmasını önlemek için medya sunucusunda Güvenli SRTP kimlik doğrulamasının kontrol edildiği doğrulanmalıdır. | 2 |
| **17.2.4** | Verify that the media server is able to continue processing incoming media traffic when encountering malformed Secure Real-time Transport Protocol (SRTP) packets. | 2 |
| **17.2.5** | Medya sunucusunun, meşru kullanıcılardan gelen SRTP flood'ı sırasında gelen medya trafiğini işlemeye devam edebildiği doğrulanmalıdır. | 3 |
| **17.2.6** | Medya sunucusunun DTLS içinde yer alan "ClientHello" yarış durumu güvenlik açığına karşı savunmasız olmadığı, medya sunucusunun güvenlik açığına sahip olduğunun açıkça bilinip bilinmediği kontrol edilerek veya yarış koşulu testi gerçekleştirilerek doğrulanmalıdır. | 3 |
| **17.2.7** | Medya sunucusuna bağlı ses veya video kayıt mekanizmalarının, meşru kullanıcı kaynaklı SRTP flood'ı sırasında medya trafiğini işlemeye devam edebildiği doğrulanmalıdır. | 3 |
| **17.2.8** | DTLS sertifikasının, SDP (Session Description Protocol) fingerprint özelliği ile karşılaştırıldığı ve doğrulama başarısız olursa medya akışının sonlandırıldığı, medya akışının özgünlüğünü sağlamak için doğrulanmalıdır. | 3 |

## V17.3 Sinyalizasyon

Bu bölüm, kendi WebRTC sinyalizasyon sunucularını işleten sistemler için güvenlik gereksinimlerini tanımlar. Sinyalizasyon, peer-to-peer iletişimi koordine eder ve oturum kurulumunu veya kontrolünü bozabilecek saldırılara karşı dayanıklı olmalıdır.

Sinyalizasyonun güvenli olması için sistemler bozuk girdileri zararsız biçimde işleyebilmeli ve yük altında erişilebilir kalmalıdır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **17.3.1** | Sinyalizasyon sunucusunun, flood saldırısı altında bile meşru sinyalizasyon mesajlarını işlemeye devam edebildiği doğrulanmalıdır. Bu, sinyalizasyon düzeyinde oran sınırlaması uygulanarak sağlanmalıdır. | 2 |
| **17.3.2** | Sinyalizasyon sunucusunun, hizmet reddine yol açabilecek şekilde yapılandırılmış bozuk sinyalizasyon mesajlarıyla karşılaştığında bile meşru mesajları işlemeye devam edebildiği doğrulanmalıdır. Bu, girdi doğrulaması, integer overflow ve buffer overflow'a karşı savunma ve sağlam hata işleme teknikleri ile sağlanmalıdır.	 | 2 |

## Referanslar

Daha fazla bilgi için:

* WebRTC DTLS ClientHello DoS hakkında en iyi dokümantasyonlar: [Enable Security's blog post aimed at security professionals](https://www.enablesecurity.com/blog/novel-dos-vulnerability-affecting-webrtc-media-servers/) ve ilgili, [WebRTC geliştiricilerine yönelik white paper](https://www.enablesecurity.com/blog/webrtc-hello-race-conditions-paper/)
* [RFC 3550 - RTP: A Transport Protocol for Real-Time Applications](https://www.rfc-editor.org/rfc/rfc3550)
* [RFC 3711 - The Secure Real-time Transport Protocol (SRTP)](https://datatracker.ietf.org/doc/html/rfc3711)
* [RFC 5764 - Datagram Transport Layer Security (DTLS) Extension to Establish Keys for the Secure Real-time Transport Protocol (SRTP))](https://datatracker.ietf.org/doc/html/rfc5764)
* [RFC 8825 - Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/info/rfc8825)
* [RFC 8826 - Security Considerations for WebRTC](https://www.rfc-editor.org/info/rfc8826)
* [RFC 8827 - WebRTC Security Architecture](https://www.rfc-editor.org/info/rfc8827)
* [DTLS-SRTP Protection Profiles](https://www.iana.org/assignments/srtp-protection/srtp-protection.xhtml)
