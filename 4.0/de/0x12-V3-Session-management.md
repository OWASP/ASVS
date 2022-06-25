# V3 Sessionmanagement

## Ziel

Das Sessionmanagement ist die Kernkomponente jeder webbasierten Anwendung oder zustandsbezogenen API, mit dem sie den Zustand für einen Benutzer oder ein Gerät, das mit ihr kommuniziert, steuert und aufrechterhält. Es ist entscheidend für die Unterscheidung verschiedener Benutzer oder Geräte. Es ändert ein zustandsloses Protokoll in ein zustandsbehaftetes. Prüfen Sie, dass eine verifizierte Anwendung die folgenden Anforderungen an das High-Level Session Management erfüllt:

* Sessions sind für jede Person einzigartig und können nicht erraten oder geteilt werden.
* Sessions werden ungültig, wenn sie nicht mehr benötigt werden.
* Sessions laufen ab, wenn sie eine bestimmte Zeit nicht aktiv sind.

Wie bereits erwähnt, wurden diese Anforderungen so angepasst, dass sie eine konforme Teilmenge ausgewählter NIST 800-63b- Maßnahmen darstellen, die sich auf gemeinsame Bedrohungen und häufig genutzte Authentifizierungsschwachstellen konzentrieren. Frühere Verifizierungsanforderungen wurden entfernt oder in den meisten Fällen so angepasst, dass sie sich stark an der Absicht der verbindlichen Anforderungen des NIST 800-63b  orientieren.

## V3.1 Grundlegende Sicherheit des Sessionmanagements

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.1.1** | Prüfen Sie, dass die Anwendung niemals Sessiontoken in URL-Parametern oder Fehlermeldungen offenbart. | ✓ | ✓ | ✓ | 598 | |

## V3.2 Session Binding

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.2.1** | Prüfen Sie, ob die Anwendung bei der Authentifizierung eines Benutzers ein neues Sessiontoken generiert. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 384 | 7.1 |
| **3.2.2** | Prüfen Sie, dass Session-Token mindestens 64 Bit Entropie aufweisen. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 331 | 7.1 |
| **3.2.3** | Prüfen Sie, dass die Anwendung Sessiontoken im Browser nur mit sicheren Methoden wie z.B. gesicherten Cookies (siehe Abschnitt 3.4) oder den HTML 5-Methoden speichert. | ✓ | ✓ | ✓ | 539 | 7.1 |
| **3.2.4** | Prüfen Sie, dass die Sessiontoken mit anerkannten kryptografischen Algorithmen generiert werden. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 331 | 7.1 |

TLS oder ein anderer sicherer Transportkanal ist für das Sessionmanagement obligatorisch. Dies wird im Kapitel Kommunikationssicherheit behandelt.

## V3.3 Beenden der Session

Die Session Timeouts wurden an NIST 800-63 angeglichen, was wesentlich längere Sitzungsauszeiten erlaubt, als die Sicherheitsstandards traditionell zulassen. Prüfen Sie die nachstehende Tabelle: Falls eine längere Zeit der Inaktivität mit dem Risiko des Geschäftsbetriebes vereinbar ist, kann sich die Obergrenze am oberen NIST-Grenzwert des Session-Timeouts orientieren.

L1 (Stufe 1) ist in diesem Zusammenhang IAL1/AAL1, L2 (Stufe 2) ist IAL2/AAL3, L3 (Stufe 3) ist IAL3/AAL3. Je kürzer die Leerlaufzeit für IAL2/AAL2 und IAL3/AAL3 ist, desto niedriger ist die Grenze der Leerlaufzeiten für das Ausloggen oder die erneute Authentifizierung zur Wiederaufnahme der Sitzung.

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.3.1** | Prüfen Sie, dass Abmeldung und Ablauf das Session-Token ungültig machen, so dass die Zurück-Taste oder eine nachgeschaltete Relying Party eine authentifizierte Sitzung auch nicht zwischen den Relying Parties wiederaufnimmt. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 613 | 7.1 |
| **3.3.2** | Wenn die Benutzer eingeloggt bleiben, Prüfen Sie, dass eine erneute Authentifizierung in regelmäßigen Abständen sowohl bei aktiver Nutzung als auch nach einer Leerlaufphase erfolgt. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | 30 Tage | 12 Stunden oder 30 Minuten Inaktivität, 2FA optional | 12 Stunden oder 15 Minuten Inaktivität, mit 2FA | 613 | 7.2 |
| **3.3.3** | Prüfen Sie, dass es die Anwendung ermöglicht, alle anderen aktiven Sitzungen nach einer erfolgreichen Kennwortänderung zu beendeen. Dies muss in der gesamten Anwendung, der föderierten Anmeldung (falls vorhanden) und bei allen Relying Parties wirksam sein. | | ✓ | ✓ | 613 | |
| **3.3.4** | Prüfen Sie, dass die Benutzer jede oder alle derzeit aktiven Sitzungen und Geräte sehen und sich von ihnen abmelden können. | | ✓ | ✓ | 613 | 7.1 |

## V3.4 Cookie-basiertes Session Management

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.4.1** | Prüfen Sie, dass bei Session-Cookies das Attribut „secure“ gesetzt ist. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 614 | 7.1.1 |
| **3.4.2** | Prüfen Sie, dass bei Session-Cookies das Attribut „HttpOnly“ gesetzt ist. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1004 | 7.1.1 |
| **3.4.3** | Prüfen Sie, dass Session-Cookies das 'SameSite'-Attribut verwenden, um die Anfälligkeit für Cross-Site Request Forgery zu begrenzen. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1275 | 7.1.1 |
| **3.4.4** | Prüfen Sie, dass Session-Cookies das Präfix „__Host-“ verwenden (siehe Referenzen), um die Vertraulichkeit von Session-Cookies zu gewährleisten. | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.5** | Falls die Anwendung unter einem Domänennamen zusammen mit anderen Anwendungen veröffentlicht wird, die Session-Cookies nutzen, welche die Sitzungscookies der geprüften Anwendung außer Kraft setzen oder offenlegen könnten, prüfen Sie, dass das Pfadattribut in den Cookies einen möglichst exakten Pfad erhält. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |

## V3.5 Tokenbasiertes Sessionmanagement

Tokenbasiertes Sessionmanagement umfasst z.B. JWT-, OAuth-, SAML- und API-Schlüssel. API-Schlüssel sind bekanntermaßen schwach und sollten im neuen Code nicht mehr verwendet werden.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.5.1** | Prüfen Sie, dass die Anwendung Benutzern erlaubt, OAuth-Token, die Vertrauensbeziehungen zu verknüpften Anwendungen herstellen, zurückzuziehen. | | ✓ | ✓ | 290 | 7.1.2 |
| **3.5.2** | Prüfen Sie, dass die Anwendung Sessiontoken anstatt statischer API-Schlüssel verwendet, außer bei Legacy-Implementierungen. | | ✓ | ✓ | 798 | |
| **3.5.3** | Prüfen Sie, dass zustandslose Session-Token digitale Signaturen, Verschlüsselung und andere Gegenmaßnahmen zum Schutz vor Manipulation, Enveloping, Wiedergabe, Null-Chiffren und Schlüsselaustausch-Angriffen verwenden. | | ✓ | ✓ | 345 | |

V3.6 Erneute Authentisierung

Dieser Abschnitt bezieht sich auf Entwickler, die den Code für die Relying Party (RP) oder den Credential Service Provider (CSP) schreiben. Wenn Sie auf eine Software vertrauen, die diese Funktionen implementiert, Prüfen Sie, dass die folgenden Punkte korrekt behandelt werden.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.6.1** | Prüfen Sie, dass die Relying Parties gegenüber den CSPs die maximale Authentifizierungszeit angeben, und dass die CSPs den Teilnehmer erneut authentifizieren, wenn sie innerhalb dieses Zeitraums keine Sitzung verwendet haben. | | | ✓ | 613 | 7.2.1 |
| **3.6.2** | Prüfen Sie, dass die CSPs die Relying Parties über das letzte Authentifizierungsereignis informieren, damit die RPs feststellen können, ob sie den Benutzer erneut authentifizieren müssen. | | | ✓ | 613 | 7.2.1 |

## V3.7 Verteidigung gegen Session Management Exploits

Es gibt eine kleine Anzahl von Angriffen auf das Sessionmanagement, von denen einige mit der Benutzerführung von Sessions zusammenhängen. Auf der Grundlage des ISO 27002 Standards haben Vorversionen des ASVS das Blockieren mehrerer gleichzeitiger Sitzungen gefordert. Das Blockieren gleichzeitiger Sitzungen ist jedoch nicht mehr zeitgemäß, nicht nur, weil die heutigen Benutzer viele Geräte haben oder die Anwendung eine API ohne Browser-Session ist, sondern auch weil in den meisten dieser Implementierungen der letzte Authentifikator – meist der Angreifer - gewinnt. Dieser Abschnitt ist eine Anleitung zum Abschrecken, Verzögern und Erkennen von Angriffen auf das Sessionmanagement.

### Beschreibung des halboffenen Angriffs

Anfang 2018 wurden mehrere Finanzinstitute durch sogenannte halboffene Angriffe kompromittiert. Die Angreifer griffen sowohl unterschiedliche Institute mit unterschiedlichen proprietären Codebasen an als auch scheinbar verschiedenen Codebasen innerhalb derselben Institute. Der halboffene Angriff macht sich einen Fehler im Design vieler Authentifizierungs-, Sessionmanagement- und Zugangskontrollsysteme zu Nutze. Die Angreifer starten einen halboffenen Angriff, indem sie versuchen, Zugangsdaten zu sperren, zurückzusetzen oder wiederherzustellen. Ein beliebtes Designmuster für das Sessionmanagement verwendet Benutzerprofile in Sessionobjekten bzw. -modellen zwischen nicht authentifiziertem, halb-authentifiziertem, z.B. Kennwortrücksetzung, vergessener Benutzername, und vollständig authentifiziertem Code wieder. Dieses Designmuster pflegt ein gültiges Sessionobjekt oder Token mit dem Profil des Opfers, einschließlich des Passwort-Hashes und der Rollen ein. Wenn die Zugriffskontrollprüfungen nicht korrekt verifizieren, dass der Benutzer vollständig angemeldet ist, kann der Angreifer als der Benutzer handeln. Angriffe könnten das Benutzerkennwort auf einen bekannten Wert ändern, die E-Mail-Adresse zur Durchführung einer gültigen Kennwortzurücksetzung aktualisieren, die Mehrfaktorauthentifizierung deaktivieren oder ein neues MFA-Gerät registrieren, API-Schlüssel offenlegen bzw. ändern und so weiter.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.7.1** | Prüfen Sie, dass die Anwendung eine gültige Login Session gewährleistet oder eine erneute Authentifizierung oder eine sekundäre Verifizierung erfordert, bevor sensible Transaktionen oder Kontenänderungen zugelassen werden. | ✓ | ✓ | ✓ | 306 | |

## Referenzen

Weitere Informationen finden Sie unter:

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#Directives)
