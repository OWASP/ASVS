# V12 File e risorse

## Obiettivo del controllo

Verificare che un'applicazione soddisfi i seguenti requisiti di alto livello:

* I file non considerati attendibili devono essere gestiti in modo appropriato e sicuro.
* I file non considerati attendibili ottenuti da fonti non affidabili devono essere archiviati al di fuori della root web e con permessi limitati.

## V12.1 Caricamento di file

Sebbene gli attacchi "Zip Bomb" siano facilmente testabili tramite tecniche di penetration testing, sono classificati come di livello L2 e superiore per incoraggiare una progettazione e uno sviluppo accurati, con una revisione manuale attenta. Questo evita il ricorso a test di penetration testing automatizzati o manuali non qualificati per individuare condizioni di denial-of-service.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.1.1** | Verificare che l'applicazione non accetti file di grandi dimensioni che potrebbero saturare lo storage o causare un denial-of-service. | ✓ | ✓ | ✓ | 400 |
| **12.1.2** | Verificare che l'applicazione controlli i file compressi (es. zip, gz, docx, odt) confrontandoli con la dimensione massima consentita allo stato non compresso e con il numero massimo di file prima di procedere alla decompressione. | | ✓ | ✓ | 409 |
| **12.1.3** | Verificare che venga applicata una quota per la dimensione dei file e un numero massimo di file per utente, per garantire che un singolo utente non possa saturare lo storage con troppi file o file eccessivamente grandi. | | ✓ | ✓ | 770 |

## V12.2 Integrità dei file

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.2.1** | Verificare che i file provenienti da fonti non affidabili siano effettivamente del tipo dichiarato, analizzandone il contenuto. | | ✓ | ✓ | 434 |

## V12.3 Esecuzione dei file

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **12.3.1** | Verificare che il nome del file inviato dall'utente non venga utilizzato direttamente dai filesystem di sistema o del framework e che venga utilizzata una API URL per proteggere da path traversal. | ✓ | ✓ | ✓ | 22 |
| **12.3.2** | Verificare o ignorare il nome del file inviato dall'utente per impedire la divulgazione, la creazione, l'aggiornamento o l'eliminazione di file locali (LFI). | ✓ | ✓ | ✓ | 73 |
| **12.3.3** | Verificare o ignorare il nome del file inviato dall'utente per impedire la divulgazione o l'esecuzione di file remoti tramite attacchi di Remote File Inclusion (RFI) o Server-Side Request Forgery (SSRF). | ✓ | ✓ | ✓ | 98 |
| **12.3.4** | Verificare che l'applicazione protegga dal Reflective File Download (RFD) convalidando o ignorando i nomi dei file inviati dall'utente in un parametro JSON, JSONP o URL. L'header Content-Type della risposta deve essere impostato su "text/plain" e l'header Content-Disposition deve avere un nome file immutabile. | ✓ | ✓ | ✓ | 641 |
| **12.3.5** | Verificare che i metadati di file non affidabili non vengano utilizzati direttamente con le API o le librerie di sistema per proteggere da OS command injection. | ✓ | ✓ | ✓ | 78 |
| **12.3.6** | Verificare che l'applicazione non includa ed esegua funzionalità da fonti non affidabili, come content delivery network non verificate, librerie JavaScript, librerie npm di Node.js o DLL lato server. | | ✓ | ✓ | 829 |

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
