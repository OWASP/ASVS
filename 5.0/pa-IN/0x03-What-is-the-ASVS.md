<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x03-What-is-the-ASVS.md -->
<!-- Translator: GeeksikhSecurity -->

# What is the ASVS?
# ASVS ਕੀ ਹੈ?

The Application Security Verification Standard (ASVS) defines security requirements for web applications and services, and it is a valuable resource for anyone aiming to design, develop, and maintain secure applications or evaluate their security.

ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਤਸਦੀਕ ਮਿਆਰ (Application Security Verification Standard, ASVS) ਵੈੱਬ ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਲਈ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ, ਅਤੇ ਇਹ ਹਰ ਉਸ ਵਿਅਕਤੀ ਲਈ ਇੱਕ ਕੀਮਤੀ ਸਰੋਤ ਹੈ ਜੋ ਸੁਰੱਖਿਅਤ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਡਿਜ਼ਾਈਨ ਕਰਨ, ਵਿਕਸਿਤ ਕਰਨ ਅਤੇ ਬਣਾਈ ਰੱਖਣ, ਜਾਂ ਉਹਨਾਂ ਦੀ ਸੁਰੱਖਿਆ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਦਾ ਟੀਚਾ ਰੱਖਦਾ ਹੈ।

This chapter outlines the essential aspects of using the ASVS, including its scope, the structure of its priority-based levels, and the primary use cases for the standard.

ਇਹ ਅਧਿਆਇ ASVS ਦੀ ਵਰਤੋਂ ਦੇ ਜ਼ਰੂਰੀ ਪਹਿਲੂਆਂ ਦੀ ਰੂਪਰੇਖਾ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਇਸ ਦਾ ਘੇਰਾ (scope), ਇਸ ਦੇ ਤਰਜੀਹ-ਆਧਾਰਿਤ ਪੱਧਰਾਂ (levels) ਦੀ ਬਣਤਰ, ਅਤੇ ਮਿਆਰ ਦੇ ਮੁੱਖ ਵਰਤੋਂ ਦੇ ਮਾਮਲੇ ਸ਼ਾਮਲ ਹਨ।

## Scope of the ASVS
## ASVS ਦਾ ਘੇਰਾ

The scope of the ASVS is defined by its name: Application, Security, Verification, and Standard. It establishes which requirements are included or excluded, with the overarching goal of identifying the security principles that must be achieved. The scope also considers documentation requirements, which serve as the foundation for implementation requirements.

ASVS ਦਾ ਘੇਰਾ ਇਸ ਦੇ ਨਾਂ ਦੁਆਰਾ ਪਰਿਭਾਸ਼ਿਤ ਹੁੰਦਾ ਹੈ: ਐਪਲੀਕੇਸ਼ਨ (Application), ਸੁਰੱਖਿਆ (Security), ਤਸਦੀਕ (Verification), ਅਤੇ ਮਿਆਰ (Standard)। ਇਹ ਸਥਾਪਿਤ ਕਰਦਾ ਹੈ ਕਿ ਕਿਹੜੀਆਂ ਲੋੜਾਂ ਸ਼ਾਮਲ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ ਜਾਂ ਬਾਹਰ ਰੱਖੀਆਂ ਜਾਂਦੀਆਂ ਹਨ, ਜਿਸ ਦਾ ਸਰਬ-ਵਿਆਪਕ ਟੀਚਾ ਉਹਨਾਂ ਸੁਰੱਖਿਆ ਸਿਧਾਂਤਾਂ ਦੀ ਪਛਾਣ ਕਰਨਾ ਹੈ ਜੋ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਪ੍ਰਾਪਤ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ। ਘੇਰਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲੋੜਾਂ (documentation requirements) ਨੂੰ ਵੀ ਵਿਚਾਰਦਾ ਹੈ, ਜੋ ਲਾਗੂਕਰਨ ਲੋੜਾਂ ਦੀ ਨੀਂਹ ਵਜੋਂ ਕੰਮ ਕਰਦੀਆਂ ਹਨ।

There is no such thing as scope for attackers. Therefore, ASVS requirements should be evaluated alongside guidance for other aspects of the application lifecycle, including CI/CD processes, hosting, and operational activities.

ਹਮਲਾਵਰਾਂ ਲਈ ਘੇਰਾ ਵਰਗੀ ਕੋਈ ਚੀਜ਼ ਨਹੀਂ ਹੁੰਦੀ। ਇਸ ਲਈ, ASVS ਲੋੜਾਂ ਦਾ ਮੁਲਾਂਕਣ ਐਪਲੀਕੇਸ਼ਨ ਜੀਵਨ-ਚੱਕਰ ਦੇ ਹੋਰ ਪਹਿਲੂਆਂ ਲਈ ਮਾਰਗਦਰਸ਼ਨ ਦੇ ਨਾਲ-ਨਾਲ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ CI/CD ਪ੍ਰਕਿਰਿਆਵਾਂ, ਹੋਸਟਿੰਗ, ਅਤੇ ਸੰਚਾਲਨ ਸੰਬੰਧੀ ਗਤੀਵਿਧੀਆਂ ਸ਼ਾਮਲ ਹਨ।

### Application
### ਐਪਲੀਕੇਸ਼ਨ

ASVS defines an "application" as the software product being developed, into which security controls must be integrated. ASVS does not prescribe development lifecycle activities or dictate how the application should be built via a CI/CD pipeline; instead, it specifies the security outcomes that must be achieved within the product itself.

ASVS ਇੱਕ "ਐਪਲੀਕੇਸ਼ਨ" ਨੂੰ ਉਸ ਸਾਫ਼ਟਵੇਅਰ ਉਤਪਾਦ ਵਜੋਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਵਿਕਸਿਤ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ, ਅਤੇ ਜਿਸ ਵਿੱਚ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣਾਂ (security controls) ਨੂੰ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਏਕੀਕ੍ਰਿਤ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ASVS ਵਿਕਾਸ ਜੀਵਨ-ਚੱਕਰ ਦੀਆਂ ਗਤੀਵਿਧੀਆਂ ਨੂੰ ਨਿਰਧਾਰਿਤ ਨਹੀਂ ਕਰਦਾ ਅਤੇ ਨਾ ਹੀ ਇਹ ਤੈਅ ਕਰਦਾ ਹੈ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ CI/CD ਪਾਈਪਲਾਈਨ ਰਾਹੀਂ ਕਿਵੇਂ ਬਣਾਇਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ; ਇਸ ਦੀ ਬਜਾਏ, ਇਹ ਉਹਨਾਂ ਸੁਰੱਖਿਆ ਨਤੀਜਿਆਂ ਨੂੰ ਨਿਰਧਾਰਿਤ ਕਰਦਾ ਹੈ ਜੋ ਉਤਪਾਦ ਦੇ ਅੰਦਰ ਹੀ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਪ੍ਰਾਪਤ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ।

Components that serve, modify, or validate HTTP traffic, such as Web Application Firewalls (WAFs), load balancers, or proxies, may be considered part of the application for those specific purposes, as some security controls depend directly on them or can be implemented through them. These components should be considered for requirements related to cached responses, rate limiting, or restricting incoming and outgoing connections based on source and destination.

ਉਹ ਹਿੱਸੇ ਜੋ HTTP ਟ੍ਰੈਫ਼ਿਕ ਨੂੰ ਪਰੋਸਦੇ, ਸੋਧਦੇ, ਜਾਂ ਪ੍ਰਮਾਣਿਤ ਕਰਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਵੈੱਬ ਐਪਲੀਕੇਸ਼ਨ ਫ਼ਾਇਰਵਾਲ (WAF), ਲੋਡ ਬੈਲੈਂਸਰ, ਜਾਂ ਪ੍ਰਾਕਸੀ, ਉਹਨਾਂ ਖ਼ਾਸ ਉਦੇਸ਼ਾਂ ਲਈ ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਹਿੱਸਾ ਮੰਨੇ ਜਾ ਸਕਦੇ ਹਨ, ਕਿਉਂਕਿ ਕੁਝ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਸਿੱਧੇ ਉਹਨਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ ਜਾਂ ਉਹਨਾਂ ਰਾਹੀਂ ਲਾਗੂ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਇਹਨਾਂ ਹਿੱਸਿਆਂ ਨੂੰ ਕੈਸ਼ ਕੀਤੇ ਜਵਾਬਾਂ, ਦਰ ਸੀਮਾ (rate limiting), ਜਾਂ ਸਰੋਤ ਅਤੇ ਮੰਜ਼ਿਲ ਦੇ ਆਧਾਰ 'ਤੇ ਅੰਦਰ-ਆਉਣ ਵਾਲੇ ਅਤੇ ਬਾਹਰ-ਜਾਣ ਵਾਲੇ ਸੰਪਰਕਾਂ ਨੂੰ ਪ੍ਰਤਿਬੰਧਿਤ ਕਰਨ ਨਾਲ ਸੰਬੰਧਿਤ ਲੋੜਾਂ ਲਈ ਵਿਚਾਰਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

Conversely, ASVS generally excludes requirements that are not directly relevant to the application or where configuration is outside the application's responsibility. For example, DNS issues are typically managed by a separate team or function.

ਇਸ ਦੇ ਉਲਟ, ASVS ਆਮ ਤੌਰ 'ਤੇ ਉਹਨਾਂ ਲੋੜਾਂ ਨੂੰ ਬਾਹਰ ਰੱਖਦਾ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਨਾਲ ਸਿੱਧੇ ਤੌਰ 'ਤੇ ਸੰਬੰਧਿਤ ਨਹੀਂ ਹਨ ਜਾਂ ਜਿੱਥੇ ਸੰਰਚਨਾ (configuration) ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਜ਼ਿੰਮੇਵਾਰੀ ਤੋਂ ਬਾਹਰ ਹੈ। ਉਦਾਹਰਨ ਲਈ, DNS ਮੁੱਦਿਆਂ ਦਾ ਪ੍ਰਬੰਧਨ ਆਮ ਤੌਰ 'ਤੇ ਇੱਕ ਵੱਖਰੀ ਟੀਮ ਜਾਂ ਕਾਰਜ-ਇਕਾਈ ਦੁਆਰਾ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

Similarly, while the application is responsible for how it consumes input and produces output, if an external process interacts with the application or its data, it is considered out of scope for ASVS. For instance, backing up the application or its data is usually the responsibility of an external process and is not controlled by the application or its developers.

ਇਸੇ ਤਰ੍ਹਾਂ, ਭਾਵੇਂ ਐਪਲੀਕੇਸ਼ਨ ਇਸ ਗੱਲ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਹੈ ਕਿ ਉਹ ਇਨਪੁੱਟ ਨੂੰ ਕਿਵੇਂ ਖਪਤ ਕਰਦੀ ਹੈ ਅਤੇ ਆਊਟਪੁੱਟ ਕਿਵੇਂ ਪੈਦਾ ਕਰਦੀ ਹੈ, ਜੇਕਰ ਕੋਈ ਬਾਹਰੀ ਪ੍ਰਕਿਰਿਆ ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ ਇਸ ਦੇ ਡਾਟੇ ਨਾਲ ਆਪਸੀ ਤਾਲਮੇਲ ਕਰਦੀ ਹੈ, ਤਾਂ ਉਸ ਨੂੰ ASVS ਦੇ ਘੇਰੇ ਤੋਂ ਬਾਹਰ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ। ਮਿਸਾਲ ਵਜੋਂ, ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ ਇਸ ਦੇ ਡਾਟੇ ਦਾ ਬੈਕਅੱਪ ਲੈਣਾ ਆਮ ਤੌਰ 'ਤੇ ਇੱਕ ਬਾਹਰੀ ਪ੍ਰਕਿਰਿਆ ਦੀ ਜ਼ਿੰਮੇਵਾਰੀ ਹੁੰਦੀ ਹੈ ਅਤੇ ਇਹ ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ ਇਸ ਦੇ ਵਿਕਾਸਕਾਰਾਂ ਦੁਆਰਾ ਨਿਯੰਤਰਿਤ ਨਹੀਂ ਹੁੰਦੀ।

### Security
### ਸੁਰੱਖਿਆ

Every requirement must have a demonstrable impact on security. The absence of a requirement must result in a less secure application, and implementing the requirement must reduce either the likelihood or the impact of a security risk.

ਹਰ ਲੋੜ ਦਾ ਸੁਰੱਖਿਆ 'ਤੇ ਇੱਕ ਪ੍ਰਦਰਸ਼ਨਯੋਗ ਪ੍ਰਭਾਵ ਹੋਣਾ ਲਾਜ਼ਮੀ ਹੈ। ਕਿਸੇ ਲੋੜ ਦੀ ਗ਼ੈਰ-ਮੌਜੂਦਗੀ ਦਾ ਨਤੀਜਾ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਇੱਕ ਘੱਟ ਸੁਰੱਖਿਅਤ ਐਪਲੀਕੇਸ਼ਨ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ, ਅਤੇ ਲੋੜ ਨੂੰ ਲਾਗੂ ਕਰਨ ਨਾਲ ਕਿਸੇ ਸੁਰੱਖਿਆ ਜੋਖਮ (risk) ਦੀ ਸੰਭਾਵਨਾ ਜਾਂ ਉਸ ਦੇ ਪ੍ਰਭਾਵ ਵਿੱਚੋਂ ਕਿਸੇ ਇੱਕ ਦਾ ਘਟਣਾ ਲਾਜ਼ਮੀ ਹੈ।

All other considerations, such as functional aspects, code style, or policy requirements, are out of scope.

ਹੋਰ ਸਾਰੇ ਵਿਚਾਰ, ਜਿਵੇਂ ਕਿ ਕਾਰਜਾਤਮਕ ਪਹਿਲੂ, ਕੋਡ ਸ਼ੈਲੀ, ਜਾਂ ਨੀਤੀ ਸੰਬੰਧੀ ਲੋੜਾਂ, ਘੇਰੇ ਤੋਂ ਬਾਹਰ ਹਨ।

### Verification
### ਤਸਦੀਕ

The requirement must be verifiable, and the verification must result in a "fail" or "pass" decision.

ਲੋੜ ਤਸਦੀਕਯੋਗ ਹੋਣੀ ਲਾਜ਼ਮੀ ਹੈ, ਅਤੇ ਤਸਦੀਕ ਦਾ ਨਤੀਜਾ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਇੱਕ "ਅਸਫਲ" (fail) ਜਾਂ "ਸਫਲ" (pass) ਫ਼ੈਸਲਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

### Standard
### ਮਿਆਰ

The ASVS is designed to be a collection of security requirements to be implemented to comply with the standard. This means that requirements are limited to defining the security goal to achieve that. Other related information can be built on top of ASVS or linked via mappings.

ASVS ਨੂੰ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਦੇ ਇੱਕ ਸੰਗ੍ਰਹਿ ਵਜੋਂ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ ਜਿਨ੍ਹਾਂ ਨੂੰ ਮਿਆਰ ਦੀ ਪਾਲਣਾ ਕਰਨ ਲਈ ਲਾਗੂ ਕੀਤਾ ਜਾਣਾ ਹੈ। ਇਸ ਦਾ ਅਰਥ ਹੈ ਕਿ ਲੋੜਾਂ ਉਸ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਸੁਰੱਖਿਆ ਟੀਚੇ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਤੱਕ ਸੀਮਤ ਹਨ। ਹੋਰ ਸੰਬੰਧਿਤ ਜਾਣਕਾਰੀ ASVS ਦੇ ਉੱਪਰ ਬਣਾਈ ਜਾ ਸਕਦੀ ਹੈ ਜਾਂ ਮੈਪਿੰਗ ਰਾਹੀਂ ਜੋੜੀ ਜਾ ਸਕਦੀ ਹੈ।

Specifically, OWASP has many projects, and the ASVS deliberately avoids overlapping with the content in other projects. For example, developers may have a question, "how do I implement a particular requirement in my particular technology or environment," and this should be covered by the Cheat Sheet Series project. Verifiers may have a question "how do I test this requirement in this environment," and this should be covered by the Web Security Testing Guide project.

ਖ਼ਾਸ ਤੌਰ 'ਤੇ, OWASP ਦੇ ਕਈ ਪ੍ਰੋਜੈਕਟ ਹਨ, ਅਤੇ ASVS ਜਾਣ-ਬੁੱਝ ਕੇ ਹੋਰ ਪ੍ਰੋਜੈਕਟਾਂ ਦੀ ਸਮੱਗਰੀ ਨਾਲ ਓਵਰਲੈਪ ਹੋਣ ਤੋਂ ਬਚਦਾ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਵਿਕਾਸਕਾਰਾਂ ਦਾ ਇੱਕ ਸਵਾਲ ਹੋ ਸਕਦਾ ਹੈ, "ਮੈਂ ਆਪਣੀ ਖ਼ਾਸ ਤਕਨਾਲੋਜੀ ਜਾਂ ਵਾਤਾਵਰਣ ਵਿੱਚ ਇੱਕ ਖ਼ਾਸ ਲੋੜ ਨੂੰ ਕਿਵੇਂ ਲਾਗੂ ਕਰਾਂ," ਅਤੇ ਇਸ ਨੂੰ Cheat Sheet Series ਪ੍ਰੋਜੈਕਟ ਦੁਆਰਾ ਕਵਰ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਤਸਦੀਕਕਰਤਾਵਾਂ ਦਾ ਇੱਕ ਸਵਾਲ ਹੋ ਸਕਦਾ ਹੈ "ਮੈਂ ਇਸ ਵਾਤਾਵਰਣ ਵਿੱਚ ਇਸ ਲੋੜ ਨੂੰ ਕਿਵੇਂ ਟੈਸਟ ਕਰਾਂ," ਅਤੇ ਇਸ ਨੂੰ Web Security Testing Guide ਪ੍ਰੋਜੈਕਟ ਦੁਆਰਾ ਕਵਰ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

Whilst the ASVS is not just intended for security experts to use, it does expect the reader to have technical knowledge to understand the content or the ability to research particular concepts.

ਭਾਵੇਂ ASVS ਸਿਰਫ਼ ਸੁਰੱਖਿਆ ਮਾਹਰਾਂ ਦੀ ਵਰਤੋਂ ਲਈ ਹੀ ਨਹੀਂ ਬਣਾਇਆ ਗਿਆ, ਇਹ ਪਾਠਕ ਤੋਂ ਸਮੱਗਰੀ ਨੂੰ ਸਮਝਣ ਲਈ ਤਕਨੀਕੀ ਗਿਆਨ ਜਾਂ ਖ਼ਾਸ ਸੰਕਲਪਾਂ ਦੀ ਖੋਜ ਕਰਨ ਦੀ ਯੋਗਤਾ ਦੀ ਉਮੀਦ ਜ਼ਰੂਰ ਰੱਖਦਾ ਹੈ।

### Requirement
### ਲੋੜ

The word requirement is used specifically in the ASVS as it describes what must be achieved to satisfy it. The ASVS only contains requirements (must) and does not contain recommendations (should) as the main condition.

ASVS ਵਿੱਚ "ਲੋੜ" (requirement) ਸ਼ਬਦ ਦੀ ਵਰਤੋਂ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿਉਂਕਿ ਇਹ ਵਰਣਨ ਕਰਦਾ ਹੈ ਕਿ ਉਸ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਕੀ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ASVS ਵਿੱਚ ਮੁੱਖ ਸ਼ਰਤ ਵਜੋਂ ਸਿਰਫ਼ ਲੋੜਾਂ (ਲਾਜ਼ਮੀ, must) ਹੀ ਸ਼ਾਮਲ ਹਨ ਅਤੇ ਸਿਫ਼ਾਰਸ਼ਾਂ (ਚਾਹੀਦਾ, should) ਸ਼ਾਮਲ ਨਹੀਂ ਹਨ।

In other words, recommendations, whether they are just one of many possible options to solve a problem or code style considerations, do not satisfy the definition to be a requirement.

ਦੂਜੇ ਸ਼ਬਦਾਂ ਵਿੱਚ, ਸਿਫ਼ਾਰਸ਼ਾਂ, ਭਾਵੇਂ ਉਹ ਕਿਸੇ ਸਮੱਸਿਆ ਨੂੰ ਹੱਲ ਕਰਨ ਦੇ ਕਈ ਸੰਭਵ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ ਸਿਰਫ਼ ਇੱਕ ਹੋਣ ਜਾਂ ਕੋਡ ਸ਼ੈਲੀ ਸੰਬੰਧੀ ਵਿਚਾਰ ਹੋਣ, ਲੋੜ ਹੋਣ ਦੀ ਪਰਿਭਾਸ਼ਾ ਨੂੰ ਪੂਰਾ ਨਹੀਂ ਕਰਦੀਆਂ।

ASVS requirements are intended to address specific security principles without being too implementation or technology-specific, at the same time, being self-explanatory as to why they exist. This also means that requirements are not built around a particular verification method or implementation.

ASVS ਲੋੜਾਂ ਦਾ ਉਦੇਸ਼ ਬਹੁਤ ਜ਼ਿਆਦਾ ਲਾਗੂਕਰਨ- ਜਾਂ ਤਕਨਾਲੋਜੀ-ਵਿਸ਼ੇਸ਼ ਹੋਏ ਬਿਨਾਂ ਖ਼ਾਸ ਸੁਰੱਖਿਆ ਸਿਧਾਂਤਾਂ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਨਾ ਹੈ, ਅਤੇ ਨਾਲ ਹੀ ਇਸ ਬਾਰੇ ਸਵੈ-ਵਿਆਖਿਆਤਮਕ ਹੋਣਾ ਹੈ ਕਿ ਉਹ ਕਿਉਂ ਮੌਜੂਦ ਹਨ। ਇਸ ਦਾ ਇਹ ਅਰਥ ਵੀ ਹੈ ਕਿ ਲੋੜਾਂ ਕਿਸੇ ਖ਼ਾਸ ਤਸਦੀਕ ਵਿਧੀ ਜਾਂ ਲਾਗੂਕਰਨ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਨਹੀਂ ਬਣਾਈਆਂ ਗਈਆਂ।

### Documented security decisions
### ਦਸਤਾਵੇਜ਼ੀ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲੇ

In software security, planning security design and the mechanisms to be used early on will lead to a more consistent and reliable implementation in the finished product or feature.

ਸਾਫ਼ਟਵੇਅਰ ਸੁਰੱਖਿਆ ਵਿੱਚ, ਸੁਰੱਖਿਆ ਡਿਜ਼ਾਈਨ ਅਤੇ ਵਰਤੀਆਂ ਜਾਣ ਵਾਲੀਆਂ ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਯੋਜਨਾ ਸ਼ੁਰੂ ਵਿੱਚ ਹੀ ਬਣਾਉਣ ਨਾਲ ਤਿਆਰ ਉਤਪਾਦ ਜਾਂ ਫ਼ੀਚਰ ਵਿੱਚ ਵਧੇਰੇ ਇਕਸਾਰ ਅਤੇ ਭਰੋਸੇਯੋਗ ਲਾਗੂਕਰਨ ਹੋਵੇਗਾ।

Additionally, for certain requirements, implementation will be complicated and very specific to an application's needs. Common examples include permissions, input validation, and protective controls around different levels of sensitive data.

ਇਸ ਤੋਂ ਇਲਾਵਾ, ਕੁਝ ਲੋੜਾਂ ਲਈ, ਲਾਗੂਕਰਨ ਗੁੰਝਲਦਾਰ ਅਤੇ ਕਿਸੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀਆਂ ਲੋੜਾਂ ਲਈ ਬਹੁਤ ਖ਼ਾਸ ਹੋਵੇਗਾ। ਆਮ ਉਦਾਹਰਨਾਂ ਵਿੱਚ ਇਜਾਜ਼ਤਾਂ, ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ (input validation), ਅਤੇ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟੇ ਦੇ ਵੱਖ-ਵੱਖ ਪੱਧਰਾਂ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਸੁਰੱਖਿਆਤਮਕ ਨਿਯੰਤਰਣ ਸ਼ਾਮਲ ਹਨ।

To account for this, rather than sweeping statements like "all data must be encrypted" or trying to cover every possible use case in a requirement, documentation requirements were included which mandate that the application developer's approach and configuration to these sorts of controls must be documented. This can then be reviewed for appropriateness and then the actual implementation can be compared to the documentation to assess whether the implementation matches expectations.

ਇਸ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣ ਲਈ, "ਸਾਰਾ ਡਾਟਾ ਲਾਜ਼ਮੀ ਤੌਰ 'ਤੇ ਏਨਕ੍ਰਿਪਟ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ" ਵਰਗੇ ਵਿਆਪਕ ਕਥਨਾਂ ਜਾਂ ਇੱਕ ਲੋੜ ਵਿੱਚ ਹਰ ਸੰਭਵ ਵਰਤੋਂ ਦੇ ਮਾਮਲੇ ਨੂੰ ਕਵਰ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਦੀ ਬਜਾਏ, ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲੋੜਾਂ ਸ਼ਾਮਲ ਕੀਤੀਆਂ ਗਈਆਂ ਜੋ ਇਹ ਲਾਜ਼ਮੀ ਕਰਦੀਆਂ ਹਨ ਕਿ ਇਸ ਕਿਸਮ ਦੇ ਨਿਯੰਤਰਣਾਂ ਪ੍ਰਤੀ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸਕਾਰ ਦੀ ਪਹੁੰਚ ਅਤੇ ਸੰਰਚਨਾ ਨੂੰ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਦਿੱਤਾ ਜਾਵੇ। ਫਿਰ ਇਸ ਦੀ ਢੁਕਵੇਂਪਣ ਲਈ ਸਮੀਖਿਆ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ ਅਤੇ ਫਿਰ ਅਸਲ ਲਾਗੂਕਰਨ ਦੀ ਦਸਤਾਵੇਜ਼ ਨਾਲ ਤੁਲਨਾ ਕਰਕੇ ਇਹ ਮੁਲਾਂਕਣ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਕਿ ਲਾਗੂਕਰਨ ਉਮੀਦਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ ਜਾਂ ਨਹੀਂ।

These requirements are intended to document the decisions which the organization developing the application has taken regarding how to implement certain security requirements.

ਇਹਨਾਂ ਲੋੜਾਂ ਦਾ ਉਦੇਸ਼ ਉਹਨਾਂ ਫ਼ੈਸਲਿਆਂ ਨੂੰ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਦੇਣਾ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਸਿਤ ਕਰਨ ਵਾਲੀ ਸੰਸਥਾ ਨੇ ਕੁਝ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਨੂੰ ਕਿਵੇਂ ਲਾਗੂ ਕਰਨਾ ਹੈ, ਇਸ ਬਾਰੇ ਲਏ ਹਨ।

Documentation requirements are always in the first section of a chapter (although not every chapter has them) and always have a related implementation requirement where the decisions that are documented should actually be put into place. The point here is that verifying that the documentation is in place and that the actual implementation are two separate activities.

ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲੋੜਾਂ ਹਮੇਸ਼ਾ ਕਿਸੇ ਅਧਿਆਇ ਦੇ ਪਹਿਲੇ ਭਾਗ ਵਿੱਚ ਹੁੰਦੀਆਂ ਹਨ (ਹਾਲਾਂਕਿ ਹਰ ਅਧਿਆਇ ਵਿੱਚ ਇਹ ਨਹੀਂ ਹੁੰਦੀਆਂ) ਅਤੇ ਇਹਨਾਂ ਦੀ ਹਮੇਸ਼ਾ ਇੱਕ ਸੰਬੰਧਿਤ ਲਾਗੂਕਰਨ ਲੋੜ ਹੁੰਦੀ ਹੈ ਜਿੱਥੇ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਦਿੱਤੇ ਗਏ ਫ਼ੈਸਲਿਆਂ ਨੂੰ ਅਸਲ ਵਿੱਚ ਲਾਗੂ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਇੱਥੇ ਨੁਕਤਾ ਇਹ ਹੈ ਕਿ ਇਹ ਤਸਦੀਕ ਕਰਨਾ ਕਿ ਦਸਤਾਵੇਜ਼ ਮੌਜੂਦ ਹੈ ਅਤੇ ਅਸਲ ਲਾਗੂਕਰਨ ਦੀ ਤਸਦੀਕ ਕਰਨਾ, ਦੋ ਵੱਖਰੀਆਂ ਗਤੀਵਿਧੀਆਂ ਹਨ।

There are two key drivers for including these requirements. The first driver is that a security requirement will often involve enforcing rules e.g., what kind of file types are allowed to be uploaded, what business controls should be enforced, what are the allowed characters for a particular field. These rules will differ for every application, and therefore, the ASVS cannot prescriptively define what they should be, nor will a cheat sheet or more detailed response help in this case. Similarly, without these decisions being documented, it will not be possible to perform verification of the requirements that implement these decisions.

ਇਹਨਾਂ ਲੋੜਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਨ ਦੇ ਦੋ ਮੁੱਖ ਕਾਰਨ ਹਨ। ਪਹਿਲਾ ਕਾਰਨ ਇਹ ਹੈ ਕਿ ਇੱਕ ਸੁਰੱਖਿਆ ਲੋੜ ਵਿੱਚ ਅਕਸਰ ਨਿਯਮ ਲਾਗੂ ਕਰਨਾ ਸ਼ਾਮਲ ਹੋਵੇਗਾ, ਜਿਵੇਂ ਕਿ ਕਿਸ ਕਿਸਮ ਦੀਆਂ ਫ਼ਾਈਲ ਕਿਸਮਾਂ ਨੂੰ ਅੱਪਲੋਡ ਕਰਨ ਦੀ ਇਜਾਜ਼ਤ ਹੈ, ਕਿਹੜੇ ਕਾਰੋਬਾਰੀ ਨਿਯੰਤਰਣ ਲਾਗੂ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ, ਕਿਸੇ ਖ਼ਾਸ ਫ਼ੀਲਡ (field) ਲਈ ਇਜਾਜ਼ਤ ਪ੍ਰਾਪਤ ਅੱਖਰ ਕਿਹੜੇ ਹਨ। ਇਹ ਨਿਯਮ ਹਰ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਵੱਖਰੇ ਹੋਣਗੇ, ਅਤੇ ਇਸ ਲਈ, ASVS ਨਿਰਦੇਸ਼ਾਤਮਕ ਤੌਰ 'ਤੇ ਇਹ ਪਰਿਭਾਸ਼ਿਤ ਨਹੀਂ ਕਰ ਸਕਦਾ ਕਿ ਉਹ ਕੀ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ, ਅਤੇ ਨਾ ਹੀ ਇਸ ਮਾਮਲੇ ਵਿੱਚ ਕੋਈ ਚੀਟ ਸ਼ੀਟ ਜਾਂ ਵਧੇਰੇ ਵਿਸਤ੍ਰਿਤ ਜਵਾਬ ਮਦਦ ਕਰੇਗਾ। ਇਸੇ ਤਰ੍ਹਾਂ, ਇਹਨਾਂ ਫ਼ੈਸਲਿਆਂ ਨੂੰ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਦਿੱਤੇ ਬਿਨਾਂ, ਇਹਨਾਂ ਫ਼ੈਸਲਿਆਂ ਨੂੰ ਲਾਗੂ ਕਰਨ ਵਾਲੀਆਂ ਲੋੜਾਂ ਦੀ ਤਸਦੀਕ ਕਰਨਾ ਸੰਭਵ ਨਹੀਂ ਹੋਵੇਗਾ।

The second driver is that for certain requirements, it is important to provide an application development with flexibility regarding how to address particular security challenges. For example, in previous ASVS versions, session timeout rules were very prescriptive. Practically speaking, many applications, especially those that are consumer-facing, have much more relaxed rules and prefer to implement other mitigation controls instead. Documentation requirements, therefore, explicitly allow for flexibility around this.

ਦੂਜਾ ਕਾਰਨ ਇਹ ਹੈ ਕਿ ਕੁਝ ਲੋੜਾਂ ਲਈ, ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਨੂੰ ਇਸ ਬਾਰੇ ਲਚਕ ਪ੍ਰਦਾਨ ਕਰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਖ਼ਾਸ ਸੁਰੱਖਿਆ ਚੁਣੌਤੀਆਂ ਨੂੰ ਕਿਵੇਂ ਸੰਬੋਧਿਤ ਕਰਨਾ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਪਿਛਲੇ ASVS ਸੰਸਕਰਣਾਂ ਵਿੱਚ, ਸੈਸ਼ਨ ਸਮਾਂ-ਸੀਮਾ ਦੇ ਨਿਯਮ ਬਹੁਤ ਨਿਰਦੇਸ਼ਾਤਮਕ ਸਨ। ਵਿਹਾਰਕ ਤੌਰ 'ਤੇ, ਬਹੁਤ ਸਾਰੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ, ਖ਼ਾਸ ਕਰਕੇ ਉਹ ਜੋ ਖਪਤਕਾਰ-ਮੁਖੀ ਹਨ, ਦੇ ਨਿਯਮ ਕਿਤੇ ਵਧੇਰੇ ਢਿੱਲੇ ਹਨ ਅਤੇ ਉਹ ਇਸ ਦੀ ਬਜਾਏ ਹੋਰ ਘਟਾਉ ਨਿਯੰਤਰਣ ਲਾਗੂ ਕਰਨ ਨੂੰ ਤਰਜੀਹ ਦਿੰਦੀਆਂ ਹਨ। ਇਸ ਲਈ, ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲੋੜਾਂ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਇਸ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਲਚਕ ਦੀ ਇਜਾਜ਼ਤ ਦਿੰਦੀਆਂ ਹਨ।

Clearly, it is not expected that individual developers will be making and documenting these decisions but rather the organization as a whole will be taking those decisions and making sure that they are communicated to developers who then make sure to follow them.

ਸਪੱਸ਼ਟ ਹੈ ਕਿ ਇਹ ਉਮੀਦ ਨਹੀਂ ਕੀਤੀ ਜਾਂਦੀ ਕਿ ਵਿਅਕਤੀਗਤ ਵਿਕਾਸਕਾਰ ਇਹ ਫ਼ੈਸਲੇ ਲੈਣਗੇ ਅਤੇ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਦੇਣਗੇ, ਸਗੋਂ ਸੰਸਥਾ ਸਮੁੱਚੇ ਤੌਰ 'ਤੇ ਉਹ ਫ਼ੈਸਲੇ ਲਵੇਗੀ ਅਤੇ ਯਕੀਨੀ ਬਣਾਏਗੀ ਕਿ ਉਹ ਵਿਕਾਸਕਾਰਾਂ ਤੱਕ ਪਹੁੰਚਾਏ ਜਾਣ, ਜੋ ਫਿਰ ਉਹਨਾਂ ਦੀ ਪਾਲਣਾ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਉਣਗੇ।

Providing developers with specifications and designs for new features and functionality is a standard part of software development. Similarly, developers are expected to use common components and user interface mechanisms rather than just making their own decisions each time. As such, extending this to security should not be seen as surprising or controversial.

ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਨਵੇਂ ਫ਼ੀਚਰਾਂ ਅਤੇ ਕਾਰਜਸ਼ੀਲਤਾ ਲਈ ਨਿਰਧਾਰਨ (specifications) ਅਤੇ ਡਿਜ਼ਾਈਨ ਪ੍ਰਦਾਨ ਕਰਨਾ ਸਾਫ਼ਟਵੇਅਰ ਵਿਕਾਸ ਦਾ ਇੱਕ ਮਿਆਰੀ ਹਿੱਸਾ ਹੈ। ਇਸੇ ਤਰ੍ਹਾਂ, ਵਿਕਾਸਕਾਰਾਂ ਤੋਂ ਹਰ ਵਾਰ ਸਿਰਫ਼ ਆਪਣੇ ਫ਼ੈਸਲੇ ਆਪ ਲੈਣ ਦੀ ਬਜਾਏ ਸਾਂਝੇ ਹਿੱਸਿਆਂ ਅਤੇ ਉਪਭੋਗਤਾ ਇੰਟਰਫ਼ੇਸ ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਉਮੀਦ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਲਈ, ਇਸ ਨੂੰ ਸੁਰੱਖਿਆ ਤੱਕ ਵਧਾਉਣ ਨੂੰ ਹੈਰਾਨੀਜਨਕ ਜਾਂ ਵਿਵਾਦਪੂਰਨ ਨਹੀਂ ਸਮਝਿਆ ਜਾਣਾ ਚਾਹੀਦਾ।

There is also flexibility around how to achieve this. Security decisions might be documented in a literal document, which developers are expected to refer to. Alternatively, security decisions could be documented and implemented in a common code library that all developers are mandated to use. In both cases, the desired result is achieved.

ਇਸ ਨੂੰ ਕਿਵੇਂ ਪ੍ਰਾਪਤ ਕਰਨਾ ਹੈ, ਇਸ ਬਾਰੇ ਵੀ ਲਚਕ ਹੈ। ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ ਨੂੰ ਇੱਕ ਅਸਲ ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਦਰਜ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਜਿਸ ਦਾ ਹਵਾਲਾ ਲੈਣ ਦੀ ਵਿਕਾਸਕਾਰਾਂ ਤੋਂ ਉਮੀਦ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਬਦਲ ਵਜੋਂ, ਸੁਰੱਖਿਆ ਫ਼ੈਸਲਿਆਂ ਨੂੰ ਇੱਕ ਸਾਂਝੀ ਕੋਡ ਲਾਇਬ੍ਰੇਰੀ ਵਿੱਚ ਦਸਤਾਵੇਜ਼ੀ ਰੂਪ ਦਿੱਤਾ ਅਤੇ ਲਾਗੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਜਿਸ ਦੀ ਵਰਤੋਂ ਸਾਰੇ ਵਿਕਾਸਕਾਰਾਂ ਲਈ ਲਾਜ਼ਮੀ ਹੋਵੇ। ਦੋਵਾਂ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਲੋੜੀਂਦਾ ਨਤੀਜਾ ਪ੍ਰਾਪਤ ਹੋ ਜਾਂਦਾ ਹੈ।

## Application Security Verification Levels
## ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਤਸਦੀਕ ਪੱਧਰ

The ASVS defines three security verification levels, with each level increasing in depth and complexity. The general aim is for organizations to start with the first level to address the most critical security concerns, and then move up to the higher levels according to the organization and application needs. Levels may be presented as L1, L2, and L3 in the document and in requirement texts.

ASVS ਤਿੰਨ ਸੁਰੱਖਿਆ ਤਸਦੀਕ ਪੱਧਰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ, ਜਿਨ੍ਹਾਂ ਵਿੱਚੋਂ ਹਰ ਪੱਧਰ ਡੂੰਘਾਈ ਅਤੇ ਗੁੰਝਲਤਾ ਵਿੱਚ ਵਧਦਾ ਜਾਂਦਾ ਹੈ। ਆਮ ਉਦੇਸ਼ ਇਹ ਹੈ ਕਿ ਸੰਸਥਾਵਾਂ ਸਭ ਤੋਂ ਨਾਜ਼ੁਕ ਸੁਰੱਖਿਆ ਚਿੰਤਾਵਾਂ ਨੂੰ ਸੰਬੋਧਿਤ ਕਰਨ ਲਈ ਪਹਿਲੇ ਪੱਧਰ ਤੋਂ ਸ਼ੁਰੂ ਕਰਨ, ਅਤੇ ਫਿਰ ਸੰਸਥਾ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀਆਂ ਲੋੜਾਂ ਅਨੁਸਾਰ ਉੱਚੇ ਪੱਧਰਾਂ ਵੱਲ ਵਧਣ। ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਅਤੇ ਲੋੜਾਂ ਦੇ ਪਾਠ ਵਿੱਚ ਪੱਧਰਾਂ ਨੂੰ L1, L2, ਅਤੇ L3 ਵਜੋਂ ਪੇਸ਼ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

Each ASVS level indicates the security requirements that are required to achieve from that level, with the higher remaining level requirements as recommendations.

ਹਰ ASVS ਪੱਧਰ ਉਹਨਾਂ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ ਜਿਨ੍ਹਾਂ ਨੂੰ ਉਸ ਪੱਧਰ ਤੋਂ ਪ੍ਰਾਪਤ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ, ਜਦੋਂ ਕਿ ਬਾਕੀ ਰਹਿੰਦੇ ਉੱਚੇ ਪੱਧਰਾਂ ਦੀਆਂ ਲੋੜਾਂ ਸਿਫ਼ਾਰਸ਼ਾਂ ਵਜੋਂ ਹੁੰਦੀਆਂ ਹਨ।

In order to avoid duplicate requirements or requirements that are no longer relevant at higher levels, some requirements apply to a particular level but have more stringent conditions for higher levels.

ਦੁਹਰਾਈਆਂ ਗਈਆਂ ਲੋੜਾਂ ਜਾਂ ਉਹਨਾਂ ਲੋੜਾਂ ਤੋਂ ਬਚਣ ਲਈ ਜੋ ਉੱਚੇ ਪੱਧਰਾਂ 'ਤੇ ਹੁਣ ਸੰਬੰਧਿਤ ਨਹੀਂ ਰਹਿੰਦੀਆਂ, ਕੁਝ ਲੋੜਾਂ ਇੱਕ ਖ਼ਾਸ ਪੱਧਰ 'ਤੇ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ ਪਰ ਉੱਚੇ ਪੱਧਰਾਂ ਲਈ ਵਧੇਰੇ ਸਖ਼ਤ ਸ਼ਰਤਾਂ ਰੱਖਦੀਆਂ ਹਨ।

### Level evaluation
### ਪੱਧਰ ਮੁਲਾਂਕਣ

Levels are defined by priority-based evaluation of each requirement based on experience implementing and testing security requirements. The main focus is on comparing risk reduction with the effort to implement the requirement. Another key factor is to keep a low barrier to entry.

ਪੱਧਰਾਂ ਨੂੰ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਨੂੰ ਲਾਗੂ ਕਰਨ ਅਤੇ ਟੈਸਟ ਕਰਨ ਦੇ ਤਜਰਬੇ ਦੇ ਆਧਾਰ 'ਤੇ ਹਰ ਲੋੜ ਦੇ ਤਰਜੀਹ-ਆਧਾਰਿਤ ਮੁਲਾਂਕਣ ਦੁਆਰਾ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਮੁੱਖ ਧਿਆਨ ਜੋਖਮ ਘਟਾਉ ਦੀ ਤੁਲਨਾ ਲੋੜ ਨੂੰ ਲਾਗੂ ਕਰਨ ਦੇ ਯਤਨ ਨਾਲ ਕਰਨ 'ਤੇ ਹੈ। ਇੱਕ ਹੋਰ ਮੁੱਖ ਕਾਰਕ ਦਾਖ਼ਲੇ ਦੀ ਰੁਕਾਵਟ ਨੂੰ ਘੱਟ ਰੱਖਣਾ ਹੈ।

Risk reduction considers the extent to which the requirement reduces the level of security risk within the application, taking into account the classic Confidentiality, Integrity, and Availability impact factors as well as considering whether this is a primary layer of defense or whether it would be considered defense in depth.

ਜੋਖਮ ਘਟਾਉ ਇਸ ਹੱਦ ਨੂੰ ਵਿਚਾਰਦਾ ਹੈ ਕਿ ਲੋੜ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਅੰਦਰ ਸੁਰੱਖਿਆ ਜੋਖਮ ਦੇ ਪੱਧਰ ਨੂੰ ਕਿੰਨਾ ਘਟਾਉਂਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਕਲਾਸਿਕ ਗੁਪਤਤਾ (Confidentiality), ਅਖੰਡਤਾ (Integrity), ਅਤੇ ਉਪਲਬਧਤਾ (Availability) ਪ੍ਰਭਾਵ ਕਾਰਕਾਂ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਨਾਲ ਹੀ ਇਹ ਵਿਚਾਰਿਆ ਜਾਂਦਾ ਹੈ ਕਿ ਕੀ ਇਹ ਰੱਖਿਆ ਦੀ ਇੱਕ ਮੁੱਢਲੀ ਪਰਤ ਹੈ ਜਾਂ ਇਸ ਨੂੰ ਡੂੰਘਾਈ ਵਿੱਚ ਰੱਖਿਆ (defense in depth) ਮੰਨਿਆ ਜਾਵੇਗਾ।

The rigorous discussions around both the criteria and the leveling decisions have resulted in an allocation which should hold true for the vast majority of cases, whilst accepting that it may not be a 100% fit for every situation. This means that in certain cases, organizations may wish to prioritize requirements from a higher level earlier on based on their own specific risk considerations.

ਮਾਪਦੰਡਾਂ ਅਤੇ ਪੱਧਰ-ਨਿਰਧਾਰਨ ਦੇ ਫ਼ੈਸਲਿਆਂ, ਦੋਵਾਂ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਸਖ਼ਤ ਵਿਚਾਰ-ਵਟਾਂਦਰੇ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਇੱਕ ਅਜਿਹੀ ਵੰਡ ਹੋਈ ਹੈ ਜੋ ਮਾਮਲਿਆਂ ਦੀ ਵੱਡੀ ਬਹੁਗਿਣਤੀ ਲਈ ਸਹੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ, ਜਦੋਂ ਕਿ ਇਹ ਸਵੀਕਾਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਕਿ ਇਹ ਹਰ ਸਥਿਤੀ ਲਈ 100% ਢੁਕਵੀਂ ਨਹੀਂ ਹੋ ਸਕਦੀ। ਇਸ ਦਾ ਅਰਥ ਹੈ ਕਿ ਕੁਝ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਸੰਸਥਾਵਾਂ ਆਪਣੇ ਖ਼ਾਸ ਜੋਖਮ ਵਿਚਾਰਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਉੱਚੇ ਪੱਧਰ ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਪਹਿਲਾਂ ਤਰਜੀਹ ਦੇਣਾ ਚਾਹ ਸਕਦੀਆਂ ਹਨ।

The types of requirements in each level could be characterized as follows.

ਹਰ ਪੱਧਰ ਵਿੱਚ ਲੋੜਾਂ ਦੀਆਂ ਕਿਸਮਾਂ ਨੂੰ ਹੇਠ ਲਿਖੇ ਅਨੁਸਾਰ ਦਰਸਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

### Level 1
### ਪੱਧਰ 1

This level contains the minimum requirements to consider when securing an application and represents a critical starting point. This level contains around 20% of the ASVS requirements. The goal for this level is to have as few requirements as possible, to decrease the barrier to entry.

ਇਸ ਪੱਧਰ ਵਿੱਚ ਕਿਸੇ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਦੇ ਸਮੇਂ ਵਿਚਾਰਨ ਲਈ ਘੱਟੋ-ਘੱਟ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ ਅਤੇ ਇਹ ਇੱਕ ਨਾਜ਼ੁਕ ਸ਼ੁਰੂਆਤੀ ਬਿੰਦੂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ। ਇਸ ਪੱਧਰ ਵਿੱਚ ASVS ਲੋੜਾਂ ਦਾ ਲਗਭਗ 20% ਸ਼ਾਮਲ ਹੈ। ਇਸ ਪੱਧਰ ਦਾ ਟੀਚਾ ਦਾਖ਼ਲੇ ਦੀ ਰੁਕਾਵਟ ਨੂੰ ਘਟਾਉਣ ਲਈ, ਜਿੰਨੀਆਂ ਸੰਭਵ ਹੋ ਸਕੇ ਓਨੀਆਂ ਘੱਟ ਲੋੜਾਂ ਰੱਖਣਾ ਹੈ।

These requirements are generally critical or basic, first-layer of defense requirements for preventing common attacks that do not require other vulnerabilities or preconditions to be exploitable.

ਇਹ ਲੋੜਾਂ ਆਮ ਤੌਰ 'ਤੇ ਨਾਜ਼ੁਕ ਜਾਂ ਬੁਨਿਆਦੀ, ਰੱਖਿਆ ਦੀ ਪਹਿਲੀ ਪਰਤ ਵਾਲੀਆਂ ਲੋੜਾਂ ਹਨ ਜੋ ਉਹਨਾਂ ਆਮ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਹਨ ਜਿਨ੍ਹਾਂ ਦੇ ਸ਼ੋਸ਼ਣਯੋਗ ਹੋਣ ਲਈ ਹੋਰ ਕਮਜ਼ੋਰੀਆਂ ਜਾਂ ਪੂਰਵ-ਸ਼ਰਤਾਂ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ।

In addition to the first layer of defense requirements, some requirements have less of an impact at higher levels, such as requirements related to passwords. Those are more important for Level 1, as from higher levels, the multi-factor authentication requirements become relevant.

ਰੱਖਿਆ ਦੀ ਪਹਿਲੀ ਪਰਤ ਵਾਲੀਆਂ ਲੋੜਾਂ ਤੋਂ ਇਲਾਵਾ, ਕੁਝ ਲੋੜਾਂ ਦਾ ਉੱਚੇ ਪੱਧਰਾਂ 'ਤੇ ਘੱਟ ਪ੍ਰਭਾਵ ਹੁੰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਪਾਸਵਰਡਾਂ ਨਾਲ ਸੰਬੰਧਿਤ ਲੋੜਾਂ। ਉਹ ਪੱਧਰ 1 ਲਈ ਵਧੇਰੇ ਮਹੱਤਵਪੂਰਨ ਹਨ, ਕਿਉਂਕਿ ਉੱਚੇ ਪੱਧਰਾਂ ਤੋਂ, ਬਹੁ-ਕਾਰਕ ਪ੍ਰਮਾਣੀਕਰਨ (multi-factor authentication) ਦੀਆਂ ਲੋੜਾਂ ਸੰਬੰਧਿਤ ਹੋ ਜਾਂਦੀਆਂ ਹਨ।

Level 1 is not necessarily penetration testable by an external tester without internal access to documentation or code (such as "black box" testing), although the lower number of requirements should make it easier to verify.

ਪੱਧਰ 1 ਜ਼ਰੂਰੀ ਤੌਰ 'ਤੇ ਦਸਤਾਵੇਜ਼ ਜਾਂ ਕੋਡ ਤੱਕ ਅੰਦਰੂਨੀ ਪਹੁੰਚ ਤੋਂ ਬਿਨਾਂ ਕਿਸੇ ਬਾਹਰੀ ਟੈਸਟਰ ਦੁਆਰਾ ਪੈਨੀਟ੍ਰੇਸ਼ਨ ਟੈਸਟ ਕਰਨ ਯੋਗ ਨਹੀਂ ਹੈ (ਜਿਵੇਂ ਕਿ "ਬਲੈਕ ਬਾਕਸ" ਟੈਸਟਿੰਗ), ਹਾਲਾਂਕਿ ਲੋੜਾਂ ਦੀ ਘੱਟ ਗਿਣਤੀ ਇਸ ਦੀ ਤਸਦੀਕ ਨੂੰ ਆਸਾਨ ਬਣਾਉਣੀ ਚਾਹੀਦੀ ਹੈ।

### Level 2
### ਪੱਧਰ 2

Most applications should be striving to achieve this level of security. Around 50% of the requirements in the ASVS are L2 meaning that an application needs to implement around 70% of the requirements in the ASVS (all of the L1 and L2 requirements) in order to comply with L2.

ਬਹੁਤੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਸੁਰੱਖਿਆ ਦੇ ਇਸ ਪੱਧਰ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਦਾ ਯਤਨ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ। ASVS ਵਿੱਚ ਲਗਭਗ 50% ਲੋੜਾਂ L2 ਹਨ, ਜਿਸ ਦਾ ਅਰਥ ਹੈ ਕਿ L2 ਦੀ ਪਾਲਣਾ ਕਰਨ ਲਈ ਇੱਕ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ASVS ਦੀਆਂ ਲਗਭਗ 70% ਲੋੜਾਂ (ਸਾਰੀਆਂ L1 ਅਤੇ L2 ਲੋੜਾਂ) ਨੂੰ ਲਾਗੂ ਕਰਨ ਦੀ ਲੋੜ ਹੈ।

These requirements generally relate to either less common attacks or more complicated protections against common attacks. They may still be a first layer of defense, or they may require certain preconditions for the attack to be successful.

ਇਹ ਲੋੜਾਂ ਆਮ ਤੌਰ 'ਤੇ ਜਾਂ ਤਾਂ ਘੱਟ ਆਮ ਹਮਲਿਆਂ ਨਾਲ ਜਾਂ ਆਮ ਹਮਲਿਆਂ ਵਿਰੁੱਧ ਵਧੇਰੇ ਗੁੰਝਲਦਾਰ ਸੁਰੱਖਿਆਵਾਂ ਨਾਲ ਸੰਬੰਧਿਤ ਹਨ। ਇਹ ਅਜੇ ਵੀ ਰੱਖਿਆ ਦੀ ਪਹਿਲੀ ਪਰਤ ਹੋ ਸਕਦੀਆਂ ਹਨ, ਜਾਂ ਹਮਲੇ ਦੇ ਸਫਲ ਹੋਣ ਲਈ ਇਹਨਾਂ ਨੂੰ ਕੁਝ ਪੂਰਵ-ਸ਼ਰਤਾਂ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ।

### Level 3
### ਪੱਧਰ 3

This level should be the goal for applications looking to demonstrate the highest levels of security and provides the final ~30% of requirements to comply with.

ਇਹ ਪੱਧਰ ਉਹਨਾਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਟੀਚਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਜੋ ਸੁਰੱਖਿਆ ਦੇ ਸਭ ਤੋਂ ਉੱਚੇ ਪੱਧਰਾਂ ਦਾ ਪ੍ਰਦਰਸ਼ਨ ਕਰਨਾ ਚਾਹੁੰਦੀਆਂ ਹਨ ਅਤੇ ਇਹ ਪਾਲਣਾ ਕਰਨ ਲਈ ਅੰਤਿਮ ~30% ਲੋੜਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

Requirements in this section are generally either defense-in-depth mechanisms or other useful but hard-to-implement controls.

ਇਸ ਭਾਗ ਦੀਆਂ ਲੋੜਾਂ ਆਮ ਤੌਰ 'ਤੇ ਜਾਂ ਤਾਂ ਡੂੰਘਾਈ ਵਿੱਚ ਰੱਖਿਆ ਦੀਆਂ ਪ੍ਰਣਾਲੀਆਂ ਹਨ ਜਾਂ ਹੋਰ ਲਾਭਦਾਇਕ ਪਰ ਲਾਗੂ ਕਰਨ ਵਿੱਚ ਔਖੇ ਨਿਯੰਤਰਣ ਹਨ।

### Which level to achieve
### ਕਿਹੜਾ ਪੱਧਰ ਪ੍ਰਾਪਤ ਕਰਨਾ ਹੈ

The priority-based levels are intended to provide a reflection of the application security maturity of the organization and the application. Rather than the ASVS prescriptively stating what level an application should be at, an organization should analyze its risks and decide what level it believes it should be at, depending on the sensitivity of the application and of course, the expectations of the application's users.

ਤਰਜੀਹ-ਆਧਾਰਿਤ ਪੱਧਰਾਂ ਦਾ ਉਦੇਸ਼ ਸੰਸਥਾ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਪਰਿਪੱਕਤਾ ਦਾ ਪ੍ਰਤੀਬਿੰਬ ਪ੍ਰਦਾਨ ਕਰਨਾ ਹੈ। ASVS ਦੁਆਰਾ ਨਿਰਦੇਸ਼ਾਤਮਕ ਤੌਰ 'ਤੇ ਇਹ ਦੱਸਣ ਦੀ ਬਜਾਏ ਕਿ ਇੱਕ ਐਪਲੀਕੇਸ਼ਨ ਕਿਸ ਪੱਧਰ 'ਤੇ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ, ਇੱਕ ਸੰਸਥਾ ਨੂੰ ਆਪਣੇ ਜੋਖਮਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ ਇਹ ਫ਼ੈਸਲਾ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਉਸ ਦੇ ਵਿਸ਼ਵਾਸ ਅਨੁਸਾਰ ਉਸ ਨੂੰ ਕਿਸ ਪੱਧਰ 'ਤੇ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ, ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਅਤੇ ਬੇਸ਼ੱਕ, ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਉਪਭੋਗਤਾਵਾਂ ਦੀਆਂ ਉਮੀਦਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ।

For example, an early-stage startup that is only collecting limited sensitive data may decide to focus on Level 1 for its initial security goals, but a bank may have difficulty justifying anything less than Level 3 to its customers for its online banking application.

ਉਦਾਹਰਨ ਲਈ, ਇੱਕ ਸ਼ੁਰੂਆਤੀ-ਪੜਾਅ ਦਾ ਸਟਾਰਟਅੱਪ ਜੋ ਸਿਰਫ਼ ਸੀਮਤ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਇਕੱਠਾ ਕਰ ਰਿਹਾ ਹੈ, ਆਪਣੇ ਸ਼ੁਰੂਆਤੀ ਸੁਰੱਖਿਆ ਟੀਚਿਆਂ ਲਈ ਪੱਧਰ 1 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਨ ਦਾ ਫ਼ੈਸਲਾ ਕਰ ਸਕਦਾ ਹੈ, ਪਰ ਇੱਕ ਬੈਂਕ ਨੂੰ ਆਪਣੀ ਆਨਲਾਈਨ ਬੈਂਕਿੰਗ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਆਪਣੇ ਗਾਹਕਾਂ ਸਾਹਮਣੇ ਪੱਧਰ 3 ਤੋਂ ਘੱਟ ਕਿਸੇ ਵੀ ਚੀਜ਼ ਨੂੰ ਜਾਇਜ਼ ਠਹਿਰਾਉਣ ਵਿੱਚ ਮੁਸ਼ਕਲ ਹੋ ਸਕਦੀ ਹੈ।

## How to use the ASVS
## ASVS ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰੀਏ

### The structure of the ASVS
### ASVS ਦੀ ਬਣਤਰ

The ASVS is made up of a total of around 350 requirements which are divided into 17 chapters, each of which is further divided into sections.

ASVS ਕੁੱਲ ਲਗਭਗ 350 ਲੋੜਾਂ ਤੋਂ ਬਣਿਆ ਹੈ, ਜੋ 17 ਅਧਿਆਇਆਂ ਵਿੱਚ ਵੰਡੀਆਂ ਗਈਆਂ ਹਨ, ਅਤੇ ਇਹਨਾਂ ਵਿੱਚੋਂ ਹਰ ਅਧਿਆਇ ਨੂੰ ਅੱਗੇ ਭਾਗਾਂ ਵਿੱਚ ਵੰਡਿਆ ਗਿਆ ਹੈ।

The aim of the chapter and section division is to simplify choosing or filtering out chapters and sections based on what is relevant for the application. For example, for a machine-to-machine API, the requirements in chapter V3 related to web frontends will not be relevant. If there is no use of OAuth or WebRTC, then those chapters can be ignored as well.

ਅਧਿਆਇ ਅਤੇ ਭਾਗ ਦੀ ਵੰਡ ਦਾ ਉਦੇਸ਼ ਇਹ ਹੈ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਜੋ ਸੰਬੰਧਿਤ ਹੈ, ਉਸ ਦੇ ਆਧਾਰ 'ਤੇ ਅਧਿਆਇਆਂ ਅਤੇ ਭਾਗਾਂ ਨੂੰ ਚੁਣਨਾ ਜਾਂ ਛਾਂਟ ਕੇ ਬਾਹਰ ਕੱਢਣਾ ਸਰਲ ਬਣਾਇਆ ਜਾਵੇ। ਉਦਾਹਰਨ ਲਈ, ਇੱਕ ਮਸ਼ੀਨ-ਤੋਂ-ਮਸ਼ੀਨ API ਲਈ, ਅਧਿਆਇ V3 ਵਿੱਚ ਵੈੱਬ ਫਰੰਟਐਂਡਾਂ ਨਾਲ ਸੰਬੰਧਿਤ ਲੋੜਾਂ ਸੰਬੰਧਿਤ ਨਹੀਂ ਹੋਣਗੀਆਂ। ਜੇ OAuth ਜਾਂ WebRTC ਦੀ ਕੋਈ ਵਰਤੋਂ ਨਹੀਂ ਹੈ, ਤਾਂ ਉਹਨਾਂ ਅਧਿਆਇਆਂ ਨੂੰ ਵੀ ਨਜ਼ਰਅੰਦਾਜ਼ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

### Release strategy
### ਰਿਲੀਜ਼ ਰਣਨੀਤੀ

ASVS releases follow the pattern "Major.Minor.Patch" and the numbers provide information on what has changed within the release. In a major release, the first number will change, in a minor release, the second number will change, and in a patch release, the third number will change.

ASVS ਰਿਲੀਜ਼ਾਂ "Major.Minor.Patch" ਦੇ ਨਮੂਨੇ ਦੀ ਪਾਲਣਾ ਕਰਦੀਆਂ ਹਨ ਅਤੇ ਇਹ ਅੰਕ ਇਸ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿੰਦੇ ਹਨ ਕਿ ਰਿਲੀਜ਼ ਦੇ ਅੰਦਰ ਕੀ ਬਦਲਿਆ ਹੈ। ਇੱਕ ਮੇਜਰ (major) ਰਿਲੀਜ਼ ਵਿੱਚ ਪਹਿਲਾ ਅੰਕ ਬਦਲੇਗਾ, ਇੱਕ ਮਾਈਨਰ (minor) ਰਿਲੀਜ਼ ਵਿੱਚ ਦੂਜਾ ਅੰਕ ਬਦਲੇਗਾ, ਅਤੇ ਇੱਕ ਪੈਚ (patch) ਰਿਲੀਜ਼ ਵਿੱਚ ਤੀਜਾ ਅੰਕ ਬਦਲੇਗਾ।

* Major release - Full reorganization, almost everything may have changed, including requirement numbers. Reevaluation for compliance will be necessary (for example, 4.0.3 -> 5.0.0).
* Minor release - Requirements may be added or removed, but overall numbering will stay the same. Reevaluation for compliance will be necessary, but should be easier (for example, 5.0.0 -> 5.1.0).
* Patch release - Requirements may be removed (for example, if they are duplicates or outdated) or made less stringent, but an application that complied with the previous release will comply with the patch release as well (for example, 5.0.0 -> 5.0.1).

* ਮੇਜਰ ਰਿਲੀਜ਼ - ਪੂਰਾ ਪੁਨਰਗਠਨ, ਲਗਭਗ ਸਭ ਕੁਝ ਬਦਲਿਆ ਹੋ ਸਕਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਲੋੜਾਂ ਦੇ ਨੰਬਰ ਵੀ ਸ਼ਾਮਲ ਹਨ। ਪਾਲਣਾ ਲਈ ਮੁੜ-ਮੁਲਾਂਕਣ ਜ਼ਰੂਰੀ ਹੋਵੇਗਾ (ਉਦਾਹਰਨ ਲਈ, 4.0.3 -> 5.0.0)।
* ਮਾਈਨਰ ਰਿਲੀਜ਼ - ਲੋੜਾਂ ਜੋੜੀਆਂ ਜਾਂ ਹਟਾਈਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ, ਪਰ ਸਮੁੱਚੀ ਨੰਬਰਿੰਗ ਉਹੀ ਰਹੇਗੀ। ਪਾਲਣਾ ਲਈ ਮੁੜ-ਮੁਲਾਂਕਣ ਜ਼ਰੂਰੀ ਹੋਵੇਗਾ, ਪਰ ਇਹ ਆਸਾਨ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ (ਉਦਾਹਰਨ ਲਈ, 5.0.0 -> 5.1.0)।
* ਪੈਚ ਰਿਲੀਜ਼ - ਲੋੜਾਂ ਹਟਾਈਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ (ਉਦਾਹਰਨ ਲਈ, ਜੇ ਉਹ ਦੁਹਰਾਈਆਂ ਗਈਆਂ ਜਾਂ ਪੁਰਾਣੀਆਂ ਹਨ) ਜਾਂ ਘੱਟ ਸਖ਼ਤ ਬਣਾਈਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ, ਪਰ ਜਿਹੜੀ ਐਪਲੀਕੇਸ਼ਨ ਪਿਛਲੀ ਰਿਲੀਜ਼ ਦੀ ਪਾਲਣਾ ਕਰਦੀ ਸੀ, ਉਹ ਪੈਚ ਰਿਲੀਜ਼ ਦੀ ਵੀ ਪਾਲਣਾ ਕਰੇਗੀ (ਉਦਾਹਰਨ ਲਈ, 5.0.0 -> 5.0.1)।

The above specifically relates to the requirements in the ASVS. Changes to surrounding text and other content such as the appendices will not be considered to be a breaking change.

ਉਪਰੋਕਤ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ASVS ਵਿਚਲੀਆਂ ਲੋੜਾਂ ਨਾਲ ਸੰਬੰਧਿਤ ਹੈ। ਆਲੇ-ਦੁਆਲੇ ਦੇ ਪਾਠ ਅਤੇ ਹੋਰ ਸਮੱਗਰੀ, ਜਿਵੇਂ ਕਿ ਅੰਤਿਕਾਵਾਂ, ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਨੂੰ ਤੋੜਨ ਵਾਲੀ ਤਬਦੀਲੀ (breaking change) ਨਹੀਂ ਮੰਨਿਆ ਜਾਵੇਗਾ।

### Flexibility with the ASVS
### ASVS ਨਾਲ ਲਚਕ

Several of the points described above, such as documentation requirements and the levels mechanism, provide the ability to use the ASVS in a more flexible and organization-specific way.

ਉੱਪਰ ਦੱਸੇ ਗਏ ਕਈ ਨੁਕਤੇ, ਜਿਵੇਂ ਕਿ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲੋੜਾਂ ਅਤੇ ਪੱਧਰਾਂ ਦੀ ਪ੍ਰਣਾਲੀ, ASVS ਨੂੰ ਵਧੇਰੇ ਲਚਕਦਾਰ ਅਤੇ ਸੰਸਥਾ-ਵਿਸ਼ੇਸ਼ ਢੰਗ ਨਾਲ ਵਰਤਣ ਦੀ ਸਮਰੱਥਾ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।

Additionally, organizations are strongly encouraged to create an organization- or domain-specific fork.

ਇਸ ਤੋਂ ਇਲਾਵਾ, ਸੰਸਥਾਵਾਂ ਨੂੰ ਇੱਕ ਸੰਸਥਾ- ਜਾਂ ਖੇਤਰ-ਵਿਸ਼ੇਸ਼ (domain-specific) ਫ਼ੋਰਕ (fork) ਬਣਾਉਣ ਲਈ ਜ਼ੋਰਦਾਰ ਢੰਗ ਨਾਲ ਉਤਸ਼ਾਹਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

### Forking the ASVS
### ASVS ਨੂੰ ਫ਼ੋਰਕ ਕਰਨਾ

Organizations can benefit from adopting ASVS by choosing one of the three levels or by creating a domain-specific fork that adjusts requirements per application risk level. This type of fork is encouraged, provided that it maintains traceability so that passing requirement 4.1.1 means the same across all versions.

ਸੰਸਥਾਵਾਂ ਤਿੰਨ ਪੱਧਰਾਂ ਵਿੱਚੋਂ ਇੱਕ ਨੂੰ ਚੁਣ ਕੇ, ਜਾਂ ਇੱਕ ਅਜਿਹਾ ਖੇਤਰ-ਵਿਸ਼ੇਸ਼ ਫ਼ੋਰਕ ਬਣਾ ਕੇ ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਜੋਖਮ ਪੱਧਰ ਅਨੁਸਾਰ ਲੋੜਾਂ ਨੂੰ ਵਿਵਸਥਿਤ ਕਰਦਾ ਹੈ, ASVS ਨੂੰ ਅਪਣਾਉਣ ਦਾ ਲਾਭ ਲੈ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਕਿਸਮ ਦੇ ਫ਼ੋਰਕ ਨੂੰ ਉਤਸ਼ਾਹਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਬਸ਼ਰਤੇ ਕਿ ਇਹ ਖੋਜਯੋਗਤਾ (traceability) ਬਣਾਈ ਰੱਖੇ, ਤਾਂ ਜੋ ਲੋੜ 4.1.1 ਨੂੰ ਪਾਸ ਕਰਨ ਦਾ ਅਰਥ ਸਾਰੇ ਸੰਸਕਰਣਾਂ ਵਿੱਚ ਇੱਕੋ ਜਿਹਾ ਰਹੇ।

Ideally, each organization should create its own tailored ASVS, omitting irrelevant sections (e.g., GraphQL, Websockets, SOAP, if unused). Forking should start with ASVS Level 1 as a baseline, advancing to Levels 2 or 3 based on the application’s risk.

ਆਦਰਸ਼ਕ ਤੌਰ 'ਤੇ, ਹਰ ਸੰਸਥਾ ਨੂੰ ਆਪਣਾ ਅਨੁਕੂਲਿਤ ASVS ਬਣਾਉਣਾ ਚਾਹੀਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਅਸੰਬੰਧਿਤ ਭਾਗਾਂ ਨੂੰ ਛੱਡ ਦਿੱਤਾ ਜਾਵੇ (ਜਿਵੇਂ, GraphQL, Websockets, SOAP, ਜੇ ਵਰਤੇ ਨਹੀਂ ਜਾਂਦੇ)। ਫ਼ੋਰਕ ਕਰਨਾ ASVS ਪੱਧਰ 1 ਨੂੰ ਆਧਾਰ-ਰੇਖਾ (baseline) ਵਜੋਂ ਲੈ ਕੇ ਸ਼ੁਰੂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ, ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਜੋਖਮ ਦੇ ਆਧਾਰ 'ਤੇ ਪੱਧਰ 2 ਜਾਂ 3 ਵੱਲ ਅੱਗੇ ਵਧਣਾ ਚਾਹੀਦਾ ਹੈ।

### How to Reference ASVS Requirements
### ASVS ਲੋੜਾਂ ਦਾ ਹਵਾਲਾ ਕਿਵੇਂ ਦੇਣਾ ਹੈ

Each requirement has an identifier in the format `<chapter>.<section>.<requirement>`, where each element is a number. For example, `1.11.3`.

ਹਰ ਲੋੜ ਦਾ `<chapter>.<section>.<requirement>` ਫਾਰਮੈਟ ਵਿੱਚ ਇੱਕ ਪਛਾਣਕਰਤਾ (identifier) ਹੁੰਦਾ ਹੈ, ਜਿੱਥੇ ਹਰ ਤੱਤ ਇੱਕ ਅੰਕ ਹੈ। ਉਦਾਹਰਨ ਲਈ, `1.11.3`।

* The `<chapter>` value corresponds to the chapter from which the requirement comes; for example, all `1.#.#` requirements are from the 'Encoding and Sanitization' chapter.
* The `<section>` value corresponds to the section within that chapter where the requirement appears, for example: all `1.2.#` requirements are in the 'Injection Prevention' section of the 'Encoding and Sanitization' chapter.
* The `<requirement>` value identifies the specific requirement within the chapter and section, for example, `1.2.5` which as of version 5.0.0 of this standard is:

* `<chapter>` ਮੁੱਲ ਉਸ ਅਧਿਆਇ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ ਜਿਸ ਤੋਂ ਲੋੜ ਆਉਂਦੀ ਹੈ; ਉਦਾਹਰਨ ਲਈ, ਸਾਰੀਆਂ `1.#.#` ਲੋੜਾਂ 'ਏਨਕੋਡਿੰਗ ਅਤੇ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ' (Encoding and Sanitization) ਅਧਿਆਇ ਤੋਂ ਹਨ।
* `<section>` ਮੁੱਲ ਉਸ ਅਧਿਆਇ ਦੇ ਅੰਦਰਲੇ ਉਸ ਭਾਗ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ ਜਿੱਥੇ ਲੋੜ ਦਿਖਾਈ ਦਿੰਦੀ ਹੈ, ਉਦਾਹਰਨ ਲਈ: ਸਾਰੀਆਂ `1.2.#` ਲੋੜਾਂ 'ਏਨਕੋਡਿੰਗ ਅਤੇ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ' ਅਧਿਆਇ ਦੇ 'ਇੰਜੈਕਸ਼ਨ ਰੋਕਥਾਮ' (Injection Prevention) ਭਾਗ ਵਿੱਚ ਹਨ।
* `<requirement>` ਮੁੱਲ ਅਧਿਆਇ ਅਤੇ ਭਾਗ ਦੇ ਅੰਦਰ ਖ਼ਾਸ ਲੋੜ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ, ਉਦਾਹਰਨ ਲਈ, `1.2.5`, ਜੋ ਇਸ ਮਿਆਰ ਦੇ ਸੰਸਕਰਣ 5.0.0 ਅਨੁਸਾਰ ਇਹ ਹੈ:

> Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding.

> ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ OS ਕਮਾਂਡ ਇੰਜੈਕਸ਼ਨ ਤੋਂ ਬਚਾਅ ਕਰਦੀ ਹੈ ਅਤੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਕਾਲਾਂ ਪੈਰਾਮੀਟਰਾਈਜ਼ਡ OS ਕਿਊਰੀਆਂ ਵਰਤਦੀਆਂ ਹਨ ਜਾਂ ਸੰਦਰਭੀ ਕਮਾਂਡ ਲਾਈਨ ਆਊਟਪੁੱਟ ਏਨਕੋਡਿੰਗ ਵਰਤਦੀਆਂ ਹਨ।

Since the identifiers may change between versions of the standard, it is preferable for other documents, reports, or tools to use the following format: `v<version>-<chapter>.<section>.<requirement>`, where: 'version' is the ASVS version tag. For example: `v5.0.0-1.2.5` would be understood to mean specifically the 5th requirement in the 'Injection Prevention' section of the 'Encoding and Sanitization' chapter from version 5.0.0. (This could be summarized as `v<version>-<requirement_identifier>`.)

ਕਿਉਂਕਿ ਪਛਾਣਕਰਤਾ ਮਿਆਰ ਦੇ ਸੰਸਕਰਣਾਂ ਦੇ ਵਿਚਕਾਰ ਬਦਲ ਸਕਦੇ ਹਨ, ਇਸ ਲਈ ਹੋਰ ਦਸਤਾਵੇਜ਼ਾਂ, ਰਿਪੋਰਟਾਂ, ਜਾਂ ਟੂਲਾਂ ਲਈ ਹੇਠ ਲਿਖੇ ਫਾਰਮੈਟ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਬਿਹਤਰ ਹੈ: `v<version>-<chapter>.<section>.<requirement>`, ਜਿੱਥੇ: 'version' ASVS ਸੰਸਕਰਣ ਟੈਗ ਹੈ। ਉਦਾਹਰਨ ਲਈ: `v5.0.0-1.2.5` ਨੂੰ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ਸੰਸਕਰਣ 5.0.0 ਦੇ 'ਏਨਕੋਡਿੰਗ ਅਤੇ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ' ਅਧਿਆਇ ਦੇ 'ਇੰਜੈਕਸ਼ਨ ਰੋਕਥਾਮ' ਭਾਗ ਦੀ 5ਵੀਂ ਲੋੜ ਵਜੋਂ ਸਮਝਿਆ ਜਾਵੇਗਾ। (ਇਸ ਨੂੰ `v<version>-<requirement_identifier>` ਵਜੋਂ ਸੰਖੇਪ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ)।

Note: The `v` preceding the version number in the format should always be lowercase.

ਨੋਟ: ਫਾਰਮੈਟ ਵਿੱਚ ਸੰਸਕਰਣ ਨੰਬਰ ਤੋਂ ਪਹਿਲਾਂ ਆਉਣ ਵਾਲਾ `v` ਹਮੇਸ਼ਾ ਛੋਟੇ ਅੱਖਰ (lowercase) ਵਿੱਚ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

If identifiers are used without including the `v<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. As the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

ਜੇ ਪਛਾਣਕਰਤਾਵਾਂ ਨੂੰ `v<version>` ਤੱਤ ਸ਼ਾਮਲ ਕੀਤੇ ਬਿਨਾਂ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਇਹ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਉਹ ਨਵੀਨਤਮ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਤਸਦੀਕ ਮਿਆਰ ਦੀ ਸਮੱਗਰੀ ਵੱਲ ਇਸ਼ਾਰਾ ਕਰਦੇ ਹਨ। ਜਿਵੇਂ-ਜਿਵੇਂ ਮਿਆਰ ਵਧਦਾ ਅਤੇ ਬਦਲਦਾ ਹੈ, ਇਹ ਸਮੱਸਿਆ ਵਾਲਾ ਬਣ ਜਾਂਦਾ ਹੈ, ਇਸੇ ਕਰਕੇ ਲੇਖਕਾਂ ਜਾਂ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਸੰਸਕਰਣ ਤੱਤ ਸ਼ਾਮਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।

ASVS requirement lists are made available in CSV, JSON, and other formats which may be useful for reference or programmatic use.

ASVS ਲੋੜਾਂ ਦੀਆਂ ਸੂਚੀਆਂ CSV, JSON, ਅਤੇ ਹੋਰ ਫਾਰਮੈਟਾਂ ਵਿੱਚ ਉਪਲਬਧ ਕਰਵਾਈਆਂ ਜਾਂਦੀਆਂ ਹਨ, ਜੋ ਹਵਾਲੇ ਜਾਂ ਪ੍ਰੋਗਰਾਮੀ ਵਰਤੋਂ ਲਈ ਲਾਭਦਾਇਕ ਹੋ ਸਕਦੀਆਂ ਹਨ।

## Use cases for the ASVS
## ASVS ਦੇ ਵਰਤੋਂ ਦੇ ਮਾਮਲੇ

The ASVS can be used to assess the security of an application and this is explored in more depth in the next chapter. However, several other potential uses for the ASVS (or a forked version) have been identified.

ASVS ਦੀ ਵਰਤੋਂ ਕਿਸੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਸੁਰੱਖਿਆ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ ਅਤੇ ਅਗਲੇ ਅਧਿਆਇ ਵਿੱਚ ਇਸ ਦੀ ਵਧੇਰੇ ਡੂੰਘਾਈ ਨਾਲ ਪੜਚੋਲ ਕੀਤੀ ਗਈ ਹੈ। ਹਾਲਾਂਕਿ, ASVS (ਜਾਂ ਇਸ ਦੇ ਫ਼ੋਰਕ ਕੀਤੇ ਸੰਸਕਰਣ) ਦੇ ਕਈ ਹੋਰ ਸੰਭਾਵੀ ਉਪਯੋਗਾਂ ਦੀ ਪਛਾਣ ਕੀਤੀ ਗਈ ਹੈ।

### As Detailed Security Architecture Guidance
### ਵਿਸਤ੍ਰਿਤ ਸੁਰੱਖਿਆ ਆਰਕੀਟੈਕਚਰ ਮਾਰਗਦਰਸ਼ਨ ਵਜੋਂ

One of the more common uses for the Application Security Verification Standard is as a resource for security architects. There are limited resources available for how to build a secure application architecture, especially with modern applications. ASVS can be used to fill in those gaps by allowing security architects to choose better controls for common problems, such as data protection patterns and input validation strategies. The architecture and documentation requirements will be particularly useful for this.

ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਤਸਦੀਕ ਮਿਆਰ ਦੇ ਵਧੇਰੇ ਆਮ ਉਪਯੋਗਾਂ ਵਿੱਚੋਂ ਇੱਕ ਸੁਰੱਖਿਆ ਆਰਕੀਟੈਕਟਾਂ ਲਈ ਇੱਕ ਸਰੋਤ ਵਜੋਂ ਹੈ। ਇੱਕ ਸੁਰੱਖਿਅਤ ਐਪਲੀਕੇਸ਼ਨ ਆਰਕੀਟੈਕਚਰ (architecture) ਕਿਵੇਂ ਬਣਾਈ ਜਾਵੇ, ਇਸ ਬਾਰੇ ਸੀਮਤ ਸਰੋਤ ਉਪਲਬਧ ਹਨ, ਖ਼ਾਸ ਕਰਕੇ ਆਧੁਨਿਕ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਮਾਮਲੇ ਵਿੱਚ। ASVS ਦੀ ਵਰਤੋਂ ਸੁਰੱਖਿਆ ਆਰਕੀਟੈਕਟਾਂ ਨੂੰ ਆਮ ਸਮੱਸਿਆਵਾਂ, ਜਿਵੇਂ ਕਿ ਡਾਟਾ ਸੁਰੱਖਿਆ ਨਮੂਨਿਆਂ ਅਤੇ ਇਨਪੁੱਟ ਪ੍ਰਮਾਣਿਕਤਾ ਰਣਨੀਤੀਆਂ, ਲਈ ਬਿਹਤਰ ਨਿਯੰਤਰਣ ਚੁਣਨ ਦੇ ਯੋਗ ਬਣਾ ਕੇ ਇਹਨਾਂ ਖੱਪਿਆਂ ਨੂੰ ਭਰਨ ਲਈ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਆਰਕੀਟੈਕਚਰ ਅਤੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲੋੜਾਂ ਇਸ ਲਈ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ਲਾਭਦਾਇਕ ਹੋਣਗੀਆਂ।

### As a Specialized Secure Coding Reference
### ਇੱਕ ਵਿਸ਼ੇਸ਼ ਸੁਰੱਖਿਅਤ ਕੋਡਿੰਗ ਹਵਾਲੇ ਵਜੋਂ

The ASVS can be used as a basis for preparing a secure coding reference during application development, helping developers to make sure that they keep security in mind when they build software. Whilst the ASVS can be the base, organizations should prepare their own specific guidance which is clear and unified and ideally be prepared based on guidance from security engineers or security architects. As an extension to this, organizations are encouraged wherever possible to prepare approved security mechanisms and libraries that can be referenced in the guidance and used by developers.

ASVS ਦੀ ਵਰਤੋਂ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਦੌਰਾਨ ਇੱਕ ਸੁਰੱਖਿਅਤ ਕੋਡਿੰਗ ਹਵਾਲਾ ਤਿਆਰ ਕਰਨ ਦੇ ਆਧਾਰ ਵਜੋਂ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ, ਜੋ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ ਕਿ ਉਹ ਸਾਫ਼ਟਵੇਅਰ ਬਣਾਉਂਦੇ ਸਮੇਂ ਸੁਰੱਖਿਆ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣ। ਭਾਵੇਂ ASVS ਆਧਾਰ ਹੋ ਸਕਦਾ ਹੈ, ਸੰਸਥਾਵਾਂ ਨੂੰ ਆਪਣਾ ਖ਼ਾਸ ਮਾਰਗਦਰਸ਼ਨ ਤਿਆਰ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ, ਜੋ ਸਪੱਸ਼ਟ ਅਤੇ ਇਕਸਾਰ ਹੋਵੇ ਅਤੇ ਆਦਰਸ਼ਕ ਤੌਰ 'ਤੇ ਸੁਰੱਖਿਆ ਇੰਜੀਨੀਅਰਾਂ ਜਾਂ ਸੁਰੱਖਿਆ ਆਰਕੀਟੈਕਟਾਂ ਦੇ ਮਾਰਗਦਰਸ਼ਨ ਦੇ ਆਧਾਰ 'ਤੇ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੋਵੇ। ਇਸ ਦੇ ਵਿਸਤਾਰ ਵਜੋਂ, ਸੰਸਥਾਵਾਂ ਨੂੰ ਜਿੱਥੇ ਵੀ ਸੰਭਵ ਹੋਵੇ, ਪ੍ਰਵਾਨਿਤ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀਆਂ ਅਤੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਤਿਆਰ ਕਰਨ ਲਈ ਉਤਸ਼ਾਹਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜਿਨ੍ਹਾਂ ਦਾ ਮਾਰਗਦਰਸ਼ਨ ਵਿੱਚ ਹਵਾਲਾ ਦਿੱਤਾ ਜਾ ਸਕੇ ਅਤੇ ਜੋ ਵਿਕਾਸਕਾਰਾਂ ਦੁਆਰਾ ਵਰਤੀਆਂ ਜਾ ਸਕਣ।

### As a Guide for Automated Unit and Integration Tests
### ਸਵੈਚਾਲਿਤ ਯੂਨਿਟ ਅਤੇ ਏਕੀਕਰਨ ਟੈਸਟਾਂ ਲਈ ਇੱਕ ਮਾਰਗਦਰਸ਼ਕ ਵਜੋਂ

The ASVS is designed to be highly testable. Some verifications will be technical where as other requirements (such as the architectural and documentation requirements) may require documentation or architecture review. By building unit and integration tests that test and fuzz for specific and relevant abuse cases related to the requirements that are verifiable by technical means, it should be easier to check that these controls are operating correctly on each build. For example, additional tests can be crafted for the test suite for a login controller, testing the username parameter for common default usernames, account enumeration, brute forcing, LDAP and SQL injection, and XSS. Similarly, a test on the password parameter should include common passwords, password length, null byte injection, removing the parameter, XSS, and more.

ASVS ਨੂੰ ਉੱਚ ਪੱਧਰ 'ਤੇ ਟੈਸਟ ਕਰਨ ਯੋਗ ਹੋਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਕੁਝ ਤਸਦੀਕਾਂ ਤਕਨੀਕੀ ਹੋਣਗੀਆਂ, ਜਦੋਂ ਕਿ ਹੋਰ ਲੋੜਾਂ (ਜਿਵੇਂ ਕਿ ਆਰਕੀਟੈਕਚਰ ਅਤੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲੋੜਾਂ) ਲਈ ਦਸਤਾਵੇਜ਼ ਜਾਂ ਆਰਕੀਟੈਕਚਰ ਦੀ ਸਮੀਖਿਆ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ। ਤਕਨੀਕੀ ਸਾਧਨਾਂ ਦੁਆਰਾ ਤਸਦੀਕ ਕਰਨ ਯੋਗ ਲੋੜਾਂ ਨਾਲ ਸੰਬੰਧਿਤ ਖ਼ਾਸ ਅਤੇ ਸੰਬੰਧਿਤ ਦੁਰਵਰਤੋਂ ਦੇ ਮਾਮਲਿਆਂ (abuse cases) ਲਈ ਟੈਸਟ ਅਤੇ ਫ਼ਜ਼ (fuzz) ਕਰਨ ਵਾਲੇ ਯੂਨਿਟ ਅਤੇ ਏਕੀਕਰਨ (integration) ਟੈਸਟ ਬਣਾ ਕੇ, ਹਰ ਬਿਲਡ 'ਤੇ ਇਹ ਜਾਂਚ ਕਰਨਾ ਆਸਾਨ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਇਹ ਨਿਯੰਤਰਣ ਸਹੀ ਢੰਗ ਨਾਲ ਕੰਮ ਕਰ ਰਹੇ ਹਨ। ਉਦਾਹਰਨ ਲਈ, ਇੱਕ ਲੌਗਇਨ ਕੰਟਰੋਲਰ ਦੇ ਟੈਸਟ ਸੂਟ ਲਈ ਵਾਧੂ ਟੈਸਟ ਤਿਆਰ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ, ਜੋ ਉਪਭੋਗਤਾ-ਨਾਂ ਪੈਰਾਮੀਟਰ ਨੂੰ ਆਮ ਡਿਫ਼ਾਲਟ ਉਪਭੋਗਤਾ-ਨਾਵਾਂ, ਖਾਤਾ ਐਨੂਮਰੇਸ਼ਨ (account enumeration), ਬਰੂਟ ਫੋਰਸਿੰਗ, LDAP ਅਤੇ SQL ਇੰਜੈਕਸ਼ਨ, ਅਤੇ XSS ਲਈ ਟੈਸਟ ਕਰਨ। ਇਸੇ ਤਰ੍ਹਾਂ, ਪਾਸਵਰਡ ਪੈਰਾਮੀਟਰ 'ਤੇ ਇੱਕ ਟੈਸਟ ਵਿੱਚ ਆਮ ਪਾਸਵਰਡ, ਪਾਸਵਰਡ ਦੀ ਲੰਬਾਈ, ਨਲ ਬਾਈਟ ਇੰਜੈਕਸ਼ਨ, ਪੈਰਾਮੀਟਰ ਨੂੰ ਹਟਾਉਣਾ, XSS, ਅਤੇ ਹੋਰ ਸ਼ਾਮਲ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ।

### For Secure Development Training
### ਸੁਰੱਖਿਅਤ ਵਿਕਾਸ ਸਿਖਲਾਈ ਲਈ

ASVS can also be used to define the characteristics of secure software. Many “secure coding” courses are simply ethical hacking courses with a light smear of coding tips. This may not necessarily help developers to write more secure code. Instead, secure development courses can use the ASVS with a strong focus on the positive mechanisms found in the ASVS, rather than the Top 10 negative things not to do. The ASVS structure also provides a logical structure for walking through the different topics when securing an application.

ASVS ਦੀ ਵਰਤੋਂ ਸੁਰੱਖਿਅਤ ਸਾਫ਼ਟਵੇਅਰ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਲਈ ਵੀ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਬਹੁਤ ਸਾਰੇ "ਸੁਰੱਖਿਅਤ ਕੋਡਿੰਗ" ਕੋਰਸ ਅਸਲ ਵਿੱਚ ਕੋਡਿੰਗ ਸੁਝਾਵਾਂ ਦੀ ਹਲਕੀ ਜਿਹੀ ਪਰਤ ਵਾਲੇ ਨੈਤਿਕ ਹੈਕਿੰਗ ਕੋਰਸ ਹੀ ਹੁੰਦੇ ਹਨ। ਇਹ ਜ਼ਰੂਰੀ ਨਹੀਂ ਕਿ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਵਧੇਰੇ ਸੁਰੱਖਿਅਤ ਕੋਡ ਲਿਖਣ ਵਿੱਚ ਮਦਦ ਕਰੇ। ਇਸ ਦੀ ਬਜਾਏ, ਸੁਰੱਖਿਅਤ ਵਿਕਾਸ ਕੋਰਸ ASVS ਦੀ ਵਰਤੋਂ ASVS ਵਿੱਚ ਮਿਲਣ ਵਾਲੀਆਂ ਸਕਾਰਾਤਮਕ ਪ੍ਰਣਾਲੀਆਂ 'ਤੇ ਮਜ਼ਬੂਤ ਧਿਆਨ ਨਾਲ ਕਰ ਸਕਦੇ ਹਨ, ਨਾ ਕਿ ਨਾ ਕਰਨ ਵਾਲੀਆਂ Top 10 ਨਕਾਰਾਤਮਕ ਚੀਜ਼ਾਂ 'ਤੇ। ASVS ਦੀ ਬਣਤਰ ਕਿਸੇ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਦੇ ਸਮੇਂ ਵੱਖ-ਵੱਖ ਵਿਸ਼ਿਆਂ ਵਿੱਚੋਂ ਲੰਘਣ ਲਈ ਇੱਕ ਤਰਕਪੂਰਨ ਬਣਤਰ ਵੀ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ।

### As a Framework for Guiding the Procurement of Secure Software
### ਸੁਰੱਖਿਅਤ ਸਾਫ਼ਟਵੇਅਰ ਦੀ ਖ਼ਰੀਦ ਦੇ ਮਾਰਗਦਰਸ਼ਨ ਲਈ ਇੱਕ ਫ੍ਰੇਮਵਰਕ ਵਜੋਂ

The ASVS is a great framework to help with secure software procurement or procurement of custom development services. The buyer can simply set a requirement that the software they wish to procure must be developed at ASVS level X, and request that the seller proves that the software satisfies ASVS level X.

ASVS ਸੁਰੱਖਿਅਤ ਸਾਫ਼ਟਵੇਅਰ ਦੀ ਖ਼ਰੀਦ ਜਾਂ ਕਸਟਮ ਵਿਕਾਸ ਸੇਵਾਵਾਂ ਦੀ ਖ਼ਰੀਦ ਵਿੱਚ ਮਦਦ ਕਰਨ ਲਈ ਇੱਕ ਬਹੁਤ ਵਧੀਆ ਫ੍ਰੇਮਵਰਕ (framework) ਹੈ। ਖ਼ਰੀਦਦਾਰ ਬਸ ਇਹ ਲੋੜ ਨਿਰਧਾਰਿਤ ਕਰ ਸਕਦਾ ਹੈ ਕਿ ਜੋ ਸਾਫ਼ਟਵੇਅਰ ਉਹ ਖ਼ਰੀਦਣਾ ਚਾਹੁੰਦਾ ਹੈ, ਉਹ ASVS ਪੱਧਰ X 'ਤੇ ਵਿਕਸਿਤ ਕੀਤਾ ਜਾਣਾ ਲਾਜ਼ਮੀ ਹੈ, ਅਤੇ ਵਿਕਰੇਤਾ ਤੋਂ ਇਹ ਮੰਗ ਕਰ ਸਕਦਾ ਹੈ ਕਿ ਉਹ ਸਾਬਤ ਕਰੇ ਕਿ ਸਾਫ਼ਟਵੇਅਰ ASVS ਪੱਧਰ X ਨੂੰ ਸੰਤੁਸ਼ਟ ਕਰਦਾ ਹੈ।

## Applying ASVS in Practice
## ASVS ਨੂੰ ਅਮਲ ਵਿੱਚ ਲਾਗੂ ਕਰਨਾ

Different threats have different motivations. Some industries have unique information and technology assets and domain-specific regulatory compliance requirements.

ਵੱਖ-ਵੱਖ ਖ਼ਤਰਿਆਂ ਦੀਆਂ ਵੱਖ-ਵੱਖ ਪ੍ਰੇਰਨਾਵਾਂ ਹੁੰਦੀਆਂ ਹਨ। ਕੁਝ ਉਦਯੋਗਾਂ ਕੋਲ ਵਿਲੱਖਣ ਜਾਣਕਾਰੀ ਅਤੇ ਤਕਨਾਲੋਜੀ ਸੰਪਤੀਆਂ ਅਤੇ ਖੇਤਰ-ਵਿਸ਼ੇਸ਼ ਨਿਯਮਕ ਪਾਲਣਾ ਲੋੜਾਂ ਹੁੰਦੀਆਂ ਹਨ।

Organizations are strongly encouraged to look deeply at their unique risk characteristics based on the nature of their business, and based upon that risk and business requirements determine the appropriate ASVS level.

ਸੰਸਥਾਵਾਂ ਨੂੰ ਆਪਣੇ ਕਾਰੋਬਾਰ ਦੇ ਸੁਭਾਅ ਦੇ ਆਧਾਰ 'ਤੇ ਆਪਣੀਆਂ ਵਿਲੱਖਣ ਜੋਖਮ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਡੂੰਘਾਈ ਨਾਲ ਵੇਖਣ ਲਈ, ਅਤੇ ਉਸ ਜੋਖਮ ਅਤੇ ਕਾਰੋਬਾਰੀ ਲੋੜਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਢੁਕਵਾਂ ASVS ਪੱਧਰ ਨਿਰਧਾਰਿਤ ਕਰਨ ਲਈ ਜ਼ੋਰਦਾਰ ਢੰਗ ਨਾਲ ਉਤਸ਼ਾਹਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।
