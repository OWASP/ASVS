# V7 Fehlerbehandlung und Protokollierung

## Ziel

Das primäre Ziel der Fehlerbehandlung und Protokollierung ist es, nützliche Informationen für den Benutzer, die Administratoren und die Incident Response Teams bereitzustellen. Das Ziel besteht nicht darin, große Mengen von Protokollen zu erstellen, sondern hochwertige Protokolle, die mehr Informationen als nutzloses Rauschen enthalten.

Hochwertige Protokolle enthalten oft sensible Daten und müssen gemäß den lokalen Datenschutzgesetzen oder -richtlinien geschützt werden. Dies sollte beinhalten:

* Keine sensiblen Informationen zu protokollieren, es sei denn, dies ist ausdrücklich erforderlich.
* Sicherzustellen, dass alle protokollierten Informationen sicher gehandhabt und gemäß ihrer Datenklassifizierung geschützt werden.
* Sicherzustellen, dass die Protokolle nicht für immer gespeichert werden, sondern eine möglichst kurze Lebensdauer haben.

Wenn Protokolle personenbezogene oder sensible Daten enthalten, werden sie für Angreifer sehr attraktiv.

Es ist ferner wichtig zu gewährleisten, dass die Anwendung in sichere Fehlerzustände fällt und dass Fehler keine unnötigen Informationen offenbaren.

## V7.1 Protokollinhalt

Die Protokollierung sensibler Informationen ist gefährlich - die Protokolle werden selbst sensibel und müssen verschlüsselt werden. Sie unterliegen Aufbewahrungsrichtlinien und müssen bei Sicherheitsaudits offengelegt werden. Prüfen Sie, dass nur die notwendigen Informationen in den Protokollen aufbewahrt werden, jedoch auf keinen Fall Zahlungen, Anmeldedaten, einschließlich Sessiontoken, sensible oder personenbezogene Informationen.

Dieser Abschnitt deckt OWASP Top 10 2017:A10 ab. Weil er nicht durch Penetrationstests verifizierbar ist, sollen:

* Entwickler die vollständige Einhaltung dieses Abschnitts sicherstellen, als ob alle Punkte mit L1 gekennzeichnet wären.
* Penetrationstester die vollständige Einhaltung aller Punkte durch Befragung, Screenshots oder Zusicherungen validieren.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **7.1.1** | Prüfen Sie, dass die Anwendung keine Anmeldeinformationen oder Zahlungsdetails protokolliert. Sessiontoken sollten nur in einer irreversiblen, gehashten Form in Protokollen gespeichert werden. ([C9, C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 532 |
| **7.1.2** | Prüfen Sie, dass die Anwendung keine sonstigen sensiblen Daten protokolliert, die z. B. gemäß Datenschutzgesetzen oder den einschlägigen Sicherheitsrichtlinien als solche definiert werden. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 532 |
| **7.1.3** | Prüfen Sie, dass die Anwendung sicherheitsrelevante Ereignisse, einschließlich erfolgreicher und fehlgeschlagener Authentifizierungsereignisse, Fehler bei der Zugriffskontrolle, Deserialisierungsfehler und Fehler bei der Eingabeprüfung protokolliert. ([C5, C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 778 |
| **7.1.4** | Prüfen Sie, dass jedes Protokollereignis die notwendigen Informationen enthält, um bei einem Vorfall eine detaillierte Untersuchung der Timeline zu ermöglichen. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 778 |

## V7.2 Protokollbearbeitung

Die rechtzeitige Protokollierung ist entscheidend für Auditereignisse, Triage und Eskalation. Prüfen Sie, dass die Anwendungsprotokolle klar sind und entweder lokal oder per Versand an ein Fernüberwachungssystem leicht überwacht und analysiert werden können.

Dieser Abschnitt deckt OWASP Top 10 2017:A10 ab. Weil er nicht durch Penetrationstests verifizierbar ist, sollen:

* Entwickler die vollständige Einhaltung dieses Abschnitts sicherstellen, als ob alle Punkte mit L1 gekennzeichnet wären.
* Penetrationstester die vollständige Einhaltung aller Punkte durch Befragung, Screenshots oder Zusicherungen validieren.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **7.2.1** | Prüfen Sie, dass alle Authentifizierungsentscheidungen protokolliert werden, ohne dass sensible Sitzungstoken oder Passwörter gespeichert werden. Dies sollte auch die relevanten Metadaten umfassen, die für Sicherheitsuntersuchungen benötigt werden. | | ✓ | ✓ | 778 |
| **7.2.2** | Prüfen Sie, dass alle Authentifizierungen protokolliert werden können, und dass alle fehlgeschlagenen Versuche protokolliert werden. Dies sollte die relevanten Metadaten umfassen, die für Sicherheitsuntersuchungen benötigt werden. | | ✓ | ✓ | 285 |

## V7.3 Schutz von Protokollen

Protokolle, die einfach geändert oder gelöscht werden können, sind für Sicherheitsuntersuchungen nutzlos. Die Offenlegung von Protokollen kann interne Details über die Anwendung oder die darin enthaltenen Daten enthüllen. Schützen Sie Protokoll sorgfältig vor unbefugter Offenlegung, Änderung oder Löschung.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **7.3.1** | Prüfen Sie, dass alle Komponenten Daten angemessen codieren, um Log-Injektions-Angriffe zu verhindern. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 117 |
| **7.3.2** | [GELÖSCHT, DUPLIKAT VON 7.3.1] | | | | |
| **7.3.3** | Prüfen Sie, dass die Protokolle vor unbefugtem Zugriff und Änderungen geschützt werden. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 200 |
| **7.3.4** | Prüfen Sie, dass die Zeitquellen mit der richtigen Zeit und Zeitzone synchronisiert sind. Erwägen Sie ernsthaft die Protokollierung ausschließlich in UTC, wenn die Systeme global sind, damit die forensische Analyse nach dem Vorfall unterstützt wird. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

Hinweis: Das korrekte Codieren von Logeinträgen (7.3.1) ist mit automatisierten Tools und Penetrationstests schwer zu testen, aber Architekten, Entwickler und Quellcodeprüfer sollten sie dennoch als L1-Anforderung betrachten.

## V7.4 Fehlerbehandlung

Der Zweck der Fehlerbehandlung besteht darin, dass die Anwendung sicherheitsrelevante Ereignisse zur Überwachung, Triage und Eskalation bereitstellen kann. Ihr Zweck ist nicht die Erstellung von Protokollen. Bei der Protokollierung sicherheitsrelevanter Ereignisse ist sicherzustellen, dass das Protokoll zielgerichtet ist und dass es durch SIEM- oder Analysesoftware ausgewertet werden kann.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **7.4.1** | Prüfen Sie, dass bei Auftreten eines unerwarteten oder sicherheitsrelevanten Fehlers eine generische Meldung angezeigt wird. Ggf. kann die Meldung eine ID enthalten, die dem Supportpersonal die Untersuchung erleichtert. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 210 |
| **7.4.2** | Prüfen Sie, dass die Ausnahmebehandlung in der gesamten Codebasis verwendet wird, um erwartete und unerwartete Fehlerbedingungen zu berücksichtigen. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 544 |
| **7.4.3** | Prüfen Sie, dass ein Fehlerbehandlungsdienst der letzten Instanz definiert ist, der alle nicht behandelten Ausnahmen abfängt. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 431 |

Hinweis: Bestimmte Sprachen, wie z.B. Swift und Go - und durch gängige Designpraxis - viele funktionale Sprachen, unterstützen keine Ausnahmen oder letztinstanzliche Fehlerbehandlung. In diesem Fall sollten Architekten und Entwickler anderweitig sicherstellen, dass Anwendungen außergewöhnliche, unerwartete oder sicherheitsrelevante Ereignisse sicher handhaben können.

## Referenzen

Weitere Informationen finden Sie unter:

* [OWASP Testing Guide 4.0 content: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README.html)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
