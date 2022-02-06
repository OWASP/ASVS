# ت5: التحقق من الصحة Validation والتعقيم Sanitization  والترميز Encoding

## الهدف من ضوابط الأمان

إن أكثر نقاط ضعف أمان تطبيقات الويب شيوعًا هي الفشل في التحقق بشكل صحيح من المدخلات الواردة Input validation  من العميل أو البيئة قبل استخدامها مباشرة دون أي ترميز للمخرجاتoutput encoding . تؤدي هذه المشكلة تقريبًا إلى جميع نقاط الضعف المهمة في تطبيقات الويب ، مثل البرمجة النصية عبر الموقع Cross-Site Scripting (XSS) ، وحقن قواعد البيانات SQL injection ، وحقن المترجم interpreter injection ، وهجمات الإعدادات المحلية / Unicode (locale/Unicode attacks)، وهجمات نظام الملفات file system attacks ، وتدفقات المخزن المؤقت buffer overflows.

تأكد من أن التطبيق الذي يتم التحقق منه يفي بالمتطلبات عالية المستوى التالية:

* التحقق من صحة المدخلات ومعمارية ترميز المخرجات output encoding architecture لهاpipeline  متفق عليه لمنع هجمات الحقن.
* يتم كتابة بيانات المدخلات بشكل صارم strongly typed ، ويتم التحقق من صحتها ومن النطاق  range أو الطول ، أو في أسوأ الأحوال ، يتم تعقيمها sanitized أو تصفيتها filtered.
* يتم ترميز بيانات المخرجاتencoded  أو تفعيل أحرف الهروب escaped وفقًا لسياق البيانات context of the data  بحيث تكون أقرب ما يمكن للمترجم interpreter.

في هندسة تطبيقات الويب الحديثة ، أصبح ترميز المخرجات أكثر أهمية من أي وقت مضى. من الصعب توفير التحقق القوي من صحة المدخلات في سيناريوهات معينة ، لذا فإن استخدام واجهة برمجة تطبيقات أكثر أمانًا safer API مثل الاستعلامات ذات البارامترات parameterized queries  أو إطارات عمل القوالب التلقائية auto-escaping templating frameworks أو اختيار طريقة ترميز المخرجات بعناية أمر بالغ الأهمية لأمان التطبيق.

## ق1.5 التحقق من صحة المدخلات

إن استخدام قوائم السماح الإيجابيةpositive allow lists  وكتابة البيانات بشكل صارم strong data typing في ضوابط التحقق من صحة المدخلات المطبقة بشكل صحيح يمكّن من القضاء على أكثر من 90٪ من جميع هجمات الحقن. يمكن لفحوصات الطول والنطاق Length and range checks أن تقلل هذا بدرجة أكبر. إن البناء باستخدام التحقق الآمن من صحة المدخلات هو مطلوب في معمارية التطبيق، وسرعة التصميم ، وكتابة الشيفرة المصدرية، واختبارات الوحدة والتكامل unit and integration testing. على الرغم من أن العديد من هذه العناصر لا يمكن العثور عليها في اختبارات الاختراق ، إلا أن نتائج عدم تنفيذها توجد عادةً في ق3.5 - متطلبات ترميز المخرجات ومنع الحقن. يوصى المطورين ومراجعي الشيفرة المصدرية الآمنة secure code reviewers بالتعامل مع هذا القسم كما لو كان L1 مطلوبًا لجميع العناصر لمنع عمليات الحقن.

| # | التوصيف | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.1.5** | تحقق من أن التطبيق لديه دفاعات ضد هجمات تلوث مدخلات HTTP (HTTP parameter pollution attacks)، خاصةً إذا كان إطار عمل التطبيق application framework  لا يميز مصدر مدخلات الطلب (GET أو POST أو ملفات تعريف الارتباط cookies أو الرؤوس headers أو متغيرات البيئة environment variables). | ✓ | ✓ | ✓ | 235 |
| **2.1.5** | تحقق من أن إطارات العمل تحمي من هجمات تخصيص المدخلات الجماعية mass parameter assignment attacks ، أو أن التطبيق لديه إجراءات مضادة للحماية من تعيين قيم المدخلات بشكل غير آمن unsafe parameter assignment ، مثل وضع علامة على الحقول على أنها خاصة أو مشابهة marking fields private. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 915 |
| **3.1.5** | تأكد من التحقق من صحة جميع المدخلات (حقول نموذج HTML (HTML form fields) وطلبات REST وبارامترات URL ورؤوس HTTP وملفات تعريف الارتباط Cookies و batch files و RSS feedsوما إلى ذلك) باستخدام التحقق الإيجابي (قوائم السماح).  ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **4.1.5** | Vتحقق من أن البيانات المنظمة مكتوبة بشكل صارم وتم التحقق من صحتها مقابل مخطط schema  محدد بما في ذلك الأحرف المسموح بها والطول والنمط (مثل أرقام بطاقة الائتمان، البريد الالكتروني وأرقام الهواتف ، أو التحقق من صحة حقلين مرتبطين ، مثل التحقق من الضاحية ومطابقة الرمز البريدي).  ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.5** | تحقق من أن عمليات إعادة التوجيه إلى الخلف وإعادة التوجيه إلى الأمام (URL redirects and forwards) لعناوين URL تسمح فقط بالوجهات التي تظهر في قائمة السماح ، أو تظهر تحذيرًا عند إعادة التوجيه إلى محتوى يحتمل أن يكون غير موثوق به. | ✓ | ✓ | ✓ | 601 |

## ق2.5 التعقيم Sanitization ووضع الحماية Sandboxing

| # | التوصيف | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.2.5** | تحقق من أن جميع مدخلات HTML غير الموثوق بها من محرري WYSIWYG أو ما شابهها قد تم تعقيمها بشكل صحيح باستخدام HTML sanitizer library  أو ميزة في إطار العمل. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **2.2.5** | تحقق من تعقيم البيانات غير المهيكلة unstructured لفرض تدابير السلامة مثل الأحرف والطول المسموح بهما. | ✓ | ✓ | ✓ | 138 |
| **3.2.5** | تحقق من أن التطبيق يقوم بتعقيم مدخلات المستخدم قبل المرور إلى أنظمة البريد للحماية من هجمات حقن SMTP أو IMAP. | ✓ | ✓ | ✓ | 147 |
| **4.2.5** | تحقق من أن التطبيق يتجنب استخدام ()eval أو ميزات تنفيذ التعليمات البرمجية الديناميكية الأخرى dynamic code execution features. في حالة عدم وجود بديل ، يجب تعقيم sanitized أي مدخلات للمستخدم يتم تضمينه أو استخدام وضع الحماية sandboxed له قبل تنفيذه. | ✓ | ✓ | ✓ | 95 |
| **5.2.5** | تحقق من أن التطبيق يحمي من هجمات حقن القالب template injection attacks من خلال التأكد من أن أي مدخلات للمستخدم يتم تضمينه معقم أو وضع الحماية. | ✓ | ✓ | ✓ | 94 |
| **6.2.5** | تحقق من أن التطبيق يحمي من هجمات SSRF ، عن طريق التحقق من صحة البيانات غير الموثوق بها أو بيانات تعريف ملف HTTP (HTTP file metadata) أو تعقيمها ، مثل أسماء الملفات وحقول مدخلات عنوان URL ، واستخدام قوائم البروتوكولات والنطاقات والمسارات والمنافذ المسموح بها. | ✓ | ✓ | ✓ | 918 |
| **7.2.5** | تحقق من أن التطبيق يقوم بتعقيم أو تعطيل أو وضع الحماية للمحتوى القابل للبرمجة Scalable Vector Graphics (SVG) الذي يوفره المستخدم ، خاصةً فيما يتعلق بـ XSS الناتج عن البرامج النصية المضمنة inline scripts و ForeignObject. | ✓ | ✓ | ✓ | 159 |
| **8.2.5** | تحقق من أن التطبيق يقوم بتعقيم أو تعطيل أو وضع الحماية لمحتوى لغة قالب التعبير user-supplied scriptable  أو لغة قالب التعبير  expression template languageالتي يوفرها المستخدم ، مثل Markdown أو CSS أو XSL Stylesheets أو BBCode أو ما شابه ذلك. | ✓ | ✓ | ✓ | 94 |

## ق3.5 ترميز المخرجات ومنع الحقن

يعد ترميز المخرجات بالقرب من المترجم أو بجواره أمرًا بالغ الأهمية لأمن أي تطبيق. عادةً ، ترميز المخرجات هو غير دائم not persisted ، ولكن يتم استخدامه لجعل المخرجات آمنة في سياق المخرجات المناسب للاستخدام الفوري. سيؤدي الفشل في ترميز المخرجات إلى تطبيق غير آمن وقابل للحقن.

| # | التوصيف | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.3.5** | تحقق من أن ترميز المخرجات مناسب للمترجم والسياق المطلوب. على سبيل المثال ، استخدم المرمزات encoders خصيصًا لقيم HTML ، وسماتHTML  attributes)  (HTML  ، وJavaScript ، وبارامترات URL ، ورؤوس HTTP ، و SMTP ، وغيرها كما يتطلب السياق ، لا سيما من المدخلات غير الموثوق بها (مثل الأسماء التي تحتوي على Unicode أو الفواصل العليا ، مثل ね こ أو O'Hara). ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **2.3.5** | تحقق من أن ترميز المخرجات يحافظ على مجموعة الأحرف واللغة التي اختارها المستخدم، بحيث تكون أي نقطة محرف Unicode (Unicode character point) صالحة ويتم التعامل معها بأمان. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 176 |
| **3.3.5** | تحقق من العناية بالسياق context-aware ، ويفضل أن يكون مؤتمتًا - أو في أسوأ الأحوال ، يدويًا - يحمي من XSS المنعكس والمخزن والمستند إلى DOM (reflected, stored, and DOM based XSS). ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 79 |
| **4.3.5** | تحقق من أن اختيار البيانات أو استعلامات قاعدة البيانات (مثل SQL و HQL و ORM و NoSQL) تستخدم الاستعلامات ذات المدخلات parameterized  أو ORMs أو أطر عمل الكيانات entity frameworks أو أن تكون محمية بطريقة أخرى من هجمات حقن قواعد البيانات. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.5** | تحقق من أنه في حالة عدم وجود parameterized  أو تقنيات أكثر أمانًا ، يتم استخدام ترميز المخرجات الخاص بالسياق للحماية من هجمات الحقن ، مثل استخدام SQL escaping للحماية من حقن SQL. ([C3, C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **6.3.5** | تحقق من أن التطبيق يحمي من هجمات حقن JSON وهجمات JSON eval وJavaScript expression evaluation. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 830 |
| **7.3.5** | تحقق من أن التطبيق يحمي من الثغرات الأمنية كحقن LDAP ، أو أنه يتم تنفيذ ضوابط أمان محددة لمنع حقن LDAP. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 90 |
| **8.3.5** | تحقق من أن التطبيق يحمي من حقن أوامر نظام التشغيل وأن استدعاءات نظام التشغيل تستخدم استعلامات نظام تشغيل ذات مدخلات parameterized OS queries  أو تستخدم ترميز إخراج سطر الأوامر السياقي contextual command line output encoding. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 78 |
| **9.3.5** | تحقق من أن التطبيق يحمي من هجمات تضمين الملفات المحلية Local File Inclusion (LFI)  أو تضمين الملفات عن بُعد Remote File Inclusion (RFI). | ✓ | ✓ | ✓ | 829 |
| **1.3.5** | تحقق من أن التطبيق يحمي من حقن XPath أو هجمات حقن XML. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 643 |

ملاحظة: استخدام الاستعلامات ذات المدخلات parameterized queries أو الهروب من SQL (parameterized queries) لا يكفي دائمًا ؛ لا يمكن الهروب من أسماء الجداول والأعمدة ، ORDER BY وما إلى ذلك. يؤدي تضمين البيانات التي قدمها المستخدم التي تم تجاوزها في هذه الحقول إلى فشل الاستعلامات أو حقن SQL.

ملاحظة: يسمح تنسيق SVG صراحةً بـ ECMA script  في جميع السياقات تقريبًا ، لذلك قد لا يكون من الممكن حظر جميع SVG XSS vectors  تمامًا. إذا كان تحميل SVG مطلوبًا ، فنحن نوصي بشدة إما بتقديم هذه الملفات التي تم تحميلها كـ text/plain أو استخدام مجال محتوى منفصل يوفره المستخدم separate user supplied content domain لمنع XSS الناجح من الاستيلاء على التطبيق.

## ق4.5 الذاكرة Memory والسلسلة String والشيفرة المصدرية غير المُدارة unmanaged code

سيتم تطبيق المتطلبات التالية فقط عندما يستخدم التطبيق لغة أنظمة systems language أو شيفرة مصدرية غير مُدارة unmanaged code.

| # | التوصيف | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.4.5** | تحقق من أن التطبيق يستخدم سلسلة آمنة للذاكرة memory-safe string ونسخ ذاكرة أكثر أمانًا و المؤشرpointer arithmetic  لاكتشاف أو منع stack, buffer, heap overflows. | | ✓ | ✓ | 120 |
| **2.4.5** | تحقق من أن سلاسل التنسيق format strings  لا تأخذ مدخلات يحتمل أن تكون معادية ، وأنها ثابتة. | | ✓ | ✓ | 134 |
| **3.4.5** | تحقق من استخدام تقنيات التحقق من صحة الإشارة والمجال والمدخلات sign, range, and input validation techniques  لمنع integer overflows.  | | ✓ | ✓ | 190 |

## ق5.5 متطلبات منع فك التسلسل

| # | التوصيف | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.5.1** | تحقق من أن الكائنات المتسلسلة تستخدم فحوصات سلامة integrity checks أو أنها مشفرة لمنع إنشاء كائن معاد hostile object creation  أو التلاعب بالبيانات data tampering.  ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 502 |
| **5.5.2** | تحقق من أن التطبيق يقيد محللات XML (XML Parsers) بشكل صحيح لاستخدام التكوين الأكثر تقييدًا restrictive configuration  وللتأكد من تعطيل الميزات غير الآمنة مثل حل الكيانات الخارجية resolving external entities لمنع هجمات XML eXternal Entity (XXE). | ✓ | ✓ | ✓ | 611 |
| **5.5.3** | تحقق من أن فك تسلسل البيانات غير الموثوق بها يتم تجنبه أو حمايته في كل من التعليمات البرمجية المخصصة ومكتبات الجهات الخارجية (مثل محللات JSON و XML و YAML). | ✓ | ✓ | ✓ | 502 |
| **5.5.4** | تحقق من أنه عند تحليل JSON في المتصفحات أو الخلفيات المستندة إلى JavaScript ، يتم استخدام JSON.parse لتحليل مستند JSON. لا تستخدم ()eval  لتحليل JSON. | ✓ | ✓ | ✓ | 95 |

## المراجع

لمزيد من المعلومات، يمكن أيضاً الاطلاع على:

* [OWASP Testing Guide 4.0: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Cheat Sheet: Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution.html)
* [OWASP LDAP Injection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client Side Testing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client_Side_Testing/)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [XML External Entity (XXE) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)

لمزيد من المعلومات حول الهروب التلقائي auto-escaping ، يرجى الاطلاع على:

* [Reducing XSS by way of Automatic Context-Aware Escaping in Template Systems](https://googleonlinesecurity.blogspot.com/2009/03/reducing-xss-by-way-of-automatic.html)
* [AngularJS Strict Contextual Escaping](https://docs.angularjs.org/api/ng/service/$sce)
* [AngularJS ngBind](https://docs.angularjs.org/api/ng/directive/ngBind)
* [Angular Sanitization](https://angular.io/guide/security#sanitization-and-security-contexts)
* [Angular Security](https://angular.io/guide/security)
* [ReactJS Escaping](https://reactjs.org/docs/introducing-jsx.html#jsx-prevents-injection-attacks)
* [Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

لمزيد من المعلومات حول فك التسلسل deserialization ، يرجى الاطلاع على:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [OWASP Deserialization of Untrusted Data Guide](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)
