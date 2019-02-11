# V1: Architecture, Design and Threat Modeling Requirements

## Control Objective

Security architecture has almost become a lost art in many organizations. The days of the enterprise architect have passed in the age of DevSecOps. The application security field must catch up and adopt agile security principles, whilst re-introducing leading security architecture principles to software practicioners. Architecture is not an implementation, but a way of thinking about a problem that has potentially many different answers, and no one single "correct" answer. All too often, security is seen as inflexible and demanding that developers fix code in a particular way, when the developers may know a great deal better way to solve the problem. There is no single, simple solution for architecture, and to pretend otherwise is a disservice to the software engineering field.

A specific implementation of a web application be constantly revised throughout its lifetime, but the overall architecture to never really change. Security architecture is identical - we need authentication today, we will need authentication tomorrow, and we will need it five years from now. If we make sound decisions today, we can save a lot of effort, time, and money if we select and re-use architecturally compliant solutions. For example, a decade ago, multifactor authentication was rarely implemented. 

If developers had invested in a single, secure identity provider model, such as SAML federated identity, the identity provider could be updated to incorporate new requirements such as NIST 800-63 compliance, whilst not changing the interfaces of the original application. If many applications shared the same security architecture and thus that same component, they all benefit from this upgrade at once. This is not to say SAML will remain the solution - it could be easily swapped out with JWT or similar as needs arise. Changes like this are either extremely difficult, so costly as to neceessitate a complete re-write, or outright impossible without security architecture.  

In this chapter, the ASVS covers off the primary aspects of any sound security architecture: security, availability, confidentiality, processing integrity, and privacy. Each of these security principles must be built in and be innate to all applications, which is why it is critical to "shift left", starting with developer enablement with secure coding checklists, mentoring and training, coding and testing, building, deployment, configuration, and operations, and finishing with follow up independant testing to provide assurance that all of the security controls are present and functional. The last step used to be everything we did as an industry, but that is no longer sufficient when developers push code into production tens or hundreds of times a day. Application security professionals must keep up with agile techniques, which means adopting developer tools, learning to code, and working with developers rather than criticizing the project months after everyone else has moved on.

## V1.1 Secure Software Development Lifecycle Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.1.1** | Verify that a secure software development lifecycle is in place, to ensure that security is addressed within all parts of the software development lifecycle. | ✓ | ✓ | ✓ | tbd | tbd |
| **1.1.2** | Verify that threat modeling is performed for every design change or planning sprint to help identify potential threats and countermeasures, facilitate appropriate risk responses and guide testing of weaknesses and countermeasures. | | ✓ | ✓ | tbd | tbd |
| **1.1.4** | Verify that all user stories and features have functional constraints, such as "As a user, I should be able to view and edit my profile. I should not be able to view or edit anyone else's profile" | ✓ | ✓ | ✓ | tbd | tbd |
| **1.1.5** | Verify that all app trust boundaries, components, and significant data flows are identified and are known to be needed. | ✓ | ✓ | ✓ | tbd | tbd |
| **1.1.6** | Verify that a high-level architecture for the application and all connected remote services has been defined and security has been addressed in that architecture. | | ✓ | ✓ | tbd | tbd |
| **1.1.7** | Verify that all security controls have a centralized, simple (economy of design), vetted, secure, and re-usable implementation, to avoid duplicate, missing, ineffective, or insecure controls. | | ✓ | ✓ | 637 | tbd |
| **1.1.8** | Verify that a secure coding checklist or guideline is available to all developers and testers. | ✓ | ✓ | ✓ | 637 | tbd |

## V1.2 Authentication Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.2.1** | Verify that all application components, services, and servers use unique, low-privilege service accounts, that are not shared between applications nor used by administrators. | ✓ | ✓ | ✓ | 250 | tbd |
| **1.2.2** | Verify that communications between application components, including APIs, middleware and data layers, are authenticated with the least necessary privileges. | ✓ | ✓ | ✓ | 306 | tbd |
| **1.2.3** | Verify that the application uses a single vetted authentication mechanism that is known to be secure, can be extended to include strong authentication, and has sufficient logging and monitoring to detect acccount abuse or breaches. | ✓ | ✓ | ✓ | 306 | tbd |

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
| **1.5.1** | Verify that all data, including data flows, is clearly defined based on type, how it is processed and what laws/regulations/compliance requirements relate to the data and how it is handled and processed. | | ✓ | ✓ | tbd | tbd |

## V1.7 Cryptographic Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.7.1** | Verify that there is an explicit policy for how cryptographic keys (if any) are managed, and that a cryptographic key lifecycle is enforced following a key management standard such as NIST SP 800-57. | | ✓ | ✓ | tbd | tbd |

## V1.8 Errors, Logging and Auditing Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## V1.9 Data Protection and Privacy Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## V1.10 Communciations Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.10.1** | Verify that communications between components are encrypted, particularly when the components (such as between the application server and the database server) are in different containers, cloud providers, or on completely different systems.|  | ✓ | ✓ | 319 | tbd |
| **1.10.2** | Verify that communications between components verifies the authenticity of both sides to prevent a Person in the Middle attack. For example, TLS certificate validation. |  | ✓ | ✓ | tbd | tbd |

## V1.15 Business Logic Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.15.1** | All components are defined in terms of the business functions, and/or security functions, they provide. | | | ✓ | tbd | tbd |
| **1.15.2** | Verify that all high value business logic flows, including authentication, session management and access control, are thread safe and designed to be resistant to time of check, time of use race conditions. | | | ✓ | 367 | tbd |
| **1.15.2** | Verify that all high value business logic flows, including authentication, session management and access control, do not share unsynchronized shared state. | | ✓ | ✓ | 362 | tbd |

## V1.16 Secure Files Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## V1.17 API Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |

## V1.19 Configuration Architectural Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **1.19.1** | Verify that components of differing trust levels are segregated from each other via a defined security control, such as network or micro segmentation, firewall rules, API gateways, reverse proxies, or cloud based security groups. | | ✓ | ✓ | tbd | tbd |
| **1.19.2** | Verify that if binaries are delivered to untrusted devices, ensure that an secure automatic updating mechanism is present in the architecture which ensures that only signed binaries are downloaded from trusted sites over a secure connection. | | ✓ | ✓ | tbd | tbd |
| **1.19.3** | Verify that the build pipeline has a mandatory build step that warns if it finds out of date components, and breaks the build if vulnerable components are discovered. | | ✓ | ✓ | tbd | tbd |
| **1.19.4** | Verify that the build pipeline contains a build step to automatically build and verify the secure deployment of the application, particularly if the application infrastructure is software defined, such as cloud environment build scripts. | | ✓ | ✓ | tbd | tbd |
| **1.19.5** | Verify that application deployments are adequately sandboxed, containerized and/or isolated at the network level to delay and deter attackers from attacking other applications, especially when they are performing sensitive or dangerous actions such as deserialization. | ✓ | ✓ | ✓ | 265 | tbd |
| **1.19.6** | Verify that all mission critical components have at least one level of redundancy. |  |  | ✓ | tbd | tbd |
| **1.19.7** | Verify that unsupported, insecure or deprecated client-side technologies are not used, such as NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | ✓ | ✓ | ✓ | tbd | tbd |

## References

For more information, see also:

* [OWASP Threat Modeling Cheat Sheet](https://www.owasp.org/index.php/Threat_Modeling_Cheat_Sheet)
* [OWASP Attack Surface Analysis Cheat Sheet](https://www.owasp.org/index.php/Attack_Surface_Analysis_Cheat_Sheet)
* [OWASP Threat modeling](https://www.owasp.org/index.php/Application_Threat_Modeling)
* [OWASP Secure SDLC Cheat Sheet](https://www.owasp.org/index.php/Secure_SDLC_Cheat_Sheet)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-4/final)
