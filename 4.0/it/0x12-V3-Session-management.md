# V3 Gestione delle sessioni

## Obiettivo del controllo

Uno dei componenti principali di qualsiasi applicazione web o API stateful è il meccanismo con cui controlla e mantiene lo stato di un utente o dispositivo che interagisce con essa. La gestione delle sessioni trasforma un protocollo senza stato in uno con stato, il che è fondamentale per differenziare diversi utenti o dispositivi.

Verificare che un'applicazione soddisfi i seguenti requisiti di alto livello per la gestione delle sessioni:
Ensure that a verified application satisfies the following high-level session management requirements:

* Le sessioni sono uniche per ogni individuo e non possono essere indovinate o condivise.
* Le sessioni vengono invalidate quando non sono più necessarie e scadono durante periodi di inattività.

Come osservato in precedenza, questi requisiti sono stati adattati per essere un sottoinsieme conforme dei controlli selezionati dal NIST 800-63b, focalizzati su minacce comuni e debolezze di autenticazione sfruttate di frequente. I precedenti requisiti di verifica sono stati ritirati, deduplicati o, nella maggior parte dei casi, adattati per essere fortemente allineati con l'intento dei requisiti obbligatori del [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) .

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

TLS o un canale di trasporto sicuro comparabile è obbligatorio per la gestione delle sessioni. Questo verrà coperto nel capitolo relativo alla sicurezza delle comunicazioni.

## V3.3 Terminazione Sessione

I timeout di sessione sono stati allineati con NIST 800-63, che consente timeout di sessione molto più lunghi di quelli tradizionalmente consentiti dagli standard di sicurezza. Le organizzazioni dovrebbero esaminare la tabella seguente e, se dato il rischio dell'applicazione è desiderabile un timeout più lungo, il valore NIST dovrebbe essere il limite superiore dei timeout di inattività della sessione.

Session timeouts have been aligned with NIST 800-63, which permits much longer session timeouts than traditionally permitted by security standards. Organizations should review the table below, and if a longer time out is desirable based around the application's risk, the NIST value should be the upper bounds of session idle timeouts.

L1 in questo contesto è IAL1/AAL1, L2 è IAL2/AAL3, L3 è IAL3/AAL3. Per IAL2/AAL2 e IAL3/AAL3, minore è il timeout di inattività, minore è il limite inferiore dei tempi di inattività per la disconnessione o la riautenticazione per riprendere la sessione.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.3.1** | Verificare che la disconnessione e la scadenza invalidino il token di sessione, in modo che il pulsante Indietro o una relying party a valle non riprendano una sessione autenticata, anche tra relying party.  ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 613 | 7.1 |
| **3.3.2** | Se gli autenticatori consentono agli utenti di rimanere collegati, verificare che la riautenticazione avvenga periodicamente sia quando viene utilizzata attivamente sia dopo un periodo di inattività. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | 30 days | 12 hours or 30 minutes of inactivity, 2FA optional | 12 hours or 15 minutes of inactivity, with 2FA | 613 | 7.2 |
| **3.3.3** | Verificare che l'applicazione offra la possibilità di terminare tutte le altre sessioni attive dopo un cambio password riuscito (incluso il cambio tramite reset/recupero password) e che ciò sia efficace in tutta l'applicazione, l'accesso federato (se presente) e qualsiasi relying party. | | ✓ | ✓ | 613 | |
| **3.3.4** | Verificare che gli utenti possano visualizzare e (dopo aver reinserito le credenziali di accesso) disconnettersi da una o tutte le sessioni e i dispositivi attualmente attivi. | | ✓ | ✓ | 613 | 7.1 |

## V3.4 Gestione Sessioni Basate su Cookie

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.4.1** | Verificare che i token di sessione basati su cookie abbiano impostato l'attributo 'Sicure'. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 614 | 7.1.1 |
| **3.4.2** | Verificare che i token di sessione basati su cookie abbiano impostato l'attributo 'HttpOnly'. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1004 | 7.1.1 |
| **3.4.3** | Verificare che i token di sessione basati su cookie utilizzino l'attributo 'SameSite' per limitare l'esposizione ad attacchi di Cross-Site Request Forgery (CSRF). ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1275 | 7.1.1 |
| **3.4.4** | Verificare che i token di sessione basati su cookie utilizzino il prefisso "__Host-" in modo che i cookie vengano inviati solo all'host che ha inizialmente impostato il cookie. | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.5** | Verificare che se l'applicazione viene pubblicata su un nome di dominio con altre applicazioni che impostano o utilizzano cookie di sessione che potrebbero rivelare i cookie di sessione, che sia presente l'attributo 'path' nei token di sessione utilizzando il percorso più preciso possibile. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |

## V3.5 Gestione Sessioni Basate su Token

La gestione delle sessioni basate su token include JWT, OAuth, SAML e API key. Tra queste, le API key sono note per essere deboli e non dovrebbero essere utilizzate nel codice recente.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.5.1** | Verificare che l'applicazione consenta agli utenti di revocare i token OAuth che creano relazioni di fiducia verso le applicazioni collegate. | | ✓ | ✓ | 290 | 7.1.2 |
| **3.5.2** | Verificare che l'applicazione utilizzi token di sessione anziché segreti e API key statici, tranne in implementazioni legacy. | | ✓ | ✓ | 798 | |
| **3.5.3** | Verificare che i token di sessione stateless utilizzino firme digitali, crittografia e altre contromisure per proteggersi da manomissioni, enveloping, replay, null cipher, attacchi di key substitution. | | ✓ | ✓ | 345 | |

## V3.6 Riautenticazione Federata

Questa sezione riguarda coloro che scrivono codice per Relying Party (RP) o Credential Service Provider (CSP). Se ci si affida a codice che implementa queste funzionalità, assicurarsi che questi problemi vengano gestiti correttamente.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.6.1** | Verificare che i Relying Party (RP) specifichino il tempo massimo di autenticazione ai Credential Service Provider (CSP) e che i CSP richiedano una nuova autenticazione dell'utente se è stata utilizzata una sessione entro tale periodo. | | | ✓ | 613 | 7.2.1 |
| **3.6.2** | Verificare che i Credential Service Provider (CSP) informino i Relying Party (RP) dell'ultimo evento di autenticazione, per consentire ai RP di determinare se è necessario richiedere una nuova autenticazione dell'utente. | | | ✓ | 613 | 7.2.1 |

## V3.7 Difese contro gli Exploit di Gestione Sessione

Esistono un numero limitato di attacchi di gestione delle sessioni, alcuni legati all'esperienza utente (UX) relativa alle sessioni. In precedenza, basandosi sui requisiti ISO 27002, l'ASVS richiedeva il blocco di sessioni simultanee multiple. Il blocco di sessioni simultanee non è più appropriato, non solo perché gli utenti moderni dispongono di molti dispositivi o l'applicazione è un'API senza sessione del browser, ma nella maggior parte di queste implementazioni vince l'ultimo autenticatore, che spesso è l'attaccante. Questa sezione fornisce una guida avanzata per scoraggiare, ritardare e rilevare gli attacchi di gestione delle sessioni lato codice.

### Descrizione dell'Attacco Half-Open

All'inizio del 2018, diversi istituti finanziari sono stati compromessi utilizzando quello che gli attaccanti chiamavano "attacchi half-open" (semi-aperti). Questo termine è rimasto in uso nel settore. Gli attaccanti hanno colpito molteplici istituzioni codice proprietario diverso anche all'interno delle stesse istituzioni. L'attacco half-open sfrutta un difetto del pattern di progettazione comunemente riscontrato in molti sistemi di autenticazione, gestione delle sessioni e controllo degli accessi esistenti.

Gli attaccanti iniziano un attacco half-open tentando di bloccare, reimpostare o recuperare una credenziale. Un pattern di progettazione popolare per la gestione delle sessioni riutilizza gli oggetti/modelli di sessione del profilo utente tra codice non autenticato, parzialmente autenticato (ripristino password, username dimenticato) e completamente autenticato. Questo pattern di progettazione popola un oggetto o token di sessione valido contenente il profilo della vittima, inclusi hash di password e ruoli. Se i controlli di accesso nei controller o nei router non verificano correttamente che l'utente sia completamente connesso, l'attaccante potrà agire come l'utente. Gli attacchi potrebbero includere la modifica della password dell'utente su un valore noto, l'aggiornamento dell'indirizzo email per eseguire un ripristino password valido, la disabilitazione dell'autenticazione a due fattori o la registrazione di un nuovo dispositivo MFA, la visualizzazione o la modifica delle API key e così via.

| # | Descrizione | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.7.1** | Verificare che l'applicazione garantisca una sessione di accesso completa e valida o richieda una riautenticazione o una verifica secondaria prima di consentire qualsiasi transazione sensibile o modifica dell'account. | ✓ | ✓ | ✓ | 306 | |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#Directives)
