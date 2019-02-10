# V1: Architecture, Design and Threat Modeling Requirements

## Control Objective

To build secure software, we need to consider security throughout all development phases. However, in reality, security is often only an afterthought in the Software Development Life Cycle (SDLC).

The ASVS remediates this problem by not only focusing on technical controls but also by requiring the explicit adoption of security processes. These processes ensure that security is taken into account as soon as the first architecture diagram is drawn. Additionally, the ASVS requires specifying both functional and security properties for application components.

It should be noted that distributed applications, such as mobile clients or Single Page Applications (SPAs) that interact with APIs, should not be tested in isolation, but rather tested in their intended distributed setups.

Category “V1” lists requirements related to the architecture and design of the application. Unlike other requirements in the ASVS, these requirements do not map to technical test cases in the OWASP Testing Guide. The resources at the end of this category include related OWASP projects that do cover these requirements. Example requirements are threat modeling, a secure SDLC, cryptographic key management, etc.

## V1.1 Secure Software Development Lifecycle Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.1.1** | Verify that a secure software development lifecycle is in place, to ensure that security is addressed within all parts of the software development lifecycle. | ✓ | ✓ | ✓ | tbd | tbd |
| **1.1.2** | Verify that threat modeling is performed for every design change or planning sprint to help identify potential threats and countermeasures, facilitate appropriate risk responses and guide testing of weaknesses and countermeasures. | | ✓ | ✓ | tbd | tbd |
| **1.1.3** | Verify that attacker-driven design is used to determine likely threat actors, such that effective controls and countermeasures are in place sufficient to detect, deter and delay that class of threat actor. | | ✓ | ✓ | tbd | tbd |
| **1.1.4** | Verify that all user stories and features have functional constraints, such as "As a user, I should be able to view and edit my profile. I should not be able to view or edit anyone else's profile" | ✓ | ✓ | ✓ | tbd | tbd |
| **1.1.5** | Verify that all app trust boundaries, components, and significant data flows are identified and are known to be needed. | ✓ | ✓ | ✓ | tbd | tbd |
| **1.1.6** | Verify that a high-level architecture for the application and all connected remote services has been defined and security has been addressed in that architecture. | | ✓ | ✓ | tbd | tbd |
| **1.1.7** | Verify that all security controls have a centralized, vetted, secure, and re-usable implementation, to avoid duplicate, missing, ineffective, or insecure controls. | | ✓ | ✓ | tbd | tbd |

## V1.2 Authentication Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **19.2.1** | Verify that all application components, services, and servers use unique, low-privilege service accounts, that are not shared between applications nor used by administrators. | ✓ | ✓ | ✓ | 250 | tbd |
| **19.2.2** | Verify that communications between application components, including APIs, middleware and data layers, are authenticated with the least necessary privileges. | ✓ | ✓ | ✓ | 306 | tbd |
| **19.2.3** | Verify that the application uses a single vetted authentication mechanism that is known to be secure, can be extended to include strong authentication, and has sufficient logging and monitoring to detect acccount abuse or breaches. | ✓ | ✓ | ✓ | 306 | tbd |

## V1.3 Session Management Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## V1.4 Access Control Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.4.1** | Verify that access controls are enforced at trusted enforcement points, such as at access control gateways, servers, or serverless functions. Access control can be evaluated on untrusted clients, but should never be enforced there. | | ✓ | ✓ | tbd | tbd |
| **1.4.2** | Verify that the chosen access control solution is flexible enough to meet the application's needs.  | ✓ | ✓ | ✓ | tbd | tbd |
| **1.4.3** | Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege. | ✓ | ✓ | ✓ |  tbd | tbd |
| **1.4.4** | Verify that there is only one vetted access control mechanism for protecting access to protected data and resources which all requests must go through. This should mean that hardcoded access control checks are not required throughout the application. | ✓ | ✓ | ✓ | tbd | tbd |

## V1.5 Input and Output Pipeline Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.4** | Verify that all data, including data flows, is clearly defined based on type, how it is processed and what laws/regulations/compliance requirements relate to the data and how it is handled and processed. | | ✓ | ✓ | tbd | tbd |

## V1.7 Cryptographic Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.13** | Verify that there is an explicit policy for how cryptographic keys (if any) are managed, and that a cryptographic key lifecycle is enforced following a key management standard such as NIST SP 800-57. | | ✓ | ✓ | tbd | tbd |

## V1.8 Errors, Logging and Auditing Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## V1.9 Data Protection and Privacy Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## V1.10 Communciations Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **19.1.4** | Verify that communications between components, such as between the application server and the database server, are encrypted, particularly when the components are in different containers or on different systems.|  | ✓ | ✓ | 319 | tbd |
| **19.1.5** | Verify that any communication encryption solution between components verifies the authenticity of both sides to prevent a Person in the Middle attack. For example, TLS certificate validation. |  | ✓ | ✓ | tbd | tbd |

## V1.15 Business logic Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.5** | All components are defined in terms of the business functions, and/or security functions, they provide. | | | ✓ | tbd | tbd |

## V1.16 Secure Files Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## V1.17 API Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## V1.19 Configuration Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.9** | Verify that components of differing trust levels are segregated from each other via a defined security control, such as network or micro segmentation, firewall rules, API gateways, reverse proxies, or cloud based security groups. | | ✓ | ✓ | tbd | tbd |
| **1.10** | Verify that if binaries are delivered to untrusted devices, ensure that an secure automatic updating mechanism is present in the architecture which ensures that only signed binaries are downloaded from trusted sites over a secure connection. | | ✓ | ✓ | tbd | tbd |
| **1.12** | Verify that the build pipeline has a mandatory build step that warns if it finds out of date components, and breaks the build if vulnerable components are discovered. | | ✓ | ✓ | tbd | tbd |
| **1.12** | Verify that the build pipeline contains a build step to automatically build and verify the secure deployment of the application, particularly if the application infrastructure is software defined, such as cloud environment build scripts. | | ✓ | ✓ | tbd | tbd |
| **19.1.2** | Verify that application deployments are adequately sandboxed, containerized and/or isolated at the network level to delay and deter attackers from attacking other applications, especially when they are performing sensitive or dangerous actions such as deserialization. | ✓ | ✓ | ✓ | 265 | tbd |
| **19.1.6** | Verify that all mission critical components have at least one level of redundancy. |  |  | ✓ | tbd | tbd |
| **16.9** | Verify that unsupported, insecure or deprecated client-side technologies are not used, such as NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | ✓ | ✓ | ✓ | tbd | tbd |

## References

For more information, see also:

* [OWASP Threat Modeling Cheat Sheet](https://www.owasp.org/index.php/Threat_Modeling_Cheat_Sheet)
* [OWASP Attack Surface Analysis Cheat Sheet](https://www.owasp.org/index.php/Attack_Surface_Analysis_Cheat_Sheet)
* [OWASP Threat modeling](https://www.owasp.org/index.php/Application_Threat_Modeling)
* [OWASP Secure SDLC Cheat Sheet](https://www.owasp.org/index.php/Secure_SDLC_Cheat_Sheet)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-4/final)
