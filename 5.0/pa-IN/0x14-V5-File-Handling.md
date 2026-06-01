<!-- Translation Status: ✅ Complete -->
<!-- Original: 5.0/en/0x14-V5-File-Handling.md -->
<!-- Translator: GeeksikhSecurity -->

# V5 File Handling
# V5 ਫ਼ਾਈਲ ਪ੍ਰਬੰਧਨ

## Control Objective
## ਨਿਯੰਤਰਣ ਉਦੇਸ਼

The use of files can present a variety of risks to the application, including denial of service, unauthorized access, and storage exhaustion. This chapter includes requirements to address these risks.

ਫ਼ਾਈਲਾਂ ਦੀ ਵਰਤੋਂ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਕਈ ਤਰ੍ਹਾਂ ਦੇ ਖ਼ਤਰੇ ਪੇਸ਼ ਕਰ ਸਕਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਸੇਵਾ-ਇਨਕਾਰ (denial of service), ਅਣਅਧਿਕਾਰਤ ਪਹੁੰਚ, ਅਤੇ ਭੰਡਾਰਨ ਥਕਾਵਟ ਸ਼ਾਮਲ ਹਨ. ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਇਹਨਾਂ ਖ਼ਤਰਿਆਂ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ.

## V5.1 File Handling Documentation
## V5.1 ਫ਼ਾਈਲ ਪ੍ਰਬੰਧਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ

This section includes a requirement to document the expected characteristics of files accepted by the application, as a necessary precondition for developing and verifying relevant security checks.

ਇਸ ਭਾਗ ਵਿੱਚ ਇੱਕ ਲੋੜ ਸ਼ਾਮਲ ਹੈ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਸਵੀਕਾਰ ਕੀਤੀਆਂ ਜਾਣ ਵਾਲੀਆਂ ਫ਼ਾਈਲਾਂ ਦੀਆਂ ਅਨੁਮਾਨਿਤ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਦਸਤਾਵੇਜ਼ ਕੀਤਾ ਜਾਵੇ, ਜੋ ਸੰਬੰਧਿਤ ਸੁਰੱਖਿਆ ਜਾਂਚਾਂ ਨੂੰ ਵਿਕਸਤ ਅਤੇ ਤਸਦੀਕ ਕਰਨ ਲਈ ਇੱਕ ਜ਼ਰੂਰੀ ਪੂਰਵ-ਸ਼ਰਤ ਹੈ.

| # | Description | Level |
| :---: | :--- | :---: |
| **5.1.1** | Verify that the documentation defines the permitted file types, expected file extensions, and maximum size (including unpacked size) for each upload feature. Additionally, ensure that the documentation specifies how files are made safe for end-users to download and process, such as how the application behaves when a malicious file is detected. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **5.1.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਹਰ ਅਪਲੋਡ ਫ਼ੀਚਰ ਲਈ ਆਗਿਆ ਪ੍ਰਾਪਤ ਫ਼ਾਈਲ ਕਿਸਮਾਂ, ਅਨੁਮਾਨਿਤ ਫ਼ਾਈਲ ਐਕਸਟੈਂਸ਼ਨਾਂ, ਅਤੇ ਵੱਧ ਤੋਂ ਵੱਧ ਆਕਾਰ (ਅਨਪੈਕ ਕੀਤੇ ਆਕਾਰ ਸਮੇਤ) ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ. ਇਸ ਤੋਂ ਇਲਾਵਾ, ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਇਹ ਦੱਸਦਾ ਹੈ ਕਿ ਅੰਤਮ-ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਡਾਊਨਲੋਡ ਅਤੇ ਪ੍ਰਕਿਰਿਆ ਕਰਨ ਲਈ ਫ਼ਾਈਲਾਂ ਨੂੰ ਕਿਵੇਂ ਸੁਰੱਖਿਅਤ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਜਦੋਂ ਕੋਈ ਖ਼ਤਰਨਾਕ ਫ਼ਾਈਲ ਪਛਾਣੀ ਜਾਂਦੀ ਹੈ ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ ਕਿਵੇਂ ਵਿਵਹਾਰ ਕਰਦੀ ਹੈ. | ੨ |

## V5.2 File Upload and Content
## V5.2 ਫ਼ਾਈਲ ਅਪਲੋਡ ਅਤੇ ਸਮੱਗਰੀ

File upload functionality is a primary source of untrusted files. This section outlines the requirements for ensuring that the presence, volume, or content of these files cannot harm the application.

ਫ਼ਾਈਲ ਅਪਲੋਡ ਕਾਰਜਸ਼ੀਲਤਾ ਅਣਭਰੋਸੇਯੋਗ ਫ਼ਾਈਲਾਂ ਦਾ ਮੁੱਖ ਸਰੋਤ ਹੈ. ਇਹ ਭਾਗ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਲੋੜਾਂ ਦੀ ਰੂਪਰੇਖਾ ਦਿੰਦਾ ਹੈ ਕਿ ਇਹਨਾਂ ਫ਼ਾਈਲਾਂ ਦੀ ਮੌਜੂਦਗੀ, ਮਾਤਰਾ, ਜਾਂ ਸਮੱਗਰੀ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਨੁਕਸਾਨ ਨਾ ਪਹੁੰਚਾ ਸਕੇ.

| # | Description | Level |
| :---: | :--- | :---: |
| **5.2.1** | Verify that the application will only accept files of a size which it can process without causing a loss of performance or a denial of service attack. | 1 |
| **5.2.2** | Verify that when the application accepts a file, either on its own or within an archive such as a zip file, it checks if the file extension matches an expected file extension and validates that the contents correspond to the type represented by the extension. This includes, but is not limited to, checking the initial 'magic bytes', performing image re-writing, and using specialized libraries for file content validation. For L1, this can focus just on files which are used to make specific business or security decisions. For L2 and up, this must apply to all files being accepted. | 1 |
| **5.2.3** | Verify that the application checks compressed files (e.g., zip, gz, docx, odt) against maximum allowed uncompressed size and against maximum number of files before uncompressing the file. | 2 |
| **5.2.4** | Verify that a file size quota and maximum number of files per user are enforced to ensure that a single user cannot fill up the storage with too many files, or excessively large files. | 3 |
| **5.2.5** | Verify that the application does not allow uploading compressed files containing symlinks unless this is specifically required (in which case it will be necessary to enforce an allowlist of the files that can be symlinked to). | 3 |
| **5.2.6** | Verify that the application rejects uploaded images with a pixel size larger than the maximum allowed, to prevent pixel flood attacks. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **5.2.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸਿਰਫ਼ ਉਸ ਆਕਾਰ ਦੀਆਂ ਫ਼ਾਈਲਾਂ ਨੂੰ ਸਵੀਕਾਰ ਕਰੇਗੀ ਜਿਸਨੂੰ ਉਹ ਪ੍ਰਦਰਸ਼ਨ ਦੇ ਨੁਕਸਾਨ ਜਾਂ ਸੇਵਾ-ਇਨਕਾਰ (denial of service) ਹਮਲੇ ਦਾ ਕਾਰਨ ਬਣੇ ਬਿਨਾਂ ਪ੍ਰਕਿਰਿਆ ਕਰ ਸਕਦੀ ਹੈ. | ੧ |
| **5.2.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਦੋਂ ਐਪਲੀਕੇਸ਼ਨ ਇੱਕ ਫ਼ਾਈਲ ਨੂੰ ਸਵੀਕਾਰ ਕਰਦੀ ਹੈ, ਭਾਵੇਂ ਆਪਣੇ ਆਪ ਜਾਂ ਕਿਸੇ ਆਰਕਾਈਵ ਜਿਵੇਂ ਕਿ ਜ਼ਿਪ ਫ਼ਾਈਲ ਦੇ ਅੰਦਰ, ਇਹ ਜਾਂਚ ਕਰਦੀ ਹੈ ਕਿ ਫ਼ਾਈਲ ਐਕਸਟੈਂਸ਼ਨ ਇੱਕ ਅਨੁਮਾਨਿਤ ਫ਼ਾਈਲ ਐਕਸਟੈਂਸ਼ਨ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ ਅਤੇ ਪ੍ਰਮਾਣਿਤ ਕਰਦੀ ਹੈ ਕਿ ਸਮੱਗਰੀ ਐਕਸਟੈਂਸ਼ਨ ਦੁਆਰਾ ਦਰਸਾਈ ਕਿਸਮ ਨਾਲ ਮੇਲ ਖਾਂਦੀ ਹੈ. ਇਸ ਵਿੱਚ ਸ਼ੁਰੂਆਤੀ 'ਮੈਜਿਕ ਬਾਈਟਸ' ਦੀ ਜਾਂਚ ਕਰਨਾ, ਚਿੱਤਰ ਮੁੜ-ਲਿਖਾਈ ਕਰਨਾ, ਅਤੇ ਫ਼ਾਈਲ ਸਮੱਗਰੀ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ ਵਿਸ਼ੇਸ਼ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਸ਼ਾਮਲ ਹੈ, ਪਰ ਇਹਨਾਂ ਤੱਕ ਸੀਮਿਤ ਨਹੀਂ. L1 ਲਈ, ਇਹ ਸਿਰਫ਼ ਉਹਨਾਂ ਫ਼ਾਈਲਾਂ 'ਤੇ ਕੇਂਦ੍ਰਿਤ ਹੋ ਸਕਦਾ ਹੈ ਜੋ ਖ਼ਾਸ ਕਾਰੋਬਾਰੀ ਜਾਂ ਸੁਰੱਖਿਆ ਫ਼ੈਸਲੇ ਲੈਣ ਲਈ ਵਰਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ. L2 ਅਤੇ ਉੱਪਰ ਲਈ, ਇਹ ਸਾਰੀਆਂ ਸਵੀਕਾਰ ਕੀਤੀਆਂ ਜਾ ਰਹੀਆਂ ਫ਼ਾਈਲਾਂ 'ਤੇ ਲਾਗੂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ. | ੧ |
| **5.2.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸੰਕੁਚਿਤ ਫ਼ਾਈਲਾਂ (ਜਿਵੇਂ, zip, gz, docx, odt) ਦੀ ਫ਼ਾਈਲ ਨੂੰ ਡੀ-ਸੰਕੁਚਿਤ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਵੱਧ ਤੋਂ ਵੱਧ ਆਗਿਆ ਪ੍ਰਾਪਤ ਡੀ-ਸੰਕੁਚਿਤ ਆਕਾਰ ਅਤੇ ਫ਼ਾਈਲਾਂ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਗਿਣਤੀ ਦੇ ਵਿਰੁੱਧ ਜਾਂਚ ਕਰਦੀ ਹੈ. | ੨ |
| **5.2.4** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਪ੍ਰਤੀ ਉਪਭੋਗਤਾ ਇੱਕ ਫ਼ਾਈਲ ਆਕਾਰ ਕੋਟਾ ਅਤੇ ਫ਼ਾਈਲਾਂ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਗਿਣਤੀ ਲਾਗੂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਤਾਂ ਜੋ ਇੱਕ ਇਕੱਲਾ ਉਪਭੋਗਤਾ ਬਹੁਤ ਜ਼ਿਆਦਾ ਫ਼ਾਈਲਾਂ, ਜਾਂ ਬਹੁਤ ਵੱਡੀਆਂ ਫ਼ਾਈਲਾਂ ਨਾਲ ਭੰਡਾਰਨ ਨੂੰ ਨਾ ਭਰ ਸਕੇ. | ੩ |
| **5.2.5** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਸਿਮਲਿੰਕ (symlinks) ਵਾਲੀਆਂ ਸੰਕੁਚਿਤ ਫ਼ਾਈਲਾਂ ਨੂੰ ਅਪਲੋਡ ਕਰਨ ਦੀ ਆਗਿਆ ਨਹੀਂ ਦਿੰਦੀ ਜਦੋਂ ਤੱਕ ਇਹ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ਜ਼ਰੂਰੀ ਨਾ ਹੋਵੇ (ਉਸ ਸੂਰਤ ਵਿੱਚ ਉਹਨਾਂ ਫ਼ਾਈਲਾਂ ਦੀ ਇੱਕ allowlist ਲਾਗੂ ਕਰਨੀ ਜ਼ਰੂਰੀ ਹੋਵੇਗੀ ਜਿਨ੍ਹਾਂ ਨਾਲ ਸਿਮਲਿੰਕ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ). | ੩ |
| **5.2.6** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਪਿਕਸਲ ਫ਼ਲੱਡ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਆਗਿਆ ਪ੍ਰਾਪਤ ਵੱਧ ਤੋਂ ਵੱਧ ਨਾਲੋਂ ਵੱਡੇ ਪਿਕਸਲ ਆਕਾਰ ਵਾਲੇ ਅਪਲੋਡ ਕੀਤੇ ਚਿੱਤਰਾਂ ਨੂੰ ਰੱਦ ਕਰਦੀ ਹੈ. | ੩ |

## V5.3 File Storage
## V5.3 ਫ਼ਾਈਲ ਭੰਡਾਰਨ

This section includes requirements to prevent files from being inappropriately executed after upload, to detect dangerous content, and to avoid untrusted data being used to control where files are being stored.

ਇਸ ਭਾਗ ਵਿੱਚ ਫ਼ਾਈਲਾਂ ਨੂੰ ਅਪਲੋਡ ਤੋਂ ਬਾਅਦ ਅਣਉਚਿਤ ਢੰਗ ਨਾਲ ਚਲਾਏ ਜਾਣ ਤੋਂ ਰੋਕਣ, ਖ਼ਤਰਨਾਕ ਸਮੱਗਰੀ ਦਾ ਪਤਾ ਲਗਾਉਣ, ਅਤੇ ਇਹ ਨਿਯੰਤਰਣ ਕਰਨ ਲਈ ਅਣਭਰੋਸੇਯੋਗ ਡਾਟਾ ਦੀ ਵਰਤੋਂ ਤੋਂ ਬਚਣ ਲਈ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ ਕਿ ਫ਼ਾਈਲਾਂ ਕਿੱਥੇ ਸੰਭਾਲੀਆਂ ਜਾ ਰਹੀਆਂ ਹਨ.

| # | Description | Level |
| :---: | :--- | :---: |
| **5.3.1** | Verify that files uploaded or generated by untrusted input and stored in a public folder, are not executed as server-side program code when accessed directly with an HTTP request. | 1 |
| **5.3.2** | Verify that when the application creates file paths for file operations, instead of user-submitted filenames, it uses internally generated or trusted data, or if user-submitted filenames or file metadata must be used, strict validation and sanitization must be applied. This is to protect against path traversal, local or remote file inclusion (LFI, RFI), and server-side request forgery (SSRF) attacks. | 1 |
| **5.3.3** | Verify that server-side file processing, such as file decompression, ignores user-provided path information to prevent vulnerabilities such as zip slip. | 3 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **5.3.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਅਣਭਰੋਸੇਯੋਗ ਇਨਪੁੱਟ ਦੁਆਰਾ ਅਪਲੋਡ ਕੀਤੀਆਂ ਜਾਂ ਪੈਦਾ ਕੀਤੀਆਂ ਅਤੇ ਜਨਤਕ ਫੋਲਡਰ ਵਿੱਚ ਸੰਭਾਲੀਆਂ ਫ਼ਾਈਲਾਂ, HTTP ਬੇਨਤੀ ਨਾਲ ਸਿੱਧੇ ਪਹੁੰਚਣ 'ਤੇ ਸਰਵਰ-ਪਾਸੇ ਪ੍ਰੋਗਰਾਮ ਕੋਡ ਵਜੋਂ ਨਹੀਂ ਚਲਾਈਆਂ ਜਾਂਦੀਆਂ. | ੧ |
| **5.3.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਜਦੋਂ ਐਪਲੀਕੇਸ਼ਨ ਫ਼ਾਈਲ ਕਾਰਵਾਈਆਂ ਲਈ ਫ਼ਾਈਲ ਪਾਥ ਬਣਾਉਂਦੀ ਹੈ, ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਸੌਂਪੇ ਫ਼ਾਈਲ ਨਾਮਾਂ ਦੀ ਬਜਾਏ, ਇਹ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ ਪੈਦਾ ਕੀਤੇ ਜਾਂ ਭਰੋਸੇਯੋਗ ਡਾਟਾ ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ, ਜਾਂ ਜੇ ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਸੌਂਪੇ ਫ਼ਾਈਲ ਨਾਮ ਜਾਂ ਫ਼ਾਈਲ ਮੈਟਾਡਾਟਾ ਦੀ ਵਰਤੋਂ ਕਰਨੀ ਜ਼ਰੂਰੀ ਹੈ, ਤਾਂ ਸਖ਼ਤ ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ ਲਾਗੂ ਕੀਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ. ਇਹ ਪਾਥ ਟਰੈਵਰਸਲ, ਲੋਕਲ ਜਾਂ ਰਿਮੋਟ ਫ਼ਾਈਲ ਇਨਕਲੂਜ਼ਨ (LFI, RFI), ਅਤੇ ਸਰਵਰ-ਸਾਈਡ ਰਿਕੁਐਸਟ ਫੋਰਜਰੀ (SSRF) ਹਮਲਿਆਂ ਤੋਂ ਬਚਾਅ ਲਈ ਹੈ. | ੧ |
| **5.3.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸਰਵਰ-ਪਾਸੇ ਫ਼ਾਈਲ ਪ੍ਰਕਿਰਿਆ, ਜਿਵੇਂ ਕਿ ਫ਼ਾਈਲ ਡੀ-ਸੰਕੁਚਨ, ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤੀ ਪਾਥ ਜਾਣਕਾਰੀ ਨੂੰ ਅਣਡਿੱਠ ਕਰਦੀ ਹੈ ਤਾਂ ਜੋ zip slip ਵਰਗੀਆਂ ਕਮਜ਼ੋਰੀਆਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ. | ੩ |

## V5.4 File Download
## V5.4 ਫ਼ਾਈਲ ਡਾਊਨਲੋਡ

This section contains requirements to mitigate risks when serving files to be downloaded, including path traversal and injection attacks. This also includes making sure they don't contain dangerous content.

ਇਸ ਭਾਗ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕੀਤੀਆਂ ਜਾਣ ਵਾਲੀਆਂ ਫ਼ਾਈਲਾਂ ਦੀ ਸੇਵਾ ਕਰਦੇ ਸਮੇਂ ਖ਼ਤਰਿਆਂ ਨੂੰ ਘਟਾਉਣ ਲਈ ਲੋੜਾਂ ਸ਼ਾਮਲ ਹਨ, ਜਿਸ ਵਿੱਚ ਪਾਥ ਟਰੈਵਰਸਲ ਅਤੇ ਇੰਜੈਕਸ਼ਨ ਹਮਲੇ ਸ਼ਾਮਲ ਹਨ. ਇਸ ਵਿੱਚ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਵੀ ਸ਼ਾਮਲ ਹੈ ਕਿ ਉਹਨਾਂ ਵਿੱਚ ਖ਼ਤਰਨਾਕ ਸਮੱਗਰੀ ਨਾ ਹੋਵੇ.

| # | Description | Level |
| :---: | :--- | :---: |
| **5.4.1** | Verify that the application validates or ignores user-submitted filenames, including in a JSON, JSONP, or URL parameter and specifies a filename in the Content-Disposition header field in the response. | 2 |
| **5.4.2** | Verify that file names served (e.g., in HTTP response header fields or email attachments) are encoded or sanitized (e.g., following RFC 6266) to preserve document structure and prevent injection attacks. | 2 |
| **5.4.3** | Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent serving of known malicious content. | 2 |

| # | ਵੇਰਵਾ | ਪੱਧਰ |
| :---: | :--- | :---: |
| **5.4.1** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨ ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਸੌਂਪੇ ਫ਼ਾਈਲ ਨਾਮਾਂ ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਦੀ ਹੈ ਜਾਂ ਅਣਡਿੱਠ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ JSON, JSONP, ਜਾਂ URL ਪੈਰਾਮੀਟਰ ਸ਼ਾਮਲ ਹਨ, ਅਤੇ ਜਵਾਬ ਵਿੱਚ Content-Disposition ਹੈਡਰ ਖੇਤਰ ਵਿੱਚ ਇੱਕ ਫ਼ਾਈਲ ਨਾਮ ਨਿਰਧਾਰਤ ਕਰਦੀ ਹੈ. | ੨ |
| **5.4.2** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਸੇਵਾ ਕੀਤੇ ਫ਼ਾਈਲ ਨਾਮ (ਜਿਵੇਂ, HTTP ਜਵਾਬ ਹੈਡਰ ਖੇਤਰਾਂ ਜਾਂ ਈਮੇਲ ਅਟੈਚਮੈਂਟਾਂ ਵਿੱਚ) ਦਸਤਾਵੇਜ਼ ਢਾਂਚੇ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਣ ਅਤੇ ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਏਨਕੋਡ ਜਾਂ ਸੈਨੀਟਾਈਜ਼ ਕੀਤੇ ਜਾਂਦੇ ਹਨ (ਜਿਵੇਂ, RFC 6266 ਦੇ ਅਨੁਸਾਰ). | ੨ |
| **5.4.3** | ਤਸਦੀਕ ਕਰੋ ਕਿ ਅਣਭਰੋਸੇਯੋਗ ਸਰੋਤਾਂ ਤੋਂ ਪ੍ਰਾਪਤ ਫ਼ਾਈਲਾਂ ਨੂੰ ਜਾਣੀ-ਪਛਾਣੀ ਖ਼ਤਰਨਾਕ ਸਮੱਗਰੀ ਦੀ ਸੇਵਾ ਨੂੰ ਰੋਕਣ ਲਈ ਐਂਟੀਵਾਇਰਸ ਸਕੈਨਰਾਂ ਦੁਆਰਾ ਸਕੈਨ ਕੀਤਾ ਜਾਂਦਾ ਹੈ. | ੨ |

## References
## ਹਵਾਲੇ

For more information, see also:

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਵੀ ਵੇਖੋ:

* [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
* [Example of using symlinks for arbitrary file read](https://hackerone.com/reports/1439593)
* [Explanation of "Magic Bytes" from Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures)
