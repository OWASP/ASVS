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