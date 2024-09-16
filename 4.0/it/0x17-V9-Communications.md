# V9 Comunicazione

## Obiettivo del controllo

Assicurarsi che l'applicazione rispetti i seguenti requisiti di alto livello:

* È necessaria la crittografia TLS o una crittografia equivalente, indipendentemente dalla riservatezza del contenuto.
* Seguire le linee guida più recenti, comprese:
  * Consigli sulla configurazione
  * Cifrari e algoritmi consigliati
* Evitare l'uso di algoritmi e cifrature deboli o prossimi alla deprecazione, salvo necessità specifiche.
* Disabilitare algoritmi e cifrature deprecati o noti per essere insicuri.

All'interno di questi requisiti:

* Seguire costantemente i consigli del settore sulla configurazione sicura di TLS, poiché tali indicazioni cambiano frequentemente a causa di vulnerabilità critiche rilevate in algoritmi e cifrature esistenti.
* Utilizzare le versioni più aggiornate degli strumenti di revisione della configurazione TLS per definire l'ordine preferito e la selezione degli algoritmi.
* Verificare la validità e l'attendibilità dei certificati utilizzati per l'autenticazione TLS.

## V9.1 Sicurezza della Comunicazione lato Client

Garantire che tutti i messaggi client vengano inviati su reti crittografate, utilizzando TLS 1.2 o versioni successive. 
Utilizzare strumenti aggiornati per esaminare regolarmente la configurazione del client.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.1.1** | Verificare che TLS venga utilizzato per tutte le connessioni client e che non si ripieghi su comunicazioni non sicure o non crittografate. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | Utilizzare strumenti l'ultima versione dei test TLS per verificare che siano abilitate solo suite crittografiche robuste, con le suite più sicure impostate come preferite. | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | Verificare che siano abilitate solo le versioni più recenti consigliate del protocollo TLS, come TLS 1.2 e TLS 1.3. La versione più recente del protocollo TLS dovrebbe essere l'opzione preferita. | ✓ | ✓ | ✓ | 326 |

## V9.2 Sicurezza della Comunicazione lato Server

La comunicazione server va oltre il semplice HTTP. Devono essere implementate connessioni sicure da e verso altri sistemi, come sistemi di monitoraggio, strumenti di gestione, accesso remoto e SSH, middleware, database, mainframe, sistemi partner o sorgenti esterne. Tutte queste connessioni devono essere crittografate per evitare situazioni in cui le difese perimetrali siano robuste, ma l'intercettazione interna risulti banale.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.2.1** | Verificare che le connessioni da e verso il server utilizzino certificati TLS affidabili. Se vengono utilizzati certificati auto-generati o self-signed, il server deve essere configurato per fidarsi solo di CA interne specifiche e di certificati self-signed specifici. Tutti gli altri devono essere rifiutati. | | ✓ | ✓ | 295 |
| **9.2.2** | Verificare che la comunicazione crittografata, come TLS, venga utilizzata per tutte le connessioni in ingresso e in uscita, incluse quelle per porte di gestione, monitoraggio, autenticazione, chiamate API o di servizi web, database, cloud, serverless, mainframe, connessioni esterne e con partner. Il server non deve ripiegare su protocolli non sicuri o non crittografati. | | ✓ | ✓ | 319 |
| **9.2.3** | Verificare che tutte le connessioni crittografate a sistemi esterni che coinvolgono informazioni o funzioni sensibili siano autenticate. | | ✓ | ✓ | 287 |
| **9.2.4** | Verificare che la revoca corretta dei certificati, come lo "Online Certificate Status Protocol (OCSP) Stapling", sia abilitata e configurata. | | ✓ | ✓ | 299 |
| **9.2.5** | Verificare che gli errori di connessione TLS con il backend vengano loggati. | | | ✓ | 544 |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* [OWASP - Pinning Guide](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)
* Note su "Modalità di TSL approvate":
    * In passato, l'ASVS faceva riferimento allo standard statunitense FIPS 140-2, ma applicare standard americani a livello globale può essere difficile, contraddittorio o confusionario.
    * Un metodo migliore per raggiungere la conformità alla sezione 9.1 sarebbe quello di consultare guide come [TLS lato server di Mozilla](https://wiki.mozilla.org/Security/Server_Side_TLS), [generare configurazioni note e sicure](https://mozilla.github.io/server-side-tls/ssl-config-generator/), e utilizzare strumenti di valutazione TLS aggiornati e riconosciuti per ottenere il livello di sicurezza desiderato.
