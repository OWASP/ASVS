# V9 Communication

## Control Objective

Ensure that a verified application meets the following high level requirements:

* Require TLS or strong encryption, independent of sensitivity of the content.
* Follow the latest guidance, including:
  * Configuration advice
  * Preferred algorithms and ciphers
* Avoid weak or soon to be deprecated algorithms and ciphers, except as a last resort
* Disable deprecated or known insecure algorithms and ciphers.

Within these requirements:

* Stay current with recommended industry advice on secure TLS configuration, as it changes frequently (often due to catastrophic breaks in existing algorithms and ciphers).
* Use the most recent versions of TLS configuration review tools to configure the preferred order and algorithm selection.
* Check your configuration periodically to ensure that secure communication is always present and effective.

## V9.1 Client Communication Security

Ensure all client messages are sent over encrypted networks, using TLS 1.2 or later.
Use up to date tools to review the client configuration on a regular basis.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.1.1** | [MODIFIED] Verify that TLS is used for all client connectivity, and does not fall back to insecure or unencrypted communications. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | [MODIFIED] Verify using up to date TLS testing tools that only strong cipher suites are enabled, with the strongest cipher suites set as preferred. | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | [MODIFIED] Verify that only the latest recommended versions of the TLS protocol are enabled, such as TLS 1.2 and TLS 1.3. The latest version of the TLS protocol should be the preferred option. | ✓ | ✓ | ✓ | 326 |


## V9.2 Server Communication Security

Server communications are more than just HTTP. Secure connections to and from other systems, such as monitoring systems, management tools, remote access and ssh, middleware, database, mainframes, partner or external source systems &mdash; must be in place. All of these must be encrypted to prevent "hard on the outside, trivially easy to intercept on the inside".

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.2.1** | [LEVEL L2 > L1] Verify that connections to and from the server use trusted TLS certificates. Where internally generated or self-signed certificates are used, the server must be configured to only trust specific internal CAs and specific self-signed certificates. All others should be rejected. | ✓ | ✓ | ✓ | 295 |
| **9.2.2** | Verify that encrypted communications such as TLS is used for all inbound and outbound connections, including for management ports, monitoring, authentication, API, or web service calls, database, cloud, serverless, mainframe, external, and partner connections. The server must not fall back to insecure or unencrypted protocols. | | ✓ | ✓ | 319 |
| **9.2.3** | Verify that all encrypted connections to external systems that involve sensitive information or functions are authenticated. | | ✓ | ✓ | 287 |
| **9.2.4** | Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured. | | ✓ | ✓ | 299 |
| **9.2.5** | Verify that backend TLS connection failures are logged. | | | ✓ | 544 |

## References

For more information, see also:

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* [OWASP - Pinning Guide](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)
* Notes on “Approved modes of TLS”:
    * In the past, the ASVS referred to the US standard FIPS 140-2, but as a global standard, applying US standards can be difficult, contradictory, or confusing to apply.
    * A better method of achieving compliance with section 9.1 would be to review guides such as [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) or [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known and up to date TLS evaluation tools to obtain a desired level of security.
