# V7 Oturum Yönetimi

## Kontrol Amacı

Oturum yönetim mekanizmaları, durum bilgisi olmayan iletişim protokolleri (örneğin HTTP) kullanılırken bile uygulamaların kullanıcı ve cihaz etkileşimlerini zaman içinde ilişkilendirmesini sağlar. Modern uygulamalar, farklı özelliklere ve amaçlara sahip birden fazla oturum belirteci kullanabilir. Güvenli bir oturum yönetim sistemi, saldırganların bir kurbanın oturumunu ele geçirmesini, kullanmasını veya kötüye kullanmasını önlemelidir. Oturumları yöneten uygulamaların aşağıdaki üst düzey oturum yönetimi gereksinimlerini karşılaması gerekir:

* Oturumlar her bireye özgüdür, tahmin edilemez veya paylaşılamaz.
* Oturumlar artık gerekmediğinde geçersiz kılınır ve inaktivite durumunda zaman aşımına uğrar.

Bu bölümdeki birçok gereksinim, yaygın tehditlere ve sıkça kötüye kullanılan kimlik doğrulama zayıflıklarına odaklanarak seçilmiş [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/) kontrolleriyle ilgilidir.

Belirli oturum yönetim mekanizmalarının bazı uygulama detaylarına ilişkin gereksinimler diğer bölümlerde yer almaktadır:

* HTTP Çerezleri, oturum belirteçlerini güvence altına almak için yaygın bir mekanizmadır. Çerezler için özel güvenlik gereksinimleri "Web Frontend Güvenliği" bölümünde bulunabilir.
* Kendinden içerikli token'lar, oturumları sürdürmenin yaygın yollarından biridir. Bu token'lara özel güvenlik gereksinimleri "Kendinden İçerikli Token'lar" bölümünde ele alınmıştır.

## V7.1 Oturum Yönetim Dokümantasyonu

Tüm uygulamalara uyan tek bir kalıp yoktur. Bu nedenle, tüm durumlara uygun evrensel sınırlar ve limitler tanımlamak mümkün değildir. Oturum yönetimi uygulama ve testine başlanmadan önce, oturum işleme ile ilgili güvenlik kararlarının belgelenmiş olduğu bir risk analizi yapılmalıdır. Bu, oturum yönetim sisteminin uygulamanın özel ihtiyaçlarına göre uyarlanmasını sağlar.

Durum bilgili ya da durumsuz (stateful ya da stateless) oturum mekanizması tercih edilse bile, analiz eksiksiz ve belgelenmiş olmalı ve seçilen çözümün ilgili tüm güvenlik gereksinimlerini karşılayabildiğini göstermelidir. Kullanılan herhangi bir Tek Oturum Açma (SSO) mekanizması ile olan etkileşim de değerlendirilmelidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **7.1.1** | Kullanıcının oturum inaktivite zaman aşımı süresi ve mutlak maksimum oturum süresinin belgelendiği, diğer kontrollerle birlikte uygun olduğu ve NIST SP 800-63B yeniden kimlik doğrulama gereksinimlerinden herhangi bir sapma varsa gerekçesinin belgede yer aldığı doğrulanmalıdır. | 2 |
| **7.1.2** | Belgede bir hesap için kaç adet eşzamanlı (paralel) oturuma izin verildiği ile birlikte, maksimum aktif oturum sayısına ulaşıldığında uygulanacak davranış ve işlemlerin tanımlandığı doğrulanmalıdır. | 2 |
| **7.1.3** | Birleşik kimlik yönetim ekosisteminin bir parçası olarak kullanıcı oturumu oluşturan ve yöneten tüm sistemlerin, oturum ömrü, sonlandırma ve yeniden kimlik doğrulama gerektiren diğer koşulların nasıl koordine edildiğini açıklayan kontrollerle birlikte belgede yer aldığı doğrulanmalıdır. | 2 |

## V7.2 Temel Oturum Yönetimi Güvenliği

Bu bölüm, oturum token'larının güvenli bir şekilde oluşturulup doğrulandığını teyit eden, güvenli oturumların temel gereksinimlerini içerir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **7.2.1** | Uygulamanın tüm oturum token'ı doğrulama işlemlerini güvenilir bir backend servisi aracılığıyla gerçekleştirdiği doğrulanmalıdır. | 1 |
| **7.2.2** | Uygulamanın, statik API gizli anahtarları veya sabit değerler yerine, oturum yönetimi için dinamik olarak oluşturulan kendi kendine yeterli veya referans token'ları kullandığı doğrulanmalıdır. | 1 |
| **7.2.3** | Uygulama kullanıcı oturumlarını temsil etmek için referans token'ları kullanıyorsa, bu token'ların benzersiz olduğu, kriptografik olarak güvenli bir sözde rastgele sayı üreteci (CSPRNG) kullanılarak üretildiği ve en az 128 bit entropiye sahip olduğu doğrulanmalıdır. | 1 |
| **7.2.4** | Uygulamanın, kullanıcı kimlik doğrulaması (yeniden kimlik doğrulama dahil) sırasında yeni bir oturum token'ı oluşturduğu ve mevcut oturum token'ını sonlandırdığı doğrulanmalıdır. | 1 |

## V7.3 Oturum Zaman Aşımı

Oturum zaman aşımı mekanizmaları, oturum gaspı (session hijacking) ve diğer oturum kötüye kullanımı biçimlerine karşı fırsat aralığını en aza indirmeyi amaçlar. Zaman aşımı süreleri, belgelenmiş güvenlik kararlarını karşılamalıdır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **7.3.1** | Risk analizi ve belgelenmiş güvenlik kararlarına göre yeniden kimlik doğrulamanın zorunlu kılınmasını sağlayacak şekilde bir hareketsizlik zaman aşımı bulunduğu doğrulanmalıdır. | 2 |
| **7.3.2** | Risk analizi ve belgelenmiş güvenlik kararlarına göre yeniden kimlik doğrulamanın zorunlu kılınmasını sağlayacak şekilde mutlak bir maksimum oturum süresi bulunduğu doğrulanmalıdır. | 2 |

## V7.4 Oturum Sonlandırma

Oturum sonlandırma işlemi, uygulamanın kendisi tarafından veya oturum yönetimi uygulama yerine SSO sağlayıcısı tarafından yürütülüyorsa SSO sağlayıcısı tarafından gerçekleştirilebilir. Bu bölümdeki gereksinimler değerlendirilirken SSO sağlayıcısının kapsam dahilinde olup olmadığına karar verilmesi gerekebilir çünkü bazı kontroller sağlayıcı tarafından yürütülüyor olabilir.

Oturum sonlandırma, yeniden kimlik doğrulamanın gerekli olmasını sağlamalı ve uygulama genelinde, birleşik oturum açma (varsa) ve tüm güvenen taraflar genelinde etkili olmalıdır.

Durum bilgili oturum mekanizmaları için sonlandırma tipik olarak oturumu backend tarafında geçersiz kılmayı içerir. Kendinden içerikli token'lar durumunda ise, bu token'ları geçersiz kılmak veya engellemek için ek önlemler gerekir; aksi halde bunlar süresi dolana kadar geçerli kalabilir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **7.4.1** | Oturum sonlandırma tetiklendiğinde (örneğin, çıkış yapıldığında veya süre dolduğunda), uygulamanın oturumun daha fazla kullanılmasına izin vermediği doğrulanmalıdır. Referans token'lar veya durum bilgili oturumlar için bu, oturum verilerinin uygulama arka ucunda geçersiz kılınması anlamına gelir. Kapsamlı token kullanan uygulamaların; sonlandırılmış token listesi tutmak, kullanıcıya özel tarih ve saatten önce oluşturulan token'ları reddetmek veya kullanıcıya özel imzalama anahtarını yenilemek gibi bir çözüm uygulaması gerekir. | 1 |
| **7.4.2** | Bir kullanıcı hesabı devre dışı bırakıldığında veya silindiğinde (örneğin bir çalışanın şirketten ayrılması), uygulamanın tüm aktif oturumları sonlandırdığı doğrulanmalıdır. | 1 |
| **7.4.3** | Herhangi bir kimlik doğrulama faktörünün başarılı bir şekilde değiştirilmesi veya kaldırılmasından (şifre sıfırlama veya kurtarma yoluyla yapılan değişiklikler dahil ve varsa MFA ayarları güncellemeleri dahil) sonra, uygulamanın diğer tüm aktif oturumları sonlandırma seçeneği sunduğu doğrulanmalıdır. | 2 |
| **7.4.4** | Kimlik doğrulama gerektiren tüm sayfalarda kolay erişilebilir ve görünür bir çıkış yap (logout) işlevi bulunduğu doğrulanmalıdır. | 2 |
| **7.4.5** | Uygulama yöneticilerinin, bireysel bir kullanıcının veya tüm kullanıcıların aktif oturumlarını sonlandırabilme yetkisine sahip olduğu doğrulanmalıdır. | 2 |

## V7.5 Oturum Kötüye Kullanımına Karşı Savunmalar

Bu bölüm, aktif oturumların ele geçirilmesi veya kötüye kullanılması riskini azaltmaya yönelik gereksinimleri içerir. Bu riskler, örneğin kimliği doğrulanmış bir kurbanın internet tarayıcısının, kurbanın oturumunu kullanarak bir eylemi gerçekleştirmeye zorlanması gibi vektörler aracılığıyla ortaya çıkabilir.

Bu bölümdeki gereksinimler değerlendirilirken "Kimlik Doğrulama" bölümündeki seviyeye özel yönergeler dikkate alınmalıdır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **7.5.1** | E-posta adresi, telefon numarası, MFA yapılandırması veya hesap kurtarmada kullanılan diğer bilgiler gibi kimlik doğrulamayı etkileyebilecek hassas hesap özniteliklerinde değişiklik yapılmadan önce uygulamanın tam yeniden kimlik doğrulama gerektirdiği doğrulanmalıdır. | 2 |
| **7.5.2** | Kullanıcıların, (en az bir faktörle yeniden kimlik doğrulama yaptıktan sonra) mevcut tüm aktif oturumları görüntüleyebilmesi ve sonlandırabilmesinin mümkün olduğu doğrulanmalıdır. | 2 |
| **7.5.3** | Uygulamanın, son derece hassas işlemler veya operasyonlar gerçekleştirilmeden önce en az bir faktörle ek kimlik doğrulaması veya ikincil bir doğrulama gerektirdiği doğrulanmalıdır. | 3 |

## V7.6 Birleşik Yeniden Kimlik Doğrulama

Bu bölüm, Güvenen Taraf (Relying Party – RP) veya Kimlik Sağlayıcı (Identity Provider – IdP) kodu yazanlar için geçerlidir. Bu gereksinimler [NIST SP 800-63C Federation & Assertions](https://pages.nist.gov/800-63-4/sp800-63c.html) (Federasyon ve Beyanlar) rehberinden türetilmiştir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **7.6.1** | Güvenen Taraf (RP) ile Kimlik Sağlayıcı (IdP) arasındaki oturum süresi ve oturum sonlandırma davranışlarının belgelenmiş olduğu ve, örneğin IdP kimlik doğrulama olayları arasında maksimum süreye ulaşıldığında yeniden kimlik doğrulamanın gerekli kılındığı doğrulanmalıdır. | 2 |
| **7.6.2** | Yeni bir oturum oluşturulmasının, kullanıcı onayı veya açık bir eylem gerektirdiği; kullanıcı etkileşimi olmaksızın yeni uygulama oturumlarının oluşturulmasının önlendiği doğrulanmalıdır. | 2 |

## Referanslar

Daha fazla bilgi için:

* [OWASP Web Security Testing Guide: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/06-Session_Management_Testing)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
