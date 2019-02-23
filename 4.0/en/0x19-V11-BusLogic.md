# V11: Business Logic Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* The business logic flow is sequential, processed in order, and cannot be bypassed.
* Business logic includes limits to detect and prevent automated attacks, such as continuous small funds transfers, or adding a million friends one at a time, and so on.
* High value business logic flows have considered abuse cases and malicious actors, and have protections against spoofing, tampering, repudiation, information disclosure, and elevation of privilege attacks.

## V11.1 Business Logic Security Requirements

Business logic security is so individual to every application that no one checklist will ever apply. Business logic security must be designed in to protect against likely external threats - it cannot be added using web application firewalls or secure communications. We recommend the use of threat modelling during design sprints, for example using the OWASP Cornucopia or similar tools.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **11.1.1** | Verify the application will only process business logic flows for the same user in sequential step order and without skipping steps.| ✓ | ✓ | ✓ | 841 |
| **11.1.2** | Verify the application will only process business logic flows with all steps being processed in realistic human time, i.e. transactions are not submitted too quickly.| ✓ | ✓ | ✓ | 779 |
| **11.1.3** | Verify the application has appropriate limits for specific business actions or transactions which are correctly enforced on a per user basis. | ✓ | ✓ | ✓ | 770 |
| **11.1.4** | Verify the application has sufficient anti-automation controls to detect and protect against data exfiltration, excessive business logic requests, excessive file uploads or denial of service attacks. | ✓ | ✓ | ✓ | 770 |
| **11.1.5** | Verify the application has business logic limits or validation to protect against likely business risks or threats, identified using threat modelling or similar methodologies. | ✓ | ✓ | ✓ | 841 |
| **11.1.6** | Verify the application does not suffer from "time of check to time of use" (TOCTOU) issues or other race conditions for sensitive operations. | | ✓ | ✓ | 367 |
| **11.1.7** | Verify the application monitors for unusual events or activity from a business logic perspective. For example, attempts to perform actions out of order or actions which a normal user would never attempt. ([C9](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering)) | ✓ | ✓ | ✓ | 754 |
| **11.1.8** | Verify the application has configurable alerting when automated attacks or unusual activity is detected. | | ✓ | ✓ | 390 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Business Logic Testing](https://www.owasp.org/index.php/Testing_for_business_logic)
* [OWASP Cheat Sheet](https://www.owasp.org/index.php/Business_Logic_Security_Cheat_Sheet)
* Anti-automation can be achieved in many ways, including the use of [OWASP AppSensor](https://www.owasp.org/index.php/OWASP_AppSensor_Project) and [OWASP Automated Threats to Web Applications](https://www.owasp.org/index.php/OWASP_Automated_Threats_to_Web_Applications)
* [OWASP AppSensor](https://www.owasp.org/index.php/OWASP_AppSensor_Project) can also help with Attack Detection and Response.
* [OWASP Cornucopia](https://www.owasp.org/index.php/OWASP_Cornucopia)