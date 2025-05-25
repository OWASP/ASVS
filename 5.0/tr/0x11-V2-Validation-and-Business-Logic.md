# V2 Doğrulama ve İş Mantığı

## Kontrol Amacı

Bu bölümün amacı, doğrulanan bir uygulamanın aşağıdaki üst düzey hedefleri karşıladığından emin olmaktır:

* Uygulamanın aldığı girdiler, işlevsel veya iş gereksinimleriyle uyumludur.
* İş mantığı akışı sıralıdır, sırayla işlenir ve atlanamaz.
* İş mantığı, sürekli küçük para transferleri veya her seferinde 1 tane olmak üzere 1 milyon arkadaş ekleme gibi otomatik saldırıları tespit edip engellemek için sınırlar ve kontroller içerir.
* Yüksek değerli iş mantığı akışları, kötüye kullanım senaryoları ve kötü niyetli aktörler göz önüne alınarak oluşturulmuştur ve kimlik sahteciliği, manipülasyon, bilgi sızıntısı ve yetki yükseltme saldırılarına karşı korumaya sahiptir.
 
## V2.1 Doğrulama ve İş Mantığı Dokümantasyonu

Doğrulama ve iş mantığı dokümantasyonu; iş mantığı sınırlarını, doğrulama kurallarını ve birleştirilmiş veri öğelerinin bağlamsal tutarlılığını açıkça tanımlamalıdır. Böylece uygulamada neyin uygulanması gerektiği net olur.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **2.1.1** | Uygulama dokümantasyonunda, veri öğelerinin beklenen yapıya göre nasıl doğrulanacağına ilişkin giriş doğrulama kurallarının tanımlandığı doğrulanmalıdır. Bu; kredi kartı numaraları, e-posta adresleri, telefon numaraları gibi yaygın veri biçimleri olabileceği gibi iç sistemlere özel biçimler de olabilir. | 1 | v5.0.be-1.11.5 |
| **2.1.2** | Uygulama dokümantasyonunda, birleştirilmiş veri öğelerinin mantıksal ve bağlamsal tutarlılığının nasıl doğrulanacağı tanımlanmalıdır (örneğin, mahalle ve posta kodunun eşleşip eşleşmediğinin kontrolü). | 2 | v5.0.be-1.11.6 |
| **2.1.3** | Hem kullanıcı bazında hem de uygulama genelinde geçerli olacak şekilde, iş mantığı sınırları ve doğrulama beklentilerinin belgelendiği doğrulanmalıdır. | 2 | v5.0.be-1.11.4 |


## V2.2 Girdi Doğrulama

Etkili girdi doğrulama kontrolleri, uygulamanın beklediği veri türüne yönelik işlevsel ya da iş gereksinimlerinin sağlanmasını zorunlu kılar. Bu sayede veri kalitesi artar ve saldırı yüzeyi daraltılır. Ancak bu, verinin başka bileşenlerde kullanılmadan veya çıktıya aktarılmadan önce doğru şekilde kodlanması, parametreleştirilmesi ya da temizlenmesi ihtiyacını ortadan kaldırmaz.

Bu bağlamda "girdi"; HTML form alanları, REST istekleri, URL parametreleri, HTTP başlıkları, çerezler, disk dosyaları, veritabanları veya harici API'lerden gelebilir.

Bir iş mantığı kontrolü, belirli bir girdinin 100'den küçük bir sayı olup olmadığını kontrol edebilir. Bir işlevsel beklenti ise bu sayının belirli bir eşiğin altında olmasını isteyebilir, çünkü bu sayı örneğin bir döngünün kaç kez çalışacağını belirliyor olabilir; büyük bir değer, aşırı işlemeye ve hizmet reddi (DoS) durumuna yol açabilir.

Şema doğrulaması zorunlu tutulmamış olsa da, HTTP API'leri veya JSON/XML kullanan diğer arayüzlerin tamamen doğrulanması için en etkili yöntem olabilir.

Şema doğrulamasıyla ilgili aşağıdaki hususlara dikkat edilmelidir:

* JSON Schema doğrulama standardının “yayınlanmış sürümü” üretime hazır kabul edilmekte ancak “stabil” değildir. Kullanıldığında, aşağıdaki gereksinimlerle çelişmediğinden emin olunmalıdır.
* Kullanılan JSON Schema kütüphaneleri, standart resmileştiğinde izlenmeli ve gerekirse güncellenmelidir.
* DTD'lere karşı yapılan XXE saldırılarını önlemek için DTD doğrulaması kullanılmamalı ve çerçeve içindeki DTD işleme özellikleri devre dışı bırakılmalıdır.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **2.2.1** | Girdilerin, işlevsel ya da iş gereksinimlerine uygunluğunun doğrulandığı teyit edilmelidir. Bu işlem; izinli değerler, desenler ve aralıklar listesine karşı pozitif doğrulama ile ya da girdinin beklenen yapıya ve mantıksal sınırlara uygunluğunun önceden tanımlanmış kurallara göre karşılaştırılması ile yapılmalıdır. Seviye 1 için bu, güvenlik veya iş kararlarında kullanılan girdilere odaklanabilir. Seviye 2 ve üstü için tüm girdilere uygulanmalıdır. | 1 | v5.0.be-11.3.1 |
| **2.2.2** | Uygulamanın, güvenilir bir servis katmanında girdi doğrulama zorunluluğu uygulayacak şekilde tasarlandığı doğrulanmalıdır. İstemci tarafında gerçekleştirilen doğrulama, kullanılabilirliği artırabilir ve teşvik edilmelidir. Ancak bu doğrulama,güvenlik kontrolü olarak kabul edilmemelidir. | 1 | v5.0.be-11.3.2 |
| **2.2.3** | Uygulamanın, ilişkili veri öğelerinin önceden tanımlanmış kurallara göre makul olup olmadığını kontrol ettiği doğrulanmalıdır. | 2 | v5.0.be-11.3.3 |

## V2.3 İş Mantığı Güvenliği

Bu bölüm, uygulamanın iş mantığı süreçlerini doğru şekilde yürüttüğünden ve bu mantık ve akışın istismarına karşı savunmasız olmadığından emin olunması için temel gereksinimleri kapsar.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **2.3.1** | Uygulamanın, aynı kullanıcı için iş mantığı akışlarını yalnızca beklenen adım sırasına göre ve adım atlamadan işlediği doğrulanmalıdır. | 1 | v5.0.be-11.1.1 |
| **2.3.2** | İş mantığı sınırlarının, uygulama dokümantasyonuna uygun şekilde uygulandığı doğrulanmalıdır. | 2 | v5.0.be-11.1.3 |
| **2.3.3** | İş mantığı seviyesinde işlemlerin (transaction) kullanıldığı ve bir iş mantığı işleminin ya bütünüyle başarıyla tamamlandığı ya da önceki geçerli duruma geri döndürüldüğü (rollback) doğrulanmalıdır. | 2 | v5.0.be-11.1.9 |
| **2.3.4** | İş mantığı düzeyinde kilitleme mekanizmalarının, sınırlı kaynakların (ör. sinema koltukları, teslimat zamanları) uygulamanın mantığı manipüle edilerek çift rezervasyona neden olmamasını sağladığı doğrulanmalıdır. | 2 | v5.0.be-11.1.11 |
| **2.3.5** | Yüksek değerli iş mantığı akışlarının, yetkisiz veya kazara gerçekleşebilecek işlemleri önlemek için çoklu kullanıcı onayı gerektirdiği doğrulanmalıdır. Bu işlemler büyük para transferleri, sözleşme onayları, gizli bilgilere erişim veya üretimde güvenlik kurallarının geçersiz kılınmaları gibi durumları içerebilir. | 3 | v5.0.be-11.1.10 |


## V2.4 Otomasyon Karşıtı Önlemler

Bu bölümde, insan benzeri etkileşimlerin zorunlu kılındığı ve aşırı miktardaki otomatik taleplerin engellendiği kontroller yer alır.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **2.4.1** | Uygulama işlevlerine yönelik aşırı miktardaki çağrılara karşı; veri sızdırma, anlamsız veri üretme, kota tüketme, hız sınırının aşılması, hizmet reddi (DoS) ya da maliyetli kaynakların aşırı kullanımı gibi risklere karşı otomasyon karşıtı kontrollerin bulunduğu doğrulanmalıdır. | 2 | v5.0.be-11.2.2 |
| **2.4.2** | İş mantığı akışlarının, aşırı hızlı işlem gönderimlerini önleyecek şekilde gerçekçi insan zamanlaması gerektirdiği doğrulanmalıdır. | 3 | v5.0.be-11.2.1 |


## Referanslar

Daha fazla bilgi için:

* [OWASP Web Security Testing Guide 4.2: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Web Security Testing Guide 4.2: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README)
* Anti-automation can be achieved in many ways, including the use of the [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [JSON Schema](https://json-schema.org/specification.html)
