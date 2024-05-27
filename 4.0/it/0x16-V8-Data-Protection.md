# V8 Protezione dei dati

## Obiettivo del controllo

Esistono tre elementi chiave per una sana protezione dei dati: riservatezza, integrità e disponibilità (CIA). Questo standard presuppone che la protezione dei dati venga applicata su un sistema affidabile, come un server, opportunamente protetto e dotato di adeguate misure di sicurezza.

Le applicazioni devono presumere che tutti i dispositivi degli utenti siano in qualche modo compromessi. Quando un'applicazione trasmette o archivia informazioni sensibili su dispositivi non sicuri, come computer condivisi, telefoni e tablet, è responsabilità dell'applicazione garantire che i dati archiviati su tali dispositivi siano crittografati e non possano essere facilmente ottenuti, alterati o divulgati in modo illecito.

Verificare che un'applicazione soddisfi i seguenti requisiti di alto livello:

* Riservatezza: I dati devono essere protetti da lettura o divulgazione non autorizzate sia durante il trasferimento che durante l'archiviazione.
* Integrità: I dati devono essere protetti dalla creazione, alterazione o eliminazione malevola da parte di attori malevoli.
* Disponibilità: I dati devono essere disponibili all'occorrenza per gli utenti autorizzati.

## V8.1 Protezione Generale dei Dati

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.1.1** | Verificare che l'applicazione impedisca la memorizzazione nella cache di dati sensibili in componenti del server come bilanciatori di carico e cache applicative. | | ✓ | ✓ | 524 |
| **8.1.2** | Verificare che tutte le copie temporanee o memorizzate nella cache dei dati sensibili archiviate sul server siano protette dall'accesso non autorizzato o eliminate/invalidate dopo che l'utente autorizzato accede ai dati sensibili. | | ✓ | ✓ | 524 |
| **8.1.3** | Verificare che l'applicazione riduca al minimo il numero di parametri in una richiesta, come campi nascosti, variabili Ajax, cookie e header. | | ✓ | ✓ | 233 |
| **8.1.4** | Verificare che l'applicazione possa rilevare e allertare su un numero anomalo di richieste, ad esempio per IP, utente, totale per ora o giorno, o qualsiasi elemento che abbia senso per l'applicazione. | | ✓ | ✓ | 770 |
| **8.1.5** | Verificare che vengano eseguiti backup regolari dei dati importanti e che venga eseguito un ripristino di prova dei dati. | | | ✓ | 19 |
| **8.1.6** | Verificare che i backup siano archiviati in modo sicuro per impedire il furto o la corruzione dei dati. | | | ✓ | 19 |

## V8.2 Protezione dei Dati lato Client

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.2.1** | Verificare che l'applicazione imposti header anti-caching sufficienti in modo che i dati sensibili non vengano memorizzati nella cache dei browser moderni. | ✓ | ✓ | ✓ | 525 |
| **8.2.2** | Verificare che i dati memorizzati nell'archiviazione del browser (come localStorage, sessionStorage, IndexedDB o cookie) non contengano dati sensibili. | ✓ | ✓ | ✓ | 922 |
| **8.2.3** | Verificare che i dati autenticati vengano cancellati dall'archiviazione client, come il DOM del browser, dopo la chiusura del client o della sessione. | ✓ | ✓ | ✓ | 922 |

## V8.3 Protezione dei Dati Sensibili e Privati

Questa sezione aiuta a proteggere i dati sensibili dall'essere creati, letti, aggiornati o eliminati senza autorizzazione, in particolare in grandi quantità.

La conformità a questa sezione implica la conformità al controllo degli accessi V4, e in particolare a V4.2. Ad esempio, per proteggere da aggiornamenti o divulgazioni non autorizzate di informazioni personali sensibili, è necessario rispettare V4.2.1. Per una copertura completa, attenersi a questa sezione e a V4.

Nota: i regolamenti e le leggi sulla privacy, come i principi australiani sulla privacy APP-11 o il GDPR, influenzano direttamente il modo in cui le applicazioni devono affrontare l'implementazione dello storage, utilizzo e trasmissione di informazioni personali sensibili. Questo va da severe sanzioni a semplici consigli. Si prega di consultare le leggi e i regolamenti locali e, se necessario, consultare uno specialista della privacy o un avvocato qualificato.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.3.1** | Verificare che i dati sensibili vengano inviati al server nel corpo del messaggio HTTP o negli header, e che i parametri della stringa di query di qualsiasi metodo HTTP non contengano dati sensibili. | ✓ | ✓ | ✓ | 319 |
| **8.3.2** | Verificare che gli utenti abbiano un metodo per rimuovere o esportare i propri dati su richiesta. | ✓ | ✓ | ✓ | 212 |
| **8.3.3** | Verificare che agli utenti venga fornita una spiegazione chiara in merito alla raccolta e all'utilizzo delle informazioni personali fornite e che gli utenti abbiano fornito il consenso esplicito all'utilizzo di tali dati prima che vengano utilizzati in qualsiasi modo. | ✓ | ✓ | ✓ | 285 |
| **8.3.4** | Verificare che tutti i dati sensibili creati ed elaborati dall'applicazione siano stati identificati e che sia presente una politica su come trattare i dati sensibili. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 200 |
| **8.3.5** | Verificare che l'accesso ai dati sensibili venga registrato (senza registrare i dati sensibili stessi), se i dati vengono raccolti ai sensi delle direttive pertinenti sulla protezione dei dati o laddove sia richiesta la registrazione degli accessi. | | ✓ | ✓ | 532 |
| **8.3.6** | Verificare che le informazioni sensibili contenute nella memoria vengano sovrascritte non appena non sono più necessarie per mitigare gli attacchi di dump della memoria, utilizzando zeri o dati casuali. | | ✓ | ✓ | 226 |
| **8.3.7** | Verificare che le informazioni sensibili o private che necessitano confidenzialità vengano crittografate utilizzando algoritmi approvati che forniscono sia riservatezza che integrità. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 327 |
| **8.3.8** | Verificare che le informazioni personali sensibili siano soggette a classificazione della conservazione dei dati, in modo tale che i dati vecchi o obsoleti vengano eliminati automaticamente, secondo una pianificazione specifica o in base alla situazione. | | ✓ | ✓ | 285 |

Quando si considera la protezione dei dati, una considerazione primaria dovrebbe riguardare l'estrazione o la modifica in blocco o l'utilizzo eccessivo. Ad esempio, molti sistemi di social media consentono agli utenti di aggiungere solo 100 nuovi amici al giorno, ma non è importante da quale sistema provengano queste richieste. Una piattaforma bancaria potrebbe voler bloccare più di 5 transazioni all'ora che trasferiscono fondi per oltre 1000 euro a istituzioni esterne. I requisiti di ciascun sistema possono essere molto diversi, quindi decidere cosa sia "anormale" deve tenere conto del modello di minaccia e del rischio aziendale. Criteri importanti sono la capacità di rilevare, scoraggiare o preferibilmente bloccare tali azioni anomale in blocco.

## Riferimenti

Per approfondimenti, consultare:

* [Consider using Security Headers website to check security and anti-caching headers](https://securityheaders.io)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [European Union General Data Protection Regulation (GDPR) overview](https://edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
