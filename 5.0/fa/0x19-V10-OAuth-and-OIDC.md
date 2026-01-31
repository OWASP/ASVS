# V10 OAuth and OIDC

## هدف

OAuth2 (که در این فصل با عنوان OAuth از آن یاد می‌شود) یک چارچوب استاندارد در صنعت برای واگذاری مجوز دسترسیauthorization)   (delegated است. برای مثال، با استفاده از OAuth یک برنامه‌ی کاربری (Client Application) می‌تواند به نمایندگی از کاربر، به APIها (منابع سرور) دسترسی پیدا کند، مشروط بر اینکه کاربر، دسترسی مورد نیاز را به آن برنامه اعطا کرده باشد.

به‌تنهایی، OAuth برای احراز هویت کاربر طراحی نشده است. چارچوب OpenID Connect (OIDC) با افزودن یک لایه‌ی هویت کاربر بر رویOAuth، آن را گسترش می‌دهد. OIDCامکاناتی مانند اطلاعات استاندارد هویت کاربر، ورود یکپارچه (Single Sign-On - SSO) و مدیریت نشست (Session Management) را پشتیبانی می‌کند.از آنجا که OIDC یک افزونه‌ی OAuth محسوب می‌شود، الزامات مربوط به OAuth در این فصل، شامل OIDC نیز می‌گردد.

نقش‌های زیر در OAuth  تعریف شده‌اند:

* مشتری OAuth (OAuth Client) برنامه‌ای است که تلاش می‌کند به منابع سرور دسترسی پیدا کند (برای مثال، با فراخوانی یک API به کمک توکن دسترسی صادرشده) مشتری OAuth اغلب یک برنامه‌ی سمت سرور (Server-side Application) است.
  * یک Confidential Client  نوعی OAuth Client  است که توانایی حفظ محرمانگی اعتبارنامه‌هایی (Credentials)  را دارد که برای احراز هویت خود در برابر سرور مجوز (Authorization Server) استفاده می‌کند.
  * یک Public Client  توانایی حفظ محرمانگی اعتبارنامه‌ها (Credentials) برای احراز هویت در برابر Authorization Server  را ندارد. بنابراین، به جای احراز هویت خود (برای مثال با استفاده از پارامترهای client_id  و client_secret)، صرفاً خودش را شناسایی می‌کند (با استفاده از پارامتر client_id)
* OAuth Resource Server (RS)  سروری است که از طریق API، منابع را در اختیار OAuth Clients  قرار می‌دهد.
* OAuth Authorization Server (AS)  یک برنامه‌ی سرور است که به OAuth Clients  توکن‌های دسترسی (Access Tokens)  صادر می‌کند. این توکن‌ها به OAuth Clients امکان می‌دهند تا به منابع موجود در RS  دسترسی پیدا کنند؛ یا به نمایندگی از کاربر نهایی (End-User)، یا به نمایندگی از خود OAuth Client. معمولاً AS یک برنامه‌ی مجزا است، اما در صورت لزوم می‌تواند در یک RS مناسب نیز ادغام شود.
* Resource Owner (RO)  همان کاربر نهایی (End-User) است که به OAuth Clients  اجازه می‌دهد تا به نمایندگی از او، دسترسی محدودی به منابع موجود روی Resource Server  داشته باشند.
  Resource Owner  با تعامل با Authorization Server، رضایت خود را برای این واگذاری مجوز دسترسی (Delegated Authorization)  اعلام می‌کند.

نقش‌های زیر در OIDC  تعریف شده‌اند:

* Relying Party (RP)  برنامه‌ی کاربری (Client Application) است که از طریق OpenID Provider درخواست احراز هویت کاربر نهایی (End-User) را می‌دهد. این نقش در واقع همان نقش یک OAuth Client را بر عهده دارد.
* OpenID Provider (OP)  یک OAuth AS  است که توانایی احراز هویت کاربر نهایی (End-User) را دارد و اطلاعات هویتی (OIDC Claims) را در اختیار RP قرار می‌دهد.OP  می‌تواند همان Identity Provider (IdP) باشد، اما در سناریوهای فدراسیونی (Federated Scenarios)، OP و Identity Provider  (جایی که کاربر نهایی احراز هویت می‌شود) ممکن است دو برنامه‌ی سرور جداگانه باشند.

OAuth و OIDC در ابتدا برای برنامه‌های سوم‌شخص (Third-Party Applications) طراحی شده بودند.
امروزه، این پروتکل‌ها به‌طور گسترده در برنامه‌های اول‌شخص (First-Party Applications) نیز مورد استفاده قرار می‌گیرند. با این حال، هنگام استفاده در سناریوهای اول‌شخص مانند احراز هویت (Authentication) و مدیریت نشست (Session Management) این پروتکل‌ها پیچیدگی‌هایی را به همراه می‌آورند که ممکن است چالش‌های امنیتی جدیدی ایجاد کنند.

OAuth  وOIDC  را می‌توان در انواع مختلف برنامه‌ها به کار برد، اما تمرکز در ASVS  و همچنین الزامات مطرح‌شده در این فصل، بر روی برنامه‌های وب (Web Applications) و رابط‌های برنامه‌نویسی کاربردی (APIs) است.

از آنجا کهOAuth  وOIDC  را می‌توان به‌عنوان لایه‌ای منطقی بر بستر فناوری‌های وب در نظر گرفت، الزامات عمومی مطرح‌شده در فصل‌های دیگر همواره در اینجا نیز کاربرد دارند. بنابراین، این فصل را نمی‌توان به‌صورت جدا از بقیه‌ی محتوا در نظر گرفت.

این فصل به بهترین شیوه‌های جاری (Best Current Practices) برای OAuth2  و OIDC می‌پردازد که با مشخصات منتشرشده در نشانی‌های https://oauth.net/2 و https://openid.net/developers/specs همسو هستند. حتی اگرچه RFCها به بلوغ رسیده محسوب می‌شوند، اما به‌طور مداوم به‌روزرسانی می‌شوند. بنابراین، هنگام به‌کارگیری الزامات این فصل، همسویی با آخرین نسخه‌ها بسیار اهمیت دارد. برای جزئیات بیشتر به بخش مراجع (References) مراجعه کنید.

با توجه به پیچیدگی این حوزه، برای داشتن یک راهکار امن مبتنی بر OAuth  یا OIDC  بسیار ضروری است که از Authorization Serverهای شناخته‌شده و استاندارد در صنعت استفاده شود و پیکربندی‌های امنیتی توصیه‌شده به‌کار گرفته شوند.

اصطلاحات به‌کاررفته در این فصل با RFCهای OAuth و مشخصات OIDC  همسو هستند. با این حال، توجه داشته باشید که اصطلاحات OIDC  تنها در مواردی استفاده می‌شوند که مربوط به الزامات خاص OIDC باشند؛ در غیر این صورت، از اصطلاحات OAuth استفاده خواهد شد.

در زمینه‌ی OAuth  و OIDC، اصطلاح توکن(Token) در این فصل اشاره دارد به:

* Access Tokens، که فقط باید توسطRS  مصرف شوند و می‌توانند یاReference Tokens  باشند که با استفاده از Introspection  اعتبارسنجی می‌شوند، یا Self-contained Tokens باشند که با استفاده از کلید رمزنگاری (Key Material ) اعتبارسنجی می‌شوند.
* Refresh Tokens، که فقط باید توسط Authorization Serverای مصرف شوند که توکن را صادر کرده است.
* OIDC ID Tokens، که فقط باید توسط Clientای مصرف شوند که جریان احراز مجوز (Authorization Flow) را آغاز کرده است.

سطوح ریسک برای برخی از الزامات این فصل به این بستگی دارد که آیا Client  یک Confidential Client  است یا به‌عنوان یک Public Client  در نظر گرفته می‌شود. از آنجا که استفاده از احراز هویت قوی Client بسیاری از بردارهای حمله را کاهش می‌دهد، برخی از الزامات ممکن است در هنگام استفاده از یک Confidential Client  برای برنامه‌های L1  آسان‌تر در نظر گرفته شوند.

## V10.1 Generic OAuth and OIDC Security

این بخش الزامات معماری عمومی را پوشش می‌دهد که برای همه‌ی برنامه‌هایی که ازOAuth  یا OIDC استفاده می‌کنند، اعمال می‌شوند.

| #          | شرح الزام                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | سطح |
|:----------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-----:|
| **10.1.1** | توکن‌ها باید فقط به مؤلفه‌هایی ارسال شوند که به‌طور دقیق به آن‌ها نیاز دارند. برای مثال، هنگام استفاده از الگوی Backend-for-Frontend  برای برنامه‌های JavaScript  مبتنی بر مرورگر، Access Tokens  و Refresh Tokens  باید فقط برای Backend  قابل دسترس باشند.                                                                                                                                                                                                                                       | 2     |
| **10.1.2** | Client باید فقط مقادیری را از Authorization Server  بپذیرد (مانند Authorization Code  یاID Token ) که این مقادیر حاصل از یک Authorization Flow  باشند که توسط همان نشست (Session)  و تراکنش User Agent  آغاز شده است. این موضوع مستلزم آن است که Secretهای تولیدشده توسط کلاینت  مانند code_verifier  در PKCE، یا مقادیر state  و nonce  در OIDC قابل حدس زدن نباشند، مخصوص همان تراکنش باشند، و به‌صورت امن هم به کلاینت و هم به نشست (Session) مرورگری که تراکنش در آن شروع شده، متصل شده باشند. | 2     |

## V10.2 OAuth Client

این الزامات مسئولیت‌هایی را که بر عهده برنامه‌های کلاینتِ OAuth است مشخص می‌کنند. کلاینت می‌تواند مثلاً یک بک‌اندِ وب‌سرور باشد (که اغلب به‌عنوان Backend For Frontend یا BFF عمل می‌کند) یک سرویس بک‌اندِ یکپارچه‌ساز، یا یک برنامه فرانت‌اند تک‌صفحه‌ای (SPA یا همان برنامه مبتنی بر مرورگر باشد.

به‌طور کلی، Backend Clients  به‌عنوانConfidential Clients  وFrontend Clients  به‌عنوانPublic Clients  در نظر گرفته می‌شوند. با این حال، برنامه‌های Native که روی دستگاه کاربر نهایی اجرا می‌شوند می‌توانند در صورتی که ازOAuth Dynamic Client Registration  استفاده کنند، به‌عنوانConfidential  در نظر گرفته شوند.

| #          | شرح الزام                                                                                                                                                                                                                                                                                                             | سطح |
|:----------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-----:|
| **10.2.1** | درCode Flow، باید OAuth Client  در برابر حملاتBrowser-based Request Forgery  که معمولاً با عنوان Cross-Site Request Forgery (CSRF)  شناخته می‌شوند و درخواست‌های توکن را ایجاد می‌کنند، محافظت داشته باشد. این محافظت باید با استفاده از قابلیت PKCE  یا با بررسی پارامترstate  که در درخواست احراز مجوز ارسال شده است. | 2     |
| **10.2.2** | اگر OAuth Client  بتواند با بیش از یک Authorization Server  تعامل داشته باشد، باید دارای سازوکاری برای دفاع در برابر Mix-up Attacks  باشد. برای مثال، می‌تواند الزام کند که Authorization Server  مقدار پارامتر ‘iss’ را برگرداند و این مقدار هم درAuthorization Response  و هم درToken Response  اعتبارسنجی شود.       | 2     |
| **10.2.3** | OAuth Client باید فقطScopes  (یا سایر پارامترهای مجوزدهی) مورد نیاز را در درخواست‌ها به Authorization Server  درخواست کند.                                                                                                                                                                                              | 3     |

## V10.3 OAuth Resource Server

در زمینه‌ی ASVS و این فصل، Resource Server یک API است. برای فراهم‌کردن دسترسی ایمن، Resource Server باید:

* Access Token را مطابق با فرمت توکن و مشخصات پروتکل مربوطه اعتبارسنجی کند، برای مثال با استفاده از JWT-validation یا OAuth Token Introspection.
* اگر Access Token معتبر باشد، تصمیمات مجوزدهی (Authorization Decisions) را بر اساس اطلاعات موجود در توکن و دسترسی‌های اعطا شده اعمال نماید. برای مثال، Resource Server باید بررسی کند که آیا Client (که به نمایندگی از RO عمل می‌کند) اجازه‌ی دسترسی به Resource درخواستی را دارد یا خیر.

بنابراین، الزامات ذکرشده در اینجا مختص OAuth یا OIDC هستند و باید پس از اعتبارسنجی توکن و پیش از اعمال تصمیمات مجوزدهی بر اساس اطلاعات موجود در توکن انجام شوند.

| #                                                                                                        | شرح الزام                                                                                                                                                                                                                                                                                  | سطح |
|:--------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-----:|
| **10.3.1**                                                                                               | Resource Server  باید فقط Access Tokenهایی را بپذیرد که برای استفاده با همان سرویس در نظر گرفته شده‌اند(Audience). Audience می‌تواند در یک Access Token ساختاریافته (مانند مقدار aud در JWT) درج شده باشد، یا از طریق Token Introspection Endpoint بررسی شود.                                | 2     |
| **10.3.2**                                                                                               | Resource Server باید تصمیمات مجوزدهی (Authorization Decisions)  را بر اساس  Claims  موجود در Access Token که واگذاری مجوز (Delegated Authorization) را تعریف می‌کنند، اعمال کند. اگر Claimsهایی مانند sub، scope و authorization_details موجود باشند، باید جزو فرآیند تصمیم‌گیری قرار گیرند. | 2     |
| **10.3.3**                                                                                               | اگر برای گرفتن یک تصمیم کنترل دسترسی، لازم است یک کاربرِ یکتا از داخل Access Token  (چه JWT  و چه پاسخ Token Introspection ) شناسایی شود، سرور منبع (Resource Server) کاربر را از روی Claimهایی شناسایی کند که قابل اختصاص‌دادن به کاربران دیگر نیستند.                                      |       |
                                                                                                                                                                                                                                                                                            |       |
| **10.3.4**                                                                                               | اگر Resource Server نیازمند قدرت، روش یا تازگی خاص احراز هویت باشد، بررسی کند که Access Token  ارائه‌شده این محدودیت‌ها را برآورده می‌کند. برای مثال، در صورت وجود، از Claimsهای OIDC مانند acr، amr و auth_time به ترتیب استفاده شود.                                                       | 2     |
| **10.3.5**                                                                                               | تأیید کنید که Resource Server از استفاده از Access Tokenهای سرقت‌شده یا Replay توکن‌ها (توسط افراد غیرمجاز) جلوگیری کند، با الزام استفاده از Sender-Constrained Access Tokens، مانند Mutual TLS برای OAuth 2 یا OAuth2  Demonstration of Proof of Possession (DPoP).                         | 3     |

## V10.4 OAuth Authorization Server

این الزامات، مسئولیت‌های مربوط به OAuth Authorization Servers، شامل OpenID Providers را تشریح می‌کنند.

برای Client Authentication، روش ‘self_signed_tls_client_auth’ مجاز است، همراه با پیش‌نیازهایی که در [بخش 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) از [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705) مشخص شده‌اند.

| #           | شرح الزام                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | سطح |
|:-----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-----:|
| **10.4.1**  | سرور احراز هویت باید آدرس‌های بازگشتی (Redirect URI) را بر اساس فهرست مجاز (Allowlist) از URIهای از پیش‌ثبت‌شده و مخصوص هر کلاینت، با استفاده از مقایسه دقیقِ رشته‌ای Comparison)  (Exact String اعتبارسنجی می‌کند.                                                                                                                                                                                                                                                                                                                                                             | 1     |
| **10.4.2**  | اگر Authorization Server کد احراز مجوز (Authorization Code) را در Authorization Response  برمی‌گرداند، این کد فقط یک‌بار برای درخواست توکن باید قابل استفاده باشد. برای دومین درخواست معتبر با یک Authorization Code که قبلاً برای صدور Access Token استفاده شده است، Authorization Server باید درخواست توکن را رد کند و هر توکن صادرشده‌ی مرتبط با آن Authorization Code را باطل نماید.                                                                                                                                                                                        | 1     |
| **10.4.3**  | تأیید کنید که Authorization Code دارای مدت زمان معتبر بودن محدود باشد. حداکثر طول عمر می‌تواند برای برنامه‌های کاربردی در سطوح L1 و L2 تا ۱۰ دقیقه و برای برنامه‌های کاربردی در سطح L3 تا ۱ دقیقه باشد.                                                                                                                                                                                                                                                                                                                                                                         | 1     |
| **10.4.4**  | برای یک Client مشخص، Authorization Server  فقط استفاده از Grantهایی را مجاز بداند که آن Client  به استفاده از آن‌ها نیاز دارد. توجه داشته باشید که Grantهای ‘token’ (Implicit Flow) و ‘password’ (Resource Owner Password Credentials Flow) دیگر نباید استفاده شوند.                                                                                                                                                                                                                                                                                                            | 1     |
| **10.4.5**  | Authorization Server باید حملات Refresh Token Replay را برای  Public Clientها کاهش دهد، ترجیحاً با استفاده از Sender-Constrained Refresh Tokens، یعنی Demonstrating Proof of Possession (DPoP) یا Certificate-Bound Access Tokens با استفاده از Mutual TLS (mTLS). برای برنامه‌های L1 و L2، می‌توان از Refresh Token Rotation استفاده کرد. اگر Refresh Token Rotation به‌کار گرفته شود، Authorization Server باید پس از استفاده، Refresh Token را باطل کند و اگر یک Refresh Token که قبلاً استفاده و باطل شده ارائه شود، تمام Refresh Tokenهای مربوط به آن مجوز را ابطال نماید. | 1     |
| **10.4.6**  | اگر از Code Grant استفاده شود، Authorization Server  باید حملات Authorization Code Interception  را با الزام به استفاده از Proof Key for Code Exchange (PKCE)  کاهش دهد. برای Authorization Requestها، Authorization Server  باید یک مقدار معتبر برای 'code_challenge' الزام کند و نباید مقدار 'code_challenge_method'  از نوع 'plain' را بپذیرد. برای Token Request، باید اعتبارسنجی پارامتر 'code_verifier' الزامی باشد.                                                                                                                                                      | 2     |
| **10.4.7**  | اگر Authorization Server از Unauthenticated Dynamic Client Registration  پشتیبانی می‌کند، ریسک مربوط به Client Applicationهای مخرب را باید کاهش دهد. این کار باید شامل اعتبارسنجی Client Metadata (مانند هر Registered URI)، اطمینان از رضایت کاربر، و هشدار به کاربر پیش از پردازش یک Authorization Request با یک Client Application غیرقابل اعتماد باشد.                                                                                                                                                                                                                      | 2     |
| **10.4.8**  | Refresh Tokenها باید دارای یک انقضای مطلق (Absolute Expiration) باشند، حتی اگر از Sliding Refresh Token Expiration استفاده شود.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 2     |
| **10.4.9**  | Refresh Tokenها و Reference Access Tokenها باید توسط کاربر مجاز از طریق User Interface Authorization Server قابل ابطال باشند، تا ریسک Clientهای مخرب یا توکن‌های سرقت‌شده کاهش یابد.                                                                                                                                                                                                                                                                                                                                                                                            | 2     |
| **10.4.10** | Confidential Client باید برای درخواست‌های Backchannel بین Client و Authorization Server، مانند Token Requests، Pushed Authorization Requests (PAR) و Token Revocation Requests، احراز هویت شود.                                                                                                                                                                                                                                                                                                                                                                                 | 2     |
| **10.4.11** | پیکربندی Authorization Server باید فقط Scopes موردنیاز را به OAuth Client اختصاص دهد.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 2     |
| **10.4.12** | برای یک Client مشخص، Authorization Server  فقط مقدار 'response_mode'  را که این Client نیاز دارد، مجاز بداند. برای مثال، با اعتبارسنجی این مقدار توسط Authorization Server در برابر مقادیر مورد انتظار یا با استفاده از Pushed Authorization Request (PAR) یا JWT-secured Authorization Request (JAR).                                                                                                                                                                                                                                                                          | 3     |
| **10.4.13** | Grant Type ‘code’ همواره همراه با Pushed Authorization Requests (PAR) باید استفاده شود.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 3     |
| **10.4.14** | Authorization Server باید فقط توکن‌های دسترسی از نوع وابسته به ارسال‌کننده (Proof-of-Possession) صادر می‌کند؛ چه به‌صورت توکن‌های دسترسی مبتنی بر گواهی از طریق TLS دوسویه (mTLS) و چه به‌صورت توکن‌های دسترسی وابسته به DPoP (Demonstration of Proof of Possession).                                                                                                                                                                                                                                                                                                           | 3     |
| **10.4.15** | برای یک کلاینت سمت‌سرور (که روی دستگاه کاربر نهایی اجرا نمی‌شود)، سرور احراز هویت اطمینان حاصل می‌کند که مقدار پارامترِ authorization_details  از بک‌اند کلاینت ارسال شده و کاربر در آن دستکاری نکرده است. به‌عنوان مثال، با الزام به استفاده از درخواست احراز هویت پوش‌شده (PAR) یا درخواست احراز هویت ایمن‌شده با JWT (JAR).                                                                                                                                                                                                                                                  | 3     |
| **10.4.16** | کلاینت باید از نوع Confidential Client  باشد و سرور احراز هویت استفاده از روش‌های قدرتمند احراز هویت کلاینت ـ مبتنی بر رمزنگاری کلید عمومی و مقاوم در برابر حملات replay attacks ـ را الزامی کند؛ مانند TLS دوسویه (tls_client_auth ‎، ‎self_signed_tls_client_auth  یا JWT مبتنی بر کلید خصوصی (private_key_jwt).                                                                                                                                                                                                                                                              | 3     |

## V10.5 OIDC Client

از آنجا که Relying Party در OIDC نقش یک کلاینت OAuth را هم ایفا می‌کند، الزامات بخش «OAuth Client» نیز در اینجا قابل اعمال هستند.

همچنین توجه داشته باشید که بخش «Authentication with an Identity Provider» در فصل «Authentication» نیز شامل الزامات عمومی مرتبط و مهمی است.

| #          | شرح الزام                                                                                                                                                                                                                                                                                                                                                                               | سطح |
|:----------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-----:|
| **10.5.1** | Client به‌عنوان Relying Partyباید  در برابر حملات بازپخش (Replay) توکن ID محافظت شده است. برای مثال، با بررسی اینکه مقدار claim مربوط به nonce  در ID Token دقیقاً با مقدار **nonce**ای که در درخواست احراز هویت به OpenID Provider  ارسال شده، یکسان باشد(که در OAuth 2 به آن authorization request ارسالی به authorization server گفته می‌شود).                                         | 2     |
| **10.5.2** | Client باید کاربر را به‌صورت یکتا از ID Token Claims شناسایی کند، معمولاً از ‘sub’ Claim ، که قابل انتساب مجدد به کاربران دیگر نیست (در محدوده‌ی همان Identity Provider).                                                                                                                                                                                                                 | 2     |
| **10.5.3** | Client باید تلاش‌های یک Authorization Server مخرب برای جا زدن خود به‌جای یک Authorization Server  دیگر از طریق متادیتای Authorization Server را رد می‌کند.کلاینت باید متادیتای Authorization Server را رد کند اگر مقدار issuer URL موجود در متادیتا دقیقاً با issuer URL از پیش پیکربندی‌شده و مورد انتظار کلاینت یکسان نباشد.                                                            | 2     |
| **10.5.4** | Client باید اعتبارسنجی کند ID Token برای استفاده توسط همان Client در نظر گرفته شده است (Audience)، با بررسی اینکه ‘aud’ Claim در توکن برابر با مقدار ‘client_id’ مربوط به Client باشد.                                                                                                                                                                                                    | 2     |
| **10.5.5** | هنگام استفاده ازOIDC Back-Channel Logout، Relying Party  از Denial of Service از طریق Forced Logout  و Cross-JWT Confusion در جریان Logout  باید جلوگیری کند. Client باید بررسی کند که Logout Token به درستی با مقدار typ  آن برابر با logout+jwt  باشد ، شامل ‘event’ Claim با نام عضو صحیح باشد و شامل ‘nonce’ Claim  نباشد. همچنین توصیه می‌شود Expiration کوتاه باشد (مثلاً ۲ دقیقه). | 2     |

## V10.6 OpenID Provider

از آنجا که OpenID Providerها نقش Authorization Server در OAuth را نیز ایفا می‌کنند، الزامات بخش «OAuth Authorization Server» در اینجا نیز قابل اعمال هستند.

 توجه شود در صورتی که از ID Token Flow و نه Code Flow استفاده شود، Access Tokenای صادر نمی‌شود و در نتیجه بسیاری از الزامات مربوط به OAuth Authorization Server قابل اعمال نخواهند بود.

| #          | شرح الزام                                                                                                                                                                                                                                                      | سطح |
|:----------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-----:|
| **10.6.1** | OpenID Provider  باید فقط مقادیر 'code'، 'ciba'، 'id_token' یا 'id_token code' را برای Response Mode  مجاز بداند. توجه داشته باشید که 'code' نسبت به 'id_token code' (که OIDC Hybrid Flow است) ترجیح داده می‌شود و 'token' (هر Implicit Flow) نباید استفاده شود. | 2     |
| **10.6.2** | OpenID Provider از Denial of Service از طریق Forced Logout جلوگیری کند. این کار با دریافت تأیید صریح از کاربر نهایی یا در صورت وجود، اعتبارسنجی پارامترها در Logout Request (که توسط Relying Party آغاز شده است)، مانند ‘id_token_hint’، انجام می‌شود.           | 2     |

## V10.7 Consent Management

این الزامات، فرآیند تأیید رضایت (Consent) کاربر توسط Authorization Server را پوشش می‌دهند.در صورت نبودِ تأیید صحیح رضایت کاربر، یک مهاجم می‌تواند از طریق جعل (Spoofing) یا مهندسی اجتماعی (Social Engineering) به‌جای کاربر مجوزها (Permissions) را به دست آورد.

| #          | شرح الزام                                                                                                                                                                                                                                                                                                                                                                                   | سطح |
|:----------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-----:|
| **10.7.1** | Authorization Server باید تضمین ‌کند کاربر برای هر درخواست مجوز (Authorization Request) رضایت خود را اعلام کرده است. در صورتی که هویت کلاینت قابل اطمینان نباشد، Authorization Server باید در همه موارد کاربر را به‌صورت صریح برای اعلام رضایت (Consent) راهنمایی و از او تأیید بگیرد.                                                                                                        | 2     |
| **10.7.2** | زمانی که Authorization Server از کاربر درخواست رضایت (Consent) می‌کند باید اطلاعات کافی و شفافی درباره آنچه کاربر در حال تأیید آن است ارائه ‌دهد. در صورت لزوم، این اطلاعات باید شامل این موارد باشد: ماهیت مجوزهای درخواستی )معمولاً بر اساس scope، resource server  و جزئیات مجوز در Rich Authorization Requests – RAR)، هویت برنامه یا اپلیکیشن دریافت‌کننده مجوز و مدت اعتبار این مجوزها. | 2     |
| **10.7.3** | کاربر باید بتواند رضایت‌هایی (Consents) را که از طریق Authorization Server صادر کرده است، مشاهده، ویرایش و لغو (Revoke) کند.                                                                                                                                                                                                                                                                  | 2     |

## References

برای اطلاعات بیشتر دربارهٔ OAuth، لطفاً مشاهده کنید:

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

برای الزامات مرتبط با OAuth در ASVS، از RFCهای منتشر شده و در وضعیت پیش‌نویس زیر استفاده می‌شود:

* [RFC6749 The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
* [RFC6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)
* [RFC6819 OAuth 2.0 Threat Model and Security Considerations](https://datatracker.ietf.org/doc/html/rfc6819)
* [RFC7636 Proof Key for Code Exchange by OAuth Public Clients](https://datatracker.ietf.org/doc/html/rfc7636)
* [RFC7591 OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591)
* [RFC8628 OAuth 2.0 Device Authorization Grant](https://datatracker.ietf.org/doc/html/rfc8628)
* [RFC8707 Resource Indicators for OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc8707)
* [RFC9068 JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
* [RFC9126 OAuth 2.0 Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126)
* [RFC9207 OAuth 2.0 Authorization Server Issuer Identification](https://datatracker.ietf.org/doc/html/rfc9207)
* [RFC9396 OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)
* [RFC9449 OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)
* [RFC9700 Best Current Practice for OAuth 2.0 Security](https://datatracker.ietf.org/doc/html/rfc9700)
* [draft OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)<!-- recheck on release -->
* [draft The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12)<!-- recheck on release -->

برای اطلاعات بیشتر در مورد OpenID Connect، لطفاً به بخش زیر مراجعه کنید:

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
