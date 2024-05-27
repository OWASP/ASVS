# Valutazione e certificazione

## La posizione di OWASP sulle certificazioni e i marchi di fiducia ASVS

OWASP, in qualità di organizzazione no profit indipendente dai fornitori, attualmente non certifica alcun fornitore, ente verificatore o software.

Tutte le affermazioni di garanzia, i marchi di fiducia o le certificazioni di questo tipo non sono ufficialmente esaminati, registrati o certificati da OWASP. Pertanto, un'organizzazione che si affida a tali elementi deve essere cauta riguardo alla fiducia riposta in qualsiasi terza parte o marchio di fiducia che dichiari la certificazione ASVS.

Questo non dovrebbe impedire alle organizzazioni di offrire tali servizi di garanzia, a condizione che non rivendichino una certificazione OWASP ufficiale.

## Linee guida per gli organismi di certificazione

Lo standard di verifica della sicurezza delle applicazioni può essere utilizzato come verifica open book dell'applicazione, incluso l'accesso aperto e senza restrizioni a risorse chiave quali architetti del software e sviluppatori, documentazione di progetto, codice sorgente, accesso autenticato ai sistemi di test (incluso l'accesso a uno o più account per ogni ruolo), in particolare per le verifiche L2 e L3.

Storicamente, i penetration test e le revisioni del codice sicuro hanno incluso problematiche "per eccezione", ovvero solo i test falliti compaiono nel rapporto finale. Un organismo di certificazione deve includere in qualsiasi rapporto l'ambito della verifica (in particolare se un componente chiave è fuori dall'ambito, come l'autenticazione SSO), un riepilogo dei risultati della verifica, inclusi i test superati e non superati, con chiare indicazioni su come risolvere quelli non superati.

Alcuni requisiti di verifica potrebbero non essere applicabili all'applicazione sotto test. Ad esempio, se si fornisce ai clienti un'API del livello di servizio stateless e senza implementazione client, molti dei requisiti in V3 in Gestione sessione non sono direttamente applicabili. In tali casi, un organismo di certificazione può comunque dichiarare la piena conformità ASVS, ma deve indicare chiaramente in qualsiasi rapporto una motivazione per la non applicabilità di tali requisiti di verifica esclusi.

Conservare rapporti di lavoro dettagliati, screenshot o filmati, script per sfruttare in modo affidabile e ripetuto un problema e registrazioni elettroniche dei test, come il log di un proxy e note associate come un elenco di cleanup, è considerata una prassi standard del settore e può essere davvero utile come prova dei risultati per gli sviluppatori più scettici. Non è sufficiente eseguire semplicemente uno strumento e segnalare i fallimenti; questo non fornisce affatto prove sufficienti che tutti i problemi a un livello di certificazione siano stati testati e testati a fondo. In caso di controversia, dovrebbero esserci sufficienti elementi di prova a garanzia che ogni singolo requisito verificato sia stato effettivamente testato.

### Metodi di valutazione

Gli organismi di certificazione sono liberi di scegliere i metodi di valutazione più appropriati, ma devono indicarli in un documento.

A seconda dell'applicazione sottoposta a test e del requisito di verifica, possono essere utilizzati diversi metodi di valutazione per ottenere una garanzia adeguata dei risultati. Ad esempio, la convalida dell'efficacia dei meccanismi di verifica dell'input di un'applicazione può essere analizzata con un penetration test manuale o mediante analisi del codice sorgente.

#### Ruolo degli strumenti di test di sicurezza automatizzati

Si incoraggia l'uso di strumenti di penetration testing automatizzati per fornire la copertura più ampia possibile.

Non è possibile completare nella sua interezza la verifica ASVS utilizzando solo strumenti di penetration testing automatizzati. Sebbene una grande maggioranza dei requisiti in L1 possa essere eseguita utilizzando test automatizzati, la maggior parte dei requisiti non è adatta a test di penetration testing automatizzati.

Si noti che la linea di demarcazione tra test automatizzati e manuali è ormai meno marcata con la maturazione del settore della sicurezza delle applicazioni. Gli strumenti automatizzati sono spesso calibrati manualmente da esperti e i tester manuali spesso sfruttano una vasta gamma di strumenti automatizzati.

#### Ruolo del Penetration Testing

Nella versione 4.0, abbiamo deciso di rendere il Livello ASVS 1 completamente testabile tramite penetration testing senza accesso a codice sorgente, documentazione o sviluppatori. Due elementi di logging, necessari per soddisfare l'OWASP Top 10 2017 A10, richiederanno interviste, screenshot o altre raccolte di prove, proprio come fanno nell'OWASP Top 10 2017. Tuttavia, testare senza accesso alle informazioni necessarie non è il metodo ideale per la verifica della sicurezza, in quanto non si esamina il codice sorgente, per identificare le minacce e i controlli mancanti, ed eseguire un test molto più approfondito in un lasso di tempo minore.

Se possibile, l'accesso a sviluppatori, documentazione, codice e accesso a un'applicazione di test con dati non di produzione è necessario quando si esegue una valutazione di Livello 2 o 3. Il penetration testing eseguito a questi livelli richiede questo livello di accesso, che chiamiamo "revisioni ibride" o "penetration test ibridi".

## Altri utilizzi per la ASVS

L'ASVS non è solo utile per valutare la sicurezza di un'applicazione, ma ha anche diversi altri potenziali impieghi.

### Come guida dettagliata per l'architettura della sicurezza

Uno degli usi più comuni del'Application Security Verification Standard è come risorsa per gli architetti della sicurezza. Lo Sherwood Applied Business Security Architecture (SABSA) manca di molte informazioni necessarie per completare una revisione completa dell'architettura della sicurezza delle applicazioni. L'ASVS può essere utilizzato per colmare queste lacune consentendo agli architetti della sicurezza di scegliere controlli migliori per i problemi comuni, come modelli di protezione dei dati e strategie di convalida degli input.

### Come sostituto degli elenchi di controllo predefiniti per la codifica sicura

Molte organizzazioni possono trarre vantaggio dall'adozione dell'ASVS, scegliendo uno dei tre livelli o modificando l'ASVS e cambiando ciò che è richiesto per ciascun livello di rischio dell'applicazione in modo specifico per il dominio. Incoraggiamo questo tipo di modifica a condizione che venga mantenuta la tracciabilità, in modo che se un'app ha superato il requisito 4.1, ciò significhi lo stesso per le copie modificate rispetto allo standard man mano che evolve.

### Come guida per unit test e test di integrazione automatizzati

L'ASVS è progettato per essere altamente testabile, con la sola eccezione dei requisiti architetturali e del codice malevolo. Creando unit test e test di integrazione che testano con fuzzing, abuse case specifici e pertinenti, l'applicazione diventa quasi auto-verificante con ogni singola build. Ad esempio, è possibile creare test aggiuntivi per la suite di test di un controller di login, testando il parametro username per nomi utente predefiniti comuni, enumerazione degli account, attacchi brute force, iniezione LDAP e SQL e XSS. Allo stesso modo, un test sul parametro password dovrebbe includere password comuni, lunghezza della password, iniezione di byte null, rimozione completa del parametro, XSS e altro ancora.

### Per la formazione allo sviluppo sicuro

L'ASVS può essere utilizzato anche per definire le caratteristiche di un software sicuro. Molti corsi di "programmazione sicura" sono semplicemente corsi di hacking etico con un leggero accenno a suggerimenti di programmazione. Ciò potrebbe non aiutare necessariamente gli sviluppatori a scrivere codice più sicuro. Al contrario, i corsi di sviluppo sicuro possono utilizzare l'ASVS con una forte attenzione sui controlli proattivi presenti nell'ASVS, piuttosto che sui 10 principali aspetti negativi da evitare.

### Come motore per la sicurezza delle applicazioni agili

L'ASVS può essere utilizzato in un processo di sviluppo agile come framework per definire attività specifiche che devono essere implementate dal team per avere un prodotto sicuro. Un approccio potrebbe essere: a partire dal Livello 1, verificare l'applicazione o il sistema specifico in base ai requisiti ASVS per il livello specificato, individuare quali controlli mancano e aprire ticket/attività specifici nel backlog. Ciò aiuta a stabilire le priorità per attività specifiche (o grooming) e rende la sicurezza visibile nel processo agile. Può anche essere utilizzato per dare priorità alle attività di auditing e revisione nell'organizzazione, dove un requisito ASVS specifico può guidare la revisione, il refactoring o l'audit per un membro specifico del team e visibile come "debito" nel backlog che deve essere eventualmente sanato.

### Come framework per orientare l'approvvigionamento di software sicuro

L'ASVS è un ottimo framework per aiutare con l'approvvigionamento di software sicuro o l'approvvigionamento di servizi di sviluppo personalizzati. L'acquirente può semplicemente stabilire un requisito secondo cui il software che desidera acquistare deve essere sviluppato a livello ASVS X e richiedere che il venditore dimostri che il software soddisfa il livello ASVS X. Questo funziona bene se combinato con l'Allegato Contrattuale per Software Sicuro OWASP.
