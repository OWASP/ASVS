# V7 Gestione degli errori e logging

## Obiettivo del controllo

L'obiettivo principale della gestione degli errori e del logging è fornire informazioni utili all'utente, agli amministratori e ai team di risposta agli incidenti. Lo scopo non è quello di generare enormi quantità di log, ma piuttosto log di alta qualità, con un rapporto più elevato di "segnale" rispetto a "rumore" inutile.

I log di alta qualità spesso contengono dati sensibili e devono essere protetti in conformità con le leggi o direttive locali sulla privacy dei dati. Questo dovrebbe includere:

* Evitare di raccogliere o registrare informazioni sensibili a meno che non siano strettamente necessarie.
* Garantire che tutte le informazioni registrate siano gestite in modo sicuro e protette in base alla loro classificazione dei dati.
* Garantire che i log non vengano conservati indefinitamente, ma abbiano un periodo di conservazione il più breve possibile.

Se i log contengono dati privati o sensibili, la cui definizione può variare da paese a paese, essi diventano alcune delle informazioni più sensibili detenute dall'applicazione e quindi un obiettivo molto appetibile per gli attaccanti.

È inoltre fondamentale garantire che l'applicazione fallisca in modo sicuro e che gli errori non rivelino informazioni sensibili o non necessarie.

## V7.1 Contenuto del Log

La registrazione di informazioni sensibili è rischiosa: i log stessi diventano dati riservati, il che implica che devono essere crittografati, soggetti a politiche di conservazione e resi disponibili durante gli audit di sicurezza. È essenziale garantire che nei log siano conservate solo le informazioni strettamente necessarie, evitando categoricamente informazioni di pagamento, credenziali (inclusi token di sessione), informazioni sensibili o dati personali identificabili.

La sezione V7.1 copre la voce A10 dell'OWASP Top 10 del 2017. Poiché né la voce A10 del 2017 né questa sezione sono facilmente verificabili tramite penetration testing, è importante:

* Per gli sviluppatori: garantire la piena conformità a questa sezione, trattando tutte le voci come se fossero contrassegnate come L1.
* Per i penetration tester: convalidare la piena conformità di tutte le voci in V7.1 tramite interviste, screenshot o dichiarazioni.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.1.1** | Verificare che l'applicazione non registri credenziali o dettagli di pagamento. I token di sessione devono essere memorizzati nei log solo in forma di hash irreversibile. ([C9, C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 532 |
| **7.1.2** | Verificare che l'applicazione non registri altri dati sensibili come definiti dalle leggi sulla privacy locali o dalla relativa politica di sicurezza. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 532 |
| **7.1.3** | Verificare che l'applicazione registri eventi rilevanti per la sicurezza, inclusi eventi di autenticazione riusciti e non riusciti, errori di controllo dell'accesso, errori di deserializzazione ed errori di convalida dell'input. ([C5, C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 778 |
| **7.1.4** | Verificare che ogni evento di log includa le informazioni necessarie per consentire un'analisi dettagliata della cronologia degli eventi. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 778 |

## V7.2 Elaborazione dei Log

La registrazione tempestiva è fondamentale per gli eventi di audit, la classificazione e la gestione delle escalation. È necessario assicurarsi che i log dell'applicazione siano chiari e possano essere facilmente monitorati e analizzati localmente oppure inviati ad un sistema di monitoraggio remoto.

La sezione V7.2 copre la voce A10 dell'OWASP Top 10 2017. Poiché né la voce A10 del 2017 né questa sezione sono facilmente verificabili tramite penetration testing, è importante:

* Per gli sviluppatori: garantire la piena conformità a questa sezione, trattando tutte le voci come se fossero contrassegnate come L1.
* Per i penetration tester: convalidare la piena conformità di tutte le voci in V7.1 tramite interviste, screenshot o dichiarazioni.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.2.1** | Verificare che tutti i tentativi di autenticazione vengano registrati, senza memorizzare token di sessione o password sensibili. Questo dovrebbe includere le richieste con metadati necessari per le indagini di sicurezza. | | ✓ | ✓ | 778 |
| **7.2.2** | Verificare che tutte le decisioni di controllo dell'accesso possano essere registrate e che tutte le autorizzazioni negate vengano registrate. Questo dovrebbe includere le richieste con metadati pertinenti necessari per le indagini di sicurezza. | | ✓ | ✓ | 285 |

## V7.3 Protezione dei log

I log che possono essere facilmente modificati o eliminati risultano inutili per indagini e le azioni legali. La divulgazione dei log può esporre dettagli interni sull'applicazione o sui dati in essa contenuti. È quindi necessario proteggere i log da divulgazione, modifica o eliminazione non autorizzate.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.3.1** | Verificare che tutti i componenti di logging codifichino opportunamente i dati per prevenire l'injection di log. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 117 |
| **7.3.2** | [ELIMINATO, DUPLICATO DI 7.3.1] | | | | |
| **7.3.3** | Verificare che i log di sicurezza siano protetti da accesso e da modifiche non autorizzate. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 200 |
| **7.3.4** | Verificare che le sorgenti temporali siano sincronizzate con l'ora e il fuso orario corretti. Valutare attentamente la registrazione solo in UTC se i sistemi sono globali per facilitare l'analisi forense post-incidente. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

Nota: la codifica dei log (7.3.1) è difficile da testare e revisionare utilizzando strumenti dinamici automatizzati e penetration test, ma architetti, sviluppatori e revisori del codice sorgente dovrebbero considerarla un requisito L1.

## V7.4 Gestione degli Errori

Lo scopo della gestione degli errori è permettere all'applicazione di generare eventi rilevanti per la sicurezza, utili per monitoraggio, classificazione ed escalation. Non si tratta solo di creare log. Quando si registrano eventi di sicurezza, assicurarsi che i log abbiano uno scopo preciso e possano essere facilmente distinti da SIEM o software di analisi.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.4.1** | Verificare che venga visualizzato un messaggio generico quando si verifica un errore imprevisto o relativo alla sicurezza, potenzialmente con un ID univoco che il personale di supporto può utilizzare per indagare. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 210 |
| **7.4.2** | Verificare che la gestione delle eccezioni (o un equivalente funzionale) venga utilizzata in tutto il codice per tenere conto di condizioni di errore previste e impreviste. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 544 |
| **7.4.3** | Verificare che sia definito un gestore di errori "di ultima istanza" in grado di intercettare tutte le eccezioni non gestite ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 431 |

Nota: alcuni linguaggi, come Swift e Go, e molti linguaggi funzionali a causa delle comuni pratiche di progettazione, non supportano eccezioni o gestori di eventi di ultima istanza. In questo caso, architetti e sviluppatori devono utilizzare un modello, un linguaggio o un framework che consenta alle applicazioni di gestire in modo sicuro eventi eccezionali, imprevisti o relativi alla sicurezza.

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Testing Guide 4.0 content: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README.html)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
