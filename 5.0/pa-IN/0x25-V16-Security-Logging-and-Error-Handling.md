<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x25-V16-Security-Logging-and-Error-Handling.md -->
<!-- Translator: GeeksikhSecurity -->

# V16 Security Logging and Error Handling
# V16 ਸੁਰੱਖਿਆ ਲੌਗਿੰਗ ਅਤੇ ਗਲਤੀ ਪ੍ਰਬੰਧਨ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

Security logs are distinct from error or performance logs and are used to record security-relevant events such as authentication decisions, access control decisions, and attempts to bypass security controls, such as input validation or business logic validation. Their purpose is to support detection, response, and investigation by providing high-signal, structured data for analysis tools like SIEMs.

ਸੁਰੱਖਿਆ ਲੌਗ (security logs) ਗਲਤੀ ਜਾਂ ਕਾਰਗੁਜ਼ਾਰੀ ਲੌਗਾਂ ਤੋਂ ਵੱਖਰੇ ਹੁੰਦੇ ਹਨ ਅਤੇ ਸੁਰੱਖਿਆ-ਸੰਬੰਧੀ ਘਟਨਾਵਾਂ ਨੂੰ ਦਰਜ ਕਰਨ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਪ੍ਰਮਾਣੀਕਰਨ ਫ਼ੈਸਲੇ, ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਫ਼ੈਸਲੇ, ਅਤੇ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣਾਂ, ਜਿਵੇਂ ਕਿ ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ ਜਾਂ ਕਾਰੋਬਾਰੀ ਤਰਕ ਪ੍ਰਮਾਣਿਕਤਾ, ਨੂੰ ਬਾਈਪਾਸ ਕਰਨ ਦੀਆਂ ਕੋਸ਼ਿਸ਼ਾਂ। ਇਹਨਾਂ ਦਾ ਉਦੇਸ਼ SIEM ਵਰਗੇ ਵਿਸ਼ਲੇਸ਼ਣ ਟੂਲਾਂ ਲਈ ਉੱਚ-ਸੰਕੇਤ (high-signal), ਢਾਂਚਾਬੱਧ (structured) ਡਾਟਾ ਪ੍ਰਦਾਨ ਕਰਕੇ ਪਤਾ ਲਗਾਉਣ (detection), ਪ੍ਰਤੀਕਿਰਿਆ (response), ਅਤੇ ਤਫ਼ਤੀਸ਼ (investigation) ਦਾ ਸਮਰਥਨ ਕਰਨਾ ਹੈ।

Logs should not include sensitive personal data unless legally required, and any logged data must be protected as a high-value asset. Logging must not compromise privacy or system security. Applications must also fail securely, avoiding unnecessary disclosure or disruption.

ਲੌਗਾਂ ਵਿੱਚ ਸੰਵੇਦਨਸ਼ੀਲ ਨਿੱਜੀ ਡਾਟਾ ਸ਼ਾਮਲ ਨਹੀਂ ਹੋਣਾ ਚਾਹੀਦਾ ਜਦੋਂ ਤੱਕ ਕਾਨੂੰਨੀ ਤੌਰ 'ਤੇ ਲੋੜੀਂਦਾ ਨਾ ਹੋਵੇ, ਅਤੇ ਕਿਸੇ ਵੀ ਲੌਗ ਕੀਤੇ ਡਾਟੇ ਨੂੰ ਇੱਕ ਉੱਚ-ਮੁੱਲ ਸੰਪਤੀ ਵਜੋਂ ਸੁਰੱਖਿਅਤ ਰੱਖਣਾ ਲਾਜ਼ਮੀ ਹੈ। ਲੌਗਿੰਗ ਨੂੰ ਨਿੱਜਤਾ ਜਾਂ ਸਿਸਟਮ ਸੁਰੱਖਿਆ ਨਾਲ ਸਮਝੌਤਾ ਨਹੀਂ ਕਰਨਾ ਚਾਹੀਦਾ। ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਅਸਫਲ ਹੋਣਾ (fail securely) ਵੀ ਲਾਜ਼ਮੀ ਹੈ, ਬੇਲੋੜੇ ਖੁਲਾਸੇ ਜਾਂ ਵਿਘਨ ਤੋਂ ਬਚਦੇ ਹੋਏ।

For detailed implementation guidance, refer to the OWASP Cheat Sheets in the references section.

ਵਿਸਤ੍ਰਿਤ ਲਾਗੂਕਰਨ ਮਾਰਗਦਰਸ਼ਨ ਲਈ, ਹਵਾਲੇ ਭਾਗ ਵਿੱਚ ਦਿੱਤੀਆਂ OWASP Cheat Sheets ਵੇਖੋ।

## V16.1 Security Logging Documentation
## V16.1 ਸੁਰੱਖਿਆ ਲੌਗਿੰਗ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

This section ensures a clear and complete inventory of logging across the application stack. This is essential for effective security monitoring, incident response, and compliance.

ਇਹ ਭਾਗ ਐਪਲੀਕੇਸ਼ਨ ਸਟੈਕ ਭਰ ਵਿੱਚ ਲੌਗਿੰਗ ਦੀ ਇੱਕ ਸਪੱਸ਼ਟ ਅਤੇ ਸੰਪੂਰਨ ਇਨਵੈਂਟਰੀ (inventory) ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਸੁਰੱਖਿਆ ਨਿਗਰਾਨੀ, ਘਟਨਾ ਪ੍ਰਤੀਕਿਰਿਆ (incident response), ਅਤੇ ਪਾਲਣਾ ਲਈ ਜ਼ਰੂਰੀ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **16.1.1** | Verify that an inventory exists documenting the logging performed at each layer of the application's technology stack, what events are being logged, log formats, where that logging is stored, how it is used, how access to it is controlled, and for how long logs are kept. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **16.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇੱਕ ਇਨਵੈਂਟਰੀ ਮੌਜੂਦ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਤਕਨਾਲੋਜੀ ਸਟੈਕ ਦੀ ਹਰੇਕ ਪਰਤ 'ਤੇ ਕੀਤੀ ਜਾਂਦੀ ਲੌਗਿੰਗ, ਕਿਹੜੀਆਂ ਘਟਨਾਵਾਂ ਲੌਗ ਕੀਤੀਆਂ ਜਾ ਰਹੀਆਂ ਹਨ, ਲੌਗ ਫ਼ਾਰਮੈਟ, ਉਹ ਲੌਗਿੰਗ ਕਿੱਥੇ ਸਟੋਰ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਇਸ ਨੂੰ ਕਿਵੇਂ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਇਸ ਤੱਕ ਪਹੁੰਚ ਨੂੰ ਕਿਵੇਂ ਨਿਯੰਤਰਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਲੌਗ ਕਿੰਨੇ ਸਮੇਂ ਲਈ ਰੱਖੇ ਜਾਂਦੇ ਹਨ, ਨੂੰ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਦਿੰਦੀ ਹੈ। | 2 |

## V16.2 General Logging
## V16.2 ਆਮ ਲੌਗਿੰਗ

This section provides requirements to ensure that security logs are consistently structured and contain the expected metadata. The goal is to make logs machine-readable and analyzable across distributed systems and tools.

ਇਹ ਭਾਗ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਲੋੜਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਕਿ ਸੁਰੱਖਿਆ ਲੌਗ ਇਕਸਾਰ ਢੰਗ ਨਾਲ ਢਾਂਚਾਬੱਧ ਹੋਣ ਅਤੇ ਉਹਨਾਂ ਵਿੱਚ ਉਮੀਦ ਕੀਤਾ ਮੈਟਾਡਾਟਾ ਸ਼ਾਮਲ ਹੋਵੇ। ਟੀਚਾ ਲੌਗਾਂ ਨੂੰ ਵੰਡੇ ਹੋਏ (distributed) ਸਿਸਟਮਾਂ ਅਤੇ ਟੂਲਾਂ ਭਰ ਵਿੱਚ ਮਸ਼ੀਨ-ਪੜ੍ਹਨਯੋਗ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣਯੋਗ ਬਣਾਉਣਾ ਹੈ।

Naturally, security events often involve sensitive data. If such data is logged without consideration, the logs themselves become classified and therefore subject to encryption requirements, stricter retention policies, and potential disclosure during audits.

ਸੁਭਾਵਿਕ ਤੌਰ 'ਤੇ, ਸੁਰੱਖਿਆ ਘਟਨਾਵਾਂ ਵਿੱਚ ਅਕਸਰ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ। ਜੇਕਰ ਅਜਿਹਾ ਡਾਟਾ ਬਿਨਾਂ ਸੋਚ-ਵਿਚਾਰ ਦੇ ਲੌਗ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਲੌਗ ਖ਼ੁਦ ਵਰਗੀਕ੍ਰਿਤ (classified) ਬਣ ਜਾਂਦੇ ਹਨ ਅਤੇ ਇਸ ਲਈ ਏਨਕ੍ਰਿਪਸ਼ਨ ਲੋੜਾਂ, ਵਧੇਰੇ ਸਖ਼ਤ ਧਾਰਨ (retention) ਨੀਤੀਆਂ, ਅਤੇ ਆਡਿਟਾਂ ਦੌਰਾਨ ਸੰਭਾਵੀ ਖੁਲਾਸੇ ਦੇ ਅਧੀਨ ਹੋ ਜਾਂਦੇ ਹਨ।

Therefore, it is critical to log only what is necessary and to treat log data with the same care as other sensitive assets.

ਇਸ ਲਈ, ਸਿਰਫ਼ ਉਹੀ ਲੌਗ ਕਰਨਾ ਜੋ ਜ਼ਰੂਰੀ ਹੈ ਅਤੇ ਲੌਗ ਡਾਟੇ ਨਾਲ ਹੋਰ ਸੰਵੇਦਨਸ਼ੀਲ ਸੰਪਤੀਆਂ ਵਾਂਗ ਹੀ ਸਾਵਧਾਨੀ ਨਾਲ ਪੇਸ਼ ਆਉਣਾ ਬਹੁਤ ਮਹੱਤਵਪੂਰਨ ਹੈ।

The requirements below establish foundational requirements for logging metadata, synchronization, format, and control.

ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਲੋੜਾਂ ਲੌਗਿੰਗ ਮੈਟਾਡਾਟਾ, ਸਮਕਾਲੀਕਰਨ (synchronization), ਫ਼ਾਰਮੈਟ, ਅਤੇ ਨਿਯੰਤਰਣ ਲਈ ਬੁਨਿਆਦੀ ਲੋੜਾਂ ਸਥਾਪਿਤ ਕਰਦੀਆਂ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **16.2.1** | Verify that each log entry includes necessary metadata (such as when, where, who, what) that would allow for a detailed investigation of the timeline when an event happens. | 2 |
| **16.2.2** | Verify that time sources for all logging components are synchronized, and that timestamps in security event metadata use UTC or include an explicit time zone offset. UTC is recommended to ensure consistency across distributed systems and to prevent confusion during daylight saving time transitions. | 2 |
| **16.2.3** | Verify that the application only stores or broadcasts logs to the files and services that are documented in the log inventory. | 2 |
| **16.2.4** | Verify that logs can be read and correlated by the log processor that is in use, preferably by using a common logging format. | 2 |
| **16.2.5** | Verify that when logging sensitive data, the application enforces logging based on the data's protection level. For example, it may not be allowed to log certain data, such as credentials or payment details. Other data, such as session tokens, may only be logged by being hashed or masked, either in full or partially. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **16.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਹਰੇਕ ਲੌਗ ਐਂਟਰੀ ਵਿੱਚ ਲੋੜੀਂਦਾ ਮੈਟਾਡਾਟਾ (ਜਿਵੇਂ ਕਿ ਕਦੋਂ, ਕਿੱਥੇ, ਕੌਣ, ਕੀ) ਸ਼ਾਮਲ ਹੈ ਜੋ ਕਿਸੇ ਘਟਨਾ ਦੇ ਵਾਪਰਨ 'ਤੇ ਸਮਾਂ-ਰੇਖਾ (timeline) ਦੀ ਵਿਸਤ੍ਰਿਤ ਤਫ਼ਤੀਸ਼ ਦੀ ਇਜਾਜ਼ਤ ਦੇਵੇਗਾ। | 2 |
| **16.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੇ ਲੌਗਿੰਗ ਹਿੱਸਿਆਂ ਲਈ ਸਮਾਂ ਸਰੋਤ (time sources) ਸਮਕਾਲੀ ਕੀਤੇ ਗਏ ਹਨ, ਅਤੇ ਸੁਰੱਖਿਆ ਘਟਨਾ ਮੈਟਾਡਾਟਾ ਵਿੱਚ ਟਾਈਮਸਟੈਂਪ UTC ਵਰਤਦੇ ਹਨ ਜਾਂ ਇੱਕ ਸਪੱਸ਼ਟ ਸਮਾਂ ਖੇਤਰ ਆਫ਼ਸੈੱਟ (time zone offset) ਸ਼ਾਮਲ ਕਰਦੇ ਹਨ। ਵੰਡੇ ਹੋਏ ਸਿਸਟਮਾਂ ਭਰ ਵਿੱਚ ਇਕਸਾਰਤਾ ਯਕੀਨੀ ਬਣਾਉਣ ਅਤੇ ਡੇਲਾਈਟ ਸੇਵਿੰਗ ਟਾਈਮ ਤਬਦੀਲੀਆਂ ਦੌਰਾਨ ਉਲਝਣ ਰੋਕਣ ਲਈ UTC ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 2 |
| **16.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਲੌਗਾਂ ਨੂੰ ਸਿਰਫ਼ ਉਹਨਾਂ ਫ਼ਾਈਲਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਵਿੱਚ ਹੀ ਸਟੋਰ ਜਾਂ ਪ੍ਰਸਾਰਿਤ ਕਰਦੀ ਹੈ ਜੋ ਲੌਗ ਇਨਵੈਂਟਰੀ ਵਿੱਚ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਵਿੱਚ ਦਰਜ ਹਨ। | 2 |
| **16.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਲੌਗਾਂ ਨੂੰ ਵਰਤੋਂ ਵਿੱਚ ਆ ਰਹੇ ਲੌਗ ਪ੍ਰੋਸੈਸਰ ਦੁਆਰਾ ਪੜ੍ਹਿਆ ਅਤੇ ਸਹਿ-ਸੰਬੰਧਿਤ (correlated) ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਤਰਜੀਹੀ ਤੌਰ 'ਤੇ ਇੱਕ ਸਾਂਝੇ ਲੌਗਿੰਗ ਫ਼ਾਰਮੈਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ। | 2 |
| **16.2.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਲੌਗ ਕਰਦੇ ਸਮੇਂ, ਐਪਲੀਕੇਸ਼ਨ ਡਾਟੇ ਦੇ ਸੁਰੱਖਿਆ ਪੱਧਰ ਦੇ ਆਧਾਰ 'ਤੇ ਲੌਗਿੰਗ ਲਾਗੂ ਕਰਦੀ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਕੁਝ ਡਾਟਾ, ਜਿਵੇਂ ਕਿ ਪ੍ਰਮਾਣ-ਪੱਤਰ ਜਾਂ ਭੁਗਤਾਨ ਵੇਰਵੇ, ਲੌਗ ਕਰਨ ਦੀ ਇਜਾਜ਼ਤ ਨਹੀਂ ਹੋ ਸਕਦੀ। ਹੋਰ ਡਾਟਾ, ਜਿਵੇਂ ਕਿ ਸੈਸ਼ਨ ਟੋਕਨ, ਸਿਰਫ਼ ਹੈਸ਼ ਕੀਤੇ ਜਾਂ ਮਾਸਕ ਕੀਤੇ (masked) ਜਾਣ 'ਤੇ ਹੀ ਲੌਗ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਭਾਵੇਂ ਪੂਰੀ ਤਰ੍ਹਾਂ ਜਾਂ ਅੰਸ਼ਕ ਤੌਰ 'ਤੇ। | 2 |

## V16.3 Security Events
## V16.3 ਸੁਰੱਖਿਆ ਘਟਨਾਵਾਂ

This section defines requirements for logging security-relevant events within the application. Capturing these events is critical for detecting suspicious behavior, supporting investigations, and fulfilling compliance obligations.

ਇਹ ਭਾਗ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਅੰਦਰ ਸੁਰੱਖਿਆ-ਸੰਬੰਧੀ ਘਟਨਾਵਾਂ ਨੂੰ ਲੌਗ ਕਰਨ ਲਈ ਲੋੜਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ। ਇਹਨਾਂ ਘਟਨਾਵਾਂ ਨੂੰ ਦਰਜ ਕਰਨਾ ਸ਼ੱਕੀ ਵਿਹਾਰ ਦਾ ਪਤਾ ਲਗਾਉਣ, ਤਫ਼ਤੀਸ਼ਾਂ ਦਾ ਸਮਰਥਨ ਕਰਨ, ਅਤੇ ਪਾਲਣਾ ਦੀਆਂ ਜ਼ਿੰਮੇਵਾਰੀਆਂ ਪੂਰੀਆਂ ਕਰਨ ਲਈ ਬਹੁਤ ਮਹੱਤਵਪੂਰਨ ਹੈ।

This section outlines the types of events that should be logged but does not attempt to provide exhaustive detail. Each application has unique risk factors and operational context.

ਇਹ ਭਾਗ ਉਹਨਾਂ ਘਟਨਾਵਾਂ ਦੀਆਂ ਕਿਸਮਾਂ ਦੀ ਰੂਪਰੇਖਾ ਦਿੰਦਾ ਹੈ ਜੋ ਲੌਗ ਕੀਤੀਆਂ ਜਾਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ, ਪਰ ਸੰਪੂਰਨ ਵੇਰਵਾ ਪ੍ਰਦਾਨ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਨਹੀਂ ਕਰਦਾ। ਹਰੇਕ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਆਪਣੇ ਵਿਲੱਖਣ ਜੋਖਮ ਕਾਰਕ ਅਤੇ ਸੰਚਾਲਨ ਸੰਦਰਭ ਹੁੰਦੇ ਹਨ।

Note that while ASVS includes logging of security events in scope, alerting and correlation (e.g., SIEM rules or monitoring infrastructure) are considered out of scope and are handled by operational and monitoring systems.

ਧਿਆਨ ਦਿਓ ਕਿ ਭਾਵੇਂ ASVS ਸੁਰੱਖਿਆ ਘਟਨਾਵਾਂ ਦੀ ਲੌਗਿੰਗ ਨੂੰ ਘੇਰੇ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ, ਚੇਤਾਵਨੀ ਦੇਣਾ (alerting) ਅਤੇ ਸਹਿ-ਸੰਬੰਧ (correlation) (ਜਿਵੇਂ, SIEM ਨਿਯਮ ਜਾਂ ਨਿਗਰਾਨੀ ਬੁਨਿਆਦੀ ਢਾਂਚਾ) ਘੇਰੇ ਤੋਂ ਬਾਹਰ ਮੰਨੇ ਜਾਂਦੇ ਹਨ ਅਤੇ ਸੰਚਾਲਨ ਅਤੇ ਨਿਗਰਾਨੀ ਸਿਸਟਮਾਂ ਦੁਆਰਾ ਸੰਭਾਲੇ ਜਾਂਦੇ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **16.3.1** | Verify that all authentication operations are logged, including successful and unsuccessful attempts. Additional metadata, such as the type of authentication or factors used, should also be collected. | 2 |
| **16.3.2** | Verify that failed authorization attempts are logged. For L3, this must include logging all authorization decisions, including logging when sensitive data is accessed (without logging the sensitive data itself). | 2 |
| **16.3.3** | Verify that the application logs the security events that are defined in the documentation and also logs attempts to bypass the security controls, such as input validation, business logic, and anti-automation. | 2 |
| **16.3.4** | Verify that the application logs unexpected errors and security control failures such as backend TLS failures. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **16.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੀਆਂ ਪ੍ਰਮਾਣੀਕਰਨ ਕਾਰਵਾਈਆਂ ਲੌਗ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ, ਜਿਸ ਵਿੱਚ ਸਫਲ ਅਤੇ ਅਸਫਲ ਕੋਸ਼ਿਸ਼ਾਂ ਸ਼ਾਮਲ ਹਨ। ਵਾਧੂ ਮੈਟਾਡਾਟਾ, ਜਿਵੇਂ ਕਿ ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਕਿਸਮ ਜਾਂ ਵਰਤੇ ਗਏ ਕਾਰਕ, ਵੀ ਇਕੱਠਾ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। | 2 |
| **16.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਅਸਫਲ ਅਧਿਕਾਰੀਕਰਨ ਕੋਸ਼ਿਸ਼ਾਂ ਲੌਗ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ। L3 ਲਈ, ਇਸ ਵਿੱਚ ਸਾਰੇ ਅਧਿਕਾਰੀਕਰਨ ਫ਼ੈਸਲਿਆਂ ਦੀ ਲੌਗਿੰਗ ਸ਼ਾਮਲ ਹੋਣੀ ਲਾਜ਼ਮੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਇਹ ਲੌਗ ਕਰਨਾ ਵੀ ਸ਼ਾਮਲ ਹੈ ਕਿ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਤੱਕ ਕਦੋਂ ਪਹੁੰਚ ਕੀਤੀ ਗਈ (ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਨੂੰ ਖ਼ੁਦ ਲੌਗ ਕੀਤੇ ਬਿਨਾਂ)। | 2 |
| **16.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਸੁਰੱਖਿਆ ਘਟਨਾਵਾਂ ਨੂੰ ਲੌਗ ਕਰਦੀ ਹੈ ਅਤੇ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣਾਂ, ਜਿਵੇਂ ਕਿ ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ, ਕਾਰੋਬਾਰੀ ਤਰਕ, ਅਤੇ ਸਵੈਚਾਲਨ-ਵਿਰੋਧੀ, ਨੂੰ ਬਾਈਪਾਸ ਕਰਨ ਦੀਆਂ ਕੋਸ਼ਿਸ਼ਾਂ ਨੂੰ ਵੀ ਲੌਗ ਕਰਦੀ ਹੈ। | 2 |
| **16.3.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਅਣਕਿਆਸੀਆਂ ਗਲਤੀਆਂ ਅਤੇ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਅਸਫਲਤਾਵਾਂ, ਜਿਵੇਂ ਕਿ ਬੈਕਐਂਡ TLS ਅਸਫਲਤਾਵਾਂ, ਨੂੰ ਲੌਗ ਕਰਦੀ ਹੈ। | 2 |

## V16.4 Log Protection
## V16.4 ਲੌਗ ਸੁਰੱਖਿਆ

Logs are valuable forensic artifacts and must be protected. If logs can be easily modified or deleted, they lose their integrity and become unreliable for incident investigations or legal proceedings. Logs may expose internal application behavior or sensitive metadata, making them an attractive target for attackers.

ਲੌਗ ਕੀਮਤੀ ਫ਼ੋਰੈਂਸਿਕ ਸਬੂਤ (forensic artifacts) ਹਨ ਅਤੇ ਇਹਨਾਂ ਦੀ ਸੁਰੱਖਿਆ ਲਾਜ਼ਮੀ ਹੈ। ਜੇਕਰ ਲੌਗਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਸੋਧਿਆ ਜਾਂ ਮਿਟਾਇਆ ਜਾ ਸਕਦਾ ਹੈ, ਤਾਂ ਉਹ ਆਪਣੀ ਅਖੰਡਤਾ ਗੁਆ ਦਿੰਦੇ ਹਨ ਅਤੇ ਘਟਨਾ ਤਫ਼ਤੀਸ਼ਾਂ ਜਾਂ ਕਾਨੂੰਨੀ ਕਾਰਵਾਈਆਂ ਲਈ ਭਰੋਸੇਯੋਗ ਨਹੀਂ ਰਹਿੰਦੇ। ਲੌਗ ਅੰਦਰੂਨੀ ਐਪਲੀਕੇਸ਼ਨ ਵਿਹਾਰ ਜਾਂ ਸੰਵੇਦਨਸ਼ੀਲ ਮੈਟਾਡਾਟਾ ਉਜਾਗਰ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਕਾਰਨ ਉਹ ਹਮਲਾਵਰਾਂ ਲਈ ਇੱਕ ਆਕਰਸ਼ਕ ਨਿਸ਼ਾਨਾ ਬਣ ਜਾਂਦੇ ਹਨ।

This section defines requirements to ensure that logs are protected from unauthorized access, tampering, and disclosure, and that they are safely transmitted and stored in secure, isolated systems.

ਇਹ ਭਾਗ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਲੋੜਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਕਿ ਲੌਗ ਅਣਅਧਿਕਾਰਤ ਪਹੁੰਚ, ਛੇੜਛਾੜ, ਅਤੇ ਖੁਲਾਸੇ ਤੋਂ ਸੁਰੱਖਿਅਤ ਹੋਣ, ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਪ੍ਰਸਾਰਿਤ ਕੀਤਾ ਜਾਵੇ ਅਤੇ ਸੁਰੱਖਿਅਤ, ਅਲੱਗ-ਥਲੱਗ (isolated) ਸਿਸਟਮਾਂ ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਜਾਵੇ।

| # | Description | Level |
| :---: | :--- | :---: |
| **16.4.1** | Verify that all logging components appropriately encode data to prevent log injection. | 2 |
| **16.4.2** | Verify that logs are protected from unauthorized access and cannot be modified. | 2 |
| **16.4.3** | Verify that logs are securely transmitted to a logically separate system for analysis, detection, alerting, and escalation. The aim is to ensure that if the application is breached, the logs are not compromised. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **16.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੇ ਲੌਗਿੰਗ ਹਿੱਸੇ ਲੌਗ ਇੰਜੈਕਸ਼ਨ ਨੂੰ ਰੋਕਣ ਲਈ ਡਾਟੇ ਨੂੰ ਢੁਕਵੇਂ ਢੰਗ ਨਾਲ ਏਨਕੋਡ ਕਰਦੇ ਹਨ। | 2 |
| **16.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਲੌਗ ਅਣਅਧਿਕਾਰਤ ਪਹੁੰਚ ਤੋਂ ਸੁਰੱਖਿਅਤ ਹਨ ਅਤੇ ਇਹਨਾਂ ਨੂੰ ਸੋਧਿਆ ਨਹੀਂ ਜਾ ਸਕਦਾ। | 2 |
| **16.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਲੌਗਾਂ ਨੂੰ ਵਿਸ਼ਲੇਸ਼ਣ, ਪਤਾ ਲਗਾਉਣ, ਚੇਤਾਵਨੀ ਦੇਣ, ਅਤੇ ਐਸਕੇਲੇਸ਼ਨ (escalation) ਲਈ ਇੱਕ ਲਾਜ਼ੀਕਲ ਤੌਰ 'ਤੇ ਵੱਖਰੇ (logically separate) ਸਿਸਟਮ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਪ੍ਰਸਾਰਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਉਦੇਸ਼ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਜੇਕਰ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਸੰਨ੍ਹ ਲੱਗ ਜਾਵੇ (breached), ਤਾਂ ਲੌਗਾਂ ਦਾ ਸਮਝੌਤਾ ਨਾ ਹੋਵੇ। | 2 |

## V16.5 Error Handling
## V16.5 ਗਲਤੀ ਪ੍ਰਬੰਧਨ

This section defines requirements to ensure that applications fail gracefully and securely without disclosing sensitive internal details.

ਇਹ ਭਾਗ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਲੋੜਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਕਿ ਐਪਲੀਕੇਸ਼ਨਾਂ ਸੰਵੇਦਨਸ਼ੀਲ ਅੰਦਰੂਨੀ ਵੇਰਵਿਆਂ ਦਾ ਖੁਲਾਸਾ ਕੀਤੇ ਬਿਨਾਂ ਸੁਚਾਰੂ ਅਤੇ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਅਸਫਲ ਹੋਣ (fail gracefully and securely)।

| # | Description | Level |
| :---: | :--- | :---: |
| **16.5.1** | Verify that a generic message is returned to the consumer when an unexpected or security-sensitive error occurs, ensuring no exposure of sensitive internal system data such as stack traces, queries, secret keys, and tokens. | 2 |
| **16.5.2** | Verify that the application continues to operate securely when external resource access fails, for example, by using patterns such as circuit breakers or graceful degradation. | 2 |
| **16.5.3** | Verify that the application fails gracefully and securely, including when an exception occurs, preventing fail-open conditions such as processing a transaction despite errors resulting from validation logic. | 2 |
| **16.5.4** | Verify that a "last resort" error handler is defined which will catch all unhandled exceptions. This is both to avoid losing error details that must go to log files and to ensure that an error does not take down the entire application process, leading to a loss of availability. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **16.5.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਦੋਂ ਕੋਈ ਅਣਕਿਆਸੀ ਜਾਂ ਸੁਰੱਖਿਆ-ਸੰਵੇਦਨਸ਼ੀਲ ਗਲਤੀ ਵਾਪਰਦੀ ਹੈ ਤਾਂ ਖਪਤਕਾਰ ਨੂੰ ਇੱਕ ਆਮ ਸੁਨੇਹਾ ਵਾਪਸ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੇ ਹੋਏ ਕਿ ਸੰਵੇਦਨਸ਼ੀਲ ਅੰਦਰੂਨੀ ਸਿਸਟਮ ਡਾਟਾ, ਜਿਵੇਂ ਕਿ ਸਟੈਕ ਟ੍ਰੇਸ, ਕਿਊਰੀਆਂ, ਗੁਪਤ ਕੁੰਜੀਆਂ, ਅਤੇ ਟੋਕਨ, ਉਜਾਗਰ ਨਾ ਹੋਵੇ। | 2 |
| **16.5.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਦੋਂ ਬਾਹਰੀ ਸਰੋਤ ਪਹੁੰਚ ਅਸਫਲ ਹੋ ਜਾਂਦੀ ਹੈ ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਕੰਮ ਕਰਨਾ ਜਾਰੀ ਰੱਖਦੀ ਹੈ, ਉਦਾਹਰਨ ਲਈ, ਸਰਕਟ ਬ੍ਰੇਕਰ (circuit breaker) ਜਾਂ ਸੁਚਾਰੂ ਨਿਘਾਰ (graceful degradation) ਵਰਗੇ ਨਮੂਨਿਆਂ (patterns) ਦੀ ਵਰਤੋਂ ਕਰਕੇ। | 2 |
| **16.5.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸੁਚਾਰੂ ਅਤੇ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਅਸਫਲ ਹੁੰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਅਪਵਾਦ (exception) ਵਾਪਰਨ 'ਤੇ ਵੀ ਸ਼ਾਮਲ ਹੈ, ਅਤੇ ਫ਼ੇਲ-ਓਪਨ (fail-open) ਸਥਿਤੀਆਂ ਨੂੰ ਰੋਕਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਪ੍ਰਮਾਣਿਕਤਾ ਤਰਕ ਤੋਂ ਪੈਦਾ ਹੋਈਆਂ ਗਲਤੀਆਂ ਦੇ ਬਾਵਜੂਦ ਕਿਸੇ ਟ੍ਰਾਂਜ਼ੈਕਸ਼ਨ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਨਾ। | 2 |
| **16.5.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇੱਕ "ਆਖ਼ਰੀ ਸਹਾਰਾ" (last resort) ਗਲਤੀ ਹੈਂਡਲਰ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਗਿਆ ਹੈ ਜੋ ਸਾਰੇ ਅਣ-ਸੰਭਾਲੇ (unhandled) ਅਪਵਾਦਾਂ ਨੂੰ ਫੜੇਗਾ। ਇਹ ਉਹਨਾਂ ਗਲਤੀ ਵੇਰਵਿਆਂ ਦੇ ਗੁਆਚਣ ਤੋਂ ਬਚਣ ਲਈ ਵੀ ਹੈ ਜਿਨ੍ਹਾਂ ਦਾ ਲੌਗ ਫ਼ਾਈਲਾਂ ਵਿੱਚ ਜਾਣਾ ਲਾਜ਼ਮੀ ਹੈ, ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਵੀ ਕਿ ਕੋਈ ਗਲਤੀ ਪੂਰੇ ਐਪਲੀਕੇਸ਼ਨ ਪ੍ਰੋਸੈਸ (process) ਨੂੰ ਬੰਦ ਨਾ ਕਰ ਦੇਵੇ, ਜਿਸ ਨਾਲ ਉਪਲਬਧਤਾ ਦਾ ਨੁਕਸਾਨ ਹੋਵੇ। | 3 |

Note: Certain languages, (including Swift, Go, and through common design practice, many functional languages,) do not support exceptions or last-resort event handlers. In this case, architects and developers should use a pattern, language, or framework-friendly way to ensure that applications can securely handle exceptional, unexpected, or security-related events.

ਨੋਟ: ਕੁਝ ਭਾਸ਼ਾਵਾਂ, (Swift, Go, ਅਤੇ ਆਮ ਡਿਜ਼ਾਈਨ ਅਮਲ ਰਾਹੀਂ, ਕਈ ਫੰਕਸ਼ਨਲ ਭਾਸ਼ਾਵਾਂ ਸਮੇਤ,) ਅਪਵਾਦਾਂ ਜਾਂ ਆਖ਼ਰੀ-ਸਹਾਰਾ ਘਟਨਾ ਹੈਂਡਲਰਾਂ ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦੀਆਂ। ਇਸ ਸਥਿਤੀ ਵਿੱਚ, ਆਰਕੀਟੈਕਟਾਂ ਅਤੇ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਇੱਕ ਨਮੂਨਾ-, ਭਾਸ਼ਾ-, ਜਾਂ ਫ੍ਰੇਮਵਰਕ-ਅਨੁਕੂਲ ਤਰੀਕਾ ਵਰਤਣਾ ਚਾਹੀਦਾ ਹੈ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਪਵਾਦੀ, ਅਣਕਿਆਸੀਆਂ, ਜਾਂ ਸੁਰੱਖਿਆ-ਸੰਬੰਧੀ ਘਟਨਾਵਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਸੰਭਾਲ ਸਕਣ।

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP Web Security Testing Guide: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
* [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
* [OWASP Application Logging Vocabulary Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html)
