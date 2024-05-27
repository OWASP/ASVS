# V12 File e risorse

## Obiettivo del controllo

Verificare che un'applicazione soddisfi i seguenti requisiti di alto livello:

* I file non considerati attendibili devono essere gestiti in modo appropriato e sicuro.
* I file non considerati attendibili ottenuti da fonti non affidabili devono essere archiviati al di fuori della root web e con permessi limitati.

## V12.1 Caricamento di file

Sebbene gli attacchi "Zip Bomb" siano facilmente testabili utilizzando tecniche di penetration testing, vengono considerati di livello L2 e superiore per incoraggiare la progettazione e lo sviluppo con un'attenta revisione manuale, evitando test di penetration testing automatizzati o manuali non qualificati per individuare condizioni di denial-of-service.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.1.1** | Verificare che l'applicazione non accetti file di grandi dimensioni che potrebbero saturare lo storage o causare un denial-of-service. | ✓ | ✓ | ✓ | 400 |
| **12.1.2** | Verificare che l'applicazione controlli i file compressi (es. zip, gz, docx, odt) confrontandoli con la dimensione massima consentita allo stato non compresso e con il numero massimo di file prima di procedere alla decompressione. | | ✓ | ✓ | 409 |
| **12.1.3** | Verificare che venga applicata una quota per la dimensione dei file e un numero massimo di file per utente, per garantire che un singolo utente non possa saturare lo storage con troppi file o file eccessivamente grandi. | | ✓ | ✓ | 770 |

## V12.2 File Integrity

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.2.1** | Verify that files obtained from untrusted sources are validated to be of expected type based on the file's content. | | ✓ | ✓ | 434 |

## V12.3 File Execution

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.3.1** | Verify that user-submitted filename metadata is not used directly by system or framework filesystems and that a URL API is used to protect against path traversal. | ✓ | ✓ | ✓ | 22 |
| **12.3.2** | Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure, creation, updating or removal of local files (LFI). | ✓ | ✓ | ✓ | 73 |
| **12.3.3** | Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure or execution of remote files via Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks. | ✓ | ✓ | ✓ | 98 |
| **12.3.4** | Verify that the application protects against Reflective File Download (RFD) by validating or ignoring user-submitted filenames in a JSON, JSONP, or URL parameter, the response Content-Type header should be set to text/plain, and the Content-Disposition header should have a fixed filename. | ✓ | ✓ | ✓ | 641 |
| **12.3.5** | Verify that untrusted file metadata is not used directly with system API or libraries, to protect against OS command injection. | ✓ | ✓ | ✓ | 78 |
| **12.3.6** | Verify that the application does not include and execute functionality from untrusted sources, such as unverified content distribution networks, JavaScript libraries, node npm libraries, or server-side DLLs. | | ✓ | ✓ | 829 |

## V12.4 Archiviazione File

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.4.1** | Verificare che i file ottenuti da fonti non affidabili siano archiviati al di fuori della root web, con permessi limitati. | ✓ | ✓ | ✓ | 552 |
| **12.4.2** | Verificare che i file ottenuti da fonti non affidabili vengano scansionati da antivirus per prevenire il caricamento e la distribuzione di contenuti dannosi noti. | ✓ | ✓ | ✓ | 509 |

## V12.5 Download file

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.5.1** | Verificare che il livello web sia configurato per servire solo file con estensioni specifiche per prevenire divulgazione involontaria di informazioni e codice sorgente. Ad esempio, è necessario bloccare il download di file di backup (es. .bak), file di lavoro temporanei (es. .swp), file compressi (.zip, .tar.gz, ecc.) e altre estensioni comunemente utilizzate dagli editor, a meno che non siano espressamente richiesti. | ✓ | ✓ | ✓ | 552 |
| **12.5.2** | Verificare che le richieste dirette a file caricati non vengano mai eseguite come contenuto HTML/JavaScript. | ✓ | ✓ | ✓ | 434 |

## V12.6 Protezione da SSRF

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.6.1** | Verificare che il server web o applicativo sia configurato con una allow-list di risorse o sistemi verso i quali il server può inviare richieste o caricare dati/file. | ✓ | ✓ | ✓ | 918 |

## Riferimenti

Per approfondimenti, consultare:

* [File Extension Handling for Sensitive Information](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
* [Reflective file download by Oren Hafif](https://www.trustwave.com/Resources/SpiderLabs-Blog/Reflected-File-Download---A-New-Web-Attack-Vector/)
* [OWASP Third Party JavaScript Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html)
