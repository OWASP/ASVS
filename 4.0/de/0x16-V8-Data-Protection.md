# V8 Schutz von Informationen

## Ziel

Es gibt drei Schlüsselelemente für die Informationssicherheit: Vertraulichkeit, Integrität und Verfügbarkeit. Dieser Standard geht davon aus, dass die Informationssicherheit auf einem vertrauenswürdigen System, wie z.B. einem Server, durchgesetzt wird, das gehärtet wurde und ausreichend geschützt ist.

Anwendungen müssen davon ausgehen, dass alle Benutzergeräte in irgendeiner Weise gefährdet sind. Wenn eine Anwendung sensible Informationen auf unsicheren Geräten wie gemeinsam genutzten Computern, Telefonen und Tablets überträgt oder speichert, ist die Anwendung dafür verantwortlich, dass die auf diesen Geräten gespeicherten Daten verschlüsselt werden und nicht so einfach unrechtmäßig erlangt, verändert oder offengelegt werden können.

Prüfen Sie, dass eine verifizierte Anwendung die folgenden High-Level Anforderungen erfüllt:

* Vertraulichkeit: Daten sollten sowohl während der Übertragung als auch bei der Speicherung vor unbefugter Beobachtung oder Offenlegung geschützt werden.
* Integrität: Daten sollten vor böswilliger Erstellung, Änderung oder Löschung durch unbefugte Angreifer geschützt werden.
* Verfügbarkeit: Die Daten sollten für autorisierte Benutzer nach Bedarf verfügbar sein.

## V8.1 Allgemeines

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.1.1** | Prüfen Sie, dass die Anwendung sensible Daten davor schützt, in Serverkomponenten wie Load-Balancern, Proxies u.ä. zwischengespeichert zu werden. | | ✓ | ✓ | 524 |
| **8.1.2** | Prüfen Sie, dass alle serverseitigen temporären Kopien sensibler Daten vor unbefugtem Zugriff geschützt oder nach dem Zugriff des autorisierten Benutzers auf die sensiblen Daten bereinigt/invalidiert werden. | | ✓ | ✓ | 524 |
| **8.1.3** | Prüfen Sie, dass die Anwendung die Anzahl der Parameter in einer Anfrage, wie z.B. versteckte Felder, Ajax-Variablen, Cookies und Header-Werte minimiert. | | ✓ | ✓ | 233 |
| **8.1.4** | Prüfen Sie, dass die Anwendung eine abnormale Anzahl von Anfragen, z.B. nach IP, Benutzer, Gesamtzahl pro Stunde oder Tag o. ä., erkennt und Alarm auslöst. | | ✓ | ✓ | 770 |
| **8.1.5** | Prüfen Sie, dass wichtige Daten regelmäßig gesichert werden und dass die Wiederherstellung regelmäßig geübt wird. | | | ✓ | 19 |
| **8.1.6** | Prüfen Sie, dass die Backups sicher aufbewahrt werden, um zu verhindern, dass Daten gestohlen oder verfälscht werden. | | | ✓ | 19 |

## V8.2 Clientseitiger Schutz

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.2.1** | Prüfen Sie, dass die Anwendung Anti-Caching-Header sendet, damit sensible Daten in modernen Browsern nicht zwischengespeichert werden. | ✓ | ✓ | ✓ | 525 |
| **8.2.2** | Prüfen Sie, dass die im clientseitigen Speicher (z. B. lokaler HTML5-Speicher, Sitzungsspeicher, IndexedDB oder Cookies) gespeicherten Daten keine sensiblen Daten enthalten. | ✓ | ✓ | ✓ | 922 |
| **8.2.3** | Prüfen Sie, dass authentifizierte Daten aus dem Client-Speicher, z. B. dem Browser-DOM, gelöscht werden, nachdem der Client geschlossen oder die Sitzung beendet wurde. | ✓ | ✓ | ✓ | 922 |

## V8.3 Personenbezogene Daten

Dieser Abschnitt trägt dazu bei, sensible Daten vor unbefugtem Erstellen, Lesen, Ändern oder Löschen zu schützen. Voraussetzung ist die Einhaltung von V4-Zugriffskontrollmaßnahmen, insbesondere V4.2. So erfordert zum Beispiel der Schutz von personenbezogenen Daten vor unbefugten Veränderungen oder Offenlegung die Einhaltung von V4.2.1. Bitte halten Sie sich an diesen Abschnitt und an V4, um eine vollständige Abdeckung zu erreichen.

Hinweis: Datenschutzbestimmungen und -gesetze wie die EU-Datenschutzgrundverordnung oder die Australian Privacy Principles APP-11 wirken sich direkt darauf aus, wie die Speicherung, Nutzung und Übertragung von personenbezogenen Daten in der Anwendung umgesetzt werden muss. Dies reicht von einfachen Ratschlägen bis hin zu schweren Strafen. Bitte prüfen Sie Ihre lokalen Gesetze und Vorschriften und wenden Sie sich bei Bedarf an einen Datenschutzspezialisten.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.3.1** | Prüfen Sie, dass sensible Daten im HTTP-Textkörper oder in Headern an den Server gesendet werden, und dass die Query-String-Parameter aller HTTP-Requests keine sensiblen Daten enthalten. | ✓ | ✓ | ✓ | 319 |
| **8.3.2** | Prüfen Sie, dass die Benutzer ihre Daten bei Bedarf entfernen oder exportieren können. | ✓ | ✓ | ✓ | 212 |
| **8.3.3** | Prüfen Sie, dass die Benutzer in verständlicher Sprache über die Erfassung und Verwendung der bereitgestellten personenbezogenen Daten informiert werden und dass die Benutzer ihr Einverständnis zur Verwendung dieser Daten gegeben haben, bevor diese verwendet werden. | ✓ | ✓ | ✓ | 285 |
| **8.3.4** | Prüfen Sie, dass alle von der Anwendung erstellten und verarbeiteten personenbezogenen Daten identifiziert wurden und dass eine Regelung für den Umgang mit diesen Daten vorhanden ist. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 200 |
| **8.3.5** | Prüfen Sie, dass bei Zugriff auf personenbezogene Daten geprüft wird - ohne die Daten selbst zu protokollieren - ob die Daten gemäß den einschlägigen Datenschutzrichtlinien erfasst werden oder ob eine Protokollierung des Zugriffs erforderlich ist. | | ✓ | ✓ | 532 |
| **8.3.6** | Prüfen Sie, dass die im Speicher enthaltenen Informationen überschrieben werden, sobald sie nicht mehr benötigt werden, um Memory-Dump-Angriffe abzuschwächen. | | ✓ | ✓ | 226 |
| **8.3.7** | Prüfen Sie, dass zu verschlüsselnde Informationen mit anerkannten Algorithmen verschlüsselt werden, die sowohl Vertraulichkeit als auch Integrität gewährleisten. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 327 |
| **8.3.8** | Prüfen Sie, dass personenbezogene Daten in Bezug auf die Datenspeicherung klassifiziert werden, so dass alte oder veraltete Daten automatisch, nach einem Zeitplan oder je nach Situation gelöscht werden können. | | ✓ | ✓ | 285 |

Wenn es um den Datenschutz geht, sollte man in erster Linie an die Massenextraktion oder -modifikation oder an eine übermäßige Nutzung denken. Viele Social-Media-Systeme erlauben beispielsweise nur das Hinzufügen von 100 neuen Freunden pro Tag, aber es ist nicht wichtig, aus welchem System diese Anfragen kommen. Eine Banking-Platt-form sollte vielleicht mehr als 5 Transaktionen pro Stunde blockieren, welche mehr als 1000 Euro an externe Institu-te überweisen. Jedes System hat sehr unterschiedliche Anforderungen. Deshalb muss man bei der Entscheidung, was „abnormal“ ist, das Bedrohungsmodell und das Geschäftsrisiko berücksichtigen. Wichtige Kriterien sind hierbei die Fähigkeit, solche abnormalen Massenaktionen zu erkennen, abzuwenden oder vorzugsweise zu blockieren.

## Referenzen

Weitere Informationen finden Sie unter:

* [Nutzen SIe die Website securityheaders.com, um Ihre Site zu testen.](https://securityheaders.io)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [Übersicht über die Datenschutz-Grundverordnung der Europäischen Union (DSGVO/ GDPR)](https://edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
