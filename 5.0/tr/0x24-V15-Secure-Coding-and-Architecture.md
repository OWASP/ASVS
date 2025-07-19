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

## V15.3 Savunmacı Kodlama

Bu bölüm, belirli bir programlama dilinde güvensiz kodlama kalıplarının kullanılması sonucu oluşan tür oynama (type juggling), prototip zehirleme (prototype pollution) gibi güvenlik açıklarını kapsar. Bazıları tüm dillere uygun olmayabilirken, diğerleri dile özel düzeltmelere sahip olabilir ya da HTTP parametrelerinin işlenmesi gibi framework'e özgü davranışlarla ilişkilidir. Ayrıca uygulama güncellemelerinin kriptografik olarak doğrulanmamasıyla ilgili riskleri de ele alır.

Ayrıca, veri öğelerini temsil etmek için nesnelerin kullanılması ve bu nesnelerin dış API’ler üzerinden alınması ve döndürülmesi durumunda ortaya çıkan riskleri de dikkate alır. Bu durumda, uygulama kullanıcı girdileriyle değiştirilmemesi gereken alanların değiştirilememesini (kitlesel atama – mass assignment) sağlamalı ve hangi alanların döndürüldüğü konusunda seçici olmalıdır. Alan erişimi bir kullanıcının izinlerine bağlıysa, bu durum "Authorization" bölümündeki domain düzeyinde erişim kontrolü gereksinimi bağlamında değerlendirilmelidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **15.3.1** | Uygulamanın yalnızca gerekli alanların bir alt kümesini veri nesnesinden döndürdüğü doğrulanmalıdır. Örneğin, bazı alanlara kullanıcıların erişmemesi gerektiğinden tüm veri nesnesi döndürülmemelidir. | 1 |
| **15.3.2** | Uygulama backend'i harici URL’lere çağrı yaptığında, yalnızca amaçlanan işlevsellik söz konusuysa yönlendirmeleri takip edecek şekilde yapılandırıldığının doğrulanması gerekir. | 2 |
| **15.3.3** | Uygulamanın, kitlesel atama saldırılarına karşı, her bir controller ve eylem için izin verilen alanları sınırlandırarak savunmalar sağladığı doğrulanmalıdır. Örneğin, bir alan değeri, bu işlemde değiştirilmesi amaçlanmadıysa eklenememeli veya güncellenememelidir. | 2 |
| **15.3.4** | Tüm proxy ve ara katman bileşenlerinin kullanıcının orijinal IP adresini, uç kullanıcı tarafından değiştirilemeyecek güvenilir veri alanları kullanarak doğru şekilde ilettiği ve uygulamanın ve web sunucusunun bu doğru değeri, loglama ve hız sınırlama gibi güvenlik kararları için kullandığı doğrulanmalıdır. Ayrıca, orijinal IP adresinin bile dinamik IP'ler, VPN'ler veya kurumsal güvenlik duvarları nedeniyle güvenilir olmayabileceği dikkate alınmalıdır. | 2 |
| **15.3.5** | Uygulamanın değişkenlerin doğru türde olduğunu açıkça doğruladığı ve sıkı eşitlik ve karşılaştırma işlemleri kullandığı doğrulanmalıdır. Bu, değişken türüyle ilgili varsayımlardan kaynaklanan tür oynama (type juggling) veya tür karışıklığı (type confusion) güvenlik açıklarını önlemek içindir. | 2 |
| **15.3.6** | 	JavaScript kodunun prototip zehirleme (prototype pollution) saldırılarını önleyecek şekilde yazıldığı, örneğin, nesne literal’leri yerine Set() veya Map() gibi yapılar kullanıldığı doğrulanmalıdır. | 2 |
| **15.3.7** | Uygulamanın, özellikle framework'ün istek parametrelerinin kaynağı (sorgu dizgisi, gövde parametreleri, çerezler veya başlık alanları) arasında ayrım yapmadığı durumlarda, HTTP parametre kirliliği (HTTP parameter pollution) saldırılarına karşı savunmalar uyguladığı doğrulanmalıdır. | 2 |

## V15.4 Güvenli Eş Zamanlılık (Concurrency)

Yarış durumları (race condition), kontrol anından kullanım anına (TOCTOU - time-of-check to time-of-use) açıkları, deadlock, livelock, iş parçacığı (thread) açlığı ve hatalı senkronizasyon gibi eş zamanlılık sorunları, öngörülemeyen davranışlara ve güvenlik risklerine yol açabilir. Bu bölüm, bu riskleri azaltmaya yardımcı olacak çeşitli teknikleri ve stratejileri içerir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **15.4.1** | Çok iş parçacıklı kodda (örneğin cache'ler, dosyalar veya birden fazla iş parçacığı tarafından erişilen bellek içi nesneler gibi) paylaşılan nesnelere yalnızca thread-safe (iş parçacığı güvenli) türler ve kilitleme (lock) veya semaphore gibi senkronizasyon mekanizmaları kullanılarak erişildiği doğrulanmalıdır. Bu, yarış durumlarını ve veri bozulmasını önlemeye yöneliktir. | 3 |
| **15.4.2** | Bir kaynağın durumu üzerindeki kontroller (örneğin varlığı ya da izinleri gibi) ile bu kontrole bağlı eylemlerin tek bir atomik işlem olarak gerçekleştirildiği doğrulanmalıdır. Bu, TOCTOU (time-of-check to time-of-use) yarış durumlarını önlemeye yöneliktir. Bir dosyanın varlığının kontrol edilip ardından açılması veya bir kullanıcının erişiminin doğrulanıp ardından yetki verilmesi gibi işlemler buna örnektir. | 3 |
| **15.4.3** | Kilitlerin (locks) tutarlı biçimde kullanıldığı, iş parçacıklarının birbirini beklemesi ya da sonsuz döngüye girmesi (deadlock veya livelock) gibi durumların önlendiği doğrulanmalıdır. Ayrıca, kilitleme mantığı, kaynağı yöneten kod içinde kalmalı ve dış sınıflar veya dış kodlar tarafından istemeden veya kötü niyetli şekilde değiştirilememelidir. | 3 |
| **15.4.4** | Kaynak tahsis politikalarının, iş parçacığı açlığını önleyecek şekilde, kaynaklara adil erişimi sağladığı doğrulanmalıdır. Örneğin, thread pool (iş parçacığı havuzu) kullanımı, düşük öncelikli iş parçacıklarının da makul sürelerde çalışabilmesi için uygulanmalıdır. | 3 |

## Referanslar

Daha fazla bilgi için:

* [OWASP Prototype Pollution Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [OWASP CycloneDX Bill of Materials Specification](https://owasp.org/www-project-cyclonedx/)
* [OWASP Web Security Testing Guide: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution)
