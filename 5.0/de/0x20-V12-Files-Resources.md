# V12 Dateien und andere Ressourcen

## Ziel

Stellen Sie sicher, dass eine verifizierte Anwendung die folgenden High-Level Anforderungen erfüllt:

* nicht vertrauenswürdige Datendateien müssen angepasst und auf sichere Weise behandelt werden.
* nicht vertrauenswürdige Datendateien, die aus nicht vertrauenswürdigen Quellen stammen, werden außerhalb des Webroots und mit eingeschränkten Berechtigungen gespeichert.
           
## V12.1 Datei-Upload

Obwohl Zip-Bomben hervorragend mit Penetrationstests getestet werden können, werden sie als L2 und höher eingestuft, um die Berücksichtigung von Design und Entwicklung durch sorgfältige manuelle Tests zu fördern und einen Denial-of-Service Zustand durch automatische oder unqualifizierte manuelle Penetrationstests zu vermeiden.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.1.1** | Prüfen Sie, dass die Anwendung keine großen Dateien akzeptiert, die den Speicher füllen oder einen Denial of Service Angriff verursachen könnten. | ✓ | ✓ | ✓ | 400 |
| **12.1.2** | Prüfen Sie, dass die Anwendung gepackte Formate, wie z.B. zip, gz, docx oder odt vor dem Entpacken auf die maximal zulässige Filegröße und die maximale Anzahl Dateien überprüft. | | ✓ | ✓ | 409 |
| **12.1.3** | Prüfen Sie, dass die Dateigröße und die maximale Anzahl von Dateien pro Benutzer limitiert wird, um sicherzustellen, dass ein einzelner Benutzer den Speicher nicht mit zu vielen oder übermäßig großen Dateien füllen kann. | | ✓ | ✓ | 770 |

## V12.2 Dateiintegrität

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.2.1** | Prüfen Sie, dass Dateien aus nicht vertrauenswürdigen Quellen sowohl auf der Grundlage des Dateiinhalts als auch des erwarteten Typs validiert werden. | | ✓ | ✓ | 434 |

## V12.3 Ausführbare Dateien

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.3.1** | Prüfen Sie, dass die vom Benutzer eingereichten Metadaten der Dateinamen nicht direkt vom Filesystem des Betriebssystems oder des Frameworks genutzt werden. Weiterhin ist eine URL-API zu verwenden, um vor Path Traversal zu schützen. | ✓ | ✓ | ✓ | 22 |
| **12.3.2** | Prüfen Sie, dass die vom Benutzer eingereichten Metadaten der Dateinamen validiert oder ignoriert werden, um die Offenlegung, Erstellung, Aktualisierung oder Entfernung lokaler Dateien zu verhindern. | ✓ | ✓ | ✓ | 73 |
| **12.3.3** | Prüfen Sie, dass die vom Benutzer eingereichten Metadaten der Dateinamen validiert oder ignoriert werden, um die Offenlegung oder Ausführung von serverseitigen Dateien via Remote File Inclusion (RFI) oder Serverside Request Forgery (SSRF) Angriffen zu verhindern. | ✓ | ✓ | ✓ | 98 |
| **12.3.4** | Prüfen Sie, dass die Anwendung vor Reflective File Download (RFD) schützt, indem sie die vom Benutzer eingereichten Dateinamen in einem JSON-, JSONP- oder URL-Parameter validiert oder ignoriert. Der Content-Type-Header der Antwort muss auf text/plain gesetzt werden, und der Content-Disposition-Header muss einen festen Dateinamen haben. | ✓ | ✓ | ✓ | 641 |
| **12.3.5** | Prüfen Sie, dass nicht vertrauenswürdige Datei-Metadaten nicht direkt mit der System-API oder Bibliotheken verwendet werden, um vor OS Command Injection zu schützen. | ✓ | ✓ | ✓ | 78 |
| **12.3.6** | Prüfen Sie, dass die Anwendung keine Funktionen aus nicht vertrauenswürdigen Quellen, wie z. B. nicht verifizierte Inhaltsverteilungsnetzwerke, JavaScript-Bibliotheken, node npm-Bibliotheken oder serverseitige DLLs, enthält und ausführt. | | ✓ | ✓ | 829 |

## V12.4 Speicherung von Dateien

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.4.1** | Prüfen Sie, dass Dateien aus nicht vertrauenswürdigen Quellen mit eingeschränkten Berechtigungen und vorzugsweise mit starker Validierung außerhalb des Webroots gespeichert werden. | ✓ | ✓ | ✓ | 552 |
| **12.4.2** | Prüfen Sie, dass Dateien aus nicht vertrauenswürdigen Quellen von Antiviren-Scannern gescannt werden, um das Hochladen bekannter bösartiger Inhalte zu verhindern. | ✓ | ✓ | ✓ | 509 |

## V12.5 Download von Dateien

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.5.1** | Prüfen Sie, dass die Web-Schicht so konfiguriert ist, dass nur Dateien mit bestimmten Dateierweiterungen bedient werden, um unbeabsichtigte Informations- und Quellcode-Lecks zu vermeiden. Beispielsweise sollten Sicherungsdateien (z.B. .bak), temporäre Arbeitsdateien (z.B. .swp), komprimierte Dateien (.zip, .tar, .gz, usw.) und andere von den Editoren üblicherweise verwendete Erweiterungen blockiert werden, sofern sie nicht erforderlich sind. | ✓ | ✓ | ✓ | 552 |
| **12.5.2** | Prüfen Sie, dass direkte Anfragen an hochgeladene Dateien niemals als HTML/JavaScript-Inhalt ausgeführt werden. | ✓ | ✓ | ✓ | 434 |

## V12.6 SSRF-Schutz

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.6.1** | Prüfen Sie, dass der Web- oder Anwendungsserver mit einer Whitelist von Ressourcen oder Systemen konfiguriert ist, an die der Server Anfragen senden oder Daten/Dateien laden kann. | ✓ | ✓ | ✓ | 918 |

## Referenzen

Weitere Informationen finden Sie unter:

* [File Extension Handling for Sensitive Information](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
* [Reflective file download by Oren Hafif](https://www.trustwave.com/Resources/SpiderLabs-Blog/Reflected-File-Download---A-New-Web-Attack-Vector/)
* [OWASP Third Party JavaScript Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html)
