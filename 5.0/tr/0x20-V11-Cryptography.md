# V11 Kriptografi

## Kontrol Amacı

Bu bölümün amacı, kriptografinin genel kullanımı için en iyi uygulamaları tanımlamak, kriptografik ilkelere dair temel bir anlayış kazandırmak ve daha dayanıklı ve modern yaklaşımlara yönelimi teşvik etmektir. Bu doğrultuda aşağıdakileri teşvik eder:

* Güvenli şekilde hata veren, gelişen tehditlere uyum sağlayan ve geleceğe yönelik sağlam kriptografik sistemlerin uygulanması,
* Hem güvenli hem de sektörün en iyi uygulamalarıyla uyumlu kriptografik mekanizmaların kullanılması,
* Uygun erişim kontrolleri ve denetimle birlikte güvenli bir kriptografik anahtar yönetim sisteminin sürdürülmesi,
* Kriptografik ortamın düzenli olarak değerlendirilerek yeni risklerin analiz edilmesi ve algoritmaların buna göre uyarlanması,
* Uygulamanın yaşam döngüsü boyunca tüm kriptografik varlıkların keşfedildiğinden ve güvence altına alındığından emin olmak için kriptografi kullanım alanlarının belirlenmesi ve yönetilmesi.

Genel ilkeleri ve en iyi uygulamaları özetlemenin yanı sıra, bu belge Ek C - Kriptografi Standartları bölümünde gereksinimlerle ilgili daha teknik bilgiler de sunar. Bu bölüm, "onaylı" kabul edilen algoritmaları ve modları içerir.

Kriptografinin sır yönetimi ya da iletişim güvenliği gibi başka bir sorunu çözmek için kullanıldığı gereksinimler, bu standardın başka bölümlerinde yer almaktadır.

## V11.1 Kriptografik Envanter ve Dokümantasyon

Veri varlıklarını sınıflandırmalarına uygun şekilde korumak için uygulamaların güçlü bir kriptografik mimari ile tasarlanması gerekir. Her şeyi şifrelemek kaynak israfına, hiçbir şeyi şifrelememek ise hukuki ihlallere yol açar. Genellikle mimari tasarım, tasarım sprintleri veya mimari zirveler sırasında bir denge kurulmalıdır. Kriptografiyi "doğaçlama" yapmak veya sonradan eklemek, güvenli biçimde uygulamak için her zaman daha maliyetli olacaktır.

Tüm kriptografik varlıkların düzenli olarak keşfedildiğinden, envantere alındığından ve değerlendirildiğinden emin olunması önemlidir. Bunun nasıl yapılacağı hakkında daha fazla bilgi için ekteki bölüme bakınız.

Kriptografik sistemlerin kuantum bilgisayarların olası yükselişine karşı geleceğe yönelik olarak dayanıklı hale getirilmesi de kritik önemdedir. Post-Kuantum Kriptografi (PQC), kuantum bilgisayar saldırılarına karşı güvenli kalacak şekilde tasarlanmış kriptografik algoritmaları ifade eder; bu tür bilgisayarların, RSA ve eliptik eğri kriptografisi (ECC) gibi yaygın algoritmaları kırması beklenmektedir.

Onaylı PQC ilkelikleri ve standartlarıyla ilgili güncel bilgiler için ekteki bölüme bakınız.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **11.1.1** | Kriptografik anahtarların yönetimi için belgelenmiş bir politika ve NIST SP 800-57 gibi bir anahtar yönetim standardını izleyen bir kriptografik anahtar yaşam döngüsü tanımlandığı doğrulanmalıdır. Bu, anahtarların aşırı miktarda paylaşılmadığını (örneğin, paylaşılan sırlar için ikiden fazla tarafla veya özel anahtarlar için birden fazla tarafla) garanti altına almalıdır. | 2 |
| **11.1.2** | Tüm kriptografik anahtarlar, algoritmalar ve uygulama tarafından kullanılan sertifikaları içeren bir kriptografik envanterin oluşturulduğu, sürdürüldüğü ve düzenli olarak güncellendiği doğrulanmalıdır. Bu envanter ayrıca, sistemde anahtarların nerede kullanılabileceğini ve kullanılamayacağını, ve hangi veri türlerinin bu anahtarlarla korunup korunamayacağını da belgelemelidir. | 2 |
| **11.1.3** | Sistem içerisinde şifreleme, özetleme ve imzalama işlemleri dahil olmak üzere kriptografi kullanımının tüm örneklerini tespit etmek için kriptografik keşif mekanizmalarının kullanıldığı doğrulanmalıdır. | 3 |
| **11.1.4** | Kriptografik bir envanterin sürdürüldüğü doğrulanmalıdır. Bu envanter, gelecekteki tehditlere karşı tepki verebilmek amacıyla post-kuantum kriptografiye geçiş yolunu belirten belgelenmiş bir plan içermelidir. | 3 |

## V11.2 Güvenli Kriptografi Uygulaması

Bu bölüm, bir uygulama için temel kriptografik algoritmaların seçimi, uygulanması ve sürekli yönetimine yönelik gereksinimleri tanımlar. Amaç, yalnızca sağlam, sektör tarafından kabul görmüş kriptografik ilkeliklerin, güncel standartlara (örneğin NIST, ISO/IEC) ve en iyi uygulamalara uygun biçimde kullanılmasını sağlamaktır. Kuruluşlar, her kriptografik bileşenin peer-review uygulanmış kanıtlar ve pratik güvenlik testlerine dayalı olarak seçildiğinden emin olmalıdır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **11.2.1** | Kriptografik işlemler için sektör tarafından doğrulanmış uygulamaların (kütüphaneler ve donanım hızlandırmalı uygulamalar dahil) kullanıldığı doğrulanmalıdır. | 2 |
| **11.2.2** | Uygulamanın, rastgele sayı üreticileri, kimliği doğrulanmış şifreleme, MAC veya özetleme algoritmaları, anahtar uzunlukları, turlar, şifreler ve modların herhangi bir zamanda yeniden yapılandırılabilir, yükseltilebilir veya değiştirilebilir olacağı şekilde kripto çevikliği (crypto agility) ile tasarlandığı doğrulanmalıdır. Aynı şekilde, anahtarların ve parolaların değiştirilebilmesi ve verilerin yeniden şifrelenebilmesi mümkün olmalıdır. Bu, onaylanmış PQC şemalarının yüksek güvenlikli uygulamaları yaygın olarak kullanılabilir hale geldiğinde sorunsuz geçişe olanak tanır. | 2 |
| **11.2.3** | Tüm kriptografik ilkeliklerin, algoritma, anahtar boyutu ve yapılandırmaya göre minimum 128 bit güvenlik sağladığı doğrulanmalıdır. Örneğin, 256-bit ECC anahtarı yaklaşık 128 bit güvenlik sağlarken, RSA için aynı güvenliği elde etmek 3072-bit anahtar gerektirir. | 2 |
| **11.2.4** | Tüm kriptografik işlemlerin sabit süreli (constant-time) olduğu, karşılaştırmalarda, hesaplamalarda veya geri dönüşlerde kısa devre (short-circuit) işlemleri yapılmadığı doğrulanmalıdır; bu, bilgi sızıntısını önlemek için gereklidir. | 3 |
| **11.2.5** | Tüm kriptografik modüllerin güvenli şekilde hata verdiği ve hataların, padding oracle saldırıları gibi zafiyetleri mümkün kılmayacak şekilde ele alındığı doğrulanmalıdır. | 3 |


## V11.3 Şifreleme Algoritmaları

AES ve CHACHA20 üzerine kurulu kimliği doğrulanmış şifreleme algoritmaları, modern kriptografik uygulamaların temelini oluşturur.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **11.3.1** | Güvensiz blok modlarının (örneğin, ECB) ve zayıf doldurma (padding) şemalarının (örneğin, PKCS#1 v1.5) kullanılmadığı doğrulanmalıdır. | 1 |
| **11.3.2** | Yalnızca AES ile GCM gibi onaylı şifreleme algoritmalarının ve modlarının kullanıldığı doğrulanmalıdır. | 1 |
| **11.3.3** | Şifrelenmiş verilerin yetkisiz değişikliklere karşı korunduğu doğrulanmalıdır. Tercihen bu koruma, onaylı bir kimliği doğrulanmış şifreleme yöntemi kullanılarak ya da onaylı bir şifreleme yöntemi ile onaylı bir MAC algoritmasının kombinasyonu ile sağlanmalıdır. | 2 |
| **11.3.4** | Sayılar, başlatma vektörleri (IV) ve diğer tek kullanımlık değerlerin, aynı şifreleme anahtarı ve veri öğesi çifti için birden fazla kez kullanılmadığı doğrulanmalıdır. Oluşturma yöntemi kullanılan algoritmaya uygun olmalıdır. | 3 |
| **11.3.5** | Şifreleme algoritması ve MAC algoritması kombinasyonlarının "encrypt-then-MAC" modunda çalıştığı doğrulanmalıdır. | 3 |


## V11.4 Hashing ve Hash Temelli Fonksiyonlar

Kriptografik hash'ler, dijital imzalar, HMAC, anahtar türetme fonksiyonları (KDF), rastgele bit üretimi ve parola saklama gibi çok çeşitli kriptografik protokollerde kullanılır. Kriptografik sistemin güvenliği, kullanılan hash fonksiyonlarının güvenliği ile doğrudan ilişkilidir. Bu bölüm, kriptografik işlemlerde güvenli hash fonksiyonlarının kullanımına dair gereksinimleri özetler.

Parola saklama ve kriptografi ile ilgili ek için [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms) belgesi de fayda ve rehberlik sağlar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **11.4.1** | Dijital imzalar, HMAC, KDF ve rastgele bit üretimi gibi genel kriptografik kullanım senaryolarında yalnızca onaylı hash fonksiyonlarının kullanıldığı doğrulanmalıdır. MD5 gibi yasaklı hash fonksiyonları hiçbir kriptografik amaçla kullanılmamalıdır. | 1 |
| **11.4.2** | Parolaların, onaylı, hesaplama açısından yoğun ve mevcut rehberliğe göre yapılandırılmış bir anahtar türetme fonksiyonu (diğer adıyla parola hash'leme fonksiyonu) kullanılarak saklandığı doğrulanmalıdır. Ayarlar, güvenlik ve performans dengesini sağlayarak kaba kuvvet saldırılarını zorlaştırmalıdır. | 2 |
| **11.4.3** | Dijital imzalarda kullanılan hash fonksiyonlarının, veri bütünlüğü ve kimlik doğrulama amacıyla kullanıldığında çakışmaya karşı dayanıklı ve yeterli bit uzunluğuna sahip olduğu doğrulanmalıdır. Çakışma dayanıklılığı gerekiyorsa çıktı uzunluğu en az 256 bit olmalıdır. Sadece ikinci ön-görüntü (2nd pre-iamge) saldırılarına karşı dayanıklılık gerekiyorsa çıktı uzunluğu en az 128 bit olmalıdır. | 2 |
| **11.4.4** | Parolalardan gizli anahtarlar türetilirken, onaylı anahtar türetme fonksiyonlarının anahtar uzatma (key stretching) parametreleriyle birlikte kullanıldığı doğrulanmalıdır. Bu parametreler, kaba kuvvet saldırılarını önleyecek şekilde güvenlik ve performans dengesine sahip olmalıdır. | 2 |

## V11.5 Rastgele Değerler

Kriptografik olarak güvenli sözde rastgele sayı üretimini (Cryptographically secure Pseudo-random Number Generation - CSPRNG), doğru şekilde uygulamak son derece zordur. Genellikle, bir sistemdeki iyi entropi kaynakları aşırı kullanıldığında hızla tükenir. Düşük rastgelelik seviyesine sahip kaynaklar ise tahmin edilebilir anahtarlara ve sırların ortaya çıkmasına yol açabilir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **11.5.1** | Tahmin edilemez olması amaçlanan tüm rastgele sayıların ve dizelerin, CSPRNG ile oluşturulduğu ve en az 128 bit entropiye sahip olduğu doğrulanmalıdır. UUID'lerin bu koşulu dikkate almadığını unutmayın. | 2 |
| **11.5.2** | Kullanılan rastgele sayı üretim mekanizmasının, yoğun talep altında dahi güvenli çalışacak şekilde tasarlandığı doğrulanmalıdır. | 3 |

## V11.6 Açık Anahtar (Public Key) Kriptografisi

Birden fazla taraf arasında ortak bir sır paylaşımının mümkün olmadığı ya da arzu edilmediği durumlarda açık anahtar kriptografisi kullanılır.

Bu bağlamda, modern tehditlere karşı sistemin güvenliğini sağlamak için Diffie-Hellman ve Eliptik Eğri Diffie-Hellman (ECDH) gibi onaylı anahtar değişim mekanizmalarına ihtiyaç vardır. “Güvenli İletişim” bölümü, TLS için gereksinimleri sağlar; bu bölümdeki gereksinimler ise TLS dışındaki açık anahtar kriptografisi kullanım durumlarına yöneliktir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **11.6.1** | Anahtar üretimi, tohumlama (seeding) ve dijital imza üretimi ve doğrulama için yalnızca onaylı kriptografik algoritmalar ve çalışma modlarının kullanıldığı doğrulanmalıdır. Anahtar üretim algoritmaları, bilinen saldırılara karşı savunmasız anahtarlar üretmemelidir. Örneğin, Fermat çarpanlama yöntemine karşı savunmasız RSA anahtarları oluşturulmamalıdır. | 2 |
| **11.6.2** | Anahtar değişimi için yalnızca onaylı kriptografik algoritmaların kullanıldığı doğrulanmalıdır (örneğin Diffie-Hellman). Kullanılan parametrelerin güvenli olması gerektiğine dikkat edilmelidir. Bu, anahtar kurulum sürecine yönelik saldırıları önleyecek ve araya girme (adversary-in-the-middle) ya da kriptografik kırılmaları engelleyecektir. | 3 |

## V11.7 Kullanım Halindeki Verilerin Kriptografisi

Veri işlenirken korunması çok önemlidir. Tam bellek şifreleme, veri iletiminde şifreleme ve verilerin kullanımdan hemen sonra mümkün olan en kısa sürede şifrelenmesi gibi teknikler önerilir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **11.7.1** | Hassas verilerin kullanım sırasında korunmasını sağlamak amacıyla, yetkisiz kullanıcıların veya süreçlerin bu verilere erişmesini engelleyen tam bellek şifrelemesinin kullanıldığı doğrulanmalıdır. | 3 |
| **11.7.2** | Veri asgariyetinin sağlandığı, yani işleme sırasında mümkün olan en az miktarda verinin ortaya çıktığı ve verilerin kullanımdan hemen sonra veya mümkün olan en kısa sürede şifrelendiği doğrulanmalıdır. | 3 |

## Referanslar

Daha fazla bilgi için:

* [OWASP Web Security Testing Guide: Testing for Weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography)
* [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
