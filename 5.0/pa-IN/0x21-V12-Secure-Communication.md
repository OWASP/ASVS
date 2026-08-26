<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x21-V12-Secure-Communication.md -->
<!-- Translator: GeeksikhSecurity -->

# V12 Secure Communication
# V12 ਸੁਰੱਖਿਅਤ ਸੰਚਾਰ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

This chapter includes requirements related to the specific mechanisms that should be in place to protect data in transit, both between an end-user client and a backend service, as well as between internal and backend services.

ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਉਹਨਾਂ ਖ਼ਾਸ ਪ੍ਰਣਾਲੀਆਂ ਨਾਲ ਸੰਬੰਧਿਤ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ ਜੋ ਡਾਟਾ ਨੂੰ ਪ੍ਰਸਾਰਣ ਦੌਰਾਨ (data in transit) ਸੁਰੱਖਿਅਤ ਰੱਖਣ ਲਈ ਮੌਜੂਦ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ — ਇੱਕ ਅੰਤਮ-ਉਪਭੋਗਤਾ ਕਲਾਇੰਟ ਅਤੇ ਬੈਕਐਂਡ ਸੇਵਾ ਦੇ ਵਿਚਕਾਰ, ਨਾਲ ਹੀ ਅੰਦਰੂਨੀ ਅਤੇ ਬੈਕਐਂਡ ਸੇਵਾਵਾਂ ਦੇ ਵਿਚਕਾਰ ਵੀ।

The general concepts promoted by this chapter include:

ਇਸ ਅਧਿਆਇ ਦੁਆਰਾ ਪ੍ਰਚਾਰਿਤ ਆਮ ਸੰਕਲਪਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

* Ensuring that communications are encrypted externally, and ideally internally as well.
* Configuring encryption mechanisms using the latest guidance, including preferred algorithms and ciphers.
* Using signed certificates to ensure that communications are not being intercepted by unauthorized parties.

* ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਕਿ ਸੰਚਾਰ ਬਾਹਰੀ ਤੌਰ 'ਤੇ ਏਨਕ੍ਰਿਪਟ ਕੀਤੇ ਜਾਣ, ਅਤੇ ਆਦਰਸ਼ਕ ਤੌਰ 'ਤੇ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ ਵੀ।
* ਨਵੀਨਤਮ ਮਾਰਗਦਰਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਏਨਕ੍ਰਿਪਸ਼ਨ ਪ੍ਰਣਾਲੀਆਂ ਨੂੰ ਕੌਨਫ਼ਿਗਰ ਕਰਨਾ, ਜਿਸ ਵਿੱਚ ਤਰਜੀਹੀ ਐਲਗੋਰਿਦਮ ਅਤੇ ਸਾਈਫ਼ਰ ਸ਼ਾਮਲ ਹਨ।
* ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਦਸਤਖ਼ਤ ਕੀਤੇ ਸਰਟੀਫ਼ਿਕੇਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਕਿ ਸੰਚਾਰ ਅਣਅਧਿਕਾਰਤ ਧਿਰਾਂ ਦੁਆਰਾ ਰੋਕੇ ਨਹੀਂ ਜਾ ਰਹੇ।

In addition to outlining general principles and best practices, the ASVS also provides more in-depth technical information about cryptographic strength in Appendix C - Cryptography Standards.

ਆਮ ਸਿਧਾਂਤਾਂ ਅਤੇ ਸਭ ਤੋਂ ਚੰਗੇ ਅਮਲਾਂ ਦੀ ਰੂਪਰੇਖਾ ਦੇਣ ਤੋਂ ਇਲਾਵਾ, ASVS ਅੰਤਿਕਾ C — ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ੀ ਮਿਆਰਾਂ ਵਿੱਚ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫ਼ਿਕ ਤਾਕਤ ਬਾਰੇ ਵਧੇਰੇ ਡੂੰਘੀ ਤਕਨੀਕੀ ਜਾਣਕਾਰੀ ਵੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

## V12.1 General TLS Security Guidance
## V12.1 ਆਮ TLS ਸੁਰੱਖਿਆ ਮਾਰਗਦਰਸ਼ਨ

This section provides initial guidance on how to secure TLS communications. Up-to-date tools should be used to review TLS configuration on an ongoing basis.

ਇਹ ਭਾਗ TLS ਸੰਚਾਰਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਬਾਰੇ ਸ਼ੁਰੂਆਤੀ ਮਾਰਗਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। TLS ਕੌਨਫ਼ਿਗਰੇਸ਼ਨ ਦੀ ਨਿਰੰਤਰ ਆਧਾਰ 'ਤੇ ਸਮੀਖਿਆ ਕਰਨ ਲਈ ਅੱਪ-ਟੂ-ਡੇਟ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ।

While the use of wildcard TLS certificates is not inherently insecure, a compromise of a certificate that is deployed across all owned environments (e.g., production, staging, development, and test) may lead to a compromise of the security posture of the applications using it. Proper protection, management, and the use of separate TLS certificates in different environments should be employed if possible.

ਭਾਵੇਂ ਵਾਈਲਡਕਾਰਡ TLS ਸਰਟੀਫ਼ਿਕੇਟਾਂ ਦੀ ਵਰਤੋਂ ਆਪਣੇ ਆਪ ਵਿੱਚ ਅਸੁਰੱਖਿਅਤ ਨਹੀਂ ਹੈ, ਉਹ ਸਰਟੀਫ਼ਿਕੇਟ ਜੋ ਸਾਰੇ ਮਲਕੀਅਤ ਵਾਲੇ ਵਾਤਾਵਰਣਾਂ (ਜਿਵੇਂ, ਪ੍ਰੋਡਕਸ਼ਨ, ਸਟੇਜਿੰਗ, ਡਿਵੈਲਪਮੈਂਟ, ਅਤੇ ਟੈਸਟ) ਵਿੱਚ ਤਾਇਨਾਤ ਹੈ, ਉਸ ਦੇ ਸਮਝੌਤੇ ਨਾਲ ਉਸ ਦੀ ਵਰਤੋਂ ਕਰਨ ਵਾਲੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੀ ਸੁਰੱਖਿਆ ਸਥਿਤੀ ਦਾ ਸਮਝੌਤਾ ਹੋ ਸਕਦਾ ਹੈ। ਜੇ ਸੰਭਵ ਹੋਵੇ, ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਵੱਖਰੇ TLS ਸਰਟੀਫ਼ਿਕੇਟਾਂ ਦੀ ਸਹੀ ਸੁਰੱਖਿਆ, ਪ੍ਰਬੰਧਨ, ਅਤੇ ਵਰਤੋਂ ਕੀਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ।

| # | Description | Level |
| :---: | :--- | :---: |
| **12.1.1** | Verify that only the latest recommended versions of the TLS protocol are enabled, such as TLS 1.2 and TLS 1.3. The latest version of the TLS protocol must be the preferred option. | 1 |
| **12.1.2** | Verify that only recommended cipher suites are enabled, with the strongest cipher suites set as preferred. L3 applications must only support cipher suites which provide forward secrecy. | 2 |
| **12.1.3** | Verify that the application validates that mTLS client certificates are trusted before using the certificate identity for authentication or authorization. | 2 |
| **12.1.4** | Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured. | 3 |
| **12.1.5** | Verify that Encrypted Client Hello (ECH) is enabled in the application's TLS settings to prevent exposure of sensitive metadata, such as the Server Name Indication (SNI), during TLS handshake processes. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **12.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਿਰਫ਼ TLS ਪ੍ਰੋਟੋਕਾਲ ਦੇ ਨਵੀਨਤਮ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੇ ਸੰਸਕਰਣ ਸਮਰੱਥ ਹਨ, ਜਿਵੇਂ ਕਿ TLS 1.2 ਅਤੇ TLS 1.3। TLS ਪ੍ਰੋਟੋਕਾਲ ਦਾ ਨਵੀਨਤਮ ਸੰਸਕਰਣ ਤਰਜੀਹੀ ਵਿਕਲਪ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। | 1 |
| **12.1.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਿਰਫ਼ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੇ ਸਾਈਫ਼ਰ ਸੂਟ ਸਮਰੱਥ ਹਨ, ਜਿਨ੍ਹਾਂ ਵਿੱਚੋਂ ਸਭ ਤੋਂ ਮਜ਼ਬੂਤ ਸਾਈਫ਼ਰ ਸੂਟਾਂ ਨੂੰ ਤਰਜੀਹੀ ਵਜੋਂ ਸੈੱਟ ਕੀਤਾ ਗਿਆ ਹੈ। L3 ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਸਿਰਫ਼ ਉਹਨਾਂ ਸਾਈਫ਼ਰ ਸੂਟਾਂ ਦਾ ਸਮਰਥਨ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਜੋ ਅੱਗੇ ਦੀ ਗੁਪਤਤਾ (forward secrecy) ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ। | 2 |
| **12.1.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ mTLS ਕਲਾਇੰਟ ਸਰਟੀਫ਼ਿਕੇਟਾਂ ਨੂੰ ਪ੍ਰਮਾਣੀਕਰਨ ਜਾਂ ਅਧਿਕਾਰੀਕਰਨ ਲਈ ਸਰਟੀਫ਼ਿਕੇਟ ਪਛਾਣ ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ ਪ੍ਰਮਾਣਿਤ ਕਰਦੀ ਹੈ ਕਿ ਉਹ ਭਰੋਸੇਯੋਗ ਹਨ। | 2 |
| **12.1.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਹੀ ਸਰਟੀਫ਼ਿਕੇਟ ਰੱਦ ਕਰਨ ਦੀ ਪ੍ਰਣਾਲੀ, ਜਿਵੇਂ ਕਿ Online Certificate Status Protocol (OCSP) Stapling, ਸਮਰੱਥ ਅਤੇ ਕੌਨਫ਼ਿਗਰ ਕੀਤੀ ਗਈ ਹੈ। | 3 |
| **12.1.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ Encrypted Client Hello (ECH) ਐਪਲੀਕੇਸ਼ਨ ਦੀਆਂ TLS ਸੈਟਿੰਗਾਂ ਵਿੱਚ ਸਮਰੱਥ ਹੈ ਤਾਂ ਜੋ TLS ਹੈਂਡਸ਼ੇਕ ਪ੍ਰਕਿਰਿਆਵਾਂ ਦੌਰਾਨ ਸੰਵੇਦਨਸ਼ੀਲ ਮੈਟਾਡਾਟਾ, ਜਿਵੇਂ ਕਿ Server Name Indication (SNI), ਦੇ ਖੁਲਾਸੇ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। | 3 |

## V12.2 HTTPS Communication with External Facing Services
## V12.2 ਬਾਹਰ-ਮੁਖੀ ਸੇਵਾਵਾਂ ਨਾਲ HTTPS ਸੰਚਾਰ

Ensure all HTTP traffic to external-facing services which the application exposes is sent encrypted, with publicly trusted certificates.

ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਉਜਾਗਰ ਕੀਤੀਆਂ ਬਾਹਰ-ਮੁਖੀ ਸੇਵਾਵਾਂ ਨੂੰ ਜਾਣ ਵਾਲਾ ਸਾਰਾ HTTP ਟ੍ਰੈਫ਼ਿਕ ਜਨਤਕ ਤੌਰ 'ਤੇ ਭਰੋਸੇਯੋਗ ਸਰਟੀਫ਼ਿਕੇਟਾਂ ਨਾਲ ਏਨਕ੍ਰਿਪਟ ਕਰਕੇ ਭੇਜਿਆ ਜਾਵੇ।

| # | Description | Level |
| :---: | :--- | :---: |
| **12.2.1** | Verify that TLS is used for all connectivity between a client and external facing, HTTP-based services, and does not fall back to insecure or unencrypted communications. | 1 |
| **12.2.2** | Verify that external facing services use publicly trusted TLS certificates. | 1 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **12.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ TLS ਦੀ ਵਰਤੋਂ ਕਲਾਇੰਟ ਅਤੇ ਬਾਹਰ-ਮੁਖੀ, HTTP-ਆਧਾਰਿਤ ਸੇਵਾਵਾਂ ਦੇ ਵਿਚਕਾਰ ਸਾਰੀ ਕਨੈਕਟੀਵਿਟੀ ਲਈ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਅਤੇ ਇਹ ਅਸੁਰੱਖਿਅਤ ਜਾਂ ਏਨਕ੍ਰਿਪਟ ਨਾ ਕੀਤੇ ਸੰਚਾਰਾਂ 'ਤੇ ਵਾਪਸ ਨਹੀਂ ਜਾਂਦੀ। | 1 |
| **12.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਬਾਹਰ-ਮੁਖੀ ਸੇਵਾਵਾਂ ਜਨਤਕ ਤੌਰ 'ਤੇ ਭਰੋਸੇਯੋਗ TLS ਸਰਟੀਫ਼ਿਕੇਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ। | 1 |

## V12.3 General Service to Service Communication Security
## V12.3 ਆਮ ਸੇਵਾ-ਤੋਂ-ਸੇਵਾ ਸੰਚਾਰ ਸੁਰੱਖਿਆ

Server communications (both internal and external) involve more than just HTTP. Connections to and from other systems must also be secure, ideally using TLS.

ਸਰਵਰ ਸੰਚਾਰਾਂ (ਅੰਦਰੂਨੀ ਅਤੇ ਬਾਹਰੀ ਦੋਵੇਂ) ਵਿੱਚ HTTP ਤੋਂ ਇਲਾਵਾ ਹੋਰ ਵੀ ਸ਼ਾਮਲ ਹੈ। ਹੋਰ ਸਿਸਟਮਾਂ ਨੂੰ ਅਤੇ ਉਹਨਾਂ ਤੋਂ ਸੰਪਰਕ ਵੀ ਸੁਰੱਖਿਅਤ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ, ਆਦਰਸ਼ਕ ਤੌਰ 'ਤੇ TLS ਦੀ ਵਰਤੋਂ ਕਰਕੇ।

| # | Description | Level |
| :---: | :--- | :---: |
| **12.3.1** | Verify that an encrypted protocol such as TLS is used for all inbound and outbound connections to and from the application, including monitoring systems, management tools, remote access and SSH, middleware, databases, mainframes, partner systems, or external APIs. The server must not fall back to insecure or unencrypted protocols. | 2 |
| **12.3.2** | Verify that TLS clients validate certificates received before communicating with a TLS server. | 2 |
| **12.3.3** | Verify that TLS or another appropriate transport encryption mechanism used for all connectivity between internal, HTTP-based services within the application, and does not fall back to insecure or unencrypted communications. | 2 |
| **12.3.4** | Verify that TLS connections between internal services use trusted certificates. Where internally generated or self-signed certificates are used, the consuming service must be configured to only trust specific internal CAs and specific self-signed certificates. | 2 |
| **12.3.5** | Verify that services communicating internally within a system (intra-service communications) use strong authentication to ensure that each endpoint is verified. Strong authentication methods, such as TLS client authentication, must be employed to ensure identity, using public-key infrastructure and mechanisms that are resistant to replay attacks. For microservice architectures, consider using a service mesh to simplify certificate management and enhance security. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **12.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇੱਕ ਏਨਕ੍ਰਿਪਟ ਕੀਤੇ ਪ੍ਰੋਟੋਕਾਲ ਜਿਵੇਂ ਕਿ TLS ਦੀ ਵਰਤੋਂ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਅਤੇ ਉਸ ਤੋਂ ਸਾਰੇ ਅੰਦਰ-ਆਉਣ ਵਾਲੇ ਅਤੇ ਬਾਹਰ-ਜਾਣ ਵਾਲੇ ਸੰਪਰਕਾਂ ਲਈ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਨਿਗਰਾਨੀ ਸਿਸਟਮ, ਪ੍ਰਬੰਧਨ ਟੂਲ, ਰਿਮੋਟ ਪਹੁੰਚ ਅਤੇ SSH, ਮਿਡਲਵੇਅਰ, ਡਾਟਾਬੇਸ, ਮੇਨਫ਼੍ਰੇਮ, ਭਾਈਵਾਲ ਸਿਸਟਮ, ਜਾਂ ਬਾਹਰੀ API ਸ਼ਾਮਲ ਹਨ। ਸਰਵਰ ਨੂੰ ਅਸੁਰੱਖਿਅਤ ਜਾਂ ਏਨਕ੍ਰਿਪਟ ਨਾ ਕੀਤੇ ਪ੍ਰੋਟੋਕਾਲਾਂ 'ਤੇ ਵਾਪਸ ਨਹੀਂ ਜਾਣਾ ਚਾਹੀਦਾ। | 2 |
| **12.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ TLS ਕਲਾਇੰਟ TLS ਸਰਵਰ ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਪ੍ਰਾਪਤ ਕੀਤੇ ਸਰਟੀਫ਼ਿਕੇਟਾਂ ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਦੇ ਹਨ। | 2 |
| **12.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ TLS ਜਾਂ ਕੋਈ ਹੋਰ ਢੁਕਵੀਂ ਟ੍ਰਾਂਸਪੋਰਟ ਏਨਕ੍ਰਿਪਸ਼ਨ ਪ੍ਰਣਾਲੀ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਅੰਦਰ ਅੰਦਰੂਨੀ, HTTP-ਆਧਾਰਿਤ ਸੇਵਾਵਾਂ ਦੇ ਵਿਚਕਾਰ ਸਾਰੀ ਕਨੈਕਟੀਵਿਟੀ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ, ਅਤੇ ਇਹ ਅਸੁਰੱਖਿਅਤ ਜਾਂ ਏਨਕ੍ਰਿਪਟ ਨਾ ਕੀਤੇ ਸੰਚਾਰਾਂ 'ਤੇ ਵਾਪਸ ਨਹੀਂ ਜਾਂਦੀ। | 2 |
| **12.3.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਅੰਦਰੂਨੀ ਸੇਵਾਵਾਂ ਦੇ ਵਿਚਕਾਰ TLS ਸੰਪਰਕ ਭਰੋਸੇਯੋਗ ਸਰਟੀਫ਼ਿਕੇਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ। ਜਿੱਥੇ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ ਪੈਦਾ ਕੀਤੇ ਜਾਂ ਸਵੈ-ਦਸਤਖ਼ਤੀ ਸਰਟੀਫ਼ਿਕੇਟ ਵਰਤੇ ਜਾਂਦੇ ਹਨ, ਉਪਭੋਗ ਕਰਨ ਵਾਲੀ ਸੇਵਾ ਨੂੰ ਸਿਰਫ਼ ਖ਼ਾਸ ਅੰਦਰੂਨੀ CA ਅਤੇ ਖ਼ਾਸ ਸਵੈ-ਦਸਤਖ਼ਤੀ ਸਰਟੀਫ਼ਿਕੇਟਾਂ 'ਤੇ ਭਰੋਸਾ ਕਰਨ ਲਈ ਕੌਨਫ਼ਿਗਰ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ। | 2 |
| **12.3.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਇੱਕ ਸਿਸਟਮ ਦੇ ਅੰਦਰ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ ਸੰਚਾਰ ਕਰਨ ਵਾਲੀਆਂ ਸੇਵਾਵਾਂ (ਇੰਟਰਾ-ਸੇਵਾ ਸੰਚਾਰ) ਮਜ਼ਬੂਤ ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ ਤਾਂ ਜੋ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਹਰ ਅੰਤ-ਬਿੰਦੂ ਦੀ ਤਸਦੀਕ ਕੀਤੀ ਜਾਵੇ। ਪਛਾਣ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਮਜ਼ਬੂਤ ਪ੍ਰਮਾਣੀਕਰਨ ਵਿਧੀਆਂ, ਜਿਵੇਂ ਕਿ TLS ਕਲਾਇੰਟ ਪ੍ਰਮਾਣੀਕਰਨ, ਨੂੰ ਨਿਯੁਕਤ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਜਨਤਕ-ਕੁੰਜੀ ਬੁਨਿਆਦੀ ਢਾਂਚੇ (PKI) ਅਤੇ ਪ੍ਰਣਾਲੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜੋ ਰੀਪਲੇ ਹਮਲਿਆਂ ਪ੍ਰਤੀ ਰੋਧਕ ਹਨ। ਮਾਈਕਰੋਸਰਵਿਸ ਆਰਕੀਟੈਕਚਰ ਲਈ, ਸਰਟੀਫ਼ਿਕੇਟ ਪ੍ਰਬੰਧਨ ਨੂੰ ਸਰਲ ਬਣਾਉਣ ਅਤੇ ਸੁਰੱਖਿਆ ਵਧਾਉਣ ਲਈ ਸੇਵਾ ਮੈਸ਼ (service mesh) ਦੀ ਵਰਤੋਂ ਕਰਨ 'ਤੇ ਵਿਚਾਰ ਕਰੋ। | 3 |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP - Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
* [Mozilla's Server Side TLS configuration guide](https://wiki.mozilla.org/Security/Server_Side_TLS)
* [Mozilla's tool to generate known good TLS configurations](https://ssl-config.mozilla.org/).
* [O-Saft - OWASP Project to validate TLS configuration](https://owasp.org/www-project-o-saft/)
