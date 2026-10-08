# V17 WebRTC

## 控制目标

Web 实时通信（WebRTC）使应用能够实时交换语音、视频和数据。随着 WebRTC 日益普及，保护相关基础设施也越来越重要。本章面向开发、托管或集成 WebRTC 系统的相关方，给出相应的安全要求。

WebRTC 市场大致可分为三个部分：

1. 产品开发者：开发并提供专有或开源 WebRTC 产品与解决方案的厂商，重点是为其他组织提供稳健、安全的 WebRTC 技术。

2. 通信平台即服务（CPaaS）提供方：通过 API、SDK 和必要的基础设施或平台提供 WebRTC 能力。它们既可能采用第一类厂商的产品，也可能自行开发 WebRTC 软件。

3. 服务提供方：采用产品开发者或 CPaaS 提供方的产品，或者自行开发 WebRTC 解决方案，为在线会议、医疗、在线教育等依赖实时通信的场景提供应用。

这里概述的安全要求主要面向以下产品开发者、CPaaS 和服务提供方：

* 使用开源解决方案构建其 WebRTC 应用。
* 将商业 WebRTC 产品作为其基础设施的一部分。
* 使用内部开发的 WebRTC 解决方案，或将多个组件集成为统一服务。

如果开发人员完全通过 CPaaS 厂商提供的 SDK 和 API 使用 WebRTC，则本章要求并不适用。此时，大多数底层安全问题通常由 CPaaS 提供方负责，ASVS 这类通用标准也未必能完整覆盖开发人员需要关注的问题。

## V17.1 TURN 服务器

本节适用于自行运行 TURN（Traversal Using Relays around NAT）服务器的系统。TURN 服务器负责在受限网络中转发媒体流，但配置不当也会引入风险，因此需要正确过滤目标地址并防止资源耗尽。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **17.1.1** | 验证 TURN 服务禁止访问保留作特殊用途的 IP 地址，例如内部网络地址、广播地址和回环地址。此要求同时适用于 IPv4 和 IPv6。 | 2 |
| **17.1.2** | 验证合法用户尝试在 TURN 服务器上打开大量端口时，不会耗尽 TURN 服务的资源。 | 3 |

## V17.2 媒体

这些要求只适用于自行部署并运行 WebRTC 媒体服务器的系统，例如选择性转发单元（SFU）、多点控制单元（MCU）、录制服务器或网关服务器。媒体服务器处理并分发媒体流，其安全性直接关系到参与通信的各个客户端之间的通信安全。在 WebRTC 应用中，保护媒体流是重中之重，以防止窃听、篡改和拒绝服务攻击危及用户隐私和通信质量。

媒体服务器尤其需要防范洪泛攻击。可以采用速率限制、校验时间戳、使用同步时钟匹配实际时间间隔，以及管理缓冲区防止溢出并维持正确时序。某个媒体会话的数据包到达过快时，应丢弃多余的数据包。系统还应通过输入验证、安全处理整数溢出、防止缓冲区溢出和稳健的错误处理来抵御畸形数据包。

完全依赖 Web 浏览器之间点对点媒体通信，且没有中间媒体服务器参与的系统，不适用这些特定媒体相关安全要求。

本节提到在 WebRTC 中使用数据报传输层安全（Datagram Transport Layer Security，DTLS）。关于记录密码学密钥管理策略的要求位于“密码学”章节。关于符合安全要求的密码方法，可参考 ASVS 密码学附录，也可参考 NIST SP 800‑52 Rev. 2 或 BSI TR‑02102‑2（2025‑01 版）等文档。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **17.2.1** | 验证 DTLS 证书密钥按照书面的密码学密钥管理策略进行管理和保护。 | 2 |
| **17.2.2** | 验证媒体服务器配置为使用并支持获认可的 DTLS 密码套件，以及用于为安全实时传输协议建立密钥的 DTLS 扩展（DTLS-SRTP）的安全保护配置（protection profile）。 | 2 |
| **17.2.3** | 验证媒体服务器会校验安全实时传输协议（SRTP）的认证信息，防止实时传输协议（RTP）注入攻击导致拒绝服务，或将音频、视频插入媒体流。 | 2 |
| **17.2.4** | 验证媒体服务器在收到畸形安全实时传输协议（SRTP）数据包时，仍能正常处理传入的媒体流量。 | 2 |
| **17.2.5** | 验证媒体服务器在合法用户产生安全实时传输协议（SRTP）数据包洪泛时，仍能正常处理传入的媒体流量。 | 3 |
| **17.2.6** | 验证媒体服务器不受 DTLS `ClientHello` 竞态条件漏洞影响，验证方式为检查媒体服务器是否已知存在相关漏洞，或进行竞态条件测试。 | 3 |
| **17.2.7** | 验证与媒体服务器关联的音频或视频录制机制，在合法用户产生安全实时传输协议（SRTP）数据包洪泛时，仍能正常处理传入的媒体流量。 | 3 |
| **17.2.8** | 验证根据会话描述协议（SDP）的 `fingerprint` 属性校验 DTLS 证书，并在校验失败时终止媒体流，以确保媒体流的真实性。 | 3 |

## V17.3 信令

本节适用于自行运行 WebRTC 信令服务器的系统。信令用于协调点对点通信，必须能够抵御可能干扰会话建立或控制的攻击。

信令服务器必须能够安全处理畸形输入，并在高负载下保持可用。

| # | 描述 | 级别 |
| :---: | :--- | :---: |
| **17.3.1** | 验证信令服务器在洪泛攻击期间仍能处理合法的传入信令消息。这应通过在信令层实施速率限制来实现。 | 2 |
| **17.3.2** | 验证信令服务器在收到可能导致拒绝服务的畸形信令消息时，仍能正常处理合法信令消息。可采用的措施包括输入验证、安全处理整数溢出、防止缓冲区溢出，以及其他稳健的错误处理技术。 | 2 |

## 参考资料

更多信息，另见：

* WebRTC DTLS ClientHello DoS 的最佳文档包括 [Enable Security 面向安全专业人员的博客文章](https://www.enablesecurity.com/blog/novel-dos-vulnerability-affecting-webrtc-media-servers/) 以及相关的[面向 WebRTC 开发人员的白皮书](https://www.enablesecurity.com/blog/webrtc-hello-race-conditions-paper/)
* [RFC 3550 - RTP: A Transport Protocol for Real-Time Applications](https://www.rfc-editor.org/rfc/rfc3550)
* [RFC 3711 - The Secure Real-time Transport Protocol (SRTP)](https://datatracker.ietf.org/doc/html/rfc3711)
* [RFC 5764 - Datagram Transport Layer Security (DTLS) Extension to Establish Keys for the Secure Real-time Transport Protocol (SRTP))](https://datatracker.ietf.org/doc/html/rfc5764)
* [RFC 8825 - Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/info/rfc8825)
* [RFC 8826 - Security Considerations for WebRTC](https://www.rfc-editor.org/info/rfc8826)
* [RFC 8827 - WebRTC Security Architecture](https://www.rfc-editor.org/info/rfc8827)
* [DTLS-SRTP Protection Profiles](https://www.iana.org/assignments/srtp-protection/srtp-protection.xhtml)
