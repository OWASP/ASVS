# V19: Configuration Verification Requirements

## Control Objective

Ensure that a verified application has:

* A secure, repeatable, automatable build environment.
* Hardended third party library, dependency and configuration management such that out of date or insecure components are not included by the application.
* A secure-by-default configuration, such that administrators and users have to weaken the default security posture.

Configuration of the application out of the box should be safe to be on the Internet, which means a safe out of the box configuration.

## 19.2 Build

Build pipelines are the basis for repeatable security - every time something insecure is discovered, it can be resolved in the source code, build or deployment scripts, and tested automatically. We are strongly encouraging the use of build pipelines with automatic security and dependency checks that warn or break the build to prevent known security issues being deployed into production. Manual steps performed irregularly directly leads to avoidable security mistakes.

Compliance with this section requires an automated build system, and access to build and deployment scripts.

| # | Description | L1 | L2 | L3 | CWE |
| --- | --- | --- | --- | -- | -- |
| **19.2.1** | Verify that the application build and deployment processes are performed in a secure and repeatable way, such as CI / CD automation, automated configuration management, and automated deployment scripts.  | ✓ | ✓ | ✓ | tbd |
| **19.2.2** | Verify that build processes for system-level languages have all security flags enabled, such as ASLR, DEP, and security checks.  | ✓ | ✓ | ✓ | 970 |

## 19.3 Dependency

Dependency management is critical to the safe operation of any application of any type. Failure to keep up to date with outdated or insecure dependencies is the root of cause of the largest and most expensive attacks to date.

| # | Description | L1 | L2 | L3 | CWE |
| --- | --- | --- | --- | -- | -- |
| **19.3.1** | Verify that all components are up to date with secure or hardened configuration(s) and version(s), preferably using a dependency checker during build or compile time.  | ✓ | ✓ | ✓ | 1026 |
| **19.3.2** | Verify that all unneeded features, documentation, samples, configurations are removed, such as sample applications, platform documentation, and default or example users.  | ✓ | ✓ | ✓ | 1002 |
| **19.3.3** | Verify that if application assets, such as JavaScript libraries, CSS stylesheets or web fonts, are hosted externally on a content delivery network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset. | ✓ | ✓ | ✓ | 714 |
| **19.3.4** | Verify that third party components come from pre-defined, trusted and continually maintained repositories. | ✓ | ✓ | ✓ | 829 |
| **19.3.5** | Verify that an inventory catalog is maintained of all third party libraries in use. | ✓ | ✓ | ✓ | tbd |
| **19.3.6** | Verify that the attack surface is reduced by sandboxing or encapsulating third party libraries to expose only the required behaviour into the application. | | ✓ | ✓ | tbd |

## 19.4 Hardened Configuration

The application server contains HTTP response headers that help provide a layer of security to help users mitigate certain types of attacks and vulnerabilities.

| # | Description | L1 | L2 | L3 | CWE |
| --- | --- | --- | --- | -- | -- |
| **19.4.1** | Verify that the application server only accepts the HTTP methods in use by the application or API, including pre-flight OPTIONS. | ✓ | ✓ | ✓ | tbd |
| **19.4.2** | Verify that every HTTP response contains a content type header specifying a safe character set (e.g., UTF-8, ISO 8859-1). | ✓ | ✓ | ✓ | tbd |
| **19.4.3** | Verify that HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, are authenticated by the application. |  | ✓ | ✓ | tbd |
| **19.4.4** | Verify that a suitable X-Frame-Options or Content-Security-Policy: frame-ancestors header is in use for sites where content should not be embedded in a 3rd party site. |  | ✓ | ✓ | tbd |
| **19.4.5** | Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components. | ✓ | ✓ | ✓ | tbd |
| **19.4.6** | Verify that all API responses contain Content-Disposition: attachment; filename="api.json" (or other appropriate filename for the content type). | ✓ | ✓ | ✓ | tbd |
| **19.4.7** | Verify that a content security policy (CSPv2) is in place that helps mitigate common DOM, XSS, JSON, and JavaScript injection vulnerabilities. | ✓ | ✓ | ✓ | tbd |
| **19.4.8** | Verify that the X-XSS-Protection: 1; mode=block header is in place to enable browser reflected XSS filters. | ✓ | ✓ | ✓ | tbd |
| **19.4.9** | Verify that the supplied Origin header is not used for authentication or access control decisions, as the Origin header can easily be changed by an attacker. | ✓ | ✓ | ✓ | tbd |
| **19.4.10** | Verify that the cross-domain resource sharing (CORS) Access-Control-Allow-Origin header uses a strict white-list of trusted domains to match against and does not support the "null" origin. | ✓ | ✓ | ✓ | tbd |
| **19.4.11** | Verify that all responses contain X-Content-Type-Options: nosniff. | ✓ | ✓ | ✓ | tbd |
| **19.4.12** | Verify that application components remove, disable, or sandbox inline scripts found in SVG files. | ✓ | ✓ | ✓ | tbd |
| **19.4.13** | Verify that application components remove, disable, or sandbox scripts by Markdown and other markup languages such as BBCode. | ✓ | ✓ | ✓ | tbd |

## 19.5 Other Configuration

| # | Description | L1 | L2 | L3 | CWE |
| --- | --- | --- | --- | -- | -- |
| **19.5.1** | Verify that authorized administrators have the capability to verify the integrity of all security-relevant configurations to detect tampering.  |  |  | ✓ | tbd |
| **19.5.3** | Verify that regular backups of all configuration files and other custom components are performed and that the application can be restored to a previous working state from that backup. | ✓ | ✓ | ✓ | tbd |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Testing for HTTP Verb Tampering]( https://www.owasp.org/index.php/Testing_for_HTTP_Verb_Tampering_%28OTG-INPVAL-003%29)
* Adding Content-Disposition to API responses helps prevent many attacks based on misunderstanding on the MIME type between client and server, and the "filename" option specifically helps prevent [Reflected File Download attacks.](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://www.owasp.org/index.php?title=Content_Security_Policy_Cheat_Sheet)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Testing Guide 4.0: Configuration and Deployment Management Testing](https://www.owasp.org/index.php/Testing_for_configuration_management)
* [Sandboxing third party components](https://www.owasp.org/index.php/3rd_Party_Javascript_Management_Cheat_Sheet#Sandboxing_Content)