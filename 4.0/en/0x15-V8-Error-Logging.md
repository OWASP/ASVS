# V8: Error Handling and Logging Verification Requirements

## Control Objective

The primary objective of error handling and logging is to provide useful information for the user, administrators, and incident response teams. The objective is not to create massive amounts of logs, but high quality logs, with more signal than discarded noise.

High quality logs will often contain sensitive data, and must be protected as per local data privacy laws or directives. This should include:

* Not collecting or logging sensitive information unless specifically required.
* Ensuring all logged information is handled securely and protected as per its data classification.
* Ensuring that logs are not stored forever, but have an absolute lifetime that is as short as possible.

If logs contain private or sensitive data, the definition of which varies from country to country, the logs become some of the most sensitive information held by the application and thus very attractive to attackers in their own right.

## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **8.1** | Verify that the application does not log credentials, session tokens or payment details. | ✓ | ✓ | ✓ | 4.0 |
| **8.2** | Verify that the application does not log other sensitive data as defined under local privacy laws or relevant security policy. |  | ✓ | ✓ | 3.0 |
| **8.3** | Verify that the application logs security relevant events including successful and failed authentication events, access control failures and input validation failures. | ✓ | ✓ | ✓ | 4.0 |
| **8.4** | Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens. |  | ✓ | ✓ | 1.0 |
| **8.5** | Verify that all events are protected from injection when viewed in log viewing software. |  | ✓ | ✓ | 1.0 |
| **8.6** | Verify that security logs are protected from unauthorized access and modification. |  | ✓ | ✓ | 1.0 |
| **8.7** | Verify that the application appropriately encodes user-supplied data to prevent log injection. | ✓ | ✓ | ✓ | 4.0 |
| **8.8** | Verify that logs are transmitted to a remote system for analysis, detection, alerting, and escalation. |  |  | ✓ | 4.0 |
| **8.9** | Verify that time sources are synchronized to the correct time and time zone. | ✓ | ✓ | ✓ | 4.0 |
| **8.10** | Verify that all authentication decisions are logged, without storing sensitive session identifiers or memorized secrets. This should include requests with relevant metadata needed for security investigations.  | ✓ | ✓ | ✓ | 4.0 |
| **8.11** | Verify that a common logging format and approach is used across the system.  | ✓ | ✓ | ✓ | 4.0 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0 content: Testing for Error Handling](https://www.owasp.org/index.php/Testing_for_Error_Handling)
