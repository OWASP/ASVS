# 4.0 Sürümünü Kullananlar İçin Rehber

ASVS’nin 4.0 sürümünü kullananlar için, 5.0 sürümünde içeriğe, kapsama ve felsefeye dair yapılan bazı önemli değişiklikleri görmek faydalı olabilir.

## 5.0’daki Yenilikler

Aşağıdaki bölümler, en büyük değişiklikleri kapsamayı amaçlamaktadır:

### Numaralandırma ve Sıralamanın Tamamen Yeniden Yapılandırılması

Neredeyse her bir gereksinim bir şekilde değiştirilmiştir; değiştirilmemiş veya yerinden oynatılmamış olanlar bile, diğer gereksinimlerin hareketi nedeniyle yeniden numaralandırılmıştır.

Sunulan eşlemeler (mapping) sayesinde, 4.0 sürümündeki gereksinimlerin 5.0 sürümüne nasıl geçtiği veya geçip geçmediği takip edilebilir.

### NIST Dijital Kimlik Kılavuzları ile Daha Az Bağlantı

NIST’in [Dijital Kimlik Kılavuzları (SP 800-63)](https://pages.nist.gov/800-63-3/) (Digital Identity Guidelines) kimlik doğrulama ve yetkilendirme kontrolleri için kanıta dayalı mükemmel bir standart olmuştur ve olmaya devam etmektedir. 4.0 sürümündeki bazı bölümler bu kılavuzlara yapı ve terminoloji açısından oldukça bağlıydı.

Bu kılavuzlar hâlâ önemli bir başvuru kaynağı olsa da, bu sıkı bağlantı çeşitli zorluklara yol açtı ve bu yaklaşımdan uzaklaşılmasına karar verildi. Bu zorluklar arasında; daha az tanınan terminolojiler, benzer durumlar için yinelenen gereksinimler ve ASVS için uygun görülen alanlarla eksik eşleşmeler yer alıyordu.

### CWE'den Uzaklaşma

MITRE’nin [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) projesi, yazılımların güvenlik açıklarını sınıflandırmak için faydalı bir yöntemdir. Ancak bazı CWE’ler yalnızca kategori olarak tanımlanmış olup eşlemede kullanılmamalıdır. Ayrıca bazı mevcut gereksinimleri doğrudan tek bir CWE ile eşleştirmek zor olabilir. 4.0 sürümünde bazı eşlemeler de gevşek ve belirsizdi.

Bu nedenle, CWE (ve diğer harici eşlemeler) kaldırılmış ve onun yerine, ASVS'nin farklı OWASP projeleri ve dış standartlarla ilişkilendirileceği OWASP Common Requirement Enumeration (CRE) projesine geçiş hedeflenmiştir.

### Mekanizmadan Çok Hedefe Odaklanma

4.0 sürümünde birçok gereksinim, ulaşılması istenen güvenlik hedefine değil, belirli bir teknik yönteme odaklanıyordu. 5.0 sürümünde ise, eğer tek bir yöntemle sağlanabilecek bir hedef değilse, gereksinimler belirli güvenlik hedeflerine odaklanır ve uygulanabilecek yöntemleri örnek olarak verir ya da rehber belgelerine yönlendirir.

### Güvenlik Kararlarının Belgelendirilmesi

Bazı gereksinimlerin uygulanması karmaşıktır ve uygulamaya özel değişkenlik gösterebilir. Yaygın örnekler arasında yetkilendirme, girdi doğrulama ve hassas veriye yönelik koruma kontrolleri yer alır. Bu durumlar için “tüm veriler şifrelenmelidir” gibi genelleştirilmiş ifadeler yerine, geliştiricilerin kullandığı yöntemlerin ve yapılandırmaların belgelenmesi gerektiği belirtilmiştir. Böylece bu belgeler uygunluk açısından gözden geçirilebilir ve uygulama ile belgelenen yapı karşılaştırılarak uyumluluk değerlendirilebilir.

<!-- ### YAPILACAKLAR: daha fazla madde eklenecek 

ASVS 4.0 Seviye 1’in, uygulama tasarımı, kodlama, test, güvenli kod incelemeleri ve sızma testleri açısından PCI DSS 3.2.1’in 6.5 bölümlerinin kapsamlı bir üst kümesi olmasını sağlamak amacıyla yola çıktık. Bu hedef, mevcut uygulama ve web servis doğrulama gereksinimlerine ek olarak, V5’te taşma (buffer overflow) ve güvensiz bellek işlemlerini, V14’te ise güvensiz bellekle ilgili derleyici bayraklarını kapsamayı gerekli kıldı.

ASVS'yi yalnızca sunucu taraflı monolitik kontrollerden, tüm modern uygulamalar ve API'ler için güvenlik kontrolleri sunacak şekilde dönüştürmeyi tamamladık. Fonksiyonel programlama, sunucusuz API’ler, mobil, bulut, konteyner, CI/CD, DevSecOps, federasyon ve daha fazlasının çağında, modern uygulama mimarisini görmezden gelemeyiz. Modern uygulamalar, ASVS'nin ilk kez yayınlandığı 2009 yılındaki uygulamalardan çok farklı tasarlanmaktadır. ASVS, ana hedef kitlesi olan geliştiricilere sağlam tavsiyeler verebilmek için her zaman geleceğe dönük olmalıdır. Tek bir kuruma ait sistemlerde çalıştığı varsayılan uygulamalara özel gereksinimleri ya netleştirdik ya da tamamen kaldırdık. 

ASVS 4.0’ın boyutu ve diğer tüm ASVS çabalarına temel olmak istememiz nedeniyle, mobil bölüm kaldırılmış ve onun yerine Mobil Uygulama Güvenliği Doğrulama Standardı (MASVS) getirilmiştir. Benzer şekilde, Nesnelerin İnterneti eki de kaldırılmış ve onun yerine IoT Güvenlik Doğrulama Standardı (ISVS) getirilmiştir. OWASP Mobil Ekibi ve OWASP IoT Projesi Ekibi’ne ASVS’ye verdikleri destekten dolayı teşekkür ederiz ve gelecekte tamamlayıcı standartlar oluşturmak için onlarla çalışmayı dört gözle bekliyoruz. 

Son olarak, düşük etkili kontrolleri sadeleştirdik ve bazılarını kaldırdık. Zamanla ASVS, kapsamlı bir kontrol setine dönüştü; ancak tüm kontroller, güvenli yazılım üretimine eşit düzeyde katkı sağlamamaktadır. Düşük etkili maddelerin elenmesine yönelik bu çaba daha da ileriye taşınabilir. Gelecekteki bir ASVS sürümünde, Common Weakness Scoring System (CWSS) gerçekten önemli kontrollerin önceliklendirilmesine ve kaldırılması gerekenlerin belirlenmesine yardımcı olacaktır. 

ASVS, 4.0 sürümünden itibaren yalnızca geleneksel ve modern uygulama mimarilerini, çevik güvenlik uygulamalarını ve DevSecOps kültürünü kapsayan lider bir web uygulamaları ve servis standardı olma hedefine odaklanacaktır.

-->

## Seviye Yaklaşımındaki Değişikliğe Ek Gerekçeler

ASVS 4.0’da seviyeler şöyle tanımlanıyordu: L1 - "Minimum", L2 - "Standart", L3 - "İleri Seviye", ve hassas veri işleyen tüm uygulamaların en az L2 seviyesinde olması gerektiği varsayılıyordu.

Bu yaklaşım bazı zorluklar doğurdu ve 4.0 sürümünü kullananlar için aşağıdaki bağlam bilgilendirici olabilir.

### Yüksek Giriş Engeli

4.0 sürümünde Seviye 1’in 100’ün üzerinde gereksinimi vardı, Seviye 2 de benzer sayıda gereksinim içeriyordu ve sadece az sayıda gereksinim Seviye 3’teydi. Bu da, daha “minimum” olarak tanımlanan Seviye 1’i bile karşılamak için yüksek efor gerektiği anlamına geliyordu. Ayrıca kullanıcıya, standart bir güvenlik seviyesi için 100 gereksinimin daha gerektiği söyleniyordu. Geri bildirimler, bu durumun kullanıcılar için caydırıcı olduğunu ve ASVS’ye geçişi zorlaştırdığını ortaya koydu.

### Test Edilebilirlik Yanılgısı

4.0 sürümünde kontrollerin Seviye 1’e dahil edilmesinin başlıca nedenlerinden biri, bunların “kara kutu” (black box) testi ile kontrol edilebiliyor olmasıydı. Ancak bu, minimum güvenlik kontrolleri fikriyle tamamen örtüşmüyordu. Bir yandan bazı kullanıcılar Seviye 1’in güvenli bir uygulama için yetersiz olduğunu söylüyor, diğer yandan test edilmesinin zor olduğundan şikayet ediyordu.

Ayrıca, test edilebilirlik görecelidir ve bazı durumlarda yanıltıcıdır. Bir şey test edilebilir olabilir ama bu onun otomatik veya kolay şekilde test edilebileceği anlamına gelmez. Son olarak, en kolay test edilebilen gereksinimler, her zaman en etkili güvenlik etkisine sahip veya en kolay uygulanabilir olanlar değildir.

### Sadece Risk Değil

4.0’daki risk temelli seviyelendirme yaklaşımı, her uygulamanın belirli bir seviyede olması gerektiğini zorunlu kılacak kadar katıydı. Ancak gerçek dünyada, güvenlik kontrollerinin uygulanma sırası yalnızca risk azaltımı ile değil, aynı zamanda uygulama zorluğu ile de ilgilidir.