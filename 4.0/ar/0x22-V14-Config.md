# ت14: التكوين

## الهدف من ضوابط الأمان

تأكد من أن التطبيق الذي يتم التحقق منه لديه:

* بيئة بناء build environment آمنة وقابلة للتكرار وقابلة للأتمتة automatable.
* أن  تكون مكتبات الطرف الثالث Third-party libraries، وإدارة التبعية dependency والتكوين configuration  متينة Hardened بحيث لا يتم تضمين المكونات القديمة أو غير الآمنة في التطبيق.

يجب أن يكون تكوين التطبيق الذي يتضمن التشغيل الأساسي فقط آمنًا ليكون على الإنترنت ، مما يعني تكوينًا خارج الصندوق بشكل آمن(safe out of the box).

## ق1.14 البناء والنشر Build and Deploy

الأنابيب الخاصة بالبناء Build pipelines  هو الأساس للأمان المتكرر - في كل مرة يتم اكتشاف شيء غير آمن ، يمكن حله في الشيفرة المصدرية ، أو السكربتات الخاصة بالبناء أو النشر  build or deployment scripts ، واختبارها تلقائيًا. نحن نشجع بشدة على استخدام الأنابيب الخاصة بالبناء Build pipelines مع عمليات فحص الأمان والتبعية المؤتمتة automatic security and dependency checks  والتي تحذر أو تكسر البناء warn or break the build لمنع نشر مشكلات الأمان المعروفة في بيئة الإنتاج الحقيقية. تؤدي الخطوات اليدوية التي يتم إجراؤها بشكل غير منتظم مباشرة إلى أخطاء أمنية يمكن تجنبها.

بما أن الصناعة تنتقل إلى نموذج DevSecOps ، من المهم ضمان استمرار توافر وسلامة النشر deployment  والتكوين configuration  لتحقيق حالة "جيدة معروفة known good ". في الماضي ، إذا تم اختراق نظام ما ، فقد يستغرق الأمر أيامًا إلى شهور لإثبات عدم حدوث مزيد من الاختراقات. اليوم ، مع ظهور بنية تحتية محددة بالبرمجيات ، وعمليات نشر A / B سريعة rapid A/B deployments بدون توقف ، وإنشاء حاويات آلية للبناء automated containerized builds ، فمن الممكن بشكل تلقائي ومستمر بناء ، وتقوية ، ونشر بديل "معروف بشكل جيد "known good" لأي نظام مخترق

إذا كانت النماذج التقليدية لا تزال موجودة، فيجب اتخاذ خطوات يدوية لتقوية هذا التكوين وعمل نسخة احتياطية منه للسماح باستبدال الأنظمة المخترقة بأنظمة ذات سلامة عالية وغير مخترقة في الوقت المناسب.

يتطلب الامتثال لهذا القسم نظام بناء مؤتمتًا automated build system ، وإمكانية الوصول إلى السكربتات الخاصة بالبناء أو النشر  build or deployment scripts.

| # | التوصيف | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.1.14** | تحقق من تنفيذ عمليات بناء التطبيق ونشره بطريقة آمنة وقابلة للتكرار ، مثل أتمتة CI / CD ، وإدارة التكوين المؤتمت automated configuration management، وسكربتات النشر المؤتمت automated deployment scripts. | | ✓ | ✓ | |
| **2.1.14** | تحقق من تكوين أعلام المترجم compiler flags  لتمكين جميع عمليات الحماية والتحذيرات المتاحة لـ buffer overflow protections ، بما في ذلك التوزيع العشوائي للمكدس stack randomization  ، ومنع تنفيذ البيانات data execution prevention ، ولكسر البناء o break the build إذا تم العثور على مؤشر أو ذاكرة أو سلسلة تنسيق أو عدد صحيح أو عمليات السلسلة غير آمنة unsafe pointer, memory, format string, integer, or string operations. | | ✓ | ✓ | 120 |
| **3.1.14** | تحقق من أن تكوين الخادم مقوّى hardened  وفقًا لتوصيات مخدم التطبيق والأطر المستخدمة. | | ✓ | ✓ | 16 |
| **4.1.14** | تحقق من أن التطبيق والتكوين وجميع التبعيات dependencies يمكن إعادة نشرها باستخدام سكربتات النشر المؤتمت automated deployment scripts، والتي تم إنشاؤها من دفتر تشغيل runbook  موثق ومختبر في وقت معقول ، أو استعادتها من النسخ الاحتياطية في الوقت المناسب. | | ✓ | ✓ | |
| **5.1.14** | تحقق من أن المسؤولين المصرح لهم يمكنهم التحقق من سلامة جميع التكوينات ذات الصلة بالأمان لاكتشاف التلاعب. | | | ✓ | |

## ق2.14 التبعية Dependency

تعد إدارة التبعية  Dependency أمرًا بالغ الأهمية للتشغيل الآمن لأي تطبيق من أي نوع. يعد الفشل في مواكبة التبعيات القديمة أو غير الآمنة هو السبب الجذري لأكبر الهجمات وأكثرها تكلفة حتى الآن.

ملاحظة: في المستوى 1 ، يتعلق الامتثال بالبند 1.2.14 بالملاحظات أو اكتشافات جانب العميل والمكتبات والمكونات الأخرى ، بدلاً من التحليل الثابت للشيفرة المصدرية static code analysis  أو تحليل التبعية dependency analysis الأكثر دقة. يمكن اكتشاف هذه التقنيات الأكثر دقة عن طريق المقابلة كما هو مطلوب.

| # | التوصيف | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.2.14** | تحقق من أن جميع المكونات محدثة ، ويفضل استخدام مدقق التبعية dependency checker أثناء وقت البناء build أو الترجمة compile. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1026 |
| **2.2.14** | تحقق من إزالة جميع الميزات والوثائق ونماذج التطبيقات والإعدادات غير الضرورية. | ✓ | ✓ | ✓ | 1002 |
| **3.2.14** | تحقق من أنه إذا كانت أصول التطبيق ، مثل مكتبات JavaScript أو CSS أو خطوط الويب ، مستضافة خارجيًا على شبكة توصيل المحتوى Content Delivery Network (CDN) أو مزود خارجي ، فيجب أن يتم استخدام تكامل الموارد الفرعية Subresource Integrity (SRI) للتحقق من سلامة الأصل asset. | ✓ | ✓ | ✓ | 829 |
| **4.2.14** | تحقق من أن مكونات المكتبات الخارجية تأتي من مستودعات repositories محددة مسبقًا وموثوقة وتتم صيانتها باستمرار.  ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 829 |
| **5.2.14** | تحقق من الاحتفاظ بقائمة مواد البرمجيات Software Bill of Materials (SBOM) لكافة المكتبات الخارجية third party libraries المستخدمة. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **6.2.14** | تحقق من تخفيض سطح الهجوم attack surface  عن طريق وضع الحماية sandbox أو تغليف المكتبات الخارجية لكشف السلوك المطلوب فقط في التطبيق. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |

## ق3.14 الإفصاح الأمني غير المقصود

يجب تقوية التكوينات الخاصة بالبيئة الحقيقية للحماية من الهجمات الشائعة ، مثل debug consoles ، ورفع مستوى هجمات البرمجة النصية عبر المواقع Cross-site Scripting (XSS) و Remote File Inclusion (RFI) ، وللتخلص من "نقاط الضعف" في اكتشاف المعلومات غير المهمة والمتواجدة من تقارير اختبار الاختراق. نادرًا ما يتم تصنيف العديد من هذه المشكلات على أنها مخاطر كبيرة ، ولكنها مرتبطة ببعضها البعض مع نقاط ضعف أخرى. إذا لم تكن هذه المشكلات موجودة بشكل افتراضي ، فإنها ترفع المستوى قبل أن تنجح معظم الهجمات.

| # | التوصيف | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.3.14** | [تم حذفها ، مكررة عن 1.4.7] | | | | |
| **2.3.14** | تحقق من أن أنماط تصحيح الأخطاء debug modes  في  إطار عمل التطبيق أو خادم الويب والتطبيق معطلة في البيئة الحقيقية لإزالة ميزات تصحيح الأخطاء debug features  ووحدات تحكم المطورين developer consoles  وإفصاحات الأمان غير المقصودة unintended security disclosures. | ✓ | ✓ | ✓ | 497 |
| **3.3.14** | تحقق من أن رؤوس HTTP أو أي جزء من استجابة HTTP لا تعرض معلومات إصدار تفصيلية لمكونات النظام. | ✓ | ✓ | ✓ | 200 |

## ق4.14 رؤوس أمان HTTP

| # | التوصيف | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.4.14** | تحقق من أن كل استجابة HTTP تحتوي على رأس نوع المحتوى Content-Type header. أيضاً يجب أن تحدد مجموعة محارف character set  آمنة (على سبيل المثال ، UTF-8 و ISO-8859-1). إذا كان المحتوى هو text / * و / + xml و application / xml فيجب أن يتوافق المحتوى مع رأس نوع المحتوى. | ✓ | ✓ | ✓ | 173 |
| **2.4.14** | تحقق من أن جميع استجابات API تحتوي على رأس Content-Disposition: attachment؛ filename="api.json" (أو اسم ملف آخر مناسب لنوع المحتوى). | ✓ | ✓ | ✓ | 116 |
| **3.4.14** | تحقق من وجود رأس استجابة سياسة أمان المحتوى Content Security Policy (CSP) header التي تساعد في التخفيف من تأثير هجمات XSS مثل ثغرات حقن HTML و DOM و JSON و JavaScript. | ✓ | ✓ | ✓ | 1021 |
| **4.4.14** | تحقق من أن جميع الاستجابات تحتوي على  X-Content-Type-Options: nosniff header. | ✓ | ✓ | ✓ | 116 |
| **5.4.14** | تحقق من تضمين Strict-Transport-Security header في جميع الاستجابات ولجميع النطاقات الفرعية subdomains ، مثل Strict-Transport-Security: max-age=15724800; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **6.4.14** | تحقق من تضمين Referrer-Policy header  مناسب لتجنب كشف المعلومات الحساسة في عنوان URL من خلال الرأس "Referer" لأطراف غير موثوق بها. | ✓ | ✓ | ✓ | 116 |
| **7.4.14** | تحقق من أن محتوى تطبيق الويب لا يمكن تضمينه في موقع جهة خارجية بشكل افتراضي وأن تضمين الموارد الدقيقة مسموح به فقط عند الضرورة باستخدام الرؤوس Content-Security-Policy: frame-ancestors and X-Frame-Options response headers. | ✓ | ✓ | ✓ | 1021 |

## ق5.14 متطلبات رأس طلب HTTP

| # | التوصيف | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.5.14** | تحقق من أن خادم التطبيق لا يقبل سوى طرق  HTTP المستخدمة من قبل التطبيق / واجهة برمجة التطبيقات ، بما في ذلك pre-flight OPTIONS ، والسجلات / التنبيهات بشأن أي طلبات غير صالحة لسياق التطبيق. | ✓ | ✓ | ✓ | 749 |
| **2.5.14** | تحقق من أن Origin header  المقدم لا يتم استخدامه للمصادقة أو قرارات التحكم في الوصول ، حيث يمكن للمهاجم تغيير عنوان Origin بسهولة. | ✓ | ✓ | ✓ | 346 |
| **3.5.14** | تحقق من أن Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header  يستخدم قائمة سماح صارمة للنطاقات الموثوقة والمجالات الفرعية للمطابقة معها ولا يدعم الأصل "الفارغ" "null" origin. | ✓ | ✓ | ✓ | 346 |
| **4.5.14** | تحقق من أن رؤوس HTTP المضافة بواسطة proxy  موثوق به أو أجهزة SSO ، مثل رمز الحامل bearer token ، قد تمت مصادقتها بواسطة التطبيق. | | ✓ | ✓ | 306 |

## المراجع

لمزيد من المعلومات، يمكن أيضاً الاطلاع على:

* [OWASP Web Security Testing Guide 4.1: Testing for HTTP Verb Tampering]( https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* •	تساعد إضافة Content-Disposition إلى استجابات واجهة برمجة التطبيقات على منع العديد من الهجمات استنادًا إلى سوء فهم نوع MIME بين العميل والخادم ، ويساعد خيار "filename" على وجه التحديد في منع [Reflected File Download attacks هجمات تنزيل الملفات المنعكسة Reflected](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Sandboxing third party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
