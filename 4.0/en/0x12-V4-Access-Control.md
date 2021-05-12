# V4 Access Control

## Control Objective

Authorization is the concept of allowing access to resources only to those permitted to use them. Ensure that a verified application satisfies the following high level requirements:

* Persons accessing resources hold valid credentials to do so.
* Users are associated with a well-defined set of roles and privileges.
* Role and permission metadata is protected from replay or tampering.

## Security Verification Requirements

## V4.1 General Access Control Design

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.1.1** | Verify that the application enforces access control rules on a trusted service layer, especially if client-side access control is present and could be bypassed. | ✓ | ✓ | ✓ | 602 |
| **4.1.2** | Verify that all user and data attributes and policy information used by access controls cannot be manipulated by end users unless specifically authorized. | ✓ | ✓ | ✓ | 639 |
| **4.1.3** | Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |
| **4.1.4** | Verify that the principle of deny by default exists whereby new users/roles start with minimal or no permissions and users/roles do not receive access to new features until access is explicitly assigned. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 276 |
| **4.1.5** | Verify that access controls fail securely including when an exception occurs. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |

## V4.2 Operation Level Access Control

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.2.1** | Verify that sensitive data and APIs are protected against Insecure Direct Object Reference (IDOR) attacks targeting creation, reading, updating and deletion of records, such as creating or updating someone else's record, viewing everyone's records, or deleting all records. | ✓ | ✓ | ✓ | 639 |
| **4.2.2** | [MODIFIED, MERGED 13.2.3] Verify that the application defends against Cross-Site Request Forgery (CSRF) attacks to protect authenticated or sensitive public functionality using the developemnt framework's built-in anti-CSRF functionality or CSRF tokens plus additional defense in depth measures. | ✓ | ✓ | ✓ | 352 |
| **4.2.3** | [ADDED] Verify that messages received by the postMessage interface are discarded if the origin of the message is not trusted, or if the syntax of the message is invalid. | | ✓ | ✓ | 346 |

## V4.3 Other Access Control Considerations

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.3.1** | Verify administrative interfaces use appropriate multi-factor authentication to prevent unauthorized use. | ✓ | ✓ | ✓ | 419 |
| **4.3.2** | [SPLIT TO 14.3.4, 14.3.5] | | | | |
| **4.3.3** | Verify the application has additional authorization (such as step up or adaptive authentication) for lower value systems, and / or segregation of duties for high value applications to enforce anti-fraud controls as per the risk of application and past fraud. | | ✓ | ✓ | 732 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Access Control](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
* [OWASP CSRF Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [OWASP REST Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
