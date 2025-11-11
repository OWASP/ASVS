# Ek D: Tavsiyeler

## Giriş

Uygulama Güvenliği Doğrulama Standardının (ASVS) 5.0 sürümü hazırlanırken, 5.0'da gereklilik olarak yer almaması gereken bir dizi mevcut ve yeni önerilen öğe olduğu anlaşıldı. Bunun nedeni, 5.0 tanımına göre ASVS kapsamında olmamaları veya alternatif olarak iyi bir fikir olmalarına rağmen zorunlu hale getirilemeyeceklerinin düşünülmesi olabilir.

Tüm bu maddeleri tamamen kaybetmek istemediğimiz için bazıları bu ekte yer almaktadır.

## Önerilen, kapsam dahilindeki mekanizmalar

Aşağıdaki maddeler ASVS için kapsam dahilindedir. Bunlar zorunlu hale getirilmemelidir ancak güvenli bir uygulamanın parçası olarak dikkate alınmaları şiddetle tavsiye edilir.

* Kullanıcıların daha güçlü bir parola belirlemesine yardımcı olmak için bir parola gücü ölçer sağlanmalıdır.
* Uygulamanın kök dizininde ya da .well-known dizininde, kullanıcıların güvenlik sorunları hakkında sahipleriyle iletişime geçebilecekleri bir bağlantı ya da e-posta adresini açıkça tanımlayan, herkese açık bir security.txt dosyası oluşturulmalıdır.
* İstemci tarafı girdi doğrulaması, güvenilir bir hizmet katmanında doğrulamaya ek olarak zorunlu kılınmalıdır. Çünkü bu, birisinin uygulamaya saldırmak amacıyla istemci tarafı kontrolleri atladığını keşfetmek için iyi bir fırsat sağlamaktadır.
* Bir robots.txt dosyası, X-Robots-Tag yanıt başlığı veya robots html meta etiketi kullanarak yanlışlıkla erişilebilen ve hassas sayfaların arama motorlarında görünmesi önlenmelidir.
* GraphQL kullanırken, yetkilendirmeyi her ayrı arayüzde ele almak zorunda kalmamak için yetkilendirme mantığı GraphQL veya çözümleyici katmanı yerine iş mantığı katmanında uygulanmalıdır.

Referanslar:

* [RFC bağlantısı da dahil olmak üzere security.txt hakkında daha fazla bilgi](https://securitytxt.org/)

## Yazılım Güvenliği İlkeleri

Aşağıdaki maddeler daha önce ASVS'de yer almaktaydı ancak tam olarak gereklilik değillerdir. Bunlar daha ziyade güvenlik kontrollerini uygularken göz önünde bulundurulması gereken ve takip edildiğinde daha sağlam kontrollere yol açacak ilkelerdir. Bunlar aşağıdakileri içerir:

* Güvenlik kontrolleri merkezi, basit (tasarım ekonomisi), doğrulanabilir şekilde güvenli ve yeniden kullanılabilir olmalıdır. Bu sayede mükerrer, eksik veya etkisiz kontrollerden kaçınılabilir.
* Mümkün olan her yerde, kontrolleri sıfırdan uygulamaya güvenmek yerine daha önce yazılmış ve iyi incelenmiş güvenlik kontrolü uygulamaları kullanılmalıdır.
* İdeal olarak, korunan verilere ve kaynaklara erişmek için tek bir erişim kontrol mekanizması kullanılmalıdır. Kopyala yapıştır veya güvensiz alternatif yollardan kaçınmak için tüm istekler bu tek mekanizmadan geçmelidir.
* Öznitelik veya özellik tabanlı erişim kontrolü, kodun kullanıcının sadece rolü yerine bir özellik veya veri öğesi için yetkisini kontrol ettiği önerilen bir modeldir. İzinler yine de roller kullanılarak tahsis edilmelidir.

## Yazılım Güvenliği Süreçleri

ASVS 5.0'dan kaldırılan ancak hala iyi bir fikir olan bir dizi güvenlik süreci vardır. OWASP SAMM projesi bu süreçlerin nasıl etkili bir şekilde uygulanacağı konusunda iyi bir kaynak olabilir. Daha önce ASVS'de yer alan maddeler şunlardır:

* Geliştirmenin tüm aşamalarında güvenliği ele alan güvenli bir yazılım geliştirme yaşam döngüsünün kullanıldığı doğrulanmalıdır.
* Tehditleri belirlemek, karşı önlemleri planlamak, uygun risk yanıtlarını kolaylaştırmak ve güvenlik testlerine rehberlik etmek için her tasarım değişikliği veya sprint planlaması için tehdit modellemesinin kullanıldığı doğrulanmalıdır.
* Tüm kullanıcı hikayelerinin ve özelliklerinin işlevsel güvenlik kısıtlamaları içerdiği doğrulanmalıdır. "Bir kullanıcı olarak profilimi görüntüleyebilmeli ve düzenleyebilmeliyim. Başkasının profilini görüntüleyememeli veya düzenleyememeliyim." gibi kısıtlamalar örnek olabilir.
* Tüm geliştiriciler ve test uzmanları için güvenli kodlama kontrol listesi, güvenlik gereksinimleri, kılavuz veya politikanın mevcut olduğu doğrulanmalıdır.
* Uygulama kaynak kodunun arka kapılardan, kötü amaçlı kodlardan (örn. salami saldırıları, mantık bombaları, saatli bombalar) ve belgelenmemiş veya gizli özelliklerden (örn. Easter eggs, güvensiz hata ayıklama araçları) arındırılmış olmasını sağlamak için devam eden bir sürecin var olduğu doğrulanmalıdır. Bu bölüme uymak, üçüncü taraf kütüphaneleri de dahil olmak üzere kaynak koduna tam erişim olmadan mümkün değildir ve bu nedenle muhtemelen yalnızca en yüksek düzeyde güvenlik gerektiren uygulamalar için uygundur.
* Konuşlandırılmış ortamlarda yapılandırma kaymasını tespit etmek ve buna yanıt vermek için mekanizmaların mevcut olduğu doğrulanmalıdır. Bu, değişmez altyapı, güvenli bir taban çizgisinden otomatik yeniden dağıtım veya mevcut durumu onaylanmış yapılandırmalarla karşılaştıran sapma tespit araçlarının kullanılmasını içerebilir.
* Tüm üçüncü taraf ürünlerde, kütüphanelerde, çerçevelerde ve hizmetlerde kendi önerilerine göre yapılandırma sağlamlaştırması yapıldığı doğrulanmalıdır.
  
Referanslar:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-project-threat-model/)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/securityengineering/sdl/)
