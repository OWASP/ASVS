# V14 配置

## 控制目标

确保经过验证的应用程序具有：

* 一个安全的、可重复的、可自动化的构建环境。
* 加固第三方库、依赖和配置管理，使应用不包括过时的或不安全的组件。

应用程序开箱即用配置应该是安全的，可以放在互联网上，这意味着安全的开箱配置。

## V14.1 构建和部署

构建管道是可重复安全性的基础——每次发现不安全的东西时，都可以在源代码、构建或部署脚本中解决它，并自动进行测试。我们强烈鼓励使用自动化的构建管道来执行安全和依赖检查，这些检查会警告或破坏构建，以防止已知的安全问题被部署到生产环境中。不定期执行的手动步骤会直接导致可避免的安全错误。

随着行业向DevSecOps模式的转变，必须确保部署和配置的持续可用性和完整性，以实现“已知良好”的状态。在过去，如果一个系统被入侵，需要几天到几个月的时间来证明没有进一步的入侵发生。今天，随着软件定义的基础设施、零停机时间的快速A/B部署和自动化容器构建的出现，自动和持续地构建、加固和部署一个“已知良好”的替代品来替代任何被入侵的系统，是有可能的。

如果传统模式仍然存在，那么就必须采取手动步骤来加固和备份该配置，以便及时用高完整性的、未受损害的系统快速替换受损害的系统。

遵守本节的规定要求一个自动化的构建系统，以及对构建和部署脚本的访问。

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.1.1** | 验证应用程序的构建和部署过程是以安全和可重复的方式进行的，如 CI / CD 自动化、自动配置管理和自动部署脚本。 | | ✓ | ✓ | |
| **14.1.2** | 验证编译器标志的配置是否配置为启用所有可用的缓冲区溢出保护和警告，包括堆栈随机化、数据执行保护，并在发现不安全的指针、内存、格式字符串、整数或字符串操作时中断构建。 | | ✓ | ✓ | 120 |
| **14.1.3** | 验证服务器配置是否按照应用程序服务器和所使用框架的建议进行了加固。 | | ✓ | ✓ | 16 |
| **14.1.4** | 验证应用程序、配置和所有依赖项是否可以使用自动部署脚本重新部署、在合理的时间内根据记录和测试的运行手册构建，或者及时从备份中恢复。 | | ✓ | ✓ | |
| **14.1.5** | 验证授权管理员可以验证所有安全相关配置的完整性，以发现篡改行为。 | | | ✓ | |

## V14.2 依赖

依赖管理，对于任何类型应用程序的安全运行都至关重要。未能及时更新过时的或不安全的依赖，是迄今为止最大和最昂贵攻击的根本原因。

注意：在 L1 ，14.2.1 的合规性与客户端和其他库、组件的观察或检测有关，而不是更准确的构建时静态代码分析或依赖分析。这些更准确的技术可根据需要在访谈中发现。

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.2.1** | 验证所有组件都是最新的，最好是在构建或编译时使用依赖检查工具。 ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1026 |
| **14.2.2** | 验证所有不需要的功能、文档、示例应用程序和配置均已被删除。 | ✓ | ✓ | ✓ | 1002 |
| **14.2.3** | 应用资产，例如JavaScript库、CSS或网页字体，如果被托管在外部的内容分发网络（CDN）或供应商，则验证使用子资源完整性（SRI）来验证该资产的完整性。 | ✓ | ✓ | ✓ | 829 |
| **14.2.4** | 验证第三方组件来自预先定义的、可信的和持续维护的资源库。 ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 829 |
| **14.2.5** | 验证是否维护了正在使用中的所有第三方库的软件材料清单（SBOM）。 ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **14.2.6** | 验证通过沙盒或封装第三方库来减少攻击面，只将必需的行为暴露在应用程序中。 ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |

## V14.3 意外安全泄露

应加强生产配置以防止常见攻击，例如调试控制台，提高跨站点脚本 (XSS) 和远程文件包含 (RFI) 攻击的门槛，并消除琐碎的信息发现“漏洞”，这是许多渗透测试报告中不受欢迎的标志。 其中许多问题很少被评为重大风险，但它们可跟其他漏洞联系在一起。如果这些问题在默认情况下不存在，那就提高了大多数攻击的门槛。

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.3.1** | [删除，与7.4.1重复] | | | | |
| **14.3.2** | 验证Web或应用服务器和应用框架的调试模式在生产中是否被禁用，以消除调试功能、开发人员控制台和非预期的安全披露。 | ✓ | ✓ | ✓ | 497 |
| **14.3.3** | 验证HTTP标头或HTTP响应的任何部分不暴露系统组件的详细版本信息。 | ✓ | ✓ | ✓ | 200 |

## V14.4 HTTP 安全标头

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.4.1** | 验证每个HTTP响应都包含一个 Content-Type 头。如果内容类型是 text/* 、 /+xml 和 application/xml ，还要指定一个安全的字符集（如UTF-8，ISO-8859-1）。内容必须与提供的Content-Type头相匹配。 | ✓ | ✓ | ✓ | 173 |
| **14.4.2** | 验证所有 API 响应是否包含 Content-Disposition: attachment; filename="api.json" 标头（或内容类型的其他适当文件名）。 | ✓ | ✓ | ✓ | 116 |
| **14.4.3** | 验证内容安全策略 (CSP) 响应标头是否到位，有助于减轻对 HTML、DOM、JSON 和 JavaScript 注入漏洞等 XSS 攻击的影响。 | ✓ | ✓ | ✓ | 1021 |
| **14.4.4** | 验证所有响应是否包含 X-Content-Type-Options: nosniff 标头。 | ✓ | ✓ | ✓ | 116 |
| **14.4.5** | 验证所有响应和所有子域中是否包含 Strict-Transport-Security 标头，例如 Strict-Transport-Security: max-age=15724800; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **14.4.6** | 验证是否包含合适的 Referrer-Policy 标头，以避免通过 Referer 标头将 URL 中的敏感信息暴露给不受信任的各方。 | ✓ | ✓ | ✓ | 116 |
| **14.4.7** | 验证网络应用程序的内容在默认情况下不能被嵌入第三方网站，只有在必要时，才允许使用合适的Content-Security-Policy: frame-ancestors和X-Frame-Options响应头嵌入确切的资源。 | ✓ | ✓ | ✓ | 1021 |

## V14.5 HTTP 请求头验证

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.5.1** | 验证应用服务器只接受应用/API使用的HTTP方法，包括预检请求的OPTIONS，并对使应用上下文无效的请求进行记录/警告。 | ✓ | ✓ | ✓ | 749 |
| **14.5.2** | 验证提供的 Origin 标头是否不用于身份验证或访问控制决策，因为 Origin 标头很容易被攻击者更改。 | ✓ | ✓ | ✓ | 346 |
| **14.5.3** | 验证跨域资源共享 (CORS) 的 Access-Control-Allow-Origin 标头是否使用受信任域和子域的严格白名单匹配。并且不支持“null”源。 | ✓ | ✓ | ✓ | 346 |
| **14.5.4** | 验证由受信任的代理或 SSO 设备添加的 HTTP 标头（例如bearer令牌）是否已通过应用程序的身份验证。 | | ✓ | ✓ | 306 |

## 参考文献

有关更多信息，请参阅：

* [OWASP Web Security Testing Guide 4.1: Testing for HTTP Verb Tampering]( https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* 将 Content-Disposition 添加到 API 响应，有助于防止许多基于客户端和服务器之间的MIME类型误解的攻击，并且“filename”选项特别有助于防止 [Reflected File Download attacks.](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Sandboxing third party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
