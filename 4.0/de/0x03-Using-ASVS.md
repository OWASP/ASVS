# Verwendung des ASVS

Der ASVS hat die zwei Hauptziele:

* Organisationen bei der Entwicklung und Pflege sicherer Anwendungen zu unterst�tzen.
* Anbietern von Sicherheitsdienstleistungen oder -werkzeugen und deren Kunden die M�glichkeit zu geben, ihre Anforderungen und Angebote aufeinander abzustimmen.

## Stufen zur Verifizierung der Anwendungssicherheit

Der Application Security Verification Standard definiert drei Stufen der Sicherheitsverifikation, wobei jede Stufe an Tiefe zunimmt.

* Stufe 1 ist f�r geringe Sicherheitsanforderungen gedacht und l�sst sich mittels Pentests pr�fen.
* Stufe 2 ist f�r Anwendungen, die sensible Daten enthalten und diese sch�tzen m�ssen. Das ist die empfohlene Stufe f�r die meisten Anwendungen.  
* Stufe 3 ist f�r die kritischsten Anwendungen, z. B. solche, die hochwertige Transaktionen durchf�hren, sensible medizinische Daten enthalten oder aus anderen Gr�nden ein H�chstma� an Vertrauen erfordern.

Jede Stufe des ASVS enth�lt eine Liste von Sicherheitsanforderungen. Jede dieser Anforderungen kann auch auf sicherheitsspezifische Merkmale und F�higkeiten abgebildet werden, die von den Entwicklern in die Software eingebaut werden m�ssen.

![ASVS Levels](https://raw.githubusercontent.com/OWASP/ASVS/master/4.0/images/asvs_40_levels.png "ASVS Stufen")

Figure 1 - Stufen des OWASP Application Security Verification Standard 4.0 

Stufe 1 ist die einzige Stufe, die sich komplett mittels Pentests pr�fen l�sst. Alle anderen Stufen ben�tigen Zugang zu Dokumentation, Quellcode, Konfiguration und den am Entwicklungsprozess beteiligten Personen. Jedoch stellen Black Box Tests ohne Dokumentation und ohne Quellen keine wirksame Absicherung dar. Sie m�ssen langfristig erg�nzt werden. B�swillige Angreifer haben sehr viel Zeit. Die meisten Penetrationstests hingegen sind innerhalb von wenigen Wochen abgeschlossen. Die Verteidiger m�ssen alle Sicherheitsma�nahmen umsetzen, alle Schwachstellen finden und beheben sowie b�swillige Akteure innerhalb einer angemessenen Zeit aufsp�ren und Gegenma�nahmen ergreifen. B�swillige Akteure haben im Wesentlichen unendlich viel Zeit und ben�tigen nur eine einzige L�cke in der Verteidigung, eine einzige Schwachstelle, um erfolgreich zu sein. Black Box Tests, die oft am Ende der Entwicklung schnell oder gar nicht durchgef�hrt werden, sind v�llig ungeeignet, dieser Asymmetrie gerecht zu werden.

Die letzten 30 Jahre haben gezeigt, dass Black Box Tests immer wieder kritische Sicherheitsprobleme �bersehen, welche direkt zu weiteren, massiveren Problemen gef�hrt haben. Wir bef�rworten ausdr�cklich den Einsatz einer breiten Palette von Ma�nahmen zur Gew�hrleistung und Verifizierung der Sicherheit, einschlie�lich des Ersatzes der Penetrationstests durch quellcodegef�hrte (hybride) Penetrationstests auf Stufe 1, mit vollem Zugang zu den Entwicklern und der Dokumentation w�hrend des gesamten Entwicklungsprozesses. Die Finanzaufsichtsbeh�rden dulden keine externen Finanzpr�fungen ohne Zugang zu den B�chern, zu Stichproben von Gesch�ftsvorg�ngen oder zu den Personen, welche die Pr�fungen durchf�hren. Derselbe Standard an Transparenz muss von der Industrie und den Regierungen auch im Bereich der Softwareentwicklung gefordert werden.

Wir bef�rworten ausdr�cklich die Verwendung von Sicherheitstools innerhalb des Entwicklungsprozesses. DAST- und SAST-Tools k�nnen in die Buildpipeline eingebunden werden, um leicht zu findende Sicherheitsprobleme aufzusp�ren, die niemals vorhanden sein d�rfen. Automatisierte Tools und Onlinescans k�nnen h�chsten nur noch die H�lfte des ASVS ohne menschliches Zutun erfassen. Ist eine umfassende Testautomatisierung f�r jeden Buildprozess erforderlich, wird eine Kombination aus benutzerdefinierten Unit- und Integrationstests zusammen mit den vom Buildprozess veranlassten Onlinescans verwendet. M�ngel der Gesch�ftslogik und der Zugriffskontrolle lassen sich nur mit menschlicher Hilfe testen, am besten in Unit- und Integrationstests.
           
## Verwendung dieses Standards

Eine der besten M�glichkeiten, den Application Security Verification Standard zu nutzen, ist seine Verwendung als Vorlage f�r die Erstellung einer Checkliste f�r Anforderungen zur sicheren Softwareentwicklung, die speziell auf Ihre Anwendung, Plattform oder Organisation zugeschnitten ist. In dem Sie die Anforderungen des ASVS auf Ihre Anwendungsf�lle passend zuschneiden, setzen Sie den Schwerpunkt auf die Sicherheitsanforderungen, die f�r Ihre Projekte und Umgebungen am wichtigsten sind.

Zu den Sicherheitszielen aller Stufen geh�ren die Gew�hrleistung der Vertraulichkeit (z.B. Verschl�sselung), der Integrit�t (z.B. Transaktionen, Eingabevalidierung), der Verf�gbarkeit (z.B. ordnungsgem��e Lastverteilung), der Authentifizierung (auch zwischen Systemen), der Nichtabstreitbarkeit, der Autorisierung und der Protokollierung.

### Stufe 1 - Erste Schritte oder das absolute Minimum

Eine Anwendung erreicht ASVS Stufe 1, wenn sie einen ausreichenden Schutz gegen leicht zu entdeckende Schwachstellen bietet, die auch in den OWASP Top 10 und anderen �hnlichen Checklisten aufgef�hrt sind. Stufe 1 ist das f�r alle Anwendungen erforderliche absolute Minimum. Sie ist auch n�tzlich als erster Schritt eines mehrstufigen Prozesses oder f�r den Fall, wenn Anwendungen keine sensiblen Daten verarbeiten und daher nicht die strengeren Anforderungen der Stufen 2 oder 3 ben�tigen. Anforderungen der Stufe 1 k�nnen entweder automatisch durch Tools oder manuell ohne Zugriff auf den Quellcode �berpr�ft werden. 

Bedrohungen auf Stufe 1 gehen von Angreifern aus, die einfache und wenig aufwendige Techniken verwenden, um leicht zu findende und leicht ausnutzbare Schwachstellen zu ermitteln. Sie ist ungeeignet zur Abwehr entschlossener Angreifer, die die Anwendung gezielt ins Visier nehmen. Wenn Ihre Anwendung hochwertige Daten verarbeitet, werden Sie kaum mit einer �berpr�fung der Stufe 1 zufrieden sein.

### Stufe 2 � Die meisten Anwendungen

Eine Anwendung erreicht ASVS Level 2 (oder Standard), wenn sie die meisten Risiken, die heutzutage mit dem Einsatz von Software verbunden sind, angemessen abwehrt. Dabei wird sichergestellt, dass Sicherheitsma�nahmen wirksam umgesetzt sind. Stufe 2 eignet sich in der Regel f�r Anwendungen, die wichtige Gesch�ftsvorg�nge abwickeln, einschlie�lich solcher, die Informationen aus dem Gesundheitswesen verarbeiten, gesch�ftskritische oder sensible Funktionen umsetzen oder andere sensible Verm�genswerte verarbeiten. Sie eignet sich auch f�r Branchen, in denen Integrit�t ein kritischer Aspekt zum Schutz ihres Gesch�fts ist, wie z. B. die Spieleindustrie, um Betr�gern und Gamehacks entgegenzuwirken.

Ma�nahmen zum Schutz der Anwendung auf Stufe 2 gehen in der Regel von geschickten und motivierten Angreifern aus, die sich auf bestimmte Ziele konzentrieren und Tools und Techniken einsetzen, die sehr versiert und wirksam Schwachstellen in Anwendungen entdecken und ausnutzen.

### Stufe 3 - Hoher Wert, hohe Zuverl�ssigkeit oder hohe Sicherheit

ASVS Stufe 3 (oder Erweitert) ist die h�chste Verifizierungsstufe innerhalb des ASVS. Diese Stufe ist in der Regel Anwendungen vorbehalten, die ein erhebliches Ma� an gepr�ften Sicherheitsniveau erfordern. Diese sind z.B. im milit�rischen Bereich, dem Gesundheitssektor oder kritischen Infrastrukturen zu finden. Organisationen k�nnen ASVS Stufe 3 bei Anwendungen ben�tigen, die kritische Funktionen ausf�hren und bei denen ein Ausfall die Betriebsabl�ufe der Organisation oder sogar ihre �berlebensf�higkeit erheblich beeintr�chtigen k�nnte. Eine Anwendung erreicht ASVS-Stufe 3, wenn sie angemessen vor fortgeschrittenen Schwachstellen gesch�tzt ist und die Grunds�tze eines guten Sicherheitsdesigns aufweist. Eine Pr�fung auf ASVS-Stufe 3 erfordert eine tiefgr�ndigere Analyse der Architektur, der Programmierung und der Testprozesse als alle anderen Ebenen. Eine sichere Anwendung wird auf sinnvolle Weise modularisiert. So k�nnen Resilienz, Skalierbarkeit und vor allem Kapselung leichter umgesetzt werden, da sich jedes Modul selbst um seine eigenen Sicherheitsma�nahmen k�mmern kann (Defense in Depth). Die Umsetzung dieser Ma�nahmen muss ordnungsgem�� dokumentiert werden.

## Auswahl der ASVS-Stufen in der Praxis

Unterschiedliche Angreifer haben unterschiedliche Beweggr�nde. Einige Branchen verf�gen �ber einzigartige Informations- und Technologiewerte sowie branchenspezifische gesetzliche Regulierungen. Wir raten Organisationen dringend dazu, ihre spezifischen Risikomerkmale auf der Grundlage ihres Gesch�ftsmodells eingehend zu pr�fen. Auf dieser Basis w�hlen sie dann die geeignete ASVS-Stufe aus.

## Referenzen auf Anforderungen des ASVS

Jede Anforderung des ASVS wird durch v`<Version>-<Kapitel>.<Abschnitt>.<Laufende Nummer>` identifiziert, z.B.: `v4.0.3-1.11.3`

- Die `<Version>` benennt die Version des ASVS. Im Laufe der Entwicklung des ASVS kann sich die Nummerierung zwischen den Versionen des Standards �ndern. Das sich Referenzen ohne Versionsangabe immer auf die aktuelle Version des Standards beziehen, kann dies problematisch werden. Das �v� wird dabei klein geschrieben.
- Das `<Kapitel>` gibt Anforderungen das Kapitel des Standards an, dem die Anforderung entstammt, z.B.: alle Anforderungen mit der Nummer `1.#.#` sind an die Architektur.
- Der `<Abschnitt>` referenziert auf den Abschnitt, in dem die Anforderung beschrieben wird, z.B.: alle Anforderungen mit der Nummer `1.11.#` beziehen sich auf die architekturellen Anforderungen an die Gesch�ftslogik.
- Innerhalb der Abschnitte gibt die `<Laufende Nummer>` schlie�lich die konkrete Anforderung an.

Die ASVS Anforderungen werden in CSV, JSON und anderen Formaten zur Verf�gung gestellt.
