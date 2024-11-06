# V4 Access Control

## Control Objective

Authorization is the concept of allowing access to resources only to those permitted to use them. Ensure that a verified application satisfies the following high-level requirements:

* Persons accessing resources hold valid credentials to do so.
* Users are associated with a well-defined set of entitlements.
* Access control policy metadata is protected from replay or tampering.

Access control deficiencies are unlikely to be discovered using generic automated testing tools. Verifying the requirements in this section will either require manual or manual assisted testing or alternatively a robust series of automated end-to-end access control tests which validate the effectiveness of the access controls under various scenarios. Integrating these tests into the continuous integration/continuous deployment (CI/CD) pipeline will make it easier to validate these requirements on an ongoing basis.

## V1.4 Access Control Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.4.1** | [DELETED, DUPLICATE OF 4.1.1] | | | | |
| **1.4.2** | [DELETED] | | | | |
| **1.4.3** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **1.4.4** | [DELETED, INSUFFICIENT IMPACT] | | | | |
| **1.4.5** | [DELETED, INSUFFICIENT IMPACT] | | | | |
| **1.4.6** | [ADDED] Verify that the application documentation defines controls which use changes to a user's regular environmental and contextual attributes (such as time of day, location, IP address, or device) to make security decisions, including those pertaining to authentication and authorization. These changes should be detected both when the user tries to start a new session and also in the course of an existing session. | | | ✓ | |
| **1.4.7** | [ADDED] Verify that access control documentation defines the rules for access control decision-making, specifying user and subject attributes, resource attributes, and relevant environmental factors involved in the process. | ✓ | ✓ | ✓ | |

## V4.1 General Access Control Design

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.1.1** | [MODIFIED] Verify that the application enforces access control rules at a trusted service layer and doesn't rely on controls which an untrusted user could manipulate such as client-side JavaScript. | ✓ | ✓ | ✓ | 602 |
| **4.1.2** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **4.1.3** | [MODIFIED] Verify that the application ensures that function level access is restricted to consumers with explicit permissions. | ✓ | ✓ | ✓ | 285 |
| **4.1.4** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **4.1.5** | [GRAMMAR] Verify that access controls fail securely by denying access, including when an exception occurs. | ✓ | ✓ | ✓ | 285 |
| **4.1.6** | [ADDED] Verify that changes to values on which access control decisions are made, are applied immediately. Where changes cannot be applied immediately, (such as when relying on data in cryptographically secured tokens), there must be mitigating controls to alert when a user performs an action when they should no longer be able to do so, and revert the change. Note that this would be unable to mitigate information leakage. | | ✓ | ✓ | |

## V4.2 Operation Level Access Control

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.2.1** | [MODIFIED] Verify that the application ensures that data specific access is restricted to consumers with explicit permissions to specific data items to mitigate insecure direct object reference (IDOR) and broken object level authorization (BOLA). | ✓ | ✓ | ✓ | 639 |
| **4.2.2** | [MOVED TO 50.3.1] | | | | |
| **4.2.3** | [ADDED] Verify that the application ensures that field level access is restricted to consumers with explicit permissions to specific fields to mitigate broken object property level authorization (BOPLA). | | ✓ | ✓ | 283 |
| **4.2.4** | [ADDED] Verify that multi-tenant applications use cross-tenant controls to ensure user operations will never affect tenants with which they do not have permissions to interact. | ✓ | ✓ | ✓ | 283 |
| **4.2.5** | [ADDED] Verify that access to an object is based on the originating subject's (e.g. user's) permissions, not on the permissions of any intermediary or service acting on their behalf. For example, if a user calls a web service using a signed token for authentication, and the service then requests data from a different service, the second service should use the user's signed token, rather than a machine-to-machine token from the first service, to make permission decisions. | | | ✓ | 441 |

## V4.3 Other Access Control Considerations

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.3.1** | [MODIFIED, LEVEL L1 > L3] Verify that access to administrative interfaces incorporates multiple layers of security, including continuous user identity verification, device security posture assessment, and contextual risk analysis, ensuring that network location or trusted endpoints are not the sole factors for authorization even though they reduce likelihood. | | | ✓ | 419 |
| **4.3.2** | [SPLIT TO 14.3.4, 14.3.5] | | | | |
| **4.3.3** | [MODIFIED] Verify that, if the application allows changing highly sensitive configurations around passwords or connection parameters for integrations with databases and third-party systems, they are protected by extra controls such as re-authentication or multi-user approval.| | ✓ | ✓ | 732 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Access Control](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
