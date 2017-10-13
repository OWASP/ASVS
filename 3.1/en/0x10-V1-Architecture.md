# V1: Architecture, Design and Threat Modeling Requirements

## Control Objective

In a perfect world, security would be considered throughout all phases of development. In reality however, security is often only a consideration at a late stage in the SDLC. Besides the technical controls, the ASVS requires processes to be in place that ensure that the security has been explicitly addressed when planning the architecture of the application or API, and that the functional and security roles of all components are known. Since single page applications and act as clients to remote API or services, it must be ensured that appropriate security standards are also applied to those services - testing the app in isolation is not sufficient.

The category “V1” lists requirements pertaining to architecture and design of the app. As such, this is the only category that does not map to technical test cases in the OWASP Testing Guide. To cover topics such as threat modelling, secure SDLC, key management, users of the ASVS should consult the respective OWASP projects and/or other standards such as the ones linked below.

## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **1.1** | All app components are identified and known to be needed. | ✓ | ✓ | ✓ | 1.0 |
| **1.2** | Security controls are never enforced only on the client side, but on the respective remote endpoints. |  | ✓ | ✓ | 1.0 |
| **1.3** | A high-level architecture for the application and all connected remote services has been defined and security has been addressed in that architecture. |  | ✓ | ✓ | 1.0 |
| **1.4** | Data considered sensitive in the context of the application is clearly identified. |  |  | ✓ | 1.0 |
| **1.5** | All app components are defined in terms of the business functions and/or security functions they provide. | | | ✓ | 1.0 |
| **1.6** | A threat model for the application and the associated remote services has been produced that identifies potential threats and countermeasures. |  |  | ✓ | 1.0 |
| **1.7** | All security controls have a centralized implementation. | |✓ |✓ | 3.0 |
| **1.8** | Components are segregated from each other via a defined security control, such as network segmentation, firewall rules, or cloud based security groups. | |✓ |✓ | 3.0 |
| **1.9** | A mechanism for enforcing updates of the application exists. | |✓ |✓ | 3.0 |
| **1.10** | Security is addressed within all parts of the software development lifecycle. | |✓ |✓ | 3.0 |
| **1.11** | all application components, libraries, modules, frameworks, platform, and operating systems are free from known vulnerabilities | |✓ |✓ | 3.0.1 |
| **1.12** | There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced. Ideally, follow a key management standard such as NIST SP 800-57. | |✓ |✓ | 3.1 |

## References

For more information, see also:

For more information, please see:
* [OWASP Threat Modeling Cheat Sheet](https://www.owasp.org/index.php/Application_Security_Architecture_Cheat_Sheet)
* [OWASP Attack Surface Analysis Cheat Sheet](https://www.owasp.org/index.php/Attack_Surface_Analysis_Cheat_Sheet)
* [OWASP Security Architecture Cheat Sheet](https://www.owasp.org/index.php/Application_Security_Architecture_Cheat_Sheet)
* [OWASP Thread modelling](https://www.owasp.org/index.php/Application_Threat_Modeling)
* [OWASP Secure SDLC Cheat Sheet](https://www.owasp.org/index.php/Secure_SDLC_Cheat_Sheet)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf)
