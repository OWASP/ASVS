# V1 Architettura, progettazione e Threat Modeling

## Obiettivo del controllo

L'architettura di sicurezza in molte organizzazioni è diventata quasi un'arte perduta. Nell'era del DevSecOps, l'epoca degli architetti enterprise sembra superata. Il campo della sicurezza delle applicazioni deve evolversi, adottando i principi di sicurezza agile, pur reintroducendo i concetti di architettura della sicurezza più avanzati per i professionisti del software. L'architettura non riguarda l'implementazione, ma è un modo di affrontare i problemi che può portare a molte soluzioni diverse, senza una risposta "corretta" unica. Troppo spesso la sicurezza è percepita come rigida, richiedendo agli sviluppatori di correggere il codice in un modo specifico, quando potrebbero conoscere soluzioni migliori. Pensare che esista una soluzione unica per l'architettura è dannoso per l'ingegneria del software.

Un'applicazione web verrà probabilmente rivista più volte durante il suo ciclo di vita, ma la sua architettura complessiva cambierà raramente, evolvendosi lentamente. Lo stesso vale per l'architettura della sicurezza: oggi abbiamo bisogno dell'autenticazione, la richiederemo domani e tra cinque anni. Decisioni ponderate oggi possono far risparmiare tempo, sforzi e risorse in futuro, se si selezionano soluzioni conformi all'architettura esistente. Ad esempio, un decennio fa, l'autenticazione a più fattori era poco diffusa, ma oggi è una componente chiave.

Se gli sviluppatori avessero investito in un unico modello sicuro di provider di identità, come l'identità federata tramite SAML, il provider di identità potrebbe essere aggiornato per soddisfare nuovi requisiti, come la conformità al NIST 800-63, senza dover modificare le interfacce dell'applicazione originale. Se più applicazioni condividono la stessa architettura di sicurezza e, quindi, lo stesso componente, tutte beneficerebbero contemporaneamente di questo aggiornamento. Tuttavia, SAML non sarà sempre la soluzione di autenticazione migliore o più adatta: potrebbe essere necessario sostituirla con altre soluzioni in base ai nuovi requisiti. Tali cambiamenti possono essere molto complessi, costosi al punto da richiedere una riscrittura completa, o impossibili da gestire senza una solida architettura di sicurezza.

In questo capitolo, l'ASVS affronta i principi fondamentali di una buona architettura di sicurezza: disponibilità, riservatezza, integrità dell'elaborazione, non ripudio e privacy. Questi principi devono essere integrati in modo nativo in tutte le applicazioni. È essenziale "spostarsi a sinistra", iniziando con l'adozione di checklist di programmazione sicura, mentoring, formazione, test di programmazione, build, distribuzione, configurazione e operations, fino a concludere con test indipendenti per garantire che tutti i controlli di sicurezza siano attivi e funzionanti. Tradizionalmente, l'ultimo passaggio era l'unico svolto nel settore, ma non è più sufficiente quando il codice viene distribuito in produzione decine o centinaia di volte al giorno. I professionisti della sicurezza devono tenere il passo con le metodologie agili, adottare strumenti di sviluppo, imparare a programmare e collaborare con gli sviluppatori, piuttosto che criticare i progetti mesi dopo che il lavoro è stato concluso e il team è passato oltre.

## V1.1 Ciclo di vita sicuro dello sviluppo software (S-SDLC)

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.1.1** | Verificare l'utilizzo di un ciclo di vita sicuro dello sviluppo software (S-SDLC) che tenga conto della sicurezza in tutte le fasi di sviluppo. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **1.1.2** | Verificare l'utilizzo del threat modeling per ogni modifica del design o nella pianificazione dello sprint al fine di identificare le minacce, pianificare contromisure, facilitare risposte ai rischi appropriate e guidare i test di sicurezza. | | ✓ | ✓ | 1053 |
| **1.1.3** | Verificare che tutte le user story e le funzionalità includano vincoli di sicurezza funzionali, come "Come utente, dovrei poter visualizzare e modificare il mio profilo. Non dovrei poter visualizzare o modificare il profilo di nessun altro" | | ✓ | ✓ | 1110 |
| **1.1.4** | Verificare che tutti i perimetri di trust, i componenti e i flussi di dati significativi dell'applicazione siano documentati e giustificati in modo accurato. | | ✓ | ✓ | 1059 |
| **1.1.5** | Verificare che l'architettura di alto livello dell'applicazione e tutti i servizi remoti collegati siano definiti e sottoposti a un'analisi approfondita dal punto di vista della sicurezza. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1059 |
| **1.1.6** | Verificare che siano implementati controlli di sicurezza centralizzati, semplici (secondo il principio dell'economia di progettazione), verificati, sicuri e riutilizzabili, per evitare controlli duplicati, mancanti, inefficaci o non sicuri. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 637 |
| **1.1.7** | Verificare che tutti gli sviluppatori e tester abbiano a disposizione una checklist di programmazione sicura, requisiti di sicurezza, linee guida o policy. | | ✓ | ✓ | 637 |

## V1.2 Architettura di autenticazione

Quando si progetta un sistema di autenticazione, è irrilevante se si utilizza l'autenticazione a più fattori basata su hardware se un aggressore può reimpostare un account semplicemente chiamando un call center e rispondendo a domande facilmente reperibili. Tutti i percorsi di autenticazione devono avere la stessa efficacia nella verifica dell'identità.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.2.1** | Verificare l'utilizzo di account di sistema operativo univoci o speciali con privilegi minimi per tutti i componenti, servizi e server dell'applicazione. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 250 |
| **1.2.2** | Verificare che le comunicazioni tra i componenti dell'applicazione, incluse le API, il middleware e il data layer, siano autenticate. I componenti devono avere i privilegi minimi necessari. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 306 |
| **1.2.3** | Verificare che l'applicazione utilizzi un unico meccanismo di autenticazione verificato noto per essere sicuro, estendibile per includere l'autenticazione forte e disponga di registri e monitoraggio sufficienti per rilevare abusi o violazioni dell'account. | | ✓ | ✓ | 306 |
| **1.2.4** | Verificare che tutti i flussi di autenticazione e le API di gestione delle identità implementino dei controlli di autenticazione coerenti in efficacia, in modo tale che non ci siano alternative più deboli, in linea con il livello di rischio dell'applicazione. | | ✓ | ✓ | 306 |

## V1.3 Architettura della gestione sessioni

Questo è un segnaposto per requisiti architetturali futuri. 

## V1.4 Architettura del Controllo Accessi

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.4.1** | Verificare che i punti di applicazione trusted, come gateway di controllo accessi, server e funzioni serverless, applichino controlli di accesso. Non implementare mai controlli di accesso sul client. | | ✓ | ✓ | 602 |
| **1.4.2** | [ELIMINATO, NON APPLICABILE] | | | | |
| **1.4.3** | [ELIMINATO, DUPLICATO DI 4.1.3] | | | | |
| **1.4.4** | Verificare che l'applicazione utilizzi un unico meccanismo di controllo accessi ben collaudato per accedere a dati e risorse protette. Tutte le richieste devono passare attraverso questo meccanismo per evitare copia e incolla o percorsi alternativi non sicuri. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 284 |
| **1.4.5** | Verificare che venga utilizzato il controllo di accesso basato su attributi o su funzionalità, in modo che il codice verifichi l'autorizzazione dell'utente per una funzionalità/elemento dati, non solo per il suo ruolo. Le autorizzazioni devono comunque essere assegnate utilizzando i ruoli. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 275 |

## V1.5 Architettura di Input e Output 

Nella versione 4.0, abbiamo abbandonato il termine "lato server" poiché ambiguo in relazione al perimetro di trust. Tuttavia, il perimetro di trust rimane un aspetto cruciale: i controlli implementati su browser o dispositivi client non affidabili possono essere facilmente aggirati. Nelle moderne architetture tradizionali, il punto di contatto con un componente trusted è cambiato radicalmente. Pertanto, nell'ASVS, il termine "livello di servizio trusted" si riferisce a qualsiasi punto di applicazione considerato affidabile, indipendentemente dalla sua posizione. Questo include microservizi, API serverless, componenti lato server, API trusted su dispositivi client con secure boot, API di partner o esterne, e altre implementazioni simili.

Il termine "client non affidabile" si riferisce, in questo contesto, alle tecnologie lato client che gestiscono la presentazione, comunemente definite tecnologie "front-end". Il termine "serializzazione" non si limita al semplice trasferimento di dati in rete sotto forma di array di valori o alla lettura di strutture JSON, ma comprende anche il passaggio di oggetti complessi che possono includere logica.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.5.1** | Verificare che i requisiti di input e output definiscano chiaramente come gestire ed elaborare i dati in base al tipo, al contenuto, alle leggi in vigore, ai regolamenti e alla conformità ad altre policy applicabili. | | ✓ | ✓ | 1029 |
| **1.5.2** | Verificare che la serializzazione non venga utilizzata nelle comunicazioni con client non affidabili. Se inevitabile, applicare controlli di integrità adeguati (e possibilmente la crittografia se vengono inviati dati sensibili) per prevenire attacchi di deserializzazione, inclusa l'injection di oggetti. | | ✓ | ✓ | 502 |
| **1.5.3** | Verificare che la convalida degli input venga applicata su un livello di servizio trusted. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 602 |
| **1.5.4** | Verificare che la codifica dell'output avvenga vicino o dall'interprete per il quale è destinata. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 116 |

## V1.6 Architettura Crittografica

Le applicazioni devono essere progettate con una solida architettura crittografica per proteggere i dati in base alla loro classificazione. Crittografare tutto indiscriminatamente è uno spreco, mentre non crittografare nulla può configurarsi come negligenza legale. È fondamentale trovare un equilibrio, generalmente durante la fase di progettazione architetturale, gli sprint di design o le analisi ad alto livello. Progettare la crittografia "al volo" o integrarla successivamente comporta costi significativamente maggiori per implementarla in modo sicuro rispetto a un'integrazione pianificata fin dall'inizio.

I requisiti architetturali riguardano l'intero sistema e sono quindi difficili da testare a livello di unità o integrazione. Questi requisiti devono essere considerati negli standard di programmazione durante tutta la fase di sviluppo e rivisti in occasione delle revisioni di sicurezza architetturale, nelle revisioni del codice (anche tra pari) o durante le retrospettive.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.6.1** | Verificare che esista una policy esplicita per la gestione delle chiavi crittografiche e che il ciclo di vita delle chiavi crittografiche segua uno standard di gestione delle chiavi come il NIST SP 800-57. | | ✓ | ✓ | 320 |
| **1.6.2** | Verificare che gli utilizzatori di servizi crittografici proteggano il materiale chiave e altri segreti utilizzando key vault o alternative basate su API. | | ✓ | ✓ | 320 |
| **1.6.3** | Verificare che tutte le chiavi e le password siano sostituibili e facciano parte di un processo ben definito per la ri-crittografia dei dati sensibili. | | ✓ | ✓ | 320 |
| **1.6.4** | Verificare che l'architettura consideri i segreti lato client, come chiavi simmetriche, password o token API, come non sicuri e non li utilizzi mai per proteggere o accedere a dati sensibili. | | ✓ | ✓ | 320 |

## V1.7 Architettura Errori, Logging e Audit

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.7.1** | Verificare che venga utilizzato un formato e un approccio di logging comune in tutto il sistema. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1009 |
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
| **1.14.5** | Verificare che le distribuzioni dell'applicazione implementino adeguatamente sandbox, containerizzazione e/o isolamento a livello di rete per rallentare e scoraggiare gli attori malevoli dall'attaccare altre applicazioni, specialmente quando eseguono azioni sensibili o pericolose come la deserializzazione. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |
| **1.14.6** | Verificare che l'applicazione non utilizzi tecnologie client-side non supportate, non sicure o obsolete come plugin NSAPI, Flash, Shockwave, ActiveX, Silverlight, NACL o applet Java client-side. | | ✓ | ✓ | 477 |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
