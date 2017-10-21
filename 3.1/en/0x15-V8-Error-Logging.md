# V8: Error Handling and Logging Verification Requirements

## Control Objective

The primary objective of error handling and logging is to provide a useful reaction by the user, administrators, and incident response teams. The objective is not to create massive amounts of logs, but high quality logs, with more signal than discarded noise.

High quality logs will often contain sensitive data, and must be protected as per local data privacy laws or directives. This should include:

* Not collecting or logging sensitive information if not specifically required.
* Ensuring all logged information is handled securely and protected as per its data classification.
* Ensuring that logs are not forever, but have an absolute lifetime that is as short as possible.

If logs contain private or sensitive data, the definition of which varies from country to country, the logs become some of the most sensitive information held by the application and thus very attractive to attackers in their own right.


## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **8.1** | Verify that the application does not output error messages or stack traces containing sensitive data that could assist an attacker, including session id, software/framework versions and personal information. | ✓ | ✓ | ✓ | 1.0 |
| **8.1** | Verify that error handling logic in security controls denies access by default. |  | ✓ | ✓ | 1.0 |
| **8.1** | Verify security logging controls provide the ability to log success and particularly failure events that are identified as security-relevant. |  | ✓ | ✓ | 1.0 |
| **8.1** | Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens. |  | ✓ | ✓ | 1.0 |
| **8.1** | Verify that all events that include untrusted data will not execute as code in the intended log viewing software. |  | ✓ | ✓ | 1.0 |
| **8.1** | Verify that security logs are protected from unauthorized access and modification. |  | ✓ | ✓ | 1.0 |
| **8.1** | Verify that the application does not log sensitive data as defined under local privacy laws or regulations, organizational sensitive data as defined by a risk assessment, or sensitive authentication data that could assist an attacker, including user’s session identifiers, passwords, hashes, or API tokens. |  | ✓ | ✓ | 3.0 |
| **8.1** | Verify that all non-printable symbols and field separators are properly encoded in log entries, to prevent log injection. |  |  | ✓ | 2.0 |
| **8.1** | Verify that log fields from trusted and untrusted sources are distinguishable in log entries. |  |  | ✓ | 2.0 |
| **8.1** | Verify that an audit log or similar allows for non-repudiation of key transactions. | ✓ | ✓ | ✓ | 3.0 |
| **8.1** | Verify that security logs have some form of integrity checking or controls to prevent unauthorized modification. |  |  | ✓ | 3.0 |
| **8.1** | Verify that logs are stored on a different partition than the application is running with proper log rotation. |  |  | ✓ | 3.1 |
| **8.1** | Verify that time sources are synchronized to the correct time and time zone. | ✓ | ✓ | ✓ | 3.1 |



## References

For more information, see also:

* [OWASP Testing Guide 4.0 content: Testing for Error Handling](https://www.owasp.org/index.php/Testing_for_Error_Handling)
