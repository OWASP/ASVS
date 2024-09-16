# Valutazione e certificazione

## La posizione di OWASP sulle certificazioni e i marchi di fiducia ASVS

OWASP, in quanto organizzazione no profit indipendente dai fornitori, attualmente non certifica alcun fornitore, ente verificatore o software.

Pertanto, tutte le dichiarazioni di garanzia, i marchi di fiducia o le certificazioni di questo tipo non sono ufficialmente esaminate, registrate o certificate da OWASP. Le organizzazioni che si affidano a tali elementi devono essere caute nel riporre fiducia in terze parti o marchi che dichiarano la certificazione ASVS.

Ciò non impedisce alle organizzazioni di offrire servizi di garanzia, purché non rivendichino ufficialmente una certificazione OWASP.

## Linee guida per gli organismi di certificazione

Lo standard di verifica della sicurezza delle applicazioni può essere utilizzato come una verifica "open book", con accesso completo e senza restrizioni a risorse chiave, quali architetti del software e sviluppatori, documentazione di progetto, codice sorgente, e accesso autenticato ai sistemi di test (incluso l'accesso a uno o più account per ogni ruolo). Questo approccio è particolarmente importante per le verifiche di Livello 2 e Livello 3.

Storicamente, i penetration test e le revisioni del codice sicuro hanno incluso solo problematiche "per eccezione", ovvero solo i test falliti vengono riportati nel rapporto finale. Tuttavia, un organismo di certificazione deve includere nel rapporto l'intero ambito della verifica (soprattutto se un componente chiave, come l'autenticazione SSO, è fuori ambito), un riepilogo dei risultati, compresi i test superati e non, con indicazioni chiare su come risolvere eventuali test falliti.

Alcuni requisiti di verifica potrebbero non essere applicabili all'applicazione sotto test. Ad esempio, se si offre ai clienti un'API stateless a livello di servizio, senza una componente client, molti dei requisiti della sezione V3 (Gestione sessioni) non si applicheranno direttamente. In questi casi, un organismo di certificazione può comunque dichiarare la piena conformità ASVS, a patto che venga fornita una chiara motivazione per l'esclusione di tali requisiti nel rapporto finale.

La conservazione di rapporti di lavoro dettagliati, screenshot o filmati, script per riprodurre un problema in modo affidabile e log elettronici dei test (come i log di proxy e note di cleanup) è considerata una prassi standard nel settore. Questi elementi sono fondamentali per fornire prove solide dei risultati, soprattutto di fronte a sviluppatori scettici. Non è sufficiente eseguire uno strumento e segnalare semplicemente i fallimenti: questo non dimostra che tutti i problemi siano stati effettivamente testati in modo approfondito. In caso di controversia, devono esserci prove sufficienti per garantire che ogni singolo requisito sia stato effettivamente verificato.

### Metodi di valutazione

Gli organismi di certificazione sono liberi di scegliere i metodi di valutazione più appropriati, ma devono documentarli in modo trasparente.

A seconda dell'applicazione sottoposta a test e dei requisiti di verifica, possono essere utilizzati vari metodi per garantire un'adeguata affidabilità dei risultati. Ad esempio, la convalida dell'efficacia dei meccanismi di verifica dell'input di un'applicazione può essere eseguita attraverso un penetration test manuale o tramite un'analisi del codice sorgente.

#### Ruolo degli strumenti di test di sicurezza automatizzati

Si incoraggia l'uso di strumenti di penetration testing automatizzati per garantire la copertura più ampia possibile.

Tuttavia, non è possibile completare interamente la verifica ASVS solo con strumenti automatizzati. Sebbene molti dei requisiti del Livello 1 possano essere soddisfatti tramite test automatizzati, gran parte dei requisiti non è adatta a essere verificata esclusivamente con penetration test automatizzati.

Va inoltre considerato che la distinzione tra test automatizzati e manuali si è ridotta con l'evoluzione del settore della sicurezza delle applicazioni. Gli strumenti automatizzati vengono spesso calibrati da esperti, mentre i tester manuali sfruttano una varietà di strumenti automatizzati per migliorare l'efficacia delle loro analisi.

#### Ruolo del Penetration Testing

Nella versione 4.0, abbiamo deciso di rendere il Livello ASVS 1 completamente testabile tramite penetration testing, senza necessità di accedere a codice sorgente, documentazione o sviluppatori. Tuttavia, per soddisfare i requisiti di logging dell'OWASP Top 10 2017 A10, saranno necessarie interviste, screenshot o altre prove, come indicato anche nell'OWASP Top 10 2017. Nonostante ciò, condurre test senza l'accesso alle informazioni essenziali non è il metodo ideale per una verifica della sicurezza completa, poiché non permette di esaminare il codice sorgente per identificare minacce e controlli mancanti, limitando così la profondità dell'analisi.

Per le valutazioni di Livello 2 o 3, è preferibile avere accesso a sviluppatori, documentazione, codice sorgente e a un ambiente di test con dati non di produzione. Il penetration testing a questi livelli richiede questo tipo di accesso, definito "revisioni ibride" o "penetration test ibridi", per eseguire un'analisi più approfondita e accurata.

## Altri utilizzi del ASVS

L'ASVS non è solo utile per valutare la sicurezza di un'applicazione, ma ha anche diversi altri potenziali impieghi.

### Come guida completa per l'architettura della sicurezza

Uno degli utilizzi più comuni dell'Application Security Verification Standard (ASVS) è come risorsa per gli architetti della sicurezza. Lo Sherwood Applied Business Security Architecture (SABSA) non fornisce molte delle informazioni necessarie per una revisione completa dell'architettura di sicurezza delle applicazioni. L'ASVS può colmare queste lacune, aiutando gli architetti della sicurezza a selezionare controlli più efficaci per affrontare problemi comuni, come i modelli di protezione dei dati e le strategie di convalida degli input.

### Come alternativa agli elenchi di controllo predefiniti per la codifica sicura

Molte organizzazioni possono beneficiare dell'adozione del ASVS, scegliendo uno dei tre livelli o modificandolo per adattare i requisiti a ciascun livello di rischio specifico per il proprio dominio. Incoraggiamo questo tipo di personalizzazione, a condizione che venga mantenuta la tracciabilità. In questo modo, se un'applicazione soddisfa il requisito 4.1, il risultato sarà coerente anche nelle versioni modificate rispetto allo standard originale, man mano che evolve.

### Come guida per unit test e test di integrazione automatizzati

L'ASVS è progettato per essere altamente testabile, ad eccezione dei requisiti relativi all'architettura e al codice malevolo. Creando unit test e test di integrazione che includono fuzzing e scenari malevoli specifici e pertinenti, l'applicazione può diventare quasi auto-verificante a ogni build. Ad esempio, è possibile ampliare la suite di test di un controller di login, verificando il parametro *username* per nomi utente predefiniti comuni, enumerazione degli account, attacchi brute force, injection LDAP, SQL e XSS. Allo stesso modo, i test per il parametro *password* dovrebbero coprire password comuni, lunghezza minima, injection di byte null, rimozione completa del parametro, XSS e altre vulnerabilità.

### Per la formazione allo sviluppo sicuro

L'ASVS può essere utilizzato anche per definire le caratteristiche di un software sicuro. Molti corsi di "programmazione sicura" tendono a concentrarsi principalmente su tecniche di hacking etico, offrendo solo alcuni suggerimenti di programmazione, il che potrebbe non essere sufficiente per aiutare gli sviluppatori a scrivere codice più sicuro. Invece, i corsi di sviluppo sicuro possono basarsi sull'ASVS, ponendo maggiore enfasi sui controlli proattivi descritti nello standard, piuttosto che focalizzarsi solo sui 10 principali rischi da evitare. Questo approccio fornisce agli sviluppatori una guida pratica e concreta per costruire applicazioni sicure fin dall'inizio.

### Come catalizzatore per la sicurezza agile delle applicazioni

L'ASVS può essere utilizzato in un processo di sviluppo agile come framework per definire attività specifiche necessarie a garantire un prodotto sicuro. Un approccio potrebbe consistere nel partire dal Livello 1, verificando l'applicazione o il sistema rispetto ai requisiti ASVS per il livello selezionato, individuando i controlli mancanti e creando ticket o attività specifiche nel backlog. Questo aiuta a dare priorità alle attività di sicurezza (o grooming) e rende la sicurezza una parte visibile e integrata del processo agile. L'ASVS può anche essere utilizzato per dare priorità ad attività di audit e revisione, dove un requisito specifico guida la revisione, il refactoring o l'audit da parte di un membro del team, e viene trattato come "debito" nel backlog, che dovrà essere risolto nel tempo.

### Come framework per orientare l'approvvigionamento di software sicuro

L'ASVS è un ottimo framework per facilitare l'approvvigionamento di software sicuro o servizi di sviluppo personalizzati. L'acquirente può specificare come requisito che il software da acquistare sia sviluppato in conformità al Livello ASVS X, e richiedere al venditore di dimostrare che il software soddisfa tale livello. Questo approccio è particolarmente efficace se combinato con l'Allegato Contrattuale per Software Sicuro OWASP, garantendo che le aspettative di sicurezza siano chiaramente definite e concordate contrattualmente.
