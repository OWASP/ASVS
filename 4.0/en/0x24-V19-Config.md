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
| **19.3.4** | Verify that third party components come from pre-defined, trusted repositories. | ✓ | ✓ | ✓ | 829 | [8.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N) |

## 19.4 Configuration

| # | Description | L1 | L2 | L3 | CWE | CVSSv3 |
| --- | --- | --- | --- | -- | -- | -- |
| **19.4.1** | Verify that all parsers used by the application such as XML parsers are configured to prevent external entity attacks. | ✓ | ✓ | ✓ | 1030 | 9.8 |
| **19.4.2** | Verify that authorized administrators have the capability to verify the integrity of all security-relevant configurations to detect tampering.  |  |  | ✓ | -- | -- |

## References

For more information, see also:

* [OWASP Testing Guide --: Configuration and Deployment Management Testing](https://www.owasp.org/index.php/Testing_for_configuration_management)
* [XML External Entity (XXE) Prevention Cheat Sheet](https://www.owasp.org/index.php/XML_External_Entity_(XXE)_Prevention_Cheat_Sheet))
