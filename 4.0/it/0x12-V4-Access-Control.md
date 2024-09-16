# V4 Controllo degli accessi

## Obiettivo del controllo

Con il termine autorizzazione si intende il processo di consentire l'accesso alle risorse solo a coloro che sono autorizzati a utilizzarle. È essenziale che un'applicazione verificata soddisfi i seguenti requisiti di alto livello:

* Gli utenti che accedono alle risorse devono disporre di credenziali valide.
* Agli utenti devono essere associati ruoli e privilegi ben definiti.
* I metadati di ruoli e permessi devono essere protetti da attacchi di replay o manomissione (tampering).

## Requisiti di verifica della sicurezza

## V4.1 Progettazione generale del controllo degli accessi

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.1.1** | Verificare che l'applicazione applichi le regole di controllo degli accessi su un livello di servizio trusted, soprattutto se è presente il controllo degli accessi lato client che potrebbe essere bypassato. | ✓ | ✓ | ✓ | 602 |
| **4.1.2** | Verificare che tutti gli attributi utente e dati e le informazioni sulle policy utilizzate dai controlli di accesso non possano essere manipolati dagli utenti finali se non espressamente autorizzati. | ✓ | ✓ | ✓ | 639 |
| **4.1.3** | Verificare che esista il principio del privilegio minimo: gli utenti dovrebbero poter accedere solo a funzioni, file di dati, URL, controller, servizi e altre risorse per le quali possiedono un'autorizzazione specifica. Ciò implica una protezione contro lo spoofing e l'escalation di privilegi ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |
| **4.1.4** | [ELIMINATO, DUPLICATO DI 4.1.3] | | | | |
| **4.1.5** | Verificare che i controlli di accesso falliscano in modo sicuro anche in caso di eccezione. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |

## V4.2 Controllo degli accessi a livello di operazione

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.2.1** | Verificare che i dati sensibili e le API siano protetti da attacchi IDOR (Insecure Direct Object Reference). Questi attacchi mirano alla creazione, lettura, aggiornamento ed eliminazione di record, come ad esempio quelli appartenenti ad altri utenti, la visualizzazione di tutti i record o l'eliminazione di tutti i dati. | ✓ | ✓ | ✓ | 639 |
| **4.2.2** | Verificare che l'applicazione o il framework implementi un meccanismo anti-CSRF robusto per proteggere le funzionalità autenticate e che un meccanismo anti-automazione o anti-CSRF efficace protegga anche le funzionalità non autenticate. | ✓ | ✓ | ✓ | 352 |

## V4.3 Ulteriori considerazioni sul controllo degli accessi

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.3.1** | Verificare che le interfacce di amministrazione utilizzino un'adeguata autenticazione a due fattori per prevenire l'utilizzo non autorizzato. | ✓ | ✓ | ✓ | 419 |
| **4.3.2** | Verificare che il directory listing sia disabilitato a meno che non sia espressamente richiesto. Inoltre, le applicazioni non devono consentire la scoperta o la divulgazione di metadati di file o directory, come cartelle Thumbs.db, .DS_Store, .git o .svn. | ✓ | ✓ | ✓ | 548 |
| **4.3.3** | Verificare che l'applicazione implementi un'autorizzazione aggiuntiva (step-up o adattiva) per i sistemi di basso valore e/o separazione dei compiti per le applicazioni di alto valore, al fine di applicare controlli antifrode in base al rischio e alle frodi passate. | | ✓ | ✓ | 732 |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Access Control](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
* [OWASP CSRF Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [OWASP REST Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
