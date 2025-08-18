# V14 Data Protection
# V14 데이터 보호

## Control Objective
## 통제 목표

Applications cannot account for all usage patterns and user behaviors, and should therefore implement controls to limit unauthorized access to sensitive data on client devices.

애플리케이션은 모든 사용 패턴과 사용자 행동을 고려할수 없으므로, 클라이언트 기기의 민감한 데이터에 대한 비인가 엑세스를 제한하는 기능 구현이 권장된다.

This chapter includes requirements related to defining what data needs to be protected, how it should be protected, and specific mechanisms to implement or pitfalls to avoid.

이 장에서는 보호해야 하는 데이터, 보호해야 하는 방법, 구현해야 하는 구체적인 메커니즘 또는 피해야 할 실수들과 관련된 요구사항이 포함된다.

Another consideration for data protection is bulk extraction, modification, or excessive usage. Each system's requirements are likely to be very different, so determining what is "abnormal" must consider the threat model and business risk. From an ASVS perspective, detecting these issues is handled in the "Security Logging and Error Handling" chapter, and setting limits is handled in the "Validation and Business Logic" chapter.

데이터 보호에서 또 다른 고려 사항은 데이터 대량 추출, 무단 변경, 과도한 자원 사용이다. 각 시스템의 요구사항은 매우 다를 가능성이 높으므로, 무엇이 "비정상"인지 판단하려면 위협 모델과 비즈니스 리스크를 고려해야 한다. ASVS 관점에서 이러한 문제들을 탐지하는 것은 “보안 로그와 오류 처리” 장에서 다루며, 한도 설정은 “검증과 비즈니스 로직” 장에서 다룬다.

## V14.1 Data Protection Documentation
## V14.1 데이터 보호 문서화


A key prerequisite for being able to protect data is to categorize what data should be considered sensitive. There are likely to be several different levels of sensitivity, and for each level, the controls required to protect data at that level will be different.

데이터를 보호하기 위한 핵심 조건은 어떤 데이터를 민감한 데이터로 간주해야 하는지 분류하는 것이다. 민감도에는 몇가지 수준이 있을 수 있으며, 각 수준별로 데이터를 보호하기 위해 필요한 통제는 서로 다르다.

There are various privacy regulations and laws that affect how applications must approach the storage, use, and transmission of sensitive personal information. This section no longer tries to duplicate these types of data protection or privacy legislation, but rather focuses on key technical considerations for protecting sensitive data. Please consult local laws and regulations, and consult a qualified privacy specialist or lawyer as required.

애플리케이션이 민감한 개인정보를 저장, 사용, 전송의 접근 방식에 영향을 미치는 다양한 개인정보보호 규정 및 법률이 존재한다. 이 절에서는 이러한 유형의 테이터 보호 또는 개인정보보호 법률을 반복해서 다루지 않지만, 민감한 데이터를 보호하기 위한 핵심기술의 고려사항에 초점을 맞춘다. 현지 법률 및 규정을 확인하고, 필요에 따라 자격을 갖춘 개인정보보호 전문가나 변호사와 상의한다.

| # | Description | Level |
| # | 설명 | 수준 |
| :---: | :--- | :---: |
| **14.1.1** | Verify that all sensitive data created and processed by the application has been identified and classified into protection levels. This includes data that is only encoded and therefore easily decoded, such as Base64 strings or the plaintext payload inside a JWT. Protection levels need to take into account any data protection and privacy regulations and standards which the application is required to comply with. | 2 |
| **14.1.1** | 애플리케이션이 생성하고 처리하는 모든 민감한 데이터가 식별되고 보호 수준으로 분류되었는지 확인한다. 여기에는 단순히 인코딩되어 있고 쉽게 디코딩할 수 있는 데이터, 예를 들어 Base64 문자열이나 JWT 내부 평문 페이로드가 포함된다. 보호 수준은 애플리케이션이 준수해야 하는 모든 데이터 보호 및 개인정보 보호 관련 규정과 표준을 반드시 고려해야 한다. | 2 |
| **14.1.2** | Verify that all sensitive data protection levels have a documented set of protection requirements. This must include (but not be limited to) requirements related to general encryption, integrity verification, retention, how the data is to be logged, access controls around sensitive data in logs, database-level encryption, privacy and privacy-enhancing technologies to be used, and other confidentiality requirements. | 2 |
| **14.1.2** | 모든 민감한 데이터의 보호 수준에 대해 문서화된 요구사항이 있는지 확인한다. 반드시 여기에는(이에 한정되지 않지만) 일반적인 암호화, 무결성 검증, 보존 기간, 데이터 로그 기록 방식, 로그 내 민감한 데이터에 대한 접근 제어, 데이터베이스 암호화 수준, 사용할 개인정보 보호 및 개인정보 보호 강화 기술, 그리고 기타 기밀성 요구사항들 관련하여 포함되어야 한다. | 2 |

## V14.2 General Data Protection
## V14.2 일반 데이터 보호

This section contains various practical requirements related to the protection of data. Most are specific to particular issues such as unintended data leakage, but there is also a general requirement to implement protection controls based on the protection level required for each data item.

이 절에는 데이터 보호와 관련하여 다양하게 실제로 적용가능한 요구사항들이 포함되어 있다. 대부분은 의도하지 않은 데이터 유출과 같은 특정 문제를 다루지만, 각 데이터 항목에 요구되는 보호 수준에 따라 보호 통제를 구현해야 하는 일반적인 요구사항도 있다.

| # | Description | Level |
| # | 설명 | 수준 |
| :---: | :--- | :---: |
| **14.2.1** | Verify that sensitive data is only sent to the server in the HTTP message body or header fields, and that the URL and query string do not contain sensitive information, such as an API key or session token. | 1 |
| **14.2.1** | 민감한 데이터는 HTTP 메시지 본문이나 헤더 필드로만 서버에 전송되고, URL과 쿼리 문자열에는 API키나 세션토큰처럼 민감한 정보가 포함되지 않도록 검증한다. | 1 |
| **14.2.2** | Verify that the application prevents sensitive data from being cached in server components, such as load balancers and application caches, or ensures that the data is securely purged after use. | 2 |
| **14.2.2** | 서버 구성 요소에서 로드밸런서나 애플리케이션 캐시와 같은 민감한 데이터가 캐시되지 않게 하거나, 사용 후 해당 데이터를 안전하게 삭제하도록 검증한다. | 2 |
| **14.2.3** | Verify that defined sensitive data is not sent to untrusted parties (e.g., user trackers) to prevent unwanted collection of data outside of the application's control. | 2 |
| **14.2.3** | 정의된 민감한 데이터가 애플리케이션의 통제를 벗어난 곳에서 원치 않는 수집을 예방하기 위해 신뢰할 수 없는 대상(예: 사용자 추적기)에게 전송되지 않도록 검증한다. | 2 |
| **14.2.4** | Verify that controls around sensitive data related to encryption, integrity verification, retention, how the data is to be logged, access controls around sensitive data in logs, privacy and privacy-enhancing technologies, are implemented as defined in the documentation for the specific data's protection level. | 2 |
| **14.2.4** | 암호화, 무결성 검증, 보존, 데이터 로그 기록 방식, 로그 내 민감한 데이터 접근 제어, 개인정보 보호 및 개인정보 보호 강화 기술과 관련된 민감한 데이터 통제가, 해당 데이터 보호 수준에 대한 문서에 정의된 대로 구현되었는지 검증한다. | 2 |
| **14.2.5** | Verify that caching mechanisms are configured to only cache responses which have the expected content type for that resource and do not contain sensitive, dynamic content. The web server should return a 404 or 302 response when a non-existent file is accessed rather than returning a different, valid file. This should prevent Web Cache Deception attacks. | 3 |
| **14.2.5** | 캐싱 메커니즘이 해당 리소스에 대해 예상되는 콘텐츠 유형을 가진 응답만 캐시하고, 민감하거나 동적인 콘텐츠는 캐시하지 않도록 구성되어 있는지 검증한다. 존재하지 않는 파일에 접근했을 때 다른 유효한 파일을 반환하는 대신 웹 서버는 404 또는 302 응답을 반환해야 한다. 이는 Web Cache Deception  공격을 예방한다. | 3 |
| **14.2.6** | Verify that the application only returns the minimum required sensitive data for the application's functionality. For example, only returning some of the digits of a credit card number and not the full number. If the complete data is required, it should be masked in the user interface unless the user specifically views it. | 3 |
| **14.2.6** | 애플리케이션 기능에 필요한 최소한의 민감한 데이터만 반환을 검증한다. 예를 들어, 전체 신용카드 번호가 아닌 일부 숫자만 반환해야 한다. 만약 전체 데이터가 필요한 경우, 사용자가 구체적으로 조회하지 않는 한 사용자 인터페이스에서는 마스킹하는 것이 권장된다. | 3 |
| **14.2.7** | Verify that sensitive information is subject to data retention classification, ensuring that outdated or unnecessary data is deleted automatically, on a defined schedule, or as the situation requires. | 3 |
| **14.2.7** | 민감한 정보는 데이터 보존 분류 기준에 따라 관리되어야 하고, 오래되었거나 불필요한 데이터는 사전에 정의된 작업 또는 상황에 따라 자동으로 삭제되도록 검증한다. | 3 |
| **14.2.8** | Verify that sensitive information is removed from the metadata of user-submitted files unless storage is consented to by the user. | 3 |
| **14.2.8** | 사용자가 제출한 파일의 메타데이터에서 사용자가 저장에 동의하지 않는 한 민감한 정보는 제거를 검증한다. | 3 |

## V14.3 Client-side Data Protection
## V14.3 클라이언트 측 데이터 보호

This section contains requirements preventing data from leaking in specific ways at the client or user agent side of an application.

이 절에서는 클라이언트 또는 사용자 에이전트 측에서 애플리케이션의 데이터가 특정 방식으로 유출되는 것을 방지하기 위한 요구사항을 다룬다.

| # | Description | Level |
| # | 설명 | 수준 |
| :---: | :--- | :---: |
| **14.3.1** | Verify that authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated. The 'Clear-Site-Data' HTTP response header field may be able to help with this but the client-side should also be able to clear up if the server connection is not available when the session is terminated. | 1 |
| **14.3.1** | 클라이언트나 세션이 종료된 후에 브라우저 DOM과 같은 클라이언트 스토리지에서 인증된 데이터를 삭제를 검증한다. 이를 위해 ‘Clear-Site-Data’ HTTP 응답 헤더 필드를 사용할 수 있으나, 세션 종료 시 서버 연결이 불가능한 경우에도 클라이언트 측에서 해당 데이터를 삭제하는 것이 권장된다. | 1 |
| **14.3.2** | Verify that the application sets sufficient anti-caching HTTP response header fields (i.e., Cache-Control: no-store) so that sensitive data is not cached in browsers. | 2 |
| **14.3.2** | 애플리케이션이 브라우저에서 민감한 데이터가 캐시되지 않도록, (Cache-Control: no-store)충분한 캐시 방지 HTTP 응답 헤더 필드를 설정을 검증한다. | 2 |
| **14.3.3** | Verify that data stored in browser storage (such as localStorage, sessionStorage, IndexedDB, or cookies) does not contain sensitive data, with the exception of session tokens. | 2 |
| **14.3.3** | 브라우저 저장소(localStorage, sessionStorage, IndexedDB, 쿠키)에 저장되는 데이터에는 세션 토큰을 제외한 민감 데이터가 포함되지 않도록 검증한다. | 2 |

## References
## 참조

자세한 내용은 다음을 참조한다:

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
