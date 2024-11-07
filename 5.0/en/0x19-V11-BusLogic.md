# V11 Business Logic

## Definition

Business logic in application security refers to the customized rules and processes that safeguard an application in accordance with its specific requirements or the needs of the business it serves. These rules dictate various aspects such as user interactions, data handling, and system behavior, tailored to suit the unique characteristics of each application, business, or industry.

Some examples of business logic vulnerabilities:

### Example 1

* Business Rule: Products should only be provided to customers after their transactions are successfully verified to prevent loss due to fraud or non-payment.
* Vulnerability: If an attacker can manipulate the application to deliver a product before the purchase is verified, there's a risk of providing goods without receiving payment, leading to financial losses for the business.

### Example 2

* **Business Rule:** High-value transactions above a certain threshold should be manually reviewed to ensure accuracy, legitimacy, and compliance with business policies.
* **Vulnerability:** If an attacker can manipulate the application to skip the review process for high-value transactions, then fraudulent or erroneous transactions may go unnoticed, increasing the risk of financial losses or compliance violations.

## Control Objective

Ensure that a verified application satisfies the following high-level requirements:

* The business logic flow is sequential, processed in order, and cannot be bypassed.
* Business logic includes limits and controls to detect and prevent automated attacks, such as continuous small funds transfers and adding a million friends one at a time.
* High-value business logic flows have considered abuse cases and malicious actors, and have protections against spoofing, tampering, information disclosure, and elevation of privilege attacks.

## V1.11 Business Logic Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.11.1** | [DELETED, NOT IN SCOPE] | | | | |
| **1.11.2** | [MOVED TO 10.7.2] | | | | |
| **1.11.3** | [DELETED, DUPLICATE OF 11.1.6] | | | | |
| **1.11.4** | [ADDED] Verify that expectations for business logic limits and validations are clearly documented including both per-user and also globally across the application. | | ✓ | ✓ | |

## V11.1 Business Logic Security

Business logic security is so individual to every application that no one checklist will ever apply. Business logic security must be designed into the system to protect against likely external threats - it cannot be added using web application firewalls or secure communications.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **11.1.1** | Verify that the application will only process business logic flows for the same user in sequential step order and without skipping steps. | ✓ | ✓ | ✓ | 841 |
| **11.1.2** | [MOVED TO 11.2.1] | | | | |
| **11.1.3** | [MODIFIED, MERGED FROM 11.1.5] Verify that business logic limits and validations are implemented as per the application's documentation. | ✓ | ✓ | ✓ | |
| **11.1.4** | [MOVED TO 11.2.2] | | | | |
| **11.1.5** | [DELETED, MERGED TO 11.1.3] | | | | |
| **11.1.6** | [SPLIT TO 10.7.1, 10.7.2, 10.7.3] | | | | |
| **11.1.7** | [MOVED TO 7.2.4] | | | | |
| **11.1.8** | [MOVED TO 7.2.5] | | | | |
| **11.1.9** | [ADDED] Verify that "atomic transactions" are being used at the business logic level such that either a business logic operation succeeds in its entirety, or it is rolled back to the previous correct state. | | ✓ | ✓ | |
| **11.1.10** | [ADDED] Verify that very high-value business logic flows are restricted with multi-user approval to prevent unauthorized or accidental actions. This could include but is not limited to large monetary transfers, contract approvals, access to critical nuclear facility operations, healthcare record modifications, access to classified information, or safety overrides in manufacturing. | | | ✓ | |

## V11.2 Anti-automation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **11.2.1** | [MOVED FROM 11.1.2, LEVEL L1 > L3] Verify that business logic processes require realistic human timing, preventing excessively rapid transaction submissions. | | | ✓ | 799 |
| **11.2.2** | [MODIFIED, MOVED FROM 11.1.4, LEVEL L1 > L2] Verify that anti-automation controls are in place to protect against excessive calls to application functions that could lead to data exfiltration, garbage data creation, quota exhaustion, rate limit breaches, denial of service, or overuse of costly resources. | | ✓ | ✓ | 770 |

## References

For more information, see also:

* [OWASP Web Security Testing Guide 4.2: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README)
* Anti-automation can be achieved in many ways, including the use of the [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
