<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x24-V15-Secure-Coding-and-Architecture.md -->
<!-- Translator: GeeksikhSecurity -->

# V15 Secure Coding and Architecture
# V15 ਸੁਰੱਖਿਅਤ ਕੋਡਿੰਗ ਅਤੇ ਆਰਕੀਟੈਕਚਰ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

Many ASVS requirements either relate to a particular area of security, such as authentication or authorization, or pertain to a particular type of application functionality, such as logging or file handling.

ਕਈ ASVS ਲੋੜਾਂ ਜਾਂ ਤਾਂ ਸੁਰੱਖਿਆ ਦੇ ਕਿਸੇ ਖ਼ਾਸ ਖੇਤਰ ਨਾਲ ਸੰਬੰਧਿਤ ਹੁੰਦੀਆਂ ਹਨ, ਜਿਵੇਂ ਕਿ ਪ੍ਰਮਾਣੀਕਰਨ ਜਾਂ ਅਧਿਕਾਰੀਕਰਨ, ਜਾਂ ਕਿਸੇ ਖ਼ਾਸ ਕਿਸਮ ਦੀ ਐਪਲੀਕੇਸ਼ਨ ਕਾਰਜਸ਼ੀਲਤਾ ਨਾਲ ਸੰਬੰਧਿਤ ਹੁੰਦੀਆਂ ਹਨ, ਜਿਵੇਂ ਕਿ ਲੌਗਿੰਗ ਜਾਂ ਫ਼ਾਈਲ ਪ੍ਰਬੰਧਨ।

This chapter provides general security requirements to consider when designing and developing applications. These requirements focus not only on clean architecture and code quality but also on specific architecture and coding practices necessary for application security.

ਇਹ ਅਧਿਆਇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਡਿਜ਼ਾਈਨ ਅਤੇ ਵਿਕਸਿਤ ਕਰਦੇ ਸਮੇਂ ਵਿਚਾਰਨ ਲਈ ਆਮ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਇਹ ਲੋੜਾਂ ਨਾ ਸਿਰਫ਼ ਸਾਫ਼ ਆਰਕੀਟੈਕਚਰ (architecture) ਅਤੇ ਕੋਡ ਗੁਣਵੱਤਾ 'ਤੇ ਕੇਂਦਰਿਤ ਹਨ, ਸਗੋਂ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਲਈ ਜ਼ਰੂਰੀ ਖ਼ਾਸ ਆਰਕੀਟੈਕਚਰ ਅਤੇ ਕੋਡਿੰਗ ਅਮਲਾਂ 'ਤੇ ਵੀ ਕੇਂਦਰਿਤ ਹਨ।

## V15.1 Secure Coding and Architecture Documentation
## V15.1 ਸੁਰੱਖਿਅਤ ਕੋਡਿੰਗ ਅਤੇ ਆਰਕੀਟੈਕਚਰ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

Many requirements for establishing a secure and defensible architecture depend on clear documentation of decisions made regarding the implementation of specific security controls and the components used within the application.

ਇੱਕ ਸੁਰੱਖਿਅਤ ਅਤੇ ਰੱਖਿਆ-ਯੋਗ ਆਰਕੀਟੈਕਚਰ ਸਥਾਪਿਤ ਕਰਨ ਲਈ ਕਈ ਲੋੜਾਂ ਖ਼ਾਸ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣਾਂ ਦੇ ਲਾਗੂਕਰਨ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਅੰਦਰ ਵਰਤੇ ਗਏ ਘਟਕਾਂ (components) ਬਾਰੇ ਲਏ ਗਏ ਫ਼ੈਸਲਿਆਂ ਦੇ ਸਪੱਸ਼ਟ ਦਸਤਾਵੇਜ਼ੀਕਰਨ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀਆਂ ਹਨ।

This section outlines the documentation requirements, including identifying components considered to contain "dangerous functionality" or to be "risky components."

ਇਹ ਭਾਗ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲੋੜਾਂ ਦੀ ਰੂਪਰੇਖਾ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਉਹਨਾਂ ਘਟਕਾਂ ਦੀ ਪਛਾਣ ਕਰਨਾ ਸ਼ਾਮਲ ਹੈ ਜਿਨ੍ਹਾਂ ਨੂੰ "ਖ਼ਤਰਨਾਕ ਕਾਰਜਸ਼ੀਲਤਾ" (dangerous functionality) ਰੱਖਣ ਵਾਲੇ ਜਾਂ "ਜੋਖਮ ਭਰੇ ਘਟਕ" (risky components) ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ।

A component with "dangerous functionality" may be an internally developed or third-party component that performs operations such as deserialization of untrusted data, raw file or binary data parsing, dynamic code execution, or direct memory manipulation. Vulnerabilities in these types of operations pose a high risk of compromising the application and potentially exposing its underlying infrastructure.

"ਖ਼ਤਰਨਾਕ ਕਾਰਜਸ਼ੀਲਤਾ" ਵਾਲਾ ਘਟਕ ਇੱਕ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ ਵਿਕਸਿਤ ਕੀਤਾ ਜਾਂ ਤੀਜੀ-ਧਿਰ ਘਟਕ ਹੋ ਸਕਦਾ ਹੈ ਜੋ ਅਜਿਹੀਆਂ ਕਾਰਵਾਈਆਂ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਕਿ ਗ਼ੈਰ-ਭਰੋਸੇਯੋਗ ਡਾਟੇ ਦੀ ਡੀਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ (deserialization), ਕੱਚੀ ਫ਼ਾਈਲ ਜਾਂ ਬਾਈਨਰੀ ਡਾਟਾ ਪਾਰਸਿੰਗ (parsing), ਗਤੀਸ਼ੀਲ ਕੋਡ ਚਲਾਉਣਾ (dynamic code execution), ਜਾਂ ਸਿੱਧੀ ਮੈਮੋਰੀ ਹੇਰਾਫੇਰੀ। ਇਸ ਕਿਸਮ ਦੀਆਂ ਕਾਰਵਾਈਆਂ ਵਿਚਲੀਆਂ ਕਮਜ਼ੋਰੀਆਂ ਐਪਲੀਕੇਸ਼ਨ ਨਾਲ ਸਮਝੌਤਾ ਹੋਣ ਅਤੇ ਸੰਭਾਵੀ ਤੌਰ 'ਤੇ ਇਸ ਦੇ ਅੰਤਰੀਵ ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਦੇ ਉਜਾਗਰ ਹੋਣ ਦਾ ਉੱਚ ਜੋਖਮ ਪੈਦਾ ਕਰਦੀਆਂ ਹਨ।

A "risky component" is a 3rd party library (i.e., not internally developed) with missing or poorly implemented security controls around its development processes or functionality. Examples include components that are poorly maintained, unsupported, at the end-of-life stage, or have a history of significant vulnerabilities.

"ਜੋਖਮ ਭਰਿਆ ਘਟਕ" ਇੱਕ ਤੀਜੀ-ਧਿਰ ਲਾਇਬ੍ਰੇਰੀ (ਭਾਵ, ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ ਵਿਕਸਿਤ ਨਹੀਂ ਕੀਤੀ ਗਈ) ਹੈ ਜਿਸ ਦੀਆਂ ਵਿਕਾਸ ਪ੍ਰਕਿਰਿਆਵਾਂ ਜਾਂ ਕਾਰਜਸ਼ੀਲਤਾ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਗ਼ਾਇਬ ਹਨ ਜਾਂ ਮਾੜੇ ਢੰਗ ਨਾਲ ਲਾਗੂ ਕੀਤੇ ਗਏ ਹਨ। ਉਦਾਹਰਣਾਂ ਵਿੱਚ ਉਹ ਘਟਕ ਸ਼ਾਮਲ ਹਨ ਜੋ ਮਾੜੇ ਢੰਗ ਨਾਲ ਸਾਂਭੇ ਜਾਂਦੇ ਹਨ, ਗ਼ੈਰ-ਸਮਰਥਿਤ ਹਨ, ਜੀਵਨ-ਅੰਤ (end-of-life) ਪੜਾਅ 'ਤੇ ਹਨ, ਜਾਂ ਜਿਨ੍ਹਾਂ ਦਾ ਮਹੱਤਵਪੂਰਨ ਕਮਜ਼ੋਰੀਆਂ ਦਾ ਇਤਿਹਾਸ ਹੈ।

This section also emphasizes the importance of defining appropriate timeframes for addressing vulnerabilities in third-party components.

ਇਹ ਭਾਗ ਤੀਜੀ-ਧਿਰ ਘਟਕਾਂ ਵਿਚਲੀਆਂ ਕਮਜ਼ੋਰੀਆਂ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਢੁਕਵੀਆਂ ਸਮਾਂ-ਮਿਆਦਾਂ (timeframes) ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਦੀ ਮਹੱਤਤਾ 'ਤੇ ਵੀ ਜ਼ੋਰ ਦਿੰਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **15.1.1** | Verify that application documentation defines risk based remediation time frames for 3rd party component versions with vulnerabilities and for updating libraries in general, to minimize the risk from these components. | 1 |
| **15.1.2** | Verify that an inventory catalog, such as software bill of materials (SBOM), is maintained of all third-party libraries in use, including verifying that components come from pre-defined, trusted, and continually maintained repositories. | 2 |
| **15.1.3** | Verify that the application documentation identifies functionality which is time-consuming or resource-demanding. This must include how to prevent a loss of availability due to overusing this functionality and how to avoid a situation where building a response takes longer than the consumer's timeout. Potential defenses may include asynchronous processing, using queues, and limiting parallel processes per user and per application. | 2 |
| **15.1.4** | Verify that application documentation highlights third-party libraries which are considered to be "risky components". | 3 |
| **15.1.5** | Verify that application documentation highlights parts of the application where "dangerous functionality" is being used. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **15.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਕਮਜ਼ੋਰੀਆਂ ਵਾਲੇ ਤੀਜੀ-ਧਿਰ ਘਟਕ ਸੰਸਕਰਣਾਂ ਲਈ ਅਤੇ ਆਮ ਤੌਰ 'ਤੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨ ਲਈ ਜੋਖਮ-ਆਧਾਰਿਤ ਸੁਧਾਰ (remediation) ਸਮਾਂ-ਮਿਆਦਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ, ਤਾਂ ਜੋ ਇਹਨਾਂ ਘਟਕਾਂ ਤੋਂ ਜੋਖਮ ਨੂੰ ਘੱਟੋ-ਘੱਟ ਕੀਤਾ ਜਾ ਸਕੇ। | 1 |
| **15.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਵਰਤੋਂ ਵਿੱਚ ਸਾਰੀਆਂ ਤੀਜੀ-ਧਿਰ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦਾ ਇੱਕ ਇਨਵੈਂਟਰੀ ਕੈਟਾਲਾਗ (inventory catalog), ਜਿਵੇਂ ਕਿ ਸਾਫ਼ਟਵੇਅਰ ਸਮੱਗਰੀ ਸੂਚੀ (software bill of materials, SBOM), ਬਣਾਈ ਰੱਖਿਆ ਜਾਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਇਹ ਤਸਦੀਕ ਕਰਨਾ ਵੀ ਸ਼ਾਮਲ ਹੈ ਕਿ ਘਟਕ ਪਹਿਲਾਂ ਤੋਂ ਪਰਿਭਾਸ਼ਿਤ, ਭਰੋਸੇਯੋਗ, ਅਤੇ ਨਿਰੰਤਰ ਸਾਂਭੀਆਂ ਜਾਂਦੀਆਂ ਰਿਪੋਜ਼ਟਰੀਆਂ (repositories) ਤੋਂ ਆਉਂਦੇ ਹਨ। | 2 |
| **15.1.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਉਸ ਕਾਰਜਸ਼ੀਲਤਾ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ ਜੋ ਜ਼ਿਆਦਾ ਸਮਾਂ ਲੈਣ ਵਾਲੀ ਜਾਂ ਜ਼ਿਆਦਾ ਸਰੋਤ ਮੰਗਣ ਵਾਲੀ ਹੈ। ਇਸ ਵਿੱਚ ਇਹ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਸ਼ਾਮਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਇਸ ਕਾਰਜਸ਼ੀਲਤਾ ਦੀ ਵਧੇਰੇ ਵਰਤੋਂ ਕਾਰਨ ਉਪਲਬਧਤਾ (availability) ਦੇ ਨੁਕਸਾਨ ਨੂੰ ਕਿਵੇਂ ਰੋਕਿਆ ਜਾਵੇ ਅਤੇ ਅਜਿਹੀ ਸਥਿਤੀ ਤੋਂ ਕਿਵੇਂ ਬਚਿਆ ਜਾਵੇ ਜਿੱਥੇ ਜਵਾਬ ਤਿਆਰ ਕਰਨ ਵਿੱਚ ਖਪਤਕਾਰ ਦੀ ਸਮਾਂ-ਸੀਮਾ (timeout) ਤੋਂ ਵੱਧ ਸਮਾਂ ਲੱਗਦਾ ਹੈ। ਸੰਭਾਵੀ ਰੱਖਿਆਵਾਂ ਵਿੱਚ ਅਸਿੰਕ੍ਰੋਨਸ (asynchronous) ਪ੍ਰੋਸੈਸਿੰਗ, ਕਤਾਰਾਂ (queues) ਦੀ ਵਰਤੋਂ, ਅਤੇ ਪ੍ਰਤੀ ਉਪਭੋਗਤਾ ਅਤੇ ਪ੍ਰਤੀ ਐਪਲੀਕੇਸ਼ਨ ਸਮਾਨਾਂਤਰ ਪ੍ਰਕਿਰਿਆਵਾਂ ਨੂੰ ਸੀਮਤ ਕਰਨਾ ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ। | 2 |
| **15.1.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਉਹਨਾਂ ਤੀਜੀ-ਧਿਰ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਉਭਾਰ ਕੇ ਦਰਸਾਉਂਦਾ ਹੈ ਜਿਨ੍ਹਾਂ ਨੂੰ "ਜੋਖਮ ਭਰੇ ਘਟਕ" ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ। | 3 |
| **15.1.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਉਹਨਾਂ ਹਿੱਸਿਆਂ ਨੂੰ ਉਭਾਰ ਕੇ ਦਰਸਾਉਂਦਾ ਹੈ ਜਿੱਥੇ "ਖ਼ਤਰਨਾਕ ਕਾਰਜਸ਼ੀਲਤਾ" ਵਰਤੀ ਜਾ ਰਹੀ ਹੈ। | 3 |

## V15.2 Security Architecture and Dependencies
## V15.2 ਸੁਰੱਖਿਆ ਆਰਕੀਟੈਕਚਰ ਅਤੇ ਨਿਰਭਰਤਾਵਾਂ

This section includes requirements for handling risky, outdated, or insecure dependencies and components through dependency management.

ਇਸ ਭਾਗ ਵਿੱਚ ਨਿਰਭਰਤਾ ਪ੍ਰਬੰਧਨ (dependency management) ਰਾਹੀਂ ਜੋਖਮ ਭਰੀਆਂ, ਪੁਰਾਣੀਆਂ, ਜਾਂ ਅਸੁਰੱਖਿਅਤ ਨਿਰਭਰਤਾਵਾਂ ਅਤੇ ਘਟਕਾਂ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ।

It also includes using architectural-level techniques such as sandboxing, encapsulation, containerization, and network isolation to reduce the impact of using "dangerous operations" or "risky components" (as defined in the previous section) and prevent loss of availability due to overusing resource-demanding functionality.

ਇਸ ਵਿੱਚ "ਖ਼ਤਰਨਾਕ ਕਾਰਵਾਈਆਂ" (dangerous operations) ਜਾਂ "ਜੋਖਮ ਭਰੇ ਘਟਕਾਂ" (ਜਿਵੇਂ ਕਿ ਪਿਛਲੇ ਭਾਗ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਹੈ) ਦੀ ਵਰਤੋਂ ਦੇ ਪ੍ਰਭਾਵ ਨੂੰ ਘਟਾਉਣ ਅਤੇ ਜ਼ਿਆਦਾ ਸਰੋਤ ਮੰਗਣ ਵਾਲੀ ਕਾਰਜਸ਼ੀਲਤਾ ਦੀ ਵਧੇਰੇ ਵਰਤੋਂ ਕਾਰਨ ਉਪਲਬਧਤਾ ਦੇ ਨੁਕਸਾਨ ਨੂੰ ਰੋਕਣ ਲਈ ਆਰਕੀਟੈਕਚਰ-ਪੱਧਰ ਦੀਆਂ ਤਕਨੀਕਾਂ, ਜਿਵੇਂ ਕਿ ਸੈਂਡਬਾਕਸਿੰਗ (sandboxing), ਇਨਕੈਪਸੂਲੇਸ਼ਨ (encapsulation), ਕੰਟੇਨਰਾਈਜ਼ੇਸ਼ਨ (containerization), ਅਤੇ ਨੈੱਟਵਰਕ ਅਲਹਿਦਗੀ (network isolation), ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਵੀ ਸ਼ਾਮਲ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **15.2.1** | Verify that the application only contains components which have not breached the documented update and remediation time frames. | 1 |
| **15.2.2** | Verify that the application has implemented defenses against loss of availability due to functionality which is time-consuming or resource-demanding, based on the documented security decisions and strategies for this. | 2 |
| **15.2.3** | Verify that the production environment only includes functionality that is required for the application to function, and does not expose extraneous functionality such as test code, sample snippets, and development functionality. | 2 |
| **15.2.4** | Verify that third-party components and all of their transitive dependencies are included from the expected repository, whether internally owned or an external source, and that there is no risk of a dependency confusion attack. | 3 |
| **15.2.5** | Verify that the application implements additional protections around parts of the application which are documented as containing "dangerous functionality" or using third-party libraries considered to be "risky components". This could include techniques such as sandboxing, encapsulation, containerization or network level isolation to delay and deter attackers who compromise one part of an application from pivoting elsewhere in the application. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **15.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਸਿਰਫ਼ ਉਹ ਘਟਕ ਸ਼ਾਮਲ ਹਨ ਜਿਨ੍ਹਾਂ ਨੇ ਦਸਤਾਵੇਜ਼ੀ ਅੱਪਡੇਟ ਅਤੇ ਸੁਧਾਰ ਸਮਾਂ-ਮਿਆਦਾਂ ਦੀ ਉਲੰਘਣਾ ਨਹੀਂ ਕੀਤੀ ਹੈ। | 1 |
| **15.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਨੇ ਇਸ ਲਈ ਦਸਤਾਵੇਜ਼ੀ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ ਅਤੇ ਰਣਨੀਤੀਆਂ ਦੇ ਆਧਾਰ 'ਤੇ, ਜ਼ਿਆਦਾ ਸਮਾਂ ਲੈਣ ਵਾਲੀ ਜਾਂ ਜ਼ਿਆਦਾ ਸਰੋਤ ਮੰਗਣ ਵਾਲੀ ਕਾਰਜਸ਼ੀਲਤਾ ਕਾਰਨ ਉਪਲਬਧਤਾ ਦੇ ਨੁਕਸਾਨ ਵਿਰੁੱਧ ਰੱਖਿਆਵਾਂ ਲਾਗੂ ਕੀਤੀਆਂ ਹਨ। | 2 |
| **15.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰੋਡਕਸ਼ਨ ਵਾਤਾਵਰਣ ਵਿੱਚ ਸਿਰਫ਼ ਉਹ ਕਾਰਜਸ਼ੀਲਤਾ ਸ਼ਾਮਲ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਕੰਮ ਕਰਨ ਲਈ ਲੋੜੀਂਦੀ ਹੈ, ਅਤੇ ਇਹ ਬੇਲੋੜੀ ਕਾਰਜਸ਼ੀਲਤਾ, ਜਿਵੇਂ ਕਿ ਟੈਸਟ ਕੋਡ, ਨਮੂਨਾ ਸਨਿੱਪਟ, ਅਤੇ ਵਿਕਾਸ ਕਾਰਜਸ਼ੀਲਤਾ, ਨੂੰ ਉਜਾਗਰ ਨਹੀਂ ਕਰਦਾ। | 2 |
| **15.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਤੀਜੀ-ਧਿਰ ਘਟਕ ਅਤੇ ਉਹਨਾਂ ਦੀਆਂ ਸਾਰੀਆਂ ਟ੍ਰਾਂਜ਼ਿਟਿਵ ਨਿਰਭਰਤਾਵਾਂ (transitive dependencies) ਉਮੀਦ ਕੀਤੀ ਰਿਪੋਜ਼ਟਰੀ ਤੋਂ ਸ਼ਾਮਲ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ, ਭਾਵੇਂ ਉਹ ਅੰਦਰੂਨੀ ਮਲਕੀਅਤ ਵਾਲੀ ਹੋਵੇ ਜਾਂ ਕੋਈ ਬਾਹਰੀ ਸਰੋਤ, ਅਤੇ ਇਹ ਕਿ ਨਿਰਭਰਤਾ ਉਲਝਣ (dependency confusion) ਹਮਲੇ ਦਾ ਕੋਈ ਜੋਖਮ ਨਹੀਂ ਹੈ। | 3 |
| **15.2.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਆਪਣੇ ਉਹਨਾਂ ਹਿੱਸਿਆਂ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਵਾਧੂ ਸੁਰੱਖਿਆਵਾਂ ਲਾਗੂ ਕਰਦੀ ਹੈ ਜੋ "ਖ਼ਤਰਨਾਕ ਕਾਰਜਸ਼ੀਲਤਾ" ਰੱਖਣ ਵਾਲੇ ਜਾਂ "ਜੋਖਮ ਭਰੇ ਘਟਕ" ਮੰਨੀਆਂ ਜਾਂਦੀਆਂ ਤੀਜੀ-ਧਿਰ ਲਾਇਬ੍ਰੇਰੀਆਂ ਵਰਤਣ ਵਾਲੇ ਵਜੋਂ ਦਸਤਾਵੇਜ਼ੀ ਹਨ। ਇਸ ਵਿੱਚ ਸੈਂਡਬਾਕਸਿੰਗ, ਇਨਕੈਪਸੂਲੇਸ਼ਨ, ਕੰਟੇਨਰਾਈਜ਼ੇਸ਼ਨ ਜਾਂ ਨੈੱਟਵਰਕ-ਪੱਧਰ ਅਲਹਿਦਗੀ ਵਰਗੀਆਂ ਤਕਨੀਕਾਂ ਸ਼ਾਮਲ ਹੋ ਸਕਦੀਆਂ ਹਨ ਤਾਂ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਇੱਕ ਹਿੱਸੇ ਨਾਲ ਸਮਝੌਤਾ ਕਰਨ ਵਾਲੇ ਹਮਲਾਵਰਾਂ ਨੂੰ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਹੋਰ ਕਿਤੇ ਪਿਵਟ ਕਰਨ (pivoting) ਤੋਂ ਦੇਰੀ ਅਤੇ ਨਿਰਉਤਸ਼ਾਹਿਤ ਕੀਤਾ ਜਾ ਸਕੇ। | 3 |

## V15.3 Defensive Coding
## V15.3 ਰੱਖਿਆਤਮਕ ਕੋਡਿੰਗ

This section covers vulnerability types, including type juggling, prototype pollution, and others, which result from using insecure coding patterns in a particular language. Some may not be relevant to all languages, whereas others will have language-specific fixes or may relate to how a particular language or framework handles a feature such as HTTP parameters. It also considers the risk of not cryptographically validating application updates.

ਇਹ ਭਾਗ ਕਮਜ਼ੋਰੀ ਕਿਸਮਾਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਟਾਈਪ ਜਗਲਿੰਗ (type juggling), ਪ੍ਰੋਟੋਟਾਈਪ ਪ੍ਰਦੂਸ਼ਣ (prototype pollution), ਅਤੇ ਹੋਰ ਸ਼ਾਮਲ ਹਨ, ਜੋ ਕਿਸੇ ਖ਼ਾਸ ਭਾਸ਼ਾ ਵਿੱਚ ਅਸੁਰੱਖਿਅਤ ਕੋਡਿੰਗ ਪੈਟਰਨ ਵਰਤਣ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਪੈਦਾ ਹੁੰਦੀਆਂ ਹਨ। ਕੁਝ ਸ਼ਾਇਦ ਸਾਰੀਆਂ ਭਾਸ਼ਾਵਾਂ ਲਈ ਢੁਕਵੀਆਂ ਨਾ ਹੋਣ, ਜਦੋਂ ਕਿ ਹੋਰਾਂ ਦੇ ਭਾਸ਼ਾ-ਵਿਸ਼ੇਸ਼ ਹੱਲ ਹੋਣਗੇ ਜਾਂ ਉਹ ਇਸ ਨਾਲ ਸੰਬੰਧਿਤ ਹੋ ਸਕਦੀਆਂ ਹਨ ਕਿ ਕੋਈ ਖ਼ਾਸ ਭਾਸ਼ਾ ਜਾਂ ਫ੍ਰੇਮਵਰਕ (framework) ਕਿਸੇ ਵਿਸ਼ੇਸ਼ਤਾ, ਜਿਵੇਂ ਕਿ HTTP ਪੈਰਾਮੀਟਰਾਂ, ਨੂੰ ਕਿਵੇਂ ਸੰਭਾਲਦਾ ਹੈ। ਇਹ ਐਪਲੀਕੇਸ਼ਨ ਅੱਪਡੇਟਾਂ ਨੂੰ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਤੌਰ 'ਤੇ ਪ੍ਰਮਾਣਿਤ ਨਾ ਕਰਨ ਦੇ ਜੋਖਮ 'ਤੇ ਵੀ ਵਿਚਾਰ ਕਰਦਾ ਹੈ।

It also considers the risks associated with using objects to represent data items and accepting and returning these via external APIs. In this case, the application must ensure that data fields that should not be writable are not modified by user input (mass assignment) and that the API is selective about what data fields get returned. Where field access depends on a user's permissions, this should be considered in the context of the field-level access control requirement in the Authorization chapter.

ਇਹ ਡਾਟਾ ਇਕਾਈਆਂ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਆਬਜੈਕਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਅਤੇ ਇਹਨਾਂ ਨੂੰ ਬਾਹਰੀ API ਰਾਹੀਂ ਸਵੀਕਾਰ ਕਰਨ ਅਤੇ ਵਾਪਸ ਕਰਨ ਨਾਲ ਜੁੜੇ ਜੋਖਮਾਂ 'ਤੇ ਵੀ ਵਿਚਾਰ ਕਰਦਾ ਹੈ। ਇਸ ਸਥਿਤੀ ਵਿੱਚ, ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਜਿਹੜੇ ਡਾਟਾ ਖੇਤਰ (fields) ਲਿਖਣਯੋਗ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ ਉਹ ਉਪਭੋਗਤਾ ਇਨਪੁੱਟ ਦੁਆਰਾ ਸੋਧੇ ਨਾ ਜਾਣ (ਮਾਸ ਅਸਾਈਨਮੈਂਟ, mass assignment) ਅਤੇ ਇਹ ਕਿ API ਇਸ ਬਾਰੇ ਚੋਣਵੀਂ ਹੈ ਕਿ ਕਿਹੜੇ ਡਾਟਾ ਖੇਤਰ ਵਾਪਸ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। ਜਿੱਥੇ ਖੇਤਰ ਪਹੁੰਚ ਉਪਭੋਗਤਾ ਦੀਆਂ ਇਜਾਜ਼ਤਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ, ਉੱਥੇ ਇਸ 'ਤੇ "ਅਧਿਕਾਰੀਕਰਨ" (Authorization) ਅਧਿਆਇ ਵਿਚਲੀ ਖੇਤਰ-ਪੱਧਰ ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਲੋੜ ਦੇ ਸੰਦਰਭ ਵਿੱਚ ਵਿਚਾਰ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **15.3.1** | Verify that the application only returns the required subset of fields from a data object. For example, it should not return an entire data object, as some individual fields should not be accessible to users. | 1 |
| **15.3.2** | Verify that where the application backend makes calls to external URLs, it is configured to not follow redirects unless it is intended functionality. | 2 |
| **15.3.3** | Verify that the application has countermeasures to protect against mass assignment attacks by limiting allowed fields per controller and action, e.g., it is not possible to insert or update a field value when it was not intended to be part of that action. | 2 |
| **15.3.4** | Verify that all proxying and middleware components transfer the user's original IP address correctly using trusted data fields that cannot be manipulated by the end user, and the application and web server use this correct value for logging and security decisions such as rate limiting, taking into account that even the original IP address may not be reliable due to dynamic IPs, VPNs, or corporate firewalls. | 2 |
| **15.3.5** | Verify that the application explicitly ensures that variables are of the correct type and performs strict equality and comparator operations. This is to avoid type juggling or type confusion vulnerabilities caused by the application code making an assumption about a variable type. | 2 |
| **15.3.6** | Verify that JavaScript code is written in a way that prevents prototype pollution, for example, by using Set() or Map() instead of object literals. | 2 |
| **15.3.7** | Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (query string, body parameters, cookies, or header fields). | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **15.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਕਿਸੇ ਡਾਟਾ ਆਬਜੈਕਟ ਤੋਂ ਸਿਰਫ਼ ਖੇਤਰਾਂ ਦਾ ਲੋੜੀਂਦਾ ਉਪ-ਸਮੂਹ ਹੀ ਵਾਪਸ ਕਰਦੀ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਇਸ ਨੂੰ ਪੂਰਾ ਡਾਟਾ ਆਬਜੈਕਟ ਵਾਪਸ ਨਹੀਂ ਕਰਨਾ ਚਾਹੀਦਾ, ਕਿਉਂਕਿ ਕੁਝ ਵਿਅਕਤੀਗਤ ਖੇਤਰ ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਪਹੁੰਚਯੋਗ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ। | 1 |
| **15.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਿੱਥੇ ਐਪਲੀਕੇਸ਼ਨ ਬੈਕਐਂਡ ਬਾਹਰੀ URL ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ, ਉੱਥੇ ਇਸ ਨੂੰ ਰੀਡਾਇਰੈਕਟਾਂ ਦਾ ਪਾਲਣ ਨਾ ਕਰਨ ਲਈ ਕੌਨਫ਼ਿਗਰ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਦੋਂ ਤੱਕ ਇਹ ਇੱਛਿਤ ਕਾਰਜਸ਼ੀਲਤਾ ਨਾ ਹੋਵੇ। | 2 |
| **15.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਕੋਲ ਪ੍ਰਤੀ ਕੰਟਰੋਲਰ ਅਤੇ ਐਕਸ਼ਨ ਇਜਾਜ਼ਤ ਪ੍ਰਾਪਤ ਖੇਤਰਾਂ ਨੂੰ ਸੀਮਤ ਕਰਕੇ ਮਾਸ ਅਸਾਈਨਮੈਂਟ ਹਮਲਿਆਂ ਤੋਂ ਬਚਾਅ ਲਈ ਜਵਾਬੀ ਉਪਾਅ ਹਨ, ਜਿਵੇਂ ਕਿ, ਕਿਸੇ ਖੇਤਰ ਦੇ ਮੁੱਲ ਨੂੰ ਸ਼ਾਮਲ ਕਰਨਾ ਜਾਂ ਅੱਪਡੇਟ ਕਰਨਾ ਸੰਭਵ ਨਹੀਂ ਹੈ ਜਦੋਂ ਉਸ ਦਾ ਉਸ ਐਕਸ਼ਨ ਦਾ ਹਿੱਸਾ ਹੋਣਾ ਇੱਛਿਤ ਨਹੀਂ ਸੀ। | 2 |
| **15.3.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਾਰੇ ਪ੍ਰੌਕਸੀ ਅਤੇ ਮਿਡਲਵੇਅਰ ਘਟਕ ਉਪਭੋਗਤਾ ਦੇ ਅਸਲ IP ਪਤੇ ਨੂੰ ਅਜਿਹੇ ਭਰੋਸੇਯੋਗ ਡਾਟਾ ਖੇਤਰਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਹੀ ਢੰਗ ਨਾਲ ਅੱਗੇ ਭੇਜਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਨਾਲ ਅੰਤਮ ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਹੇਰਾਫੇਰੀ ਨਹੀਂ ਕੀਤੀ ਜਾ ਸਕਦੀ, ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਅਤੇ ਵੈੱਬ ਸਰਵਰ ਇਸ ਸਹੀ ਮੁੱਲ ਦੀ ਵਰਤੋਂ ਲੌਗਿੰਗ ਅਤੇ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ, ਜਿਵੇਂ ਕਿ ਦਰ ਸੀਮਾ (rate limiting), ਲਈ ਕਰਦੇ ਹਨ, ਇਹ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ ਕਿ ਗਤੀਸ਼ੀਲ IP, VPN, ਜਾਂ ਕਾਰਪੋਰੇਟ ਫ਼ਾਇਰਵਾਲਾਂ ਕਾਰਨ ਅਸਲ IP ਪਤਾ ਵੀ ਭਰੋਸੇਯੋਗ ਨਹੀਂ ਹੋ ਸਕਦਾ। | 2 |
| **15.3.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਵੇਰੀਏਬਲ ਸਹੀ ਕਿਸਮ (type) ਦੇ ਹਨ ਅਤੇ ਸਖ਼ਤ ਸਮਾਨਤਾ (strict equality) ਅਤੇ ਤੁਲਨਾਕਾਰ (comparator) ਕਾਰਵਾਈਆਂ ਕਰਦੀ ਹੈ। ਇਹ ਐਪਲੀਕੇਸ਼ਨ ਕੋਡ ਦੁਆਰਾ ਵੇਰੀਏਬਲ ਕਿਸਮ ਬਾਰੇ ਧਾਰਨਾ ਬਣਾਉਣ ਕਾਰਨ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਟਾਈਪ ਜਗਲਿੰਗ ਜਾਂ ਟਾਈਪ ਉਲਝਣ (type confusion) ਕਮਜ਼ੋਰੀਆਂ ਤੋਂ ਬਚਣ ਲਈ ਹੈ। | 2 |
| **15.3.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ JavaScript ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਲਿਖਿਆ ਗਿਆ ਹੈ ਜੋ ਪ੍ਰੋਟੋਟਾਈਪ ਪ੍ਰਦੂਸ਼ਣ ਨੂੰ ਰੋਕਦਾ ਹੈ, ਉਦਾਹਰਨ ਲਈ, ਆਬਜੈਕਟ ਲਿਟਰਲਾਂ (object literals) ਦੀ ਬਜਾਏ Set() ਜਾਂ Map() ਦੀ ਵਰਤੋਂ ਕਰਕੇ। | 2 |
| **15.3.7** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਕੋਲ HTTP ਪੈਰਾਮੀਟਰ ਪ੍ਰਦੂਸ਼ਣ (HTTP parameter pollution) ਹਮਲਿਆਂ ਵਿਰੁੱਧ ਰੱਖਿਆਵਾਂ ਹਨ, ਖ਼ਾਸ ਕਰਕੇ ਜੇ ਐਪਲੀਕੇਸ਼ਨ ਫ੍ਰੇਮਵਰਕ ਬੇਨਤੀ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਸਰੋਤ (ਕਿਊਰੀ ਸਟ੍ਰਿੰਗ, ਬਾਡੀ ਪੈਰਾਮੀਟਰ, ਕੁਕੀਆਂ, ਜਾਂ ਹੈੱਡਰ ਖੇਤਰ) ਬਾਰੇ ਕੋਈ ਫ਼ਰਕ ਨਹੀਂ ਕਰਦਾ। | 2 |

## V15.4 Safe Concurrency
## V15.4 ਸੁਰੱਖਿਅਤ ਸਮਕਾਲੀਨਤਾ

Concurrency issues such as race conditions, time-of-check to time-of-use (TOCTOU) vulnerabilities, deadlocks, livelocks, thread starvation, and improper synchronization can lead to unpredictable behavior and security risks. This section includes various techniques and strategies to help mitigate these risks.

ਸਮਕਾਲੀਨਤਾ (concurrency) ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ, ਜਿਵੇਂ ਕਿ ਰੇਸ ਕੰਡੀਸ਼ਨਾਂ (race conditions), ਜਾਂਚ-ਦੇ-ਸਮੇਂ ਤੋਂ ਵਰਤੋਂ-ਦੇ-ਸਮੇਂ (time-of-check to time-of-use, TOCTOU) ਕਮਜ਼ੋਰੀਆਂ, ਡੈੱਡਲਾਕ (deadlocks), ਲਾਈਵਲਾਕ (livelocks), ਥ੍ਰੈੱਡ ਸਟਾਰਵੇਸ਼ਨ (thread starvation), ਅਤੇ ਗ਼ਲਤ ਸਿੰਕ੍ਰੋਨਾਈਜ਼ੇਸ਼ਨ (synchronization), ਅਣਕਿਆਸੇ ਵਿਵਹਾਰ ਅਤੇ ਸੁਰੱਖਿਆ ਜੋਖਮਾਂ ਵੱਲ ਲੈ ਜਾ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਭਾਗ ਵਿੱਚ ਇਹਨਾਂ ਜੋਖਮਾਂ ਨੂੰ ਘਟਾਉਣ ਵਿੱਚ ਮਦਦ ਲਈ ਵੱਖ-ਵੱਖ ਤਕਨੀਕਾਂ ਅਤੇ ਰਣਨੀਤੀਆਂ ਸ਼ਾਮਲ ਹਨ।

| # | Description | Level |
| :---: | :--- | :---: |
| **15.4.1** | Verify that shared objects in multi-threaded code (such as caches, files, or in-memory objects accessed by multiple threads) are accessed safely by using thread-safe types and synchronization mechanisms like locks or semaphores to avoid race conditions and data corruption. | 3 |
| **15.4.2** | Verify that checks on a resource's state, such as its existence or permissions, and the actions that depend on them are performed as a single atomic operation to prevent time-of-check to time-of-use (TOCTOU) race conditions. For example, checking if a file exists before opening it, or verifying a user’s access before granting it. | 3 |
| **15.4.3** | Verify that locks are used consistently to avoid threads getting stuck, whether by waiting on each other or retrying endlessly, and that locking logic stays within the code responsible for managing the resource to ensure locks cannot be inadvertently or maliciously modified by external classes or code. | 3 |
| **15.4.4** | Verify that resource allocation policies prevent thread starvation by ensuring fair access to resources, such as by leveraging thread pools, allowing lower-priority threads to proceed within a reasonable timeframe. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **15.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਬਹੁ-ਥ੍ਰੈੱਡ ਕੋਡ ਵਿੱਚ ਸਾਂਝੇ ਆਬਜੈਕਟਾਂ (ਜਿਵੇਂ ਕਿ ਕੈਸ਼, ਫ਼ਾਈਲਾਂ, ਜਾਂ ਕਈ ਥ੍ਰੈੱਡਾਂ ਦੁਆਰਾ ਪਹੁੰਚ ਕੀਤੇ ਜਾਂਦੇ ਇਨ-ਮੈਮੋਰੀ ਆਬਜੈਕਟ) ਤੱਕ ਰੇਸ ਕੰਡੀਸ਼ਨਾਂ ਅਤੇ ਡਾਟਾ ਖ਼ਰਾਬ ਹੋਣ (data corruption) ਤੋਂ ਬਚਣ ਲਈ ਥ੍ਰੈੱਡ-ਸੁਰੱਖਿਅਤ ਕਿਸਮਾਂ ਅਤੇ ਲਾਕ ਜਾਂ ਸੇਮਾਫ਼ੋਰ ਵਰਗੀਆਂ ਸਿੰਕ੍ਰੋਨਾਈਜ਼ੇਸ਼ਨ ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਪਹੁੰਚ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। | 3 |
| **15.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਕਿਸੇ ਸਰੋਤ ਦੀ ਸਥਿਤੀ, ਜਿਵੇਂ ਕਿ ਉਸ ਦੀ ਹੋਂਦ ਜਾਂ ਇਜਾਜ਼ਤਾਂ, ਦੀਆਂ ਜਾਂਚਾਂ ਅਤੇ ਉਹਨਾਂ 'ਤੇ ਨਿਰਭਰ ਕਾਰਵਾਈਆਂ ਇੱਕੋ ਅਟੁੱਟ (atomic) ਕਾਰਵਾਈ ਵਜੋਂ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ ਤਾਂ ਜੋ ਜਾਂਚ-ਦੇ-ਸਮੇਂ ਤੋਂ ਵਰਤੋਂ-ਦੇ-ਸਮੇਂ (TOCTOU) ਰੇਸ ਕੰਡੀਸ਼ਨਾਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। ਉਦਾਹਰਨ ਲਈ, ਕਿਸੇ ਫ਼ਾਈਲ ਨੂੰ ਖੋਲ੍ਹਣ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਜਾਂਚਣਾ ਕਿ ਉਹ ਮੌਜੂਦ ਹੈ, ਜਾਂ ਉਪਭੋਗਤਾ ਦੀ ਪਹੁੰਚ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ ਉਸ ਦੀ ਤਸਦੀਕ ਕਰਨਾ। | 3 |
| **15.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਥ੍ਰੈੱਡਾਂ ਦੇ ਫਸ ਜਾਣ ਤੋਂ ਬਚਣ ਲਈ ਲਾਕਾਂ ਦੀ ਵਰਤੋਂ ਇਕਸਾਰ ਢੰਗ ਨਾਲ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਭਾਵੇਂ ਉਹ ਇੱਕ-ਦੂਜੇ ਦੀ ਉਡੀਕ ਕਰਕੇ ਫਸਣ ਜਾਂ ਬੇਅੰਤ ਮੁੜ-ਕੋਸ਼ਿਸ਼ ਕਰਕੇ, ਅਤੇ ਇਹ ਕਿ ਲਾਕਿੰਗ ਤਰਕ ਸਰੋਤ ਦੇ ਪ੍ਰਬੰਧਨ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਕੋਡ ਦੇ ਅੰਦਰ ਹੀ ਰਹਿੰਦਾ ਹੈ ਤਾਂ ਜੋ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਲਾਕਾਂ ਨੂੰ ਬਾਹਰੀ ਕਲਾਸਾਂ ਜਾਂ ਕੋਡ ਦੁਆਰਾ ਅਣਜਾਣੇ ਵਿੱਚ ਜਾਂ ਦੁਰਭਾਵਨਾਪੂਰਨ ਢੰਗ ਨਾਲ ਸੋਧਿਆ ਨਹੀਂ ਜਾ ਸਕਦਾ। | 3 |
| **15.4.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਰੋਤ ਵੰਡ ਨੀਤੀਆਂ ਸਰੋਤਾਂ ਤੱਕ ਨਿਰਪੱਖ ਪਹੁੰਚ ਯਕੀਨੀ ਬਣਾ ਕੇ ਥ੍ਰੈੱਡ ਸਟਾਰਵੇਸ਼ਨ ਨੂੰ ਰੋਕਦੀਆਂ ਹਨ, ਜਿਵੇਂ ਕਿ ਥ੍ਰੈੱਡ ਪੂਲਾਂ ਦਾ ਲਾਭ ਉਠਾ ਕੇ, ਜਿਸ ਨਾਲ ਘੱਟ-ਤਰਜੀਹ ਵਾਲੇ ਥ੍ਰੈੱਡ ਇੱਕ ਵਾਜਬ ਸਮਾਂ-ਮਿਆਦ ਦੇ ਅੰਦਰ ਅੱਗੇ ਵਧ ਸਕਦੇ ਹਨ। | 3 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP Prototype Pollution Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [OWASP CycloneDX Bill of Materials Specification](https://owasp.org/www-project-cyclonedx/)
* [OWASP Web Security Testing Guide: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution)
