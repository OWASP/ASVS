# V15 Güvenli Kodlama ve Mimari

## Kontrol Amacı

ASVS gereksinimlerinin birçoğu kimlik doğrulama veya yetkilendirme gibi belirli bir güvenlik alanına ya da loglama veya dosya işleme gibi belirli uygulama işlevlerine ilişkindir.

Bu bölüm, uygulamalar tasarlanırken ve geliştirilirken dikkate alınması gereken genel güvenlik gereksinimlerini kapsar. Bu gereksinimler yalnızca temiz mimari ve kod kalitesine değil, aynı zamanda uygulama güvenliği için gerekli olan belirli mimari ve kodlama uygulamalarına da odaklanır.

## V15.1 Güvenli Kodlama ve Mimari Dokümantasyonu

Güvenli ve savunulabilir bir mimarinin oluşturulmasına yönelik birçok gereksinim, uygulamada kullanılan bileşenler ve belirli güvenlik kontrollerinin uygulanmasına ilişkin kararların açıkça belgelenmesine dayanır.

Bu bölüm, “tehlikeli işlevsellik” içeren bileşenler veya “riskli bileşenler” olarak kabul edilen parçaların tanımlanması dahil olmak üzere, dokümantasyon gereksinimlerini açıklar.

"Tehlikeli işlevsellik" içeren bir bileşen, güvenilmeyen verilerin serisizleştirmesini (deserialization) yapan, ham dosya veya ikili veri ayrıştırması gerçekleştiren, dinamik kod çalıştıran veya doğrudan bellekle etkileşen bir dahili ya da üçüncü taraf bileşen olabilir. Bu tür işlemlerdeki güvenlik açıkları, uygulamanın ve altında yatan altyapının ele geçirilmesine yol açabilecek yüksek risklidir.

"Riskli bileşen", güvenlik kontrolleri eksik ya da zayıf şekilde uygulanmış bir üçüncü taraf (ekip içinde geliştirilmemiş) kütüphanedir. Örnekler arasında kötü şekilde sürdürülen, desteklenmeyen, ömrünün sonuna gelmiş veya ciddi güvenlik açıkları geçmişi olan bileşenler yer alır.

Bu bölüm aynı zamanda üçüncü taraf bileşenlerdeki güvenlik açıklarının giderilmesi için uygun zaman çerçevelerinin tanımlanmasının önemini vurgular.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **15.1.1** | Güvenlik açığı içeren üçüncü taraf bileşen sürümleri ve genel olarak kütüphane güncellemeleri için, uygulama dokümantasyonunda risk bazlı düzeltme zamanlarının tanımlandığı doğrulanmalıdır. | 1 |
| **15.1.2** | Yazılım bileşen listesi (Software Bill of Materials - SBOM) gibi bir envanterin tutulduğu, kullanılan tüm üçüncü taraf kütüphanelerin önceden tanımlanmış, güvenilir ve düzenli olarak güncellenen depolardan alındığı doğrulanmalıdır. | 2 |
| **15.1.3** | Uygulama dokümantasyonunda zaman veya kaynak açısından yoğun işlevlerin tanımlandığı, bu işlevlerin aşırı kullanımı durumunda kullanılabilirlik kaybının nasıl önleneceği ve yanıt oluşturma süresinin istemci zaman aşımını aşmaması için hangi önlemlerin alındığı belirtilmelidir. Örnek savunmalar kuyruklama, eşzamansız işleme, kullanıcı başına ve uygulama genelinde paralel işlem sınırlarını içerebilir. | 2 |
| **15.1.4** | Uygulama dokümantasyonunda "riskli bileşenler" olarak değerlendirilen üçüncü taraf kütüphanelerin vurgulandığı doğrulanmalıdır. | 3 |
| **15.1.5** | Uygulama dokümantasyonunda "tehlikeli işlevsellik" içeren uygulama bölümlerinin açıkça belirtildiği doğrulanmalıdır. | 3 |

## V15.2 Güvenlik Mimarisi ve Bağımlılıklar

Bu bölüm riskli, güncel olmayan veya güvensiz bağımlılıkların ve bileşenlerin bağımlılık yönetimi yoluyla nasıl ele alınması gerektiğine dair gereksinimleri içerir.

Ayrıca, “tehlikeli işlemler” veya “riskli bileşenlerin” (önceki bölümde tanımlandığı şekilde) kullanımının etkisini azaltmak ve kaynak yoğun işlevlerin aşırı kullanımından kaynaklı kullanılabilirlik kayıplarını önlemek amacıyla sandboxing, kapsülleme (encapsulation), konteynerleştirme ve ağ izolasyonu gibi mimari düzeydeki tekniklerin kullanımını da kapsar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **15.2.1** | Uygulamanın yalnızca, belgelenmiş güncelleme ve düzeltme sürelerini aşmamış bileşenleri içerdiği doğrulanmalıdır. | 1 |
| **15.2.2** | Uygulamanın, belgelenmiş güvenlik kararları ve stratejilere dayanarak, zaman veya kaynak açısından yoğun işlevlerin neden olabileceği kullanılabilirlik kaybına karşı savunmalar uyguladığı doğrulanmalıdır. | 2 |
| **15.2.3** | Üretim ortamının yalnızca uygulamanın çalışması için gerekli işlevleri içerdiği ve test kodları, örnek kod parçaları veya geliştirme işlevleri gibi gereksiz işlevsellikleri açığa çıkarmadığı doğrulanmalıdır. | 2 |
| **15.2.4** | Üçüncü taraf bileşenlerin ve bunların tüm transitif bağımlılıklarının beklenen depolardan (iç kaynaklı ya da harici) alındığı ve bağımlılık karışıklığı (dependency confusion) saldırılarına açık olmadığı doğrulanmalıdır. | 3 |
| **15.2.5** | Uygulamanın, “tehlikeli işlevsellik” içeren veya “riskli bileşenler” kullanan bölümlerine ek korumalar uyguladığı doğrulanmalıdır. Bu korumalar sandbox, kapsülleme, konteynerleştirme veya ağ düzeyinde izolasyon gibi teknikler aracılığıyla, bir uygulama bölümünün ele geçirilmesi durumunda saldırganın diğer bölümlere sıçramasını geciktirmeyi veya engellemeyi amaçlamalıdır. | 3 |

## V15.3 Defensive Coding

This section covers vulnerability types, including type juggling, prototype pollution, and others, which result from using insecure coding patterns in a particular language. Some may not be relevant to all languages, whereas others will have language-specific fixes or may relate to how a particular language or framework handles a feature such as HTTP parameters. It also considers the risk of not cryptographically validating application updates.

It also considers the risks associated with using objects to represent data items and accepting and returning these via external APIs. In this case, the application must ensure that data fields that should not be writable are not modified by user input (mass assignment) and that the API is selective about what data fields get returned. Where field access depends on a user's permissions, this should be considered in the context of the field-level access control requirement in the Authorization chapter.

| # | Description | Level |
| :---: | :--- | :---: |
| **15.3.1** | Verify that the application only returns the required subset of fields from a data object. For example, it should not return an entire data object, as some individual fields should not be accessible to users. | 1 |
| **15.3.2** | Verify that where the application backend makes calls to external URLs, it is configured to not follow redirects unless it is intended functionality. | 2 |
| **15.3.3** | Verify that the application has countermeasures to protect against mass assignment attacks by limiting allowed fields per controller and action, e.g., it is not possible to insert or update a field value when it was not intended to be part of that action. | 2 |
| **15.3.4** | Verify that all proxying and middleware components transfer the user's original IP address correctly using trusted data fields that cannot be manipulated by the end user, and the application and web server use this correct value for logging and security decisions such as rate limiting, taking into account that even the original IP address may not be reliable due to dynamic IPs, VPNs, or corporate firewalls. | 2 |
| **15.3.5** | Verify that the application explicitly ensures that variables are of the correct type and performs strict equality and comparator operations. This is to avoid type juggling or type confusion vulnerabilities caused by the application code making an assumption about a variable type. | 2 |
| **15.3.6** | Verify that JavaScript code is written in a way that prevents prototype pollution, for example, by using Set() or Map() instead of object literals. | 2 |
| **15.3.7** | Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (query string, body parameters, cookies, or header fields). | 2 |

## V15.4 Safe Concurrency

Concurrency issues such as race conditions, time-of-check to time-of-use (TOCTOU) vulnerabilities, deadlocks, livelocks, thread starvation, and improper synchronization can lead to unpredictable behavior and security risks. This section includes various techniques and strategies to help mitigate these risks.

| # | Description | Level |
| :---: | :--- | :---: |
| **15.4.1** | Verify that shared objects in multi-threaded code (such as caches, files, or in-memory objects accessed by multiple threads) are accessed safely by using thread-safe types and synchronization mechanisms like locks or semaphores to avoid race conditions and data corruption. | 3 |
| **15.4.2** | Verify that checks on a resource's state, such as its existence or permissions, and the actions that depend on them are performed as a single atomic operation to prevent time-of-check to time-of-use (TOCTOU) race conditions. For example, checking if a file exists before opening it, or verifying a user’s access before granting it. | 3 |
| **15.4.3** | Verify that locks are used consistently to avoid threads getting stuck, whether by waiting on each other or retrying endlessly, and that locking logic stays within the code responsible for managing the resource to ensure locks cannot be inadvertently or maliciously modified by external classes or code. | 3 |
| **15.4.4** | Verify that resource allocation policies prevent thread starvation by ensuring fair access to resources, such as by leveraging thread pools, allowing lower-priority threads to proceed within a reasonable timeframe. | 3 |

## References

For more information, see also:

* [OWASP Prototype Pollution Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [OWASP CycloneDX Bill of Materials Specification](https://owasp.org/www-project-cyclonedx/)
* [OWASP Web Security Testing Guide: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution)
