# V15 Secure Coding Architecture and Implementation

## Control Objective

Many ASVS requirements either relate to a particular area of security like authentication or authorization or relate to a particular type of application functionality such as logging or file handling.

However, this chapter provides more general guidance on how to build applications and how to write secure code correctly. Not just from the perspective of clean architecture and code quality, but rather specific architecture and coding practices that need to be followed in order for the application to be secure.

This chapter also contains requirements to prevent the introduction of malicious code into the application.

## V15.1 Secure Coding Documentation

Many of the requirements needed for a secure and defendable architecture require having clear documentation around what components are used in the application. This section provides the requirements for this documentation including which of these components are risky due to being poorly maintained, unsupported, end of life, or with a history of significant vulnerabilities and which components perform risky operations such as deserialization of untrusted data, raw file parsing or direct memory manipulation. It also includes mandates defining appropriate timescales for addressing vulnerabilities in 3rd party components.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **15.1.1** | Verify that application documentation defines risk based remediation time frames for 3rd party component versions with vulnerabilities and for updating libraries in general, to minimize the risk from these components. | 1 | v5.0.be-1.10.5 |
| **15.1.2** | Verify that an inventory catalog, such as software bill of materials (SBOM), is maintained of all third-party libraries in use, including verifying that components come from pre-defined, trusted, and continually maintained repositories. | 2 | v5.0.be-1.10.2 |
| **15.1.3** | Verify that the application documentation identifies functionality which is time-consuming or resource-demanding. This must include how to prevent a loss of availability due to overusing this functionality and how to avoid a situation where building a response takes longer than the consumer's timeout. Potential defenses may include asynchronous processing, using queues, and limiting parallel processes per user and per application. | 2 | v5.0.be-1.10.6 |
| **15.1.4** | Verify that application documentation highlights "risky" third party libraries which should include: libraries which perform operations which are dangerous from a security perspective, libraries which are poorly maintained, unsupported, or end of life and libraries which have historically had several significant vulnerabilities. | 3 | v5.0.be-1.10.3 |
| **15.1.5** | Verify that application documentation highlights parts of the application where "risky" operations are being performed. "Risky" in this context means those with a high likelihood of being dangerously exploited such as: deserialization of untrusted data, raw file parsing or direct memory manipulation. | 3 | v5.0.be-1.10.4 |

## V15.2 Security Architecture and Dependencies

This section includes requirements for handling risky, outdated or insecure dependencies and components through dependency management. It also includes using architectural level techniques such as sandboxing, encapsulation, containerization, and network isolation to reduce the impact of risky operations or libaries and preventing loss of availability due to overusing resource-demanding functionality.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **15.2.1** | Verify that the application only contains components which have not breached the documented update and remediation time frames. | 1 | v5.0.be-10.6.1 |
| **15.2.2** | Verify that the application has implemented defences against loss of availability loss due to functionality which is time-consuming or resource-demanding, based on the documented security decisions and strategies for this. | 2 | v5.0.be-10.6.4 |
| **15.2.3** | Verify that third-party components and all of their transitive dependencies are included from the expected repository, whether internally owned or an external source, and that there is no risk of a dependency confusion attack. | 3 | v5.0.be-10.6.2 |
| **15.2.4** | Verify that the application implements additional protections around parts of the application which are documented as performing "risky" operations or using "risky" third-party libraries. This could include techniques such as sandboxing, encapsulation, containerization or network level isolation to delay and deter attackers who compromise one part of an application from pivoting elsewhere in the application. | 3 | v5.0.be-10.6.3 |

## V15.3 Defensive Coding

This section covers vulnerability types including type juggling, prototype pollution, mass assignment, and others which result from the use of insecure coding patterns in a particular language. Some may not be relevant to all languages whereas others will have language specific fixes or may relate to the way that a particular language or framework handles a feature such as HTTP parameters. It also considers the risk of not cryptographically validating application updates.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **15.3.1** | Verify that the application only returns data which the user has permission to access. For example, the API response does not return a full object with attributes that contain values the user has no permission to access, despite having permission to access the data object itself. | 1 | v5.0.be-10.4.5 |
| **15.3.2** | Verify that where the application backend makes calls to external URLs, it is configured to not follow redirects unless it is intended functionality. | 2 | v5.0.be-10.4.8 |
| **15.3.3** | Verify that the application has countermeasures to protect against mass assignment attacks by limiting allowed fields per controller and action, e.g., it is not possible to insert or update a field value when it was not intended to be part of that action. | 2 | v5.0.be-10.4.4 |
| **15.3.4** | Verify that the application is able to discern and utilizes the user's true IP address to provide for sensitive functions, including rate limiting and logging. | 2 | v5.0.be-10.4.6 |
| **15.3.5** | Verify that the application explicitly ensures that variables are of the correct type and performs strict equality and comparator operations. This is to avoid type juggling or type confusion vulnerabilities caused by the application code making an assumption about a variable type. | 2 | v5.0.be-10.4.1 |
| **15.3.6** | Verify that JavaScript code is written in a way that prevents prototype pollution, for example, by using Set() or Map() instead of object literals. | 2 | v5.0.be-10.4.3 |
| **15.3.7** | Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (query string, body parameters, cookies, or header fields). | 2 | v5.0.be-10.4.7 |
| **15.3.8** | Verify that the application avoids DOM clobbering when using client-side JavaScript by employing explicit variable declarations, performing strict type checking, avoiding storing global variables on the document object, and implementing namespace isolation. | 3 | v5.0.be-10.4.2 |
| **15.3.9** | Verify that, if the application (backend or frontend) builds and sends requests, it uses validation, sanitization, or other mechanisms to avoid creating URIs (such as for API calls) or HTTP request header fields (such as Authorization or Cookie), which are too long to be accepted by the receiving component. This could cause a denial of service, such as when sending an overly long request (e.g. a long cookie header field) results in the server always responding with an error status. | 3 | v5.0.be-10.4.9 |
| **15.3.10** | Verify that, if the application has an auto-update feature, updates must be digitally signed, with the digital signature being validated before installing or executing the update. | 3 | v5.0.be-10.4.10 |

## V15.4 Concurrency

Concurrency issues such as race conditions, TOC/TOU vulnerabilities, deadlocks, livelocks, thread starvation, and improper synchronization can lead to unpredictable behavior and security risks. This section includes various techniques and strategies to help mitigate these risks.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **15.4.1** | Verify that only thread-safe types are used in multi-threaded contexts, or that non-thread-safe types are synchronized to prevent race conditions. | 3 | v5.0.be-10.7.1 |
| **15.4.2** | Verify that concurrent access to shared resources is controlled using synchronization primitives (e.g., locks, mutexes, semaphores) to prevent race conditions and ensure atomic operations on these resources. | 3 | v5.0.be-10.7.2 |
| **15.4.3** | Verify that all access to shared resources is consistently checked and accessed in a single atomic operation to prevent Time-of-Check to Time-of-Use (TOCTOU) race conditions, ensuring resource state consistency between check and use. | 3 | v5.0.be-10.7.3 |
| **15.4.4** | Verify that resource acquisition uses a consistent locking strategy to avoid circular dependencies and ensure forward progress, preventing both deadlocks and livelock scenarios. | 3 | v5.0.be-10.7.4 |
| **15.4.5** | Verify that resource allocation policies prevent thread starvation by ensuring fair access to resources, such as by leveraging thread pools, allowing lower-priority threads to proceed within a reasonable timeframe. | 3 | v5.0.be-10.7.5 |
| **15.4.6** | Verify that locking primitives are only accessible to the owning class or module and are not publicly modifiable, ensuring that locks cannot be inadvertently or maliciously modified by external classes or code. | 3 | v5.0.be-10.7.6 |

## References

For more information, see also:

* [Reference on Protecting against DOM Clobbering](https://domclob.xyz/domc_wiki/indicators/patterns.html#secure-patterns--guidelines)
* [OWASP Prototype Pollution Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [Software Component Verification Standard V2 L1-3 requirements](https://github.com/OWASP/Software-Component-Verification-Standard/blob/master/en/0x11-V2-Software_Bill_of_Materials.md)
* [OWASP Testing Guide: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution)
