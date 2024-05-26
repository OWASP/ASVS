# V14 Configurazioni

## Obiettivo del controllo

Assicurarsi che un'applicazione verificata disponga di::

* Un ambiente di build sicuro, ripetibile e automatizzabile.
* Gestione rigorosa di librerie, dipendenze e configurazione di terze parti in modo che l'applicazione non includa componenti obsoleti o non sicuri.

La configurazione predefinita dell'applicazione deve essere sicura per l'utilizzo su Internet.

## V14.1 Build e distribuzione

Le pipeline di build sono fondamentali per garantire una sicurezza ripetibile: ogni volta che viene rilevata una vulnerabilità, è possibile correggerla nel codice sorgente, negli script di build o di distribuzione, e testare automaticamente la correzione. Si raccomanda vivamente di utilizzare pipeline di build con controlli automatici di sicurezza e gestione delle dipendenze, che avvisino o interrompano la build per prevenire la distribuzione in produzione di problemi di sicurezza noti. L'esecuzione irregolare di passaggi manuali può portare direttamente a errori di sicurezza evitabili.

Con l'avvento del modello DevSecOps, diventa essenziale garantire la continua disponibilità e integrità della distribuzione e della configurazione per mantenere uno stato noto e funzionante. In passato, se un sistema veniva compromesso, potevano volerci giorni o mesi per dimostrare che non si erano verificate ulteriori intrusioni. Oggi, grazie all'infrastruttura software-defined, alle distribuzioni A/B rapide a zero downtime e alle build automatizzate in container, è possibile creare, rafforzare e distribuire automaticamente e continuamente una versione "nota e funzionante" di qualsiasi sistema compromesso.

Se si utilizzano ancora modelli tradizionali, è necessario adottare procedure manuali per rafforzare ed eseguire il backup di tali configurazioni, in modo da consentire la rapida sostituzione dei sistemi compromessi con sistemi integri e non compromessi in modo tempestivo.

La conformità a questa sezione richiede un sistema di build automatizzato e l'accesso agli script di build e distribuzione.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.1.1** | Verificare che i processi di build e distribuzione dell'applicazione vengano eseguiti in modo sicuro e ripetibile, come automazione CI/CD, gestione automatizzata della configurazione e script di distribuzione automatizzati.	 | | ✓ | ✓ | |
| **14.1.2** | Verificare che le flag del compilatore siano configurate per abilitare tutte le protezioni disponibili e gli avvisi per buffer overflow, inclusa la randomizzazione dello stack, la data execution prevention e l'interruzione della build se vengono trovate operazioni non sicure su puntatori, memoria, format string, numeri interi o stringhe.	 | | ✓ | ✓ | 120 |
| **14.1.3** | Verificare che la configurazione del server sia rafforzata secondo le raccomandazioni del server applicativo e dei framework utilizzati.	 | | ✓ | ✓ | 16 |
| **14.1.4** | Verificare che l'applicazione, la configurazione e tutte le dipendenze possano essere ridistribuite in un lasso di tempo ragionevole utilizzando script di distribuzione automatizzati, creati da un runbook documentato e testato, o ripristinate da backup in modo tempestivo.	 | | ✓ | ✓ | |
| **14.1.5** | che gli amministratori autorizzati possano verificare l'integrità di tutte le configurazioni relative alla sicurezza, al fine di rilevare eventuali manomissioni. | | | ✓ | |

## V14.2 Dipendenze

La gestione delle dipendenze è fondamentale per il funzionamento sicuro di qualsiasi applicazione di qualsiasi tipo. La mancata manutenzione di dipendenze obsolete o non sicure fino ad oggi è la causa principale degli attacchi maggiori e costosi.

Nota: Al Livello 1, la conformità a 14.2.1 riguarda le osservazioni o i rilevamenti di librerie e componenti lato client e di altro tipo, piuttosto che una più accurata analisi statica del codice in fase di build o analisi delle dipendenze. L'utilizzo di queste tecniche più affidabili potrebbe essere documentato attraverso colloquio, all'occorrenza.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.2.1** | Verificare che tutti i componenti siano aggiornati, preferibilmente utilizzando un dependency checker durante la fase di build o compilazione. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1026 |
| **14.2.2** | Verificare che tutte le funzionalità, documentazione, applicazioni di esempio e configurazioni non necessarie vengano rimosse.	 | ✓ | ✓ | ✓ | 1002 |
| **14.2.3** | Verificare che se le risorse dell'applicazione, come librerie JavaScript, CSS o web font, sono ospitate esternamente su una Content Delivery Network (CDN) o un provider esterno, venga utilizzata la Subresource Integrity (SRI) per assicurare l'integrità della risorsa. | ✓ | ✓ | ✓ | 829 |
| **14.2.4** | Verificare che i componenti di terze parti provengano da repository predefiniti, affidabili e mantenuti frequentemente. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 829 |
| **14.2.5** | Verificare che venga mantenuto un Software Bill of Materials (SBOM) di tutte le librerie di terze parti utilizzate. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **14.2.6** | Verificare che la superficie di attacco sia ridotta tramite sandbox o incapsulamento delle librerie di terze parti per esporre all'applicazione solo le funzionalità richieste. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |

## V14.3 Divulgazione accidentale di informazioni di sicurezza

Le configurazioni di produzione devono essere rafforzate per proteggersi da attacchi comuni, come modalità di debug attiva, gli attacchi Cross-Site Scripting (XSS) e Remote File Inclusion (RFI), ed eliminare le "vulnerabilità" di information discovery, spesso segnalate nei report di penetration testing. Sebbene molti di questi problemi raramente vengano classificati come rischi significativi, possono essere sfruttati in combinazione con altre vulnerabilità. Garantendo che questi problemi siano assenti di default, si rende più difficile il successo della maggior parte degli attacchi.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.3.1** | [ELIMINATO, DUPLICATO DI 7.4.1] | | | | |
| **14.3.2** | Verificare che le modalità di debug del server web o dell'applicazione e del framework dell'applicazione siano disabilitate in produzione per eliminare funzionalità di debug, console degli sviluppatori e divulgazioni di sicurezza accidentali.	 | ✓ | ✓ | ✓ | 497 |
| **14.3.3** | Verificare che gli header HTTP o qualsiasi parte della risposta HTTP non espongano informazioni dettagliate sulla versione dei componenti di sistema.	 | ✓ | ✓ | ✓ | 200 |

## V14.4 Header di sicurezza HTTP

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.4.1** | Verificare che ogni risposta HTTP contenga un header Content-Type. Specificare inoltre un set di caratteri sicuro (ad esempio, UTF-8, ISO-8859-1) se i tipi di contenuto sono text/*, /+xml e application/xml. Il contenuto deve corrispondere all'header Content-Type fornito. | ✓ | ✓ | ✓ | 173 |
| **14.4.2** | Verificare che tutte le risposte dell'API contengano un header Content-Disposition: attachment; filename="api.json" (o altro nome file appropriato per il tipo di contenuto). | ✓ | ✓ | ✓ | 116 |
| **14.4.3** | Verificare che sia presente un header di risposta Content Security Policy (CSP) che contribuisca a mitigare l'impatto degli attacchi XSS come vulnerabilità di HTML, DOM, JSON e JavaScript injection. | ✓ | ✓ | ✓ | 1021 |
| **14.4.4** | Verificare che tutte le risposte contengano un header X-Content-Type-Options: nosniff.	 | ✓ | ✓ | ✓ | 116 |
| **14.4.5** | Verificare che un header Strict-Transport-Security sia incluso su tutte le risposte e per tutti i sottodomini, come Strict-Transport-Security: max-age=15724800; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **14.4.6** | Verificare che sia incluso un header Referrer-Policy adatto per evitare di esporre informazioni sensibili nell'URL tramite l'header Referer a terze parti non fidate. | ✓ | ✓ | ✓ | 116 |
| **14.4.7** | Verificare che il contenuto di un'applicazione web non possa essere incorporato per impostazione predefinita in un sito di terze parti e che l'incorporamento delle risorse sia consentito solo se necessario utilizzando header di risposta Content-Security-Policy: frame-ancestors e X-Frame-Options appropriati.	 | ✓ | ✓ | ✓ | 1021 |

## V14.5 Validazione dell'header di richiesta HTTP

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.5.1** | Verificare che il server dell'applicazione accetti solo i metodi HTTP utilizzati dall'applicazione/API, incluse le opzioni di pre-flight (OPTIONS), e registri o generi alert per qualsiasi richiesta non valida per il contesto dell'applicazione.	 | ✓ | ✓ | ✓ | 749 |
| **14.5.2** | Verificare che l'header Origin fornito non venga utilizzato per l'autenticazione o il controllo degli accessi, in quanto può essere facilmente modificato da un attaccante.	| ✓ | ✓ | ✓ | 346 |
| **14.5.3** | Verificare che l'header CORS (Cross-Origin Resource Sharing) Access-Control-Allow-Origin utilizzi una allow-list di domini e sottodomini trusted per il confronto e non supporti l'origine "null". | ✓ | ✓ | ✓ | 346 |
| **14.5.4** | Verificare che gli header HTTP aggiunti da un proxy trusted o da dispositivi SSO, come un token bearer, siano autenticati dall'applicazione.	 | | ✓ | ✓ | 306 |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Web Security Testing Guide 4.1: Testing for HTTP Verb Tampering]( https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* Adding Content-Disposition to API responses helps prevent many attacks based on misunderstanding on the MIME type between client and server, and the "filename" option specifically helps prevent [Reflected File Download attacks.](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Sandboxing third party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
