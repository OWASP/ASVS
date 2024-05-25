# V10 Codice malevolo

## Obiettivo del controllo

Assicurarsi che l'applicazione rispetti i seguenti requisiti di alto livello:

* La gestione delle attività malevole deve essere sicura e appropriata per non compromettere il resto dell'applicazione.
* Il codice non deve contenere bombe a tempo o altri attacchi temporizzati.
* Il codice non deve "chiamare casa" verso destinazioni malevole o non autorizzate.
* Il codice deve essere privo di backdoor, Easter egg, attacchi salami, rootkit o codice non autorizzato controllabile da un aggressore.

È impossibile verificare completamente l'assenza di codice malevolo. Tuttavia, si devono compiere tutti gli sforzi possibili per garantire che il codice non contenga funzionalità dannose o indesiderate.

## V10.1 Code Integrity

La migliore difesa contro il codice malevolo è "fidarsi, ma verificare". L'introduzione di codice non autorizzato o malevolo nel sorgente è spesso considerata un reato in molte giurisdizioni. 
Le politiche e le procedure dovrebbero chiarire le sanzioni relative al codice malevolo.

I lead developer dovrebbero revisionare regolarmente i commit del codice, in particolare quelli che potrebbero accedere alle funzioni di time, I/O o di rete.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **10.1.1** | Verificare che sia in uso uno strumento di analisi del codice in grado di rilevare codice potenzialmente malevolo, come funzioni temporali, operazioni insicure su file e connessioni di rete.	 | | | ✓ | 749 |

## V10.2 Ricerca di codice malevolo

Il codice malevolo è estremamente raro e difficile da individuare. La revisione manuale riga per riga del codice può aiutare a cercare bombe logiche, ma anche il revisore di codice più esperto avrà difficoltà a trovare codice malevolo anche se sa che esiste.

La conformità a questa sezione non è possibile senza un accesso completo al codice sorgente, incluse le librerie di terze parti.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **10.2.1** | Verificare che il codice sorgente dell'applicazione e le librerie di terze parti non contengano funzionalità non autorizzate di "chiamata a casa" o raccolta dati. Se tale funzionalità esiste, è necessario ottenere il permesso dell'utente prima di raccogliere qualsiasi dato.	 | | ✓ | ✓ | 359 |
| **10.2.2** | Verificare che l'applicazione non richieda autorizzazioni non necessarie o eccessive per funzionalità o sensori legati alla privacy, come contatti, fotocamere, microfoni o posizione.	 | | ✓ | ✓ | 272 |
| **10.2.3** | Verificare che il codice sorgente dell'applicazione e le librerie di terze parti non contengano backdoor, come account o chiavi aggiuntive non documentate e codificate, offuscamento del codice, blob binari non documentati, rootkit, funzionalità anti-debug, funzionalità di debug non sicure o funzionalità obsolete, non sicure o nascoste che potrebbero essere utilizzate in modo malevolo se scoperte.	 | | | ✓ | 507 |
| **10.2.4** | Verificare che il codice sorgente dell'applicazione e le librerie di terze parti non contengano bombe a tempo cercando funzioni relative a data e ora.	 | | | ✓ | 511 |
| **10.2.5** | Verificare che il codice sorgente dell'applicazione e le librerie di terze parti non contengano codice malevolo, come attacchi salami, bypass logici o bombe logiche.	 | | | ✓ | 511 |
| **10.2.6** | Verificare che il codice sorgente dell'applicazione e le librerie di terze parti non contengano Easter egg o altre funzionalità potenzialmente indesiderate.	 | | | ✓ | 507 |

## V10.3 Integrità dell'applicazione

Anche dopo la distribuzione di un'applicazione, è possibile inserire codice malevolo. Le applicazioni devono proteggersi da attacchi comuni, come l'esecuzione di codice non firmato da fonti non fidate e takeover di sottodomini.

La conformità a questa sezione richiede probabilmente controlli operativi e continui.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **10.3.1** | Verificare che, se l'applicazione dispone di una funzione di aggiornamento automatico client o server, gli aggiornamenti vengano ottenuti su canali sicuri e firmati digitalmente. Il codice di aggiornamento deve convalidare la firma digitale dell'aggiornamento prima di installarlo o eseguirlo.	 | ✓ | ✓ | ✓ | 16 |
| **10.3.2** | Verificare che l'applicazione impieghi protezioni dell'integrità, come la firma del codice o l'integrità delle sotto-risorse. L'applicazione non deve caricare o eseguire codice da fonti non fidate, come inclusioni, moduli, plugin, codice o librerie provenienti da fonti non fidate o da Internet.	 | ✓ | ✓ | ✓ | 353 |
| **10.3.3** | Verificare che l'applicazione disponga di protezioni contro takeover di sottodomini se si affida a voci DNS o sottodomini DNS, come nomi di dominio scaduti, puntatori DNS o CNAME obsoleti, progetti scaduti in repository di codice sorgente pubblici, o API cloud temporanee, funzioni serverless o bucket di archiviazione (autogen-bucket-id.cloud.example.com) o simili. Le protezioni possono includere la verifica periodica della scadenza o della modifica dei nomi DNS utilizzati dalle applicazioni.	 | ✓ | ✓ | ✓ | 350 |

## Riferimenti

Per approfondimenti, consultare:

* [Hostile Subdomain Takeover, Detectify Labs](https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/)
* [Hijacking of abandoned subdomains part 2, Detectify Labs](https://labs.detectify.com/2014/12/08/hijacking-of-abandoned-subdomains-part-2/)
