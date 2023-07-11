# V6 kryptographische Komponenten

## Ziel

Prüfen Sie, dass eine verifizierte Anwendung die folgenden High Level Anforderungen erfüllt:

* Alle kryptographischen Module fallen in einen sicheren Fehlerzustand und behandeln Fehler korrekt.
* Es wird ein geeigneter Zufallszahlengenerator verwendet.
* Der Zugriff auf Schlüssel wird sicher verwaltet.

## V6.1 Datenklassifizierung

Das wichtigste Gut sind die Daten, die von einer Anwendung verarbeitet, gespeichert oder übertragen werden. Führen Sie immer eine Datenschutzfolgenabschätzung durch, um die Datenschutzbedürfnisse der gespeicherten Daten korrekt einzuschätzen.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **6.1.1** | Prüfen Sie, dass sensible personenbezogene Daten, oder Daten, die unter andere gesetzliche Regelungen zur Vertraulichkeit fallen, verschlüsselt gespeichert werden. | | ✓ | ✓ | 311 |
| **6.1.2** | Prüfen Sie, dass Gesundheitsdaten, wie z. B. medizinische Aufzeichnungen, Details zu medizinischen Geräten oder deanonymisierte Forschungsaufzeichnungen, verschlüsselt gespeichert werden. | | ✓ | ✓ | 311 |
| **6.1.3** | Prüfen Sie, dass Finanzdaten, wie z.B. Konten, Zahlungsausfälle oder Kredithistorie, Steuerunterlagen, Lohnhistorie, Begünstigte oder deanonymisierte Markt- oder Forschungsaufzeichnungen verschlüsselt gespeichert werden. | | ✓ | ✓ | 311 |

## V6.2 Algorithmen

Fortschritte in der Kryptographie führen dazu, dass bisher sichere Algorithmen und Schlüssellängen nicht länger sicher genug sind, um Daten zu schützen. Daher muss es möglich sein, die Algorithmen zu ändern.

Obwohl dieser Abschnitt nicht leicht mittels Pentests geprüft werden kann, sollten Entwickler diesen gesamten Abschnitt als obligatorisch betrachten, auch wenn L1 bei den meisten Punkten fehlt.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **6.2.1** | Prüfen Sie, dass alle kryptografischen Module in einen sicheren Fehlerzustand fallen und Fehler so behandelt werden, dass keine Padding-Orakel-Angriffe möglich sind. | ✓ | ✓ | ✓ | 310 |
| **6.2.2** | Prüfen Sie, dass allgemein anerkannte oder von der Regierung freigegebene kryptografische Algorithmen, Modi und Bibliotheken anstelle von Eigenentwicklungen verwendet werden. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 327 |
| **6.2.3** | Prüfen Sie, dass der Initialisierungsvektoren, die Chiffrierkonfiguration und die Blockmodi gemäß den neuesten Empfehlungen sicher konfiguriert werden. | | ✓ | ✓ | 326 |
| **6.2.4** | Prüfen Sie, dass Zufallszahlengeneratoren, Verschlüsselungs- oder Hashalgorithmen, Schlüssellängen, Runden, Chiffren oder Modi jederzeit rekonfiguriert, aktualisiert oder ausgetauscht werden können. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 326 |
| **6.2.5** | Prüfen Sie, dass unsichere Blockmodi, wie ECB u.a., Padding-Modi, wie PKCS#1 v1.5 u.a., Algorithmen mit kleinen Blockgrößen, wie Triple-DES, Blowfish u.a., sowie schwache Hashalgorithmen, wie MD5, SHA1 u.a., nicht verwendet werden, es sei denn, dies ist aus Gründen der Rückwärtskompatibilität erforderlich. | | ✓ | ✓ | 326 |
| **6.2.6** | Prüfen Sie, dass Nonces, Initialisierungsvektoren u. ä. nicht mehr als einmal mit einem bestimmten Verschlüsselungsschlüssel verwendet werden dürfen. Die Methode der Generierung muss für den verwendeten Algorithmus geeignet sein. | | ✓ | ✓ | 326 |
| **6.2.7** | Prüfen Sie, dass verschlüsselte Daten mittels Signaturen, authentifizierte Chiffriermodi oder HMAC authentifiziert werden, um sicherzustellen, dass der Chiffriertext nicht von Unbefugten verändert wird. | | | ✓ | 326 |
| **6.2.8** | Prüfen Sie, dass alle kryptografischen Operationen zeitkonstant sind und keine „Kurzschluss“-Operationen bei Vergleichen, Berechnungen oder Rückgaben stattfinden, um Informationslecks zu vermeiden. | | | ✓ | 385 |

## V6.3 Zufallswerte

Das Erzeugen von guten Pseudo-Zufallszahlen (PRN) ist unglaublich schwer. Im Allgemeinen werden gute Entropiequellen innerhalb eines Systems schnell erschöpft, wenn sie übermäßig genutzt werden, Quellen mit weniger Entropie hingegen können zu vorhersagbaren Schlüsseln bzw. Geheimnissen führen.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **6.3.1** | Prüfen Sie, dass alle Zufallszahlen, zufälligen Dateinamen, zufälligen GUIDs und Zufallszeichenfolgen mit einem anerkannten kryptografisch sicheren Zufallszahlengenerator generiert werden, wenn diese Zufallswerte für einen Angreifer nicht zu erraten sein sollen. | | ✓ | ✓ | 338 |
| **6.3.2** | Prüfen Sie, dass zufällige GUIDs mit dem GUID v4-Algorithmus und einem kryptografisch sicheren Zufallszahlengenerator erstellt werden. GUIDs, die mit anderen Zufallszahlengeneratoren erstellt wurden, können vorhersehbar sein. | | ✓ | ✓ | 338 |
| **6.3.3** | Prüfen Sie, dass die Zufallszahlen mit der richtigen Entropie erzeugt werden, auch wenn die Anwendung unter starker Belastung steht, oder dass die Anwendung unter solchen Umständen angemessen reagiert. | | | ✓ | 338 |

## V6.4 Management von Schlüsseln und Geheimnissen

Obwohl dieser Abschnitt nicht leicht mittels Pentests getestet werden kann, sollten Entwickler diesen gesamten Abschnitt als obligatorisch betrachten, auch wenn L1 bei den meisten Punkten fehlt.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **6.4.1** | Prüfen Sie, dass eine Lösung für das Schlüsselmanagement, wie z.B. ein Schlüsseltresor, verwendet wird, um Geheimnisse sicher zu erstellen, zu speichern, die Nutzung zu kontrollieren und sie zu zerstören. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 798 |
| **6.4.2** | Prüfen Sie, dass das Schlüsselmaterial nicht in der Anwendung genutzt wird sondern ein Sicherheitsmodul kryptographische Operationen ausführt. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 320 |

## Referenzen

Weitere Informationen finden Sie unter:

* [OWASP Testing Guide 4.0: Testing for weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/README.html)
* [OWASP Cheat Sheet: Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-2](https://csrc.nist.gov/publications/detail/fips/140/2/final)
