# V5 Validazione, Sanificazione e Codifica

## Obiettivo del controllo

La problematica di sicurezza più comune nelle applicazioni web è la mancanza di una valida convalida dell'input proveniente dal client o dall'ambiente, e l'assenza di codifica dell'output. Questa carenza è alla base delle vulnerabilità più gravi delle applicazioni web, come Cross-Site Scripting (XSS), SQL injection, injection di interprete, attacchi locale/Unicode, attacchi al file system e buffer overflow.

Per garantire la sicurezza dell'applicazione, è essenziale soddisfare i seguenti requisiti di alto livello:

* L'architettura di convalida dell'input e di codifica dell'output deve seguire procedure concordate per prevenire gli attacchi di injection.
* I dati di input devono essere fortemente tipizzati, validati, controllati per range o lunghezza, sanitizzati o filtrati.
* I dati di output devono essere codificati o "escaped" in base al contesto, il più vicino possibile all'interprete.

Con l'architettura moderna delle applicazioni web, la codifica dell'output è più importante che mai. In alcuni scenari è difficile fornire una convalida dell'input efficace, quindi l'utilizzo di API sicure come query parametrizzate, framework di templating con escaping automatico o una codifica dell'output accuratamente scelta è fondamentale per la sicurezza dell'applicazione.

## V5.1 Input Validation

L'implementazione corretta dei controlli di convalida dell'input, utilizzando allow list e tipizzazione forte dei dati, può eliminare oltre il 90% di tutti gli attacchi di injection. I controlli di lunghezza e di range possono ridurre ulteriormente tali attacchi. Integrare una convalida dell'input sicura è fondamentale durante l'architettura dell'applicazione, gli sprint di progettazione, l'implementazione e i test unitari e di integrazione. Sebbene molti di questi aspetti non possano essere verificati durante i penetration test, i risultati della loro mancata implementazione si riflettono generalmente in V5.3 - Requisiti di codifica dell'output e prevenzione delle injection. Si consiglia a sviluppatori e revisori di codice sicuro di trattare questa sezione come se il livello L1 fosse obbligatorio per tutte le voci al fine di prevenire le injection.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.1.1** | Verificare che l'applicazione disponga di difese contro gli attacchi di HTTP Parameter Pollution (HPP), soprattutto se il framework applicativo non distingue tra le sorgenti dei parametri di richiesta (GET, POST, cookie, header o variabili d'ambiente). | ✓ | ✓ | ✓ | 235 |
| **5.1.2** | Verificare che il framework protegga dagli attacchi di assegnazione di massa dei parametri (Mass Assignment) o che l'applicazione implementi contromisure, come la marcatura dei campi come privati, per prevenire l'assegnazione insicura dei parametri. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 915 |
| **5.1.3** | Verificare che tutti gli input (campi di form HTML, richieste REST, parametri URL, header HTTP, cookie, file batch, feed RSS, ecc.) siano validati utilizzando la convalida positiva (liste positive o allow list). ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.4** | Verificare che i dati strutturati siano fortemente tipizzati e validati rispetto a uno schema definito, inclusi caratteri consentiti, lunghezza e pattern (ad esempio numeri di carta di credito, indirizzi e-mail, numeri di telefono o convalida di coerenza tra campi correlati, come la verifica della corrispondenza tra città e codice postale). ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.5** | Verificare che i redirect e i forward degli URL consentano solo destinazioni presenti in una lista consentita, oppure che mostrino un avviso quando si reindirizza verso contenuti potenzialmente non sicuri. | ✓ | ✓ | ✓ | 601 |

## V5.2 Sanitization and Sandboxing

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.2.1** | Verificare che tutto l'input HTML non fidato proveniente da editor WYSIWYG o simili venga correttamente sanitizzato con una libreria o funzionalità del framework per la sanitizzazione HTML. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.2.2** | Verificare che i dati non strutturati vengano sanitizzati per applicare misure di sicurezza come caratteri consentiti e vincoli sulla lunghezza. | ✓ | ✓ | ✓ | 138 |
| **5.2.3** | Verificare che l'applicazione sanitizzi l'input dell'utente prima di inviarlo ai sistemi di posta elettronica per proteggersi dall'injection di codice SMTP o IMAP. | ✓ | ✓ | ✓ | 147 |
| **5.2.4** | Verificare che l'applicazione eviti l'utilizzo di eval() o altre funzionalità di esecuzione dinamica del codice. Se non ci sono alternative, qualsiasi input utente incluso deve essere sanitizzato o eseguito in sandbox prima dell'esecuzione. | ✓ | ✓ | ✓ | 95 |
| **5.2.5** | Verificare che l'applicazione si protegga dagli attacchi di injection di template assicurando che qualsiasi input utente incluso venga sanitizzato o eseguito in sandbox. | ✓ | ✓ | ✓ | 94 |
| **5.2.6** | Verificare che l'applicazione si protegga dagli attacchi SSRF convalidando o sanificando dati non fidati o metadati di file HTTP, come nomi di file e campi di input URL, e utilizzando liste consentite di protocolli, domini, percorsi e porte. | ✓ | ✓ | ✓ | 918 |
| **5.2.7** | Verificare che l'applicazione sanitizzi, disabiliti o esegua in sandbox contenuti SVG (Scalable Vector Graphics) scriptabili forniti dall'utente, in particolare quelli relativi a XSS derivanti da script inline e foreignObject. | ✓ | ✓ | ✓ | 159 |
| **5.2.8** | Verificare che l'applicazione sanitizzi, disabiliti o esegua in sandbox contenuti forniti dall'utente in linguaggi di scripting o di templating come Markdown, fogli di stile CSS o XSL, BBCode o simili. | ✓ | ✓ | ✓ | 94 |

## V5.3 V5.3 Codifica dell'output e prevenzione delle injection

L'applicazione della codifica dell'output nelle immediate vicinanze o direttamente all'interno dell'interprete utilizzato è fondamentale per garantire la sicurezza di qualsiasi applicazione. Generalmente, la codifica dell'output non viene memorizzata in modo permanente, ma serve a rendere sicuro l'output nel contesto appropriato per un utilizzo immediato. La mancata codifica dell'output rende l'applicazione vulnerabile a iniezioni e potenzialmente pericolosa.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.3.1** | Verificare che la codifica dell'output sia pertinente all'interprete e al contesto specifico. Ad esempio, utilizzare codificatori specifici per valori HTML, attributi HTML, JavaScript, parametri URL, header HTTP, SMTP e altri a seconda del contesto, soprattutto per input non fidati (ad esempio nomi con caratteri Unicode o apostrofi, come ねこ o O'Hara). ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.3.2** | Verificare che la codifica dell'output preservi il set di caratteri e la località scelti dall'utente, in modo tale che qualsiasi punto del carattere Unicode sia valido e gestito in modo sicuro. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 176 |
| **5.3.3** | Verificare che l'escape dell'output contestuale, preferibilmente automatico o, in casi limite, manuale, protegga da XSS riflessa, memorizzata e basata su DOM.  ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 79 |
| **5.3.4** | Verificare che la selezione dei dati o le query del database (ad esempio SQL, HQL, ORM, NoSQL) utilizzino query parametrizzate, ORM, framework di entità o siano altrimenti protette dagli attacchi di injection del database. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.5** | Verificare che, quando i meccanismi parametrizzati o più sicuri non siano presenti, venga utilizzata la codifica dell'output specifica del contesto per proteggersi dagli attacchi di injection, come l'utilizzo dell'escaping SQL per proteggersi dall'injection SQL. ([C3, C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.6** | Verificare che l'applicazione si protegga dagli attacchi di injection JSON, dagli attacchi eval JSON e dalla valutazione delle espressioni JavaScript. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 830 |
| **5.3.7** | Verificare che l'applicazione si protegga dalle vulnerabilità di injection LDAP o che siano stati implementati controlli di sicurezza specifici per prevenire l'injection LDAP. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 90 |
| **5.3.8** | Verificare che l'applicazione si protegga dall'injection di comandi del SO e che le chiamate al sistema operativo utilizzino query del SO parametrizzate o la codifica contestuale dell'output della riga di comando. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 78 |
| **5.3.9** | Verificare che l'applicazione si protegga dagli attacchi di inclusione locale di file (LFI) o inclusione remota di file (RFI). | ✓ | ✓ | ✓ | 829 |
| **5.3.10** | Verificare che l'applicazione si protegga dagli attacchi di injection XPath o injection XML. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 643 |

Nota: L'utilizzo di query SQL parametrizzate o l'escaping del codice SQL non è sempre sufficiente a prevenire le injection. Nomi di tabelle, colonne, clausole ORDER BY e altri elementi simili non possono essere soggetti a escaping. L'inclusione di dati forniti dall'utente, anche se sottoposti a escaping, in questi campi può portare a query errate o a vulnerabilità di injection SQL.

Nota: Il formato SVG consente esplicitamente l'esecuzione di script ECMA in quasi tutti i contesti, il che potrebbe rendere impossibile bloccare completamente tutti i vettori XSS basati su SVG. Se il caricamento di file SVG è necessario, si raccomanda fortemente di servire tali file con il tipo MIME testo/plain o di utilizzare un dominio separato per i contenuti forniti dagli utenti, in modo da evitare che un attacco XSS riuscito possa compromettere l'intera applicazione.

## V5.4 Memoria, Stringhe e Codice Non Gestito

I seguenti requisiti si applicano solo quando l'applicazione utilizza un linguaggio di sistema o codice non gestito.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.4.1** | Verificare che l'applicazione utilizzi stringhe memory-safe, copie di memoria sicure e operazioni aritmetiche su puntatori per rilevare o prevenire overflow dello stack, del buffer o dell'heap. | | ✓ | ✓ | 120 |
| **5.4.2** | Verificare che le format string non accettino input potenzialmente ostile e siano immutabili. | | ✓ | ✓ | 134 |
| **5.4.3** | Verificare che vengano utilizzate tecniche di convalida del segno, dell'intervallo e dell'input per prevenire overflow di interi. | | ✓ | ✓ | 190 |

## V5.5 Prevenzione dalla Deserializzazione

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.5.1** | Verificare che gli oggetti serializzati utilizzino controlli di integrità o siano crittografati per prevenire la creazione di oggetti malevoli o la manomissione dei dati. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 502 |
| **5.5.2** | Verificare che l'applicazione limiti correttamente i parser XML a utilizzare solo la configurazione più restrittiva possibile e che funzionalità non sicure come la risoluzione di entità esterne vengano disabilitate per prevenire attacchi di injection di Entità Esterne XML (XXE). | ✓ | ✓ | ✓ | 611 |
| **5.5.3** | Verificare che la deserializzazione di dati non fidati venga evitata o protetta sia nel codice personalizzato che nelle librerie di terze parti (come parser JSON, XML e YAML). | ✓ | ✓ | ✓ | 502 |
| **5.5.4** | Verificare che durante l'analisi del JSON nei browser o nei backend basati su JavaScript, venga utilizzato JSON.parse per analizzare il documento JSON. Evitare di utilizzare eval() per analizzare il JSON. | ✓ | ✓ | ✓ | 95 |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Testing Guide 4.0: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Cheat Sheet: Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution.html)
* [OWASP LDAP Injection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client Side Testing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client_Side_Testing/)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [XML External Entity (XXE) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)

Per informazioni aggiuntive su auto-escaping, consultare:

* [Reducing XSS by way of Automatic Context-Aware Escaping in Template Systems](https://googleonlinesecurity.blogspot.com/2009/03/reducing-xss-by-way-of-automatic.html)
* [AngularJS Strict Contextual Escaping](https://docs.angularjs.org/api/ng/service/$sce)
* [AngularJS ngBind](https://docs.angularjs.org/api/ng/directive/ngBind)
* [Angular Sanitization](https://angular.io/guide/security#sanitization-and-security-contexts)
* [Angular Security](https://angular.io/guide/security)
* [ReactJS Escaping](https://reactjs.org/docs/introducing-jsx.html#jsx-prevents-injection-attacks)
* [Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

Per informazioni aggiuntive su deserialization, consultare:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [OWASP Deserialization of Untrusted Data Guide](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)
