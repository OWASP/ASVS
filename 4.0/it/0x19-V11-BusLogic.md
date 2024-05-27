# V11 Logica di business

## Obiettivo del controllo

Verificare che un'applicazione soddisfi i seguenti requisiti di alto livello:

* Il flusso della logica di business deve essere sequenziale, elaborato in ordine e non deve poter essere aggirato.
* La logica di business deve includere limiti per rilevare e prevenire attacchi automatizzati, come trasferimenti di fondi continui di piccolo importo o l'aggiunta di un milione di amici contemporaneamente.
* I flussi della logica di business ad alto valore devono tenere conto di possibili abusi e attori malintenzionati, e devono essere dotati di protezioni contro attacchi di spoofing (falsificazione), manomissione, divulgazione di informazioni e escalation di privilegi.

## V11.1 Sicurezza della logica di business

La sicurezza della logica di business è così specifica per ogni applicazione che non esiste una lista di controllo univoca applicabile universalmente. La sicurezza della logica di business deve essere progettata per proteggersi da probabili minacce esterne - non può essere aggiunta utilizzando firewall per applicazioni web o comunicazioni sicure. Si raccomanda l'utilizzo del threat modeling durante le fasi di progettazione, ad esempio utilizzando OWASP Cornucopia o strumenti simili.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **11.1.1** | Verificare che l'applicazione elabori i flussi della logica di business per lo stesso utente solo in sequenza e senza saltare passaggi. | ✓ | ✓ | ✓ | 841 |
| **11.1.2** | Verificare che l'applicazione elabori i flussi della logica di business solo con tutti i passaggi completati in un lasso di tempo umano realistico, ovvero le transazioni non vengono inviate troppo rapidamente. | ✓ | ✓ | ✓ | 799 |
| **11.1.3** | Verificare che l'applicazione abbia limiti appropriati per azioni o transazioni aziendali specifiche, applicati correttamente su base per utente. | ✓ | ✓ | ✓ | 770 |
| **11.1.4** | Verificare che l'applicazione disponga di controlli anti-automazione per proteggersi da chiamate eccessive, come esfiltrazione di massa di dati, richieste di logica di business, caricamenti di file o attacchi denial of service. | ✓ | ✓ | ✓ | 770 |
| **11.1.5** | Verificare che l'applicazione disponga di limiti o convalide della logica di business per proteggersi da probabili rischi o minacce aziendali, identificati mediante threat modeling o metodologie simili. | ✓ | ✓ | ✓ | 841 |
| **11.1.6** | Verificare che l'applicazione non soffra di problemi "Time Of Check to Time Of Use" (TOCTOU) o altre condizioni di race condition per operazioni sensibili. | | ✓ | ✓ | 367 |
| **11.1.7** | Verificare che l'applicazione monitori eventi o attività inusuali da una prospettiva di logica di business. Ad esempio, tentativi di eseguire azioni fuori ordine o azioni che un utente normale non proverebbe mai ad eseguire. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 754 |
| **11.1.8** | Verificare che l'applicazione abbia un sistema di allerta configurabile in caso di rilevamento di attacchi automatizzati o attività inusuali. | | ✓ | ✓ | 390 |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Web Security Testing Guide 4.1: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README.html)
* Anti-automation can be achieved in many ways, including the use of [OWASP AppSensor](https://github.com/jtmelton/appsensor) and [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP AppSensor](https://github.com/jtmelton/appsensor) can also help with Attack Detection and Response.
* [OWASP Cornucopia](https://owasp.org/www-project-cornucopia/)
