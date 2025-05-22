# ASVS'yi Kullanma

Uygulama Güvenliği Doğrulama Standardı (ASVS), modern web uygulamaları ve servisleri için güvenlik gereksinimlerini tanımlar ve uygulama geliştiricilerin kontrolünde olan unsurlara odaklanır.

ASVS, güvenli uygulamalar geliştirmeyi, sürdürmeyi ya da uygulamaların güvenliğini değerlendirmeyi amaçlayan herkes için faydalıdır. Bu bölümde, ASVS'nin kullanımına dair öncelik temelli seviyeler ve standardın farklı kullanım senaryoları gibi temel konular ele alınmaktadır.

## Uygulama Güvenliği Doğrulama Seviyeleri

ASVS, her biri artan derinlik ve karmaşıklığa sahip üç güvenlik doğrulama seviyesi tanımlar. Her ASVS seviyesi, o seviyeye ulaşmak için gerekli olan güvenlik gereksinimlerini belirtir (diğer gereksinimler ise öneri olarak kalır). Genel hedef, organizasyonların en düşük seviyeden başlayarak daha yüksek seviyelere geçmeleridir.

### Seviye Değerlendirme Kriterleri

Sürüm 5.0 için seviye tanımlama yaklaşımı, ASVS kullanıcılarından gelen geri bildirimler doğrultusunda Çalışma Grubu içerisinde yapılan yoğun tartışmalar sonucunda ve önceki bölümde açıklanan 5.0 sürümünün ilkeleri rehberliğinde belirlenmiştir. Sürüm 5.0, her bir güvenlik gereksinimini uygulama deneyimlerine dayanarak öncelik temelli bir değerlendirmeye tabi tutar. Bu yaklaşım benimsenerek, her gereksinim aşağıdaki kriterlere göre değerlendirilmiştir.

#### Risk Azaltma

Bu gereksinim, uygulama içindeki güvenlik riskini ne ölçüde azaltıyor? Bu değerlendirme, klasik Gizlilik, Bütünlük ve Erişilebilirlik (CIA Triad) etki faktörlerini dikkate alır ve aynı zamanda bunun birincil savunma katmanı mı yoksa savunma derinliği (defense in depth) kapsamında mı değerlendirileceğini göz önünde bulundurur.

Genel olarak, en yüksek risk azaltımını sağlayan gereksinimler Seviye 1 veya Seviye 2'de yer alırken; hâlâ değerli olan ancak savunma derinliği kapsamında olan ya da daha niş alanlara veya konulara hitap eden gereksinimler Seviye 3’te yer alır.

#### Hayata Geçirme Eforu

ASVS bir doğrulama standardı olarak adlandırılsa da, bir gereksinim uygulamada hayata geçirilmediği sürece doğrulanacak bir şey yoktur. Bazı gereksinimlerin uygulanması ve sürdürülmesi diğerlerine göre çok daha karmaşıktır ve bir gereksinimin göreceli önceliği belirlenirken bunun dikkate alınması önemlidir.

Bazı karmaşık kontroller uygulaması zor olsa da ciddi risk azaltımı sağladıkları için Seviye 1'de yer alabilir; ancak genellikle daha karmaşık gereksinimler Seviye 2 veya Seviye 3’te konumlandırılır.

#### Düşük Başlangıç Eşiği

Önceki ASVS sürümlerinin sektördeki kullanımına (veya kullanılmayışına) ilişkin geri bildirimlerden çıkan en büyük sorunlardan biri, Seviye 1’in yaklaşık 120 gereksinim içermesi nedeniyle oldukça kapsamlı olması ama aynı zamanda çoğu uygulama için “yetersiz asgari düzey” olarak değerlendirilmesiydi. Bu durum, organizasyonların ya başlamadan vazgeçmesine ya da gereksinimlerin sadece bir kısmını uygulamaya çalışmasına, ancak gerçek anlamda Seviye 1’i başaramamasına neden oldu; bu da ilerleme ve başarı hissini zayıflattı.

Bu nedenle Seviye 1’in, en yüksek önceliğe sahip yaklaşık 70 gereksinimle sınırlandırılmasına karar verildi. Bu sayı, hem uygulanabilirlik hem de güçlü bir güvenlik düzeyi sağlama açısından iyi bir denge olarak değerlendirildi. Diğer gereksinimler ise Seviye 2 veya Seviye 3’e aktarıldı. Bu hedefe ulaşmak için, Seviye 1'e nelerin dahil edileceği konusunda zorlu kararlar alındı. Amaç, uygulanabilir bir "iyi" Seviye 1 sunmaktı; uygulanamaz ama "mükemmel" bir Seviye 1 değil.

#### Daha İyi Seviye Dengesi

Sürüm 4.0’da, Seviye 1 ve Seviye 2’nin her birinde yaklaşık 120 gereksinim yer alırken, Seviye 3 sadece yaklaşık 30 gereksinim içeriyordu. Sürüm 5.0, gereksinimleri seviyeler arasında daha dengeli bir şekilde dağıtarak özellikle Seviye 2 ve Seviye 3 arasında eşitliği sağlamayı amaçlamaktadır. Bu sayede, Seviye 2 daha uygulanabilir ve gerçekçi hale gelirken, Seviye 3 ise en üst düzey güvenliği hedefleyen uygulamalar için ayrılmıştır.

### Seviye Tanımları

Yukarıda belirtilen kriterlere dayanarak, 5.0 sürümündeki gereksinimler üç seviyeden birine tahsis edilmiştir. Bu faktörlere dayalı karşılaştırmalı analizler, tahsis sürecinde bir miktar yorum payı bıraksa da, hem kriterler hem de seviye belirleme kararları üzerine yapılan titiz tartışmalar sonucunda, büyük çoğunlukla geçerli olacak bir dağılım elde edilmiştir. Her duruma %100 uymasa da genellikle yeterli olacaktır.

Bu, bazı durumlarda organizasyonların kendi özel risk değerlendirmelerine göre üst seviyedeki bazı gereksinimlere daha erken öncelik vermek isteyebileceği anlamına gelir.

Her seviyedeki gereksinim türleri aşağıdaki şekilde özetlenebilir.

#### Seviye 1 Gereksinimleri

Bu gereksinimler, genel olarak kritik veya temel düzeyde, yaygın saldırıları önlemeye yönelik, başka güvenlik açıkları veya ön koşullar gerektirmeyen ilk savunma katmanı gereksinimleridir. Bu gereksinimler ya uygulanması görece kolaydır ya da çabaya değecek kadar önemlidir.

Seviye 1 her zaman insanlar tarafından yapılan sızma testleriyle test edilebilir olmayabilir; ancak daha az sayıda gereksinim içermesi, doğrulamasını kolaylaştırır.

#### Seviye 2 Gereksinimleri

Bu gereksinimler genellikle daha az yaygın saldırılarla veya yaygın saldırılara karşı daha karmaşık koruma mekanizmalarıyla ilgilidir. Hâlâ birincil savunma katmanı olabilirler ya da saldırının başarılı olması için belirli ön koşulları gerektirebilirler.

#### Seviye 3 Gereksinimleri

Bu bölümdeki gereksinimler genellikle derinlemesine savunma mekanizmaları ya da uygulanması zor fakat faydalı kontrollerdir. Ayrıca, yalnızca belirli durumlarda geçerli olan veya daha niş saldırı türleriyle ilgili olabilirler.

### Hangi Seviye Hedeflenmeli

Her bir gereksinimin önceliğine dayalı bir değerlendirme yaklaşımına geçilmesiyle birlikte, seviyeler artık daha çok bir organizasyonun ve uygulamanın güvenlik olgunluğunu yansıtmaktadır. ASVS, uygulamanın hangi seviyede olması gerektiğini katı bir şekilde belirtmek yerine, organizasyonun uygulamanın hassasiyeti ve kullanıcıların beklentilerine göre hangi seviyede olması gerektiğine karar vermesini önerir.

Örneğin, yalnızca sınırlı miktarda hassas veri toplayan bir erken aşama girişim, Seviye 1’in yeterli olduğuna karar verebilirken; bir banka, çevrimiçi bankacılık uygulaması için Seviye 3’ten daha azını müşterilerine gerekçelendirmekte zorlanabilir.

## ASVS Gereksinimlerine Nasıl Atıfta Bulunulur?

Her gereksinimin `<bölüm>.<kısım>.<gereksinim>` formatında bir tanımlayıcısı vardır ve her öğe bir numaradan oluşur. Örneğin, `1.11.3`.

* `<bölüm>`(Chapter) değeri, gereksinimin geldiği bölümü belirtir. Örneğin, tüm `1.#.#` gereksinimleri `Mimari`(Architecture) bölümünden gelir.
* `<kısım>`(Section) değeri, o bölüm içinde gereksinimin yer aldığı kısmı belirtir. Örneğin, tüm `1.11.#` gereksinimleri `Mimari` bölümünün `İş Mantığı Mimari Gereksinimleri` kısmında bulunur.
* `<gereksinim>`(Requirement) değeri, bölüm ve kısım içindeki belirli bir gereksinimi tanımlar. Örneğin, `1.11.3` gereksinimi (bu standardın 4.0.2 sürümüne göre):

> Tüm yüksek değerli iş mantığı akışlarının — kimlik doğrulama, oturum yönetimi ve erişim kontrolü dahil — iş parçacığına (thread) karşı güvenli ve zaman kontrolü ile zaman kullanımı arasındaki yarış durumu (race condition) saldırılarına dayanıklı olduğu doğrulanmalıdır.

Tanımlayıcılar standart sürümleri arasında değişebileceğinden, diğer belgeler, raporlar veya araçların şu formatı kullanması tercih edilir: `v<sürüm>-<bölüm>.<kısım>.<gereksinim>`, burada 'sürüm', ASVS sürüm etiketini ifade eder. Örneğin: `v4.0.2-1.11.3`, `Mimari` bölümünün `İş Mantığı Mimari Gereksinimleri` kısmındaki 3. gereksinimin 4.0.2 sürümüne ait olduğunu açıkça belirtir. (Bu, `v<sürüm>-<gereksinim_tanımlayıcısı>` olarak özetlenebilir.)

Not: Format içinde sürüm numarasından önce gelen `v` her zaman küçük harf olmalıdır.

Tanımlayıcılar `v<sürüm>` öğesi olmadan kullanıldığında, varsayılan olarak en güncel Uygulama Güvenliği Doğrulama Standardı içeriğine atıfta bulunulduğu kabul edilir. Ancak standart büyüyüp değiştikçe bu durum sorun yaratabilir, bu nedenle yazarlar veya geliştiriciler sürüm öğesini eklemelidir.

ASVS gereksinim listeleri, başvuru veya programatik kullanım için yararlı olabilecek CSV, JSON ve diğer formatlarda sunulmaktadır.

## ASVS’yi Çatallama (Forklama)

Kuruluşlar, ASVS’yi benimseyerek üç seviyeden birini seçebilir ya da uygulama risk seviyesine göre gereksinimleri uyarlayan alan (domain) odaklı bir çatallanma (fork) oluşturabilir. Bu tür çatallamaları teşvik ediyoruz; yeter ki izlenebilirlik korunmuş olsun, yani bir sürümde 4.1.1 gereksiniminin karşılanması diğer tüm sürümlerde de aynı anlama gelmelidir.

İdeal olarak, her kuruluş kendi ihtiyaçlarına özel, özelleştirilmiş bir ASVS oluşturmalıdır; kullanılmayan bölümler (örneğin, GraphQL, Websockets, SOAP gibi) bu özelleştirmede çıkarılabilir. Çatallanma, temel olarak ASVS Seviye 1 ile başlamalı ve uygulamanın risk düzeyine bağlı olarak Seviye 2 veya Seviye 3’e doğru ilerlemelidir.

## ASVS’nin Kullanım Alanları

ASVS, bir uygulamanın güvenliğini değerlendirmek amacıyla kullanılabilir ve bu konu bir sonraki bölümde daha ayrıntılı olarak ele alınacaktır. Ancak, ASVS'nin (veya çatallanmış bir sürümünün) başka potansiyel kullanım alanlarını da belirledik.

### Ayrıntılı Güvenlik Mimarisi Rehberi Olarak Kullanma

Uygulama Güvenliği Doğrulama Standardı'nın en yaygın kullanım alanlarından biri, güvenlik mimarları için bir kaynak olarak kullanılmasıdır. Sherwood Applied Business Security Architecture (SABSA), kapsamlı bir uygulama güvenliği mimarisi değerlendirmesini tamamlamak için gereken pek çok bilgiden yoksundur. ASVS, güvenlik mimarlarının veri koruma desenleri ve girdi doğrulama stratejileri gibi yaygın problemler için daha iyi kontroller seçmesine olanak tanıyarak bu boşlukları doldurabilir.

### Özelleştirilmiş Bir Güvenli Kodlama Kontrol Listesi Olarak Kullanma

ASVS, güvenli uygulama geliştirme sürecinde geliştiricilere rehberlik etmek amacıyla güvenli kodlama kontrol listesi olarak kullanılabilir. Bu sayede geliştiriciler, yazılım oluştururken güvenliği ön planda tutabilir. Güvenli kodlama kontrol listesi; birleştirilmiş, açık ve tüm geliştirme ekiplerine uygulanabilir olmalıdır. İdeal olarak, bu liste güvenlik mühendisleri veya güvenlik mimarlarının rehberliğiyle hazırlanmalıdır.

### Otomatik Birim ve Entegrasyon Testleri İçin Rehber Olarak Kullanma

ASVS, mimari ve dokümantasyon gereksinimleri dışında, yüksek derecede test edilebilir olacak şekilde tasarlanmıştır. Spesifik ve ilgili kötüye kullanım senaryolarına yönelik birim ve entegrasyon testleri oluşturarak, her derlemede uygulanmış olan kontrollerin doğrulanması kolaylaşır. Örneğin, bir oturum açma kontrolörü için hazırlanan test paketine; yaygın varsayılan kullanıcı adları, hesap bulma, kaba kuvvet saldırıları, LDAP ve SQL enjeksiyonu, XSS gibi saldırılarla ilgili testler eklenebilir. Benzer şekilde, parola parametresi için yapılan bir testte yaygın parolalar, parola uzunluğu, null byte enjeksiyonu, parametrenin eksikliği, XSS ve benzeri senaryolar yer almalıdır.

### Güvenli Geliştirme Eğitimi İçin Kullanma

ASVS, güvenli yazılımın sahip olması gereken özellikleri tanımlamak için de kullanılabilir. Pek çok "güvenli kodlama" eğitimi, aslında yalnızca etik hacking derslerine yüzeysel birkaç kod ipucu eklenmiş hâlidir. Bu yaklaşım, geliştiricilerin daha güvenli kod yazmasına her zaman katkı sağlamaz. Bunun yerine, güvenli geliştirme eğitimleri, OWASP Top 10 gibi yapılmaması gereken olumsuzluklara değil, ASVS'de bulunan proaktif kontroller üzerine odaklanarak daha etkili hâle getirilebilir.

### Çevik (Agile) Uygulama Güvenliği İçin Bir Yönlendirici Olarak Kullanma

ASVS, agile yazılım geliştirme süreçlerinde güvenli ürün oluşturmak için takımın uygulaması gereken görevleri tanımlayan bir çerçeve olarak kullanılabilir. Örneğin Seviye 1 ile başlanır, belirli bir uygulama ya da sistem bu seviyedeki ASVS gereksinimlerine göre doğrulanır, eksik kontroller belirlenir ve bunlara ilişkin görevler backlog’a eklenir. Bu yöntem, önceliklendirme (grooming) sürecine yardımcı olur ve güvenliği agile süreçte görünür hâle getirir. Aynı zamanda, organizasyon içinde denetim ve inceleme görevlerinin önceliklendirilmesi için de kullanılabilir. Belirli bir ASVS gereksinimi, bir ekip üyesi için kod gözden geçirme, yeniden yapılandırma (refactor) veya denetim görevi olarak backlog’da "borç" olarak görünür hâle gelebilir.

### Güvenli Yazılım Tedariğini Yönlendiren Bir Framework Olarak Kullanma

ASVS, güvenli yazılım ya da özel yazılım geliştirme hizmeti satın alımı için mükemmel bir çerçevedir. Alıcı, satın alınmak istenen yazılımın ASVS Seviye X’e uygun geliştirilmesini şart koşabilir ve satıcıdan bu seviyeye uygunluğunu ispatlamasını talep edebilir. Bu yaklaşım, OWASP Güvenli Yazılım Sözleşme Eki (OWASP Secure Software Contract Annex) ile birlikte kullanıldığında oldukça etkilidir.

## ASVS’nin Pratikte Uygulanması

Farklı tehditlerin farklı motivasyonları vardır. Bazı sektörlerin kendine özgü bilgi ve teknoloji varlıkları ile alan odaklı regülasyon ve uyumluluk gereksinimleri olabilir.

Kuruluşların, işlerinin doğası gereği sahip oldukları özgün risk faktörlerini derinlemesine incelemeleri ve bu riskler ile iş ihtiyaçlarına göre uygun ASVS seviyesini belirlemeleri şiddetle tavsiye edilir.