# V5: Input Validation and Output Encoding Verification Requirements

## Control Objective

The most common web application security weakness is the failure to properly validate input coming from the client or from the environment before using it. This weakness leads to almost all of the major vulnerabilities in web applications, such as cross site scripting, SQL injection, interpreter injection, locale/Unicode attacks, file system attacks, and buffer overflows.

Ensure that a verified application satisfies the following high level requirements:

* All input is validated to be correct and fit for the intended purpose.
* Data from an external entity or client should never be trusted and should be handled accordingly.


## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **5.3** | Verify that server side input validation failures result in request rejection and are logged. | ✓ | ✓ | ✓ | 1.0 |
| **5.5** | Verify that input validation routines are enforced on the server side. | ✓ | ✓ | ✓ | 1.0 |
| **5.6** | Verify that a centralized input validation control mechanism is used by the application. | ✓ | ✓ | ✓ | 1.0 |
| **5.10** | Verify that all database queries are protected by the use of parameterized queries or proper ORM usage to avoid SQL injection. | ✓ | ✓ | ✓ | 2.0 |
| **5.11** | Verify that the application is not susceptible to LDAP Injection, or that security controls prevent LDAP Injection. | ✓ | ✓ | ✓ | 2.0 |
| **5.12** | Verify that the application is not susceptible to OS Command Injection, or that security controls prevent OS Command Injection. | ✓ | ✓ | ✓ | 2.0 |
| **5.13** | Verify that the application is not susceptible to Remote File Inclusion (RFI) or Local File Inclusion (LFI) when content is used that is a path to a file. | ✓ | ✓ | ✓ | 3.0 |
| **5.14** | Verify that the application is not susceptible XPath injection or XML injection attacks. | ✓ | ✓ | ✓ | 2.0 |
| **5.15** | Verify that all string variables placed into HTML or other web client code are either properly contextually encoded manually, or utilize templates that automatically contextually encode to ensure the application is not susceptible to reflected, stored or DOM Cross-Site Scripting (XSS) attacks. | ✓ | ✓ | ✓ | 3.1 |
| **5.16** | Verify that the application does not contain mass parameter assignment (AKA automatic variable binding) vulnerabilities. |  | ✓ | ✓ | 3.1 |
| **5.17** | Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (GET, POST, cookies, headers, environment, etc.) |  | ✓ | ✓ | 2.0 |
| **5.19** | Verify that all input data is validated, not only HTML form fields but all sources of input such as REST calls, query parameters, HTTP headers, cookies, batch files, RSS feeds, etc; using positive validation (whitelisting), then lesser forms of validation such as grey listing (eliminating known bad strings), or rejecting bad inputs (blacklisting). |  | ✓ | ✓ | 3.0 |
| **5.20** | Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length and pattern (e.g. credit card numbers or telephone, or validating that two related fields are reasonable, such as validating suburbs and zip or post codes match).  |  | ✓ | ✓ | 3.0 |
| **5.21** | Verify that unstructured data is sanitized to enforce generic safety measures such as allowed characters and length, and characters potentially harmful in given context should be escaped (e.g. natural names with Unicode or apostrophes, such as ねこ or O'Hara) |  | ✓ | ✓ | 3.0 |
| **5.22** | Verify that all untrusted HTML input from WYSIWYG editors or similar is properly sanitized with an HTML sanitizer library or framework feature.  | ✓ | ✓ | ✓ | 3.0 |
| **5.24** | Verify that where data is transferred from one DOM context to another, the transfer uses safe JavaScript methods, such as using innerText or .val to ensure the application is not susceptible to DOM Cross-Site Scripting (XSS) attacks. |  | ✓ | ✓ | 3.1 |
| **5.25** | Verify when parsing JSON in browsers or JavaScript based backends, that JSON.parse is used to parse the JSON document. Do not use eval() to parse JSON. |  | ✓ | ✓ | 3.0 |
| **5.27** | Verify the application for Server Side Request Forgery vulnerabilities. | ✓ | ✓ | ✓ | 3.1 |
| **5.28** | Verify that the application correctly restricts XML parsers to only use the most restrictive configuration possible and to ensure that dangerous features such as resolving external entities are disabled.  | ✓ | ✓ | ✓ | 3.1
| **5.29** | Verify that deserialization of untrusted data is avoided or is extensively protected when deserialization cannot be avoided.  | ✓ | ✓ | ✓ | 3.1

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Input Validation Testing](https://www.owasp.org/index.php/Testing_for_Input_Validation)
* [OWASP Cheat Sheet: Input Validation](https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet)
* [OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution](https://www.owasp.org/index.php/Testing_for_HTTP_Parameter_pollution_%28OTG-INPVAL-004%29)
* [OWASP LDAP Injection Cheat Sheet ](https://www.owasp.org/index.php/LDAP_Injection_Prevention_Cheat_Sheet)
* [OWASP Testing Guide 4.0: Client Side Testing ](https://www.owasp.org/index.php/Client_Side_Testing)
* [OWASP Cross Site Scripting Prevention Cheat Sheet ](https://www.owasp.org/index.php/XSS_%28Cross_Site_Scripting%29_Prevention_Cheat_Sheet)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet ](https://www.owasp.org/index.php/DOM_based_XSS_Prevention_Cheat_Sheet)
* [OWASP Java Encoding Project](https://www.owasp.org/index.php/OWASP_Java_Encoder_Project)

For more information on auto-escaping, please see:

* [Reducing XSS by way of Automatic Context-Aware Escaping in Template Systems](http://googleonlinesecurity.blogspot.com/2009/03/reducing-xss-by-way-of-automatic.html)
* [AngularJS Strict Contextual Escaping](https://docs.angularjs.org/api/ng/service/$sce)
* [ReactJS Escaping](https://reactjs.org/docs/introducing-jsx.html#jsx-prevents-injection-attacks)
* [Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)
