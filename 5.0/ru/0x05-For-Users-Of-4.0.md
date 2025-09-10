# Изменения по сравнению с v4.x

## Введение

Пользователям, знакомым со стандартом версии 4.x, может быть полезно ознакомиться с ключевыми изменениями, внесёнными в версию 5.0, включая обновления в содержании, области применения и основополагающей философии.

Из 286 требований версии 4.0.3 только 11 остались без изменений, в то время как 15 претерпели незначительные грамматические правки, не повлиявшие на их смысл. В общей сложности 109 требований (38%) более не являются отдельными требованиями в версии 5.0 – 50 были просто удалены, 28 удалены как дубликаты и 31 объединено с другими требованиями. Остальные требования были так или иначе пересмотрены. Даже требования, не претерпевшие существенных изменений, имеют новые идентификаторы из-за переупорядочивания или реструктуризации.

Для облегчения перехода на версию 5.0 предоставляются документы сопоставления, которые помогают пользователям отследить, как требования из версии 4.x соотносятся с требованиями в версии 5.0. Эти сопоставления не привязаны к версиям выпусков и могут при необходимости обновляться или уточняться.

## Философия требований

### Целевая область применения

Версия 4.x включала требования, которые не соответствовали целевой области применения стандарта; они были удалены. Требования, которые не удовлетворяли критериям области применения для версии 5.0 или не поддавались верификации, также были исключены.

### Акцент на целях безопасности, а не на механизмах

В версии 4.x многие требования были сфокусированы на конкретных механизмах, а не на лежащих в их основе целях безопасности. В версии 5.0 требования сконцентрированы на целях безопасности, ссылаясь на конкретные механизмы только в тех случаях, когда они являются единственным практическим решением, или предоставляя их в качестве примеров или дополнительного руководства.

Такой подход признаёт, что для достижения заданной цели безопасности может существовать несколько методов, и позволяет избежать ненужной предписанности, которая могла бы ограничить гибкость организаций. 

Кроме того, требования, касающиеся одной и той же проблемы безопасности, были объединены там, где это было необходимо.

### Documented Security Decisions

While the concept of documented security decisions may appear new in version 5.0, it is an evolution of earlier requirements related to policy application and threat modeling in version 4.0. Previously, some requirements implicitly demanded analysis to inform the implementation of security controls, such as determining permitted network connections.

To ensure that necessary information is available for implementation and verification, these expectations are now explicitly defined as documentation requirements, making them clear, actionable, and verifiable.

## Structural Changes and New Chapters

Several chapters in version 5.0 introduce entirely new content:

* OAuth and OIDC – Given the widespread adoption of these protocols for access delegation and single sign-on, dedicated requirements have been added to address the diverse scenarios developers may encounter. This area may eventually evolve into a standalone standard, similar to the treatment of Mobile and IoT requirements in previous versions.
* WebRTC – As this technology gains popularity, its unique security considerations and challenges are now addressed in a dedicated section.

Efforts have also been made to ensure that chapters and sections are organized around coherent sets of related requirements.

This restructuring has led to the creation of additional chapters:

* Self-contained Tokens – Formerly grouped under session management, self-contained tokens are now recognized as a distinct mechanism and a foundational element for stateless communication (such as in OAuth and OIDC). Due to their unique security implications, they are addressed in a dedicated chapter, with some new requirements introduced in version 5.x.
* Web Frontend Security – With the increasing complexity of browser-based applications and the rise of API-only architectures, frontend security requirements have been separated into their own chapter.
* Secure Coding and Architecture – New requirements addressing general security practices that did not fit within existing chapters have been grouped here.

Other organizational changes in version 5.0 were made to clarify intent. For example, input validation requirements were moved alongside business logic, reflecting their role in enforcing business rules, rather than being grouped with sanitization and encoding.

The former V1 Architecture chapter has been removed. Its initial section contained requirements that were out of scope, while subsequent sections have been redistributed to relevant chapters, with requirements deduplicated and clarified as necessary.

## Removal of Direct Mappings to Other Standards

Direct mappings to other standards have been removed from the main body of the standard. The aim is to prepare a mapping with the OWASP Common Requirement Enumeration (CRE) project, which in turn will link ASVS to a range of OWASP projects and external standards.

Direct mappings to CWE and NIST are no longer maintained, as explained below.

### Reduced Coupling with NIST Digital Identity Guidelines

The NIST [Digital Identity Guidelines (SP 800-63)](https://pages.nist.gov/800-63-3/) have long served as a reference for authentication and authorization controls. In version 4.x, certain chapters were closely aligned with NIST's structure and terminology.

While these guidelines remain an important reference, strict alignment introduced challenges, including less widely recognized terminology, duplication of similar requirements, and incomplete mappings. Version 5.0 moves away from this approach to improve clarity and relevance.

### Moving Away from Common Weakness Enumeration (CWE)

The [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) provides a useful taxonomy of software security weaknesses. However, challenges such as category-only CWEs, difficulties in mapping requirements to a single CWE, and the presence of imprecise mappings in version 4.x have led to the decision to discontinue direct CWE mappings in version 5.0.

## Rethinking Level Definitions

Version 4.x described the levels as L1 ("Minimum"), L2 ("Standard"), and L3 ("Advanced"), with the implication that all applications handling sensitive data should meet at least L2.

Version 5.0 addresses several issues with this approach which are described in the following paragraphs.

As a practical matter, whereas version 4.x used tick marks for level indicators, 5.x uses a simple number on all formats of the standard including markdown, PDF, DOCX, CSV, JSON and XML. For backwards compatibility, legacy versions of the CSV, JSON and XML outputs which still use tick marks are also generated.

### Easier Entry Level

Feedback indicated that the large number of Level 1 requirements (~120), combined with its designation as the "minimum" level that is not good enough for most applications, discouraged adoption. Version 5.0 aims to lower this barrier by defining Level 1 primarily around first-layer defense requirements, resulting in clearer and fewer requirements at that level. To demonstrate this numerically, in v4.0.3 there were 128 L1 requirements out of a total of 278 requirements, representing 46%. In 5.0.0 there are 70 L1 requirements out of a total of 345 requirements, representing 20%.

### The Fallacy of Testability

A key factor in selecting controls for Level 1 in version 4.x was their suitability for assessment through "black box" external penetration testing. However, this approach was not fully aligned with the intent of Level 1 as the minimum set of security controls. Some users argued that Level 1 was insufficient for securing applications, while others found it too difficult to test.

Relying on testability as a criterion is both relative and, at times, misleading. The fact that a requirement is testable does not guarantee that it can be tested in an automated or straightforward manner. Moreover, the most easily testable requirements are not always those with the greatest security impact or the simplest to implement.

As such, in version 5.0, the level decisions were made primarily based on risk reduction and also keeping in mind the effort to implement.

### Not Just About Risk

The use of prescriptive, risk-based levels that mandate a specific level for certain applications has proven to be overly rigid. In practice, the prioritization and implementation of security controls depend on multiple factors, including both risk reduction and the effort required for implementation.

Therefore, organizations are encouraged to achieve the level that they feel like they should be achieving based on their maturity and the message they want to send to their users.
