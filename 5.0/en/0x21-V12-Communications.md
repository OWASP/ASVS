# V12 Secure Communication

## Control Objective

This chapter includes requirements related to the specific mechanisms that should be in place to protect data in transit, both between an end user client and a backend service but also between internal and backend services.

The general concepts promoted by this chapter include:

* Require TLS or strong encryption, independent of the sensitivity of the content.
* Follow the latest guidance, including:
    * Configuration advice
    * Preferred algorithms and ciphers
* Avoid weak or soon-to-be deprecated algorithms and ciphers, except as a last resort.
* Disable deprecated or known insecure algorithms and ciphers.

Within these requirements:

* Stay current with recommended industry advice on secure TLS configuration, as it changes frequently (often due to catastrophic breaks in existing algorithms and ciphers).
* Use the most recent versions of TLS configuration review tools to configure the preferred order and algorithm selection.
* Check your configuration periodically to ensure that secure communication is always present and effective.

In addition to outlining general principles and best practices, this document also provides more in-depth technical information about cryptographic strength in [Appendix V](./0x97-Appendix-V_Cryptography.md).

## V12.1 General TLS Security Guidance

Use secure TLS configuration and up-to-date tools to review the configuration on a regular basis. While usage of wildcard TLS certificates is not inherently insecure, a compromise of a certificate that is deployed across all owned environments (e.g., production, staging, development and test) may lead to a compromise of the security posture of the applications using it. Proper protection, management, and usage of separate TLS certificates in different environments should be employed if possible.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **12.1.1** | Verify that only the latest recommended versions of the TLS protocol are enabled, such as TLS 1.2 and TLS 1.3. The latest version of the TLS protocol must be the preferred option. | 1 | v5.0.be-9.4.2 |
| **12.1.2** | Verify that only the latest recommended cipher suites are enabled, with the strongest cipher suites set as preferred. L3 applications must only support cipher suites which provide forward secrecy. | 2 | v5.0.be-9.4.1 |
| **12.1.3** | Verify that the application validates that mTLS client certificates are trusted before using the certificate identity for authentication or authorization. | 2 | v5.0.be-9.4.5 |
| **12.1.4** | Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured. | 3 | v5.0.be-9.4.3 |
| **12.1.5** | Verify that Encrypted Client Hello (ECH) is supported and is securely configured within the application's TLS settings to prevent exposure of sensitive metadata, such as the Server Name Indication (SNI), during TLS handshake processes. | 3 | v5.0.be-9.4.4 |

## V12.2 HTTPS Communication with External Facing Services

Ensure all HTTP traffic to external-facing services which the application exposes is sent encrypted, with publicly trusted certificates.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **12.2.1** | Verify that TLS is used for all connectivity between a client and external facing, HTTP-based services, and does not fall back to insecure or unencrypted communications. | 1 | v5.0.be-9.1.1 |
| **12.2.2** | Verify that external facing services use publicly trusted TLS certificates. | 1 | v5.0.be-9.1.4 |

## V12.3 General Service to Service Communication Security

Server communications involve more than just HTTP. Connections to and from other systems must also be secure.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **12.3.1** | Verify that an encrypted protocol such as TLS is used for all inbound and outbound connections to and from the application, including monitoring systems, management tools, remote access and SSH, middleware, databases, mainframes, partner systems, or external APIs. The server must not fall back to insecure or unencrypted protocols. | 2 | v5.0.be-9.2.2 |
| **12.3.2** | Verify that TLS clients validate certificates received before communicating with a TLS server. | 2 | v5.0.be-9.2.6 |

## V12.4 HTTPS Communication between Internal Services

HTTP traffic between internal-facing services should also be encrypted, ideally using TLS.

| # | Description | Level | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **12.4.1** | Verify that TLS or another appropriate transport encryption mechanism used for all connectivity between internal, HTTP-based services within the application, and does not fall back to insecure or unencrypted communications. | 2 | v5.0.be-9.3.1 |
| **12.4.2** | Verify that TLS connections between internal services use trusted certificates. Where internally generated or self-signed certificates are used, the consuming service must be configured to only trust specific internal CAs and specific self-signed certificates. All others must be rejected. | 2 | v5.0.be-9.3.2 |
| **12.4.3** | Verify that services communicating internally within a system (intra-service communications) use strong authentication to ensure that each endpoint is verified. Strong authentication methods, such as mTLS, must be employed to ensure identity, using public-key infrastructure and mechanisms that are resistant to replay attacks. For microservice architectures, consider using a service mesh to simplify certificate management and enhance security. | 3 | v5.0.be-9.3.3 |

## References

For more information, see also:

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
* The ideal way to achieve compliance with section 9.4 would be to review guides such as [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) or [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known and up-to-date TLS evaluation tools to obtain a desired level of security.
