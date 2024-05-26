# Appendice C: Requisiti di Verifica per l'Internet delle Cose (IoT)

Questo capitolo era originariamente nella sezione principale, ma con il lavoro svolto dal team OWASP IoT, non ha senso mantenere due filoni differenti sull'argomento. Per la versione 4.0, stiamo spostando questo contenuto nell'Appendice e invitiamo tutti coloro che ne hanno bisogno a consultare il [progetto OWASP IoT](https://owasp.org/www-project-internet-of-things/)

## Obiettivo del controllo

I dispositivi Embedded/IoT devono:

* Avere lo stesso livello di controlli di sicurezza presenti nel server, applicando i controlli di sicurezza in un ambiente trusted.
* I dati sensibili memorizzati sul dispositivo devono essere protetti in modo sicuro utilizzando meccanismi supportati dall'hardware, come secure element.
* Tutti i dati sensibili trasmessi dal dispositivo devono utilizzare la sicurezza a livello di trasporto.

## Security Verification Requirements

| # | Descrizione | L1 | L2 | L3 | Da |
| --- | --- | --- | --- | -- | -- |
| **C.1** | Verificare che le interfacce di debug a livello di applicazione come USB, UART e altre varianti seriali siano disabilitate o protette da una password complessa.	 | ✓ | ✓ | ✓ | 4.0 |
| **C.2** | Verificare che le chiavi crittografiche e i certificati siano unici per ogni singolo dispositivo.	 | ✓ | ✓ | ✓ | 4.0 |
| **C.3** | Verificare che, se applicabili, i controlli di protezione della memoria come ASLR e DEP siano abilitati dal sistema operativo embedded/IoT. | ✓ | ✓ | ✓ | 4.0 |
| **C.4** | Verificare che le interfacce di debug integrate come JTAG o SWD siano disabilitate o che il meccanismo di protezione disponibile sia abilitato e configurato adeguatamente. | ✓ | ✓ | ✓ | 4.0 |
| **C.5** | Verificare che se disponibile, la trusted execution sia implementata e abilitata sul SoC o CPU del dispositivo. | ✓ | ✓ | ✓ | 4.0 |
| **C.6** | Verificare che i dati sensibili, le chiavi private e i certificati siano memorizzati in modo sicuro in un Secure Element, TPM, TEE (Trusted Execution Environment), o protetti mediante crittografia robusta. | ✓ | ✓ | ✓ | 4.0 |
| **C.7** | Verificare che le app del firmware proteggano i dati in transito utilizzando la sicurezza a livello di trasporto. | ✓ | ✓ | ✓ | 4.0 |
| **C.8** | Verificare che le app del firmware convalidino la firma digitale delle connessioni server. | ✓ | ✓ | ✓ | 4.0 |
| **C.9** | Verificare che le comunicazioni wireless siano autenticate reciprocamente. | ✓ | ✓ | ✓ | 4.0 |
| **C.10** | Verificare che le comunicazioni wireless siano inviate su un canale criptato.  | ✓ | ✓ | ✓ | 4.0 |
| **C.11** | Verificare che qualsiasi utilizzo di funzioni C vietate sia sostituito con le versioni equivalenti sicure. | ✓ | ✓ | ✓ | 4.0 |
| **C.12** | Verificare che ogni firmware mantenga un catalogo delle terze parti (software bill of materials), con versioni e vulnerabilità pubblicate.	 | ✓ | ✓ | ✓ | 4.0 |
| **C.13** | Verificare che tutto il codice, inclusi i binari di terze parti, le librerie e i framework, sia esaminato per le credenziali hardcoded (backdoor). | ✓ | ✓ | ✓ | 4.0 |
| **C.14** | Verificare che i componenti applicativi e firmware non siano suscettibili a OS Command Injection tramite l'invocazione di wrapper di comandi shell, script, o che i controlli di sicurezza impediscano l'OS Command Injection. | ✓ | ✓ | ✓ | 4.0 |
| **C.15** | Verificare che le app del firmware associno la firma digitale ai server trusted. |  | ✓ | ✓ | 4.0 |
| **C.16** | Verificare la presenza di funzionalità di resistenza e/o rilevamento di manomissioni. |  | ✓ | ✓ | 4.0 |
| **C.17** | Verificare che le tecnologie di protezione della proprietà intellettuale fornite dal produttore del chip siano abilitate. |  | ✓ | ✓ | 4.0 |
| **C.18** | Verificare che siano presenti controlli di sicurezza per ostacolare il reverse engineering del firmware (ad esempio, rimozione di simboli di debug). |  | ✓ | ✓ | 4.0 |
| **C.19** | Verificare che il dispositivo convalidi la firma dell'immagine di boot prima di caricarla. |  | ✓ | ✓ | 4.0 |
| **C.20** | Verificare che il processo di aggiornamento del firmware non sia vulnerabile agli attacchi di time-of-check vs time-of-use. |  | ✓ | ✓ | 4.0 |
| **C.21** | Verificare che il dispositivo utilizzi la firma del codice e convalidi i file di aggiornamento del firmware prima dell'installazione. |  | ✓ | ✓ | 4.0 |
| **C.22** | Verificare che sul dispositivo non possano essere installate versioni precedenti (anti-rollback) del firmware. |  | ✓ | ✓ | 4.0 |
| **C.23** | Verificare l'uso di un generatore di numeri pseudo-casuali crittograficamente sicuro sul dispositivo embedded (ad esempio, utilizzando generatori di numeri casuali forniti dal chip). |  | ✓ | ✓ | 4.0 |
| **C.24** | Verificare che il firmware possa eseguire aggiornamenti automatici secondo una pianificazione predefinita. |  | ✓ | ✓ | 4.0 |
| **C.25** | Verificare che il dispositivo cancelli il firmware e i dati sensibili in caso di rilevamento di manomissioni o ricezione di messaggi non validi. |  |  | ✓ | 4.0 |
| **C.26** | Verificare che vengano utilizzati solo microcontrollori che supportano la disabilitazione delle interfacce di debug (ad esempio, JTAG, SWD). |  |  | ✓ | 4.0 |
| **C.27** | Verificare che vengano utilizzati solo microcontrollori che forniscono una protezione efficace contro gli attacchi di decapping e side channel. |  |  | ✓ | 4.0 |
| **C.28** | Verificare che le piste sensibili non siano esposte verso gli strati esterni del circuito stampato |  |  | ✓ | 4.0 |
| **C.29** | Verificare che la comunicazione inter-chip sia criptata (ad esempio, comunicazione tra la scheda principale e la scheda figlia). |  |  | ✓ | 4.0 |
| **C.30** | Verificare che il dispositivo utilizzi la firma del codice e convalidi il codice prima dell'esecuzione. |  |  | ✓ | 4.0 |
| **C.31** | Verificare che le informazioni sensibili mantenute in memoria vengano sovrascritte con zeri non appena non sono più necessarie. |  |  | ✓ | 4.0 |
| **C.32** | Verificare Verifica che le app del firmware utilizzino container a livello kernel per l'isolamento tra le app. |  |  | ✓ | 4.0 |
| **C.33** | Verificare che per le build del firmware siano configurate le flag di compilazione sicura come -fPIE, -fstack-protector-all, -Wl,-z,noexecstack, -Wl,-z,noexecheap. |  |  | ✓ | 4.0 |
| **C.34** | Verificare che i microcontrollori siano configurati con la protezione del codice (se applicabile). |  |  | ✓ | 4.0 |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Internet of Things Top 10](https://owasp.org/www-pdf-archive/OWASP-IoT-Top-10-2018-final.pdf)
* [OWASP Embedded Application Security Project](https://owasp.org/www-project-embedded-application-security/)
* [OWASP Internet of Things Project](https://owasp.org/www-project-internet-of-things/)
* [Trudy TCP Proxy Tool](https://github.com/praetorian-inc/trudy)
