# V3 웹 프론트엔드 보안
.
## 통제 목표

이 항목에서는 웹 프론트엔드를 통한 공격들을 막기 위한 요구사항들에 초점을 맞췄습니다. 이는 사물 간 통신(M2M) 해결책들에 대해서는 적용되지 않습니다.

## V3.1 웹 프론트엔드 보안 문서

이 섹션에서는 어플리케이션의 docs에서 알려줘야 할 브라우저 보안 특징들에 대해 설명합니다.

| # | 설명 | 단계 |
| :---: | :--- | :---: |
| **3.1.1** | 어플리케이션 docs에서 어플리케이션이 반드시 지원해야 하는, 예상되는 보안 특징들을 나타내고 있는지 확인해야 합니다. (예시: HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), 그리고 다른 관련된 HTTP 보안 메커니즘들) | 3 |

## V3.2 의도하지 않은 콘텐츠 접근

잘못된 콘텐츠나 기능을 렌더링하는 작업은 위협적인 콘텐츠를 실행하거나 나타나게 하는 결과를 초래할 수도 있습니다.

| # | 설명 | 단계 |
| :---: | :--- | :---: |
| **3.2.1** | 브라우저가 HTTP 응답에 대해 컨텐츠나 기능을 불러올 때, 의도하지 않은 상황이 보안적으로 통제되고 있는지 확인해야 합니다(예시: API, 유저가 올린 파일, 혹은 다른 리소스에 직접 접근할 때). | 1 |
| **3.2.2** | 콘텐츠는 HTML보다는 텍스트로 보여줌으로써, 의도하지 않은 HTML이나 JavaScript 등의 콘텐츠 실행을 막는 안전한 렌더 함수들을 사용함을 확인해야 합니다(createTextNode나 textContent) | 1 |
| **3.2.3** | 어플리케이션이 클라이언트 사이드 JavaScript를 사용할 때, 명시적 변수 사용, 엄격한 타입 체킹, 문서에서의 전역 변수 저장 지양, 그리고 네임스페이스 격리 구현 등으로 DOM clobbering을 막고 있음을 확인해야 합니다. | 3 |

## V3.3 쿠키 설정

이 섹션에서는 민감한 쿠키를 설정할 때, 어플리케이션 자체에서 만들어졌고, 콘텐츠 내용이 새어 나가거나, 부적절한 수정이 되는 것을 막는다는 더 높은 수준의 보장을 제공하기 위한 요구사항에 대해 설명합니다.

| # | 설명 | 단계 |
| :---: | :--- | :---: |
| **3.3.1** | 쿠키가 ‘Secure’ 속성이 있는지, 쿠키 이름에 '\__Host-’ 접두사가 사용되지 않았고, '__Secure-' 접두사가 사용되었는지 확인해야 합니다. | 1 |
| **3.3.2** | UI redress 공격, 그리고 CSRF라 알려진 브라우저 기반 요청 위조 공격들에 대한 노출을 제한하기 위해 각 쿠키의 ‘SameSite’ 속성 값이 쿠키의 목적에 맞게 설정되어 있는지 확인해야 합니다. | 2 |
| **3.3.3** | 다른 호스트들과 명시적으로 공유되는 쿠키에 대해서, '__Host-’ 접두사를 가지고 있는지 확인해야 합니다. | 2 |
| **3.3.4** | 쿠키의 값이 클라이언트-사이드 스크립트에서 접근이 가능한 걸 의도하지 않았다면(세션 토큰 등), 쿠키는 반드시 ‘HttpOnly’ 속성을 가져야 하고, 반드시 ‘Set-Cookie’ 헤더 필드를 통해 클라이언트에게 전달돼야 합니다. | 2 |
| **3.3.5** | 어플리케이션이 쿠키를 만들 때, 쿠키 이름과 값 길이가 합쳐서 4096바이트를 넘지 않는지 확인해야 합니다. 너무 큰 쿠키는 브라우저에 저장되지 않을 것이고, 요청 전달도 안될 것이며, 사용자가 그 쿠키에 의존적인 어플리케이션 기능을 사용하지 못할 것입니다. | 3 |

## V3.4 Browser Security Mechanism Headers

This section describes which security headers should be set on HTTP responses to enable browser security features and restrictions when handling responses from the application.

| # | Description | Level |
| :---: | :--- | :---: |
| **3.4.1** | Verify that a Strict-Transport-Security header field is included on all responses to enforce an HTTP Strict Transport Security (HSTS) policy. A maximum age of at least 1 year must be defined, and for L2 and up, the policy must apply to all subdomains as well. | 1 |
| **3.4.2** | Verify that the Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header field is a fixed value by the application, or if the Origin HTTP request header field value is used, it is validated against an allowlist of trusted origins. When 'Access-Control-Allow-Origin: *' needs to be used, verify that the response does not include any sensitive information. | 1 |
| **3.4.3** | Verify that HTTP responses include a Content-Security-Policy response header field which defines directives to ensure the browser only loads and executes trusted content or resources, in order to limit execution of malicious JavaScript. As a minimum, a global policy must be used which includes the directives object-src 'none' and base-uri 'none' and defines either an allowlist or uses nonces or hashes. For an L3 application, a per-response policy with nonces or hashes must be defined. | 2 |
| **3.4.4** | Verify that all HTTP responses contain an 'X-Content-Type-Options: nosniff' header field. This instructs browsers not to use content sniffing and MIME type guessing for the given response, and to require the response's Content-Type header field value to match the destination resource. For example, the response to a request for a style is only accepted if the response's Content-Type is 'text/css'. This also enables the use of the Cross-Origin Read Blocking (CORB) functionality by the browser. | 2 |
| **3.4.5** | Verify that the application sets a referrer policy to prevent leakage of technically sensitive data to third-party services via the 'Referer' HTTP request header field. This can be done using the Referrer-Policy HTTP response header field or via HTML element attributes. Sensitive data could include path and query data in the URL, and for internal non-public applications also the hostname. | 2 |
| **3.4.6** | Verify that the web application uses the frame-ancestors directive of the Content-Security-Policy header field for every HTTP response to ensure that it cannot be embedded by default and that embedding of specific resources is allowed only when necessary. Note that the X-Frame-Options header field, although supported by browsers, is obsolete and may not be relied upon. | 2 |
| **3.4.7** | Verify that the Content-Security-Policy header field specifies a location to report violations. | 3 |
| **3.4.8** | Verify that all HTTP responses that initiate a document rendering (such as responses with Content-Type text/html), include the Cross‑Origin‑Opener‑Policy header field with the same-origin directive or the same-origin-allow-popups directive as required. This prevents attacks that abuse shared access to Window objects, such as tabnabbing and frame counting. | 3 |

## V3.5 Browser Origin Separation

When accepting a request to sensitive functionality on the server side, the application needs to ensure the request is initiated by the application itself or by a trusted party and has not been forged by an attacker.

Sensitive functionality in this context could include accepting form posts for authenticated and non-authenticated users (such as an authentication request), state-changing operations, or resource-demanding functionality (such as data export).

The key protections here are browser security policies like Same Origin Policy for JavaScript and also SameSite logic for cookies. Another common protection is the CORS preflight mechanism. This mechanism will be critical for endpoints designed to be called from a different origin, but it can also be a useful request forgery prevention mechanism for endpoints which are not designed to be called from a different origin.

| # | Description | Level |
| :---: | :--- | :---: |
| **3.5.1** | Verify that, if the application does not rely on the CORS preflight mechanism to prevent disallowed cross-origin requests to use sensitive functionality, these requests are validated to ensure they originate from the application itself. This may be done by using and validating anti-forgery tokens or requiring extra HTTP header fields that are not CORS-safelisted request-header fields. This is to defend against browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF). | 1 |
| **3.5.2** | Verify that, if the application relies on the CORS preflight mechanism to prevent disallowed cross-origin use of sensitive functionality, it is not possible to call the functionality with a request which does not trigger a CORS-preflight request. This may require checking the values of the 'Origin' and 'Content-Type' request header fields or using an extra header field that is not a CORS-safelisted header-field. | 1 |
| **3.5.3** | Verify that HTTP requests to sensitive functionality use appropriate HTTP methods such as POST, PUT, PATCH, or DELETE, and not methods defined by the HTTP specification as "safe" such as HEAD, OPTIONS, or GET. Alternatively, strict validation of the Sec-Fetch-* request header fields can be used to ensure that the request did not originate from an inappropriate cross-origin call, a navigation request, or a resource load (such as an image source) where this is not expected. | 1 |
| **3.5.4** | Verify that separate applications are hosted on different hostnames to leverage the restrictions provided by same-origin policy, including how documents or scripts loaded by one origin can interact with resources from another origin and hostname-based restrictions on cookies. | 2 |
| **3.5.5** | Verify that messages received by the postMessage interface are discarded if the origin of the message is not trusted, or if the syntax of the message is invalid. | 2 |
| **3.5.6** | Verify that JSONP functionality is not enabled anywhere across the application to avoid Cross-Site Script Inclusion (XSSI) attacks. | 3 |
| **3.5.7** | Verify that data requiring authorization is not included in script resource responses, like JavaScript files, to prevent Cross-Site Script Inclusion (XSSI) attacks. | 3 |
| **3.5.8** | Verify that authenticated resources (such as images, videos, scripts, and other documents) can be loaded or embedded on behalf of the user only when intended. This can be accomplished by strict validation of the Sec-Fetch-* HTTP request header fields to ensure that the request did not originate from an inappropriate cross-origin call, or by setting a restrictive Cross-Origin-Resource-Policy HTTP response header field to instruct the browser to block returned content. | 3 |

## V3.6 External Resource Integrity

This section provides guidance for the safe hosting of content on third-party sites.

| # | Description | Level |
| :---: | :--- | :---: |
| **3.6.1** | Verify that client-side assets, such as JavaScript libraries, CSS, or web fonts, are only hosted externally (e.g., on a Content Delivery Network) if the resource is static and versioned and Subresource Integrity (SRI) is used to validate the integrity of the asset. If this is not possible, there should be a documented security decision to justify this for each resource. | 3 |

## V3.7 Other Browser Security Considerations

This section includes various other security controls and modern browser security features required for client-side browser security.

| # | Description | Level |
| :---: | :--- | :---: |
| **3.7.1** | Verify that the application only uses client-side technologies which are still supported and considered secure. Examples of technologies which do not meet this requirement include NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | 2 |
| **3.7.2** | Verify that the application will only automatically redirect the user to a different hostname or domain (which is not controlled by the application) where the destination appears on an allowlist. | 2 |
| **3.7.3** | Verify that the application shows a notification when the user is being redirected to a URL outside of the application's control, with an option to cancel the navigation. | 3 |
| **3.7.4** | Verify that the application's top-level domain (e.g., site.tld) is added to the public preload list for HTTP Strict Transport Security (HSTS). This ensures that the use of TLS for the application is built directly into the main browsers, rather than relying only on the Strict-Transport-Security response header field. | 3 |
| **3.7.5** | Verify that the application behaves as documented (such as warning the user or blocking access) if the browser used to access the application does not support the expected security features. | 3 |

## References

For more information, see also:

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
* [OWASP DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)
