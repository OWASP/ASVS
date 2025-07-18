# V13 Konfigürasyon

## Kontrol Amacı

Uygulamanın varsayılan konfigürasyonu, İnternet üzerinde güvenli kullanım için uygun olmalıdır.

Bu bölüm, geliştirme, derleme ve dağıtım aşamalarında uygulanması gereken çeşitli konfigürasyonlara dair rehberlik sağlar.

Ele alınan konular veri sızıntısını önlemek, bileşenler arası iletişimi güvenli şekilde yönetmek ve gizli verileri korumayı içerir.

## V13.1 Konfigürasyon Dokümantasyonu

Bu bölüm, uygulamanın iç ve dış hizmetlerle nasıl iletişim kurduğunu açıklayan dokümantasyon gereksinimlerini ve hizmetlerin erişilemez olması durumunda erişilebilirliğin kaybını önlemek için kullanılabilecek teknikleri tanımlar. Ayrıca, gizli verilerle ilgili belgeleri de kapsar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **13.1.1** | Uygulamanın tüm iletişim ihtiyaçlarının dokümante edildiği doğrulanmalıdır. Buna, uygulamanın bağımlı olduğu dış hizmetler ve son kullanıcının uygulamanın bağlantı kurmasını sağlayabileceği dış konumlar da dahil olmalıdır. | 2 |
| **13.1.2** | Uygulamanın kullandığı her bir hizmet için, dokümantasyonda eşzamanlı bağlantı sayısı (örn. bağlantı havuzu limitleri) ve bu sınır aşıldığında uygulamanın davranışı, geri dönüş veya kurtarma mekanizmaları da dahil olmak üzere hizmet reddi koşullarını önlemek için tanımlandığı doğrulanmalıdır. | 3 |
| **13.1.3** | Uygulamanın, kullandığı her bir dış sistem veya hizmet (örn. veritabanları, dosya tanıtıcıları, iş parçacıkları, HTTP bağlantıları) için kaynak yönetimi stratejilerini tanımladığı doğrulanmalıdır. Bu stratejiler, kaynak serbest bırakma prosedürlerini, zaman aşımı ayarlarını, hata durumlarını ve tekrar deneme mantığı uygulanmışsa sınırları, gecikmeleri ve geri çekilme (back-off) algoritmalarını içermelidir. Senkron HTTP istek–yanıt işlemleri için kısa zaman aşımı süreleri zorunlu tutulmalı ve tekrar eden denemeler devre dışı bırakılmalı ya da sıkı şekilde sınırlandırılmalıdır. | 3 |
| **13.1.4** | Uygulamanın, güvenlik açısından kritik olan gizli verileri tanımladığı ve kuruluşun tehdit modeli ve iş ihtiyaçlarına göre bu verilerin döndürülme (rotation) zamanlamasının belgelendiği doğrulanmalıdır. | 3 |

## V13.2 Backend İletişim Konfigürasyonu

Uygulamalar, API'ler, veritabanları veya diğer bileşenler gibi çok sayıda hizmetle etkileşime girer. Bu hizmetler, uygulamaya dâhil olarak kabul edilebilir ancak uygulamanın standart erişim kontrol mekanizmalarına dahil olmayabilir veya tamamen dış sistemler olabilir. Her iki durumda da, uygulamanın bu bileşenlerle güvenli şekilde iletişim kuracak şekilde yapılandırılması ve gerekiyorsa bu yapılandırmanın korunması gereklidir.

Not: "Güvenli İletişim" bölümü, aktarım sırasında şifreleme için rehberlik sağlar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **13.2.1** | Uygulamanın, standart kullanıcı oturum mekanizmasını desteklemeyen backend bileşenleri (örneğin API'ler, ara katmanlar, veri katmanları) arasında gerçekleşen iletişimlerin kimlik doğrulamasıyla korunduğu doğrulanmalıdır. Kimlik doğrulama; bireysel hizmet hesapları, kısa ömürlü token'lar ya da sertifika tabanlı kimlik doğrulama ile yapılmalıdır ve parola, API anahtarı ya da ayrıcalıklı erişime sahip paylaşımlı hesaplar gibi sabit kimlik bilgileri kullanılmamalıdır. | 2 |
| **13.2.2** | Uygulamanın backend bileşenleri arasında (yerel hizmetler, işletim sistemi hizmetleri, API'ler, ara katmanlar ve veri katmanları dahil) gerçekleştirilen iletişimlerin, yalnızca gerekli en az ayrıcalığa sahip hesaplarla yapıldığı doğrulanmalıdır. | 2 |
| **13.2.3** | Bir hizmet kimlik doğrulaması için bir kimlik bilgisi kullanılması gerekiyorsa, bu kimlik bilgisinin varsayılan bir değer (örneğin root/root veya admin/admin) olmadığının doğrulanması gereklidir. | 2 |
| **13.2.4** | Uygulamanın iletişim kurmasına izin verilen dış kaynaklar ya da sistemlerin, bir allowlist (izinli liste) ile tanımlandığı doğrulanmalıdır. Bu liste, uygulama katmanında, web sunucusunda, güvenlik duvarında veya farklı katmanların birleşiminde uygulanabilir. | 2 |
| **13.2.5** | Web veya uygulama sunucusunun, dış sistemlere veri veya dosya gönderimi veya yüklemesi yaparken sadece belirli kaynaklara izin verecek şekilde allowlist ile yapılandırıldığı doğrulanmalıdır. | 2 |
| **13.2.6** | Uygulamanın farklı hizmetlere bağlantı kurduğu durumlarda, bu bağlantılar için belgelenmiş yapılandırmaları (örn. maksimum eşzamanlı bağlantı, bağlantı limiti aşıldığında davranış, zaman aşımı, tekrar deneme stratejileri) takip ettiğinin doğrulanması gereklidir. | 3 |

## V13.3 Gizli Bilgi Yönetimi

Gizli bilgilerin (secret) yönetimi, uygulama tarafından kullanılan verilerin korunması açısından temel bir konfigürasyon görevidir. Kriptografi ile ilgili özel gereksinimler "Kriptografi" bölümünde yer almakla birlikte bu bölüm, gizli verilerin yönetimi ve işlenmesine odaklanır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **13.3.1** | Parolalar, anahtar materyalleri, veritabanı ve üçüncü parti sistemlerle entegrasyon bilgileri, zaman tabanlı token'lar için tohum (seed) bilgileri, dahili gizli veriler ve API anahtarları gibi backend sırlarının güvenli bir şekilde oluşturulması, saklanması, erişim denetiminin sağlanması ve imha edilmesi için bir gizli bilgi yönetim çözümünün (örneğin key vault) kullanıldığı doğrulanmalıdır. Bu gizli bilgiler uygulama kaynak koduna dahil edilmemeli ve yapı çıktılarında yer almamalıdır. Seviye 3 uygulamalar için donanım destekli bir çözüm (örneğin HSM) gereklidir. | 2 |
| **13.3.2** | Gizli bilgilere erişimin en az ayrıcalık prensibine uygun şekilde yapılandırıldığı doğrulanmalıdır. | 2 |
| **13.3.3** | Tüm kriptografik işlemlerin, anahtar materyallerinin güvenli bir şekilde yönetilmesi ve dışarıya sızmasının engellenmesi amacıyla, izole edilmiş bir güvenlik modülü (örneğin vault ya da donanım güvenlik modülü) aracılığıyla gerçekleştirildiği doğrulanmalıdır. | 3 |
| **13.3.4** | Uygulamanın belgelerinde belirtildiği şekilde gizli bilgilerin süresinin dolacak şekilde yapılandırıldığı ve düzenli olarak döndürüldüğü doğrulanmalıdır. | 3 |

## V13.4 İstenmeyen Bilgi Sızıntısı

Üretim yapılandırmaları, gereksiz veri ifşasını önleyecek şekilde sertleştirilmiş (hardened) olmalıdır. Bu tür güvenlik açıkları genellikle tek başına büyük risk olarak değerlendirilmese de diğer açıklıklarla zincirlenerek sömürülebilir. Varsayılan olarak bu açıklıkların bulunmaması, uygulamaya yapılacak saldırıların zorluk seviyesini artırır.

Örneğin, sunucu taraflı bileşenlerin sürüm bilgisini gizlemek, tüm bileşenlerin yamanması ihtiyacını ortadan kaldırmaz; dizin listelemeyi devre dışı bırakmak, yetkilendirme kontrolleri ihtiyacını ya da dosyaların herkese açık klasörden uzak tutulması gerekliliğini ortadan kaldırmaz. Ancak bunlar, saldırıların başarıya ulaşma olasılığını azaltır.


Production configurations should be hardened to avoid disclosing unnecessary data. Many of these issues are rarely rated as significant risks but are often chained with other vulnerabilities. If these issues are not present by default, it raises the bar for attacking an application.

For example, hiding the version of server-side components does not eliminate the need to patch all components, and disabling folder listing does not remove the need to use authorization controls or keep files away from the public folder, but it raises the bar.

| # | Description | Level |
| :---: | :--- | :---: |
| **13.4.1** | Verify that the application is deployed either without any source control metadata, including the .git or .svn folders, or in a way that these folders are inaccessible both externally and to the application itself. | 1 |
| **13.4.2** | Verify that debug modes are disabled for all components in production environments to prevent exposure of debugging features and information leakage. | 2 |
| **13.4.3** | Verify that web servers do not expose directory listings to clients unless explicitly intended. | 2 |
| **13.4.4** | Verify that using the HTTP TRACE method is not supported in production environments, to avoid potential information leakage. | 2 |
| **13.4.5** | Verify that documentation (such as for internal APIs) and monitoring endpoints are not exposed unless explicitly intended. | 2 |
| **13.4.6** | Verify that the application does not expose detailed version information of backend components. | 3 |
| **13.4.7** | Verify that the web tier is configured to only serve files with specific file extensions to prevent unintentional information, configuration, and source code leakage. | 3 |

## References

For more information, see also:

* [OWASP Web Security Testing Guide: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing)
