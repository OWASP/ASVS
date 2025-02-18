# ASVS'yi Kullanma

ASVS, modern web uygulamaları ve hizmetleri için işlevsel ve işlevsel olmayan güvenlik gereksinimlerini tanımlar ve uygulama geliştiricilerin kontrolünde olan unsurlara odaklanır.

ASVS, güvenli uygulamalar geliştirmeyi ve bunu sürdürmeyi amaçlayan ya da uygulamaların güvenliğini değerlendirmek isteyen herkes için faydalıdır. Bu bölüm, ASVS’nin öncelik bazlı seviyeleri ve standart için çeşitli kullanım senaryoları da dahil olmak üzere, ASVS’nin nasıl kullanılacağına dair temel unsurları ele almaktadır.

## Uygulama Güvenliği Doğrulama Seviyeleri

Uygulama Güvenliği Doğrulama Standardı, her biri derinlik ve karmaşıklık açısından artan üç güvenlik doğrulama seviyesi tanımlar. Her ASVS seviyesi, o seviyeye ulaşmak için gerekli güvenlik gereksinimlerini belirtir (diğer gereksinimler ise öneri olarak kalır). Genel amaç, kuruluşların L1 seviyesi ile başlayıp, buradan itibaren daha üst seviyelere geçmeleridir.

### Sürüm 5.0'da Seviyelere Yaklaşım

Sürüm 5.0'daki seviye tamımlarına olan yaklaşım, ASVS kullanıcılarından gelen geri bildirimler ve yukarıdaki değerlendirmeler temel alınarak "Çalışma Grubu" içinde yapılan uzun tartışmalar sonucunda kararlaştırılmıştır.

Üç seviye ile devam edilmesi konusunda fikir birliğine varılmış olsa da, Seviye 1’deki gereksinim sayısı önemli ölçüde azaltılarak giriş engeli düşürülmüştür. Bir gereksinimin hangi seviyeye dahil edileceğini tanımlamak için kullanılan kriterler değiştirilmiş ve bu da seviyelerin tanımını yeniden şekillendirmiştir.

### Seviye Değerlendirme Kriterleri

Sürüm 5.0, güvenlik gereksinimlerinin uygulanmasındaki deneyimlere dayanarak her bir gereksinimi öncelik bazlı bir değerlendirmeye tabi tutar. Bu yaklaşımda, her gereksinim aşağıdaki kriterler kullanılarak değerlendirilmiştir.

#### Risk Azaltma

Bu gereksinim, uygulama içindeki güvenlik riskini ne ölçüde azaltıyor? Bu değerlendirme, klasik Gizlilik, Bütünlük ve Erişilebilirlik (CIA Triad) etki faktörlerini dikkate alır ve bunun birincil savunma katmanı mı yoksa derinlemesine savunma (defense in depth) olarak mı değerlendirileceğini göz önünde bulundurur.

Genel olarak, en büyük risk azaltımını sağlayan gereksinimler Seviye 1 veya Seviye 2’de yer alırken, hâlâ değerli olmakla birlikte daha çok derinlemesine savunmaya hizmet eden veya daha niş bir alan ya da sorunla ilgili olan gereksinimler Seviye 3’te bulunur.

#### Hayata Geçirme Eforu

ASVS bir doğrulama standardı olarak adlandırılsa da, bir gereksinim uygulamada hayata geçirilmediği sürece doğrulanacak bir şey yoktur. Bazı gereksinimlerin uygulanması ve sürdürülmesi diğerlerine göre çok daha karmaşıktır ve bir gereksinimin göreceli önceliği belirlenirken bunun dikkate alınması önemlidir.

Büyük bir risk azaltımı sağlayarak Seviye 1’de yer almayı hak eden bazı zorlayıcı kontroller olsa da, daha karmaşık gereksinimler genellikle Seviye 2 veya Seviye 3’te yer alacaktır.

#### Düşük Giriş Engeli

ASVS’nin sektörde kullanımı (veya kullanılmaması) hakkında alınan geri bildirimlere göre belirlenen en büyük sorun, Seviye 1’in yaklaşık 120 gereksinim içermesi nedeniyle hem oldukça kapsamlı olması hem de çoğu uygulama için yeterli bulunmayan bir "asgari" seviye olarak görülmesidir. Bu durum, kuruluşların ya başlamadan vazgeçmesine ya da Seviye 1’e tam olarak ulaşmadan yalnızca bazı gereksinimleri uygulamaya çalışmasına, dolayısıyla başarı ve ilerleme duygusunun azalmasına yol açıyor gibi görünmektedir.

Bu nedenle, Seviye 1’de en fazla yaklaşık 60 yüksek öncelikli gereksinimin bulunmasına ve diğerlerinin Seviye 2 veya Seviye 3’e kaydırılmasına karar verilmiştir. Bunu başarmak için, Seviye 1’e hangi gereksinimlerin dahil edileceği ve hangilerinin edilmeyeceği konusunda zor kararlar alınmıştır. Hedef, ulaşılamaz derecede "mükemmel" bir Seviye 1 yerine, gerçekleştirilebilir bir "iyi" Seviye 1 oluşturmaktı.

#### Daha İyi Seviye Dengesi

Sürüm 4.0’da, Seviye 1 ve Seviye 2’nin her biri yaklaşık 120 gereksinime sahipken, Seviye 3’te yaklaşık 30 gereksinim bulunuyordu. Sürüm 5.0, gereksinimleri seviyeler arasında daha dengeli bir şekilde dağıtarak, Seviye 2 ve Seviye 3’ü daha eşit bir yapıya kavuşturmayı amaçlamaktadır. Amaç, Seviye 2’yi daha ulaşılabilir ve gerçekçi hale getirirken, Seviye 3’ü en yüksek güvenlik seviyesini göstermek isteyen uygulamalara bırakmaktır.

### Seviyelerin Tanımları

Yukarıdaki kriterlere dayanarak, sürüm 5.0’daki gereksinimler üç seviyeden birine yerleştirilmiştir. Kuralcı bir seviye tanımından, çeşitli faktörlere dayanan karşılaştırmalı bir analize geçmek, bu yerleştirme sürecinde belli bir ölçüde değerlendirme yapılmasını gerektirmiştir.

Bununla birlikte, hem kriterler hem de seviye kararları üzerine yapılan titiz tartışmalar, çoğu durumda geçerliliğini koruyacak bir dağılım sağlamıştır. Ancak, her durum için %100 uyum sağlanamayabileceği de kabul edilmektedir. Bu, bazı durumlarda kuruluşların kendi özel risk değerlendirmelerine göre daha yüksek seviyedeki gereksinimlere daha erken öncelik verebileceği anlamına gelir.

Her seviyedeki gereksinim türleri aşağıdaki şekilde karakterize edilebilir.

#### Seviye 1 Gereksinimleri

Bu gereksinimler, genellikle yaygın saldırıları önlemek için kritik veya temel öneme sahip, birincil savunma katmanı gereksinimleridir ve uygulanması nispeten kolay ya da çabaya değecek kadar önemli olanlardır.

Seviye 1, mutlaka insanlarla yapılan bir sızma testiyle doğrulanabilir olmak zorunda değildir; ancak gereksinim sayısının azaltılması, doğrulamayı kolaylaştırmalıdır.

#### Seviye 2 Gereksinimleri

Bu gereksinimler genellikle daha az yaygın saldırılarla veya yaygın saldırılara karşı daha karmaşık korumalarla ilgilidir. Yine de genellikle birincil savunma katmanını oluştururlar.

#### Seviye 3 Gereksinimleri

Bu gereksinimler genellikle çok daha niş saldırılarla veya yalnızca belirli koşullarda geçerli olan senaryolarla ilgilidir. Bu bölümdeki gereksinimler aynı zamanda derinlemesine savunma mekanizmaları veya uygulanması zor ama faydalı diğer kontroller olabilir.

### Hangi Seviye Hedeflenmeli

Her bir gereksinimin öncelik bazlı değerlendirilmesine geçilmesiyle birlikte, seviyeler artık bir kuruluşun ve uygulamanın uygulama güvenliği olgunluğunu daha iyi yansıtır hale gelmiştir. ASVS’nin bir uygulamanın hangi seviyede olması gerektiğini kesin bir şekilde belirtmesi yerine, bir kuruluşun, uygulamanın hassasiyetine ve elbette kullanıcılarının beklentilerine bağlı olarak hangi seviyede olması gerektiğine kendisinin karar vermesi gerekir.

Örneğin, yalnızca sınırlı hassas veriler toplayan erken aşamadaki bir girişim, Seviye 1’in yeterli olduğuna karar verebilirken, bir bankanın çevrim içi bankacılık uygulaması için Seviye 3’ün altındaki bir seviyeyi müşterilerine gerekçelendirmesi zor olabilir.

## ASVS Gereksinimlerine Nasıl Atıfta Bulunulur?

Her gereksinimin <bölüm>.<kısım>.<gereksinim> formatında bir tanımlayıcısı vardır ve her öğe bir numaradan oluşur. Örneğin, `1.11.3`.

* `<bölüm>`(Chapter) değeri, gereksinimin geldiği bölümü belirtir. Örneğin, tüm `1.#.#` gereksinimleri `Mimari`(Architecture) bölümünden gelir.
* `<kısım>`(Section) değeri, o bölüm içinde gereksinimin yer aldığı kısmı belirtir. Örneğin, tüm `1.11.#` gereksinimleri `Mimari` bölümünün `İş Mantığı Mimari Gereksinimleri` kısmında bulunur.
* `<gereksinim>`(Requirement) değeri, bölüm ve kısım içindeki belirli bir gereksinimi tanımlar. Örneğin, `1.11.3` gereksinimi (bu standardın 4.0.2 sürümüne göre):

> Kimlik doğrulama, oturum yönetimi ve erişim kontrolü de dahil olmak üzere tüm yüksek değerli iş mantığı akışlarının, iş parçacığı açısından güvenli ve kontrol zamanı ile kullanım zamanı arasındaki yarış koşullarına karşı dirençli olduğunu doğrulayın.

Tanımlayıcılar standart sürümleri arasında değişebileceğinden, diğer belgeler, raporlar veya araçların şu formatı kullanması tercih edilir: `v<sürüm>-<bölüm>.<kısım>.<gereksinim>`, burada 'sürüm', ASVS sürüm etiketini ifade eder. Örneğin: `v4.0.2-1.11.3`, `Mimari` bölümünün `İş Mantığı Mimari Gereksinimleri` kısmındaki 3. gereksinimin 4.0.2 sürümüne ait olduğunu açıkça belirtir. (Bu, `v<sürüm>-<gereksinim_tanımlayıcısı>` olarak özetlenebilir.)

Not: Format içinde sürüm numarasından önce gelen `v` her zaman küçük harf olmalıdır.

Tanımlayıcılar `v<sürüm>` öğesi olmadan kullanıldığında, varsayılan olarak en güncel Uygulama Güvenliği Doğrulama Standardı içeriğine atıfta bulunulduğu kabul edilir. Ancak standart büyüyüp değiştikçe bu durum sorun yaratabilir, bu nedenle yazarlar veya geliştiriciler sürüm öğesini eklemelidir.

ASVS gereksinim listeleri, başvuru veya programatik kullanım için yararlı olabilecek CSV, JSON ve diğer formatlarda sunulmaktadır.

## ASVS’yi Çatallama (Forklama)

Organizations can benefit from adopting ASVS by choosing one of the three levels or by creating a domain-specific fork that adjusts requirements per application risk level. We encourage such forking, provided it maintains traceability so that passing requirement 4.1.1 means the same across all versions.

Ideally, each organization should create its own tailored ASVS, omitting irrelevant sections (e.g., GraphQL, Websockets, SOAP, if unused). Forking should start with ASVS Level 1 as a baseline, advancing to Levels 2 or 3 based on the application’s risk.

Kuruluşlar, ASVS’nin üç seviyesinden birini seçerek veya uygulamanın risk seviyesine göre gereksinimleri ayarlayan alan spesifik bir çatal (fork) oluşturarak ASVS’yi benimseyerek fayda sağlayabilir. Geçerli bir çatallamanın, 4.1.1 gereksinimini geçmenin tüm sürümlerde aynı anlama gelmesini sağlayacak şekilde izlenebilirliği korumasını öneriyoruz.

İdeal olarak, her kuruluş kendi ihtiyaçlarına özel bir ASVS oluşturmalı ve gereksiz bölümleri (örneğin, GraphQL, Websockets, SOAP gibi kullanılmayan teknolojiler) çıkarmalıdır. Çatallama, temel olarak ASVS Seviye 1’den başlamalı ve uygulamanın riskine bağlı olarak Seviye 2 veya Seviye 3’e ilerlemelidir.

## ASVS’nin Kullanım Alanları

ASVS, bir uygulamanın güvenliğini değerlendirmek için kullanılabilir ve bu konu bir sonraki bölümde daha ayrıntılı olarak ele alınmaktadır. Bununla birlikte, ASVS’nin (veya çatallanmış bir sürümünün) potansiyel diğer kullanım alanlarını da belirledik.

### Ayrıntılı Güvenlik Mimarisi Rehberi Olarak Kullanma

Uygulama Güvenliği Doğrulama Standardı’nın en yaygın kullanım alanlarından biri, güvenlik mimarları için bir kaynak olarak kullanılmasıdır. Sherwood Uygulamalı İş Güvenliği Mimarisi (SABSA), kapsamlı bir uygulama güvenliği mimarisi incelemesini tamamlamak için gerekli olan birçok bilgiden yoksundur. ASVS, güvenlik mimarlarının veri koruma modelleri ve girdi doğrulama stratejileri gibi yaygın sorunlar için daha iyi kontroller seçmesine olanak tanıyarak bu boşlukları doldurmak için kullanılabilir.

### Özelleştirilmiş Bir Güvenli Kodlama Kontrol Listesi Olarak Kullanma

ASVS, güvenli uygulama geliştirme sürecinde geliştiricilerin yazılım oluştururken güvenliği göz önünde bulundurmalarını sağlamak amacıyla güvenli kodlama kontrol listesi olarak kullanılabilir. Güvenli kodlama kontrol listesinin tüm geliştirme ekipleri için birleştirilmiş, net ve uygulanabilir olması gerekir. İdeal olarak, bu liste güvenlik mühendisleri veya güvenlik mimarlarının rehberliğinde hazırlanmalıdır.

### Otomatik Birim ve Entegrasyon Testleri İçin Rehber Olarak Kullanma

ASVS, mimari ve kötü amaçlı kod gereksinimleri dışında, yüksek test edilebilirlik göz önünde bulundurularak tasarlanmıştır. Belirli ve ilgili fuzzing (bulanık test) ve kötüye kullanım senaryolarını test eden birim ve entegrasyon testleri oluşturarak, her bir yapı (build) ile uygulamanın neredeyse kendi kendini doğrulaması sağlanabilir. Örneğin, bir oturum açma denetleyicisi (login controller) için hazırlanan test paketi, kullanıcı adı parametresini yaygın varsayılan kullanıcı adlarına, hesap enumerasyonu (numaralandırması), kaba kuvvet saldırılarına, LDAP ve SQL enjeksiyonlarına ve XSS saldırılarına karşı test eden ek testlerle geliştirilebilir. Benzer şekilde, parola parametresi için yapılacak bir test; yaygın parolalar, parola uzunluğu, null bayt enjeksiyonu, parametreyi kaldırma, XSS ve daha fazlasını içermelidir.

### Güvenli Geliştirme Eğitimi İçin Kullanma

ASVS, güvenli yazılımın özelliklerini tanımlamak için de kullanılabilir. Birçok “güvenli kodlama” kursu, sadece hafif kodlama ipuçları içeren etik hackerlık kurslarından ibarettir. Bu tür kurslar, geliştiricilerin daha güvenli kod yazmasına mutlaka yardımcı olmayabilir. Bunun yerine, güvenli yazılım geliştirme eğitimleri, ASVS’de bulunan proaktif kontrolleri temel alarak, yapılmaması gereken 10 olumsuz şeye odaklanmak yerine ASVS’yi merkeze alabilir.

### Çevik (Agile) Uygulama Güvenliği İçin Bir Yönlendirici Olarak Kullanma

ASVS, Agile geliştirme sürecinde ekibin güvenli bir ürün oluşturmak için uygulaması gereken belirli görevleri tanımlayan bir çerçeve(framework) olarak kullanılabilir. Örnek bir yaklaşım: Seviye 1’den başlayarak, belirli uygulama veya sistemi ASVS gereksinimlerine göre doğrulamak, eksik kontrolleri belirlemek ve kapsamda(backlog) belirli biletler/görevler açmak. Bu, belirli görevlerin önceliklendirilmesine (veya backlog’un düzenlenmesine) yardımcı olur ve güvenliği Agile süreçte görünür hale getirir. Bu yaklaşım ayrıca kuruluş içinde denetim ve inceleme görevlerinin önceliklendirilmesi için de uygulanabilir. Belirli bir ASVS gereksinimi, belirli bir ekip üyesi için bir inceleme, yeniden yapılandırma veya denetim sürecini tetikleyebilir ve sonunda ele alınması gereken bir ‘teknik borç’ olarak backlog’da görünebilir.

### Güvenli Yazılım Tedarikini Yönlendiren Bir Framework Olarak Kullanma

ASVS, güvenli yazılım tedariki veya özel yazılım geliştirme hizmetlerinin tedarikini kolaylaştırmak için harika bir çerçevedir. Müşteri, temin etmek istediği yazılımın ASVS Seviye X’e uygun olarak geliştirilmesini bir gereklilik olarak belirtebilir ve satıcıdan yazılımın ASVS Seviye X’i karşıladığını kanıtlamasını isteyebilir. Bu yaklaşım, OWASP Güvenli Yazılım Sözleşme Eki ile birlikte kullanıldığında oldukça etkili olur.

## ASVS’nin Pratikte Uygulanması

Farklı tehditler, farklı motivasyonlara sahiptir. Bazı sektörler, benzersiz bilgi ve teknoloji varlıklarına ve alana özgü düzenleyici uyumluluk gereksinimlerine sahiptir.

Kuruluşların, işlerinin doğasına bağlı olarak benzersiz risk özelliklerini derinlemesine incelemeleri ve bu risklere ve iş gereksinimlerine dayanarak uygun ASVS seviyesini belirlemeleri şiddetle tavsiye edilir.

Topluluktaki çeşitli üyelerden, standardı pratikte nasıl uyguladıklarına dair geri bildirimler aldık: