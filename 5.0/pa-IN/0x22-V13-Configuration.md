<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x22-V13-Configuration.md -->
<!-- Translator: GeeksikhSecurity -->

# V13 Configuration
# V13 ਸੰਰਚਨਾ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

The application's default configuration must be secure for use on the Internet.

ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਡਿਫ਼ਾਲਟ ਸੰਰਚਨਾ (configuration) ਇੰਟਰਨੈੱਟ 'ਤੇ ਵਰਤੋਂ ਲਈ ਸੁਰੱਖਿਅਤ ਹੋਣੀ ਲਾਜ਼ਮੀ ਹੈ।

This chapter provides guidance on the various configurations necessary to achieve this, including those applied during development, build, and deployment.

ਇਹ ਅਧਿਆਇ ਇਸ ਨੂੰ ਹਾਸਲ ਕਰਨ ਲਈ ਲੋੜੀਂਦੀਆਂ ਵੱਖ-ਵੱਖ ਸੰਰਚਨਾਵਾਂ ਬਾਰੇ ਮਾਰਗਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਵਿਕਾਸ, ਬਿਲਡ (build), ਅਤੇ ਤਾਇਨਾਤੀ (deployment) ਦੌਰਾਨ ਲਾਗੂ ਕੀਤੀਆਂ ਜਾਣ ਵਾਲੀਆਂ ਸੰਰਚਨਾਵਾਂ ਵੀ ਸ਼ਾਮਲ ਹਨ।

Topics covered include preventing data leakage, securely managing communication between components, and protecting secrets.

ਸ਼ਾਮਲ ਕੀਤੇ ਗਏ ਵਿਸ਼ਿਆਂ ਵਿੱਚ ਡਾਟਾ ਲੀਕੇਜ ਨੂੰ ਰੋਕਣਾ, ਘਟਕਾਂ (components) ਦੇ ਵਿਚਕਾਰ ਸੰਚਾਰ ਦਾ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਪ੍ਰਬੰਧਨ ਕਰਨਾ, ਅਤੇ ਭੇਦਾਂ (secrets) ਦੀ ਰੱਖਿਆ ਕਰਨਾ ਸ਼ਾਮਲ ਹੈ।

## V13.1 Configuration Documentation
## V13.1 ਸੰਰਚਨਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

This section outlines documentation requirements for how the application communicates with internal and external services, as well as techniques to prevent loss of availability due to service inaccessibility. It also addresses documentation related to secrets.

ਇਹ ਭਾਗ ਇਸ ਬਾਰੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲੋੜਾਂ ਦੀ ਰੂਪਰੇਖਾ ਦਿੰਦਾ ਹੈ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਅੰਦਰੂਨੀ ਅਤੇ ਬਾਹਰੀ ਸੇਵਾਵਾਂ ਨਾਲ ਕਿਵੇਂ ਸੰਚਾਰ ਕਰਦੀ ਹੈ, ਨਾਲ ਹੀ ਉਹਨਾਂ ਤਕਨੀਕਾਂ ਦੀ ਵੀ ਜੋ ਸੇਵਾ ਤੱਕ ਪਹੁੰਚ ਨਾ ਹੋ ਸਕਣ ਕਾਰਨ ਉਪਲਬਧਤਾ (availability) ਦੇ ਨੁਕਸਾਨ ਨੂੰ ਰੋਕਦੀਆਂ ਹਨ। ਇਹ ਭੇਦਾਂ ਨਾਲ ਸੰਬੰਧਿਤ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਨੂੰ ਵੀ ਸੰਬੋਧਿਤ ਕਰਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **13.1.1** | Verify that all communication needs for the application are documented. This must include external services which the application relies upon and cases where an end user might be able to provide an external location to which the application will then connect. | 2 |
| **13.1.2** | Verify that for each service the application uses, the documentation defines the maximum number of concurrent connections (e.g., connection pool limits) and how the application behaves when that limit is reached, including any fallback or recovery mechanisms, to prevent denial of service conditions. | 3 |
| **13.1.3** | Verify that the application documentation defines resource‑management strategies for every external system or service it uses (e.g., databases, file handles, threads, HTTP connections). This should include resource‑release procedures, timeout settings, failure handling, and where retry logic is implemented, specifying retry limits, delays, and back‑off algorithms. For synchronous HTTP request–response operations it should mandate short timeouts and either disable retries or strictly limit retries to prevent cascading delays and resource exhaustion. | 3 |
| **13.1.4** | Verify that the application's documentation defines the secrets that are critical for the security of the application and a schedule for rotating them, based on the organization's threat model and business requirements. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **13.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦੀਆਂ ਸਾਰੀਆਂ ਸੰਚਾਰ ਲੋੜਾਂ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਵਿੱਚ ਦਰਜ ਹਨ। ਇਸ ਵਿੱਚ ਉਹ ਬਾਹਰੀ ਸੇਵਾਵਾਂ ਸ਼ਾਮਲ ਹੋਣੀਆਂ ਲਾਜ਼ਮੀ ਹਨ ਜਿਨ੍ਹਾਂ 'ਤੇ ਐਪਲੀਕੇਸ਼ਨ ਨਿਰਭਰ ਕਰਦੀ ਹੈ, ਅਤੇ ਉਹ ਮਾਮਲੇ ਜਿੱਥੇ ਕੋਈ ਅੰਤਮ ਉਪਭੋਗਤਾ ਇੱਕ ਅਜਿਹਾ ਬਾਹਰੀ ਟਿਕਾਣਾ ਪ੍ਰਦਾਨ ਕਰ ਸਕਦਾ ਹੈ ਜਿਸ ਨਾਲ ਐਪਲੀਕੇਸ਼ਨ ਫਿਰ ਸੰਪਰਕ ਕਰੇਗੀ। | 2 |
| **13.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਵਰਤੀ ਜਾਂਦੀ ਹਰੇਕ ਸੇਵਾ ਲਈ, ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਸਮਕਾਲੀ ਸੰਪਰਕਾਂ (concurrent connections) ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਗਿਣਤੀ (ਜਿਵੇਂ, ਕਨੈਕਸ਼ਨ ਪੂਲ ਸੀਮਾਵਾਂ) ਅਤੇ ਇਹ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਕਿ ਉਹ ਸੀਮਾ ਪਹੁੰਚਣ 'ਤੇ ਐਪਲੀਕੇਸ਼ਨ ਕਿਵੇਂ ਵਿਹਾਰ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਕੋਈ ਵੀ ਫ਼ਾਲਬੈਕ (fallback) ਜਾਂ ਰਿਕਵਰੀ ਪ੍ਰਣਾਲੀਆਂ ਸ਼ਾਮਲ ਹਨ, ਤਾਂ ਜੋ ਸੇਵਾ-ਇਨਕਾਰ (denial of service) ਸਥਿਤੀਆਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 3 |
| **13.1.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਇਸ ਦੁਆਰਾ ਵਰਤੇ ਜਾਂਦੇ ਹਰੇਕ ਬਾਹਰੀ ਸਿਸਟਮ ਜਾਂ ਸੇਵਾ (ਜਿਵੇਂ, ਡਾਟਾਬੇਸ, ਫ਼ਾਈਲ ਹੈਂਡਲ, ਥ੍ਰੈੱਡ, HTTP ਸੰਪਰਕ) ਲਈ ਸਰੋਤ-ਪ੍ਰਬੰਧਨ ਰਣਨੀਤੀਆਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਸਰੋਤ-ਰਿਹਾਈ ਪ੍ਰਕਿਰਿਆਵਾਂ, ਸਮਾਂ-ਸੀਮਾ (timeout) ਸੈਟਿੰਗਾਂ, ਅਸਫਲਤਾ ਸੰਭਾਲ, ਅਤੇ ਜਿੱਥੇ ਮੁੜ-ਕੋਸ਼ਿਸ਼ (retry) ਤਰਕ ਲਾਗੂ ਕੀਤਾ ਗਿਆ ਹੈ, ਉੱਥੇ ਮੁੜ-ਕੋਸ਼ਿਸ਼ ਸੀਮਾਵਾਂ, ਦੇਰੀਆਂ, ਅਤੇ ਬੈਕ-ਆਫ਼ (back-off) ਐਲਗੋਰਿਦਮਾਂ ਦਾ ਨਿਰਧਾਰਨ ਸ਼ਾਮਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਸਿੰਕ੍ਰੋਨਸ (synchronous) HTTP ਬੇਨਤੀ-ਜਵਾਬ ਕਾਰਜਾਂ ਲਈ ਇਸ ਨੂੰ ਛੋਟੀਆਂ ਸਮਾਂ-ਸੀਮਾਵਾਂ ਲਾਜ਼ਮੀ ਕਰਨੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ ਅਤੇ ਲੜੀਵਾਰ (cascading) ਦੇਰੀਆਂ ਅਤੇ ਸਰੋਤ ਖ਼ਤਮ ਹੋ ਜਾਣ ਨੂੰ ਰੋਕਣ ਲਈ ਜਾਂ ਤਾਂ ਮੁੜ-ਕੋਸ਼ਿਸ਼ਾਂ ਨੂੰ ਅਸਮਰੱਥ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਜਾਂ ਮੁੜ-ਕੋਸ਼ਿਸ਼ਾਂ ਨੂੰ ਸਖ਼ਤੀ ਨਾਲ ਸੀਮਤ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ। | 3 |
| **13.1.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਉਹਨਾਂ ਭੇਦਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਸੁਰੱਖਿਆ ਲਈ ਅਤਿ ਮਹੱਤਵਪੂਰਨ ਹਨ, ਅਤੇ ਸੰਸਥਾ ਦੇ ਖ਼ਤਰਾ ਮਾਡਲ (threat model) ਅਤੇ ਕਾਰੋਬਾਰੀ ਲੋੜਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਉਹਨਾਂ ਨੂੰ ਰੋਟੇਟ ਕਰਨ ਦੀ ਇੱਕ ਸਮਾਂ-ਸਾਰਣੀ ਵੀ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ। | 3 |

## V13.2 Backend Communication Configuration
## V13.2 ਬੈਕਐਂਡ ਸੰਚਾਰ ਸੰਰਚਨਾ

Applications interact with multiple services, including APIs, databases, or other components. These may be considered internal to the application but not included in the application's standard access control mechanisms, or they may be entirely external. In either case, it is necessary to configure the application to interact securely with these components and, if required, protect that configuration.

ਐਪਲੀਕੇਸ਼ਨਾਂ ਕਈ ਸੇਵਾਵਾਂ ਨਾਲ ਆਪਸੀ ਤਾਲਮੇਲ ਕਰਦੀਆਂ ਹਨ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ API, ਡਾਟਾਬੇਸ, ਜਾਂ ਹੋਰ ਘਟਕ ਸ਼ਾਮਲ ਹਨ। ਇਹਨਾਂ ਨੂੰ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਅੰਦਰੂਨੀ ਮੰਨਿਆ ਜਾ ਸਕਦਾ ਹੈ ਪਰ ਇਹ ਐਪਲੀਕੇਸ਼ਨ ਦੀਆਂ ਮਿਆਰੀ ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਪ੍ਰਣਾਲੀਆਂ ਵਿੱਚ ਸ਼ਾਮਲ ਨਹੀਂ ਹੁੰਦੇ, ਜਾਂ ਇਹ ਪੂਰੀ ਤਰ੍ਹਾਂ ਬਾਹਰੀ ਹੋ ਸਕਦੇ ਹਨ। ਦੋਵਾਂ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਇਹਨਾਂ ਘਟਕਾਂ ਨਾਲ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਆਪਸੀ ਤਾਲਮੇਲ ਕਰਨ ਲਈ ਸੰਰਚਿਤ ਕਰਨਾ ਅਤੇ, ਜੇ ਲੋੜ ਹੋਵੇ, ਉਸ ਸੰਰਚਨਾ ਦੀ ਰੱਖਿਆ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ।

Note: The "Secure Communication" chapter provides guidance for encryption in transit.

ਨੋਟ: "ਸੁਰੱਖਿਅਤ ਸੰਚਾਰ" (Secure Communication) ਅਧਿਆਇ ਪ੍ਰਸਾਰਣ ਦੌਰਾਨ ਏਨਕ੍ਰਿਪਸ਼ਨ (encryption in transit) ਲਈ ਮਾਰਗਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **13.2.1** | Verify that communications between backend application components that don't support the application's standard user session mechanism, including APIs, middleware, and data layers, are authenticated. Authentication must use individual service accounts, short-term tokens, or certificate-based authentication and not unchanging credentials such as passwords, API keys, or shared accounts with privileged access. | 2 |
| **13.2.2** | Verify that communications between backend application components, including local or operating system services, APIs, middleware, and data layers, are performed with accounts assigned the least necessary privileges. | 2 |
| **13.2.3** | Verify that if a credential has to be used for service authentication, the credential being used by the consumer is not a default credential (e.g., root/root or admin/admin). | 2 |
| **13.2.4** | Verify that an allowlist is used to define the external resources or systems with which the application is permitted to communicate (e.g., for outbound requests, data loads, or file access). This allowlist can be implemented at the application layer, web server, firewall, or a combination of different layers. | 2 |
| **13.2.5** | Verify that the web or application server is configured with an allowlist of resources or systems to which the server can send requests or load data or files from. | 2 |
| **13.2.6** | Verify that where the application connects to separate services, it follows the documented configuration for each connection, such as maximum parallel connections, behavior when maximum allowed connections is reached, connection timeouts, and retry strategies. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **13.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਹਨਾਂ ਬੈਕਐਂਡ ਐਪਲੀਕੇਸ਼ਨ ਘਟਕਾਂ ਦੇ ਵਿਚਕਾਰ ਸੰਚਾਰਾਂ ਦਾ ਪ੍ਰਮਾਣੀਕਰਨ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਮਿਆਰੀ ਉਪਭੋਗਤਾ ਸੈਸ਼ਨ ਪ੍ਰਣਾਲੀ ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦੇ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ API, ਮਿਡਲਵੇਅਰ, ਅਤੇ ਡਾਟਾ ਪਰਤਾਂ ਸ਼ਾਮਲ ਹਨ। ਪ੍ਰਮਾਣੀਕਰਨ ਲਈ ਵਿਅਕਤੀਗਤ ਸੇਵਾ ਖਾਤਿਆਂ (service accounts), ਥੋੜ੍ਹੇ ਸਮੇਂ ਦੇ ਟੋਕਨਾਂ, ਜਾਂ ਸਰਟੀਫ਼ਿਕੇਟ-ਆਧਾਰਿਤ ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ, ਨਾ ਕਿ ਨਾ ਬਦਲਣ ਵਾਲੇ ਪ੍ਰਮਾਣ-ਪੱਤਰਾਂ ਦੀ, ਜਿਵੇਂ ਕਿ ਪਾਸਵਰਡ, API ਕੁੰਜੀਆਂ, ਜਾਂ ਵਿਸ਼ੇਸ਼-ਅਧਿਕਾਰ ਪ੍ਰਾਪਤ ਪਹੁੰਚ ਵਾਲੇ ਸਾਂਝੇ ਖਾਤੇ। | 2 |
| **13.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਬੈਕਐਂਡ ਐਪਲੀਕੇਸ਼ਨ ਘਟਕਾਂ ਦੇ ਵਿਚਕਾਰ ਸੰਚਾਰ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਸਥਾਨਕ ਜਾਂ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਸੇਵਾਵਾਂ, API, ਮਿਡਲਵੇਅਰ, ਅਤੇ ਡਾਟਾ ਪਰਤਾਂ ਸ਼ਾਮਲ ਹਨ, ਅਜਿਹੇ ਖਾਤਿਆਂ ਨਾਲ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਘੱਟੋ-ਘੱਟ ਲੋੜੀਂਦੇ ਅਧਿਕਾਰ ਸੌਂਪੇ ਗਏ ਹਨ। | 2 |
| **13.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜੇ ਸੇਵਾ ਪ੍ਰਮਾਣੀਕਰਨ ਲਈ ਕੋਈ ਪ੍ਰਮਾਣ-ਪੱਤਰ ਵਰਤਣਾ ਪਵੇ, ਤਾਂ ਖਪਤਕਾਰ ਦੁਆਰਾ ਵਰਤਿਆ ਜਾ ਰਿਹਾ ਪ੍ਰਮਾਣ-ਪੱਤਰ ਇੱਕ ਡਿਫ਼ਾਲਟ ਪ੍ਰਮਾਣ-ਪੱਤਰ (default credential) ਨਹੀਂ ਹੈ (ਜਿਵੇਂ, root/root ਜਾਂ admin/admin)। | 2 |
| **13.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਉਹਨਾਂ ਬਾਹਰੀ ਸਰੋਤਾਂ ਜਾਂ ਸਿਸਟਮਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਲਈ ਇੱਕ allowlist ਵਰਤੀ ਜਾਂਦੀ ਹੈ ਜਿਨ੍ਹਾਂ ਨਾਲ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਸੰਚਾਰ ਕਰਨ ਦੀ ਇਜਾਜ਼ਤ ਹੈ (ਜਿਵੇਂ, ਬਾਹਰ-ਜਾਣ ਵਾਲੀਆਂ ਬੇਨਤੀਆਂ, ਡਾਟਾ ਲੋਡ, ਜਾਂ ਫ਼ਾਈਲ ਪਹੁੰਚ ਲਈ)। ਇਹ allowlist ਐਪਲੀਕੇਸ਼ਨ ਪਰਤ, ਵੈੱਬ ਸਰਵਰ, ਫ਼ਾਇਰਵਾਲ, ਜਾਂ ਵੱਖ-ਵੱਖ ਪਰਤਾਂ ਦੇ ਸੁਮੇਲ 'ਤੇ ਲਾਗੂ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। | 2 |
| **13.2.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਵੈੱਬ ਜਾਂ ਐਪਲੀਕੇਸ਼ਨ ਸਰਵਰ ਉਹਨਾਂ ਸਰੋਤਾਂ ਜਾਂ ਸਿਸਟਮਾਂ ਦੀ ਇੱਕ allowlist ਨਾਲ ਸੰਰਚਿਤ ਕੀਤਾ ਗਿਆ ਹੈ ਜਿਨ੍ਹਾਂ ਨੂੰ ਸਰਵਰ ਬੇਨਤੀਆਂ ਭੇਜ ਸਕਦਾ ਹੈ ਜਾਂ ਜਿਨ੍ਹਾਂ ਤੋਂ ਡਾਟਾ ਜਾਂ ਫ਼ਾਈਲਾਂ ਲੋਡ ਕਰ ਸਕਦਾ ਹੈ। | 2 |
| **13.2.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਿੱਥੇ ਐਪਲੀਕੇਸ਼ਨ ਵੱਖਰੀਆਂ ਸੇਵਾਵਾਂ ਨਾਲ ਸੰਪਰਕ ਕਰਦੀ ਹੈ, ਉੱਥੇ ਇਹ ਹਰੇਕ ਸੰਪਰਕ ਲਈ ਦਸਤਾਵੇਜ਼ੀ ਸੰਰਚਨਾ ਦੀ ਪਾਲਣਾ ਕਰਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਵੱਧ ਤੋਂ ਵੱਧ ਸਮਾਨਾਂਤਰ ਸੰਪਰਕ, ਵੱਧ ਤੋਂ ਵੱਧ ਇਜਾਜ਼ਤ-ਪ੍ਰਾਪਤ ਸੰਪਰਕਾਂ ਦੀ ਗਿਣਤੀ ਪਹੁੰਚਣ 'ਤੇ ਵਿਹਾਰ, ਸੰਪਰਕ ਸਮਾਂ-ਸੀਮਾਵਾਂ, ਅਤੇ ਮੁੜ-ਕੋਸ਼ਿਸ਼ ਰਣਨੀਤੀਆਂ। | 3 |

## V13.3 Secret Management
## V13.3 ਭੇਦ ਪ੍ਰਬੰਧਨ

Secret management is an essential configuration task to ensure the protection of data used in the application. Specific requirements for cryptography can be found in the "Cryptography" chapter, but this section focuses on the management and handling aspects of secrets.

ਭੇਦ ਪ੍ਰਬੰਧਨ (secret management) ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਵਰਤੇ ਜਾਂਦੇ ਡਾਟੇ ਦੀ ਰੱਖਿਆ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਇੱਕ ਜ਼ਰੂਰੀ ਸੰਰਚਨਾ ਕਾਰਜ ਹੈ। ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ ਲਈ ਖ਼ਾਸ ਲੋੜਾਂ "ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ" (Cryptography) ਅਧਿਆਇ ਵਿੱਚ ਮਿਲ ਸਕਦੀਆਂ ਹਨ, ਪਰ ਇਹ ਭਾਗ ਭੇਦਾਂ ਦੇ ਪ੍ਰਬੰਧਨ ਅਤੇ ਸੰਭਾਲ ਦੇ ਪਹਿਲੂਆਂ 'ਤੇ ਕੇਂਦ੍ਰਿਤ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **13.3.1** | Verify that a secrets management solution, such as a key vault, is used to securely create, store, control access to, and destroy backend secrets. These could include passwords, key material, integrations with databases and third-party systems, keys and seeds for time-based tokens, other internal secrets, and API keys. Secrets must not be included in application source code or included in build artifacts. For an L3 application, this must involve a hardware-backed solution such as an HSM. | 2 |
| **13.3.2** | Verify that access to secret assets adheres to the principle of least privilege. | 2 |
| **13.3.3** | Verify that all cryptographic operations are performed using an isolated security module (such as a vault or hardware security module) to securely manage and protect key material from exposure outside of the security module. | 3 |
| **13.3.4** | Verify that secrets are configured to expire and be rotated based on the application's documentation. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **13.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਬੈਕਐਂਡ ਭੇਦਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਬਣਾਉਣ, ਸਟੋਰ ਕਰਨ, ਉਹਨਾਂ ਤੱਕ ਪਹੁੰਚ ਨਿਯੰਤਰਿਤ ਕਰਨ, ਅਤੇ ਨਸ਼ਟ ਕਰਨ ਲਈ ਇੱਕ ਭੇਦ ਪ੍ਰਬੰਧਨ ਹੱਲ, ਜਿਵੇਂ ਕਿ ਕੁੰਜੀ ਵਾਲਟ (key vault), ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਇਹਨਾਂ ਵਿੱਚ ਪਾਸਵਰਡ, key material, ਡਾਟਾਬੇਸਾਂ ਅਤੇ ਤੀਜੀ-ਧਿਰ ਸਿਸਟਮਾਂ ਨਾਲ ਏਕੀਕਰਨ, ਸਮਾਂ-ਆਧਾਰਿਤ ਟੋਕਨਾਂ ਲਈ ਕੁੰਜੀਆਂ ਅਤੇ ਸੀਡ, ਹੋਰ ਅੰਦਰੂਨੀ ਭੇਦ, ਅਤੇ API ਕੁੰਜੀਆਂ ਸ਼ਾਮਲ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਭੇਦਾਂ ਨੂੰ ਐਪਲੀਕੇਸ਼ਨ ਸਰੋਤ ਕੋਡ ਵਿੱਚ ਜਾਂ ਬਿਲਡ ਆਰਟੀਫ਼ੈਕਟਾਂ (build artifacts) ਵਿੱਚ ਸ਼ਾਮਲ ਨਹੀਂ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ। L3 ਐਪਲੀਕੇਸ਼ਨ ਲਈ, ਇਸ ਵਿੱਚ ਇੱਕ ਹਾਰਡਵੇਅਰ-ਸਮਰਥਿਤ ਹੱਲ, ਜਿਵੇਂ ਕਿ HSM, ਸ਼ਾਮਲ ਹੋਣਾ ਲਾਜ਼ਮੀ ਹੈ। | 2 |
| **13.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਭੇਦ ਸੰਪਤੀਆਂ (secret assets) ਤੱਕ ਪਹੁੰਚ ਘੱਟੋ-ਘੱਟ ਅਧਿਕਾਰ ਦੇ ਸਿਧਾਂਤ ਦੀ ਪਾਲਣਾ ਕਰਦੀ ਹੈ। | 2 |
| **13.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੀਆਂ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਕਾਰਵਾਈਆਂ ਇੱਕ ਅਲੱਗ-ਥਲੱਗ ਸੁਰੱਖਿਆ ਮਾਡਿਊਲ (ਜਿਵੇਂ ਕਿ ਵਾਲਟ ਜਾਂ ਹਾਰਡਵੇਅਰ ਸੁਰੱਖਿਆ ਮਾਡਿਊਲ) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ ਤਾਂ ਜੋ key material ਦਾ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਪ੍ਰਬੰਧਨ ਕੀਤਾ ਜਾ ਸਕੇ ਅਤੇ ਇਸ ਨੂੰ ਸੁਰੱਖਿਆ ਮਾਡਿਊਲ ਤੋਂ ਬਾਹਰ ਉਜਾਗਰ ਹੋਣ ਤੋਂ ਬਚਾਇਆ ਜਾ ਸਕੇ। | 3 |
| **13.3.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਭੇਦਾਂ ਨੂੰ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਦੇ ਆਧਾਰ 'ਤੇ ਮਿਆਦ ਪੁੱਗਣ ਅਤੇ ਰੋਟੇਟ ਕੀਤੇ ਜਾਣ ਲਈ ਸੰਰਚਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। | 3 |

## V13.4 Unintended Information Leakage
## V13.4 ਅਣਇੱਛਤ ਜਾਣਕਾਰੀ ਲੀਕੇਜ

Production configurations should be hardened to avoid disclosing unnecessary data. Many of these issues are rarely rated as significant risks but are often chained with other vulnerabilities. If these issues are not present by default, it raises the bar for attacking an application.

ਪ੍ਰੋਡਕਸ਼ਨ ਸੰਰਚਨਾਵਾਂ ਨੂੰ ਬੇਲੋੜੇ ਡਾਟੇ ਦੇ ਖੁਲਾਸੇ ਤੋਂ ਬਚਣ ਲਈ ਸਖ਼ਤ (hardened) ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਇਹਨਾਂ ਵਿੱਚੋਂ ਬਹੁਤ ਸਾਰੇ ਮੁੱਦਿਆਂ ਨੂੰ ਘੱਟ ਹੀ ਮਹੱਤਵਪੂਰਨ ਜੋਖਮਾਂ ਵਜੋਂ ਦਰਜਾ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ, ਪਰ ਇਹ ਅਕਸਰ ਹੋਰ ਕਮਜ਼ੋਰੀਆਂ ਨਾਲ ਜੋੜ ਕੇ (chained) ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਜੇ ਇਹ ਮੁੱਦੇ ਡਿਫ਼ਾਲਟ ਤੌਰ 'ਤੇ ਮੌਜੂਦ ਨਾ ਹੋਣ, ਤਾਂ ਇਹ ਕਿਸੇ ਐਪਲੀਕੇਸ਼ਨ 'ਤੇ ਹਮਲਾ ਕਰਨ ਲਈ ਰੁਕਾਵਟ ਨੂੰ ਉੱਚਾ ਕਰ ਦਿੰਦਾ ਹੈ (raises the bar)।

For example, hiding the version of server-side components does not eliminate the need to patch all components, and disabling folder listing does not remove the need to use authorization controls or keep files away from the public folder, but it raises the bar.

ਉਦਾਹਰਨ ਲਈ, ਸਰਵਰ-ਪੱਖੀ ਘਟਕਾਂ ਦਾ ਸੰਸਕਰਣ ਲੁਕਾਉਣਾ ਸਾਰੇ ਘਟਕਾਂ ਨੂੰ ਪੈਚ ਕਰਨ ਦੀ ਲੋੜ ਨੂੰ ਖ਼ਤਮ ਨਹੀਂ ਕਰਦਾ, ਅਤੇ ਫ਼ੋਲਡਰ ਸੂਚੀਕਰਨ (folder listing) ਨੂੰ ਅਸਮਰੱਥ ਕਰਨਾ ਅਧਿਕਾਰੀਕਰਨ ਨਿਯੰਤਰਣ ਵਰਤਣ ਜਾਂ ਫ਼ਾਈਲਾਂ ਨੂੰ ਜਨਤਕ ਫ਼ੋਲਡਰ ਤੋਂ ਦੂਰ ਰੱਖਣ ਦੀ ਲੋੜ ਨੂੰ ਨਹੀਂ ਹਟਾਉਂਦਾ, ਪਰ ਇਹ ਰੁਕਾਵਟ ਨੂੰ ਉੱਚਾ ਕਰਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **13.4.1** | Verify that the application is deployed either without any source control metadata, including the .git or .svn folders, or in a way that these folders are inaccessible both externally and to the application itself. | 1 |
| **13.4.2** | Verify that debug modes are disabled for all components in production environments to prevent exposure of debugging features and information leakage. | 2 |
| **13.4.3** | Verify that web servers do not expose directory listings to clients unless explicitly intended. | 2 |
| **13.4.4** | Verify that using the HTTP TRACE method is not supported in production environments, to avoid potential information leakage. | 2 |
| **13.4.5** | Verify that documentation (such as for internal APIs) and monitoring endpoints are not exposed unless explicitly intended. | 2 |
| **13.4.6** | Verify that the application does not expose detailed version information of backend components. | 3 |
| **13.4.7** | Verify that the web tier is configured to only serve files with specific file extensions to prevent unintentional information, configuration, and source code leakage. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **13.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ ਤਾਂ ਬਿਨਾਂ ਕਿਸੇ ਸਰੋਤ ਨਿਯੰਤਰਣ (source control) ਮੈਟਾਡਾਟੇ ਦੇ, ਜਿਸ ਵਿੱਚ .git ਜਾਂ .svn ਫ਼ੋਲਡਰ ਸ਼ਾਮਲ ਹਨ, ਤਾਇਨਾਤ ਕੀਤੀ ਗਈ ਹੈ, ਜਾਂ ਇਸ ਤਰੀਕੇ ਨਾਲ ਕਿ ਇਹ ਫ਼ੋਲਡਰ ਬਾਹਰੀ ਤੌਰ 'ਤੇ ਅਤੇ ਖ਼ੁਦ ਐਪਲੀਕੇਸ਼ਨ ਲਈ, ਦੋਵਾਂ ਲਈ ਪਹੁੰਚਯੋਗ ਨਹੀਂ ਹਨ। | 1 |
| **13.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰੋਡਕਸ਼ਨ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਸਾਰੇ ਘਟਕਾਂ ਲਈ ਡੀਬੱਗ (debug) ਮੋਡ ਅਸਮਰੱਥ ਹਨ ਤਾਂ ਜੋ ਡੀਬੱਗਿੰਗ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੇ ਉਜਾਗਰ ਹੋਣ ਅਤੇ ਜਾਣਕਾਰੀ ਲੀਕੇਜ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 2 |
| **13.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਵੈੱਬ ਸਰਵਰ ਕਲਾਇੰਟਾਂ ਨੂੰ ਡਾਇਰੈਕਟਰੀ ਸੂਚੀਕਰਨ (directory listings) ਉਜਾਗਰ ਨਹੀਂ ਕਰਦੇ ਜਦੋਂ ਤੱਕ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਇਰਾਦਾ ਨਾ ਹੋਵੇ। | 2 |
| **13.4.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੰਭਾਵੀ ਜਾਣਕਾਰੀ ਲੀਕੇਜ ਤੋਂ ਬਚਣ ਲਈ, ਪ੍ਰੋਡਕਸ਼ਨ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ HTTP TRACE ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕੀਤਾ ਜਾਂਦਾ। | 2 |
| **13.4.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਦਸਤਾਵੇਜ਼ (ਜਿਵੇਂ ਕਿ ਅੰਦਰੂਨੀ API ਲਈ) ਅਤੇ ਨਿਗਰਾਨੀ ਅੰਤ-ਬਿੰਦੂ ਉਜਾਗਰ ਨਹੀਂ ਕੀਤੇ ਜਾਂਦੇ ਜਦੋਂ ਤੱਕ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਇਰਾਦਾ ਨਾ ਹੋਵੇ। | 2 |
| **13.4.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਬੈਕਐਂਡ ਘਟਕਾਂ ਦੀ ਵਿਸਤ੍ਰਿਤ ਸੰਸਕਰਣ ਜਾਣਕਾਰੀ ਉਜਾਗਰ ਨਹੀਂ ਕਰਦੀ। | 3 |
| **13.4.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਵੈੱਬ ਟੀਅਰ (web tier) ਨੂੰ ਸਿਰਫ਼ ਖ਼ਾਸ ਫ਼ਾਈਲ ਐਕਸਟੈਂਸ਼ਨਾਂ ਵਾਲੀਆਂ ਫ਼ਾਈਲਾਂ ਹੀ ਪਰੋਸਣ ਲਈ ਸੰਰਚਿਤ ਕੀਤਾ ਗਿਆ ਹੈ ਤਾਂ ਜੋ ਅਣਇੱਛਤ ਜਾਣਕਾਰੀ, ਸੰਰਚਨਾ, ਅਤੇ ਸਰੋਤ ਕੋਡ ਲੀਕੇਜ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 3 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP Web Security Testing Guide: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing)
