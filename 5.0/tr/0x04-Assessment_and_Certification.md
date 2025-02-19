# Değerlendirme ve Sertifikasyon

## OWASP’in ASVS Sertifikaları ve Güven Damgaları Konusundaki Tutumu

OWASP, satıcıdan bağımsız bir kar amacı gütmeyen kuruluş olarak, herhangi bir satıcıyı, doğrulayıcıyı veya yazılımı sertifikalandırmaz. ASVS uyumluluğunu iddia eden herhangi bir güvence, güven damgası veya sertifikasyon OWASP tarafından resmi olarak onaylanmamaktadır. Bu nedenle, kuruluşlar üçüncü tarafların ASVS sertifikasyonu iddialarına karşı dikkatli olmalıdır.

Kuruluşlar, resmi bir OWASP sertifikası sunduklarını iddia etmemek koşuluyla güvence hizmetleri sunabilirler.

## Sertifikasyon Sağlayan Kuruluşlar İçin Rehberlik

Uygulama Güvenliği Doğrulama Standardı (ASVS), özellikle Seviye 2 ve Seviye 3 doğrulamaları için mimarlar, geliştiriciler, dokümantasyon, kaynak kod ve kimlik doğrulama gerektiren test sistemleri gibi kaynaklara açık erişim gerektirir.

Geleneksel sızma testi raporları yalnızca “istisnaları” bildirerek başarısızlıkları listeler. Ancak, sertifikalandırma raporları; kapsamı, başarılı ve başarısız testlerin özetlerini ve sorunların nasıl çözüleceğine dair rehberliği içermelidir. Bazı gereksinimler geçerli olmayabilir (örneğin, durum bilgisi olmayan API’lerde oturum yönetimi), bu gibi durumlar raporda belirtilmelidir.

Bulgulara sağlam kanıt sağlamak için çalışma notları, ekran görüntüleri, betikler ve test günlükleri gibi ayrıntılı belgeler standart uygulama olmalıdır. Yalnızca bir aracı çalıştırmak yeterli değildir; her gereksinim doğrulanabilir şekilde test edilmelidir.

## ASVS Uyumluluğu Nasıl Doğrulanır?

ASVS, uyumluluğun nasıl doğrulanacağı konusunda kasıtlı olarak kesin bir yöntem belirtmez. Ancak, bazı temel noktaların vurgulanması önemlidir.

### Doğrulama Kapsamı

Bir kuruluş genellikle tüm gereksinimleri uygulamayacaktır, çünkü bazıları onlar için alakasız veya daha az önemli olabilir. Bu nedenle, doğrulamanın kapsamı net bir şekilde tanımlanmalıdır. Doğrulayıcı, kuruluşun hangi Seviye'ye ulaşmayı hedeflediğini açıkça belirtmeli ve uygulanmayan gereksinimlerin neden dışarıda bırakıldığına dair bir gerekçe sunmalıdır.

Bu, doğrulama raporunu inceleyen kişinin doğrulamanın bağlamını anlamasını ve uygulamaya ne kadar güvenebileceği konusunda bilinçli bir karar vermesini sağlamalıdır.

Sertifikasyon sağlayan kuruluşlar test yöntemlerini kendileri belirleyebilir, ancak bunları raporda açıkça belirtmelidir. Manuel sızma testleri veya kaynak kod analizi gibi farklı yöntemler, uygulamanın gereksinimlerine bağlı olarak giriş doğrulama (input validation) gibi belirli güvenlik kontrollerini doğrulamak için kullanılabilir.

### Doğrulama Mekanizmaları

Belirli ASVS gereksinimlerini doğrulamak için çeşitli teknikler gerekebilir. Sızma testlerinin yanı sıra, ASVS gereksinimlerini doğrulamak için dokümantasyon, kaynak kod, yapılandırma ayarları ve geliştirme sürecine dahil olan kişilerle etkileşim gerekebilir.

ASVS gereksinimlerini doğrulamak için otomasyon kullanımı sürekli olarak ilgi çeken bir konudur. Sürüm 5.0 yayınlandıktan sonra, gereksinimlerin nasıl doğrulanabileceğini göstermek amacıyla bir test rehberi hazırlamak istiyoruz. Ancak, şimdilik otomatik testler ve kara kutu testleriyle ilgili bazı önemli noktaların netleştirilmesi gerekmektedir.

#### Otomatik Güvenlik Testi Araçlarının Rolü

DAST ve SAST gibi otomatik güvenlik testi araçları, derleme hattına (build pipeline) etkili bir şekilde entegre edildiğinde, asla var olmaması gereken bazı güvenlik açıklarını tespit edebilir. Ancak, dikkatli yapılandırma ve ayarlamalar yapılmadığı takdirde, bu araçlar beklenen kapsama alanını sağlayamayabilir ve ürettikleri yüksek miktarda gürültü (false positive) nedeniyle gerçek güvenlik sorunlarının tespit edilmesini ve giderilmesini zorlaştırabilir.

Bu araçlar, çıktı kodlama (output encoding) veya girdi temizleme (sanitization) gibi daha temel ve doğrudan teknik gereksinimlerin bir kısmını kapsayabilir. Ancak, daha karmaşık ASVS gereksinimlerini ya da iş mantığı ve erişim kontrolüyle ilgili gereksinimleri tamamen doğrulamalarının mümkün olmadığını vurgulamak önemlidir.

Daha karmaşık gereksinimler için otomasyon yine de kullanılabilir, ancak bunun için uygulamaya özel doğrulama mekanizmalarının yazılması gerekecektir. Bu mekanizmalar, kuruluşun hâlihazırda kullandığı birim testleri ve entegrasyon testlerine benzer olabilir. Dolayısıyla, mevcut test otomasyonu altyapısı kullanılarak ASVS’ye özgü testler yazmak mümkün olabilir. Bu yaklaşım kısa vadede yatırım gerektirse de, ASVS gereksinimlerinin sürekli olarak doğrulanabilmesini sağlamak uzun vadede önemli faydalar sağlayacaktır.

Özetle, "otomasyon ile test edilebilir" ifadesi "hazır bir aracı çalıştırmak" anlamına gelmez.

#### Sızma Testlerinin Rolü

Sürüm 4.0'daki Seviye 1, "kara kutu" (belge ve kaynak kod erişimi olmadan) testlerinin yapılabilmesi için optimize edilmiş olsa da, bunun etkili bir güvence yöntemi olmadığı ve aktif olarak caydırılması gerektiği konusunda net bir duruş sergiledik.

Gerekli ek bilgilere erişim olmadan yapılan testler, güvenlik doğrulaması için verimsiz ve etkisiz bir yöntemdir. Bu tür testler, kaynak kodun incelenmesi, tehditlerin ve eksik kontrollerin belirlenmesi gibi kritik adımları içermediğinden, çok daha kapsamlı bir testin daha kısa sürede gerçekleştirilme imkanını ortadan kaldırır.

Sızma testlerinin, geliştirme süreci boyunca geliştiricilere ve dokümantasyona tam erişim sağlayan, belge veya kaynak kod odaklı (hibrit) sızma testleriyle değiştirilmesini şiddetle tavsiye ediyoruz. ASVS gereksinimlerinin çoğunu doğrulamak için bu yaklaşım gerekli olacaktır.
