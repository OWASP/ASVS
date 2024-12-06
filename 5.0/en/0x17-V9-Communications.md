# V9 Secure Communication

## Control Objective

This chapter includes requirements related to the specific mechanisms that should be in place to protect data in transit, both between an end user client and a back-end service but also between internal and back-end services.

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

## V1.9 Communications Documentation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.9.1** | [DELETED, DUPLICATE OF 9.1.1, 9.2.2, 9.3.1] | | | | |
| **1.9.2** | [DELETED, DUPLICATE OF 9.2.3, 9.3.2] | | | | |

## V9.1 HTTPS Communication with External Facing Services

Ensure all HTTP traffic to external-facing services which the application exposes is sent encrypted, with publicly trusted certificates.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **9.1.1** | [MODIFIED] Verify that TLS is used for all connectivity between a client and external facing, HTTP-based services, and does not fall back to insecure or unencrypted communications. | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | [MOVED TO 9.4.1] | | | | |
| **9.1.3** | [MOVED TO 9.4.2] | | | | |
| **9.1.4** | [ADDED] Verify that external facing services use publicly trusted TLS certificates. | ✓ | ✓ | ✓ | 295 |

## V9.2 General Service to Service Communication Security

Server communications involve more than just HTTP. Connections to and from other systems must also be secure.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **9.2.1** | [MOVED TO 9.3.2] | | | | |
| **9.2.2** | [MODIFIED] Verify that an encrypted protocol such as TLS is used for all inbound and outbound connections to and from the application, including monitoring systems, management tools, remote access and SSH, middleware, databases, mainframes, partner systems, or external APIs. The server must not fall back to insecure or unencrypted protocols. | | ✓ | ✓ | 319 |
| **9.2.3** | [DELETED, NOT IN SCOPE] | | | | |
| **9.2.4** | [MOVED TO 9.4.3] | | | | |
| **9.2.5** | [MOVED TO 7.2.6] | | | | |
| **9.2.6** | [ADDED] Verify that TLS clients validate certificates received before communicating with a TLS server. | ✓ | ✓ | ✓ | |

## V9.3 HTTPS Communication between Internal Services

HTTP traffic between internal-facing services should also be encrypted, ideally using TLS.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **9.3.1** | [ADDED] Verify that TLS or another appropriate transport encryption mechanism used for all connectivity between internal, HTTP-based services within the application, and does not fall back to insecure or unencrypted communications. | | ✓ | ✓ | 319 |
| **9.3.2** | [MODIFIED, MOVED FROM 9.2.1] Verify that TLS connections between internal services use trusted certificates. Where internally generated or self-signed certificates are used, the consuming service must be configured to only trust specific internal CAs and specific self-signed certificates. All others should be rejected. | | ✓ | ✓ | 295 |
| **9.3.3** | [MODIFIED, MOVED FROM 2.2.5] Verify that services communicating internally within a system (intra-service communications) use strong authentication to ensure that each endpoint is verified. Strong authentication methods, such as mTLS, should be employed to ensure identity, using public-key infrastructure and mechanisms that are resistant to replay attacks. For microservice architectures, consider using a service mesh to simplify certificate management and enhance security. | | | ✓ | 295 |

## V9.4 General TLS Security Guidance

Use secure TLS configuration and up-to-date tools to review the configuration on a regular basis. While usage of wildcard TLS certificates is not inherently insecure, a compromise of a certificate that is deployed across all owned environments (e.g. production, staging, development, test, etc.) may lead to a compromise of the security posture of the applications using it. Proper protection, management, and usage of separate TLS certificates in different environments should be employed if possible.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **9.4.1** | [MODIFIED, MOVED FROM 9.1.2] Verify that only the latest recommended cipher suites are enabled, with the strongest cipher suites set as preferred. L3 applications must only support cipher suites which provide forward secrecy. | ✓ | ✓ | ✓ | 326 |
| **9.4.2** | [MOVED FROM 9.1.3] Verify that only the latest recommended versions of the TLS protocol are enabled, such as TLS 1.2 and TLS 1.3. The latest version of the TLS protocol should be the preferred option. | ✓ | ✓ | ✓ | 326 |
| **9.4.3** | [MOVED FROM 9.2.4] Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured. | | ✓ | ✓ | 299 |
| **9.4.4** | [ADDED] Verify that Encrypted Client Hello (ECH) is supported and properly configured within the application’s TLS settings to prevent exposure of sensitive metadata, such as the Server Name Indication (SNI), during TLS handshake processes. | | | ✓ | |
| **9.4.5** | [ADDED] Verify that the application validates that mTLS client certificates are trusted before using the certificate identity for authentication or authorization. | | | ✓ | |

## References

For more information, see also:

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
* The ideal way to achieve compliance with section 9.4 would be to review guides such as [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) or [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known and up-to-date TLS evaluation tools to obtain a desired level of security.
