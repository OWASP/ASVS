# V1: Architecture, Design and Threat Modeling Requirements

## Control Objective

To build secure software, we need to consider security throughout all development phases. However, in reality, security is often only an afterthought in the Software Development Life Cycle (SDLC).

The ASVS remediates this problem by not only focusing on technical controls but also by requiring the explicit adoption of security processes. These processes ensure that security is taken into account as soon as the first architecture is drawn. Additionally, the ASVS requires specifying both functional and security properties for application components.

It should be noted that distributed applications, such as mobile clients or Single Page Applications (SPAs) that interact with an APIs, should not be tested in isolation, rather tested in their intended distributed setups.

Category “V1” lists requirements related to the architecture and design of the application. Unlike other requirements in the ASVS, these requirements do not map to technical test cases in the OWASP Testing Guide. The resources at the end of this category include related OWASP projects that do cover these requirements. Example requirements are threat modeling, a secure SDLC, cryptographic key management etc.

## Secure Software Development Lifecycle

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.11** | Security is addressed within all parts of the software development lifecycle. | ✓ | ✓ | ✓ | tbd | tbd |
| **1.7** | A threat modeling exercise for all components should be performed to help identify potential threats and countermeasures, facilitate appropriate risk responses and guide testing of weaknesses and countermeasures. | | ✓ | ✓ | tbd | tbd |
| **1.6** | Verify that rudimentary threat analysis has been made to determine which attackers are in scope, and which are currently not in scope. | | ✓ | ✓ | tbd | tbd |
| **1.7** | Verify that all user stories and features have functional constraints, such as "As a user, I should be able to view and edit only my own profile." | ✓ | ✓ | ✓ | tbd | tbd |

## General architecture requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.1** | Verify that all app trust boundaries, components, and significant data flows are identified and known to be needed. | ✓ | ✓ | ✓ | tbd | tbd |
| **1.3** | Verify that a high-level architecture for the application and all connected remote services has been defined and security has been addressed in that architecture. | | ✓ | ✓ | tbd | tbd |
| **1.8** | Verify that all security controls have a centralized implementation as to avoid duplication of critical code. | | ✓ | ✓ | tbd | tbd |
| **1.8** | Verify that all security controls have a centralized implementation as to avoid duplication of critical code. | | ✓ | ✓ | tbd | tbd |

## Authentication Architecture

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## Access Control Architecture

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.2** | Security controls are never enforced only on the client side, but on the respective remote endpoints. | | ✓ | ✓ | tbd | tbd |


## Input pipeline architecture

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.4** | All data, including data flows, should be clearly defined on type, how it is processed and what laws/regulations/compliance requirements relate to said data and how it is handled and processed. | | ✓ | ✓ | tbd | tbd |

## Output pipeline architecture 

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## Cryptographic architecture

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.13** | There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced following a key management standard such as NIST SP 800-57. | | ✓ | ✓ | tbd | tbd |

## Auditing and assurance architecture 

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## Data Protection and Privacy architecture

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## Business logic architecture

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.5** | All components are defined in terms of the business functions, and/or security functions, they provide. | | | ✓ | tbd | tbd |

## Files architecture

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## API architecture

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## Configuration architecture

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.9** | Verify that components of differing trust levels are segregated from each other via a defined security control, such as network or micro segmentation, firewall rules, API gateways, reverse proxies, or cloud based security groups. | | ✓ | ✓ | tbd | tbd |
| **1.10** | Verify that if binaries are delivered to untrusted devices, ensure that an secure automatic updating mechanism is present in the architecture that ensures only signed binaries are downloaded from trusted sites over a secure connection. | | ✓ | ✓ | tbd | tbd |
| **1.12** | Verify that the build pipeline has a mandatory build step that warns if it finds out of date components, and breaks the build if vulnerable components are discovered. | | ✓ | ✓ | tbd | tbd |
| **1.12** | Verify that the build pipeline contains a build step to automatically build and verify the secure deployment of the application, particularly if the application infrastructure is software defined, such as cloud environment build scripts. | | ✓ | ✓ | tbd | tbd |
| **19.1.1** | Verify that communications between components, such as between the application server and traditional, cloud or NoSQL database servers, are authenticated using an account with the least necessary privileges. | ✓ | ✓ | ✓ | 306 | tbd |
| **19.1.2** | Verify application deployments are adequately sandboxed, containerized and/or isolated at the network level to delay and deter attackers from attacking other applications, especially when they are performing sensitive or dangerous actions such as deserialization. | ✓ | ✓ | ✓ | 265 | tbd |
| **19.1.3** | Verify that all application components, services, and servers each use their own low-privilege service account, that is not shared between applications nor used by administrators.  | ✓ | ✓ | ✓ | 250 | tbd |
| **19.1.4** | Verify that communications between components, such as between the application server and the database server, are encrypted, particularly when the components are in different containers or on different systems.|  | ✓ | ✓ | 319 | tbd |
| **19.1.5** | Verify that any communication encryption solution between components verifies the authenticity of both sides to prevent a Person in the Middle attack. For example, TLS certificate validation. |  | ✓ | ✓ | tbd | tbd |
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
