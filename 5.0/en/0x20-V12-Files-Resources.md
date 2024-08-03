# V12 File and Resources

## Control Objective

Ensure that a verified application satisfies the following high-level requirements:

* Untrusted file data should be handled accordingly and in a secure manner.
* Untrusted file data obtained from untrusted sources are stored outside the web root and with limited permissions.

## V12.1 File Upload

Although zip bombs can be effectively tested using penetration testing techniques, they are classified as L2 and above to encourage consideration during design and development, as well as careful manual testing. This classification also aims to prevent automated or unskilled manual penetration testing from triggering a denial of service condition.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.1.1** | [MODIFIED] Verify that the application will only accept files of a size which it can process without causing a loss of performance or denial of service attack. | ✓ | ✓ | ✓ | 400 |
| **12.1.2** | Verify that the application checks compressed files (e.g. zip, gz, docx, odt) against maximum allowed uncompressed size and against maximum number of files before uncompressing the file. | | ✓ | ✓ | 409 |
| **12.1.3** | Verify that a file size quota and maximum number of files per user is enforced to ensure that a single user cannot fill up the storage with too many files, or excessively large files. | | ✓ | ✓ | 770 |
| **12.1.4** | [ADDED] Verify that the application does not allow uploading compressed files containing symlinks unless this is specifically required (in which case it will be necessary to enforce an allow list of the files that can be symlinked to). | | ✓ | ✓ | 61 |

## V12.2 File Integrity

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.2.1** | [MODIFIED] Verify that when the application accepts a file, it checks if the file extension matches an expected file extension and validates that the contents correspond to the type represented by the extension. This includes, but is not limited to, checking the initial 'magic bytes', performing image re-writing, and using specialized libraries for file content validation. | | ✓ | ✓ | 434 |
| **12.2.2** | [ADDED] Verify that the application blocks uploaded images with a pixel size larger than the maximum allowed, to prevent pixel flood attacks. | ✓ | ✓ | ✓ | 400 |

## V12.3 File Execution

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.3.1** | Verify that user-submitted filename metadata is not used directly by system or framework filesystems and that a URL API is used to protect against path traversal. | ✓ | ✓ | ✓ | 22 |
| **12.3.2** | Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure, creation, updating or removal of local files (LFI). | ✓ | ✓ | ✓ | 73 |
| **12.3.3** | Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure or execution of remote files via Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks. | ✓ | ✓ | ✓ | 73 |
| **12.3.4** | [MOVED TO 12.5.3] | | | | |
| **12.3.5** | [DELETED, DUPLICATE OF 5.3.8] | | | | |
| **12.3.6** | Verify that the application does not include and execute functionality from untrusted sources, such as unverified content distribution networks, JavaScript libraries, node npm libraries, or server-side DLLs. | | ✓ | ✓ | 829 |
| **12.3.7** | [ADDED] Verify that server-side file processing such as file decompression ignores user-provided path information to prevent vulnerabilities such as zip slip. | ✓ | ✓ | ✓ | 23 |

## V12.4 File Storage

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.4.1** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **12.4.2** | Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent upload and serving of known malicious content. | ✓ | ✓ | ✓ | 509 |

## V12.5 File Download

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.5.1** | [MOVED TO 14.3.6] | | | | |
| **12.5.2** | [MOVED TO 50.5.1] | | | | |
| **12.5.3** | [MODIFIED, MOVED FROM 12.3.4] Verify that the application validates or ignores user-submitted filenames, including in a JSON, JSONP, or URL parameter and specifies a filename in the Content-Disposition header in the response. | ✓ | ✓ | ✓ | 641 |

## V12.6 SSRF Protection

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.6.1** | [MOVED TO 14.7.1] | | | | |

## V12.7 Application Resources

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.7.1** | [ADDED] Verify that the application proactively releases system resources, such as database connections, open files, threads, etc, when it finishes using them to prevent resource exhaustion. | | ✓ | ✓ | 404 |

## References

For more information, see also:

* [File Extension Handling for Sensitive Information](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
* [OWASP Third Party JavaScript Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html)
* [Example of using symlinks for arbitrary file read](https://hackerone.com/reports/1439593)
* [Explanation of "Magic Bytes" from Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures)
