# V3 Web Frontend Security

## Control Objective

This category focuses on requirements that protect against attacks executed via a web frontend. These requirements are not relevant for machine-to-machine solutions.

## V3.1 Web Frontend Security Documentation

This section defines the browser security features that should be specified in the application’s documentation.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.1.1** | Verify that application documentation states the expected security features that browser-based applications must support (such as HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), and other relevant HTTP security mechanisms). It must also define how the application behaves when these features are unavailable (such as warning the user or blocking access). | 3 | v5.0.be-1.50.1 |

## V3.2 Unintended Content Interpretation

Rendering content or functionality in an incorrect context can lead to malicious content being executed or displayed.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.2.1** | Verify that security controls are in place to prevent browsers from rendering content or functionality in HTTP responses in an incorrect context (e.g., when an API, a user-uploaded file, or other resource is requested directly). Possible controls include: not serving the content unless HTTP request header fields (such as Sec-Fetch-*) indicate the correct context, using the sandbox directive of the Content-Security-Policy header field, or using the attachment disposition type in the Content-Disposition header field. | 1 | v5.0.be-50.6.1 |
| **3.2.2** | Verify that content intended to be displayed as text, rather than rendered as HTML, is handled using safe rendering functions (such as createTextNode or textContent) to prevent unintended execution of content such as HTML or JavaScript. | 1 | v5.0.be-50.6.2 |

## V3.3 Cookie Setup

This section provides requirements for how to securely configure a sensitive cookie to provide a higher level of assurance that it was created by the application itself and to prevent its contents from leaking or being inappropriately modified.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.3.1** | Verify that cookies have the 'Secure' attribute set, and if the '\__Host-' prefix is not used for the cookie name, the '__Secure-' prefix must be used for the cookie name. | 1 | v5.0.be-50.2.1 |
| **3.3.2** | Verify that each cookie’s 'SameSite' attribute value is set according to the purpose of the cookie, to limit exposure to user-interface redress attacks and browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF). | 2 | v5.0.be-50.2.3 |
| **3.3.3** | Verify that cookies have the '__Host-' prefix for the cookie name unless they are explicitly designed to be shared with other hosts. | 2 | v5.0.be-50.2.4 |
| **3.3.4** | Verify that if the value of a cookie is not meant to be accessible to client-side scripts (e.g., a session token), the cookie must have the 'HttpOnly' attribute set, and the same value (e.g., session token) must only be transferred via the 'Set-Cookie' header field. | 2 | v5.0.be-50.2.2 |
| **3.3.5** | Verify that when the application writes a cookie, the combined name and value length does not exceed 4096 bytes. Overly large cookies will not be stored by the browser and therefore will not be sent with requests, preventing reliance on that cookie from breaking functionality. | 3 | v5.0.be-50.2.5 |

## V3.4 Browser Security Mechanism Headers

This section indicates which security headers should be set on HTTP responses to enable browser security features and restrictions.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.4.1** | Verify that a Strict-Transport-Security header is included on all responses to enforce an HSTS policy. A maximum age of at least 1 year must be defined, and for L2 and up, the policy must apply to all subdomains. | 1 | v5.0.be-50.3.3 |
| **3.4.2** | Verify that the CORS Access-Control-Allow-Origin header is fixed by the application or, if echoing the Origin header, validated against an allowlist of trusted origins. When Access-Control-Allow-Origin: * is used, verify that the response contains no sensitive information. | 1 | v5.0.be-50.3.6 |
| **3.4.3** | Verify that HTTP responses include a Content-Security-Policy header defining directives to ensure the browser only loads and executes trusted resources. At minimum, a global policy must include object-src 'none' and base-uri 'none', and define either an allowlist or use nonces or hashes. For L3, a per-response policy with nonces or hashes must be defined. | 2 | v5.0.be-50.3.1 |
| **3.4.4** | Verify that all responses include an X-Content-Type-Options: nosniff header field. | 2 | v5.0.be-50.3.2 |
| **3.4.5** | Verify that the application sets a Referrer-Policy header or equivalent HTML attribute to prevent leakage of sensitive data (such as URL path, query data, or hostname) via the Referer header. | 2 | v5.0.be-50.3.4 |
| **3.4.6** | Verify that the application uses the frame-ancestors directive of the Content-Security-Policy header on every response to prevent default embedding, allowing only necessary resources. Note that X-Frame-Options is obsolete and must not be relied upon. | 2 | v5.0.be-50.3.5 |
| **3.4.7** | Verify that the Content-Security-Policy header specifies a reporting endpoint for violations. | 3 | v5.0.be-50.3.7 |

## V3.5 Browser Origin Separation

When accepting requests for sensitive functionality, the application must ensure they originate from itself or a trusted party and have not been forged by an attacker.

Sensitive functionality may include form posts for authenticated or unauthenticated users (such as authentication requests), state-changing operations, or resource-intensive features (such as data export).

Key protections include the Same Origin Policy for JavaScript and SameSite logic for cookies. CORS preflight is also critical for endpoints intended to be called from different origins, and it can help prevent request forgery on other endpoints.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.5.1** | Verify that CORS-safelisted requests for sensitive functionality are validated to ensure they originate from the application—e.g., by validating anti-forgery tokens or requiring additional non-safelisted headers—to defend against CSRF attacks. | 1 | v5.0.be-50.4.1 |
| **3.5.2** | Verify that if CORS preflight is used to protect sensitive functionality, it is impossible to invoke that functionality with a CORS-safelisted request. This may require validating the Origin and Content-Type headers or using a non-safelisted header. | 1 | v5.0.be-50.4.3 |
| **3.5.3** | Verify that HTTP methods for sensitive functionality are appropriate (POST, PUT, PATCH, DELETE—not safe methods such as GET, HEAD, OPTIONS). Alternatively, strictly validate Sec-Fetch-* headers to ensure requests did not originate from unauthorized cross-origin calls or resource loads. | 1 | v5.0.be-50.4.4 |
| **3.5.4** | Verify that separate applications are hosted on different hostnames to leverage same-origin policy restrictions on scripts and cookies. | 2 | v5.0.be-50.1.1 |
| **3.5.5** | Verify that messages received via postMessage are discarded if the message origin is untrusted or the message syntax is invalid. | 2 | v5.0.be-50.4.2 |
| **3.5.6** | Verify that JSONP is not enabled anywhere in the application to avoid XSSI attacks. | 3 | v5.0.be-50.5.1 |
| **3.5.7** | Verify that data requiring authorization is not included in script responses (e.g., JavaScript files) to prevent XSSI attacks. | 3 | v5.0.be-50.5.2 |
| **3.5.8** | Verify that authenticated resources (such as images, videos, scripts, and other documents) load or embed on behalf of the user only when intended—e.g., by validating Sec-Fetch-* headers or setting a restrictive Cross-Origin-Resource-Policy header to block unauthorized content. | 3 | v5.0.be-50.5.3 |

## V3.6 External Resource Integrity

This section provides guidance for the safe hosting of content on third-party sites.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.6.1** | Verify that client-side assets (JavaScript libraries, CSS, web fonts) are hosted externally (e.g., on a CDN) only if they are static and versioned, and Subresource Integrity (SRI) is used to validate the asset. If not, a documented security decision must justify each resource. | 3 | v5.0.be-50.7.1 |

## V3.7 Other Browser Security Considerations

This section includes various other security controls and modern browser security features required for client-side security.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.7.1** | Verify that the application uses only supported, secure client-side technologies. Examples of disallowed technologies include NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NaCl, or Java applets. | 2 | v5.0.be-50.8.2 |
| **3.7.2** | Verify that automatic redirects to external domains occur only when the destination is on an allowlist. | 2 | v5.0.be-50.8.5 |
| **3.7.3** | Verify that the application’s top-level domain is added to the HSTS preload list, ensuring TLS enforcement is built into browsers rather than relying solely on the Strict-Transport-Security header. | 3 | v5.0.be-50.8.4 |
| **3.7.4** | Verify that the application shows a notification when the user is redirected to a URL outside the application’s control, with an option to cancel the navigation. | 3 | v5.0.be-50.8.1 |
| **3.7.5** | Verify that the application behaves as documented (such as warning the user or blocking access) if the browser does not support the expected security features. | 3 | v5.0.be-50.8.3 |

## References

For more information, see also:

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [Sandboxing third-party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
