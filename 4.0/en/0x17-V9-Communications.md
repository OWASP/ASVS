# V9: Communications Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* TLS or strong encryption is always used, regardless of the sensitivity of the data being transmitted
* The most recent, leading configuration advice is used to enable and order preferred algorithms and ciphers
* Weak or soon to be deprecated algorithms and ciphers are ordered as a last resort
* Deprecated or known insecure algorithms and ciphers are disabled.

Leading industry advice on secure TLS configuration changes frequently, often due to catastrophic breaks in existing algorithms and ciphers. Always use the most recent versions of TLS configuration review tools (such as SSLyze or other TLS scanners) to configure the preferred order and algorithm selection. Configuration should be periodically checked to ensure that secure communications configuration is always present and effective.

## V9.1 Communications Security Requirements

All client communications should only take place over encrypted communication paths. In particular, the use of TLS 1.2 or later is essentially all but required by modern browsers and search engines. Configuration should be regularly reviewed using online tools to ensure that the latest leading practices are in place.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.1.1** | Verify that secured TLS is used for all client connectivity, and does not fall back to insecure or unencrypted protocols. ([C8](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | Verify using online or up to date TLS testing tools that only strong algorithms, ciphers, and protocols are enabled, with the strongest algorithms and ciphers set as preferred. | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | Verify that old versions of SSL and TLS protocols, algorithms, ciphers, and configuration are disabled, such as SSLv2, SSLv3, or TLS 1.0 and TLS 1.1. The latest version of TLS should be the preferred cipher suite. | ✓ | ✓ | ✓ | 326 |

## V9.2 Server Communications Security Requirements

Server communications are more than just HTTP. Secure connections to and from other systems, such as monitoring systems, management tools, remote access and ssh, middleware, database, mainframes, partner or external source systems &mdash; must be in place. All of these must be encrypted to prevent "hard on the outside, trivially easy to intercept on the inside".

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.2.1** | Verify that connections to and from the server use trusted TLS certificates. Where internally generated or self-signed certificates are used, the server must be configured to only trust specific internal CAs and specific self-signed certificates. All others should be rejected. | | ✓ | ✓ | 295 |
| **9.2.2** | Verify that encrypted communications such as TLS is used for all inbound and outbound connections, including for management ports, monitoring, authentication, API, or web service calls, database, cloud, serverless, mainframe, external, and partner connections. The server must not fall back to insecure or unencrypted protocols. |  | ✓ | ✓ | 319 |
| **9.2.3** | Verify that all encrypted connections to external systems that involve sensitive information or functions are authenticated. |  | ✓ | ✓ | 287 |
| **9.2.4** | Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured. |  | ✓ | ✓ | 299 |
| **9.2.5** | Verify that backend TLS connection failures are logged. |  |  | ✓ | 544 |

## References

For more information, see also:

* [OWASP – TLS Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.md)
* Notes on “Approved modes of TLS”. In the past, the ASVS referred to the US standard FIPS 140-2, but as a global standard, applying US standards can be difficult, contradictory, or confusing to apply. A better method of achieving compliance with 9.1.3 would be to review guides such as [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) or  [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known TLS evaluation tools, such as sslyze, various vulnerability scanners or trusted TLS online assessment services to obtain a desired level of security. In general, we see non-compliance for this section being the use of outdated or insecure ciphers and algorithms, the lack of perfect forward secrecy, outdated or insecure SSL protocols, weak preferred ciphers, and so on.
