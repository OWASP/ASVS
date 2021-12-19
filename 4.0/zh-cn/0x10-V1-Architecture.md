# V1架构、设计和威胁建模

## 控制目标

在许多组织中，安全架构几乎已成为一门失传的艺术。 在DevSecOps时代，企业架构师的日子已经过去。应用安全领域必须迎头赶上，采用敏捷安全原则，同时将领先的安全架构原则重新介绍给软件从业者。 A架构不是一种实施，而是一种思考问题的方式，它可能有许多不同的答案，而没有一个单一的“正确”答案。 很多时候，安全被视为不灵活的，要求开发人员以特定方式修复代码，而开发人员可能知道解决问题的更好方法。 对于架构来说，没有单一的、简单的解决方案，尝试寻找这种方案，是对软件工程领域的一种损害。

一个Web应用程序的具体实现，很可能在其生命周期中不断被修改，但整体架构可能很少改变，而是缓慢发展。 安全架构也是一样的，身份验证——我们今天需要、明天需要、五年后也需要。 如果我们今天做出合理的决定，选择和复用符合架构的解决方案，那么就可以节省大量的精力、时间和金钱。 例如，十年前，多因素认证很少被实施。

如果开发人员已经在单一的“安全标识提供程序模型”上有所投入（例如SAML联邦认证），身份提供者可以更新以纳入新的要求（例如NIST 800-63标准），同时不改变原始应用程序的接口。 如果许多应用程序共享相同的安全架构和组件，那么它们都将同时从这次升级中受益。 然而，SAML 并不总是最好或最合适的身份验证解决方案——随着需求的变化，可能需要替换为其他解决方案。 像这样的更改要么很复杂，成本高到需要完全重写，要么在没有安全架构的情况下完全不可能。

在本章中，ASVS涵盖了任何良好安全架构的主要方面：可用性、保密性、完整性、不可抵赖性和隐私。 这些安全原则中的每一条，都必须适用并内置于所有应用程序中。 “左移”至关重要，从安全编码Checklists、指导和培训、编码和测试、构建、部署、配置和操作开始，到后续的独立测试，确保所有安全控制存在且功能正常。 这最后一步，曾经是我们作为一个行业所做的一切，但当开发人员每天数十次或数百次地推送代码时，就已经不够了。 应用安全专业人员必须跟上敏捷技术的步伐，这意味着要适应开发人员的工具，学习编码，并与开发人员一起工作，而不是在其他人离开的几个月后再批评项目。

## V1.1 安全软件开发生命周期

| # | 说明 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.1.1** | 验证使用安全的软件开发生命周期，在开发的各个阶段解决安全问题。 ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **1.1.2** | 验证在每次设计变更或sprint计划中使用威胁建模，以识别威胁、计划对策、促进适当的风险响应，并指导安全测试。 | | ✓ | ✓ | 1053 |
| **1.1.3** | Verify that all user stories and features contain functional security constraints, such as "As a user, I should be able to view and edit my profile. I should not be able to view or edit anyone else's profile" | | ✓ | ✓ | 1110 |
| **1.1.4** | Verify documentation and justification of all the application's trust boundaries, components, and significant data flows. | | ✓ | ✓ | 1059 |
| **1.1.5** | Verify definition and security analysis of the application's high-level architecture and all connected remote services. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1059 |
| **1.1.6** | Verify implementation of centralized, simple (economy of design), vetted, secure, and reusable security controls to avoid duplicate, missing, ineffective, or insecure controls. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 637 |
| **1.1.7** | Verify availability of a secure coding checklist, security requirements, guideline, or policy to all developers and testers. | | ✓ | ✓ | 637 |

## V1.2 Authentication Architecture

When designing authentication, it doesn't matter if you have strong hardware enabled multi-factor authentication if an attacker can reset an account by calling a call center and answering commonly known questions. When proving identity, all authentication pathways must have the same strength.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.2.1** | Verify the use of unique or special low-privilege operating system accounts for all application components, services, and servers. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 250 |
| **1.2.2** | Verify that communications between application components, including APIs, middleware and data layers, are authenticated. Components should have the least necessary privileges needed. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 306 |
| **1.2.3** | Verify that the application uses a single vetted authentication mechanism that is known to be secure, can be extended to include strong authentication, and has sufficient logging and monitoring to detect account abuse or breaches. | | ✓ | ✓ | 306 |
| **1.2.4** | Verify that all authentication pathways and identity management APIs implement consistent authentication security control strength, such that there are no weaker alternatives per the risk of the application. | | ✓ | ✓ | 306 |

## V1.3 Session Management Architecture

This is a placeholder for future architectural requirements.

## V1.4 Access Control Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.4.1** | Verify that trusted enforcement points, such as access control gateways, servers, and serverless functions, enforce access controls. Never enforce access controls on the client. | | ✓ | ✓ | 602 |
| **1.4.2** | [DELETED, NOT ACTIONABLE] | | | | |
| **1.4.3** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **1.4.4** | Verify the application uses a single and well-vetted access control mechanism for accessing protected data and resources. All requests must pass through this single mechanism to avoid copy and paste or insecure alternative paths. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 284 |
| **1.4.5** | Verify that attribute or feature-based access control is used whereby the code checks the user's authorization for a feature/data item rather than just their role. Permissions should still be allocated using roles. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 275 |

## V1.5 Input and Output Architecture

In 4.0, we have moved away from the term "server-side" as a loaded trust boundary term. The trust boundary is still concerning - making decisions on untrusted browsers or client devices is bypassable. However, in mainstream architectural deployments today, the trust enforcement point has dramatically changed. Therefore, where the term "trusted service layer" is used in the ASVS, we mean any trusted enforcement point, regardless of location, such as a microservice, serverless API, server-side, a trusted API on a client device that has secure boot, partner or external APIs, and so on.

The "untrusted client" term here refers to client-side technologies that render the presentation layer, commonly refered to as 'front-end' technologies. The term "serialization" here not only refers to sending data over the wire like an array of values or taking and reading a JSON structure, but also passing complex objects which can contain logic.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.5.1** | Verify that input and output requirements clearly define how to handle and process data based on type, content, and applicable laws, regulations, and other policy compliance. | | ✓ | ✓ | 1029 |
| **1.5.2** | Verify that serialization is not used when communicating with untrusted clients. If this is not possible, ensure that adequate integrity controls (and possibly encryption if sensitive data is sent) are enforced to prevent deserialization attacks including object injection. | | ✓ | ✓ | 502 |
| **1.5.3** | Verify that input validation is enforced on a trusted service layer. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 602 |
| **1.5.4** | Verify that output encoding occurs close to or by the interpreter for which it is intended. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 116 |

## V1.6 Cryptographic Architecture

Applications need to be designed with strong cryptographic architecture to protect data assets as per their classification. Encrypting everything is wasteful, not encrypting anything is legally negligent. A balance must be struck, usually during architectural or high level design, design sprints or architectural spikes. Designing cryptography as you go or retrofitting it will inevitably cost much more to implement securely than simply building it in from the start.

Architectural requirements are intrinsic to the entire code base, and thus difficult to unit or integrate test. Architectural requirements require consideration in coding standards, throughout the coding phase, and should be reviewed during security architecture, peer or code reviews, or retrospectives.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.6.1** | Verify that there is an explicit policy for management of cryptographic keys and that a cryptographic key lifecycle follows a key management standard such as NIST SP 800-57. | | ✓ | ✓ | 320 |
| **1.6.2** | Verify that consumers of cryptographic services protect key material and other secrets by using key vaults or API based alternatives. | | ✓ | ✓ | 320 |
| **1.6.3** | Verify that all keys and passwords are replaceable and are part of a well-defined process to re-encrypt sensitive data. | | ✓ | ✓ | 320 |
| **1.6.4** | Verify that the architecture treats client-side secrets--such as symmetric keys, passwords, or API tokens--as insecure and never uses them to protect or access sensitive data. | | ✓ | ✓ | 320 |

## V1.7 Errors, Logging and Auditing Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.7.1** | Verify that a common logging format and approach is used across the system. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1009 |
| **1.7.2** | Verify that logs are securely transmitted to a preferably remote system for analysis, detection, alerting, and escalation. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

## V1.8 Data Protection and Privacy Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.8.1** | Verify that all sensitive data is identified and classified into protection levels. | | ✓ | ✓ | |
| **1.8.2** | Verify that all protection levels have an associated set of protection requirements, such as encryption requirements, integrity requirements, retention, privacy and other confidentiality requirements, and that these are applied in the architecture. | | ✓ | ✓ | |

## V1.9 Communications Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.9.1** | Verify the application encrypts communications between components, particularly when these components are in different containers, systems, sites, or cloud providers. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 319 |
| **1.9.2** | Verify that application components verify the authenticity of each side in a communication link to prevent person-in-the-middle attacks. For example, application components should validate TLS certificates and chains. | | ✓ | ✓ | 295 |

## V1.10 Malicious Software Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.10.1** | Verify that a source code control system is in use, with procedures to ensure that check-ins are accompanied by issues or change tickets. The source code control system should have access control and identifiable users to allow traceability of any changes. | | ✓ | ✓ | 284 |

## V1.11 Business Logic Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.11.1** | Verify the definition and documentation of all application components in terms of the business or security functions they provide. | | ✓ | ✓ | 1059 |
| **1.11.2** | Verify that all high-value business logic flows, including authentication, session management and access control, do not share unsynchronized state. | | ✓ | ✓ | 362 |
| **1.11.3** | Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions. | | | ✓ | 367 |

## V1.12 Secure File Upload Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.12.1** | [DELETED, DUPLICATE OF 12.4.1] | | | | |
| **1.12.2** | Verify that user-uploaded files - if required to be displayed or downloaded from the application - are served by either octet stream downloads, or from an unrelated domain, such as a cloud file storage bucket. Implement a suitable Content Security Policy (CSP) to reduce the risk from XSS vectors or other attacks from the uploaded file. | | ✓ | ✓ | 646 |

## V1.13 API Architecture

This is a placeholder for future architectural requirements.

## V1.14 Configuration Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.14.1** | Verify the segregation of components of differing trust levels through well-defined security controls, firewall rules, API gateways, reverse proxies, cloud-based security groups, or similar mechanisms. | | ✓ | ✓ | 923 |
| **1.14.2** | Verify that binary signatures, trusted connections, and verified endpoints are used to deploy binaries to remote devices. | | ✓ | ✓ | 494 |
| **1.14.3** | Verify that the build pipeline warns of out-of-date or insecure components and takes appropriate actions. | | ✓ | ✓ | 1104 |
| **1.14.4** | Verify that the build pipeline contains a build step to automatically build and verify the secure deployment of the application, particularly if the application infrastructure is software defined, such as cloud environment build scripts. | | ✓ | ✓ | |
| **1.14.5** | Verify that application deployments adequately sandbox, containerize and/or isolate at the network level to delay and deter attackers from attacking other applications, especially when they are performing sensitive or dangerous actions such as deserialization. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |
| **1.14.6** | Verify the application does not use unsupported, insecure, or deprecated client-side technologies such as NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | | ✓ | ✓ | 477 |

## References

For more information, see also:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
