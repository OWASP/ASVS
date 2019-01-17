# V1: Architecture, Design and Threat Modeling Requirements

## Control Objective

To build secure software, we need to consider security throughout all development phases. However, in reality, security is often only an afterthought in the Software Development Life Cycle (SDLC).

The ASVS remediates this problem by not only focusing on technical controls but also by requiring the explicit adoption of security processes. These processes ensure that security is taken into account as soon as the first architecture is drawn. Additionally, the ASVS requires specifying both functional and security properties for application components.

It should be noted that distributed applications, such as mobile clients or Single Page Applications (SPAs) that interact with an APIs, should not be tested in isolation, rather tested in their intended distributed setups.

Category “V1” lists requirements related to the architecture and design of the application. Unlike other requirements in the ASVS, these requirements do not map to technical test cases in the OWASP Testing Guide. The resources at the end of this category include related OWASP projects that do cover these requirements. Example requirements are threat modeling, a secure SDLC, cryptographic key management etc.

## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **1.1** | All app components and data flows are identified and known to be needed. | ✓ | ✓ | ✓ | 1.0 |
| **1.2** | Security controls are never enforced only on the client side, but on the respective remote endpoints. |  | ✓ | ✓ | 1.0 |
| **1.3** | A high-level architecture for the application and all connected remote services has been defined and security has been addressed in that architecture. |  | ✓ | ✓ | 1.0 |
| **1.4** | All data, including data flows, should be clearly defined on type, how it is processed and what laws/regulations/compliance requirements relate to said data and how it is handled and processed.  |  | ✓ | ✓ | 1.0 |
| **1.5** | All components are defined in terms of the business functions, and/or security functions, they provide. | | | ✓ | 1.0 |
| **1.6** | A rudimentary threat analysis has been made to determine which attackers are in scope, and which are currently not in scope. |  | ✓ | ✓ | 4.0 |
| **1.7** | A threat modeling exercise for all components should be performed to help identify potential threats and countermeasures, facilitate appropriate risk responses and guide testing of weaknesses and countermeasures. |  | ✓ | ✓ | 1.0 |
| **1.8** | All security controls have a centralized implementation as to avoid duplication of critical code. | | ✓ | ✓ | 3.0 |
| **1.9** | Components are segregated from each other via a defined security control, such as network segmentation, firewall rules, or cloud based security groups. | | ✓ | ✓ | 3.0 |
| **1.10** | A mechanism for enforcing updates of the application exists. | | ✓ | ✓ | 3.0 |
| **1.11** | Security is addressed within all parts of the software development lifecycle. | ✓ | ✓ | ✓ | 3.0 |
| **1.12** | All application components, libraries, modules, frameworks, platforms, and operating systems are free from known vulnerabilities. | |✓ |✓ | 3.0.1 |
| **1.13** | There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced following a key management standard such as NIST SP 800-57. | | ✓ | ✓ | 4.0 |

## References

For more information, see also:

* [OWASP Threat Modeling Cheat Sheet](https://www.owasp.org/index.php/Threat_Modeling_Cheat_Sheet)
* [OWASP Attack Surface Analysis Cheat Sheet](https://www.owasp.org/index.php/Attack_Surface_Analysis_Cheat_Sheet)
* [OWASP Threat modeling](https://www.owasp.org/index.php/Application_Threat_Modeling)
* [OWASP Secure SDLC Cheat Sheet](https://www.owasp.org/index.php/Secure_SDLC_Cheat_Sheet)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-4/final)
