# V16 Güvenlik Günlüklemesi (Logging) ve Hata Yönetimi

## Kontrol Amacı

Güvenlik logları hata ya da performans loglarından farklı olarak kimlik doğrulama kararları, erişim kontrol kararları ve giriş doğrulama ya da iş mantığı doğrulama gibi güvenlik kontrollerini aşma girişimleri gibi güvenlikle ilgili olayları kaydetmek için kullanılır. Bu logların amacı tespit, müdahale ve inceleme süreçlerini desteklemek için SIEM gibi analiz araçlarına uygun, yüksek sinyalli ve yapılandırılmış veri sağlamaktır.

Loglar, yasal bir zorunluluk olmadıkça hassas kişisel verileri içermemeli ve kaydedilen tüm veriler yüksek değerli birer varlık olarak korunmalıdır. Loglama işlemleri gizliliği veya sistem güvenliğini tehlikeye atmamalıdır. Uygulamalar ayrıca, hata durumlarında gereksiz bilgi sızdırma veya kesinti olmaksızın güvenli şekilde başarısız olmalıdır.

Detaylı uygulama rehberliği için referanslar bölümündeki OWASP Cheat Sheet dökümanlarına başvurulabilir.

## V16.1 Güvenlik Loglaması Dokümantasyonu

Bu bölüm, uygulama katmanları genelinde gerçekleştirilen loglamanın açık ve eksiksiz bir envanterini oluşturmayı amaçlar. Bu, etkili güvenlik izleme, olay müdahalesi ve uyumluluk için gereklidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **16.1.1** | Uygulamanın teknoloji yığını boyunca her katmanda hangi olayların loglandığını, log formatlarını, logların nereye yazıldığını, nasıl kullanıldığını, erişimin nasıl kontrol edildiğini ve logların ne kadar süre saklandığını belgeleyen bir envanterin mevcut olduğu doğrulanmalıdır. | 2 |

## V16.2 Genel Loglama

Bu bölüm, güvenlik loglarının tutarlı şekilde yapılandırılmasını ve beklenen meta verileri içermesini sağlamaya yönelik gereksinimleri kapsar. Amaç, logların makine tarafından okunabilir ve dağıtık sistemler ile araçlarda analiz edilebilir olmasını sağlamaktır.

Güvenlik olayları çoğunlukla hassas veriler içerir. Bu tür verilerin dikkatsizce kaydedilmesi durumunda, loglar da hassas veri niteliği kazanır ve bu da şifreleme zorunluluğu, daha sıkı saklama politikaları ve denetimlerde açıklanma riski gibi sonuçlara yol açar.

Bu nedenle yalnızca gerekli verilerin loglanması ve log verilerinin diğer hassas varlıklar gibi korunması kritik önemdedir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **16.2.1** | Her bir log girdisinin, olayın ne zaman, nerede, kim tarafından ve ne olduğuna dair detaylı bir zaman çizelgesi oluşturulmasına olanak tanıyacak gerekli meta verileri içerdiği doğrulanmalıdır. | 2 |
| **16.2.2** | Tüm loglama bileşenlerinin zaman kaynaklarının senkronize olduğu ve güvenlik olayı meta verisindeki zaman damgalarının UTC kullanarak ya da açık zaman dilimi ofsetiyle belirtildiği doğrulanmalıdır. UTC kullanımı, özellikle yaz saati uygulamaları nedeniyle oluşabilecek karışıklıkları önlemek için tavsiye edilir. | 2 |
| **16.2.3** | Uygulamanın yalnızca log envanterinde belgelenmiş dosya ve hizmetlere log yazdığı ya da ilettiği doğrulanmalıdır. | 2 |
| **16.2.4** | Logların kullanılan log işleyici (log processor) tarafından okunabildiği ve ilişkilendirilebildiği doğrulanmalıdır. Tercihen yaygın bir log formatı kullanılmalıdır. | 2 |
| **16.2.5** | Hassas veriler loglanırken, uygulamanın veri koruma seviyesine uygun olarak loglama yaptığı doğrulanmalıdır. Örneğin kimlik bilgileri veya ödeme detayları gibi bazı verilerin loglanmasına izin verilmemelidir. Session token’ları gibi veriler ise yalnızca tamamen ya da kısmen maskelenmiş ya da hash’lenmiş olarak loglanmalıdır. | 2 |

## V16.3 Güvenlik Olayları

Bu bölüm, uygulama içerisinde güvenlikle ilgili olayların loglanmasına dair gereksinimleri tanımlar. Bu olayların yakalanması şüpheli davranışların tespiti, olay incelemelerinin desteklenmesi ve uyumluluk yükümlülüklerinin yerine getirilmesi açısından kritiktir.

Buradaki olay türleri örnek niteliğindedir. Her uygulama, kendine özgü risk faktörleri ve operasyonel bağlama sahiptir.

Not: ASVS, güvenlik olaylarının loglanmasını kapsam içine alır. Ancak SIEM kuralları veya izleme altyapısı gibi uyarı ve korelasyon sistemleri kapsam dışıdır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **16.3.1** | Tüm kimlik doğrulama işlemlerinin (başarılı ve başarısız girişimler dahil) loglandığı doğrulanmalıdır. Kullanılan kimlik doğrulama türü veya faktörleri gibi ek meta veriler de toplanmalıdır. | 2 |
| **16.3.2** | Başarısız yetkilendirme girişimlerinin loglandığı doğrulanmalıdır. Seviye 3 uygulamalar için, tüm yetkilendirme kararlarının ve hassas verilere erişim olaylarının (verinin kendisi olmadan) loglandığı da doğrulanmalıdır. | 2 |
| **16.3.3** | Uygulamanın, belgelenmiş güvenlik olaylarını ve güvenlik kontrollerini aşma girişimlerini (girdi doğrulama, iş mantığı, otomasyon karşıtı kontroller vb.) logladığı doğrulanmalıdır. | 2 |
| **16.3.4** | Beklenmeyen hatalar ve güvenlik kontrolü başarısızlıkları (örneğin backend TLS hataları gibi) loglandığı doğrulanmalıdır. | 2 |

## V16.4 Log Koruması

Loglar, olay incelemeleri ve adli analizler için değerli kanıtlardır ve korunmaları gerekir. Kolayca silinebilen ya da değiştirilebilen loglar güvenilirliğini kaybeder. Ayrıca loglar, uygulamanın iç davranışları veya hassas meta veriler hakkında bilgi barındırabileceğinden saldırganlar için cazip hedeflerdir.

Bu bölüm, logların yetkisiz erişimden, değiştirilmeden ve açıklanmaktan korunmasını ve güvenli, izole sistemlere aktarılmasını sağlamaya yönelik gereksinimleri tanımlar.

| # | Description | Level |
| :---: | :--- | :---: |
| **16.4.1** | Tüm loglama bileşenlerinin, log enjeksiyonunu (log injection) önlemek amacıyla verileri uygun biçimde encode ettiği doğrulanmalıdır. | 2 |
| **16.4.2** | Logların yetkisiz erişime karşı korunduğu ve değiştirilemez olduğu doğrulanmalıdır. | 2 |
| **16.4.3** | Logların analiz, tespit, uyarı ve yükseltme amacıyla mantıksal olarak ayrı bir sisteme güvenli biçimde iletildiği doğrulanmalıdır. Böylece uygulama ihlal edilse bile logların tehlikeye girmesi önlenmiş olur. | 2 |

## V16.5 Hata Yönetimi

Bu bölüm, uygulamaların beklenmedik durumlarda güvenli şekilde başarısız olmasını ve hassas içsel detayları açıklamamasını sağlamak için gerekli gereksinimleri tanımlar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **16.5.1** | Beklenmedik ya da güvenlikle ilgili bir hata oluştuğunda, tüketiciye genel bir mesaj döndürüldüğü ve yığın izleri (stack trace), sorgular, gizli anahtarlar, token’lar gibi hassas sistem içi verilerin açıklanmadığı doğrulanmalıdır. | 2 |
| **16.5.2** | Uygulamanın, dış kaynaklara erişim başarısız olduğunda bile güvenli şekilde çalışmaya devam ettiği doğrulanmalıdır. Örneğin, circuit breaker ya da graceful degradation gibi desenler kullanılmalıdır. | 2 |
| **16.5.3** | Uygulamanın hata durumlarında güvenli ve düzenli şekilde başarısız olduğu doğrulanmalıdır. Bu, örneğin doğrulama hatalarına rağmen işlemlerin işlenmesine yol açabilecek fail-open durumlarını önlemelidir. | 2 |
| **16.5.4** | Ele alınmamış tüm istisnaları yakalayacak şekilde tanımlanmış bir “son çare hata yöneticisi” bulunduğu doğrulanmalıdır. Bu, hem loglara gitmesi gereken hata detaylarının kaybolmaması hem de tüm uygulama sürecinin çökerek hizmet dışı kalmasının önlenmesi açısından önemlidir. | 3 |

Not: Swift, Go ve birçok fonksiyonel dilde olduğu gibi bazı diller, istisnaları veya “son çare” hata yöneticilerini desteklemez. Bu durumda, geliştiriciler uygulamanın beklenmeyen veya güvenlikle ilgili olayları güvenli şekilde ele almasını sağlamak için dile veya çerçeveye uygun desenler kullanmalıdır.

## Referanslar

Daha fazla bilgi için:

* [OWASP Web Security Testing Guide: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
* [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
* [OWASP Application Logging Vocabulary Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html)
