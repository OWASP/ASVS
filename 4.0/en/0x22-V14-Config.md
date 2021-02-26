# V14: Configuration Verification Requirements

## Control Objective

Ensure that a verified application has:

* A secure, repeatable, automatable build environment.
* Hardened third party library, dependency and configuration management such that out of date or insecure components are not included by the application.
* A secure-by-default configuration, such that administrators and users have to weaken the default security posture.

Configuration of the application out of the box should be safe to be on the Internet, which means a safe out of the box configuration.

## V14.1 Build

Build pipelines are the basis for repeatable security - every time something insecure is discovered, it can be resolved in the source code, build or deployment scripts, and tested automatically. We are strongly encouraging the use of build pipelines with automatic security and dependency checks that warn or break the build to prevent known security issues being deployed into production. Manual steps performed irregularly directly leads to avoidable security mistakes.

As the industry moves to a DevSecOps model, it is important to ensure the continued availability and integrity of deployment and configuration to achieve a "known good" state. In the past, if a system was hacked, it would take days to months to prove that no further intrusions had taken place. Today, with the advent of software defined infrastructure, rapid A/B deployments with zero downtime, and automated containerized builds, it is possible to automatically and continuously build, harden, and deploy a "known good" replacement for any compromised system.

If traditional models are still in place, then manual steps must be taken to harden and back up that configuration to allow the compromised systems to be quickly replaced with high integrity, uncompromised systems in a timely fashion.

Compliance with this section requires an automated build system, and access to build and deployment scripts.

| # | Description | L1 | L2 | L3 | CWE |
| --- | --- | --- | --- | -- | -- |
| **14.1.1** | Verify that the application build and deployment processes are performed in a secure and repeatable way, such as CI / CD automation, automated configuration management, and automated deployment scripts. | | ✓ | ✓ | |
| **14.1.2** | Verify that compiler flags are configured to enable all available buffer overflow protections and warnings, including stack randomization, data execution prevention, and to break the build if an unsafe pointer, memory, format string, integer, or string operations are found. |  | ✓ | ✓ | 120 |
| **14.1.3** | Verify that server configuration is hardened as per the recommendations of the application server and frameworks in use. | | ✓ | ✓ | 16 |
| **14.1.4** | Verify that the application, configuration, and all dependencies can be re-deployed using automated deployment scripts, built from a documented and tested runbook in a reasonable time, or restored from backups in a timely fashion. | | ✓ | ✓ | |
| **14.1.5** | Verify that authorized administrators can verify the integrity of all security-relevant configurations to detect tampering. | | | ✓ | |

## V14.2 Dependency

Dependency management is critical to the safe operation of any application of any type. Failure to keep up to date with outdated or insecure dependencies is the root cause of the largest and most expensive attacks to date.

Note: At Level 1, 14.2.1 compliance relates to observations or detections of client-side and other libraries and components, rather than the more accurate build-time static code analysis or dependency analysis. These more accurate techniques could be discoverable by interview as required.

| # | Description | L1 | L2 | L3 | CWE |
| --- | --- | --- | --- | -- | -- |
| **14.2.1** | Verify that all components are up to date, preferably using a dependency checker during build or compile time. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1026 |
| **14.2.2** | Verify that all unneeded features, documentation, samples, configurations are removed, such as sample applications, platform documentation, and default or example users. | ✓ | ✓ | ✓ | 1002 |
| **14.2.3** | Verify that if application assets, such as JavaScript libraries, CSS or web fonts, are hosted externally on a Content Delivery Network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset. | ✓ | ✓ | ✓ | 829 |
| **14.2.4** | Verify that third party components come from pre-defined, trusted and continually maintained repositories. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 829 |
| **14.2.5** | Verify that an inventory catalog is maintained of all third party libraries in use. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **14.2.6** | Verify that the attack surface is reduced by sandboxing or encapsulating third party libraries to expose only the required behaviour into the application. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |
| **14.2.7** | Verify that third party components are sourced separately from internally owned and developed applications | ✓ | ✓ | ✓ | 441 |


Note: Certain languages and package managers, have ecosystems that require the identification of packages using multiple factors (e.g groupId and artifactId). This would allow the build process to more specifically identify a resource. In other cases, package managers operate by the order of repositories or mirrors included. Consult your package managers to specifically indicate search order. 



## V14.3 Unintended Security Disclosure Requirements

Configurations for production should be hardened to protect against common attacks, such as debug consoles, raise the bar for Cross-site Scripting (XSS) and Remote File Inclusion (RFI) attacks, and to eliminate trivial information discovery "vulnerabilities" that are the unwelcome hallmark of many penetration testing reports. Many of these issues are rarely rated as a significant risk, but they are chained together with other vulnerabilities. If these issues are not present by default, it raises the bar before most attacks can succeed.

| # | Description | L1 | L2 | L3 | CWE |
| --- | --- | --- | --- | -- | -- |
| **14.3.1** | Verify that web or application server and framework error messages are configured to deliver user actionable, customized responses to eliminate any unintended security disclosures. | ✓ | ✓ | ✓ | 209 |
| **14.3.2** | Verify that web or application server and application framework debug modes are disabled in production to eliminate debug features, developer consoles, and unintended security disclosures. | ✓ | ✓ | ✓ | 497 |
| **14.3.3** | Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components. | ✓ | ✓ | ✓ | 200 |

## V14.4 HTTP Security Headers Requirements

| # | Description | L1 | L2 | L3 | CWE |
| --- | --- | --- | --- | -- | -- |
| **14.4.1** | Verify that every HTTP response contains a Content-Type header. text/*, */*+xml and application/xml content types should also specify a safe character set (e.g., UTF-8, ISO-8859-1). | ✓ | ✓ | ✓ | 173 |
| **14.4.2** | Verify that all API responses contain a Content-Disposition: attachment; filename="api.json" header (or other appropriate filename for the content type). | ✓ | ✓ | ✓ | 116 |
| **14.4.3** | Verify that a Content Security Policy (CSP) response header is in place that helps mitigate impact for XSS attacks like HTML, DOM, JSON, and JavaScript injection vulnerabilities. | ✓ | ✓ | ✓ | 1021 |
| **14.4.4** | Verify that all responses contain a X-Content-Type-Options: nosniff header. | ✓ | ✓ | ✓ | 116 |
| **14.4.5** | Verify that a Strict-Transport-Security header is included on all responses and for all subdomains, such as Strict-Transport-Security: max-age=15724800; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **14.4.6** | Verify that a suitable "Referrer-Policy" header is included, such as "no-referrer" or "same-origin". | ✓ | ✓ | ✓ | 116 |
| **14.4.7** | Verify that the content of a web application cannot be embedded in a third-party site by default and that embedding of the exact resources is only allowed where necessary by using suitable Content-Security-Policy: frame-ancestors and X-Frame-Options response headers. | ✓ | ✓ | ✓ | 346 |

## V14.5 Validate HTTP Request Header Requirements

| # | Description | L1 | L2 | L3 | CWE |
| --- | --- | --- | --- | -- | -- |
| **14.5.1** | Verify that the application server only accepts the HTTP methods in use by the application/API, including pre-flight OPTIONS, and logs/alerts on any requests that are not valid for the application context. | ✓ | ✓ | ✓ | 749 |
| **14.5.2** | Verify that the supplied Origin header is not used for authentication or access control decisions, as the Origin header can easily be changed by an attacker. | ✓ | ✓ | ✓ | 346 |
| **14.5.3** | Verify that the Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header uses a strict allow list of trusted domains and subdomains to match against and does not support the "null" origin. | ✓ | ✓ | ✓ | 346 |
| **14.5.4** | Verify that HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, are authenticated by the application. | | ✓ | ✓ | 306 |

## References

For more information, see also:

* [OWASP Web Security Testing Guide 4.1: Testing for HTTP Verb Tampering]( https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* Adding Content-Disposition to API responses helps prevent many attacks based on misunderstanding on the MIME type between client and server, and the "filename" option specifically helps prevent [Reflected File Download attacks.](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Sandboxing third party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
* [Defining multiple repositories in maven](https://maven.apache.org/guides/mini/guide-multiple-repositories.html)