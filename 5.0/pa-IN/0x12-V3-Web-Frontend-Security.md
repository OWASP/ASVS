<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x12-V3-Web-Frontend-Security.md -->
<!-- Translator: GeeksikhSecurity -->

# V3 Web Frontend Security
# V3 ਵੈੱਬ ਫਰੰਟਐਂਡ ਸੁਰੱਖਿਆ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

This chapter focuses on requirements designed to protect against attacks executed via a web frontend. These requirements do not apply to machine-to-machine solutions.

ਇਹ ਅਧਿਆਇ ਉਹਨਾਂ ਲੋੜਾਂ 'ਤੇ ਕੇਂਦਰਿਤ ਹੈ ਜੋ ਵੈੱਬ ਫਰੰਟਐਂਡ (web frontend) ਰਾਹੀਂ ਕੀਤੇ ਜਾਣ ਵਾਲੇ ਹਮਲਿਆਂ ਤੋਂ ਬਚਾਅ ਲਈ ਤਿਆਰ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ। ਇਹ ਲੋੜਾਂ ਮਸ਼ੀਨ-ਤੋਂ-ਮਸ਼ੀਨ ਹੱਲਾਂ 'ਤੇ ਲਾਗੂ ਨਹੀਂ ਹੁੰਦੀਆਂ।

## V3.1 Web Frontend Security Documentation
## V3.1 ਵੈੱਬ ਫਰੰਟਐਂਡ ਸੁਰੱਖਿਆ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

This section outlines the browser security features that should be specified in the application's documentation.

ਇਹ ਭਾਗ ਉਹਨਾਂ ਬ੍ਰਾਊਜ਼ਰ ਸੁਰੱਖਿਆ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਰੂਪਰੇਖਾ ਦਿੰਦਾ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ ਦਰਸਾਈਆਂ ਜਾਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **3.1.1** | Verify that application documentation states the expected security features that browsers using the application must support (such as HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), and other relevant HTTP security mechanisms). It must also define how the application must behave when some of these features are not available (such as warning the user or blocking access). | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **3.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਉਹਨਾਂ ਉਮੀਦ ਕੀਤੀਆਂ ਸੁਰੱਖਿਆ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ ਜਿਨ੍ਹਾਂ ਦਾ ਸਮਰਥਨ ਐਪਲੀਕੇਸ਼ਨ ਵਰਤਣ ਵਾਲੇ ਬ੍ਰਾਊਜ਼ਰਾਂ ਲਈ ਲਾਜ਼ਮੀ ਹੈ (ਜਿਵੇਂ ਕਿ HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), ਅਤੇ ਹੋਰ ਸੰਬੰਧਿਤ HTTP ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀਆਂ)। ਇਸ ਨੂੰ ਇਹ ਵੀ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ ਕਿ ਜਦੋਂ ਇਹਨਾਂ ਵਿੱਚੋਂ ਕੁਝ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਉਪਲਬਧ ਨਾ ਹੋਣ ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਕਿਵੇਂ ਵਿਹਾਰ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ (ਜਿਵੇਂ ਕਿ ਉਪਭੋਗਤਾ ਨੂੰ ਚੇਤਾਵਨੀ ਦੇਣਾ ਜਾਂ ਪਹੁੰਚ ਨੂੰ ਰੋਕਣਾ)। | 3 |

## V3.2 Unintended Content Interpretation
## V3.2 ਅਣਇੱਛਤ ਸਮੱਗਰੀ ਵਿਆਖਿਆ

Rendering content or functionality in an incorrect context can result in malicious content being executed or displayed.

ਸਮੱਗਰੀ ਜਾਂ ਕਾਰਜਸ਼ੀਲਤਾ ਨੂੰ ਗ਼ਲਤ ਸੰਦਰਭ ਵਿੱਚ ਰੈਂਡਰ (render) ਕਰਨ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਖ਼ਤਰਨਾਕ ਸਮੱਗਰੀ ਚਲਾਈ ਜਾਂ ਪ੍ਰਦਰਸ਼ਿਤ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **3.2.1** | Verify that security controls are in place to prevent browsers from rendering content or functionality in HTTP responses in an incorrect context (e.g., when an API, a user-uploaded file or other resource is requested directly). Possible controls could include: not serving the content unless HTTP request header fields (such as Sec-Fetch-\*) indicate it is the correct context, using the sandbox directive of the Content-Security-Policy header field or using the attachment disposition type in the Content-Disposition header field. | 1 |
| **3.2.2** | Verify that content intended to be displayed as text, rather than rendered as HTML, is handled using safe rendering functions (such as createTextNode or textContent) to prevent unintended execution of content such as HTML or JavaScript. | 1 |
| **3.2.3** | Verify that the application avoids DOM clobbering when using client-side JavaScript by employing explicit variable declarations, performing strict type checking, avoiding storing global variables on the document object, and implementing namespace isolation. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **3.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਬ੍ਰਾਊਜ਼ਰਾਂ ਨੂੰ HTTP ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ (responses) ਵਿਚਲੀ ਸਮੱਗਰੀ ਜਾਂ ਕਾਰਜਸ਼ੀਲਤਾ ਨੂੰ ਗ਼ਲਤ ਸੰਦਰਭ ਵਿੱਚ ਰੈਂਡਰ ਕਰਨ ਤੋਂ ਰੋਕਣ ਲਈ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਮੌਜੂਦ ਹਨ (ਜਿਵੇਂ ਕਿ, ਜਦੋਂ ਕਿਸੇ API, ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਅੱਪਲੋਡ ਕੀਤੀ ਫ਼ਾਈਲ ਜਾਂ ਹੋਰ ਸਰੋਤ ਦੀ ਸਿੱਧੀ ਬੇਨਤੀ ਕੀਤੀ ਜਾਂਦੀ ਹੈ)। ਸੰਭਵ ਨਿਯੰਤਰਣਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ: ਸਮੱਗਰੀ ਨੂੰ ਉਦੋਂ ਤੱਕ ਨਾ ਪਰੋਸਣਾ ਜਦੋਂ ਤੱਕ HTTP ਬੇਨਤੀ ਹੈੱਡਰ ਖੇਤਰ (ਜਿਵੇਂ ਕਿ Sec-Fetch-\*) ਇਹ ਸੰਕੇਤ ਨਾ ਦੇਣ ਕਿ ਇਹ ਸਹੀ ਸੰਦਰਭ ਹੈ, Content-Security-Policy ਹੈੱਡਰ ਖੇਤਰ ਦੇ sandbox ਨਿਰਦੇਸ਼ (directive) ਦੀ ਵਰਤੋਂ ਕਰਨਾ, ਜਾਂ Content-Disposition ਹੈੱਡਰ ਖੇਤਰ ਵਿੱਚ attachment ਡਿਸਪੋਜ਼ੀਸ਼ਨ ਕਿਸਮ ਦੀ ਵਰਤੋਂ ਕਰਨਾ। | 1 |
| **3.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜੋ ਸਮੱਗਰੀ HTML ਵਜੋਂ ਰੈਂਡਰ ਕੀਤੇ ਜਾਣ ਦੀ ਬਜਾਏ ਟੈਕਸਟ ਵਜੋਂ ਪ੍ਰਦਰਸ਼ਿਤ ਕੀਤੇ ਜਾਣ ਲਈ ਹੈ, ਉਸ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੈਂਡਰਿੰਗ ਫੰਕਸ਼ਨਾਂ (ਜਿਵੇਂ ਕਿ createTextNode ਜਾਂ textContent) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੰਭਾਲਿਆ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਜੋ HTML ਜਾਂ JavaScript ਵਰਗੀ ਸਮੱਗਰੀ ਨੂੰ ਅਣਇੱਛਤ ਤੌਰ 'ਤੇ ਚੱਲਣ ਤੋਂ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 1 |
| **3.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਕਲਾਇੰਟ-ਸਾਈਡ JavaScript ਵਰਤਦੇ ਸਮੇਂ DOM clobbering ਤੋਂ ਬਚਦੀ ਹੈ, ਜਿਸ ਲਈ ਸਪੱਸ਼ਟ ਵੇਰੀਏਬਲ ਘੋਸ਼ਣਾਵਾਂ ਦੀ ਵਰਤੋਂ, ਸਖ਼ਤ ਕਿਸਮ ਜਾਂਚ (strict type checking), document ਆਬਜੈਕਟ 'ਤੇ ਗਲੋਬਲ ਵੇਰੀਏਬਲ ਸਟੋਰ ਕਰਨ ਤੋਂ ਬਚਣਾ, ਅਤੇ ਨੇਮਸਪੇਸ ਅਲਹਿਦਗੀ (namespace isolation) ਲਾਗੂ ਕਰਨਾ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। | 3 |

## V3.3 Cookie Setup
## V3.3 ਕੁਕੀ ਸੈੱਟਅੱਪ

This section outlines requirements for securely configuring sensitive cookies to provide a higher level of assurance that they were created by the application itself and to prevent their contents from leaking or being inappropriately modified.

ਇਹ ਭਾਗ ਸੰਵੇਦਨਸ਼ੀਲ ਕੁਕੀਆਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਕੌਨਫ਼ਿਗਰ ਕਰਨ ਦੀਆਂ ਲੋੜਾਂ ਦੀ ਰੂਪਰੇਖਾ ਦਿੰਦਾ ਹੈ, ਤਾਂ ਜੋ ਇਸ ਗੱਲ ਦਾ ਉੱਚ ਪੱਧਰ ਦਾ ਭਰੋਸਾ ਮਿਲੇ ਕਿ ਉਹ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਖ਼ੁਦ ਬਣਾਈਆਂ ਗਈਆਂ ਸਨ, ਅਤੇ ਉਹਨਾਂ ਦੀ ਸਮੱਗਰੀ ਨੂੰ ਲੀਕ ਹੋਣ ਜਾਂ ਅਣਉਚਿਤ ਢੰਗ ਨਾਲ ਸੋਧੇ ਜਾਣ ਤੋਂ ਰੋਕਿਆ ਜਾ ਸਕੇ।

| # | Description | Level |
| :---: | :--- | :---: |
| **3.3.1** | Verify that cookies have the 'Secure' attribute set, and if the '\__Host-' prefix is not used for the cookie name, the '__Secure-' prefix must be used for the cookie name. | 1 |
| **3.3.2** | Verify that each cookie's 'SameSite' attribute value is set according to the purpose of the cookie, to limit exposure to user interface redress attacks and browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF). | 2 |
| **3.3.3** | Verify that cookies have the '__Host-' prefix for the cookie name unless they are explicitly designed to be shared with other hosts. | 2 |
| **3.3.4** | Verify that if the value of a cookie is not meant to be accessible to client-side scripts (such as a session token), the cookie must have the 'HttpOnly' attribute set and the same value (e. g. session token) must only be transferred to the client via the 'Set-Cookie' header field. | 2 |
| **3.3.5** | Verify that when the application writes a cookie, the cookie name and value length combined are not over 4096 bytes. Overly large cookies will not be stored by the browser and therefore not sent with requests, preventing the user from using application functionality which relies on that cookie. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **3.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕੁਕੀਆਂ 'ਤੇ 'Secure' ਗੁਣ (attribute) ਸੈੱਟ ਹੈ, ਅਤੇ ਜੇ ਕੁਕੀ ਨਾਮ ਲਈ '\__Host-' ਅਗੇਤਰ ਨਹੀਂ ਵਰਤਿਆ ਜਾਂਦਾ, ਤਾਂ ਕੁਕੀ ਨਾਮ ਲਈ '__Secure-' ਅਗੇਤਰ ਵਰਤਿਆ ਜਾਣਾ ਲਾਜ਼ਮੀ ਹੈ। | 1 |
| **3.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਹਰੇਕ ਕੁਕੀ ਦੇ 'SameSite' ਗੁਣ ਦਾ ਮੁੱਲ ਕੁਕੀ ਦੇ ਉਦੇਸ਼ ਅਨੁਸਾਰ ਸੈੱਟ ਕੀਤਾ ਗਿਆ ਹੈ, ਤਾਂ ਜੋ ਉਪਭੋਗਤਾ ਇੰਟਰਫ਼ੇਸ ਰੀਡਰੈੱਸ (user interface redress) ਹਮਲਿਆਂ ਅਤੇ ਬ੍ਰਾਊਜ਼ਰ-ਆਧਾਰਿਤ ਬੇਨਤੀ ਜਾਅਲਸਾਜ਼ੀ ਹਮਲਿਆਂ, ਜਿਨ੍ਹਾਂ ਨੂੰ ਆਮ ਤੌਰ 'ਤੇ ਕਰਾਸ-ਸਾਈਟ ਬੇਨਤੀ ਜਾਅਲਸਾਜ਼ੀ (CSRF) ਕਿਹਾ ਜਾਂਦਾ ਹੈ, ਪ੍ਰਤੀ ਐਕਸਪੋਜ਼ਰ ਨੂੰ ਸੀਮਤ ਕੀਤਾ ਜਾ ਸਕੇ। | 2 |
| **3.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕੁਕੀਆਂ ਦੇ ਨਾਮ ਲਈ '__Host-' ਅਗੇਤਰ ਹੈ, ਜਦੋਂ ਤੱਕ ਉਹਨਾਂ ਨੂੰ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਹੋਰ ਹੋਸਟਾਂ ਨਾਲ ਸਾਂਝਾ ਕੀਤੇ ਜਾਣ ਲਈ ਡਿਜ਼ਾਈਨ ਨਾ ਕੀਤਾ ਗਿਆ ਹੋਵੇ। | 2 |
| **3.3.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜੇ ਕਿਸੇ ਕੁਕੀ ਦਾ ਮੁੱਲ ਕਲਾਇੰਟ-ਸਾਈਡ ਸਕ੍ਰਿਪਟਾਂ ਲਈ ਪਹੁੰਚਯੋਗ ਨਹੀਂ ਹੋਣਾ ਚਾਹੀਦਾ (ਜਿਵੇਂ ਕਿ ਸੈਸ਼ਨ ਟੋਕਨ), ਤਾਂ ਕੁਕੀ 'ਤੇ 'HttpOnly' ਗੁਣ ਸੈੱਟ ਹੋਣਾ ਲਾਜ਼ਮੀ ਹੈ ਅਤੇ ਉਹੀ ਮੁੱਲ (ਜਿਵੇਂ ਕਿ ਸੈਸ਼ਨ ਟੋਕਨ) ਕੇਵਲ 'Set-Cookie' ਹੈੱਡਰ ਖੇਤਰ ਰਾਹੀਂ ਹੀ ਕਲਾਇੰਟ ਨੂੰ ਭੇਜਿਆ ਜਾਣਾ ਲਾਜ਼ਮੀ ਹੈ। | 2 |
| **3.3.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਦੋਂ ਐਪਲੀਕੇਸ਼ਨ ਕੋਈ ਕੁਕੀ ਲਿਖਦੀ ਹੈ, ਤਾਂ ਕੁਕੀ ਦੇ ਨਾਮ ਅਤੇ ਮੁੱਲ ਦੀ ਸਾਂਝੀ ਲੰਬਾਈ 4096 ਬਾਈਟ ਤੋਂ ਵੱਧ ਨਹੀਂ ਹੁੰਦੀ। ਬਹੁਤ ਵੱਡੀਆਂ ਕੁਕੀਆਂ ਬ੍ਰਾਊਜ਼ਰ ਦੁਆਰਾ ਸਟੋਰ ਨਹੀਂ ਕੀਤੀਆਂ ਜਾਣਗੀਆਂ ਅਤੇ ਇਸ ਲਈ ਬੇਨਤੀਆਂ ਨਾਲ ਨਹੀਂ ਭੇਜੀਆਂ ਜਾਣਗੀਆਂ, ਜਿਸ ਨਾਲ ਉਪਭੋਗਤਾ ਉਸ ਕੁਕੀ 'ਤੇ ਨਿਰਭਰ ਐਪਲੀਕੇਸ਼ਨ ਕਾਰਜਸ਼ੀਲਤਾ ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕਰ ਸਕੇਗਾ। | 3 |

## V3.4 Browser Security Mechanism Headers
## V3.4 ਬ੍ਰਾਊਜ਼ਰ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀ ਹੈੱਡਰ

This section describes which security headers should be set on HTTP responses to enable browser security features and restrictions when handling responses from the application.

ਇਹ ਭਾਗ ਦੱਸਦਾ ਹੈ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਤੋਂ ਆਈਆਂ ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ ਨੂੰ ਸੰਭਾਲਦੇ ਸਮੇਂ ਬ੍ਰਾਊਜ਼ਰ ਸੁਰੱਖਿਆ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਪਾਬੰਦੀਆਂ ਨੂੰ ਸਮਰੱਥ ਕਰਨ ਲਈ HTTP ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ 'ਤੇ ਕਿਹੜੇ ਸੁਰੱਖਿਆ ਹੈੱਡਰ ਸੈੱਟ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **3.4.1** | Verify that a Strict-Transport-Security header field is included on all responses to enforce an HTTP Strict Transport Security (HSTS) policy. A maximum age of at least 1 year must be defined, and for L2 and up, the policy must apply to all subdomains as well. | 1 |
| **3.4.2** | Verify that the Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header field is a fixed value by the application, or if the Origin HTTP request header field value is used, it is validated against an allowlist of trusted origins. When 'Access-Control-Allow-Origin: *' needs to be used, verify that the response does not include any sensitive information. | 1 |
| **3.4.3** | Verify that HTTP responses include a Content-Security-Policy response header field which defines directives to ensure the browser only loads and executes trusted content or resources, in order to limit execution of malicious JavaScript. As a minimum, a global policy must be used which includes the directives object-src 'none' and base-uri 'none' and defines either an allowlist or uses nonces or hashes. For an L3 application, a per-response policy with nonces or hashes must be defined. | 2 |
| **3.4.4** | Verify that all HTTP responses contain an 'X-Content-Type-Options: nosniff' header field. This instructs browsers not to use content sniffing and MIME type guessing for the given response, and to require the response's Content-Type header field value to match the destination resource. For example, the response to a request for a style is only accepted if the response's Content-Type is 'text/css'. This also enables the use of the Cross-Origin Read Blocking (CORB) functionality by the browser. | 2 |
| **3.4.5** | Verify that the application sets a referrer policy to prevent leakage of technically sensitive data to third-party services via the 'Referer' HTTP request header field. This can be done using the Referrer-Policy HTTP response header field or via HTML element attributes. Sensitive data could include path and query data in the URL, and for internal non-public applications also the hostname. | 2 |
| **3.4.6** | Verify that the web application uses the frame-ancestors directive of the Content-Security-Policy header field for every HTTP response to ensure that it cannot be embedded by default and that embedding of specific resources is allowed only when necessary. Note that the X-Frame-Options header field, although supported by browsers, is obsolete and may not be relied upon. | 2 |
| **3.4.7** | Verify that the Content-Security-Policy header field specifies a location to report violations. | 3 |
| **3.4.8** | Verify that all HTTP responses that initiate a document rendering (such as responses with Content-Type text/html), include the Cross‑Origin‑Opener‑Policy header field with the same-origin directive or the same-origin-allow-popups directive as required. This prevents attacks that abuse shared access to Window objects, such as tabnabbing and frame counting. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **3.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ HTTP Strict Transport Security (HSTS) ਨੀਤੀ ਲਾਗੂ ਕਰਨ ਲਈ ਸਾਰੀਆਂ ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ 'ਤੇ Strict-Transport-Security ਹੈੱਡਰ ਖੇਤਰ ਸ਼ਾਮਲ ਕੀਤਾ ਗਿਆ ਹੈ। ਘੱਟੋ-ਘੱਟ 1 ਸਾਲ ਦੀ ਵੱਧ-ਤੋਂ-ਵੱਧ ਉਮਰ (maximum age) ਪਰਿਭਾਸ਼ਿਤ ਕਰਨੀ ਲਾਜ਼ਮੀ ਹੈ, ਅਤੇ L2 ਅਤੇ ਇਸ ਤੋਂ ਉੱਪਰ ਲਈ, ਇਹ ਨੀਤੀ ਸਾਰੇ ਸਬਡੋਮੇਨਾਂ 'ਤੇ ਵੀ ਲਾਗੂ ਹੋਣੀ ਲਾਜ਼ਮੀ ਹੈ। | 1 |
| **3.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin ਹੈੱਡਰ ਖੇਤਰ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਨਿਰਧਾਰਿਤ ਇੱਕ ਸਥਿਰ ਮੁੱਲ ਹੈ, ਜਾਂ ਜੇ Origin HTTP ਬੇਨਤੀ ਹੈੱਡਰ ਖੇਤਰ ਦਾ ਮੁੱਲ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਇਸ ਨੂੰ ਭਰੋਸੇਯੋਗ ਓਰਿਜਿਨਾਂ (origins) ਦੀ ਇੱਕ allowlist ਦੇ ਵਿਰੁੱਧ ਪ੍ਰਮਾਣਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਜਦੋਂ 'Access-Control-Allow-Origin: *' ਵਰਤਣ ਦੀ ਲੋੜ ਹੋਵੇ, ਤਾਂ ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰਤੀਕਿਰਿਆ ਵਿੱਚ ਕੋਈ ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਣਕਾਰੀ ਸ਼ਾਮਲ ਨਹੀਂ ਹੈ। | 1 |
| **3.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ HTTP ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ ਵਿੱਚ ਇੱਕ Content-Security-Policy ਪ੍ਰਤੀਕਿਰਿਆ ਹੈੱਡਰ ਖੇਤਰ ਸ਼ਾਮਲ ਹੈ ਜੋ ਅਜਿਹੇ ਨਿਰਦੇਸ਼ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੇ ਹਨ ਕਿ ਬ੍ਰਾਊਜ਼ਰ ਕੇਵਲ ਭਰੋਸੇਯੋਗ ਸਮੱਗਰੀ ਜਾਂ ਸਰੋਤ ਹੀ ਲੋਡ ਅਤੇ ਚਲਾਏ, ਤਾਂ ਜੋ ਖ਼ਤਰਨਾਕ JavaScript ਦੇ ਚੱਲਣ ਨੂੰ ਸੀਮਤ ਕੀਤਾ ਜਾ ਸਕੇ। ਘੱਟੋ-ਘੱਟ, ਇੱਕ ਗਲੋਬਲ ਨੀਤੀ ਵਰਤਣੀ ਲਾਜ਼ਮੀ ਹੈ ਜਿਸ ਵਿੱਚ object-src 'none' ਅਤੇ base-uri 'none' ਨਿਰਦੇਸ਼ ਸ਼ਾਮਲ ਹੋਣ ਅਤੇ ਜੋ ਜਾਂ ਤਾਂ ਇੱਕ allowlist ਪਰਿਭਾਸ਼ਿਤ ਕਰੇ ਜਾਂ ਨੌਂਸ (nonce) ਜਾਂ ਹੈਸ਼ ਵਰਤੇ। L3 ਐਪਲੀਕੇਸ਼ਨ ਲਈ, ਨੌਂਸ ਜਾਂ ਹੈਸ਼ ਵਾਲੀ ਪ੍ਰਤੀ-ਪ੍ਰਤੀਕਿਰਿਆ ਨੀਤੀ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨੀ ਲਾਜ਼ਮੀ ਹੈ। | 2 |
| **3.4.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੀਆਂ HTTP ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ ਵਿੱਚ 'X-Content-Type-Options: nosniff' ਹੈੱਡਰ ਖੇਤਰ ਸ਼ਾਮਲ ਹੈ। ਇਹ ਬ੍ਰਾਊਜ਼ਰਾਂ ਨੂੰ ਨਿਰਦੇਸ਼ ਦਿੰਦਾ ਹੈ ਕਿ ਉਹ ਦਿੱਤੀ ਗਈ ਪ੍ਰਤੀਕਿਰਿਆ ਲਈ ਸਮੱਗਰੀ ਸਨਿਫ਼ਿੰਗ (content sniffing) ਅਤੇ MIME ਕਿਸਮ ਦੇ ਅਨੁਮਾਨ ਦੀ ਵਰਤੋਂ ਨਾ ਕਰਨ, ਅਤੇ ਇਹ ਲੋੜ ਰੱਖਣ ਕਿ ਪ੍ਰਤੀਕਿਰਿਆ ਦੇ Content-Type ਹੈੱਡਰ ਖੇਤਰ ਦਾ ਮੁੱਲ ਮੰਜ਼ਿਲ ਸਰੋਤ ਨਾਲ ਮੇਲ ਖਾਵੇ। ਉਦਾਹਰਨ ਲਈ, ਕਿਸੇ ਸਟਾਈਲ ਲਈ ਬੇਨਤੀ ਦੀ ਪ੍ਰਤੀਕਿਰਿਆ ਕੇਵਲ ਤਾਂ ਹੀ ਸਵੀਕਾਰ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਜੇ ਪ੍ਰਤੀਕਿਰਿਆ ਦਾ Content-Type 'text/css' ਹੋਵੇ। ਇਹ ਬ੍ਰਾਊਜ਼ਰ ਦੁਆਰਾ Cross-Origin Read Blocking (CORB) ਕਾਰਜਸ਼ੀਲਤਾ ਦੀ ਵਰਤੋਂ ਨੂੰ ਵੀ ਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ। | 2 |
| **3.4.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ 'Referer' HTTP ਬੇਨਤੀ ਹੈੱਡਰ ਖੇਤਰ ਰਾਹੀਂ ਤਕਨੀਕੀ ਤੌਰ 'ਤੇ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਦੇ ਤੀਜੀ-ਧਿਰ ਸੇਵਾਵਾਂ ਨੂੰ ਲੀਕ ਹੋਣ ਤੋਂ ਰੋਕਣ ਲਈ ਇੱਕ ਰੈਫ਼ਰਰ ਨੀਤੀ (referrer policy) ਸੈੱਟ ਕਰਦੀ ਹੈ। ਇਹ Referrer-Policy HTTP ਪ੍ਰਤੀਕਿਰਿਆ ਹੈੱਡਰ ਖੇਤਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਾਂ HTML ਐਲੀਮੈਂਟ ਗੁਣਾਂ ਰਾਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਵਿੱਚ URL ਵਿਚਲਾ ਪਾਥ ਅਤੇ ਕਿਊਰੀ ਡਾਟਾ ਸ਼ਾਮਲ ਹੋ ਸਕਦਾ ਹੈ, ਅਤੇ ਅੰਦਰੂਨੀ ਗ਼ੈਰ-ਜਨਤਕ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਹੋਸਟਨੇਮ (hostname) ਵੀ। | 2 |
| **3.4.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਵੈੱਬ ਐਪਲੀਕੇਸ਼ਨ ਹਰੇਕ HTTP ਪ੍ਰਤੀਕਿਰਿਆ ਲਈ Content-Security-Policy ਹੈੱਡਰ ਖੇਤਰ ਦੇ frame-ancestors ਨਿਰਦੇਸ਼ ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਇਸ ਨੂੰ ਮੂਲ ਰੂਪ ਵਿੱਚ ਏਮਬੈੱਡ (embed) ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਅਤੇ ਖ਼ਾਸ ਸਰੋਤਾਂ ਦੀ ਏਮਬੈਡਿੰਗ ਦੀ ਇਜਾਜ਼ਤ ਕੇਵਲ ਲੋੜ ਪੈਣ 'ਤੇ ਹੀ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ। ਧਿਆਨ ਦਿਓ ਕਿ X-Frame-Options ਹੈੱਡਰ ਖੇਤਰ, ਭਾਵੇਂ ਬ੍ਰਾਊਜ਼ਰਾਂ ਦੁਆਰਾ ਸਮਰਥਿਤ ਹੈ, ਅਪ੍ਰਚਲਿਤ (obsolete) ਹੈ ਅਤੇ ਇਸ 'ਤੇ ਭਰੋਸਾ ਨਹੀਂ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ। | 2 |
| **3.4.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ Content-Security-Policy ਹੈੱਡਰ ਖੇਤਰ ਉਲੰਘਣਾਵਾਂ ਦੀ ਰਿਪੋਰਟ ਕਰਨ ਲਈ ਇੱਕ ਟਿਕਾਣਾ ਨਿਰਧਾਰਿਤ ਕਰਦਾ ਹੈ। | 3 |
| **3.4.8** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੀਆਂ HTTP ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ ਜੋ ਦਸਤਾਵੇਜ਼ ਰੈਂਡਰਿੰਗ ਸ਼ੁਰੂ ਕਰਦੀਆਂ ਹਨ (ਜਿਵੇਂ ਕਿ Content-Type text/html ਵਾਲੀਆਂ ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ), ਲੋੜ ਅਨੁਸਾਰ same-origin ਨਿਰਦੇਸ਼ ਜਾਂ same-origin-allow-popups ਨਿਰਦੇਸ਼ ਦੇ ਨਾਲ Cross‑Origin‑Opener‑Policy ਹੈੱਡਰ ਖੇਤਰ ਸ਼ਾਮਲ ਕਰਦੀਆਂ ਹਨ। ਇਹ ਉਹਨਾਂ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਦਾ ਹੈ ਜੋ Window ਆਬਜੈਕਟਾਂ ਤੱਕ ਸਾਂਝੀ ਪਹੁੰਚ ਦੀ ਦੁਰਵਰਤੋਂ ਕਰਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ tabnabbing ਅਤੇ frame counting। | 3 |

## V3.5 Browser Origin Separation
## V3.5 ਬ੍ਰਾਊਜ਼ਰ ਓਰਿਜਿਨ ਵੱਖਰੇਵਾਂ

When accepting a request to sensitive functionality on the server side, the application needs to ensure the request is initiated by the application itself or by a trusted party and has not been forged by an attacker.

ਸਰਵਰ ਵਾਲੇ ਪਾਸੇ ਸੰਵੇਦਨਸ਼ੀਲ ਕਾਰਜਸ਼ੀਲਤਾ ਲਈ ਕੋਈ ਬੇਨਤੀ ਸਵੀਕਾਰ ਕਰਦੇ ਸਮੇਂ, ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ ਕਿ ਬੇਨਤੀ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਖ਼ੁਦ ਜਾਂ ਕਿਸੇ ਭਰੋਸੇਯੋਗ ਧਿਰ ਦੁਆਰਾ ਸ਼ੁਰੂ ਕੀਤੀ ਗਈ ਹੈ ਅਤੇ ਕਿਸੇ ਹਮਲਾਵਰ ਦੁਆਰਾ ਜਾਅਲੀ ਨਹੀਂ ਬਣਾਈ ਗਈ।

Sensitive functionality in this context could include accepting form posts for authenticated and non-authenticated users (such as an authentication request), state-changing operations, or resource-demanding functionality (such as data export).

ਇਸ ਸੰਦਰਭ ਵਿੱਚ ਸੰਵੇਦਨਸ਼ੀਲ ਕਾਰਜਸ਼ੀਲਤਾ ਵਿੱਚ ਪ੍ਰਮਾਣੀਕ੍ਰਿਤ (authenticated) ਅਤੇ ਗ਼ੈਰ-ਪ੍ਰਮਾਣੀਕ੍ਰਿਤ ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਫ਼ਾਰਮ ਪੋਸਟਾਂ ਸਵੀਕਾਰ ਕਰਨਾ (ਜਿਵੇਂ ਕਿ ਪ੍ਰਮਾਣੀਕਰਨ ਬੇਨਤੀ), ਸਥਿਤੀ-ਬਦਲਣ ਵਾਲੇ ਕਾਰਜ, ਜਾਂ ਸਰੋਤ-ਮੰਗ ਵਾਲੀ ਕਾਰਜਸ਼ੀਲਤਾ (ਜਿਵੇਂ ਕਿ ਡਾਟਾ ਨਿਰਯਾਤ) ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ।

The key protections here are browser security policies like Same Origin Policy for JavaScript and also SameSite logic for cookies. Another common protection is the CORS preflight mechanism. This mechanism will be critical for endpoints designed to be called from a different origin, but it can also be a useful request forgery prevention mechanism for endpoints which are not designed to be called from a different origin.

ਇੱਥੇ ਮੁੱਖ ਸੁਰੱਖਿਆਵਾਂ JavaScript ਲਈ Same Origin Policy ਅਤੇ ਕੁਕੀਆਂ ਲਈ SameSite ਤਰਕ ਵਰਗੀਆਂ ਬ੍ਰਾਊਜ਼ਰ ਸੁਰੱਖਿਆ ਨੀਤੀਆਂ ਹਨ। ਇੱਕ ਹੋਰ ਆਮ ਸੁਰੱਖਿਆ CORS ਪ੍ਰੀਫ਼ਲਾਈਟ (preflight) ਪ੍ਰਣਾਲੀ ਹੈ। ਇਹ ਪ੍ਰਣਾਲੀ ਉਹਨਾਂ ਅੰਤ-ਬਿੰਦੂਆਂ ਲਈ ਅਤਿ ਮਹੱਤਵਪੂਰਨ ਹੋਵੇਗੀ ਜੋ ਕਿਸੇ ਵੱਖਰੇ ਓਰਿਜਿਨ ਤੋਂ ਕਾਲ ਕੀਤੇ ਜਾਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਗਏ ਹਨ, ਪਰ ਇਹ ਉਹਨਾਂ ਅੰਤ-ਬਿੰਦੂਆਂ ਲਈ ਵੀ ਇੱਕ ਲਾਭਦਾਇਕ ਬੇਨਤੀ ਜਾਅਲਸਾਜ਼ੀ ਰੋਕਥਾਮ ਪ੍ਰਣਾਲੀ ਹੋ ਸਕਦੀ ਹੈ ਜੋ ਕਿਸੇ ਵੱਖਰੇ ਓਰਿਜਿਨ ਤੋਂ ਕਾਲ ਕੀਤੇ ਜਾਣ ਲਈ ਡਿਜ਼ਾਈਨ ਨਹੀਂ ਕੀਤੇ ਗਏ।

| # | Description | Level |
| :---: | :--- | :---: |
| **3.5.1** | Verify that, if the application does not rely on the CORS preflight mechanism to prevent disallowed cross-origin requests to use sensitive functionality, these requests are validated to ensure they originate from the application itself. This may be done by using and validating anti-forgery tokens or requiring extra HTTP header fields that are not CORS-safelisted request-header fields. This is to defend against browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF). | 1 |
| **3.5.2** | Verify that, if the application relies on the CORS preflight mechanism to prevent disallowed cross-origin use of sensitive functionality, it is not possible to call the functionality with a request which does not trigger a CORS-preflight request. This may require checking the values of the 'Origin' and 'Content-Type' request header fields or using an extra header field that is not a CORS-safelisted header-field. | 1 |
| **3.5.3** | Verify that HTTP requests to sensitive functionality use appropriate HTTP methods such as POST, PUT, PATCH, or DELETE, and not methods defined by the HTTP specification as "safe" such as HEAD, OPTIONS, or GET. Alternatively, strict validation of the Sec-Fetch-* request header fields can be used to ensure that the request did not originate from an inappropriate cross-origin call, a navigation request, or a resource load (such as an image source) where this is not expected. | 1 |
| **3.5.4** | Verify that separate applications are hosted on different hostnames to leverage the restrictions provided by same-origin policy, including how documents or scripts loaded by one origin can interact with resources from another origin and hostname-based restrictions on cookies. | 2 |
| **3.5.5** | Verify that messages received by the postMessage interface are discarded if the origin of the message is not trusted, or if the syntax of the message is invalid. | 2 |
| **3.5.6** | Verify that JSONP functionality is not enabled anywhere across the application to avoid Cross-Site Script Inclusion (XSSI) attacks. | 3 |
| **3.5.7** | Verify that data requiring authorization is not included in script resource responses, like JavaScript files, to prevent Cross-Site Script Inclusion (XSSI) attacks. | 3 |
| **3.5.8** | Verify that authenticated resources (such as images, videos, scripts, and other documents) can be loaded or embedded on behalf of the user only when intended. This can be accomplished by strict validation of the Sec-Fetch-* HTTP request header fields to ensure that the request did not originate from an inappropriate cross-origin call, or by setting a restrictive Cross-Origin-Resource-Policy HTTP response header field to instruct the browser to block returned content. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **3.5.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ ਐਪਲੀਕੇਸ਼ਨ ਸੰਵੇਦਨਸ਼ੀਲ ਕਾਰਜਸ਼ੀਲਤਾ ਵਰਤਣ ਵਾਲੀਆਂ ਅਣ-ਇਜਾਜ਼ਤਸ਼ੁਦਾ ਕਰਾਸ-ਓਰਿਜਿਨ ਬੇਨਤੀਆਂ ਨੂੰ ਰੋਕਣ ਲਈ CORS ਪ੍ਰੀਫ਼ਲਾਈਟ ਪ੍ਰਣਾਲੀ 'ਤੇ ਨਿਰਭਰ ਨਹੀਂ ਕਰਦੀ, ਤਾਂ ਇਹਨਾਂ ਬੇਨਤੀਆਂ ਨੂੰ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਪ੍ਰਮਾਣਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਕਿ ਉਹ ਐਪਲੀਕੇਸ਼ਨ ਤੋਂ ਹੀ ਉਤਪੰਨ ਹੁੰਦੀਆਂ ਹਨ। ਇਹ ਜਾਅਲਸਾਜ਼ੀ-ਰੋਕੂ ਟੋਕਨਾਂ ਨੂੰ ਵਰਤ ਕੇ ਅਤੇ ਪ੍ਰਮਾਣਿਤ ਕਰਕੇ ਜਾਂ ਅਜਿਹੇ ਵਾਧੂ HTTP ਹੈੱਡਰ ਖੇਤਰਾਂ ਦੀ ਲੋੜ ਰੱਖ ਕੇ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਜੋ CORS-safelisted ਬੇਨਤੀ-ਹੈੱਡਰ ਖੇਤਰ ਨਹੀਂ ਹਨ। ਇਹ ਬ੍ਰਾਊਜ਼ਰ-ਆਧਾਰਿਤ ਬੇਨਤੀ ਜਾਅਲਸਾਜ਼ੀ ਹਮਲਿਆਂ, ਜਿਨ੍ਹਾਂ ਨੂੰ ਆਮ ਤੌਰ 'ਤੇ ਕਰਾਸ-ਸਾਈਟ ਬੇਨਤੀ ਜਾਅਲਸਾਜ਼ੀ (CSRF) ਕਿਹਾ ਜਾਂਦਾ ਹੈ, ਤੋਂ ਬਚਾਅ ਲਈ ਹੈ। | 1 |
| **3.5.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ, ਜੇ ਐਪਲੀਕੇਸ਼ਨ ਸੰਵੇਦਨਸ਼ੀਲ ਕਾਰਜਸ਼ੀਲਤਾ ਦੀ ਅਣ-ਇਜਾਜ਼ਤਸ਼ੁਦਾ ਕਰਾਸ-ਓਰਿਜਿਨ ਵਰਤੋਂ ਨੂੰ ਰੋਕਣ ਲਈ CORS ਪ੍ਰੀਫ਼ਲਾਈਟ ਪ੍ਰਣਾਲੀ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ, ਤਾਂ ਅਜਿਹੀ ਬੇਨਤੀ ਨਾਲ ਕਾਰਜਸ਼ੀਲਤਾ ਨੂੰ ਕਾਲ ਕਰਨਾ ਸੰਭਵ ਨਹੀਂ ਹੈ ਜੋ CORS-ਪ੍ਰੀਫ਼ਲਾਈਟ ਬੇਨਤੀ ਨੂੰ ਟ੍ਰਿਗਰ ਨਹੀਂ ਕਰਦੀ। ਇਸ ਲਈ 'Origin' ਅਤੇ 'Content-Type' ਬੇਨਤੀ ਹੈੱਡਰ ਖੇਤਰਾਂ ਦੇ ਮੁੱਲਾਂ ਦੀ ਜਾਂਚ ਕਰਨ ਜਾਂ ਅਜਿਹੇ ਵਾਧੂ ਹੈੱਡਰ ਖੇਤਰ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ ਜੋ CORS-safelisted ਹੈੱਡਰ-ਖੇਤਰ ਨਹੀਂ ਹੈ। | 1 |
| **3.5.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੰਵੇਦਨਸ਼ੀਲ ਕਾਰਜਸ਼ੀਲਤਾ ਲਈ HTTP ਬੇਨਤੀਆਂ ਢੁਕਵੇਂ HTTP ਮੈਥਡ (method) ਜਿਵੇਂ ਕਿ POST, PUT, PATCH, ਜਾਂ DELETE ਵਰਤਦੀਆਂ ਹਨ, ਨਾ ਕਿ HTTP ਨਿਰਧਾਰਨ ਦੁਆਰਾ "ਸੁਰੱਖਿਅਤ" ਵਜੋਂ ਪਰਿਭਾਸ਼ਿਤ ਮੈਥਡ ਜਿਵੇਂ ਕਿ HEAD, OPTIONS, ਜਾਂ GET। ਵਿਕਲਪਕ ਤੌਰ 'ਤੇ, Sec-Fetch-* ਬੇਨਤੀ ਹੈੱਡਰ ਖੇਤਰਾਂ ਨੂੰ ਸਖ਼ਤੀ ਨਾਲ ਪ੍ਰਮਾਣਿਤ ਕਰਕੇ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਕਿ ਬੇਨਤੀ ਕਿਸੇ ਅਣਉਚਿਤ ਕਰਾਸ-ਓਰਿਜਿਨ ਕਾਲ, ਨੈਵੀਗੇਸ਼ਨ ਬੇਨਤੀ, ਜਾਂ ਸਰੋਤ ਲੋਡ (ਜਿਵੇਂ ਕਿ ਚਿੱਤਰ ਸਰੋਤ) ਤੋਂ ਉਤਪੰਨ ਨਹੀਂ ਹੋਈ ਜਿੱਥੇ ਇਸ ਦੀ ਉਮੀਦ ਨਹੀਂ ਹੈ। | 1 |
| **3.5.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਵੱਖਰੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵੱਖ-ਵੱਖ ਹੋਸਟਨੇਮਾਂ 'ਤੇ ਹੋਸਟ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ ਤਾਂ ਜੋ same-origin policy ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਪਾਬੰਦੀਆਂ ਦਾ ਲਾਭ ਲਿਆ ਜਾ ਸਕੇ, ਜਿਸ ਵਿੱਚ ਇਹ ਸ਼ਾਮਲ ਹੈ ਕਿ ਇੱਕ ਓਰਿਜਿਨ ਦੁਆਰਾ ਲੋਡ ਕੀਤੇ ਦਸਤਾਵੇਜ਼ ਜਾਂ ਸਕ੍ਰਿਪਟਾਂ ਕਿਸੇ ਹੋਰ ਓਰਿਜਿਨ ਦੇ ਸਰੋਤਾਂ ਨਾਲ ਕਿਵੇਂ ਆਪਸੀ ਕਿਰਿਆ ਕਰ ਸਕਦੀਆਂ ਹਨ ਅਤੇ ਕੁਕੀਆਂ 'ਤੇ ਹੋਸਟਨੇਮ-ਆਧਾਰਿਤ ਪਾਬੰਦੀਆਂ। | 2 |
| **3.5.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ postMessage ਇੰਟਰਫ਼ੇਸ ਦੁਆਰਾ ਪ੍ਰਾਪਤ ਕੀਤੇ ਸੁਨੇਹੇ ਰੱਦ ਕਰ ਦਿੱਤੇ ਜਾਂਦੇ ਹਨ ਜੇ ਸੁਨੇਹੇ ਦਾ ਓਰਿਜਿਨ ਭਰੋਸੇਯੋਗ ਨਹੀਂ ਹੈ, ਜਾਂ ਜੇ ਸੁਨੇਹੇ ਦਾ ਸਿੰਟੈਕਸ ਅਵੈਧ ਹੈ। | 2 |
| **3.5.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ Cross-Site Script Inclusion (XSSI) ਹਮਲਿਆਂ ਤੋਂ ਬਚਣ ਲਈ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਕਿਤੇ ਵੀ JSONP ਕਾਰਜਸ਼ੀਲਤਾ ਸਮਰੱਥ ਨਹੀਂ ਹੈ। | 3 |
| **3.5.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ Cross-Site Script Inclusion (XSSI) ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ, ਅਧਿਕਾਰੀਕਰਨ ਦੀ ਲੋੜ ਵਾਲਾ ਡਾਟਾ ਸਕ੍ਰਿਪਟ ਸਰੋਤ ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ, ਜਿਵੇਂ ਕਿ JavaScript ਫ਼ਾਈਲਾਂ, ਵਿੱਚ ਸ਼ਾਮਲ ਨਹੀਂ ਕੀਤਾ ਜਾਂਦਾ। | 3 |
| **3.5.8** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰਮਾਣੀਕ੍ਰਿਤ ਸਰੋਤ (ਜਿਵੇਂ ਕਿ ਚਿੱਤਰ, ਵੀਡੀਓ, ਸਕ੍ਰਿਪਟਾਂ, ਅਤੇ ਹੋਰ ਦਸਤਾਵੇਜ਼) ਉਪਭੋਗਤਾ ਦੀ ਤਰਫ਼ੋਂ ਕੇਵਲ ਉਦੋਂ ਹੀ ਲੋਡ ਜਾਂ ਏਮਬੈੱਡ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ ਜਦੋਂ ਅਜਿਹਾ ਇਰਾਦਾ ਹੋਵੇ। ਇਹ Sec-Fetch-* HTTP ਬੇਨਤੀ ਹੈੱਡਰ ਖੇਤਰਾਂ ਨੂੰ ਸਖ਼ਤੀ ਨਾਲ ਪ੍ਰਮਾਣਿਤ ਕਰਕੇ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕਿ ਬੇਨਤੀ ਕਿਸੇ ਅਣਉਚਿਤ ਕਰਾਸ-ਓਰਿਜਿਨ ਕਾਲ ਤੋਂ ਉਤਪੰਨ ਨਹੀਂ ਹੋਈ, ਜਾਂ ਬ੍ਰਾਊਜ਼ਰ ਨੂੰ ਵਾਪਸ ਕੀਤੀ ਸਮੱਗਰੀ ਨੂੰ ਰੋਕਣ ਦਾ ਨਿਰਦੇਸ਼ ਦੇਣ ਲਈ ਇੱਕ ਪ੍ਰਤਿਬੰਧਕ Cross-Origin-Resource-Policy HTTP ਪ੍ਰਤੀਕਿਰਿਆ ਹੈੱਡਰ ਖੇਤਰ ਸੈੱਟ ਕਰਕੇ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। | 3 |

## V3.6 External Resource Integrity
## V3.6 ਬਾਹਰੀ ਸਰੋਤ ਅਖੰਡਤਾ

This section provides guidance for the safe hosting of content on third-party sites.

ਇਹ ਭਾਗ ਤੀਜੀ-ਧਿਰ ਸਾਈਟਾਂ 'ਤੇ ਸਮੱਗਰੀ ਦੀ ਸੁਰੱਖਿਅਤ ਹੋਸਟਿੰਗ ਲਈ ਮਾਰਗਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **3.6.1** | Verify that client-side assets, such as JavaScript libraries, CSS, or web fonts, are only hosted externally (e.g., on a Content Delivery Network) if the resource is static and versioned and Subresource Integrity (SRI) is used to validate the integrity of the asset. If this is not possible, there should be a documented security decision to justify this for each resource. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **3.6.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਲਾਇੰਟ-ਸਾਈਡ ਸੰਪਤੀਆਂ (assets), ਜਿਵੇਂ ਕਿ JavaScript ਲਾਇਬ੍ਰੇਰੀਆਂ, CSS, ਜਾਂ ਵੈੱਬ ਫ਼ੌਂਟ, ਕੇਵਲ ਤਾਂ ਹੀ ਬਾਹਰੀ ਤੌਰ 'ਤੇ ਹੋਸਟ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ (ਜਿਵੇਂ ਕਿ, ਕਿਸੇ Content Delivery Network 'ਤੇ) ਜੇ ਸਰੋਤ ਸਥਿਰ ਅਤੇ ਸੰਸਕਰਣਬੱਧ ਹੈ ਅਤੇ ਸੰਪਤੀ ਦੀ ਅਖੰਡਤਾ (integrity) ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਨ ਲਈ Subresource Integrity (SRI) ਵਰਤੀ ਜਾਂਦੀ ਹੈ। ਜੇ ਇਹ ਸੰਭਵ ਨਹੀਂ ਹੈ, ਤਾਂ ਹਰੇਕ ਸਰੋਤ ਲਈ ਇਸ ਨੂੰ ਜਾਇਜ਼ ਠਹਿਰਾਉਣ ਵਾਲਾ ਇੱਕ ਦਸਤਾਵੇਜ਼ੀ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। | 3 |

## V3.7 Other Browser Security Considerations
## V3.7 ਹੋਰ ਬ੍ਰਾਊਜ਼ਰ ਸੁਰੱਖਿਆ ਵਿਚਾਰ

This section includes various other security controls and modern browser security features required for client-side browser security.

ਇਸ ਭਾਗ ਵਿੱਚ ਕਲਾਇੰਟ-ਸਾਈਡ ਬ੍ਰਾਊਜ਼ਰ ਸੁਰੱਖਿਆ ਲਈ ਲੋੜੀਂਦੇ ਵੱਖ-ਵੱਖ ਹੋਰ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਅਤੇ ਆਧੁਨਿਕ ਬ੍ਰਾਊਜ਼ਰ ਸੁਰੱਖਿਆ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਸ਼ਾਮਲ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **3.7.1** | Verify that the application only uses client-side technologies which are still supported and considered secure. Examples of technologies which do not meet this requirement include NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | 2 |
| **3.7.2** | Verify that the application will only automatically redirect the user to a different hostname or domain (which is not controlled by the application) where the destination appears on an allowlist. | 2 |
| **3.7.3** | Verify that the application shows a notification when the user is being redirected to a URL outside of the application's control, with an option to cancel the navigation. | 3 |
| **3.7.4** | Verify that the application's top-level domain (e.g., site.tld) is added to the public preload list for HTTP Strict Transport Security (HSTS). This ensures that the use of TLS for the application is built directly into the main browsers, rather than relying only on the Strict-Transport-Security response header field. | 3 |
| **3.7.5** | Verify that the application behaves as documented (such as warning the user or blocking access) if the browser used to access the application does not support the expected security features. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **3.7.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਕੇਵਲ ਉਹੀ ਕਲਾਇੰਟ-ਸਾਈਡ ਤਕਨਾਲੋਜੀਆਂ ਵਰਤਦੀ ਹੈ ਜੋ ਅਜੇ ਵੀ ਸਮਰਥਿਤ ਹਨ ਅਤੇ ਸੁਰੱਖਿਅਤ ਮੰਨੀਆਂ ਜਾਂਦੀਆਂ ਹਨ। ਇਸ ਲੋੜ ਨੂੰ ਪੂਰਾ ਨਾ ਕਰਨ ਵਾਲੀਆਂ ਤਕਨਾਲੋਜੀਆਂ ਦੀਆਂ ਉਦਾਹਰਨਾਂ ਵਿੱਚ NSAPI ਪਲੱਗਇਨ, Flash, Shockwave, ActiveX, Silverlight, NACL, ਜਾਂ ਕਲਾਇੰਟ-ਸਾਈਡ Java ਐਪਲੈੱਟ ਸ਼ਾਮਲ ਹਨ। | 2 |
| **3.7.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਉਪਭੋਗਤਾ ਨੂੰ ਕਿਸੇ ਵੱਖਰੇ ਹੋਸਟਨੇਮ ਜਾਂ ਡੋਮੇਨ (ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਨਿਯੰਤਰਿਤ ਨਹੀਂ ਹੈ) ਵੱਲ ਕੇਵਲ ਉਦੋਂ ਹੀ ਸਵੈਚਾਲਿਤ ਤੌਰ 'ਤੇ ਰੀਡਾਇਰੈਕਟ ਕਰੇਗੀ ਜਦੋਂ ਮੰਜ਼ਿਲ ਕਿਸੇ allowlist ਵਿੱਚ ਦਰਜ ਹੋਵੇ। | 2 |
| **3.7.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਦੋਂ ਉਪਭੋਗਤਾ ਨੂੰ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਨਿਯੰਤਰਣ ਤੋਂ ਬਾਹਰ ਕਿਸੇ URL ਵੱਲ ਰੀਡਾਇਰੈਕਟ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੋਵੇ ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ ਇੱਕ ਸੂਚਨਾ ਦਿਖਾਉਂਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਨੈਵੀਗੇਸ਼ਨ ਰੱਦ ਕਰਨ ਦਾ ਵਿਕਲਪ ਹੁੰਦਾ ਹੈ। | 3 |
| **3.7.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਸਿਖਰ-ਪੱਧਰੀ ਡੋਮੇਨ (ਜਿਵੇਂ ਕਿ, site.tld) HTTP Strict Transport Security (HSTS) ਲਈ ਜਨਤਕ ਪ੍ਰੀਲੋਡ ਸੂਚੀ ਵਿੱਚ ਜੋੜਿਆ ਗਿਆ ਹੈ। ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਲਈ TLS ਦੀ ਵਰਤੋਂ ਕੇਵਲ Strict-Transport-Security ਪ੍ਰਤੀਕਿਰਿਆ ਹੈੱਡਰ ਖੇਤਰ 'ਤੇ ਨਿਰਭਰ ਰਹਿਣ ਦੀ ਬਜਾਏ ਸਿੱਧੇ ਮੁੱਖ ਬ੍ਰਾਊਜ਼ਰਾਂ ਵਿੱਚ ਹੀ ਬਣਾਈ ਗਈ ਹੈ। | 3 |
| **3.7.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜੇ ਐਪਲੀਕੇਸ਼ਨ ਤੱਕ ਪਹੁੰਚ ਕਰਨ ਲਈ ਵਰਤਿਆ ਗਿਆ ਬ੍ਰਾਊਜ਼ਰ ਉਮੀਦ ਕੀਤੀਆਂ ਸੁਰੱਖਿਆ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦਾ ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਅਨੁਸਾਰ ਵਿਹਾਰ ਕਰਦੀ ਹੈ (ਜਿਵੇਂ ਕਿ ਉਪਭੋਗਤਾ ਨੂੰ ਚੇਤਾਵਨੀ ਦੇਣਾ ਜਾਂ ਪਹੁੰਚ ਨੂੰ ਰੋਕਣਾ)। | 3 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
* [OWASP DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)
