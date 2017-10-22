# V19: Configuration Verification Requirements

## Control Objective

Ensure that a verified application has:

* Up to date libraries and platform(s).
* A secure by default configuration.
* Sufficient hardening that user initiated changes to default configuration do not unnecessarily expose or create security weaknesses or flaws to underlying systems.


## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **19.1** | Verify that all components are up to date with proper security configuration(s) and version(s). This should include removal of unneeded configurations and folders such as sample applications, platform documentation, and default or example users.  | ✓ | ✓ | ✓ | 3.1 |
| **19.2** | Verify that communications between components, such as between the application server and the database server, are encrypted, particularly when the components are in different containers or on different systems. |  | ✓ | ✓ | 3.1 |
| **19.3** | Verify that communications between components, such as between the application server and the database server, is authenticated using an account with the least necessary privileges. |  | ✓ | ✓ | 3.1 |
| **19.4** | Verify application deployments are adequately sandboxed, containerized or isolated to delay and deter attackers from attacking other applications. |  | ✓ | ✓ | 3.0 |
| **19.5** | Verify that the application build and deployment processes are performed in a secure and repeatable method, such as CI / CD automation and automated configuration management.  |  | ✓ | ✓ | 3.1 |
| **19.6** | Verify that authorised administrators have the capability to verify the integrity of all security-relevant configurations to detect tampering.  |  |  | ✓ | 3.1 |
| **19.7** | Verify that all application components are signed. |  |  | ✓ | 3.0 |
| **19.8** | Verify that third party components come from trusted repositories. |  |  | ✓ | 3.0 |
| **19.9** | Verify that build processes for system level languages have all security flags enabled, such as ASLR, DEP, and security checks.  |  |  | ✓ | 3.0 |
| **19.10** | Verify that all application assets are hosted by the application, such as JavaScript libraries, CSS stylesheets and web fonts are hosted by the application rather than rely on a CDN or external provider. |  |  | ✓ | 3.0.1 |
| **19.11** | Verify that all application components, services, and servers each use their own low privilege service account, that is not shared between applications nor used by administrators.  |  | ✓ | ✓ | 3.1 |


## References

For more information, see also:

* [OWASP Testing Guide 4.0: Configuration and Deployment Management Testing](https://www.owasp.org/index.php/Testing_for_configuration_management)
