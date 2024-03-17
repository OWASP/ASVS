# V50 Web Frontend Security

The category focuses on requirements that protect against attacks that are executed via a web frontend for an application. These requirements will not be relevant for machine-to-machine solutions.

## V50.1 Site Isolation Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.1.1** | [ADDED, DEPRECATES 3.4.5] Verify that separate applications are hosted on different hostnames to benefit from the restrictions provided by the "same-origin policy" including how documents or scripts loaded by one origin can interact with resources from another origin and hostname restrictions on cookies. | ✓ | ✓ | ✓ | 668 |

## V50.2 Browser Security Mechanism Headers

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.2.1** | [MODIFIED, MOVED FROM 14.4.3] Verify that a Content Security Policy (CSP) response header is in place that helps mitigate impact for XSS attacks like HTML, DOM, CSS, JSON, and JavaScript injection vulnerabilities. | ✓ | ✓ | ✓ | 1021 |
| **50.2.2** | [MOVED FROM 14.4.4] Verify that all responses contain a X-Content-Type-Options: nosniff header. | ✓ | ✓ | ✓ | 116 |
| **50.2.3** | [MODIFIED, MOVED FROM 14.4.5] Verify that a Strict-Transport-Security header is included on all responses and for all subdomains, such as Strict-Transport-Security: max-age=31536000; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **50.2.4** | [MOVED FROM 14.4.6] Verify that a suitable Referrer-Policy header is included to avoid exposing sensitive information in the URL through the Referer header to untrusted parties. | ✓ | ✓ | ✓ | 116 |
| **50.2.5** | [MODIFIED, MOVED FROM 14.4.7] Verify that the content of a web application cannot be embedded in a third-party site by default and that embedding of the exact resources is only allowed where necessary by using suitable Content-Security-Policy: frame-ancestors. Note that the X-Frame-Options solution is obsoleted. | ✓ | ✓ | ✓ | 1021 |
| **50.2.6** | [ADDED, SPLIT FROM 14.5.3] Verify that the Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header uses a strict allow list of trusted origins. When "Access-Control-Allow-Origin: *" needs to be used, verify that the responses do not include any sensitive information. | ✓ | ✓ | ✓ | 183 |

## V50.3 Browser Origin Separation

When accepting a request on the server side, we need to be sure it is initiated by the application itself or by a trusted party.

The keywords here are browser security policies like Same Origin Policy for JavaScript and also SameSite logic for cookies.

The category should contain requirements with ideas:

* Verify that the request was initiated by a trusted party (CSRF, CORS misconfiguration)
* Verify that the response is readable only for trusted parties (CORS misconfiguration)

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.3.1** | [MODIFIED, MOVED FROM 4.2.2, MERGED FROM 13.2.3] Verify that the application defends against Cross-Site Request Forgery (CSRF) attacks to protect authenticated or sensitive public functionality using the development framework's built-in anti-CSRF functionality or CSRF tokens plus additional defense in depth measures. | ✓ | ✓ | ✓ | 352 |
| **50.3.2** | [ADDED] Verify that messages received by the postMessage interface are discarded if the origin of the message is not trusted, or if the syntax of the message is invalid. | | ✓ | ✓ | 346 |
| **50.3.3** | [ADDED, SPLIT FROM 14.5.3] Verify that the Origin header is validated against a defined list of allowed origins to match the desired Cross-Origin Resource Sharing (CORS) policy. | ✓ | ✓ | ✓ | 346 |

## V50.4 Cross-Site Script Inclusion

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.4.1** | [ADDED] Verify that JSONP functionality is not enabled anywhere across the application to avoid Cross-Site Script Inclusion (XSSI) attacks. | ✓ | ✓ | ✓ | |
| **50.4.2** | [ADDED] Verify that data requiring authorization is not included in script resource responses, like JavaScript files, to prevent Cross-Site Script Inclusion (XSSI) attacks. | ✓ | ✓ | ✓ | |

## V50.5 Unintended Content Interpretation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.5.1** | [GRAMMAR, MOVED FROM 12.5.2] Verify that direct requests to uploaded files will never be executed as HTML and JavaScript content. | ✓ | ✓ | ✓ | 434 |
| **50.5.2** | [MODIFIED, MOVED FROM 1.12.2] Verify that user-uploaded files - if required to be displayed or downloaded from the application - are served by either octet stream downloads, or from an unrelated domain, such as a cloud file storage bucket. | | ✓ | ✓ | 646 |
| **50.5.3** | [ADDED, DEPRECATES 14.4.2] Verify that security controls are in place to prevent browsers from rendering content or functionality in HTTP responses in an incorrect context (e.g., when an API or other resource is loaded directly). Possible controls could include: not serving the content unless headers indicate it is the correct context, Content-Security-Policy: sandbox, Content-Disposition: attachment, etc. | ✓ | ✓ | ✓ | |

## V50.6 External Resource Integrity

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.6.1** | [MODIFIED, MOVED FROM 14.2.3] Verify that if client-side assets, such as JavaScript libraries, CSS or web fonts, are hosted externally on a Content Delivery Network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset. | ✓ | ✓ | ✓ | 829 |

## V50.7 Other Browser Security Considerations

<!--
it may need other separate section for "end-user protection via UI"
-->

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.7.1** | [ADDED, SPLIT FROM 5.1.5] Verify that the application shows a notification when the user is being redirected to a URL outside of the application's control, with an option to cancel the navigation. | | | ✓ | |


## References

For more information, see also:

* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [Sandboxing third-party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
