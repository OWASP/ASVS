# V2: Authentifizierung

## Ziel

Authentifizierung ist die Bestätigung einer Eigenschaft, wie z.B. der Identität einer Person oder eines Gerätes. Sie muss u.a. widerstandsfähig gegen Nachahmer sein und Passwörter sicher übertragen. Als der ASVS zum ersten Mal freigegeben wurde, waren Benutzername und Passwort die gebräuchlichste Form der Authentifizierung außerhalb von Hochsicherheitssystemen. Die Mehrfaktorauthentifizierung (MFA) wurde in Sicherheitskreisen allgemein akzeptiert, aber anderswo nur selten verlangt. Mit zunehmenden Passwortverletzungen wurde die Idee, dass Benutzernamen vertraulich und Passwörter unbekannt sind, als Sicherheitsmaßnahme unhaltbar. NIST 800‑63 betrachtet beispielsweise Benutzernamen und wissensbasierte Authentifizierung als öffentliche Informationen, SMS- und E-Mail-Benachrichtigungen als [„eingeschränkte“ Authentifikatoren (restricted authenticators)](https://pages.nist.gov/800-63-FAQ/#q-b1) und Passwörter als praktisch unsicher. Diese Realität macht wissensbasierte Authentifikatoren, SMS- und E-Mail-Wiederherstellung, Passwortverlauf, Komplexität und Passwortwechselstrategien nutzlos. Diese Maßnahmen waren schon immer wenig hilfreich und zwangen die Benutzer oft dazu, sich alle paar Monate schwache Passwörter auszudenken. Mit der Veröffentlichung von über 5 Milliarden Kombinationen von Benutzernamen und Passwörtern ist es an der Zeit, sich weiter zu entwickeln.

Daher haben sich die Kapitel „Authentifizierung“ und „Session Management“ am meisten verändert. Das Ausrichten an einem effektiven, evidenzbasierten Vorbild wird für viele eine Herausforderung sein, das ist völlig in Ordnung. Wir müssen jetzt den Übergang zu einer Zukunft ohne Passwort einleiten.

## NIST 800-63 - Ein moderner, evidenzbasierter Authentifizierungsstandard

[NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) ist ein moderner, evidenzbasierter Standard. Der Standard ist für alle Organisationen auf der ganzen Welt hilfreich, besonders relevant jedoch für US-Behörden und Organisationen, die mit ihnen in Verbindung stehen.

Wenn man die Authentifizierung mit Benutzername und Passwort gewohnt ist, kann die Terminologie von NIST 800‑63 kann anfangs etwas verwirrend sein. Fortschritte in der modernen Authentifizierung sind notwendig, daher müssen wir eine Terminologie einführen, die in Zukunft allgemein üblich sein wird. Wir verstehen aber auch die Verständnisschwierigkeiten, die sich ergeben, bis alle sich auf diese neuen Begriffe eingestellt haben. Wir haben viele Anforderungen des NIST umformuliert, um die Absicht der Anforderung und nicht die Buchstaben der Anforderung zu erfüllen. Zum Beispiel verwendet der ASVS den Begriff „Passwort“, wenn das NIST von einem „gespeicherten Geheimnis“ spricht.

Die Kapitel V2: Authentifizierung, V3: Session Management und in geringerem Maße auch V4: Zugriffskontrollen wurden so angepasst, dass sie eine standardkonforme Teilmenge der Maßnahmen gemäß NIST 800-63b sind, die sich auf allgemeine Bedrohungen und häufig ausgenutzte Authentifizierungsschwachstellen konzentrieren. Muss NIST 800-63 vollständig erfüllt werden, so nutzen Sie bitte NIST 800-63 direkt.

### Auswahl einer geeigneten NIST AAL-Stufe

Bei der Erstellung des ASVS 4.0 haben wir ASVS L1 den Anforderungen von NIST AAL1, L2 zu AAL2 und L3 zu AAL3 zugeordnet. Dabei ist zu beachten, dass hier die ASVS-Stufe 1 nicht mehr die Voraussetzung für alle anderen Stufen ist: Soll die Anwendung beispielsweise NIST AAL3 erfüllen, so muss in den Abschnitten V2 und V3 Session Management die Stufe 3 - und nur die Stufe 3 - gewählt werden.  Die Auswahl des NIST AAL sollte gemäß den Richtlinien von NIST 800-63b erfolgen, wie sie in [NIST800-63b, Abschnitt 6.2](https://pages.nist.gov/800-63-3/sp800-63-3.html#AAL_CYOA) unter *Selecting AAL* beschrieben sind.

## Legende

Anwendungen können immer die Anforderungen der aktuellen Stufe überschreiten, insbesondere wenn eine moderne Authentifizierung auf der Roadmap einer Anwendung steht. In den Vorgängerversionen erforderte der ASVS obligatorisch eine Mehrfaktorauthentifizierung (MFA). NIST tut dies nicht. Daher haben wir in diesem Kapitel eine Option eingeführt, die anzeigt, wenn der ASVS eine Eigenschaft empfiehlt. Dabei gilt:

| Symbol | Beschreibung |
| :--: | :-- |
| | Nicht erforderlich |
| o | Empfohlen |
| ✓ | Erforderlich |

## V2.1 Passwortsicherheit

Passwörter, in NIST 800-63 als „gespeicherte Geheimnisse“ bezeichnet, umfassen Passwörter, PINs, Entsperrmuster, die Auswahl des richtigen Bildelements sowie Passphrasen. Sie werden im Allgemeinen als „Wissen“ betrachtet und oft als Einfaktor-Authentifikatoren verwendet. Die weitere Verwendung der Einfaktor-Authentifizierung steht vor erheblichen Herausforderungen, z.B.: Milliarden von öffentlich verfügbaren Kombinationen von Benutzername und Passwort, Standardpasswörtern, schwachen Passwörtern, Rainbowtables sowie Wörterbücher der häufigsten Passwörter.

Anwendungen sollten die Benutzer nachdrücklich dazu ermutigen, sich mittels Mehrfaktor-Authentifizierung anzumelden und ihnen erlauben, Token, wie z.B. FIDO- oder U2F-Token, die sie bereits besitzen, einzusetzen oder sich mit einem Credential Service Provider (CSP) zu verbinden, der Mehrfaktor-Authentifizierung anbietet. CSPs bieten ihren Benutzern eine föderierte Identität an. Benutzer verfügen oft über mehrere Identitäten bei mehreren CSPs, z. B. eine Unternehmensidentität bei Azure AD, Okta, Ping Identity oder Google und eine Verbraucheridentität bei Facebook, Twitter, Google oder WeChat, um nur einige gängige Alternativen zu nennen. Diese Liste soll keine Bestätigung dieser Unternehmen oder Dienste sein, sie soll lediglich Entwickler dazu anspornen, die Realität zu berücksichtigen, dass viele Benutzer viele etablierte Identitäten haben. Organisationen sollten entsprechend ihrem Risikoprofil die Einbindung der Benutzeridentität in Betracht ziehen, die sich aus der Stärke der Identitätsprüfung des CSP ergibt. So ist es beispielsweise unwahrscheinlich, dass eine Regierungsorganisation eine Social-Media-Identität als Login für sensible Systeme akzeptiert, da es leicht ist, falsche Identitäten zu erstellen. Ein Unternehmen für Handyspiele muss sich für die Erweiterung seiner aktiven Spielerbasis möglicherweise an eine große Social-Media-Plattformen anbinden.

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.1.1** | Prüfen Sie, dass Benutzerpasswörter mindestens 12 Zeichen lang sind, nachdem zusammenhängende Leerzeichen gekürzt wurden. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.2** | Prüfen Sie, dass Passwörter mit 64 oder mehr Zeichen erlaubt sind, jedoch nicht mehr als 128 Zeichen. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.3** | Prüfen Sie, dass Passwörter nicht gekürzt werden. Mehrere aufeinanderfolgende Leerzeichen können zu einem zusammengefasst werden. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.4** | Prüfen Sie, ob alle druckbaren Unicode-Zeichen, auch Leerzeichen oder Emojis,  in Passwörtern zulässig sind. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.5** | Prüfen Sie, dass Benutzer ihr Passwort ändern können. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.6** | Prüfen Sie, dass die Passwortänderungsfunktion das bisherige sowie das neue Kennwort des Benutzers erfordert. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.7** | Prüfen Sie, dass die bei der Kontoregistrierung, beim Login und bei der Passwortänderung übermittelten Passwörter mit einen Satz verletzter Passwörtern verglichen werden, und zwar entweder lokal (z. B. mit den 1.000 oder 10.000 häufigsten Passwörtern, die mit der Passwortrichtlinie des Systems übereinstimmen) oder mit Hilfe einer externen API. Bei Verwendung einer API muss sichergestellt werden, dass das Klartextpasswort nicht gesendet oder anderweitig offengelegt wird. Wird das Passwort offengelegt, muss die Anwendung den Benutzer auffordern, ein neues Passwort festzulegen. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.8** | Prüfen Sie, dass ein Maß für die Passwortstärke bereitgestellt wird, damit Benutzer ein stärkeres Passwort erstellen können. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.9** | Prüfen Sie, dass es keine Regeln für die Zusammenstellung der Passwörter gibt, welche die Art der zulässigen Zeichen einschränken. Die Verwendung bestimmter Zeichen, wie Groß- oder Kleinschreibung, Zahlen oder Sonderzeichen sollte nicht verlangt werden. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.10** | Prüfen Sie, dass weder periodischer Passwortwechsel notwendig ist noch eine Passworthistorie gespeichert wird. | ✓ | ✓ | ✓ | 263 | 5.1.1.2 |
| **2.1.11** | Prüfen Sie, dass die „Einfügen“-Funktion, Passworthilfen der Browser und externe Passwortmanager zugelassen sind. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.12** | Prüfen Sie, dass der Benutzer wählen kann, entweder das gesamte Passwort vorübergehend angezeigt zu bekommen oder das letzte eingetippte Zeichen des Passwortes angezeigt zu bekommen. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |

Hinweis: Die Möglichkeit des Benutzers, sein Passwort angezeigt zu bekommen oder vorübergehend das letzte Zeichen zu sehen, soll die Eingabefreundlichkeit der Anmeldedaten verbessern, insbesondere bei der Verwendung längerer Passwörter, Passphrasen und Passwortmanager. Weiterhin sollen diese Anforderungen verhindern, Organisationen unnötigerweise dazu zwingen, dieses moderne benutzerfreundliche Sicherheitskonzept einiger Betriebssysteme zu deaktivieren.

## V2.2 Allgemeine Sicherheitsanforderungen an den Authentifikator

Die Agilität des Authentifikators ist für zukunftssichere Anwendungen unerlässlich. Überarbeiten Sie die Application Verifier um zusätzliche Authentifikatoren nach Benutzerpräferenz zuzulassen. Entfernen Sie veraltete oder unsichere Authentifikatoren.

NIST betrachtet E-Mail und SMS als „eingeschränkt zur Authentifikation tauglich”, und es ist wahrscheinlich, dass sie in der Zukunft aus dem NIST 800-63 und damit dem ASVS entfernt werden. Anwendungen sollten so geplant werden, dass sie ohne E-Mail oder SMS auskommen.

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.2.1** | Prüfen Sie, dass Maßnahmen gegen automatische Angriffe, wie das Ausprobieren von Passworten oder das Aussperren von Benutzern, wirksam umgesetzt sind. Dazu gehören das Blockieren der am häufigsten verwendeten Passwörter, Soft-Lockouts, die Begrenzung der Anzahl von Anmeldungen, CAPTCHA, wachsende Verzögerungen zwischen den Fehlversuchen, IP-Adressbeschränkungen oder risikobasierte Einschränkungen wie Standort, erste Anmeldung auf einem Gerät, kürzliche Versuche, das Konto zu entsperren oder Ähnliches. Prüfen Sie, dass nicht mehr als 100 Fehlversuche pro Stunde bei einem einzelnen Konto möglich sind. | ✓ | ✓ | ✓ | 307 | 5.2.2 / 5.1.1.2 / 5.1.4.2 / 5.1.5.2 |
| **2.2.2** | Prüfen Sie, dass der Einsatz schwacher Authentifikationsmethoden, wie SMS und E-Mail, auf die sekundäre Verifizierung und Transaktionsgenehmigung beschränkt ist und nicht als Ersatz für sicherere Authentifizierungsmethoden dient. Prüfen Sie, dass stärkere Methoden vor schwachen Methoden eingesetzt werden, dass sich die Benutzer der Risiken bewusst sind oder dass geeignete Maßnahmen zur Begrenzung des Risikos getroffen werden. | ✓ | ✓ | ✓ | 304 | 5.2.10 |
| **2.2.3** | Prüfen Sie, dass die Benutzer sichere Benachrichtigungen nach Aktualisierungen der Authentifizierungsdetails, wie z. B. das Zurücksetzen von Anmeldedaten, E-Mail- oder Adressänderungen, Anmeldung von unbekannten oder risikobehafteten Orten erhalten. Die Verwendung von Push-Benachrichtigungen - anstelle von SMS oder E-Mail - ist vorzuziehen. Bei fehlenden Push-Benachrichtigungen sind SMS oder E-Mail jedoch akzeptabel, solange in der Benachrichtigung keine sensiblen Informationen offengelegt werden. | ✓ | ✓ | ✓ | 620 | |
| **2.2.4** | Prüfen Sie die Resistenz gegen Phishing durch Authentifizierung mittels Mehrfaktor-Authentifizierung, Public Key Kryptographie, Chipkarten und Push-Nachrichten, auf höheren AAL-Ebenen: clientseitige Zertifikate. | | | ✓ | 308 | 5.2.5 |
| **2.2.5** | Prüfen Sie, dass der CSP und die nutzende Anwendung über zweiseitig authentifiziertes TLS kommunizieren. | | | ✓ | 319 | 5.2.6 |
| **2.2.6** | Prüfen Sie, dass Authentifikationsdaten nicht wieder eingespielt werden können. Dies kann z.B. mit One Time Password (OTP) Generatoren, Chipkarten o.ä. verhindert werden. | | | ✓ | 308 | 5.2.8 |
| **2.2.7** | Prüfen Sie, dass eine Authentifikation nicht unbeabsichtigt stattfinden kann. Verlangen Sie die Eingabe eines OTP-Tokens oder eine vom Benutzer initiierte Aktion, wie z.B. einen Tastendruck auf einem FIDO-Hardwaretoken. | | | ✓ | 308 | 5.2.9 |

## V2.3 Lebenszyklus des Authentifikators

Authentifikatoren sind Passwörter, Softtoken, Hardwaretoken und biometrische Geräte. Ihr Lebenszyklus ist für die Sicherheit einer Anwendung entscheidend: Wenn sich jemand auf einem Konto ohne Identitätsnachweis selbst registrieren kann, ist die Identitätsbehauptung wenig vertrauenswürdig. Für Social-Media-Sites wie Reddit ist das völlig in Ordnung. Bei Bankinganwendungen hingegen ist ein größeres Augenmerk auf die Registrierung, die Anmeldedaten bzw. -geräten entscheidend für die Sicherheit der Anwendung.

Hinweis: Die NIST hat die Regulierung von Passwörtern geändert. Sie dürfen keine maximale Lebensdauer haben und sollten keinem routinemäßigen Wechsel mehr unterliegen. Passwörter müssen nur noch beim Verdacht auf Offenlegung ersetzt werden.

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.3.1** | Vom System generierte Anfangspasswörter oder Aktivierungscodes SOLLTEN sicher zufällig generiert werden. Sie SOLLTEN mindestens 6 Zeichen lang sein und KÖNNEN Buchstaben und Zahlen enthalten. Sie MÜSSEN nach einer kurzen Zeitspanne ablaufen. Diese Initialpasswörter dürfen nicht zum dauerhaften Passwort werden. | ✓ | ✓ | ✓ | 330 | 5.1.1.2 / A.3 |
| **2.3.2** | Prüfen Sie, dass die Registrierung und die Verwendung von vom Teilnehmer bereitgestellten Authentifizierungsgeräten unterstützt werden, wie z. B. U2F- oder FIDO-Token. | | ✓ | ✓ | 308 | 6.1.3 |
| **2.3.3** | Prüfen Sie, dass die Aufforderung zur Erneuerung zeitgebundener Authentifikatoren rechtzeitig gesendet werden. | | ✓ | ✓ | 287 | 6.1.4 |

## V2.4 Speicherung der Anmeldedaten

Architekten und Entwickler sollten sich bei der Erstellung oder dem Refactoring von Software an diesen Abschnitt halten. Dieser Abschnitt kann nur durch Codereview oder durch sichere Unit- oder Integrationstests vollständig verifiziert werden. Penetrationstests können diese Probleme nicht nachweisen, daher sind die Maßnahmen nicht mit L1 gekennzeichnet. Dieser Abschnitt ist jedoch von entscheidender Bedeutung für die Sicherheit von Anmeldedaten, falls diese gestohlen werden. Wenn Sie also den ASVS als Architektur- oder Programmierrichtlinie oder als Checkliste zum Codereview nutzen, setzen Sie diese Maßnahmen bitte wieder auf L1.

Die Liste der anerkannten Einwegfunktionen für die Schlüsselableitung wird in NIST 800-63 B, Abschnitt 5.1.1.2 und in [BSI Kryptographische Verfahren: Empfehlungen und Schlüssellängen (2018)](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile) detailliert aufgeführt. Anstelle dieser Auswahlmöglichkeiten können die neuesten nationalen oder regionalen Algorithmen und Schlüssellängenstandards gewählt werden.

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.4.1** | Prüfen Sie, dass die Passwörter in einer Form gespeichert werden, die immun gegen Offlineangriffe ist. Passwörter MÜSSEN mit einem Salt versehen werden. Der Passworthash muss mit Hilfe einer sicheren Funktion zur Schlüsselberechnung oder einer Passwort-Hashfunktion berechnet werden. Die Funktionen zur Schlüsselberechnung und zum Passwort-Hashing nehmen ein Passwort, einen Salt und einen Kostenfaktor als Eingabewerte. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.2** | Prüfen Sie, dass das Salt mindestens 32 Bit lang ist und zufällig gewählt wird, um Saltwertkollisionen zwischen gespeicherten Hashes zu minimieren. Für jede Anmeldeinformation (Credential) MUSS ein eindeutiger Saltwert und der daraus resultierende Hash gespeichert werden. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.3** | Prüfen Sie, dass bei Verwendung von PBKDF2 der Iterationszähler so groß sein SOLLTE, wie es die Leistung des Verifikationsservers zulässt, normalerweise mindestens 100.000 Iterationen. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.4** | Prüfen Sie, dass bei Verwendung von bcrypt der Arbeitsfaktor so groß sein SOLLTE, wie es die Leistung des Verifikationsservers erlaubt, jedoch mindestens 10. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.5** | Prüfen Sie, dass eine zusätzliche Iteration einer Funktion zur Schlüsselberechnung durchgeführt wird. Dabei ist ein Saltwert zu verwenden, der nur dem Verifizierer bekannt ist. Generieren Sie den Saltwert mit einem zugelassenen Zufallsgenerator [SP 800-90Ar1]. Stellen Sie die in der letzten Revision von SP 800-131A angegebene Mindestsicherheitsstärke sicher. Der geheime Saltwert MUSS getrennt von den gehashten Passwörtern gespeichert werden, z.B. in einem speziellen Gerät wie einem HSM. | | ✓ | ✓ | 916 | 5.1.1.2 |

Wo US-Normen erwähnt werden, kann bei Bedarf anstelle der US-Norm oder zusätzlich zu dieser eine lokale Norm verwendet werden. Ein Teil der Inhalte des SP 800-131A wird von der TR-02102-1 "Kryptographische Verfahren: Empfehlungen und Schlüssellängen" des BSI abgedeckt.

## V2.5 Wiederherstellung von Anmeldedaten

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.5.1** | Prüfen Sie, dass ein vom System generiertes Initial- oder Wiederherstellungsgeheimnis nicht im Klartext an den Benutzer gesendet wird. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.2** | Prüfen Sie, dass keine Hinweise auf Passwörter oder wissensbasierte Authentifizierung, z.B. „geheime Fragen“ vorliegen. | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.3** | Prüfen Sie, dass die Wiederherstellung von Anmeldedaten das aktuelle Kennwort nicht preisgibt. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.4** | Prüfen Sie, dass Gemeinschafts- oder Standardkonten, z.B. „root“, „admin“, „Gast“ oder „sa“ deaktiviert oder gelöscht sind. | ✓ | ✓ | ✓ | 16 | 5.1.1.2 / A.3 |
| **2.5.5** | Prüfen Sie, dass der Benutzer informiert wird, wenn ein Authentifizierungsfaktor geändert oder ersetzt wird. | ✓ | ✓ | ✓ | 304 | 6.1.2.3 |
| **2.5.6** | Prüfen Sie, dass der Prozess zur Wiederherstellung, z.B. für vergessene Passwörter, einen sicheren Kanal, z. B. TOTP oder andere Softtoken, Mobile Push oder andere Offlinekanäle, verwendet. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.7** | Prüfen Sie, dass der Identitätsnachweis bei Verlust von OTP- oder Mehrfaktor-Token auf derselben Ebene wie bei der Registrierung durchgeführt wird. | | ✓ | ✓ | 308 | 6.1.2.3 |

## V2.6 Verifizierung von TAN-Listen

Vorgenerierte Listen von Geheimcodes, z.B. Transaktionsnummern (TAN), Wiederherstellungscodes für soziale Medien oder eine andere Reihe von Zufallswerten. Diese werden sicher an die Benutzer versandt. Diese Geheimcodes werden einmal verwendet. Wenn alle verwendet wurden, wird die Liste entsorgt. Diese Art von Authentifikator gilt als „etwas, das Sie haben“ bzw. Besitz.

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.6.1** | Prüfen Sie, dass die Geheimcodes nur einmal verwendet werden können. | | ✓ | ✓ | 308 | 5.1.2.2 |
| **2.6.2** | Prüfen Sie, ob die Geheimcodes eine ausreichende Zufälligkeit aufweisen (112 Bit Entropie). Falls weniger als 112 Bit Entropie vorhanden sind, sind ein einzigartiger und zufälliger 32 Bit Salt und eine zugelassene Hashfunktion zu nutzen. | | ✓ | ✓ | 330 | 5.1.2.2 |
| **2.6.3** | Prüfen Sie, dass Geheimcodes gegen Offlineangriffe, wie z.B. vorhersehbare Werte, immun sind. | | ✓ | ✓ | 310 | 5.1.2.2 |

## V2.7 Out-of-Band Verifizierer

In der Vergangenheit wäre ein üblicher Out-of-Band Verifizierer eine E-Mail oder SMS mit einem Link zum Zurücksetzen des Passworts gewesen. Angreifer nutzen diesen schwachen Mechanismus, um Konten, die sie noch nicht kontrollieren, zurückzusetzen, z. B. indem sie das E-Mail-Konto einer Person übernehmen und Passwörter neu anfordern. Es gibt bessere Möglichkeiten, die Out-of-Band Verifizierung zu handhaben.

Sichere Out-of-Band Authentifikatoren sind physische Geräte, die mit dem Verifizierer über einen sicheren Zweitkanal kommunizieren können. Das sind z.B. Push-Nachrichten an mobile Geräte. Diese Art von Authentifikator gilt als „etwas, das Sie haben“ bzw. Besitz. Will sich ein Benutzer authentifizieren, sendet die verifizierende Anwendung eine Nachricht an den Out-of-Band Authentifikator. Die Nachricht enthält einen Authentifizierungscode, z.B. eine zufällige sechsstellige Zahl oder eine Abfrage der Genehmigung. Die verifizierende Anwendung wartet auf den Empfang des Authentifizierungscodes über den Primärkanal und vergleicht den Hash des empfangenen Wertes mit dem Hash des ursprünglichen Authentifizierungscodes. Wenn sie übereinstimmen, kann der Out-of-Band Verifizierer davon ausgehen, dass der sich der Benutzer authentifiziert hat. Der Prozess kann direkt oder über einen Dienst Dritter ablaufen.

Der ASVS geht davon aus, dass nur wenige Entwickler neue Out-of-Band Authentifizierer wie Push-Nachrichten entwickeln werden, und daher gelten die folgenden Maßnahmen des ASVS für Verifizierer, wie die Authentifizierungs-API, Anwendungen und Single-Sign-On Implementierungen. Wenn Sie einen neuen Out-of-Band Authentifikator entwickeln, beachten Sie bitte NIST 800-63B § 5.1.3.1.

Unsichere Out-of-Band Authentifizierer wie E-Mail und VOIP sind nicht zulässig. PSTN- oder SMS-Authentifizierung ist derzeit durch NIST als eingeschränkt geeignet eingeschätzt und sollten durch Push-Nachrichten oder ähnliche ersetzt werden. Müssen Sie Telefon- oder SMS zur Out-of-Band Authentifizierung verwenden, lesen Sie bitte NIST 800-63B § 5.1.3.3.

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.7.1** | Prüfen  Sie, dass Out-of-Band Authentifikatoren, die NIST „restricted“ sind, wie z.B. SMS, nicht standardmäßig angeboten werden und dass stärkere Alternativen wie Push-Nachrichten zuerst angeboten werden. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.2** | Prüfen Sie, dass der Out-of-Band Verifizierer bei Out-of-Band Authentifizierungsanforderungen, -Codes oder -Tokens nach 10 Minuten abläuft. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.3** | Prüfen Sie, dass Authentifizierungsanfragen, -Codes oder ‑Token an den Out-of-Band Verifizierer nur einmal und nur für die ursprüngliche Authentifizierungsanfrage verwendbar sind. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.4** | Prüfen Sie, dass der Out-of-Band Authentifizierer und der Verifizierer über einen sicheren, unabhängigen Kanal kommunizieren. | ✓ | ✓ | ✓ | 523 | 5.1.3.2 |
| **2.7.5** | Prüfen Sie, dass der Out-of-Band Verifizierer nur eine gehashte Version des Authentifizierungscodes speichert. | | ✓ | ✓ | 256 | 5.1.3.2 |
| **2.7.6** | Prüfen Sie, dass der initiale Authentifizierungscode von einem sicheren Zufallszahlengenerator erzeugt wird, der mindestens 20 Bit Entropie enthält. Normalerweise ist eine sechsstellige Zufallszahl ausreichend. | | ✓ | ✓ | 310 | 5.1.3.2 |

## V2.8 Ein- oder Mehrfaktor-Einwegverifizierer

Einmal-Passwörter (OTPs) sind physische oder Softtoken, die ein sich ständig veränderndes pseudozufälliges Passwort bereitstellen. Diese Geräte erschweren Imitiationsangriffe, wie Phishing, verhindern sie aber nicht. Diese Art von Authentifikator gilt als „etwas, das Sie haben“ bzw. Besitz. Mehrfaktor-Token sind ähnlich wie Einmalpasswörter erfordern jedoch zusätzlich einen gültigen PIN-Code, biometrische Entsperrung, USB-Stick oder NFC-Kontakt o.ä., der eingegeben werden muss, um den endgültigen OTP zu erstellen.

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.8.1** | Prüfen Sie, dass zeitbasierte OTPs eine definierte Lebensdauer haben, bevor sie ablaufen. | ✓ | ✓ | ✓ | 613 | 5.1.4.2 / 5.1.5.2 |
| **2.8.2** | Prüfen Sie, dass die symmetrischen Schlüssel, die zur Prüfung der eingegebenen OTPs verwendet werden, sicher geschützt sind, z.B. durch Verwendung eines HSM oder der sicheren Schlüsselspeicherung des Betriebssystems. | | ✓ | ✓ | 320 | 5.1.4.2 / 5.1.5.2 |
| **2.8.3** | Prüfen Sie, dass anerkannte kryptografische Algorithmen bei der Generierung, dem Seeding und der Verifizierung verwendet werden. | | ✓ | ✓ | 326 | 5.1.4.2 / 5.1.5.2 |
| **2.8.4** | Prüfen Sie, dass das zeitbasierte OTP nur einmal innerhalb des Gültigkeitszeitraums verwendet werden können. | | ✓ | ✓ | 287 | 5.1.4.2 / 5.1.5.2 |
| **2.8.5** | Prüfen Sie, dass ein zeitbasiertes Mehrfaktor-OTP, das während der Gültigkeitsdauer wiederverwendet wird, protokolliert und mit sicheren Benachrichtigungen an den Inhaber des Geräts abgelehnt wird. | | ✓ | ✓ | 287 | 5.1.5.2 |
| **2.8.6** | Prüfen Sie, ob physische OTP-Generatoren im Falle von Diebstahl oder Verlust gesperrt werden können. Stellen Sie sicher, dass der Widerruf sofort für alle eingeloggten Sitzungen, unabhängig vom Standort, wirksam ist. | | ✓ | ✓ | 613 | 5.2.1 |
| **2.8.7** | Prüfen Sie, dass biometrische Authentifikatoren nur als sekundäre Faktoren in Verbindung mit etwas, das Sie haben oder etwas, das Sie wissen, verwendet werden dürfen. | | o | ✓ | 308 | 5.2.3 |

## V2.9 Kryptografische Software und Geräte im Authentifizierungsprozess

Kryptographische Geräte sind Chipkarten oder USB-Sticks, die der Benutzer an den Computer anschließen muss, um die Authentifizierung abzuschließen. Der Verifizierer sendet einen Zufallswert (Nonce) an das kryptographische Gerät oder die Software. Dort wird eine Antwort auf der Grundlage eines sicher gespeicherten kryptographischen Schlüssels berechnet. Die Anforderungen für kryptographische Geräte und Software sind für Ein- und Mehrfaktorauthentifizierung gleich, da die Verifizierung der berechneten Antwort den Besitz des Authentisierungsfaktors nachweist.

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.9.1** | Prüfen Sie, dass die bei der Authentifizierung verwendeten kryptografischen Schlüssel sicher gespeichert und gegen Offenlegung geschützt sind, z. B. durch Verwendung eines Trusted Platform Module (TPM) oder eines Hardware Security Modules (HSM) oder eines Betriebssystemdienstes. | | ✓ | ✓ | 320 | 5.1.7.2 |
| **2.9.2** | Prüfen Sie, dass der Zufallswert mindestens 64 Bit lang ist und statistisch einmalig oder für die Lebensdauer des kryptografischen Geräts einmalig ist. | | ✓ | ✓ | 330 | 5.1.7.2 |
| **2.9.3** | Prüfen Sie, dass anerkannte kryptografische Algorithmen bei allen kryptographischen Operationen verwendet werden. | | ✓ | ✓ | 327 | 5.1.7.2 |

## V2.10 Service-Authentifizierung

Dieser Abschnitt ist kann nicht mittels Penetrationstest getestet werden und hat daher also keine L1-Anforderungen. Wenn sie jedoch in einer Architektur-, Programmier- oder Codereview verwendet wird, gehen Sie bitte davon aus, dass Software, ebenso wie Java Key Store, die Mindestanforderung von L1 hat. Das Speichern von Geheimnissen im Klartext ist unter keinen Umständen zulässig.

| # | Beschreibung | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.10.1** | Prüfen Sie, dass Intra-Service-Geheimnisse nicht auf unveränderlichen Credentials, wie Passwörtern, API-Schlüsseln oder gemeinsam genutzten privilegierten Konten beruhen. | | OS assisted | HSM | 287 | 5.1.1.1 |
| **2.10.2** | Prüfen Sie, dass Servicekonten, die zur Anmeldung genutzt werden, keine Standardpasswörter, wie root / root oder admin / admin, die häufig voreingestellt sind, nutzen. | | OS assisted | HSM | 255 | 5.1.1.1 |
| **2.10.3** | Prüfen Sie, dass Passworthashwerte mit ausreichendem Schutz gespeichert werden, um Offlineangriffe, zu verhindern. | | OS assisted | HSM | 522 | 5.1.1.1 |
| **2.10.4** | Prüfen Sie, dass Passwörter, Zugänge zu Datenbanken o.a. Systemen, Seeds, interne Geheimnisse sowie API-Schlüssel sicher verwaltet werden. Sie dürfen nicht in den Quellcode aufgenommen bzw. in Quellcoderepositories gespeichert werden. Eine solche Speicherung muss Offline-Angriffen widerstehen. Für die Passwortspeicherung wird die Verwendung eines sicheren Softwareschlüsselspeichers (L1), eines TPM oder eines HSM (L3) empfohlen. | | OS assisted | HSM | 798 | |

## Zusätzliche Anforderungen der US-Behörden

US-Behörden müssen NIST 800-63 zwingend erfüllen. Der ASVS konzentriert sich auf die 80 % der Maßnahmen, die für fast alle Anwendungen gelten. In diesem Sinne ist der ASVS eine Teilmenge von NIST 800-63, besonders für die IAL1/2- und AAL1/2-Klassifikationen. Er ist jedoch nicht umfassend genug, insbesondere für die IAL3/AAL3-Klassifikationen. Wenn Sie Software für die US-Regierungsbehörden entwickeln, müssen Sie NIST 800‑63 in seiner Gesamtheit überprüfen und umzusetzen.

## Referenzen

Weitere Informationen finden Sie unter:
        
* [NIST 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST 800-63 A - Enrollment and Identity Proofing](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf) 
* [NIST 800-63 B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST 800-63 C - Federation and Assertions](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [OWASP Cheat Sheet - Password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Forgot password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Choosing and using security questions](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html) 
