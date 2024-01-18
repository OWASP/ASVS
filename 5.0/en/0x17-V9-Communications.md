# V9 Communication Encryption

## Control Objective

Ensure that a verified application meets the following high-level requirements:

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

## V9.1 HTTPS Communication with External Facing Services

Ensure all HTTP traffic to external-facing services to the application is sent encrypted, using TLS 1.2 or later, with publically trusted certificates.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **9.1.1** | [MODIFIED] Verify that TLS is used for all connectivity between the client and external facing, HTTP-based services, and does not fall back to insecure or unencrypted communications. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | [MOVED TO 9.4.1] | | | | |
| **9.1.3** | [MOVED TO 9.4.2] | | | | |
| **9.1.4** | [ADDED] Verify that external facing services use publically trusted TLS certificates. | ✓ | ✓ | ✓ | 295 |

## V9.2 General Service-to-Service Communication Security

Server communications involve more than just HTTP. Secure connections to and from other systems, such as monitoring systems, management tools, remote access and SSH, middleware, database, mainframes, partner systems, or external source systems &mdash; must be in place. All of these must be encrypted to prevent "hard on the outside, trivially easy to intercept on the inside".

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **9.2.1** | [MOVED TO 9.3.2] | | | | |
| **9.2.2** | Verify that encrypted communications such as TLS is used for all inbound and outbound connections, including for management ports, monitoring, authentication, API, or web service calls, database, cloud, serverless, mainframe, external, and partner connections. The server must not fall back to insecure or unencrypted protocols. | | ✓ | ✓ | 319 |
| **9.2.3** | Verify that all encrypted connections to external systems that involve sensitive information or functions are authenticated. | | ✓ | ✓ | 287 |
| **9.2.4** | [MOVED TO 9.4.3] | | | | |
| **9.2.5** | Verify that backend TLS connection failures are logged. | | | ✓ | 544 |

## V9.3 HTTPS Communication between Internal Services

HTTP traffic between internal-facing services should also be encrypted, ideally using TLS.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **9.3.1** | [ADDED] Verify that TLS or another appropriate transport encryption mechanism used for all connectivity between internal, HTTP-based services, and does not fall back to insecure or unencrypted communications. | ✓ | ✓ | ✓ | 319 |
| **9.3.2** | [MODIFIED, MOVED FROM 9.2.1] Verify that TLS connections between internal services use trusted certificates. Where internally generated or self-signed certificates are used, the consuming service must be configured to only trust specific internal CAs and specific self-signed certificates. All others should be rejected. | | ✓ | ✓ | 295 |
| **9.3.3** | [ADDED] Verify that mutual TLS (mTLS) is used by services communicating internally within a system or "intra-service communications" to ensure all the involved parties at each end of a network connection are who they claim to be. | | | ✓ | 295 |

## V9.4 General TLS Security Guidance

Use secure TLS configuration and up-to-date tools to review the configuration on a regular basis. While usage of wildcard TLS certificates is not inherently insecure, a compromise of a certificate that is deployed across all owned environments (e.g. production, staging, development, test, etc.) may lead to a compromise of the security posture of the applications using it. Proper protection, management, and usage of separate TLS certificates in different environments should be employed if possible.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **9.4.1** | [MODIFIED, MOVED FROM 9.1.2] Verify that only the latest recommended cipher suites are enabled, with the strongest cipher suites set as preferred. | ✓ | ✓ | ✓ | 326 |
| **9.4.2** | [MOVED FROM 9.1.3] Verify that only the latest recommended versions of the TLS protocol are enabled, such as TLS 1.2 and TLS 1.3. The latest version of the TLS protocol should be the preferred option. | ✓ | ✓ | ✓ | 326 |
| **9.4.3** | [MOVED FROM 9.2.4] Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured. | | ✓ | ✓ | 299 |
| **9.4.4** | [ADDED] Verify that if TLS wildcard certificates are used, wildcard certificates from a non-production environment are not valid for a production environment. | ✓ | ✓ | ✓ | 1008 |

## References

For more information, see also:

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* Notes on “Approved modes of TLS”:
  * In the past, the ASVS referred to the US FIPS 140 standard, but as a global standard, applying US standards can be difficult, contradictory, or confusing to apply.
  * A better method of achieving compliance with section 9.1 would be to review guides such as [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) or [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known and up-to-date TLS evaluation tools to obtain a desired level of security.
