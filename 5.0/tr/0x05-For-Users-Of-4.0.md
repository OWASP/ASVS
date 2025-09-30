# v4.x ile Karşılaştırıldığında Yapılan Değişiklikler

## Giriş

Standartın 4.x sürümüne aşina olan kullanıcılar, 5.0 sürümünde yapılan temel değişiklikleri içerik, kapsam ve altında yatan felsefe bakımından gözden geçirmeyi faydalı bulabilirler.

Sürüm 4.0.3'te yer alan 286 gereksinimin yalnızca 11 tanesi hiçbir değişikliğe uğramadan korunmuştur. 15 gereksinimde ise yalnızca anlamı değiştirmeyen dilbilgisel düzeltmeler yapılmıştır. Toplamda 109 gereksinim (%38) artık 5.0 sürümünde bağımsız birer gereksinim olarak yer almamaktadır. Bunların 50’si doğrudan silinmiş, 28’i yinelenen olarak kaldırılmış ve 31’i başka gereksinimlerle birleştirilmiştir. Geri kalan tüm gereksinimler bir şekilde revize edilmiştir. İçeriği esasen değiştirilmemiş olan gereksinimler bile, yeniden sıralama veya yapısal değişiklikler nedeniyle artık farklı tanımlayıcılara (ID) sahiptir.

Sürüm 5.0'ın benimsenmesini kolaylaştırmak için, kullanıcıların sürüm 4.x'teki gereksinimlerin sürüm 5.0'daki gereksinimlerle nasıl eşleştiğini izlemelerine yardımcı olmak için eşleme belgeleri sağlanmıştır. Bu eşlemeler sürüm numaralandırmasına bağlı değildir ve gerektiğinde güncellenebilir veya açıklığa kavuşturulabilir.

## Gereksinim Felsefesi

### Kapsam ve Odak

Sürüm 4.x, standardın hedeflenen kapsamıyla uyumlu olmayan bazı gereksinimler içeriyordu. Bu gereksinimler kaldırılmıştır. 5.0 sürümünün kapsam kriterlerini karşılamayan veya doğrulanabilir olmayan gereksinimler de eklenen gereksinimlerden hariç tutulmuştur.

### Mekanizmalar Yerine Güvenlik Hedeflerine Önem Verilmesi

Sürüm 4.x'te birçok gereksinim, altında yatan güvenlik hedefleri yerine belirli mekanizmalara odaklanıyordu. 5.0 sürümünde ise gereksinimler, belirli güvenlik hedefleri etrafında yapılandırılmıştır. Belirli mekanizmalara yalnızca bunların tek pratik çözüm olması durumunda doğrudan referans verilmiş veya örnek/rehber olarak yer verilmiştir.

Bu yaklaşım, belirli bir güvenlik hedefinin birden fazla yolla gerçekleştirilebileceğini kabul eder ve kuruluşların esnekliğini kısıtlayabilecek gereksiz derecede kuralcı yönlendirmelerden kaçınır.

Ayrıca, aynı güvenlik sorununu ele alan gereksinimler uygun şekilde birleştirilmiştir.

### Belgelenmiş Güvenlik Kararları

"Belgelenmiş güvenlik kararları" kavramı 5.0 sürümünde yeni gibi görünse de, 4.0 sürümündeki politika uygulamaları ve tehdit modellemesi ile ilgili daha önceki gereksinimlerin evrimleşmiş halidir. Önceki sürümlerde bazı gereksinimler, örneğin izin verilen ağ bağlantılarının belirlenmesi gibi, güvenlik kontrollerinin uygulanmasına yön verecek analizlerin yapılmasını dolaylı olarak talep etmekteydi.

Gerekli bilgilerin hem uygulama hem de doğrulama süreçlerinde erişilebilir olmasını sağlamak amacıyla bu beklentiler artık açıkça belgelenmesi gereken gereksinimler olarak tanımlanmıştır. Böylece bu gereksinimler daha net, uygulanabilir ve doğrulanabilir hale getirilmiştir.

## Yapısal Değişiklikler ve Yeni Bölümler

Sürüm 5.0’daki bazı bölümler tamamen yeni içerikler sunmaktadır:

* OAuth ve OIDC – Bu protokollerin erişim yetkisi devri ve tek oturum açma (SSO) için yaygın biçimde benimsenmiş olması nedeniyle, geliştiricilerin karşılaşabileceği çeşitli senaryoları kapsayan özel gereksinimler eklenmiştir. Bu alan, geçmişte Mobil ve IoT gereksinimlerinin ayrı bir standarda dönüştürülmesinde olduğu gibi, zamanla bağımsız bir standarda da dönüşebilir.
* WebRTC – Bu teknolojinin yaygınlaşmasıyla birlikte, kendine özgü güvenlik gereksinimleri ve zorlukları artık özel bir bölümde ele alınmaktadır.

Bölüm ve kısımların birbiriyle ilişkili gereksinim kümeleri etrafında daha tutarlı şekilde düzenlenmesine de özen gösterilmiştir.

Bu yeniden yapılandırma kapsamında şu ek bölümler oluşturulmuştur:

* Kendi İçinde Taşıyıcı Token’lar – Daha önce oturum yönetimi altında yer alan bu mekanizmalar artık ayrı bir yapı olarak tanınmakta ve OAuth ile OIDC gibi durumsuz iletişim yapılarının temel unsurlarından biri olarak ele alınmaktadır. Kendilerine özgü güvenlik etkileri nedeniyle, 5.x sürümünde bazı yeni gereksinimlerle birlikte ayrı bir bölümde toplanmıştır.
* Web Ön Yüz Güvenliği (Frontend Security) – Tarayıcı tabanlı uygulamaların artan karmaşıklığı ve yalnızca API’lara dayalı mimarilerin yaygınlaşması nedeniyle, frontend güvenliği gereksinimleri ayrı bir bölümde ele alınmıştır.
* Güvenli Kodlama ve Mimari – Diğer mevcut bölümlere doğrudan uymayan genel güvenlik uygulamalarıyla ilgili yeni gereksinimler burada gruplandırılmıştır.

Sürüm 5.0’daki diğer düzenleyici değişiklikler ise niyetin daha net şekilde anlaşılmasını sağlamayı amaçlamıştır. Örneğin, girdi doğrulama gereksinimleri iş kuralları doğrultusunda işletim sağladıkları için artık iş mantığı ile birlikte gruplanmış, eski yapıda yer aldıkları temizleme ve kodlama (sanitization & encoding) konularından ayrılmıştır.

Önceki V1 Mimari bölümü tamamen kaldırılmıştır. Bu bölümün ilk kısmı kapsam dışı gereksinimler içeriyordu. Sonraki kısımlar ise ilgili yeni bölümlere taşınmış, gereksinimler sadeleştirilmiş ve gerektiğinde yinelenen maddeler birleştirilerek açıklığa kavuşturulmuştur.

## Diğer Standartlara Yapılan Doğrudan Eşlemelerin Kaldırılması

Standardın ana kısmında yer alan diğer standartlara yönelik doğrudan eşlemeler kaldırılmıştır. Bunun yerine, ASVS'nin OWASP projeleri ve harici standartlarla ilişkilendirilmesini sağlayacak OWASP Common Requirement Enumeration (CRE) projesiyle bir eşleme hazırlanması hedeflenmektedir.

Aşağıda açıklanan nedenlerle, CWE ve NIST gibi standartlara yapılan doğrudan eşlemeler artık devam ettirilmemektedir.

### NIST Dijital Kimlik Kılavuzları (Digital Identity Guidelines) ile Azaltılmış Bağlılık

NIST [Digital Identity Guidelines (SP 800-63)](https://pages.nist.gov/800-63-3/) uzun süredir kimlik doğrulama ve yetkilendirme kontrolleri için bir başvuru noktası olarak kullanılmıştır. Sürüm 4.x’te bazı bölümler, NIST’in yapısı ve terminolojisiyle oldukça örtüşüyordu.

Bu kılavuzlar hâlâ önemli bir referans noktası olsa da, böyle bir sıkı örtüşme birtakım sorunlara yol açmıştır. Bu sorunlara yaygın olarak benimsenmemiş terimlerin kullanımı, benzer gereksinimlerin yinelenmesi ve eşlemenin eksik kalması örnek verilebilir. Sürüm 5.0, bu yaklaşımdan uzaklaşarak daha açık ve uygulanabilir bir yapı sunmayı hedeflemektedir.

### Common Weakness Enumeration'dan (CWE) Uzaklaşma

Common Weakness Enumeration (CWE), yazılım güvenliği zafiyetleri için faydalı bir sınıflandırma sistemidir. Ancak, yalnızca kategori düzeyinde tanımlanmış CWE’ler, bir gereksinimin yalnızca tek bir CWE ile eşleştirilememesi gibi eşleme zorlukları ve sürüm 4.x’teki bazı belirsiz eşlemeler sürüm 5.0’da doğrudan CWE eşlemelerinin sonlandırılmasına neden olmuştur.

## Seviye Tanımlarının Yeniden Düşünülmesi

Sürüm 4.x’te seviyeler L1 ("Minimum"), L2 ("Standart") ve L3 ("Gelişmiş") olarak tanımlanıyordu. Hassas veri işleyen tüm uygulamaların en az L2 seviyesini sağlaması gerektiği ima ediliyordu.

Sürüm 5.0, bu yaklaşıma dair çeşitli sorunları ele almaktadır.

Sürüm 4.x'te seviye göstergeleri tik işaretleriyle ifade edilirken, 5.x sürümünde tüm formatlarda (Markdown, PDF, DOCX, CSV, JSON ve XML) basit sayılar kullanılmaktadır. Geriye dönük uyumluluk için eski CSV, JSON ve XML çıktı formatlarında onay işaretleri hâlâ kullanılmaktadır.

### Daha Kolay Giriş Seviyesi

Geri bildirimler, yaklaşık 120 maddeden oluşan Seviye 1 gereksinimlerinin, aynı zamanda "minimum" olarak etiketlenip birçok uygulama için yetersiz görülmesi nedeniyle benimsenmesinin zorlaştığını göstermiştir. Sürüm 5.0, bu eşiği düşürmeyi hedefleyerek Seviye 1’i öncelikli olarak ilk savunma katmanına ait gereksinimler etrafında tanımlar ve bu seviyedeki gereksinimleri daha az ve daha net hale getirir. Sayısal olarak örnek vermek gerekirse sürüm 4.0.3'te 278 gereksinimden 128’i Seviye 1’di (%46). Sürüm 5.0.0'da ise 345 gereksinimden yalnızca 70’i Seviye 1’dir (%20).

### Test Edilebilirlik Yanılgısı

Sürüm 4.x’te Seviye 1 gereksinimleri belirlenirken, "dışsal kara kutu sızma testleriyle değerlendirilebilirlik" ön plandaydı. Ancak bu yaklaşım, Seviye 1’in güvenlik kontrolleri için minimum bir temel olması yönündeki amacıyla tam olarak örtüşmüyordu. Bazı kullanıcılar, Seviye 1’in yetersiz olduğunu savunurken, bazıları ise uygulanabilirliğini zor buluyordu.

Test edilebilirliğe odaklanmak hem göreceli hem de zaman zaman yanıltıcı olabilir. Bir gereksinimin test edilebilir olması, onun kolayca veya otomatik biçimde test edilebileceği anlamına gelmez. Ayrıca, en kolay test edilebilen gereksinimler her zaman en yüksek güvenlik katkısına sahip ya da en kolay uygulanabilir olanlar değildir.

Bu nedenle sürüm 5.0’da seviye belirleme kararları, esas olarak risk azaltımı temeline dayanır ve uygulama çabası da göz önünde bulundurulmuştur.

### Sadece Risk Odaklı Değil

Belirli uygulamalar için belirli bir seviyeyi zorunlu kılan, katı ve risk bazlı seviye yaklaşımı fazlasıyla sert bir yapıya dönüşmüştür. Gerçekte, güvenlik kontrollerinin önceliklendirilmesi ve uygulanması yalnızca risk değil, aynı zamanda uygulama çabası, organizasyonel olgunluk ve kullanıcıya verilmek istenen güvenlik mesajı gibi çeşitli faktörlere bağlıdır.

Bu nedenle, kuruluşların olgunluk düzeylerine ve kullanıcılarına vermek istedikleri mesaja göre hangi seviyeyi hedeflemeleri gerektiğine kendilerinin karar vermesi teşvik edilmektedir.
