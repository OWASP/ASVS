# V8 Authorization

## Control Objective

Authorization ensures that access is granted only to permitted consumers (users, servers, and other clients). To enforce the Principle of Least Privilege (POLP), verified applications must meet the following high-level requirements:

* Document authorization rules, including decision-making factors and environmental contexts.
* Consumers should have access only to resources permitted by their defined entitlements.

## V8.1 Authorization Documentation

Comprehensive authorization documentation is essential to ensure that security decisions are consistently applied, auditable, and aligned with organizational policies, reducing the risk of unauthorized access by making security requirements clear and actionable for developers, administrators, and testers.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.4.7** | [ADDED] Verify that authorization documentation defines rules for restricting function-level and data-specific access based on consumer permissions and resource attributes. | 1 | v5.0.be-1.4.7 |
| **1.4.8** | [ADDED] Verify that authorization documentation defines rules for field-level access restrictions based on consumer permissions and resource attributes. | 2 | v5.0.be-1.4.8 |
| **1.4.6** | [ADDED] Verify that authorization documentation defines controls that incorporate changes to a consumer's environmental and contextual attributes (such as time of day, location, IP address, or device) to make security decisions, including those pertaining to authentication and authorization. These changes should be detected both when the consumer tries to start a new session or during an existing session. | 3 | v5.0.be-1.4.6 |
| **1.4.9** | [ADDED] Verify that authorization documentation considers environmental and contextual factors in decision-making, in addition to function-level, data-specific, and field-level authorization. | 3 | v5.0.be-1.4.9 |

## V8.2 General Authorization Design

Implementing granular authorization controls at the function, data, and field levels will ensure that consumers can only access what has been explicitly granted to them.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **4.1.3** | [MODIFIED, COVERS 4.1.2] Verify that the application ensures that function-level access is restricted to consumers with explicit permissions. | 1 | v5.0.be-4.1.3 |
| **4.1.6** | [MODIFIED, MOVED FROM 4.2.1, COVERS 13.1.4] Verify that the application ensures that data-specific access is restricted to consumers with explicit permissions to specific data items to mitigate insecure direct object reference (IDOR) and broken object level authorization (BOLA). | 1 | v5.0.be-4.1.6 |
| **4.1.7** | [ADDED] Verify that the application ensures that field-level access is restricted to consumers with explicit permissions to specific fields to mitigate broken object property level authorization (BOPLA). | 2 | v5.0.be-4.1.7 |
| **4.1.8** | [ADDED] Verify that adaptive security controls related to authentication and authorization decisions based on a consumer's environmental and contextual attributes (such as time of day, location, IP address, or device) are implemented as defined in authorization documentation. | 3 | v5.0.be-4.1.8 |

## V8.3 Operation Level Authorization

The immediate application of authorization changes in the appropriate tier of an application's architecture is crucial to preventing unauthorized actions, especially in dynamic environments.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **4.2.3** | [MODIFIED, MOVED FROM 4.1.1, COVERS 1.4.1, 14.5.2] Verify that the application enforces authorization rules at a trusted service layer and doesn't rely on controls that an untrusted consumer could manipulate, such as client-side JavaScript. | 1 | v5.0.be-4.2.3 |
| **4.2.4** | [ADDED] Verify that changes to values on which authorization decisions are made are applied immediately. Where changes cannot be applied immediately, (such as when relying on data in self-contained tokens), there must be mitigating controls to alert when a consumer performs an action when they should no longer be able to do so and revert the change. Note that this would be unable to mitigate information leakage. | 3 | v5.0.be-4.2.4 |
| **4.2.5** | [ADDED] Verify that access to an object is based on the originating subject's (e.g. consumer's) permissions, not on the permissions of any intermediary or service acting on their behalf. For example, if a consumer calls a web service using a self-contained token for authentication, and the service then requests data from a different service, the second service should use the consumer's token, rather than a machine-to-machine token from the first service, to make permission decisions. | 3 | v5.0.be-4.2.5 |

## V8.4 Other Authorization Considerations

Additional considerations for authorization, particularly for administrative interfaces and multi-tenant environments, will help prevent unauthorized access.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **4.3.4** | [ADDED] Verify that multi-tenant applications use cross-tenant controls to ensure consumer operations will never affect tenants with which they do not have permissions to interact. | 2 | v5.0.be-4.3.4 |
| **4.3.1** | [MODIFIED, LEVEL L1 > L3] Verify that access to administrative interfaces incorporates multiple layers of security, including continuous consumer identity verification, device security posture assessment, and contextual risk analysis, ensuring that network location or trusted endpoints are not the sole factors for authorization even though they may reduce the likelihood of unauthorized access. | 3 | v5.0.be-4.3.1 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
