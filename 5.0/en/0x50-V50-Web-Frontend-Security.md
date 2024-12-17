# V50 Web Frontend Security

The category focuses on requirements that protect against attacks that are executed via a web frontend for an application. These requirements will not be relevant for machine-to-machine solutions.

## V1.50 Web Frontend Security Documentation

Application documentation must specify required browser security features.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.50.1** | [ADDED] Verify that application documentation states the expected security features that browsers using the application should support (such as HTTPS, HSTS, Content Security Policy (CSP), and other relevant HTTP security mechanisms). It should also define how the application must behave when some of these features are not available (such as warning the user or blocking access). | | | ✓ | |

## V50.1 Site Isolation Architecture

To leverage the benefits of same-origin isolation, applications should be hosted on distinct hostnames.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.1.1** | [ADDED, DEPRECATES 3.4.5] Verify that separate applications are hosted on different hostnames to leverage the restrictions provided by same-origin policy, including how documents or scripts loaded by one origin can interact with resources from another origin and hostname-based restrictions on cookies. | ✓ | ✓ | ✓ | 668 |

## V50.2 Cookie Setup

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.2.1** | [MODIFIED, MOVED FROM 3.4.1] Verify that cookies have the 'Secure' attribute set, and if the '\__Host-' prefix is not used for the cookie name, the '__Secure-' prefix must be used for the cookie name. | ✓ | ✓ | ✓ | 614 |
| **50.2.2** | [MODIFIED, MOVED FROM 3.4.2, LEVEL L1 > L2] Verify that if the value of a cookie is not meant to be accessible to client-side scripts (such as a session token), the cookie must have the 'HttpOnly' attribute set and the same value (e. g. session token) must only be transferred to the client via the 'Set-Cookie' header field. | | ✓ | ✓ | 1004 |
| **50.2.3** | [MODIFIED, MOVED FROM 3.4.3, LEVEL L1 > L2] Verify that each cookie's 'SameSite' attribute value is set according to the purpose of the cookie, to limit exposure to cross-site request forgery and user interface redress attacks. | | ✓ | ✓ | 1275 |
| **50.2.4** | [MODIFIED, MOVED FROM 3.4.4, LEVEL L1 > L2] Verify that cookies have the '__Host-' prefix for the cookie name unless they are explicitly designed to be shared with other hosts. | | ✓ | ✓ | |
| **50.2.5** | [ADDED] Verify that when the application writes a cookie the cookie name and value length combined are not over 4096 bytes. Overly large cookies will not be stored by the browser and therefore not sent with requests, preventing the user from using application functionality which relies on that cookie. | | ✓ | ✓ | |

## V50.3 Browser Security Mechanism Headers

HTTP responses must include security headers to set rules to how browsers can securely render content.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.3.1** | [MODIFIED, MOVED FROM 14.4.3, LEVEL L1 > L2] Verify that every HTTP response includes a Content-Security-Policy header to reduce the risk of malicious JavaScript. The directives object-src 'none' and base-uri 'none' must be defined. For an L3 application, a per-response policy with nonces or hashes must be defined. | | ✓ | ✓ | |
| **50.3.2** | [GRAMMAR, MOVED FROM 14.4.4] Verify that all responses contain a X-Content-Type-Options: nosniff header field. | ✓ | ✓ | ✓ | 116 |
| **50.3.3** | [MODIFIED, MOVED FROM 14.4.5] Verify that a Strict-Transport-Security header field is included on all responses and for all subdomains, such as Strict-Transport-Security: max-age=31536000; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **50.3.4** | [MODIFIED, MOVED FROM 14.4.6] Verify that an suitable Referrer-Policy header is included to prevent sensitive information in the URL from being exposed to untrusted parties via the Referer header. | ✓ | ✓ | ✓ | 116 |
| **50.3.5** | [MODIFIED, MOVED FROM 14.4.7] Verify that the content of the web application cannot be embedded in a third-party site by default, and that embedding of specific resources is allowed only when necessary, using the Content-Security-Policy frame-ancestors directive. Note that X-Frame-Options is now obsolete. | ✓ | ✓ | ✓ | 1021 |
| **50.3.6** | [ADDED, SPLIT FROM 14.5.3] Verify that the Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header field is validated against an allowlist of trusted origins. When "Access-Control-Allow-Origin: *" needs to be used, verify that the responses do not include any sensitive information. | ✓ | ✓ | ✓ | 183 |
| **50.3.7** | [ADDED] Verify that the Content-Security-Policy header field specifies a location to report violations. | | | ✓ | |
| **50.3.8** | [ADDED] Verify that the application's top-level domain (e.g., site.tld) is added to the public HSTS preload list so that the use of TLS for the application is built directly into the main browsers, rather than relying only on the relevant HTTP response header field. | | | ✓ | |

## V50.4 Browser Origin Separation

When accepting a request on the server side, we need to be sure it is initiated by the application itself or by a trusted party.

The keywords here are browser security policies like Same Origin Policy for JavaScript and also SameSite logic for cookies.

The category should contain requirements with ideas:

* Verify that the request was initiated by a trusted party (CSRF, CORS misconfiguration)
* Verify that the response is readable only for trusted parties (CORS misconfiguration)

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.4.1** | [MODIFIED, MOVED FROM 4.2.2, MERGED FROM 13.2.3] Verify that the application defends against Cross-Site Request Forgery (CSRF) attacks to protect authenticated or sensitive public functionality, using the development framework's built-in anti-CSRF functionality or CSRF tokens, along with additional defense-in-depth measures. | ✓ | ✓ | ✓ | 352 |
| **50.4.2** | [ADDED] Verify that messages received by the postMessage interface are discarded if the origin of the message is not trusted, or if the syntax of the message is invalid. | | ✓ | ✓ | 346 |
| **50.4.3** | [ADDED, SPLIT FROM 14.5.3] Verify that the Origin header field is validated against a defined list of allowed origins to match the desired Cross-Origin Resource Sharing (CORS) policy. | ✓ | ✓ | ✓ | 346 |

## V50.5 Cross-Site Script Inclusion

JSONP is an anti-pattern that can lead to data theft. Poor authorization in scripts that include sensitive data can lead to Cross-Site Script Inclusion (XSSI) attacks.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.5.1** | [ADDED] Verify that JSONP functionality is not enabled anywhere across the application to avoid Cross-Site Script Inclusion (XSSI) attacks. | ✓ | ✓ | ✓ | |
| **50.5.2** | [ADDED] Verify that data requiring authorization is not included in script resource responses, like JavaScript files, to prevent Cross-Site Script Inclusion (XSSI) attacks. | ✓ | ✓ | ✓ | |

## V50.6 Unintended Content Interpretation

Rendering content or functionality in an incorrect context can lead to a wide variety of security issues.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.6.1** | [MODIFIED, MOVED FROM 12.5.2, MERGED FROM 1.12.2, 14.4.2] Verify that security controls are in place to prevent browsers from rendering content or functionality in HTTP responses in an incorrect context (e.g., when an API, a user-uploaded file or other resource is requested directly). Possible controls could include: not serving the content unless HTTP request header fields, such as Sec-Fetch-\*, indicate it is the correct context, Content-Security-Policy: sandbox, Content-Disposition: attachment, etc. | ✓ | ✓ | ✓ | |
| **50.6.2** | [ADDED, SPLIT FROM 5.3.3] Verify that untrusted input must not be applied via innerHTML, document.write, or other properties or functions that render HTML. Instead, use createTextNode, textContent, and similar safe functions that do not render HTML and only render content as text. | ✓ | ✓ | ✓ | |

## V50.7 External Resource Integrity

Hosting content on third-party sites can lead to malicious content modification and supply chain attacks.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.7.1** | [MODIFIED, MOVED FROM 14.2.3] Verify that if client-side assets, such as JavaScript libraries, CSS or web fonts, are hosted externally on a Content Delivery Network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset. | ✓ | ✓ | ✓ | 829 |

## V50.8 Other Browser Security Considerations

<!--
it may need other separate section for "end-user protection via UI"
-->

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.8.1** | [ADDED, SPLIT FROM 5.1.5] Verify that the application shows a notification when the user is being redirected to a URL outside of the application's control, with an option to cancel the navigation. | | | ✓ | |
| **50.8.2** | [MODIFIED, MOVED FROM 1.14.6] Verify that the application only uses client-side technologies which are still supported and considered secure. Examples of technologies which do not meet this requirement include NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | | ✓ | ✓ | 477 |
| **50.8.3** | [ADDED] Verify that the application behaves as documented (such as warning the user or blocking access) if the browser used to access the application does not support the expected security features. | | | ✓ | |

## References

For more information, see also:

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [Sandboxing third-party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
