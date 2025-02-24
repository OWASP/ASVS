# V2 Kimlik Doğrulama

## Kontrolün Amacı

Kimlik doğrulama, bir bireyin veya cihazın kimliğinin belirlenmesi veya doğrulanması sürecidir. Bu süreç, bir kişinin veya cihazın sunduğu kimlik iddialarını doğrulamayı, taklit girişimlerine karşı dayanıklılığı sağlamayı ve parolaların ele geçirilmesini veya engellenmesini önlemeyi içerir.

Kanıta dayalı, etkili güvenlik uygulamalarını benimsemek birçok kuruluş için zorlayıcı olabilir ve bu tamamen normaldir. Ancak, artık parola sonrası bir geleceğe geçiş sürecini başlatmamız gerekiyor.

[NIST SP 800-63](https://pages.nist.gov/800-63-3/), modern, kanıta dayalı bir standart olup, her durumda uygulanabilir olmasa da mevcut en iyi önerileri sunmaktadır. Bu standart, dünya genelindeki tüm kuruluşlar için faydalı olsa da özellikle ABD kurumları ve ABD kurumlarıyla çalışan kuruluşlar için büyük önem taşımaktadır.

Bu bölümdeki gereksinimleri hazırlarken, NIST standardının ikinci bölümü olan ve NIST SP 800-63B "Dijital Kimlik Rehberi - Kimlik Doğrulama ve Yaşam Döngüsü Yönetimi" olarak bilinen bölüme başvurmak faydalı oldu.

Ancak, NIST SP 800-63 terminolojisi bazen farklı olabilmektedir. Bu nedenle, mümkün olduğunca daha yaygın olarak anlaşılan terimler kullanılarak bölümü daha anlaşılır hale getirmeye çalıştık.

Bu durum, bu bölümün NIST SP 800-63B’nin seçilmiş bir alt kümesiyle uyumlu olduğu anlamına gelirken, aynı zamanda yaygın tehditlere ve sıkça istismar edilen kimlik doğrulama zayıflıklarına odaklandığımızı gösterir. Tam NIST SP 800-63 uyumluluğunun gerekli olduğu durumlar için lütfen doğrudan NIST SP 800-63 standardına başvurun.


## V1.2 Kimlik Doğrulama Dokümantasyonu

<!-- Kimlik doğrulama sistemleri tasarlanırken, donanım destekli çok faktörlü kimlik doğrulamanın gücü, bir saldırganın çağrı merkezini arayıp yaygın olarak bilinen soruları yanıtlayarak bir hesabı kolayca sıfırlayabilmesi durumunda anlamsız hale gelir. Güvenli kimlik doğrulamanın sağlamak için tüm kimlik doğrulama yollarının eşit derecede güçlü olması gerekir. -->

| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **1.2.1** | [14.6.2'YE TAŞINDI] | | |  
| **1.2.2** | [SİLİNDİ, 14.7.1 İLE BİRLEŞTİRİLDİ] | | |  
| **1.2.3** | [SİLİNDİ, 1.2.4 TARAFINDAN KAPSANIYOR] | | |  
| **1.2.4** | [GÜNCELLENDİ, 2.2.11’E BÖLÜNDÜ, 1.2.3’Ü KAPSIYOR] Uygulama birden fazla kimlik doğrulama yolu içeriyorsa, bunların tamamının belgelenmiş olması ve her biri için güvenlik kontrollerinin ve kimlik doğrulama gücünün tutarlı bir şekilde uygulanmasının sağlanması gerektiğini doğrulayın. | 2 | 306 |  
| **1.2.5** | [EKLENDİ] Parolalarda kullanılmasını önlemek için bağlama özel kelimelerin bulunduğu bir listenin belgelenmiş olduğunu doğrulayın. | 2 | 521 |  
| **1.2.6** | [EKLENDİ, 2.2.1’DEN AYRILDI] Uygulama dokümantasyonunun, hız sınırlama (rate limiting), otomasyona karşı koruma (anti-automation) ve uyarlanabilir tepki (adaptive response) gibi kontrollerin, kimlik bilgisi doldurma (credential stuffing) ve parola kaba kuvvet (brute-force) saldırılarına karşı nasıl kullanıldığını tanımladığını doğrulayın. Dokümantasyonun, bu kontrollerin nasıl yapılandırıldığını ve kötü niyetli hesap kilitlemelerini nasıl önlediğini net bir şekilde açıklaması gerekir. | 1 | 307 |  

## V2.1 Parola Güvenliği

NIST SP 800-63 tarafından "Ezberlenmiş Sırlar" (Memorized Secrets) olarak adlandırılan parolalar; parolalar, PIN kodları, ekran kilidi desenleri, doğru kediyi veya başka bir görsel öğeyi seçme gibi yöntemler ve parola ifadelerini içerir. Genellikle "bildiğiniz bir şey" olarak kabul edilir ve çoğunlukla tek faktörlü kimlik doğrulama mekanizması olarak kullanılır. Ancak, tek faktörlü kimlik doğrulamanın kullanımıyla ilgili ciddi güvenlik riskleri bulunmaktadır. Bu riskler arasında, internete sızdırılmış milyarlarca geçerli kullanıcı adı ve parola, varsayılan veya zayıf parolalar, rainbow tabloları ve en yaygın parolaları içeren sıralı sözlükler bulunmaktadır.

Uygulamalar, kullanıcıları güçlü bir şekilde çok faktörlü kimlik doğrulamaya (MFA) kaydolmaya teşvik etmeli ve mevcutta sahip oldukları FIDO veya U2F token'leri gibi kimlik doğrulama araçlarını yeniden kullanmalarına izin vermelidir. Alternatif olarak, çok faktörlü kimlik doğrulama sağlayan bir kimlik doğrulama hizmeti sağlayıcısına (CSP) bağlanma imkanı sunulmalıdır.

Kimlik Doğrulama Hizmeti Sağlayıcıları (Credential Service Providers - CSPs), kullanıcılar için federasyonlu kimlik yönetimi sunar. Kullanıcılar genellikle birden fazla CSP ile ilişkili birden fazla kimliğe sahip olabilir. Örneğin, Azure AD, Okta, Ping Identity veya Google gibi kurumsal kimlik doğrulama sağlayıcılarını kullanabilirler ya da Facebook, Twitter, Google veya WeChat gibi platformlar üzerinden tüketici kimliği oluşturabilirler. Bu liste, belirtilen şirketleri veya hizmetleri onaylamak amacıyla verilmemiştir; yalnızca geliştiricilerin birçok kullanıcının halihazırda farklı kimlik sağlayıcılarına sahip olduğunu dikkate almasını teşvik etmek için sunulmuştur. Kuruluşlar, CSP'nin kimlik doğrulama güvenliğine ilişkin risk profiline göre mevcut kullanıcı kimlikleriyle entegrasyon sağlamayı düşünebilir. Örneğin, bir devlet kurumu, sahte veya geçici kimliklerin kolayca oluşturulabilmesi nedeniyle bir sosyal medya kimliğini hassas sistemlerine giriş yapmak için kabul etmeyebilir. Buna karşın, bir mobil oyun şirketi, aktif oyuncu tabanını büyütmek amacıyla büyük sosyal medya platformlarıyla entegrasyon sağlamaya ihtiyaç duyabilir.

Bu bölümdeki gereksinimlerin çoğu, [NIST Kılavuzu](https://pages.nist.gov/800-63-3/sp800-63b.html) içindeki [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) bölümüne dayanmaktadır.


| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **2.1.1** | [GÜNCELLENDİ] Kullanıcı tarafından belirlenen parolaların en az 8 karakter uzunluğunda olmasını doğrulayın; ancak en az 15 karakter kullanılması şiddetle tavsiye edilir. | 1 | 521 |  
| **2.1.2** | [GÜNCELLENDİ] En az 64 karakter uzunluğundaki parolalara izin verildiğini doğrulayın. | 1 | 521 |  
| **2.1.3** | [GÜNCELLENDİ] Uygulamanın, kullanıcının parolasını aldığı şekilde, herhangi bir değişiklik yapmadan (örneğin, kısaltma veya büyük/küçük harf dönüşümü olmadan) doğruladığını doğrulayın. | 1 | |  
| **2.1.4** | [SİLİNDİ, YETERSİZ ETKİ] | | |  
| **2.1.5** | [GRAMER DÜZELTİLDİ] Kullanıcıların parolalarını değiştirebileceğini doğrulayın. | 1 | 620 |  
| **2.1.6** | Parola değiştirme işlevinin, kullanıcının mevcut ve yeni parolasını girmesini gerektirdiğini doğrulayın. | 1 | 620 |  
| **2.1.7** | [GÜNCELLENDİ, 2.1.13’E BÖLÜNDÜ] Hesap kaydı veya parola değişikliği sırasında girilen parolaların en az en yaygın 3000 parola listesiyle karşılaştırılarak kontrol edildiğini doğrulayın. | 1 | 521 |  
| **2.1.8** | [SİLİNDİ, YETERSİZ ETKİ] | | |  
| **2.1.9** | Parola oluşturma kurallarının, belirli karakter türlerini zorunlu kılmadığını doğrulayın. Üst/büyük harf, küçük harf, rakam veya özel karakter kullanımı zorunlu olmamalıdır. | 1 | 521 |  
| **2.1.10** | [GÜNCELLENDİ, SEVİYE L1 > L2] Kullanıcının parolasının, ancak güvenliği ihlal edildiğinde veya kullanıcı tarafından değiştirildiğinde geçersiz hale geldiğini doğrulayın. Uygulama, periyodik kimlik bilgisi değişimini zorunlu kılmamalıdır. | 2 | |  
| **2.1.11** | "Yapıştır" işlevinin, tarayıcı parola yöneticilerinin ve harici parola yöneticilerinin kullanımına izin verildiğini doğrulayın. | 1 | 521 |  
| **2.1.12** | [GÜNCELLENDİ] Parola giriş alanlarının girdi maskeleme (type=password) kullandığını doğrulayın. Uygulamalar, kullanıcının geçici olarak tüm maskelenmiş parolayı veya en son girilen karakteri görmesine izin verebilir.** | 1 | 549 |  
| **2.1.13** | [EKLENDİ, 2.1.7’DEN AYRILDI, SEVİYE L1 > L3] Hesap kaydı veya parola değişikliği sırasında girilen parolaların, ihlal edilmiş parolalar listesiyle karşılaştırılarak kontrol edildiğini doğrulayın. | 3 | |  
| **2.1.14** | [EKLENDİ] Belgelenmiş bağlama özgü kelime listelerinin, tahmin edilmesi kolay parolaların oluşturulmasını engellemek için kullanıldığını doğrulayın. | 2 | 521 |  

Sık kullanılan parolaların gereksinim 2.1.7 için kullanılabilecek kaynakları:

* <https://github.com/danielmiessler/SecLists/tree/master/Passwords>
* <https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt>

## V2.2 Genel Kimlik Doğrulama Güvenliği

Kimlik doğrulama faktörü esnekliği, uygulamaların geleceğe uyum sağlaması açısından kritik öneme sahiptir. Uygulamalar, kullanıcı tercihlerine bağlı olarak ek güvenli kimlik doğrulama faktörlerinin kullanımına izin vermeli ve aynı zamanda eski veya güvensiz kimlik doğrulama mekanizmalarını aşamalı olarak devre dışı bırakmalıdır.

NIST, SMS tabanlı kimlik doğrulamayı ["kısıtlı" bir kimlik doğrulama mekanizması](https://pages.nist.gov/800-63-FAQ/#q-b01) olarak değerlendirmektedir ve gelecekte NIST SP 800-63'ten, dolayısıyla ASVS’den kaldırılması muhtemeldir. Bu belge yazıldığı sırada henüz kaldırılmamış olsa da, uygulamaların SMS kullanımı gerektirmeyen bir yol haritası planlaması önerilmektedir.

NIST SP 800-63, e-posta tabanlı kimlik doğrulamayı [kabul edilemez](https://pages.nist.gov/800-63-FAQ/#q-b11) olarak değerlendirmektedir.

Bu bölümdeki gereksinimler, [NIST Kılavuzu](https://pages.nist.gov/800-63-3/sp800-63b.html) içindeki çeşitli bölümlerle ilgilidir: [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling) ve [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding).


| # | Açıklama | Seviye | CWE |
| :---: | :--- | :---: | :---: |
| **2.2.1** | [GÜNCELLENDİ, 1.2.6'YA BÖLÜNDÜ] Kimlik bilgisi doldurma (credential stuffing) ve parola brute-force saldırılarını önlemek için güvenlik dokümantasyonunda belirtilen kontrollerin uygulandığını doğrulayın. | 1 | 307 |
| **2.2.2** | [GÜNCELLENDİ] E-postanın tek faktörlü veya çok faktörlü kimlik doğrulama mekanizması olarak kullanılmadığını doğrulayın. | 1 | 304 |
| **2.2.3** | [GÜNCELLENDİ, 2.2.10’A BÖLÜNDÜ, 2.5.5'İ KAPSIYOR] Kullanıcılara, kimlik bilgisi sıfırlama veya kullanıcı adı/e-posta adresi değişikliği gibi kimlik doğrulama bilgileri güncellendikten sonra bildirim gönderildiğini doğrulayın. | 1 | 778 |
| **2.2.4** | [GÜNCELLENDİ, 2.2.9’A BÖLÜNDÜ, 2.2.7 VE 2.3.2 İLE BİRLEŞTİRİLDİ] Kimlik avı (phishing) saldırılarına karşı taklit koruması sağlayan (örn. WebAuthn gibi) ve kullanıcının kimlik doğrulama amacını açıkça belirlemesini gerektiren (örn. bir FIDO donanım anahtarında düğmeye basma) donanım tabanlı kimlik doğrulama mekanizmalarının desteklendiğini doğrulayın. | 3 | 308 |
| **2.2.5** | [9.3.3’E TAŞINDI] | | |
| **2.2.6** | [SİLİNDİ, 2.6.1 TARAFINDAN KAPSANIYOR] | | |
| **2.2.7** | [SİLİNDİ, 2.2.4 İLE BİRLEŞTİRİLDİ] | | |
| **2.2.8** | [EKLENDİ] Geçersiz kimlik doğrulama girişimlerinden, hata mesajları, HTTP yanıt kodları veya farklı yanıt süreleri gibi yöntemlerle geçerli kullanıcıların belirlenemediğini doğrulayın. Bu koruma, kayıt ve parola sıfırlama işlevleri için de uygulanmalıdır. | 3 | |
| **2.2.9** | [EKLENDİ, 2.2.4’TEN BÖLÜNDÜ] Uygulamanın, kullanıcılardan ya çok faktörlü kimlik doğrulama mekanizmaları kullanmasını ya da birden fazla tek faktörlü kimlik doğrulama mekanizmasını bir arada kullanmasını gerektirdiğini doğrulayın. | 2 | 308 |
| **2.2.10** | [EKLENDİ, 2.2.3’TEN BÖLÜNDÜ] Kullanıcılara şüpheli kimlik doğrulama girişimleri hakkında bildirim gönderildiğini doğrulayın. Bu bildirimler; bilinmeyen bir konum veya istemciden yapılan başarılı veya başarısız kimlik doğrulama girişimleri, birden fazla faktör gerektiren bir sistemde yalnızca tek bir faktörle kısmen başarılı kimlik doğrulama girişimleri, uzun süre etkin olmayan bir hesapta yapılan başarılı veya başarısız kimlik doğrulama girişimleri ve birden fazla başarısız denemenin ardından başarılı kimlik doğrulama girişimlerini içerebilir. | 2 | 778 |      
| **2.2.11** | [EKLENDİ, 1.2.4’TEN BÖLÜNDÜ] Uygulama birden fazla kimlik doğrulama yolu içeriyorsa, belgelenmemiş kimlik doğrulama yollarının bulunmadığını ve güvenlik kontrollerinin tutarlı bir şekilde uygulandığını doğrulayın. | 2 | 306 |

## V2.3 Kimlik Doğrulama Faktörü Yaşam Döngüsü

Kimlik doğrulama mekanizmaları; parolalar, yazılım (soft) token'ları, donanım (hardware) token'ları ve biyometrik cihazları içerebilir. Bu kimlik doğrulama mekanizmalarının yaşam döngüsü, bir uygulamanın güvenliği açısından kritik öneme sahiptir - eğer herhangi biri, kimliğine dair herhangi bir kanıt sunmadan kendi kendine bir hesap oluşturabiliyorsa, kimlik iddiasına olan güven oldukça düşük olacaktır. Reddit gibi sosyal medya siteleri için bu durum tamamen kabul edilebilir. Bankacılık sistemleri için ise kimlik doğrulama bilgileri ve cihazlarının kaydı ve dağıtımı sürecine daha fazla önem verilmesi çok önemlidir.


Not: Parolaların maksimum kullanım süresi olmamalıdır veya zorunlu parola değişimi (rotation) uygulanmamalıdır. Parolaların düzenli olarak değiştirilmesi yerine, ihlal edilip edilmediği kontrol edilmelidir.

| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **2.3.1** | [GÜNCELLENDİ] Sistem tarafından oluşturulan ilk parolaların veya aktivasyon kodlarının güvenli bir şekilde rastgele üretildiğini, mevcut parola politikasına uygun olduğunu ve kısa bir süre içinde veya ilk kullanımdan sonra geçersiz hale geldiğini doğrulayın. Bu başlangıç şifreleri, uzun vadeli parola olarak kullanılmamalıdır. | 1 | 330 |  
| **2.3.2** | [SİLİNDİ, 2.2.4 İLE BİRLEŞTİRİLDİ] | | |  
| **2.3.3** | [GÜNCELLENDİ] Süresi dolacak kimlik doğrulama mekanizmalarının yenilenmesine yönelik talimatların, kullanıcıların eski kimlik doğrulama mekanizmasının süresi dolmadan önce işlemi tamamlayabilmesi için yeterli süre öncesinde gönderildiğini doğrulayın. Gerekirse otomatik hatırlatmaların yapılandırıldığını kontrol edin. | 2 | 287 |  
| **2.3.4** | [EKLENDİ] Yönetici kullanıcıların, bir kullanıcının parola sıfırlama sürecini başlatabilmesini ancak kullanıcının parolasını değiştiremeyeceğini veya yeni bir parola belirleyemeyeceğini doğrulayın. Bu, yöneticilerin kullanıcının parolasını bilmesini engellemek için gereklidir. | 1 | 620 |  

## V2.4 Kimlik Bilgisinin Depolanması

Mimarlar ve geliştiriciler, yeni kod oluştururken veya mevcut kodu yeniden yapılandırırken bu bölüme bağlı kalmalıdır.

Mevcut onaylanmış parola hash'leme algoritmalarının listesi, NIST SP 800-63B bölüm 5.1.1.2 ve [OWASP Parola Depolama Hatırlatma Notu](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms) belgelerinde ayrıntılı olarak açıklanmıştır. Her algoritmanın uygulanmasıyla ilgili potansiyel zorluklar veya sınırlamalar hakkında farkındalık sağlamak için yapılandırma rehberine özellikle dikkat edilmelidir. Bu belge yazıldığı sırada, Argon2id en çok önerilen parola hash'leme algoritmasıdır. Yan kanal saldırılarına (side-channel attacks) karşı direnci ve bellek, CPU kullanımı ve paralellik parametrelerinin özelleştirilebilir olması nedeniyle tercih edilmektedir.

Özellikle dikkate alınması gereken bir nokta, bu algoritmaların bilinçli olarak hesaplama açısından yoğun (compute-intensive) olarak tasarlandığıdır. Geçmişte, çok uzun parolaların işlenmesinin hizmet aksatma (Denial of Service - DoS) koşullarına yol açtığı bazı vakalar yaşanmıştır. Bu nedenle, sistemin bu tür saldırılara karşı korunduğundan emin olmak büyük önem taşımaktadır.

| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **2.4.1** | [6.6.2'YE TAŞINDI] | | |  
| **2.4.2** | [SİLİNDİ, HATALI BİLGİ] | | |  
| **2.4.3** | [SİLİNDİ, 6.6.2 İLE BİRLEŞTİRİLDİ] | | |  
| **2.4.4** | [SİLİNDİ, 6.6.2 İLE BİRLEŞTİRİLDİ] | | |  
| **2.4.5** | [SİLİNDİ, HATALI BİLGİ] | | |  

## V2.5 Kimlik Bilgisinin Kurtarılması

Bu bölümdeki gereksinimlerin çoğu, [NIST Kılavuzu](https://pages.nist.gov/800-63-3/sp800-63b.html) içindeki [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) veya [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) bölümleriyle ilgilidir.

| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **2.5.1** | [SİLİNDİ, HATALI BİLGİ] | | |  
| **2.5.2** | [GRAMER DÜZELTİLDİ] Parola ipuçlarının (password hints) veya bilgi tabanlı kimlik doğrulamanın ("gizli sorular") kullanılmadığını doğrulayın. | 1 | 640 |  
| **2.5.3** | [SİLİNDİ, 6.6.2 TARAFINDAN KAPSANIYOR] | | |  
| **2.5.4** | [14.1.10’A TAŞINDI] | | |  
| **2.5.5** | [SİLİNDİ, 2.2.3 TARAFINDAN KAPSANIYOR] | | |  
| **2.5.6** | [GÜNCELLENDİ] Unutulan parolaların sıfırlanması için güvenli bir sürecin uygulandığını ve bu sürecin etkinleştirilmiş herhangi bir çok faktörlü kimlik doğrulama mekanizmasını atlamadığını doğrulayın. | 1 | 640 |  
| **2.5.7** | [GRAMER DÜZELTİLDİ, SEVİYE L2 > L1] Tek kullanımlık parola (OTP) veya diğer çok faktörlü kimlik doğrulama faktörleri kaybolduğunda, kimlik doğrulama sürecinin, kaydolma sırasında uygulanan kimlik doğrulama seviyesiyle aynı düzeyde kanıt talep ettiğini doğrulayın. | 1 | 308 |  

## V2.6 Genel Çok Faktörlü Kimlik Doğrulama Gereksinimleri

Bu bölüm, çeşitli çok faktörlü kimlik doğrulama (MFA) yöntemleri ile ilgili genel yönergeleri içermektedir.

Bu mekanizmalar şunları içerir:

* Önceden oluşturulmuş gizli kodlar (Lookup Secrets)
* Zaman tabanlı tek kullanımlık parolalar (TOTP - Time-based One-Time Passwords)
* Bant dışı (Out-of-Band) kimlik doğrulama mekanizmaları

Lookup secrets, önceden oluşturulmuş rastgele gizli kodlardan oluşan listelerdir. İşlem Yetkilendirme Numaraları (TAN - Transaction Authorization Numbers), sosyal medya hesap kurtarma kodları veya rastgele değerlerden oluşan bir yerleşim bu kategoriye girer. Bu tür kimlik doğrulama mekanizmaları "sahip olduğunuz bir şey" olarak değerlendirilir, çünkü kodlar rastgeledir ve bunları bir yerde saklamış olmanız gerekir.

Zaman tabanlı tek kullanımlık parolalar (TOTP), fiziksel veya yazılım tabanlı token'lar aracılığıyla sürekli değişen, sözde-rastgele (pseudo-random) bir kimlik doğrulama kodu üretir. Bu tür kimlik doğrulama mekanizmaları "sahip olduğunuz bir şey" olarak kabul edilir. Çok faktörlü TOTP yöntemleri, tek faktörlü TOTP yöntemlerine benzer ancak geçerli bir PIN kodu, biyometrik doğrulama, USB takma veya NFC eşleştirme gibi ek bir değer gerektirir. Örneğin, işlem imzalama hesaplayıcıları (transaction signing calculators) ek bir doğrulama faktörü olarak kullanılabilir.

Bant dışı (Out-of-Band) kimlik doğrulama mekanizmaları hakkında daha fazla ayrıntı sonraki bölümlerde verilecektir.

Bu bölümdeki gereksinimler, [NIST Kılavuzu](https://pages.nist.gov/800-63-3/sp800-63b.html) içindeki [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators) ve [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) bölümleriyle ilgilidir.

| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **2.6.1** | [GÜNCELLENDİ, 2.8.4 İLE BİRLEŞTİRİLDİ, 2.7.3’TEN AYRILDI, 2.2.6’YI KAPSIYOR] Lookup secrets, bant dışı kimlik doğrulama kodları veya zaman tabanlı tek kullanımlık parolaların (TOTP) yalnızca bir kez kullanılabildiğini doğrulayın. | 2 | 308 |  
| **2.6.2** | [GÜNCELLENDİ, 2.6.4’E AYRILDI] Uygulamanın arka ucunda (backend) saklanan lookup secrets, 112 bitten daha az entropiye (rastgelelik seviyesine) sahipse, onaylanmış bir parola hash'leme algoritması kullanılarak 32 bit rastgele salt ile hash'lenmesi gerektiğini doğrulayın. Eğer gizli kod 112 bit veya daha fazla entropiye sahipse, standart bir hash fonksiyonu kullanılabilir. | 2 | 330 |  
| **2.6.3** | [GÜNCELLENDİ, 2.8.3 İLE BİRLEŞTİRİLDİ, 2.7.6’DAN AYRILDI] Lookup secrets, bant dışı kimlik doğrulama kodları ve TOTP kodlarının, tahmin edilebilir değerleri önlemek için Kriptografik Olarak Güvenli Bir Sahte Rastgele Sayı Üretici (CSPRNG) kullanılarak üretildiğini doğrulayın. | 2 | 310 |  
| **2.6.4** | [EKLENDİ, 2.6.2 VE 2.7.6’DAN AYRILDI] Lookup secrets ve bant dışı kimlik doğrulama kodlarının en az 20 bit entropiye sahip olduğunu doğrulayın (genellikle 4 rastgele alfasayısal karakter veya 6 rastgele rakam yeterlidir). | 2 | 330 |  
| **2.6.5** | [GÜNCELLENDİ, 2.7.2’DEN TAŞINDI, 2.8.1 İLE BİRLEŞTİRİLDİ] Bant dışı kimlik doğrulama isteklerinin, kodlarının veya token'larının yanı sıra TOTP'lerin belirli bir kullanım süresi (lifetime) olduğunu doğrulayın. Bant dışı kimlik doğrulama için süre 10 dakika olmalı, TOTP için ise genellikle 30 saniye olacak şekilde mümkün olduğunca kısa tutulmalıdır. | 1 | 287 |  
| **2.6.6** | [GÜNCELLENDİ, 2.8.6’DAN TAŞINDI, SEVİYE L2 > L3] Herhangi bir kimlik doğrulama faktörünün (fiziksel cihazlar dahil) çalınma veya kaybolma durumunda iptal edilebildiğini doğrulayın. | 3 | 613 |  
| **2.6.7** | [GÜNCELLENDİ, 2.8.7’DEN TAŞINDI, SEVİYE L2 > L3] Biyometrik kimlik doğrulama mekanizmalarının yalnızca ikincil faktör olarak kullanıldığını ve "sahip olduğunuz bir şey" veya "bildiğiniz bir şey" ile birlikte çalıştığını doğrulayın. | 3 | 308 |  
| **2.6.8** | [EKLENDİ] Zaman tabanlı tek kullanımlık parolaların (TOTP), güvenilir bir hizmetten sağlanan zaman kaynağına dayanarak kontrol edildiğini ve güvensiz veya istemci tarafından sağlanan bir zaman kaynağının kullanılmadığını doğrulayın. | 3 | 367 |  

## V2.7 Bant Dışı (Out-of-Band) Kimlik Doğrulama Mekanizmaları

Bu mekanizmalar genellikle, kimlik doğrulama sunucusunun güvenli ikincil bir kanal üzerinden fiziksel bir cihazla iletişim kurmasını içerir. Örnekler arasında mobil cihazlara gönderilen anlık bildirimler (push notifications) ve kullanıcılara SMS ile iletilen tek kullanımlık parolalar (OTP) yer alır. Bu tür kimlik doğrulama mekanizmaları "sahip olduğunuz bir şey" kategorisine girer.

Güvensiz bant dışı kimlik doğrulama mekanizmalarına, e-posta ve VOIP dahil değildir ve bunların kullanımı yasaktır. NIST, PSTN (Geleneksel Telefon Ağı) ve SMS kimlik doğrulamasını "kısıtlı" olarak sınıflandırmıştır ve bu yöntemlerin yerine anlık bildirimler (push notifications) gibi daha güvenli alternatiflerin kullanılması önerilmektedir. Telefon veya SMS tabanlı bir bant dışı kimlik doğrulaması kullanmanız gerekiyorsa, NIST SP 800-63B'nin [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network) bölümünü inceleyin..

| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **2.7.1** | [GÜNCELLENDİ] Geleneksel Telefon Ağı (PSTN) üzerinden telefon veya SMS yoluyla Tek Kullanımlık Parola (OTP) ile kimlik doğrulama mekanizmalarının yalnızca, daha güçlü alternatifler (örneğin anlık bildirimler) sunulduğunda ve hizmet sağlayıcının bu yöntemlerin güvenlik riskleri hakkında kullanıcıları bilgilendirdiğinde sunulduğunu doğrulayın. | 1 | 287 |  
| **2.7.2** | [2.6.5’E TAŞINDI] | | |  
| **2.7.3** | [GÜNCELLENDİ, 2.6.1’E BÖLÜNDÜ] Bant dışı kimlik doğrulama isteklerinin, kodlarının veya token'larının yalnızca oluşturuldukları orijinal kimlik doğrulama isteği için geçerli olduğunu ve önceki veya sonraki istekler için kullanılamadığını doğrulayın. | 1 | 287 |  
| **2.7.4** | [SİLİNDİ, KAPSAM DIŞI] | | |  
| **2.7.5** | [SİLİNDİ, YETERSİZ ETKİ] | | |  
| **2.7.6** | [2.6.3 VE 2.6.4’E BÖLÜNDÜ] | | |  
| **2.7.7** | [EKLENDİ] Kod tabanlı bant dışı kimlik doğrulama mekanizmasının, ya hız sınırlama (rate limiting) ya da en az 64 bit entropiye sahip bir kod kullanılarak kaba kuvvet saldırılarına karşı korunduğunu doğrulayın. | 2 | 307 |  
| **2.7.8** | [EKLENDİ] Çok faktörlü kimlik doğrulamada anlık bildirimler (push notifications) kullanılıyorsa, push bombing saldırılarını önlemek için hız sınırlama (rate limiting) veya sayı eşleştirme (number matching) gibi koruma mekanizmalarının uygulandığını doğrulayın. | 3 | |  

## V2.8 Zaman Tabanlı Tek Kullanımlık Parolalar (TOTP)  

| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **2.8.1** | [SİLİNDİ, 2.6.5 İLE BİRLEŞTİRİLDİ] | | |  
| **2.8.2** | [SİLİNDİ, 14.8.1 TARAFINDAN KAPSANIYOR] | | |  
| **2.8.3** | [SİLİNDİ, 2.6.3 İLE BİRLEŞTİRİLDİ] | | |  
| **2.8.4** | [SİLİNDİ, 2.6.1 İLE BİRLEŞTİRİLDİ] | | |  
| **2.8.5** | [SİLİNDİ, YETERSİZ ETKİ] | | |  
| **2.8.6** | [2.6.6’YA TAŞINDI] | | |  
| **2.8.7** | [2.6.7’YE TAŞINDI] | | |  

## V2.9 Kriptografik Kimlik Doğrulama Mekanizması  

Kriptografik kimlik doğrulama mekanizmaları, akıllı kartlar (smart cards) veya FIDO anahtarları gibi cihazları içerir. Kullanıcının kimlik doğrulamayı tamamlamak için kriptografik cihazı bilgisayara takması veya eşleştirmesi gerekir. Kimlik doğrulama sunucusu, kriptografik cihaza veya yazılıma bir "nonce" (rastgele bir doğrulama değeri) gönderir ve cihaz veya yazılım, güvenli bir şekilde saklanan bir kriptografik anahtar kullanarak bir yanıt hesaplar.

Tek faktörlü ve çok faktörlü kriptografik cihazlar/yazılımlar için gereksinimler aynıdır, çünkü kriptografik cihazın doğrulanması, kimlik doğrulama faktörüne sahip olunduğunu kanıtlar. Kriptografik kimlik doğrulama için kullanılan paylaşılan veya gizli anahtarlar, diğer sistem sırlarıyla aynı mekanizmalar kullanılarak saklanmalıdır. Bu mekanizmalar, "Sır Yönetimi" (Secret Management) bölümünde açıklanmıştır ve "Yapılandırma" (Configuration) bölümünde yer almaktadır.

Bu bölümdeki gereksinimler, [NIST Kılavuzu](https://pages.nist.gov/800-63-3/sp800-63b.html) içindeki [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) bölümüyle ilgilidir.

| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **2.9.1** | [GÜNCELLENDİ, 14.8.1’E BÖLÜNDÜ, SEVİYE L2 > L3] Kriptografik kimlik doğrulama iddialarını doğrulamak için kullanılan sertifikaların, değiştirilmesini önleyecek şekilde güvenli bir ortamda saklandığını doğrulayın. | 3 | 320 |  
| **2.9.2** | [SEVİYE L2 > L3] Kimlik doğrulama için kullanılan "nonce" (rastgele doğrulama değeri) en az 64 bit uzunluğunda olmalı ve kriptografik cihazın ömrü boyunca istatistiksel olarak benzersiz veya tamamen benzersiz olmalıdır. | 3 | 330 |  
| **2.9.3** | [GÜNCELLENDİ, SEVİYE L2 > L3] Kriptografik anahtarların oluşturulması, tohumlanması (seeding) ve doğrulanması için yalnızca onaylanmış kriptografik algoritmaların kullanıldığını doğrulayın. | 3 | 327 |  

## V2.10 Hizmet Kimlik Doğrulaması (Service Authentication)  

| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **2.10.1** | [14.7.1’E TAŞINDI] | | |  
| **2.10.2** | [14.7.2’YE TAŞINDI] | | |  
| **2.10.3** | [SİLİNDİ, 14.8.1 TARAFINDAN KAPSANIYOR] | | |  
| **2.10.4** | [SİLİNDİ, 14.8.1 İLE BİRLEŞTİRİLDİ] | | |  

## V2.11 Kimlik Sağlayıcıları (Identity Providers) ile Kimlik Doğrulama

Harici kimlik sağlayıcılarının (Identity Providers - IDP) güvenli bir şekilde kullanımı, kimlik sahtekarlığını veya sahte kimlik doğrulama iddialarını önlemek için dikkatli yapılandırma ve doğrulama gerektirir. Bu bölüm, bu riskleri ele almak için gereksinimleri içermektedir.

| # | Açıklama | Seviye | CWE |  
| :---: | :--- | :---: | :---: |  
| **2.11.1** | [EKLENDİ] Uygulama birden fazla kimlik sağlayıcısını (IDP) destekliyorsa, kullanıcının kimliğinin başka bir desteklenen kimlik sağlayıcı aracılığıyla (örneğin aynı kullanıcı tanımlayıcısını kullanarak) taklit edilemediğini doğrulayın. Genellikle, uygulamanın kullanıcıyı IDP kimliği (IDP ID) ve kullanıcı kimliği kombinasyonunu kullanarak kaydetmesi ve tanımlaması gerekir. | 2 | |  
| **2.11.2** | [EKLENDİ] Kimlik doğrulama iddialarının (örneğin JWT veya SAML iddialarının) dijital imzalarının varlığı ve bütünlüğünün her zaman doğrulandığını, imzasız veya geçersiz imzalı iddiaların reddedildiğini doğrulayın. | 2 | |  
| **2.11.3** | [EKLENDİ] SAML iddialarının benzersiz bir şekilde işlendiğini ve geçerlilik süresi içinde yalnızca bir kez kullanıldığını, yeniden yürütme saldırılarını (replay attacks) önlemek için doğrulayın. | 2 | |  


## Referanslar

Daha fazla bilgi için aşağıdaki kaynaklara bakabilirsiniz:

* [NIST SP 800-63 - Dijital Kimlik Yönergeleri](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST SP 800-63A - Kayıt ve Kimlik İspatlama](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST SP 800-63B - Kimlik Doğrulama ve Yaşam Döngüsü Yönetimi](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST SP 800-63C - Birleştirme ve Kimlik Doğrulama İddiaları](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST SP 800-63 SSS](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Test Kılavuzu 4.0: Kimlik Doğrulama Testi](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [OWASP Hatırlatma Notu - Parola Depolama](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Hatırlatma Notu - Parola Sıfırlama](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Hatırlatma Notu - Güvenlik Sorularının Seçilmesi ve Kullanımı](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
* ["Sayı Eşleştirme" Üzerine CISA Rehberi](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
