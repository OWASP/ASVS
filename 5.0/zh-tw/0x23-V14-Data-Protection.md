# V14 資料保護

## 控制目標

應用無法掌控所有使用方式和使用者行為，因此應實施控制，限制對用戶端裝置上敏感資料的未授權存取。

本章說明如何識別需要保護的資料、如何確定保護方式，以及應採用哪些機制、避免哪些常見問題。

資料保護還要考慮批量提取、批量修改和過度使用資料。不同系統對「異常行為」的定義差異很大，必須結合威脅模型和業務風險判斷。在 ASVS 中，這類行為的檢測要求見「安全日誌和錯誤處理」章節，使用限制見「驗證和業務邏輯」章節。

## V14.1 資料保護文件

保護資料的前提是先識別哪些資料屬於敏感資料，並劃分敏感等級。不同等級的資料需要採用不同強度的保護措施。

有多種隱私法規和法律會影響應用必須如何儲存、使用和傳輸敏感個人資訊。本節不再試圖重複這些資料保護或隱私法律，而是聚焦於保護敏感資料的關鍵技術考慮。請查閱當地法律法規，並按需諮詢合格的隱私專家或律師。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **14.1.1** | 驗證應用已經識別其建立和處理的所有敏感資料，並為每類資料指定保護等級。僅經過編碼、很容易復原原文的資料也屬於識別範圍，例如 Base64 字串或 JWT 中的明文載荷。劃分等級時，必須考慮應用需要遵守的資料保護和隱私法律、法規及標準。 | 2 |
| **14.1.2** | 驗證每個敏感資料保護等級都有書面的保護要求。要求必須涵蓋但不限於加密、完整性檢核、保留期限、日誌記錄方式、日誌中敏感資料的存取控制、資料庫級加密、隱私保護和隱私增強技術，以及其他保密措施。 | 2 |

## V14.2 通用資料保護

本節給出資料保護的具體要求。多數要求針對意外洩露等特定問題，同時也要求按照每項資料的保護等級落實相應控制。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **14.2.1** | 驗證向伺服器傳送敏感資料時，只把資料放在 HTTP 訊息正文或標頭欄位中。URL 和查詢字串不得包含 API 金鑰、工作階段權杖等敏感資訊。 | 1 |
| **14.2.2** | 驗證應用防止負載平衡器、應用快取等伺服器端元件快取敏感資料，或確保這些資料在使用後得到安全清除。 | 2 |
| **14.2.3** | 驗證應用不會把已經認定為敏感的資料傳送給使用者跟蹤器等不可信方，防止資料脫離應用控制後被不必要地收集。 | 2 |
| **14.2.4** | 驗證應用按照相應保護等級的文件要求，對敏感資料實施加密、完整性檢核、保留期限、日誌記錄、日誌存取控制、隱私保護和隱私增強等措施。 | 2 |
| **14.2.5** | 驗證快取系統僅快取同時滿足以下條件的回應：回應的 `Content-Type` 與該資源應有的類型一致，並且不包含動態生成的敏感內容。如果請求的檔案不存在，Web 伺服器應傳回 404 或 302 回應，而不是傳回另一個實際存在的檔案，以防止 Web 快取欺騙（Web Cache Deception）攻擊。 | 3 |
| **14.2.6** | 驗證應用只傳回實作當前功能所必需的最少敏感資料。例如，只傳回信用卡號的部分數字，而不是完整卡號。如果需要完整資料，應在使用者介面中將其遮蔽，除非使用者明確選擇查看。 | 3 |
| **14.2.7** | 驗證敏感資訊受資料保留分類規則約束，確保過時或不再需要的資料會被自動刪除、按既定計畫刪除，或在具體情況需要時刪除。 | 3 |
| **14.2.8** | 驗證應用會從使用者提交檔案的中繼資料中刪除敏感資訊；只有使用者明確同意保留時才可以例外。 | 3 |

## V14.3 用戶端資料保護

本節包含防止資料在應用用戶端或使用者代理側以特定方式洩露的要求。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **14.3.1** | 驗證用戶端關閉或工作階段終止後，用戶端儲存（例如瀏覽器 DOM）中的身分驗證後取得的資料會被清除。`Clear-Site-Data` 回應標頭可以幫助完成清理；但即使工作階段終止時無法連線伺服器，用戶端也應能夠自行清除資料。 | 1 |
| **14.3.2** | 驗證應用設定了足以防止快取的 HTTP 回應標頭欄位（即 `Cache-Control: no-store`），使敏感資料不會被瀏覽器快取。 | 2 |
| **14.3.3** | 驗證 localStorage、sessionStorage、IndexedDB、Cookie 等瀏覽器儲存中不保存敏感資料；工作階段權杖是唯一例外。 | 2 |

## 參考資料

更多資訊，另見：

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
