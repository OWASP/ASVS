# V9 通讯

## 控制目标

确保经过验证的应用程序满足以下高级要求：

* 要求 TLS 或强加密，与内容的敏感性无关。
* 遵循最新指南，包括：
  * 配置建议
  * 首选算法和密码
* 避免使用弱的或即将被废弃的算法和密码，除非是最后的手段。
* 禁用已废弃或已知不安全的算法和密码。

在这些要求范围内：

* 了解业界对安全TLS配置的建议，因为它经常变化（往往是由于现有算法和密码的灾难性破坏）。
* 使用最新版本的TLS配置审查工具，来配置首选顺序和算法选择。
* 定期检查你的配置，以确保安全通信始终存在并有效。

## V9.1 客户端通信安全

确保所有客户端消息都通过加密网络发送，使用TLS 1.2或更高版本。
使用最新的工具定期检查客户端配置。

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.1.1** | 验证所有客户端连接都使用了TLS，并且不会降级到不安全或未加密的通信。 ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | 使用最新的TLS测试工具，验证是否只启用了强密码套件，并将最强的密码套件设置为首选。 | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | 验证只启用最新推荐版本的TLS协议，如TLS 1.2和TLS 1.3。最新版本的TLS协议应该是首选项。 | ✓ | ✓ | ✓ | 326 |

## V9.2 服务器通信安全

服务器通信不仅仅是 HTTP。与其他系统的安全连接，例如监控系统、管理工具、远程访问和 ssh、中间件、数据库、大型机、合作伙伴或外部源系统——必须到位。所有这些都必须加密，以防止“外面安全，里面被轻易截获”。

| # | 描述 | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.2.1** | 验证与服务器的连接是否使用受信任的TLS证书。在使用内部生成或自签名证书的情况下，必须将服务器配置为只信任特定的内部CA和特定的自签证书。所有其他的都应该被拒绝。 | | ✓ | ✓ | 295 |
| **9.2.2** | 确认所有入站和出站连接都使用了 TLS 等加密通信，包括管理端口、监控、身份验证、API 或 Web 服务调用、数据库、云、serverless、大型机、外部和合作伙伴的连接。服务器不得回退到不安全或未加密的协议。 | | ✓ | ✓ | 319 |
| **9.2.3** | 验证所有外部系统中与敏感信息/功能相关的加密连接，均已通过身份验证。 | | ✓ | ✓ | 287 |
| **9.2.4** | 验证是否启用并配置了正确的证书吊销，例如在线证书状态协议 (OCSP) Stapling。 | | ✓ | ✓ | 299 |
| **9.2.5** | 验证是否记录了后端TLS连接失败（的事件）。 | | | ✓ | 544 |

## 参考文献

有关更多信息，请参阅：

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* [OWASP - Pinning Guide](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)
* Notes on “Approved modes of TLS”:
    * In the past, the ASVS referred to the US standard FIPS 140-2, but as a global standard, applying US standards can be difficult, contradictory, or confusing to apply.
    * A better method of achieving compliance with section 9.1 would be to review guides such as [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) or [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known and up to date TLS evaluation tools to obtain a desired level of security.