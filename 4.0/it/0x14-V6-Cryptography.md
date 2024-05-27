# V6 Crittografia per lo storage

## Obiettivo del controllo

Verificare che un'applicazione soddisfi i seguenti requisiti di alto livello:

* Tutti i moduli crittografici falliscono in modo sicuro e gli errori vengono gestiti correttamente.
* Viene utilizzato un generatore di numeri casuali appropriato.
* L'accesso alle chiavi è gestito in modo sicuro.

## V6.1 Classificazione dei Dati

L'asset più importante è il dato elaborato, memorizzato o trasmesso da un'applicazione. Eseguire sempre una valutazione di impatto sulla privacy per classificare correttamente le esigenze di protezione dei dati memorizzati.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.1.1** | Verificare che i dati personali regolamentati siano memorizzati crittografati a riposo, come le Informazioni di identificazione personale (PII), le informazioni personali sensibili o i dati considerati soggetti al GDPR dell'UE. | | ✓ | ✓ | 311 |
| **6.1.2** | Verificare che i dati sanitari regolamentati siano memorizzati crittografati a riposo, come cartelle cliniche, dettagli sui dispositivi medici o record di ricerca deanonimizzati. | | ✓ | ✓ | 311 |
| **6.1.3** | Verificare che i dati finanziari regolamentati siano memorizzati crittografati a riposo, come conti finanziari, inadempienze o cronologie creditizie, registri fiscali, cronologie retributive, beneficiari o record di mercato o di ricerca deanonimizzati. | | ✓ | ✓ | 311 |

## V6.2 Algoritmi

I recenti progressi in crittografia fanno sì che algoritmi e lunghezze delle chiavi in precedenza sicuri non siano più sicuri o sufficienti a proteggere i dati. Pertanto, dovrebbe essere possibile cambiare algoritmo.

Sebbene questa sezione non sia facilmente testabile da penetration testing, gli sviluppatori dovrebbero considerare obbligatoria l'intera sezione anche se il livello 1 è assente nella maggior parte degli elementi.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.2.1** | Verificare che tutti i moduli crittografici falliscano in modo sicuro e che gli errori vengano gestiti in modo tale da non consentire attacchi Oracle Padding. | ✓ | ✓ | ✓ | 310 |
| **6.2.2** | Verificare che vengano utilizzati algoritmi, modalità e librerie crittografiche comprovate dal settore o approvate dal governo, invece della crittografia creata da zero. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 327 |
| **6.2.3** | Verificare che il vettore di inizializzazione, la configurazione e le modalità dei cifrari a blocchi siano impostate in modo sicuro utilizzando le pratiche più recenti. | | ✓ | ✓ | 326 |
| **6.2.4** | Verificare che numeri casuali, algoritmi di crittografia o hashing, lunghezze delle chiavi, round, cifrari o modalità possano essere riconfigurati, aggiornati o scambiati in qualsiasi momento, per proteggersi da violazioni crittografiche. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 326 |
| **6.2.5** | Verificare che non vengano utilizzate modalità a blocchi insicure (ad esempio ECB, ecc.), modalità di padding (ad esempio PKCS # 1 v1.5, ecc.), cifrari con dimensioni del blocco ridotte (ad esempio Triple-DES, Blowfish, ecc.) e algoritmi di hashing deboli (ad esempio MD5, SHA1, ecc.) a meno che non siano necessari per la compatibilità con versioni precedenti. | | ✓ | ✓ | 326 |
| **6.2.6** | Verificare che i nonce, i vettori di inizializzazione e altri valori monouso non vengano utilizzati più di una volta con una determinata chiave crittografica. Il metodo di generazione deve essere appropriato per l'algoritmo utilizzato. | | ✓ | ✓ | 326 |
| **6.2.7** | Verificare che i dati crittografati siano autenticati tramite firme, modalità di cifratura autenticate o HMAC per garantire che il testo cifrato non venga alterato da una terzo non autorizzato. | | | ✓ | 326 |
| **6.2.8** | Verificare che tutte le operazioni crittografiche siano a tempo costante, senza operazioni di 'cortocircuito' per confronti, calcoli o restituzione di valori, per evitare di rivelare informazioni. | | | ✓ | 385 |

## V6.3 Valori casuali

La generazione di numeri pseudo-casuali (PRNG) veramente casuale è incredibilmente difficile da ottenere. In generale, buone fonti di entropia all'interno di un sistema si esauriranno rapidamente se utilizzate eccessivamente, ma fonti con meno casualità possono portare a chiavi e segreti prevedibili.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.3.1** | Verificare che tutti i numeri casuali, nomi di file, GUID e stringhe siano generati utilizzando il generatore di numeri casuali crittograficamente sicuro approvato dal modulo crittografico quando si desidera che questi valori casuali non siano indovinabili da un attaccante. | | ✓ | ✓ | 338 |
| **6.3.2** | Verificare che i GUID casuali siano creati utilizzando l'algoritmo GUID v4 e un generatore di numeri pseudo-casuali crittograficamente sicuro (CSPRNG). I GUID creati utilizzando altri generatori di numeri pseudo-casuali potrebbero essere prevedibili. | | ✓ | ✓ | 338 |
| **6.3.3** | Verificare che i numeri casuali vengano creati con un'entropia adeguata anche quando l'applicazione è sotto carico elevato, oppure che l'applicazione si degradi adeguatamente in tali circostanze. | | | ✓ | 338 |

## V6.4 Gestione dei Segreti

Sebbene questa sezione non sia facilmente testabile tramite penetration testing, gli sviluppatori dovrebbero considerarla obbligatoria nella sua interezza, anche se il livello 1 è assente nella maggior parte delle voci.

| # | Descrizione | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.4.1** | Verificare che venga utilizzata una soluzione di gestione dei segreti, come un key vault, per creare, archiviare, controllare l'accesso e distruggere i segreti in modo sicuro. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 798 |
| **6.4.2** | Verificare che il materiale crittografico non venga esposto all'applicazione ma utilizzi invece un modulo di sicurezza isolato, come un vault, per le operazioni crittografiche. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 320 |

## Riferimenti

Per approfondimenti, consultare:

* [OWASP Testing Guide 4.0: Testing for weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/README.html)
* [OWASP Cheat Sheet: Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-2](https://csrc.nist.gov/publications/detail/fips/140/2/final)
