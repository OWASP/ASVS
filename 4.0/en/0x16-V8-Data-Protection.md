# V8: Data Protection Verification Requirements

## Control Objective

There are three key elements to sound data protection: Confidentiality, Integrity and Availability (CIA). This standard assumes that data protection is enforced on a trusted system, such as a server, which has been hardened and has sufficient protections.

Applications have to assume that all user devices are compromised in some way. Where an application transmits or stores sensitive information on insecure devices, such as shared computers, phones and tablets, the application is responsible for ensuring data stored on these devices is encrypted and cannot be easily illicitly obtained, altered or disclosed.

Ensure that a verified application satisfies the following high level data protection requirements:

* Confidentiality: Data should be protected from unauthorized observation or disclosure both in transit and when stored.
* Integrity: Data should be protected being maliciously created, altered or deleted by unauthorized attackers.
* Availability: Data should be available to authorized users as required.

## V8.1 General Data Protection

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.1.1** | Verify the application protects sensitive data from being cached in server components such as load balancers and application caches. | | ✓ | ✓ | 524 |
| **8.1.2** | Verify that all cached or temporary copies of sensitive data stored on the server are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data. | | ✓ | ✓ | 524 |
| **8.1.3** | Verify the application minimizes the number of parameters in a request, such as hidden fields, Ajax variables, cookies and header values. | | ✓ | ✓ | 233 |
| **8.1.4** | Verify the application has the ability to detect and alert on abnormal numbers of requests, such as by IP, user, total per hour or day, or whatever makes sense for the application. | | ✓ | ✓ | 770 |
| **8.1.5** | Verify that regular backups of important data are performed and that test restoration of data is performed. | | | ✓ | 19 |
| **8.1.6** | Verify that backups are stored securely to prevent the data being stolen or corrupted. | | | ✓ | 19 |

## V8.2 Client-side Data Protection

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.2.1** | Verify the application sets sufficient anti-caching headers so that sensitive data is not cached in modern browsers. | ✓ | ✓ | ✓ | 525 |
| **8.2.2** | Verify that data stored in client side storage (such as HTML5 local storage, session storage, IndexedDB, regular cookies or Flash cookies) does not contain sensitive data or PII. | ✓ | ✓ | ✓ | 922 |
| **8.2.3** | Verify that authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated. | ✓ | ✓ | ✓ | 922 |

## V8.3 Sensitive Private Data

This sections helps protect sensitive data from being created, read, updated, or deleted without authorization, particularly in bulk quantities.

Compliance with this section implies compliance with V4 Access Control, and in particular V4.2. For example, to protect against unauthorized updates or disclosure of sensitive personal information requires adherance to V4.2.1. Please comply with this section and V4 for full coverage. 

Note: Privacy regulations and laws, such as the Australian Privacy Principles APP-11 or GDPR, directly affect how applications must approach the implementation of storage, use, and transmission of sensitive personal information. This ranges from severe penalties to simple advice. Please consult your local laws and regulations, and consult a qualified privacy specialist or lawyer as required.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.3.1** | Verify that sensitive data is sent to the server in the HTTP message body or headers, and that query string parameters from any HTTP verb do not contain sensitive data. | ✓ | ✓ | ✓ | 319 |
| **8.3.2** | Verify that users have a method to remove or export their data on demand. | ✓ | ✓ | ✓ | 212 |
| **8.3.3** | Verify that users are provided clear language regarding collection and use of supplied personal information and that users have provided opt-in consent for the use of that data before it is used in any way. | ✓ | ✓ | ✓ | 285 |
| **8.3.4** | Verify that all sensitive data created and processed by the application has been identified, and ensure that a policy is in place on how to deal with sensitive data. |  | ✓ | ✓ | 200 |
| **8.3.5** | Verify accessing sensitive data is audited (without logging the sensitive data itself), if the data is collected under relevant data protection directives or where logging of access is required. | | ✓ | ✓ | 532 |
| **8.3.6** | Verify that sensitive information contained in memory is overwritten as soon as it is no longer required to mitigate memory dumping attacks, using zeroes or random data. | | ✓ | ✓ | 226 |
| **8.3.7** | Verify that sensitive or private information that is required to be encrypted, is encrypted using approved algorithms that provide both confidentiality and integrity. | | ✓ | ✓ | 327 |
| **8.3.8** | Verify that sensitive personal information is subject to data retention classification, such that old or out of date data is deleted automatically, on a schedule, or as the situation requires. | | ✓ | ✓ | 285 |

When considering data protection, a primary consideration should be around bulk extraction or modification or excessive usage. For example, many social media systems only allow users to add 100 new friends per day, but which system these requests came from is not important. A banking platform might wish to block more than 5 transactions per hour transferring more than 1000 euro of funds to external institutions. Each system's requirements are likely to be very different, so deciding on "abnormal" must consider the threat model and business risk. The important criteria is the ability to detect, deter, or preferably block such abnormal bulk actions.

## References

For more information, see also:

* [Consider using Security Headers website to check security and anti-caching headers](https://securityheaders.io)
* [OWASP Secure Headers project](https://www.owasp.org/index.php/OWASP_Secure_Headers_Project)
* [User Privacy Protection Cheat Sheet](https://www.owasp.org/index.php/User_Privacy_Protection_Cheat_Sheet)
