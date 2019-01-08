# V19: Configuration Verification Requirements

## Control Objective

Ensure that a verified application has:

* Up to date libraries and platform(s).
* A secure-by-default configuration.
* Sufficient hardening so that user-initiated changes to the default configuration do not unnecessarily expose or create security weaknesses or flaws in underlying systems.

## 19.1 Architecture

| # | Description | L1 | L2 | L3 | CWE | CVSSv3 |
| --- | --- | --- | --- | -- | -- | -- |
| **19.1.1** | Verify that communications between components, such as between the application server and traditional, cloud or NoSQL database servers, are authenticated using an account with the least necessary privileges. | ✓ | ✓ | ✓ | 306 | [8.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N) |
| **19.1.2** | Verify application deployments are adequately sandboxed, containerized or isolated to delay and deter attackers from attacking other applications. | ✓ | ✓ | ✓ | 265 | [7.7](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:A/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:N) |
| **19.1.3** | Verify that all application components, services, and servers each use their own low-privilege service account, that is not shared between applications nor used by administrators.  | ✓ | ✓ | ✓ | 250 | [7.4](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H) |
| **19.1.4** | Verify that communications between components, such as between the application server and the database server, are encrypted, particularly when the components are in different containers or on different systems. |  | ✓ | ✓ | 319 | [4.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:N/A:N) |
| **19.1.5** | Verify that all mission critical components have at least one level of redundancy. |  |  | ✓ |  |  |

## 19.2 Build

Build pipelines are the basis for repeatable security - every time something insecure is discovered, it can be resolved in the source code, build or deployment scripts, and tested automatically. We are strongly encouraging the use of build pipelines with automatic security and dependency checks that warn or break the build to prevent known security issues into production. Manual steps performed irregularly directly leads to avoidable security mistakes.

Compliance with this section requires an automated build system, and access to build and deployment scripts. 

| # | Description | L1 | L2 | L3 | CWE | CVSSv3 |
| --- | --- | --- | --- | -- | -- | -- |
| **19.2.1** | Verify that the application build and deployment processes are performed in a secure and repeatable way, such as CI / CD automation, automated configuration management, and automated deployment scripts.  | ✓ | ✓ | ✓ | -- | 10.0 |
| **19.2.2** | Verify that build processes for system-level languages have all security flags enabled, such as ASLR, DEP, and security checks.  | ✓ | ✓ | ✓ | 970 | [9.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) |

## 19.3 Dependency

Dependency management is critical to the safe operation of any application of any type. Failure to keep up to date with outdated or insecure dependencies is the root of cause of the largest and most expensive attacks to date.

| # | Description | L1 | L2 | L3 | CWE | CVSSv3 |
| --- | --- | --- | --- | -- | -- | -- |
| **19.3.1** | Verify that all components are up to date with proper security configuration(s) and version(s), preferably using a dependency checker during build or compile time.  | ✓ | ✓ | ✓ | 1026 | [10.0](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) |
| **19.3.2** | Verify that all unneeded features, documentation, samples, configurations are removed, such as sample applications, platform documentation, and default or example users.  | ✓ | ✓ | ✓ | 1002 | [10.0](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) |
| **19.3.3** | Verify that if application assets, such as JavaScript libraries, CSS stylesheets or web fonts, are hosted externally on a content delivery network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset. | ✓ | ✓ | ✓ | 714 | [8.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N) |
| **19.3.4** | Verify that third party components come from pre-defined, trusted and continually maintained repositories. | ✓ | ✓ | ✓ | 829 | [8.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N) |
| **19.3.5** | Verify that an inventory catalog is maintained of all third party libraries in use. | ✓ | ✓ | ✓ |  |  |

## 19.4 HTTP Configuration

The application server contains HTTP response headers that help provide a layer of security to help users mitigate certain types of attacks and vulnerabilities.

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **19.4.1** | Verify that the application server only accepts the HTTP methods in use by the application or API, including pre-flight OPTIONS. | ✓ | ✓ | ✓ | 1.0 |
| **19.4.2** | Verify that every HTTP response contains a content type header specifying a safe character set (e.g., UTF-8, ISO 8859-1). | ✓ | ✓ | ✓ | 1.0 |
| **19.4.3** | Verify that HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, are authenticated by the application. |  | ✓ | ✓ | 2.0 |
| **19.4.4** | Verify that a suitable X-Frame-Options or Content-Security-Policy: frame-ancestors header is in use for sites where content should not be embedded in a 3rd party site. |  | ✓ | ✓ | 3.0.1 |
| **19.4.5** | Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components. | ✓ | ✓ | ✓ | 2.0 |
| **19.4.6** | Verify that all API responses contain X-Content-Type-Options: nosniff and Content-Disposition: attachment; filename="api.json" (or other appropriate filename for the content type). | ✓ | ✓ | ✓ | 3.0 |
| **19.4.7** | Verify that a content security policy (CSPv2) is in place that helps mitigate common DOM, XSS, JSON, and JavaScript injection vulnerabilities. | ✓ | ✓ | ✓ | 3.0.1 |
| **19.4.8** | Verify that the X-XSS-Protection: 1; mode=block header is in place to enable browser reflected XSS filters. | ✓ | ✓ | ✓ | 3.0 |
| **19.4.9** | Verify that the supplied Origin header is not used for authentication or access control decisions, as the Origin header can easily be changed by an attacker. | ✓ | ✓ | ✓ | 4.0 |
| **19.4.10** | Verify that the cross-domain resource sharing (CORS) Access-Control-Allow-Origin header does not reflect the request's origin header or support the "null" origin. | ✓ | ✓ | ✓ | 4.0 |

## 19.5 Other Configuration

| # | Description | L1 | L2 | L3 | CWE | CVSSv3 |
| --- | --- | --- | --- | -- | -- | -- |
| **19.5.1** | Verify that all parsers used by the application such as XML parsers are configured to prevent external entity attacks (XXE). | ✓ | ✓ | ✓ | 1030 | 9.8 |
| **19.5.2** | Verify that authorized administrators have the capability to verify the integrity of all security-relevant configurations to detect tampering.  |  |  | ✓ | -- | -- |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Testing for HTTP Verb Tampering]( https://www.owasp.org/index.php/Testing_for_HTTP_Verb_Tampering_%28OTG-INPVAL-003%29)
* Adding Content-Disposition to API responses helps prevent many attacks based on misunderstanding on the MIME type between client and server, and the "filename" option specifically helps prevent [Reflected File Download attacks.](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://www.owasp.org/index.php?title=Content_Security_Policy_Cheat_Sheet)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Testing Guide --: Configuration and Deployment Management Testing](https://www.owasp.org/index.php/Testing_for_configuration_management)
* [XML External Entity (XXE) Prevention Cheat Sheet](https://www.owasp.org/index.php/XML_External_Entity_(XXE)_Prevention_Cheat_Sheet))
