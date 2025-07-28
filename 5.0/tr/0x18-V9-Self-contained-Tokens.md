# V9 Kendi İçinde Taşıyıcı Token (Self-contained Token)

## Kontrol Amacı

Kendi içinde taşıyıcı token ya da self-contained token kavramı, ilk olarak 2012 tarihli RFC 6749 OAuth 2.0 standardında belirtilmiştir. Bu kavram, içeriğinde bir hizmetin güvenlik kararlarını almak için kullanacağı veri veya iddiaları (claim) taşıyan bir token'ı ifade eder. Bu, yalnızca bir tanımlayıcı içeren ve hizmetin veriyi yerel olarak aramasına yarayan basit token'lardan ayrıdır. Self-contained token'lara en yaygın örnekler JSON Web Tokens (JWT) ve SAML assertion'lardır.

Self-contained token kullanımı, OAuth ve OIDC dışında bile oldukça yaygın hale gelmiştir. Aynı zamanda bu mekanizmanın güvenliği, token'ın bütünlüğünün doğrulanabilmesine ve belirli bir bağlam için geçerli olduğunun teyit edilmesine bağlıdır. Bu süreçte birçok güvenlik açığı ortaya çıkabilir ve bu bölüm, uygulamaların alması gereken önlemleri ayrıntılı şekilde açıklamaktadır.

## V9.1 Token Kaynağı ve Bütünlüğü

Bu bölüm, token'ın güvenilir bir tarafça üretildiğini ve üzerinde oynama yapılmadığını sağlamak için gereken gereksinimleri içerir.

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **9.1.1** | Self-contained token'ların içerikleri kabul edilmeden önce, oynama (tampering) saldırılarına karşı dijital imza veya MAC ile doğrulama yapıldığı doğrulanmalıdır. | 1 |
| **9.1.2** | Belirli bir bağlam için yalnızca bir allowlist üzerinde bulunan algoritmaların self-contained token oluşturmak ve doğrulamak için kullanılabildiği doğrulanmalıdır. Bu allowlist, yalnızca simetrik ya da yalnızca asimetrik algoritmaları içermeli ve kesinlikle 'None' algoritmasını içermemelidir. Hem simetrik hem de asimetrik algoritmalar desteklenmek zorundaysa, anahtar karışıklığını (key confusion) önlemek için ek kontroller uygulanmalıdır. | 1 |
| **9.1.3** | Self-contained token'ları doğrulamak için kullanılan anahtar malzemesinin, token issuer için önceden yapılandırılmış güvenilir kaynaklardan alındığı doğrulanmalıdır. Bu, saldırganların güvenilmeyen kaynak ve anahtarları belirtmesini engeller. JWT ve diğer JWS yapılarında 'jku', 'x5u' ve 'jwk' gibi header'lar güvenilir kaynaklardan oluşan bir allowlist'e göre doğrulanmalıdır. | 1 |

## V9.2 Token İçeriği

Bir self-contained token içeriğine dayanarak güvenlik kararı alınmadan önce, token'ın geçerlilik süresi içinde sunulup sunulmadığı ve belirli bir hizmet tarafından belirli bir amaç için kullanıma uygun olup olmadığı doğrulanmalıdır. Bu, aynı issuer'dan gelen farklı token türlerinin farklı hizmetler arasında güvensiz şekilde yeniden kullanılmasını önlemeye yardımcı olur.

OAuth ve OIDC'ye özgü gereksinimler ilgili bölümde yer almaktadır.

| # | Description | Level |
| :---: | :--- | :---: |
| **9.2.1** | Verify that, if a validity time span is present in the token data, the token and its content are accepted only if the verification time is within this validity time span. For example, for JWTs, the claims 'nbf' and 'exp' must be verified. | 1 |
| **9.2.2** | Verify that the service receiving a token validates the token to be the correct type and is meant for the intended purpose before accepting the token's contents. For example, only access tokens can be accepted for authorization decisions and only ID Tokens can be used for proving user authentication. | 2 |
| **9.2.3** | Verify that the service only accepts tokens which are intended for use with that service (audience). For JWTs, this can be achieved by validating the 'aud' claim against an allowlist defined in the service. | 2 |
| **9.2.4** | Verify that, if a token issuer uses the same private key for issuing tokens to different audiences, the issued tokens contain an audience restriction that uniquely identifies the intended audiences. This will prevent a token from being reused with an unintended audience. If the audience identifier is dynamically provisioned, the token issuer must validate these audiences in order to make sure that they do not result in audience impersonation. | 2 |

| # | Açıklama | Seviye |
| :---: | :--- | :---: |
| **9.2.1** | Token verisinde bir geçerlilik zaman aralığı (validity time span) varsa, yalnızca doğrulama zamanı bu zaman aralığı içerisindeyse token ve içeriği kabul edilmelidir. Örneğin, JWT'ler için 'nbf' ve 'exp' claim'leri doğrulanmalıdır. | 1 |
| **9.2.2** | Token'ı alan hizmetin, token içeriğini kabul etmeden önce bu token'ın doğru türde olduğunu ve sunulma amacına uygun olduğunu doğruladığı teyit edilmelidir. Örneğin, yalnızca erişim token'ları yetkilendirme kararları için, yalnızca ID Token'lar kullanıcı kimlik doğrulamasını kanıtlamak için kullanılabilir. | 2 |
| **9.2.3** | Hizmetin yalnızca kendisiyle kullanılması amaçlanan (audience) token'ları kabul ettiği doğrulanmalıdır. JWT'lerde bu, 'aud' claim'inin hizmet içinde tanımlı bir allowlist ile doğrulanması yoluyla sağlanabilir. | 2 |
| **9.2.4** | Eğer bir token issuer, farklı audience'lara token oluşturmak için aynı private key'i kullanıyorsa, oluşturulan token'ların hedef audience'ları benzersiz şekilde tanımlayan bir audience kısıtlaması içerdiği doğrulanmalıdır. Bu, bir token'ın farklı bir audience ile yeniden kullanılmasını önler. Audience tanımlayıcısı dinamik olarak sağlanıyorsa, token issuer bu audience'ları doğrulamalı ve audience taklitlerinin (impersonation) önüne geçmelidir. | 2 |

## Referanslar

Daha fazla bilgi için:

* [OWASP JSON Web Token Cheat Sheet for Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) (genel olarak yönlendirme için kullanışlı)
