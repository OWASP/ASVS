# V14 Configuration

## Control Objective

Ensure that a verified application has:

* A secure, repeatable, automatable build environment.
* Hardened third-party library, dependency, and configuration management to ensure that out-of-date or insecure components are not included in the application.

Configuration of the application out of the box should be safe to be on the Internet, which means a safe out-of-the-box configuration.

## V1.14 Configuration Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.14.1** | [DELETED, NOT IN SCOPE] | | | | |
| **1.14.2** | [DELETED, NOT IN SCOPE] | | | | |
| **1.14.3** | [DELETED, DUPLICATE OF 14.2.1] | | | | |
| **1.14.4** | [DELETED, NOT IN SCOPE] | | | | |
| **1.14.5** | [SPLIT TO 1.10.4, 10.5.1] | | | | |
| **1.14.6** | [MOVED TO 50.8.2] | | | | |
| **1.14.7** | [MODIFIED, MOVED FROM 1.1.5] Verify that all communication needs for the application are documented. This should include external services which the application relies upon and cases where an end user might be able to provide an external location to which the application will then connect. | | ✓ | ✓ | 1059 |

## V14.1 Build and Deploy

Build pipelines are the basis for repeatable security - every time something insecure is discovered, it can be resolved in the source code, build or deployment scripts, and tested automatically. We strongly encourage the use of build pipelines with automatic security and dependency checks that warn about or break the build to prevent known security issues from being deployed into production. Manual steps performed irregularly can directly lead to avoidable security mistakes.

As the industry moves to a DevSecOps model, it is important to ensure the continued availability and integrity of deployment and configuration to achieve a "known good" state. In the past, if a system was hacked, it would take days to months to prove that no further intrusions had taken place. Today, with the advent of software-defined infrastructure, rapid A/B deployments with zero downtime, and automated containerized builds, it is possible to automatically and continuously build, harden, and deploy a "known good" replacement for any compromised system.

If traditional models are still in place, then manual steps must be taken to harden and back up that configuration to allow the compromised systems to be quickly replaced with high-integrity, uncompromised systems in a timely fashion.

Compliance with this section requires an automated build system, and access to build and deployment scripts.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.1.1** | [DELETED, NOT IN SCOPE] | | | | |
| **14.1.2** | [LEVEL L2 > L3] Verify that compiler flags are configured to enable all available buffer overflow protections and warnings, including stack randomization, data execution prevention, and to break the build if an unsafe pointer, memory, format string, integer, or string operations are found. | | | ✓ | 120 |
| **14.1.3** | [MODIFIED] Verify that configuration hardening is performed on all third-party products, libraries, frameworks and services as per their individual recommendations. | | ✓ | ✓ | 16 |
| **14.1.4** | [DELETED, NOT IN SCOPE] | | | | |
| **14.1.5** | [MODIFIED] Verify that deployed environments are short lived and frequently redeployed to a "known good" but updated state. Alternatively, long lived environments should use some form of "drift prevention" to ensure that deployed configurations are not changed to an insecure state. | | | ✓ | |
| **14.1.6** | [MOVED FROM 14.2.2] Verify that all unneeded features, documentation, sample applications and configurations are removed. | ✓ | ✓ | ✓ | 1002 |
| **14.1.7** | [ADDED] Verify that production environment does not include test code. | | ✓ | ✓ | 489 |
| **14.1.8** | [ADDED] Verify that data, state information, and server instances related to the build and deployment process do not persist after the process has ended. (Ephemerality). | | | ✓ | |
| **14.1.9** | [ADDED] Verify that application code or functionality can only be changed via the standard update or build process and not directly in production through application functionality or some other direct modification mechanism. | | ✓ | ✓ | |
| **14.1.10** | [MODIFIED, MOVED FROM 2.5.4] Verify that default user accounts (e.g. "root", "admin", or "sa") are not present in the application or are disabled. | ✓ | ✓ | ✓ | 798 |

## V14.2 Dependency

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.2.1** | [SPLIT TO 1.10.5, 10.6.1] | | | | |
| **14.2.2** | [MOVED TO 14.1.6] | | | | |
| **14.2.3** | [MOVED TO 50.7.1] | | | | |
| **14.2.4** | [DELETED, MERGED TO 1.10.2] | | | | |
| **14.2.5** | [MOVED TO 1.10.2] | | | | |
| **14.2.6** | [SPLIT TO 1.10.3, 10.5.1] | | | | |

## V14.3 Unintended Information Leakage

Configurations for production should be hardened to protect against common attacks. Measures should include disabling debug consoles, raising the bar against Cross-site Scripting (XSS) and Remote File Inclusion (RFI) attacks, and eliminating trivial information discovery "vulnerabilities" that often litter penetration testing reports. Many of these issues are rarely rated as a significant risk, but they are chained together with other vulnerabilities. If these issues are not present by default, it raises the bar before most attacks can succeed.

For example, hiding the version of server-side components does not fix the need to patch all components, and disabling the folder listing does not eliminate the need to use authorization controls or keep files away from the public folder, but it raises the bar.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.3.1** | [DELETED, DUPLICATE OF 7.4.1] | | | | |
| **14.3.2** | [MODIFIED] Verify that debug modes are disabled in production environments for every component to prevent exposure of debug features and unintended information leakage. | ✓ | ✓ | ✓ | 497 |
| **14.3.3** | [MODIFIED] Verify that the application does not expose detailed version information of server-side components. | ✓ | ✓ | ✓ | 200 |
| **14.3.4** | [ADDED, SPLIT FROM 4.3.2] Verify that directory browsing is disabled unless deliberately desired. | ✓ | ✓ | ✓ | 548 |
| **14.3.5** | [ADDED, SPLIT FROM 4.3.2] Verify that the application does not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS_Store, .git or .svn folders. | ✓ | ✓ | ✓ | |
| **14.3.6** | [GRAMMAR, MOVED FROM 12.5.1] Verify that the web tier is configured to serve only files with specific file extensions to prevent unintentional information and source code leakage. For example, backup files (e.g. .bak), temporary working files (e.g. .swp), compressed files (.zip, .tar.gz, etc.) and other extensions commonly used by editors should be blocked unless required. | ✓ | ✓ | ✓ | 552 |

## V14.4 HTTP Security Headers

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.4.1** | [MOVED TO 13.1.7] | | | | |
| **14.4.2** | [DELETED, MERGED TO 50.6.1] | | | | |
| **14.4.3** | [MOVED TO 50.3.1] | | | | |
| **14.4.4** | [MOVED TO 50.3.2] | | | | |
| **14.4.5** | [MOVED TO 50.3.3] | | | | |
| **14.4.6** | [MOVED TO 50.3.4] | | | | |
| **14.4.7** | [MOVED TO 50.3.5] | | | | |

## V14.5 HTTP Request Header Validation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.5.1** | [MOVED TO 13.6.1] | | | | |
| **14.5.2** | [DELETED, DUPLICATE OF 4.1.1] | | | | |
| **14.5.3** | [SPLIT TO 50.3.6, 50.4.3] | | | | |
| **14.5.4** | [DELETED, INCORRECT] | | | | |

## V14.6 Web or Application Server Configuration

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.6.1** | [GRAMMAR, MOVED FROM 12.6.1] Verify that the web or application server is configured with an allowlist of resources or systems to which the server can send requests or load data or files from. | ✓ | ✓ | ✓ | 918 |
| **14.6.2** | [MODIFIED, MOVED FROM 1.2.1] Verify that communications between back-end application components, including local or operating system services, APIs, middleware and data layers, are performed with accounts assigned the least necessary privileges. | | ✓ | ✓ | 272 |

## V14.7 External Service Configuration

Applications need to interact with multiple external services including APIs, databases or other components. These might be considered internal to the application but not be included in the application's standard access control mechanisms or might be entirely external. In either case, it will be necessary to configure the application to interact securely with these components and, if necessary protect that configuration.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.7.1** | [MODIFIED, MOVED FROM 2.10.1, MERGED FROM 1.2.2] Verify that communications between back-end application components which don't support the application's standard user session mechanism, including APIs, middleware and data layers, are authenticated. Authentication should use individual service accounts, short-term tokens or certificate based authentication and not unchanging credentials such as passwords, API keys or shared accounts with privileged access. | | ✓ | ✓ | 287 |
| **14.7.2** | [GRAMMAR, MOVED FROM 2.10.2] Verify that if a credential has to be used for service authentication, the credential being used by the consumer is not a default credential (e.g. root/root or admin/admin are default in some services during installation). | | ✓ | ✓ | 255 |
| **14.7.3** | [MODIFIED, MOVED FROM 4.3.3] Verify that, if the application allows changing configurations around passwords or connection parameters for integrations with external databases and services, they are protected by extra controls such as re-authentication or multi-user approval. | | ✓ | ✓ | 732 |

## V14.8 Secret Management

Secret Management is a configuration task that is essential to ensure the protection of data being used in the application. Specific requirements on cryptography can be found in chapter V6 but this section focuses on the management and handling aspects of secrets.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.8.1** | [MODIFIED, MOVED FROM 6.4.1, MERGED FROM 1.6.2, 2.10.4] Verify that a secrets management solution such as a key vault is used to securely create, store, control access to, and destroy back-end secrets. These could include passwords, key material, integrations with databases and third-party systems, seeds and internal secrets, and API keys. Secrets must not be included in application source code or included in build artifacts. For a L3 application, this should involve a hardware-backed solution such as an HSM. | | ✓ | ✓ | 798 |
| **14.8.2** | [MODIFIED, MOVED FROM 6.4.2] Verify that key material is not exposed to the application (neither the front-end nor the back-end) but instead uses an isolated security module like a vault for cryptographic operations. | | ✓ | ✓ | 320 |
| **14.8.3** | [ADDED] Verify that key secrets have defined expiration dates and are rotated on a schedule based on the organization’s threat model and business requirements. | | ✓ | ✓ | 320 |
| **14.8.4** | [ADDED] Verify that access to secret assets adheres to the principle of least privilege. | | ✓ | ✓ | 320 |

## References

For more information, see also:

* [OWASP Web Security Testing Guide 4.1: Testing for HTTP Verb Tampering]( https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Tips to Reduce the Attack Surface When Using Third-Party Libraries](https://www.slideshare.net/KatyAnton1/tips-to-reduce-the-attack-surface-when-using-thirdparty-libraries)
