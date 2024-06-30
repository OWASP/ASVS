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

Il Livello 1 è l'unico completamente testabile tramite penetration test con personale umano. Tutti gli altri livelli richiedono l'accesso a documentazione, codice sorgente, configurazione e alle persone coinvolte nel processo di sviluppo. Tuttavia, anche se il Livello 1 consente test "black box" (senza documentazione e codice sorgente), non è un'attività di verifica efficace e dovrebbe essere scoraggiata attivamente. Gli attori malintenzionati hanno molto tempo a disposizione, mentre la maggior parte dei penetration test si concludono in un paio di settimane. I difensori devono integrare controlli di sicurezza, proteggere, trovare e risolvere tutte le debolezze e rilevare e rispondere agli attori malintenzionati in un lasso di tempo ragionevole. Gli attaccanti hanno a disposizione un tempo potenzialmente infinito e necessitano solo di una singola falla nella difesa, una singola debolezza o un rilevamento mancante per avere successo. I test "black box", spesso eseguiti alla fine dello sviluppo, in modo rapido o addirittura non svolti, sono completamente inadeguati a far fronte a tale asimmetria.

Negli ultimi 30 anni, i test "black box" hanno dimostrato più volte di non essere in grado di individuare problemi di sicurezza critici che hanno portato direttamente a violazioni sempre più massicce. Raccomandiamo vivamente l'utilizzo di una vasta gamma di attività di verifica e garanzie di sicurezza, inclusa la sostituzione dei penetration test con penetration test ibridi di Livello 1 guidati dal codice sorgente, con dialogo aperto verso gli sviluppatori e accesso alla documentazione durante l'intero processo di sviluppo. Gli enti di regolamentazione finanziaria non tollerano audit finanziari esterni senza accesso ai libri contabili, a transazioni campione o alle persone che eseguono i controlli. Il settore e i governi devono richiedere lo stesso standard di trasparenza nel campo dell'ingegneria del software.

Promuoviamo vivamente l'utilizzo di strumenti di sicurezza all'interno del processo di sviluppo stesso. Gli strumenti DAST e SAST possono essere utilizzati continuamente dalla pipeline di build per individuare problemi di sicurezza facili da identificare che non dovrebbero mai essere presenti.

Strumenti automatizzati e scansioni online non sono in grado di completare più della metà dell'ASVS senza l'assistenza umana. Se è necessaria un'automazione completa dei test per ogni build, viene utilizzata una combinazione di unit test e test di integrazione personalizzati, insieme a scansioni online avviate dalla build. Le falle nella logica di business e i test relativi al controllo degli accessi sono possibili solo con l'assistenza umana. Questi dovrebbero essere trasformati in unit test e test di integrazione.

## Come utilizzare questo standard

Uno dei modi migliori per utilizzare lo standard di verifica della sicurezza delle applicazioni è utilizzarlo come modello per creare una checklist di sviluppo sicuro specifica per la propria applicazione, piattaforma o organizzazione. Adattare l'ASVS ai propri casi d'uso aumenterà l'attenzione sui requisiti di sicurezza più importanti per i propri progetti e ambienti.

### Livello 1 - Primi passi, automatizzato o visione d'insieme del portfolio

Un'applicazione raggiunge il Livello ASVS 1 se si difende adeguatamente dalle vulnerabilità di sicurezza applicative facili da scoprire e incluse nella OWASP Top 10 e in altri elenchi simili.

Il Livello 1 rappresenta il minimo indispensabile che tutte le applicazioni dovrebbero ottenere. È utile anche come primo passo in un processo multifase o quando le applicazioni non memorizzano o gestiscono dati sensibili e quindi non necessitano dei controlli più rigorosi del Livello 2 o 3. I controlli di Livello 1 possono essere verificati automaticamente dagli strumenti oppure manualmente senza accesso al codice sorgente. Consideriamo il Livello 1 il minimo richiesto per tutte le applicazioni.

Le minacce verso le applicazioni provengono principalmente da attaccanti che utilizzano tecniche semplici e richiedono poco sforzo per identificare vulnerabilità facili da trovare e sfruttare. Questo è in netto contrasto con un attore malevolo determinato che dedicherà energia mirata per colpire specificamente un'applicazione. Se i dati elaborati dalla vostra applicazione hanno un valore elevato, raramente vi accontenterete di una verifica di Livello 1.

### Livello 2 - La maggior parte delle applicazioni

Un'applicazione raggiunge il Livello ASVS 2 (o Standard) se si difende adeguatamente dalla maggior parte dei rischi associati al software odierno.

Il Livello 2 garantisce che i controlli di sicurezza siano implementati, efficaci e utilizzati all'interno dell'applicazione. Il Livello 2 è in genere appropriato per le applicazioni che gestiscono transazioni business-to-business significative, comprese quelle che elaborano informazioni sanitarie, implementano funzioni aziendali critiche o sensibili, o elaborano altre risorse sensibili, o per settori in cui l'integrità è un aspetto fondamentale per proteggere il proprio business, come l'industria dei videogiochi per contrastare imbroglioni e hack.

Le minacce alle applicazioni di Livello 2 saranno in genere attaccanti qualificati e motivati che si concentrano su obiettivi specifici utilizzando strumenti e tecniche altamente pratiche ed efficaci per scoprire e sfruttare le debolezze all'interno delle applicazioni.

### Livello 3 - Alto valore, alta affidabilità o alta sicurezza

Il Livello ASVS 3 è il livello più alto di verifica all'interno dell'ASVS. Questo livello è in genere riservato alle applicazioni che richiedono livelli significativi di verifica della sicurezza, come quelle che si possono trovare in settori come la difesa, la sanità e la sicurezza, le infrastrutture critiche, ecc.

Le organizzazioni possono richiedere l'ASVS Livello 3 per applicazioni che svolgono funzioni critiche, dove un guasto potrebbe avere un impatto significativo sulle operazioni dell'organizzazione e persino sulla sua sopravvivenza. Di seguito vengono fornite alcune linee guida sull'applicazione dell'ASVS Livello 3. Un'applicazione raggiunge il Livello ASVS 3 (o Avanzato) se si difende adeguatamente dalle vulnerabilità di sicurezza applicative avanzate e dimostra inoltre i principi di una buona progettazione della sicurezza.

Un'applicazione di Livello ASVS 3 richiede un'analisi più approfondita dell'architettura, della codifica e dei test rispetto a tutti gli altri livelli. Un'applicazione sicura è modularizzata in modo sensato (per facilitare la resilienza, la scalabilità e, soprattutto, i livelli di sicurezza), e ogni modulo (separato da connessione di rete e/o istanza fisica) si occupa delle proprie responsabilità di sicurezza (difesa in profondità), che devono essere adeguatamente documentate. Le responsabilità includono controlli per garantire la riservatezza (ad esempio crittografia), l'integrità (ad esempio transazioni, convalida degli input), la disponibilità (ad esempio gestione del carico in modo efficiente), l'autenticazione (anche tra sistemi), l'autorizzazione e la l'auditing (logging).

## Applicazione pratica dell'ASVS

Gli attaccanti hanno motivazioni diverse. Alcuni settori possiedono asset informatici e informativi unici, con requisiti normativi specifici del dominio.

Si incoraggiano vivamente le organizzazioni a esaminare attentamente le loro caratteristiche di rischio uniche in base alla natura della propria attività e, in base a tali rischi e requisiti aziendali, a determinare il livello ASVS appropriato.

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
