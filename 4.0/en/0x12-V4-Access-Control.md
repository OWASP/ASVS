# V4: Access Control Verification Requirements

## Control Objective

Authorization is the concept of allowing access to resources only to those permitted to use them. Ensure that a verified application satisfies the following high level requirements:

* Persons accessing resources hold valid credentials to do so.
* Users are associated with a well-defined set of roles and privileges.
* Role and permission metadata is protected from replay or tampering.

## Security Verification Requirements

### 4.1 General Access Control design

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **4.1.1** | Verify that the chosen access control solution is flexible enough to meet the application's needs.  | ✓ | ✓ | ✓ | 4.0 |
| **4.1.2** | Verify that access control policy is enforced server-side.  | ✓ | ✓ | ✓ | 4.0 |
| **4.1.3** | Verify that the same access control rules implied by the presentation layer are enforced on the server side. | ✓ | ✓ | ✓ | 1.0 |
| **4.1.4** | Verify that all user and data attributes and policy information used by access controls cannot be manipulated by end users unless specifically authorized. | ✓ | ✓ | ✓ | 1.0 |
| **4.1.5** | Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege. | ✓ | ✓ | ✓ | 1.0 |
| **4.1.6** | Verify that the principle of deny by default exists whereby new users/roles start with minimal or no permissions and users/roles do not receive access to new features until access is explicitly assigned.  | ✓ | ✓ | ✓ | 4.0 |
| **4.1.7** | Verify that access controls fail securely including when an exception occurs. | ✓ | ✓ | ✓ | 1.0 |
| **4.1.8** | Verify that all access control decisions can be logged and all failed decisions are logged. | ✓ | ✓ | ✓ | 2.0 |

### 4.2 Operation Level Access Control

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **4.2.1** | Verify that there is only one vetted access control mechanism for protecting access to protected data and resources which all requests must go through. This should mean that hard coded access control checks are not required throughout the application. | ✓ | ✓ | ✓ | 4.0 |
| **4.2.2** | Verify that attribute or feature-based access control is used whereby the code checks the user's authorization for a feature/data item rather than just their role. Permissions should still be allocated using roles. | ✓ | ✓ | ✓ | 4.0 |
| **4.2.3** | Verify that sensitive data and APIs are protected against direct object attacks targeting creation, reading, updating and deletion of records. | ✓ | ✓ | ✓ | 4.0 |
| **4.2.4** | Verify that the application or framework enforces a strong anti-CSRF mechanism to protect any sensitive functionality. | ✓ | ✓ | ✓ | 4.0 |
| **4.2.5** | Verify that data-level access control is implemented such that access to individual records can be managed in a centralized and standard way. | ✓ | ✓ | ✓ | 4.0 |

### 4.3 Other Access Control Considerations

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **4.3.1** | Verify administrative interfaces use appropriate multi-factor authentication to prevent unauthorized use. | ✓ | ✓ | ✓ | 4.0 |
| **4.3.2** | Verify that directory browsing is disabled unless deliberately desired. Additionally, applications should not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS_Store, .git or .svn folders. | ✓ | ✓ | ✓ | 1.0 |
| **4.3.3** | Verify the application has additional authorization (such as step up or adaptive authentication) for lower value systems, and / or segregation of duties for high value applications to enforce anti-fraud controls as per the risk of application and past fraud. |  | ✓ | ✓ | 3.0 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Authorization](https://www.owasp.org/index.php/Testing_for_Authorization)
* [OWASP Cheat Sheet: Access Control](https://www.owasp.org/index.php/Access_Control_Cheat_Sheet)
* [OWASP CSRF Cheat Sheet](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)_Prevention_Cheat_Sheet)
* [OWASP REST Cheat Sheet](https://www.owasp.org/index.php/REST_Security_Cheat_Sheet)
