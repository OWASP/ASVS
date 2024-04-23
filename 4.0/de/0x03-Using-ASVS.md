# Verwendung des ASVS

Der ASVS hat die zwei Hauptziele:

* Organisationen bei der Entwicklung und Pflege sicherer Anwendungen zu unterstützen.
* Anbietern von Sicherheitsdienstleistungen oder -werkzeugen und deren Kunden die Möglichkeit zu geben, ihre Anforderungen und Angebote aufeinander abzustimmen.

## Stufen zur Verifizierung der Anwendungssicherheit

Der Application Security Verification Standard definiert drei Stufen der Sicherheitsverifikation, wobei jede Stufe an Tiefe zunimmt.

* Stufe 1 ist für geringe Sicherheitsanforderungen gedacht und lässt sich mittels Pentests prüfen.
* Stufe 2 ist für Anwendungen, die sensible Daten enthalten und diese schützen müssen. Das ist die empfohlene Stufe für die meisten Anwendungen.
* Stufe 3 ist für die kritischsten Anwendungen, z. B. solche, die hochwertige Transaktionen durchführen, sensible medizinische Daten enthalten oder aus anderen Gründen ein Höchstmaß an Vertrauen erfordern.

Jede Stufe des ASVS enthält eine Liste von Sicherheitsanforderungen. Jede dieser Anforderungen kann auch auf sicherheitsspezifische Merkmale und Fähigkeiten abgebildet werden, die von den Entwicklern in die Software eingebaut werden müssen.

![ASVS Levels](https://raw.githubusercontent.com/OWASP/ASVS/master/4.0/images/asvs_40_levels.png "ASVS Stufen")

Bild 1 - Stufen des OWASP Application Security Verification Standard 4.0

Stufe 1 ist die einzige Stufe, die sich komplett mittels Pentests prüfen lässt. Alle anderen Stufen benötigen Zugang zu Dokumentation, Quellcode, Konfiguration und den am Entwicklungsprozess beteiligten Personen. Jedoch stellen Black Box Tests ohne Dokumentation und ohne Quellen keine wirksame Absicherung dar. Sie müssen langfristig ergänzt werden. Böswillige Angreifer haben sehr viel Zeit. Die meisten Penetrationstests hingegen sind innerhalb von wenigen Wochen abgeschlossen. Die Verteidiger müssen alle Sicherheitsmaßnahmen umsetzen, alle Schwachstellen finden und beheben sowie böswillige Akteure innerhalb einer angemessenen Zeit aufspüren und Gegenmaßnahmen ergreifen. Böswillige Akteure haben im Wesentlichen unendlich viel Zeit und benötigen nur eine einzige Lücke in der Verteidigung, eine einzige Schwachstelle, um erfolgreich zu sein. Black Box Tests, die oft am Ende der Entwicklung schnell oder gar nicht durchgeführt werden, sind völlig ungeeignet, dieser Asymmetrie gerecht zu werden.

Die letzten 30 Jahre haben gezeigt, dass Black Box Tests immer wieder kritische Sicherheitsprobleme übersehen, welche direkt zu weiteren, massiveren Problemen geführt haben. Wir befürworten ausdrücklich den Einsatz einer breiten Palette von Maßnahmen zur Gewährleistung und Verifizierung der Sicherheit, einschließlich des Ersatzes der Penetrationstests durch quellcodegeführte (hybride) Penetrationstests auf Stufe 1, mit vollem Zugang zu den Entwicklern und der Dokumentation während des gesamten Entwicklungsprozesses. Die Finanzaufsichtsbehörden dulden keine externen Finanzprüfungen ohne Zugang zu den Büchern, zu Stichproben von Geschäftsvorgängen oder zu den Personen, welche die Prüfungen durchführen. Derselbe Standard an Transparenz muss von der Industrie und den Regierungen auch im Bereich der Softwareentwicklung gefordert werden.

Wir befürworten ausdrücklich die Verwendung von Sicherheitstools innerhalb des Entwicklungsprozesses. DAST- und SAST-Tools können in die Buildpipeline eingebunden werden, um leicht zu findende Sicherheitsprobleme aufzuspüren, die niemals vorhanden sein dürfen.

Automatisierte Tools und Onlinescans können höchsten nur noch die Hälfte des ASVS ohne menschliches Zutun erfassen. Ist eine umfassende Testautomatisierung für jeden Buildprozess erforderlich, wird eine Kombination aus benutzerdefinierten Unit- und Integrationstests zusammen mit den vom Buildprozess veranlassten Onlinescans verwendet. Mängel der Geschäftslogik und der Zugriffskontrolle lassen sich nur mit menschlicher Hilfe testen, am besten in Unit- und Integrationstests.

## Verwendung dieses Standards

Eine der besten Möglichkeiten, den Application Security Verification Standard zu nutzen, ist seine Verwendung als Vorlage für die Erstellung einer Checkliste für Anforderungen zur sicheren Softwareentwicklung, die speziell auf Ihre Anwendung, Plattform oder Organisation zugeschnitten ist. In dem Sie die Anforderungen des ASVS auf Ihre Anwendungsfälle passend zuschneiden, setzen Sie den Schwerpunkt auf die Sicherheitsanforderungen, die für Ihre Projekte und Umgebungen am wichtigsten sind.

Zu den Sicherheitszielen aller Stufen gehören die Gewährleistung der Vertraulichkeit (z.B. Verschlüsselung), der Integrität (z.B. Transaktionen, Eingabevalidierung), der Verfügbarkeit (z.B. ordnungsgemäße Lastverteilung), der Authentifizierung (auch zwischen Systemen), der Nichtabstreitbarkeit, der Autorisierung und der Protokollierung.

### Stufe 1 - Erste Schritte oder das absolute Minimum

Eine Anwendung erreicht ASVS Stufe 1, wenn sie einen ausreichenden Schutz gegen leicht zu entdeckende Schwachstellen bietet, die auch in den OWASP Top 10 und anderen ähnlichen Checklisten aufgeführt sind.

Stufe 1 ist das für alle Anwendungen erforderliche absolute Minimum. Sie ist auch nützlich als erster Schritt eines mehrstufigen Prozesses oder für den Fall, wenn Anwendungen keine sensiblen Daten verarbeiten und daher nicht die strengeren Anforderungen der Stufen 2 oder 3 benötigen. Anforderungen der Stufe 1 können entweder automatisch durch Tools oder manuell ohne Zugriff auf den Quellcode überprüft werden.

Bedrohungen auf Stufe 1 gehen von Angreifern aus, die einfache und wenig aufwendige Techniken verwenden, um leicht zu findende und leicht ausnutzbare Schwachstellen zu ermitteln. Sie ist ungeeignet zur Abwehr entschlossener Angreifer, die die Anwendung gezielt ins Visier nehmen. Wenn Ihre Anwendung hochwertige Daten verarbeitet, werden Sie kaum mit einer Überprüfung der Stufe 1 zufrieden sein.

### Stufe 2 – Die meisten Anwendungen

Eine Anwendung erreicht ASVS Level 2 (oder Standard), wenn sie die meisten Risiken, die heutzutage mit dem Einsatz von Software verbunden sind, angemessen abwehrt.

Dabei wird sichergestellt, dass Sicherheitsmaßnahmen wirksam umgesetzt sind. Stufe 2 eignet sich in der Regel für Anwendungen, die wichtige Geschäftsvorgänge abwickeln, einschließlich solcher, die Informationen aus dem Gesundheitswesen verarbeiten, geschäftskritische oder sensible Funktionen umsetzen oder andere sensible Vermögenswerte verarbeiten. Sie eignet sich auch für Branchen, in denen Integrität ein kritischer Aspekt zum Schutz ihres Geschäfts ist, wie z. B. die Spieleindustrie, um Betrügern und Gamehacks entgegenzuwirken.

Maßnahmen zum Schutz der Anwendung auf Stufe 2 gehen in der Regel von geschickten und motivierten Angreifern aus, die sich auf bestimmte Ziele konzentrieren und Tools und Techniken einsetzen, die sehr versiert und wirksam Schwachstellen in Anwendungen entdecken und ausnutzen.

### Stufe 3 - Hoher Wert, hohe Zuverlässigkeit oder hohe Sicherheit

ASVS Stufe 3 (oder Erweitert) ist die höchste Verifizierungsstufe innerhalb des ASVS. Diese Stufe ist in der Regel Anwendungen vorbehalten, die ein erhebliches Maß an geprüften Sicherheitsniveau erfordern. Diese sind z.B. im militärischen Bereich, dem Gesundheitssektor oder kritischen Infrastrukturen zu finden.

Organisationen können ASVS Stufe 3 bei Anwendungen benötigen, die kritische Funktionen ausführen und bei denen ein Ausfall die Betriebsabläufe der Organisation oder sogar ihre Überlebensfähigkeit erheblich beeinträchtigen könnte. Eine Anwendung erreicht ASVS-Stufe 3, wenn sie angemessen vor fortgeschrittenen Schwachstellen geschützt ist und die Grundsätze eines guten Sicherheitsdesigns aufweist.

Eine Prüfung auf ASVS-Stufe 3 erfordert eine tiefgründigere Analyse der Architektur, der Programmierung und der Testprozesse als alle anderen Ebenen. Eine sichere Anwendung wird auf sinnvolle Weise modularisiert. So können Resilienz, Skalierbarkeit und vor allem Kapselung leichter umgesetzt werden, da sich jedes Modul selbst um seine eigenen Sicherheitsmaßnahmen kümmern kann (Defense in Depth). Die Umsetzung dieser Maßnahmen muss ordnungsgemäß dokumentiert werden.

## Auswahl der ASVS-Stufen in der Praxis

Unterschiedliche Angreifer haben unterschiedliche Beweggründe. Einige Branchen verfügen über einzigartige Informations- und Technologiewerte sowie branchenspezifische gesetzliche Regulierungen.

Wir raten Organisationen dringend dazu, ihre spezifischen Risikomerkmale auf der Grundlage ihres Geschäftsmodells eingehend zu prüfen. Auf dieser Basis wählen sie dann die geeignete ASVS-Stufe aus.

## Referenzen auf Anforderungen des ASVS

Jede Anforderung des ASVS wird mittels `<Kapitel>.<Abschnitt>.<Laufende Nummer>` identifiziert, z.B.: `1.11.3`.
- Das `<Kapitel>` gibt Anforderungen das Kapitel des Standards an, dem die Anforderung entstammt, z.B.: alle Anforderungen mit der Nummer `1.#.#` sind an die Architektur.
- Der `<Abschnitt>` referenziert auf den Abschnitt, in dem die Anforderung beschrieben wird, z.B.: alle Anforderungen mit der Nummer `1.11.#` beziehen sich auf die architekturellen Anforderungen an die Geschäftslogik.
- Innerhalb der Abschnitte gibt die `<Laufende Nummer>` schließlich die konkrete Anforderung an, so steht `1.11.3` in der Version 4.0.3 dieses Standards für:

> Prüfen Sie, dass alle geschäftskritischen Abläufe, einschließlich der Authentifizierung, des Sessionmanagements und der Zugriffssteuerung thread-sicher und sicher gegen TOCTOU Race Conditions sind.

Da sich die Kennungen der Anforderungen von Version zu Version ändern, sollten andere DOkumente oder Werkzeuge das Format `v<Version>-<Kapitel>.<Abschnitt>.<Laufende Nummer>` nutzen. 'Version' ist die Versionsnummer des ASVS, z.B.: ist `v4.0.3-1.11.3` die dritte Anforderung des Abschnittes Architektur der Geschäftslogik im Kapitel Architektur, Design und Threat Modeling der Version 4.0.3. Das kann zu `v<Version>-<AnforderungsID>` zusammengefasst werden.

Hinweis: Das `v` vor der Versionsnummer ist ein Kleinbuchstabe.

Falls AnforderungsIDs ohne die Angabe der Version genutzt werden, so ist anzunehmen, dass die aktuelle Version des ASVS gemeint ist. Da der Standard wächst, sollte die Version stets angegeben werden.

Die ASVS Anforderungen werden in CSV, JSON und anderen Formaten zur Verfügung gestellt.
