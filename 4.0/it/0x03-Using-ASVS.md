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

Il Livello 1 dell'ASVS è l'unico che può essere testato completamente tramite penetration test eseguiti da personale umano. Tuttavia, tutti gli altri livelli richiedono accesso a documentazione, codice sorgente, configurazioni e interazione con il team di sviluppo. Sebbene il Livello 1 permetta test "black box" (senza accesso a documentazione e codice sorgente), questo tipo di verifica non è efficace e dovrebbe essere attivamente scoraggiato. Gli attori malintenzionati hanno tutto il tempo a disposizione per condurre attacchi, mentre la maggior parte dei penetration test si conclude in poche settimane. I difensori, invece, devono non solo integrare controlli di sicurezza, ma anche individuare e risolvere tutte le vulnerabilità e rilevare e rispondere alle minacce in tempi ragionevoli. Gli attaccanti, avendo potenzialmente tempo illimitato, necessitano solo di una singola falla, debolezza o errore di rilevamento per avere successo. I test "black box", spesso eseguiti alla fine dello sviluppo, in modo affrettato o persino trascurati, sono del tutto inadeguati per gestire questa disparità temporale tra difensori e attaccanti.

Negli ultimi 30 anni, i test "black box" hanno dimostrato ripetutamente la loro inefficacia nell'individuare problemi di sicurezza critici, portando a violazioni sempre più gravi. Per questo motivo, raccomandiamo vivamente di adottare una gamma più ampia di attività di verifica e misure di garanzia della sicurezza, inclusa la sostituzione dei tradizionali penetration test con test ibridi di Livello 1. Questi dovrebbero essere guidati dall'analisi del codice sorgente, accompagnati da un dialogo aperto con gli sviluppatori e un accesso continuo alla documentazione durante tutto il processo di sviluppo. Analogamente a come gli enti di regolamentazione finanziaria non accetterebbero un audit esterno senza accesso ai libri contabili, a transazioni campione o al personale responsabile dei controlli, il settore e i governi dovrebbero richiedere lo stesso livello di trasparenza nell'ingegneria del software.

Sosteniamo fortemente l'integrazione di strumenti di sicurezza direttamente nel processo di sviluppo. Strumenti come DAST (Dynamic Application Security Testing) e SAST (Static Application Security Testing) possono essere impiegati continuamente all'interno della pipeline di build, per identificare in modo proattivo vulnerabilità facili da rilevare, che non dovrebbero mai essere presenti nelle applicazioni.

Gli strumenti automatizzati e le scansioni online non possono coprire più della metà dell'ASVS senza supporto umano. Per automatizzare completamente i test su ogni build, si utilizzano unit test e test di integrazione personalizzati, insieme a scansioni online avviate dalla build. Tuttavia, le vulnerabilità nella logica di business e i controlli sugli accessi richiedono l'intervento umano e dovrebbero essere tradotti in unit test e test di integrazione.

## Come utilizzare questo standard

Uno dei modi migliori per sfruttare lo standard di verifica della sicurezza delle applicazioni è usarlo come base per creare una checklist di sviluppo sicuro, adattata alla propria applicazione, piattaforma o organizzazione. Personalizzare l'ASVS in base ai propri casi d'uso permette di concentrarsi sui requisiti di sicurezza più rilevanti per i propri progetti e contesti operativi.

### Livello 1 - Primi passi, automatizzato o visione d'insieme del portfolio

Un'applicazione raggiunge il Livello ASVS 1 se è adeguatamente protetta contro vulnerabilità applicative facilmente individuabili, come quelle incluse nella OWASP Top 10 e in elenchi simili.

Il Livello 1 rappresenta il requisito minimo che tutte le applicazioni dovrebbero soddisfare. È utile come primo passo in un processo più ampio o per applicazioni che non gestiscono dati sensibili e quindi non richiedono i controlli più severi dei Livelli 2 o 3. I controlli di Livello 1 possono essere verificati automaticamente tramite strumenti o manualmente senza accesso al codice sorgente. Consideriamo il Livello 1 come il requisito di base per qualsiasi applicazione.

Le minacce verso le applicazioni spesso provengono da attaccanti che utilizzano tecniche semplici per individuare e sfruttare vulnerabilità facilmente rilevabili, in contrasto con attori malevoli determinati che dedicano più risorse per colpire specifiche applicazioni. Se la vostra applicazione gestisce dati di alto valore, una verifica di Livello 1 non sarà quasi mai sufficiente.

### Livello 2 - La maggior parte delle applicazioni

Un'applicazione raggiunge il Livello ASVS 2 (o Standard) se è in grado di difendersi adeguatamente dalla maggior parte dei rischi associati al software moderno.

Il Livello 2 assicura che i controlli di sicurezza siano implementati, funzionino correttamente e siano utilizzati in modo efficace all'interno dell'applicazione. È generalmente indicato per applicazioni che gestiscono transazioni business-to-business significative, come quelle che trattano informazioni sanitarie, svolgono funzioni aziendali critiche o sensibili, o elaborano altre risorse sensibili. È anche essenziale in settori dove l'integrità è cruciale, come l'industria dei videogiochi, per contrastare imbroglioni e attacchi hacker.

Le minacce a cui si espongono le applicazioni di Livello 2 provengono solitamente da attaccanti qualificati e motivati, che si concentrano su obiettivi specifici utilizzando strumenti e tecniche avanzate per scoprire e sfruttare le debolezze delle applicazioni.

### Livello 3 - Alto valore, alta affidabilità o alta sicurezza

Il Livello ASVS 3 rappresenta il livello più elevato di verifica della sicurezza all'interno dell'ASVS. È generalmente riservato a quelle applicazioni che richiedono un grado significativo di protezione, come nei settori della difesa, sanità, sicurezza e infrastrutture critiche.

Le organizzazioni possono richiedere il Livello ASVS 3 per applicazioni che svolgono funzioni critiche, dove un fallimento potrebbe avere conseguenze gravi sulle operazioni o persino sulla sopravvivenza dell'azienda. Un'applicazione raggiunge il Livello ASVS 3 (o Avanzato) se non solo si difende adeguatamente da vulnerabilità avanzate, ma dimostra anche i principi di una progettazione di sicurezza solida.

Le applicazioni di Livello ASVS 3 richiedono un'analisi più approfondita dell'architettura, del codice e dei test rispetto agli altri livelli. Un'applicazione sicura a questo livello è modularizzata in modo sensato per garantire resilienza, scalabilità e sicurezza. Ogni modulo, separato da una connessione di rete o un'istanza fisica, gestisce autonomamente le proprie responsabilità di sicurezza, implementando una difesa in profondità. Queste responsabilità devono essere documentate e includere controlli per la riservatezza (come crittografia), l'integrità (transazioni, convalida degli input), la disponibilità (gestione efficiente del carico), l'autenticazione (anche tra sistemi), l'autorizzazione e l'auditing (logging).

## Applicazione pratica dell'ASVS

Gli attaccanti possono avere motivazioni diverse e alcuni settori possiedono asset informatici e informativi unici, con requisiti normativi specifici del proprio dominio.

Si raccomanda vivamente alle organizzazioni di valutare attentamente le loro specifiche caratteristiche di rischio in base alla natura del loro business e, in funzione di tali rischi e delle esigenze aziendali, determinare il livello ASVS più appropriato per garantire la sicurezza delle applicazioni.

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
