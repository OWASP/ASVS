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
| **4.2.5** | 애플리케이션이 다른 서버로 API요청을 보낼 때, 요청 주소(URI)나 쿠키나 검증과 같은 HTTP 헤더 필드가 너무 길어져서 를 생성하는  | 3 |

## V4.3 GraphQL

GraphQL is becoming more common as a way of creating data-rich clients that are not tightly coupled to a variety of backend services. This section covers security considerations for GraphQL.

| # | Description | Level |
| :---: | :--- | :---: |
| **4.3.1** | Verify that a query allowlist, depth limiting, amount limiting, or query cost analysis is used to prevent GraphQL or data layer expression Denial of Service (DoS) as a result of expensive, nested queries. | 2 |
| **4.3.2** | Verify that GraphQL introspection queries are disabled in the production environment unless the GraphQL API is meant to be used by other parties. | 2 |

## V4.4 WebSocket

WebSocket is a communications protocol that provides a simultaneous two-way communication channel over a single TCP connection. It was standardized by the IETF as RFC 6455 in 2011 and is distinct from HTTP, even though it is designed to work over HTTP ports 443 and 80.

This section provides key security requirements to prevent attacks related to communication security and session management that specifically exploit this real-time communication channel.

| # | Description | Level |
| :---: | :--- | :---: |
| **4.4.1** | Verify that WebSocket over TLS (WSS) is used for all WebSocket connections. | 1 |
| **4.4.2** | Verify that, during the initial HTTP WebSocket handshake, the Origin header field is checked against a list of origins allowed for the application. | 2 |
| **4.4.3** | Verify that, if the application's standard session management cannot be used, dedicated tokens are being used for this, which comply with the relevant Session Management security requirements. | 2 |
| **4.4.4** | Verify that dedicated WebSocket session management tokens are initially obtained or validated through the previously authenticated HTTPS session when transitioning an existing HTTPS session to a WebSocket channel. | 2 |

## References

For more information, see also:

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* Resources on GraphQL Authorization from [graphql.org](https://graphql.org/learn/authorization/) and [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods).
* [OWASP Web Security Testing Guide: GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [OWASP Web Security Testing Guide: Testing WebSockets](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)

