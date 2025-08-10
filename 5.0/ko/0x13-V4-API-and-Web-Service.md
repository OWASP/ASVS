# V4 API 와 WEB 서비스

## 제어 목표

웹 브라우저나 다른 클리어언트에서 사용하기 위해서 API를 노출하는 애플리케이션 (일반적으로 JSON, XML, GraphQL 사용)에는 몇 가지 특별히 고려해야 할 사항이 적용된다. 이번 장에서는 관련 보안 설정과 적용해야할 매커니즘에 대해 다룬다.

다른 장에서 다루는 인증, 세션 관리, 입력값 검증과 관련된 문제들은 API에도 동일하게 적용되므로, 이 챕터의 내용을 전체 맥락에서 벗어나 개별적으로 테스트해서는 안 된다는 점에 유의해야 한다.

## V4.1 일반적인 웹 서비스 보안

이 섹션은 일반적인 웹 서비스 보안 고려사항과 기본적인 웹 서비스 보안 수칙에 대해서 다룬다.

| # | 설명 | 수준 |
| :---: | :--- | :---: |
| **4.1.1** | 메세지 본문이 포함된 모든 HTTP 응답에는 실제 내용과 일치하는 Content-Type 헤더 필드가 포함되어 있는지 검증한다. 이때 IANA 미디어 타입(text, /+xml, /xml 등)에 따라 안전한 문자 인코딩 (ex. UTF-8, ISO-8859-1)을 지정하는 charset 파라미터도 포함되어야 한다. | 1 |
| **4.1.2** | 사용자가 대면하는 엔드포인트(사람이 직접 웹 브라우저에 접속하는 경우)만 HTTP에서 HTTPS로 자동 리디렉션하고, 그 외에 서비스나 API 엔드포인트는 명백한 리디렉션을 구현하지 않았는지 검증한다. 이는 클라이언트가 실수로 암호화되지 않은 HTTP 요청을 보내고 있음에도, 요청이 자동으로 HTTPS로 리디렉션되어 민감한 데이터의 유출 사실을 발견하지 못하게 되는 상황을 방지하기 위함이다. | 2 |
| **4.1.3** | 로드 밸런서, 웹 프록시, 백엔드-프론트엔드 서비스 등 중간 계층에서 설정되며, 애플리케이션에서 사용하는 모든 HTTP 헤더 필드를 사용자가 재정의할 수 없는지 확인한다. 예를 들어 X-Real-IP, X-Frowarded-*, X-User-ID 등의 헤더가 포함될 수 있다. | 2 |
| **4.1.4** | 애플리케이션이나 API에서 명시적으로 지원하는 HTTP 메서드(프리플라이트 요청 시에 OPTIONS 포함)만 사용할 수 있으며, 사용되지 않는 메서드는 차단되어 있는지 확인한다. | 3 |
| **4.1.5** | 매우 민감하거나 여러 시스템을 거치는 요청이나 거래에 대한 전송 계층 보호에 더하여 메세지별 디지털 서명들을 사용함으로써 추가적인 보증을 제공하는지 확인한다. | 3 |

## V4.2 HTTP 메세지 구조 검증

이번 섹션은 지나치게 긴 HTTP 메세지를 통한 요청 smuggling, 응답 분할, 헤더 인젝션, 그리고 DOS와 같은 공격을 방지하기 위해 HTTP 메세지의 구조와 헤더 필드를 어떻게 검증해야 하는지를 설명한다.

이러한 요구 사항은 일반적인 HTTP 메세지 처리 및 생성과 관련이 있지만, 서로 다른 HTTP버전 간에 HTTP 메세지를 변환할 때 특히 중요하다.

| # | 설명 | 수준 |
| :---: | :--- | :---: |
| **4.2.1** | 모든 애플리케이션 구성 요소(로드 밸런서, 방화벽, 애플리케이션 서버 포함)가 HTTP 요청 smuggling을 예방하는 HTTP 버전의 적합한 메커니즘을 사용하는지에 대해, 수신되는 HTTP 메세지의 끝을 결정하는지 확인한다. HTTP/1.x에서 Transfer-encoding 헤더 필드가 있는 경우에 RFC 2616에 따라서 Content-Length 헤더는 무시해야 한다. HTTP/2 또는 HTTP/3를 사용할 때 Content-Length 헤더 필드가 있는 경우에 수신기는 DATA 프레임의 길이와 일치하는지 확인해야 한다. | 2 |
| **4.2.2** | HTTP 메세지를 생성할 때, 요청 smuggling 공격을 예방하기 위해서 HTTP 프로토콜의 프레이밍 방식에 의해 결정된 Content의 길이와 Content-Length 헤더 필드가 충돌하지 않는지 확인한다.  | 3 |
| **4.2.3** | 응답 분할 및 헤더 인젝션 공격을 예방하기 위해서 애플리케이션이 Transfer-encoding과 같은 connection-specific 헤더 필드를 가진 HTTP/2또는 HTTP/3 메세지를 전송하거나 수락하지 않는지 확인한다. | 3 |
| **4.2.4** | 헤더 인젝션 공격을 예방하기 위해서, 애플리케이션이 헤더 이름과 값에 CR(\r), LF(\n), CRLF(\r\n)과 같은 줄바꿈 문자가 포함되어 있지 않은 HTTP/2 및 HTTP/3 요청만 허용하는지 확인한다. | 3 |
| **4.2.5** | 애플리케이션(백엔드 또는 프론트엔드)이 요청을 빌드하고 전송하는 경우, 수신 구성 요소가 수학하기에는 너무 긴 URI(ex. API 호출) 또는 HTTP 요청 헤더 필드(ex. Authorization 또는 Cookie)를 생성하지 않도록 검증, 검열 또는 기타 메커니즘을 사용하는지 확인한다. 이로 인해서 지나치게 긴 요청(ex. 긴 쿠키 헤더 필드)을 보낼 때와 같이 서비스 거부가 발생하여 서버가 항상 오류 상태로 응답할 수 있다. | 3 |

## V4.3 GraphQL

GraphQL은 다양한 백엔드 서비스와 긴밀하게 연결되지 않은 데이터가 풍부한 클라이언트를 만드는 방법으로, 점점 일반화 되고 있다. 이 섹션에서는 GraphQL의 보안 고려 사항을 다룬다.

| # | 설명 | 수준 |
| :---: | :--- | :---: |
| **4.3.1** | 쿼리 허용 목록, 깊이 제한, 양 제한 또는 쿼리 비용 분석을 사용하여 값비싼 중첩 쿼리로 인해 GraphQL 또는 데이터 계층 표현식 거부(DOS)를 방지하는지 확인한다. | 2 |
| **4.3.2** | GraphQL API가 다른 사용자에 의해 사용되지 않는 한, 운영 환경에서 GraphQL 점검 쿼리들이 비비활성화되어 있는지 확인한다. | 2 |

## V4.4 WebSocket

WebSocket은 단일 TCP 연결을 통해 동시에 양방향 통신 채널을 제공하는 통신 프로토콜이다. 2011년에 IETF에 의해 RFC 6455로 표준화되었으며, HTTP 포트 443 및 80에서 동작하도록 설계되었음에도 불구하고 HTTP와는 다르다.

이 섹션에서는 실시간 통신 채널을 악용하는 통신 보안 및 세션 관리와 관련된 공격을 방지하기 위한 주요 보안 요구 사항을 제공한다.

| # | 설명 | 수준 |
| :---: | :--- | :---: |
| **4.4.1** | 모든 WebSocket 연결에 WebSocket over TLS(WSS)이 사용되는지 확인한다. | 1 |
| **4.4.2** | 초기 HTTP WebSocket Handshake 중에 기존 헤더 필드가 애플리케이션에 허용된 기존 목록과 대조되는지 확인한다. | 2 |
| **4.4.3** | 애플리케이션의 표준 세션 관리를 사용할 수 없는 경우, 관련 세션 관리 보안 요구 사항을 준수하는 전용 토큰이 사용되고 있는지 확인한다. | 2 |
| **4.4.4** | 기존 HTTPS 세션을 WebSocket 채널로 전환할 때 이전에 인증된 HTTPS 세션을 통해 전용 WebSocket 세션 관리 토큰을 처음 얻거나 검증하는지 확인한다. | 2 |

## 참고

더 많은 정보를 위해서는 아래의 링크를 확인하면 된다.

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* Resources on GraphQL Authorization from [graphql.org](https://graphql.org/learn/authorization/) and [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods).
* [OWASP Web Security Testing Guide: GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [OWASP Web Security Testing Guide: Testing WebSockets](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)

