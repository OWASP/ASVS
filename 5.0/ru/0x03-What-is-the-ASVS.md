# What is the ASVS?

Стандарт верификации требований к безопасности приложений (ASVS) определяет требования безопасности для веб-приложений и сервисов, представляя собой ценный ресурс для всех, кто стремится проектировать, разрабатывать и поддерживать безопасные приложения или оценивать их уровень защищённости.

В этой главе описываются ключевые аспекты применения ASVS, включая его область действия, структуру уровней, основанных на приоритетах, и основные сценарии использования стандарта.

## Область действия ASVS

Область действия ASVS определяется его названием: Приложение (Application), Безопасность (Security), Верификация (Verification) и Стандарт (Standard). Он устанавливает, какие требования включены в стандарт, а какие — исключены из него, с глобальной целью определения основополагающих принципов безопасности, которые должны быть достигнуты. Область действия также учитывает требования к документации, которые служат основой для требований к реализации.

Не существует такого понятия, как «область действия» для злоумышленника. Поэтому требования ASVS должны оцениваться в совокупности с рекомендациями по другим аспектам жизненного цикла приложения, включая процессы CI/CD, хостинг и операционную деятельность.

### Приложение

ASVS определяет «Приложение» как разрабатываемый программный продукт, в который должны быть интегрированы механизмы безопасности. ASVS не регламентирует процессы жизненного цикла разработки и не указывает на методы сборки приложения в CI/CD; Его задача — описать требуемый уровень защищённости, который должен быть достигнут в конечном продукте.

Компоненты для обработки HTTP-трафика (WAF, балансировщики нагрузки, прокси) могут считаться частью приложения в контексте безопасности, поскольку некоторые механизмы безопасности напрямую зависят от них или могут быть реализованы с их помощью. Это касается требований по кешированию, rate limiting, а также фильтрации входящих/исходящих подключений по источнику и получателю.

В свою очередь, ASVS не включает требования, относящиеся к приложению напрямую или находящиеся за пределами его зоны ответственности. Так, например, проблемы DNS обычно относятся в ведении отдельной команды или функции.

Аналогично, хотя в зону ответственности приложения входит обработка входящих данных и генерация исходящих данных, если внешний процесс взаимодействует с приложением или его данными, это считается выходящим за рамки ASVS. Например, резервное копирование приложения или его данных обычно выполняется внешними процессами и не контролируется самим приложением или его разработчиками.

### Безопасность

Каждое требование должно иметь очевидное влияние на безопасность. Отсутствие требования должно привести к снижению уровня защищённости приложения, а реализация требования должна либо уменьшить  вероятность возникнования риска безопасности, либо смягчить последствия.

Все прочие аспекты, такие как функциональные характеристики, стиль кода или требования политик, выходят за рамки стандарта.

### Верификация

Требование должно быть верифицируемым, а его проверка должна приводить к однозначному решению: «не выполнено» или «выполнено».

### Стандарт

ASVS представляет собой набор требований безопасности, которые необходимо реализовать для соответствия стандарту. Это означает, что требования ограничиваются определением целевого показателя безопасности, которого необходимо достичь. Прочая сопутствующая информация может быть надстроена на основе ASVS или связана с ним через сопоставления.

В частности, в рамках OWASP существует множество проектов, и ASVS намеренно избегает дублирования содержания других проектов. Например, у разработчиков может возникнуть вопрос: «как мне реализовать конкретное требование в моем технологическом стеке или окружении?» — на него должен отвечать проект Cheat Sheet Series. У тестировщиков может возникнуть вопрос: «как мне проверить это требование в данном окружении?» — на него должен отвечать проект Web Security Testing Guide.

Хотя ASVS предназначен не только для специалистов по безопасности, он ожидает, что читатель обладает техническими знаниями для понимания содержания или способен самостоятельно изучить конкретные концепции.

### Требование

Слово "Требование" специально используется в ASVS, поскольку оно обязательное условие, которое должно быть достигнуто для его выполнения. ASVS содержит только требования (обязательно к выполнению) и не содержит рекомендаций.

Другими словами, рекомендации, независимо от того, являются ли они лишь одним из многих возможных вариантов для решения проблем или вопросов стиля кода, не удовлетворяют определению требования.

Требования ASVS предназначены для целевых конкретных принципов безопасности без привязки к конкретной реализации или технологии, в то же время, являясь самоочевидными в отношении того, зачем они существуют. Это также означает, что требования не основаны на конкретном методе проверки или реализации.

### Документированные решения по безопасности

В области безопасности программного обеспечения заблаговременное планирование архитектуры безопасности и защитных механизмов позволяет добиться более последовательной и предсказуемой реализации в конечном продукте или функции.

Кроме того, некоторые требования сложны в реализации и зависят от специфики приложения. Например, система прав доступа, проверка вводимых данных и защита данных с разной степенью чувствительности.

Чтобы учесть это, вместо общих формулировок, таких как «все данные должны быть зашифрованы», или попыток охватить каждый возможный случай в требовании, были включены требования к документации. Они предписывают, чтобы подход и конфигурация, выбранные разработчиком приложения для механизмов управления, были задокументированы. Это позволяет провести оценку целесообразности подхода, а затем сравнить фактическую реализацию с документацией, чтобы оценить, соответствует ли реализация ожиданиям.

Задача этих требований — фиксировать решения, которые организация-разработчик приняла в отношении того, каким образом реализовать определенные требования безопасности.

Требования к документации всегда размещаются в первом разделе главы (хотя присутствуют не в каждой из них), и каждое из них всегда связано с соответствующим требованием к реализации, в рамках которого документированные решения должны быть воплощены на практике. Ключевая идея заключается в том, что проверка наличия документации и проверка фактической реализации — это два самостоятельных вида деятельности.

There are two key drivers for including these requirements. The first driver is that a security requirement will often involve enforcing rules e.g., what kind of file types are allowed to be uploaded, what business controls should be enforced, what are the allowed characters for a particular field. These rules will differ for every application, and therefore, the ASVS cannot prescriptively define what they should be, nor will a cheat sheet or more detailed response help in this case. Similarly, without these decisions being documented, it will not be possible to perform verification of the requirements that implement these decisions.

The second driver is that for certain requirements, it is important to provide an application development with flexibility regarding how to address particular security challenges. For example, in previous ASVS versions, session timeout rules were very prescriptive. Practically speaking, many applications, especially those that are consumer-facing, have much more relaxed rules and prefer to implement other mitigation controls instead. Documentation requirements, therefore, explicitly allow for flexibility around this.

Clearly, it is not expected that individual developers will be making and documenting these decisions but rather the organization as a whole will be taking those decisions and making sure that they are communicated to developers who then make sure to follow them.

Providing developers with specifications and designs for new features and functionality is a standard part of software development. Similarly, developers are expected to use common components and user interface mechanisms rather than just making their own decisions each time. As such, extending this to security should not be seen as surprising or controversial.

There is also flexibility around how to achieve this. Security decisions might be documented in a literal document, which developers are expected to refer to. Alternatively, security decisions could be documented and implemented in a common code library that all developers are mandated to use. In both cases, the desired result is achieved.

## Application Security Verification Levels

The ASVS defines three security verification levels, with each level increasing in depth and complexity. The general aim is for organizations to start with the first level to address the most critical security concerns, and then move up to the higher levels according to the organization and application needs. Levels may be presented as L1, L2, and L3 in the document and in requirement texts.

Each ASVS level indicates the security requirements that are required to achieve from that level, with the higher remaining level requirements as recommendations.

In order to avoid duplicate requirements or requirements that are no longer relevant at higher levels, some requirements apply to a particular level but have more stringent conditions for higher levels.

### Level evaluation

Levels are defined by priority-based evaluation of each requirement based on experience implementing and testing security requirements. The main focus is on comparing risk reduction with the effort to implement the requirement. Another key factor is to keep a low barrier to entry.

Risk reduction considers the extent to which the requirement reduces the level of security risk within the application, taking into account the classic Confidentiality, Integrity, and Availability impact factors as well as considering whether this is a primary layer of defense or whether it would be considered defense in depth.

The rigorous discussions around both the criteria and the leveling decisions have resulted in an allocation which should hold true for the vast majority of cases, whilst accepting that it may not be a 100% fit for every situation. This means that in certain cases, organizations may wish to prioritize requirements from a higher level earlier on based on their own specific risk considerations.

The types of requirements in each level could be characterized as follows.

### Level 1

This level contains the minimum requirements to consider when securing an application and represents a critical starting point. This level contains around 20% of the ASVS requirements. The goal for this level is to have as few requirements as possible, to decrease the barrier to entry.

These requirements are generally critical or basic, first-layer of defense requirements for preventing common attacks that do not require other vulnerabilities or preconditions to be exploitable.

In addition to the first layer of defense requirements, some requirements have less of an impact at higher levels, such as requirements related to passwords. Those are more important for Level 1, as from higher levels, the multi-factor authentication requirements become relevant.

Level 1 is not necessarily penetration testable by an external tester without internal access to documentation or code (such as "black box" testing), although the lower number of requirements should make it easier to verify.

### Level 2

Most applications should be striving to achieve this level of security. Around 50% of the requirements in the ASVS are L2 meaning that an application needs to implement around 70% of the requirements in the ASVS (all of the L1 and L2 requirements) in order to comply with L2.

These requirements generally relate to either less common attacks or more complicated protections against common attacks. They may still be a first layer of defense, or they may require certain preconditions for the attack to be successful.

### Level 3

This level should be the goal for applications looking to demonstrate the highest levels of security and provides the final ~30% of requirements to comply with.

Requirements in this section are generally either defense-in-depth mechanisms or other useful but hard-to-implement controls.

### Which level to achieve

The priority-based levels are intended to provide a reflection of the application security maturity of the organization and the application. Rather than the ASVS prescriptively stating what level an application should be at, an organization should analyze its risks and decide what level it believes it should be at, depending on the sensitivity of the application and of course, the expectations of the application's users.

For example, an early-stage startup that is only collecting limited sensitive data may decide to focus on Level 1 for its initial security goals, but a bank may have difficulty justifying anything less than Level 3 to its customers for its online banking application.

## How to use the ASVS

### The structure of the ASVS

The ASVS is made up of a total of around 350 requirements which are divided into 17 chapters, each of which is further divided into sections.

The aim of the chapter and section division is to simplify choosing or filtering out chapters and sections based on the what is relevant for the application. For example, for a machine-to-machine API, the requirements in chapter V3 related to web frontends will not be relevant. If there is no use of OAuth or WebRTC, then those chapters can be ignored as well.

### Release strategy

ASVS releases follow the pattern "Major.Minor.Patch" and the numbers provide information on what has changed within the release. In a major release, the first number will change, in a minor release, the second number will change, and in a patch release, the third number will change.

* Major release - Full reorganization, almost everything may have changed, including requirement numbers. Reevaluation for compliance will be necessary (for example, 4.0.3 -> 5.0.0).
* Minor release - Requirements may be added or removed, but overall numbering will stay the same. Reevaluation for compliance will be necessary, but should be easier (for example, 5.0.0 -> 5.1.0).
* Patch release - Requirements may be removed (for example, if they are duplicates or outdated) or made less stringent, but an application that complied with the previous release will comply with the patch release as well (for example, 5.0.0 -> 5.0.1).

The above specifically relates to the requirements in the ASVS. Changes to surrounding text and other content such as the appendices will not be considered to be a breaking change.

### Flexibility with the ASVS

Several of the points described above, such as documentation requirements and the levels mechanism, provide the ability to use the ASVS in a more flexible and organization-specific way.

Additionally, organizations are strongly encouraged to create an organization- or domain-specific fork that adjusts requirements based on the specific characteristics and risk levels of their applications. However, it is important to maintain traceability so that passing requirement 4.1.1 means the same across all versions.

Ideally, each organization should create its own tailored ASVS, omitting irrelevant sections (e.g., GraphQL, WebSockets, SOAP, if unused). An organization-specific ASVS version or supplement is also a good place to provide organization-specific implementation guidance, detailing libraries or resources to use when complying with requirements.

### How to Reference ASVS Requirements

Each requirement has an identifier in the format `<chapter>.<section>.<requirement>`, where each element is a number. For example, `1.11.3`.

* The `<chapter>` value corresponds to the chapter from which the requirement comes; for example, all `1.#.#` requirements are from the 'Encoding and Sanitization' chapter.
* The `<section>` value corresponds to the section within that chapter where the requirement appears, for example: all `1.2.#` requirements are in the 'Injection Prevention' section of the 'Encoding and Sanitization' chapter.
* The `<requirement>` value identifies the specific requirement within the chapter and section, for example, `1.2.5` which as of version 5.0.0 of this standard is:

> Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding.

Since the identifiers may change between versions of the standard, it is preferable for other documents, reports, or tools to use the following format: `v<version>-<chapter>.<section>.<requirement>`, where: 'version' is the ASVS version tag. For example: `v5.0.0-1.2.5` would be understood to mean specifically the 5th requirement in the 'Injection Prevention' section of the 'Encoding and Sanitization' chapter from version 5.0.0. (This could be summarized as `v<version>-<requirement_identifier>`.)

Note: The `v` preceding the version number in the format should always be lowercase.

If identifiers are used without including the `v<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. As the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

ASVS requirement lists are made available in CSV, JSON, and other formats which may be useful for reference or programmatic use.

### Forking the ASVS

Organizations can benefit from adopting ASVS by choosing one of the three levels or by creating a domain-specific fork that adjusts requirements per application risk level. This type of fork is encouraged, provided that it maintains traceability so that passing requirement 4.1.1 means the same across all versions.

Ideally, each organization should create its own tailored ASVS, omitting irrelevant sections (e.g., GraphQL, Websockets, SOAP, if unused). Forking should start with ASVS Level 1 as a baseline, advancing to Levels 2 or 3 based on the application’s risk.

## Use cases for the ASVS

The ASVS can be used to assess the security of an application and this is explored in more depth in the next chapter. However, several other potential uses for the ASVS (or a forked version) have been identified.

### As Detailed Security Architecture Guidance

One of the more common uses for the Application Security Verification Standard is as a resource for security architects. There are limited resources available for how to build a secure application architecture, especially with modern applications. ASVS can be used to fill in those gaps by allowing security architects to choose better controls for common problems, such as data protection patterns and input validation strategies. The architecture and documentation requirements will be particularly useful for this.

### As a Specialized Secure Coding Reference

The ASVS can be used as a basis for preparing a secure coding reference during application development, helping developers to make sure that they keep security in mind when they build software. Whilst the ASVS can be the base, organizations should prepare their own specific guidance which is clear and unified and ideally be prepared based on guidance from security engineers or security architects. As an extension to this, organizations are encouraged wherever possible to prepare approved security mechanisms and libraries that can be referenced in the guidance and used by developers.

### As a Guide for Automated Unit and Integration Tests

The ASVS is designed to be highly testable. Some verifications will be technical where as other requirements (such as the architectural and documentation requirements) may require documentation or architecture review. By building unit and integration tests that test and fuzz for specific and relevant abuse cases related to the requirements that are verifiable by technical means, it should be easier to check that these controls are operating correctly on each build. For example, additional tests can be crafted for the test suite for a login controller, testing the username parameter for common default usernames, account enumeration, brute forcing, LDAP and SQL injection, and XSS. Similarly, a test on the password parameter should include common passwords, password length, null byte injection, removing the parameter, XSS, and more.

### For Secure Development Training

ASVS can also be used to define the characteristics of secure software. Many “secure coding” courses are simply ethical hacking courses with a light smear of coding tips. This may not necessarily help developers to write more secure code. Instead, secure development courses can use the ASVS with a strong focus on the positive mechanisms found in the ASVS, rather than the Top 10 negative things not to do. The ASVS structure also provides a logical structure for walking through the different topics when securing an application.

### As a Framework for Guiding the Procurement of Secure Software

The ASVS is a great framework to help with secure software procurement or procurement of custom development services. The buyer can simply set a requirement that the software they wish to procure must be developed at ASVS level X, and request that the seller proves that the software satisfies ASVS level X.

## Applying ASVS in Practice

Different threats have different motivations. Some industries have unique information and technology assets and domain-specific regulatory compliance requirements.

Organizations are strongly encouraged to look deeply at their unique risk characteristics based on the nature of their business, and based upon that risk and business requirements determine the appropriate ASVS level.
