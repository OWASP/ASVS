# V2 Autenticazione

## Obiettivo del controllo

L'autenticazione consiste nel confermare l'identità di qualcuno (o qualcosa) e nell'assicurarsi che le affermazioni fatte da una persona o su un dispositivo siano corrette, resistenti all'impersonazione e proteggano le password da furti o intercettazioni.

Quando l'ASVS è stato pubblicato per la prima volta, la combinazione di username e password era la forma più comune di autenticazione, eccetto nei sistemi ad alta sicurezza. L'Autenticazione Multi-Fattore (MFA) era generalmente riservata agli ambienti più critici e raramente richiesta altrove. Con l'aumento delle violazioni di password, l'idea che gli username fossero confidenziali e le password sconosciute è diventata obsoleta, invalidando molti controlli di sicurezza tradizionali. Ad esempio, il NIST 800-63 considera gli username e l'Autenticazione Basata sulla Conoscenza (KBA) come informazioni pubbliche, e classifica notifiche via SMS ed email come modalità di autenticazione ["restricted"](https://pages.nist.gov/800-63-FAQ/#q-b1), mentre le password sono considerate già compromesse. Ciò rende inutili gli autenticatori basati sulla conoscenza, il recupero tramite SMS o email, la cronologia delle password, la loro rotazione e complessità. Questi controlli, spesso poco efficaci, hanno portato gli utenti a creare password deboli ad ogni cambio, e con oltre 5 miliardi di username e password compromessi, è il momento di cambiare approccio.

Tra tutti i capitoli dell'ASVS, quelli relativi all'autenticazione e alla gestione delle sessioni hanno subito i cambiamenti più significativi. L'adozione di pratiche efficaci e basate su evidenze sarà una sfida per molti, ma è normale. La transizione verso un futuro post-password deve iniziare adesso.

## NIST 800-63 - Standard di autenticazione moderno basato su evidenze

Lo standard [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) è moderno, basato su evidenze e rappresenta un punto di riferimento per la sicurezza dell'autenticazione, indipendentemente dalla sua applicabilità specifica. È utile per tutte le organizzazioni a livello globale, ma è particolarmente rilevante per le agenzie statunitensi e per coloro che collaborano con esse.

La terminologia del NIST 800-63 può risultare inizialmente un po' complessa, soprattutto se si ha familiarità solo con l'autenticazione tradizionale tramite username e password. I progressi nell'autenticazione moderna richiedono l'introduzione di nuovi termini, che diventeranno comuni in futuro, ma comprendiamo che la loro adozione richiede tempo. Per semplificare la comprensione, abbiamo fornito un glossario alla fine di questo capitolo. Inoltre, molti requisiti sono stati riformulati per chiarirne meglio l'intento piuttosto che mantenere una corrispondenza letterale. Ad esempio, l'ASVS utilizza il termine "password", mentre lo standard NIST usa "segreto memorizzato".

Le sezioni sull'Autenticazione (V2), la Gestione delle Sessioni (V3) e, in misura minore, i Controlli di Accesso (V4) dell'ASVS sono state adattate per essere un sottoinsieme conforme ai controlli selezionati dal NIST 800-63b. Questi controlli sono mirati a contrastare le minacce comuni e le debolezze di autenticazione più sfruttate. Per ottenere la piena conformità con il NIST 800-63, è necessario fare riferimento direttamente a tale standard.

### Selezione di un livello AAL NIST appropriato

L'Application Security Verification Standard (ASVS) ha tentato di mappare i requisiti ASVS L1 a NIST AAL1, L2 a AAL2 e L3 a AAL3. Tuttavia, l'approccio del Livello 1 dell'ASVS, che considera i controlli come "essenziali", potrebbe non sempre corrispondere perfettamente al livello AAL corretto per verificare un'applicazione o un'API. Ad esempio, se un'applicazione è di Livello 3 o ha requisiti normativi che richiedono il rispetto di AAL3, allora il Livello 3 dovrebbe essere selezionato per i capitoli V2 (Autenticazione) e V3 (Gestione delle sessioni). La scelta del livello di Authentication Assurance Level (AAL) conforme al NIST dovrebbe seguire le linee guida NIST 800-63b, come indicato nella sezione *Selecting AAL* [NIST 800-63b Sezione 6.2](https://pages.nist.gov/800-63-3/sp800-63-3.html#AAL_CYOA).

## Legenda

Le applicazioni possono sempre superare i requisiti del livello attuale, specialmente se nella roadmap è previsto un meccanismo di autenticazione più moderno. In precedenza, l'ASVS richiedeva l'MFA obbligatorio, mentre il NIST non lo impone sempre. Perciò, in questo capitolo abbiamo introdotto indicazioni facoltative per evidenziare dove l'ASVS incoraggia ma non richiede un determinato controllo. Le seguenti indicazioni sono utilizzate in tutto il documento:

| Simbolo | Descrizione |
| :--: | :-- |
| | Non richiesto |
| o | Consigliato, ma non necessario |
| ✓ | Necessario |

## V2.1 Sicurezza delle Password

Le password, definite "segreti memorizzati" nel NIST 800-63, comprendono anche PIN, sequenze di sblocco, la scelta di immagini corrette (come gattini o altri elementi visivi) e frasi d'accesso. Questi sono generalmente considerati "qualcosa che sai" e vengono spesso utilizzati come meccanismo di autenticazione a singolo fattore. Tuttavia, ci sono sfide significative legate all'uso continuato dell'autenticazione a singolo fattore, tra cui la divulgazione online di miliardi di username e password validi, l'uso di password predefinite o deboli, e l'accessibilità di tabelle rainbow o dizionari delle password più comuni.

Le applicazioni dovrebbero incoraggiare fortemente gli utenti a utilizzare l'autenticazione a più fattori (MFA) e permettere loro di riutilizzare token già in loro possesso, come token FIDO o U2F, oppure collegarsi a un *Credential Service Provider* (CSP) che offre l'autenticazione a più fattori.

I *Credential Service Providers* (CSP) offrono identità federate agli utenti, che spesso possiedono più identità con diversi CSP, come Azure AD, Okta, Ping Identity o Google per identità aziendali, oppure Facebook, Twitter, Google o WeChat per identità consumer. Questo elenco non rappresenta un'approvazione di tali servizi, ma è un invito agli sviluppatori a considerare il fatto che molti utenti dispongono di identità consolidate con questi provider. Le organizzazioni dovrebbero valutare l'integrazione con identità utente esistenti in base al profilo di rischio associato al CSP. Ad esempio, una organizzazione governativa potrebbe non accettare un'identità social come login per sistemi sensibili, poiché è relativamente semplice creare identità fasulle o temporanee, mentre un'azienda di giochi mobile potrebbe essere incentivata a integrarsi con le principali piattaforme di social media per espandere la propria base di utenti attivi.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.1.1** | Verificare che le password impostate dagli utenti siano lunghe almeno 12 caratteri (dopo aver unito gli spazi multipli). ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.2** | Verificare che siano consentite password di almeno 64 caratteri e che vengano rifiutate quelle di oltre 128 caratteri. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.3** | Verificare che non venga effettuato il troncamento della password. Tuttavia, gli spazi multipli consecutivi possono essere sostituiti da un singolo spazio. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.4** | Verificare che nelle password siano consentiti tutti i caratteri Unicode stampabili, inclusi caratteri neutri come spazi ed emoji. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.5** | Verificare che gli utenti possano cambiare la propria password. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.6** | Verificare che la funzionalità di cambio password richieda all'utente la password corrente e quella nuova. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.7** | Verificare che le password inviate durante la registrazione dell'account, l'accesso e il cambio password vengano confrontate con un set di password violate, sia localmente (come le prime 1.000 o 10.000 password più comuni che corrispondono alla policy password del sistema) o utilizzando un'API esterna. Se si utilizza un'API, è necessario utilizzare zero-knowledge proof o un altro meccanismo per garantire che la password non venga inviata o utilizzata in chiaro per verificare il suo stato di violazione. Se la password è violata, l'applicazione deve richiedere all'utente di impostarne una nuova. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.8** | Verificare che venga fornito un misuratore di robustezza della password per aiutare gli utenti a impostare una password più sicura. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.9** | Verificare che non esistano regole di composizione password che limitino il tipo di caratteri consentiti. Non dovrebbe essere richiesto l'utilizzo di maiuscole, minuscole, numeri o caratteri speciali. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.10** | Verificare che non vi siano requisiti periodici di rotazione delle credenziali o cronologia delle password. | ✓ | ✓ | ✓ | 263 | 5.1.1.2 |
| **2.1.11** | Verificare che siano consentite le funzionalità "incolla", gli assistenti password del browser e i gestori di password esterni. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.12** | Verificare che l'utente possa scegliere di visualizzare temporaneamente l'intera password mascherata o l'ultimo carattere digitato su piattaforme che non dispongono nativamente di questa funzionalità. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |

Nota: L'obiettivo di consentire all'utente di visualizzare temporaneamente la propria password o l'ultimo carattere digitato è migliorare l'usabilità nell'inserimento delle credenziali, soprattutto quando si utilizzano password lunghe, passphrase o gestori di password. Un ulteriore motivo per includere questo requisito è evitare che, in fase di test, si chieda inutilmente alle organizzazioni di sovrascrivere il comportamento predefinito del campo password della piattaforma, eliminando una moderna funzionalità di sicurezza che risulta user-friendly.

## V2.2 Sicurezza Generale degli Authenticator

La flessibilità degli authenticator è essenziale per la sicurezza a lungo termine delle applicazioni. È necessario svolgere un refactor dell'applicazione per consentire l'utilizzo di authenticator aggiuntivi in base alle preferenze dell'utente, nonché per consentire la rimozione graduale di authenticator obsoleti o non sicuri.

Il NIST considera email e SMS come tipi di authenticator ["restricted"](https://pages.nist.gov/800-63-FAQ/#q-b1), ed è probabile che vengano rimossi da NIST 800-63 e di conseguenza in futuro anche dall'ASVS. Le applicazioni dovrebbero avere una roadmap che non richieda l'utilizzo di email o SMS.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.2.1** | Verificare che i controlli anti-automazione siano efficaci nel mitigare gli attacchi relativi a credenziali compromesse, forza bruta e blocco dell'account. Tali controlli includono il blocco delle password violate più comuni, i blocchi temporanei, la limitazione della velocità, i CAPTCHA, ritardi sempre crescenti tra i tentativi, restrizioni degli indirizzi IP o restrizioni basate sul rischio come posizione, primo accesso su un dispositivo, tentativi recenti di sbloccare l'account o simili. Verificare che non siano possibili più di 100 tentativi falliti all'ora su un singolo account. | ✓ | ✓ | ✓ | 307 | 5.2.2 / 5.1.1.2 / 5.1.4.2 / 5.1.5.2 |
| **2.2.2** | Verificare che l'uso di authenticator deboli (come SMS ed email) sia limitato alla verifica secondaria o all'approvazione delle transazioni e non come sostituto di metodi di autenticazione più sicuri. Verificare che vengano offerti in primis metodi più robusti, che gli utenti siano consapevoli dei rischi o che siano implementate misure adeguate per limitare i rischi di compromissione dell'account. | ✓ | ✓ | ✓ | 304 | 5.2.10 |
| **2.2.3** | Verificare che agli utenti vengano inviate notifiche dopo aggiornamenti dei dettagli di autenticazione, come reset delle credenziali, modifiche dell'email o dell'indirizzo, accessi da posizioni sconosciute o rischiose. Si preferisca l'uso di notifiche push, piuttosto che SMS o email, ma in assenza di notifiche push, SMS o email sono accettabili purché non venga divulgata nessuna informazione sensibile. | ✓ | ✓ | ✓ | 620 | |
| **2.2.4** | Verificare la resistenza all'impersonificazione tramite phishing, come l'utilizzo dell'autenticazione a due fattori, dispositivi crittografici (come chiavi connesse con un pulsante per l'autenticazione) o, a livelli AAL più alti, certificati lato client. | | | ✓ | 308 | 5.2.5 |
| **2.2.5** | Verificare che quando un Credential Service Provider (CSP) e l'applicazione che verifica l'autenticazione sono separati, sia presente un mutual TLS tra i due endpoint. | | | ✓ | 319 | 5.2.6 |
| **2.2.6** | Verificare la resistenza al replay mediante l'uso obbligatorio di dispositivi OTP (One-Time Password), autenticatori crittografici o codici di lookup. | | | ✓ | 308 | 5.2.8 |
| **2.2.7** | Verificare l'autenticazione richiedendo l'inserimento di un token OTP o un'azione iniziata dall'utente come la pressione di un pulsante su una chiave hardware FIDO. | | | ✓ | 308 | 5.2.9 |

## V2.3 Ciclo di Vita degli Authenticator

Gli *authenticator* includono password, *soft token* (token digitali software), *hardware token* (token digitali fisici) e dispositivi biometrici. Il ciclo di vita degli *authenticator* è cruciale per garantire la sicurezza di un'applicazione. Se chiunque potesse registrarsi autonomamente senza una verifica dell'identità, la fiducia nell'identità sarebbe compromessa. Per piattaforme come Reddit, questo livello di sicurezza può essere accettabile. Tuttavia, per sistemi bancari e altre applicazioni sensibili, è fondamentale prestare particolare attenzione durante la fase di registrazione e l'emissione di credenziali o dispositivi, per assicurare la sicurezza dell'applicazione.

Nota: alle password non deve essere assegnata una scadenza massima, né devono essere soggette a rotazione periodica. Le password devono essere verificate per eventuali compromissioni, non sostituite regolarmente.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.3.1** | Verificare che le password iniziali o i codici di attivazione generate dal sistema SIANO casuali e sicuri, DEVONO essere lunghi almeno 6 caratteri e POSSONO contenere lettere e numeri, con scadenza dopo un breve periodo di tempo. Non è consentito l'utilizzo a lungo termine di questi segreti iniziali. | ✓ | ✓ | ✓ | 330 | 5.1.1.2 / A.3 |
| **2.3.2** | Verificare che sia supportata la registrazione e l'utilizzo di dispositivi di autenticazione forniti dall'utente, come token U2F o FIDO. | | ✓ | ✓ | 308 | 6.1.3 |
| **2.3.3** | Verificare che le istruzioni di rinnovo siano inviate con sufficiente anticipo per permettere il rinnovo degli autenticatori con scadenza. | | ✓ | ✓ | 287 | 6.1.4 |

## V2.4 Memorizzazione delle credenziali

Questa sezione è rivolta ad architetti e sviluppatori impegnati nella creazione o ristrutturazione del codice. La verifica completa può essere effettuata solo attraverso la revisione del codice sorgente o tramite unit test o integration test specifici per la sicurezza. I penetration test non coprono nessuno di questi aspetti.

La lista della funzioni one-way per la derivazione delle chiavi è dettagliata nella sezione 5.1.1.2 del NIST 800-63 B, e nel [BSI Kryptographische Verfahren: Empfehlungen und Schlussell&auml;ngen (2018)](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile). In alternativa, si possono utilizzare gli standard nazionali o regionali più aggiornati per algoritmi e lunghezza delle chiavi.

Questa sezione non può essere soggetta a penetration test, pertanto i controlli non sono classificati come L1. Tuttavia, è cruciale per la sicurezza delle credenziali in caso di furto. Se si esegue il fork dell'ASVS per delineare un'architettura o linee guida di sviluppo sicuro o un elenco di controlli per la revisione del codice sorgente, si consiglia di riportare questi controlli a L1 nella propria versione privata.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.4.1** | Verificare che le password siano archiviate in una forma resistente agli attacchi offline. Le password DEVONO essere sottoposte ad hashing e sale usando funzioni approvate di derivazione di chiavi unidirezionale o di hashing delle password. Le funzioni di derivazione di chiavi e di hashing delle password utilizzano come input una password, un sale e un fattore di costo per generare un hash della password. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.2** | Verificare che il sale sia lungo almeno 32 bit e scelto in modo arbitrario per ridurre al minimo le collisioni relative al sale tra gli hash memorizzati. Per ogni credenziale, DEVONO essere archiviati un valore di sale univoco e l'hash risultante. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.3** | Verificare che se viene utilizzato PBKDF2, il numero di iterazioni DOVREBBE essere il più alto consentito dalle prestazioni del server, in genere almeno 100.000 iterazioni. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.4** | Verificare che se viene utilizzato bcrypt, il fattore di lavoro DOVREBBE essere il più alto consentito dalle prestazioni del server, con un minimo di 10. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.5** | Verificare che venga eseguita un'ulteriore iterazione di una funzione di derivazione di chiavi, utilizzando un valore di sale segreto noto solo al verificatore. Generare il valore di sale utilizzando un generatore di bit casuali approvato [SP 800-90Ar1] e fornire almeno il livello minimo di robustezza specificato nell'ultima revisione di SP 800-131A. Il valore segreto del sale DEVE essere archiviato separatamente dalle password con hash (ad esempio, in un dispositivo specializzato come un modulo di sicurezza hardware). | | ✓ | ✓ | 916 | 5.1.1.2 |

Laddove sono menzionati gli standard US, possono essere utilizzati, in alternativa, standard regionali o locali.

## V2.5 Recupero delle Credenziali

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.5.1** | Verificare che un segreto di attivazione iniziale o di recupero generato dal sistema non venga inviato all'utente in chiaro. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.2** | Verificare che i suggerimenti per la password o l'autenticazione basata sulla conoscenza (le cosiddette "domande segrete") non siano presenti. | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.3** | Verificare che il recupero delle credenziali tramite password non riveli in alcun modo la password corrente. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.4** | Verificare che non siano presenti account condivisi o di default (ad esempio "root", "admin" o "sa"). | ✓ | ✓ | ✓ | 16 | 5.1.1.2 / A.3 |
| **2.5.5** | Verificare che se un fattore di autenticazione viene modificato o sostituito, l'utente ne venga informato. | ✓ | ✓ | ✓ | 304 | 6.1.2.3 |
| **2.5.6** | Verificare che la password dimenticata e gli altri percorsi di recupero utilizzino un meccanismo di recupero sicuro, come OTP basato sul tempo (TOTP) o un altro soft token, push mobile o un altro meccanismo di recupero offline ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.7** | Verificare che in caso di perdita di OTP o di meccanismi di autenticazione a più fattori, venga effettuata una verifica dell'identità comparabile al livello di quella effettuata durante la registrazione. | | ✓ | ✓ | 308 | 6.1.2.3 |

## V2.6 Verifica con Look-up Secret 

I look up secrets sono liste pre-generate di codici segreti, simili ai Numeri di Autorizzazione alle Transazioni (TAN), ai codici di recupero dei social media o a una griglia contenente un set di valori casuali. Questi codici vengono distribuiti in modo sicuro agli utenti. Vengono utilizzati una sola volta e, una volta esauriti, la lista dei look up secret viene scartata. Questo tipo di autenticatore appartiene alla categoria di "qualcosa che possiedi".

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.6.1** | Verificare che i look up secrets possano essere utilizzati una sola volta. | | ✓ | ✓ | 308 | 5.1.2.2 |
| **2.6.2** | Verificare che i lookup secrets abbiano un'entropia sufficiente (112 bit) oppure, se inferiore a 112 bit, siano salati con un valore casuale unico di 32 bit e soggetti ad una funzione hash unidirezionale approvata. | | ✓ | ✓ | 330 | 5.1.2.2 |
| **2.6.3** | Verificare che i lookup secrets siano resistenti agli attacchi offline, che non siano facilmente prevedibili. | | ✓ | ✓ | 310 | 5.1.2.2 |

## V2.7 Verifica Out of Band 

In passato, un metodo comune per la verifica out of band era inviare un'email o un SMS con un link per reimpostare la password. Tuttavia, questo meccanismo debole è stato sfruttato dagli attaccanti, che possono prendere il controllo dell'account email della vittima e riutilizzare il link di reset per impadronirsi dell'account. Oggi esistono soluzioni più sicure per gestire la verifica out of band.

I meccanismi sicuri di autenticazione out of band includono dispositivi fisici in grado di comunicare con il verificatore attraverso un canale secondario sicuro, come le notifiche push su dispositivi mobili. Questo tipo di autenticatore rientra nella categoria "qualcosa che possiedi". Quando un utente tenta di autenticarsi, l'applicazione verificatrice invia un messaggio al verificatore out of band tramite una connessione sicura diretta o indiretta attraverso un servizio di terze parti. Il messaggio contiene un codice di autenticazione, solitamente un numero casuale a sei cifre o una finestra di dialogo di approvazione. Il verificatore confronta l'hash del codice ricevuto tramite il canale primario con quello del codice originale. Se corrispondono, l'utente è considerato autenticato.

L'ASVS presuppone che raramente gli sviluppatori creeranno nuovi verificatori out of band, come le notifiche push. Pertanto, i seguenti controlli ASVS si applicano a verificatori esistenti, come API di autenticazione, applicazioni e implementazioni di single sign-on. Se si sta sviluppando un nuovo autenticatore out of band, fare riferimento a NIST 800-63B &sect; 5.1.3.1.

Verificatori out of band insicuri, come email e VOIP, non sono consentiti. L'autenticazione PSTN e SMS è attualmente "restricted" dal NIST e dovrebbe essere abbandonata a favore di notifiche push o simili. Se è necessario utilizzare l'autenticazione out of band telefonica o SMS, consultare il § 5.1.3.3.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.7.1** | Verificare che gli autenticatori out of band in chiaro (NIST "restricted"), come SMS o PSTN, non siano offerti per impostazione predefinita e che vengano prima offerte alternative più sicure come le notifiche push. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.2** | Verificare che il meccanismo out of band faccia scadere le richieste di autenticazione, i codici o i token dopo 10 minuti. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.3** | Verificare che le richieste di autenticazione, i codici o i token del verificatore fuori banda siano utilizzabili una sola volta e solo per la richiesta di autenticazione originale. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.4** | Verificare che il meccanismo out of band di autenticazione e di verifica comunichino su un canale indipendente sicuro. | ✓ | ✓ | ✓ | 523 | 5.1.3.2 |
| **2.7.5** | Verificare che il meccanismo out of band conservi solo una versione con hash del codice di autenticazione. | | ✓ | ✓ | 256 | 5.1.3.2 |
| **2.7.6** | Verificare che il codice di autenticazione iniziale sia generato da un generatore di numeri casuali sicuro, contenente almeno 20 bit di entropia (in genere è sufficiente un numero casuale a sei cifre). | | ✓ | ✓ | 310 | 5.1.3.2 |

## V2.8 Verifica Monouso

Le password monouso (OTP) monofattore sono token software o fisici che visualizzano un segreto monouso pseudo-casuale che cambia continuamente. Questi dispositivi rendono il phishing (impersonificazione) difficile, ma non impossibile. Questo tipo di autenticazione appartiene alla categoria "qualcosa che possiedi". I token multifattore, simili agli OTP monofattore, richiedono ulteriori procedure di sicurezza per generare l'OTP finale. Queste includono l'inserimento di un codice PIN valido, l'autenticazione biometrica, la connessione tramite USB o NFC, o l'aggiunta di un valore supplementare, come quello generato da una transaction signing calculator.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.8.1** | Verificare che gli OTP basati sul tempo abbiano una durata definita prima della scadenza. | ✓ | ✓ | ✓ | 613 | 5.1.4.2 / 5.1.5.2 |
| **2.8.2** | Verificare che le chiavi simmetriche utilizzate per verificare gli OTP inviati siano protette adeguatamente, ad esempio utilizzando un modulo di sicurezza hardware (HSM) o un key storage sicuro fornito dal sistema operativo. | | ✓ | ✓ | 320 | 5.1.4.2 / 5.1.5.2|
| **2.8.3** | Verificare che nella generazione, nell'inizializzazione e nella verifica degli OTP vengano utilizzati algoritmi crittografici approvati. | | ✓ | ✓ | 326 | 5.1.4.2 / 5.1.5.2 |
| **2.8.4** | Verificare che gli OTP monouso basati sul tempo possano essere utilizzati una sola volta entro il periodo di validità. | | ✓ | ✓ | 287 | 5.1.4.2 / 5.1.5.2 |
| **2.8.5** | Verificare che se un token OTP multi-fattore basato sul tempo viene riutilizzato durante il periodo di validità, venga registrato e rifiutato con l'invio di una notifica al detentore del dispositivo. | | ✓ | ✓ | 287 | 5.1.5.2 |
| **2.8.6** | Verificare che il dispositivo hardware generatore di codici OTP possa essere revocato in caso di furto o smarrimento. Garantire che la revoca sia immediata su tutte le sessioni aperte, indipendentemente dalla posizione. | | ✓ | ✓ | 613 | 5.2.1 |
| **2.8.7** | Verificare che gli autenticatori biometrici siano limitati all'uso solo come fattori secondari in combinazione con qualcosa che si possiede e qualcosa che si conosce. | | o | ✓ | 308 | 5.2.3 |

## V2.9 Verifica Crittografica

Le chiavi di sicurezza crittografiche, come le smart card o le chiavi FIDO, richiedono che l'utente colleghi o associ il dispositivo crittografico al computer per completare l'autenticazione. Il verificatore invia un *nonce* (numero casuale) al dispositivo o software crittografico, che risponde calcolando una risposta basata su una chiave crittografica memorizzata in modo sicuro.

I requisiti per i dispositivi e i software crittografici, sia monofattore che multifattore, sono gli stessi, poiché la verifica dell'autenticatore crittografico dimostra il possesso dell'autenticatore stesso.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.9.1** | Verificare che le chiavi crittografiche utilizzate nella verifica siano archiviate in modo sicuro e protette dalla divulgazione, ad esempio utilizzando un Trusted Platform Module (TPM) o un Hardware Security Module (HSM), o un servizio del sistema operativo in grado di utilizzare questi meccanismi. | | ✓ | ✓ | 320 | 5.1.7.2 |
| **2.9.2** | Verificare che il nonce sia di almeno 64 bit e statisticamente unico o unico per l'intera durata di vita del dispositivo crittografico. | | ✓ | ✓ | 330 | 5.1.7.2 |
| **2.9.3** | Verificare che vengano utilizzati algoritmi crittografici approvati per la generazione, l'inizializzazione e la verifica. | | ✓ | ✓ | 327 | 5.1.7.2 |

## V2.10 Autenticazione del Servizio

Questa sezione non può essere verificata tramite penetration test, quindi non include requisiti L1. Tuttavia, se applicata nell'ambito di un'architettura, nella scrittura o nella revisione del codice sicuro, è consigliabile trattare il software di gestione delle chiavi (come Java Key Store) come requisito minimo a livello L1. La memorizzazione in chiaro di segreti non è accettabile in nessun caso.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.10.1** | Verificare che i segreti interni al servizio non si basino su credenziali statiche come password, chiavi API o account condivisi con accesso privilegiato. | | OS assisted | HSM | 287 | 5.1.1.1 |
| **2.10.2** | Verificare che, se sono richieste password per l'autenticazione del servizio, l'account di servizio utilizzato non sia uno predefinito. (ad esempio root/root o admin/admin sono predefiniti in alcuni servizi durante l'installazione). | | OS assisted | HSM | 255 | 5.1.1.1 |
| **2.10.3** | Verificare che le password siano archiviate con una protezione sufficiente per prevenire attacchi di recupero offline, incluso l'accesso al sistema locale. | | OS assisted | HSM | 522 | 5.1.1.1 |
| **2.10.4** | Verificare che password, integrazioni con database e sistemi di terze parti, seed e segreti interni e chiavi API siano gestiti in modo sicuro e non siano inclusi nel codice sorgente o archiviati all'interno dei repository del codice sorgente. Tale archiviazione DOVREBBE resistere agli attacchi offline. Si raccomanda l'utilizzo di un archivio software sicuro delle chiavi (L1), hardware TPM o un HSM (L3) per l'archiviazione delle password. | | OS assisted | HSM | 798 | |

## Requisiti aggiuntivi per le agenzie statunitensi

Le agenzie statunitensi hanno requisiti obbligatori relativi a NIST 800-63. L'Application Security Verification Standard ha sempre riguardato l'80% dei controlli che si applicano a quasi il 100% delle applicazioni, e non l'ultimo 20% dei controlli avanzati o quelli con applicabilità limitata. Pertanto, l'ASVS è un sottoinsieme rigoroso di NIST 800-63, specialmente per le classificazioni IAL1/2 e AAL1/2, ma non è sufficientemente completo, in particolare per le classificazioni IAL3/AAL3.

Esortiamo vivamente le agenzie governative statunitensi a rivedere e implementare NIST 800-63 nella sua interezza.

## Glossario

| Termine | Significato |
| --- | --- |
| CSP | Credential Service Provider also called an Identity Provider, un servizio che gestisce le identità degli utenti e fornisce credenziali di autenticazione. |
| Authenticator | Componente che verifica le credenziali presentate dall'utente. Può gestire diversi fattori come password, token, autenticazione a due fattori (MFA) o accessi federati. |
| Verifier | Questa entità verifica la validità delle credenziali dell'utente in base alle informazioni ricevute dall'autenticatore. Potrebbe anche confermare se le credenziali sono associate a un utente valido e se sono attive/non revocate. |
| OTP | One-time password. Password valida per un solo tentativo di accesso e poi scade |
| SFA | Single-factor authenticators, come qualcosa che conosci (segreti, password, frasi segrete, PINs), qualcosa che sei (biometria, impronte digitali, scansioni facciali), o qualcosa che possiedi (token OTP, un dispositivo crittografico come una smart card). |
| MFA | Multi-factor authentication, che include almeno due fattori |

## Riferimenti

Per approfondimenti, consultare:

* [NIST 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST 800-63 A - Enrollment and Identity Proofing](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST 800-63 B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST 800-63 C - Federation and Assertions](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [OWASP Cheat Sheet - Password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Forgot password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Choosing and using security questions](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
