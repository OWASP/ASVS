# V3 Web Ön Uç (Frontend) Güvenliği

## Kontrol Amacı

Bu kategori, bir web frontend'i üzerinden gerçekleştirilen saldırılara karşı koruma sağlamak amacıyla belirlenmiş gereksinimlere odaklanır. Bu gereksinimler, makineden makineye çözümler için geçerli değildir.

## V3.1 Web Frontend Güvenlik Dokümantasyonu

Bu bölüm, uygulamanın dokümantasyonunda belirtilmesi gereken tarayıcı güvenlik özelliklerini tanımlar.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.1.1** | Uygulama dokümantasyonunda, uygulamayı kullanan tarayıcıların desteklemesi gereken güvenlik özelliklerinin (ör. HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP) ve diğer ilgili HTTP güvenlik mekanizmaları) tanımlandığı doğrulanmalıdır. Ayrıca bu özelliklerin mevcut olmadığı durumlarda uygulamanın nasıl davranması gerektiği (ör. kullanıcıyı uyarmak veya erişimi engellemek) de tanımlanmalıdır. | 3 | v5.0.be-1.50.1 |

## V3.2 İçeriğin Yanlış Yorumlanması

İçerik veya işlevin yanlış bir bağlamda sunulması, kötü amaçlı içeriğin çalıştırılmasına veya görüntülenmesine neden olabilir.

| # | Açıklama | Seviye | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.2.1** | Tarayıcıların HTTP yanıtlarında içerik veya işlevi yanlış bir bağlamda sunmalarını önlemek amacıyla güvenlik kontrollerinin uygulandığı doğrulanmalıdır (ör. API, kullanıcı tarafından yüklenen dosya veya başka bir kaynağın doğrudan çağrılması durumunda). Olası kontroller arasında; yalnızca HTTP istek başlıklarının (ör. Sec-Fetch-\*) doğru bağlamı gösterdiği durumlarda içeriğin sunulması, Content-Security-Policy başlığında "sandbox" yönergesinin kullanılması veya Content-Disposition başlığında "attachment" biçiminin kullanılması yer alabilir. | 1 | v5.0.be-50.6.1 |
| **3.2.2** | HTML yerine metin olarak görüntülenmesi amaçlanan içeriğin, HTML veya JavaScript gibi içeriklerin istenmeden çalıştırılmasını önleyecek şekilde "createTextNode" veya "textContent" gibi güvenli işleme fonksiyonlarıyla işlendiği doğrulanmalıdır. | 1 | v5.0.be-50.6.2 |
| **3.2.3** | Uygulamanın istemci tarafı JavaScript kullanırken açık değişken tanımlamaları yaparak, sıkı tür kontrolü uygulayarak, global değişkenleri document nesnesine kaydetmekten kaçınarak ve ad alanı izolasyonu sağlayarak DOM clobbering’den kaçındığı doğrulanmalıdır. | 3 | v5.0.be-10.4.2 |

## V3.3 Çerez Yapılandırması

Bu bölüm, hassas çerezlerin güvenli biçimde yapılandırılması için gereksinimleri tanımlar. Amaç, çerezlerin gerçekten uygulama tarafından oluşturulduğuna dair daha yüksek düzeyde güvence sağlamak ve içeriklerinin sızmasını veya uygunsuz şekilde değiştirilmesini önlemektir.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.3.1** | Çerezlerin 'Secure' niteliğine sahip olduğu ve eğer çerez adı '\__Host-' ön eki ile başlamıyorsa, '__Secure-' ön ekinin kullanıldığı doğrulanmalıdır. | 1 | v5.0.be-50.2.1 |
| **3.3.2** | Kullanıcı arayüzü kandırma saldırılarına ve tarayıcı tabanlı istek sahteciliği saldırılarına (CSRF) karşı koruma sağlamak amacıyla, her çerezin 'SameSite' niteliğinin kullanım amacına uygun şekilde ayarlandığı doğrulanmalıdır. | 2 | v5.0.be-50.2.3 |
| **3.3.3** | Çerez adı, diğer sunucularla paylaşılmak üzere açıkça tasarlanmadığı sürece '__Host-' ön eki ile tanımlanmalıdır. | 2 | v5.0.be-50.2.4 |
| **3.3.4** | Bir çerez değeri istemci tarafı betikleri tarafından erişilememesi gereken bir veri içeriyorsa (ör. oturum token'ı), çerezin 'HttpOnly' niteliğine sahip olduğu ve aynı değerin (ör. oturum token'ı) yalnızca 'Set-Cookie' başlığı ile istemciye iletildiği doğrulanmalıdır. | 2 | v5.0.be-50.2.2 |
| **3.3.5** | Uygulama bir çerez oluştururken, çerez adı ve değerinin toplam uzunluğunun 4096 baytı aşmadığı doğrulanmalıdır. Çok büyük çerezler tarayıcı tarafından saklanmaz ve isteklerle gönderilmez; bu da çereze bağlı çalışan uygulama işlevlerinin bozulmasına yol açabilir. | 3 | v5.0.be-50.2.5 |

## V3.4 Browser Security Mechanism Headers

This section describes which security headers should be set on HTTP responses to enable browser security features and restrictions when handling responses from the application.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.4.1** | Verify that a Strict-Transport-Security header field is included on all responses to enforce an HTTP Strict Transport Security (HSTS) policy. A maximum age of at least 1 year must be defined, and for L2 and up, the policy must apply to all subdomains as well. | 1 | v5.0.be-50.3.3 |
| **3.4.2** | Verify that the Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header field is a fixed value by the application, or if the Origin HTTP request header field value is used, it is validated against an allowlist of trusted origins. When 'Access-Control-Allow-Origin: *' needs to be used, verify that the response does not include any sensitive information. | 1 | v5.0.be-50.3.6 |
| **3.4.3** | Verify that HTTP responses include a Content-Security-Policy response header field which defines directives to ensure the browser only loads and executes trusted content or resources, in order to limit execution of malicious JavaScript. As a minimum, a global policy must be used which includes the directives object-src 'none' and base-uri 'none' and defines either an allowlist or uses nonces or hashes. For an L3 application, a per-response policy with nonces or hashes must be defined. | 2 | v5.0.be-50.3.1 |
| **3.4.4** | Verify that all HTTP responses contain an 'X-Content-Type-Options: nosniff' header field. This instructs browsers not to use content sniffing and MIME type guessing for the given response, and to require the response's Content-Type header field value to match the destination resource. For example, the response to a request for a style is only accepted if the response's Content-Type is 'text/css'. This also enables the use of the Cross-Origin Read Blocking (CORB) functionality by the browser. | 2 | v5.0.be-50.3.2 |
| **3.4.5** | Verify that the application sets a referrer policy to prevent leakage of technically sensitive data to third-party services via the 'Referer' HTTP request header field. This can be done using the Referrer-Policy HTTP response header field or via HTML element attributes. Sensitive data could include path and query data in the URL, and for internal non-public applications also the hostname. | 2 | v5.0.be-50.3.4 |
| **3.4.6** | Verify that the web application uses the frame-ancestors directive of the Content-Security-Policy header field for every HTTP response to ensure that it cannot be embedded by default and that embedding of specific resources is allowed only when necessary. Note that the X-Frame-Options header field, although supported by browsers, is obsolete and may not be relied upon. | 2 | v5.0.be-50.3.5 |
| **3.4.7** | Verify that the Content-Security-Policy header field specifies a location to report violations. | 3 | v5.0.be-50.3.7 |
| **3.4.8** | Verify that all HTTP responses that initiate a document rendering (such as responses with Content-Type text/html), include the Cross‑Origin‑Opener‑Policy header field with the same-origin directive or the same-origin-allow-popups directive as required. This prevents attacks that abuse shared access to Window objects, such as tabnabbing and frame counting. | 3 | v5.0.be-50.3.8 |

## V3.5 Browser Origin Separation

When accepting a request to sensitive functionality on the server side, the application needs to ensure the request is initiated by the application itself or by a trusted party and has not been forged by an attacker.

Sensitive functionality in this context could include accepting form posts for authenticated and non-authenticated users (such as an authentication request), state-changing operations, or resource-demanding functionality (such as data export).

The key protections here are browser security policies like Same Origin Policy for JavaScript and also SameSite logic for cookies. Another common protection is the CORS preflight mechanism. This mechanism will be critical for endpoints designed to be called from a different origin, but it can also be a useful request forgery prevention mechanism for endpoints which are not designed to be called from a different origin.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.5.1** | Verify that, if the application does not rely on the CORS preflight mechanism to prevent disallowed cross-origin requests to use sensitive functionality, these requests are validated to ensure they originate from the application itself. This may be done by using and validating anti-forgery tokens or requiring extra HTTP header fields that are not CORS-safelisted request-header fields. This is to defend against browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF). | 1 | v5.0.be-50.4.1 |
| **3.5.2** | Verify that, if the application relies on the CORS preflight mechanism to prevent disallowed cross-origin use of sensitive functionality, it is not possible to call the functionality with a request which does not trigger a CORS-preflight request. This may require checking the values of the 'Origin' and 'Content-Type' request header fields or using an extra header field that is not a CORS-safelisted header-field. | 1 | v5.0.be-50.4.3 |
| **3.5.3** | Verify that HTTP requests to sensitive functionality use appropriate HTTP methods such as POST, PUT, PATCH, or DELETE, and not methods defined by the HTTP specification as "safe" such as HEAD, OPTIONS, or GET. Alternatively, strict validation of the Sec-Fetch-* request header fields can be used to ensure that the request did not originate from an inappropriate cross-origin call, a navigation request, or a resource load (such as an image source) where this is not expected. | 1 | v5.0.be-50.4.4 |
| **3.5.4** | Verify that separate applications are hosted on different hostnames to leverage the restrictions provided by same-origin policy, including how documents or scripts loaded by one origin can interact with resources from another origin and hostname-based restrictions on cookies. | 2 | v5.0.be-50.1.1 |
| **3.5.5** | Verify that messages received by the postMessage interface are discarded if the origin of the message is not trusted, or if the syntax of the message is invalid. | 2 | v5.0.be-50.4.2 |
| **3.5.6** | Verify that JSONP functionality is not enabled anywhere across the application to avoid Cross-Site Script Inclusion (XSSI) attacks. | 3 | v5.0.be-50.5.1 |
| **3.5.7** | Verify that data requiring authorization is not included in script resource responses, like JavaScript files, to prevent Cross-Site Script Inclusion (XSSI) attacks. | 3 | v5.0.be-50.5.2 |
| **3.5.8** | Verify that authenticated resources (such as images, videos, scripts, and other documents) can be loaded or embedded on behalf of the user only when intended. This can be accomplished by strict validation of the Sec-Fetch-* HTTP request header fields to ensure that the request did not originate from an inappropriate cross-origin call, or by setting a restrictive Cross-Origin-Resource-Policy HTTP response header field to instruct the browser to block returned content. | 3 | v5.0.be-50.5.3 |

## V3.6 External Resource Integrity

This section provides guidance for the safe hosting of content on third-party sites.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.6.1** | Verify that client-side assets, such as JavaScript libraries, CSS, or web fonts, are only hosted externally (e.g., on a Content Delivery Network) if the resource is static and versioned and Subresource Integrity (SRI) is used to validate the integrity of the asset. If this is not possible, there should be a documented security decision to justify this for each resource. | 3 | v5.0.be-50.7.1 |

## V3.7 Other Browser Security Considerations

This section includes various other security controls and modern browser security features required for client-side browser security.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.7.1** | Verify that the application only uses client-side technologies which are still supported and considered secure. Examples of technologies which do not meet this requirement include NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | 2 | v5.0.be-50.8.2 |
| **3.7.2** | Verify that the application will only automatically redirect the user to a different hostname or domain (which is not controlled by the application) where the destination appears on an allowlist. | 2 | v5.0.be-50.8.5 |
| **3.7.3** | Verify that the application shows a notification when the user is being redirected to a URL outside of the application's control, with an option to cancel the navigation. | 3 | v5.0.be-50.8.1 |
| **3.7.4** | Verify that the application's top-level domain (e.g., site.tld) is added to the public preload list for HTTP Strict Transport Security (HSTS). This ensures that the use of TLS for the application is built directly into the main browsers, rather than relying only on the Strict-Transport-Security response header field. | 3 | v5.0.be-50.8.4 |
| **3.7.5** | Verify that the application behaves as documented (such as warning the user or blocking access) if the browser used to access the application does not support the expected security features. | 3 | v5.0.be-50.8.3 |

## References

For more information, see also:

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [Sandboxing third-party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
