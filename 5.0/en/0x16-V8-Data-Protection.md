# V8 Data Protection

## Control Objective

There are three key elements to sound data protection: Confidentiality, Integrity and Availability (CIA). This standard assumes that data protection is enforced on a trusted system, such as a server, which has been hardened and has sufficient protections.

Applications have to assume that all user devices are compromised in some way. Where an application transmits or stores sensitive information on insecure devices, such as shared computers, phones and tablets, the application is responsible for ensuring data stored on these devices is encrypted and cannot be easily illicitly obtained, altered or disclosed.

Ensure that a verified application satisfies the following high-level data protection requirements:

* Confidentiality: Data should be protected from unauthorized observation or disclosure both in transit and when stored.
* Integrity: Data should be protected from being maliciously created, altered or deleted by unauthorized attackers.
* Availability: Data should be available to authorized users as required.

## V1.8 Data Protection and Privacy Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.8.1** | [MODIFIED, MERGED FROM 8.3.4, 6.1.1, 6.1.2] Verify that all sensitive data created and processed by the application has been identified and classified into protection levels, and ensure that a policy is in place on how to deal with sensitive data. Note that this includes sensitive data that is being encoded in a recoverable form such as Base64 and JWT. Protection levels need to take into account any data protection and privacy regulations and standards which the application is required to comply with. | | ✓ | ✓ | 213 |
| **1.8.2** | [MODIFIED, SPLIT TO 8.1.9] Verify that all protection levels have a documented set of protection requirements. This should include (but not be limited to) requirements related to general encryption, integrity verification, retention, how the data should be logged, access controls around sensitive data in logs, database-level encryption, privacy and privacy-enhancing technologies to be used, and other confidentiality requirements. | | ✓ | ✓ | |

## V8.1 General Data Protection

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **8.1.1** | [MODIFIED, MERGED FROM 8.1.2] Verify that the application prevents sensitive data from being cached in server components such as load balancers and application caches or ensures that the data is securely purged after use. | | ✓ | ✓ | 524 |
| **8.1.2** | [DELETED, MERGED TO 8.1.1] | | | | |
| **8.1.3** | [DELETED, INSUFFICIENT IMPACT] | | | | |
| **8.1.4** | Verify the application can detect and alert on abnormal numbers of requests, such as by IP, user, total per hour or day, or whatever makes sense for the application. | | ✓ | ✓ | 770 |
| **8.1.5** | [DELETED, NOT IN SCOPE] | | | | |
| **8.1.6** | [DELETED, NOT IN SCOPE] | | | | |
| **8.1.7** | [ADDED] Verify that caching mechanisms are configured to only cache responses which have the correct content type and do not contain sensitive, dynamic content. The web server should return a 404 or 302 response when an non-existent file is accessed rather than returning a different, valid file. This should prevent Web Cache Deception attacks. | | ✓ | ✓ | 444 |
| **8.1.8** | [ADDED] Verify that defined sensitive data is not sent to untrusted parties (e.g. user trackers) to prevent unwanted collection of data outside of the application's control. | | ✓ | ✓ | 200 |
| **8.1.9** | [ADDED, SPLIT FROM 1.8.2] Verify that controls around sensitive data are implemented as defined in the documentation for the specific data's protection level. | | ✓ | ✓ | |
| **8.1.10** | [ADDED] Verify that the application only returns the minimum required sensitive data for the application's functionality. For example, only returning some of the digits of a credit card number and not the full number. If the full data is absolutely required, it should be masked in the user interface unless the user specifically views it. | | | ✓ | |

## V8.2 Client-side Data Protection

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **8.2.1** | [MODIFIED] Verify that the application sets sufficient anti-caching HTTP response header fields (i.e. Cache-Control: no-store) so that sensitive data is not cached in browsers. | ✓ | ✓ | ✓ | 525 |
| **8.2.2** | [MODIFIED, MERGED FROM 3.2.3] Verify that data stored in browser storage (such as localStorage, sessionStorage, IndexedDB, or cookies) does not contain sensitive data, with the exception of session identifiers. | ✓ | ✓ | ✓ | 922 |
| **8.2.3** | [MODIFIED] Verify that authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated. The "Clear-Site-Data header" may be able to help with this but the client-side should also be able to clear up if the server connection is lost. | ✓ | ✓ | ✓ | 922 |

## V8.3 Sensitive Private Data

This section helps protect sensitive data from being created, read, updated, or deleted without authorization, particularly in bulk quantities.

Compliance with this section implies compliance with V4 Access Control, and in particular V4.2. For example, to protect against unauthorized updates or disclosure of sensitive personal information requires adherence to V4.2.1. Please comply with this section and V4 for full coverage.

Note: Privacy regulations and laws, such as the Australian Privacy Principles APP-11 or GDPR, directly affect how applications must approach the implementation of storage, use, and transmission of sensitive personal information. This ranges from severe penalties to simple advice. Please consult your local laws and regulations, and consult a qualified privacy specialist or lawyer as required.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **8.3.1** | [MODIFIED, MERGED FROM 3.1.1, 13.1.3] Verify that sensitive data is only sent to the server in the HTTP message body or header fields and that the URL and query string do not contain sensitive information, such as an API key or session token. | ✓ | ✓ | ✓ | 598 |
| **8.3.2** | [DELETED, NOT IN SCOPE] | | | | |
| **8.3.3** | [DELETED, NOT IN SCOPE] | | | | |
| **8.3.4** | [DELETED, MERGED TO 1.8.1] | | | | |
| **8.3.5** | [MOVED TO 7.2.7] | | | | |
| **8.3.6** | [DELETED, NOT PRACTICAL] | | | | |
| **8.3.7** | [DELETED, DUPLICATE OF 1.8.2] | | | | |
| **8.3.8** | [LEVEL L2 > L3] Verify that sensitive personal information is subject to data retention classification, such that old or out of date data is deleted automatically, on a schedule, or as the situation requires. | | | ✓ | |
| **8.3.9** | [ADDED] Verify that sensitive information is removed from the metadata of user-submitted files unless storage is consented to by the user. | | ✓ | ✓ | 212 |

When considering data protection, a primary consideration should be around bulk extraction or modification or excessive usage. For example, many social media systems only allow users to add 100 new friends per day, but which system these requests came from is not important. A banking platform might wish to block more than 5 transactions per hour transferring more than 1000 euro of funds to external institutions. Each system's requirements are likely to be very different, so deciding on "abnormal" must consider the threat model and business risk. Important criteria are the ability to detect, deter, or preferably block such abnormal bulk actions.

## References

For more information, see also:

* [Consider using the Security Headers website to check security and anti-caching header fields](https://securityheaders.com/)
* [Documentation about anti-caching headers by Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [Australian Privacy Principle 11 - Security of personal information](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-11-app-11-security-of-personal-information)
* [European Union General Data Protection Regulation (GDPR) overview](https://www.edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://www.edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
* [Information on the "Clear-Site-Data" header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data)
* [White paper on Web Cache Deception](https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack-wp.pdf)
