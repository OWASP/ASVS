<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x13-V4-API-and-Web-Service.md -->
<!-- Translator: GeeksikhSecurity -->

# V4 API and Web Service
# V4 API ਅਤੇ ਵੈੱਬ ਸੇਵਾ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

Several considerations apply specifically to applications that expose APIs for use by web browsers or other consumers (commonly using JSON, XML, or GraphQL). This chapter covers the relevant security configurations and mechanisms that should be applied.

ਕਈ ਵਿਚਾਰ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ਉਹਨਾਂ ਐਪਲੀਕੇਸ਼ਨਾਂ 'ਤੇ ਲਾਗੂ ਹੁੰਦੇ ਹਨ ਜੋ ਵੈੱਬ ਬ੍ਰਾਊਜ਼ਰਾਂ ਜਾਂ ਹੋਰ ਖਪਤਕਾਰਾਂ (consumers) ਦੁਆਰਾ ਵਰਤੋਂ ਲਈ API ਉਜਾਗਰ ਕਰਦੀਆਂ ਹਨ (ਆਮ ਤੌਰ 'ਤੇ JSON, XML, ਜਾਂ GraphQL ਦੀ ਵਰਤੋਂ ਕਰਕੇ)। ਇਹ ਅਧਿਆਇ ਉਹਨਾਂ ਸੰਬੰਧਿਤ ਸੁਰੱਖਿਆ ਸੰਰਚਨਾਵਾਂ (configurations) ਅਤੇ ਪ੍ਰਣਾਲੀਆਂ (mechanisms) ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ ਜੋ ਲਾਗੂ ਕੀਤੀਆਂ ਜਾਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ।

Note that authentication, session management, and input validation concerns from other chapters also apply to APIs, so this chapter cannot be taken out of context or tested in isolation.

ਧਿਆਨ ਦਿਓ ਕਿ ਹੋਰ ਅਧਿਆਵਾਂ ਦੇ ਪ੍ਰਮਾਣੀਕਰਨ, ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ, ਅਤੇ ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ ਸੰਬੰਧੀ ਸਰੋਕਾਰ ਵੀ API 'ਤੇ ਲਾਗੂ ਹੁੰਦੇ ਹਨ, ਇਸ ਲਈ ਇਸ ਅਧਿਆਇ ਨੂੰ ਸੰਦਰਭ ਤੋਂ ਬਾਹਰ ਨਹੀਂ ਲਿਆ ਜਾ ਸਕਦਾ ਜਾਂ ਇਕੱਲਿਆਂ ਟੈਸਟ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ।

## V4.1 Generic Web Service Security
## V4.1 ਆਮ ਵੈੱਬ ਸੇਵਾ ਸੁਰੱਖਿਆ

This section addresses general web service security considerations and, consequently, basic web service hygiene practices.

ਇਹ ਭਾਗ ਆਮ ਵੈੱਬ ਸੇਵਾ ਸੁਰੱਖਿਆ ਵਿਚਾਰਾਂ ਨੂੰ ਅਤੇ, ਨਤੀਜੇ ਵਜੋਂ, ਬੁਨਿਆਦੀ ਵੈੱਬ ਸੇਵਾ ਸਫ਼ਾਈ (hygiene) ਅਮਲਾਂ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **4.1.1** | Verify that every HTTP response with a message body contains a Content-Type header field that matches the actual content of the response, including the charset parameter to specify safe character encoding (e.g., UTF-8, ISO-8859-1) according to IANA Media Types, such as "text/", "/+xml" and "/xml". | 1 |
| **4.1.2** | Verify that only user-facing endpoints (intended for manual web-browser access) automatically redirect from HTTP to HTTPS, while other services or endpoints do not implement transparent redirects. This is to avoid a situation where a client is erroneously sending unencrypted HTTP requests, but since the requests are being automatically redirected to HTTPS, the leakage of sensitive data goes undiscovered. | 2 |
| **4.1.3** | Verify that any HTTP header field used by the application and set by an intermediary layer, such as a load balancer, a web proxy, or a backend-for-frontend service, cannot be overridden by the end-user. Example headers might include X-Real-IP, X-Forwarded-*, or X-User-ID. | 2 |
| **4.1.4** | Verify that only HTTP methods that are explicitly supported by the application or its API (including OPTIONS during preflight requests) can be used and that unused methods are blocked. | 3 |
| **4.1.5** | Verify that per-message digital signatures are used to provide additional assurance on top of transport protections for requests or transactions which are highly sensitive or which traverse a number of systems. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **4.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੁਨੇਹਾ ਬਾਡੀ (message body) ਵਾਲੇ ਹਰੇਕ HTTP ਜਵਾਬ ਵਿੱਚ ਇੱਕ Content-Type ਹੈੱਡਰ ਖੇਤਰ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ ਜੋ ਜਵਾਬ ਦੀ ਅਸਲ ਸਮੱਗਰੀ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ IANA Media Types ਦੇ ਅਨੁਸਾਰ, ਜਿਵੇਂ ਕਿ "text/", "/+xml" ਅਤੇ "/xml", ਸੁਰੱਖਿਅਤ ਅੱਖਰ ਏਨਕੋਡਿੰਗ (ਜਿਵੇਂ ਕਿ UTF-8, ISO-8859-1) ਨਿਰਧਾਰਿਤ ਕਰਨ ਲਈ charset ਪੈਰਾਮੀਟਰ ਵੀ ਸ਼ਾਮਲ ਹੈ। | 1 |
| **4.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਿਰਫ਼ ਉਪਭੋਗਤਾ-ਮੁਖੀ ਅੰਤ-ਬਿੰਦੂ (endpoints) (ਜੋ ਹੱਥੀਂ ਵੈੱਬ-ਬ੍ਰਾਊਜ਼ਰ ਪਹੁੰਚ ਲਈ ਬਣਾਏ ਗਏ ਹਨ) ਹੀ HTTP ਤੋਂ HTTPS ਵੱਲ ਆਪਣੇ-ਆਪ ਰੀਡਾਇਰੈਕਟ ਕਰਦੇ ਹਨ, ਜਦੋਂ ਕਿ ਹੋਰ ਸੇਵਾਵਾਂ ਜਾਂ ਅੰਤ-ਬਿੰਦੂ ਪਾਰਦਰਸ਼ੀ ਰੀਡਾਇਰੈਕਟ ਲਾਗੂ ਨਹੀਂ ਕਰਦੇ। ਇਹ ਅਜਿਹੀ ਸਥਿਤੀ ਤੋਂ ਬਚਣ ਲਈ ਹੈ ਜਿੱਥੇ ਕੋਈ ਕਲਾਇੰਟ ਗਲਤੀ ਨਾਲ ਏਨਕ੍ਰਿਪਟ ਨਾ ਕੀਤੀਆਂ HTTP ਬੇਨਤੀਆਂ ਭੇਜ ਰਿਹਾ ਹੁੰਦਾ ਹੈ, ਪਰ ਕਿਉਂਕਿ ਬੇਨਤੀਆਂ ਆਪਣੇ-ਆਪ HTTPS ਵੱਲ ਰੀਡਾਇਰੈਕਟ ਹੋ ਰਹੀਆਂ ਹੁੰਦੀਆਂ ਹਨ, ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਦੀ ਲੀਕੇਜ ਅਣਖੋਜੀ ਰਹਿ ਜਾਂਦੀ ਹੈ। | 2 |
| **4.1.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ ਅਤੇ ਕਿਸੇ ਵਿਚੋਲੀ ਪਰਤ, ਜਿਵੇਂ ਕਿ ਲੋਡ ਬੈਲੈਂਸਰ, ਵੈੱਬ ਪ੍ਰੌਕਸੀ, ਜਾਂ backend-for-frontend ਸੇਵਾ, ਦੁਆਰਾ ਸੈੱਟ ਕੀਤਾ ਗਿਆ ਕੋਈ ਵੀ HTTP ਹੈੱਡਰ ਖੇਤਰ ਅੰਤਮ-ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਓਵਰਰਾਈਡ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ। ਉਦਾਹਰਨ ਹੈੱਡਰਾਂ ਵਿੱਚ X-Real-IP, X-Forwarded-*, ਜਾਂ X-User-ID ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ। | 2 |
| **4.1.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਿਰਫ਼ ਉਹੀ HTTP ਮੈਥਡ (methods) ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ ਇਸ ਦੇ API ਦੁਆਰਾ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਸਮਰਥਿਤ ਹਨ (ਪ੍ਰੀਫ਼ਲਾਈਟ ਬੇਨਤੀਆਂ ਦੌਰਾਨ OPTIONS ਸਮੇਤ) ਅਤੇ ਅਣਵਰਤੇ ਮੈਥਡ ਬਲੌਕ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। | 3 |
| **4.1.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਹਨਾਂ ਬੇਨਤੀਆਂ ਜਾਂ ਲੈਣ-ਦੇਣਾਂ ਲਈ, ਜੋ ਬਹੁਤ ਜ਼ਿਆਦਾ ਸੰਵੇਦਨਸ਼ੀਲ ਹਨ ਜਾਂ ਜੋ ਕਈ ਸਿਸਟਮਾਂ ਵਿੱਚੋਂ ਲੰਘਦੀਆਂ ਹਨ, ਟ੍ਰਾਂਸਪੋਰਟ ਸੁਰੱਖਿਆਵਾਂ ਦੇ ਉੱਪਰ ਵਾਧੂ ਭਰੋਸਾ ਪ੍ਰਦਾਨ ਕਰਨ ਲਈ ਪ੍ਰਤੀ-ਸੁਨੇਹਾ ਡਿਜ਼ੀਟਲ ਦਸਤਖ਼ਤ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। | 3 |

## V4.2 HTTP Message Structure Validation
## V4.2 HTTP ਸੁਨੇਹਾ ਢਾਂਚਾ ਪ੍ਰਮਾਣਿਕਤਾ

This section explains how the structure and header fields of an HTTP message should be validated to prevent attacks such as request smuggling, response splitting, header injection, and denial of service via overly long HTTP messages.

ਇਹ ਭਾਗ ਸਮਝਾਉਂਦਾ ਹੈ ਕਿ ਬੇਨਤੀ ਸਮਗਲਿੰਗ (request smuggling), ਜਵਾਬ ਵਿਭਾਜਨ (response splitting), ਹੈੱਡਰ ਇੰਜੈਕਸ਼ਨ (header injection), ਅਤੇ ਬਹੁਤ ਜ਼ਿਆਦਾ ਲੰਬੇ HTTP ਸੁਨੇਹਿਆਂ ਰਾਹੀਂ ਸੇਵਾ-ਇਨਕਾਰ (denial of service) ਵਰਗੇ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਕਿਸੇ HTTP ਸੁਨੇਹੇ (message) ਦੇ ਢਾਂਚੇ ਅਤੇ ਹੈੱਡਰ ਖੇਤਰਾਂ ਨੂੰ ਕਿਵੇਂ ਪ੍ਰਮਾਣਿਤ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

These requirements are relevant for general HTTP message processing and generation, but are especially important when converting HTTP messages between different HTTP versions.

ਇਹ ਲੋੜਾਂ ਆਮ HTTP ਸੁਨੇਹੇ ਪ੍ਰੋਸੈਸ ਕਰਨ ਅਤੇ ਬਣਾਉਣ ਲਈ ਸੰਬੰਧਿਤ ਹਨ, ਪਰ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ਉਦੋਂ ਮਹੱਤਵਪੂਰਨ ਹੁੰਦੀਆਂ ਹਨ ਜਦੋਂ HTTP ਸੁਨੇਹਿਆਂ ਨੂੰ ਵੱਖ-ਵੱਖ HTTP ਸੰਸਕਰਣਾਂ ਦੇ ਵਿਚਕਾਰ ਰੂਪਾਂਤਰਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **4.2.1** | Verify that all application components (including load balancers, firewalls, and application servers) determine boundaries of incoming HTTP messages using the appropriate mechanism for the HTTP version to prevent HTTP request smuggling. In HTTP/1.x, if a Transfer-Encoding header field is present, the Content-Length header must be ignored per RFC 2616. When using HTTP/2 or HTTP/3, if a Content-Length header field is present, the receiver must ensure that it is consistent with the length of the DATA frames. | 2 |
| **4.2.2** | Verify that when generating HTTP messages, the Content-Length header field does not conflict with the length of the content as determined by the framing of the HTTP protocol, in order to prevent request smuggling attacks. | 3 |
| **4.2.3** | Verify that the application does not send nor accept HTTP/2 or HTTP/3 messages with connection-specific header fields such as Transfer-Encoding to prevent response splitting and header injection attacks. | 3 |
| **4.2.4** | Verify that the application only accepts HTTP/2 and HTTP/3 requests where the header fields and values do not contain any CR (\r), LF (\n), or CRLF (\r\n) sequences, to prevent header injection attacks. | 3 |
| **4.2.5** | Verify that, if the application (backend or frontend) builds and sends requests, it uses validation, sanitization, or other mechanisms to avoid creating URIs (such as for API calls) or HTTP request header fields (such as Authorization or Cookie), which are too long to be accepted by the receiving component. This could cause a denial of service, such as when sending an overly long request (e.g., a long cookie header field), which results in the server always responding with an error status. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **4.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੇ ਐਪਲੀਕੇਸ਼ਨ ਘਟਕ (components) (ਲੋਡ ਬੈਲੈਂਸਰ, ਫ਼ਾਇਰਵਾਲ, ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਸਰਵਰ ਸਮੇਤ) HTTP ਬੇਨਤੀ ਸਮਗਲਿੰਗ ਨੂੰ ਰੋਕਣ ਲਈ HTTP ਸੰਸਕਰਣ ਲਈ ਢੁਕਵੀਂ ਪ੍ਰਣਾਲੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਉਣ ਵਾਲੇ HTTP ਸੁਨੇਹਿਆਂ ਦੀਆਂ ਸੀਮਾਵਾਂ ਨਿਰਧਾਰਿਤ ਕਰਦੇ ਹਨ। HTTP/1.x ਵਿੱਚ, ਜੇ Transfer-Encoding ਹੈੱਡਰ ਖੇਤਰ ਮੌਜੂਦ ਹੈ, ਤਾਂ RFC 2616 ਦੇ ਅਨੁਸਾਰ Content-Length ਹੈੱਡਰ ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਅਣਡਿੱਠ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। HTTP/2 ਜਾਂ HTTP/3 ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਸਮੇਂ, ਜੇ Content-Length ਹੈੱਡਰ ਖੇਤਰ ਮੌਜੂਦ ਹੈ, ਤਾਂ ਪ੍ਰਾਪਤਕਰਤਾ ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਯਕੀਨੀ ਬਣਾਉਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਇਹ DATA ਫ਼੍ਰੇਮਾਂ ਦੀ ਲੰਬਾਈ ਨਾਲ ਇਕਸਾਰ ਹੈ। | 2 |
| **4.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ HTTP ਸੁਨੇਹੇ ਬਣਾਉਂਦੇ ਸਮੇਂ, ਬੇਨਤੀ ਸਮਗਲਿੰਗ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ, Content-Length ਹੈੱਡਰ ਖੇਤਰ HTTP ਪ੍ਰੋਟੋਕਾਲ ਦੀ ਫ਼੍ਰੇਮਿੰਗ ਦੁਆਰਾ ਨਿਰਧਾਰਿਤ ਸਮੱਗਰੀ ਦੀ ਲੰਬਾਈ ਨਾਲ ਟਕਰਾਉਂਦਾ ਨਹੀਂ ਹੈ। | 3 |
| **4.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਵਾਬ ਵਿਭਾਜਨ ਅਤੇ ਹੈੱਡਰ ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਐਪਲੀਕੇਸ਼ਨ Transfer-Encoding ਵਰਗੇ ਕਨੈਕਸ਼ਨ-ਵਿਸ਼ੇਸ਼ ਹੈੱਡਰ ਖੇਤਰਾਂ ਵਾਲੇ HTTP/2 ਜਾਂ HTTP/3 ਸੁਨੇਹੇ ਨਾ ਤਾਂ ਭੇਜਦੀ ਹੈ ਅਤੇ ਨਾ ਹੀ ਸਵੀਕਾਰ ਕਰਦੀ ਹੈ। | 3 |
| **4.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸਿਰਫ਼ ਉਹੀ HTTP/2 ਅਤੇ HTTP/3 ਬੇਨਤੀਆਂ ਸਵੀਕਾਰ ਕਰਦੀ ਹੈ ਜਿਨ੍ਹਾਂ ਦੇ ਹੈੱਡਰ ਖੇਤਰਾਂ ਅਤੇ ਮੁੱਲਾਂ ਵਿੱਚ ਕੋਈ CR (\r), LF (\n), ਜਾਂ CRLF (\r\n) ਲੜੀਆਂ ਨਹੀਂ ਹੁੰਦੀਆਂ, ਤਾਂ ਜੋ ਹੈੱਡਰ ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 3 |
| **4.2.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ ਐਪਲੀਕੇਸ਼ਨ (ਬੈਕਐਂਡ ਜਾਂ ਫਰੰਟਐਂਡ) ਬੇਨਤੀਆਂ ਬਣਾਉਂਦੀ ਅਤੇ ਭੇਜਦੀ ਹੈ, ਤਾਂ ਇਹ ਅਜਿਹੇ URI (ਜਿਵੇਂ ਕਿ API ਕਾਲਾਂ ਲਈ) ਜਾਂ HTTP ਬੇਨਤੀ ਹੈੱਡਰ ਖੇਤਰ (ਜਿਵੇਂ ਕਿ Authorization ਜਾਂ Cookie) ਬਣਾਉਣ ਤੋਂ ਬਚਣ ਲਈ, ਜੋ ਪ੍ਰਾਪਤ ਕਰਨ ਵਾਲੇ ਘਟਕ ਦੁਆਰਾ ਸਵੀਕਾਰ ਕੀਤੇ ਜਾਣ ਲਈ ਬਹੁਤ ਜ਼ਿਆਦਾ ਲੰਬੇ ਹੋਣ, ਪ੍ਰਮਾਣਿਕਤਾ, ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ, ਜਾਂ ਹੋਰ ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ। ਇਹ ਸੇਵਾ-ਇਨਕਾਰ ਦਾ ਕਾਰਨ ਬਣ ਸਕਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਜਦੋਂ ਕੋਈ ਬਹੁਤ ਜ਼ਿਆਦਾ ਲੰਬੀ ਬੇਨਤੀ (ਜਿਵੇਂ ਕਿ ਇੱਕ ਲੰਬਾ cookie ਹੈੱਡਰ ਖੇਤਰ) ਭੇਜੀ ਜਾਂਦੀ ਹੈ, ਜਿਸ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਸਰਵਰ ਹਮੇਸ਼ਾ ਇੱਕ ਗਲਤੀ ਸਥਿਤੀ (error status) ਨਾਲ ਜਵਾਬ ਦਿੰਦਾ ਹੈ। | 3 |

## V4.3 GraphQL
## V4.3 GraphQL (ਗ੍ਰਾਫ਼ਕਿਊਐੱਲ)

GraphQL is becoming more common as a way of creating data-rich clients that are not tightly coupled to a variety of backend services. This section covers security considerations for GraphQL.

GraphQL ਅਜਿਹੇ ਡਾਟਾ-ਭਰਪੂਰ ਕਲਾਇੰਟ ਬਣਾਉਣ ਦੇ ਇੱਕ ਢੰਗ ਵਜੋਂ ਵਧੇਰੇ ਆਮ ਹੁੰਦਾ ਜਾ ਰਿਹਾ ਹੈ ਜੋ ਵੱਖ-ਵੱਖ ਬੈਕਐਂਡ ਸੇਵਾਵਾਂ ਨਾਲ ਸਖ਼ਤੀ ਨਾਲ ਜੁੜੇ ਹੋਏ (tightly coupled) ਨਹੀਂ ਹੁੰਦੇ। ਇਹ ਭਾਗ GraphQL ਲਈ ਸੁਰੱਖਿਆ ਵਿਚਾਰਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **4.3.1** | Verify that a query allowlist, depth limiting, amount limiting, or query cost analysis is used to prevent GraphQL or data layer expression Denial of Service (DoS) as a result of expensive, nested queries. | 2 |
| **4.3.2** | Verify that GraphQL introspection queries are disabled in the production environment unless the GraphQL API is meant to be used by other parties. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **4.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਮਹਿੰਗੀਆਂ, ਨੇਸਟਡ (nested) ਕਿਊਰੀਆਂ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਹੋਣ ਵਾਲੇ GraphQL ਜਾਂ ਡਾਟਾ ਪਰਤ ਐਕਸਪ੍ਰੈਸ਼ਨ ਸੇਵਾ-ਇਨਕਾਰ (Denial of Service, DoS) ਨੂੰ ਰੋਕਣ ਲਈ ਇੱਕ ਕਿਊਰੀ allowlist, ਡੂੰਘਾਈ ਸੀਮਾਬੰਦੀ, ਮਾਤਰਾ ਸੀਮਾਬੰਦੀ, ਜਾਂ ਕਿਊਰੀ ਲਾਗਤ ਵਿਸ਼ਲੇਸ਼ਣ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 2 |
| **4.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰੋਡਕਸ਼ਨ ਵਾਤਾਵਰਣ ਵਿੱਚ GraphQL introspection ਕਿਊਰੀਆਂ ਅਸਮਰੱਥ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ, ਜਦੋਂ ਤੱਕ ਕਿ GraphQL API ਹੋਰ ਧਿਰਾਂ ਦੁਆਰਾ ਵਰਤੇ ਜਾਣ ਲਈ ਨਾ ਹੋਵੇ। | 2 |

## V4.4 WebSocket
## V4.4 WebSocket (ਵੈੱਬਸਾਕਟ)

WebSocket is a communications protocol that provides a simultaneous two-way communication channel over a single TCP connection. It was standardized by the IETF as RFC 6455 in 2011 and is distinct from HTTP, even though it is designed to work over HTTP ports 443 and 80.

WebSocket ਇੱਕ ਸੰਚਾਰ ਪ੍ਰੋਟੋਕਾਲ ਹੈ ਜੋ ਇੱਕ ਸਿੰਗਲ TCP ਕਨੈਕਸ਼ਨ ਉੱਤੇ ਇੱਕੋ ਸਮੇਂ ਦੋ-ਪਾਸੜ ਸੰਚਾਰ ਚੈਨਲ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਇਸ ਨੂੰ IETF ਦੁਆਰਾ 2011 ਵਿੱਚ RFC 6455 ਵਜੋਂ ਮਿਆਰੀਕ੍ਰਿਤ ਕੀਤਾ ਗਿਆ ਸੀ ਅਤੇ ਇਹ HTTP ਤੋਂ ਵੱਖਰਾ ਹੈ, ਭਾਵੇਂ ਇਹ HTTP ਪੋਰਟਾਂ 443 ਅਤੇ 80 ਉੱਤੇ ਕੰਮ ਕਰਨ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ।

This section provides key security requirements to prevent attacks related to communication security and session management that specifically exploit this real-time communication channel.

ਇਹ ਭਾਗ ਸੰਚਾਰ ਸੁਰੱਖਿਆ ਅਤੇ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਨਾਲ ਸੰਬੰਧਿਤ ਉਹਨਾਂ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਮੁੱਖ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ਇਸ ਰੀਅਲ-ਟਾਈਮ ਸੰਚਾਰ ਚੈਨਲ ਦਾ ਸ਼ੋਸ਼ਣ (exploit) ਕਰਦੇ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **4.4.1** | Verify that WebSocket over TLS (WSS) is used for all WebSocket connections. | 1 |
| **4.4.2** | Verify that, during the initial HTTP WebSocket handshake, the Origin header field is checked against a list of origins allowed for the application. | 2 |
| **4.4.3** | Verify that, if the application's standard session management cannot be used, dedicated tokens are being used for this, which comply with the relevant Session Management security requirements. | 2 |
| **4.4.4** | Verify that dedicated WebSocket session management tokens are initially obtained or validated through the previously authenticated HTTPS session when transitioning an existing HTTPS session to a WebSocket channel. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **4.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੇ WebSocket ਕਨੈਕਸ਼ਨਾਂ ਲਈ WebSocket over TLS (WSS) ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 1 |
| **4.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਸ਼ੁਰੂਆਤੀ HTTP WebSocket ਹੈਂਡਸ਼ੇਕ ਦੌਰਾਨ, Origin ਹੈੱਡਰ ਖੇਤਰ ਦੀ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਇਜਾਜ਼ਤ ਪ੍ਰਾਪਤ ਓਰਿਜਿਨਾਂ (origins) ਦੀ ਸੂਚੀ ਦੇ ਵਿਰੁੱਧ ਜਾਂਚ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 2 |
| **4.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਮਿਆਰੀ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਨਹੀਂ ਵਰਤਿਆ ਜਾ ਸਕਦਾ, ਤਾਂ ਇਸ ਲਈ ਸਮਰਪਿਤ ਟੋਕਨ ਵਰਤੇ ਜਾ ਰਹੇ ਹਨ, ਜੋ ਸੰਬੰਧਿਤ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹਨ। | 2 |
| **4.4.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਿਸੇ ਮੌਜੂਦਾ HTTPS ਸੈਸ਼ਨ ਨੂੰ WebSocket ਚੈਨਲ ਵਿੱਚ ਤਬਦੀਲ ਕਰਦੇ ਸਮੇਂ, ਸਮਰਪਿਤ WebSocket ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਟੋਕਨ ਸ਼ੁਰੂ ਵਿੱਚ ਪਹਿਲਾਂ ਪ੍ਰਮਾਣੀਕਰਨ ਕੀਤੇ ਗਏ HTTPS ਸੈਸ਼ਨ ਰਾਹੀਂ ਪ੍ਰਾਪਤ ਕੀਤੇ ਜਾਂ ਪ੍ਰਮਾਣਿਤ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। | 2 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* Resources on GraphQL Authorization from [graphql.org](https://graphql.org/learn/authorization/) and [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods).
* [OWASP Web Security Testing Guide: GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [OWASP Web Security Testing Guide: Testing WebSockets](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)
