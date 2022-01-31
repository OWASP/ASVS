# V5 验证、过滤和编码

## 控制目标

最常见的 Web 应用程序安全漏洞，是在没有任何输出编码的情况下，直接使用来自客户端或环境的输入（缺乏正确的验证）。 这一弱点导致了 Web 应用程序中几乎所有的重大漏洞，例如跨站点脚本（XSS）、SQL 注入、解释器注入、语言环境/Unicode 攻击、文件系统攻击和缓冲区溢出。

确保经过验证的应用程序满足以下高级要求：

* 输入验证和输出编码架构有一条约定的管道来防止注入攻击。
* 输入数据是强类型的，经过验证，范围或长度检查，或者在最坏的情况下，经过消毒或过滤。
* 输出结果根据数据的上下文进行编码或转义，尽可能地接近解释器。

随着现代网络应用架构的发展，输出编码比以往任何时候都更重要。在某些情况下很难提供健壮的输入验证，因此使用更安全的API，如参数化查询、自动转义的模板框架或精心选择的输出编码，对应用程序的安全性至关重要。

## V5.1 输入验证

正确实施的输入验证控制，使用白名单列表和强数据类型，可以消除 90% 以上的所有注入攻击。长度和范围检查可以进一步减少这种情况。在应用程序架构、设计冲刺（Design Sprint）、编码以及单元和集成测试期间，需要构建安全输入验证。 尽管其中许多项目在渗透测试中找不到，但不实施它们的结果通常可以在 V5.3 - 输出编码和注入预防要求 中找到。建议开发人员和安全代码审查人员将本小节作为基础（正如所有项目都需要满足 L1 那样），以防止注入。

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.1.1** | 验证应用程序是否有HTTP参数污染攻击的防御措施，特别是当应用程序框架没有区分请求参数的来源（GET、POST、cookies、请求头或环境变量）。 | ✓ | ✓ | ✓ | 235 |
| **5.1.2** | 验证框架是否能防止批量参数分配攻击，或者应用程序是否有对策来防止不安全的参数分配，如将字段标记为私有等类型。 ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 915 |
| **5.1.3** | 验证所有输入（HTML 表单字段、REST 请求、URL 参数、HTTP 请求头、cookies、批处理文件、RSS 源等）都使用“白名单”（允许列表）。 ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.4** | 验证结构化数据是强类型的，并根据定义的模式进行验证，包括允许的字符、长度和模式（如信用卡号码、电子邮件地址、电话号码，或验证两个相关字段是否合理，如检查郊区和邮政编码是否匹配）。 ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.5** | 验证URL重定向和转发的目标地址都在白名单中，或者在重定向到可能不受信任的内容时显示警告。 | ✓ | ✓ | ✓ | 601 |

## V5.2 过滤和沙盒化

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.2.1** | 验证所有来自“所见即所得”编辑器或类似的不受信任的HTML输入，都已经通过HTML过滤库或框架功能，进行了适当的净化。 ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.2.2** | 验证非结构化数据是否经过消毒处理，以执行安全措施，如允许的字符集和长度。 | ✓ | ✓ | ✓ | 138 |
| **5.2.3** | 验证应用程序在传递给邮件系统之前，对用户的输入进行过滤，以防止SMTP或IMAP注入。 | ✓ | ✓ | ✓ | 147 |
| **5.2.4** | 验证应用程序是否避免使用eval()或其他动态代码执行功能。在没有其他选择的情况下，任何被包含的用户输入必须在执行前进行过滤或沙箱处理。 | ✓ | ✓ | ✓ | 95 |
| **5.2.5** | 验证应用程序是否对相关的用户输入进行过滤或沙箱处理，来防止模板注入攻击。 | ✓ | ✓ | ✓ | 94 |
| **5.2.6** | 验证应用程序是否通过验证或净化不受信任的数据或HTTP文件元数据（如文件名和URL输入字段），并使用协议、域、路径和端口的白名单，来防止SSRF攻击。 | ✓ | ✓ | ✓ | 918 |
| **5.2.7** | 验证应用程序是否过滤、禁用或沙盒处理了用户提供的可扩展矢量图（SVG）脚本内容，特别是与内联脚本产生的XSS有关的内容，以及外部对象。 | ✓ | ✓ | ✓ | 159 |
| **5.2.8** | 验证应用程序是否对用户提供的模板语言内容（脚本或表达式，如Markdown、CSS或XSL样式表、BBCode或类似内容）进行过滤、禁用或沙盒处理。 | ✓ | ✓ | ✓ | 94 |

## V5.3 输出编码和预防注入

靠近或邻近当前解释器的输出编码，对应用程序的安全至关重要。通常情况下，输出编码并不持久化，而是用于在适当的输出环境中使输出安全，以便立即使用。不进行输出编码，将最终形成一个不安全、可注入的应用程序。

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.3.1** | 验证输出编码是否与所需的解释器和环境相关。例如，根据HTML值、HTML属性、JavaScript、URL参数、HTTP头、SMTP等上下文的要求，使用专门的编码器，特别是来自不可信任的输入（如带有Unicode或单引号的名字，如ねこ或O'Hara）。 ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.3.2** | 验证输出编码是否保留了用户选择的字符集和地域，从而使任何Unicode字符点都能得到有效和安全的处理。 ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 176 |
| **5.3.3** | 验证上下文感知，最好是自动——或者最差也是手动——转义输出，以防止反射、存储或基于DOM的XSS。 ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 79 |
| **5.3.4** | 验证数据选择或数据库查询（如 SQL、HQL、ORM、NoSQL）是否使用参数化查询、ORM、实体框架，或以其他方式防止数据库注入攻击。 ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.5** | 验证在没有参数化或更安全机制的情况下，使用特定上下文的输出编码来防止注入攻击，例如使用SQL转义来防止SQL注入。 ([C3, C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.6** | 验证应用程序是否可以防止JSON注入攻击、JSON eval攻击和JavaScript表达式评估。 ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 830 |
| **5.3.7** | 验证应用程序可以防止LDAP注入漏洞，或者已经实施了特定的安全控制来防止LDAP注入。 ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 90 |
| **5.3.8** | 验证应用程序是否能防止操作系统命令注入，以及操作系统调用是否使用参数化的操作系统查询或使用上下文命令行输出编码。 ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 78 |
| **5.3.9** | 验证应用程序是否能防止本地文件包含（LFI）或远程文件包含（RFI）攻击。 | ✓ | ✓ | ✓ | 829 |
| **5.3.10** | 验证应用程序是否能防止XPath注入或XML注入攻击。 ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 643 |

注意：使用参数化查询或转义SQL并不总是足够的；表和列名、ORDER BY等不能被转义。若在这些字段中转义用户提供的数据，会导致查询失败或SQL注入。

注意：SVG格式在几乎所有情况下都明确允许ECMA脚本，所以可能无法完全阻止所有的SVG XSS向量。如果需要上传SVG，我们强烈建议将这些上传的文件作为text/plain提供，或者使用一个单独的“用户提供内容”域，以防止成功的XSS接管应用程序。

## V5.4 内存、字符串和非托管代码

以下要求仅在应用程序使用系统语言或非托管代码时适用。

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.4.1** | 验证应用程序是否使用内存安全字符串、更安全的内存复制和指针运算，以检测或防止堆栈、缓冲区或堆溢出。 | | ✓ | ✓ | 120 |
| **5.4.2** | 验证格式化字符串不接受潜在的有害输入，并且是常量。 | | ✓ | ✓ | 134 |
| **5.4.3** | 验证运用了符号、范围和输入验证技术来防止整数溢出。 | | ✓ | ✓ | 190 |

## V5.5 预防反序列化

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.5.1** | 验证序列化对象是否使用完整性检查或加密，以防止恶意对象的创建或数据篡改。 ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 502 |
| **5.5.2** | 验证应用程序正确限制 XML 解析器，使其只使用最严格的配置，并确保禁用不安全的功能，如解析外部实体，以防止 XML 外部实体注入（XXE）攻击。 | ✓ | ✓ | ✓ | 611 |
| **5.5.3** | 验证自定义代码和第三方库（如JSON、XML和YAML解析器）禁止或限制不受信任数据的反序列化。 | ✓ | ✓ | ✓ | 502 |
| **5.5.4** | 验证在浏览器或基于 JavaScript 的后端解析 JSON 时，使用 JSON.parse 来解析 JSON 文档。不使用 eval() 来解析 JSON。 | ✓ | ✓ | ✓ | 95 |

## 参考文献

有关更多信息，请参阅：

* [OWASP Testing Guide 4.0: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Cheat Sheet: Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution.html)
* [OWASP LDAP Injection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client Side Testing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client_Side_Testing/)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [XML External Entity (XXE) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)

有关自动转义的更多信息，请参阅：

* [Reducing XSS by way of Automatic Context-Aware Escaping in Template Systems](https://googleonlinesecurity.blogspot.com/2009/03/reducing-xss-by-way-of-automatic.html)
* [AngularJS Strict Contextual Escaping](https://docs.angularjs.org/api/ng/service/$sce)
* [AngularJS ngBind](https://docs.angularjs.org/api/ng/directive/ngBind)
* [Angular Sanitization](https://angular.io/guide/security#sanitization-and-security-contexts)
* [Angular Security](https://angular.io/guide/security)
* [ReactJS Escaping](https://reactjs.org/docs/introducing-jsx.html#jsx-prevents-injection-attacks)
* [Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

有关反序列化的更多信息，请参阅：

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [OWASP Deserialization of Untrusted Data Guide](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)
