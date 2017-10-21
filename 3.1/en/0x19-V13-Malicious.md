# V13: Malicious Code Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* Malicious activity is handled securely and properly as to not affect the rest of the application.
* Do not have time bombs or other time based attacks built into them
* Do not “phone home” to malicious or unauthorized destinations
* Applications do not have back doors, Easter eggs, salami attacks, or logic flaws that can be controlled by an attacker

Malicious code is extremely rare, and is difficult to detect. Manual line by line code review can assist looking for logic bombs, but even the most experienced code reviewer will struggle to find malicious code even if they know it exists. This section is not possible to complete without access to source code, including as many third party libraries as possible.


## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **13.1** | Verify all malicious activity is adequately sandboxed, containerized or isolated to delay and deter attackers from attacking other applications. | ✓ | ✓ | ✓ | 2.0 |
| **13.2** | Verify that the application source code, and as many third party libraries as possible, does not contain back doors, Easter eggs, and logic flaws in authentication, access control, input validation, and the business logic of high value transactions.  | ✓ | ✓ | ✓ | 3.0.1 |



## References
