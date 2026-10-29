# V1 編碼和淨化

## 控制目標

本章討論與不安全處理不可信資料有關的常見 Web 應用程式安全弱點。這類弱點可能導致多種技術弱點，其中不可信資料會按照相應解釋器的語法規則被解析。

對於現代 Web 應用，最好始終使用更安全的 API，例如參數化查詢、自動轉義機制或範本框架。否則，謹慎執行輸出編碼、轉義或淨化對應用程式安全至關重要。

輸入驗證是一種縱深防禦機制，用來防止意外或危險內容。不過，由於它的主要目的是確保傳入內容符合功能和業務預期，因此相關要求位於「驗證和業務邏輯」章節。

## V1.1 編碼和淨化架構

以下各節針對不同語法和解釋器，說明如何安全處理不可信內容。本節則規定這些處理應在何時、何處執行。資料在儲存時應保持原始形式，不應儲存為已經編碼或轉義的形式（例如經過 HTML 編碼的文字），否則容易發生重複編碼。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **1.1.1** | 驗證輸入最多只經過一次解碼或反轉義，並轉換為規範形式。只有在預期輸入本身採用了相應編碼時，才可以進行解碼。解碼或反轉義必須先於其他輸入處理；例如，不得在輸入驗證或淨化之後再進行解碼或反轉義。 | 2 |
| **1.1.2** | 驗證應用將輸出編碼和轉義作為資料交由目標解釋器使用之前的最後一個處理步驟，或者由目標解釋器自身執行這些操作。 | 2 |

## V1.2 注入預防

在接近或緊鄰潛在危險情境的位置進行輸出編碼或轉義，對任何應用的安全都至關重要。通常，輸出編碼和轉義的結果不會被持久化保存，而是用於使輸出能夠立即在相應解釋器中安全使用。過早執行這些操作可能導致內容格式錯誤，或使編碼或轉義失效。

許多函式庫都提供能夠自動完成這些處理的安全函數。即便如此，仍須確認所用函數適合資料所在的具體情境。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **1.2.1** | 驗證應用在生成 HTTP 回應、HTML 文件或 XML 文件時，根據資料所在的具體情境進行編碼。例如，針對 HTML 元素、HTML 屬性、HTML 註解、CSS 或 HTTP 標頭欄位分別編碼相應的特殊字元，防止資料改變訊息或文件結構。 | 1 |
| **1.2.2** | 驗證動態建置 URL 時，根據資料所在位置對不可信資料進行編碼。例如，對查詢參數或路徑參數採用 URL 編碼或 base64url 編碼。同時，只允許使用安全的 URL 通訊協定，不得允許 `javascript:`、`data:` 等危險通訊協定。 | 1 |
| **1.2.3** | 驗證應用動態生成 JavaScript 內容（包括 JSON）時，會根據 JavaScript 或 JSON 情境，對插入的資料進行適當編碼或轉義，防止不可信資料改變訊息或文件結構，從而避免 JavaScript 注入和 JSON 注入。 | 1 |
| **1.2.4** | 驗證資料檢索或資料庫查詢（例如 SQL、HQL、NoSQL、Cypher）採用參數化查詢、ORM、實體框架或其他有效措施，以防範 SQL 注入及其他資料庫注入攻擊。編寫預存程序時也必須滿足此要求。 | 1 |
| **1.2.5** | 驗證應用能夠防範作業系統命令注入，且作業系統呼叫採用參數化作業系統查詢，或採用適合命令行情境的輸出編碼。 | 1 |
| **1.2.6** | 驗證應用能夠防範 LDAP 注入弱點，或已實施用於防止 LDAP 注入的特定安全控制。 | 2 |
| **1.2.7** | 驗證應用使用參數化查詢或預編譯查詢來防範 XPath 注入。 | 2 |
| **1.2.8** | 驗證 LaTeX 處理器採用了安全組態，例如不啟用 `--shell-escape`；同時使用命令允許清單來防範 LaTeX 注入。 | 2 |
| **1.2.9** | 驗證應用對正規表示式中的特殊字元進行轉義（通常使用反斜線），以防止這些字元被誤解釋為元字元。 | 2 |
| **1.2.10** | 驗證應用能夠防範 CSV 和公式注入。匯出 CSV 內容時，應用必須遵循 RFC 4180 第 2.6 和 2.7 節定義的轉義規則。此外，匯出為 CSV 或其他試算表格式（例如 XLS、XLSX 或 ODF）時，如果特殊字元（包括 '='、'+'、'-'、'@'、'\t'（定位字元）和 '\0'（空字元））出現在欄位值的第一個字元位置，必須用單引號進行轉義。 | 3 |

注意：參數化查詢或 SQL 轉義並不能解決所有問題。資料表名稱、欄位名稱（包括 `ORDER BY` 子句中的欄位名稱）等查詢結構無法通過轉義來保證安全。如果把使用者提供的值用於這些位置，即使經過轉義，也可能造成查詢失敗或 SQL 注入。

## V1.3 淨化

需要在危險情境中使用不可信內容時，首選方法是根據情境進行編碼或轉義。這樣既能保留原內容的含義，又能保證它在該情境中安全使用。上一節對此作了詳細說明。

如果無法做到這一點，就需要進行淨化，移除潛在危險字元或內容。在某些情況下，這可能會改變輸入的語義，但出於安全原因，可能沒有其他選擇。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **1.3.1** | 驗證所有來自 WYSIWYG 編輯器或類似來源的不可信 HTML，都經過知名且安全的 HTML 淨化函式庫或框架功能處理。 | 1 |
| **1.3.2** | 驗證應用避免使用 `eval()`、Spring Expression Language（SpEL）等動態程式碼執行功能。如果確實沒有替代方案，則必須先淨化其中包含的所有使用者輸入，再執行動態程式碼。 | 1 |
| **1.3.3** | 驗證資料進入潛在危險的情境之前已經過淨化，並且符合該情境的安全限制。例如，只允許安全字元，並截斷過長的輸入。 | 2 |
| **1.3.4** | 驗證使用者提供的可縮放向量圖形（SVG）內容經過驗證或淨化，只保留對應用程式安全的標籤和屬性（例如繪圖相關內容），不得包含腳本、`foreignObject` 等危險內容。 | 2 |
| **1.3.5** | 驗證應用對使用者提供的可腳本化內容或表達式範本內容進行淨化，或者徹底停用這類內容，例如 Markdown、CSS、XSL 樣式表、BBCode 等。 | 2 |
| **1.3.6** | 驗證應用能夠防範伺服器端請求偽造（SSRF）攻擊：在使用不可信資料呼叫其他服務前，先按通訊協定、網域名稱、路徑和連接埠允許清單驗證這些資料，並淨化潛在危險字元。 | 2 |
| **1.3.7** | 驗證應用禁止使用不可信輸入來建置範本，以防範範本注入。如果沒有其他可行方案，則必須對範本建立過程中動態插入的所有不可信輸入進行淨化或嚴格驗證。 | 2 |
| **1.3.8** | 驗證不可信輸入在用於 Java Naming and Directory Interface（JNDI）查詢之前已經過適當淨化，並且 JNDI 本身採用了安全組態，以防範 JNDI 注入。 | 2 |
| **1.3.9** | 驗證內容傳送到 memcache 之前已經過淨化，以防範注入攻擊。 | 2 |
| **1.3.10** | 驗證在使用時可能以非預期或惡意方式解析的格式字串，在處理之前已經過淨化。 | 2 |
| **1.3.11** | 驗證使用者輸入在傳遞給郵件系統之前已經過淨化，以防範 SMTP 或 IMAP 注入。 | 2 |
| **1.3.12** | 驗證正規表示式中沒有可能引發指數級回溯的結構，並對不可信輸入進行淨化，以降低 ReDoS 或失控正規表示式攻擊的風險。 | 3 |

## V1.4 記憶體、字串和非託管程式碼

以下要求處理不安全記憶體使用帶來的風險，這通常適用於使用系統語言或非託管程式碼的應用。

部分要求可以通過編譯器選項來落實。例如，啟用緩衝區溢位保護、堆疊隨機化、資料執行保護和相關警告；一旦發現不安全的指標、記憶體、格式字串、整數或字串操作，就讓建置失敗。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **1.4.1** | 驗證應用採用記憶體安全的字串操作、更安全的記憶體複製方法和指標運算，以檢測或防止堆疊溢位、緩衝區溢位和堆積溢位。 | 2 |
| **1.4.2** | 驗證應用通過符號檢查、範圍檢查和輸入驗證來防止整數溢位。 | 2 |
| **1.4.3** | 驗證動態分配的記憶體和資源在使用完畢後得到釋放；同時刪除或置空指向已釋放記憶體的引用和指標，以防止懸空指標和釋放後使用（use-after-free）弱點。 | 2 |

## V1.5 安全反序列化

反序列化是把儲存或傳輸形式的資料轉換為應用物件的過程。這個過程曾引發多種程式碼注入弱點，因此必須謹慎、安全地處理。

尤其要注意，有些反序列化方法已被程式語言或框架文件認定為不安全，無法使其在處理不可信資料時安全執行。應對每一種正在使用的反序列化機制進行審慎評估。

| # | 描述 | 級別 |
| :---: | :--- | :---: |
| **1.5.1** | 驗證 XML 解析器採用嚴格的安全組態，並停用外部實體解析等危險功能，以防範 XML 外部實體（XXE）攻擊。 | 1 |
| **1.5.2** | 驗證應用在反序列化不可信資料時，強制採用安全的輸入處理方式，例如設定物件類型允許清單，或限制用戶端能夠指定的物件類型，以防範反序列化攻擊。不得使用已經明確認定為不安全的反序列化機制來處理不可信輸入。 | 2 |
| **1.5.3** | 驗證應用使用多個解析器處理同一類資料時（例如使用不同的 JSON、XML 或 URL 解析器），各解析器採用一致的解析規則和字元編碼。這樣可以避免 JSON 互操作性弱點，也可以防止攻擊者利用不同解析器對 URI 或文件的解釋差異實施遠端檔案包含（RFI）或伺服器端請求偽造（SSRF）攻擊。 | 3 |

## 參考資料

更多資訊，另見：

* [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
* [OWASP Web Security Testing Guide: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [RFC4180 - Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180#section-2)

關於反序列化或解析問題的更多資訊，請參見：

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai - A New Era of SSRF Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
