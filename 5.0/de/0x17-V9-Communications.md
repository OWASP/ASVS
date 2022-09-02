# V9 Kommunikation

## Ziel

Eine verifizierte Anwendung erfüllt die folgenden High-Level Anforderungen:

* Unabhängig von der Brisanz der Daten wird bei der Übertragung stets TLS oder eine starke Verschlüsselung verwendet.
* Es werden die aktuellsten Empfehlungen werden verwendet, ins Besondere:
  * Konfigurationen der Algorithmen
  * bevorzugt zu verwendende Algorithmen. 
* schwache oder bald veraltende Algorithmen werden am besten gar nicht, höchstens aber mit geringster Priorität genutzt
* Veraltete oder unsichere Algorithmen werden deaktiviert.

Weiterhin sollten sollten Sie stets:
* auf dem aktuellsten Stand bleiben, da sich die Empfehlungen zur sicheren TLS-Konfiguration häufig ändern. Dies kann auch auf Grund von katastrophalen Angriffen auf Algorithemn geschehen.
* die aktuellsten Versionen der TLS-Testtools zur Prüfung der Konfiguration nutzen.
* regelmäßig die Konfiguration testen, um sicherzustellen, dass die Sicherheit der Kommunikation jederzeit gewährleistet ist.

## V9.1 Kommunikationssicherheit des Clients

Stellen Sie sicher, dass alle Nahrichten des Clients mit TLS 1.2 oder neuer verschlüsselt werden.
Nutzen Sie regelmäßig die aktuellen Testwerkzeuge, um die Clientkonfiguration zu testen.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **9.1.1** | Prüfen Sie, dass der Client stets TLS-Verbindungen verwendet, das nicht auf unsichere oder unverschlüsselte Konfigurationen zurückfallen. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | Prüfen Sie mit aktuellen TLS-Testtools, dass nur starke Algorithmen und Protokolle genutzt werden. Dabei sind die stärksten Algorithmen und neuesten Protokollversionen zu bevorzugen. | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | Prüfen Sie, dass nur die aktuell empfohlenen Versionen der TLS-Protokolle, also TLS 1.2 und TLS 1.3, genutzt werden. Die neueste Version ist dabei zu bevorzugen. | ✓ | ✓ | ✓ | 326 |

## V9.2 Sicherheit der Serverkommunikation

Serverkommunikation ist mehr als nur HTTP. Es müssen sichere Verbindungen zu und von anderen Systemen - wie Überwachungssysteme, Management-Tools, Fernzugriff und ssh, Middleware, Datenbank, Mainframes, Partner- oder externe Quellsysteme eingerichtet werden. All diese müssen verschlüsselt werden, um zu verhindern, dass sie nach außen schwer aber nach innen kinderleicht abzufangen sind.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **9.2.1** | Prüfen Sie, dass Verbindungen zum und vom Server vertrauenswürdige TLS-Zertifikate verwenden. Werden intern generierte oder selbstsignierte Zertifikate verwendet, muss der Server so konfiguriert werden, dass er nur bestimmten internen CAs vertraut. Alle anderen müssen abgelehnt werden. | | ✓ | ✓ | 295 |
| **9.2.2** | Prüfen Sie, dass eine verschlüsselte Kommunikation wie TLS für alle ein- und ausgehenden Verbindungen, einschließlich für Management-Ports, Über-wachung, Authentifizierung, API- oder Webservice-Calls, Datenbank-, Cloud-, serverlose, Mainframe-, externe und Partnerverbindungen verwendet wird. Der Server darf nicht auf unsichere oder unverschlüsselte Protokolle zurückgreifen. | | ✓ | ✓ | 319 |
| **9.2.3** | Prüfen Sie, dass alle verschlüsselten Verbindungen zu externen Systemen, die sensible Informationen oder Funktionen beinhalten, authentifiziert sind. | | ✓ | ✓ | 287 |
| **9.2.4** | Prüfen Sie, dass eine ordnungsgemäßer Zertifikatsperre wie z. B. das Online Certificate Status Protocol Stapling aktiviert und konfiguriert ist. | | ✓ | ✓ | 299 |
| **9.2.5** | Prüfen Sie, dass TLS-Verbindungsfehler in das Backend protokolliert werden. | | | ✓ | 544 |

## Referenzen

Weitere Informationen finden Sie unter:

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* [OWASP - Pinning Guide](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)
* Notes on “Approved modes of TLS”:
    * In the past, the ASVS referred to the US standard FIPS 140-2, but as a global standard, applying US standards can be difficult, contradictory, or confusing to apply.
    * A better method of achieving compliance with section 9.1 would be to review guides such as [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) or [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known and up to date TLS evaluation tools to obtain a desired level of security.

* Hinweise zu „Anerkannten TLS-Modi”: 
    * In der Vergangenheit bezog sich der ASVS auf den US-Standard FIPS 140. Als globaler Standard kann die Anwendung von US-Standards allerdings schwierig, widersprüchlich oder verwirrend sein.  
    * Eine bessere Methode, um die Einhaltung des Abschnittes 9.1 zu erreichen, wäre die Überprüfung von Leitfäden wie [Mozillas serverseitigem TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) oder die [Erstellung  anerkannt sicherer Konfigurationen](https://mozilla.github.io/server-side-tls/ssl-config-generator/) und die Verwendung bekannter TLS-Evaluierungs-Tools wie Sslyze, verschiedener Schwachstellen-Scanner oder vertrauenswürdiger TLS-Online-Assessment Services, um ein gewünschtes Sicherheitsniveau zu erreichen. In Sicherheitstests sehen wir die Nicht-Konformität zu diesem Abschnitt durch die Verwendung veralteter oder unsicherer Algorithmen, dem Fehlen einer perfekten Forward Secrecy, veralteten oder unsicheren SSL-Protokollen, schwachen bevorzugten Algorithmen usw.
    * Für Deutschland veröffentlicht das BSI die [Technische Richtlinie TR-02102 Kryptographische Verfahren: Empfehlungen und Schlüssellängen](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr02102/tr02102_node.html) als Richtlinie für die Verwendung von TLS sowie zur Nutzung sicherer Algorithmen und Schlüssellängen.