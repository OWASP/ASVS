# V17 WebRTC

## 控制目標

Web 實時通信（WebRTC）使應用能夠實時交換語音、視頻和資料。隨著 WebRTC 日益普及，保護相關基礎設施也越來越重要。本章面向開發、托管或整合 WebRTC 系統的相關方，給出相應的安全要求。

WebRTC 市場大致可分為三個部分：

1. 產品開發者：開發並提供專有或開源 WebRTC 產品與解決方案的廠商，重點是為其他組織提供穩健、安全的 WebRTC 技術。

2. 通信平台即服務（CPaaS）提供方：通過 API、SDK 和必要的基礎設施或平台提供 WebRTC 能力。它們既可能採用第一類廠商的產品，也可能自行開發 WebRTC 軟體。

3. 服務提供方：採用產品開發者或 CPaaS 提供方的產品，或者自行開發 WebRTC 解決方案，為在線會議、醫療、在線教育等依賴實時通信的場景提供應用。

這裡概述的安全要求主要面向以下產品開發者、CPaaS 和服務提供方：

* 使用開源解決方案建置其 WebRTC 應用。
* 將商業 WebRTC 產品作為其基礎設施的一部分。
* 使用內部開發的 WebRTC 解決方案，或將多個元件整合為統一服務。

如果開發人員完全通過 CPaaS 廠商提供的 SDK 和 API 使用 WebRTC，則本章要求並不適用。此時，大多數底層安全問題通常由 CPaaS 提供方負責，ASVS 這類通用標準也未必能完整覆蓋開發人員需要關注的問題。

## V17.1 TURN 伺服器

本節適用於自行執行 TURN（Traversal Using Relays around NAT）伺服器的系統。TURN 伺服器負責在受限網路中轉發媒體流，但組態不當也會引入風險，因此需要正確過濾目標位址並防止資源耗盡。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **17.1.1** | 驗證 TURN 服務禁止存取保留作特殊用途的 IP 位址，例如內部網路位址、廣播位址和回環位址。此要求同時適用於 IPv4 和 IPv6。 | 2 |
| **17.1.2** | 驗證合法使用者嘗試在 TURN 伺服器上打開大量端口時，不會耗盡 TURN 服務的資源。 | 3 |

## V17.2 媒體

這些要求只適用於自行部署並執行 WebRTC 媒體伺服器的系統，例如選擇性轉發單元（SFU）、多點控制單元（MCU）、錄制伺服器或網關伺服器。媒體伺服器處理並分發媒體流，其安全性直接關係到參與通信的各個用戶端之間的通信安全。在 WebRTC 應用中，保護媒體流是重中之重，以防止竊聽、篡改和拒絕服務攻擊危及使用者隱私和通信品質。

媒體伺服器尤其需要防範洪泛攻擊。可以採用速率限制、檢核時間戳、使用同步時鐘匹配實際時間間隔，以及管理緩衝區防止溢出並維持正確時序。某個媒體工作階段的資料包到達過快時，應丟棄多餘的資料包。系統還應通過輸入驗證、安全處理整數溢出、防止緩衝區溢出和穩健的錯誤處理來抵御畸形資料包。

完全依賴 Web 瀏覽器之間點對點媒體通信，且沒有中間媒體伺服器參與的系統，不適用這些特定媒體相關安全要求。

本節提到在 WebRTC 中使用資料報傳輸層安全（Datagram Transport Layer Security，DTLS）。關於記錄密碼學金鑰管理策略的要求位於「密碼學」章節。關於符合安全要求的密碼方法，可參考 ASVS 密碼學附錄，也可參考 NIST SP 800‑52 Rev. 2 或 BSI TR‑02102‑2（2025‑01 版）等文件。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **17.2.1** | 驗證 DTLS 憑證金鑰按照書面的密碼學金鑰管理策略進行管理和保護。 | 2 |
| **17.2.2** | 驗證媒體伺服器組態為使用並支援獲認可的 DTLS 密碼套件，以及用於為安全實時傳輸協議建立金鑰的 DTLS 擴展（DTLS-SRTP）的安全保護組態（protection profile）。 | 2 |
| **17.2.3** | 驗證媒體伺服器會檢核安全實時傳輸協議（SRTP）的身分驗證資訊，防止實時傳輸協議（RTP）注入攻擊導致拒絕服務，或將音頻、視頻插入媒體流。 | 2 |
| **17.2.4** | 驗證媒體伺服器在收到畸形安全實時傳輸協議（SRTP）資料包時，仍能正常處理傳入的媒體流量。 | 2 |
| **17.2.5** | 驗證媒體伺服器在合法使用者產生安全實時傳輸協議（SRTP）資料包洪泛時，仍能正常處理傳入的媒體流量。 | 3 |
| **17.2.6** | 驗證媒體伺服器不受 DTLS `ClientHello` 競態條件弱點影響，驗證方式為檢查媒體伺服器是否已知存在相關弱點，或進行競態條件測試。 | 3 |
| **17.2.7** | 驗證與媒體伺服器關聯的音頻或視頻錄制機制，在合法使用者產生安全實時傳輸協議（SRTP）資料包洪泛時，仍能正常處理傳入的媒體流量。 | 3 |
| **17.2.8** | 驗證根據工作階段描述協議（SDP）的 `fingerprint` 屬性檢核 DTLS 憑證，並在檢核失敗時終止媒體流，以確保媒體流的真實性。 | 3 |

## V17.3 信令

本節適用於自行執行 WebRTC 信令伺服器的系統。信令用於協調點對點通信，必須能夠抵御可能幹擾工作階段建立或控制的攻擊。

信令伺服器必須能夠安全處理畸形輸入，並在高負載下保持可用。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **17.3.1** | 驗證信令伺服器在洪泛攻擊期間仍能處理合法的傳入信令訊息。這應通過在信令層實施速率限制來實作。 | 2 |
| **17.3.2** | 驗證信令伺服器在收到可能導致拒絕服務的畸形信令訊息時，仍能正常處理合法信令訊息。可採用的措施包括輸入驗證、安全處理整數溢出、防止緩衝區溢出，以及其他穩健的錯誤處理技術。 | 2 |

## 參考資料

更多資訊，另見：

* WebRTC DTLS ClientHello DoS 的最佳文件包括 [Enable Security 面向安全專業人員的博客文章](https://www.enablesecurity.com/blog/novel-dos-vulnerability-affecting-webrtc-media-servers/) 以及相關的[面向 WebRTC 開發人員的白皮書](https://www.enablesecurity.com/blog/webrtc-hello-race-conditions-paper/)
* [RFC 3550 - RTP: A Transport Protocol for Real-Time Applications](https://www.rfc-editor.org/rfc/rfc3550)
* [RFC 3711 - The Secure Real-time Transport Protocol (SRTP)](https://datatracker.ietf.org/doc/html/rfc3711)
* [RFC 5764 - Datagram Transport Layer Security (DTLS) Extension to Establish Keys for the Secure Real-time Transport Protocol (SRTP))](https://datatracker.ietf.org/doc/html/rfc5764)
* [RFC 8825 - Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/info/rfc8825)
* [RFC 8826 - Security Considerations for WebRTC](https://www.rfc-editor.org/info/rfc8826)
* [RFC 8827 - WebRTC Security Architecture](https://www.rfc-editor.org/info/rfc8827)
* [DTLS-SRTP Protection Profiles](https://www.iana.org/assignments/srtp-protection/srtp-protection.xhtml)
