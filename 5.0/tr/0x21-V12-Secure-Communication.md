# V12 Güvenli İletişim

## Kontrol Amacı

Bu bölüm, hem bir son kullanıcı istemcisi ile backend hizmeti arasında hem de iç sistemler ile backend hizmetleri arasındaki veri iletimini korumak için uygulanması gereken özel mekanizmalara ilişkin gereksinimleri içerir.

Bu bölümde öne çıkan genel kavramlar şunlardır:

* İletişimlerin dış sistemlerle şifreli, ideal olarak iç sistemlerde de şifreli olması.
* Şifreleme mekanizmalarının, tercih edilen algoritmalar ve şifreler dahil olmak üzere en güncel rehberliklere göre yapılandırılması.
* Yetkisiz taraflarca iletişimin engellenmediğinden emin olmak amacıyla imzalı sertifikaların kullanılması.

Genel ilkelere ve en iyi uygulamalara ek olarak, ASVS ayrıca Ek C - Kriptografi Standartları bölümünde kriptografik güç hakkında daha derin teknik bilgiler sunar.

## V12.1 Genel TLS Güvenlik Rehberi

Bu bölüm, TLS iletişimini güvenli hale getirmek için başlangıç seviyesinde rehberlik sağlar. TLS yapılandırmasının güncel araçlarla düzenli olarak gözden geçirilmesi gerekir.

Wildcard TLS sertifikalarının kullanımı doğası gereği güvensiz değildir, ancak aynı sertifikanın üretim, hazırlık (staging), geliştirme ve test gibi tüm ortamlarda kullanılması halinde sertifika güvenliğinin tehlikeye girmesi, bu ortamlarda çalışan uygulamaların da güvenlik postürünü olumsuz etkileyebilir. Mümkünse her ortam için ayrı TLS sertifikalarının kullanılması, bu sertifikaların güvenli bir şekilde yönetilmesi ve korunması gereklidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **12.1.1** | Yalnızca TLS protokolünün en güncel ve önerilen sürümlerinin (örneğin TLS 1.2 ve TLS 1.3) etkinleştirildiği ve en son sürümün varsayılan olarak tercih edildiği doğrulanmalıdır. | 1 |
| **12.1.2** | Yalnızca önerilen şifre takımlarının (cipher suite) etkinleştirildiği ve en güçlü şifre takımlarının tercih edildiği doğrulanmalıdır. Seviye 3 (L3) uygulamalar yalnızca ileri gizlilik (forward secrecy) sağlayan şifre takımlarını desteklemelidir. | 2 |
| **12.1.3** | Uygulamanın, mTLS istemci sertifikalarını kimlik doğrulama veya yetkilendirme amacıyla kullanmadan önce bu sertifikaların güvendiği sertifikalar arasında olduğunu doğruladığı kontrol edilmelidir. | 2 |
| **12.1.4** | Online Certificate Status Protocol (OCSP) Stapling gibi geçerli bir sertifika iptal kontrolü yönteminin etkinleştirildiği ve yapılandırıldığı doğrulanmalıdır. | 3 |
| **12.1.5** | TLS el sıkışma (handshake) sürecinde Server Name Indication (SNI) gibi hassas meta verilerin ifşa edilmesini önlemek için, uygulamanın TLS yapılandırmasında Encrypted Client Hello (ECH) özelliğinin etkinleştirildiği doğrulanmalıdır. | 3 |

## V12.2 Dışa Açık Hizmetlerle HTTPS İletişimi

Uygulamanın dışa açtığı tüm HTTP trafiğinin şifreli olarak iletildiğinden ve bu iletişimlerde herkese açık olarak güvenilen sertifikaların kullanıldığından emin olunmalıdır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **12.2.1** | İstemci ile dışa açık, HTTP tabanlı hizmetler arasındaki tüm bağlantılarda TLS kullanıldığı ve bu bağlantıların güvensiz ya da şifrelenmemiş iletişime geri dönmediği doğrulanmalıdır. | 1 |
| **12.2.2** | Dışa açık hizmetlerin herkese açık olarak güvenilen TLS sertifikaları kullandığı doğrulanmalıdır. | 1 |

## V12.3 Genel Servisler Arası İletişim Güvenliği

Sunucu iletişimleri (hem iç hem dış) sadece HTTP ile sınırlı değildir. Diğer sistemlerle olan bağlantıların da güvenli olması gerekir ve ideal olarak TLS kullanılmalıdır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **12.3.1** | Uygulamaya gelen ve uygulamadan çıkan tüm bağlantılarda izleme sistemleri, yönetim araçları, uzaktan erişim ve SSH, ara yazılımlar, veritabanları, ana sistemler (mainframe), iş ortağı sistemleri ya da dış API'ler dahil olmak üzere TLS gibi şifreli bir protokolün kullanıldığı ve güvensiz ya da şifrelenmemiş protokollere geri dönülmediği doğrulanmalıdır. | 2 |
| **12.3.2** | TLS istemcilerinin bir TLS sunucusu ile iletişime geçmeden önce alınan sertifikaları doğruladığı kontrol edilmelidir. | 2 |
| **12.3.3** | Uygulama içindeki HTTP tabanlı iç hizmetler arasında gerçekleşen tüm bağlantılarda TLS ya da uygun başka bir aktarım şifreleme mekanizmasının kullanıldığı ve güvensiz ya da şifrelenmemiş iletişime geri dönülmediği doğrulanmalıdır. | 2 |
| **12.3.4** | İç hizmetler arasındaki TLS bağlantılarında güvenilir sertifikaların kullanıldığı doğrulanmalıdır. İç sistemlerde oluşturulmuş ya da kendinden imzalı (self-signed) sertifikalar kullanılıyorsa, bu sertifikalara güvenen hizmetlerin yalnızca belirli dahili sertifika otoritelerine (CA) ve belirli kendinden imzalı sertifikalara güvenecek şekilde yapılandırıldıkları doğrulanmalıdır. | 2 |
| **12.3.5** | Sistem içindeki hizmetlerin birbiriyle iletişim kurarken her bir uç noktanın kimliğini doğrulamak için güçlü kimlik doğrulama yöntemlerinin kullanıldığı doğrulanmalıdır. Bu yöntemler arasında, açık anahtar altyapısı (public-key infrastructure) kullanan ve tekrar oynatma saldırılarına karşı dayanıklı olan TLS istemci kimlik doğrulaması gibi yöntemler yer almalıdır. Mikroservis mimarilerinde, sertifika yönetimini basitleştirmek ve güvenliği artırmak amacıyla bir servis ağı (service mesh) kullanılması değerlendirilmelidir. | 3 |

## Referanslar

Daha fazla bilgi için:

* [OWASP - Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
* [Mozilla's Server Side TLS configuration guide](https://wiki.mozilla.org/Security/Server_Side_TLS)
* [Mozilla's tool to generate known good TLS configurations](https://ssl-config.mozilla.org/).
* [O-Saft - OWASP Project to validate TLS configuration](https://owasp.org/www-project-o-saft/)
