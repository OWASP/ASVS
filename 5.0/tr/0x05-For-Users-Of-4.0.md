# Guidance for users of version 4.0

## YAPILACAKLAR: Daha fazla içerik ekle

### Önceki Yaklaşımla İlgili Zorluklar

ASVS’nin 4.0 sürümünde seviyeler şu şekilde tanımlanmıştır: L1 - "Minimum", L2 - "Standart", ve L3 - "İleri Düzey". Bu tanımlama, hassas verileri işleyen tüm uygulamaların en az Seviye 2’ye ulaşması gerektiği anlamına gelmektedir.

Bu yaklaşım bazı zorlukları beraberinde getirmiştir.

#### Yüksek Giriş Engeli

Sürüm 4.0’daki Seviye 1, 100’den fazla gereksinim içeriyordu ve Seviye 2 de benzer sayıda gereksinime sahipti; yalnızca birkaç gereksinim Seviye 3’te kalmıştı. Bu durum, daha Seviye 1’e ulaşmak için bile yüksek düzeyde çaba gerektirirken, kullanıcıların bunun yalnızca "minimum" seviye olduğu ve "standart" güvenlik seviyesine ulaşmak için 100 ek gereksinimi daha tamamlamaları gerektiği mesajını almasına neden oluyordu. ASVS kullanıcılarından ve topluluktan gelen geri bildirimlere dayanarak, bu yaklaşımın caydırıcı olduğu ve uygulamaların ASVS’yi benimsemekte zorlanmasına yol açtığı anlaşıldı.

#### Test Edilebilirlik Yanılgısı

A primary motivator behind putting controls in L1 version 4.0 was whether they could be checked using "black box" style testing which was not entirely in line with the concept of L1 being the minimum security controls. On the one hand, ASVS users would say that L1 was not sufficient for a secure application whilst on the other hand user would complain that ASVS was too difficult to test.

Additionally, testability is relative and in some cases misleading. Just because something is testable does not mean that it is testable in an automated or trivial way. Finally, the most testable requirements are not necessarily those that have the most important security impact or are the easiest to implement.

#### Sadece Riskle İlgili Değil

Belirli bir uygulamanın belirli bir seviyede olması gerektiğini zorunlu kılan risk temelli seviyelerin kullanımı, geriye dönüp bakıldığında fazla kısıtlayıcı bir yaklaşım olarak değerlendirilmektedir. Gerçekte, güvenlik kontrollerinin uygulanma sırası yalnızca risk azaltımı ile değil, aynı zamanda uygulama zorluğu gibi diğer faktörlerle de belirlenir.


