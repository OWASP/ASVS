# V11 Fachliche Funktionalität

## Ziel

Stellen Sie sicher, dass eine verifizierte Anwendung die folgenden High-Level Anforderungen erfüllt:
 
* Der Fluss der Geschäftslogik ist sequentiell: Er wird der Reihe nach verarbeitet und kann nicht umgangen werden.
* Die Geschäftslogik enthält Grenzen zur Erkennung und Verhinderung automatisierter Angriffe, wie z. B. kontinuierliche kleine Geldtransfers oder das Hinzufügen von einer Million Freunden, einer nach dem anderen, etc.
* Hochwertige Modelle der Geschäftslogik haben Missbrauchsfälle und böswillige Akteure in Betracht gezogen und sind gegen Spoofing, Manipulation, Abstreiten, Informationspreisgabe und die Erweiterung von Rechten immun.
           
## V11.1 Sicherheit der fachlichen Funktionen

Die Sicherheit der Geschäftslogik ist für jede Anwendung zu individuell, als dass dafür jemals eine einzige Checkliste erstellt werden könnte. Die Sicherheit der Geschäftslogik muss so konzipiert sein, dass sie vor voraussichtlichen externen Bedrohungen Schutz bietet - sie kann nicht durch Webanwendungs-Firewalls oder sichere Kommunikation hinzugefügt werden. Wir empfehlen die Verwendung von Threat Modeling während der Design-Sprints, z.B. mit dem OWASP Cornucopia oder ähnlichen Tools.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **11.1.1** | Prüfen Sie, dass die Anwendung nur Geschäftslogikflüsse für denselben Benutzer in sequentieller Schrittfolge und ohne das Überspringen von Schritten verarbeitet.| ✓ | ✓ | ✓ | 841 |
| **11.1.2** | Prüfen Sie, dass die Anwendung nur Abläufe der Geschäftslogik verarbeitet, wenn alle Schritte in realistischer menschlicher Zeit bearbeitet werden, d.h. die Transaktionen werden nicht zu schnell durch automatisierte Angreifer eingereicht.| ✓ | ✓ | ✓ | 799 |
| **11.1.3** | Prüfen Sie, dass die Anwendung über angemessene Grenzen für bestimmte Geschäftsaktionen oder Transaktionen verfügt, die für jeden Benutzer korrekt durchgesetzt werden. | ✓ | ✓ | ✓ | 770 |
| **11.1.4** | Prüfen Sie, dass die Anwendung über ausreichende Maßnahmen gegen automatische Nutzung verfügt, um Daten-Exfiltration, übermäßige Anforderungen an die Geschäftslogik, übermäßige Datei-Uploads oder Denial-of-Service Angriffe zu erkennen und sich dagegen zu schützen. | ✓ | ✓ | ✓ | 770 |
| **11.1.5** | Prüfen Sie, ob die Anwendung Grenzen der Geschäftslogik oder eine Validierung zum Schutz vor wahrscheinlichen Geschäftsrisiken oder Bedrohungen aufweist, die mit Hilfe von Threat Modeling oder ähnlichen Methoden ermittelt wurden. | ✓ | ✓ | ✓ | 841 |
| **11.1.6** | Prüfen Sie, dass die Anwendung nicht unter TOCTOU oder anderen Race-Conditions für sensible Operationen leidet. | | ✓ | ✓ | 367 |
| **11.1.7** | Prüfen Sie die Anwendungsmonitore auf ungewöhnliche Ereignisse oder Aktivitäten aus der Sicht der Geschäftslogik. Zum Beispiel auf Versuche, Aktionen durchzuführen, die außerhalb der Reihe sind, oder Aktionen, die ein normaler Benutzer niemals versuchen würde. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 754 |
| **11.1.8** | Prüfen Sie, dass die Anwendung über konfigurierbare Web Warnmeldungen verfügt, wenn automatisierte Angriffe oder ungewöhnliche Aktivitäten entdeckt werden. | | ✓ | ✓ | 390 |

## Referenzen

Weitere Informationen finden Sie unter:

* [OWASP Web Security Testing Guide 4.1: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README.html)
* Schutz gegen automatische Angriffe kann auf vielfältige Weise erreicht werden, z.B.: [OWASP AppSensor](https://github.com/jtmelton/appsensor) and [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* Der [OWASP AppSensor](https://github.com/jtmelton/appsensor) kann auch bei der Erkennung und der Bewältigung von Angriffen helfen.
* [OWASP Cornucopia](https://owasp.org/www-project-cornucopia/)
