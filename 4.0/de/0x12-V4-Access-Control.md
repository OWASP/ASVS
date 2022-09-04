# V4 Maßnahmen zur Zugriffssteuerung 

## Ziel

Autorisierung ist das Konzept, nur denjenigen den Zugriff auf Ressourcen zu gestatten, die diese auch nutzen dürfen. Prüfen Sie, dass eine verifizierte Anwendung die folgenden High Level Anforderungen erfüllt:

* Personen, die auf Ressourcen zugreifen, müssen dafür über gültige Berechtigungen verfügen.
* Die Benutzer sind mit einem genau definierten Satz von Rollen und Berechtigungen verbunden.
* Rollen- und Berechtigungsmetadaten sind vor Wiedereinspielen oder Manipulation geschützt.

## V4.1 Design der Allgemeinen Zugriffssteuerung

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.1.1** | Prüfen Sie, dass die Anwendung Regeln zur Steuerung der Zugriffe auf einer vertrauenswürdigen Serviceschicht durchsetzt, insbesondere wenn die clientseitige Zugriffssteuerung umgangen werden könnte. | ✓ | ✓ | ✓ | 602 |
| **4.1.2** | Prüfen Sie, dass alle Benutzer- und Datenattribute sowie Richtlinieninformationen, die von der Zugriffssteuerung verwendet werden, von den Endnutzern nicht manipuliert werden können, es sei denn, dies wird ausdrücklich genehmigt. | ✓ | ✓ | ✓ | 639 |
| **4.1.3** | Prüfen Sie, dass das Prinzip der minimalen Berechtigung gilt: Benutzer sollten nur auf die unbedingt notwendigen Funktionen, Dateien, URLs, Controller, Dienste und andere Ressourcen zugreifen können. Dies bedeutet Schutz vor Spoofing und Ausweitung der Berechtigungen. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |
| **4.1.4** | [GELÖSCHT, DUPLIKAT VON 4.1.3] | | | | |
| **4.1.5** | Prüfen Sie, dass die Zugriffssteuerungsroutinen im Fehlerfall in einen sicheren Zustand fallen. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |

## V4.2 Operative Zugriffssteuerung

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.2.1** | Prüfen Sie, dass sensible Daten und APIs vor direkten Objektangriffen geschützt sind, die auf das Erstellen, Lesen, Aktualisieren und Löschen von Datensätzen abzielen, z. B. das Erstellen oder Aktualisieren von Datensätzen einer anderen Person, das Anzeigen oder Löschen aller Datensätze. | ✓ | ✓ | ✓ | 639 |
| **4.2.2** | Prüfen Sie, dass die Anwendung oder das Framework einen starken Anti-CSRF-Mechanismus zum Schutz authentifizierter Funktionen durchsetzt, und dass eine effektive Anti-Automatisierung oder Anti-CSRF nicht authentifizierte Funktionen schützt. | ✓ | ✓ | ✓ | 352 |

## V4.3 Weitere Maßnahmen zur Zugriffssteuerung

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.3.1** | Prüfen Sie, dass administrative Schnittstellen eine geeignete Mehrfaktorauthentifizierung verwenden, um unbefugte Nutzung zu verhindern. | ✓ | ✓ | ✓ | 419 |
| **4.3.2** | Prüfen Sie, dass das Durchsuchen von Verzeichnissen deaktiviert ist, es sei denn, dies ist absichtlich gewünscht. Ferner ist das Auffinden oder die Offenlegung von Datei- oder Verzeichnis-Metadaten, wie z.B. Thumbs.db, .DS_Store, .git oder .svn-Ordner, nicht zulässig. | ✓ | ✓ | ✓ | 548 |
| **4.3.3** | Prüfen Sie, dass die Anwendung über zusätzliche Berechtigungen (z. B. Step-Up oder adaptive Authentifizierung) für risikoarme Systeme und / oder Aufgabentrennung für brisante Anwendungen verfügt, um Betrugsbekämpfungsmaßnahmen entsprechend dem Anwendungsrisiko durchzusetzen. | | ✓ | ✓ | 732 |

## Referenzen

Weitere Informationen finden Sie unter:

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Access Control](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
* [OWASP CSRF Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [OWASP REST Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
