# V4 API ve Web Servisi

## Kontrol Amacı

Web tarayıcıları veya diğer istemciler tarafından kullanılmak üzere API'ler sunan uygulamalara özgü bazı ek değerlendirmeler bulunmaktadır (genellikle JSON, XML veya GraphQL kullanılır). Bu bölüm, uygulanması gereken ilgili güvenlik yapılandırmaları ve mekanizmaları kapsar.

Kimlik doğrulama, oturum yönetimi ve girdi doğrulama gibi diğer bölümlerde ele alınan konuların API'ler için de geçerli olduğunu unutmayın; bu nedenle bu bölüm bağlamından bağımsız düşünülemez veya tek başına test edilemez.

## V4.1 Genel Web Servisi Güvenliği

Bu bölüm, genel web servisi güvenliğiyle ilgili değerlendirmeleri ve temel web servisi hijyen uygulamalarını ele alır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **4.1.1** | İleti gövdesi içeren her HTTP yanıtında, yanıtın gerçek içeriğiyle eşleşen bir Content-Type header alanı bulunduğu ve güvenli karakter kodlamasını (örneğin, UTF-8, ISO-8859-1) belirtmek üzere charset parametresi içerdiği doğrulanmalıdır. Bu işlem, IANA Medya Türleri'nden "text/", "/+xml" ve "/xml" gibi içerikler için geçerlidir. | 1 |
| **4.1.2** | Yalnızca kullanıcı arayüzüne yönelik uç noktaların (manuel olarak web tarayıcısı ile erişilmesi amaçlanan) otomatik olarak HTTP'den HTTPS'e yönlendirme yaptığı ve diğer hizmetlerin veya uç noktaların şeffaf yönlendirme gerçekleştirmediği doğrulanmalıdır. Bu, istemcinin farkında olmadan şifrelenmemiş HTTP istekleri göndermesi ve bu isteklerin otomatik olarak HTTPS'e yönlendirilmesi sonucunda hassas verilerin sızmasının fark edilmemesi riskini önlemek içindir. | 2 |
| **4.1.3** | Uygulama tarafından kullanılan ve yük dengeleyici, web proxy veya frontend için backend hizmeti gibi bir ara katman tarafından ayarlanan herhangi bir HTTP başlık alanının, son kullanıcı tarafından geçersiz kılınamayacağı doğrulanmalıdır. Örnek başlıklar arasında X-Real-IP, X-Forwarded-* veya X-User-ID yer alabilir. | 2 |
| **4.1.4** | Uygulama veya API tarafından açıkça desteklenen HTTP yöntemlerinin (preflight istekleri sırasında OPTIONS dahil) dışında hiçbir yöntemin kullanılmadığı ve kullanılmayan yöntemlerin engellendiği doğrulanmalıdır. | 3 |
| **4.1.5** | Çok hassas istekler veya birçok sistemden geçen işlemler için, taşıma katmanı güvenliğinin üzerine ek bir güvence sağlamak amacıyla, her iletiye özel dijital imzaların kullanıldığı doğrulanmalıdır. | 3 |

## V4.2 HTTP İleti Yapısı Doğrulama

Bu bölüm, HTTP ileti yapısının ve başlık alanlarının doğrulanma biçimini açıklar. Amaç, istek kaçakçılığı, yanıt bölme, başlık enjeksiyonu ve aşırı uzun HTTP iletileri aracılığıyla hizmet reddi gibi saldırıları önlemektir.

Bu gereksinimler, genel HTTP ileti işleme ve üretimi için geçerlidir; ancak farklı HTTP sürümleri arasında HTTP iletileri dönüştürülürken özellikle önemlidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **4.2.1** | Tüm uygulama bileşenlerinin (yük dengeleyiciler, güvenlik duvarları ve uygulama sunucuları dahil) HTTP sürümüne uygun mekanizmaları kullanarak gelen HTTP iletilerinin sınırlarını belirlediği ve bu sayede HTTP istek kaçakçılığına karşı koruma sağlandığı doğrulanmalıdır. HTTP/1.x sürümünde Transfer-Encoding başlık alanı varsa, RFC 2616'ya göre Content-Length başlığı göz ardı edilmelidir. HTTP/2 veya HTTP/3 kullanıldığında, Content-Length başlığı varsa, alıcının bu değerin DATA çerçevelerinin uzunluğuyla tutarlı olduğunu doğrulaması gerekir. | 2 |
| **4.2.2** | HTTP iletileri üretilirken, Content-Length başlığının, HTTP protokolünün çerçeveleme yöntemine göre belirlenen içerik uzunluğu ile çelişmediği doğrulanmalıdır. Bu, istek kaçakçılığı saldırılarını önlemek için gereklidir. | 3 |
| **4.2.3** | Uygulamanın, yanıt bölme ve header enjeksiyonu saldırılarını önlemek amacıyla, bağlantıya özel başlık alanları (örneğin Transfer-Encoding) içeren HTTP/2 veya HTTP/3 iletilerini göndermediği ve kabul etmediği doğrulanmalıdır. | 3 |
| **4.2.4** | Uygulamanın yalnızca başlık alanları ve değerleri CR (\r), LF (\n) veya CRLF (\r\n) karakter dizileri içermeyen HTTP/2 ve HTTP/3 isteklerini kabul ettiği doğrulanmalıdır. Bu, başlık enjeksiyonu saldırılarını önlemek içindir. | 3 |
| **4.2.5** | Uygulama (backend veya frontend) istek oluşturuyor ve gönderiyorsa, URI'ler (örneğin API çağrıları için) veya HTTP istek başlıkları (örneğin Authorization veya Cookie) gibi bileşenlerin, alıcı sistemler tarafından kabul edilemeyecek kadar uzun olmamasını sağlamak amacıyla doğrulama, temizleme veya diğer mekanizmaları kullandığı doğrulanmalıdır. Bu tür çok uzun istekler (örneğin çok uzun bir Cookie başlığı) gönderildiğinde sunucunun sürekli hata durumu döndürmesiyle hizmet reddi oluşabilir. | 3 |

## V4.3 GraphQL

GraphQL, veri açısından zengin istemcilerin çeşitli backend servislerine sıkı sıkıya bağlı olmadan oluşturulması için giderek daha yaygın hale gelen bir yöntemdir. Bu bölüm, GraphQL ile ilgili güvenlik değerlendirmelerini kapsar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **4.3.1** | Maliyetli ve iç içe geçmiş sorgular sonucu oluşabilecek GraphQL veya veri katmanı ifadelerine yönelik Hizmet Reddi (DoS) saldırılarını önlemek için, sorgu izin listesi (allowlist), derinlik sınırlandırması, sorgu sayısı sınırlandırması veya sorgu maliyeti analizi kullanıldığı doğrulanmalıdır. | 2 |
| **4.3.2** | GraphQL introspection (iç yapı sorgulama) sorgularının, GraphQL API'nin üçüncü taraflar tarafından kullanılmasına yönelik olmadığı sürece, üretim ortamında devre dışı bırakıldığı doğrulanmalıdır. | 2 |

## V4.4 WebSocket

WebSocket, tek bir TCP bağlantısı üzerinden eşzamanlı çift yönlü iletişim sağlayan bir iletişim protokolüdür. 2011 yılında IETF tarafından RFC 6455 olarak standartlaştırılmıştır ve HTTP'den farklıdır, ancak 443 ve 80 numaralı HTTP portları üzerinden çalışacak şekilde tasarlanmıştır.

Bu bölüm, özellikle bu gerçek zamanlı iletişim kanalını hedef alan iletişim güvenliği ve oturum yönetimi ile ilgili saldırılara karşı korunmak için gerekli olan güvenlik gereksinimlerini sunar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **4.4.1** | Tüm WebSocket bağlantılarında TLS üzerinden WebSocket (WSS) kullanıldığı doğrulanmalıdır. | 1 |
| **4.4.2** | WebSocket'in başlangıçtaki HTTP el sıkışması (handshake) sırasında, Origin başlık alanının uygulama için izin verilen origin listesiyle karşılaştırılarak kontrol edildiği doğrulanmalıdır. | 2 |
| **4.4.3** | Uygulamanın standart oturum yönetimi kullanılamıyorsa, bunun yerine ilgili Oturum Yönetimi güvenlik gereksinimlerine uygun özel token'ların kullanıldığı doğrulanmalıdır. | 2 |
| **4.4.4** | HTTPS oturumu WebSocket kanalına geçerken, özel WebSocket oturum yönetim token’larının önceki şekilde kimliği doğrulanmış HTTPS oturumu aracılığıyla elde edildiği veya doğrulandığı doğrulanmalıdır. | 2 |

## Referanslar

Daha fazla bilgi için:

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* Resources on GraphQL Authorization from [graphql.org](https://graphql.org/learn/authorization/) and [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods).
* [WSTG - v4.2 | GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [WSTG - v4.1 | OWASP Foundation](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)
