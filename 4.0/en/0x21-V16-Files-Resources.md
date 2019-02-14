# V16: File and Resources Verification Requirements

## Control Objective

Ensure that a verified application satisfies the following high level requirements:

* Untrusted file data should be handled accordingly and in a secure manner.
* Untrusted file data obtained from untrusted sources are stored outside the web root and with limited permissions.

## V16.1 File Upload Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **16.1.1** | Verify that the application will not accept files which are too big and could fill up the server or incur excessive storage costs. | ✓ | ✓ | ✓ | tbd | tbd |
| **16.1.2** | Verify that a file size quota per user is enforced to ensure that a single user cannot fill up the server with too many files. | | ✓ | ✓ | tbd | tbd |

## V16.2 File Integrity Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **16.2.1** | Verify that files obtained from untrusted sources are validated to be of expected type based on the file's "magic number" or other content. | | ✓ | ✓ | tbd | tbd |

## V16.3 File execution Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **16.3.1** | Verify that user-submitted filename metadata is not used directly with system or framework file and URL API to protect against path traversal. | ✓ | ✓ | ✓ | 22 | tbd |
| **16.3.2** | Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure, creation, updating or removal of local files (LFI). | ✓ | ✓ | ✓ | 73 | tbd |
| **16.3.3** | Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure or execution of remote files (RFI), which may also lead to SSRF.  | ✓ | ✓ | ✓ | 98 | tbd |
| **16.3.4** | Verify that the application protects against reflective file download (RFD) by ensuring where an application allows a user-submitted filename in a JSON, JSONP, or URL parameter, the filename is validated or ignored, the resulting Content-Type is set to text/plain, the Content-Disposition header has a fixed filename. | ✓ | ✓ | ✓ | XXX | tbd |
| **16.3.5** | Verify that untrusted file metadata is not used directly with system API or libraries, to protect against OS command injection. | ✓ | ✓ | ✓ | 78 | tbd |
| **16.3.3** | Verify that application does not include and execute functionality, such as external JavaScript libraries or server-side DLLs, from untrusted sources. | ✓ | ✓ | ✓ | 829 | tbd |

## V16.4 File Storage Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **16.4.1** | Verify that files obtained from untrusted sources are stored outside the web root, with limited permissions, preferably with strong validation. | ✓ | ✓ | ✓ | 922 | tbd |
| **16.4.2** | Verify that files obtained from untrusted sources are validated to be of expected type. | ✓ | ✓ | ✓ | 509 | tbd |
| **16.4.3** | Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent upload of known malicious content. | ✓ | ✓ | ✓ | 509 | tbd |

## V16.5 File Download Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **16.5.1** | Verify that the web tier is configured to serve only files with specific file extensions to prevent unintentional information and source code leakage. For example, .bak, .swp and similar extensions commonly used by editors should not be served by the web tier. | ✓ | ✓ | ✓ | 552 | tbd |
| **16.5.2** | Verify that untrusted uploaded HTML and SVG files are only returned as text/plain, and a separate sub-domain with no permission to access session cookies or tokens is used to prevent the uploaded file being used to launch an XSS attack. | ✓ | ✓ | ✓ | 434 | tbd |

## V16.6 SSRF Protection Requirements

| # | Description | L1 | L2 | L3 | CWE | CWSS |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **16.6.1** | Verify that the web or application server is configured by default to deny access to remote resources or systems outside the web or application server. |  | ✓ | ✓ | 15 | tbd |
| **16.6.2** | Verify that URL redirects and forwards only allow whitelisted destinations, or show a warning when redirecting to potentially untrusted content. | ✓ | ✓ | ✓ | 601 | tbd |

## References

For more information, see also:

* [File Extension Handling for Sensitive Information](https://www.owasp.org/index.php/Unrestricted_File_Upload)
* [Reflective file download by Oren Hafif](https://www.trustwave.com/Resources/SpiderLabs-Blog/Reflected-File-Download---A-New-Web-Attack-Vector/)
