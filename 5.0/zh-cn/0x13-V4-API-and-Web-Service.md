# V4 API 和 Web 服务

## 控制目标

对于向 Web 浏览器或其他调用方开放 API 的应用（通常使用 JSON、XML 或 GraphQL），需要考虑若干特有的安全问题。本章介绍应采用的相关安全配置和机制。

认证、会话管理和输入验证等其他章节的要求同样适用于 API。因此，理解和测试本章时，必须结合标准中的其他相关要求。

## V4.1 通用 Web 服务安全

本节介绍 Web 服务普遍适用的安全要求，包括最基本的安全配置和防护措施。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **4.1.1** | 验证每个包含消息正文的 HTTP 响应都带有 Content-Type 头，且其值与实际响应内容一致。对于 IANA Media Types 规定应包含字符集的类型（例如 `text/`、`/+xml` 和 `/xml`），还必须通过 `charset` 参数指定安全的字符编码，例如 UTF-8 或 ISO-8859-1。 | 1 |
| **4.1.2** | 验证只有供用户通过浏览器访问的端点，才会自动把 HTTP 请求重定向到 HTTPS。其他服务和端点不得进行这种透明重定向。否则，客户端误用未加密 HTTP 发送敏感数据后，自动重定向可能掩盖已经发生的数据泄露。 | 2 |
| **4.1.3** | 验证应用所使用且由中间层设置的任何 HTTP 头字段，例如负载均衡器、Web 代理或 BFF 服务设置的头字段，均不能被最终用户覆盖。此类头字段可能包括 X-Real-IP、X-Forwarded-* 或 X-User-ID。 | 2 |
| **4.1.4** | 验证应用或 API 只允许明确支持的 HTTP 方法，包括需要用于预检请求的 OPTIONS；所有未使用的方法都必须禁用。 | 3 |
| **4.1.5** | 验证对高度敏感或经过多个系统的请求或业务操作使用逐消息数字签名，在传输保护的基础上提供额外保证。 | 3 |

## V4.2 HTTP 消息结构验证

本节说明应如何验证 HTTP 消息的结构和头字段，以防止请求走私、响应拆分、头注入，以及由过长 HTTP 消息导致的拒绝服务等攻击。

这些要求适用于一般 HTTP 消息处理和生成，但在不同 HTTP 版本之间转换 HTTP 消息时尤其重要。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **4.2.1** | 验证所有应用组件（包括负载均衡器、防火墙和应用服务器）都按照相应 HTTP 版本的规则确定传入消息的边界，以防范 HTTP 请求走私。对于 HTTP/1.x，如果消息中含有 Transfer-Encoding 头，则必须按照 RFC 2616 忽略 Content-Length。对于 HTTP/2 或 HTTP/3，如果消息中含有 Content-Length，接收方必须确认其值与 DATA 帧的实际长度一致。 | 2 |
| **4.2.2** | 验证应用生成 HTTP 消息时，Content-Length 头所声明的长度与 HTTP 分帧机制确定的实际内容长度一致，以防范请求走私。 | 3 |
| **4.2.3** | 验证应用既不发送也不接受含有连接专用头字段（例如 Transfer-Encoding）的 HTTP/2 或 HTTP/3 消息，以防范响应拆分和头注入。 | 3 |
| **4.2.4** | 验证应用只接受头字段名称和值中均不含 CR（`\r`）、LF（`\n`）或 CRLF（`\r\n`）序列的 HTTP/2 和 HTTP/3 请求，以防范头注入。 | 3 |
| **4.2.5** | 验证应用的后端或前端在构造并发送请求时，会通过验证、净化或其他机制限制 URI（例如 API 调用地址）和 HTTP 请求头字段（例如 `Authorization` 或 `Cookie`）的长度，避免接收方因内容过长而拒绝请求。过长的请求可能造成拒绝服务；例如，发送过长的请求（如过长的 Cookie 头字段）可能导致服务器始终返回错误状态。 | 3 |

## V4.3 GraphQL

GraphQL 越来越多地用于构建数据密集型客户端，使客户端无需与多个后端服务紧密耦合。本节介绍使用 GraphQL 时需要注意的安全问题。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **4.3.1** | 验证应用通过查询允许列表、查询深度限制、数量限制或查询成本分析，防止复杂的嵌套查询耗尽 GraphQL 服务或数据层资源并造成拒绝服务（DoS）。 | 2 |
| **4.3.2** | 验证生产环境已经禁用 GraphQL 内省查询；如果该 GraphQL API 本来就需要提供给外部使用方，则可以例外。 | 2 |

## V4.4 WebSocket

WebSocket 是一种通信协议，可在单个 TCP 连接上提供同时双向通信通道。它于 2011 年由 IETF 以 RFC 6455 标准化；虽然它被设计为通过 HTTP 端口 443 和 80 工作，但它不同于 HTTP。

本节提供关键安全要求，用于防止专门利用这种实时通信通道的通信安全和会话管理相关攻击。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **4.4.1** | 验证所有 WebSocket 连接都使用基于 TLS 的 WebSocket（WSS）。 | 1 |
| **4.4.2** | 验证初次进行 HTTP WebSocket 握手时，会对照应用允许的源列表检查 Origin 头字段。 | 2 |
| **4.4.3** | 验证无法沿用应用原有会话管理机制时，WebSocket 使用专用的会话令牌，并且这些令牌满足相关的会话管理安全要求。 | 2 |
| **4.4.4** | 验证把现有 HTTPS 会话升级为 WebSocket 通道时，专用 WebSocket 会话令牌最初是通过已经认证的 HTTPS 会话获取或验证的。 | 2 |

## 参考资料

更多信息，另见：

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* 来自 [graphql.org](https://graphql.org/learn/authorization/) 和 [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods) 的 GraphQL 授权资源。
* [OWASP Web Security Testing Guide: GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [OWASP Web Security Testing Guide: Testing WebSockets](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)
