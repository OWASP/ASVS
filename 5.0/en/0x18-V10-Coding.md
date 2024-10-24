# V10 Secure Coding Architecture and Implementation

## Control Objective

Many ASVS requirements either relate to a particular area of security like authentication or access control or relate to a particular type of application functionality such as logging or file handling.

However, this chapter provides more general guidance on how to build applications and how to write secure code correctly. Not just from the perspective of clean architecture and code quality, but rather specific architecture and coding practices that need to be followed in order for the application to be secure.

This chapter also contains requirements to prevent the introduction of malicious code into the application.

## V10.1 Code Integrity

<!--
The best defense against malicious code is "trust, but verify". Introducing unauthorized or malicious code into code is often a criminal offense in many jurisdictions. Policies and procedures should make sanctions regarding malicious code clear.

Lead developers should regularly review code check-ins, particularly those that might access time, I/O, or network functions.
-->

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.1.1** | [DELETED, NOT IN SCOPE] | | | | |

## V10.2 Malicious Code Search

Malicious code is extremely rare and is difficult to detect. Manual line-by-line code review can assist with detecting logic bombs, but even the most experienced code reviewers will struggle to find malicious code even if they know it exists. As such, this section is mostly L3. Complying with this section is not possible without complete access to source code, including third-party libraries.

Ultimately, finding malicious code is proof of the negative, which is impossible to completely validate. Best efforts should be undertaken to ensure that the code has no inherent malicious code or unwanted functionality.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.2.1** | Verify that the application source code and third party libraries do not contain unauthorized phone home or data collection capabilities. Where such functionality exists, obtain the user's permission for it to operate before collecting any data. | | ✓ | ✓ | 359 |
| **10.2.2** | [MOVED TO 8.3.11] | | | | |
| **10.2.3** | Verify that the application source code and third party libraries do not contain back doors, such as hard-coded or additional undocumented accounts or keys, code obfuscation, undocumented binary blobs, rootkits, or anti-debugging, insecure debugging features, or otherwise out of date, insecure, or hidden functionality that could be used maliciously if discovered. | | | ✓ | 507 |
| **10.2.4** | Verify that the application source code and third party libraries do not contain time bombs by searching for date and time related functions. | | | ✓ | 511 |
| **10.2.5** | Verify that the application source code and third party libraries do not contain malicious code, such as salami attacks, logic bypasses, or logic bombs. | | | ✓ | 511 |
| **10.2.6** | Verify that the application source code and third party libraries do not contain Easter eggs or any other potentially unwanted functionality. | | | ✓ | 507 |

## V10.3 Application Integrity

Once an application is deployed, malicious code can still be inserted. Applications need to protect themselves against common attacks, such as executing unsigned code from untrusted sources and subdomain takeovers.

Complying with this section is likely to be operational and continuous.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.3.1** | Verify that if the application has a client or server auto-update feature, updates should be obtained over secure channels and digitally signed. The update code must validate the digital signature of the update before installing or executing the update. | ✓ | ✓ | ✓ | 16 |
| **10.3.2** | [MODIFIED] Verify that the application only loads or executes code, modules, content or plugins from sources not under the application's direct control or protection if it employs integrity protections, such as code signing. | ✓ | ✓ | ✓ | 829 |
| **10.3.3** | [DELETED, NOT IN SCOPE] | | | | |

## V10.4 Defensive Coding

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.4.1** | [ADDED] Verify that the application explicitly ensures that variables are of the correct type and performs strict equality and comparator operations to avoid type juggling or confusion vulnerabilities caused by the application code making an assumption about a variable type. | ✓ | ✓ | ✓ | 843 |
| **10.4.2** | [ADDED] Verify that the application avoids DOM clobbering when using client-side JavaScript by employing explicit variable declarations, performing strict type checking, avoiding storing global variables on the document object, and implementing namespace isolation. | | ✓ | ✓ | 79 |
| **10.4.3** | [ADDED] Verify that JavaScript code is written in a way that prevents prototype pollution, for example, by using Set() or Map() instead of object literals. | | ✓ | ✓ | |
| **10.4.4** | [MODIFIED, MOVED FROM 5.1.2] Verify that the application has countermeasures to protect against mass assignment attacks by limiting allowed fields per controller and action, e.g. it is not possible to insert or update a field value when it was not intended to be part of that action. | ✓ | ✓ | ✓ | 915 |
| **10.4.5** | [ADDED] Verify that the application only returns data which the user has permission to access. For example, the API response does not return a full object with attributes that contain values the user has no permission to access, despite having permission to access the data object itself. | ✓ | ✓ | ✓ | |
| **10.4.6** | [ADDED] Verify that the application is able to discern and utilizes the user's true IP address to provide for sensitive functions, including rate limiting and logging. | | ✓ | ✓ | 348 |

## 10.5 Security Architecture

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.5.1** | [MODIFIED, MOVED FROM 1.14.5, LEVEL L2 > L3] Verify that the application architecture uses techniques such as sandboxing, containerization or network level isolation to delay and deter attackers from attacking other parts of the application, especially when the application is performing sensitive or dangerous actions such as deserialization. | | | ✓ | 265 |

## 10.6 Code Dependencies

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.6.1** | [ADDED] Verify that third party components are being included from the expected repository, whether that is internally owned or an external source, and that there is no risk of a dependency confusion attack. | ✓ | ✓ | ✓ | 427 |

## References

For more information, see also:

* [Reference on Protecting against DOM Clobbering](https://domclob.xyz/domc_wiki/indicators/patterns.html#secure-patterns--guidelines)
* [OWASP Prototype Pollution Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
