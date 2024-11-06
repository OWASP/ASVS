# V4 Access Control

## Control Objective

Authorization is the concept of allowing access to resources only to those permitted to use them. Ensure that a verified application satisfies the following high-level requirements:

* Persons accessing resources hold valid credentials to do so.
* Users are associated with a well-defined set of entitlements.
* Access control policy metadata is protected from replay or tampering.

Access control deficiencies are unlikely to be discovered using generic automated testing tools. Verifying the requirements in this section will either require manual or manual assisted testing or alternatively a robust series of automated end-to-end access control tests which validate the effectiveness of the access controls under various scenarios. Integrating these tests into the continuous integration/continuous deployment (CI/CD) pipeline will make it easier to validate these requirements on an ongoing basis.

## V4.1 General Access Control Design

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.1.1** | [MODIFIED] Verify that the application enforces access control rules at a trusted service layer and doesn't rely on controls which an untrusted user could manipulate such as client-side JavaScript. | ✓ | ✓ | ✓ | 602 |
| **4.1.2** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **4.1.3** | Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege. | ✓ | ✓ | ✓ | 285 |
| **4.1.4** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **4.1.5** | [GRAMMAR] Verify that access controls fail securely by denying access, including when an exception occurs. | ✓ | ✓ | ✓ | 285 |
| **4.1.6** | [ADDED] Verify that changes to values on which access control decisions are made, are applied immediately. Where changes cannot be applied immediately, (such as when relying on data in cryptographically secured tokens), there must be mitigating controls to alert when a user performs an action when they should no longer be able to do so, and revert the change. Note that this would be unable to mitigate information leakage. | | ✓ | ✓ | |

## V4.2 Operation Level Access Control

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.2.1** | Verify that sensitive data and APIs are protected against Insecure Direct Object Reference (IDOR) attacks targeting creation, reading, updating and deletion of records, such as creating or updating someone else's record, viewing everyone's records, or deleting all records. | ✓ | ✓ | ✓ | 639 |
| **4.2.2** | [MOVED TO 50.3.1] | | | | |
| **4.2.3** | [ADDED] Verify that multi-tenant applications use cross-tenant controls to ensure user operations will never affect tenants with which they do not have permissions to interact. | ✓ | ✓ | ✓ | 283 |
| **4.2.4** | [ADDED] Verify that access to an object is based on the originating subject's (e.g. user's) permissions, not on the permissions of any intermediary or service acting on their behalf. For example, if a user calls a web service using a signed token for authentication, and the service then requests data from a different service, the second service should use the user's signed token, rather than a machine-to-machine token from the first service, to make permission decisions. | | | ✓ | 441 |

## V4.3 Other Access Control Considerations

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.3.1** | [MODIFIED] Verify administrative interfaces can only be logically accessed from trusted endpoints or locations. For example, restricting access to bastion or jump hosts, trusted admin workstations or endpoints (e.g., device authentication), administrative LANs, etc. | ✓ | ✓ | ✓ | 419 |
| **4.3.2** | [SPLIT TO 14.3.4, 14.3.5] | | | | |
| **4.3.3** | [MODIFIED] Verify that, if the application allows changing highly sensitive configurations around passwords or connection parameters for integrations with databases and third-party systems, they are protected by extra controls such as re-authentication or multi-user approval. | | ✓ | ✓ | 732 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Access Control](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
