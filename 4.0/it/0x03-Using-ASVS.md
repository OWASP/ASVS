# Utilizzo del ASVS

ASVS ha due obiettivi principali:

* aiutare le organizzazioni a sviluppare e mantenere applicazioni sicure.
* consentire ai fornitori di servizi di sicurezza, ai fornitori di strumenti di sicurezza e ai consumatori di allineare i propri requisiti e le loro offerte.

## Livelli di verifica della sicurezza delle applicazioni

Lo standard di verifica della sicurezza delle applicazioni (ASVS) definisce tre livelli di verifica della sicurezza, ciascuno con un livello di approfondimento crescente.

* ASVS Livello 1 è pensato per bassi livelli di garanzie di sicurezza ed è completamente testabile tramite penetration test.
* ASVS Levello 2 è adatto per applicazioni che contengono dati sensibili che richiedono protezione, ed è il livello raccomandato per la maggior parte delle applicazioni.
* ASVS Levello 3 è riservato alle applicazioni più critiche, come quelle che eseguono transazioni di alto valore, contengono dati medici sensibili o qualsiasi applicazione che richieda il massimo livello di sicurezza.

Ciascun livello ASVS contiene un elenco di requisiti di sicurezza. Ognuno di questi requisiti può essere mappato anche su funzionalità e capacità specifiche per la sicurezza che devono essere integrate nel software dagli sviluppatori.

![ASVS Levels](https://raw.githubusercontent.com/OWASP/ASVS/master/4.0/images/asvs_40_levels.png "ASVS Levels")

Figura 1 - Livelli dell'OWASP Application Security Verification Standard 4.0 

Il Livello 1 del ASVS è l'unico che può essere testato completamente tramite penetration test eseguiti da personale umano. Tuttavia, tutti gli altri livelli richiedono accesso a documentazione, codice sorgente, configurazioni e interazione con il team di sviluppo. Sebbene il Livello 1 permetta test "black box" (senza accesso a documentazione e codice sorgente), questo tipo di verifica non è efficace e dovrebbe essere attivamente scoraggiato. Gli attori malintenzionati hanno tutto il tempo a disposizione per condurre attacchi, mentre la maggior parte dei penetration test si conclude in poche settimane. I difensori, invece, devono non solo integrare controlli di sicurezza, ma anche individuare e risolvere tutte le vulnerabilità e rilevare e rispondere alle minacce in tempi ragionevoli. Gli attaccanti, avendo potenzialmente tempo illimitato, necessitano solo di una singola falla, debolezza o errore di rilevamento per avere successo. I test "black box", spesso eseguiti alla fine dello sviluppo, in modo affrettato o persino trascurati, sono del tutto inadeguati per gestire questa disparità temporale tra difensori e attaccanti.

Negli ultimi 30 anni, i test "black box" hanno dimostrato ripetutamente la loro inefficacia nell'individuare problemi di sicurezza critici, portando a violazioni sempre più gravi. Per questo motivo, raccomandiamo vivamente di adottare una gamma più ampia di attività di verifica e misure di garanzia della sicurezza, inclusa la sostituzione dei tradizionali penetration test con test ibridi di Livello 1. Questi dovrebbero essere guidati dall'analisi del codice sorgente, accompagnati da un dialogo aperto con gli sviluppatori e un accesso continuo alla documentazione durante tutto il processo di sviluppo. Analogamente a come gli enti di regolamentazione finanziaria non accetterebbero un audit esterno senza accesso ai libri contabili, a transazioni campione o al personale responsabile dei controlli, il settore e i governi dovrebbero richiedere lo stesso livello di trasparenza nell'ingegneria del software.

Sosteniamo fortemente l'integrazione di strumenti di sicurezza direttamente nel processo di sviluppo. Strumenti come DAST (Dynamic Application Security Testing) e SAST (Static Application Security Testing) possono essere impiegati continuamente all'interno della pipeline di build, per identificare in modo proattivo vulnerabilità facili da rilevare, che non dovrebbero mai essere presenti nelle applicazioni.

Gli strumenti automatizzati e le scansioni online non possono coprire più della metà del ASVS senza supporto umano. Per automatizzare completamente i test su ogni build, si utilizzano unit test e test di integrazione personalizzati, insieme a scansioni online avviate dalla build. Tuttavia, le vulnerabilità nella logica di business e i controlli sugli accessi richiedono l'intervento umano e dovrebbero essere tradotti in unit test e test di integrazione.

## Come utilizzare questo standard

Uno dei modi migliori per sfruttare lo standard di verifica della sicurezza delle applicazioni è usarlo come base per creare una checklist di sviluppo sicuro, adattata alla propria applicazione, piattaforma o organizzazione. Personalizzare l'ASVS in base ai propri casi d'uso permette di concentrarsi sui requisiti di sicurezza più rilevanti per i propri progetti e contesti operativi.

### Livello 1 - Primi passi, automatizzato o visione d'insieme del portfolio

Un'applicazione raggiunge il Livello ASVS 1 se è sufficientemente protetta contro vulnerabilità applicative facilmente individuabili, come quelle presenti nella OWASP Top 10 o in elenchi simili.

Il Livello 1 rappresenta il requisito minimo che tutte le applicazioni dovrebbero soddisfare. È utile come punto di partenza in un percorso di sicurezza più ampio o per applicazioni che non trattano dati sensibili e non richiedono i controlli più rigorosi previsti dai Livelli 2 o 3. I controlli di Livello 1 possono essere verificati automaticamente tramite strumenti o manualmente senza accesso al codice sorgente. Consideriamo il Livello 1 come la soglia di sicurezza di base per qualsiasi applicazione.

Le minacce alle applicazioni spesso provengono da attaccanti che utilizzano tecniche semplici per identificare e sfruttare vulnerabilità facilmente rilevabili, a differenza di attori malevoli più determinati che impiegano risorse significative per colpire applicazioni specifiche. Se la vostra applicazione gestisce dati di alto valore, una verifica di Livello 1 non sarà quasi mai sufficiente.

### Livello 2 - La maggior parte delle applicazioni

Un'applicazione raggiunge il Livello ASVS 2 (o Standard) se è in grado di proteggersi adeguatamente dalla maggior parte dei rischi associati al software moderno.

Il Livello 2 garantisce che i controlli di sicurezza siano implementati correttamente, funzionino in modo efficace e siano applicati in maniera appropriata all'interno dell'applicazione. È generalmente raccomandato per applicazioni che gestiscono transazioni business-to-business rilevanti, come quelle che trattano informazioni sanitarie, svolgono funzioni aziendali critiche o sensibili, o elaborano altre risorse sensibili. È anche fondamentale in settori dove l'integrità è essenziale, come l'industria dei videogiochi, per contrastare truffatori e attacchi hacker.

Le minacce per le applicazioni di Livello 2 provengono tipicamente da attaccanti qualificati e motivati, che mirano a obiettivi specifici utilizzando strumenti e tecniche avanzate per individuare e sfruttare le vulnerabilità delle applicazioni.

### Livello 3 - Alto valore, alta affidabilità o alta sicurezza

Il Livello ASVS 3 rappresenta il più alto standard di verifica della sicurezza nell'ASVS, ed è generalmente destinato ad applicazioni che richiedono un livello significativo di protezione, come quelle dei settori della difesa, della sanità, della sicurezza e delle infrastrutture critiche.

Le organizzazioni possono adottare il Livello ASVS 3 per applicazioni che eseguono funzioni critiche, dove un eventuale fallimento potrebbe avere gravi conseguenze operative o compromettere persino la sopravvivenza dell'azienda. Un'applicazione raggiunge il Livello ASVS 3 (o Avanzato) se non solo protegge da vulnerabilità avanzate, ma dimostra anche una progettazione di sicurezza robusta e ben strutturata.

Le applicazioni di Livello ASVS 3 richiedono un'analisi più dettagliata dell'architettura, del codice e dei test rispetto ai livelli inferiori. Un'applicazione sicura a questo livello è organizzata in moduli distinti, in modo da garantire resilienza, scalabilità e sicurezza. Ogni modulo, isolato tramite connessioni di rete o istanze fisiche, è responsabile della propria sicurezza, implementando una difesa stratificata. Queste responsabilità devono essere ben documentate e includere controlli per la riservatezza (ad esempio, crittografia), l'integrità (come la gestione delle transazioni e la validazione degli input), la disponibilità (ottimizzazione della gestione del carico), l'autenticazione (anche tra sistemi), l'autorizzazione e l'auditing (logging).

## Applicazione pratica del ASVS

Gli attaccanti possono avere motivazioni diverse e alcuni settori dispongono di asset informatici e informativi unici, con requisiti normativi specifici.

Si raccomanda vivamente alle organizzazioni di valutare con attenzione le proprie caratteristiche di rischio in base alla natura del business e, in funzione di tali rischi e delle esigenze aziendali, determinare il livello ASVS più adatto per garantire la sicurezza delle applicazioni.

## Come fare riferimento ai requisiti ASVS

Ciascun requisito dispone di un identificatore in formato `<capitolo>.<sezione>.<requisito>` dove ogni elemento è un numero, per esempio: `1.11.3`.
- Il valore `<capitolo>` corrisponde al capitolo da cui proviene il requisito, per esempio: tutti i requisiti `1.#.#` appartengono al capitolo `Architettura`.
- Il valore `<sezione>` corrisponde alla sezione all'interno di quel capitolo in cui compare il requisito, per esempio: tutti i requisiti, `1.11.#` si trovano nella sezione `Architettura logica di business` del capitolo `Architettura`.
- Il valore `<requisito>` identifica il requisito specifico all'interno del capitolo e della sezione, per esempio: `1.11.3` che, nella versione 4.0.3 di questo standard è:

> Verificare che tutti i flussi logici di business di alto valore, inclusi autenticazione, gestione delle sessioni e controllo degli accessi, siano thread-safe e resistenti alle race conditions quali time-of-check e time-of-use.

Gli identificatori possono cambiare tra le versioni dello standard, pertanto è preferibile che altri documenti, rapporti o strumenti utilizzino il formato `v<version>-<chapter>.<section>.<requirement>`, dove 'versione'è l'etichetta della versione ASVS. Per esempio: `v4.0.3-1.11.3` indicherebbe specificatamente il 3° requisito nella sezione 'Architettura logica di business' del capitolo 'Architettura' della versione 4.0.3. (Questo può essere riassunto come `v<version>-<requirement_identifier>`.)

Nota: la `v` che precede la parte relativa alla versione deve essere minuscola.

Se gli identificatori vengono usati senza includere l'elemento `v<version>` si presuppone che facciano riferimento al contenuto più recente dello standard ASVS. Ovviamente, man mano che lo standard cresce e cambia, ciò diventa problematico. Ecco perché gli autori o gli sviluppatori dovrebbero sempre includere l'elemento versione.

Gli elenchi dei requisiti ASVS sono disponibili in CSV, JSON e altri formati che possono essere utili per riferimento o uso programmatico.
