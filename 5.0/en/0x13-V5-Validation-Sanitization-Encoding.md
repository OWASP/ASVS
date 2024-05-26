# V5 Validation, Sanitization and Encoding

## Control Objective

The most common web application security weakness is using untrusted content in an unsafe context without any output encoding, query parameterization, or other output handling defense. This weakness leads to almost all of the significant vulnerabilities in web applications, such as Cross-Site Scripting (XSS), SQL injection, OS command injection, template injection, log injection, LDAP injection, and more.

Ensure that a verified application satisfies the following high-level requirements:

* Input validation and output encoding architecture have an agreed pipeline to prevent injection attacks.
* Input data is strongly typed, validated, range or length checked, or at worst, sanitized or filtered.
* Output data is encoded or escaped as per the context of the data as close to the interpreter as possible.

With modern web application architecture, output encoding is more important than ever. It is difficult to provide robust input validation in certain scenarios, so the use of safer API such as parameterized queries, auto-escaping templating frameworks, or carefully chosen output encoding is critical to the security of the application.

## V5.1 Input Validation

Input can come from a variety of sources including HTML form fields, REST requests, URL parameters, HTTP headers, cookies, files on disk, databases, external APIs, etc.

Properly implemented input validation controls, using positive allow lists and strong data typing, provide an important enforcement of business logic controls around the type of data that the app expects to receive. However, except in specific cases, it is generally not intended to prevent specific attacks.

Input validation still provides valuable security hygiene and should be applied to all inputs where possible. However, since input validation is not a complete security strategy, one should also make use of sandboxing, sanitization, encoding and parameterization whenever the input is being used in a potentially dangerous context.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.1.1** | [MODIFIED] Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (query string, body parameters, cookies, or headers). | ✓ | ✓ | ✓ | 235 |
| **5.1.2** | Verify that frameworks protect against mass parameter assignment attacks, or that the application has countermeasures to protect against unsafe parameter assignment, such as marking fields private or similar. | ✓ | ✓ | ✓ | 915 |
| **5.1.3** | [MODIFIED] Verify that all input is validated using positive validation, using an allowed list of values or patterns. | ✓ | ✓ | ✓ | 20 |
| **5.1.4** | [GRAMMAR] Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length and pattern (e.g. credit card numbers, e-mail addresses, telephone numbers, or validating that two related fields are reasonable, such as checking that suburb and zipcode match). | ✓ | ✓ | ✓ | 20 |
| **5.1.5** | [MODIFIED, SPLIT TO 50.7.1] Verify that the application will only automatically redirect the user to a different URL directly from an application URL where the destination appears on an allow list. | ✓ | ✓ | ✓ | 601 |
| **5.1.6** | [ADDED] Verify that untrusted input is validated for length before being included in a cookie (including as part of a JWT) and that the cookie name and value length combined are not over 4096 bytes. | | ✓ | ✓ | |

## V5.2 Sanitization and Sandboxing

Input validation is a complicated topic.

Sometimes input validation is not going to be helpful for security, other times it will help it to a moderate degree, whilst other times it will be fundamental for security defense. It depends on the type of data and the use of that data to determine how effective input validation will be.

For example:

* Sanitization: When a user is authoring HTML, the standard defense is to standardize HTML to remove Performing JSON sanitizing before JSON parsers are used, and of course HTML sanitization for XSS defense
* Escaping: Done in the UI when you want to preserve displaying content as the user typed it in, also for some injection protection like LDAP injection protection
* Parameterization: For SQL Injection, primarily
* Sandboxing: When you can't sanitize HTML for some reason and need to dump potentially active content on your web page, iFrame sandboxing is critical. CSP has some sandboxing capabilities, too.
* URLs in Web UIs should block JavaScript and data URLs as a defense against XSS attacks. However, it's important to note that often, even valid data can still pose a threat.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.2.1** | [MODIFIED] Verify that all untrusted HTML input from WYSIWYG editors or similar is properly sanitized using a well-known and secure HTML sanitization library or framework feature. | ✓ | ✓ | ✓ | 116 |
| **5.2.2** | Verify that unstructured data is sanitized to enforce safety measures such as allowed characters and length. | ✓ | ✓ | ✓ | 138 |
| **5.2.3** | Verify that the application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection. | ✓ | ✓ | ✓ | 147 |
| **5.2.4** | Verify that the application avoids the use of eval() or other dynamic code execution features. Where there is no alternative, any user input being included must be sanitized or sandboxed before being executed. | ✓ | ✓ | ✓ | 95 |
| **5.2.5** | [MODIFIED] Verify that the application protects against template injection attacks by not allowing templates to be built based on untrusted input. Where there is no alternative, any untrusted input being included dynamically during template creation must be sanitized or strictly validated. | ✓ | ✓ | ✓ | 94 |
| **5.2.6** | Verify that the application protects against SSRF attacks, by validating or sanitizing untrusted data or HTTP file metadata, such as filenames and URL input fields, and uses allow lists of protocols, domains, paths and ports. | ✓ | ✓ | ✓ | 918 |
| **5.2.7** | Verify that the application sanitizes, disables, or sandboxes user-supplied Scalable Vector Graphics (SVG) scriptable content, especially as they relate to XSS resulting from inline scripts, and foreignObject. | ✓ | ✓ | ✓ | 159 |
| **5.2.8** | Verify that the application sanitizes, disables, or sandboxes user-supplied scriptable or expression template language content, such as Markdown, CSS or XSL stylesheets, BBCode, or similar. | ✓ | ✓ | ✓ | 94 |
| **5.2.9** | [ADDED] Verify that the application uses slashes to correctly escape special characters being used in regular expressions to ensure they are not misinterpreted as control characters. | ✓ | ✓ | ✓ | 624 |
| **5.2.10** | [ADDED] Verify that regular expressions are free from elements causing exponential backtracking, and ensure untrusted input is sanitized to mitigate ReDoS or Runaway Regex attacks. | ✓ | ✓ | ✓ | 1333 |
| **5.2.11** | [ADDED] Verify that the application appropriately sanitizes untrusted input before use in Java Naming and Directory Interface (JNDI) queries and that JNDI is configured as securely as possible to prevent JNDI injection attacks. | ✓ | ✓ | ✓ | 917 |
| **5.2.12** | [ADDED] Verify that the application sanitizes content before it is sent to memcache to prevent injection attacks. | | ✓ | ✓ | |

## V5.3 Output Encoding and Injection Prevention

Output encoding close or adjacent to the interpreter in use is critical to the security of any application. Typically, output encoding is not persisted, but rather used to render output safely in the appropriate context for immediate use. Failing to output encode will result in an insecure, injectable, and unsafe application.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.3.1** | [MODIFIED] Verify that output encoding is relevant for the interpreter and context required. For example, use encoders specifically for HTML values, HTML attributes, JavaScript, CSS, URL parameters, HTTP headers, SMTP, and others as the context requires, especially from untrusted inputs (e.g. names with Unicode or apostrophes, such as ねこ or O'Hara). | ✓ | ✓ | ✓ | 116 |
| **5.3.2** | [DELETED, DUPLICATE OF 14.4.1] | | | | |
| **5.3.3** | Verify that context-aware, preferably automated - or at worst, manual - output escaping protects against reflected, stored, and DOM based XSS. | ✓ | ✓ | ✓ | 79 |
| **5.3.4** | [MODIFIED] Verify that data selection or database queries (e.g. SQL, HQL, NoSQL, Cypher) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from database injection attacks. | ✓ | ✓ | ✓ | 89 |
| **5.3.5** | [DELETED, DUPLICATE OF 5.3.4] | | | | |
| **5.3.6** | [MODIFIED] Verify that the application protects against JSON injection attacks. | ✓ | ✓ | ✓ | 75 |
| **5.3.7** | Verify that the application protects against LDAP injection vulnerabilities, or that specific security controls to prevent LDAP injection have been implemented. | ✓ | ✓ | ✓ | 90 |
| **5.3.8** | Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding. | ✓ | ✓ | ✓ | 78 |
| **5.3.9** | [DELETED, DUPLICATE OF 12.3.2, 12.3.3] | | | | |
| **5.3.10** | Verify that the application protects against XPath injection or XML injection attacks. | ✓ | ✓ | ✓ | 643 |
| **5.3.11** | [ADDED] Verify that the application is protected against CSV and Formula Injection. The application should follow the escaping rules defined in RFC4180 2.6 and 2.7 when exporting CSV files. The application should escape special characters including '=', '+', '-', '@' '\t' (tab) and '\00' (null character) using a single quote, if they are the first character in a field, when exporting CSV files and other spreadsheet formats such as xls, xlsx, odf. | ✓ | ✓ | ✓ | 1236 |
| **5.3.12** | [ADDED] Verify that LaTeX processors are configured securely (such as not using the "--shell-escape" flag) and command allow-listing is used to prevent LaTeX injection attacks. | | ✓ | ✓ | |

Note: Using parameterized queries or escaping SQL is not always sufficient; table and column names, ORDER BY and so on, cannot be escaped. The inclusion of escaped user-supplied data in these fields results in failed queries or SQL injection.

Note: The SVG format explicitly allows ECMA script in almost all contexts, so it may not be possible to block all SVG XSS vectors completely. If SVG upload is required, we strongly recommend either serving these uploaded files as text/plain or using a separate user-supplied content domain to prevent successful XSS from taking over the application.

## V5.4 Memory, String, and Unmanaged Code

The following requirements will only apply when the application uses a systems language or unmanaged code.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.4.1** | Verify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows. | | ✓ | ✓ | 120 |
| **5.4.2** | Verify that format strings do not take potentially hostile input, and are constant. | | ✓ | ✓ | 134 |
| **5.4.3** | Verify that sign, range, and input validation techniques are used to prevent integer overflows. | | ✓ | ✓ | 190 |

## V5.5 Deserialization Prevention

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.5.1** | [DELETED, INCORRECT] | | | | |
| **5.5.2** | Verify that the application correctly restricts XML parsers to only use the most restrictive configuration possible and to ensure that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks. | ✓ | ✓ | ✓ | 611 |
| **5.5.3** | [MODIFIED, MERGED FROM 1.5.2] Verify that if deserialization is used when communicating with untrusted clients, the input is handled safely. For example, by only allowing a allow-list of object types or not allowing the client to define the object type to deserialize to, in order to prevent deserialization attacks. | ✓ | ✓ | ✓ | 502 |
| **5.5.4** | Verify that when parsing JSON in browsers or JavaScript-based backends, JSON.parse is used to parse the JSON document. Do not use eval() to parse JSON. | ✓ | ✓ | ✓ | 95 |
| **5.5.5** | [MODIFIED, MOVED FROM 13.1.1, LEVEL L1 > L2] Verify that different parsers used in the application for the same data type (e.g. JSON parsers, XML parsers, URL parsers), perform parsing in a consistent way and use the same character encoding mechanism to avoid issues such as JSON Interoperability vulnerabilities or different URI or file parsing behavior being exploited in Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks. | | ✓ | ✓ | 436 |

## V5.6 Validation and Sanitization Architecture

With syntax-specific requirements we say "do the correct thing" and here are the requirements to say "do it in the correct order" and "do it in the correct place".

Also, the requirements aim to ensure that whenever data is being stored, it is stored in its original state and not in an encoded state (e.g. HTML encoding) to prevent double encoding issues.

<!--
The requirement belongs here if it is:

  * input validation, sanitization or encoding architecture
  * input validation, sanitization or encoding processing (order)

The requirement does not belong here, if it is:

  * syntax specific or clear input validation, sanitization or encoding requirement

reorg: move it to 1st chapter in the paragraph
-->

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.6.1** | [ADDED] Verify that input is decoded or unescaped into a canonical form only once and that this is done before processing the input further, for example it is not performed after input validation or sanitization. | ✓ | ✓ | ✓ | 174 |
| **5.6.2** | [MODIFIED, MOVED FROM 1.5.3, LEVEL L2 > L1] Verify that the application is designed to enforce input validation at a trusted service layer. While client-side validation improves usability, security must not rely on it. | ✓ | ✓ | ✓ | 602 |
| **5.6.3** | [MODIFIED, MOVED FROM 1.5.4] Verify that the application performs output encoding and escaping either as a final step before being used by the interpreter for which it is intended or by the interpreter itself. | | ✓ | ✓ | 116 |

## References

For more information, see also:

* [OWASP Testing Guide 4.0: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Cheat Sheet: Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution.html)
* [OWASP LDAP Injection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/README)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [XML External Entity (XXE) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)

For more information on auto-escaping, please see:

* [Reducing XSS by way of Automatic Context-Aware Escaping in Template Systems](https://googleonlinesecurity.blogspot.com/2009/03/reducing-xss-by-way-of-automatic.html)
* [AngularJS Strict Contextual Escaping](https://docs.angularjs.org/api/ng/service/$sce)
* [AngularJS ngBind](https://docs.angularjs.org/api/ng/directive/ngBind)
* [Angular Sanitization](https://angular.io/guide/security#sanitization-and-security-contexts)
* [Angular Security](https://angular.io/guide/security)
* [ReactJS Escaping](https://reactjs.org/docs/introducing-jsx.html#jsx-prevents-injection-attacks)
* [Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

For more information on deserialization or parsing issues, please see:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [OWASP Deserialization of Untrusted Data Guide](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai - A New Era of SSRF Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
