# V16: File and Resources Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* Untrusted file data should be handled accordingly and in a secure manner.
* Untrusted file data obtained from untrusted sources are stored outside the web root and with limited permissions.

## Security Verification Requirements

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **16.1** | Verify that URL redirects and forwards only allow whitelisted destinations, or show a warning when redirecting to potentially untrusted content. | ✓ | ✓ | ✓ | 2.0 |
| **16.2** | Verify that untrusted file data submitted to the application is not used directly with file I/O commands, particularly to protect against vulnerabilities involving path traversal, local file include, file mime type, reflective file download, and OS command injection. | ✓ | ✓ | ✓ | 4.0 |
| **16.3** | Verify that files obtained from untrusted sources are validated to be of expected type and scanned by antivirus scanners to prevent upload of known malicious content. | ✓ | ✓ | ✓ | 2.0 |
| **16.4** | Verify that untrusted data is not used within inclusion, class loader, or reflection capabilities to prevent remote/local code execution vulnerabilities. | ✓ | ✓ | ✓ | 4.0 |
| **16.5** | Verify that untrusted data is not used within cross-domain resource sharing (CORS) to protect against arbitrary remote content. See [0x92-Appendix-C_CodeExamples.md](0x92-Appendix-C_CodeExamples.md) for an example of how you might approach this. | ✓ | ✓ | ✓ | 2.0 |
| **16.6** | Verify that files obtained from untrusted sources are stored outside the web root, with limited permissions, preferably with strong validation. |  | ✓ | ✓ | 3.0 |
| **16.7** | Verify that the web or application server is configured by default to deny access to remote resources or systems outside the web or application server. |  | ✓ | ✓ | 2.0 |
| **16.8** | Verify that application code does not execute uploaded data obtained from untrusted sources. | ✓ | ✓ | ✓ | 3.0 |
| **16.9** | Verify that unsupported, insecure or deprecated client-side technologies are not used, such as NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. | ✓ | ✓ | ✓ | 4.0 |
| **16.10** | Verify that the web tier is configured to serve only files with specific file extensions to prevent unintentional information and source code leakage. For example, .bak, .swp and and similar extensions commonly used by editors should not be served by the web tier. | ✓ | ✓ | ✓ | -- | -- |

## References

For more information, see also:

* [File Extension Handling for Sensitive Information](https://www.owasp.org/index.php/Unrestricted_File_Upload)
* [Reflective file download by Oren Hafif](https://www.trustwave.com/Resources/SpiderLabs-Blog/Reflected-File-Download---A-New-Web-Attack-Vector/)
