# V15: Business Logic Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* The business logic flow is sequential, cannot be obviated, and processed in order.
* Business logic includes limits to detect and prevent automated attacks, such as continuous small funds transfers, or adding a million friends one at a time, and so on.
* High value business logic flows have considered abuse cases and malicious actors, and have protections against spoofing, tampering, repudiation, information disclosure, and elevation of privilege attacks.

## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **15.1** | Verify the application will only process business logic flows for the same user in sequential step order and without skipping steps.  | ✓ | ✓ | ✓ | 2.0 |
| **15.2** | Verify the application will only process business logic flows with all steps being processed in realistic human time, i.e. transactions are not submitted too quickly.  |  | ✓ | ✓ | 2.0 |
| **15.3** | Verify the application has appropriate limits for specific business actions or transactions which are correctly enforced on a per user basis. | ✓ | ✓ | ✓ | 2.0 |
| **15.4** | Verify the application monitors for unusual events or activity from a business logic perspective. For example, attempts to perform actions out of order or actions which a normal user would never attempt. |  | ✓ | ✓ | 2.0 |
| **15.5** | Verify the application has configurable alerting when automated attacks or unusual activity is detected. |  | ✓ | ✓ | 2.0 |
| **15.6** | Verify the application has automated reactions when automated attacks or unusual activity is detected. |  |  | ✓ | 2.0 | 
| **15.7** | Verify the application has sufficient anti-automation controls to detect and protect against data exfiltration, excessive business logic requests, or denial of service attacks. |  | ✓ | ✓ | 2.0 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Business Logic Testing ](https://www.owasp.org/index.php/Testing_for_business_logic)
* [OWASP Cheat Sheet](https://www.owasp.org/index.php/Business_Logic_Security_Cheat_Sheet)
* Anti-automation can be achieved in many ways, including the use of [OWASP AppSensor](https://www.owasp.org/index.php/OWASP_AppSensor_Project) and [OWASP Automated Threats to Web Applications](https://www.owasp.org/index.php/OWASP_Automated_Threats_to_Web_Applications)
* [OWASP AppSensor](https://www.owasp.org/index.php/OWASP_AppSensor_Project) can also help with Attack Detection and Response.
