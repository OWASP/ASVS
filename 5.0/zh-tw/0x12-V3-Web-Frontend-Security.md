# V3 Web 前端安全

## 控制目標

本章重點防範針對 Web 前端的攻擊，不適用於純機器間通訊的系統。

## V3.1 Web 前端安全文件

本節概述應用文件中應明確規定的瀏覽器安全功能。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **3.1.1** | 驗證應用文件列明了瀏覽器必須支援的安全功能，例如 HTTPS、HTTP 嚴格傳輸安全（HSTS）、內容安全策略（CSP）及其他 HTTP 安全機制。文件還必須說明瀏覽器不支援其中某項功能時，應用應如何處理，例如警告使用者或拒絕存取。 | 3 |

## V3.2 非預期內容解釋

如果瀏覽器在錯誤的情境中渲染內容或呼叫功能，就可能顯示甚至執行惡意內容。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **3.2.1** | 驗證應用採用了安全控制，防止瀏覽器在錯誤的情境中渲染 HTTP 回應中的內容或功能，例如直接存取 API、使用者上傳的檔案或其他資源時。可採用的措施包括：只有當 `Sec-Fetch-*` 等 HTTP 請求標頭表明情境正確時才傳回內容；在 Content-Security-Policy 標頭中使用 `sandbox` 指令；或者在 Content-Disposition 標頭中指定 `attachment`。 | 1 |
| **3.2.2** | 驗證只需顯示為文字而不應渲染成 HTML 的內容，會通過安全渲染函數（例如 `createTextNode` 或 `textContent`）處理，防止其中的 HTML 或 JavaScript 被意外執行。 | 1 |
| **3.2.3** | 驗證用戶端 JavaScript 通過明確宣告變數、進行嚴格類型檢查、不在 `document` 物件上儲存全域變數，以及隔離命名空間等方式，防範 DOM Clobbering。 | 3 |

## V3.3 Cookie 設定

本節說明如何安全組態敏感 Cookie，以盡可能確認它們確實由應用建立，並防止其內容洩露或遭到篡改。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **3.3.1** | 驗證 Cookie 已設定 `Secure` 屬性；如果 Cookie 名稱未使用 `__Host-` 前綴，則必須使用 `__Secure-` 前綴。 | 1 |
| **3.3.2** | 驗證每個 Cookie 都根據自身用途設定了合適的 `SameSite` 屬性值，以降低使用者介面偽裝攻擊和瀏覽器請求偽造攻擊（通常稱為跨站請求偽造，即 CSRF）的風險。 | 2 |
| **3.3.3** | 驗證 Cookie 名稱使用 `__Host-` 前綴，除非這些 Cookie 被明確設計為與其他主機共享。 | 2 |
| **3.3.4** | 驗證當 Cookie 的值不應由用戶端腳本存取時（例如工作階段權杖），該 Cookie 設定了 `HttpOnly` 屬性，並且該值只能通過 `Set-Cookie` 標頭欄位傳輸給用戶端。 | 2 |
| **3.3.5** | 驗證應用寫入的 Cookie，其名稱和值合計不超過 4096 位元組。瀏覽器不會保存過大的 Cookie，也不會在後續請求中傳送它，這可能導致依賴該 Cookie 的功能無法使用。 | 3 |

## V3.4 瀏覽器安全機制標頭

本節說明 HTTP 回應應設定哪些安全標頭，以便瀏覽器在處理回應時啟用相應的安全功能和限制。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **3.4.1** | 驗證所有回應都包含 Strict-Transport-Security 標頭欄位，以強制執行 HTTP 嚴格傳輸安全（HSTS）策略。必須定義至少 1 年的最大有效期；對於 L2 及以上，策略還必須適用於所有子網域名稱。 | 1 |
| **3.4.2** | 驗證應用將跨源資源共享（CORS）的 Access-Control-Allow-Origin 回應標頭欄位設定為固定值，或在使用 Origin 請求標頭欄位的值時，對照可信源允許清單驗證該值。需要使用 `Access-Control-Allow-Origin: *` 時，回應中不得包含任何敏感資訊。 | 1 |
| **3.4.3** | 驗證 HTTP 回應包含 Content-Security-Policy 標頭，並通過其中的指令限制瀏覽器只能載入和執行可信內容或資源，從而限制惡意 JavaScript 的執行。最低要求是制定全域策略：包含 `object-src 'none'` 和 `base-uri 'none'`，並為其他資源定義允許清單，或者採用 nonce 或雜湊。L3 應用必須針對每個回應定義使用 nonce 或雜湊的策略。 | 2 |
| **3.4.4** | 驗證所有 HTTP 回應都包含 `X-Content-Type-Options: nosniff` 標頭欄位，禁止瀏覽器通過內容嗅探來猜測 MIME 類型。回應的 `Content-Type` 必須與目標資源類型相符；例如，樣式資源只有在回應類型為 `text/css` 時才會被瀏覽器接受。設定該標頭欄位還會啟用瀏覽器的跨源讀取阻止（CORB）功能。 | 2 |
| **3.4.5** | 驗證應用設定了來源資訊策略（referrer policy），防止技術敏感資料通過 `Referer` 請求標頭洩露給第三方服務。可以通過 Referrer-Policy 回應標頭或 HTML 元素屬性來設定。敏感資料可能包括 URL 路徑和查詢參數；對於非公開的內部應用，還可能包括主機名。 | 2 |
| **3.4.6** | 驗證 Web 應用在每個 HTTP 回應的 Content-Security-Policy 標頭中設定了 `frame-ancestors` 指令。預設情況下應禁止嵌入應用內容，僅在必要時允許嵌入特定資源。雖然瀏覽器仍支援 X-Frame-Options，但該標頭已經過時，不應再依賴它。 | 2 |
| **3.4.7** | 驗證 Content-Security-Policy 標頭指定了策略違規報告的接收位置。 | 3 |
| **3.4.8** | 驗證所有會觸發文件渲染的 HTTP 回應（例如 Content-Type 為 `text/html` 的回應）都包含 Cross-Origin-Opener-Policy 標頭欄位，並根據需要使用 `same-origin` 或 `same-origin-allow-popups` 指令。這樣可以防止攻擊者濫用不同頁面對 `Window` 物件的共享存取，例如實施標籤頁劫持（tabnabbing）或框架計數（frame counting）攻擊。 | 3 |

## V3.5 瀏覽器源隔離

伺服器端收到敏感功能的請求時，應用必須確認請求來自應用自身或可信方，而不是攻擊者偽造的請求。

此處的敏感功能可以包括接受已身分驗證和未身分驗證使用者的表單提交（例如身分驗證請求）、改變狀態的操作，或消耗大量資源的功能（例如資料匯出）。

主要防護機制包括瀏覽器的同源策略（針對 JavaScript）和 Cookie 的 SameSite 規則。CORS 預檢也是常見的防護手段：對設計為允許跨源呼叫的端點，這一機制至關重要；對不應跨源呼叫的端點，它也能幫助阻止偽造請求。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **3.5.1** | 驗證應用在不依賴 CORS 預檢來保護敏感功能時，會檢查請求是否確實來自應用自身。可採用並驗證防偽權杖，或者要求請求攜帶不屬於 CORS 安全清單的額外 HTTP 標頭。這樣可以防範瀏覽器請求偽造攻擊，即通常所說的跨站請求偽造（CSRF）。 | 1 |
| **3.5.2** | 驗證應用依賴 CORS 預檢來保護敏感功能時，任何不會觸發預檢的請求都無法呼叫該功能。為此，應用可能需要檢查 `Origin` 和 `Content-Type` 請求標頭的值，或要求請求攜帶不屬於 CORS 安全清單的額外標頭欄位。 | 1 |
| **3.5.3** | 驗證存取敏感功能的 HTTP 請求使用合適的 HTTP 方法，例如 POST、PUT、PATCH 或 DELETE，而不是 HTTP 規範定義為「安全」的方法，例如 HEAD、OPTIONS 或 GET。或者，可以嚴格驗證 Sec-Fetch-* 請求標頭欄位，確保請求並非來自不合適的跨源呼叫、導航請求，或資源載入（例如圖片源）等非預期來源。 | 1 |
| **3.5.4** | 驗證不同應用分別託管在不同的主機名下，以充分利用同源策略和 Cookie 的主機名限制，約束一個源中的文件或腳本與另一個源中的資源互動。 | 2 |
| **3.5.5** | 驗證通過 `postMessage` 介面收到訊息時，會檢查訊息來源和格式；來源不可信或格式不合法的訊息必須丟棄。 | 2 |
| **3.5.6** | 驗證應用任何位置都未啟用 JSONP 功能，以避免跨站腳本包含（XSSI）攻擊。 | 3 |
| **3.5.7** | 驗證需要授權的資料不會包含在腳本資源回應（例如 JavaScript 檔案）中，以防止跨站腳本包含（XSSI）攻擊。 | 3 |
| **3.5.8** | 驗證只有在符合預期時，才允許以使用者身分載入或嵌入需要身分驗證的資源，例如圖片、影片、腳本和其他文件。可以嚴格檢查 `Sec-Fetch-*` 請求標頭，排除非預期的跨源呼叫；也可以設定嚴格的 Cross-Origin-Resource-Policy 回應標頭，讓瀏覽器阻止不符合策略的內容。 | 3 |

## V3.6 外部資源完整性

本節為在第三方站點上安全託管內容提供指導。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **3.6.1** | 驗證 JavaScript 函式庫、CSS、Web 字體等用戶端資源只有同時滿足以下條件時，才託管在外部站點（例如 CDN）：資源是靜態的、帶有明確版本，並通過子資源完整性（SRI）檢核其完整性。無法滿足這些條件時，應針對每項資源記錄安全決策，說明理由。 | 3 |

## V3.7 其他瀏覽器安全考慮

本節包含用戶端瀏覽器安全所需的其他各類安全控制和現代瀏覽器安全功能。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **3.7.1** | 驗證應用只使用仍受支援且被認為安全的用戶端技術。不符合此要求的技術示例包括 NSAPI 外掛程式、Flash、Shockwave、ActiveX、Silverlight、NACL 或用戶端 Java Applet。 | 2 |
| **3.7.2** | 驗證應用只有在目標主機名或網域名稱位於允許清單中時，才自動把使用者重新導向到應用控制範圍之外。 | 2 |
| **3.7.3** | 驗證使用者將被重新導向到應用控制範圍之外的 URL 時，應用會事先提示使用者，並允許使用者取消跳轉。 | 3 |
| **3.7.4** | 驗證應用的頂層網域名稱（例如 `site.tld`）已經加入 HSTS 公共預載入清單。這樣，主流瀏覽器會內建該應用必須使用 TLS 的規則，而不只是依賴 Strict-Transport-Security 回應標頭。 | 3 |
| **3.7.5** | 驗證瀏覽器不支援應用所需的安全功能時，應用按照文件規定進行處理，例如警告使用者或拒絕存取。 | 3 |

## 參考資料

更多資訊，另見：

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
* [OWASP DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)
