# V10: Communications Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* That TLS is used where sensitive data is transmitted.
* That strong algorithms and ciphers are used at all times.


## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **10.1** | Verify that a path can be built from a trusted CA to each Transport Layer Security (TLS) server certificate, and that each server certificate is valid. | ✓ | ✓ | ✓ | 1.0 |
| **10.1** | Verify that TLS is used for all connections (including both external and backend connections) that are authenticated or that involve sensitive data or functions, and does not fall back to insecure or unencrypted protocols. Ensure the strongest alternative is the preferred algorithm. | ✓ | ✓ | ✓ | 3.0 |
| **10.1** | Verify that backend TLS connection failures are logged. |  |  | ✓ | 1.0 |
| **10.1** | Verify that certificate paths are built and verified for all client certificates using configured trust anchors and revocation information. |  |  | ✓ | 1.0 |
| **10.1** | Verify that all connections to external systems that involve sensitive information or functions are authenticated. |  | ✓ | ✓ | 1.0 |
| **10.1** | Verify that there is a single standard TLS implementation that is used by the application that is configured to operate in an approved mode of operation. |  |  | ✓ | 1.0 |
| **10.1** | Verify that TLS certificate public key pinning (HPKP) is implemented with production and backup public keys. For more information, please see the references below.  |  | ✓ | ✓ | 3.0.1 |
| **10.1** | Verify that HTTP Strict Transport Security headers are included on all requests and for all subdomains, such as Strict-Transport-Security: max-age=15724800; includeSubdomains | ✓ | ✓ | ✓ | 3.0 |
| **10.1** | Verify that production website URL has been submitted to preloaded list of Strict Transport Security domains maintained by web browser vendors. Please see the references below. |  |  | ✓ | 3.0 |
| **10.1** | Verify that perfect forward secrecy is configured to mitigate passive attackers recording traffic. | ✓ | ✓ | ✓ | 3.1 |
| **10.1** | Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured. | ✓ | ✓ | ✓ | 3.0 |
| **10.1** | Verify that only strong algorithms, ciphers, and protocols are used, through all the certificate hierarchy, including root and intermediary certificates of your selected certifying authority. | ✓ | ✓ | ✓ | 3.0 |
| **10.1** | Verify that the TLS settings are in line with current leading practice, particularly as common configurations, ciphers, and algorithms become insecure. | ✓ | ✓ | ✓ | 3.0 |



## References

For more information, see also:

* [OWASP – TLS Cheat Sheet. ](https://www.owasp.org/index.php/Transport_Layer_Protection_Cheat_Sheet)
* [Notes on “Approved modes of TLS”. In the past, the ASVS referred to the US standard FIPS 140-2, but as a global standard, applying US standards this can be difficult, contradictory, or confusing to apply. A better method of achieving compliance with 10.8 would be to review guides such as (https://wiki.mozilla.org/Security/Server_Side_TLS), generate known good configurations (https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known TLS evaluation tools, such as sslyze, various vulnerability scanners or trusted TLS online assessment services to obtain a desired level of security. In general, we see non-compliance for this section being the use of outdated or insecure ciphers and algorithms, the lack of perfect forward secrecy, outdated or insecure SSL protocols, weak preferred ciphers, and so on.]
* [Certificate pinning. For more information please review ](https://tools.ietf.org/html/rfc7469.)The rationale behind certificate pinning for production and backup keys is business continuity - see (https://noncombatant.org/2015/05/01/about-http-public-key-pinning/)
* [OWASP Certificate Pinning Cheat Sheet](https://www.owasp.org/index.php/Pinning_Cheat_Sheet)
* [OWASP Certificate and Public Key Pinning](https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning)
* [Time of first use (TOFU) Pinning](https://developer.mozilla.org/en/docs/Web/Security/Public_Key_Pinning)
* [Pre-loading HTTP Strict Transport Security](https://www.chromium.org/hsts)
