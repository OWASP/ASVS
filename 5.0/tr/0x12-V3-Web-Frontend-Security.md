# V3 Web Ön Uç (Frontend) Güvenliği

## Kontrol Amacı

Bu kategori, bir web frontend'i üzerinden gerçekleştirilen saldırılara karşı koruma sağlamak amacıyla belirlenmiş gereksinimlere odaklanır. Bu gereksinimler, makineden makineye çözümler için geçerli değildir.

## V3.1 Web Frontend Güvenlik Dokümantasyonu

Bu bölüm, uygulamanın dokümantasyonunda belirtilmesi gereken tarayıcı güvenlik özelliklerini tanımlar.

| # | Açıklama | Seviye | 
| :---: | :---: | :---: |
| **3.1.1** | Uygulama dokümantasyonunda, uygulamayı kullanan tarayıcıların desteklemesi gereken güvenlik özelliklerinin (ör. HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP) ve diğer ilgili HTTP güvenlik mekanizmaları) tanımlandığı doğrulanmalıdır. Ayrıca bu özelliklerin mevcut olmadığı durumlarda uygulamanın nasıl davranması gerektiği (ör. kullanıcıyı uyarmak veya erişimi engellemek) de tanımlanmalıdır. | 3 |

## V3.2 İçeriğin Yanlış Yorumlanması

İçerik veya işlevin yanlış bir bağlamda sunulması, kötü amaçlı içeriğin çalıştırılmasına veya görüntülenmesine neden olabilir.

| # | Açıklama | Seviye | 
| :---: | :---: | :---: | 
| **3.2.1** | Tarayıcıların HTTP yanıtlarında içerik veya işlevi yanlış bir bağlamda sunmalarını önlemek amacıyla güvenlik kontrollerinin uygulandığı doğrulanmalıdır (ör. API, kullanıcı tarafından yüklenen dosya veya başka bir kaynağın doğrudan çağrılması durumunda). Olası kontroller arasında; yalnızca HTTP istek başlıklarının (ör. Sec-Fetch-\*) doğru bağlamı gösterdiği durumlarda içeriğin sunulması, Content-Security-Policy başlığında "sandbox" yönergesinin kullanılması veya Content-Disposition başlığında "attachment" biçiminin kullanılması yer alabilir. | 1 |
| **3.2.2** | HTML yerine metin olarak görüntülenmesi amaçlanan içeriğin, HTML veya JavaScript gibi içeriklerin istenmeden çalıştırılmasını önleyecek şekilde "createTextNode" veya "textContent" gibi güvenli işleme fonksiyonlarıyla işlendiği doğrulanmalıdır. | 1 |
| **3.2.3** | Uygulamanın istemci tarafı JavaScript kullanırken açık değişken tanımlamaları yaparak, sıkı tür kontrolü uygulayarak, global değişkenleri document nesnesine kaydetmekten kaçınarak ve ad alanı izolasyonu sağlayarak DOM clobbering’den kaçındığı doğrulanmalıdır. | 3 |

## V3.3 Çerez Yapılandırması

Bu bölüm, hassas çerezlerin güvenli biçimde yapılandırılması için gereksinimleri tanımlar. Amaç, çerezlerin gerçekten uygulama tarafından oluşturulduğuna dair daha yüksek düzeyde güvence sağlamak ve içeriklerinin sızmasını veya uygunsuz şekilde değiştirilmesini önlemektir.

| # | Açıklama | Seviye |
| :---: | :---: | :---: | 
| **3.3.1** | Çerezlerin 'Secure' niteliğine sahip olduğu ve eğer çerez adı '\__Host-' ön eki ile başlamıyorsa, '__Secure-' ön ekinin kullanıldığı doğrulanmalıdır. | 1 |
| **3.3.2** | Kullanıcı arayüzü kandırma saldırılarına ve tarayıcı tabanlı istek sahteciliği saldırılarına (CSRF) karşı koruma sağlamak amacıyla, her çerezin 'SameSite' niteliğinin kullanım amacına uygun şekilde ayarlandığı doğrulanmalıdır. | 2 | 
| **3.3.3** | Çerez adı, diğer sunucularla paylaşılmak üzere açıkça tasarlanmadığı sürece '__Host-' ön eki ile tanımlanmalıdır. | 2 | 
| **3.3.4** | Bir çerez değeri istemci tarafı betikleri tarafından erişilememesi gereken bir veri içeriyorsa (ör. oturum token'ı), çerezin 'HttpOnly' niteliğine sahip olduğu ve aynı değerin (ör. oturum token'ı) yalnızca 'Set-Cookie' başlığı ile istemciye iletildiği doğrulanmalıdır. | 2 |
| **3.3.5** | Uygulama bir çerez oluştururken, çerez adı ve değerinin toplam uzunluğunun 4096 baytı aşmadığı doğrulanmalıdır. Çok büyük çerezler tarayıcı tarafından saklanmaz ve isteklerle gönderilmez; bu da çereze bağlı çalışan uygulama işlevlerinin bozulmasına yol açabilir. | 3 |

## V3.4 Tarayıcı Güvenlik Mekanizması Başlıkları (Header)

Bu bölüm, tarayıcıların uygulamadan gelen yanıtları işlerken güvenlik özelliklerini etkinleştirmesi ve kısıtlamaları uygulaması için HTTP yanıtlarında hangi güvenlik header'larının ayarlanması gerektiğini açıklar.

| # | Açıklama | Seviye |
| :---: | :---: | :---: |
| **3.4.1**| Tüm yanıtların, HTTP Strict Transport Security (HSTS) politikasını zorunlu kılmak için Strict-Transport-Security header alanını içerdiği doğrulanmalıdır. En az 1 yıl süreli bir max-age tanımlanmalı ve Seviye 2 ve üzeri için bu politika tüm alt alan adlarını da kapsamalıdır. | 1 |
| **3.4.2** | Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header'ı, uygulama tarafından sabit bir değer olarak tanımlanmalı veya gelen Origin header değeri güvenilir origin’lerden oluşan bir izinli listeye karşı doğrulanmalıdır. ‘Access-Control-Allow-Origin: *’ kullanılması gerekiyorsa, yanıtın hassas bilgi içermediği doğrulanmalıdır. | 1 |
| **3.4.3** | HTTP yanıtlarında Content-Security-Policy header'ı bulunduğu ve bu header'ın yalnızca güvenilen içeriklerin veya kaynakların yüklenmesini ve çalıştırılmasını sağlayan yönergeler içerdiği doğrulanmalıdır. Minimum olarak "global policy", object-src 'none', base-uri 'none' yönergelerini içermeli ve izinli liste, nonce veya hash temelli bir yapı içermelidir. Seviye 3 uygulamalarında her yanıt için nonce veya hash içeren özel bir politika tanımlanmalıdır. | 2 |
| **3.4.4** | Tüm HTTP yanıtlarının 'X-Content-Type-Options: nosniff' header'ını içerdiği doğrulanmalıdır. Bu, tarayıcıya içerik türünü tahmin etmeyi bırakmasını ve yanıtın Content-Type header'ında belirtilen MIME türünün, beklenen kaynak türüyle eşleşmesini zorunlu kılar. Ayrıca bu, tarayıcıda CORB (Cross-Origin Read Blocking) özelliğini etkinleştirir. | 2 |
| **3.4.5** | Uygulamanın, 'Referer' başlığı yoluyla üçüncü taraflara teknik olarak hassas verilerin sızmasını önlemek için bir 'referrer policy' belirlediği doğrulanmalıdır. Bu, Referrer-Policy HTTP header'ıyla veya HTML öğe nitelikleriyle (element attributes) sağlanabilir. Sızabilecek hassas bilgiler, URL’deki yol ve sorgu parametreleri ile sınırlı uygulamalarda hostname bilgisini içerebilir. | 2 |
| **3.4.6** | Uygulamanın, Content-Security-Policy header'ı altında 'frame-ancestors' yönergesini her HTTP yanıtında tanımladığı ve bu sayede içeriklerin varsayılan olarak başka sayfalara gömülmesini engellediği doğrulanmalıdır. Gerekli durumlarda özel olarak izin verildiğinden emin olunmalıdır. 'X-Frame-Options' header'ı, tarayıcılar tarafından desteklenmesine rağmen, artık güncel değildir ve güvenlik amacıyla kullanılmamalıdır. | 2 |
| **3.4.7**| Content-Security-Policy header'ında ihlal bildirimlerinin gönderileceği bir adresin tanımlandığı doğrulanmalıdır. | 3 |
| **3.4.8** | Bir belgenin işlenmesini ve sunulmasını başlatan tüm HTTP yanıtlarında (örneğin 'text/html' tipi yanıtlar), 'Cross-Origin-Opener-Policy' header'ı 'same-origin' veya 'same-origin-allow-popups' yönergeleriyle birlikte yer almalıdır. Bu, tabnabbing ve frame counting gibi, pencere nesnelerine paylaşımlı erişimi sömüren saldırılara karşı koruma sağlar. | 3 |

## V3.5 Tarayıcı Menşei Ayırımı

Sunucu tarafında hassas işlevlere yönelik bir isteği kabul ederken, uygulamanın, isteğin uygulamanın kendisi veya güvenilir bir tarafça başlatıldığından ve bir saldırgan tarafından taklit edilmediğinden emin olması gerekir.

Bu bağlamda hassas işlevsellik, kimliği doğrulanmış ve doğrulanmamış kullanıcılar için form gönderilerinin kabul edilmesini (kimlik doğrulama isteği gibi), durum değiştirme işlemlerini veya kaynak gerektiren işlevselliği (veri dışa aktarma gibi) içerebilir.

Buradaki temel korumalar, JavaScript için Same Origin Policy ve çerezler için SameSite mantığı gibi tarayıcı güvenlik politikalarıdır. Bir diğer yaygın koruma ise CORS ön kontrol mekanizmasıdır. Bu mekanizma, farklı bir kaynaktan çağrılmak üzere tasarlanmış uç noktalar için kritik olacaktır, ancak farklı bir kaynaktan çağrılmak üzere tasarlanmamış uç noktalar için de yararlı bir istek sahteciliği önleme mekanizması olabilir.

| # | Açıklama | Seviye |
| :---: | :---: | :---: |
| **3.5.1** | Uygulama, hassas işlevselliğe yönelik izinsiz cross-origin istekleri önlemek için CORS preflight mekanizmasına güvenmiyorsa, bu tür isteklerin gerçekten uygulamadan geldiği doğrulanmalıdır. Bu, anti-forgery token kullanımı veya CORS tarafından güvenli kabul edilmeyen özel HTTP header'larının zorunlu kılınmasıyla yapılabilir. Bu, tarayıcı tabanlı istek sahteciliği (CSRF) saldırılarına karşı bir savunmadır. | 1 |
| **3.5.2** | Uygulama, hassas işlevlerin izinsiz cross-origin çağrılmasını önlemek için CORS preflight mekanizmasına güveniyorsa, bu işlevlerin bir CORS-preflight isteğini tetiklemeden çağrılamadığı doğrulanmalıdır. Bu, 'Origin' ve 'Content-Type' header'larının doğrulanmasını veya CORS-safelisted olmayan bir header'ın ve alanın kullanılmasını gerektirebilir. | 1 |
| **3.5.3**| Hassas işlevselliğe yönelik HTTP isteklerinin 'POST', 'PUT', 'PATCH' veya 'DELETE' gibi uygun HTTP yöntemlerini kullandığı ve HTTP spesifikasyonuna göre "güvenli" olan 'GET', 'OPTIONS' veya 'HEAD' gibi yöntemlerle çağrılamadığı doğrulanmalıdır. Alternatif olarak 'Sec-Fetch-*' header'larının sıkı şekilde doğrulanması da uygunsuz cross-origin, navigasyon veya medya yükleme isteklerini ayırt etmek için kullanılabilir. | 1 |
| **3.5.4** | Farklı uygulamaların farklı hostname'lerde barındırıldığı ve böylece Same-Origin Policy tarafından sağlanan kısıtlamalardan (örneğin çerez erişim sınırları, kaynaklar arası etkileşim kontrolleri) faydalanıldığı doğrulanmalıdır. | 2 |
| **3.5.5**| postMessage arayüzü üzerinden alınan iletilerin, mesajın kökeni güvenilir değilse veya mesaj sözdizimi geçersizse reddedildiği doğrulanmalıdır. | 2 |
| **3.5.6** | Uygulamanın herhangi bir yerinde JSONP işlevselliğinin etkin olmadığı doğrulanmalıdır. Bu, XSSI (Cross-Site Script Inclusion) saldırılarını önlemek içindir. | 3 |
| **3.5.7** | Yetkilendirme gerektiren verilerin, JavaScript dosyaları gibi betik kaynaklarının yanıtlarında yer almadığı, XSSI saldırılarını önlemek için doğrulanmalıdır. | 3 |
| **3.5.8** | Kimliği doğrulanmış kaynakların (örneğin görseller, videolar, betikler ve belgeler) yalnızca gerçekten amaçlandığında kullanıcı adına yüklenebildiği veya gömülebildiği doğrulanmalıdır. Bu, isteğin uygun olmayan bir çapraz kaynak çağrısından kaynaklanmadığından emin olmak için Sec-Fetch-* HTTP istek başlığı alanlarının sıkı bir şekilde doğrulanmasıyla veya tarayıcıya döndürülen içeriği engelleme talimatı vermek için kısıtlayıcı bir Cross-Origin-Resource-Policy HTTP yanıt başlığı alanı ayarlayarak gerçekleştirilebilir. | 3 |

## V3.6 Harici Kaynak Bütünlüğü

Bu bölüm, içeriklerin üçüncü taraf sitelerde güvenli şekilde barındırılmasıyla ilgili rehberlik sunar.

| # | Açıklama | Seviye |
| :---: | :---: | :---: |
| **3.6.1** | JavaScript kütüphaneleri, CSS veya web fontları gibi istemci tarafı varlıkların yalnızca statik ve sürümlü olması, varlığın bütünlüğünü doğrulamak için Subresource Integrity (SRI) kullanılması durumunda harici olarak (örneğin, bir İçerik Dağıtım Ağı üzerinde) barındırıldığı doğrulanmalıdır. Bu mümkün değilse, her bir kaynak için bunu gerekçelendiren belgelenmiş bir güvenlik kararı bulunmalıdır. | 3 |

## V3.7 Diğer Tarayıcı Güvenliği Hususları

Bu bölüm, istemci tarafı tarayıcı güvenliği için gerekli olan çeşitli diğer güvenlik kontrolleri ve modern tarayıcı güvenlik özelliklerini içerir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **3.7.1** | Uygulamanın yalnızca hâlâ desteklenen ve güvenli kabul edilen istemci tarafı teknolojileri kullandığı doğrulanmalıdır. Bu gereksinimi karşılamayan teknolojilere örnek olarak NSAPI eklentileri, Flash, Shockwave, ActiveX, Silverlight, NACL veya istemci tarafı Java applet’leri verilebilir. | 2 |
| **3.7.2** | Uygulamanın, yalnızca hedef adres bir izinli listede yer alıyorsa kullanıcıyı otomatik olarak farklı bir ana makine adına veya uygulamanın kontrolünde olmayan bir etki alanına yönlendirdiği doğrulanmalıdır. | 2 |
| **3.7.3** | Uygulamanın, kullanıcı uygulamanın kontrolü dışındaki bir URL’ye yönlendirildiğinde, yönlendirme hakkında bir bildirim gösterdiği ve kullanıcının bu gezintiyi iptal edebilmesi için bir seçenek sunduğu doğrulanmalıdır. | 3 |
| **3.7.4** | Uygulamanın en üst düzey etki alanının (örneğin, site.tld) HTTP Strict Transport Security (HSTS) için genel preload listesine eklendiği doğrulanmalıdır. Bu, uygulamanın TLS kullanımının ana tarayıcılar tarafından doğrudan tanınmasını ve yalnızca Strict-Transport-Security yanıt header'ına bağlı kalınmamasını sağlar. | 3 |
| **3.7.5** | Uygulamaya erişen tarayıcının beklenen güvenlik özelliklerini desteklememesi durumunda, uygulamanın dokümantasyona uygun şekilde davrandığı (örneğin kullanıcıyı uyarma veya erişimi engelleme) doğrulanmalıdır. | 3 |

## Referanslar

Daha fazla bilgi için:

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [Sandboxing third-party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)