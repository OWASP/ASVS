# V9 Comunicazione

## Obiettivo del controllo

Assicurarsi che l'applicazione rispetti i seguenti requisiti di alto livello:

* È necessaria la crittografia TLS o una crittografia equivalente, indipendentemente dalla riservatezza del contenuto.
* Segui le linee guida più recenti, inclusi:
  * Consigli sulla configurazione
  * Cifrari e algoritmi consigliati
* Evita algoritmi e cifrature deboli o che saranno presto deprecati, a meno che non sia strettamente necessario.
* Disabilita algoritmi e cifrature deprecati o noti per essere insicuri.

All'interno di questi requisiti:

* Tieni traccia dei consigli del settore sulla configurazione sicura di TLS, poiché cambiano frequentemente (spesso a causa di vulnerabilità critiche in algoritmi e cifrature esistenti).
* Utilizza le versioni più recenti degli strumenti di revisione della configurazione TLS per impostare l'ordine preferito e la selezione degli algoritmi.
* Verifica la validità e la attendibilità dei certificati utilizzati per l'autenticazione TLS.

## V9.1 Sicurezza della Comunicazione lato Client

Garantire che tutti i messaggi client vengano inviati su reti crittografate, utilizzando TLS 1.2 o versioni successive. 
Utilizzare strumenti aggiornati per esaminare regolarmente la configurazione client.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.1.1** | Verificare che TLS venga utilizzato per tutte le connessioni client e che non si ripieghi su comunicazioni non sicure o non crittografate. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | Utilizzare strumenti l'ultima versione dei test TLS per verificare che siano abilitate solo suite crittografiche robuste, con le suite più sicure impostate come preferite. | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | Verificare che siano abilitate solo le versioni più recenti consigliate del protocollo TLS, come TLS 1.2 e TLS 1.3. La versione più recente del protocollo TLS dovrebbe essere l'opzione preferita.	 | ✓ | ✓ | ✓ | 326 |

## V9.2 Sicurezza della Comunicazione lato Server

La comunicazione server va oltre il semplice HTTP. Devono essere implementate connessioni sicure da e verso altri sistemi, come sistemi di monitoraggio, strumenti di gestione, accesso remoto e SSH, middleware, database, mainframe, sistemi partner o sorgenti esterne. Tutte queste connessioni devono essere crittografate per evitare situazioni in cui le difese perimetrali siano robuste, ma l'intercettazione interna sia banale.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.2.1** | Verificare che le connessioni da e verso il server utilizzino certificati TLS affidabili. Se vengono utilizzati certificati auto-generati o self-signed, il server deve essere configurato per fidarsi solo di CA interne specifiche e di certificati self-signed specifici. Tutti gli altri devono essere rifiutati.	 | | ✓ | ✓ | 295 |
| **9.2.2** | Verificare che la comunicazione crittografata, come TLS, venga utilizzata per tutte le connessioni in ingresso e in uscita, incluse quelle per porte di gestione, monitoraggio, autenticazione, chiamate API o di servizi web, database, cloud, serverless, mainframe, connessioni esterne e con partner. Il server non deve ripiegare su protocolli non sicuri o non crittografati.	 | | ✓ | ✓ | 319 |
| **9.2.3** | Verificare che tutte le connessioni crittografate a sistemi esterni che coinvolgono informazioni o funzioni sensibili siano autenticate.	 | | ✓ | ✓ | 287 |
| **9.2.4** | Verificare che la revoca corretta dei certificati, come lo "Online Certificate Status Protocol (OCSP) Stapling", sia abilitata e configurata.	 | | ✓ | ✓ | 299 |
| **9.2.5** | Verificare che gli errori di connessione TLS con il backend vengano loggati.	 | | | ✓ | 544 |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* [OWASP - Pinning Guide](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)
* Notes on “Approved modes of TLS”:
    * In the past, the ASVS referred to the US standard FIPS 140-2, but as a global standard, applying US standards can be difficult, contradictory, or confusing to apply.
    * A better method of achieving compliance with section 9.1 would be to review guides such as [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) or [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known and up to date TLS evaluation tools to obtain a desired level of security.
