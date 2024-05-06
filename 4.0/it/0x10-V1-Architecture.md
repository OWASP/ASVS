# V1 Architettura, progettazione e Threat Modeling

## Obiettivo del controllo

L'architettura di sicurezza in molte organizzazioni è diventata quasi un'arte perduta. Nell'era del DevSecOps l'epoca degli architetti enterprise è passata. Il campo della sicurezza delle applicazioni deve aggiornarsi e adottare i principi di sicurezza agile, reintroducendo al contempo i principi di architettura della sicurezza all'avanguardia per i professionisti del software. L'architettura non è un'implementazione, ma un modo di pensare a un problema che può avere potenzialmente molte soluzioni diverse e nessuna singola risposta "corretta". Troppo spesso la sicurezza è vista come inflessibile e richiede agli sviluppatori di correggere il codice in un modo particolare, quando gli sviluppatori potrebbero conoscere un modo molto migliore per risolvere il problema. Non esiste una soluzione singola e semplice per l'architettura, e fingere il contrario è un danno per il campo dell'ingegneria del software.

È probabile che un'implementazione specifica di un'applicazione web venga continuamente rivista durante tutto il suo ciclo di vita, ma l'architettura complessiva probabilmente cambierà raramente, ma si evolverà lentamente. L'architettura della sicurezza è identica: abbiamo bisogno dell'autenticazione oggi, la richiederemo domani e anche tra cinque anni. Se prendiamo decisioni ponderate oggi, possiamo risparmiare un sacco di sforzi, tempo e denaro se selezioniamo e riutilizziamo soluzioni conformi all'architettura. Ad esempio, un decennio fa, l'autenticazione a più fattori veniva utilizzata raramente.

Se gli sviluppatori avessero investito in un singolo modello di provider di identità sicuro, come l'identità federata SAML, il provider di identità potrebbe essere aggiornato per incorporare nuovi requisiti come la conformità al NIST 800-63, pur non modificando le interfacce dell'applicazione originale. Se più applicazioni condividerebbero la stessa architettura di sicurezza e quindi lo stesso componente, beneficerebbero tutte contemporaneamente di questo aggiornamento. Tuttavia, SAML non rimarrà sempre la soluzione di autenticazione migliore o più adatta - potrebbe essere necessario sostituirla con altre soluzioni al variare dei requisiti. Cambiamenti di questo tipo sono o complicati, così costosi da richiedere una riscrittura completa, oppure impossibili senza un'architettura di sicurezza.

In questo capitolo, l'ASVS tratta gli aspetti principali di qualsiasi architettura di sicurezza solida: disponibilità, riservatezza, integrità dell'elaborazione, non ripudio e privacy. Ognuno di questi principi di sicurezza deve essere integrato e nativo in tutte le applicazioni. È fondamentale "spostarsi a sinistra", iniziando con incoraggiare gli sviluppatori all'utilizzo di checklist di programmazione sicura, mentoring e formazione, programmazione e test, build, distribuzione, configurazione e operations, e terminando con test indipendenti successivi per assicurarsi che tutti i controlli di sicurezza siano presenti e funzionanti. L'ultimo passaggio era tutto ciò che veniva svolto nel settore, ma non è più sufficiente quando gli sviluppatori spingono il codice in produzione decine o centinaia di volte al giorno. I professionisti della sicurezza delle applicazioni devono tenere il passo con le tecniche agili, il che significa adottare strumenti per sviluppatori, imparare a programmare e lavorare con gli sviluppatori piuttosto che criticare il progetto mesi dopo che tutti gli altri sono andati avanti.

## V1.1 Ciclo di vita sicuro dello sviluppo software (S-SDLC)

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.1.1** | Verificare l'utilizzo di un ciclo di vita sicuro dello sviluppo software (S-SDLC) che tenga conto della sicurezza in tutte le fasi di sviluppo. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **1.1.2** | Verificare l'utilizzo della threat modeling per ogni modifica del design o pianificazione dello sprint per identificare le minacce, pianificare contromisure, facilitare risposte ai rischi appropriate e guidare i test di sicurezza. | | ✓ | ✓ | 1053 |
| **1.1.3** | Verificare che tutte le user story e le funzionalità contengano vincoli di sicurezza funzionali, come "Come utente, dovrei poter visualizzare e modificare il mio profilo. Non dovrei poter visualizzare o modificare il profilo di nessun altro"	 | | ✓ | ✓ | 1110 |
| **1.1.4** | Verificare la documentazione e la giustificazione di tutti i perimetri di trust, componenti e flussi di dati significativi dell'applicazione. | | ✓ | ✓ | 1059 |
| **1.1.5** | Verificare la definizione e l'analisi della sicurezza dell'architettura di alto livello dell'applicazione e di tutti i servizi remoti collegati. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1059 |
| **1.1.6** | Verificare l'implementazione di controlli di sicurezza centralizzati, semplici (economia di progettazione), verificati, sicuri e riutilizzabili per evitare controlli duplicati, mancanti, inefficaci o non sicuri. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 637 |
| **1.1.7** | Verificare la disponibilità di una checklist di programmazione sicura, requisiti di sicurezza, linee guida o policy per tutti gli sviluppatori e tester.	. | | ✓ | ✓ | 637 |

## V1.2 Architettura di autenticazione

Quando si progetta l'autenticazione, non importa se si dispone di un'autenticazione multi-fattore basata su hardware se un aggressore può reimpostare un account chiamando un call center e rispondendo a domande comunemente note. Quando si verifica l'identità, tutti i percorsi di autenticazione devono avere la stessa efficacia.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.2.1** | Verificare l'utilizzo di account di sistema operativo univoci o speciali con privilegi minimi per tutti i componenti, servizi e server dell'applicazione. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 250 |
| **1.2.2** | Verificare che le comunicazioni tra i componenti dell'applicazione, incluse le API, il middleware e il data layer, siano autenticate. I componenti devono avere i privilegi minimi necessari. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 306 |
| **1.2.3** | Verificare che l'applicazione utilizzi un singolo meccanismo di autenticazione verificato noto per essere sicuro, estendibile per includere l'autenticazione forte e disponga di registri e monitoraggio sufficienti per rilevare abusi o violazioni dell'account. | | ✓ | ✓ | 306 |
| **1.2.4** | Verificare che tutti i flussi di autenticazione e le API di gestione delle identità implementino dei controlli di sicurezza di autenticazione coerenti in efficacia, in modo tale che non ci siano alternative più deboli, tenendo conto del livello di rischio dell'applicazione. | | ✓ | ✓ | 306 |
	
## V1.3 Architettura della gestione sessioni

Questo è un segnaposto per requisiti architetturali futuri. 

## V1.4 Architettura del Controllo Accessi

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.4.1** | Verificare che i punti di applicazione trusted, come gateway di controllo accessi, server e funzioni serverless, applichino i controlli di accesso. Non implementare mai controlli di accesso sul client. | | ✓ | ✓ | 602 |
| **1.4.2** | [ELIMINATO, NON APPLICABILE] | | | | |
| **1.4.3** | [ELIMINATO, DUPLICATO DI 4.1.3] | | | | |
| **1.4.4** | Verificare che l'applicazione utilizzi un unico meccanismo di controllo accessi ben collaudato per accedere a dati e risorse protette. Tutte le richieste devono passare attraverso questo singolo meccanismo per evitare copia e incolla o percorsi alternativi non sicuri. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 284 |
| **1.4.5** | Verificare che venga utilizzato il controllo di accesso basato sugli attributi o sulle funzionalità, in modo tale che il codice controlli l'autorizzazione dell'utente per una funzionalità/elemento dati piuttosto che solo per il suo ruolo. Le autorizzazioni devono comunque essere assegnate utilizzando i ruoli. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 275 |

## V1.5 Architettura di Input e Output 

Nella versione 4.0, abbiamo abbandonato il termine "lato server" in quanto termine ambiguo relativo al perimetro di trust. Il perimetro di trust rimane comunque un aspetto critico: controlli su browser o dispositivi client non affidabili possono essere facilmente aggirati. Tuttavia, nelle implementazioni architetturali tradizionali odierne, il punto di di contatto con un componente trusted è cambiato radicalmente. Pertanto, quando nell'ASVS viene utilizzato il termine "livello di servizio trusted", si intende qualsiasi punto di applicazione trusted, indipendentemente dalla posizione, come un microservizio, un'API serverless, lato server, un'API trusted su un dispositivo client con secure boot, API di partner o esterne e così via.

Il termine "client non affidabile" in questo contesto si riferisce alle tecnologie lato client che renderizzano il livello di presentazione, comunemente chiamate tecnologie "front-end". Il termine "serializzazione" qui non si riferisce solo all'invio di dati attraverso la rete come una matrice di valori o all'ottenimento e alla lettura di una struttura JSON, ma anche al passaggio di oggetti complessi che possono contenere logica.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.5.1** | Verificare che i requisiti di input e output definiscano chiaramente come gestire ed elaborare i dati in base al tipo, al contenuto, alle leggi in vigore, ai regolamenti e alla conformità ad altre policy applicabili. | | ✓ | ✓ | 1029 |
| **1.5.2** | Verificare che la serializzazione non venga utilizzata quando si comunica con client non affidabili. Se ciò non è possibile, assicurarsi che vengano applicati controlli di integrità adeguati (e possibilmente la crittografia se vengono inviati dati sensibili) per prevenire attacchi di deserializzazione, inclusa l'iniezione di oggetti. | | ✓ | ✓ | 502 |
| **1.5.3** | Verificare che la convalida degli input venga applicata su un livello di servizio trusted. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 602 |
| **1.5.4** | Verificare che la codifica dell'output avvenga vicino o dall'interprete per il quale è destinata. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 116 |

## V1.6 Architettura Crittografica

Le applicazioni devono essere progettate con una solida architettura crittografica per proteggere i dati in base alla loro classificazione. Crittografare tutto è uno spreco, non crittografare nulla è legalmente negligente. È necessario trovare un equilibrio, di solito durante la progettazione architetturale o ad alto livello, gli sprint di progettazione o le fasi di analisi architetturale. Progettare la crittografia "al volo" o adattarla a posteriori costerà inevitabilmente molto di più da implementare in modo sicuro rispetto ad un'integrazione fin dall'inizio.

I requisiti architetturali sono intrinseci all'intero codice e quindi difficili da testare a livello di unità o di integrazione. I requisiti architeturali richiedono considerazione negli standard di programmazione, durante tutta la fase di coding e dovrebbero essere rivisti durante la revisione dell'architettura di sicurezza, le revisioni del codice (anche peer) o durante le retrospettive.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.6.1** | Verificare che esista una policy esplicita per la gestione delle chiavi crittografiche e che il ciclo di vita delle chiavi crittografiche segua uno standard di gestione delle chiavi come NIST SP 800-57. | | ✓ | ✓ | 320 |
| **1.6.2** | Verificare che gli utilizzatori di servizi crittografici proteggano il materiale chiave e altri segreti utilizzando key vault o alternative basate su API. | | ✓ | ✓ | 320 |
| **1.6.3** | Verificare che tutte le chiavi e le password siano sostituibili e facciano parte di un processo ben definito per la ri-crittografia dei dati sensibili. | | ✓ | ✓ | 320 |
| **1.6.4** | Verificare che l'architettura consideri i segreti lato client, come chiavi simmetriche, password o token API, come non sicuri e non li utilizzi mai per proteggere o accedere a dati sensibili. | | ✓ | ✓ | 320 |

## V1.7 Architettura Errori, Logging e Audit

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.7.1** | Verificare che venga utilizzato un formato e un approccio di logging comuni in tutto il sistema.  ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1009 |
| **1.7.2** | Verificare che i log vengano trasmessi in modo sicuro a un sistema, preferibilmente remoto, per analisi, rilevamento, allerta e escalation. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

## V1.8 Architettura Protezione Dati e Privacy

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.8.1** | Verificare che tutti i dati sensibili siano identificati e classificati con adeguati livelli di protezione. | | ✓ | ✓ | |
| **1.8.2** | Verificare che a tutti i livelli di protezione sia associato un set di requisiti di protezione, come requisiti di crittografia, requisiti di integrità, conservazione, privacy e altri requisiti di riservatezza, e che questi vengano applicati nell'architettura. | | ✓ | ✓ | |

## V1.9 Architettura Comunicazione

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.9.1** | Verificare che l'applicazione crittografi le comunicazioni tra componenti, in particolare quando questi componenti si trovano in container, sistemi, siti o provider cloud diversi. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 319 |
| **1.9.2** | Verificare che i componenti applicativi verifichino l'autenticità di ciascuna parte in un collegamento di comunicazione per prevenire attacchi man-in-the-middle. Ad esempio, i componenti dell'applicazione dovrebbero validare i certificati e le catene TLS. | | ✓ | ✓ | 295 |

## V1.10 Architettura Software Maligno

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.10.1** | Verificare l'utilizzo di un sistema di controllo del codice sorgente, con procedure per garantire che i check-in siano accompagnati da segnalazioni o ticket di modifica. Il sistema di controllo del codice sorgente deve disporre di controlli di accesso e utenti identificabili per consentire la tracciabilità di qualsiasi modifica. | | ✓ | ✓ | 284 |

## V1.11 Architettura Logica di Business

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.11.1** | Verificare la definizione e la documentazione di tutti i componenti applicativi in termini di funzioni aziendali o di sicurezza fornite. | | ✓ | ✓ | 1059 |
| **1.11.2** | Verificare che tutti i flussi logici di business di alto valore, inclusi autenticazione, gestione sessioni e controllo degli accessi, sincronizzino correttamente lo stato. | | ✓ | ✓ | 362 |
| **1.11.3** | Verificare che tutti i flussi logici di business di alto valore, inclusi autenticazione, gestione sessioni e controllo degli accessi, siano thread-safe e resistenti a race conditions quali "time-of-check" e "time-of-use". | | | ✓ | 367 |

## V1.12 Architettura Caricamento Sicuro di File

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.12.1** | [ELIMINATO, DUPLICATO DI 12.4.1] | | | | |
| **1.12.2** | Verificare che i file caricati dagli utenti - se devono essere visualizzati o scaricati dall'applicazione - vengano serviti tramite octet stream o da un dominio non correlato, come un bucket di archiviazione file cloud. Implementare una Content Security Policy (CSP) adeguata per ridurre il rischio di vettori XSS o altri attacchi. | | ✓ | ✓ | 646 |

## V1.13 API Architecture

Questo è un segnaposto per requisiti architetturali futuri.

## V1.14 Configuration Architecture

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.14.1** | Verificare la segregazione dei componenti con livelli di trust differenti attraverso controlli di sicurezza ben definiti, regole firewall, gateway API, proxy inverso, gruppi di sicurezza basati su cloud o meccanismi simili. | | ✓ | ✓ | 923 |
| **1.14.2** | Verificare l'utilizzo di firme, connessioni affidabili e endpoint verificati per distribuire i file binari su dispositivi remoti. | | ✓ | ✓ | 494 |
| **1.14.3** | Verificare che la pipeline di build avvisi di componenti obsoleti o non sicuri e intraprenda azioni appropriate. | | ✓ | ✓ | 1104 |
| **1.14.4** | Verificare che la pipeline di build contenga un passaggio di build per automatizzare la creazione e la verifica del deployment sicuro dell'applicazione, soprattutto se l'infrastruttura dell'applicazione è software-defined, come gli script di build per ambienti cloud. | | ✓ | ✓ | |
| **1.14.5** | Verificare che le distribuzioni dell'applicazione implementino adeguatamente sandbox, containerizzazione e/o isolamento a livello di rete per rallentare e scoraggiare gli aggressori dall'attaccare altre applicazioni, specialmente quando eseguono azioni sensibili o pericolose come la deserializzazione. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |
| **1.14.6** | Verificare che l'applicazione non utilizzi tecnologie client-side non supportate, non sicure o obsolete come plugin NSAPI, Flash, Shockwave, ActiveX, Silverlight, NACL o applet Java client-side. | | ✓ | ✓ | 477 |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
