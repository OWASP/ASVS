# V6 Kimlik Doğrulama

## Kontrol Amacı

Kimlik doğrulama, bir kişinin ya da cihazın kimliğini kanıtlama veya doğrulama sürecidir. Bu süreç; bir kişi ya da cihaz hakkında yapılan iddiaların doğrulanmasını, taklit girişimlerine karşı dayanıklılığı ve parolaların ele geçirilmesine ya da dinlenmesine karşı korunmayı kapsar.

[NIST SP 800-63](https://pages.nist.gov/800-63-3/), özellikle ABD kurumları ve bu kurumlarla etkileşimde bulunanlar için geçerli olmakla birlikte, dünya çapında kuruluşlar için değerli olan modern ve kanıta dayalı bir standarttır.

Bu bölümdeki birçok gereksinim, söz konusu standardın ikinci bölümü olan NIST SP 800-63B "Dijital Kimlik Rehberi – Kimlik Doğrulama ve Yaşam Döngüsü Yönetimi" bölümünden esinlenmiştir. Ancak bu bölüm, yaygın tehditlere ve sıkça suistimal edilen kimlik doğrulama zayıflıklarına odaklanır; standardın tüm yönlerini kapsamaya çalışmaz. Tam NIST SP 800-63 uyumu gerekiyorsa, doğrudan bu belgeye başvurulmalıdır.

Ayrıca, NIST SP 800-63 terimleriyle bu bölümde kullanılan terimler zaman zaman farklılık gösterebilir. Bu bölümde, anlaşılırlığı artırmak amacıyla daha yaygın kullanılan terimler tercih edilmiştir.

Daha gelişmiş uygulamaların ortak bir özelliği, çeşitli risk faktörlerine bağlı olarak kimlik doğrulama aşamalarının uyarlanabilir şekilde yapılandırılabilmesidir. Bu özellik, yetkilendirme kararlarıyla da ilgili olduğundan "Yetkilendirme" bölümünde ele alınmıştır.

## V6.1 Kimlik Doğrulama Dokümantasyonu

Bu bölüm, bir uygulamada kimlik doğrulama ile ilgili tutulması gereken dokümantasyon gereksinimlerini içerir. Bu, ilgili kimlik doğrulama kontrollerinin nasıl yapılandırılması gerektiğini uygulamak ve değerlendirmek açısından kritik öneme sahiptir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **6.1.1** | Kimlik bilgisi doldurma (credential stuffing) ve parola kaba kuvvet saldırılarına karşı oran sınırlama (rate limiting), otomasyon karşıtı önlemler ve uyarlanabilir yanıt gibi kontrollerin nasıl kullanıldığını açıklayan bir uygulama dokümantasyonu bulunduğu doğrulanmalıdır. Dokümantasyon, bu kontrollerin nasıl yapılandırıldığını ve kötü niyetli hesap kilitlemenin nasıl önlendiğini açıkça ortaya koymalıdır. | 1 |
| **6.1.2** | Parolalarda kullanılmasını önlemek amacıyla, bağlama özgü sözcüklerin (örneğin kurum adlarının permütasyonları, ürün adları, sistem tanımlayıcıları, proje kod adları, departman veya rol adları vb.) bulunduğu belgelenmiş bir liste mevcut olduğu doğrulanmalıdır. | 2 |
| **6.1.3** | Uygulama birden fazla kimlik doğrulama yolu içeriyorsa, bunların tümünün belgelenmiş olduğu ve her yol için tutarlı şekilde uygulanması gereken güvenlik kontrolleri ile kimlik doğrulama gücünün tanımlandığı doğrulanmalıdır. | 2 |


## V6.2 Parola Güvenliği

Parolalar, NIST SP 800-63 tarafından "Ezberlenmiş Sırlar" (Memorized Secrets) olarak tanımlanır ve parolalar, parola öbekleri, PIN'ler, desen kilitleri ya da "doğru kedinin veya başka bir görsel öğenin seçilmesi" gibi yöntemleri kapsar. Genellikle "bildiğiniz bir şey" olarak kabul edilirler ve tek faktörlü kimlik doğrulamada yaygın olarak kullanılırlar.

Bu nedenle, bu bölüm parolaların güvenli şekilde oluşturulmasını ve işlenmesini sağlamak amacıyla oluşturulmuş gereksinimleri içerir. Gereksinimlerin çoğu Seviye 1’dedir çünkü temel düzeyde en önemli olanlardır. Seviye 2 ve sonrasında, çok faktörlü kimlik doğrulama mekanizmaları gereklidir ve parola bu faktörlerden yalnızca biri olabilir.

Bu bölümdeki gereksinimler büyük ölçüde [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html)'ın [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) kısmı ile ilişkilidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **6.2.1** | Kullanıcı tarafından belirlenen parolaların en az 8 karakter uzunluğunda olması sağlanmalı, ancak 15 karakter ve üzeri uzunlukta parolalar olmaları şiddetle tavsiye edilir. | 1 |
| **6.2.2** | Kullanıcıların parolalarını değiştirebilmeleri sağlanmalıdır. | 1 |
| **6.2.3** | Parola değiştirme işlevinin hem mevcut hem de yeni parolayı gerektirdiği doğrulanmalıdır. | 1 |
| **6.2.4** | Kayıt veya parola değişimi sırasında girilen parolaların, uygulamanın parola politikasına (örneğin minimum uzunluk) uyan ilk 3000 yaygın parolaya karşı kontrol edildiği doğrulanmalıdır. | 1 |
| **6.2.5** | Her tür karakterin kullanılmasına izin verildiği ve büyük/küçük harf, sayı veya özel karakter şartlarının zorunlu tutulmadığı doğrulanmalıdır. | 1 |
| **6.2.6** | Parola giriş alanlarının, girdiyi maskelemek için "type=password" kullandığı doğrulanmalıdır. Uygulamalar, kullanıcının tüm maskelenmiş parolayı ya da son girilen karakteri geçici olarak görüntülemesine izin verebilir. | 1 |
| **6.2.7** | "Yapıştır" özelliğinin, tarayıcı parola yardımcılarının ve harici parola yöneticilerinin kullanımına izin verildiği doğrulanmalıdır. | 1 |
| **6.2.8** | Uygulamanın, kullanıcıdan aldığı parolayı herhangi bir şekilde değiştirmeden, örneğin kesmeden veya harf büyüklüğünü değiştirmeden, tam olarak doğruladığı teyit edilmelidir. | 1 |
| **6.2.9** | En az 64 karakter uzunluğundaki parolalara izin verildiği doğrulanmalıdır. | 2 |
| **6.2.10** | Kullanıcının parolasının, yalnızca ele geçirildiği tespit edildiğinde veya kullanıcı tarafından yenilendiğinde geçerliliğini yitirdiği doğrulanmalıdır. Uygulama, belirli aralıklarla parola yenilenmesini zorunlu kılmamalıdır. | 2 |
| **6.2.11** | Tahmin edilmesi kolay parolaların oluşturulmasını önlemek amacıyla, bağlama özgü kelimelerin yer aldığı belgelenmiş listenin parola doğrulamada kullanıldığı teyit edilmelidir. | 2 |
| **6.2.12** | Kayıt veya parola değişikliği sırasında girilen parolaların, ele geçirilmiş parolalar listesine karşı kontrol edildiği doğrulanmalıdır. | 2 |

## V6.3 Genel Kimlik Doğrulama Güvenliği

Bu bölüm, kimlik doğrulama mekanizmalarının güvenliğine ilişkin genel gereksinimleri içerir ve farklı güvenlik seviyeleri için beklentileri ortaya koyar. Seviye 2 uygulamalarında çok faktörlü kimlik doğrulama (MFA) zorunlu olmalıdır. Seviye 3 uygulamalarında, donanım tabanlı, kanıtlanmış ve güvenli yürütme ortamında (Trusted Execution Environment - TEE) gerçekleştirilen kimlik doğrulama kullanılmalıdır. Bu, cihaza bağlı passkey’ler, eIDAS Yüksek Güvence Seviyesi (LoA High) zorunlu kimlik doğrulayıcılar, NIST Kimlik Doğrulayıcı Güvence Seviyesi 3 (AAL3) güvencesine sahip kimlik doğrulayıcılar veya eşdeğer mekanizmaları içerebilir.

Bu yaklaşım MFA konusunda oldukça katı bir duruş sergilese de, kullanıcıları korumak adına güvenlik seviyesini yükseltmek kritiktir. Bu gereksinimlerin gevşetilmesi yönündeki her girişim, kimlik doğrulama ile ilgili risklerin nasıl azaltılacağını açıkça ortaya koyan bir planla birlikte sunulmalıdır. Bu plan, NIST’in konuyla ilgili rehberleri ve araştırmalarını dikkate almalıdır.

Yayın tarihi itibarıyla, NIST SP 800-63 e-posta kullanımını bir kimlik doğrulama mekanizması olarak [kabul edilemez](https://pages.nist.gov/800-63-FAQ/#q-b11) olarak değerlendirmektedir ([arşivlenmiş kopya](https://web.archive.org/web/20250330115328/https://pages.nist.gov/800-63-FAQ/#q-b11)).

Bu bölümdeki gereksinimler, [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html)'ın [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling) ve [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding) bölümleriyle ilgilidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **6.3.1** | Kimlik bilgisi doldurma (credential stuffing) ve parola kaba kuvvet saldırıları gibi saldırıları önlemeye yönelik kontrollerin, uygulamanın güvenlik dokümantasyonuna göre uygulandığı doğrulanmalıdır. | 1 |
| **6.3.2** | "root", "admin" veya "sa" gibi varsayılan kullanıcı hesaplarının uygulamada yer almadığı veya devre dışı bırakıldığı doğrulanmalıdır. | 1 |
| **6.3.3** | Uygulamaya erişim için ya çok faktörlü bir kimlik doğrulama mekanizması ya da tek faktörlü mekanizmaların kombinasyonu kullanılmalıdır. Seviye 3 için, bu faktörlerden biri, oltalama saldırılarına karşı direnç sağlayan ve kimlik doğrulama niyetini bir kullanıcı etkileşimi (örneğin FIDO donanım anahtarında bir düğmeye basma veya mobil telefonda bir onay) gerektirerek doğrulayan donanım tabanlı bir kimlik doğrulayıcı olmalıdır. Bu gereksinimdeki herhangi bir esneklik için, gerekçesi belgelenmiş ve riskleri azaltıcı kapsamlı kontroller içeren bir plan gereklidir. | 2 |
| **6.3.4** | Uygulama birden fazla kimlik doğrulama yolu içeriyorsa, belgelendirilmemiş bir yol bulunmadığı ve tüm yollar için güvenlik kontrolleri ile kimlik doğrulama gücünün tutarlı şekilde uygulandığı doğrulanmalıdır. | 2 |
| **6.3.5** | Başarılı veya başarısız şüpheli kimlik doğrulama girişimlerinin kullanıcıya bildirildiği doğrulanmalıdır. Bu, olağandışı bir konum veya istemciden gelen girişimler, yalnızca bir faktörle yapılan kısmen başarılı doğrulamalar, uzun süreli inaktiflik sonrası yapılan girişimler veya birçok başarısız denemeden sonraki başarılı girişimler gibi durumları içerebilir. | 3 |
| **6.3.6** | E-postanın, tek faktörlü ya da çok faktörlü kimlik doğrulama mekanizması olarak kullanılmadığı doğrulanmalıdır. | 3 |
| **6.3.7** | Kimlik doğrulama detaylarında yapılan güncellemeler sonrasında (örneğin kimlik bilgisi sıfırlama, kullanıcı adı veya e-posta adresi değişiklikleri), kullanıcıların bilgilendirildiği doğrulanmalıdır. | 3 |
| **6.3.8** | Başarısız kimlik doğrulama girişimlerinden, geçerli kullanıcıların hata mesajları, HTTP yanıt kodları veya farklı yanıt süreleri gibi sonuçlara dayanarak tespit edilemediği doğrulanmalıdır. Bu koruma, kayıt ve "parolamı unuttum" işlevselliğinde de geçerli olmalıdır. | 3 |

## V6.4 Kimlik Doğrulama Faktörünün Yaşam Döngüsü ve Kurtarma

Kimlik doğrulama faktörleri; parolalar, yazılım tabanlı token'lar, donanım token'ları ve biyometrik cihazlar gibi öğeleri kapsar. Bu mekanizmaların yaşam döngüsünün güvenli şekilde yönetilmesi, bir uygulamanın güvenliği açısından kritik öneme sahiptir. Bu bölüm, bu mekanizmalarla ilgili gereksinimleri içerir.

Bu bölümdeki gereksinimler, büyük ölçüde [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html)'ın [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) veya [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) bölümleri ile ilişkilidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **6.4.1** | Sistem tarafından oluşturulan ilk parolaların veya etkinleştirme kodlarının güvenli bir şekilde rastgele üretildiği, mevcut parola politikasına uygun olduğu, kısa bir süre içinde veya ilk kullanım sonrasında geçerliliğini yitirdiği doğrulanmalıdır. Bu başlangıç sırları uzun vadeli parola olarak kullanılmasına izin verilmemelidir. | 1 |
| **6.4.2** | Parola ipuçlarının veya "gizli sorular" olarak bilinen, bilgiye dayalı kimlik doğrulama mekanizmalarının mevcut olmadığı doğrulanmalıdır. | 1 |
| **6.4.3** | Unutulmuş parolanın sıfırlanması için, etkin olan çok faktörlü kimlik doğrulama mekanizmalarını atlamayan güvenli bir sürecin uygulandığı doğrulanmalıdır. | 2 |
| **6.4.4** | Çok faktörlü kimlik doğrulama faktörlerinden biri kaybolursa, kayıt sırasında uygulanan kimlik kanıtlama seviyesiyle aynı seviyede kimlik doğrulama yapıldığı doğrulanmalıdır. | 2 |
| **6.4.5** | Süresi dolacak kimlik doğrulama mekanizmalarının yenilenmesine ilişkin talimatların, süresi dolmadan önce tamamlanacak şekilde yeterli sürede gönderildiği ve gerekiyorsa otomatik hatırlatıcıların yapılandırıldığı doğrulanmalıdır. | 3 |
| **6.4.6** | Yönetici yetkisi olan kullanıcıların, kullanıcının parola sıfırlama sürecini başlatabildiği ancak kullanıcının yeni parolasını belirleyemediği veya değiştiremediği doğrulanmalıdır. Bu, yönetici yetkisi olan kullanıcıların, kullanıcı parolasını bilmesini engeller. | 3 |

## V6.5 Çok Faktörlü Kimlik Doğrulama İçin Genel Gereksinimler

Bu bölüm, çeşitli çok faktörlü kimlik doğrulama yöntemleriyle ilgili genel yönergeleri sunar.

Bu mekanizmalar şunları içerir:

* Arama Sırları (Lookup Secrets)
* Zamana Dayalı Tek Kullanımlık Parolalar (TOTP)
* Bant Dışı (Out-of-Band) mekanizmalar

"Arama sırları", daha önceden oluşturulmuş gizli kod listeleridir. Bunlar, İşlem Yetkilendirme Numaraları (TAN), sosyal medya kurtarma kodları veya rastgele değerler içeren bir tablo şeklinde olabilir. Bu tür kimlik doğrulama mekanizmaları, “sahip olduğunuz bir şey” olarak değerlendirilir çünkü kodlar kasıtlı olarak ezberlenemez olacak şekilde tasarlanır ve bir yerde saklanmaları gerekir.

Zamana Dayalı Tek Kullanımlık Parolalar (TOTP), fiziksel veya yazılımsal token'lardır ve sürekli değişen, sözde rastgele (pseudo-random) bir tek kullanımlık parola gösterir. Bu mekanizmalar da “sahip olduğunuz bir şey” kategorisindedir. Çok faktörlü TOTP'ler tek faktörlü TOTP'lere benzer, ancak nihai Tek Kullanımlık Parolayı (OTP) oluşturmak için geçerli bir PIN kodu, biyometrik kilit açma, USB takma, NFC eşleştirme veya bazı ek değerlerin (işlem imzalama hesaplayıcıları gibi) girilmesini gerektirir.

Bant dışı mekanizmalar bir sonraki bölümde açıklanacaktır.

Bu bölümlerdeki gereklilikler çoğunlukla [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html)'ın [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators) ve [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) kısımları ile ilgilidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **6.5.1** | Arama sırları, bant dışı kimlik doğrulama istekleri veya kodları ve zamana dayalı tek kullanımlık parolaların (TOTP) yalnızca bir kez kullanılabildiği doğrulanmalıdır. | 2 |
| **6.5.2** | Uygulamanın backend tarafında saklanırken, 112 bitten az entropiye sahip (örneğin 19 rastgele harf-rakam karakteri veya 34 rastgele rakam) arama sırlarının, 32-bit rastgele bir salt içeren onaylı bir parola saklama algoritmasıyla hash’lendiği doğrulanmalıdır. Gizli bilginin entropisi 112 bit veya daha fazlaysa standart bir hash fonksiyonu kullanılabilir. | 2 |
| **6.5.3** | Arama sırları, bant dışı kimlik doğrulama kodları ve zamana dayalı tek kullanımlık parola seed'lerinin, öngörülebilir değerlerden kaçınmak için Kriptografik Olarak Güvenli Sözde Rastgele Sayı Üreteci (CSPRNG) ile oluşturulduğu doğrulanmalıdır. | 2 |
| **6.5.4** | Arama sırlarının ve bant dışı kimlik doğrulama kodlarının en az 20 bit entropiye (genellikle 4 rastgele harf-rakam karakteri veya 6 rastgele rakam) sahip olduğu doğrulanmalıdır. | 2 |
| **6.5.5** | Bant dışı kimlik doğrulama isteklerinin, kodlarının veya token'larının ve zamana dayalı tek kullanımlık parolaların (TOTP) belirli bir ömre sahip olduğu doğrulanmalıdır. Bant dışı istekler en fazla 10 dakika, TOTP’ler ise en fazla 30 saniye geçerli olmalıdır. | 2 |
| **6.5.6** | Herhangi bir kimlik doğrulama faktörünün (fiziksel cihazlar dahil) çalınması veya kaybı durumunda iptal edilebildiği doğrulanmalıdır. | 3 |
| **6.5.7** | Biyometrik kimlik doğrulama mekanizmalarının yalnızca ikincil faktör olarak, “sahip olduğunuz bir şey” veya “bildiğiniz bir şey” ile birlikte kullanıldığı doğrulanmalıdır. | 3 |
| **6.5.8** | Zamana dayalı tek kullanımlık parolaların (TOTP) doğrulamasının, güvenilir bir hizmetten alınan zaman kaynağına dayanarak yapıldığı ve güvenilir olmayan veya istemci tarafından sağlanan zaman kaynağına dayanmadığı doğrulanmalıdır. | 3 |

## V6.6 Bant Dışı Kimlik Doğrulama Mekanizmaları

Bu mekanizmalar genellikle kimlik doğrulama sunucusunun, fiziksel bir cihazla güvenli bir ikinci kanal üzerinden iletişim kurmasını (örneğin mobil cihazlara gönderilen bildirimler) içerir. Bu tür mekanizmalar, “sahip olduğunuz bir şey” olarak değerlendirilir.

E-posta ve VOIP gibi güvenli olmayan bant dışı kimlik doğrulama yöntemlerine izin verilmemektedir. PSTN ve SMS ile yapılan kimlik doğrulama şu anda NIST tarafından ["sınırlandırılmış" doğrulama mekanizmaları](https://pages.nist.gov/800-63-FAQ/#q-b01) olarak değerlendirilmekte ve yerlerine zamana dayalı tek kullanımlık parolalar (TOTP) veya benzer kriptografik mekanizmaların tercih edilmesi önerilmektedir. 

NIST SP 800-63B [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network), telefon veya SMS kullanılması gerekiyorsa cihaz değişimi, SIM değişikliği, numara taşıma gibi anormal davranışların risklerinin ele alınmasını önermektedir. Bu ASVS bölümü bunu zorunlu kılmasa da, bu önlemlerin alınmaması Seviye 2'deki hassas bir uygulamada veya Seviye 3’teki bir uygulamada ciddi bir güvenlik riski olarak değerlendirilmelidir.

Ayrıca NIST, yakın zamanda [anlık bildirimlerin kullanılmamasını öneren](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/#fig-3) bir yönerge oluşturmuştur. Bu ASVS bölümü bu konuda bir zorunluluk getirmese de, “push bombing” risklerine karşı farkındalık önemlidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **6.6.1** | Tek kullanımlık parolaların (OTP) telefon veya SMS ile Public Switched Telephone Network (PSTN) üzerinden iletildiği kimlik doğrulama mekanizmalarının, yalnızca telefon numarası önceden doğrulanmışsa, alternatif daha güçlü yöntemler (örneğin TOTP) de sunuluyorsa ve kullanıcıya güvenlik riskleri hakkında bilgi veriliyorsa sunulduğu doğrulanmalıdır. Seviye 3 uygulamalar için telefon ve SMS seçenekleri sunulmamalıdır. | 2 |
| **6.6.2** | Bant dışı kimlik doğrulama isteklerinin, kodlarının veya token'larının, oluşturuldukları özgün kimlik doğrulama isteğiyle bağlantılı olduğu ve daha önceki ya da sonraki bir istek için kullanılamadığı doğrulanmalıdır. | 2 |
| **6.6.3** | Kod tabanlı bant dışı kimlik doğrulama mekanizmalarının, oran sınırlaması ile kaba kuvvet saldırılarına karşı korunduğu doğrulanmalıdır. En az 64 bit entropiye sahip kodlar kullanılması da değerlendirilmelidir. | 2 |
| **6.6.4** | Çok faktörlü kimlik doğrulama için push bildirimleri kullanılıyorsa, push bombing saldırılarına karşı oran sınırlamasının kullanıldığı doğrulanmalıdır. “Numara eşleştirme” de bu riski azaltabilir. | 3 |

## V6.7 Kriptografik Kimlik Doğrulama Mekanizması

Kriptografik kimlik doğrulama mekanizmaları, akıllı kartlar veya FIDO anahtarları gibi kullanıcıların kimlik doğrulama işlemini tamamlamak için kriptografik cihazı bilgisayara takması ya da eşleştirmesini gerektiren mekanizmaları içerir. Kimlik doğrulama sunucusu, kriptografik cihaza veya yazılıma bir "challenge nonce" gönderir; cihaz ya da yazılım da güvenli bir şekilde saklanan kriptografik anahtara dayalı olarak bir yanıt üretir. Bu bölümdeki gereksinimler bu mekanizmalar için, “Kriptografi” bölümünde ele alınan kriptografik algoritmalarla ilgili rehberlik sağlayan kısımlarla birlikte, uygulamaya özel rehberlik sağlar. 

Kriptografik kimlik doğrulama için paylaşımlı veya gizli anahtarların kullanıldığı durumlarda, diğer sistem gizli anahtarlarıyla aynı mekanizmalar kullanılarak saklanmalıdır. Bu mekanizmalar “Yapılandırma” başlığındaki “Gizli Yönetimi” bölümünde belgelenmiştir.

Bu bölümdeki gereksinimler çoğunlukla [NIST's Guidance](https://pages.nist.gov/800-63-3/sp800-63b.html)'ın [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) kısmı ile ilişkilidir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **6.7.1** | Kriptografik kimlik doğrulama beyanlarını doğrulamak için kullanılan sertifikaların, değiştirilmeye karşı korumalı şekilde saklandığı doğrulanmalıdır. | 3 |
| **6.7.2** | Challenge nonce değerinin en az 64 bit uzunluğunda olduğu ve istatistiksel olarak benzersiz ya da cihazın ömrü boyunca benzersiz olduğu doğrulanmalıdır. | 3 |


## V6.8 Kimlik Sağlayıcısı ile Kimlik Doğrulama

Kimlik Sağlayıcılar (IdP'ler), kullanıcılar için birleştirilmiş kimlikler sunar. Kullanıcılar genellikle birden fazla IdP ile birden fazla kimliğe sahiptir; örneğin Azure AD, Okta, Ping Identity veya Google gibi bir kurumsal kimlik ya da Facebook, Twitter, Google veya WeChat gibi bir tüketici kimliği. Bu liste, bu şirketlere veya hizmetlere bir onay niteliğinde değil, sadece geliştiricilerin çoğu kullanıcının halihazırda birçok kimliğe sahip olduğu gerçeğini dikkate almaları gerektiğine dair bir hatırlatmadır. Kuruluşlar, IdP'nin kimlik doğrulama gücüne ilişkin risk profiline göre mevcut kullanıcı kimlikleriyle entegrasyon sağlamayı değerlendirmelidir. Örneğin, sahte veya geçici kimliklerin kolayca oluşturulabilmesi nedeniyle bir devlet kurumu, sosyal medya kimliklerini hassas sistemlere giriş için kabul etmeyebilir; ancak bir mobil oyun şirketi, aktif oyuncu kitlesini artırmak için büyük sosyal medya platformlarıyla entegrasyon yapmayı tercih edebilir.

Harici kimlik sağlayıcıların güvenli kullanımı, kimlik sahtekarlığını veya sahte beyanları önlemek için dikkatli yapılandırma ve doğrulama gerektirir. Bu bölüm, bu riskleri ele almak için gereksinimleri sunar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **6.8.1** | Uygulama birden fazla kimlik sağlayıcıyı (IdP) destekliyorsa, başka bir desteklenen kimlik sağlayıcı aracılığıyla (örneğin aynı kullanıcı tanımlayıcısını kullanarak) kullanıcının kimliğinin taklit edilemediği doğrulanmalıdır. Standart önlem, uygulamanın kullanıcıyı IdP kimliği (bir ad alanı işlevi görür) ve IdP içindeki kullanıcı kimliğinin birleşimiyle kaydetmesi ve tanımlamasıdır. | 2 |
| **6.8.2** | Kimlik doğrulama beyanları üzerindeki dijital imzaların (örneğin JWT veya SAML beyanları) varlığı ve bütünlüğünün her zaman doğrulandığı ve imzasız veya geçersiz imzalı beyanların reddedildiği doğrulanmalıdır. | 2 |
| **6.8.3** | SAML beyanlarının benzersiz biçimde işlendiği ve yalnızca geçerlilik süresi içinde bir kez kullanıldığı, tekrar oynatma (replay) saldırılarını önlemek amacıyla doğrulanmalıdır. | 2 |
| **6.8.4** | Uygulama ayrı bir Kimlik Sağlayıcı (IdP) kullanıyorsa ve belirli işlemler için belirli kimlik doğrulama gücü, yöntemleri veya zaman bilgisi bekliyorsa, uygulamanın bu bilgileri IdP tarafından döndürülen veriler üzerinden doğruladığı teyit edilmelidir. Örneğin OIDC kullanılıyorsa, bu durum ID Token üzerindeki 'acr', 'amr' ve 'auth_time' gibi claim’lerin (varsa) doğrulanması ile sağlanabilir. Eğer IdP bu bilgileri sağlamıyorsa, uygulamanın asgari kimlik doğrulama gücünün kullanıldığını varsayan (örneğin yalnızca kullanıcı adı ve parola ile tek faktörlü doğrulama) belgelenmiş bir yedek yaklaşımı olmalıdır. | 2 |

## Referanslar

Daha fazla bilgi için:

* [NIST SP 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST SP 800-63B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST SP 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [OWASP Cheat Sheet - Password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Forgot password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Choosing and using security questions](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
* [CISA Guidance on "Number Matching"](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
* [Details on the FIDO Alliance](https://fidoalliance.org/)
