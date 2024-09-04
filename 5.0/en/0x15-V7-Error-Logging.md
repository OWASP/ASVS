# V7 Security Logging and Error Handling

## Control Objective

Security logs are a specific type of logging which is not focused on error handling or performance but rather specifically on recording when security sensitive events occur.

The primary objective of security logging is to provide useful information for the user, administrators, and incident response teams, which contains more signal than discarded noise. When logging security-related events, ensure that there is a purpose to the log and that it can be distinguished by SIEM or analysis software.

Security logs, which often contain sensitive data, must be safeguarded in accordance with local data privacy laws or directives. This sensitive data also makes them very attractive to attackers as a target in their own right so they should be carefully protected.

Aside from this, it is also important to ensure that the application fails securely and that errors do not disclose unnecessary information or cause the application to stop operating.

## V7.1 General Logging

Logging sensitive information is dangerous - the logs become classified themselves, which means they may need to be encrypted, become subject to retention policies, and must be disclosed in security audits. Ensure only necessary information is kept in logs, and certainly no payment, credentials (including session tokens), sensitive or personally identifiable information.

For the specific information which should be included in a log entry, refer to external detailed guidance such as the OWASP Logging Cheat Sheet.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **7.1.1** | [MODIFIED, MERGED FROM 7.1.2] Verify that when logging sensitive data, the application considers the protection level of the data. For example, it may not be allowed to log certain data such as credentials or payment details. Other data such as session tokens may only be logged having been hashed or masked, either in full or partially. | ✓ | ✓ | ✓ | 532 |
| **7.1.2** | [DELETED, MERGED TO 7.1.1] | | | | |
| **7.1.3** | [MOVED TO 7.2.3] | | | | |
| **7.1.4** | [MODIFIED] Verify that each log entry includes necessary metadata that would allow for a detailed investigation of the timeline when an event happens. | | ✓ | ✓ | 778 |
| **7.1.5** | [MOVED FROM 7.3.4] Verify that time sources are synchronized to the correct time and time zone. Strongly consider logging only in UTC if systems are global to assist with post-incident forensic analysis. | | ✓ | ✓ | |
| **7.1.6** | [ADDED] Verify that the application only stores or broadcasts logs to the files and services that are documented in the log inventory. | | ✓ | ✓ | |
| **7.1.7** | [MODIFIED, MOVED FROM 1.7.1] Verify that logs can be read and correlated by the log processor which is in use, preferably by using a common logging format. | | ✓ | ✓ | |

## V7.2 Security Events

Logging events which are security relevant is an important mechanism for being able to investigate suspicious activity within the application.

This section will briefly discuss the types of events to log but deliberately does not go into too much detail. It will be necessary to refer to external detailed guidance such as the OWASP Logging Cheat Sheet and the OWASP Application Logging Vocabulary Cheat Sheet for specific implementation details.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **7.2.1** | [MODIFIED] Verify that all authentication operations are logged including both successful and unsuccessful attempts. Additional metadata such as type of authentication or factors used should also be collected. | | ✓ | ✓ | 778 |
| **7.2.2** | [MODIFIED] Verify that all access control decisions are logged including failed attempts. | | ✓ | ✓ | 285 |
| **7.2.3** | [MODIFIED, MOVED FROM 7.1.3] Verify that the application logs attempts to bypass the security controls defined in the design documentation such as input validation. | | ✓ | ✓ | 778 |
| **7.2.4** | [MODIFIED, MOVED FROM 11.1.7] Verify that the application monitors for unusual events or activity from a business logic perspective. | | ✓ | ✓ | 754 |
| **7.2.5** | [MODIFIED, MOVED FROM 11.1.8] Verify that the application has configurable alerting when unusual or malicious activity is detected. | | ✓ | ✓ | 390 |
| **7.2.6** | [MODIFIED, MOVED FROM 9.2.5] Verify that the application logs security control failures such as backend TLS failures. | | | ✓ | 778 |
| **7.2.7** | [MODIFIED, MOVED FROM 8.3.5] Verify that accessing sensitive data is logged (without logging the sensitive data itself) if this is required by relevant data protection requirements. | | ✓ | ✓ | |

## V7.3 Log Protection

Logs that can be trivially modified or deleted are useless for investigations and prosecutions. Disclosure of logs can expose inner details about the application or the data it contains. Care must be taken when protecting logs from unauthorized disclosure, modification or deletion.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **7.3.1** | Verify that all logging components appropriately encode data to prevent log injection. | | ✓ | ✓ | 117 |
| **7.3.2** | [DELETED, DUPLICATE OF 7.3.1] | | | | |
| **7.3.3** | [MODIFIED] Verify that logs are protected from unauthorized access and cannot be modified. | | ✓ | ✓ | 200 |
| **7.3.4** | [MOVED TO 7.1.5] | | | | |
| **7.3.5** | [MOVED FROM 1.7.2] Verify that logs are securely transmitted to a preferably remote system for analysis, detection, alerting, and escalation. | | ✓ | ✓ | |

## V7.4 Error Handling

The purpose of error handling is to ensure the application fails gracefully and securely without disclosing sensitive information. The application should be written in a way that ensures this will always happen.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **7.4.1** | Verify that a generic message is shown when an unexpected or security sensitive error occurs, potentially with a unique ID which support personnel can use to investigate. | ✓ | ✓ | ✓ | 210 |
| **7.4.2** | [MODIFIED] Verify that a consistent and standardized exception handling mechanism (or a functional equivalent) is used across the codebase. | | ✓ | ✓ | 544 |
| **7.4.3** | Verify that a "last resort" error handler is defined which will catch all unhandled exceptions. | | ✓ | ✓ | 431 |
| **7.4.4** | [ADDED] Verify that the application is designed in a way that a failure to access external resources does not result in the entire application failing, for example using the circuit breaker pattern. | | ✓ | ✓ | |

Note: Certain languages, such as Swift and Go - and through common design practice - many functional languages, do not support exceptions or last-resort event handlers. In this case, architects and developers should use a pattern, language, or framework-friendly way to ensure that applications can securely handle exceptional, unexpected, or security-related events.

## References

For more information, see also:

* [OWASP Testing Guide 4.0 content: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README.html)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
* [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
* [OWASP Application Logging Vocabulary Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html)
