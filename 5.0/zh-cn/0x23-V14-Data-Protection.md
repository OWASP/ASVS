# V14 数据保护

## 控制目标

应用无法掌控所有使用方式和用户行为，因此应实施控制，限制对客户端设备上敏感数据的未授权访问。

本章说明如何识别需要保护的数据、如何确定保护方式，以及应采用哪些机制、避免哪些常见问题。

数据保护还要考虑批量提取、批量修改和过度使用数据。不同系统对“异常行为”的定义差异很大，必须结合威胁模型和业务风险判断。在 ASVS 中，这类行为的检测要求见“安全日志和错误处理”章节，使用限制见“验证和业务逻辑”章节。

## V14.1 数据保护文档

保护数据的前提是先识别哪些数据属于敏感数据，并划分敏感等级。不同等级的数据需要采用不同强度的保护措施。

有多种隐私法规和法律会影响应用必须如何存储、使用和传输敏感个人信息。本节不再试图重复这些数据保护或隐私法律，而是聚焦于保护敏感数据的关键技术考虑。请查阅当地法律法规，并按需咨询合格的隐私专家或律师。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **14.1.1** | 验证应用已经识别其创建和处理的所有敏感数据，并为每类数据指定保护等级。仅经过编码、很容易恢复原文的数据也属于识别范围，例如 Base64 字符串或 JWT 中的明文载荷。划分等级时，必须考虑应用需要遵守的数据保护和隐私法律、法规及标准。 | 2 |
| **14.1.2** | 验证每个敏感数据保护等级都有书面的保护要求。要求必须涵盖但不限于加密、完整性校验、保留期限、日志记录方式、日志中敏感数据的访问控制、数据库级加密、隐私保护和隐私增强技术，以及其他保密措施。 | 2 |

## V14.2 通用数据保护

本节给出数据保护的具体要求。多数要求针对意外泄露等特定问题，同时也要求按照每项数据的保护等级落实相应控制。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **14.2.1** | 验证向服务器发送敏感数据时，只把数据放在 HTTP 消息正文或头字段中。URL 和查询字符串不得包含 API 密钥、会话令牌等敏感信息。 | 1 |
| **14.2.2** | 验证应用防止负载均衡器、应用缓存等服务端组件缓存敏感数据，或确保这些数据在使用后得到安全清除。 | 2 |
| **14.2.3** | 验证应用不会把已经认定为敏感的数据发送给用户跟踪器等不可信方，防止数据脱离应用控制后被不必要地收集。 | 2 |
| **14.2.4** | 验证应用按照相应保护等级的文档要求，对敏感数据实施加密、完整性校验、保留期限、日志记录、日志访问控制、隐私保护和隐私增强等措施。 | 2 |
| **14.2.5** | 验证缓存系统仅缓存同时满足以下条件的响应：响应的 `Content-Type` 与该资源应有的类型一致，并且不包含动态生成的敏感内容。如果请求的文件不存在，Web 服务器应返回 404 或 302 响应，而不是返回另一个实际存在的文件，以防止 Web 缓存欺骗（Web Cache Deception）攻击。 | 3 |
| **14.2.6** | 验证应用只返回实现当前功能所必需的最少敏感数据。例如，只返回信用卡号的部分数字，而不是完整卡号。如果需要完整数据，应在用户界面中将其遮蔽，除非用户明确选择查看。 | 3 |
| **14.2.7** | 验证敏感信息受数据保留分类规则约束，确保过时或不再需要的数据会被自动删除、按既定计划删除，或在具体情况需要时删除。 | 3 |
| **14.2.8** | 验证应用会从用户提交文件的元数据中删除敏感信息；只有用户明确同意保留时才可以例外。 | 3 |

## V14.3 客户端数据保护

本节包含防止数据在应用客户端或用户代理侧以特定方式泄露的要求。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **14.3.1** | 验证客户端关闭或会话终止后，客户端存储（例如浏览器 DOM）中的已认证数据会被清除。`Clear-Site-Data` 响应头可以帮助完成清理；但即使会话终止时无法连接服务器，客户端也应能够自行清除数据。 | 1 |
| **14.3.2** | 验证应用设置了足以防止缓存的 HTTP 响应头字段（即 `Cache-Control: no-store`），使敏感数据不会被浏览器缓存。 | 2 |
| **14.3.3** | 验证 localStorage、sessionStorage、IndexedDB、Cookie 等浏览器存储中不保存敏感数据；会话令牌是唯一例外。 | 2 |

## 参考资料

更多信息，另见：

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
