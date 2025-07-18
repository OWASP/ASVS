# V10 OAuth ve OIDC

## Kontrol Amacı

OAuth2 (bu bölümde kısaca OAuth olarak anılacaktır), yetki devri için endüstri standardı bir çerçevedir. Örneğin, OAuth kullanılarak bir istemci uygulama, kullanıcı tarafından yetkilendirildiği sürece, o kullanıcı adına API’lere (sunucu kaynaklarına) erişim sağlayabilir.

OAuth tek başına kullanıcı kimlik doğrulaması amacıyla tasarlanmamıştır. OpenID Connect (OIDC) çerçevesi, OAuth üzerine bir kullanıcı kimliği katmanı ekleyerek bu eksikliği tamamlar. OIDC, standartlaştırılmış kullanıcı bilgileri, Single Sign-On (SSO) ve oturum yönetimi gibi özellikleri destekler. OIDC, OAuth'un bir uzantısı olduğundan, bu bölümdeki OAuth gereksinimleri aynı zamanda OIDC için de geçerlidir.

OAuth çerçevesinde aşağıdaki roller tanımlanır:

* OAuth istemcisi, sunucu kaynaklarına erişim sağlamaya çalışan uygulamadır (örneğin, verilen access token’ı kullanarak bir API çağrısı yapar). Genellikle bu, sunucu taraflı bir uygulamadır.
    * Gizli istemci (confidential client), authorization server ile kimlik doğrulama sırasında kullandığı kimlik bilgilerini gizli tutabilecek kapasitede olan istemcidir.
    * Genel istemci (public client), authorization server ile kimlik doğrulama sırasında kullandığı kimlik bilgilerini gizli tutamayacak durumdadır. Bu nedenle kendini yalnızca bir client_id ile tanıtır, client_id ve client_secret gibi bilgilerle kimlik doğrulaması yapmaz.
* OAuth kaynak sunucusu (resource server – RS), OAuth istemcilerine kaynakları sunan API’dir.
* OAuth yetkilendirme sunucusu (authorization server – AS), access token üreten sunucu uygulamasıdır. Bu token’lar sayesinde OAuth istemcisi, son kullanıcı adına veya kendi adına RS üzerindeki kaynaklara erişim sağlayabilir. AS genellikle ayrı bir uygulama olsa da, uygun görüldüğünde RS ile entegre olabilir.
* Kaynak sahibi (resource owner – RO), OAuth istemcilerinin kendi adına, kaynak sunucusu üzerinde kısıtlı erişim elde etmesine izin veren son kullanıcıdır. Yetkilendirme sürecine AS üzerinden katılım sağlar.

OIDC çerçevesinde aşağıdaki roller tanımlanır:

* Güvenen taraf (relying party – RP), son kullanıcının kimlik doğrulamasını OpenID Provider üzerinden gerçekleştirmek isteyen istemci uygulamadır. Aynı zamanda bir OAuth istemcisidir.
* OpenID Provider (OP), son kullanıcıyı kimlik doğrulama yeteneğine sahip olan ve RP'ye OIDC claim’lerini sağlayan bir OAuth yetkilendirme sunucusudur. OP çoğu zaman bir kimlik sağlayıcı (IdP) olur; ancak federasyon senaryolarında OP ve gerçek kimlik sağlayıcı farklı uygulamalar olabilir.

OAuth ve OIDC başlangıçta üçüncü taraf uygulamalar için tasarlanmıştı. Ancak günümüzde ilk taraf uygulamalar tarafından da yaygın şekilde kullanılmaktadır. Bu kullanım senaryolarında, özellikle kimlik doğrulama ve oturum yönetimi amacıyla kullanıldığında protokol belirli bir karmaşıklık ekler ve bu durum bazı yeni güvenlik riskleri yaratabilir.

OAuth ve OIDC birçok farklı uygulama tipiyle kullanılabilir; ancak ASVS ve bu bölümdeki gereksinimler özellikle web uygulamaları ve API’ler için tasarlanmıştır.

OAuth ve OIDC, web teknolojilerinin üzerine kurulu mantıksal protokoller olduklarından, bu bölümdeki gereksinimler diğer bölümlerden bağımsız değerlendirilemez; genel güvenlik gereksinimleri geçerliliğini korur.

Bu bölüm, <https://oauth.net/2/> ve <https://openid.net/developers/specs/> üzerindeki spesifikasyonlarla uyumlu şekilde OAuth2 ve OIDC için güncel en iyi uygulamaları ele alır. RFC’ler olgun belgeler olarak görülse de, sık sık güncellenmektedir. Bu nedenle uygulamada, ilgili gereksinimlerin en güncel versiyonlarla uyumlu şekilde ele alınması önemlidir. Ayrıntılar için bölümün referans kısmına bakınız.

Bu alanın karmaşıklığı göz önünde bulundurulduğunda, güvenli bir OAuth veya OIDC çözümünün, tanınmış ve endüstri standardı yetkilendirme sunucularını kullanması ve önerilen güvenlik yapılandırmalarını uygulaması son derece önemlidir.

Bu bölümde kullanılan terimler, OAuth ve OIDC spesifikasyonlarındaki tanımlarla uyumludur. Ancak OIDC’ye özel gereksinimler dışında, genellikle OAuth terminolojisi tercih edilmiştir.

Bu bölümde geçen "token" terimi, aşağıdaki anlamlarda kullanılmıştır:

* Access token'ları sadece RS tarafından kullanılır. Bunlar ya introspection ile doğrulanan bir reference token olabilir ya da belirli bir anahtar malzemesiyle doğrulanan bir self-contained token olabilir.
* Refresh token'ları, yalnızca onu üreten authorization server tarafından kullanılabilir.
* OIDC ID Token'ları sadece authorization flow’u tetikleyen istemci tarafından kullanılabilir.

Bu bölümdeki bazı gereksinimlerin risk seviyesi, istemcinin gizli istemci mi yoksa açık istemci mi olduğuna göre değişiklik gösterebilir. Güçlü istemci kimlik doğrulaması, birçok saldırı vektörünü etkisiz hale getirebildiği için, L1 uygulamalarında bazı gereksinimler gizli istemci kullanıldığında esnetilebilir.


## V10.1 Genel OAuth ve OIDC Güvenliği

Bu bölüm, OAuth veya OIDC kullanan tüm uygulamalara uygulanabilen genel mimari gereksinimleri kapsar.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **10.1.1** | 	Token'ların yalnızca kesinlikle ihtiyaç duyan bileşenlere gönderildiği doğrulanmalıdır. Örneğin, tarayıcı tabanlı JavaScript uygulamaları için bir backend-for-frontend modeli kullanıldığında, access ve refresh token'lara yalnızca backend'in erişebilmesi gerekir. | 2 |
| **10.1.2** | Authorization server'dan gelen değerler (örneğin authorization code veya ID Token gibi) yalnızca aynı user agent oturumu ve işlemi tarafından başlatılmış bir yetkilendirme akışının sonucuysa kabul edildiği doğrulanmalıdır. Bu, client tarafından oluşturulan secret’ların 'proof key for code exchange' (PKCE) ‘code_verifier’, ‘state’ veya OIDC ‘nonce’ gibi tahmin edilemez, işleme özgü ve hem client’a hem de işlem başlatılan user agent oturumuna güvenli bir şekilde bağlı olmasını gerektirir. | 2 |

## V10.2 OAuth İstemcisi

Bu gereksinimler, OAuth istemci uygulamaları için sorumlulukları detaylandırır. Client örneğin bir web sunucusu backend’i (genellikle Backend For Frontend olarak hareket eden), bir backend servis entegrasyonu veya bir frontend Single Page Application (SPA, yani tarayıcı tabanlı uygulama) olabilir.

Genel olarak backend istemciler gizli istemci olarak, frontend istemciler ise açık istemci olarak değerlendirilir. Ancak, son kullanıcı cihazında çalışan native uygulamalar, 'OAuth dynamic client registration' kullanıldığında gizli olarak kabul edilebilir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **10.2.1** | Code flow kullanılıyorsa, OAuth client’ın token taleplerini tetikleyen CSRF saldırılarına karşı korumaya sahip olduğu doğrulanmalıdır. Bu genellikle PKCE kullanılarak veya authorization isteğinde gönderilen ‘state’ parametresinin kontrolü ile sağlanır. | 2 |
| **10.2.2** | OAuth istemcisi birden fazla AS ile etkileşime girebiliyorsa, mix-up saldırılarına karşı korumaya sahip olduğu doğrulanmalıdır. Örneğin, authorization server’ın 'iss' parametresini döndürmesi zorunlu kılınabilir ve bu parametrenin hem authorization yanıtında hem de token yanıtında doğrulanması gerekir. | 2 |
| **10.2.3** | OAuth istemcisinin authorization server’a yaptığı taleplerde yalnızca gerekli scope’ları (veya diğer yetkilendirme parametrelerini) talep ettiği doğrulanmalıdır. | 3 |

## V10.3 OAuth Kaynak Sunucusu (RS)

ASVS ve bu bölüm bağlamında resource server (RS) bir API’dir. Güvenli erişim sağlamak için RS şunları yapmalıdır:

* Access token’ı, token formatı ve ilgili protokol spesifikasyonlarına göre doğrulamalıdır; örneğin JWT doğrulaması veya OAuth token introspection.
* Geçerliyse, access token’dan alınan bilgiler ve verilmiş izinlere göre yetkilendirme kararları uygulamalıdır. Örneğin, resource server’ın client’ın (RO adına hareket eden) istenen kaynağa erişme yetkisine sahip olduğunu doğrulaması gerekir.

Bu nedenle burada listelenen gereksinimler, OAuth veya OIDC’ye özeldir ve token doğrulaması yapıldıktan sonra, token içeriğine dayalı yetkilendirme gerçekleştirilmeden önce uygulanmalıdır.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **10.3.1** | RS'nin yalnızca bu servisle kullanılmak üzere tasarlanmış access token’ları kabul ettiği doğrulanmalıdır (audience kontrolü). Audience bilgisi yapılandırılmış token’larda (örneğin JWT içindeki ‘aud’ claim’i) yer alabilir veya token introspection endpoint aracılığıyla kontrol edilebilir. | 2 |
| **10.3.2** | RS'nin, access token’dan gelen claim’lere dayanarak yetki devri tanımına uygun şekilde yetkilendirme kararları uyguladığı doğrulanmalıdır. ‘sub’, ‘scope’ ve ‘authorization_details’ gibi claim’ler varsa, bu kararın parçası olmalıdır. | 2 |
| **10.3.3** | Erişim kontrolü kararında, access token’dan (JWT veya ilgili token introspection yanıtı) benzersiz bir kullanıcının tanımlanması gerekiyorsa, RS'nin başka kullanıcılara devredilemeyecek claim’ler ile kullanıcıyı tanımladığı doğrulanmalıdır. Genellikle bu, ‘iss’ ve ‘sub’ claim’lerinin birlikte kullanılması anlamına gelir. | 2 |
| **10.3.4** | RS'nin belirli bir kimlik doğrulama gücü, yöntemi veya güncelliği (recentness) gerektirmesi durumunda, sunulan access token’ın bu kısıtlamaları karşıladığını doğruladığı, örneğin, OIDC ‘acr’, ‘amr’ ve ‘auth_time’ claim’leri kullanılarak doğrulanmalıdır.  | 2 |
| **10.3.5** | RS'nin, (yetkisiz taraflarca) çalınmış veya tekrar edilen access token’ların kullanımını önlemek için sender-constrained access token’lar kullandığı doğrulanmalıdır. Bu, OAuth 2 için Mutual TLS veya OAuth 2 Demonstration of Proof of Possession (DPoP) ile sağlanabilir. | 3 |

## V10.4 OAuth Yetkilendirme Sunucusu (AS)

Bu gereksinimler, OAuth authorization server'ların (yetkilendirme sunucuları) ve OpenID Provider'ların sorumluluklarını detaylandırır.

İstemci kimlik doğrulaması için 'self_signed_tls_client_auth' yöntemi, [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705) [böüm 2.2'de](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) belirtilen ön koşullarla birlikte kullanılabilir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **10.4.1** | AS'nin, istemciye özel önceden kaydedilmiş URI’lerden oluşan bir allowlist kullanarak redirect URI’leri tam dize karşılaştırması ile doğruladığı doğrulanmalıdır. | 1 |
| **10.4.2** | AS'nin, "authorization response" içinde "authorization code" döndürdüğü durumlarda, bu kodun yalnızca bir kez kullanılabildiği doğrulanmalıdır. Daha önce access token vermek için kullanılmış bir authorization code ile yapılan ikinci geçerli token isteği reddedilmeli ve ilgili tüm token’lar iptal edilmelidir. | 1 |
| **10.4.3** | Authorization code’un kısa ömürlü olduğu doğrulanmalıdır. L1 ve L2 uygulamalar için maksimum yaşam süresi 10 dakika, L3 uygulamalar için 1 dakikadır. | 1 |
| **10.4.4** | Belirli bir istemci için AS'nin yalnızca o istemcinin ihtiyaç duyduğu grant türlerine izin verdiği doğrulanmalıdır. "Token" (Implicit flow) ve "password" (Resource Owner Password Credentials flow) grant türlerinin artık kullanılmaması gerekir. | 1 |
| **10.4.5** | AS'nin, açık istemciler için refresh token replay saldırılarını azalttığı doğrulanmalıdır. Tercihen sender-constrained refresh token’lar (DPoP veya mutual TLS ile certificate-bound access token’lar) kullanılmalıdır. L1 ve L2 uygulamalar için refresh token rotation kullanılabilir. Rotation kullanılıyorsa, AS refresh token’ı kullanım sonrası geçersiz kılmalı ve geçersiz bir refresh token sunulması durumunda o yetkilendirme ile ilişkili tüm refresh token’ları iptal etmelidir. | 1 |
| **10.4.6** | Code grant kullanılıyorsa, AS'nin authorization code interception saldırılarına karşı koruma sağladığı doğrulanmalıdır. Yetkilendirme isteğinde geçerli bir "code_challenge" değeri zorunlu olmalı ve "code_challenge_method" olarak "plain" kabul edilmemelidir. Token isteğinde ise "code_verifier" parametresi doğrulanmalıdır. | 2 |
| **10.4.7** | AS'nin, kimlik doğrulaması yapılmamış dinamik istemci kaydını desteklemesi durumunda, kötü niyetli istemci uygulamalarına karşı riskleri azalttığı doğrulanmalıdır. Kayıtlı URI’ler gibi client metadata’sı doğrulanmalı, kullanıcı onayı alınmalı ve güvenilmeyen bir client uygulamasıyla yapılan yetkilendirme isteği işlenmeden önce kullanıcı uyarılmalıdır. | 2 |
| **10.4.8** | Refresh token’ların, sliding expiration kullanılsa bile mutlak bir sona erme süresine sahip olduğu doğrulanmalıdır. | 2 |
| **10.4.9** | Yetkili bir kullanıcı tarafından AS kullanıcı arayüzü üzerinden refresh token’ların ve reference access token’ların iptal edilebildiği doğrulanmalıdır. | 2 |
| **10.4.10** | Gizli istemcilerin token istekleri, pushed authorization request (PAR) ve token iptal istekleri gibi server’a yapılan backchannel isteklerinde kimliğinin kontrol edildiği doğrulanmalıdır. | 2 |
| **10.4.11** | AS yapılandırmasının, OAuth istemcisine yalnızca gerekli scope’ları atadığı doğrulanmalıdır. | 2 |
| **10.4.12** | Belirli bir client için, authorization server’ın yalnızca client’ın ihtiyaç duyduğu 'response_mode' değerine izin verdiği doğrulanmalıdır. Örneğin, bu değer ya beklenenlerle karşılaştırılarak doğrulanmalı ya da PAR veya JAR kullanılmalıdır. | 3 |
| **10.4.13** | "Code" grant türünün daima pushed authorization request (PAR) ile birlikte kullanıldığı doğrulanmalıdır. | 3 |
| **10.4.14** | AS'nin yalnızca sender-constrained (Proof-of-Possession) access token’lar ürettiği doğrulanmalıdır. Bu, mutual TLS ile certificate-bound access token ya da DPoP ile DPoP-bound access token olabilir. | 3 |
| **10.4.15** | Sunucu taraflı istemciler için (kullanıcı cihazında çalışmayan), AS'nin "authorization_details" parametresinin istemci backend'i tarafından sağlandığını ve kullanıcı tarafından değiştirilmediğini doğruladığı, örneğin pushed authorization request (PAR) or JWT-secured Authorization Request (JAR) zorunlu kılınarak doğrulanmalıdır. | 3 |
| **10.4.16** | Bir istemci gizli ise, AS'nin güçlü istemci kimlik doğrulama yöntemlerini zorunlu kıldığı doğrulanmalıdır. Bu yöntemler, public-key cryptography’ye dayalı ve replay saldırılarına karşı dayanıklı olmalı, örneğin mutual TLS ("tls_client_auth", "self_signed_tls_client_auth") veya private key JWT ("private_key_jwt") gibi.	| 3 |

## V10.5 OIDC İstemcisi

"OIDC relying party", bir OAuth istemcisi olarak davrandığı için "OAuth İstemcisi" bölümündeki gereksinimler burada da geçerlidir.

“Kimlik Doğrulama” başlığındaki “Kimlik Sağlayıcısı ile Kimlik Doğrulama” bölümü de ilgili genel gereksinimleri içerir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **10.5.1** | İstemcinin (relying party olarak) ID Token replay saldırılarını azalttığı doğrulanmalıdır. Örneğin, ID Token’daki 'nonce' claim’inin, OpenID Provider’a gönderilen kimlik doğrulama isteğindeki 'nonce' değeriyle eşleştiği doğrulanmalıdır. | 2 |
| **10.5.2** | İstemcinin kullanıcıyı ID Token claim’lerinden (genellikle, başka kullanıcılarla yeniden atanamayan 'sub' claim’i) benzersiz şekilde tanımladığı doğrulanmalıdır. | 2 |
| **10.5.3** | İstemcinin, kötü niyetli bir AS'nin başka bir AS'yi taklit etmesini AS metadata’sı üzerinden reddettiği doğrulanmalıdır. AS metadata’sındaki issuer URL’si, istemci tarafından beklenen önceden yapılandırılmış issuer URL’siyle tam olarak eşleşmiyorsa, metadata reddedilmelidir. | 2 |
| **10.5.4** | İstemcinin, ID Token’ın kendisi için (audience) kullanılması amaçlandığını doğruladığı doğrulanmalıdır. Bu, token’daki 'aud' claim’inin istemcinin 'client_id' değeriyle eşit olup olmadığının kontrol edilmesiyle yapılır.	 | 2 |
| **10.5.5** | OIDC back-channel logout kullanıldığında, relying party’nin "forced logout" ve "logout" akışında "cross-JWT confusion" gibi saldırılara karşı koruma sağladığı doğrulanmalıdır. Client, logout token’ın 'logout+jwt' türünde olduğunu, 'event' claim’inin doğru üyeye sahip olduğunu ve 'nonce' claim’i içermediğini doğrulamalıdır. Ayrıca token için kısa bir sona erme süresi (örneğin 2 dakika) önerilir.	| 2 |

## V10.6 OpenID Provider

OpenID Provider’lar, OAuth AS olarak davrandığı için “OAuth Yetkilendirme Sunucusu” bölümündeki gereksinimler burada da geçerlidir.

ID Token flow (code flow değil) kullanılıyorsa, access token üretilmez ve OAuth AS için geçerli olan birçok gereksinim uygulanamaz.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **10.6.1** | OpenID Provider’ın yalnızca 'code', 'ciba', 'id_token' veya 'id_token code' response mode değerlerine izin verdiği doğrulanmalıdır. 'code' değeri, 'id_token code' (OIDC Hybrid flow) yerine tercih edilmelidir. 'token' (Implicit flow) kullanılmamalıdır. | 2 |
| **10.6.2** | OpenID Provider’ın forced logout yoluyla yapılan hizmet reddi saldırılarını önlediği doğrulanmalıdır. Bu, son kullanıcıdan açık onay alınarak veya varsa logout isteğinde (relying party tarafından başlatılan) bulunan parametrelerin, örneğin 'id_token_hint', doğrulanmasıyla yapılabilir. | 2 |

## V10.7 Onay (Consent) Yönetimi

Bu gereksinimler, kullanıcı onayının AS tarafından doğrulanmasını kapsar. Uygun kullanıcı onayı olmadan, kötü niyetli bir aktör spoofing veya sosyal mühendislik yoluyla kullanıcının adına yetki elde edebilir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **10.7.1** | AS'nin her yetkilendirme isteği için kullanıcının onayını aldığı doğrulanmalıdır. İstemcinin kimliği garanti altına alınamıyorsa, AS daima kullanıcıdan açıkça onay istemelidir.	| 2 |
| **10.7.2** | AS'nin kullanıcıdan onay istediğinde, neye onay verildiğini açık ve yeterli şekilde gösterdiği doğrulanmalıdır. Uygun olduğunda bu bilgiler, istenen yetkilendirmelerin doğasını (genellikle scope, resource server, RAR gibi detaylara dayalı), yetkilendirilmiş uygulamanın kimliğini ve bu yetkilendirmelerin süresini içermelidir. | 2 |
| **10.7.3** | Kullanıcının, AS üzerinden verdiği onayları görüntüleyebildiği, değiştirebildiği ve iptal edebildiği doğrulanmalıdır.	 | 2 |

## Referanslar

OAuth ile ilgili daha fazla bilgi için:

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

ASVS içindeki OAuth ile ilgili gereksinimler için, yayımlanmış ve taslak durumundaki aşağıdaki RFC'ler kullanılmaktadır:

* [RFC6749 The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
* [RFC6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)
* [RFC6819 OAuth 2.0 Threat Model and Security Considerations](https://datatracker.ietf.org/doc/html/rfc6819)
* [RFC7636 Proof Key for Code Exchange by OAuth Public Clients](https://datatracker.ietf.org/doc/html/rfc7636)
* [RFC7591 OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591)
* [RFC8628 OAuth 2.0 Device Authorization Grant](https://datatracker.ietf.org/doc/html/rfc8628)
* [RFC8707 Resource Indicators for OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc8707)
* [RFC9068 JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
* [RFC9126 OAuth 2.0 Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126)
* [RFC9207 OAuth 2.0 Authorization Server Issuer Identification](https://datatracker.ietf.org/doc/html/rfc9207)
* [RFC9396 OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)
* [RFC9449 OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)
* [RFC9700 Best Current Practice for OAuth 2.0 Security](https://datatracker.ietf.org/doc/html/rfc9700)
* [draft OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)<!-- recheck on release -->
* [draft The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12)<!-- recheck on release -->

OpenID Connect ile ilgili daha fazla bilgi için:

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
