# V50 Web Frontend Security

The category focuses on requirements which protect against attacks that are executed via a web frontend for an application. These requirements will not be relevant for machine-to-machine solutions.


## V50.1 Site Isolation Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.1.1** | [ADDED] Verify that separate applications are hosted on different hostnames to benefit from the restrictions provided by the "same-origin policy" including how documents or scripts loaded by one origin can interact with resources from another origin and hostname restrictions on cookies. | ✓ | ✓ | ✓ | 668 |


## V50.2 Browser Security Mechanism Headers

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **50.2.1** | [MODIFIED, MOVED FROM 14.4.3] Verify that a Content Security Policy (CSP) response header is in place that helps mitigate impact for XSS attacks like HTML, DOM, CSS, JSON, and JavaScript injection vulnerabilities. | ✓ | ✓ | ✓ | 1021 |
| **50.2.2** | [MOVED FROM 14.4.4] Verify that all responses contain a X-Content-Type-Options: nosniff header. | ✓ | ✓ | ✓ | 116 |
| **50.2.3** | [MODIFIED, MOVED FROM 14.4.5] Verify that a Strict-Transport-Security header is included on all responses and for all subdomains, such as Strict-Transport-Security: max-age=31536000; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **50.2.4** | [MOVED FROM 14.4.6] Verify that a suitable Referrer-Policy header is included to avoid exposing sensitive information in the URL through the Referer header to untrusted parties. | ✓ | ✓ | ✓ | 116 |
| **50.2.5** | [MOVED FROM 14.4.7] Verify that the content of a web application cannot be embedded in a third-party site by default and that embedding of the exact resources is only allowed where necessary by using suitable Content-Security-Policy: frame-ancestors and X-Frame-Options response headers. | ✓ | ✓ | ✓ | 1021 |
| **50.2.6** | [ADDED, SPLIT FROM 14.5.3] Verify that the Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header uses a strict allow list of trusted origins. When "Access-Control-Allow-Origin: *" needs to be used, verify that the responses do not include any sensitive information. | ✓ | ✓ | ✓ | 183 |


## V50.3 Browser Origin Separation

TBD


## V50.4 Cross-Site Script Inclusion

TBD


## V50.5 Unintended Content Interpretation

TBD


## V50.6 External Resource Integrity

TBD

## V50.7 Other Browser Security Considerations

TBD
