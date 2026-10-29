# V4 API 和 Web 服務

## 控制目標

對於向 Web 瀏覽器或其他呼叫方開放 API 的應用（通常使用 JSON、XML 或 GraphQL），需要考慮若干特有的安全問題。本章介紹應採用的相關安全組態和機制。

身分驗證、工作階段管理和輸入驗證等其他章節的要求同樣適用於 API。因此，理解和測試本章時，必須結合標準中的其他相關要求。

## V4.1 通用 Web 服務安全

本節介紹 Web 服務普遍適用的安全要求，包括最基本的安全組態和防護措施。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **4.1.1** | 驗證每個包含訊息正文的 HTTP 回應都帶有 Content-Type 頭，且其值與實際回應內容一致。對於 IANA Media Types 規定應包含字元集的類型（例如 `text/`、`/+xml` 和 `/xml`），還必須通過 `charset` 參數指定安全的字元編碼，例如 UTF-8 或 ISO-8859-1。 | 1 |
| **4.1.2** | 驗證只有供使用者通過瀏覽器存取的端點，才會自動把 HTTP 請求重定向到 HTTPS。其他服務和端點不得進行這種透明重定向。否則，用戶端誤用未加密 HTTP 發送敏感資料後，自動重定向可能掩蓋已經發生的資料洩露。 | 2 |
| **4.1.3** | 驗證應用所使用且由中間層設定的任何 HTTP 頭欄位，例如負載均衡器、Web 代理或 BFF 服務設定的頭欄位，均不能被最終使用者覆蓋。此類頭欄位可能包括 X-Real-IP、X-Forwarded-* 或 X-User-ID。 | 2 |
| **4.1.4** | 驗證應用或 API 只允許明確支援的 HTTP 方法，包括需要用於預檢請求的 OPTIONS；所有未使用的方法都必須停用。 | 3 |
| **4.1.5** | 驗證對高度敏感或經過多個系統的請求或業務操作使用逐訊息數位簽章，在傳輸保護的基礎上提供額外保證。 | 3 |

## V4.2 HTTP 訊息結構驗證

本節說明應如何驗證 HTTP 訊息的結構和頭欄位，以防止請求走私、回應拆分、頭注入，以及由過長 HTTP 訊息導致的拒絕服務等攻擊。

這些要求適用於一般 HTTP 訊息處理和生成，但在不同 HTTP 版本之間轉換 HTTP 訊息時尤其重要。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **4.2.1** | 驗證所有應用元件（包括負載均衡器、防火牆和應用伺服器）都按照相應 HTTP 版本的規則確定傳入訊息的邊界，以防範 HTTP 請求走私。對於 HTTP/1.x，如果訊息中含有 Transfer-Encoding 頭，則必須按照 RFC 2616 忽略 Content-Length。對於 HTTP/2 或 HTTP/3，如果訊息中含有 Content-Length，接收方必須確認其值與 DATA 幀的實際長度一致。 | 2 |
| **4.2.2** | 驗證應用生成 HTTP 訊息時，Content-Length 頭所聲明的長度與 HTTP 分幀機制確定的實際內容長度一致，以防範請求走私。 | 3 |
| **4.2.3** | 驗證應用既不發送也不接受含有連接專用頭欄位（例如 Transfer-Encoding）的 HTTP/2 或 HTTP/3 訊息，以防範回應拆分和頭注入。 | 3 |
| **4.2.4** | 驗證應用只接受頭欄位名稱和值中均不含 CR（`\r`）、LF（`\n`）或 CRLF（`\r\n`）序列的 HTTP/2 和 HTTP/3 請求，以防範頭注入。 | 3 |
| **4.2.5** | 驗證應用的後端或前端在構造併發送請求時，會通過驗證、淨化或其他機制限制 URI（例如 API 呼叫位址）和 HTTP 請求頭欄位（例如 `Authorization` 或 `Cookie`）的長度，避免接收方因內容過長而拒絕請求。過長的請求可能造成拒絕服務；例如，發送過長的請求（如過長的 Cookie 頭欄位）可能導致伺服器始終傳回錯誤狀態。 | 3 |

## V4.3 GraphQL

GraphQL 越來越多地用於建置資料密集型用戶端，使用戶端無需與多個後端服務緊密耦合。本節介紹使用 GraphQL 時需要注意的安全問題。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **4.3.1** | 驗證應用通過查詢允許列表、查詢深度限制、數量限制或查詢成本分析，防止複雜的嵌套查詢耗盡 GraphQL 服務或資料層資源並造成拒絕服務（DoS）。 | 2 |
| **4.3.2** | 驗證生產環境已經停用 GraphQL 內省查詢；如果該 GraphQL API 本來就需要提供給外部使用方，則可以例外。 | 2 |

## V4.4 WebSocket

WebSocket 是一種通信協議，可在單個 TCP 連接上提供同時雙向通信通道。它於 2011 年由 IETF 以 RFC 6455 標準化；雖然它被設計為通過 HTTP 端口 443 和 80 工作，但它不同於 HTTP。

本節提供關鍵安全要求，用於防止專門利用這種實時通信通道的通信安全和工作階段管理相關攻擊。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **4.4.1** | 驗證所有 WebSocket 連接都使用基於 TLS 的 WebSocket（WSS）。 | 1 |
| **4.4.2** | 驗證初次進行 HTTP WebSocket 握手時，會對照應用允許的源列表檢查 Origin 頭欄位。 | 2 |
| **4.4.3** | 驗證無法沿用應用原有工作階段管理機制時，WebSocket 使用專用的工作階段權杖，並且這些權杖滿足相關的工作階段管理安全要求。 | 2 |
| **4.4.4** | 驗證把現有 HTTPS 工作階段升級為 WebSocket 通道時，專用 WebSocket 工作階段權杖最初是通過已經身分驗證的 HTTPS 工作階段獲取或驗證的。 | 2 |

## 參考資料

更多資訊，另見：

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* 來自 [graphql.org](https://graphql.org/learn/authorization/) 和 [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods) 的 GraphQL 授權資源。
* [OWASP Web Security Testing Guide: GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [OWASP Web Security Testing Guide: Testing WebSockets](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)
