# V14 Veri Koruma

## Kontrol Amacı

Uygulamalar, tüm kullanım senaryolarını ve kullanıcı davranışlarını önceden öngöremez. Bu nedenle, istemci cihazlarda hassas verilere yetkisiz erişimi sınırlamak için kontroller uygulanmalıdır.

Bu bölüm, hangi verilerin korunması gerektiğini tanımlama, nasıl korunacağını belirleme ve uygulanması gereken özel mekanizmalar ile kaçınılması gereken hatalarla ilgili gereksinimleri içerir.

Veri koruma ile ilgili bir diğer husus da toplu veri çıkarımı, değiştirme veya aşırı kullanımdır. Her sistemin gereksinimleri muhtemelen çok farklı olacaktır; bu nedenle, neyin "anormal" olduğunun belirlenmesi tehdit modeli ve iş riski dikkate alınarak yapılmalıdır. ASVS perspektifinden bakıldığında, bu tür sorunların tespiti "Güvenlik Günlüğü Tutma ve Hata Yönetimi" bölümünde, sınırlamaların belirlenmesi ise "Doğrulama ve İş Mantığı" bölümünde ele alınmaktadır.

## V14.1 Veri Koruma Dokümantasyonu

Verilerin korunabilmesi için temel ön koşullardan biri, hangi verilerin hassas olarak kabul edilmesi gerektiğinin kategorize edilmesidir. Hassasiyetin birkaç farklı düzeyi olabilir ve her düzey için uygulanması gereken kontroller farklılık gösterebilir.

Verilerin saklanması, kullanımı ve iletimi konusunda uygulamaların uyması gereken çeşitli gizlilik düzenlemeleri ve yasalar bulunmaktadır. Bu bölüm artık bu tür yasal düzenlemeleri çoğaltmaya çalışmamakta, bunun yerine hassas verileri korumaya yönelik temel teknik hususlara odaklanmaktadır. Lütfen yerel yasa ve düzenlemelere başvurun ve gerektiğinde nitelikli bir gizlilik uzmanı veya avukata danışın.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **14.1.1** | Uygulama tarafından oluşturulan ve işlenen tüm hassas verilerin tanımlanıp, koruma seviyelerine göre sınıflandırıldığından emin olun. Bu, yalnızca kodlanmış (örneğin Base64 stringleri ya da JWT içindeki düz metin yükler gibi) ve bu nedenle kolayca çözülebilir verileri de içermelidir. Koruma seviyeleri, uygulamanın uymakla yükümlü olduğu veri koruma ve gizlilik düzenlemeleri ile standartlarını dikkate almalıdır. | 2 |
| **14.1.2** | Tüm hassas veri koruma seviyeleri için belgelenmiş bir koruma gereksinimleri seti tanımlandığından emin olun. Bu gereksinimler genel şifreleme, bütünlük doğrulama, saklama süresi, verinin nasıl günlüğe kaydedileceği, günlüklerdeki hassas verilere erişim kontrolleri, veritabanı düzeyinde şifreleme, gizlilik ve gizliliği artırıcı teknolojiler ile diğer gizlilik gereksinimlerini kapsamalıdır. | 2 |

## V14.2 Genel Veri Koruması

Bu bölüm, veri korumaya yönelik çeşitli pratik gereksinimleri içerir. Bunların çoğu, istenmeyen veri sızıntısı gibi belirli konulara yöneliktir. Ancak aynı zamanda her bir veri öğesi için gerekli olan koruma düzeyine göre koruma kontrollerinin uygulanmasına ilişkin genel bir gereksinim de bulunmaktadır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **14.2.1** | Hassas verilerin yalnızca HTTP message body veya header alanlarında sunucuya gönderildiği ve URL ile sorgu parametrelerinin, API anahtarı veya session token’ı gibi hassas bilgiler içermediği doğrulanmalıdır. | 1 |
| **14.2.2** | Hassas verilerin, yük dengeleyiciler ve uygulama önbellekleri gibi sunucu bileşenlerinde önbelleğe alınmasının engellendiği veya kullanım sonrası bu verilerin güvenli biçimde temizlendiği doğrulanmalıdır.	 | 2 |
| **14.2.3** | Uygulama kontrolü dışında veri toplanmasını engellemek için, tanımlanmış hassas verilerin, kullanıcı izleyicileri gibi güvensiz taraflara gönderilmediği doğrulanmalıdır. | 2 |
| **14.2.4** | Hassas verilere yönelik şifreleme, bütünlük doğrulama, veri saklama, loglama yöntemi, loglardaki erişim kontrolleri, gizlilik teknolojileri gibi kontrollerin, söz konusu verinin belgelenmiş koruma seviyesinde tanımlandığı şekilde uygulandığı doğrulanmalıdır. | 2 |
| **14.2.5** | Önbellekleme mekanizmalarının yalnızca belirli içerik türüne sahip yanıtları önbelleğe alacak şekilde yapılandırıldığı ve hassas, dinamik içeriklerin önbelleğe alınmadığı doğrulanmalıdır. Web sunucusu, mevcut olmayan bir dosya talebinde geçerli ama farklı bir dosya döndürmek yerine 404 veya 302 cevabı vermelidir. Bu, Web Cache Deception saldırılarını önlemeye yardımcı olur.	 | 3 |
| **14.2.6** | Uygulamanın yalnızca işlevsellik için gerekli olan asgari hassas veriyi döndürdüğü doğrulanmalıdır. Örneğin, kredi kartı numarasının yalnızca bazı rakamlarının döndürülmesi; tam numaranın döndürülmesi gerekiyorsa, kullanıcı arayüzünde gizlenmiş (maskelenmiş) şekilde sunulması gerekir, aksi kullanıcı özel olarak görüntülemek istemedikçe gösterilmemelidir. | 3 |
| **14.2.7** | Hassas bilgilerin, veri saklama sınıflandırmasına tabi tutulduğu, geçerliliğini yitirmiş veya artık gerekli olmayan verilerin belirlenmiş bir zaman çizelgesiyle ya da gerektiğinde otomatik olarak silindiği doğrulanmalıdır. | 3 |
| **14.2.8** | Kullanıcı tarafından yüklenen dosyaların meta verilerinden hassas bilgilerin çıkarıldığı veya bu bilgilerin yalnızca kullanıcıdan açık onay alındığında saklandığı doğrulanmalıdır. | 3 |

## V14.3 İstemci Tarafı Veri Koruması

Bu bölüm, uygulamanın istemci veya kullanıcı aracısı tarafında verilerin belirli yollarla sızmasını önlemeye yönelik gereksinimleri içerir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **14.3.1** | Kimliği doğrulanmış verilerin, istemci veya oturum sonlandığında istemci depolamasından (örneğin tarayıcı DOM’undan) temizlendiği doğrulanmalıdır. 'Clear-Site-Data' HTTP response header bu konuda yardımcı olabilir ancak istemci tarafı, sunucu bağlantısı mevcut olmadığında da temizlik işlemini yapabiliyor olmalıdır. | 1 |
| **14.3.2** | Uygulamanın, tarayıcılarda hassas verilerin önbelleğe alınmasını önlemek amacıyla yeterli anti-önbellekleme HTTP response header (örneğin Cache-Control: no-store) ayarladığı doğrulanmalıdır. | 2 |
| **14.3.3** | Tarayıcıda depolanan verilerin (örneğin localStorage, sessionStorage, IndexedDB veya çerezler) hassas veri içermediği, yalnızca session token’larının istisna olarak kabul edildiği doğrulanmalıdır. | 2 |

## Referanslar

Daha fazla bilgi için:

* [Güvenlik ve önbelleğe alma karşıtı header field'ları kontrol etmek için Security Headers web sitesini kullanmayı değerlendirebilirsiniz](https://securityheaders.com/)
* [Mozilla'nın önbelleğe alma karşıtı header'larla ilgili dokümantasyonu](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [Australian Privacy Principle 11 - Security of personal information](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-11-app-11-security-of-personal-information)
* [European Union General Data Protection Regulation (GDPR) overview](https://www.edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://www.edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
* ["Clear-Site-Data" header'ıyla ilgili bilgi](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data)
* [Web Cache Deception hakkında white paper](https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack-wp.pdf)
