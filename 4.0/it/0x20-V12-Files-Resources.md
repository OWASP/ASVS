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
| **12.1.3** | Verificare che venga applicata una quota per la dimensione dei file e un numero massimo di file per utente, per garantire che un singolo utente non possa saturare lo storage con troppi file o file eccessivamente grandi.	| | ✓ | ✓ | 770 |

Verificare che venga applicata una quota per la dimensione dei file e un numero massimo di file per utente, per garantire che un singolo utente non possa saturare lo storage con troppi file o file eccessivamente grandi.	

## V12.4 Archiviazione File

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.4.1** | Verificare che i file ottenuti da fonti non affidabili siano archiviati al di fuori della root web, con permessi limitati.	 | ✓ | ✓ | ✓ | 552 |
| **12.4.2** | Verificare che i file ottenuti da fonti non affidabili vengano scansionati da antivirus per prevenire il caricamento e la distribuzione di contenuti dannosi noti. | ✓ | ✓ | ✓ | 509 |

## V12.5 Download file

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.5.1** | Verificare che il livello web sia configurato per servire solo file con estensioni specifiche per prevenire divulgazione involontaria di informazioni e codice sorgente. Ad esempio, è necessario bloccare il download di file di backup (es. .bak), file di lavoro temporanei (es. .swp), file compressi (.zip, .tar.gz, ecc.) e altre estensioni comunemente utilizzate dagli editor, a meno che non siano espressamente richiesti.	 | ✓ | ✓ | ✓ | 552 |
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
