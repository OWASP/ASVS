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
| 2.3.1 | [GÜNCELLENDİ] Sistem tarafından oluşturulan ilk parolaların veya aktivasyon kodlarının güvenli bir şekilde rastgele üretildiğini, mevcut parola politikasına uygun olduğunu ve kısa bir süre içinde veya ilk kullanımdan sonra geçersiz hale geldiğini doğrulayın. Bu başlangıç şifreleri, uzun vadeli parola olarak kullanılmamalıdır. | 1 | 330 |  
| 2.3.2 | [SİLİNDİ, 2.2.4 İLE BİRLEŞTİRİLDİ] | | |  
| 2.3.3 | [GÜNCELLENDİ] Süresi dolacak kimlik doğrulama mekanizmalarının yenilenmesine yönelik talimatların, kullanıcıların eski kimlik doğrulama mekanizmasının süresi dolmadan önce işlemi tamamlayabilmesi için yeterli süre öncesinde gönderildiğini doğrulayın. Gerekirse otomatik hatırlatmaların yapılandırıldığını kontrol edin. | 2 | 287 |  
| 2.3.4 | [EKLENDİ] Yönetici kullanıcıların, bir kullanıcının parola sıfırlama sürecini başlatabilmesini ancak kullanıcının parolasını değiştiremeyeceğini veya yeni bir parola belirleyemeyeceğini doğrulayın. Bu, yöneticilerin kullanıcının parolasını bilmesini engellemek için gereklidir. | 1 | 620 |  

## V2.4 Kimlik Bilgisi Depolama

Architects and developers should adhere to this section when building or refactoring code.

The current list of approved password hashing algorithms is detailed in NIST SP 800-63B section 5.1.1.2, and in the [OWASP Password Storage Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms). Pay careful attention to the configuration guidance to be aware of any implementation challenges or limits with each algorithm. At time of writing, Argon2id is the prefered password hashing algorithm, based on its resistance to side-channel attacks and its customizable memory, CPU, and parallelism parameters.

In particular, note that since these algorithms are intentionally compute-intensive, there have been cases in the past where providing a very long password leads to a denial of service condition. It is therefore very important to protect against this.

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **2.4.1** | [MOVED TO 6.6.2] | | |
| **2.4.2** | [DELETED, INCORRECT] | | |
| **2.4.3** | [DELETED, MERGED TO 6.6.2] | | |
| **2.4.4** | [DELETED, MERGED TO 6.6.2] | | |
| **2.4.5** | [DELETED, INCORRECT] | | |

## V2.5 Credential Recovery

The requirements in this section mostly relate to [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) or [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **2.5.1** | [DELETED, INCORRECT] | | |
| **2.5.2** | [GRAMMAR] Verify that password hints or knowledge-based authentication (so-called "secret questions") are not present. | 1 | 640 |
| **2.5.3** | [DELETED, COVERED BY 6.6.2] | | |
| **2.5.4** | [MOVED TO 14.1.10] | | |
| **2.5.5** | [DELETED, COVERED BY 2.2.3] | | |
| **2.5.6** | [MODIFIED] Verify that a secure process for resetting a forgotten password is implemented, that does not bypass any enabled multi-factor authentication mechanisms. | 1 | 640 |
| **2.5.7** | [GRAMMAR, LEVEL L2 > L1] Verify that if OTP or other multi-factor authentication factors are lost, that evidence of identity proofing is performed at the same level as during enrollment. | 1 | 308 |

## V2.6 General Multi-factor authentication requirements

This section provides general guidance that will be relevant to various different multi-factor authentication methods.

The mechanisms include:

* Lookup Secrets
* Time based One-time Passwords (TOTPs)
* Out-of-Band mechanisms

Lookup secrets are pre-generated lists of secret codes, similar to Transaction Authorization Numbers (TAN), social media recovery codes, or a grid containing a set of random values. This type of authentication mechanism is considered "something you have" since the codes are random so you need to have stored them somewhere.

Time based One-time Passwords (TOTPs) are physical or soft tokens that display a continually changing pseudo-random one-time challenge. This type of authentication mechanism is considered "something you have". Multi-factor TOTPs are similar to single-factor TOTPs, but require a valid PIN code, biometric unlocking, USB insertion or NFC pairing or some additional value (such as transaction signing calculators) to be entered to create the final OTP.

More details on out-of-band mechanisms will be provided in a subsequent section.

The requirements in these sections mostly relate to [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators), and [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **2.6.1** | [MODIFIED, MERGED FROM 2.8.4, SPLIT FROM 2.7.3, COVERS 2.2.6] Verify that lookup secrets, out-of-band authentication requests or codes, and time-based, one-time passwords (TOTPs) are only usable once. | 2 | 308 |
| **2.6.2** | [MODIFIED, SPLIT TO 2.6.4] Verify that, when being stored in the application's back-end, lookup secrets with less than 112 bits of entropy (19 random alphanumeric characters or 34 random digits) are hashed with an approved password storage hashing algorithm that incorporates a 32-bit random salt. A standard hash function can be used if the secret has 112 bits of entropy or more. | 2 | 330 |
| **2.6.3** | [MODIFIED, MERGED FROM 2.8.3, SPLIT FROM 2.7.6] Verify that lookup secrets, out-of-band authentication code, and time-based, one-time password seeds, are generated using a Cryptographically Secure Pseudorandom Number Generator (CSPRNG) to avoid predictable values. | 2 | 310 |
| **2.6.4** | [ADDED, SPLIT FROM 2.6.2, 2.7.6] Verify that lookup secrets and out-of-band authentication codes have a minimum of 20 bits of entropy (typically 4 random alphanumeric characters or 6 random digits is sufficient). | 2 | 330 |
| **2.6.5** | [MODIFIED, MOVED FROM 2.7.2, MERGED FROM 2.8.1] Verify that out-of-band authentication requests, codes, or tokens, as well as time-based, one-time passwords (TOTPs) have a defined lifetime. For out of band this should be 10 minutes and for TOTP this should be as short as possible, usually 30 seconds. | 1 | 287 |
| **2.6.6** | [MODIFIED, MOVED FROM 2.8.6, LEVEL L2 > L3] Verify that any authentication factor (including physical devices) can be revoked in case of theft or other loss. | 3 | 613 |
| **2.6.7** | [MODIFIED, MOVED FROM 2.8.7, LEVEL L2 > L3] Verify that biometric authentication mechanisms are only used as secondary factors together with either something you have or something you know. | 3 | 308 |
| **2.6.8** | [ADDED] Verify that time-based OTPs are checked based on a time source from a trusted service and not from an untrusted or client provided time. | 3 | 367 |

## V2.7 Out-of-Band authentication mechanisms

This will generally involve the authentication server communicating with a physical device over a secure secondary channel. Examples include push notifications to mobile devices and One-time Passwords (OTPs) sent to a user via SMS. This type of authentication mechanism is considered "something you have".

Unsafe out-of-band authentication mechanisms such as e-mail and VOIP are not permitted. PSTN and SMS authentication are currently "restricted" by NIST and should be deprecated in favor of push notifications or similar. If you need to use telephone or SMS out-of-band authentication, please see NIST SP 800-63B [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network).

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **2.7.1** | [MODIFIED] Verify that authentication mechanisms using the Public Switched Telephone Network (PSTN) to deliver One-time Passwords (OTPs) via phone or SMS are offered only when alternate stronger methods (such as push notifications) are also offered and when the service provides information on their security risks to users. | 1 | 287 |
| **2.7.2** | [MOVED TO 2.6.5]  | | |
| **2.7.3** | [MODIFIED, SPLIT TO 2.6.1] Verify that out-of-band authentication requests, codes, or tokens are only usable for the original authentication request for which they were generated and not a previous or subsequent one. | 1 | 287 |
| **2.7.4** | [DELETED, NOT IN SCOPE] | | |
| **2.7.5** | [DELETED, INSUFFICIENT IMPACT] | | |
| **2.7.6** | [SPLIT TO 2.6.3, 2.6.4] | | |
| **2.7.7** | [ADDED] Verify that a code based out-of-band authentication mechanism is protected against brute force attacks by using either rate limiting or a code with at least 64 bits of entropy. | 2 | 307 |
| **2.7.8** | [ADDED] Verify that, where push notifications are used for multi-factor authentication, rate limiting or number matching is used to prevent push bombing attacks. | 3 | |

## V2.8 Time based One-time Passwords

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **2.8.1** | [DELETED, MERGED TO 2.6.5] | | |
| **2.8.2** | [DELETED, COVERED BY 14.8.1] | | |
| **2.8.3** | [DELETED, MERGED TO 2.6.3] | | |
| **2.8.4** | [DELETED, MERGED TO 2.6.1] | | |
| **2.8.5** | [DELETED, INSUFFICIENT IMPACT] | | |
| **2.8.6** | [MOVED TO 2.6.6] | | |
| **2.8.7** | [MOVED TO 2.6.7] | | |

## V2.9 Cryptographic authentication mechanism

Cryptographic authentication mechanism include smart cards or FIDO keys, where the user has to plug in or pair the cryptographic device to the computer to complete authentication. The authenticatoin server will send a challenge nonce to the cryptographic device or software, and the device or software calculates a response based upon a securely stored cryptographic key.

The requirements for single-factor cryptographic devices and software, and multi-factor cryptographic devices and software are the same, as verification of the cryptographic device proves possession of the authentication factor. Where shared or secret keys are used for cryptographic authentication, these should be stored using the same mechanisms as other system secrets, as documented in the "Secret Management" section in the "Configuration" chapter.

The requirements in this section mostly relate to [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) of [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **2.9.1** | [MODIFIED, SPLIT TO 14.8.1, LEVEL L2 > L3] Verify that the certificates used to verify cryptographic authentication assertions are stored in a way protects them from modification. | 3 | 320 |
| **2.9.2** | [LEVEL L2 > L3] Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device. | 3 | 330 |
| **2.9.3** | [MODIFIED, LEVEL L2 > L3] Verify that approved cryptographic algorithms are used in the generation, seeding, and verification of the cryptographic keys. | 3 | 327 |

## V2.10 Service Authentication

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **2.10.1** | [MOVED TO 14.7.1] | | |
| **2.10.2** | [MOVED TO 14.7.2] | | |
| **2.10.3** | [DELETED, COVERED BY 14.8.1] | | |
| **2.10.4** | [DELETED, MERGED TO 14.8.1] | | |

## V2.11 Authentication with an Identity Providers

Secure use of external identity providers requires careful configuration and verification to prevent identity spoofing or forged assertions. This section provides requirements to address these risks.

| # | Description | Level | CWE |
| :---: | :--- | :---: | :---: |
| **2.11.1** | [ADDED] Verify that, if the application supports multiple identity providers (IDPs), the user's identity cannot be spoofed via another supported identity provider (eg. by using the same user identifier). Usually, the application should register and identify the user using a combination of the IdP ID (serving as a namespace) and the user's ID in the IDP. | 2 | |
| **2.11.2** | [ADDED] Verify that the presence and integrity of digital signatures on authentication assertions (for example on JWTs or SAML assertions) are always validated, rejecting any assertions that are unsigned or have invalid signatures. | 2 | |
| **2.11.3** | [ADDED] Verify that SAML assertions are uniquely processed and used only once within the validity period to prevent replay attacks. | 2 | |

## References

For more information, see also:

* [NIST SP 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST SP 800-63A - Enrollment and Identity Proofing](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST SP 800-63B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST SP 800-63C - Federation and Assertions](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST SP 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [OWASP Cheat Sheet - Password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Forgot password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Choosing and using security questions](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
* [CISA Guidance on "Number Matching"](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
