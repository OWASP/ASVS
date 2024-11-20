# V4 Access Control

## Control Objective

Authorization is the process of allowing access only to permitted consumers (users, servers and other clients). Ensure that a verified application satisfies the following high-level requirements:

* Document access control rules, including decision-making factors and environmental contexts.
* Consumers should have access only to resources permitted by their defined entitlements.

## V1.4 Access Control Documentation

Comprehensive access control documentation is essential to ensure that security decisions are consistently applied, auditable, and aligned with organizational policies, reducing the risk of unauthorized access by making security requirements clear and actionable for developers, administrators, and testers.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.4.1** | [DELETED, DUPLICATE OF 4.1.1] | | | | |
| **1.4.2** | [DELETED] | | | | |
| **1.4.3** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **1.4.4** | [DELETED, INSUFFICIENT IMPACT] | | | | |
| **1.4.5** | [DELETED, INSUFFICIENT IMPACT] | | | | |
| **1.4.6** | [ADDED] Verify that access control documentation defines controls that incorporate changes to a consumers environmental and contextual attributes (such as time of day, location, IP address, or device) to make security decisions, including those pertaining to authentication and authorization. These changes should be detected both when the consumer tries to start a new session or during an existing session. | | | ✓ | |
| **1.4.7** | [ADDED] Verify that access control documentation defines explicit rules for restricting function-level, data-specific, and field-level access based on consumer permissions, specifying relevant consumer and resource attributes, as well as environmental factors involved in decision-making. | ✓ | ✓ | ✓ | |

## V4.1 General Access Control Design

Implementing granular access controls at the function, data, and field levels will ensure that consumers can only access what has been explicitly granted to them.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.1.1** | [MOVED TO 4.2.3] | | | | |
| **4.1.2** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **4.1.3** | [MODIFIED] Verify that the application ensures that function-level access is restricted to consumers with explicit permissions. | ✓ | ✓ | ✓ | 285 |
| **4.1.4** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **4.1.5** | [MOVED TO 7.4.5] | | | | |
| **4.1.6** | [MODIFIED, MOVED FROM 4.2.1] Verify that the application ensures that data-specific access is restricted to consumers with explicit permissions to specific data items to mitigate insecure direct object reference (IDOR) and broken object level authorization (BOLA). | ✓ | ✓ | ✓ | 639 |
| **4.1.7** | [ADDED] Verify that the application ensures that field-level access is restricted to consumers with explicit permissions to specific fields to mitigate broken object property level authorization (BOPLA). | | ✓ | ✓ | 283 |
| **4.1.8** | [ADDED] Verify that adaptive security controls related to authentication and authorization decisions based on a consumers environmental and contextual attributes (such as time of day, location, IP address, or device) are implemented as defined in access control documentation. | | ✓ | ✓ | |

## V4.2 Operation Level Access Control

The immediate application of access control changes in the appropriate tier of an application's architecture is crucial to preventing unauthorized actions, especially in dynamic environments.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.2.1** | [MOVED TO 4.1.6] | | | | |
| **4.2.2** | [MOVED TO 50.3.1] | | | | |
| **4.2.3** | [MODIFIED, MOVED FROM 4.1.1] Verify that the application enforces access control rules at a trusted service layer and doesn't rely on controls that an untrusted consumer could manipulate, such as client-side JavaScript. | ✓ | ✓ | ✓ | 602 |
| **4.2.4** | [ADDED] Verify that changes to values on which access control decisions are made are applied immediately. Where changes cannot be applied immediately, (such as when relying on data in cryptographically secured tokens), there must be mitigating controls to alert when a consumer performs an action when they should no longer be able to do so and revert the change. Note that this would be unable to mitigate information leakage. | | ✓ | ✓ | |
| **4.2.5** | [ADDED] Verify that access to an object is based on the originating subject's (e.g. consumer's) permissions, not on the permissions of any intermediary or service acting on their behalf. For example, if a consumer calls a web service using a signed token for authentication, and the service then requests data from a different service, the second service should use the consumer's signed token, rather than a machine-to-machine token from the first service, to make permission decisions. | | | ✓ | 441 |
| **4.2.6** | [ADDED] Verify that the user can review, modify and revoke granted consents at any time. | | ✓ | ✓ | |

## V4.3 Other Access Control Considerations

Additional considerations for access control, particularly for administrative interfaces and multi-tenant environments, will help prevent unauthorized access.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.3.1** | [MODIFIED, LEVEL L1 > L3] Verify that access to administrative interfaces incorporates multiple layers of security, including continuous consumer identity verification, device security posture assessment, and contextual risk analysis, ensuring that network location or trusted endpoints are not the sole factors for authorization even though they may reduce the likelihood of unauthorized access. | | | ✓ | 419 |
| **4.3.2** | [SPLIT TO 14.3.4, 14.3.5] | | | | |
| **4.3.3** | [MOVED TO 14.7.3] | | | | |
| **4.3.4** | [ADDED] Verify that multi-tenant applications use cross-tenant controls to ensure consumer operations will never affect tenants with which they do not have permissions to interact. | ✓ | ✓ | ✓ | 283 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Access Control](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
