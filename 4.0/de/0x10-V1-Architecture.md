# V1 Architektur, Design und Threat Modeling

## Ziel

In vielen Organisationen ist die Sicherheitsarchitektur fast in Vergessenheit geraten. Die Tage des Enterprise Architekten sind im Zeitalter von DevSecOps vorbei. Der Bereich der Anwendungssicherheit muss aufholen, agile Sicherheitsprinzipien übernehmen und gleichzeitig wichtige Grundsätze der Sicherheitsarchitektur wieder in die Softwareentwicklung einführen. Architektur ist keine Implementierung, sondern die Art und Weise, über ein Problem nachzudenken, das potenziell viele verschiedene aber keine einzig richtige Antwort hat. Nur allzu oft wird Sicherheit zu unflexibel betrachtet, und man verlangt von den Entwicklern, den Code auf eine bestimmte Art und Weise zu schreiben, obwohl diese vielleicht eine viel bessere Möglichkeit kennen, das Problem zu lösen. Es gibt keine einzig richtige, einfache Lösung für die Architektur. Jeder, der anderes behauptet, tut dem Softwareengineering keinen Gefallen.

Eine spezifische Implementierung einer Webanwendung wird wahrscheinlich während ihrer gesamten Lebensdauer kontinuierlich überarbeitet, ihre Architektur hingegen wird sich kaum ändern, sondern sich nur langsam entwickeln. Die Sicherheitsarchitektur hingegen ist identisch - wir brauchen Authentifizierung heute, wir brauchen Authentifizierung morgen, und wir werden sie in fünf Jahren brauchen. Treffen wir heute fundierte Entscheidungen, können wir viel Aufwand, Zeit und Geld sparen, wenn wir architekturkonforme Lösungen auswählen und wiederverwenden. So wurde beispielsweise vor einem Jahrzehnt Mehrfaktorauthentifizierung nur selten implementiert.

Hätten Entwickler in einen einzigen, sicheren Identitätsprovider investiert, wie z.B. SAML Federated Identity, könnte der Identitätsprovider angepasst werden, um neue Anforderungen wie die Umsetzung des NIST 800-63 einzubeziehen, ohne die Schnittstellen der ursprünglichen Anwendung zu ändern. Wenn viele Anwendungen die gleiche Sicherheitsarchitektur und damit die gleiche Komponente nutzen, profitieren sie alle gleichzeitig von diesem Upgrade. SAML wird jedoch nicht immer die beste oder geeignetste Authentifizierungslösung bleiben - es muss möglicherweise gegen andere Lösungen ausgetauscht werden, wenn sich die Anforderungen ändern. Solche Änderungen sind entweder kompliziert und so kostspielig wie eine komplette Neuentwicklung oder ohne Sicherheitsarchitektur schlichtweg unmöglich.

In diesem Kapitel behandelt der ASVS die primären Aspekte jeder soliden Sicherheitsarchitektur: Verfügbarkeit, Vertraulichkeit, Integrität, Nichtabstreitbarkeit und Datenschutz. All diese Sicherheitsprinzipien müssen eingebaut sein und allen Anwendungen innewohnen. Es ist entscheidend, Sicherheit zeitig im Entwicklungsprozess zu integrieren. Das beginnt bei der Befähigung der Softwareentwickler mittels Checklisten für sichere Programmierung, Betreuung und Schulung. Es führt über Programmierung und Tests, dem Buildprozess, der Inbetriebnahme, der Konfiguration und dem Betrieb bis hin zu unabhängigen Tests, die sichern, dass alle Sicherheitsmaßnahmen vorhanden und funktionsfähig sind. Der letzte Schritt war früher alles, was wir als Branche getan haben, aber das reicht nicht mehr aus, wenn Entwickler mehrmals am Tag Änderungen in der Produktionsumgebung durchführen. Anwendungssicherheitsexperten müssen mit agilen Techniken Schritt halten, was bedeutet, dass sie Entwicklertools übernehmen, lernen zu programmieren und mit Entwicklern zusammenarbeiten müssen, anstatt das Projekt Monate später zu kritisieren, nachdem alle anderen bereits weitergemacht haben.

## V1.1 Der sichere Softwareentwicklungszyklus

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.1.1** | Prüfen Sie, dass der SDLC die Sicherheit in allen Entwicklungsphasen berücksichtigt. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **1.1.2** | Prüfen Sie, dass für Designänderung oder Sprintplanung eine Bedrohungsanalyse stattfand, um Bedrohungen zu identifizieren, Gegenmaßnahmen zu planen und umzusetzen sowie passende Sicherheitstests zu planen. | | ✓ | ✓ | 1053 |
| **1.1.3** | Prüfen Sie, dass alle Userstories und alle Merkmale funktionale Sicherheitsanforderungen enthalten, z.B. „Als Benutzer sollte ich mein Profil anzeigen und bearbeiten können. Ich sollte nicht in der Lage sein, das Profil eines anderen anzusehen oder zu bearbeiten“. | | ✓ | ✓ | 1110 |
| **1.1.4** | Prüfen Sie die Dokumentation und Erläuterung aller Sicherheitsgrenzen, Komponenten und wichtigen Datenflüsse der Anwendung. | | ✓ | ✓ | 1059 |
| **1.1.5** | Prüfen Sie die Definition und Sicherheitsanalyse der High Level Architektur der Anwendung und aller verbundenen Remoteservices. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1059 |
| **1.1.6** | Prüfen Sie, dass Sicherheitsmaßnahmen zentralisiert, einfach, geprüft, sicher und wiederverwendbar implementiert worden sind. Dies vermeidet doppelte, fehlende, unwirksame oder unsichere Maßnahmen. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 637 |
| **1.1.7** | Prüfen Sie die Verfügbarkeit einer Checkliste für die sichere Programmierung, Sicherheitsanforderungen, eines Leitfadens oder Richtlinien für alle Entwickler und Tester. | | ✓ | ✓ | 637 |

## V1.2 Architektur der Authentifizierung

Beim Entwurf der Authentifizierung spielt es keine Rolle, ob Sie über eine starke, hardwareunterstützte Mehrfaktorauthentifizierung verfügen, wenn ein Angreifer ein Konto zurücksetzen kann, indem er ein Callcenter anruft und auf allgemein bekannte Fragen antwortet. Beim Nachweis der Identität müssen alle Authentifizierungswege die gleiche Stärke haben.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.2.1** | Prüfen Sie die Nutzung spezifischer Betriebssystemkonten bzw. solcher mit minimalen Berechtigungen für alle Komponenten, Dienste und Server. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 250 |
| **1.2.2** | Prüfen Sie, dass die Kommunikation zwischen Anwendungskomponenten, einschließlich APIs, Middleware und Datenschichten, authentifiziert wird. Komponenten sollten die minimal notwendigen Berechtigungen haben. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 306 |
| **1.2.3** | Prüfen Sie, dass die Anwendung einen einzigen geprüften und sicheren Authentifizierungsmechanismus verwendet, der auf eine starke Authentifizierung erweitert werden kann und über ein ausreichendes Logging und Monitoring verfügt, um Einbrüche oder Missbrauch zu erkennen. | | ✓ | ✓ | 306 |
| **1.2.4** | Prüfen Sie, dass alle Authentifizierungspfade und Identitätsmanagement-APIs eine einheitliche Stärke der Authentifizierung implementieren, so dass es keine schwächeren Alternativen pro Anwendungsrisiko gibt. | | ✓ | ✓ | 306 |

## V1.3 Architektur des Sessionmanagements

Dies ist ein Platzhalter für zukünftige architektonische Anforderungen.

## V1.4 Architektur der Zugriffskontrolle

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.4.1** | Prüfen Sie, dass Zugriffskontrollen von vertrauenswürdigen Stellen, wie z.B. Accesscontrol Gateways, Servern oder serverlosen Funktionen, ausgeführt werden. Implementieren Sie Zugriffskontrollen niemals am Client. | | ✓ | ✓ | 602 |
| **1.4.2** | [GELÖSCHT, NICHT UMSETZBAR] | | | | |
| **1.4.3** | [GELÖSCHT, DUPLIKAT VON 4.1.3] | | | | |
| **1.4.4** | Prüfen Sie, dass die Anwendung mit einer einzigen und gut erprobten Zugriffssteuerung auf geschützte Daten und Ressourcen zugreift. Alle Anfragen müssen diesen einen Weg nutzen, um Kopieren und Einfügen oder unsichere Alternativpfade zu vermeiden. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 284 |
| **1.4.5** | Prüfen Sie, dass eine attribut- oder merkmalsbasierte Zugriffskontrolle verwendet wird, die die Berechtigung des Benutzers zum Zugriff auf ein Merkmal oder Datenelement und nicht nur seine Rolle prüft. Die Berechtigungen sollten weiterhin über Rollen vergeben werden. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 275 |

## V1.5 Architektur des Ein- und Ausgabemanagements

Mit der Version 4.0 haben wir uns von dem Begriff „serverseitig“ als Synonym für Vertrauensgrenzen verabschiedet. Die Vertrauensgrenze spielt noch immer eine wichtige Rolle: Entscheidungen von nicht vertrauenswürdigen Clients können umgangen werden. Allerdings hat sich die Stelle, an der die Entscheidungen getroffen werden, bei heutigen Mainstreamarchitekturen dramatisch verändert. Wenn im ASVS der Begriff „vertrauenswürdige Serviceschicht“ verwendet wird, meinen wir daher jede vertrauenswürdige Stelle, unabhängig von ihrer Position, wie z.B. einen Mikroservice, eine serverlose API, serverseitig, eine vertrauenswürdige API auf einem Client, das über sichere Bootmechanismen verfügt, eine Partner- oder externe APIs und so weiter.

Die Bezeichnung „nicht vertrauenswürdiger Client“ bezieht sich auf Frontendtechnologien, wie z.B. der Darstellungsschicht. Der Begriff „Serialisierung“ soll sich nicht nur Daten, wie Felder in JSON-Strukturen, beziehen sondern ebenso auf komplexe Objekte, welche Programmlogik enthalten können.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.5.1** | Prüfen Sie, dass die Ein- und Ausgabeanforderungen klar definieren, wie die Daten auf der Grundlage des Typs, des Inhalts und der anwendbaren Gesetze, Vorschriften und anderen Richtlinien zu verarbeiten sind. | | ✓ | ✓ | 1029 |
| **1.5.2** | Prüfen Sie, dass bei der Kommunikation mit nicht vertrauenswürdigen Clients keine Serialisierung verwendet wird. Ist dies nicht möglich, prüfen Sie, dass die Integrität geprüft und bei sensiblen Daten auch verschlüsselt wird, um Deserialisierungsangriffe oder Object Injection Angriffe zu verhindern. | | ✓ | ✓ | 502 |
| **1.5.3** | Prüfen Sie, dass die Eingabevalidierung in einer vertrauenswürdigen Serviceschicht durchgesetzt wird. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 602 |
| **1.5.4** | Prüfen Sie, dass die Ausgabecodierung in der Nähe des oder durch den Interpreter erfolgt, für den sie bestimmt ist. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 116 |

## V1.6 Architektur kryptographischer Maßnahmen

Anwendungen müssen mit einer starken kryptographischen Architektur entworfen werden, um die Datenbestände gemäß ihrer Klassifizierung zu schützen. Alles zu verschlüsseln ist Verschwendung, nichts zu verschlüsseln ist fahrlässig. Es muss ein Gleichgewicht gefunden werden, in der Regel bei dem architektonischen oder High Level Design, den Designsprints oder den Architectural Spikes. Die sichere Implementierung kryptographischer Methoden, die nach und nach entworfen oder nachgerüstet werden, ist zwangsläufig viel teurer, als sie von Beginn an einzubauen.

Architektonische Anforderungen sind in der gesamten Codebasis integriert und lassen sich daher schwer in Unit- oder Integrationstests prüfen. Die architektonischen Anforderungen müssen in den Programmierstandards für die gesamten Programmierphase berücksichtigt werden und sollten während der Sicherheitsarchitektur, bei Peer- oder Code-Reviews oder bei Retrospektiven überprüft werden.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.6.1** | Prüfen Sie, dass es eine explizite Richtlinie für das Schlüsselmanagement gibt, und dass der Lebenszyklus eines kryptografischen Schlüssels konform zu einem Standard für das Schlüsselmanagement wie NIST SP 800-57 ist. | | ✓ | ✓ | 320 |
| **1.6.2** | Prüfen Sie, dass Nutzer kryptografischer Dienste Schlüssel und andere Geheimnisse mit Hilfe von Schlüsseltresoren oder API-basierte Alternativen schützen. | | ✓ | ✓ | 320 |
| **1.6.3** | Prüfen Sie, dass alle Schlüssel und Passwörter ersetzbar und Teil eines genau definierten Prozesses zur Neuverschlüsselung sensibler Daten sind. | | ✓ | ✓ | 320 |
| **1.6.4** | Prüfen Sie, dass clientseitige Geheimnisse, wie symmetrische Schlüssel, Passwörter oder API-Token, architektonisch als unsicher betrachtet werden. Sie dürfen nicht zum Schutz sensibler Daten verwendet werden. | | ✓ | ✓ | 320 |

## V1.7 Architektur von Fehlerbehandlung, Protokollierung und Audit

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.7.1** | Prüfen Sie, dass im gesamten System Herangehensweise und Protokollformat einheitlich sind. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1009 |
| **1.7.2** | Prüfen Sie, dass die Protokolle zur Analyse, Erkennung, Alarmierung und Eskalation sicher übertragen werden - vorzugsweise an ein eigenständiges System. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

## V1.8 Architektonische Anforderungen zur Einhaltung des Datenschutzes

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.8.1** | Prüfen Sie, dass alle sensiblen Daten identifiziert und klassifiziert werden. | | ✓ | ✓ | |
| **1.8.2** | Prüfen Sie, dass für alle Schutzklassen entsprechende Anforderungen existieren, z. B. an die Vertraulichkeit, die Integrität, Aufbewahrung, Datenschutz etc. und dass diese in der Architektur angewendet werden. | | ✓ | ✓ | |

## V1.9 Architektur der Kommunikationsverbindungen

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.9.1** | Prüfen Sie, dass die Anwendung die Kommunikation zwischen Komponenten verschlüsselt, insbesondere wenn sich diese in verschiedenen Containern, Systemen, Standorten oder Cloudanbietern befinden. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 319 |
| **1.9.2** | Prüfen Sie, dass die Anwendungskomponenten die Authentizität beider Seiten einer Kommunikationsverbindung verifizieren, um Man-in-the-Middle-Angriffe zu verhindern. Beispielsweise sollten die Anwendungskomponenten TLS-Zertifikate und Zertifikatsketten verifizieren. | | ✓ | ✓ | 295 |

## V1.10 Architektonische Anforderungen zum Schutz vor unbefugten Änderungen

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.10.1** | Prüfen Sie, dass das Quellcodeverwaltungssystem sicherstellt, dass Check-Ins mit Issues oder Änderungstickets einhergehen. Das Quellcodeverwaltungssystem sollte über eine Zugriffskontrolle und identifizierbare Benutzer verfügen, um Änderungen nachverfolgen zu können. | | ✓ | ✓ | 284 |

## V1.11 Architektur der Geschäftslogik

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.11.1** | Prüfen Sie die Definition und Dokumentation aller Anwendungskomponenten auf die von ihnen bereitgestellten Fach- oder Sicherheitsfunktionen. | | ✓ | ✓ | 1059 |
| **1.11.2** | Prüfen Sie, dass alle geschäftskritischen Abläufe, inkl. der Authentifizierung, des Sessionmanagements und der Zugriffssteuerung stets synchronisiert sind. | | ✓ | ✓ | 362 |
| **1.11.3** | Prüfen Sie, dass alle geschäftskritischen Abläufe, einschließlich der Authentifizierung, des Sessionmanagements und der Zugriffssteuerung thread-sicher und sicher gegen TOCTOU Race Conditions sind. | | | ✓ | 367 |

## V1.12 Sicheres Datei Upload

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.12.1** | [GELÖSCHT, DUPLIKAT VON 12.4.1] | | | | |
| **1.12.2** | Prüfen Sie, dass vom Benutzer hochgeladene Dateien - sofern sie angezeigt oder von der Anwendung heruntergeladen werden müssen - entweder durch Oktett-Stream-Downloads oder von einer nicht verwandten Domäne, wie z.B. einem Cloud File Storage Bucket, bereitgestellt werden. Implementieren Sie geeignete Sicherheitsmaßnahmen für Dateiinhalte, um das Risiko von Angriffen mit Hilfe der hochgeladenen Datei zu reduzieren. | | ✓ | ✓ | 646 |

## V1.13 API-Architektur

Dies ist ein Platzhalter für zukünftige architektonische Anforderungen.

## V1.14 Architektonische Anforderungen an die Konfiguration

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.14.1** | Prüfen Sie die Trennung von Komponenten unterschiedlicher Vertrauensstufen durch gut durchdachte Sicherheitsmaßnahmen, Firewallregeln, API-Gateways, Reverseproxies, cloudbasierte Sicherheitsgruppen o.ä. | | ✓ | ✓ | 923 |
| **1.14.2** | Prüfen Sie, dass digitale Signaturen, vertrauenswürdige Verbindungen und vertrauenswürdige Downloadquellen verwendet werden, um Binärdaten auf Endgeräte zu verteilen. | | ✓ | ✓ | 494 |
| **1.14.3** | Prüfen Sie, dass die Buildpipeline vor veralteten oder unsicheren Komponenten warnt und entsprechende Maßnahmen ergreift. | | ✓ | ✓ | 1104 |
| **1.14.4** | Prüfen Sie, dass die Buildpipeline einen Schritt enthält, um die sichere Deploymentversion der Anwendung automatisch zu erstellen und zu verifizieren, insbesondere wenn die Anwendungsinfrastruktur softwarebasiert ist, wie z. B. Cloudumgebungen. | | ✓ | ✓ | |
| **1.14.5** | Prüfen Sie, dass Anwendungen auf der Netzwerkebene voneinander separiert sind, z.B. per Sandbox oder Container, um Angreifer auszubremsen und davon abzuhalten, andere Anwendungen anzugreifen, insbesondere wenn sie sensible Aktionen wie eine Deserialisierung durchführen. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |
| **1.14.6** | Prüfen Sie, dass die Anwendung keine nicht unterstützten, unsicheren oder veralteten clientseitigen Technologien wie NSAPI-Plugins, Flash, Shockwave, ActiveX, Silverlight, NACL oder clientseitige Java-Applets verwendet. | | ✓ | ✓ | 477 |

## Referenzen

Weitere Informationen finden Sie unter:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
