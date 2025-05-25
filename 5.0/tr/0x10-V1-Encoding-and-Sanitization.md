# V1 Kodlama (Encoding) ve Temizleme

## Kontrol Amacı

Bu bölüm, güvenilmeyen verilerin güvensiz işlenmesiyle ilişkili en yaygın web uygulaması güvenlik zayıflıklarına odaklanır. Bu tür durumlar, güvenilmeyen verinin ilgili yorumlayıcının sözdizimi kuralları çerçevesinde yanlış şekilde yorumlanmasına neden olan çeşitli teknik güvenlik açıklarına yol açar.

Modern web uygulamalarında, parametreli sorgular, otomatik kaçış (escaping) veya şablonlama (templating) çerçeveleri gibi daha güvenli API'lerin kullanımı her zaman en iyi yaklaşımdır. Aksi takdirde ya da bu mümkün değilse, çıktı kodlaması, kaçış veya temizleme işlemlerinin dikkatle uygulanması uygulamanın güvenliği için kritik öneme sahiptir.

Girdi doğrulama, beklenmeyen ve tehlikeli içeriklere karşı savunma derinliği mekanizması olarak kullanılabilir. Ancak asıl amacı gelen verinin işlevsel ve iş gereksinimleriyle uyumlu olup olmadığını kontrol etmektir. Bu nedenle, bu konudaki gereksinimler "Doğrulama ve İş Mantığı" bölümünde ele alınmıştır.

## V1.1 Kodlama ve Temizleme Mimarisi

Aşağıdaki bölümlerde, güvenli olmayan içeriklerin güvenli şekilde işlenmesine yönelik, sözdizimi veya yorumlayıcıya özel güvenlik gereksinimleri sunulmaktadır. Bu bölümdeki gereksinimler, bu işlemlerin hangi sırayla ve nerede gerçekleştirilmesi gerektiğini kapsar. Ayrıca, verilerin saklandığı her durumda orijinal (ham) haliyle saklanması gerektiğini (örneğin HTML kodlaması gibi kodlanmış/kaçırılmış biçimde değil) vurgular. Bu sayede çift kodlama (double encoding) gibi sorunlar önlenmiş olur.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.1.1** | Girdinin yalnızca bir kez kanonik forma (canonical form) çözümlendiği veya kaçış işlemlerinin kaldırıldığı, bu işlemin yalnızca verinin bu biçimde beklenmesi durumunda yapıldığı ve bu işlemin girdi doğrulama veya temizleme işlemlerinden sonra değil, önce gerçekleştiği doğrulanmalıdır. | 2 | v5.0.be-5.6.1 |
| **1.1.2** | Uygulamanın, çıktıyı kullanılması gereken yorumlayıcıya verilmeden hemen önce veya yorumlayıcının kendisi tarafından çıktı kodlaması ya da kaçış işlemi yaptığı doğrulanmalıdır. | 2 | v5.0.be-5.6.2 |

## V1.2 Enjeksiyon Önleme

Potansiyel olarak tehlikeli içeriklerin yakınında yapılan çıktı kodlama veya kaçış işlemleri, uygulama güvenliği için kritiktir. Genellikle çıktı kodlama ve kaçış işlemleri kalıcı değildir. Yalnızca verinin anlık olarak yorumlayıcı tarafından güvenli şekilde işlenebilmesi için uygulanır. Bu işlemin çok erken yapılması, içeriğin bozulmasına veya etkisiz hale gelmesine neden olabilir.

Çoğu durumda, yazılım kütüphaneleri bu işlemleri otomatik olarak gerçekleştiren güvenli veya daha güvenli işlevler sağlar. Ancak, bu işlevlerin geçerli bağlama uygun olduğundan emin olunmalıdır.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.2.1** | HTTP yanıtı, HTML veya XML belgesi için yapılan çıktı kodlamasının; HTML elemanları, HTML öznitelikleri, HTML yorumları, CSS ya da HTTP başlık alanları gibi bağlamlara uygun olduğu doğrulanmalıdır. Böylece mesaj veya belge yapısının bozulması önlenir. | 1 | v5.0.be-5.3.1 |
| **1.2.2** | 	Dinamik olarak URL oluşturulurken, güvenilmeyen verinin bağlamına göre (örneğin, sorgu veya yol parametreleri için URL kodlaması ya da base64url kodlaması) kodlandığı doğrulanmalıdır. Yalnızca güvenli URL protokollerine izin verilmelidir (örneğin, javascript: veya data: yasaklanmalıdır). | 1 | v5.0.be-5.3.13 |
| **1.2.3** |JavaScript içeriği (JSON dahil) dinamik olarak oluşturulurken çıktı kodlama/kaçış kullanıldığı doğrulanmalıdır. Böylece mesaj veya belge yapısı değiştirilmemiş olur (JavaScript ve JSON enjeksiyonlarının önüne geçilir). | 1 | v5.0.be-5.3.3 |
| **1.2.4** | Veri sorguları veya veritabanı sorguları (SQL, HQL, NoSQL, Cypher vb.) için parametreli sorgular, ORM’ler, entity framework’ler kullanıldığı ya da SQL enjeksiyonu ve diğer veritabanı enjeksiyon saldırılarına karşı koruma sağlandığı doğrulanmalıdır. Bu durum, saklı yordam (stored procedure) yazarken de geçerlidir. | 1 | v5.0.be-5.3.4 |
| **1.2.5** | Uygulamanın işletim sistemi komut enjeksiyonlarına karşı korunduğu ve işletim sistemi çağrılarında parametreli OS sorguları veya bağlama özgü komut satırı çıktı kodlamasının kullanıldığı doğrulanmalıdır. | 1 | v5.0.be-5.3.8 |
| **1.2.6** | Uygulamanın LDAP enjeksiyon zafiyetlerine karşı korunduğu ya da LDAP enjeksiyonlarını önlemek için özel güvenlik kontrollerinin uygulandığı doğrulanmalıdır. | 2 | v5.0.be-5.3.7 |
| **1.2.7** | XPath enjeksiyon saldırılarına karşı, sorgu parametrelemesi veya önceden derlenmiş sorgular kullanılarak koruma sağlandığı doğrulanmalıdır. | 2 | v5.0.be-5.3.10 |
| **1.2.8** | LaTeX işlemcilerinin güvenli şekilde yapılandırıldığı (örneğin, --shell-escape bayrağının kullanılmadığı) ve yalnızca izin verilen komutlardan oluşan bir listeyle çalıştırıldığı doğrulanmalıdır. | 2 | v5.0.be-5.3.12 |
| **1.2.9** | Düzenli ifadelerde (regex) özel karakterlerin (genellikle ters eğik çizgi \ ile) kaçırılarak meta karakter olarak yorumlanmalarının önlendiği doğrulanmalıdır. | 2 | v5.0.be-5.2.9 |
| **1.2.10** | Uygulamanın CSV ve formül enjeksiyonlarına karşı korunduğu doğrulanmalıdır. Uygulama, CSV içeriği dışa aktarırken RFC 4180 Bölüm 2.6 ve 2.7'de tanımlanan kaçış kurallarına uymalıdır. Ayrıca, CSV veya diğer tablo formatlarına (XLS, XLSX, ODF gibi) aktarım yapılırken, alanın ilk karakteri olarak çıkan özel karakterler ('=', '+', '-', '@', '\t' (sekme), '\0' (null karakter)) tek tırnak (') ile kaçırılmalıdır.

Not: Parametreli sorguların veya SQL kaçışlarının kullanılması her zaman yeterli değildir. Örneğin, tablo ve sütun adları (özellikle “ORDER BY” gibi) kaçırılamaz. Bu alanlarda kullanıcı tarafından sağlanan veriler kaçırılmış olarak dahil edilirse sorgular başarısız olur veya SQL enjeksiyonuna neden olabilir.

## V1.3 Temizleme (Sanitization)

Güvenilmeyen içeriğin güvensiz bir bağlamda kullanılmasına karşı ideal koruma yöntemi, önceki bölümde detaylı olarak açıklandığı gibi, bağlama özel kodlama veya kaçıştırma (escaping) kullanmaktır. Bu yöntem, içeriğin anlamını koruyarak güvenli hale getirir.

Bu mümkün olmadığında, potansiyel olarak tehlikeli karakterlerin veya içeriğin temizlenmesi (sanitize) gerekir. Bazı durumlarda, bu işlem girdinin anlamını değiştirebilir; ancak güvenlik açısından başka bir seçenek olmayabilir.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.3.1** | WYSIWYG editörlerinden veya benzer kaynaklardan gelen tüm güvenilmeyen HTML girdilerinin, bilinen ve güvenli bir HTML temizleme kütüphanesi ya da çerçeve özelliği ile temizlendiği doğrulanmalıdır. | 1 | v5.0.be-5.2.1 |
| **1.3.2** | Uygulamanın eval() veya Spring Expression Language (SpEL) gibi dinamik kod çalıştırma özelliklerini kullanmaktan kaçındığı doğrulanmalıdır. Alternatif yoksa, kullanıcı girdisi çalıştırılmadan önce mutlaka temizlenmelidir. | 1 | v5.0.be-5.2.4 |
| **1.3.3** | Potansiyel olarak tehlikeli bir bağlamda kullanılacak verilerin, bu bağlama uygun karakterlere izin vermek ve çok uzun girdileri kısaltmak gibi güvenlik önlemleriyle önceden temizlendiği doğrulanmalıdır. | 2 | v5.0.be-5.2.2 |
| **1.3.4** | Kullanıcı tarafından sağlanan SVG içeriğinin, yalnızca güvenli etiket ve özellikler (örneğin grafik çizme ile ilgili) içerdiğinden emin olmak için onaylandığı veya temizlendiği doğrulanmalıdır (ör. script veya foreignObject içermemelidir). | 2 | v5.0.be-5.2.7 |
| **1.3.5** | Markdown, CSS, XSL stil sayfaları, BBCode veya benzeri ifade şablon dillerinde kullanıcı girdisinin temizlendiği veya bu tür özelliklerin devre dışı bırakıldığı doğrulanmalıdır. | 2 | v5.0.be-5.2.8 |
| **1.3.6** | Uygulamanın, güvenilmeyen verileri başka servislere iletmeden önce izinli protokol, alan adı, yol ve port listelerine göre doğruladığı ve tehlikeli karakterleri temizlediği doğrulanarak SSRF (Sunucu Taraflı İstek Sahteciliği) saldırılarına karşı korunduğu doğrulanmalıdır. | 2 | v5.0.be-5.2.6 |
| **1.3.7** | Uygulamanın şablon enjeksiyon saldırılarına karşı, güvenilmeyen girdilere dayalı şablon oluşturmayı engellediği; eğer bu kaçınılmazsa, bu girdilerin mutlaka temizlendiği veya sıkı şekilde onaylandığı doğrulanmalıdır. | 2 | v5.0.be-5.2.5 |
| **1.3.8** | JNDI sorgularında kullanılmadan önce güvenilmeyen girdilerin temizlendiği ve JNDI'nin enjeksiyonlara karşı güvenli şekilde yapılandırıldığı doğrulanmalıdır. | 2 | v5.0.be-5.2.11 |
| **1.3.9** | Memcache’e gönderilmeden önce içeriğin temizlenerek enjeksiyon saldırılarına karşı korunduğu doğrulanmalıdır. | 2 | v5.0.be-5.2.12 |
| **1.3.10** | 	Format dizgilerinin (format strings) beklenmeyen veya zararlı şekilde çözümlenmesini önlemek için işlenmeden önce temizlendiği doğrulanmalıdır. | 2 | v5.0.be-5.2.13 |
| **1.3.11** | SMTP veya IMAP enjeksiyonlarını önlemek için, kullanıcı girdisinin posta sistemlerine iletilmeden önce temizlendiği doğrulanmalıdır. | 2 | v5.0.be-5.2.3 |
| **1.3.12** | Regex girdilerinin üstel geri izlemeye (exponential backtracking) neden olan öğeler içermediği ve güvenilmeyen girdilerin ReDoS (Regex Denial of Service) gibi saldırılara karşı temizlendiği doğrulanmalıdır. | 3 | v5.0.be-5.2.10 |

## V1.4 Bellek, Dizgi ve Yönetilmeyen Kod

Aşağıdaki gereksinimler, sistem programlama dilleri veya yönetilmeyen kod kullanan uygulamalarda görülen güvensiz bellek kullanımıyla ilişkili riskleri ele alır.

Bazı durumlarda, taşma korumaları ve uyarılar, yığın (stack) rastgeleleştirme ve veri yürütme engelleme gibi önlemleri etkinleştiren derleyici bayrakları (compiler flags) kullanılarak bu risklerin önüne geçilebilir. Ayrıca, tehlikeli işaretçi, bellek, format dizgisi, tamsayı ve dizgi işlemleri tespit edildiğinde derlemenin başarısız olmasını sağlayan ayarlar tercih edilmelidir.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.4.1** | Yığın, arabellek (buffer) veya yığın belleği taşmalarını önlemek ya da tespit etmek amacıyla, bellek güvenli dizgi işlemlerinin, daha güvenli bellek kopyalama ve işaretçi aritmetiğinin kullanıldığı doğrulanmalıdır. | 2 | v5.0.be-5.4.1 |
| **1.4.2** | Tamsayı taşmalarını önlemek için işaret (sign), aralık (range) ve giriş doğrulama tekniklerinin kullanıldığı doğrulanmalıdır. | 2 | v5.0.be-5.4.3 |
| **1.4.3** | Dinamik olarak ayrılan belleğin ve kaynakların serbest bırakıldığı ve boşaltılan belleklere ait referansların veya işaretçilerin kaldırıldığı veya null yapıldığı doğrulanmalıdır (dangling pointer ve use-after-free zafiyetlerine karşı). | 2 | v5.0.be-5.4.4 |

## V1.5 Güvenli Ters Serileştirme (Safe Deserialization)

Verilerin saklanmış veya iletilmiş bir temsilinden uygulama nesnelerine dönüştürülmesi işlemi olan ters serileştirme, geçmişte çeşitli kod enjeksiyonu zafiyetlerinin kaynağı olmuştur. Bu işlemin dikkatli ve güvenli bir şekilde yapılması, bu tür güvenlik açıklarının önlenmesi açısından son derece önemlidir.

Özellikle, bazı ters serileştirme yöntemleri, kullanılan programlama dili veya çerçevenin dokümantasyonunda güvensiz olarak tanımlanmıştır ve güvenilmeyen verilerle kullanıldığında güvenli hâle getirilemez. Kullanılan her yöntem için dikkatli bir inceleme yapılmalıdır.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.5.1** | XML ayrıştırıcılarının (parser) kısıtlayıcı şekilde yapılandırıldığı ve dış varlık çözümleme (external entity resolution) gibi güvensiz özelliklerin XXE (XML eXternal Entity) saldırılarına karşı devre dışı bırakıldığı doğrulanmalıdır . | 1 | v5.0.be-5.5.2 |
| **1.5.2** | Güvenilmeyen verilerin ters serileştirilmesinde, nesne türleri için izinli liste kullanımı veya istemci tanımlı nesne türlerinin kısıtlanması gibi güvenli giriş işleme önlemlerinin uygulandığı doğrulanmalıdır. Güvensiz olarak tanımlanmış ters serileştirme mekanizmaları, güvenilmeyen girdilerle kullanılmamalıdır. | 2 | v5.0.be-5.5.3 |
| **1.5.3** | Aynı veri türü için uygulamada kullanılan farklı parser'ların (ör. JSON, XML, URL parser'ları), veriyi tutarlı şekilde ayrıştırdığı ve aynı karakter kodlamasını kullandığı doğrulanmalıdır. Böylece JSON birlikte çalışabilirlik açıkları, URI veya dosya ayrıştırma farkları gibi sorunlar nedeniyle RFI veya SSRF saldırılarının istismar edilmesi önlenir. | 3 | v5.0.be-5.5.5 |

## Referanslar

Daha fazla bilgi için:

* [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/README)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [RFC4180 - Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180#section-2)

Ters serileştirme ve parser konularında daha fazla bilgi için:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [OWASP Deserialization of Untrusted Data Guide](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai - A New Era of SSRF Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
