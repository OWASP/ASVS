# V11 Business Logic

## Control Objective

Ensure that a verified application satisfies the following high-level requirements:

* The business logic flow is sequential, processed in order, and cannot be bypassed.
* Business logic includes limits and controls to detect and prevent automated attacks, such as continuous small funds transfers and adding a million friends one at a time.
* High-value business logic flows have considered abuse cases and malicious actors, and have protections against spoofing, tampering, information disclosure, and elevation of privilege attacks.

## V11.1 Business Logic Security

Business logic security is so individual to every application that no one checklist will ever apply. Business logic security must be designed into the system to protect against likely external threats - it cannot be added using web application firewalls or secure communications. We recommend the use of threat modeling during design sprints, for example using the OWASP Cornucopia or similar tools.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **11.1.1** | Verify that the application will only process business logic flows for the same user in sequential step order and without skipping steps. | ✓ | ✓ | ✓ | 841 |
| **11.1.2** | [MOVED TO 11.2.1] | | | | |
| **11.1.3** | [MODIFIED] Verify that the application has appropriate limits defined on a per user basis for specific business actions or transactions. | ✓ | ✓ | ✓ | |
| **11.1.4** | [MOVED TO 11.2.2] | | | | |
| **11.1.5** | [MODIFIED] Verify that the application has globally defined business logic limits or validation to protect against likely business risks or threats, identified using threat modeling or similar methodologies. | ✓ | ✓ | ✓ | |
| **11.1.6** | [MODIFIED] Verify that the application uses synchronization and locking mechanisms for sensitive operations in order to keep internal data consistent, maintain user state, and prevent race conditions, such as 'time of check to time of use (TOCTOU)' vulnerabilities. | | ✓ | ✓ | 367 |
| **11.1.7** | [DELETED, MOVED TO 7.2.4] | | | | |
| **11.1.8** | [DELETED, MOVED TO 7.2.5] | | | | |
| **11.1.9** | [ADDED] Verify that "atomic transactions" are being used at the business logic level such that either a business logic operation succeeds in its entirety, or it is rolled back to the previous correct state. | | ✓ | ✓ | |

## V11.2 Anti-automation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **11.2.1** | [MOVED FROM 11.1.2] Verify that the application will only process business logic flows with all steps being processed in realistic human time, i.e. transactions are not submitted too quickly. | ✓ | ✓ | ✓ | 799 |
| **11.2.2** | [MODIFIED, MOVED FROM 11.1.4] Verify that the application has anti-automation controls to protect against excessive calls to application functionality which could result in mass data exfiltration, junk data creation, resource quota exhaustion, rate limit breaches, out-of-band communication flooding, denial of service, overuse of an expensive resource, etc. | ✓ | ✓ | ✓ | 770 |

## References

For more information, see also:

* [OWASP Web Security Testing Guide 4.1: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README.html)
* Anti-automation can be achieved in many ways, including the use of [OWASP AppSensor](https://github.com/jtmelton/appsensor) and [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP AppSensor](https://github.com/jtmelton/appsensor) can also help with Attack Detection and Response.
* [OWASP Cornucopia](https://owasp.org/www-project-cornucopia/)
