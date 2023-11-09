# V1 Architecture, Design and Threat Modeling

## Control Objective

Security architecture has almost become a lost art in many organizations. The days of the enterprise architect have passed in the age of DevSecOps. The application security field must catch up and adopt agile security principles while re-introducing leading security architecture principles to software practitioners. Architecture is not an implementation, but a way of thinking about a problem that has potentially many different answers, and no one single "correct" answer. All too often, security is seen as inflexible and demanding that developers fix code in a particular way, when the developers may know a much better way to solve the problem. There is no single, simple solution for architecture, and to pretend otherwise is a disservice to the software engineering field.

A specific implementation of a web application is likely to be revised continuously throughout its lifetime, but the overall architecture will likely rarely change but evolve slowly. Security architecture is identical - we need authentication today, we will require authentication tomorrow, and we will need it five years from now. If we make sound decisions today, we can save a lot of effort, time, and money if we select and re-use architecturally compliant solutions. For example, a decade ago, multi-factor authentication was rarely implemented.

If developers had invested in a single, secure identity provider model, such as SAML federated identity, the identity provider could be updated to incorporate new requirements such as NIST SP 800-63 compliance, while not changing the interfaces of the original application. If many applications share the same security architecture and thus that same component, they all benefit from this upgrade at once. However, SAML will not always remain as the best or most suitable authentication solution - it might need to be swapped out for other solutions as requirements change. Changes like this are either complicated, so costly as to necessitate a complete re-write, or outright impossible without security architecture.

In this chapter, the ASVS covers the primary aspects of any sound security architecture: availability, confidentiality, processing integrity, non-repudiation, and privacy. Each of these security principles must be built in and be innate to all applications. It is critical to "shift left", starting with developer enablement with secure coding checklists, mentoring and training, coding and testing, building, deployment, configuration, and operations, and finishing with follow up independent testing to assure that all of the security controls are present and functional. The last step used to be everything we did as an industry, but that is no longer sufficient when developers push code into production tens or hundreds of times a day. Application security professionals must keep up with agile techniques, which means adopting developer tools, learning to code, and working with developers rather than criticizing the project months after everyone else has moved on.

## V1.1 Secure Software Development Lifecycle

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.1.1** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.2** | Verify the use of threat modeling for every design change or sprint planning to identify threats, plan for countermeasures, facilitate appropriate risk responses, and guide security testing. | | ✓ | ✓ | 1053 |
| **1.1.3** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.4** | Verify documentation and justification of all the application's trust boundaries, components, and significant data flows. | | ✓ | ✓ | 1059 |
| **1.1.5** | Verify definition and security analysis of the application's high-level architecture and all connected remote services. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1059 |
| **1.1.6** | Verify implementation of centralized, simple (economy of design), vetted, secure, and reusable security controls to avoid duplicate, missing, ineffective, or insecure controls. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 637 |
| **1.1.7** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.8** | [ADDED] Verify availability of a publicly available security.txt file at the root or .well-known directory of the application that clearly defines a link or e-mail address for people to contact owners about security issues. | | ✓ | ✓ | 1059 |

## V1.2 Authentication Architecture

When designing authentication, it doesn't matter if you have strong hardware enabled multi-factor authentication if an attacker can reset an account by calling a call center and answering commonly known questions. When proving identity, all authentication pathways must have the same strength.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.2.1** | [MOVED TO 1.14.7] | | | | |
| **1.2.2** | [MODIFIED] Verify that communications between back-end application components, including APIs, middleware and data layers, are authenticated and use individual user accounts. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 306 |
| **1.2.3** | [MODIFIED] Verify that the application uses a single vetted user authentication mechanism that is known to be secure, can be extended to include strong authentication, and has sufficient logging and monitoring to detect account abuse or breaches. | | ✓ | ✓ | 306 |
| **1.2.4** | [MODIFIED, SPLIT TO 2.2.11] Verify that, if the application includes multiple authentication pathways, these are all documented together with the security controls and authentication strength which should be consistently enforced across them. | | ✓ | ✓ | 306 |
| **1.2.5** | [ADDED] Verify that a list of context specific words are documented in order to prevent their use in passwords. | | ✓ | ✓ | 521 |

## V1.3 Session Management Architecture

This is a placeholder for future architectural requirements.

## V1.4 Access Control Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.4.1** | [DELETED, DUPLICATE OF 4.1.1] | | | | |
| **1.4.2** | [DELETED] | | | | |
| **1.4.3** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **1.4.4** | Verify the application uses a single and well-vetted access control mechanism for accessing protected data and resources. All requests must pass through this single mechanism to avoid copy and paste or insecure alternative paths. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 284 |
| **1.4.5** | [GRAMMAR] Verify that attribute or feature-based access control is used whereby the code checks the user's authorization for a feature or data item rather than just their role. Permissions should still be allocated using roles. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 275 |
| **1.4.6** | [ADDED] Verify that communications between back-end application components, including APIs, middleware and data layers, are performed with the least necessary privileges. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 272 |

## V1.5 Input and Output Architecture

In 4.0, we moved away from the term "server-side" as a loaded trust boundary term. The trust boundary is still concerning - making decisions on untrusted browsers or client devices is bypassable. However, in mainstream architectural deployments today, the trust enforcement point has dramatically changed. Therefore, where the term "trusted service layer" is used in the ASVS, we mean any trusted enforcement point, regardless of location, such as a microservice, serverless API, server-side, a trusted API on a client device that has secure boot, partner or external APIs, and so on.

The "untrusted client" term here refers to client-side technologies that render the presentation layer, commonly referred to as 'front-end' technologies. The term "serialization" here not only refers to sending data over the wire like an array of values or taking and reading a JSON structure, but also passing complex objects which can contain logic.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.5.1** | Verify that input and output requirements clearly define how to handle and process data based on type, content, and applicable laws, regulations, and other policy compliance. | | ✓ | ✓ | 1029 |
| **1.5.2** | [DELETED, MERGED TO 5.5.3] | | | | |
| **1.5.3** | [MOVED TO 5.1.6] | | | | |
| **1.5.4** | [MOVED TO 5.3.11] | | | | |

## V1.6 Cryptographic Architecture

Applications need to be designed with strong cryptographic architecture to protect data assets as per their classification. Encrypting everything is wasteful, not encrypting anything is legally negligent. A balance must be struck, usually during architectural or high level design, design sprints or architectural spikes. Designing cryptography as you go or retrofitting it will inevitably cost much more to implement securely than simply building it in from the start.

Architectural requirements are intrinsic to the entire code base, and thus difficult to unit or integration test. Architectural requirements require consideration in coding standards, throughout the coding phase, and should be reviewed during security architecture, peer or code reviews, or retrospectives.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.6.1** | Verify that there is an explicit policy for management of cryptographic keys and that a cryptographic key lifecycle follows a key management standard such as NIST SP 800-57. | | ✓ | ✓ | 320 |
| **1.6.2** | Verify that consumers of cryptographic services protect key material and other secrets by using key vaults or API based alternatives. | | ✓ | ✓ | 320 |
| **1.6.3** | Verify that all keys and passwords are replaceable and are part of a well-defined process to re-encrypt sensitive data. | | ✓ | ✓ | 320 |
| **1.6.4** | [GRAMMAR] Verify that the architecture treats client-side secrets (such as symmetric keys, passwords, or API tokens) as insecure and never uses them to protect or access sensitive data. | | ✓ | ✓ | 320 |

## V1.7 Errors, Logging and Auditing Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.7.1** | Verify that a common logging format and approach is used across the system. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1009 |
| **1.7.2** | [MOVED TO 7.3.5] | | | | |
| **1.7.3** | [ADDED] Verify that an inventory exists documenting the logging performed at each layer of the application's technology stack, what events are being logged, log formats, where that logging is stored, how it is used, how access to it is controlled and how long logs are kept for. | | ✓ | ✓ | 778 |

## V1.8 Data Protection and Privacy Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.8.1** | [MODIFIED, MERGED FROM 8.3.4, LEVEL L2 > L1] Verify that all sensitive data created and processed by the application has been identified and classified into protection levels, and ensure that a policy is in place on how to deal with sensitive data. | ✓ | ✓ | ✓ | 213 |
| **1.8.2** | [MODIFIED] Verify that all protection levels have an associated set of protection requirements and that these are applied in the architecture. This should include (but not be limited to) requirements related to encryption, integrity verification, retention, privacy and privacy-enhancing technologies to be used, and other confidentiality requirements. | | ✓ | ✓ | |

## V1.9 Communications Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.9.1** | [MODIFIED] Verify the application encrypts communications between back-end components, particularly when these components are in different containers, systems, sites, or cloud providers. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 319 |
| **1.9.2** | [MODIFIED] Verify that back-end application components verify the authenticity of each side in a communication link to prevent person-in-the-middle attacks. For example, application components should validate TLS certificates and chains. | | ✓ | ✓ | 295 |

## V1.10 Malicious Software Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.10.1** | [DELETED, NOT IN SCOPE] | | | | |

## V1.11 Business Logic Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.11.1** | Verify the definition and documentation of all application components in terms of the business or security functions they provide. | | ✓ | ✓ | 1059 |
| **1.11.2** | [MODIFIED] Verify that all application flows including authentication, session management and access control, maintain a consistent application and user state to prevent race conditions and business logic flaws. | | ✓ | ✓ | 362 |
| **1.11.3** | Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions. | | | ✓ | 367 |

## V1.12 Secure File Upload Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.12.1** | [DELETED, DUPLICATE OF 12.4.1] | | | | |
| **1.12.2** | [MODIFIED] Verify that user-uploaded files - if required to be displayed or downloaded from the application - are served by either octet stream downloads, or from an unrelated domain, such as a cloud file storage bucket. | | ✓ | ✓ | 646 |

## V1.13 API Architecture

This is a placeholder for future architectural requirements.

## V1.14 Configuration Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.14.1** | [MODIFIED] Verify the segregation of back-end components of differing trust levels through well-defined security controls, firewall rules, API gateways, reverse proxies, cloud-based security groups, or similar mechanisms. | | ✓ | ✓ | 923 |
| **1.14.2** | [DELETED, NOT IN SCOPE] | | | | |
| **1.14.3** | [DELETED, DUPLICATE OF 14.2.1] | | | | |
| **1.14.4** | [DELETED, NOT IN SCOPE] | | | | |
| **1.14.5** | [MODIFIED] Verify that application deployments adequately sandbox or isolate at the network level to delay and deter attackers from attacking other applications, especially when they are performing sensitive or dangerous actions such as deserialization. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |
| **1.14.6** | [MODIFIED] Verify the application only uses client-side technologies which are still supported and considered secure. Examples of technologies which do not meet this requirement include NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | | ✓ | ✓ | 477 |
| **1.14.7** | [MODIFIED, MOVED FROM 1.2.1] Verify the use of unique or special low-privilege operating system accounts for all back-end application components, services, and servers. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 250 |
| **1.14.8** | [ADDED] Verify that the application is able to discern and utilizes the user's true IP address to provide for sensitive functions, including rate limiting and logging. | | ✓ | ✓ | 348 |

## References

For more information, see also:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/securityengineering/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
* [More information on security.txt including a link to the RFC](https://securitytxt.org/)
