# V14 Configuration

## Control Objective

Ensure that a verified application has:

* A secure, repeatable, automatable build environment.
* Hardened third-party library, dependency, and configuration management to ensure that out-of-date or insecure components are not included in the application.

Configuration of the application out of the box should be safe to be on the Internet, which means a safe out-of-the-box configuration.

## V14.1 Build and Deploy

Build pipelines are the basis for repeatable security - every time something insecure is discovered, it can be resolved in the source code, build or deployment scripts, and tested automatically. We strongly encourage the use of build pipelines with automatic security and dependency checks that warn about or break the build to prevent known security issues from being deployed into production. Manual steps performed irregularly can directly lead to avoidable security mistakes.

As the industry moves to a DevSecOps model, it is important to ensure the continued availability and integrity of deployment and configuration to achieve a "known good" state. In the past, if a system was hacked, it would take days to months to prove that no further intrusions had taken place. Today, with the advent of software-defined infrastructure, rapid A/B deployments with zero downtime, and automated containerized builds, it is possible to automatically and continuously build, harden, and deploy a "known good" replacement for any compromised system.

If traditional models are still in place, then manual steps must be taken to harden and back up that configuration to allow the compromised systems to be quickly replaced with high-integrity, uncompromised systems in a timely fashion.

Compliance with this section requires an automated build system, and access to build and deployment scripts.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.1.1** | [DELETED, NOT IN SCOPE] | | | | |
| **14.1.2** | Verify that compiler flags are configured to enable all available buffer overflow protections and warnings, including stack randomization, data execution prevention, and to break the build if an unsafe pointer, memory, format string, integer, or string operations are found. | | ✓ | ✓ | 120 |
| **14.1.3** | [MODIFIED] Verify that configuration hardening is performed on all 3rd party products, libraries, frameworks and services as per their individual recommendations. | | ✓ | ✓ | 16 |
| **14.1.4** | [DELETED, NOT IN SCOPE] | | | | |
| **14.1.5** | [MODIFIED] Verify that deployed environments are short lived and frequently redeployed to a "known good" but updated state. Alternatively, long lived environments should use some form of "drift prevention" to ensure that deployed configurations are not changed to an insecure state. | | | ✓ | |
| **14.1.6** | [MOVED FROM 14.2.2] Verify that all unneeded features, documentation, sample applications and configurations are removed. | ✓ | ✓ | ✓ | 1002 |
| **14.1.7** | [ADDED] Verify that production environment does not include test code. | | ✓ | ✓ | 489 |
| **14.1.8** | [ADDED] Verify that data, state information, and server instances related to the build and deployment process do not persist after the process has ended. (Ephemerality). | | | ✓ | |
| **14.1.9** | [ADDED] Verify that application code or functionality can only be changed via the standard update or build process and not directly in production through application functionality or some other direct modification mechanism. | | ✓ | ✓ | |

## V14.2 Dependency

Dependency management is critical to the safe operation of any application of any type. Failure to keep up to date with outdated or insecure dependencies is the root cause of the largest and most expensive attacks to date. While being up-to-date with patches is essential, relying solely on updates for publicly disclosed vulnerabilities introduces risk, as vendors may fix security issues without public announcements.

Note: At Level 1, 14.2.1 compliance relates to observations or detections of client-side and other libraries and components, rather than the more accurate build-time static code analysis or dependency analysis. These more accurate techniques could be discoverable by interview as required.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.2.1** | Verify that all components are up to date. | ✓ | ✓ | ✓ | |
| **14.2.2** | [MOVED TO 14.1.6] | | | | |
| **14.2.3** | [MOVED TO 50.6.1] | | | | |
| **14.2.4** | Verify that third party components come from pre-defined, trusted and continually maintained repositories. | | ✓ | ✓ | 829 |
| **14.2.5** | Verify that a Software Bill of Materials (SBOM) is maintained of all third party libraries in use. | | ✓ | ✓ | |
| **14.2.6** | [MODIFIED, SPLIT TO 14.2.8, LEVEL L2 > L3] Verify that risky third party libraries or those with a history of vulnerabilities are encapsulated such that only required behaviour is available to the application, to reduce attack surface. | | | ✓ | 1061 |
| **14.2.7** | [ADDED] Verify that third party components are sourced separately from internally owned and developed applications to prevent dependency confusion attacks. | ✓ | ✓ | ✓ | 427 |
| **14.2.8** | [ADDED, SPLIT FROM 14.2.6] Verify that risky third party libraries or those with a history of vulnerabilities are sandboxed away from the most sensitive system modules/services so that even if a vulnerability in the library was successfully exploited, the sensitive system modules/services would not be compromised. | | | ✓ | 1061 |

Note: Certain languages and package managers, have ecosystems that require the identification of packages using multiple factors (e.g. groupId and artifactId). This would allow the build process to more specifically identify a resource. In other cases, package managers operate by the order of repositories or mirrors included. Consult your package managers to specifically indicate the search order.

## V14.3 Unintended Information Leakage

Configurations for production should be hardened to protect against common attacks. Measures should include disabling debug consoles, raising the bar against Cross-site Scripting (XSS) and Remote File Inclusion (RFI) attacks, and eliminating trivial information discovery "vulnerabilities" that often litter penetration testing reports. Many of these issues are rarely rated as a significant risk, but they are chained together with other vulnerabilities. If these issues are not present by default, it raises the bar before most attacks can succeed.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.3.1** | [DELETED, DUPLICATE OF 7.4.1] | | | | |
| **14.3.2** | [MODIFIED] Verify that debug modes are disabled in production environments for every component to prevent exposure of debug features and unintended information leakage. | ✓ | ✓ | ✓ | 497 |
| **14.3.3** | [MODIFIED] Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of server-side components. | ✓ | ✓ | ✓ | 200 |
| **14.3.4** | [ADDED, SPLIT FROM 4.3.2] Verify that directory browsing is disabled unless deliberately desired. | ✓ | ✓ | ✓ | 548 |
| **14.3.5** | [ADDED, SPLIT FROM 4.3.2] Verify that applications do not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS_Store, .git or .svn folders. | ✓ | ✓ | ✓ | |
| **14.3.6** | [GRAMMAR, MOVED FROM 12.5.1] Verify that the web tier is configured to serve only files with specific file extensions to prevent unintentional information and source code leakage. For example, backup files (e.g. .bak), temporary working files (e.g. .swp), compressed files (.zip, .tar.gz, etc.) and other extensions commonly used by editors should be blocked unless required. | ✓ | ✓ | ✓ | 552 |

## V14.4 HTTP Security Headers

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.4.1** | [MOVED TO 13.1.7] | | | | |
| **14.4.2** | [DELETED, MERGED TO 50.5.1] | | | | |
| **14.4.3** | [MOVED TO 50.2.1] | | | | |
| **14.4.4** | [MOVED TO 50.2.2] | | | | |
| **14.4.5** | [MOVED TO 50.2.3] | | | | |
| **14.4.6** | [MOVED TO 50.2.4] | | | | |
| **14.4.7** | [MOVED TO 50.2.5] | | | | |

## V14.5 HTTP Request Header Validation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.5.1** | [MOVED TO 13.6.1] | | | | |
| **14.5.2** | [DELETED, DUPLICATE OF 4.1.1] | | | | |
| **14.5.3** | [SPLIT TO 50.2.6, 50.3.3] | | | | |
| **14.5.4** | [DELETED, INCORRECT] | | | | |

## V14.6 Web or Application Server Configuration

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.6.1** | [GRAMMAR, MOVED FROM 12.6.1] Verify that the web or application server is configured with an allowlist of resources or systems to which the server can send requests or load data or files from. | ✓ | ✓ | ✓ | 918 |
| **14.6.2** | [MODIFIED, MOVED FROM 1.2.1] Verify that communications between back-end application components, including local or operating system services, APIs, middleware and data layers, are performed with accounts assigned the least necessary privileges. | | ✓ | ✓ | 272 |

## References

For more information, see also:

* [OWASP Web Security Testing Guide 4.1: Testing for HTTP Verb Tampering]( https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Defining multiple repositories in Maven](https://maven.apache.org/guides/mini/guide-multiple-repositories.html)
* [Software Component Verification Standard V2 L1-3 requirements](https://github.com/OWASP/Software-Component-Verification-Standard/blob/master/en/0x11-V2-Software_Bill_of_Materials.md)
* [Tips to Reduce the Attack Surface When Using Third-Party Libraries](https://www.slideshare.net/KatyAnton1/tips-to-reduce-the-attack-surface-when-using-thirdparty-libraries)
