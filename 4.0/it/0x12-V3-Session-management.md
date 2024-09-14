# V3 Gestione delle sessioni

## Obiettivo del controllo

Uno degli elementi fondamentali di qualsiasi applicazione web o API stateful è il meccanismo che gestisce e mantiene lo stato di un utente o dispositivo durante l'interazione con essa. La gestione delle sessioni consente di trasformare un protocollo senza stato in uno con stato, ed è essenziale per distinguere i vari utenti o dispositivi.

Verificare che un'applicazione soddisfi i seguenti requisiti di alto livello per la gestione delle sessioni:

* Le sessioni sono uniche per ciascun individuo e non possono essere né indovinate né condivise.
* Le sessioni vengono invalidate quando non più necessarie e scadono dopo un periodo di inattività.

Come già osservato, questi requisiti sono stati adattati per essere un sottoinsieme conforme ai controlli selezionati dal NIST 800-63b, concentrandosi su minacce comuni e vulnerabilità di autenticazione frequentemente sfruttate. I requisiti di verifica precedenti sono stati eliminati, deduplicati o, nella maggior parte dei casi, adattati per allinearsi strettamente con le disposizioni obbligatorie del [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) .

## Requisiti di Verifica della Sicurezza

## V3.1 Sicurezza Fondamentale della Gestione Sessione

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.1.1** | Verificare che l'applicazione non riveli mai token di sessione nei parametri dell'URL. | ✓ | ✓ | ✓ | 598 | |

## V3.2 Associazione di Sessione

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.2.1** | Verificare che l'applicazione generi un nuovo token di sessione all'autenticazione dell'utente. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 384 | 7.1 |
| **3.2.2** | Verificare che i token di sessione possiedano almeno 64 bit di entropia. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 331 | 7.1 |
| **3.2.3** | Verificare che l'applicazione memorizzi i token di sessione solo nel browser utilizzando metodi sicuri come cookie adeguatamente protetti (vedere sezione 3.4) o il session storage in HTML5 | ✓ | ✓ | ✓ | 539 | 7.1 |
| **3.2.4** | Verificare che i token di sessione siano generati utilizzando algoritmi crittografici approvati. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 331 | 7.1 |

L'uso di TLS o di un canale di trasporto sicuro equivalente è obbligatorio per la gestione delle sessioni. Questo aspetto sarà trattato nel capitolo dedicato alla sicurezza delle comunicazioni.

## V3.3 Terminazione Sessione

I timeout di sessione sono stati allineati con il NIST 800-63, che consente durate molto più lunghe rispetto a quelle tradizionalmente previste dagli standard di sicurezza. Le organizzazioni dovrebbero consultare la tabella seguente e, se il rischio associato all'applicazione giustifica un timeout più lungo, il valore NIST dovrebbe rappresentare il limite massimo per i timeout di inattività della sessione.

In questo contesto, L1 corrisponde a IAL1/AAL1, L2 a IAL2/AAL2 e L3 a IAL3/AAL3. Per IAL2/AAL2 e IAL3/AAL3, un timeout di inattività più breve implica un limite inferiore per la disconnessione o la necessità di riautenticazione per riprendere la sessione.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.3.1** | Verificare che la disconnessione e la scadenza invalidino il token di sessione, in modo che il pulsante Indietro o una relying party a valle non riprendano una sessione autenticata, anche tra relying party. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 613 | 7.1 |
| **3.3.2** | Se gli autenticatori consentono agli utenti di rimanere collegati, verificare che la riautenticazione avvenga periodicamente sia quando viene utilizzata attivamente sia dopo un periodo di inattività. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | 30 giorni | 12 ore o 30 minuti di inattività, 2FA opzionale | 12 ore o 15 minuti di inattività, con 2FA | 613 | 7.2 |
| **3.3.3** | Verificare che l'applicazione consenta di terminare tutte le altre sessioni attive dopo un cambio password riuscito (incluso il cambio tramite reset/recupero password) e che ciò si applichi all'intera l'applicazione, all'accesso federato (se presente) e a qualsiasi relying party. | | ✓ | ✓ | 613 | |
| **3.3.4** | Verificare che gli utenti possano visualizzare e (dopo aver reinserito le credenziali di accesso) disconnettersi da una o tutte le sessioni e i dispositivi attualmente attivi. | | ✓ | ✓ | 613 | 7.1 |

## V3.4 Gestione Sessioni Basate su Cookie

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.4.1** | Verificare che i token di sessione basati su cookie abbiano impostato l'attributo 'Secure'. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 614 | 7.1.1 |
| **3.4.2** | Verificare che i token di sessione basati su cookie abbiano impostato l'attributo 'HttpOnly'. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1004 | 7.1.1 |
| **3.4.3** | Verificare che i token di sessione basati su cookie utilizzino l'attributo 'SameSite' per limitare l'esposizione ad attacchi di Cross-Site Request Forgery (CSRF). ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.4** | Verificare che i token di sessione basati su cookie utilizzino il prefisso "__Host-" in modo che i cookie vengano inviati solo all'host che ha inizialmente impostato il cookie. | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.5** | Verificare che se l'applicazione viene pubblicata su un nome di dominio con altre applicazioni che impostano o utilizzano cookie di sessione che potrebbero rivelare i cookie di sessione, che sia presente l'attributo 'path' nei token di sessione utilizzando il percorso più specifico possibile. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |

## V3.5 Gestione Sessioni Basate su Token

La gestione delle sessioni basate su token include JWT, OAuth, SAML e API key. Tra queste, le API key sono note per essere deboli e non dovrebbero essere utilizzate nelle implementazioni moderne.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.5.1** | Verificare che l'applicazione consenta agli utenti di revocare i token OAuth che creano relazioni di fiducia verso le applicazioni collegate. | | ✓ | ✓ | 290 | 7.1.2 |
| **3.5.2** | Verificare che l'applicazione utilizzi token di sessione anziché segreti e API key statici, salvo nelle implementazioni legacy. | | ✓ | ✓ | 798 | |
| **3.5.3** | Verificare che i token di sessione stateless utilizzino firme digitali, crittografia e altre contromisure per proteggersi da manomissioni, enveloping, replay, null cipher, attacchi di key substitution. | | ✓ | ✓ | 345 | |

## V3.6 Riautenticazione Federata

Questa sezione riguarda coloro che scrivono codice per Relying Party (RP) o Credential Service Provider (CSP). Se ci si affida a codice che implementa queste funzionalità, assicurarsi che questi problemi vengano gestiti correttamente.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.6.1** | Verificare che i Relying Party (RP) specifichino il tempo massimo di autenticazione ai Credential Service Provider (CSP) e che i CSP richiedano una nuova autenticazione dell'utente se è stata utilizzata una sessione entro tale periodo. | | | ✓ | 613 | 7.2.1 |
| **3.6.2** | Verificare che i Credential Service Provider (CSP) informino i Relying Party (RP) dell'ultimo evento di autenticazione, per consentire ai RP di determinare se è necessario richiedere una nuova autenticazione dell'utente. | | | ✓ | 613 | 7.2.1 |

## V3.7 Difese contro gli Exploit di Gestione Sessione

Esistono pochi attacchi noti relativi alla gestione delle sessioni, alcuni dei quali sono legati all'esperienza utente (UX) con le sessioni. In passato, l'ASVS, seguendo i requisiti ISO 27002, imponeva il blocco delle sessioni simultanee multiple. Tuttavia, questo approccio non è più appropriato, sia perché gli utenti moderni utilizzano diversi dispositivi o perché l'applicazione è un'API senza sessione del browser. Inoltre, in molte implementazioni, l'ultimo autenticatore prevale, il che spesso avvantaggia l'attaccante. Questa sezione offre una guida avanzata per scoraggiare, ritardare e rilevare gli attacchi di gestione delle sessioni a livello di codice.

### Descrizione dell'Attacco Half-Open

Nel 2018, diversi istituti finanziari sono stati vittime di compromissioni attraverso quello che è noto come "attacco half-open" (semi-aperto), un termine che è rimasto in uso nel settore. Gli attaccanti hanno sfruttato vulnerabilità comuni a diversi sistemi di autenticazione, gestione delle sessioni e controllo degli accessi, anche all'interno delle stesse istituzioni.

L'attacco half-open inizia con il tentativo di bloccare, reimpostare o recuperare una credenziale. Molti sistemi di gestione delle sessioni utilizzano un pattern di progettazione che riutilizza gli oggetti o modelli di sessione del profilo utente tra stati di autenticazione diversi: non autenticato, parzialmente autenticato (ad esempio per il ripristino della password o il recupero dell'username) e completamente autenticato. Questo approccio assegna un token di sessione valido contenente informazioni del profilo della vittima, inclusi hash delle password e ruoli. Se i controlli di accesso nei controller o nei router non verificano correttamente che l'utente sia completamente autenticato, l'attaccante può agire come se fosse l'utente. Le azioni dell'attaccante possono includere la modifica della password dell'utente con un valore noto, l'aggiornamento dell'indirizzo email per effettuare un ripristino password, la disabilitazione dell'autenticazione a due fattori, la registrazione di un nuovo dispositivo MFA, o la visualizzazione e modifica delle API key.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.7.1** | Verificare che l'applicazione garantisca una sessione di accesso completa e valida o richieda una riautenticazione o una verifica secondaria prima di consentire qualsiasi transazione sensibile o modifica dell'account. | ✓ | ✓ | ✓ | 306 | |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#Directives)
