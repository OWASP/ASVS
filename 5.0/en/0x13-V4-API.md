# V4 API and Web Service

## Control Objective

A number of considerations apply specifically for applications that expose APIs for use by a web browser or other consumers (commonly using JSON, XML, or GraphQL). This chapter covers relevant security configurations and mechanisms to be applied.

Note that the general authentication, session management, or general input validation concerns from other chapters also apply to APIs so this chapter can not be taken out of context or tested separately.

## V4.1 Generic Web Service Security

This section promotes generic web service security considerations and consequently basic web service hygiene practices.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **4.1.1** | Verify that every HTTP response with a message body contains a Content-Type header field that matches the actual content of the response, including the charset parameter to specify safe character encoding (e.g., UTF-8, ISO-8859-1) according to IANA Media Types, such as "text/", "/+xml" and "/xml". | 1 | v5.0.be-13.1.7 |
| **4.1.2** | Verify that only user-facing endpoints (intended for manual web-browser access) automatically redirect from HTTP to HTTPS, while other services or endpoints do not implement transparent redirects. This is to avoid a situation where a client is erroneously sending unencrypted HTTP requests, but since the requests are being automatically redirected to HTTPS, the leakage of sensitive data goes undiscovered. | 2 | v5.0.be-13.1.8 |
| **4.1.3** | Verify that per-message digital signatures are used to provide additional assurance on top of transport protections for requests or transactions which are highly sensitive or which traverse a number of systems. | 3 | v5.0.be-13.1.6 |

## V4.2 HTTP Request Header Validation

This section details how HTTP request header fields should be validated to prevent attacks such as HTTP Request Smuggling or source spoofing.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **4.2.1** | Verify that all application components, including load balancers, firewalls, and application servers, comply with RFC 2616 by ignoring the Content-Length header field when a Transfer-Encoding header field is present, to prevent HTTP Request Smuggling. | 2 | v5.0.be-13.6.2 |
| **4.2.2** | Verify that any HTTP header field used by the application and defined by intermediary devices like load balancers or proxies, such as X-Real-IP and X-Forwarded-*, cannot be overridden by the end-user. | 2 | v5.0.be-13.6.3 |
| **4.2.3** | Verify that only HTTP methods that are explicitly supported by the application or its API (including OPTIONS during preflight requests) can be used and that unused methods are blocked. | 3 | v5.0.be-13.6.1 |

## V4.3 HTTP/2

This section focuses on specific security considerations related to HTTP/2 and may also apply to HTTP/3.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **4.3.1** | Verify that when downgrading from HTTP/2 to an older HTTP version, the standard mechanism for calculating request length is used. Ensure that conflicting Content-Length and Transfer-Encoding header fields are not introduced, as they may lead to request smuggling vulnerabilities. | 3 | v5.0.be-13.7.1 |
| **4.3.2** | Verify that all Transfer-Encoding header fields are stripped from HTTP/2 messages or that HTTP/2 requests containing them are rejected to prevent response splitting and header injection attacks. | 3 | v5.0.be-13.7.2 |
| **4.3.3** | Verify that the application only accepts HTTP/2 and HTTP/3 requests where the header fields and values do not contain any CR (\r), LF (\n), or CRLF (\r\n) sequences, to prevent header injection attacks. | 3 | v5.0.be-13.7.3 |

## V4.4 GraphQL

GraphQL is becoming more common as a way of creating data rich clients which are not coupled to a variety of different backend services. This section covers security considerations for GraphQL.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **4.4.1** | Verify that a query allowlist, depth limiting, amount limiting, or query cost analysis is used to prevent GraphQL or data layer expression Denial of Service (DoS) as a result of expensive, nested queries. | 2 | v5.0.be-13.4.1 |
| **4.4.2** | Verify that GraphQL introspection queries are disabled in the production environment unless the GraphQL API is meant to be used by other parties. | 2 | v5.0.be-13.4.3 |

## V4.5 WebSocket

WebSocket is a communications protocol, providing a simultaneous two-way communication channel over a single TCP connection. It was standardized by the IETF as RFC 6455 in 2011 and is distinct from HTTP, even though it is designed to work over HTTP ports 443 and 80.

This section provides key security requirements to prevent attacks related to communication security and session management that specifically exploit this real-time communication channel.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **4.5.1** | Verify that WebSocket over TLS (WSS) is used for all WebSocket connections. | 1 | v5.0.be-13.5.1 |
| **4.5.2** | Verify that, during the initial HTTP WebSocket handshake, the Origin header field is checked against a list of origins allowed for the application. | 2 | v5.0.be-13.5.2 |
| **4.5.3** | Verify that, if the application's standard session management cannot be used, dedicated tokens are being used for this, which comply with the relevant Session Management security requirements. | 2 | v5.0.be-13.5.3 |
| **4.5.4** | Verify that dedicated WebSocket session management tokens are initially obtained or validated through the previously authenticated HTTPS session when transitioning an existing HTTPS session to a WebSocket channel. | 2 | v5.0.be-13.5.4 |

## References

For more information, see also:

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* Resources on GraphQL Authorization from [graphql.org](https://graphql.org/learn/authorization/) and [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods).
* [WSTG - v4.2 | GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [WSTG - v4.1 | OWASP Foundation](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)
