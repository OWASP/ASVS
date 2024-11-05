# V1 Security Decision Documentation

## Control Objective

This paragraph contains documentation requirements that are pre-conditions for implementation and testing.

Note that the documentation requirements here are a temporary solution, and it is yet to be decided how to organize them in the release. The requirements, that or not documentation requirements, are subject to be removed or moved.
<!--
Security architecture has almost become a lost art in many organizations. The days of the enterprise architect have passed in the age of DevSecOps. The application security field must catch up and adopt agile security principles while re-introducing leading security architecture principles to software practitioners. Architecture is not an implementation, but a way of thinking about a problem that has potentially many different answers, and no one single "correct" answer. All too often, security is seen as inflexible and demanding that developers fix code in a particular way, when the developers may know a much better way to solve the problem. There is no single, simple solution for architecture, and to pretend otherwise is a disservice to the software engineering field.

A specific implementation of a web application is likely to be revised continuously throughout its lifetime, but the overall architecture will likely rarely change but evolve slowly. Security architecture is identical - we need authentication today, we will require authentication tomorrow, and we will need it five years from now. If we make sound decisions today, we can save a lot of effort, time, and money if we select and re-use architecturally compliant solutions. For example, a decade ago, multi-factor authentication was rarely implemented.

If developers had invested in a single, secure identity provider model, such as SAML federated identity, the identity provider could be updated to incorporate new requirements such as NIST SP 800-63 compliance, while not changing the interfaces of the original application. If many applications share the same security architecture and thus that same component, they all benefit from this upgrade at once. However, SAML may not always remain the most suitable authentication solution - it might need to be swapped out for other solutions as requirements change. Changes like this are either complicated, so costly as to necessitate a complete rewrite, or outright impossible without security architecture.

In this chapter, the ASVS covers the primary aspects of any sound security architecture: availability, confidentiality, processing integrity, non-repudiation, and privacy. Each of these security principles must be built in and be innate to all applications. It is critical to "shift left", starting with developer enablement with secure coding checklists, mentoring and training, coding and testing, building, deployment, configuration, and operations, and finishing with follow-up independent testing to ensure that all of the security controls are present and functional. The last step used to be everything we did as an industry, but that is no longer sufficient when developers push code into production tens or hundreds of times a day. Application security professionals must keep up with agile techniques, which means adopting developer tools, learning to code, and working with developers rather than criticizing the project months after everyone else has moved on.
-->

## V1.1 Secure Software Development Lifecycle

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.1.1** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.2** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.3** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.4** | [DELETED, NOT IN SCOPE] | | | | |
| **1.1.5** | [MOVED TO 1.14.7] | | | | |
| **1.1.6** | [DELETED, INSUFFICIENT IMPACT] | | | | |
| **1.1.7** | [DELETED, NOT IN SCOPE] | | | | |

## V1.2 Authentication Documentation

<!--
When designing authentication systems, the strength of hardware-enabled multi-factor authentication becomes irrelevant if an attacker can easily reset an account by calling a call center and answering commonly known questions. To ensure secure identity verification, all authentication pathways must possess equivalent strength.
-->

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.2.1** | [MOVED TO 14.6.2] | | | | |
| **1.2.2** | [DELETED, MERGED TO 2.10.1] | | | | |
| **1.2.3** | [DELETED, DUPLICATE OF 1.2.4] | | | | |
| **1.2.4** | [MODIFIED, SPLIT TO 2.2.11] Verify that, if the application includes multiple authentication pathways, these are all documented together with the security controls and authentication strength which should be consistently enforced across them. | | ✓ | ✓ | 306 |
| **1.2.5** | [ADDED] Verify that a list of context specific words are documented in order to prevent their use in passwords. | | ✓ | ✓ | 521 |

## V1.3 Session Management Documentation

Session management mechanisms give applications the ability to correlate user and device interactions over time, even when using otherwise stateless communication protocols. Modern applications may utilize multiple session identifiers or tokens with distinct characteristics and purposes. A secure session management system is one that optimally prevents attackers from obtaining, utilizing, or otherwise abusing a victim's session.

There is no single pattern that suits all applications. Therefore, it is infeasible to define universal boundaries and limits that suit all cases. A risk analysis with documented security decisions related to session handling must be conducted as a prerequisite to implementation and testing. This ensures that the session management system is tailored to the specific requirements of the application. Regardless of whether a stateful or "stateless" session mechanism is chosen, the analysis must be complete and documented to demonstrate that the selected solution is capable of satisfying all relevant security requirements.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.3.1** | [ADDED] Verify that the user's session inactivity period and maximum session lifetime before reauthentication are documented, appropriate in combination with other controls, and that documentation includes justification for any deviations from NIST SP 800-63B reauthentication requirements. | ✓ | ✓ | ✓ | |
| **1.3.2** | [ADDED] Verify that the documentation defines how many concurrent (parallel) sessions are allowed for one account as well as the intended behaviours and actions to be taken when the maximum number of active sessions is reached. | ✓ | ✓ | ✓ | |

## V1.4 Access Control Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.4.1** | [DELETED, DUPLICATE OF 4.1.1] | | | | |
| **1.4.2** | [DELETED] | | | | |
| **1.4.3** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **1.4.4** | [DELETED, INSUFFICIENT IMPACT] | | | | |
| **1.4.5** | [DELETED, INSUFFICIENT IMPACT] | | | | |
| **1.4.6** | [ADDED] Verify that the application documentation defines controls which use changes to a user's regular environmental and contextual attributes (such as time of day, location, IP address, or device) to make security decisions, including those pertaining to authentication and authorization. These changes should be detected both when the user tries to start a new session and also in the course of an existing session. | | | ✓ | |
| **1.4.7** | [ADDED] Verify that access control documentation defines the rules for access control decision-making, specifying user and subject attributes, resource attributes, and relevant environmental factors involved in the process. | ✓ | ✓ | ✓ | |

## V1.5 Input and Output Documentation

<!--
In 4.0, we moved away from the term "server-side" as a loaded trust boundary term. The trust boundary is still concerning - making decisions on untrusted browsers or client devices is bypassable. However, in mainstream architectural deployments today, the trust enforcement point has dramatically changed. Therefore, where the term "trusted service layer" is used in the ASVS, we mean any trusted enforcement point, regardless of location, such as a microservice, serverless API, server-side, a trusted API on a client device that has secure boot, partner or external APIs, and so on.

The "untrusted client" term here refers to client-side technologies that render the presentation layer, commonly referred to as 'front-end' technologies. The term 'serialization' in this context refers not only to transmitting data over the wire, such as an array of values or processing a JSON structure but also to the handling of complex objects that may contain logic.
-->

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.5.1** | [MODIFIED, SPLIT TO 1.5.5, LEVEL L2 > L1] Verify that input validation rules define how to check the validity of data items against an expected structure. This could be common data formats such as credit card numbers, e-mail addresses, telephone numbers, or it could be an internal data format. | ✓ | ✓ | ✓ | 20 |
| **1.5.2** | [DELETED, MERGED TO 5.5.3] | | | | |
| **1.5.3** | [MOVED TO 5.6.2] | | | | |
| **1.5.4** | [MOVED TO 5.6.3] | | | | |
| **1.5.5** | [ADDED, SPLIT FROM 1.5.1] Verify that input validation rules are documented and define how to ensure the logical and contextual consistency of combined data items, such as checking that suburb and zipcode match. | ✓ | ✓ | ✓ | 20 |

## V1.6 Cryptographic Inventory and Documentation

Applications need to be designed with strong cryptographic architecture to protect data assets as per their classification. Encrypting everything is wasteful, not encrypting anything is legally negligent. A balance must be struck, usually during architectural or high-level design, design sprints or architectural spikes. Designing cryptography as you go or retrofitting it will inevitably cost much more to implement securely than simply building it in from the start.

Architectural requirements are intrinsic to the entire code base, and thus difficult to unit or integration test. Architectural requirements require consideration in coding standards, throughout the coding phase, and should be reviewed during security architecture, peer or code reviews, or retrospectives.

It is also important to ensure that all cryptographic assets, such as algorithms, keys, and certificates, are regularly discovered, inventoried, and assessed.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.6.1** | Verify that there is an explicit policy for management of cryptographic keys and that a cryptographic key lifecycle follows a key management standard such as NIST SP 800-57. | | ✓ | ✓ | 320 |
| **1.6.2** | Verify that consumers of cryptographic services protect key material and other secrets by using key vaults or API based alternatives. | | ✓ | ✓ | 320 |
| **1.6.3** | [MOVED TO 6.9.2]| | | | |
| **1.6.4** | [GRAMMAR] Verify that the architecture treats client-side secrets (such as symmetric keys, passwords, or API tokens) as insecure and never uses them to protect or access sensitive data. | | ✓ | ✓ | 320 |
| **1.6.5** | [ADDED] Verify that a cryptographic inventory is performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application. | | ✓ | ✓ | 311 |
| **1.6.7** | [ADDED] Verify that cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations. | | ✓ | ✓ | 311 |

## V1.7 Errors, Logging and Auditing Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.7.1** | [MOVED TO 7.1.7] | | | | |
| **1.7.2** | [MOVED TO 7.3.5] | | | | |
| **1.7.3** | [ADDED] Verify that an inventory exists documenting the logging performed at each layer of the application's technology stack, what events are being logged, log formats, where that logging is stored, how it is used, how access to it is controlled and how long logs are kept for. | | ✓ | ✓ | 778 |

## V1.8 Data Protection and Privacy Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.8.1** | [MODIFIED, MERGED FROM 8.3.4, 6.1.1, 6.1.2] Verify that all sensitive data created and processed by the application has been identified and classified into protection levels, and ensure that a policy is in place on how to deal with sensitive data. Note that this includes sensitive data that is being encoded in a recoverable form such as Base64 and JWT. Protection levels need to take into account any data protection and privacy regulations and standards which the application is required to comply with. | | ✓ | ✓ | 213 |
| **1.8.2** | [MODIFIED, SPLIT TO 8.1.9] Verify that all protection levels have a documented set of protection requirements. This should include (but not be limited to) requirements related to general encryption, integrity verification, retention, how the data should be logged, access controls around sensitive data in logs, database-level encryption, privacy and privacy-enhancing technologies to be used, and other confidentiality requirements. | | ✓ | ✓ | |

## V1.9 Communications Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.9.1** | [DELETED, DUPLICATE OF 9.1.1, 9.2.2, 9.3.1] | | | | |
| **1.9.2** | [DELETED, DUPLICATE OF 9.2.3, 9.3.2] | | | | |

## V1.10 Secure Coding Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.10.1** | [DELETED, NOT IN SCOPE] | | | | |
| **1.10.2** | [MODIFIED, MOVED FROM 14.2.5, MERGED FROM 14.2.4] Verify that an inventory catalog, such as software bill of materials (SBOM), is maintained of all third-party libraries in use, including verifying that components come from pre-defined, trusted, and continually maintained repositories. | | ✓ | ✓ | |
| **1.10.3** | [ADDED, SPLIT FROM 14.2.6] Verify that application documentation highlights "risky" third party libraries which should include: libraries which perform operations which are dangerous from a security perspective, libraries which are poorly maintained, unsupported, or end of life, libraries which have historically had several significant vulnerabilities, etc. | | | ✓ | 1061 |
| **1.10.4** | [ADDED, SPLIT FROM 1.14.5] Verify that application documentation highlights parts of the application where "risky" operations are being performed. "Risky" in this context means those with a high likelyhood of being dangerously exploitated such as: deserialization of untrusted data, raw file parsing, direct memory manipulation, etc. | | | ✓ | |

## V1.11 Business Logic Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.11.1** | [DELETED, NOT IN SCOPE] | | | | |
| **1.11.2** | [DELETED, MERGED TO 11.1.6] | | | | |
| **1.11.3** | [DELETED, MERGED TO 11.1.6] | | | | |
| **1.11.4** | [ADDED] Verify that expectations for business logic limits and validations are clearly documented including both per-user and also globally across the application. | | ✓ | ✓ | |

## V1.12 Secure File Upload Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.12.1** | [DELETED, DUPLICATE OF 12.4.1] | | | | |
| **1.12.2** | [DELETED, MERGED TO 50.5.1] | | | | |
| **1.12.3** | [ADDED] Verify that, if the application allows uploading files, the documentation defines the permitted file types, expected file extensions, and maximum size (including unpacked size) for each upload feature. Additionally, ensure that the documentation specifies how files are made safe for end-users to download and process. | ✓ | ✓ | ✓ | |

## V1.13 API and Web Service Documentation

This is a placeholder for future documentation requirements.

## V1.14 Configuration Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.14.1** | [DELETED, NOT IN SCOPE] | | | | |
| **1.14.2** | [DELETED, NOT IN SCOPE] | | | | |
| **1.14.3** | [DELETED, DUPLICATE OF 14.2.1] | | | | |
| **1.14.4** | [DELETED, NOT IN SCOPE] | | | | |
| **1.14.5** | [SPLIT TO 1.10.4, 10.5.1] | | | | |
| **1.14.6** | [MOVED TO 50.7.2] | | | | |
| **1.14.7** | [MODIFIED, MOVED FROM 1.1.5] Verify that all communication needs for the application are documented. This should include external services which the application relies upon and cases where an end user might be able to provide an external location to which the application will then connect. | | ✓ | ✓ | 1059 |

## V1.50 Web Frontend Security Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.50.1** | [ADDED] Verify that application documentation states the expected security features that browsers using the application should support (such as HTTPS, HSTS, Content Security Policy (CSP), and other relevant HTTP security mechanisms). It should also define how the application must behave when some of these features are not available (such as warning the user or blocking access). | | | ✓ | |

## References

For more information, see also:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/securityengineering/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
* [More information on security.txt including a link to the RFC](https://securitytxt.org/)
