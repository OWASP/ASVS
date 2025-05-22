# Değerlendirme ve Sertifikasyon

## OWASP’in ASVS Sertifikaları ve Güven Damgaları Konusundaki Tutumu

OWASP, satıcıdan bağımsız bir kar amacı gütmeyen kuruluş olarak, herhangi bir satıcıyı, doğrulayıcıyı veya yazılımı sertifikalandırmaz. ASVS uyumluluğunu iddia eden herhangi bir güvence, güven damgası veya sertifikasyon OWASP tarafından resmi olarak onaylanmamaktadır. Bu nedenle, kuruluşlar üçüncü tarafların ASVS sertifikasyonu iddialarına karşı dikkatli olmalıdır.

Kuruluşlar, resmi bir OWASP sertifikası sunduklarını iddia etmemek koşuluyla güvence hizmetleri sunabilirler.

## ASVS Uyumluluğu Nasıl Doğrulanır?

ASVS, uyumluluğun nasıl doğrulanacağı konusunda kasıtlı olarak kesin bir yöntem belirtmez. Ancak, bazı temel noktaların vurgulanması önemlidir.

### Doğrulama Raporlaması

Geleneksel sızma testi raporları, yalnızca başarısız olan durumları istisnalarla listeler. Ancak bir ASVS sertifikasyon raporu; kapsamı, kontrol edilen tüm gereksinimlerin özetini, istisna tespit edilen gereksinimleri ve bu sorunların nasıl çözüleceğine dair rehberliği içermelidir. Bazı gereksinimler uygulanabilir olmayabilir (örneğin, durum bilgisi olmayan API'lerde oturum yönetimi), bu durum raporda açıkça belirtilmelidir.

### Doğrulama Kapsamı

Uygulama geliştiren bir organizasyon, uygulamanın işlevselliğine bağlı olarak bazı gereksinimleri uygulamayabilir, çünkü bunlar alakasız veya daha az önemli olabilir. Doğrulayıcı kişi veya kurum, doğrulamanın kapsamını açıkça belirtmelidir. Organizasyonun hangi Seviye’yi hedeflediği ve hangi gereksinimlerin dahil edildiği açıklanmalıdır. Bu, nelerin hariç tutulduğundan ziyade, nelerin dahil edildiği bakış açısından ele alınmalıdır. Ayrıca, uygulanmayan gereksinimlerin neden dışlandığına dair gerekçeli bir görüş sunulmalıdır.

Bu yaklaşım, raporu okuyan tarafın doğrulamanın bağlamını anlamasına ve uygulamaya ne kadar güvenebileceğine dair bilinçli bir karar vermesine olanak tanır.

Sertifikasyon yapan kuruluşlar kendi test yöntemlerini seçebilir, ancak bu yöntemler raporda açıkça belirtilmeli ve ideal olarak tekrarlanabilir olmalıdır. Girdi doğrulama gibi konular için sızma testi ya da kaynak kod analizi gibi farklı yöntemler kullanılabilir.

### Doğrulama Mekanizmaları

Bazı ASVS gereksinimlerinin doğrulanması için birden fazla teknik gerekebilir. Geçerli kullanıcı bilgileriyle tüm uygulama kapsamı elde edilerek yapılan sızma testlerine ek olarak ASVS gereksinimlerinin doğrulanması; dokümantasyon, kaynak kodu, yapılandırmalar ve geliştirme sürecine dahil kişilere, özellikle Seviye 2 ve Seviye 3 gereksinimlerinin doğrulanması için erişim gerektirebilir. Bulguların belgelenmesi standart bir uygulamadır ve buna çalışma notları, ekran görüntüleri, betikler ve test günlükleri (logs) dahil olabilir. Yalnızca otomatik bir araç çalıştırmak ve derinlemesine test yapmamak sertifikasyon için yeterli değildir; her gereksinimin doğrulanabilir şekilde test edilmiş olması gerekir.

ASVS gereksinimlerinin otomasyonla doğrulanması, her zaman ilgi çeken bir konudur. Bu nedenle, otomatik ve kara kutu (black box) testlerle ilgili bazı noktaların netleştirilmesi önemlidir.

#### Otomatik Güvenlik Testi Araçlarının Rolü

DAST ve SAST gibi dinamik ve statik güvenlik test araçları doğru şekilde build pipeline’a entegre edildiğinde, asla var olmaması gereken bazı güvenlik açıklarını tespit edebilir. Ancak, dikkatli bir şekilde yapılandırılmaz ve ayarlanmazlarsa, yeterli kapsama alanı sağlamazlar ve yüksek sayıda yanlış pozitif, gerçek güvenlik sorunlarının tespitini ve düzeltilmesini engeller.

Bu araçlar, çıktı kodlaması veya veri temizleme gibi bazı temel teknik gereksinimlerin doğrulanmasında yardımcı olabilir. Ancak, iş mantığı veya erişim kontrolü gibi daha karmaşık ASVS gereksinimlerinin doğrulanmasında yetersiz kalacaklardır.

Daha karmaşık gereksinimler için otomasyon yine de kullanılabilir, ancak uygulamaya özel testlerin yazılması gerekebilir. Bunlar, organizasyonun halihazırda kullandığı birim ve entegrasyon testlerine benzer şekilde tasarlanabilir. Mevcut test altyapısı kullanılarak bu ASVS'ye özel testler yazılabilir. Bu kısa vadede yatırım gerektirse de, uzun vadede bu gereksinimlerin sürekli olarak doğrulanabilmesi açısından önemli bir fayda sağlar.

Özetle, "otomasyon ile test edilebilir" ifadesi "hazır bir aracı çalıştırmak" anlamına gelmez.

#### Sızma Testlerinin Rolü

4.0 sürümünde Seviye 1, kara kutu (black box) test için optimize edilmişti (yani dokümantasyon veya kaynak kod olmadan). Ancak o zaman bile bunun etkili bir güvence yöntemi olmadığı ve aktif olarak kaçınılması gerektiği vurgulanmıştır.

Gerekli ek bilgilere erişim olmadan test yapmak, güvenlik doğrulaması açısından hem verimsiz hem de etkisizdir. Bu durum, kaynak kodun incelenmesi, tehditlerin ve eksik kontrollerin tespiti gibi daha kapsamlı analizlerin yapılmasını engeller ve süreci uzatır.

Geleneksel sızma testlerinin yerini, dokümantasyon ve/veya kaynak kod temelli (hibrit) sızma testlerinin almasını şiddetle tavsiye ediyoruz. Geliştirici ekip ve uygulamanın dokümantasyonuna tam erişim ile yapılan bu testler, birçok ASVS gereksiniminin doğrulanması için gerekli olacaktır.
