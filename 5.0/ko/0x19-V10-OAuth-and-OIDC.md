# V10 OAuth와 OIDC

## 제어 목표

OAuth2(본 장에서는 OAuth로 지칭)는 위임된 인가를 위한 산업 표준 프레임워크이다. 예를 들어, OAuth를 사용하면 클라이언트 애플리케이션은 사용자가 클라이언트 애플리케이션에 권한을 부여한 경우 사용자를 대신하여 API(서버 리소스)에 접근할 수 있다.

OAuth 자체는 사용자 인증을 위해 설계되지 않았다. OpenID Connect(OIDC) 프레임워크는 OAuth 위에 사용자 ID 계층을 추가하여 OAuth를 확장한다. OIDC는 표준화된 사용자 정보, 싱글 사인온(SSO), 세션 관리 등의 기능을 지원한다. OIDC는 OAuth의 확장 기능이므로 본 장의 OAuth 요구사항은 OIDC에도 적용된다.

OAuth에 정의된 역할은 다음과 같다.

* OAuth 클라이언트는 서버 리소스에 접근하려는 애플리케이션이다(예: 발급된 액세스 토큰(Access Token)을 사용하여 API 호출). OAuth 클라이언트는 서버 측 애플리케이션인 경우가 많다.
    * 기밀 클라이언트는 인가 서버에 자체 인증하는 데 사용하는 자격 증명(Credentials)의 기밀성을 유지할 수 있는 클라이언트이다.
    * 공개 클라이언트는 인가 서버에 인증하기 위한 자격 증명의 기밀성을 유지할 수 없다. 따라서 자체 인증(예: 'client_id' 및 'client_secret' 파라미터 사용)하는 대신 자체 식별만 한다('client_id' 파라미터 사용).
* OAuth 리소스 서버는 OAuth 클라이언트에 리소스를 노출하는 서버 API이다.
* OAuth 인가 서버는 OAuth 클라이언트에 액세스 토큰을 발급하는 서버 애플리케이션이다. 이 액세스 토큰을 통해 OAuth 클라이언트는 최종 사용자를 대신하여 또는 OAuth 클라이언트 자체를 대신하여 리소스 서버의 리소스에 접근할 수 있다. 인가 서버는 종종 별도의 애플리케이션이지만, (적절한 경우) 적합한 리소스 서버에 통합될 수 있다.
* 리소스 소유자는 리소스 서버에 호스팅된 리소스에 대해 제한된 접근 권한을 획득하도록 OAuth 클라이언트에 권한을 부여하는 최종 사용자이다. 리소스 소유자는 인가 서버와 상호 작용함으로써 이 위임된 인가에 동의한다.

OIDC에 정의된 역할은 다음과 같다.

* 신뢰 당사자(Replying Party)는 OpenID 공급자를 통해 최종 사용자 인증을 요청하는 클라이언트 애플리케이션이다. 이는 OAuth 클라이언트의 역할을 수행한다.
* OpenID 공급자는 최종 사용자를 인증하고 신뢰 당사자에 OIDC 클레임(claims)을 제공할 수 있는 OAuth 인가 서버이다. OpenID 공급자는 ID 공급자(IdP)일 수 있지만, 연합 인증 시나리오
(federated scenarios)에서는 OpenID 공급자와 ID 공급자(최종 사용자가 인증하는 곳)가 다른 서버 애플리케이션일 수 있다.

OAuth와 OIDC는 원래 외부(third-party) 애플리케이션을 위해 설계되었으며, 오늘날에는 내부(first-party) 애플리케이션에서도 종종 사용된다. 그러나 인증 및 세션 관리와 같은 내부 시나리오에서 사용될 때, 프로토콜이 복잡성을 더하게 되며, 이로 인해 새로운 보안 과제가 발생할 수 있습니다.

OAuth와 OIDC는 다양한 유형의 애플리케이션에 사용될 수 있지만, 이 장에서는 ASVS와 요구사항은 웹 애플리케이션과 API에 중점을 둔다.

OAuth와 OIDC는 웹 기술 위에 구축된 논리 계층으로 간주될 수 있으므로, 본 장의 내용만을 따로 떼어내서 해석하지 않고, 다른 장의 일반 요구사항과 함께 통합적으로 적용해야 한다.

본 장은 https://oauth.net/2/ 및 https://openid.net/developers/specs/ 에서 찾을 수 있는 사양에 맞춰 OAuth2 및 OIDC에 대한 현재의 모범 사례를 다룬다. RFC가 성숙하다고 간주되더라도 자주 업데이트된다. 따라서 본 장의 요구사항을 적용할 때 최신 버전과 일치시키는 것이 중요하다. 자세한 내용은 참조 섹션을 참조한다.

이 영역의 복잡성을 고려할 때, 안전한 OAuth 또는 OIDC 솔루션을 위해서는 잘 알려진 산업 표준의 인가 서버를 사용하고, 권장되는 보안 구성을 적용하는 것이 매우 중요하다.

본 장에서 사용되는 용어는 OAuth RFC 및 OIDC 사양과 일치하지만, OIDC 용어는 OIDC에 특화된 요구사항에만 사용되며, 그 외에는 OAuth 용어가 사용된다는 점에 유의해야 한다.

OAuth 및 OIDC의 맥락에서, 본 장의 "토큰(Token)"이라는 용어는 다음을 의미한다.

* 액세스 토큰(Access Tokens)은 리소스 서버에서만 사용되어야 하며, 조회(introspection)를 통해 검증되는 참조 토큰이거나 특정 키 정보를 사용하여 검증되는 자체 포함 토큰일 수 있다.
* 리프레시 토큰(Refresh Tokens)은 토큰을 발급한 인가 서버에서만 사용되어야 한다.
* OIDC ID 토큰은 인가 흐름을 트리거한 클라이언트에서만 사용되어야 한다.

본 장의 일부 요구사항에 대한 위험 수준은 클라이언트가 기밀 클라이언트인지 또는 공개 클라이언트로 간주되는지에 따라 달라진다. 강력한 클라이언트 인증을 사용하면 많은 공격 벡터가 완화되므로, L1 애플리케이션에서 기밀 클라이언트를 사용할 때 일부 요구사항은 완화될 수 있다.

## V10.1 일반 OAuth 및 OIDC 보안

이 섹션은 OAuth 또는 OIDC를 사용하는 모든 애플리케이션에 적용되는 일반적인 아키텍처 요구사항을 다룬다.

| # | Description | Level |
| :---: | :--- | :---: |
| **10.1.1** | 엄격하게 필요한 구성 요소에만 토큰이 전송되는지 검증해야 한다. 예를 들어, 브라우저 기반 JavaScript 애플리케이션에 프론트엔드 전용 백엔드(Backend For Frontend; BFF)로 작동) 패턴을 사용하는 경우, 접근 및 리프레시 토큰은 백엔드에서만 접근 가능해야 한다. | 2 |
| **10.1.2** | 클라이언트는 인가 서버에서 제공하는 값(예: 인가 코드 또는 ID토큰)이 동일한 사용자 에이전트 세션 및 트랜잭션에서 시작된 인가 흐름의 결과인 경우에만 허용하는지 검증해야 한다. 이를 위해 클라이언트가 생성하는 비밀 값들(PKCE의 code_verifier, state, OIDC의 nonce 등)은 추측이 불가능해야 하며, 해당 트랜잭션에 고유해야 하고, 트랜잭션이 시작된 클라이언트와 사용자 에이전트 세션 양쪽에 안전하게 바인딩되어 있어야 한다. | 2 |

## V10.2 OAuth 클라이언트

이 요구사항은 OAuth 클라이언트 애플리케이션의 책임을 상세히 설명한다. 클라이언트는 예를 들어 웹 서버 백엔드(일반적으로 BFF로 작동), 백엔드 서비스 통합, 또는 프론트엔드 싱글 페이지 애플리케이션(일명 브라우저 기반 애플리케이션)일 수 있다.

일반적으로 백엔드 클라이언트는 기밀 클라이언트로 간주되고, 프론트엔드 클라이언트는 공개 클라이언트로 간주된다. 그러나 최종 사용자 장치에서 실행되는 네이티브 애플리케이션은 OAuth 동적 클라이언트 등록을 사용하는 경우 기밀로 간주될 수 있다.

| # | Description | Level |
| :---: | :--- | :---: |
| **10.2.1** | 코드 플로우를 사용하는 경우, OAuth 클라이언트는 토큰 요청을 유도하는 사이트간 요청 위조 공격(Cross-Site Request Forgery; CSRF)에 대한 보호 기능을 갖추고 있는지 검증한다. 이를 위해 인가 요청 시 전송된 state 파라미터를 검증하거나, PKCE(Proof Key for Code Exchange) 기능을 사용해야 한다. | 2 |
| **10.2.2** | OAuth 클라이언트가 둘 이상의 인가 서버와 상호 작용할 수 있는 경우, 믹스업 공격에 대한 방어 기능을 갖는지 검증해야 한다. 예를 들어, 인가 서버가 'iss' 파라미터 값을 반환하도록 요구하고 인가 응답 및 토큰 응답에서 이를 검증할 수 있다. | 2 |
| **10.2.3** | OAuth 클라이언트가 인가 서버에 대한 요청에서 필요한 범위(또는 기타 인가 파라미터)만 요청하는지 검증해야 한다. | 3 |

## V10.3 OAuth 리소스 서버

ASVS 및 본 장의 맥락에서 리소스 서버는 API이다. 안전한 접근을 제공하기 위해 리소스 서버는 다음을 수행해야 한다.

* 토큰 형식 및 관련 프로토콜 사양(예: JWT 검증 또는 OAuth 토큰 조회)에 따라 액세스 토큰을 검증해야 한다.
* 토큰이 유효한 경우, 액세스 토큰의 정보 및 부여된 권한을 기반으로 인가 결정을 강제해야 한다. 예를 들어, 리소스 서버는 클라이언트(리소스 소유자를 대신하여 작동)가 요청된 리소스에 접근할 권한이 있는지 검증해야 한다.

따라서 여기에 나열된 요구사항은 OAuth 또는 OIDC에 특화되어 있으며, 토큰 검증 후 토큰의 정보를 기반으로 인가를 수행하기 전에 이행되어야 한다.

| # | Description | Level |
| :---: | :--- | :---: |
| **10.3.1** | 리소스 서버가 해당 서비스(audience)에 사용하도록 의도된 액세스 토큰만 수락하는지 검증해야 한다. 대상은 구조화된 액세스 토큰(예: JWT의 'aud' 클레임)에 포함될 수 있거나, 토큰 조회 엔드포인트를 사용하여 확인할 수 있다. | 2 |
| **10.3.2** | 리소스 서버가 위임된 인가를 정의하는 액세스 토큰의 클레임을 기반으로 인가 결정을 시행하는지 검증해야 한다. 'sub', 'scope', 'authorization_details'와 같은 클레임이 존재하는 경우, 이는 결정의 일부여야 한다. | 2 |
| **10.3.3** | 액세스 토큰(JWT 또는 관련 토큰 조회 응답)에서 고유한 사용자를 식별해야 하는 접근 제어 결정이 필요한 경우, 리소스 서버가 다른 사용자에게 재할당될 수 없는 클레임에서 사용자를 식별하는지 검증해야 한다. 일반적으로 이는 'iss' 및 'sub' 클레임의 조합을 사용하는 것을 의미한다. | 2 |
| **10.3.4** | 리소스 서버가 특정 인증 강도, 방법 또는 최신성을 요구하는 경우, 제시된 액세스 토큰이 이러한 제약 조건을 충족하는지 검증해야 한다. 예를 들어, 토큰을 제시한 경우 OIDC의 'acr', 'amr' 및 'auth_time' 클레임을 각각 사용해야 한다. | 2 |
| **10.3.5** | 리소스 서버가 발신자 제약 액세스 토큰, 즉 OAuth 2용 상호 TLS(Mutual TLS) 또는 OAuth 2 DPoP(Demonstration of Proof of Possession)를 요구하여 도난된 액세스 토큰 사용 또는 액세스 토큰 재사용(권한 없는 당사자로부터)을 방지하는지 검증해야 한다. | 3 |

## V10.4 OAuth Authorization Server
## V10.4 OAuth 권한 부여 서버

These requirements detail the responsibilities for OAuth authorization servers, including OpenID Providers.
이러한 요구 사항은 OpenID 공급자를 포함한 OAuth 권한 부여 서버의 책임을 상세히 설명한다.

For client authentication, the 'self_signed_tls_client_auth' method is allowed with the prerequisites required by [section 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) of [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705).
클라이언트 인증의 경우, 'self_signed_tls_client_auth' 메소드는 [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705)의 [섹션 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut)에서 요구하는 선행 조건과 함께 허용된다.

| # | Description | Level |
| :---: | :--- | :---: |
| **10.4.1** | Verify that the authorization server validates redirect URIs based on a client-specific allowlist of pre-registered URIs using exact string comparison. | 1 |
| **10.4.1** | 권한 부여 서버가 사전 등록된 URI의 클라이언트별 허용 목록을 기반으로 정확한 문자열 비교를 사용하여 리디렉션 URI를 검증하는지 검증해야 한다. | 1 |
| **10.4.2** | Verify that, if the authorization server returns the authorization code in the authorization response, it can be used only once for a token request. For the second valid request with an authorization code that has already been used to issue an access token, the authorization server must reject a token request and revoke any issued tokens related to the authorization code. | 1 |
| **10.4.2** | 권한 부여 서버가 권한 부여 응답에서 권한 부여 코드를 반환하는 경우, 토큰 요청에 한 번만 사용할 수 있는지 검증해야 한다. 이미 접근 토큰을 발급하는 데 사용된 권한 부여 코드를 사용하여 두 번째 유효한 요청이 발생하면, 권한 부여 서버는 토큰 요청을 거부하고 해당 권한 부여 코드와 관련된 모든 발급된 토큰을 취소해야 한다. | 1 |
| **10.4.3** | Verify that the authorization code is short-lived. The maximum lifetime can be up to 10 minutes for L1 and L2 applications and up to 1 minute for L3 applications. | 1 |
| **10.4.3** | 권한 부여 코드가 단명하는지 검증해야 한다. 최대 수명은 L1 및 L2 애플리케이션의 경우 최대 10분, L3 애플리케이션의 경우 최대 1분일 수 있다. | 1 |
| **10.4.4** | Verify that for a given client, the authorization server only allows the usage of grants that this client needs to use. Note that the grants 'token' (Implicit flow) and 'password' (Resource Owner Password Credentials flow) must no longer be used. | 1 |
| **10.4.4** | 주어진 클라이언트에 대해 권한 부여 서버가 해당 클라이언트가 사용해야 하는 권한 부여(grant)만 허용하는지 검증해야 한다. 'token'(암시적 플로우) 및 'password'(리소스 소유자 비밀번호 자격 증명 플로우)는 더 이상 사용되어서는 안 된다. | 1 |
| **10.4.5** | Verify that the authorization server mitigates refresh token replay attacks for public clients, preferably using sender-constrained refresh tokens, i.e., Demonstrating Proof of Possession (DPoP) or Certificate-Bound Access Tokens using mutual TLS (mTLS). For L1 and L2 applications, refresh token rotation may be used. If refresh token rotation is used, the authorization server must invalidate the refresh token after usage, and revoke all refresh tokens for that authorization if an already used and invalidated refresh token is provided. | 1 |
| **10.4.5** | 권한 부여 서버가 공개 클라이언트에 대한 갱신 토큰 재사용 공격을 완화하는지 검증해야 하며, 가급적이면 발신자 제약 갱신 토큰(sender-constrained refresh tokens), 즉 DPoP(Demonstrating Proof of Possession) 또는 mTLS(Mutual TLS)를 사용한 인증서 바인딩 접근 토큰을 사용해야 한다. L1 및 L2 애플리케이션의 경우 갱신 토큰 순환(rotation)이 사용될 수 있다. 갱신 토큰 순환이 사용되는 경우, 권한 부여 서버는 사용 후 갱신 토큰을 무효화해야 하며, 이미 사용되고 무효화된 갱신 토큰이 제공되면 해당 권한 부여에 대한 모든 갱신 토큰을 취소해야 한다. | 1 |
| **10.4.6** | Verify that, if the code grant is used, the authorization server mitigates authorization code interception attacks by requiring proof key for code exchange (PKCE). For authorization requests, the authorization server must require a valid 'code_challenge' value and must not accept a 'code_challenge_method' value of 'plain'. For a token request, it must require validation of the 'code_verifier' parameter. | 2 |
| **10.4.6** | 코드 권한 부여(code grant)가 사용되는 경우, 권한 부여 서버가 PKCE(Proof Key for Code Exchange)를 요구하여 권한 부여 코드 가로채기 공격을 완화하는지 검증해야 한다. 권한 부여 요청의 경우, 권한 부여 서버는 유효한 'code_challenge' 값을 요구해야 하며, 'plain' 값을 가진 'code_challenge_method'는 수락해서는 안 된다. 토큰 요청의 경우, 'code_verifier' 매개변수의 검증을 요구해야 한다. | 2 |
| **10.4.7** | Verify that if the authorization server supports unauthenticated dynamic client registration, it mitigates the risk of malicious client applications. It must validate client metadata such as any registered URIs, ensure the user's consent, and warn the user before processing an authorization request with an untrusted client application. | 2 |
| **10.4.7** | 권한 부여 서버가 인증되지 않은 동적 클라이언트 등록을 지원하는 경우, 악의적인 클라이언트 애플리케이션의 위험을 완화하는지 검증해야 한다. 등록된 URI와 같은 클라이언트 메타데이터를 검증하고, 사용자의 동의를 확인하며, 신뢰할 수 없는 클라이언트 애플리케이션으로 권한 부여 요청을 처리하기 전에 사용자에게 경고해야 한다. | 2 |
| **10.4.8** | Verify that refresh tokens have an absolute expiration, including if sliding refresh token expiration is applied. | 2 |
| **10.4.8** | 갱신 토큰이 슬라이딩 갱신 토큰 만료가 적용되더라도 절대적인 만료 기한을 갖는지 검증해야 한다. | 2 |
| **10.4.9** | Verify that refresh tokens and reference access tokens can be revoked by an authorized user using the authorization server user interface, to mitigate the risk of malicious clients or stolen tokens. | 2 |
| **10.4.9** | 악의적인 클라이언트 또는 도난된 토큰의 위험을 완화하기 위해 권한 부여 서버 사용자 인터페이스를 통해 권한 있는 사용자가 갱신 토큰 및 참조 접근 토큰을 취소할 수 있는지 검증해야 한다. | 2 |
| **10.4.10** | Verify that confidential client is authenticated for client-to-authorized server backchannel requests such as token requests, pushed authorization requests (PAR), and token revocation requests. | 2 |
| **10.4.10** | 토큰 요청, 푸시된 권한 부여 요청(PAR), 토큰 취소 요청과 같은 클라이언트-권한 부여 서버 백채널 요청에 대해 기밀 클라이언트가 인증되는지 검증해야 한다. | 2 |
| **10.4.11** | Verify that the authorization server configuration only assigns the required scopes to the OAuth client. | 2 |
| **10.4.11** | 권한 부여 서버 구성이 OAuth 클라이언트에 필요한 범위만 할당하는지 검증해야 한다. | 2 |
| **10.4.12** | Verify that for a given client, the authorization server only allows the 'response_mode' value that this client needs to use. For example, by having the authorization server validate this value against the expected values or by using pushed authorization request (PAR) or JWT-secured Authorization Request (JAR). | 3 |
| **10.4.12** | 주어진 클라이언트에 대해 권한 부여 서버가 해당 클라이언트가 사용해야 하는 'response_mode' 값만 허용하는지 검증해야 한다. 예를 들어, 권한 부여 서버가 이 값을 예상 값과 비교하여 검증하거나, PAR(Pushed Authorization Request) 또는 JAR(JWT-secured Authorization Request)을 사용하여 검증해야 한다. | 3 |
| **10.4.13** | Verify that grant type 'code' is always used together with pushed authorization requests (PAR). | 3 |
| **10.4.13** | 권한 부여 유형 'code'가 항상 PAR(Pushed Authorization Requests)과 함께 사용되는지 검증해야 한다. | 3 |
| **10.4.14** | Verify that the authorization server issues only sender-constrained (Proof-of-Possession) access tokens, either with certificate-bound access tokens using mutual TLS (mTLS) or DPoP-bound access tokens (Demonstration of Proof of Possession). | 3 |
| **10.4.14** | 권한 부여 서버가 mTLS(Mutual TLS)를 사용하는 인증서 바인딩 접근 토큰 또는 DPoP(Demonstrating Proof of Possession) 바인딩 접근 토큰을 사용하여 발신자 제약(Proof-of-Possession) 접근 토큰만 발급하는지 검증해야 한다. | 3 |
| **10.4.15** | Verify that, for a server-side client (which is not executed on the end-user device), the authorization server ensures that the 'authorization_details' parameter value is from the client backend and that the user has not tampered with it. For example, by requiring the usage of pushed authorization request (PAR) or JWT-secured Authorization Request (JAR). | 3 |
| **10.4.15** | 서버 측 클라이언트(최종 사용자 장치에서 실행되지 않는)의 경우, 권한 부여 서버가 'authorization_details' 매개변수 값이 클라이언트 백엔드에서 온 것이며 사용자가 이를 조작하지 않았는지 확인하는지 검증해야 한다. 예를 들어, PAR(Pushed Authorization Request) 또는 JAR(JWT-secured Authorization Request)의 사용을 요구하여 확인해야 한다. | 3 |
| **10.4.16** | Verify that the client is confidential and the authorization server requires the use of strong client authentication methods (based on public-key cryptography and resistant to replay attacks), such as mutual TLS ('tls_client_auth', 'self_signed_tls_client_auth') or private key JWT ('private_key_jwt'). | 3 |
| **10.4.16** | 클라이언트가 기밀이며 권한 부여 서버가 상호 TLS('tls_client_auth', 'self_signed_tls_client_auth') 또는 개인 키 JWT('private_key_jwt')와 같이 공개 키 암호화를 기반으로 하며 재사용 공격에 강한 강력한 클라이언트 인증 방법을 요구하는지 검증해야 한다. | 3 |

## V10.5 OIDC Client
## V10.5 OIDC 클라이언트

As the OIDC relying party acts as an OAuth client, the requirements from the section "OAuth Client" apply as well.
OIDC 의존 당사자가 OAuth 클라이언트로 작동하므로, "OAuth 클라이언트" 섹션의 요구 사항도 적용된다.

Note that the "Authentication with an Identity Provider" section in the "Authentication" chapter also contains relevant general requirements.
"인증" 장의 "ID 공급자를 사용한 인증" 섹션에도 관련 일반 요구 사항이 포함되어 있음에 유의해야 한다.

| # | Description | Level |
| :---: | :--- | :---: |
| **10.5.1** | Verify that the client (as the relying party) mitigates ID Token replay attacks. For example, by ensuring that the 'nonce' claim in the ID Token matches the 'nonce' value sent in the authentication request to the OpenID Provider (in OAuth2 refereed to as the authorization request sent to the authorization server). | 2 |
| **10.5.1** | 클라이언트(의존 당사자로서)가 ID 토큰 재사용 공격을 완화하는지 검증해야 한다. 예를 들어, ID 토큰의 'nonce' 클레임이 OpenID 공급자에 전송된 인증 요청(OAuth2에서는 권한 부여 서버에 전송된 권한 부여 요청으로 지칭)에서 전송된 'nonce' 값과 일치하는지 확인해야 한다. | 2 |
| **10.5.2** | Verify that the client uniquely identifies the user from ID Token claims, usually the 'sub' claim, which cannot be reassigned to other users (for the scope of an identity provider). | 2 |
| **10.5.2** | 클라이언트가 ID 토큰 클레임, 일반적으로 'sub' 클레임에서 사용자를 고유하게 식별하며, 해당 클레임이 다른 사용자에게 재할당될 수 없는지(ID 공급자 범위 내에서) 검증해야 한다. | 2 |
| **10.5.3** | Verify that the client rejects attempts by a malicious authorization server to impersonate another authorization server through authorization server metadata. The client must reject authorization server metadata if the issuer URL in the authorization server metadata does not exactly match the pre-configured issuer URL expected by the client. | 2 |
| **10.5.3** | 클라이언트가 권한 부여 서버 메타데이터를 통해 다른 권한 부여 서버를 가장하려는 악의적인 권한 부여 서버의 시도를 거부하는지 검증해야 한다. 클라이언트는 권한 부여 서버 메타데이터의 발급자 URL이 클라이언트가 예상하는 사전 구성된 발급자 URL과 정확히 일치하지 않으면 권한 부여 서버 메타데이터를 거부해야 한다. | 2 |
| **10.5.4** | Verify that the client validates that the ID Token is intended to be used for that client (audience) by checking that the 'aud' claim from the token is equal to the 'client_id' value for the client. | 2 |
| **10.5.4** | 클라이언트가 토큰의 'aud' 클레임이 클라이언트의 'client_id' 값과 동일한지 확인하여 ID 토큰이 해당 클라이언트(대상)에 사용될 목적으로 의도되었음을 검증하는지 검증해야 한다. | 2 |
| **10.5.5** | Verify that, when using OIDC back-channel logout, the relying party mitigates denial of service through forced logout and cross-JWT confusion in the logout flow. The client must verify that the logout token is correctly typed with a value of 'logout+jwt', contains the 'event' claim with the correct member name, and does not contain a 'nonce' claim. Note that it is also recommended to have a short expiration (e.g., 2 minutes). | 2 |
| **10.5.5** | OIDC 백채널 로그아웃을 사용하는 경우, 의존 당사자가 강제 로그아웃 및 로그아웃 흐름에서의 교차 JWT 혼동으로 인한 서비스 거부를 완화하는지 검증해야 한다. 클라이언트는 로그아웃 토큰이 'logout+jwt' 값으로 올바르게 유형화되었는지, 올바른 멤버 이름의 'event' 클레임을 포함하는지, 그리고 'nonce' 클레임을 포함하지 않는지 검증해야 한다. 또한, 짧은 만료 시간(예: 2분)을 갖는 것이 권장된다. | 2 |

## V10.6 OpenID Provider
## V10.6 OpenID 공급자

As OpenID Providers act as OAuth authorization servers, the requirements from the section "OAuth Authorization Server" apply as well.
OpenID 공급자는 OAuth 권한 부여 서버로 작동하므로, "OAuth 권한 부여 서버" 섹션의 요구 사항도 적용된다.

Note that if using the ID Token flow (not the code flow), no access tokens are issued, and many of the requirements for OAuth AS are not applicable.
ID 토큰 흐름(코드 흐름이 아닌)을 사용하는 경우, 접근 토큰이 발급되지 않으며 OAuth AS의 많은 요구 사항이 적용되지 않음에 유의해야 한다.

| # | Description | Level |
| :---: | :--- | :---: |
| **10.6.1** | Verify that the OpenID Provider only allows values 'code', 'ciba', 'id_token', or 'id_token code' for response mode. Note that 'code' is preferred over 'id_token code' (the OIDC Hybrid flow), and 'token' (any Implicit flow) must not be used. | 2 |
| **10.6.1** | OpenID 공급자가 'code', 'ciba', 'id_token' 또는 'id_token code' 값만 응답 모드로 허용하는지 검증해야 한다. 'code'가 'id_token code'(OIDC 하이브리드 흐름)보다 선호되며, 'token'(모든 암시적 흐름)은 사용되어서는 안 된다. | 2 |
| **10.6.2** | Verify that the OpenID Provider mitigates denial of service through forced logout. By obtaining explicit confirmation from the end-user or, if present, validating parameters in the logout request (initiated by the relying party), such as the 'id_token_hint'. | 2 |
| **10.6.2** | OpenID 공급자가 강제 로그아웃으로 인한 서비스 거부를 완화하는지 검증해야 한다. 최종 사용자로부터 명시적인 확인을 받거나, 존재하는 경우 로그아웃 요청(의존 당사자가 시작한)의 'id_token_hint'와 같은 매개변수를 검증하여 완화해야 한다. | 2 |

## V10.7 Consent Management
## V10.7 동의 관리

These requirements cover the verification of the user's consent by the authorization server. Without proper user consent verification, a malicious actor may obtain permissions on the user's behalf through spoofing or social-engineering.
이러한 요구 사항은 권한 부여 서버에 의한 사용자 동의 검증을 다룬다. 적절한 사용자 동의 검증이 없으면 악의적인 행위자가 스푸핑 또는 사회 공학을 통해 사용자를 대신하여 권한을 획득할 수 있다.

| # | Description | Level |
| :---: | :--- | :---: |
| **10.7.1** | Verify that the authorization server ensures that the user consents to each authorization request. If the identity of the client cannot be assured, the authorization server must always explicitly prompt the user for consent. | 2 |
| **10.7.1** | 권한 부여 서버가 사용자가 각 권한 부여 요청에 동의하는지 확인하는지 검증해야 한다. 클라이언트의 ID를 보장할 수 없는 경우, 권한 부여 서버는 항상 사용자에게 명시적으로 동의를 요청해야 한다. | 2 |
| **10.7.2** | Verify that when the authorization server prompts for user consent, it presents sufficient and clear information about what is being consented to. When applicable, this should include the nature of the requested authorizations (typically based on scope, resource server, Rich Authorization Requests (RAR) authorization details), the identity of the authorized application, and the lifetime of these authorizations. | 2 |
| **10.7.2** | 권한 부여 서버가 사용자 동의를 요청할 때, 동의하는 내용에 대한 충분하고 명확한 정보를 제시하는지 검증해야 한다. 해당하는 경우, 요청된 권한 부여의 성격(일반적으로 범위, 리소스 서버, RAR(Rich Authorization Requests) 권한 부여 세부 정보 기반), 권한 부여된 애플리케이션의 ID, 이러한 권한 부여의 수명 기간이 포함되어야 한다. | 2 |
| **10.7.3** | Verify that the user can review, modify, and revoke consents which the user has granted through the authorization server. | 2 |
| **10.7.3** | 사용자가 권한 부여 서버를 통해 부여한 동의를 검토, 수정 및 취소할 수 있는지 검증해야 한다. | 2 |

## 참조

더 많은 정보는 다음을 참조한다:

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 프로토콜 치트 시트](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

ASVS에서 OAuth 관련 요구 사항은 다음의 공개 및 초안 상태 RFC를 사용한다.

* [RFC6749 OAuth 2.0 권한 부여 프레임워크](https://datatracker.ietf.org/doc/html/rfc6749)
* [RFC6750 OAuth 2.0 권한 부여 프레임워크: 베어러 토큰 사용](https://datatracker.ietf.org/doc/html/rfc6750)
* [RFC6819 OAuth 2.0 위협 모델 및 보안 고려 사항](https://datatracker.ietf.org/doc/html/rfc6819)
* [RFC7636 OAuth 공개 클라이언트를 위한 코드 교환 증명 키](https://datatracker.ietf.org/doc/html/rfc7636)
* [RFC7591 OAuth 2.0 동적 클라이언트 등록 프로토콜](https://datatracker.ietf.org/doc/html/rfc7591)
* [RFC8628 OAuth 2.0 장치 권한 부여 그랜트](https://datatracker.ietf.org/doc/html/rfc8628)
* [RFC8707 OAuth 2.0을 위한 리소스 표시자](https://datatracker.ietf.org/doc/html/rfc8707)
* [RFC9068 OAuth 2.0 접근 토큰을 위한 JSON 웹 토큰(JWT) 프로파일](https://datatracker.ietf.org/doc/html/rfc9068)
* [RFC9126 OAuth 2.0 푸시된 권한 부여 요청](https://datatracker.ietf.org/doc/html/rfc9126)
* [RFC9207 OAuth 2.0 권한 부여 서버 발급자 식별](https://datatracker.ietf.org/doc/html/rfc9207)
* [RFC9396 OAuth 2.0 풍부한 권한 부여 요청](https://datatracker.ietf.org/doc/html/rfc9396)
* [RFC9449 OAuth 2.0 PoP(Demonstrating Proof of Possession)](https://datatracker.ietf.org/doc/html/rfc9449)
* [RFC9700 OAuth 2.0 보안을 위한 현재 모범 사례](https://datatracker.ietf.org/doc/html/rfc9700)
* [draft 브라우저 기반 애플리케이션을 위한 OAuth 2.0](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)
* [draft OAuth 2.1 권한 부여 프레임워크](https://datatr.ietf.org/doc/html/draft-ietf-oauth-v2-1-12)

OpenID Connect에 대한 자세한 내용은 다음을 참조한다.

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 보안 프로파일](https://openid.net/specs/fapi-security-profile-2_0-final.html)
