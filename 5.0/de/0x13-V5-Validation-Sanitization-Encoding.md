# V5 Eingabeprüfung, die Bereinigung der Ausgaben und die Zeichencodierung

## Ziel

Die häufigste Sicherheitsschwachstelle von Webanwendungen ist die mangelhafte Prüfung von Eingabedaten, die vom Client oder von der Umgebung kommen, bevor sie ohne Ausgabecodierung direkt weiterverwendet werden. Diese Schwachstelle führt zu fast allen signifikanten Schwachstellen in Webanwendungen, wie z.B. Cross-Site-Scripting (XSS), SQL-Injection, Interpreter-Injection, Angriffe auf Zeichensätze oder auf das Dateisystem und schließlich Pufferüberläufe.

Prüfen Sie, dass eine verifizierte Anwendung die folgenden High-Level Anforderungen erfüllt:

* Die Architektur der Inputvalidierung und der Ausgabebereinigung haben eine abgestimmte Pipeline, um Injektionsangriffe zu verhindern.
* Die Eingabedaten werden stark typisiert, ihr Wertebereich bzw. ihre Länge wird überprüft, im Maximum werden sie bereinigt oder gefiltert.
* Die Ausgabedaten werden entsprechend dem Kontext der Daten so nah wie möglich am Interpreter codiert oder bereinigt.

In modernen Webanwendungen ist die Ausgabecodierung wichtiger denn je. In bestimmten Fällen ist es schwierig, eine robuste Eingabevalidierung umzusetzen. Daher ist die Verwendung sichererer Schnittstellen, wie parametrisierte Abfragen, Autoescape Template-Frameworks oder die sorgfältig ausgewählte Ausgabecodierung für die Sicherheit der Anwendung von entscheidender Bedeutung.

## V5.1 Eingabeprüfung

Richtig implementierte Maßnahmen zur Eingabeprüfung, die eine positive Whitelist und eine starke Datentypisierung verwenden, können mehr als 90% aller Injektion-Angriffe eliminieren. Prüfungen der Länge- und des Wertebereiches können weitere Angriffe verhindern. Während der Anwendungsarchitektur, der Design-Sprints, der Programmierung sowie der Unit- und Integrationstests muss eine sichere Eingabeprüfung eingebaut werden. Obwohl viele dieser Punkte bei Penetrationstests nicht gefunden werden können, finden sich die Ergebnisse der Nicht-Implementierung in der Regel im Abschnitt V5.3 Anforderungen an Ausgabecodierung und Injektionsverhinderung. Entwicklern und Code-Reviewern wird empfohlen, diesen Abschnitt so zu behandeln, als ob L1 für alle Elemente erforderlich wäre, um Injektion-Angriffe zu verhindern.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.1.1** | Prüfen Sie, dass die Anwendung über Abwehrmechanismen gegen Angriffe auf HTTP-Parameter verfügt, insbesondere dann, wenn das Anwendungs-Framework die Quelle der Anforderungsparameter (GET, POST, Cookies, Header oder Umgebungsvariablen) nicht unterscheidet. | ✓ | ✓ | ✓ | 235 |
| **5.1.2** | Prüfen Sie, dass Frameworks vor Angriffen durch massenhafte Parameterzuweisung schützen, oder dass die Anwendung über Gegenmaßnahmen zum Schutz vor unsicherer Parameterzuweisung verfügt, wie z.B. das Markieren von Feldern als privat oder ähnliches. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 915 |
| **5.1.3** | Prüfen Sie, dass alle Eingaben (HTML-Formularfelder, REST-Anforderungen, URL-Parameter, HTTP-Header, Cookies, Batch-Dateien, RSS-Feeds usw.) mittels positiver Validierung (Whitelisting) validiert werden. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.4** | Prüfen Sie, dass strukturierte Daten stark typisiert sind und gemäß einem definierten Schema validiert werden. Dazu gehören die erlaubten Zeichen, Länge und Muster (z. B. Kreditkarten- oder Telefonnummern, oder die Prüfung, dass zwei zusammenhängende Felder stimmig sind, z.B. Ort und Postleitzahl). ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.5** | Prüfen Sie, dass URL-Umleitungen und -Weiterleitungen nur Whitelist-Ziele zulassen, oder bei der Weiterleitung auf potenziell nicht vertrauenswürdige Inhalte einen Warnhinweis anzeigen. | ✓ | ✓ | ✓ | 601 |

## V5.2 Bereinigung und Sandboxing

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.2.1** | Prüfen Sie, dass alle nicht vertrauenswürdigen HTML-Eingaben von WYSIWYG-Editoren o.ä. ordnungsgemäß mit einer HTML-Bereinigungsbibliothek oder einer Framework-Funktion bereinigt werden. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.2.2** | Prüfen Sie, dass unstrukturierte Daten bereinigt werden, um Sicherheitsmaßnahmen wie erlaubte Zeichen und Längenbegrenzung durchzusetzen. | ✓ | ✓ | ✓ | 138 |
| **5.2.3** | Prüfen Sie, dass die Anwendung zum Schutz vor SMTP- oder IMAP-Injektion Benutzereingaben bereinigt, bevor sie an Mailsysteme weitergeleitet werden. | ✓ | ✓ | ✓ | 147 |
| **5.2.4** | Prüfen Sie, dass die Anwendung kein eval() oder andere Funktioen zur dynamischen Ausführung von Code verwendet. Wenn es keine Alternative gibt, müssen alle Benutzereingaben, die einbezogen werden, vor der Ausführung des Programms gesäubert oder per Sandbox abgegrenzt werden. | ✓ | ✓ | ✓ | 95 |
| **5.2.5** | Prüfen Sie, dass die Anwendung vor Template-Injection-Angriffen schützt, indem Sie sicherstellen, dass alle Benutzereingaben, die aufgenommen werden, bereinigt oder per Sandbox abgegrenzt werden. | ✓ | ✓ | ✓ | 94 |
| **5.2.6** | Prüfen Sie, dass die Anwendung vor SSRF-Angriffen schützt, indem sie nicht vertrauenswürdige Daten oder HTTP-Datei-Metadaten, wie z. B. Dateinamen und URL-Eingabefelder, validiert oder bereinigt. Verwenden Sie eine Whitelist von Protokollen, Domänen, Pfaden und Ports. | ✓ | ✓ | ✓ | 918 |
| **5.2.7** | Prüfen Sie, dass die Anwendung vom Benutzer bereitgestellte Scaleable Vector Graphics (SVG) von skriptfähigen Inhalten bereinigt, deaktiviert oder in Sandboxen abgrenzt, insbesondere in Bezug auf XSS, das aus Inline-Skripten und aus foreignObject resultiert. | ✓ | ✓ | ✓ | 159 |
| **5.2.8** | Prüfen Sie, dass die Anwendung vom Benutzer zur Verfügung gestellte skriptfähige Inhalte oder Inhalte von Expression Language Templates wie Markdown, CSS- oder XSL-Stylesheets, BBCode oder Ähnliches bereinigt, deaktiviert oder in Sandboxen abgrenzt. | ✓ | ✓ | ✓ | 94 |

## V5.3 Ausgabecodierung und Injektionsverhinderung

Für die Sicherheit der Anwendung ist es entscheidend, dass die Ausgabecodierung möglichst eng bei dem verwendeten Interpreter stattfindet. In der Regel wird die Ausgabecodierung nicht beibehalten, sondern dazu verwendet, die Ausgabe im entsprechenden Kontext für die sofortige Nutzung sicher zu machen. Unzureichende Ausgabecodierung führt direkt zu einer unsicheren Anwendung.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.3.1** | Prüfen Sie, dass die Ausgabecodierung für den Interpreter und den erforderlichen Kontext relevant ist. Verwenden Sie z. B. Codierer gezielt für HTML-Werte, HTML-Attribute, JavaScript, URL-Parameter, HTTP-Header, SMTP und andere, wie es der Kontext erfordert, insbesondere bei nicht vertrauenswürdigen Eingaben (z.B. Namen mit Unicode oder Apostroph, wie z.B. ねこ oder O'Hara). ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.3.2** | Prüfen Sie, dass die Ausgabecodierung den vom Benutzer gewählten Zeichensatz sowie die Spracheinstellung beibehält, so dass jeder Unicode-Zeichenpunkt gültig ist und sicher verarbeitet wird. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 176 |
| **5.3.3** | Prüfen Sie, dass kontextabhängiges, vorzugsweise automatisches Output Escaping vor reflektierten, gespeicherten und DOM-basierten XSS schützt. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 79 |
| **5.3.4** | Prüfen Sie, dass die Datenauswahl- oder Datenbankabfragen (z.B. SQL, HQL, ORM, NoSQL) parametrisierte Abfragen, ORMs, Entity Frameworks verwenden oder anderweitig vor Datenbank-Injektionsangriffen geschützt sind. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.5** | Prüfen Sie, dass dort, wo keine parametrisierten oder sichereren Mechanismen vorhanden sind, eine kontextspezifische Ausgabecodierung, z. B. SQL-Escaping, zum Schutz vor Injektionsangriffen verwendet wird. ([C3, C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.6** | Prüfen Sie, dass die Anwendung vor Angriffen mittels JSON-Injektion, JSON-eval() und Evaluierung von JavaScript-Ausdrücken schützt. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 830 |
| **5.3.7** | Prüfen Sie, dass die Anwendung vor LDAP-Injektionsschwachstellen schützt oder das spezifische Sicherheitsmaßnahmen zur Verhinderung der LDAP-Injektion implementiert wurden. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 90 |
| **5.3.8** | Prüfen Sie, dass die Anwendung vor dem Einfügen von Betriebssystemkommandos schützt und dass Betriebssystemaufrufe parametrisierte Abfragen oder eine kontextbezogene Ausgabecodierung der Befehlszeile verwenden. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 78 |
| **5.3.9** | Prüfen Sie, dass die Anwendung vor Local File Inclusion (LFI)- oder Remote File Inclusion (RFI)-Angriffen schützt. | ✓ | ✓ | ✓ | 829 |
| **5.3.10** | Prüfen Sie, dass die Anwendung gegen XPath Injection- oder XML-Injection-Angriffe schützt. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 643 |

Hinweis: Die Verwendung parametrisierter Abfragen oder des SQL-Escape ist nicht immer ausreichend: Tabellen- und Spaltennamen, ORDER BY usw. können nicht escaped werden. Die Aufnahme von escapten, vom Benutzer bereitgestellten Daten in diesen Feldern führt zu fehlgeschlagenen Abfragen oder SQL-Injektion.

Hinweis: Das SVG-Format erlaubt explizit ECMA-Skript in fast allen Kontexten, also ist es eventuell nicht möglich, alle SVG-XSS-Vektoren vollständig zu blockieren. Wenn ein SVG-Upload erforderlich ist, empfehlen wir dringend, diese hochgeladenen Dateien entweder als Text/Plain auszuliefern oder eine separate, vom Benutzer bereitgestellte, Inhaltsdomäne zu verwenden, um zu verhindern, dass ein erfolgreiches XSS die Anwendung übernimmt.

## V5.4 Speicher, Strings und Unmanaged Code

Die folgenden Anforderungen gelten nur, wenn die Anwendung eine Systemprogrammiersprache oder unmanaged Code verwendet.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.4.1** | Prüfen Sie, dass die Anwendung speichersichere Zeichenfolgen, sicherere Speicherkopien und sichere Zeigerarithmetik verwendet, um Stapel-, Puffer- oder Heap-Überläufe zu erkennen oder zu verhindern. | | ✓ | ✓ | 120 |
| **5.4.2** | Prüfen Sie, dass Format-Strings keine potenziell feindliche Eingabe annehmen und konstant sind. | | ✓ | ✓ | 134 |
| **5.4.3** | Prüfen Sie, dass Zeichen-, Bereichs- und Eingabeprüfungstechniken verwendet werden, um Ganzzahlüberläufe zu verhindern. | | ✓ | ✓ | 190 |

## V5.5 Prävention von Deserialisierungsangriffen

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **5.5.1** | Prüfen Sie, dass serialisierte Objekte Integritätsprüfungen verwenden oder verschlüsselt sind, um die Erstellung feindlicher Objekte oder die Manipulation von Daten zu verhindern. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 502 |
| **5.5.2** | Prüfen Sie, dass XML-Parser nur die restriktivste Konfiguration verwenden und das unsichere Funktionen wie die Auflösung externer Entitäten deaktiviert sind, um XXE zu verhindern. | ✓ | ✓ | ✓ | 611 |
| **5.5.3** | Prüfen Sie, dass die Deserialisierung nicht vertrauenswürdiger Daten sowohl im benutzerdefinierten Code als auch in Bibliotheken von Drittanbietern (wie JSON-, XML- und YAML-Parser) entweder verhindert oder gesichert wird. | ✓ | ✓ | ✓ | 502 |
| **5.5.4** | Prüfen Sie, dass beim Parsen von JSON in Browsern oder JavaScript-basierten Backends JSON.parse zum Parsen des JSON-Dokuments verwendet wird. Verwenden Sie kein eval() zum Parsen von JSON. | ✓ | ✓ | ✓ | 95 |

## Referenzen

Weitere Informationen finden Sie unter:

* [OWASP Testing Guide 4.0: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Cheat Sheet: Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution.html)
* [OWASP LDAP Injection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client Side Testing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client_Side_Testing/)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [XML External Entity (XXE) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)

Weitere Informationen zum Auto-Escaping finden Sie unter:

* [Reducing XSS by way of Automatic Context-Aware Escaping in Template Systems](https://googleonlinesecurity.blogspot.com/2009/03/reducing-xss-by-way-of-automatic.html)
* [AngularJS Strict Contextual Escaping](https://docs.angularjs.org/api/ng/service/$sce)
* [AngularJS ngBind](https://docs.angularjs.org/api/ng/directive/ngBind)
* [Angular Sanitization](https://angular.io/guide/security#sanitization-and-security-contexts)
* [Angular Security](https://angular.io/guide/security)
* [ReactJS Escaping](https://reactjs.org/docs/introducing-jsx.html#jsx-prevents-injection-attacks)
* [Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

Weitere Informationen zur Deserialisierung finden Sie unter:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [OWASP Deserialization of Untrusted Data Guide](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)
