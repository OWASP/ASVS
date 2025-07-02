# V1 인코딩과 데이터 정제

## 통제 목표

이번 장에서는 신뢰할 수 없는 데이터를 안전하지 않게 처리하여 발생하는 가장 흔한 웹 애플리케이션 보안 취약점들을 다룬다. 이러한 취약점들은 신뢰할 수 없는 데이터가 관련 인터프리터의 문법 규칙에 따라 해석되면서 다양한 기술적 취약점들로 이어질 수 있다.

현대의 웹 애플리케이션에서는 파라미터화된 쿼리, 자동 이스케이핑, 또는 템플릿 프레임워크와 같은 더 안전한 응용 프로그램 프로그래밍 인터페이스(Application Programming Interface; API)들을 쓰는 것이 항상 가장 좋다. 즉, 출력값 인코딩, 이스케이핑, 또는 데이터 정제를 신중하게 처리하는 것은 애플리케이션의 보안에 매우 중요하다.

입력값 검증은 예상치 못한 입력이나 위험한 콘텐츠로부터 보호하기 위한 심층 방어(Defense-in-Depth; DID) 메커니즘 역할을 한다. 다만, 입력값 검증의 주요 목적은 입력된 데이터가 기능 및 비즈니스 요구사항에 부합하는지를 확인하는 데 있으므로, 이에 관련된 요구사항은 "검증 및 비즈니스 로직" 장에서 다루고 있다.

## V1.1 인코딩 및 데이터 정제 아키텍처

아래의 섹션에서는 위험한 콘텐츠를 안전하게 처리하여 보안 취약점을 방지하기 위한 문법 또는 인터프리터별 요구사항들이 제시된다. 이 요구사항들은 처리가 이루어져야 할 순서와 위치에 대한 내용도 포함하고 있다. 또한 데이터가 저장될 때 인코딩 되거나 이스케이프 된 형태(예: HTML 인코딩)가 아닌 원래의 상태로 저장되도록 보장함으로써 이중 인코딩 문제를 방지하는 데 목적이 있다.

| # | 설명 | 레벨 |
| :---: | :--- | :---: |
| **1.1.1** | 입력값 검증은 오직 한 번만 표준 형태로 디코딩 되거나 언이스케이프 되어야 하며, 인코딩된 데이터가 예상될 때만 디코딩 되어야한다. 이 과정은 입력값이 추가로 처리되기 전에 완료되어야 한다. 예를 들어서 입력값 검증이나 데이터 정제 이후에는 수행되면 안 된다. | 2 |
| **1.1.2** | 애플리케이션이 출력값 인코딩 또는 이스케이핑을 인터프리터가 사용하기 전의 최종 단계로 수행하거나 인터프리터 자체에서 처리하는지 검증해야 한다. | 2 |

## V1.2 인젝션 방지

잠재적으로 위험 컨텍스트(context)에 인접하거나 가까운 위치에서 수행되는 출력값 인코딩이나 이스케이핑은 애플리케이션의 보안에 매우 중요하다. 일반적으로 출력값 인코딩과 이스케이핑은 저장되지 않으며, 대신 해당 출력값을 적절한 인터프리터에서 즉시 안전하게 렌더링하기 위해 사용된다. 이를 너무 이른 시점에 수행하려고 하면 콘텐츠가 잘못 구성되거나 인코딩 및 이스케이핑이 무효화될 수 있다.

많은 경우에서 소프트웨어 라이브러리에는 이를 자동으로 처리하는 안전한 함수들이 포함되어 있지만 현재 컨텍스트에 적합한지 확인이 필요하다.

| # | 설명 | 레벨 |
| :---: | :--- | :---: |
| **1.2.1** | HTTP 응답, HTML 문서 또는 XML 문서에 대한 출력 인코딩이 해당 컨텍스트에 적절한지 검증해야 한다. 예를 들어, 메시지나 문서 구조가 변경되지 않도록 HTML 요소, HTML 속성, HTML 주석, CSS, HTTP 헤더 필드 등에 맞는 문맥별 문자 인코딩이 수행되어야 한다. | 1 |
| **1.2.2** | 통합 자원 식별자(Uniform Resource Locator; URL)들을 동적으로 생성할 때 신뢰할 수 없는 데이터가 해당 컨텍스트에 맞게 인코딩되었는지 검증해야 한다(예: 쿼리나 경로 파라미터에 대한 URL 인코딩 또는 base64url 인코딩). 또한, 오직 안전한 URL 프로토콜만이 허용되는지 검증해야 한다(예: javascript: 또는 data:를 허용하지 않음). | 1 |
| **1.2.3** | 동적으로 자바스크립트 콘텐츠(JSON 포함)를 생성할 때 메시지나 문서 구조를 바꾸는 것을 방지하기 위해 출력값 인코딩이나 이스케이핑이 사용되고 있는지 검증해야 한다(자바스크립트 또는 JSON 인젝션을 피하기 위함). | 1 |
| **1.2.4** | 데이터 선택 혹은 데이터베이스 쿼리(예: SQL, HQL, NoSQL, Cypher)들 파라미터화된 쿼리, 객체 관계 매핑(Object Relational Mapping; ORM), 엔티티 프레임워크, 또는 다른 구조화된 쿼리 언어(Structured Query Language; SQL) 인젝션 및 기타 데이터베이스 인젝션 공격으로부터 보호해 주는 것들을 사용하는지 검증해야 한다. 이는 저장 프로시저를 쓸 때도 마찬가지이다. | 1 |
| **1.2.5** | 애플리케이션이 운영체제(Operating System; OS) 명령 인젝션으로부터 보호되며 운영체제 호출 시 파라미터화된 OS 쿼리나 상황에 맞는 명령줄 출력값 인코딩을 사용하는지 검증해야 한다. | 1 |
| **1.2.6** | 애플리케이션이 경량 디렉터리 접근 프로토콜(Lightweight Directory Access Protocol; LDAP) 인젝션 취약점에 대해 보호되어 있는지, 또는 LSAP 인젝션을 방지하기 위한 특정 보안 통제가 구현되어 있는지 검증해야 한다. | 2 |
| **1.2.7** | 애플리케이션이 XPath 인젝션 공격을 쿼리 파라미터나 미리 컴파일된 쿼리들을 사용해 보호되고 있는지 검증해야 한다.. | 2 |
| **1.2.8** | LaTeX 프로세서가 안전하게 구성되어 있으며("--shell-escape" 플래그 비사용 등) LaTex 인젝션 공격을 방지하기 위해 허용된 명령어 목록이 사용되고 있는지 검증해야 한다. | 2 |
| **1.2.9** | 애플리케이션이 정규 표현식에서 특수 문자들을 메타 문자로 잘못 해석하는 것을 방지하기 위해 해당 문자들 이스케이프(보통 백슬래시를 사용)하고 있는지 검증해야 한다. | 2 |
| **1.2.10** | 애플리케이션이 쉼표 구분 데이터(Comma Separated Values; CSV) 및 수식 인젝션에 대해 보호되어 있는지 검증해야 한다. 그리고 애플리케이션은 CSV 콘텐츠를 내보낼 때 RFC 4180 2.6과 2.7 부분에 명시된 이스케이핑 규칙을 반드시 따라야 한다. 또한 CSV나 다른 스프레드시트 포맷(XLS, XLSX, ODF 등)으로 내보낼 때 필드 값의 첫 번째가 특수 문자('=', '+', '-', '@', '\t' (탭), '\0' (null 문자) 포함)라면 반드시 작은따옴표로 이스케이프되어야 한다. | 3 |

참고: 파라미터화된 쿼리를 사용하거나 SQL을 이스케이핑만으로 항상 충분하지 않다. 테이블명과 컬럼명("ORDER BY" 컬럼 이름을 포함)과 같은 쿼리의 일부는 이스케이프 될 수 없다. 이러한 필드에 이스케이프된 사용자 입력 데이터를 포함하면 쿼리가 실패하거나 SQL 인젝션에 취약해질 수 있다.

## V1.3 Sanitization

The ideal protection against using untrusted content in an unsafe context is to use context-specific encoding or escaping, which maintains the same semantic meaning of the unsafe content but renders it safe for use in that particular context, as discussed in more detail in the previous section.

Where this is not possible, sanitization becomes necessary, removing potentially dangerous characters or content. In some cases, this may change the semantic meaning of the input, but for security reasons, there may be no alternative.

| # | Description | Level |
| :---: | :--- | :---: |
| **1.3.1** | Verify that all untrusted HTML input from WYSIWYG editors or similar is sanitized using a well-known and secure HTML sanitization library or framework feature. | 1 |
| **1.3.2** | Verify that the application avoids the use of eval() or other dynamic code execution features such as Spring Expression Language (SpEL). Where there is no alternative, any user input being included must be sanitized before being executed. | 1 |
| **1.3.3** | Verify that data being passed to a potentially dangerous context is sanitized beforehand to enforce safety measures, such as only allowing characters which are safe for this context and trimming input which is too long. | 2 |
| **1.3.4** | Verify that user-supplied Scalable Vector Graphics (SVG) scriptable content is validated or sanitized to contain only tags and attributes (such as draw graphics) that are safe for the application, e.g., do not contain scripts and foreignObject. | 2 |
| **1.3.5** | Verify that the application sanitizes or disables user-supplied scriptable or expression template language content, such as Markdown, CSS or XSL stylesheets, BBCode, or similar. | 2 |
| **1.3.6** | Verify that the application protects against Server-side Request Forgery (SSRF) attacks, by validating untrusted data against an allowlist of protocols, domains, paths and ports and sanitizing potentially dangerous characters before using the data to call another service. | 2 |
| **1.3.7** | Verify that the application protects against template injection attacks by not allowing templates to be built based on untrusted input. Where there is no alternative, any untrusted input being included dynamically during template creation must be sanitized or strictly validated. | 2 |
| **1.3.8** | Verify that the application appropriately sanitizes untrusted input before use in Java Naming and Directory Interface (JNDI) queries and that JNDI is configured securely to prevent JNDI injection attacks. | 2 |
| **1.3.9** | Verify that the application sanitizes content before it is sent to memcache to prevent injection attacks. | 2 |
| **1.3.10** | Verify that format strings which might resolve in an unexpected or malicious way when used are sanitized before being processed. | 2 |
| **1.3.11** | Verify that the application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection. | 2 |
| **1.3.12** | Verify that regular expressions are free from elements causing exponential backtracking, and ensure untrusted input is sanitized to mitigate ReDoS or Runaway Regex attacks. | 3 |

## V1.4 Memory, String, and Unmanaged Code

The following requirements address risks associated with unsafe memory use, which generally apply when the application uses a systems language or unmanaged code.

In some cases, it may be possible to achieve this by setting compiler flags that enable buffer overflow protections and warnings, including stack randomization and data execution prevention, and that break the build if unsafe pointer, memory, format string, integer, or string operations are found.

| # | Description | Level |
| :---: | :--- | :---: |
| **1.4.1** | Verify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows. | 2 |
| **1.4.2** | Verify that sign, range, and input validation techniques are used to prevent integer overflows. | 2 |
| **1.4.3** | Verify that dynamically allocated memory and resources are released, and that references or pointers to freed memory are removed or set to null to prevent dangling pointers and use-after-free vulnerabilities. | 2 |

## V1.5 Safe Deserialization

The conversion of data from a stored or transmitted representation into actual application objects (deserialization) has historically been the cause of various code injection vulnerabilities. It is important to perform this process carefully and safely to avoid these types of issues.

In particular, certain methods of deserialization have been identified by programming language or framework documentation as insecure and cannot be made safe with untrusted data. For each mechanism in use, careful due diligence should be performed.

| # | Description | Level |
| :---: | :--- | :---: |
| **1.5.1** | Verify that the application configures XML parsers to use a restrictive configuration and that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks. | 1 |
| **1.5.2** | Verify that deserialization of untrusted data enforces safe input handling, such as using an allowlist of object types or restricting client-defined object types, to prevent deserialization attacks. Deserialization mechanisms that are explicitly defined as insecure must not be used with untrusted input. | 2 |
| **1.5.3** | Verify that different parsers used in the application for the same data type (e.g., JSON parsers, XML parsers, URL parsers), perform parsing in a consistent way and use the same character encoding mechanism to avoid issues such as JSON Interoperability vulnerabilities or different URI or file parsing behavior being exploited in Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks. | 3 |

## References

For more information, see also:

* [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
* [OWASP Web Security Testing Guide: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [RFC4180 - Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180#section-2)

For more information, specifically on deserialization or parsing issues, please see:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai - A New Era of SSRF Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
