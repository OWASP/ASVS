# V10: Communications Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* TLS or strong encryption is always used, regardless of the sensitivity of the data being transmitted
* The most recent leading configuration advice is used to enable and order preferred algorithms and ciphers
* Weak or soon to be deprecated algorithms and ciphers are ordered as a last resort
* Deprecated or known insecure algorithms and ciphers are disabled.

Leading industry advice on secure TLS configuration changes frequently, often due to catastrophic breaks in existing algorithms and ciphers. Always use the most recent versions of TLS configuration review tools (such as SSLyze or other TLS scanners) to configure the preferred order and algorithm selection. Configuration should be periodically checked to ensure that secure communications configuration is always present and effective.

## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **10.1** | Verify that a path can be built from a trusted CA to each Transport Layer Security (TLS) server certificate, and that each server certificate is valid. | ✓ | ✓ | ✓ | 1.0 |
| **10.3** | Verify that TLS is used for all connections (including for authentication, API or web service calls, backend, external, and partner connections), and does not fall back to insecure or unencrypted protocols. | ✓ | ✓ | ✓ | 3.0 |
| **10.4** | Verify that backend TLS connection failures are logged. |  |  | ✓ | 1.0 |
| **10.5** | Verify that certificate paths are built and verified for all client certificates using configured trust anchors and revocation information. |  |  | ✓ | 1.0 |
| **10.6** | Verify that all connections to external systems that involve sensitive information or functions are authenticated. |  | ✓ | ✓ | 1.0 |
| **10.11** | Verify that HTTP Strict Transport Security headers are included on all requests and for all subdomains, such as Strict-Transport-Security: max-age=15724800; includeSubdomains. | ✓ | ✓ | ✓ | 3.0 |
| **10.12** | Verify that the application's URL has been submitted to a preloaded list of Strict Transport Security domains maintained by web browser vendors. Please see the references below. |  |  | ✓ | 3.0 |
| **10.14** | Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured. | ✓ | ✓ | ✓ | 3.0 |
| **10.15** | Verify that only strong algorithms, ciphers, and protocols are enabled, with the strongest algorithms and ciphers set as preferred, to provide both confidentiality and integrity. | ✓ | ✓ | ✓ | 3.0 |
| **10.17** | Verify that old versions of SSL and TLS protocols, algorithms, ciphers, and configuration are not used, such as SSLv2/3 or TLS 1.0. The latest version of TLS should be the preferred cipher suite. | ✓ | ✓ | ✓ | 3.0 |

## References

For more information, see also:

* [OWASP – TLS Cheat Sheet](https://www.owasp.org/index.php/Transport_Layer_Protection_Cheat_Sheet)
* Notes on “Approved modes of TLS”. In the past, the ASVS referred to the US standard FIPS 140-2, but as a global standard, applying US standards can be difficult, contradictory, or confusing to apply. A better method of achieving compliance with 10.8 would be to review guides such as [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) or  [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known TLS evaluation tools, such as sslyze, various vulnerability scanners or trusted TLS online assessment services to obtain a desired level of security. In general, we see non-compliance for this section being the use of outdated or insecure ciphers and algorithms, the lack of perfect forward secrecy, outdated or insecure SSL protocols, weak preferred ciphers, and so on.
* [Certificate pinning](https://tools.ietf.org/html/rfc7469). The rationale behind certificate pinning for production and backup keys is [business continuity](https://noncombatant.org/2015/05/01/about-http-public-key-pinning/)
* [OWASP Certificate Pinning Cheat Sheet](https://www.owasp.org/index.php/Pinning_Cheat_Sheet)
* [OWASP Certificate and Public Key Pinning](https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning)
* [Time of first use (TOFU) Pinning](https://developer.mozilla.org/en/docs/Web/Security/Public_Key_Pinning)
* [Pre-loading HTTP Strict Transport Security](https://www.chromium.org/hsts)
