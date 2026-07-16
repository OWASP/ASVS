# ASVS Nedir?

Uygulama Güvenliği Doğrulama Standardı (ASVS), web uygulamaları ve hizmetleri için güvenlik gereksinimlerini tanımlar ve güvenli uygulamalar tasarlamayı, geliştirmeyi ve sürdürmeyi veya bunların güvenliğini değerlendirmeyi amaçlayan herkes için değerli bir kaynaktır.

Bu bölümde ASVS'nin kapsamı, önceliğe dayalı seviyelerinin yapısı ve standart için birincil kullanım durumları da dahil olmak üzere ASVS'yi kullanmanın temel yönleri özetlenmektedir.

## ASVS'nin Kapsamı

ASVS'nin kapsamı adıyla tanımlanmaktadır: Uygulama, Güvenlik, Doğrulama ve Standart. Ulaşılması gereken güvenlik ilkelerini tanımlamak amacıyla hangi gereksinimlerin dahil edileceğini veya hariç tutulacağını belirler. Kapsam, uygulama gereksinimleri için temel teşkil eden dokümantasyon gereksinimlerini de dikkate alır.

Saldırganlar için kapsam diye bir şey yoktur. Bu nedenle ASVS gereksinimleri, CI/CD süreçleri, hosting ve operasyonel faaliyetler de dahil olmak üzere uygulama yaşam döngüsünün diğer yönlerine ilişkin yönlendirmelerle birlikte değerlendirilmelidir.

### Uygulama

ASVS bir “uygulamayı”, güvenlik kontrollerinin entegre edilmesi gereken ve geliştirilmekte olan yazılım ürünü olarak tanımlar. ASVS, geliştirme yaşam döngüsü faaliyetlerini belirlemez veya uygulamanın bir CI/CD boru hattı aracılığıyla nasıl oluşturulması gerektiğini dikte etmez. Bunun yerine, ürünün kendi içinde elde edilmesi gereken güvenlik sonuçlarını belirtir.

Web Uygulaması Güvenlik Duvarları (WAF'lar), yük dengeleyiciler veya proxy'ler gibi HTTP trafiğini sunan, değiştiren veya doğrulayan bileşenler, bazı güvenlik kontrolleri doğrudan bunlara bağlı olduğundan veya bunlar aracılığıyla uygulanabildiğinden, bu özel amaçlar için uygulamanın bir parçası olarak kabul edilebilir. Bu bileşenler, önbelleğe alınan yanıtlar, hız sınırlaması veya gelen ve giden bağlantıların kaynak ve hedefe göre kısıtlanmasıyla ilgili gereksinimler için dikkate alınmalıdır.

Tersine, ASVS genellikle uygulamayla doğrudan ilgili olmayan veya yapılandırmanın uygulamanın sorumluluğu dışında olduğu gereksinimleri hariç tutar. Örneğin, DNS sorunları genellikle ayrı bir ekip veya işlev tarafından yönetilir.

Benzer şekilde, uygulama girdiyi nasıl tükettiğinden ve çıktıyı nasıl ürettiğinden sorumlu olsa da, harici bir süreç uygulama veya verileriyle etkileşime giriyorsa, ASVS için kapsam dışı kabul edilir. Örneğin, uygulamanın veya verilerinin yedeklenmesi genellikle harici bir sürecin sorumluluğundadır ve uygulama veya geliştiricileri tarafından kontrol edilmez.

### Güvenlik

Her gerekliliğin güvenlik üzerinde kanıtlanabilir bir etkisi olmalıdır. Bir gerekliliğin olmaması daha az güvenli bir uygulama ile sonuçlanmalı ve gerekliliğin uygulanması bir güvenlik riskinin olasılığını veya etkisini azaltmalıdır.

İşlevsel yönler, kod stili veya politika gereksinimleri gibi diğer tüm hususlar kapsam dışıdır.

### Doğrulama

Gereksinim doğrulanabilir olmalı ve doğrulama “başarısız” veya “başarılı” kararıyla sonuçlanmalıdır.

### Standart

ASVS, standarda uymak için uygulanması gereken bir güvenlik gereksinimleri koleksiyonu olarak tasarlanmıştır. Bu, gereksinimlerin bunu başarmak için güvenlik hedefini tanımlamakla sınırlı olduğu anlamına gelir. Diğer ilgili bilgiler ASVS'nin üzerine inşa edilebilir veya eşleştirmeler yoluyla bağlanabilir.

Özellikle, OWASP'ın birçok projesi vardır ve ASVS kasıtlı olarak diğer projelerdeki içerikle örtüşmekten kaçınır. Örneğin, geliştiricilerin “belirli bir gereksinimi kendi teknolojimde veya ortamımda nasıl uygulayabilirim” şeklinde bir sorusu olabilir ve bu, Cheat Sheet Series projesi kapsamında ele alınmalıdır. Doğrulayıcıların “bu gereksinimi bu ortamda nasıl test edebilirim” şeklinde bir sorusu olabilir ve bu Web Güvenliği Test Kılavuzu projesi kapsamında ele alınmalıdır.

ASVS sadece güvenlik uzmanlarının kullanımına yönelik olmamakla birlikte, okuyucunun içeriği anlamak için teknik bilgiye veya belirli kavramları araştırma becerisine sahip olmasını beklemektedir.

### Gereksinim

Gereksinim kelimesi ASVS'de özel olarak kullanılır çünkü bu kelimenin karşılanması için nelerin başarılması gerektiğini tanımlar. ASVS sadece gereksinimleri (must) içerir ve ana koşul olarak tavsiyeleri (should) içermez.

Başka bir deyişle, ister bir sorunu çözmek için birçok olası seçenekten biri isterse de kod stili hususları olsun, öneriler bir gereksinim olma tanımını karşılamaz.

ASVS gereksinimleri, uygulamaya veya teknolojiye özgü olmadan belirli güvenlik ilkelerini ele almayı ve aynı zamanda neden var olduklarına dair açıklayıcı olmayı amaçlamaktadır. Bu aynı zamanda gereksinimlerin belirli bir doğrulama yöntemi veya uygulaması etrafında oluşturulmadığı anlamına gelir.

### Belgelenmiş güvenlik kararları

Yazılım güvenliğinde, güvenlik tasarımını ve kullanılacak mekanizmaları erkenden planlamak, bitmiş üründe veya özellikte daha tutarlı ve güvenilir bir uygulama oluşturacaktır.

Ayrıca, belirli gereksinimler için uygulama, karmaşık ve bir uygulamanın ihtiyaçlarına çok spesifik olacaktır. Yaygın örnekler arasında izinler, girdi doğrulama ve farklı hassas veri seviyeleri etrafında koruyucu kontroller yer alır.

Bunu hesaba katmak için "tüm veriler şifrelenmelidir" gibi kapsamlı ifadeler veya bir gereksinimde olası her kullanım durumunu kapsamaya çalışmak yerine, uygulama geliştiricisinin bu tür kontrollere yaklaşımının ve yapılandırmasının belgelenmesini zorunlu kılan dokümantasyon gereksinimleri dahil edilmiştir. Bu daha sonra uygunluk açısından gözden geçirilebilir ve ardından gerçek uygulama, uygulamanın beklentilere uyup uymadığını değerlendirmek için belgelerle karşılaştırılabilir.

Bu gereksinimler, uygulamayı geliştiren kuruluşun belirli güvenlik gereksinimlerinin nasıl uygulanacağına ilişkin aldığı kararları belgelemeyi amaçlamaktadır.

Dokümantasyon gereksinimleri her zaman bir bölümün ilk kısmında yer alır (her bölümde olmasa da) ve her zaman dokümante edilen kararların gerçekten uygulamaya konulması gereken ilgili bir uygulama gerekliliğine sahiptir. Burada önemli olan nokta, dokümantasyonun yerinde olduğunu ve fiili uygulamanın iki ayrı faaliyet olduğunu doğrulamaktır.

Bu gereksinimleri dahil etmenin iki temel nedeni vardır. İlk neden, güvenlik gereksiniminin genellikle kuralların uygulanmasını içermesidir. Örneğin hangi tür dosya türlerinin yüklenmesine izin verilir, hangi iş kontrolleri uygulanmalıdır, belirli bir alan için izin verilen karakterler nelerdir gibi uygulanma biçimleri. Bu kurallar her uygulama için farklı olacaktır ve bu nedenle ASVS, bunların ne olması gerektiğini kuralcı bir şekilde tanımlayamaz ve bu durumda bir cheat sheet veya daha ayrıntılı bir yanıt da yardımcı olmaz. Benzer şekilde, bu kararlar belgelenmeden, bu kararları uygulayan gereksinimlerin doğrulanması mümkün olmayacaktır.

İkinci neden ise, belirli gereksinimler için belirli güvenlik sorunlarının nasıl ele alınacağı konusunda esnekliğe sahip bir uygulama geliştirme sağlamanın önemli olmasıdır. Örneğin, önceki ASVS sürümlerinde oturum zaman aşımı kuralları çok kuralcıydı. Pratik olarak, birçok uygulama, özellikle tüketicilere yönelik olanlar, çok daha esnek kurallara sahiptir ve bunun yerine diğer risk azaltma kontrollerini uygulamayı tercih eder. Bu nedenle, belgeleme gereksinimleri bu konuda açıkça esneklik sağlar.

Elbette ki, bu kararların bireysel geliştiriciler tarafından alınması ve belgelenmesi beklenmemektedir. Aksine, bu kararlar organizasyonun bir bütün olarak alınacak ve geliştiricilere iletilecek, geliştiriciler de bu kararları uygulamaya özen gösterecektir.

Geliştiricilere yeni özellikler ve işlevler için spesifikasyonlar ve tasarımlar sağlamak, yazılım geliştirmenin standart bir parçasıdır. Benzer şekilde, geliştiricilerin her seferinde kendi kararlarını vermek yerine ortak bileşenleri ve kullanıcı arayüzü mekanizmalarını kullanmaları beklenir. Bu nedenle, bunu güvenliğe genişletmek şaşırtıcı veya tartışmalı olarak görülmemelidir.

Bunu nasıl başaracağınız konusunda da esneklik vardır. Güvenlik kararları, geliştiricilerin başvurması beklenen yazılı bir belgede belgelenebilir. Alternatif olarak, güvenlik kararları belgelenebilir ve tüm geliştiricilerin kullanması zorunlu olan ortak bir kod kütüphanesinde uygulanabilir. Her iki durumda da istenen sonuç elde edilir.

## Uygulama Güvenliği Doğrulama Seviyeleri

ASVS, seviyesi arttıkça derinliği ve karmaşıklığı artan üç güvenlik doğrulama seviyesi tanımlar. Genel amaç, kuruluşların en kritik güvenlik sorunlarını ele almak için ilk seviyeden başlaması ve ardından kuruluşun ve uygulamanın ihtiyaçlarına göre daha yüksek seviyelere geçmesidir. Seviyeler, belgede ve gereksinim metinlerinde L1, L2 ve L3 olarak gösterilebilir.

Her ASVS seviyesi, o seviyeden elde edilmesi gereken güvenlik gereksinimlerini belirtir ve kalan daha yüksek seviye gereksinimler öneri olarak sunulur.

Yinelenen gereksinimleri veya daha yüksek seviyelerde artık geçerli olmayan gereksinimleri önlemek için bazı gereksinimler belirli bir seviyeye özel uygulanır. Fakat bu gereksinimler daha yüksek seviyeler için daha katı koşullar içerir.

### Seviye değerlendirmesi

Seviyeler, güvenlik gereksinimlerinin uygulanması ve test edilmesi deneyimine dayalı olarak her bir gereksinimin öncelik bazlı değerlendirmesiyle tanımlanır. Ana odak noktası, risk azaltma ile gereksinimin uygulanması için gereken çabayı karşılaştırmaktır. Bir diğer önemli faktör ise giriş engelini düşük tutmaktır.

Risk azaltma, gereksinimin uygulama içindeki güvenlik riskinin düzeyini ne ölçüde azalttığını, klasik Gizlilik, Bütünlük ve Kullanılabilirlik etki faktörlerini dikkate alarak ve bunun birincil savunma katmanı mı yoksa derinlemesine savunma mı olduğunu değerlendirerek değerlendirir.

Kriterler ve seviyelendirme kararları etrafında yapılan titiz tartışmalar, her duruma %100 uymayabileceğini kabul etmekle birlikte, vakaların büyük çoğunluğu için geçerli olması gereken bir dağılımla sonuçlanmıştır. Bu, belirli durumlarda kuruluşların kendi özel risk değerlendirmelerine göre daha yüksek seviyedeki gereksinimleri daha erken önceliklendirmek isteyebilecekleri anlamına gelir.

Her seviyedeki gereksinim türleri aşağıdaki gibi tanımlanabilir:

### Seviye 1

Bu seviye, bir uygulamayı güvenli hale getirirken dikkate alınması gereken minimum gereksinimleri içerir ve kritik bir başlangıç noktasıdır. Bu seviye, ASVS gereksinimlerinin yaklaşık %20'sini içerir. Bu seviyenin amacı, giriş engelini azaltmak için mümkün olduğunca az gereksinim olmasını sağlamaktır.

Bu gereksinimler genellikle kritik veya temel, diğer güvenlik açıklarının veya ön koşulların istismar edilmesini gerektirmeyen yaygın saldırıları önlemek için birinci katman savunma gereksinimleridir.

Birinci savunma katmanı gereksinimlerine ek olarak, bazı gereksinimlerin daha yüksek seviyelerde etkisi daha azdır, şifrelerle ilgili gereksinimler gibi. Bunlar Seviye 1 için daha önemlidir, çünkü daha yüksek seviyelerde çok faktörlü kimlik doğrulama gereksinimleri önem kazanır.

Seviye 1, belgelere veya koda iç erişimi olmayan bir dış test uzmanı tarafından mutlaka penetrasyon testi yapılabilir değildir (örneğin "kara kutu" testi), ancak gereksinimlerin sayısının az olması doğrulamayı kolaylaştırmalıdır.

### Seviye 2

Çoğu uygulama bu güvenlik seviyesine ulaşmak için çaba göstermelidir. ASVS'deki gereksinimlerin yaklaşık %50'si L2 seviyesindedir, yani bir uygulamanın L2 seviyesine uymak için ASVS'deki gereksinimlerin yaklaşık %70'ini (tüm L1 ve L2 gereksinimlerini) uygulaması gerekir.

Bu gereksinimler genellikle daha az yaygın saldırılarla veya yaygın saldırılara karşı daha karmaşık korumalarla ilgilidir. Bunlar hala ilk savunma katmanı olabilir veya saldırının başarılı olması için belirli ön koşullar gerektirebilir.

### Seviye 3

Bu seviye, en yüksek güvenlik seviyelerini göstermek isteyen uygulamalar için bir hedef olmalıdır. Bu seviye, uyum sağlamak için gereken gereksinimlerin son %30'unu sağlar.

Bu bölümdeki gereksinimler genellikle derinlemesine savunma mekanizmaları veya diğer yararlı ancak uygulanması zor kontrollerden oluşur.

### Hangi seviyeye ulaşılmalı?

Öncelik tabanlı seviyeler, kuruluşun ve uygulamanın uygulama güvenliği olgunluğunu yansıtmayı amaçlamaktadır. ASVS, bir uygulamanın hangi seviyede olması gerektiğini kuralcı bir şekilde belirtmek yerine, kuruluşun risklerini analiz etmesi ve uygulamanın hassasiyetine ve elbette uygulamanın kullanıcılarının beklentilerine bağlı olarak hangi seviyede olması gerektiğini belirlemesi gerekir.

Örneğin, yalnızca sınırlı miktarda hassas veri toplayan erken aşamadaki bir girişim, ilk güvenlik hedefleri için Seviye 1'e odaklanmaya karar verebilir, ancak bir banka, çevrimiçi bankacılık uygulaması için müşterilerine Seviye 3'ten daha düşük bir seviyeyi haklı çıkarmakta zorlanabilir.

## ASVS nasıl kullanılır?

### ASVS'nin yapısı

ASVS, toplamda yaklaşık 350 gereksinimden oluşur ve bu gereksinimler 17 bölüme ayrılmıştır. Her bölüm de alt bölümlere ayrılmıştır.

Bölüm ve alt bölümlerin ayrılmasının amacı, uygulama ile ilgili olanları seçmeyi veya filtrelemeyi kolaylaştırmaktır. Örneğin, bir makineler arası API için, V3 bölümündeki web ön uçlarıyla ilgili gereksinimler ilgili olmayacaktır. OAuth veya WebRTC kullanılmıyorsa, bu bölümler de göz ardı edilebilir.

### Sürüm stratejisi

ASVS sürümleri "Major.Minor.Patch" ("Büyük.Küçük.Yama") modelini izler ve sayılar sürüm içinde nelerin değiştiği hakkında bilgi verir. Büyük bir sürümde ilk sayı, küçük bir sürümde ikinci sayı ve yama sürümünde üçüncü sayı değişir.

* Büyük sürüm - Tamamen yeniden düzenleme yapılmıştır. Gereksinim numaraları da dahil olmak üzere neredeyse her şey değişebilir. Uyumluluk için yeniden değerlendirme gerekli olacaktır (örneğin, 4.0.3 -> 5.0.0).
* Küçük sürüm - Gereksinimler eklenebilir veya kaldırılabilir, ancak genel numaralandırma aynı kalır. Uyumluluk için yeniden değerlendirme gerekli olacaktır, ancak daha kolay olacaktır (örneğin, 5.0.0 -> 5.1.0).
* Yama sürümü - Gereksinimler kaldırılabilir (örneğin, tekrar eden veya güncelliğini yitiren gereksinimler) veya daha az katı hale getirilebilir, ancak önceki sürüme uygun olan bir uygulama, yama sürümüne de uygun olacaktır (örneğin, 5.0.0 -> 5.0.1).

Yukarıdaki bilgiler özellikle ASVS'deki gereksinimlerle ilgilidir. Gereksinimleri çevreleyen metin ve ekler gibi diğer içeriklerdeki değişiklikler, önemli bir değişiklik olarak değerlendirilmeyecektir.

### ASVS ile esneklik

Yukarıda açıklanan belgeleme gereksinimleri ve seviye mekanizması gibi bazı noktalar, ASVS'yi daha esnek ve kuruluşa özgü bir şekilde kullanma olanağı sağlar.

Ayrıca, kuruluşların uygulamalarının belirli özelliklerine ve risk seviyelerine göre gereksinimleri ayarlayan, kuruluşa veya alana özgü bir "fork" oluşturmaları şiddetle tavsiye edilir. Ancak, gereksinim 4.1.1'in tüm sürümlerde aynı anlama gelmesi için izlenebilirliği korumak önemlidir.

İdeal olarak, her kuruluş kendi özel ASVS'sini oluşturmalı ve ilgisiz bölümleri (örneğin, kullanılmıyorsa GraphQL, WebSockets, SOAP) çıkarmalıdır. Kuruluşa özgü bir ASVS sürümü veya eki, gereksinimlere uyum sağlarken kullanılacak kütüphaneleri veya kaynakları ayrıntılı olarak açıklayan, kuruluşa özgü uygulama kılavuzları sağlamak için de iyi bir varlıktır.

### ASVS Gereksinimlerine Nasıl Atıfta Bulunulur?

Her gereksinim, her ögesinin bir sayı olduğu `<bölüm>.<kısım>.<gereksinim>` biçiminde bir tanımlayıcıya sahiptir. Örneğin, `1.11.3`.

* `<bölüm>` (chapter) değeri, gereksinimin geldiği bölümü belirtir. Örneğin, tüm `1.#.#` gereksinimleri "Kodlama (Encoding) ve Temizleme" bölümünden gelir.
* `<kısım>` (section) değeri, o bölüm içinde gereksinimin yer aldığı kısmı belirtir. Örneğin, tüm `1.2.#` gereksinimleri "Kodlama ve Temizleme" bölümünün "Enjeksiyon Önleme" bölümündedir.
* `<gereksinim>` (requirement) değeri, bölüm ve kısım içindeki belirli bir gereksinimi tanımlar. Örneğin, bu standardın 5.0.0 sürümünde `1.2.5` şu şekildedir:

> Uygulamanın işletim sistemi komut enjeksiyonuna karşı koruma sağladığını ve işletim sistemi çağrılarının parametreli işletim sistemi sorguları veya bağlamsal komut satırı çıktı kodlaması kullandığını doğrulayın.

Tanımlayıcılar standardın sürümleri arasında değişebileceğinden, diğer belgeler, raporlar veya araçlar için aşağıdaki biçimin kullanılması tercih edilir: `v<sürüm>-<bölüm>.<kısım>.<gereksinim>`, burada: 'sürüm' ASVS sürüm etiketidir. Örneğin: `v5.0.0-1.2.5`, 5.0.0 sürümünün "Kodlama ve Temizleme" bölümünün "Enjeksiyon Önleme" alt bölümündeki 5. gereksinimi ifade eder. (Bu, `v<sürüm>-<gereksinim_tanımlayıcı>` olarak özetlenebilir.)

Not: Format içinde sürüm numarasından önce gelen v her zaman küçük harf olmalıdır.

Tanımlayıcılar v<sürüm> öğesi olmadan kullanıldığında, varsayılan olarak en güncel Uygulama Güvenliği Doğrulama Standardı içeriğine atıfta bulunulduğu kabul edilir. Ancak standart büyüyüp değiştikçe bu durum sorun yaratabilir, bu nedenle yazarlar veya geliştiriciler sürüm öğesini eklemelidir.

ASVS gereksinim listeleri, başvuru veya programatik kullanım için yararlı olabilecek CSV, JSON ve diğer formatlarda sunulmaktadır.

### ASVS’yi Çatallama (Forklama)

Kuruluşlar, üç seviyeden birini seçerek veya uygulama risk seviyesine göre gereksinimleri ayarlayan alana özgü bir fork oluşturarak ASVS'den faydalanabilir. Bu tür bir fork, izlenebilirliği koruduğu sürece teşvik edilir, böylece 4.1.1 gereksiniminin karşılanması tüm sürümlerde aynı anlama gelir.

İdeal olarak, her kuruluş kendi özel ASVS'sini oluşturmalı ve alakasız bölümleri (örneğin, kullanılmıyorsa GraphQL, Websockets, SOAP) çıkarmalıdır. Fork oluşturma, ASVS Seviye 1'i temel alarak başlamalı ve uygulamanın riskine göre Seviye 2 veya 3'e ilerlemelidir.

## ASVS’nin kullanım alanları

ASVS, bir uygulamanın güvenliğini değerlendirmek amacıyla kullanılabilir ve bu konu bir sonraki bölümde daha ayrıntılı olarak ele alınacaktır. Ancak, ASVS'nin (veya forklanmış bir sürümünün) başka potansiyel kullanım alanları da belirlenmiştir.

### Ayrıntılı Güvenlik Mimarisi Rehberi Olarak Kullanma

Uygulama Güvenliği Doğrulama Standardı'nın en yaygın kullanım alanlarından biri, güvenlik mimarları için bir kaynak olarak kullanılmasıdır. Özellikle modern uygulamalarda, güvenli bir uygulama mimarisi oluşturmak için sınırlı sayıda kaynak mevcuttur. ASVS, güvenlik mimarlarının veri koruma modelleri ve girdi doğrulama stratejileri gibi yaygın sorunlar için daha iyi kontroller seçmelerine olanak tanıyarak bu boşlukları doldurmak için kullanılabilir. Mimari ve dokümantasyon gereksinimleri bu konuda özellikle yararlı olacaktır.

### Özelleştirilmiş Bir Güvenli Kodlama Referansı Olarak Kullanma

ASVS, uygulama geliştirme sırasında güvenli kodlama referansı hazırlamak için temel olarak kullanılabilir ve geliştiricilerin yazılım oluştururken güvenliği göz önünde bulundurmalarını sağlar. ASVS temel olarak kullanılabilirken, kuruluşlar kendi özel kılavuzlarını hazırlamalıdır. Bu kılavuzlar açık ve birleşik olmalı ve ideal olarak güvenlik mühendisleri veya güvenlik mimarlarının rehberliğine dayalı olarak hazırlanmalıdır. Bunun bir uzantısı olarak, kuruluşların mümkün olduğunca kılavuzda referans gösterilebilecek ve geliştiriciler tarafından kullanılabilecek onaylanmış güvenlik mekanizmaları ve kütüphaneleri hazırlamaları teşvik edilir.

### Otomatik Birim ve Entegrasyon Testleri İçin Rehber Olarak Kullanma

ASVS, yüksek düzeyde test edilebilir şekilde tasarlanmıştır. Bazı doğrulamalar teknik nitelikteyken, bazı gereksinimler (mimari ve dokümantasyon gereksinimleri gibi) dokümantasyon veya mimari incelemesi gerektirebilir. Teknik yollarla doğrulanabilir gereksinimlerle ilgili belirli ve ilgili kötüye kullanım durumlarını test eden ve "fuzz" yapan birim ve entegrasyon testleri oluşturarak, bu kontrollerin her derlemede doğru şekilde çalıştığını kontrol etmek daha kolay hale gelmelidir. Örneğin, bir oturum açma denetleyicisi için test paketi için ek testler oluşturulabilir. Bu testlerde, kullanıcı adı parametresi için yaygın varsayılan kullanıcı adları, hesap numaralandırma, kaba kuvvet saldırısı, LDAP ve SQL enjeksiyonu ve XSS test edilir. Benzer şekilde, şifre parametresi üzerinde yapılan bir testte yaygın şifreler, şifre uzunluğu, null byte enjeksiyonu, parametrenin kaldırılması, XSS ve daha fazlası yer almalıdır.

### Güvenli Geliştirme Eğitimi İçin Kullanma

ASVS, güvenli yazılımın özelliklerini tanımlamak için de kullanılabilir. Birçok "güvenli kodlama kursu", kodlama ipuçlarının hafifçe serpiştirildiği etik hackleme kurslarından ibarettir. Bu, geliştiricilerin daha güvenli kod yazmasına yardımcı olmayabilir. Güvenli geliştirme kursları, yapılmaması gereken en önemli 10 olumsuz şey yerine ASVS'yi kullanarak ASVS'de bulunan olumlu mekanizmalara odaklanabilir. ASVS yapısı, bir uygulamayı güvenli hale getirirken farklı konuları ele almak için mantıklı bir yapı da sağlar.

### Güvenli Yazılım Satın Alımına Rehberlik Eden Bir Çerçeve Olarak Kullanma

ASVS, güvenli yazılım satın alımına veya özel geliştirme hizmetleri satın alımına yardımcı olan harika bir çerçevedir. Alıcı, satın almak istediği yazılımın ASVS seviye X'te geliştirilmesi gerektiğini belirten bir gereksinim belirleyebilir ve satıcıdan yazılımın ASVS seviye X'i karşıladığını kanıtlamasını isteyebilir.

## ASVS'nin Pratikte Uygulanması

Farklı tehditlerin farklı motivasyonları vardır. Bazı sektörler, benzersiz bilgi ve teknoloji varlıklarına ve alana özgü yasal uyumluluk gereksinimlerine sahiptir.

Kuruluşların, işlerinin doğasına göre benzersiz risk özelliklerini derinlemesine incelemeleri ve bu risk ve iş gereksinimlerine göre uygun ASVS seviyesini belirlemeleri şiddetle tavsiye edilir.
