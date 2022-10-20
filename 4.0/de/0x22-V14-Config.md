# V14 Konfiguration

## Ziel

Stellen Sie sicher, dass eine geprüfte Anwendung mit den folgenden Merkmalen ausgestattet ist:

* Eine sichere und automatisierbare Buildumgebung.
* Ein sicheres Management von Drittanbieterbibliotheken, Abhängigkeiten und Konfigurationen, so dass veraltete oder unsichere Komponenten nicht in die Anwendung integriert werden.

Die Konfiguration der Anwendung sollte „out of the box“ sicher für den jeweils geplanten Einsatzzweck sein.

## V14.1 Build- und Deployprozess

Build Pipelines sind die Grundlage für wiederholbare Sicherheit. Jedes Mal, wenn etwas Unsicheres entdeckt wird, kann es im Quellcode, den Build- oder Deploymentskripten behoben und automatisch getestet werden. Wir befürworten nachdrücklich die Verwendung von Buildpipelines mit automatischen Sicherheits- und Abhängigkeitsprüfungen, die den Build ggf. unterbrechen, um zu verhindern, dass bekannte Sicherheitsprobleme in der Produktion angewendet werden. Unregelmäßig durchgeführte manuelle Schritte führen direkt zu vermeidbaren Sicherheitsfehlern.

Da die Branche zu einem DevSecOps-Modell übergeht, ist es wichtig, die kontinuierliche Verfügbarkeit und Integrität der Bereitstellung und Konfiguration zu gewährleisten, um einen bekannten funktionierenden (known good) Zustand zu erreichen. In der Vergangenheit dauerte es Tage bis Monate, wenn ein System gehackt wurde, um nachzuweisen, dass kein weiteres Eindringen stattgefunden hatte. Heute, mit dem Aufkommen der softwaredefinierten Infrastruktur, schnellen A/B-Deployment ohne Ausfallzeiten und automatisierten, containerisierten Builds, ist es möglich, automatisch und kontinuierlich einen „known good“-Ersatz für jedes kompromittierte System zu erstellen, zu härten und einzusetzen. Sind noch traditionelle Modelle vorhanden, müssen manuelle Schritte zur Härtung und Sicherung dieser Konfiguration erfolgen, damit die kompromittierten Systeme schnell durch hochintegrierte, sichere Systeme ersetzt werden können.

Um die Anforderungen dieses Abschnitts einzuhalten, ist ein automatisiertes Buildsystem und der Zugriff auf Build- und Deploymentskripte erforderlich.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.1.1** | Prüfen Sie, dass die Build- und Deploymentprozesse auf sichere und wiederholbare Weise durchgeführt werden, z. B. durch CI-/CD-Automatisierung, automatisiertes Konfigurationsmanagement und automatisierte Deploymentskripte. | | ✓ | ✓ | |
| **14.1.2** | Prüfen Sie, dass die Compilerflags so konfiguriert sind, dass sie alle verfügbaren Pufferüberlaufschutzmechanismen und Warnungen aktivieren, einschließlich der Stackrandomisierung, der Verhinderung der Datenausführung und des Buildabbruchs, wenn ein(e) unsichere(r) Pointer, Speicher, Formatstring, Integer- oder Stringoperationen gefunden wird. | | ✓ | ✓ | 120 |
| **14.1.3** | Prüfen Sie, dass die Serverkonfiguration gemäß den Empfehlungen des verwendeten Anwendungsservers und Frameworks gehärtet wird. | | ✓ | ✓ | 16 |
| **14.1.4** | Prüfen Sie, dass die Anwendung, die Konfiguration und alle Abhängigkeiten mit Hilfe automatisierter Deploymentskripte wieder installiert werden können, indem sie innerhalb eines angemessenen Zeitraums aus einem dokumentierten und getesteten Runbook erstellt oder aus Backups zeitnah wiederhergestellt werden können. | | ✓ | ✓ | |
| **14.1.5** | Prüfen Sie, dass autorisierte Administratoren die Integrität aller sicherheitsrelevanten Konfigurationen überprüfen können, um Manipulationen zu erkennen. | | | ✓ | |

## V14.2 Management von Abhängigkeiten

Die Verwaltung von Abhängigkeiten ist für den sicheren Betrieb jeder Art von Anwendung von entscheidender Bedeutung. Das Versäumnis, veraltete oder unsichere Abhängigkeiten auf dem aktuellen Stand zu halten, ist die eigentliche Ursache für die bisher größten und teuersten Angriffe.

Hinweis: Auf Stufe 1 bezieht sich die Einhaltung von 14.2.1 auf Beobachtungen oder Feststellungen von Client- und anderen Bibliotheken und Komponenten und nicht auf die genauere statische Codeanalyse oder Abhängigkeitsanalyse zur Buildzeit. Diese genaueren Techniken könnten bei Bedarf durch Befragung festgestellt werden.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.2.1** | Prüfen Sie, dass alle Komponenten auf dem neuesten Stand sind, am besten mit einem Abhängigkeitsprüfer zur Build- oder Kompilierzeit. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1026 |
| **14.2.2** | Prüfen Sie, dass alle nicht benötigten Funktionen, Dokumentationen, Beispiele und Konfigurationen entfernt werden. | ✓ | ✓ | ✓ | 1002 |
| **14.2.3** | Prüfen Sie, dass die Integrität externen Inhaltes durch Subresource Integrity (SRI) überprüft wird, wenn Anwendungsassets wie JavaScript-Bibliotheken, CSS oder Web-Fonts extern, z.B. bei einem Content Delivery Network oder bei einem externen Anbieter, gehostet werden. | ✓ | ✓ | ✓ | 829 |
| **14.2.4** | Prüfen Sie, dass Komponenten Dritter aus bekannten, vertrauenswürdigen und kontinuierlich gepflegten Repositories stammen. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 829 |
| **14.2.5** | Prüfen Sie, dass eine Softwarestückliste (Bill of Materials, SBOM) aller genutzten Bibliotheken von Drittanbietern geführt wird. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **14.2.6** | Prüfen Sie, dass die Angriffsfläche durch Sandboxing oder Einkapselung von Bibliotheken von Drittanbietern reduziert wird, damit die Anwendung nur die erforderliche Funktionalität erhält. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |

## V14.3 Offenlegung von Informationen

Konfigurationen für die Produktion sollten gehärtet werden. So schützen sie gegen gängige Angriffe wie Debugkonsolen, und legen die Messlatte für Cross Site Scripting (XSS) und Remote File Inclusion (RFI) Angriffe höher. Triviale Schwachstellen bei der Informationserfassung, die das unwillkommene Kennzeichen vieler Penetrationstestreports sind, werden so beseitigt. Viele dieser Probleme werden selten als signifikantes Risiko eingestuft, sondern sind mit anderen Schwachstellen verkettet. Wenn diese Probleme nicht standardmäßig vorhanden sind, wird die Messlatte für einen erfolgreichen Angriff deutlich höher gelegt.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.3.1** | [GELÖSCHT, DUPLIKAT VON 7.4.1] | | | | |
| **14.3.2** | Prüfen Sie, dass die Debugmodi von Web- und Anwendungsserver sowie Anwendungsframework in der Produktion deaktiviert sind, um Sicherheitslücken durch Debugfunktionen oder Entwicklerkonsolen zu vermeiden. | ✓ | ✓ | ✓ | 497 |
| **14.3.3** | Prüfen Sie, dass die HTTP-Header und HTTP-Antworten keine detaillierten Versionsinformationen von Systemkomponenten enthalten. | ✓ | ✓ | ✓ | 200 |

## V14.4 HTTP Security Header

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.4.1** | Prüfen Sie, dass jede HTTP-Antwort einen Content Type Header enthält. Für die Content types text/*, /+xml oder application/xml sollten ein sicherer Zeichensatz (z. B. UTF-8, ISO 8859-1) angeben sein. Der Inhalt muss zum angegebenen Content Type Header passen. | ✓ | ✓ | ✓ | 173 |
| **14.4.2** | Prüfen Sie, dass alle API-Antworten die Content-Disposition: attachment; filename="api.json" Header oder einen anderen geeigneten Dateinamen für den Inhaltstyp enthalten. | ✓ | ✓ | ✓ | 116 |
| **14.4.3** | Prüfen Sie, dass ein Content Security Policy (CSP) Response Header vorhanden ist, die dazu beiträgt, die Auswirkungen von XSS-Angriffen wie HTML-, DOM-, JSON- und JavaScript-Injektionsschwachstellen abzuschwächen. | ✓ | ✓ | ✓ | 1021 |
| **14.4.4** | Prüfen Sie, dass alle Antworten X-Content-Type-Optionen: nosniff Header enthalten. | ✓ | ✓ | ✓ | 116 |
| **14.4.5** | Prüfen Sie, dass ein HTTP Strict-Transport-Security Header in allen Antworten und für alle Unterdomänen enthalten ist, z. B. Strict-Transport-Security: max-age=15724800; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **14.4.6** | Prüfen Sie, dass ein geeigneter Referrer-Policy Header enthalten ist, um das Veröffentlichen sensibler Informationen über den Referer Header zu vermeiden. | ✓ | ✓ | ✓ | 116 |
| **14.4.7** | Prüfen Sie, dass der Inhalt einer Webanwendung nicht standardmäßig in Seiten Dritter eingebunden werden kann. Das Einbinden der exakten Ressourcen ist nur erlaubt, wenn nötig. Dabei sind passende Content-Security-Policy: frame-ancestors und X-Frame-Options Response Header zu nutzen. | ✓ | ✓ | ✓ | 1021 |

## V14.5 Prüfung der HTTP Request Header

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **14.5.1** | Prüfen Sie, dass der Anwendungsserver nur die von der Anwendung oder der API verwendeten HTTP-Methoden akzeptiert, einschließlich der Pre-Flight-OPTIONS. Alle ungültigen Request sollten ins Log geschrieben werden oder einen Alarm auslösen. | ✓ | ✓ | ✓ | 749 |
| **14.5.2** | Prüfen Sie, dass der bereitgestellte Origin Header nicht für Authentifizierungs- oder Zugriffskontrollentscheidungen verwendet wird, da der Origin Header von einem Angreifer leicht geändert werden kann. | ✓ | ✓ | ✓ | 346 |
| **14.5.3** | Prüfen Sie, dass der CORS-Access-Control-Allow-Origin Header eine strikte Whitelist mit vertrauenswürdigen Domains verwendet und den "null"-Ursprung nicht unterstützt. | ✓ | ✓ | ✓ | 346 |
| **14.5.4** | Prüfen Sie, dass HTTP-Header, die von einem vertrauenswürdigen Proxy oder SSO-Geräten, wie z. B. einem Bearer-Token, hinzugefügt wurden, von der Anwendung authentifiziert werden. | | ✓ | ✓ | 306 |

## Referenzen

Weitere Informationen finden Sie unter:

* [OWASP Web Security Testing Guide 4.1: Testing for HTTP Verb Tampering](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* [Reflected File Download attacks](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf) zeigt, wie durch Hinzufügen der Content-Disposition und der "filename" Option in die API-Antwort viele Angriffe, die auf verschiedenen Interpretationen des MIME-Types durch Client und Server beruhen, unterbunden werden können.
* [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Sandboxing third party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
