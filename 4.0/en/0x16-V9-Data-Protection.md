# V9: Data Protection Verification Requirements

## Control Objective

There are three key elements to sound data protection: Confidentiality, Integrity and Availability (CIA). This standard assumes that data protection is enforced on a trusted system, such as a server, which has been hardened and has sufficient protections.

Applications have to assume that all user devices are compromised in some way. Where an application transmits or stores sensitive information on insecure devices, such as shared computers, phones and tablets, the application is responsible for ensuring data stored on these devices is encrypted and cannot be easily illicitly obtained, altered or disclosed.

Ensure that a verified application satisfies the following high level data protection requirements:

* Confidentiality: Data should be protected from unauthorized observation or disclosure both in transit and when stored.
* Integrity: Data should be protected being maliciously created, altered or deleted by unauthorized attackers.
* Availability: Data should be available to authorized users as required.

## Security Verification Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **9.2** | Identify all sensitive data created and processed by the application and ensure that a policy is in place on how to deal with sensitive data. | ✓ | ✓ | ✓ | 200 | tbd | 
| **9.3** | Verify that sensitive data is sent to the server in the HTTP/S message body or headers and that query string parameters from any HTTP verb do not contain sensitive data. | ✓ | ✓ | ✓ | 319 | tbd | 
| **9.4** | Verify that the application sets sufficient anti-caching headers so that sensitive data is not cached in modern browsers. | ✓ | ✓ | ✓ | 525 | tbd | 
| **9.5** | Verify that the application protects sensitive data from being cached in server components such as load balancers and application caches. | ✓ | ✓ | ✓ | 524 | tbd | 
| **9.6** | Verify that all cached or temporary copies of sensitive data stored on the server are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data. |  | ✓ | ✓ | 524 | tbd | 
| **9.7** | Verify that users have a method to remove or export their data on demand. | ✓ | ✓ | ✓ | 212 | tbd | 
| **9.8** | Verify the application minimizes the number of parameters in a request, such as hidden fields, Ajax variables, cookies and header values. |  | ✓ | ✓ | 233 | tbd | 
| **9.9** | Verify the application has the ability to detect and alert on abnormal numbers of requests, such as by IP, user, total per hour or day, or whatever makes sense for the application.  |  | ✓ | ✓ | 770 | tbd |
| **9.10** | Verify that data stored in client side storage (such as HTML5 local storage, session storage, IndexedDB, regular cookies or Flash cookies) does not contain sensitive data or PII. | ✓ | ✓ | ✓ | 922 | tbd |
| **9.11** | Verify accessing sensitive data is logged, if the data is collected under relevant data protection directives or where logging of access is required. |  | ✓ | ✓ | 532 | tbd | 
| **9.12** | Verify that sensitive information maintained in memory is overwritten with zeros as soon as it is no longer required, to mitigate memory dumping attacks. |  | ✓ | ✓ | 401 | tbd |
| **9.13** | Verify that sensitive or private information that is required to be encrypted, is encrypted using approved algorithms that provide both confidentiality and integrity. | ✓ | ✓ | ✓ | 327 | tbd |
| **9.14** | Verify that users are provided clear language regarding collection and use of supplied personal information and that users have provided opt-in consent for the use of that data before it is used in any way. | ✓ | ✓ | ✓ | 285 | tbd | 
| **9.15** | Verify that authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated. |  | ✓ | ✓ | 922 | tbd | 
| **9.16** | Verify that regular backups of important data are performed and that restore tests are performed. || ✓ | ✓ | 19 | tbd | 
| **9.17** | Verify that backups are stored securely to prevent the data being stolen or corrupted. || ✓ | ✓ | 19 | tbd | 

When considering data protection, a primary consideration should be around bulk extraction or modification or excessive usage. For example, many social media systems only allow users to add 100 new friends per day, but which system these requests came from is not important. A banking platform might wish to block more than 5 transactions per hour transferring more than 1000 euro of funds to external institutions. Each system's requirements are likely to be very different, so deciding on "abnormal" must consider the threat model and business risk. The important criteria is the ability to detect, deter, or preferably block such abnormal bulk actions.

## References

For more information, see also:

* [Consider using Security Headers website to check security and anti-caching headers](https://securityheaders.io)
* [OWASP Secure Headers project](https://www.owasp.org/index.php/OWASP_Secure_Headers_Project)
* [User Privacy Protection Cheat Sheet](https://www.owasp.org/index.php/User_Privacy_Protection_Cheat_Sheet)
