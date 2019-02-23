# V1: Architecture, Design and Threat Modeling Requirements

## Control Objective

Security architecture has almost become a lost art in many organizations. The days of the enterprise architect have passed in the age of DevSecOps. The application security field must catch up and adopt agile security principles while re-introducing leading security architecture principles to software practitioners. Architecture is not an implementation, but a way of thinking about a problem that has potentially many different answers, and no one single "correct" answer. All too often, security is seen as inflexible and demanding that developers fix code in a particular way, when the developers may know a great deal better way to solve the problem. There is no single, simple solution for architecture, and to pretend otherwise is a disservice to the software engineering field.

A specific implementation of a web application is likely to be revised continuously throughout its lifetime, but the overall architecture will likely rarely change but evolve slowly. Security architecture is identical - we need authentication today, we will require authentication tomorrow, and we will need it five years from now. If we make sound decisions today, we can save a lot of effort, time, and money if we select and re-use architecturally compliant solutions. For example, a decade ago, multifactor authentication was rarely implemented.

If developers had invested in a single, secure identity provider model, such as SAML federated identity, the identity provider could be updated to incorporate new requirements such as NIST 800-63 compliance, while not changing the interfaces of the original application. If many applications shared the same security architecture and thus that same component, they all benefit from this upgrade at once. SAML is neither the best or remain the authentication solution - it might be swapped out with JWT or similar as needs arise. Changes like this are either complicated, so costly as to necessitate a complete re-write, or outright impossible without security architecture.

In this chapter, the ASVS covers off the primary aspects of any sound security architecture: security, availability, confidentiality, processing integrity, and privacy. Each of these security principles must be built in and be innate to all applications. It is critical to "shift left", starting with developer enablement with secure coding checklists, mentoring and training, coding and testing, building, deployment, configuration, and operations, and finishing with follow up independent testing to assure that all of the security controls are present and functional. The last step used to be everything we did as an industry, but that is no longer sufficient when developers push code into production tens or hundreds of times a day. Application security professionals must keep up with agile techniques, which means adopting developer tools, learning to code, and working with developers rather than criticizing the project months after everyone else has moved on.

## V1.1 Secure Software Development Lifecycle Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.1.1** | Verify the use of a secure software development lifecycle that addresses security in all stages of development. | | ✓ | ✓ | |
| **1.1.2** | Verify the use of threat modeling for every design change or sprint planning to identify threats, plan for countermeasures, facilitate appropriate risk responses, and guide security testing. | | ✓ | ✓ | 1053 |
| **1.1.3** | Verify that all user stories and features contain functional security constraints, such as "As a user, I should be able to view and edit my profile. I should not be able to view or edit anyone else's profile" |  | ✓ | ✓ | 1110 |
| **1.1.4** | Verify documentation and justification of all the application's trust boundaries, components, and significant data flows. | | ✓ | ✓ | 1059 |
| **1.1.5** | Verify definition and security analysis of the application's high-level architecture and all connected remote services. | | ✓ | ✓ | 1059 |
| **1.1.6** | Verify implementation of centralized, simple (economy of design), vetted, secure, and reusable security controls to avoid duplicate, missing, ineffective, or insecure controls. | | ✓ | ✓ | 637 |
| **1.1.7** | Verify availability of a secure coding checklist, security requirements, guideline, or policy to all developers and testers. | | ✓ | ✓ | 637 |

## V1.2 Authentication Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.2.1** | Verify the use of unique or special low-privilege operating system accounts for all application components, services, and servers. | | ✓ | ✓ | 250 |
| **1.2.2** | Verify that communications between application components, including APIs, middleware and data layers, are authenticated with the least necessary privileges. | | ✓ | ✓ | 306 |
| **1.2.3** | Verify that the application uses a single vetted authentication mechanism that is known to be secure, can be extended to include strong authentication, and has sufficient logging and monitoring to detect account abuse or breaches. | | ✓ | ✓ | 306 |

## V1.3 Session Management Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |

## V1.4 Access Control Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.4.1** | Verify that trusted enforcement points such as at access control gateways, servers, and serverless functions enforce access controls. Never enforce access controls on the client. | | ✓ | ✓ | 602 |
| **1.4.2** | Verify that the chosen access control solution is flexible enough to meet the application's needs.  | | ✓ | ✓ | 284 |
| **1.4.3** | Verify enforcement of the principle of least privilege in functions, data files, URLs, controllers, services, and other resources. This implies protection against spoofing and elevation of privilege. |  | ✓ | ✓ | 272 |
| **1.4.4** | Verify the application uses a single and well-vetted access control mechanism for accessing protected data and resources. All requests must pass through this single mechanism to avoid copy and paste or insecure alternative paths. |  | ✓ | ✓ | 284 |

## V1.5 Input and Output Pipeline Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.5.1** | Verify that input and output requirements clearly define how to handle and process data based on type, content, and applicable laws, regulations, and other policy compliance.  | | ✓ | ✓ | 1029 |
| **1.5.2** | Verify that architecturally, serialized objects are not sent to untrusted clients, either entirely, or with adequate blob encryption or integrity controls to prevent deserialization attacks, replay, and object injection. | | ✓ | ✓ | 502 |

## V1.6 Cryptographic Architectural Requirements

Applications need to be designed with strong cryptographic architecture to protect data assets as per their classification. Encrypting everything is wasteful, not encrypting anything is legally negligent. A balance must be struck, usually during architectural or high level design, design sprints or architectural spikes. Designing cryptography as you go or retrofitting it will inevitably cost a great deal more to implement securely than simply building it in from the start.

Architectural requirements are intrinsic to the entire code base, and thus difficult to unit or integrate test. Architectural requirements require consideration in coding standards, throughout the coding phase, and should be reviewed during security architecture, peer or code reviews, or retrospectives.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.6.1** | Verify that there is an explicit policy for management of cryptographic keys and that a cryptographic key lifecycle follows a key management standard such as NIST SP 800-57. | | ✓ | ✓ | 320 |
| **1.6.2** | Verify that consumers of cryptographic services protect key material and other secrets by using key vaults or API based alternatives. |  | ✓ | ✓ | 320 |
| **1.6.3** | Verify that all keys and passwords are replaceable and are part of a well-defined process to re-encrypt sensitive data. |  | ✓ | ✓ | 320 |
| **1.6.4** | Verify that symmetric keys, passwords, or API secrets generated by or shared with clients are used only in protecting low risk secrets, such as encrypting local storage, or temporary ephemeral uses such as parameter obfuscation. Sharing secrets with clients is clear-text equivalent and architecturally should be treated as such. |  | ✓ | ✓ | 320 |


## V1.7 Errors, Logging and Auditing Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |

## V1.8 Data Protection and Privacy Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |

## V1.9 Communications Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.9.1** | Verify the application encrypts communications between components, particularly when these components are in different containers, systems, sites, or cloud providers.|  | ✓ | ✓ | 319 |
| **1.9.2** | Verify that application components verify the authenticity of each side in a communication link to prevent person-In-the-middle attacks. For example, application components should validate TLS certificates and chains. |  | ✓ | ✓ | 295 |

## V1.10 Malicious Software Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |

## V1.11 Business Logic Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.11.1** | Verify the definition and documentation of all application components in terms of the business or security functions they provide. | | ✓ | ✓ | 1059 |
| **1.11.2** | Verify that all high-value business logic flows, including authentication, session management and access control, do not share unsynchronized state. | | ✓ | ✓ | 362 |
| **1.11.3** | Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions. | | | ✓ | 367 |

## V1.12 Secure Files Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.12.1** | Verify that user-uploaded files are stored outside of the web root. | | ✓ | ✓ | 552 |
| **1.12.2** | Verify that user-uploaded files - if required to be displayed or downloaded by the application - are served by either octet stream downloads, or from an unrelated domain, such as a cloud file storage bucket. Implement a suitable content security policy to to reduce the risk from XSS vectors or other attacks from the uploaded file. | | ✓ | ✓ | 646 |

## V1.13 API Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |

## V1.14 Configuration Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.14.1** | Verify the segregation of components of differing trust levels through well-defined security controls, firewall rules, API gateways, reverse proxies, cloud-based security groups, or similar mechanisms. | | ✓ | ✓ | 923 |
| **1.14.2** | Verify that if deploying binaries to untrusted devices makes use of binary signatures, trusted connections, and verified endpoints. | | ✓ | ✓ | 494 |
| **1.14.3** | Verify that the build pipeline warns of out-of-date or insecure components and takes appropriate actions. | | ✓ | ✓ | 1104 |
| **1.14.4** | Verify that the build pipeline contains a build step to automatically build and verify the secure deployment of the application, particularly if the application infrastructure is software defined, such as cloud environment build scripts. | | ✓ | ✓ | |
| **1.14.5** | Verify that application deployments adequately sandbox, containerize and/or isolate at the network level to delay and deter attackers from attacking other applications, especially when they are performing sensitive or dangerous actions such as deserialization. | | ✓ | ✓ | 265 |
| **1.14.6** | Verify  the application does not use unsupported, insecure, or deprecated client-side technologies such as NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | | ✓ | ✓ | 477 |

## References

For more information, see also:

* [OWASP Threat Modeling Cheat Sheet](https://www.owasp.org/index.php/Threat_Modeling_Cheat_Sheet)
* [OWASP Attack Surface Analysis Cheat Sheet](https://www.owasp.org/index.php/Attack_Surface_Analysis_Cheat_Sheet)
* [OWASP Threat modeling](https://www.owasp.org/index.php/Application_Threat_Modeling)
* [OWASP Secure SDLC Cheat Sheet](https://www.owasp.org/index.php/Secure_SDLC_Cheat_Sheet)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-4/final)
