# V1 Encoding and Sanitization

## Control Objective

This chapter focuses on the most common web application security weaknesses that are related to unsafe processing of untrusted data. This leads to a variety of technical vulnerabilities where the untrusted data gets interpreted using the syntax rules of the relevant interpreter.

With modern web applications, it will always be best to use safer APIs such as parameterized queries, auto-escaping or templating frameworks. Otherwise, or carefully performed output encoding/escaping or sanitization will be critical to the security of the application.

Input Validation can act as a defense in depth mechanism for protecting against unexpected, dangerous content. However, since its primary purpose is to ensure that incoming content matches functional and business expectations, requirements around this can be found in the "Business Logic" chapter.

## V1.1 Validation and Sanitization Architecture

In the sections below, syntax-specific or interpreter-specific requirements for safely processing unsafe content to avoid security vulnerabilities are provided. The requirements in this section cover the order in which this processing should happen and where it should take place. They also aim to ensure that whenever data is being stored, it is stored in its original state and not in an encoded or escaped state (e.g., HTML encoding) to prevent double encoding issues.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.1.1** | [ADDED] Verify that input is decoded or unescaped into a canonical form only once, it is only decoded when encoded data in that form is expected, and that this is done before processing the input further, for example it is not performed after input validation or sanitization. | 2 | v5.0.be-5.6.1 |
| **1.1.2** | [MODIFIED, MOVED FROM 1.5.4] Verify that the application performs output encoding and escaping either as a final step before being used by the interpreter for which it is intended or by the interpreter itself. | 2 | v5.0.be-5.6.2 |

## V1.2 Injection Prevention

Output encoding or escaping close or adjacent to a potentially dangerous context is critical to the security of any application. Typically, output encoding and escaping is not persisted, but rather used to render output safe to use in the appropriate interpreter for immediate use. Trying to do this too early may lead to malformed content or even render the encoding or escaping ineffective.

In many cases, software libraries will include safe or safer functions which will do this automatically although it will be necessary to be sure that they are correct for the current context.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.2.1** | [MODIFIED, SPLIT TO 5.3.13] Verify that output encoding for an HTTP response, HTML document, or XML document is relevant for the context required, such as encoding the relevant characters for HTML elements, HTML attributes, HTML comments, CSS, or HTTP header fields, to avoid changing the message or document structure. | 1 | v5.0.be-5.3.1 |
| **1.2.2** | [ADDED, SPLIT FROM 5.3.1] Verify that when dynamically building URLs, untrusted data is encoded according to its context (e.g., URL encoding or base64url encoding for query or path parameters). Ensure that only safe URL protocols are permitted (e.g., disallow javascript: or data:). | 1 | v5.0.be-5.3.13 |
| **1.2.3** | [MODIFIED, SPLIT TO 50.6.2, COVERS 5.3.6] Verify that output encoding or escaping is used when dynamically building JavaScript content (including JSON), to avoid changing the message or document structure (to avoid JavaScript and JSON injection). | 1 | v5.0.be-5.3.3 |
| **1.2.4** | [MODIFIED, COVERS 5.3.5] Verify that data selection or database queries (e.g., SQL, HQL, NoSQL, Cypher) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from SQL Injection and other database injection attacks. This should also be considered when writing stored procedures. | 1 | v5.0.be-5.3.4 |
| **1.2.5** | [COVERS 12.3.5] Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding. | 1 | v5.0.be-5.3.8 |
| **1.2.6** | Verify that the application protects against LDAP injection vulnerabilities, or that specific security controls to prevent LDAP injection have been implemented. | 2 | v5.0.be-5.3.7 |
| **1.2.7** | [MODIFIED] Verify that the application is protected against XPath injection attacks by using query parameterization or precompiled queries. | 2 | v5.0.be-5.3.10 |
| **1.2.8** | [ADDED] Verify that LaTeX processors are configured securely (such as not using the "--shell-escape" flag) and an allowlist of commands is used to prevent LaTeX injection attacks. | 2 | v5.0.be-5.3.12 |
| **1.2.9** | [ADDED] Verify that the application is protected against CSV and Formula Injection. The application should follow the escaping rules defined in RFC4180 2.6 and 2.7 when exporting CSV files. The application should escape special characters including '=', '+', '-', '@' '\t' (tab) and '\00' (null character) using a single quote, if they are the first character in a field, when exporting CSV files and other spreadsheet formats such as xls, xlsx, odf. | 3 | v5.0.be-5.3.11 |

Note: Using parameterized queries or escaping SQL is not always sufficient; table and column names, ORDER BY and so on, cannot be escaped. The inclusion of escaped user-supplied data in these fields results in failed queries or SQL injection.

## V1.3 Sanitization and Sandboxing

The ideal protection against using untrusted content in an unsafe context is using context specific encoding or escaping which maintains the same semantic meaning of the unsafe content but renders it safe for use in this particular context. This is discussed in more detail in the next section.

Where it is not possible to do this, other options include sanitization and sandboxing. Sanitization will involve removing potentially dangerous characters or content which in some cases could change the semantic meaning of the input but for security reasons there may be no choice. Sandboxing may involve ensuring that a potentially dangerous operation is contained such that even if it suffers a security vulnerability, that will not endanger the wider application.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.3.1** | [MODIFIED] Verify that all untrusted HTML input from WYSIWYG editors or similar is sanitized using a well-known and secure HTML sanitization library or framework feature. | 1 | v5.0.be-5.2.1 |
| **1.3.2** | [MODIFIED, COVERS 5.5.4] Verify that the application avoids the use of eval() or other dynamic code execution features such as Spring Expression Language (SpEL). Where there is no alternative, any user input being included must be sanitized or sandboxed before being executed. | 1 | v5.0.be-5.2.4 |
| **1.3.3** | [MODIFIED] Verify that data being passed to a potentially dangerous context is sanitized beforehand to enforce safety measures, such as only allowing characters which are safe for this context and trimming input which is too long. | 2 | v5.0.be-5.2.2 |
| **1.3.4** | [MODIFIED] Verify that user-supplied Scalable Vector Graphics (SVG) scriptable content is validated or sanitized to contain only tags and attributes (such as draw graphics) that are safe for the application, e.g., do not contain scripts and foreignObject. | 2 | v5.0.be-5.2.7 |
| **1.3.5** | Verify that the application sanitizes, disables, or sandboxes user-supplied scriptable or expression template language content, such as Markdown, CSS or XSL stylesheets, BBCode, or similar. | 2 | v5.0.be-5.2.8 |
| **1.3.6** | [MODIFIED] Verify that the application protects against Server-side Request Forgery (SSRF) attacks, by validating untrusted data against an allowlist of protocols, domains, paths and ports and sanitizing potentially dangerous characters before using the data to call another service. | 2 | v5.0.be-5.2.6 |
| **1.3.7** | [MODIFIED] Verify that the application protects against template injection attacks by not allowing templates to be built based on untrusted input. Where there is no alternative, any untrusted input being included dynamically during template creation must be sanitized or strictly validated. | 2 | v5.0.be-5.2.5 |
| **1.3.8** | [ADDED] Verify that the application escapes special characters in regular expressions (typically using a backslash) to prevent them from being misinterpreted as metacharacters. | 2 | v5.0.be-5.2.9 |
| **1.3.9** | [ADDED] Verify that the application appropriately sanitizes untrusted input before use in Java Naming and Directory Interface (JNDI) queries and that JNDI is configured securely to prevent JNDI injection attacks. | 2 | v5.0.be-5.2.11 |
| **1.3.10** | [ADDED] Verify that the application sanitizes content before it is sent to memcache to prevent injection attacks. | 2 | v5.0.be-5.2.12 |
| **1.3.11** | [MODIFIED, MOVED FROM 5.4.2] Verify that format strings which might resolve in an unexpected or malicious way when used are sanitized before being processed. | 2 | v5.0.be-5.2.13 |
| **1.3.12** | Verify that the application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection. | 2 | v5.0.be-5.2.3 |
| **1.3.13** | [ADDED] Verify that regular expressions are free from elements causing exponential backtracking, and ensure untrusted input is sanitized to mitigate ReDoS or Runaway Regex attacks. | 3 | v5.0.be-5.2.10 |

## V1.4 Memory, String, and Unmanaged Code

The following requirements cover risks around unsafe memory use and will generally only apply when the application uses a systems language or unmanaged code.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.4.1** | Verify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows. | 2 | v5.0.be-5.4.1 |
| **1.4.2** | Verify that sign, range, and input validation techniques are used to prevent integer overflows. | 2 | v5.0.be-5.4.3 |
| **1.4.3** | [ADDED] Verify that dynamically allocated memory and resources are released, and that references or pointers to freed memory are removed or set to null to prevent dangling pointers and use-after-free vulnerabilities. | 2 | v5.0.be-5.4.4 |

## V1.5 Safe Deserialization

Conversion of data from some sort of stored or transmitted representation into actual application objects (deserialization) has historically been the cause of a variety of code injection vulnerabilities. It is important to perform this process carefully and safely to avoid these types of issues.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.5.1** | [GRAMMAR] Verify that the application configures XML parsers to use a restrictive configuration and that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks. | 1 | v5.0.be-5.5.2 |
| **1.5.2** | [MODIFIED, MERGED FROM 1.5.2] Verify that deserialization with untrusted clients enforces safe input handling, such as using an allowlist of object types or restricting client-defined object types, to prevent deserialization attacks. Deserialization mechanisms that are explicitly defined as insecure (such as BinaryFormatter) must not be used with untrusted input. | 2 | v5.0.be-5.5.3 |
| **1.5.3** | [MODIFIED, MOVED FROM 13.1.1, LEVEL L1 > L2] Verify that different parsers used in the application for the same data type (e.g., JSON parsers, XML parsers, URL parsers), perform parsing in a consistent way and use the same character encoding mechanism to avoid issues such as JSON Interoperability vulnerabilities or different URI or file parsing behavior being exploited in Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks. | 3 | v5.0.be-5.5.5 |

## References

For more information, see also:

* [OWASP LDAP Injection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/README)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
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
