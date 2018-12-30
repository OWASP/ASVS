# V13: Malicious Code Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* Malicious activity is handled securely and properly so as to not affect the rest of the application.
* Does not have time bombs or other time based attacks built into it.
* Does not “phone home” to malicious or unauthorized destinations.
* Does not have back doors, Easter eggs, salami attacks, or logic flaws that can be controlled by an attacker.

Malicious code is extremely rare, and is difficult to detect. Manual line by line code review can assist looking for logic bombs, but even the most experienced code reviewer will struggle to find malicious code even if they know it exists. This section is not possible to complete without access to source code, including as many third party libraries as possible.

## Malicious Code Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| 13.1 | Verify all malicious activity is adequately sandboxed, containerized or isolated to delay and deter attackers from attacking other applications. | ✓ | ✓ | ✓ | 2.0 |
| 13.2 | Verify that the application source code and third party libraries do not contain unauthorized phone home or data collection capabilities. Where such functionality exists, obtain the user's permission for it to operate prior to collecting any data. |  | ✓ | ✓ | 4.0 |
| 13.3 | Verify that the application does not execute external code from untrusted sources, such as loading code or libraries from the Internet post-installation.  |  | ✓ | ✓ | 4.0 |
| 13.4 | Verify that if the application has an auto-update feature, updates should be obtained over secure channels and digitally signed. The update code must validate the digital signature of the update before installing or executing the update.  |  | ✓ | ✓ | 4.0 |
| 13.5 | Verify that the application source code and third party libraries do not contain back doors, such as hard-coded or additional undocumented accounts or keys, code obfuscation, undocumented binary blobs, root kits, or anti-debugging, insecure debugging features, or otherwise out of date, insecure, or hidden functionality that could be used maliciously if discovered.  | | | ✓ | 4.0 |
| 13.6 | Verify that the application source code and third party libraries does not contain time bombs by searching for date and time related functions.  |  |  | ✓ | 4.0 |
| 13.7 | Verify that the application source code and third party libraries does not contain malicious code, such as salami attacks, logic bypasses, or logic bombs.  |  |  | ✓ | 4.0 |
| 13.8 | Verify that the application source code and third party libraries do not contain Easter eggs or any other potentially unwanted functionality. |  |  | ✓ | 4.0 |

## References

* TBA
