# V11: HTTP Security Configuration Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* The application server contains HTTP response headers that help provide a layer of security to help users mitigate certain types of attacks and vulnerabilities.


## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **11.1** | Verify that the application server only accepts the HTTP methods in use by the application or API, including pre-flight OPTIONS. | ✓ | ✓ | ✓ | 1.0 |
| **11.2** | Verify that every HTTP response contains a content type header specifying a safe character set (e.g., UTF-8, ISO 8859-1). | ✓ | ✓ | ✓ | 1.0 |
| **11.3** | Verify that HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, are authenticated by the application. |  | ✓ | ✓ | 2.0 |
| **11.4** | Verify that a suitable X-Frame-Options or Content-Security-Policy: frame-ancestors header is in use for sites where content should not be embedded in a 3rd party site. |  | ✓ | ✓ | 3.0.1 |
| **11.5** | Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components. | ✓ | ✓ | ✓ | 2.0 |
| **11.6** | Verify that all API responses contain X-Content-Type-Options: nosniff and Content-Disposition: attachment; filename="api.json" (or other appropriate filename for the content type). | ✓ | ✓ | ✓ | 3.0 |
| **11.7** | Verify that a content security policy (CSPv2) is in place that helps mitigate common DOM, XSS, JSON, and JavaScript injection vulnerabilities. | ✓ | ✓ | ✓ | 3.0.1 |
| **11.8** | Verify that the X-XSS-Protection: 1; mode=block header is in place to enable browser reflected XSS filters. | ✓ | ✓ | ✓ | 3.0 |
| **11.9** | Verify that the supplied Origin header is not used for authentication or access control decisions, as the Origin header can easily be changed by an attacker. | ✓ | ✓ | ✓ | 4.0 |

## References

For more information, please see:

* [OWASP Testing Guide 4.0: Testing for HTTP Verb Tampering]( https://www.owasp.org/index.php/Testing_for_HTTP_Verb_Tampering_%28OTG-INPVAL-003%29)
* Adding Content-Disposition to API responses helps prevent many attacks based on misunderstanding on the MIME type between client and server, and the "filename" option specifically helps prevent [Reflected File Download attacks.](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://www.owasp.org/index.php?title=Content_Security_Policy_Cheat_Sheet)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
