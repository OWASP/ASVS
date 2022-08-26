# Zertifizierung

## ASVS-Zertifizierungen und Gütesiegel

OWASP ist eine herstellerneutrale, gemeinnützige Organisation. Sie zertifiziert derzeit keine Hersteller, Prüfstellen oder Software. Alle derartigen Versicherungen, Gütesiegel oder Zertifizierungen werden von OWASP nicht offiziell überprüft, registriert oder zertifiziert. Jede Organisation sollte in Bezug auf Aussagen eines Dritten, der behauptet, ASVS-zertifiziert zu sein, vorsichtig sein. Dies ist jedoch kein Verbot, solche Assurance-Dienstleistungen anzubieten, solange sie keine offizielle OWASP-Zertifizierung geltend machen.

## Leitfaden für zertifizierende Organisationen

Der Application Security Verification Standard kann als Open Book Prüfung von Anwendungen verwendet werden, was den offenen und ungehinderten Zugang zu Schlüsselressourcen wie Architekten und Entwicklern, Projektdoku-mentation, Quellcode, authentifiziertem Zugang zu Testsystemen, einschließlich des Zugangs zu einem oder mehreren Benutzerkonten in jeder Rolle, insbesondere für L2- und L3-Verifikationen einschließt.

Klassischerweise werden Penetrationstests und Security Code Reviews so dokumentiert, dass nur fehlgeschlagene Tests im Abschlussbericht erscheinen. Eine zertifizierende Organisation muss jedoch in jedem Bericht den Umfang der Verifizierung angeben. Insbesondere, wenn eine Schlüsselkomponente außerhalb des Umfangs liegt, wie z.B. die SSO-Authentifizierung sowie eine Zusammenfassung der Verifizierungsergebnisse, einschließlich der bestandenen und fehlgeschlagenen Tests, mit klaren Angaben zur Korrektur der gefundenen Probleme.

Bestimmte Anforderungen des ASVS sind möglicherweise nicht auf die zu testende Anwendung anwendbar. Wenn Sie beispielsweise Ihren Kunden eine zustandslose API ohne eine Clientimplementierung zur Verfügung stellen, sind viele der Anforderungen im V3 Session Management nicht direkt anwendbar. In solchen Fällen kann eine zertifizierende Organisation immer noch die volle ASVS-Konformität bestätigen, muss aber im Bericht klar einen Grund für die Nichtanwendbarkeit der ausgeschlossenen Verifikationsanforderungen angeben.

Das Aufbewahren von detaillierten Arbeitspapieren, Screenshots, Filmen, Skripten zur zuverlässigen wiederholten Auswertung eines Tests sowie von elektronischen Testaufzeichnungen, wie z. B. Proxy-Protokollen und zugehörigen Notizen, wie z. B. einer CleanUp-List, gilt als gängige Praxis. Diese können für kritische Entwickler als Beleg für die Ergebnisse hilfreich sein. Es reicht also nicht aus, einfach ein Tool laufen zu lassen und über die Fehler zu berichten: Dies liefert keinen ausreichenden Beweis dafür, dass alle Probleme auf einer Zertifizierungsebene gründlich getestet und geprüft worden sind. In Streitfällen sollte es ausreichende Nachweise geben, um zu belegen, dass jede einzelne verifizierte Anforderung tatsächlich getestet wurde.

### Prüfmethode

Zertifizierende Organisationen können die geeigneten Prüfmethoden frei wählen, sollten diese aber in einem Bericht angeben. Je nach der zu testenden Anwendung und der Anforderung können unterschiedliche Testmethoden verwendet werden: Die Wirksamkeit der Input-Validierung einer Anwendung kann beispielsweise sowohl mit einem manuellen Penetrationstest als auch mit Hilfe von Quellcodeanalysen geprüft werden.

#### Die Rolle automatisierter Sicherheits-Test-Tools

Der Einsatz von automatisierten Penetrationstests wird empfohlen, um eine möglichst hohe Abdeckung zu erreichen. Die ASVS-Verifizierung kann jedoch nicht ausschließlich mit automatisierten Penetrationstest-Tools durchgeführt werden. Während die meisten Anforderungen in L1 mit automatisierten Tests durchgeführt werden kann, ist die Mehrheit der Anforderungen der Stufen 2 und 3 nicht für automatisierte Penetrationstests geeignet. Die Grenzen zwischen automatisierten und manuellen Tests verschwimmen mit zunehmender Reife der Anwendungs-sicherheitsindustrie immer mehr. Automatisierte Tools werden häufig von Experten angepasst, und manuelle Tester nutzen oft eine Vielzahl von automatisierten Werkzeugen.

#### Rolle der Penetrationstests 

In Version 4.0 haben wir uns entschieden, L1 komplett penetrationstestfähig zu machen, ohne Zugriff auf Quellcode, Dokumentation oder Entwickler. Zwei Protokollierungselemente, die zur Einhaltung der OWASP Top 10 2017 A10 erforderlich sind, erfordern Interviews, Screenshots oder eine andere Sammlung von Nachweisen, wie sie auch in der OWASP Top 10 2017 erforderlich sind. Das Testen ohne Zugang zu den notwendigen Informationen ist jedoch keine ideale Methode der Sicherheitsüberprüfung, da die Quelle nicht überprüft wird, Bedrohungen und fehlende Maßnahmen nicht identifiziert werden und ein weitaus gründlicherer Test in kürzerer Zeit nicht durchgeführt wird. Bei der Durchführung eines L2- oder L3-Assessments ist der Zugang zu Entwicklern, der Dokumentation, dem Code sowie der Zugang zu einer Testanwendung mit Nicht-Produktionsdaten erforderlich. Penetrationstests, die auf diesen Ebenen durchgeführt werden, erfordern diese Zugriffsebene, die wir „hybride Überprüfungen“ oder „hybride Penetrationstests“ nennen.

## Andere Verwendungszwecke für den ASVS

Neben der Verwendung zur Bewertung der Sicherheit einer Anwendung haben wir eine Reihe anderer möglicher Anwendungen für den ASVS identifiziert.

### Als detaillierte Anleitung zur Sicherheitsarchitektur

Eine der häufigeren Verwendungen des Application Security Verification Standards ist seine Verwendung als Ressource für Sicherheitsarchitekten. So fehlt z. B. in der Sherwood Applied Business Security Architecture (SABSA) eine Menge an Informationen, die für eine gründliche Überprüfung der Anwendungssicherheitsarchitektur erforderlich sind. ASVS kann verwendet werden, um diese Lücken zu füllen, indem Sicherheitsarchitekten bessere Maßnahmen für häufige Probleme wie Datenschutzmuster und Eingabevalidierungsstrategien wählen können.

### Ersatz für Standard-Checklisten für sichere Softwareentwicklung

Viele Organisationen können von der Übernahme des ASVS profitieren, indem sie sich für eine der drei Stufen entscheiden, oder den ASVS domänenspezifisch anpassen. Wir befürworten diese Anpassungen, solange die Rückverfolgbarkeit gewährleistet ist. Wenn also eine Anwendung die Anforderung 4.1 bestanden hat, bedeutet dies dasselbe für die angepassten Varianten wie für den Standard aus dem sie sich entwickelt haben.

### Als Leitfaden für automatisierte Unit- und Integrationstests

Der ASVS ist so konzipiert, dass er in hohem Maße testbar ist, mit Ausnahme der Anforderungen an die Architektur und den bösartigen Code. Durch die Erstellung von Unit- und Integrationstests, die spezifische und relevante Fuzz- und Missbrauchsfälle testen, wird die Anwendung mit jedem Build nahezu selbstverifizierend. Beispielsweise können zusätzliche Tests für die Testsuite eines Logincontrollers erstellt werden, der die Parameter des Benutzernamens auf gängige Standardbenutzernamen, das Erraten von Benutzernamen, Brute-Force Angriffe, LDAP- und SQL-Injektion und XSS testet. In ähnlicher Weise sollte ein Test des übermittelten Passwortes auf gängige Passwörter, die Passwortlänge, Null-Byte-Injektion, Entfernen des Parameters, XSS, etc. umfassen.

### Für Schulungen zur sicheren Softwareentwicklung

Der ASVS kann auch dazu verwendet werden, um Merkmale sicherer Software zu definieren. Viele Kurse zur sicheren Softwareentwicklung sind tatsächlich Kurse „Ethisches Hacking mit einem Hauch von Softwareentwicklung“. Wissen über Hacking hilft den Entwicklern nicht unbedingt, einen sichereren Code zu schreiben. Stattdessen können Kurse für sichere Entwicklung den ASVS verwenden, mit dem Schwerpunkt auf den Sicherheitsmaßnahmen des ASVS, an Stelle der Top 10 der Programmiersünden.

### Als Treiber für agile Anwendungssicherheit

Der ASVS kann in einem agilen Entwicklungsprozess als Framework verwendet werden, um spezifische Aufgaben zu definieren, die vom Team zum Erhalt eines sicheren Produkts implementiert werden müssen. Eine Vorgehensweise wäre: Man beginnt mit Stufe 1 und verifiziert die spezifische Anwendung oder das System gemäß Anforderungen des ASVS. Für fehlende Maßnahmen werden spezifische Tickets oder Aufgaben im Backlog generiert. Dies hilft bei der Priorisierung bestimmter Aufgaben (oder beim Grooming) und macht die Sicherheit im agilen Prozess sichtbar. Dies kann auch zur Priorisierung von Revisions- und Überprüfungsaufgaben in der Organisation verwendet werden. Bestimmte ASVS-Anforderungen können für ein bestimmtes Teammitglied Antrieb für eine Überprüfung, ein Refactoring oder eine Revision sein und werden als „Offen“ im Backlog zur Abarbeitung aufgeführt.

### Zur Beschaffung sicherer Software

Der ASVS ist ein großartiger Rahmen, der bei der Beschaffung sicherer Software oder der Beschaffung von Entwicklungsdienstleistungen hilfreich ist. Der Käufer stellt die Anforderung, dass die Software, auf ASVS-Ebene X entwickelt wird und verlangt vom Verkäufer den entsprechenden Nachweis. Dies funktioniert gut, wenn es mit dem OWASP-Vertragsanhang für sichere Software kombiniert wird.
