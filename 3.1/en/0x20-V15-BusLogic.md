# V15: Business Logic Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* The business logic flow is sequential and in order
* Business logic includes limits to detect and prevent automated attacks, such as continuous small funds transfers, or adding a million friends one at a time, and so on.
* High value business logic flows have considered abuse cases and malicious actors, and have protections against spoofing, tampering, repudiation, information disclosure, and elevation of privilege attacks.


## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **15.1** | Verify the application will only process business logic flows in sequential step order, with all steps being processed in realistic human time, and not process out of order, skipped steps, process steps from another user, or too quickly submitted transactions. |  | ✓ | ✓ | 2.0 |
| **15.2** | Verify the application has business limits and correctly enforces on a per user basis, with configurable alerting and automated reactions to automated or unusual attack. |  | ✓ | ✓ | 2.0 |



## References

For more information, see also:

* [OWASP Testing Guide 4.0: Business Logic Testing ](https://www.owasp.org/index.php/Testing_for_business_logic)
* [OWASP Cheat Sheet](https://www.owasp.org/index.php/Business_Logic_Security_Cheat_Sheet)
