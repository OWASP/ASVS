# V1 Encoding and Sanitization

## Control Objective

This chapter provides requirements that help developers avoid unsafe processing of untrusted data, which can lead to common web application security weaknesses where untrusted data becomes interpreted by the syntax rules of a relevant interpreter.

If you are using modern web application technologies, you can avoid these problems by using safer APIs such as parameterized queries, employing auto-escaping, or using templating frameworks. If these solutions are not available, it is critical to application security that developers should carefully perform output encoding, escaping, or sanitization on all data.

You may also use input validation as an in-depth defense mechanism for protecting against unexpected, or dangerous content. However, since validation matches incoming content with functional and business expectations, requirements around validation can be found in the "Validation and Business Logic" chapter.

## V1.1 Validation and Sanitization Architecture

This section includes syntax-specific or interpreter-specific requirements that allow developers to safely process unsafe content and avoid security vulnerabilities. They specify the order in which unsafe data should be processed and where the processing should take place. Also, these requirements prevent double encoding issues by indicating that data should be stored in its original state and not in an encoded or escaped state (e.g., HTML encoding). 
| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.1.1** | Verify that input is decoded or unescaped into a canonical form only once, it is only decoded when encoded data in that form is expected, and that this is done before processing the input further, for example it is not performed after input validation or sanitization. | 2 | v5.0.be-5.6.1 |
| **1.1.2** | Verify that the application performs output encoding and escaping either as a final step before being used by the interpreter for which it is intended or by the interpreter itself. | 2 | v5.0.be-5.6.2 |

## V1.2 Injection Prevention

It is critical to the security of any application that output is encoded or escaped close or adjacent to any potentially dangerous contexts. Typically, these techniques are not persisted, but rather used to render output safe to use in the appropriate interpreter for immediate use. If they are used too early, you may cause malformed content to occur or even render your output encoding or escaping ineffective.

In many situations, software libraries will include safe or safer functions which will automatically perfrom output encoding or escaping, although it will be necessary to be sure that these functions are correctly used for the current context.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.2.1** | Verify that output encoding for an HTTP response, HTML document, or XML document is relevant for the context required, such as encoding the relevant characters for HTML elements, HTML attributes, HTML comments, CSS, or HTTP header fields, to avoid changing the message or document structure. | 1 | v5.0.be-5.3.1 |
| **1.2.2** | Verify that when dynamically building URLs, untrusted data is encoded according to its context (e.g., URL encoding or base64url encoding for query or path parameters). Ensure that only safe URL protocols are permitted (e.g., disallow javascript: or data:). | 1 | v5.0.be-5.3.13 |
| **1.2.3** | Verify that output encoding or escaping is used when dynamically building JavaScript content (including JSON), to avoid changing the message or document structure (to avoid JavaScript and JSON injection). | 1 | v5.0.be-5.3.3 |
| **1.2.4** | Verify that data selection or database queries (e.g., SQL, HQL, NoSQL, Cypher) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from SQL Injection and other database injection attacks. This is also relevant when writing stored procedures. | 1 | v5.0.be-5.3.4 |
| **1.2.5** | Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding. | 1 | v5.0.be-5.3.8 |
| **1.2.6** | Verify that the application protects against LDAP injection vulnerabilities, or that specific security controls to prevent LDAP injection have been implemented. | 2 | v5.0.be-5.3.7 |
| **1.2.7** | Verify that the application is protected against XPath injection attacks by using query parameterization or precompiled queries. | 2 | v5.0.be-5.3.10 |
| **1.2.8** | Verify that LaTeX processors are configured securely (such as not using the "--shell-escape" flag) and an allowlist of commands is used to prevent LaTeX injection attacks. | 2 | v5.0.be-5.3.12 |
| **1.2.9** | Verify that the application escapes special characters in regular expressions (typically using a backslash) to prevent them from being misinterpreted as metacharacters. | 2 | v5.0.be-5.2.9 |
| **1.2.10** | Verify that the application is protected against CSV and formula injection. The application must follow the escaping rules defined in RFC 4180 sections 2.6 and 2.7 when exporting CSV content. Additionally, when exporting to CSV or other spreadsheet formats (such as XLS, XLSX, or ODF), special characters (including '=', '+', '-', '@', '\t' (tab), and '\0' (null character)) must be escaped with a single quote if they appear as the first character in a field value. | 3 | v5.0.be-5.3.11 |

Note: Using parameterized queries or escaping SQL is not always sufficient. Query parts such as table and column names (including "ORDER BY" column names) cannot be escaped. The inclusion of escaped user-supplied data in these fields results in failed queries or SQL injection.

## V1.3 Sanitization

To protect against untrusted content being used in an unsafe context, developers should use context-specific encoding or escaping which maintains the same semantic meaning of the unsafe content but renders it safe for use in this particular context (see previous section).

If it is not possible to do this, sanitization will be necessary to remove potentially dangerous characters or content. In some cases, the semantic meaning of the input may be changed, but for security reasons, there may be no choice.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.3.1** | Verify that all untrusted HTML input from WYSIWYG editors or similar is sanitized using a well-known and secure HTML sanitization library or framework feature. | 1 | v5.0.be-5.2.1 |
| **1.3.2** | Verify that the application avoids the use of eval() or other dynamic code execution features such as Spring Expression Language (SpEL). Where there is no alternative, any user input being included must be sanitized before being executed. | 1 | v5.0.be-5.2.4 |
| **1.3.3** | Verify that data being passed to a potentially dangerous context is sanitized beforehand to enforce safety measures, such as only allowing characters which are safe for this context and trimming input which is too long. | 2 | v5.0.be-5.2.2 |
| **1.3.4** | Verify that user-supplied Scalable Vector Graphics (SVG) scriptable content is validated or sanitized to contain only tags and attributes (such as draw graphics) that are safe for the application, e.g., do not contain scripts and foreignObject. | 2 | v5.0.be-5.2.7 |
| **1.3.5** | Verify that the application sanitizes or disables user-supplied scriptable or expression template language content, such as Markdown, CSS or XSL stylesheets, BBCode, or similar. | 2 | v5.0.be-5.2.8 |
| **1.3.6** | Verify that the application protects against Server-side Request Forgery (SSRF) attacks, by validating untrusted data against an allowlist of protocols, domains, paths and ports and sanitizing potentially dangerous characters before using the data to call another service. | 2 | v5.0.be-5.2.6 |
| **1.3.7** | Verify that the application protects against template injection attacks by not allowing templates to be built based on untrusted input. Where there is no alternative, any untrusted input being included dynamically during template creation must be sanitized or strictly validated. | 2 | v5.0.be-5.2.5 |
| **1.3.8** | Verify that the application appropriately sanitizes untrusted input before use in Java Naming and Directory Interface (JNDI) queries and that JNDI is configured securely to prevent JNDI injection attacks. | 2 | v5.0.be-5.2.11 |
| **1.3.9** | Verify that the application sanitizes content before it is sent to memcache to prevent injection attacks. | 2 | v5.0.be-5.2.12 |
| **1.3.10** | Verify that format strings which might resolve in an unexpected or malicious way when used are sanitized before being processed. | 2 | v5.0.be-5.2.13 |
| **1.3.11** | Verify that the application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection. | 2 | v5.0.be-5.2.3 |
| **1.3.12** | Verify that regular expressions are free from elements causing exponential backtracking, and ensure untrusted input is sanitized to mitigate ReDoS or Runaway Regex attacks. | 3 | v5.0.be-5.2.10 |

## V1.4 Memory, String, and Unmanaged Code

The following requirements discusses how unsafe memory use can lead to security risks and generally they will only apply when the application uses a system language or unmanaged code.

In some cases, you may be able to set compiler flags which enable buffer overflow protections and warnings, including stack randomization data execution prevention. They will break the build if an unsafe pointer, memory, format string, integer, or string operations are found.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.4.1** | Verify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows. | 2 | v5.0.be-5.4.1 |
| **1.4.2** | Verify that sign, range, and input validation techniques are used to prevent integer overflows. | 2 | v5.0.be-5.4.3 |
| **1.4.3** | Verify that dynamically allocated memory and resources are released, and that references or pointers to freed memory are removed or set to null to prevent dangling pointers and use-after-free vulnerabilities. | 2 | v5.0.be-5.4.4 |

## V1.5 Safe Deserialization

Many code injection vulnerabilities occr when data is converted from some sort of stored or transmitted representation into actual application objects (deserialization). To avoid these risks, it is important to perform deserialization carefully and safely.

In particular, programming languages or framework documentation can state that certain methods of deserialization are insecure and cannot be made safe with untrusted data. Careful due diligence of your deserialization mechanisms should be performed.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **1.5.1** | Verify that the application will configure XML parsers to use restrictive configurations and that unsafe features such as resolving external entities have been disabled to prevent XML eXternal Entity (XXE) attacks. | 1 | v5.0.be-5.5.2 |
| **1.5.2** | Verify that deserialization of untrusted data enforces safe input handling to prevent deserialization attacks, such as employing an allowlist of object types or restricting client-defined object types. If a deserialization mechanism is explicitly defined as insecure, it must not be used with untrusted input. | 2 | v5.0.be-5.5.3 |
| **1.5.3** | Verify that different parsers used in the application for the same data type (e.g., JSON parsers, XML parsers, URL parsers), will perform parsing in a consistent way and use the same character encoding mechanism to avoid issues such as JSON Interoperability vulnerabilities or different URI or file parsing behavior being exploited in Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks. | 3 | v5.0.be-5.5.5 |

## References

For more information, see also:

* [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/README)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [RFC4180 - Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180#section-2)

For more information on deserialization or parsing issues, please see:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [OWASP Deserialization of Untrusted Data Guide](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai - A New Era of SSRF Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
