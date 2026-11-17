<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x10-V1-Encoding-and-Sanitization.md -->
<!-- Translator: GeeksikhSecurity -->

# V1 Encoding and Sanitization
# V1 ਏਨਕੋਡਿੰਗ ਅਤੇ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

This chapter addresses the most common web application security weaknesses related to the unsafe processing of untrusted data. Such weaknesses can result in various technical vulnerabilities, where untrusted data is interpreted according to the syntax rules of the relevant interpreter.

ਇਹ ਅਧਿਆਇ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਡਾਟੇ (untrusted data) ਦੀ ਅਸੁਰੱਖਿਅਤ ਪ੍ਰੋਸੈਸਿੰਗ ਨਾਲ ਸੰਬੰਧਿਤ ਸਭ ਤੋਂ ਆਮ ਵੈੱਬ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਖ਼ਾਮੀਆਂ (weaknesses) ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਦਾ ਹੈ। ਅਜਿਹੀਆਂ ਖ਼ਾਮੀਆਂ ਵੱਖ-ਵੱਖ ਤਕਨੀਕੀ ਕਮਜ਼ੋਰੀਆਂ ਦਾ ਕਾਰਨ ਬਣ ਸਕਦੀਆਂ ਹਨ, ਜਿੱਥੇ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਡਾਟੇ ਦੀ ਵਿਆਖਿਆ ਸੰਬੰਧਿਤ ਇੰਟਰਪ੍ਰੇਟਰ (interpreter) ਦੇ ਸਿੰਟੈਕਸ ਨਿਯਮਾਂ ਅਨੁਸਾਰ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

For modern web applications, it is always best to use safer APIs, such as parameterized queries, auto-escaping, or templating frameworks. Otherwise, carefully performed output encoding, escaping, or sanitization becomes critical to the application's security.

ਆਧੁਨਿਕ ਵੈੱਬ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ, ਹਮੇਸ਼ਾ ਵਧੇਰੇ ਸੁਰੱਖਿਅਤ API ਵਰਤਣਾ ਸਭ ਤੋਂ ਚੰਗਾ ਹੁੰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਪੈਰਾਮੀਟਰਾਈਜ਼ਡ ਕਿਊਰੀਆਂ (parameterized queries), ਸਵੈ-ਐਸਕੇਪਿੰਗ (auto-escaping), ਜਾਂ ਟੈਂਪਲੇਟਿੰਗ ਫ੍ਰੇਮਵਰਕ। ਨਹੀਂ ਤਾਂ, ਧਿਆਨ ਨਾਲ ਕੀਤੀ ਗਈ ਆਊਟਪੁੱਟ ਏਨਕੋਡਿੰਗ (output encoding), ਐਸਕੇਪਿੰਗ (escaping), ਜਾਂ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ (sanitization) ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਸੁਰੱਖਿਆ ਲਈ ਅਤਿ ਮਹੱਤਵਪੂਰਨ ਬਣ ਜਾਂਦੀ ਹੈ।

Input validation serves as a defense-in-depth mechanism to protect against unexpected or dangerous content. However, since its primary purpose is to ensure that incoming content matches functional and business expectations, requirements related to this can be found in the "Validation and Business Logic" chapter.

ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ (input validation) ਅਣਕਿਆਸੀ ਜਾਂ ਖ਼ਤਰਨਾਕ ਸਮੱਗਰੀ ਤੋਂ ਬਚਾਅ ਲਈ ਇੱਕ ਡੂੰਘਾਈ-ਵਿੱਚ-ਰੱਖਿਆ (defense-in-depth) ਪ੍ਰਣਾਲੀ ਵਜੋਂ ਕੰਮ ਕਰਦੀ ਹੈ। ਹਾਲਾਂਕਿ, ਕਿਉਂਕਿ ਇਸ ਦਾ ਮੁੱਖ ਉਦੇਸ਼ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਆਉਣ ਵਾਲੀ ਸਮੱਗਰੀ ਕਾਰਜਾਤਮਕ ਅਤੇ ਕਾਰੋਬਾਰੀ ਉਮੀਦਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦੀ ਹੈ, ਇਸ ਨਾਲ ਸੰਬੰਧਿਤ ਲੋੜਾਂ "ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਕਾਰੋਬਾਰੀ ਤਰਕ" (Validation and Business Logic) ਅਧਿਆਇ ਵਿੱਚ ਮਿਲ ਸਕਦੀਆਂ ਹਨ।

## V1.1 Encoding and Sanitization Architecture
## V1.1 ਏਨਕੋਡਿੰਗ ਅਤੇ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ ਢਾਂਚਾ

In the sections below, syntax-specific or interpreter-specific requirements for safely processing unsafe content to avoid security vulnerabilities are provided. The requirements in this section cover the order in which this processing should occur and where it should take place. They also aim to ensure that whenever data is stored, it remains in its original state and is not stored in an encoded or escaped form (e.g., HTML encoding), to prevent double encoding issues.

ਹੇਠਲੇ ਭਾਗਾਂ ਵਿੱਚ, ਸੁਰੱਖਿਆ ਕਮਜ਼ੋਰੀਆਂ ਤੋਂ ਬਚਣ ਲਈ ਅਸੁਰੱਖਿਅਤ ਸਮੱਗਰੀ ਦੀ ਸੁਰੱਖਿਅਤ ਪ੍ਰੋਸੈਸਿੰਗ ਵਾਸਤੇ ਸਿੰਟੈਕਸ-ਵਿਸ਼ੇਸ਼ ਜਾਂ ਇੰਟਰਪ੍ਰੇਟਰ-ਵਿਸ਼ੇਸ਼ ਲੋੜਾਂ ਦਿੱਤੀਆਂ ਗਈਆਂ ਹਨ। ਇਸ ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ ਉਸ ਕ੍ਰਮ ਨੂੰ ਕਵਰ ਕਰਦੀਆਂ ਹਨ ਜਿਸ ਵਿੱਚ ਇਹ ਪ੍ਰੋਸੈਸਿੰਗ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ ਅਤੇ ਇਹ ਕਿੱਥੇ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ। ਇਹਨਾਂ ਦਾ ਉਦੇਸ਼ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਵੀ ਹੈ ਕਿ ਜਦੋਂ ਵੀ ਡਾਟਾ ਸਟੋਰ ਕੀਤਾ ਜਾਵੇ, ਇਹ ਆਪਣੀ ਮੂਲ ਸਥਿਤੀ ਵਿੱਚ ਰਹੇ ਅਤੇ ਏਨਕੋਡ ਕੀਤੇ ਜਾਂ ਐਸਕੇਪ ਕੀਤੇ ਰੂਪ (ਜਿਵੇਂ, HTML ਏਨਕੋਡਿੰਗ) ਵਿੱਚ ਸਟੋਰ ਨਾ ਕੀਤਾ ਜਾਵੇ, ਤਾਂ ਜੋ ਦੋਹਰੀ ਏਨਕੋਡਿੰਗ (double encoding) ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ।

| # | Description | Level |
| :---: | :--- | :---: |
| **1.1.1** | Verify that input is decoded or unescaped into a canonical form only once, it is only decoded when encoded data in that form is expected, and that this is done before processing the input further, for example it is not performed after input validation or sanitization. | 2 |
| **1.1.2** | Verify that the application performs output encoding and escaping either as a final step before being used by the interpreter for which it is intended or by the interpreter itself. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **1.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇਨਪੁੱਟ ਨੂੰ ਕੈਨੋਨੀਕਲ ਰੂਪ (canonical form) ਵਿੱਚ ਸਿਰਫ਼ ਇੱਕ ਵਾਰ ਡੀਕੋਡ ਜਾਂ ਅਨਐਸਕੇਪ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਇਸ ਨੂੰ ਸਿਰਫ਼ ਉਦੋਂ ਹੀ ਡੀਕੋਡ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜਦੋਂ ਉਸ ਰੂਪ ਵਿੱਚ ਏਨਕੋਡ ਕੀਤੇ ਡਾਟੇ ਦੀ ਉਮੀਦ ਹੋਵੇ, ਅਤੇ ਇਹ ਇਨਪੁੱਟ ਦੀ ਅਗਲੀ ਪ੍ਰੋਸੈਸਿੰਗ ਤੋਂ ਪਹਿਲਾਂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਉਦਾਹਰਨ ਲਈ ਇਹ ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ ਜਾਂ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ ਤੋਂ ਬਾਅਦ ਨਹੀਂ ਕੀਤਾ ਜਾਂਦਾ। | 2 |
| **1.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਆਊਟਪੁੱਟ ਏਨਕੋਡਿੰਗ ਅਤੇ ਐਸਕੇਪਿੰਗ ਜਾਂ ਤਾਂ ਉਸ ਇੰਟਰਪ੍ਰੇਟਰ ਦੁਆਰਾ ਵਰਤੇ ਜਾਣ ਤੋਂ ਪਹਿਲਾਂ ਅੰਤਮ ਕਦਮ ਵਜੋਂ ਕਰਦੀ ਹੈ ਜਿਸ ਲਈ ਇਹ ਨਿਰਧਾਰਿਤ ਹੈ, ਜਾਂ ਇਹ ਇੰਟਰਪ੍ਰੇਟਰ ਦੁਆਰਾ ਖ਼ੁਦ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 2 |

## V1.2 Injection Prevention
## V1.2 ਇੰਜੈਕਸ਼ਨ ਰੋਕਥਾਮ

Output encoding or escaping, performed close to or adjacent to a potentially dangerous context, is critical to the security of any application. Typically, output encoding and escaping are not persisted, but are instead used to render output safe for immediate use in the appropriate interpreter. Attempting to perform this too early may result in malformed content or render the encoding or escaping ineffective.

ਆਊਟਪੁੱਟ ਏਨਕੋਡਿੰਗ ਜਾਂ ਐਸਕੇਪਿੰਗ, ਜੋ ਸੰਭਾਵੀ ਤੌਰ 'ਤੇ ਖ਼ਤਰਨਾਕ ਸੰਦਰਭ ਦੇ ਨੇੜੇ ਜਾਂ ਨਾਲ ਲੱਗਦੀ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਕਿਸੇ ਵੀ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਸੁਰੱਖਿਆ ਲਈ ਅਤਿ ਮਹੱਤਵਪੂਰਨ ਹੈ। ਆਮ ਤੌਰ 'ਤੇ, ਆਊਟਪੁੱਟ ਏਨਕੋਡਿੰਗ ਅਤੇ ਐਸਕੇਪਿੰਗ ਨੂੰ ਸਥਾਈ ਤੌਰ 'ਤੇ ਸੰਭਾਲਿਆ ਨਹੀਂ ਜਾਂਦਾ, ਸਗੋਂ ਇਹਨਾਂ ਦੀ ਵਰਤੋਂ ਢੁਕਵੇਂ ਇੰਟਰਪ੍ਰੇਟਰ ਵਿੱਚ ਤੁਰੰਤ ਵਰਤੋਂ ਲਈ ਆਊਟਪੁੱਟ ਨੂੰ ਸੁਰੱਖਿਅਤ ਬਣਾਉਣ ਵਾਸਤੇ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਨੂੰ ਬਹੁਤ ਜਲਦੀ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਨਾਲ ਵਿਗੜੀ ਹੋਈ ਸਮੱਗਰੀ ਪੈਦਾ ਹੋ ਸਕਦੀ ਹੈ ਜਾਂ ਏਨਕੋਡਿੰਗ ਜਾਂ ਐਸਕੇਪਿੰਗ ਬੇਅਸਰ ਹੋ ਸਕਦੀ ਹੈ।

In many cases, software libraries include safe or safer functions that perform this automatically, although it is necessary to ensure that they are correct for the current context.

ਕਈ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਸਾਫ਼ਟਵੇਅਰ ਲਾਇਬ੍ਰੇਰੀਆਂ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਜਾਂ ਵਧੇਰੇ ਸੁਰੱਖਿਅਤ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ ਜੋ ਇਹ ਆਪਣੇ ਆਪ ਕਰਦੇ ਹਨ, ਹਾਲਾਂਕਿ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਜ਼ਰੂਰੀ ਹੈ ਕਿ ਉਹ ਮੌਜੂਦਾ ਸੰਦਰਭ ਲਈ ਸਹੀ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **1.2.1** | Verify that output encoding for an HTTP response, HTML document, or XML document is relevant for the context required, such as encoding the relevant characters for HTML elements, HTML attributes, HTML comments, CSS, or HTTP header fields, to avoid changing the message or document structure. | 1 |
| **1.2.2** | Verify that when dynamically building URLs, untrusted data is encoded according to its context (e.g., URL encoding or base64url encoding for query or path parameters). Ensure that only safe URL protocols are permitted (e.g., disallow javascript: or data:). | 1 |
| **1.2.3** | Verify that output encoding or escaping is used when dynamically building JavaScript content (including JSON), to avoid changing the message or document structure (to avoid JavaScript and JSON injection). | 1 |
| **1.2.4** | Verify that data selection or database queries (e.g., SQL, HQL, NoSQL, Cypher) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from SQL Injection and other database injection attacks. This is also relevant when writing stored procedures. | 1 |
| **1.2.5** | Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding. | 1 |
| **1.2.6** | Verify that the application protects against LDAP injection vulnerabilities, or that specific security controls to prevent LDAP injection have been implemented. | 2 |
| **1.2.7** | Verify that the application is protected against XPath injection attacks by using query parameterization or precompiled queries. | 2 |
| **1.2.8** | Verify that LaTeX processors are configured securely (such as not using the "--shell-escape" flag) and an allowlist of commands is used to prevent LaTeX injection attacks. | 2 |
| **1.2.9** | Verify that the application escapes special characters in regular expressions (typically using a backslash) to prevent them from being misinterpreted as metacharacters. | 2 |
| **1.2.10** | Verify that the application is protected against CSV and Formula Injection. The application must follow the escaping rules defined in RFC 4180 sections 2.6 and 2.7 when exporting CSV content. Additionally, when exporting to CSV or other spreadsheet formats (such as XLS, XLSX, or ODF), special characters (including '=', '+', '-', '@', '\t' (tab), and '\0' (null character)) must be escaped with a single quote if they appear as the first character in a field value. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **1.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ HTTP ਜਵਾਬ, HTML ਦਸਤਾਵੇਜ਼, ਜਾਂ XML ਦਸਤਾਵੇਜ਼ ਲਈ ਆਊਟਪੁੱਟ ਏਨਕੋਡਿੰਗ ਲੋੜੀਂਦੇ ਸੰਦਰਭ ਲਈ ਢੁਕਵੀਂ ਹੈ, ਜਿਵੇਂ ਕਿ HTML ਐਲੀਮੈਂਟਾਂ, HTML ਐਟ੍ਰੀਬਿਊਟਾਂ, HTML ਟਿੱਪਣੀਆਂ, CSS, ਜਾਂ HTTP ਹੈਡਰ ਫ਼ੀਲਡਾਂ ਲਈ ਸੰਬੰਧਿਤ ਅੱਖਰਾਂ ਨੂੰ ਏਨਕੋਡ ਕਰਨਾ, ਤਾਂ ਜੋ ਸੁਨੇਹੇ ਜਾਂ ਦਸਤਾਵੇਜ਼ ਦੀ ਬਣਤਰ ਵਿੱਚ ਤਬਦੀਲੀ ਤੋਂ ਬਚਿਆ ਜਾ ਸਕੇ। | 1 |
| **1.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ URL ਬਣਾਉਂਦੇ ਸਮੇਂ, ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਡਾਟੇ ਨੂੰ ਉਸ ਦੇ ਸੰਦਰਭ ਅਨੁਸਾਰ ਏਨਕੋਡ ਕੀਤਾ ਜਾਂਦਾ ਹੈ (ਜਿਵੇਂ, ਕਿਊਰੀ ਜਾਂ ਪਾਥ ਪੈਰਾਮੀਟਰਾਂ ਲਈ URL ਏਨਕੋਡਿੰਗ ਜਾਂ base64url ਏਨਕੋਡਿੰਗ)। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਿਰਫ਼ ਸੁਰੱਖਿਅਤ URL ਪ੍ਰੋਟੋਕਾਲਾਂ ਦੀ ਇਜਾਜ਼ਤ ਹੈ (ਜਿਵੇਂ, javascript: ਜਾਂ data: ਦੀ ਮਨਾਹੀ ਕਰੋ)। | 1 |
| **1.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ JavaScript ਸਮੱਗਰੀ (JSON ਸਮੇਤ) ਬਣਾਉਂਦੇ ਸਮੇਂ ਆਊਟਪੁੱਟ ਏਨਕੋਡਿੰਗ ਜਾਂ ਐਸਕੇਪਿੰਗ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਤਾਂ ਜੋ ਸੁਨੇਹੇ ਜਾਂ ਦਸਤਾਵੇਜ਼ ਦੀ ਬਣਤਰ ਵਿੱਚ ਤਬਦੀਲੀ ਤੋਂ ਬਚਿਆ ਜਾ ਸਕੇ (JavaScript ਅਤੇ JSON ਇੰਜੈਕਸ਼ਨ ਤੋਂ ਬਚਣ ਲਈ)। | 1 |
| **1.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਡਾਟਾ ਚੋਣ ਜਾਂ ਡਾਟਾਬੇਸ ਕਿਊਰੀਆਂ (ਜਿਵੇਂ, SQL, HQL, NoSQL, Cypher) ਪੈਰਾਮੀਟਰਾਈਜ਼ਡ ਕਿਊਰੀਆਂ, ORM, ਐਂਟਿਟੀ ਫ੍ਰੇਮਵਰਕ ਵਰਤਦੀਆਂ ਹਨ, ਜਾਂ ਕਿਸੇ ਹੋਰ ਤਰੀਕੇ ਨਾਲ SQL ਇੰਜੈਕਸ਼ਨ ਅਤੇ ਹੋਰ ਡਾਟਾਬੇਸ ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਤੋਂ ਸੁਰੱਖਿਅਤ ਹਨ। ਇਹ ਸਟੋਰਡ ਪ੍ਰੋਸੀਜਰ (stored procedures) ਲਿਖਦੇ ਸਮੇਂ ਵੀ ਢੁਕਵਾਂ ਹੈ। | 1 |
| **1.2.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ OS ਕਮਾਂਡ ਇੰਜੈਕਸ਼ਨ ਤੋਂ ਬਚਾਅ ਕਰਦੀ ਹੈ ਅਤੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਕਾਲਾਂ ਪੈਰਾਮੀਟਰਾਈਜ਼ਡ OS ਕਿਊਰੀਆਂ ਵਰਤਦੀਆਂ ਹਨ ਜਾਂ ਸੰਦਰਭੀ ਕਮਾਂਡ ਲਾਈਨ ਆਊਟਪੁੱਟ ਏਨਕੋਡਿੰਗ ਵਰਤਦੀਆਂ ਹਨ। | 1 |
| **1.2.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ LDAP ਇੰਜੈਕਸ਼ਨ ਕਮਜ਼ੋਰੀਆਂ ਤੋਂ ਬਚਾਅ ਕਰਦੀ ਹੈ, ਜਾਂ LDAP ਇੰਜੈਕਸ਼ਨ ਨੂੰ ਰੋਕਣ ਲਈ ਖ਼ਾਸ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਲਾਗੂ ਕੀਤੇ ਗਏ ਹਨ। | 2 |
| **1.2.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਕਿਊਰੀ ਪੈਰਾਮੀਟਰਾਈਜ਼ੇਸ਼ਨ ਜਾਂ ਪਹਿਲਾਂ ਤੋਂ ਕੰਪਾਈਲ ਕੀਤੀਆਂ ਕਿਊਰੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ XPath ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਤੋਂ ਸੁਰੱਖਿਅਤ ਹੈ। | 2 |
| **1.2.8** | ਤਸਦੀਕ ਕਰੋ ਕਿ LaTeX ਪ੍ਰੋਸੈਸਰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਕੌਨਫ਼ਿਗਰ ਕੀਤੇ ਗਏ ਹਨ (ਜਿਵੇਂ ਕਿ "--shell-escape" ਫ਼ਲੈਗ ਦੀ ਵਰਤੋਂ ਨਾ ਕਰਨਾ) ਅਤੇ LaTeX ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਕਮਾਂਡਾਂ ਦੀ allowlist ਵਰਤੀ ਜਾਂਦੀ ਹੈ। | 2 |
| **1.2.9** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਰੈਗੂਲਰ ਐਕਸਪ੍ਰੈਸ਼ਨਾਂ (regular expressions) ਵਿੱਚ ਵਿਸ਼ੇਸ਼ ਅੱਖਰਾਂ ਨੂੰ ਐਸਕੇਪ ਕਰਦੀ ਹੈ (ਆਮ ਤੌਰ 'ਤੇ ਬੈਕਸਲੈਸ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ) ਤਾਂ ਜੋ ਉਹਨਾਂ ਨੂੰ ਮੈਟਾਕੈਰੇਕਟਰਾਂ (metacharacters) ਵਜੋਂ ਗ਼ਲਤ ਸਮਝੇ ਜਾਣ ਤੋਂ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 2 |
| **1.2.10** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ CSV ਅਤੇ Formula ਇੰਜੈਕਸ਼ਨ ਤੋਂ ਸੁਰੱਖਿਅਤ ਹੈ। CSV ਸਮੱਗਰੀ ਨਿਰਯਾਤ ਕਰਦੇ ਸਮੇਂ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ RFC 4180 ਦੇ ਭਾਗ 2.6 ਅਤੇ 2.7 ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਐਸਕੇਪਿੰਗ ਨਿਯਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਨੀ ਲਾਜ਼ਮੀ ਹੈ। ਇਸ ਤੋਂ ਇਲਾਵਾ, CSV ਜਾਂ ਹੋਰ ਸਪ੍ਰੈਡਸ਼ੀਟ ਫ਼ਾਰਮੈਟਾਂ (ਜਿਵੇਂ ਕਿ XLS, XLSX, ਜਾਂ ODF) ਵਿੱਚ ਨਿਰਯਾਤ ਕਰਦੇ ਸਮੇਂ, ਵਿਸ਼ੇਸ਼ ਅੱਖਰਾਂ ('=', '+', '-', '@', '\t' (ਟੈਬ), ਅਤੇ '\0' (null ਅੱਖਰ) ਸਮੇਤ) ਨੂੰ ਇੱਕ ਸਿੰਗਲ ਕੋਟ ਨਾਲ ਐਸਕੇਪ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ ਜੇ ਉਹ ਕਿਸੇ ਫ਼ੀਲਡ ਮੁੱਲ ਵਿੱਚ ਪਹਿਲੇ ਅੱਖਰ ਵਜੋਂ ਦਿਖਾਈ ਦਿੰਦੇ ਹਨ। | 3 |

Note: Using parameterized queries or escaping SQL is not always sufficient. Query parts such as table and column names (including "ORDER BY" column names) cannot be escaped. Including escaped user-supplied data in these fields results in failed queries or SQL injection.

ਨੋਟ: ਪੈਰਾਮੀਟਰਾਈਜ਼ਡ ਕਿਊਰੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਜਾਂ SQL ਨੂੰ ਐਸਕੇਪ ਕਰਨਾ ਹਮੇਸ਼ਾ ਕਾਫ਼ੀ ਨਹੀਂ ਹੁੰਦਾ। ਕਿਊਰੀ ਦੇ ਹਿੱਸੇ ਜਿਵੇਂ ਕਿ ਟੇਬਲ ਅਤੇ ਕਾਲਮ ਦੇ ਨਾਂ ("ORDER BY" ਕਾਲਮ ਨਾਵਾਂ ਸਮੇਤ) ਐਸਕੇਪ ਨਹੀਂ ਕੀਤੇ ਜਾ ਸਕਦੇ। ਇਹਨਾਂ ਫ਼ੀਲਡਾਂ ਵਿੱਚ ਐਸਕੇਪ ਕੀਤੇ ਉਪਭੋਗਤਾ-ਦਿੱਤੇ ਡਾਟੇ ਨੂੰ ਸ਼ਾਮਲ ਕਰਨ ਨਾਲ ਕਿਊਰੀਆਂ ਅਸਫਲ ਹੁੰਦੀਆਂ ਹਨ ਜਾਂ SQL ਇੰਜੈਕਸ਼ਨ ਹੁੰਦਾ ਹੈ।

## V1.3 Sanitization
## V1.3 ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ

The ideal protection against using untrusted content in an unsafe context is to use context-specific encoding or escaping, which maintains the same semantic meaning of the unsafe content but renders it safe for use in that particular context, as discussed in more detail in the previous section.

ਕਿਸੇ ਅਸੁਰੱਖਿਅਤ ਸੰਦਰਭ ਵਿੱਚ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਸਮੱਗਰੀ ਦੀ ਵਰਤੋਂ ਵਿਰੁੱਧ ਆਦਰਸ਼ ਬਚਾਅ ਸੰਦਰਭ-ਵਿਸ਼ੇਸ਼ ਏਨਕੋਡਿੰਗ ਜਾਂ ਐਸਕੇਪਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਹੈ, ਜੋ ਅਸੁਰੱਖਿਅਤ ਸਮੱਗਰੀ ਦਾ ਉਹੀ ਅਰਥਗਤ ਭਾਵ (semantic meaning) ਕਾਇਮ ਰੱਖਦੀ ਹੈ ਪਰ ਇਸ ਨੂੰ ਉਸ ਖ਼ਾਸ ਸੰਦਰਭ ਵਿੱਚ ਵਰਤੋਂ ਲਈ ਸੁਰੱਖਿਅਤ ਬਣਾ ਦਿੰਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਪਿਛਲੇ ਭਾਗ ਵਿੱਚ ਵਧੇਰੇ ਵਿਸਥਾਰ ਨਾਲ ਚਰਚਾ ਕੀਤੀ ਗਈ ਹੈ।

Where this is not possible, sanitization becomes necessary, removing potentially dangerous characters or content. In some cases, this may change the semantic meaning of the input, but for security reasons, there may be no alternative.

ਜਿੱਥੇ ਇਹ ਸੰਭਵ ਨਹੀਂ ਹੈ, ਉੱਥੇ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ ਜ਼ਰੂਰੀ ਹੋ ਜਾਂਦੀ ਹੈ, ਜੋ ਸੰਭਾਵੀ ਤੌਰ 'ਤੇ ਖ਼ਤਰਨਾਕ ਅੱਖਰਾਂ ਜਾਂ ਸਮੱਗਰੀ ਨੂੰ ਹਟਾ ਦਿੰਦੀ ਹੈ। ਕੁਝ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਇਹ ਇਨਪੁੱਟ ਦੇ ਅਰਥਗਤ ਭਾਵ ਨੂੰ ਬਦਲ ਸਕਦੀ ਹੈ, ਪਰ ਸੁਰੱਖਿਆ ਕਾਰਨਾਂ ਕਰਕੇ, ਸ਼ਾਇਦ ਕੋਈ ਬਦਲ ਨਾ ਹੋਵੇ।

| # | Description | Level |
| :---: | :--- | :---: |
| **1.3.1** | Verify that all untrusted HTML input from WYSIWYG editors or similar is sanitized using a well-known and secure HTML sanitization library or framework feature. | 1 |
| **1.3.2** | Verify that the application avoids the use of eval() or other dynamic code execution features such as Spring Expression Language (SpEL). Where there is no alternative, any user input being included must be sanitized before being executed. | 1 |
| **1.3.3** | Verify that data being passed to a potentially dangerous context is sanitized beforehand to enforce safety measures, such as only allowing characters which are safe for this context and trimming input which is too long. | 2 |
| **1.3.4** | Verify that user-supplied Scalable Vector Graphics (SVG) scriptable content is validated or sanitized to contain only tags and attributes (such as draw graphics) that are safe for the application, e.g., do not contain scripts and foreignObject. | 2 |
| **1.3.5** | Verify that the application sanitizes or disables user-supplied scriptable or expression template language content, such as Markdown, CSS or XSL stylesheets, BBCode, or similar. | 2 |
| **1.3.6** | Verify that the application protects against Server-side Request Forgery (SSRF) attacks, by validating untrusted data against an allowlist of protocols, domains, paths and ports and sanitizing potentially dangerous characters before using the data to call another service. | 2 |
| **1.3.7** | Verify that the application protects against template injection attacks by not allowing templates to be built based on untrusted input. Where there is no alternative, any untrusted input being included dynamically during template creation must be sanitized or strictly validated. | 2 |
| **1.3.8** | Verify that the application appropriately sanitizes untrusted input before use in Java Naming and Directory Interface (JNDI) queries and that JNDI is configured securely to prevent JNDI injection attacks. | 2 |
| **1.3.9** | Verify that the application sanitizes content before it is sent to memcache to prevent injection attacks. | 2 |
| **1.3.10** | Verify that format strings which might resolve in an unexpected or malicious way when used are sanitized before being processed. | 2 |
| **1.3.11** | Verify that the application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection. | 2 |
| **1.3.12** | Verify that regular expressions are free from elements causing exponential backtracking, and ensure untrusted input is sanitized to mitigate ReDoS or Runaway Regex attacks. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **1.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ WYSIWYG ਸੰਪਾਦਕਾਂ ਜਾਂ ਇਸ ਵਰਗੇ ਸਰੋਤਾਂ ਤੋਂ ਆਉਣ ਵਾਲੇ ਸਾਰੇ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ HTML ਇਨਪੁੱਟ ਨੂੰ ਇੱਕ ਪ੍ਰਸਿੱਧ ਅਤੇ ਸੁਰੱਖਿਅਤ HTML ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ ਲਾਇਬ੍ਰੇਰੀ ਜਾਂ ਫ੍ਰੇਮਵਰਕ ਵਿਸ਼ੇਸ਼ਤਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੈਨੀਟਾਈਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। | 1 |
| **1.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ eval() ਜਾਂ ਹੋਰ ਗਤੀਸ਼ੀਲ ਕੋਡ ਐਗਜ਼ੀਕਿਊਸ਼ਨ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ, ਜਿਵੇਂ ਕਿ Spring Expression Language (SpEL), ਦੀ ਵਰਤੋਂ ਤੋਂ ਬਚਦੀ ਹੈ। ਜਿੱਥੇ ਕੋਈ ਬਦਲ ਨਹੀਂ ਹੈ, ਉੱਥੇ ਸ਼ਾਮਲ ਕੀਤੇ ਜਾ ਰਹੇ ਕਿਸੇ ਵੀ ਉਪਭੋਗਤਾ ਇਨਪੁੱਟ ਨੂੰ ਐਗਜ਼ੀਕਿਊਟ ਕੀਤੇ ਜਾਣ ਤੋਂ ਪਹਿਲਾਂ ਸੈਨੀਟਾਈਜ਼ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ। | 1 |
| **1.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੰਭਾਵੀ ਤੌਰ 'ਤੇ ਖ਼ਤਰਨਾਕ ਸੰਦਰਭ ਨੂੰ ਭੇਜੇ ਜਾ ਰਹੇ ਡਾਟੇ ਨੂੰ ਸੁਰੱਖਿਆ ਉਪਾਅ ਲਾਗੂ ਕਰਨ ਲਈ ਪਹਿਲਾਂ ਹੀ ਸੈਨੀਟਾਈਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਸਿਰਫ਼ ਉਹਨਾਂ ਅੱਖਰਾਂ ਦੀ ਇਜਾਜ਼ਤ ਦੇਣਾ ਜੋ ਇਸ ਸੰਦਰਭ ਲਈ ਸੁਰੱਖਿਅਤ ਹਨ ਅਤੇ ਬਹੁਤ ਲੰਬੇ ਇਨਪੁੱਟ ਨੂੰ ਕੱਟ ਕੇ ਛੋਟਾ ਕਰਨਾ। | 2 |
| **1.3.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਪਭੋਗਤਾ-ਦਿੱਤੀ Scalable Vector Graphics (SVG) ਸਕ੍ਰਿਪਟ-ਯੋਗ ਸਮੱਗਰੀ ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਜਾਂ ਸੈਨੀਟਾਈਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਤਾਂ ਜੋ ਇਸ ਵਿੱਚ ਸਿਰਫ਼ ਉਹ ਟੈਗ ਅਤੇ ਐਟ੍ਰੀਬਿਊਟ (ਜਿਵੇਂ ਕਿ ਗ੍ਰਾਫ਼ਿਕਸ ਬਣਾਉਣ ਵਾਲੇ) ਹੋਣ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਸੁਰੱਖਿਅਤ ਹਨ, ਜਿਵੇਂ, ਇਸ ਵਿੱਚ ਸਕ੍ਰਿਪਟਾਂ ਅਤੇ foreignObject ਸ਼ਾਮਲ ਨਾ ਹੋਣ। | 2 |
| **1.3.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਉਪਭੋਗਤਾ-ਦਿੱਤੀ ਸਕ੍ਰਿਪਟ-ਯੋਗ ਜਾਂ ਐਕਸਪ੍ਰੈਸ਼ਨ ਟੈਂਪਲੇਟ ਭਾਸ਼ਾ ਸਮੱਗਰੀ, ਜਿਵੇਂ ਕਿ Markdown, CSS ਜਾਂ XSL ਸਟਾਈਲਸ਼ੀਟਾਂ, BBCode, ਜਾਂ ਇਸ ਵਰਗੀ ਸਮੱਗਰੀ ਨੂੰ ਸੈਨੀਟਾਈਜ਼ ਜਾਂ ਅਯੋਗ ਕਰਦੀ ਹੈ। | 2 |
| **1.3.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸਰਵਰ-ਪੱਖੀ ਬੇਨਤੀ ਜਾਅਲਸਾਜ਼ੀ (Server-side Request Forgery, SSRF) ਹਮਲਿਆਂ ਤੋਂ ਬਚਾਅ ਕਰਦੀ ਹੈ, ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਡਾਟੇ ਨੂੰ ਪ੍ਰੋਟੋਕਾਲਾਂ, ਡੋਮੇਨਾਂ, ਪਾਥਾਂ ਅਤੇ ਪੋਰਟਾਂ ਦੀ allowlist ਵਿਰੁੱਧ ਪ੍ਰਮਾਣਿਤ ਕਰਕੇ ਅਤੇ ਕਿਸੇ ਹੋਰ ਸੇਵਾ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਡਾਟੇ ਦੀ ਵਰਤੋਂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਸੰਭਾਵੀ ਤੌਰ 'ਤੇ ਖ਼ਤਰਨਾਕ ਅੱਖਰਾਂ ਨੂੰ ਸੈਨੀਟਾਈਜ਼ ਕਰਕੇ। | 2 |
| **1.3.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਇਨਪੁੱਟ ਦੇ ਆਧਾਰ 'ਤੇ ਟੈਂਪਲੇਟ ਬਣਾਉਣ ਦੀ ਇਜਾਜ਼ਤ ਨਾ ਦੇ ਕੇ ਟੈਂਪਲੇਟ ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਤੋਂ ਬਚਾਅ ਕਰਦੀ ਹੈ। ਜਿੱਥੇ ਕੋਈ ਬਦਲ ਨਹੀਂ ਹੈ, ਉੱਥੇ ਟੈਂਪਲੇਟ ਬਣਾਉਣ ਦੌਰਾਨ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਸ਼ਾਮਲ ਕੀਤੇ ਜਾ ਰਹੇ ਕਿਸੇ ਵੀ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਇਨਪੁੱਟ ਨੂੰ ਸੈਨੀਟਾਈਜ਼ ਜਾਂ ਸਖ਼ਤੀ ਨਾਲ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ। | 2 |
| **1.3.8** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ Java Naming and Directory Interface (JNDI) ਕਿਊਰੀਆਂ ਵਿੱਚ ਵਰਤੋਂ ਤੋਂ ਪਹਿਲਾਂ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਇਨਪੁੱਟ ਨੂੰ ਢੁਕਵੇਂ ਢੰਗ ਨਾਲ ਸੈਨੀਟਾਈਜ਼ ਕਰਦੀ ਹੈ ਅਤੇ JNDI ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ JNDI ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਕੌਨਫ਼ਿਗਰ ਕੀਤਾ ਗਿਆ ਹੈ। | 2 |
| **1.3.9** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਸਮੱਗਰੀ ਨੂੰ memcache ਵਿੱਚ ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ ਸੈਨੀਟਾਈਜ਼ ਕਰਦੀ ਹੈ। | 2 |
| **1.3.10** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਫ਼ਾਰਮੈਟ ਸਟ੍ਰਿੰਗਾਂ (format strings), ਜੋ ਵਰਤੇ ਜਾਣ 'ਤੇ ਅਣਕਿਆਸੇ ਜਾਂ ਦੁਰਭਾਵਨਾਪੂਰਨ ਢੰਗ ਨਾਲ ਰਿਜ਼ੌਲਵ (resolve) ਹੋ ਸਕਦੀਆਂ ਹਨ, ਨੂੰ ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਜਾਣ ਤੋਂ ਪਹਿਲਾਂ ਸੈਨੀਟਾਈਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। | 2 |
| **1.3.11** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ SMTP ਜਾਂ IMAP ਇੰਜੈਕਸ਼ਨ ਤੋਂ ਬਚਾਅ ਲਈ ਉਪਭੋਗਤਾ ਇਨਪੁੱਟ ਨੂੰ ਮੇਲ ਸਿਸਟਮਾਂ ਨੂੰ ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ ਸੈਨੀਟਾਈਜ਼ ਕਰਦੀ ਹੈ। | 2 |
| **1.3.12** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਰੈਗੂਲਰ ਐਕਸਪ੍ਰੈਸ਼ਨ ਘਾਤਾਂਕੀ ਬੈਕਟ੍ਰੈਕਿੰਗ (exponential backtracking) ਪੈਦਾ ਕਰਨ ਵਾਲੇ ਤੱਤਾਂ ਤੋਂ ਮੁਕਤ ਹਨ, ਅਤੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ReDoS ਜਾਂ Runaway Regex ਹਮਲਿਆਂ ਨੂੰ ਘਟਾਉਣ ਲਈ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਇਨਪੁੱਟ ਨੂੰ ਸੈਨੀਟਾਈਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। | 3 |

## V1.4 Memory, String, and Unmanaged Code
## V1.4 ਮੈਮੋਰੀ, ਸਟ੍ਰਿੰਗ, ਅਤੇ ਅਣਪ੍ਰਬੰਧਿਤ ਕੋਡ

The following requirements address risks associated with unsafe memory use, which generally apply when the application uses a systems language or unmanaged code.

ਹੇਠ ਲਿਖੀਆਂ ਲੋੜਾਂ ਅਸੁਰੱਖਿਅਤ ਮੈਮੋਰੀ ਵਰਤੋਂ ਨਾਲ ਜੁੜੇ ਖ਼ਤਰਿਆਂ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਦੀਆਂ ਹਨ, ਜੋ ਆਮ ਤੌਰ 'ਤੇ ਉਦੋਂ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ ਜਦੋਂ ਐਪਲੀਕੇਸ਼ਨ ਕਿਸੇ ਸਿਸਟਮ ਭਾਸ਼ਾ (systems language) ਜਾਂ ਅਣਪ੍ਰਬੰਧਿਤ ਕੋਡ (unmanaged code) ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ।

In some cases, it may be possible to achieve this by setting compiler flags that enable buffer overflow protections and warnings, including stack randomization and data execution prevention, and that break the build if unsafe pointer, memory, format string, integer, or string operations are found.

ਕੁਝ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਇਹ ਅਜਿਹੇ ਕੰਪਾਈਲਰ ਫ਼ਲੈਗ ਸੈੱਟ ਕਰਕੇ ਹਾਸਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਜੋ ਬਫ਼ਰ ਓਵਰਫ਼ਲੋ (buffer overflow) ਸੁਰੱਖਿਆਵਾਂ ਅਤੇ ਚੇਤਾਵਨੀਆਂ ਨੂੰ ਸਮਰੱਥ ਕਰਦੇ ਹਨ, ਜਿਸ ਵਿੱਚ ਸਟੈਕ ਰੈਂਡਮਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਡਾਟਾ ਐਗਜ਼ੀਕਿਊਸ਼ਨ ਰੋਕਥਾਮ ਸ਼ਾਮਲ ਹਨ, ਅਤੇ ਜੋ ਅਸੁਰੱਖਿਅਤ ਪੁਆਇੰਟਰ, ਮੈਮੋਰੀ, ਫ਼ਾਰਮੈਟ ਸਟ੍ਰਿੰਗ, ਇੰਟੀਜਰ, ਜਾਂ ਸਟ੍ਰਿੰਗ ਕਾਰਵਾਈਆਂ ਮਿਲਣ 'ਤੇ ਬਿਲਡ ਨੂੰ ਤੋੜ ਦਿੰਦੇ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **1.4.1** | Verify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows. | 2 |
| **1.4.2** | Verify that sign, range, and input validation techniques are used to prevent integer overflows. | 2 |
| **1.4.3** | Verify that dynamically allocated memory and resources are released, and that references or pointers to freed memory are removed or set to null to prevent dangling pointers and use-after-free vulnerabilities. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **1.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸਟੈਕ, ਬਫ਼ਰ, ਜਾਂ ਹੀਪ ਓਵਰਫ਼ਲੋ ਦਾ ਪਤਾ ਲਗਾਉਣ ਜਾਂ ਰੋਕਣ ਲਈ ਮੈਮੋਰੀ-ਸੁਰੱਖਿਅਤ ਸਟ੍ਰਿੰਗ, ਵਧੇਰੇ ਸੁਰੱਖਿਅਤ ਮੈਮੋਰੀ ਕਾਪੀ ਅਤੇ ਪੁਆਇੰਟਰ ਅੰਕਗਣਿਤ ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ। | 2 |
| **1.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇੰਟੀਜਰ ਓਵਰਫ਼ਲੋ ਨੂੰ ਰੋਕਣ ਲਈ ਚਿੰਨ੍ਹ (sign), ਰੇਂਜ, ਅਤੇ ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ ਤਕਨੀਕਾਂ ਵਰਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ। | 2 |
| **1.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਅਲਾਟ ਕੀਤੀ ਮੈਮੋਰੀ ਅਤੇ ਸਰੋਤ ਮੁਕਤ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਅਤੇ ਮੁਕਤ ਕੀਤੀ ਮੈਮੋਰੀ ਵੱਲ ਹਵਾਲੇ ਜਾਂ ਪੁਆਇੰਟਰ ਹਟਾ ਦਿੱਤੇ ਜਾਂਦੇ ਹਨ ਜਾਂ null 'ਤੇ ਸੈੱਟ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਤਾਂ ਜੋ ਲਟਕਦੇ ਪੁਆਇੰਟਰਾਂ (dangling pointers) ਅਤੇ use-after-free ਕਮਜ਼ੋਰੀਆਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 2 |

## V1.5 Safe Deserialization
## V1.5 ਸੁਰੱਖਿਅਤ ਡੀਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ

The conversion of data from a stored or transmitted representation into actual application objects (deserialization) has historically been the cause of various code injection vulnerabilities. It is important to perform this process carefully and safely to avoid these types of issues.

ਡਾਟੇ ਨੂੰ ਸਟੋਰ ਕੀਤੀ ਜਾਂ ਪ੍ਰਸਾਰਿਤ ਕੀਤੀ ਪੇਸ਼ਕਾਰੀ ਤੋਂ ਅਸਲ ਐਪਲੀਕੇਸ਼ਨ ਆਬਜੈਕਟਾਂ ਵਿੱਚ ਬਦਲਣਾ (ਡੀਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ, deserialization) ਇਤਿਹਾਸਕ ਤੌਰ 'ਤੇ ਵੱਖ-ਵੱਖ ਕੋਡ ਇੰਜੈਕਸ਼ਨ ਕਮਜ਼ੋਰੀਆਂ ਦਾ ਕਾਰਨ ਰਿਹਾ ਹੈ। ਇਸ ਕਿਸਮ ਦੇ ਮੁੱਦਿਆਂ ਤੋਂ ਬਚਣ ਲਈ ਇਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਧਿਆਨ ਨਾਲ ਅਤੇ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਕਰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ।

In particular, certain methods of deserialization have been identified by programming language or framework documentation as insecure and cannot be made safe with untrusted data. For each mechanism in use, careful due diligence should be performed.

ਖ਼ਾਸ ਤੌਰ 'ਤੇ, ਡੀਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ ਦੀਆਂ ਕੁਝ ਵਿਧੀਆਂ ਨੂੰ ਪ੍ਰੋਗਰਾਮਿੰਗ ਭਾਸ਼ਾ ਜਾਂ ਫ੍ਰੇਮਵਰਕ ਦਸਤਾਵੇਜ਼ਾਂ ਦੁਆਰਾ ਅਸੁਰੱਖਿਅਤ ਵਜੋਂ ਪਛਾਣਿਆ ਗਿਆ ਹੈ ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਡਾਟੇ ਨਾਲ ਸੁਰੱਖਿਅਤ ਨਹੀਂ ਬਣਾਇਆ ਜਾ ਸਕਦਾ। ਵਰਤੋਂ ਵਿੱਚ ਹਰੇਕ ਪ੍ਰਣਾਲੀ ਲਈ, ਧਿਆਨਪੂਰਵਕ ਉਚਿਤ ਸਾਵਧਾਨੀ (due diligence) ਵਰਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **1.5.1** | Verify that the application configures XML parsers to use a restrictive configuration and that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks. | 1 |
| **1.5.2** | Verify that deserialization of untrusted data enforces safe input handling, such as using an allowlist of object types or restricting client-defined object types, to prevent deserialization attacks. Deserialization mechanisms that are explicitly defined as insecure must not be used with untrusted input. | 2 |
| **1.5.3** | Verify that different parsers used in the application for the same data type (e.g., JSON parsers, XML parsers, URL parsers), perform parsing in a consistent way and use the same character encoding mechanism to avoid issues such as JSON Interoperability vulnerabilities or different URI or file parsing behavior being exploited in Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **1.5.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ XML ਪਾਰਸਰਾਂ (parsers) ਨੂੰ ਇੱਕ ਪ੍ਰਤਿਬੰਧਿਤ ਸੰਰਚਨਾ ਵਰਤਣ ਲਈ ਕੌਨਫ਼ਿਗਰ ਕਰਦੀ ਹੈ ਅਤੇ XML eXternal Entity (XXE) ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਬਾਹਰੀ ਐਂਟਿਟੀਆਂ ਨੂੰ ਰਿਜ਼ੌਲਵ ਕਰਨ ਵਰਗੀਆਂ ਅਸੁਰੱਖਿਅਤ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਯੋਗ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ। | 1 |
| **1.5.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਡਾਟੇ ਦੀ ਡੀਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ ਸੁਰੱਖਿਅਤ ਇਨਪੁੱਟ ਸੰਭਾਲ ਲਾਗੂ ਕਰਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਆਬਜੈਕਟ ਕਿਸਮਾਂ ਦੀ allowlist ਵਰਤਣਾ ਜਾਂ ਕਲਾਇੰਟ-ਪਰਿਭਾਸ਼ਿਤ ਆਬਜੈਕਟ ਕਿਸਮਾਂ ਨੂੰ ਪ੍ਰਤਿਬੰਧਿਤ ਕਰਨਾ, ਤਾਂ ਜੋ ਡੀਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। ਜਿਹੜੀਆਂ ਡੀਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ ਪ੍ਰਣਾਲੀਆਂ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਅਸੁਰੱਖਿਅਤ ਵਜੋਂ ਪਰਿਭਾਸ਼ਿਤ ਹਨ, ਉਹਨਾਂ ਨੂੰ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਇਨਪੁੱਟ ਨਾਲ ਨਹੀਂ ਵਰਤਿਆ ਜਾਣਾ ਚਾਹੀਦਾ। | 2 |
| **1.5.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਇੱਕੋ ਡਾਟਾ ਕਿਸਮ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਵੱਖ-ਵੱਖ ਪਾਰਸਰ (ਜਿਵੇਂ, JSON ਪਾਰਸਰ, XML ਪਾਰਸਰ, URL ਪਾਰਸਰ) ਪਾਰਸਿੰਗ ਇਕਸਾਰ ਢੰਗ ਨਾਲ ਕਰਦੇ ਹਨ ਅਤੇ ਇੱਕੋ ਅੱਖਰ ਏਨਕੋਡਿੰਗ ਪ੍ਰਣਾਲੀ ਵਰਤਦੇ ਹਨ, ਤਾਂ ਜੋ JSON ਅੰਤਰ-ਕਾਰਜਸ਼ੀਲਤਾ (JSON Interoperability) ਕਮਜ਼ੋਰੀਆਂ ਵਰਗੇ ਮੁੱਦਿਆਂ ਤੋਂ, ਜਾਂ Remote File Inclusion (RFI) ਜਾਂ ਸਰਵਰ-ਪੱਖੀ ਬੇਨਤੀ ਜਾਅਲਸਾਜ਼ੀ (SSRF) ਹਮਲਿਆਂ ਵਿੱਚ ਵੱਖ-ਵੱਖ URI ਜਾਂ ਫ਼ਾਈਲ ਪਾਰਸਿੰਗ ਵਿਹਾਰ ਦਾ ਸ਼ੋਸ਼ਣ ਕੀਤੇ ਜਾਣ ਤੋਂ ਬਚਿਆ ਜਾ ਸਕੇ। | 3 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
* [OWASP Web Security Testing Guide: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [RFC4180 - Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180#section-2)

For more information, specifically on deserialization or parsing issues, please see:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਖ਼ਾਸ ਕਰਕੇ ਡੀਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ ਜਾਂ ਪਾਰਸਿੰਗ ਮੁੱਦਿਆਂ ਬਾਰੇ, ਕਿਰਪਾ ਕਰਕੇ ਵੇਖੋ:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai - A New Era of SSRF Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
