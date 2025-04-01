# V3 Web Frontend Security

## Control Objective

The category focuses on requirements that protect against attacks that are executed via a web frontend for an application. These requirements will not be relevant for machine-to-machine solutions.

## V3.1 Web Frontend Security Documentation

This section defines the browser security features that should be specified in the application's documentation.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.1.1** | Verify that application documentation states the expected security features that browsers using the application must support (such as HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), and other relevant HTTP security mechanisms). It must also define how the application must behave when some of these features are not available (such as warning the user or blocking access). | 3 | v5.0.be-1.50.1 |

## V3.2 Unintended Content Interpretation

Rendering content or functionality in an incorrect context can lead to a wide variety of security issues.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.2.1** | Verify that security controls are in place to prevent browsers from rendering content or functionality in HTTP responses in an incorrect context (e.g., when an API, a user-uploaded file or other resource is requested directly). Possible controls could include: not serving the content unless HTTP request header fields (such as Sec-Fetch-\*) indicate it is the correct context, using the sandbox directive of the Content-Security-Policy header field or using the attachment disposition type in the Content-Disposition header field. | 1 | v5.0.be-50.6.1 |
| **3.2.2** | Verify that content intended to be displayed as text, rather than rendered as HTML, is handled using safe rendering functions (such as createTextNode or textContent) to prevent unintended execution of content such as HTML or JavaScript. | 1 | v5.0.be-50.6.2 |

## V3.3 Cookie Setup

This section provides requirements for how to securely configure sensitive cookies to reduce the risk of them being stolen or used inappropriately.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.3.1** | Verify that cookies have the 'Secure' attribute set, and if the '\__Host-' prefix is not used for the cookie name, the '__Secure-' prefix must be used for the cookie name. | 1 | v5.0.be-50.2.1 |
| **3.3.2** | Verify that each cookie's 'SameSite' attribute value is set according to the purpose of the cookie, to limit exposure to user interface redress attacks and browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF). | 2 | v5.0.be-50.2.3 |
| **3.3.3** | Verify that cookies have the '__Host-' prefix for the cookie name unless they are explicitly designed to be shared with other hosts. | 2 | v5.0.be-50.2.4 |
| **3.3.4** | Verify that if the value of a cookie is not meant to be accessible to client-side scripts (such as a session token), the cookie must have the 'HttpOnly' attribute set and the same value (e. g. session token) must only be transferred to the client via the 'Set-Cookie' header field. | 2 | v5.0.be-50.2.2 |
| **3.3.5** | Verify that when the application writes a cookie the cookie name and value length combined are not over 4096 bytes. Overly large cookies will not be stored by the browser and therefore not sent with requests, preventing the user from using application functionality which relies on that cookie. | 3 | v5.0.be-50.2.5 |

## V3.4 Browser Security Mechanism Headers

This section indicates which security headers should be set on HTTP responses to prevent various types of attack that could disclose sensitive data.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.4.1** | Verify that a Strict-Transport-Security header field is included on all responses to enforce an HTTP Strict Transport Security (HSTS) policy. A maximum age of at least 1 year must be defined, and for L2 and up, the policy must apply to all subdomains as well. | 1 | v5.0.be-50.3.3 |
| **3.4.2** | Verify that the Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header field is validated against an allowlist of trusted origins. When 'Access-Control-Allow-Origin: *' needs to be used, verify that the responses do not include any sensitive information. | 1 | v5.0.be-50.3.6 |
| **3.4.3** | Verify that every HTTP response includes a Content-Security-Policy header field to reduce the risk of malicious JavaScript. The directives object-src 'none' and base-uri 'none' must be defined. For an L3 application, a per-response policy with nonces or hashes must be defined. | 2 | v5.0.be-50.3.1 |
| **3.4.4** | Verify that all responses contain a X-Content-Type-Options: nosniff header field. | 2 | v5.0.be-50.3.2 |
| **3.4.5** | Verify that an suitable Referrer-Policy header field is included to prevent sensitive information in the URL from being exposed to untrusted parties via the Referer header. | 2 | v5.0.be-50.3.4 |
| **3.4.6** | Verify that the web application uses the frame-ancestors directive of the Content-Security-Policy header field for every HTTP response to ensure that it cannot be embedded by default and that embedding of specific resources is allowed only when necessary. Note that the X-Frame-Options header field, although supported by browsers, is obsolete and may not be relied upon. | 2 | v5.0.be-50.3.5 |
| **3.4.7** | Verify that the Content-Security-Policy header field specifies a location to report violations. | 3 | v5.0.be-50.3.7 |

## V3.5 Browser Origin Separation

When accepting a request to sensitive functionality on the server side, the application needs to be sure the request is initiated by the application itself or by a trusted party and has not been forged by an attacker.

Sensitive functionality in this context could include accepting form posts for authenticated and non-authenticated users (such as an authentication request), state-changing operations, or resource-demanding functionality (such as data export).

The key protections here are browser security policies like Same Origin Policy for JavaScript and also SameSite logic for cookies. Another common protection is the CORS preflight mechanism. This mechanism will be critical for endpoints designed to be called from a different origin, but it can also be a useful request forgery prevention mechanism for endpoints which are not designed to be called from a different origin.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.5.1** | Verify that CORS-safelisted requests to sensitive functionality are checked to ensure that they originate from the application itself. This may be done by using and validating anti-forgery tokens or requiring extra HTTP headers that are not CORS-safelisted request-headers. This is to defend against browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF). | 1 | v5.0.be-50.4.1 |
| **3.5.2** | Verify that, if the application relies on the CORS preflight mechanism to prevent disallowed cross-origin use of sensitive functionality, it is not possible to call the functionality with a CORS-safelisted request. This may require checking the values of the 'Origin' and 'Content-Type' request headers or using an extra header field that is not CORS-safelisted. | 1 | v5.0.be-50.4.3 |
| **3.5.3** | Verify that calls to sensitive functionality use appropriate HTTP methods such as POST, PUT, PATCH or DELETE, and not methods defined by the HTTP specification as "safe" such as HEAD, OPTIONS, or GET. Alternatively, strict validation of the Sec-Fetch-* request header fields can be used to ensure that the request did not originate from an inappropriate cross-origin call, a navigation request, or a resource load (such as an image source) where this is not expected. This is particularly important if the application does not distinguish between URL parameters and message body parameters. | 1 | v5.0.be-50.4.4 |
| **3.5.4** | Verify that separate applications are hosted on different hostnames to leverage the restrictions provided by same-origin policy, including how documents or scripts loaded by one origin can interact with resources from another origin and hostname-based restrictions on cookies. | 2 | v5.0.be-50.1.1 |
| **3.5.5** | Verify that messages received by the postMessage interface are discarded if the origin of the message is not trusted, or if the syntax of the message is invalid. | 2 | v5.0.be-50.4.2 |
| **3.5.6** | Verify that JSONP functionality is not enabled anywhere across the application to avoid Cross-Site Script Inclusion (XSSI) attacks. | 3 | v5.0.be-50.5.1 |
| **3.5.7** | Verify that data requiring authorization is not included in script resource responses, like JavaScript files, to prevent Cross-Site Script Inclusion (XSSI) attacks. | 3 | v5.0.be-50.5.2 |

## V3.6 External Resource Integrity

This section provides guidance for the safe hosting of content on third-party sites.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.6.1** | Verify that if client-side assets, such as JavaScript libraries, CSS or web fonts, are hosted externally on a Content Delivery Network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset. | 3 | v5.0.be-50.7.1 |

## V3.7 Other Browser Security Considerations

This section includes various other security controls and modern browser security features which are required for client-side browser security.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **3.7.1** | Verify that the application only uses client-side technologies which are still supported and considered secure. Examples of technologies which do not meet this requirement include NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | 2 | v5.0.be-50.8.2 |
| **3.7.2** | Verify that the application will only automatically redirect the user to a different URL directly from an application URL where the destination appears on an allowlist. | 2 | v5.0.be-50.8.5 |
| **3.7.3** | Verify that the application's top-level domain (e.g., site.tld) is added to the public preload list for HTTP Strict Transport Security (HSTS). This ensures that the use of TLS for the application is built directly into the main browsers, rather than relying only on the Strict-Transport-Security response header field. | 3 | v5.0.be-50.8.4 |
| **3.7.4** | Verify that the application shows a notification when the user is being redirected to a URL outside of the application's control, with an option to cancel the navigation. | 3 | v5.0.be-50.8.1 |
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
