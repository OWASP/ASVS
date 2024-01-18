# V10 Malicious and Insecure Code

## Control Objective

Ensure that the code satisfies the following high-level requirements:

* Malicious activity is handled securely and properly to not affect the rest of the application.
* Does not have time bombs or other time-based attacks.
* Does not "phone home" to malicious or unauthorized destinations.
* Does not have back doors, Easter eggs, salami attacks, rootkits, or unauthorized code that can be controlled by an attacker.

Finding malicious code is proof of the negative, which is impossible to completely validate. Best efforts should be undertaken to ensure that the code has no inherent malicious code or unwanted functionality.

## V10.1 Code Integrity

The best defense against malicious code is "trust, but verify". Introducing unauthorized or malicious code into code is often a criminal offense in many jurisdictions. Policies and procedures should make sanctions regarding malicious code clear.

Lead developers should regularly review code check-ins, particularly those that might access time, I/O, or network functions.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.1.1** | [DELETED, NOT IN SCOPE] | | | | |

## V10.2 Malicious Code Search

Malicious code is extremely rare and is difficult to detect. Manual line-by-line code review can assist with detecting logic bombs, but even the most experienced code reviewers will struggle to find malicious code even if they know it exists.

Complying with this section is not possible without complete access to source code, including third-party libraries.

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

## References

For more information, see also:

* [Reference on Protecting against DOM Clobbering](https://domclob.xyz/domc_wiki/indicators/patterns.html#secure-patterns--guidelines)
