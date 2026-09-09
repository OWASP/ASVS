# V3 Web 前端安全

## 控制目标

本章重点防范针对 Web 前端的攻击，不适用于纯机器间通信的系统。

## V3.1 Web 前端安全文档

本节概述应用文档中应明确规定的浏览器安全功能。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **3.1.1** | 验证应用文档列明了浏览器必须支持的安全功能，例如 HTTPS、HTTP 严格传输安全（HSTS）、内容安全策略（CSP）及其他 HTTP 安全机制。文档还必须说明浏览器不支持其中某项功能时，应用应如何处理，例如警告用户或拒绝访问。 | 3 |

## V3.2 非预期内容解释

如果浏览器在错误的上下文中渲染内容或调用功能，就可能显示甚至执行恶意内容。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **3.2.1** | 验证应用采用了安全控制，防止浏览器在错误的上下文中渲染 HTTP 响应中的内容或功能，例如直接访问 API、用户上传的文件或其他资源时。可采用的措施包括：只有当 `Sec-Fetch-*` 等 HTTP 请求头表明上下文正确时才返回内容；在 Content-Security-Policy 头中使用 `sandbox` 指令；或者在 Content-Disposition 头中指定 `attachment`。 | 1 |
| **3.2.2** | 验证只需显示为文本而不应渲染成 HTML 的内容，会通过安全渲染函数（例如 `createTextNode` 或 `textContent`）处理，防止其中的 HTML 或 JavaScript 被意外执行。 | 1 |
| **3.2.3** | 验证客户端 JavaScript 通过显式声明变量、进行严格类型检查、不在 `document` 对象上存储全局变量，以及隔离命名空间等方式，防范 DOM Clobbering。 | 3 |

## V3.3 Cookie 设置

本节说明如何安全配置敏感 Cookie，以尽可能确认它们确实由应用创建，并防止其内容泄露或遭到篡改。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **3.3.1** | 验证 Cookie 已设置 `Secure` 属性；如果 Cookie 名称未使用 `__Host-` 前缀，则必须使用 `__Secure-` 前缀。 | 1 |
| **3.3.2** | 验证每个 Cookie 都根据自身用途设置了合适的 `SameSite` 属性值，以降低用户界面伪装攻击和浏览器请求伪造攻击（通常称为跨站请求伪造，即 CSRF）的风险。 | 2 |
| **3.3.3** | 验证 Cookie 名称使用 `__Host-` 前缀，除非这些 Cookie 被明确设计为与其他主机共享。 | 2 |
| **3.3.4** | 验证当 Cookie 的值不应由客户端脚本访问时（例如会话令牌），该 Cookie 设置了 `HttpOnly` 属性，并且该值只能通过 `Set-Cookie` 头字段传输给客户端。 | 2 |
| **3.3.5** | 验证应用写入的 Cookie，其名称和值合计不超过 4096 字节。浏览器不会保存过大的 Cookie，也不会在后续请求中发送它，这可能导致依赖该 Cookie 的功能无法使用。 | 3 |

## V3.4 浏览器安全机制头

本节说明 HTTP 响应应设置哪些安全头，以便浏览器在处理响应时启用相应的安全功能和限制。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **3.4.1** | 验证所有响应都包含 Strict-Transport-Security 头字段，以强制执行 HTTP 严格传输安全（HSTS）策略。必须定义至少 1 年的最大有效期；对于 L2 及以上，策略还必须适用于所有子域名。 | 1 |
| **3.4.2** | 验证应用将跨源资源共享（CORS）的 Access-Control-Allow-Origin 响应头字段设置为固定值，或在使用 Origin 请求头字段的值时，对照可信源允许列表验证该值。需要使用 `Access-Control-Allow-Origin: *` 时，响应中不得包含任何敏感信息。 | 1 |
| **3.4.3** | 验证 HTTP 响应包含 Content-Security-Policy 头，并通过其中的指令限制浏览器只能加载和执行可信内容或资源，从而限制恶意 JavaScript 的执行。最低要求是制定全局策略：包含 `object-src 'none'` 和 `base-uri 'none'`，并为其他资源定义允许列表，或者采用 nonce 或哈希。L3 应用必须针对每个响应定义使用 nonce 或哈希的策略。 | 2 |
| **3.4.4** | 验证所有 HTTP 响应都包含 `X-Content-Type-Options: nosniff` 头字段，禁止浏览器通过内容嗅探来猜测 MIME 类型。响应的 `Content-Type` 必须与目标资源类型相符；例如，样式资源只有在响应类型为 `text/css` 时才会被浏览器接受。设置该头字段还会启用浏览器的跨源读取阻止（CORB）功能。 | 2 |
| **3.4.5** | 验证应用设置了来源信息策略（referrer policy），防止技术敏感数据通过 `Referer` 请求头泄露给第三方服务。可以通过 Referrer-Policy 响应头或 HTML 元素属性来设置。敏感数据可能包括 URL 路径和查询参数；对于非公开的内部应用，还可能包括主机名。 | 2 |
| **3.4.6** | 验证 Web 应用在每个 HTTP 响应的 Content-Security-Policy 头中设置了 `frame-ancestors` 指令。默认情况下应禁止嵌入应用内容，仅在必要时允许嵌入特定资源。虽然浏览器仍支持 X-Frame-Options，但该头已经过时，不应再依赖它。 | 2 |
| **3.4.7** | 验证 Content-Security-Policy 头指定了策略违规报告的接收位置。 | 3 |
| **3.4.8** | 验证所有会触发文档渲染的 HTTP 响应（例如 Content-Type 为 `text/html` 的响应）都包含 Cross-Origin-Opener-Policy 头字段，并根据需要使用 `same-origin` 或 `same-origin-allow-popups` 指令。这样可以防止攻击者滥用不同页面对 `Window` 对象的共享访问，例如实施标签页劫持（tabnabbing）或框架计数（frame counting）攻击。 | 3 |

## V3.5 浏览器源隔离

服务端收到敏感功能的请求时，应用必须确认请求来自应用自身或可信方，而不是攻击者伪造的请求。

此处的敏感功能可以包括接受已认证和未认证用户的表单提交（例如认证请求）、改变状态的操作，或消耗大量资源的功能（例如数据导出）。

主要防护机制包括浏览器的同源策略（针对 JavaScript）和 Cookie 的 SameSite 规则。CORS 预检也是常见的防护手段：对设计为允许跨源调用的端点，这一机制至关重要；对不应跨源调用的端点，它也能帮助阻止伪造请求。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **3.5.1** | 验证应用在不依赖 CORS 预检来保护敏感功能时，会检查请求是否确实来自应用自身。可采用并验证防伪令牌，或者要求请求携带不属于 CORS 安全列表的额外 HTTP 头。这样可以防范浏览器请求伪造攻击，即通常所说的跨站请求伪造（CSRF）。 | 1 |
| **3.5.2** | 验证应用依赖 CORS 预检来保护敏感功能时，任何不会触发预检的请求都无法调用该功能。为此，应用可能需要检查 `Origin` 和 `Content-Type` 请求头，或要求请求携带不属于 CORS 安全列表的额外头字段。 | 1 |
| **3.5.3** | 验证访问敏感功能的 HTTP 请求使用合适的 HTTP 方法，例如 POST、PUT、PATCH 或 DELETE，而不是 HTTP 规范定义为“安全”的方法，例如 HEAD、OPTIONS 或 GET。或者，可以严格验证 Sec-Fetch-* 请求头字段，确保请求并非来自不合适的跨源调用、导航请求，或资源加载（例如图片源）等非预期来源。 | 1 |
| **3.5.4** | 验证不同应用分别托管在不同的主机名下，以充分利用同源策略和 Cookie 的主机名限制，约束一个源中的文档或脚本与另一个源中的资源交互。 | 2 |
| **3.5.5** | 验证通过 `postMessage` 接口收到消息时，会检查消息来源和格式；来源不可信或格式不合法的消息必须丢弃。 | 2 |
| **3.5.6** | 验证应用任何位置都未启用 JSONP 功能，以避免跨站脚本包含（XSSI）攻击。 | 3 |
| **3.5.7** | 验证需要授权的数据不会包含在脚本资源响应（例如 JavaScript 文件）中，以防止跨站脚本包含（XSSI）攻击。 | 3 |
| **3.5.8** | 验证只有在符合预期时，才允许以用户身份加载或嵌入需要认证的资源，例如图片、视频、脚本和其他文档。可以严格检查 `Sec-Fetch-*` 请求头，排除非预期的跨源调用；也可以设置严格的 Cross-Origin-Resource-Policy 响应头，让浏览器阻止不符合策略的内容。 | 3 |

## V3.6 外部资源完整性

本节为在第三方站点上安全托管内容提供指导。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **3.6.1** | 验证 JavaScript 库、CSS、Web 字体等客户端资源只有同时满足以下条件时，才托管在外部站点（例如 CDN）：资源是静态的、带有明确版本，并通过子资源完整性（SRI）校验其完整性。无法满足这些条件时，应针对每项资源记录安全决策，说明理由。 | 3 |

## V3.7 其他浏览器安全考虑

本节包含客户端浏览器安全所需的其他各类安全控制和现代浏览器安全功能。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **3.7.1** | 验证应用只使用仍受支持且被认为安全的客户端技术。不符合此要求的技术示例包括 NSAPI 插件、Flash、Shockwave、ActiveX、Silverlight、NACL 或客户端 Java 小程序。 | 2 |
| **3.7.2** | 验证应用只有在目标主机名或域名位于允许列表中时，才自动把用户重定向到应用控制范围之外。 | 2 |
| **3.7.3** | 验证用户将被重定向到应用控制范围之外的 URL 时，应用会事先提示用户，并允许用户取消跳转。 | 3 |
| **3.7.4** | 验证应用的顶级域名（例如 `site.tld`）已经加入 HSTS 公共预加载列表。这样，主流浏览器会内置该应用必须使用 TLS 的规则，而不只是依赖 Strict-Transport-Security 响应头。 | 3 |
| **3.7.5** | 验证浏览器不支持应用所需的安全功能时，应用按照文档规定进行处理，例如警告用户或拒绝访问。 | 3 |

## 参考资料

更多信息，另见：

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
* [OWASP DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)
