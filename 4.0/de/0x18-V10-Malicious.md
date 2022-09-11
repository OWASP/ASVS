# V10 Bösartiger Code

## Ziel

Stellen Sie sicher, dass der Code die folgenden High Level Anforderungen erfüllt:

* Böswillige Aktivitäten werden sicher und ordnungsgemäß behandelt, um den Rest der Anwendung nicht zu beeinträchtigen.
* Es gibt keine Zeitbomben oder andere zeitbasierte Angriffe.
* Es gibt kein „Phone Home“ zu böswilligen oder nicht autorisierten Zielen.
* Es gibt keine Hintertüren, Ostereier, Salamitaktik-Angriffe, Rootkits oder nicht autorisierte Codes, die von einem Angreifer kontrolliert werden können.

Das Feststellen der Abwesenheit bösartigen Codes ist der Negativbeweis, der unmöglich vollständig geführt werden kann. Es sollten alle Anstrengungen unternommen werden, um sicherzustellen, dass die Software keinen inhärenten bösartigen Code und keine unerwünschten Funktionen aufweist.

## V10.1 Kontrollen der Code-Integrität

Die beste Verteidigung gegen bösartigen Code ist der Wahlspruch „Vertrauen ist gut, Kontrolle ist besser“. Das Einbringen eines nicht autorisierten oder bösartigen Codes in eine Software ist in vielen Rechtsordnungen ein kriminelles Vergehen. Die Richtlinien zur Softwareentwicklung sollten auf die Sanktionen für das Einbringen bösartigen Codes deutlich hinweisen. Leitende Entwickler sollten regelmäßig die Eincheckvorgänge für den Code überprüfen, insbesondere diejenigen, die auf Zeit-, Eingabe-, Ausgabe- oder Netzwerkfunktionen zugreifen können.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.1.1** | Prüfen Sie, dass ein Codeanalyse-Tool verwendet wird, das potenziell bösartigen Code, wie Zeitfunktionen, unsichere Dateioperationen und Netzwerkverbindungen erkennen kann. | | | ✓ | 749 |

## V10.2 Suche nach bösartigem Code

Bösartiger Code ist extrem selten und schwer zu erkennen. Eine manuelle, zeilenweise Überprüfung des Codes kann bei der Suche nach Logikbomben helfen, aber selbst die erfahrensten Codereviewer werden Schwierigkeiten haben, bösartigen Code zu finden, selbst wenn sie wissen, dass er existiert. Die Einhaltung dieses Abschnitts kann nicht ohne vollständigen Zugriff auf den Quellcode, einschließlich der Bibliotheken von Drittanbietern, geprüft werden.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.2.1** | Prüfen Sie, dass der Quellcode der Anwendung und die Bibliotheken von Drittanbietern keine Möglichkeiten zum Phone Home oder zur Datenerfassung enthalten. Wenn solche Funktionen vorhanden sind, holen Sie die Erlaubnis des Benutzers ein, bevor Daten gesammelt werden. | | ✓ | ✓ | 359 |
| **10.2.2** | Prüfen Sie, dass die Anwendung keine unnötigen oder übermäßigen Genehmigungen für datenschutzrelevante Funktionen oder Sensoren wie Kontakte, Kameras, Mikrofone oder Standorte verlangt. | | ✓ | ✓ | 272 |
| **10.2.3** | Prüfen Sie, dass der Quellcode der Anwendung und die Bibliotheken von Drittanbietern keine Hintertüren enthalten, wie z. B. hartcodierte oder zusätzliche undokumentierte Konten oder Schlüssel, Codeverschleierung, undokumentierte Binärblobs, Rootkits oder Anti-Debugging, unsichere Debuggingfunktionen oder andere veraltete, unsichere oder versteckte Funktionen, die bei Entdeckung böswillig verwendet werden könnten. | | | ✓ | 507 |
| **10.2.4** | Prüfen Sie, dass der Quellcode der Anwendung und die Bibliotheken von Drittanbietern keine Zeitbomben enthalten, wenn sie nach datums- und zeitbezogenen Funktionen suchen. | | | ✓ | 511 |
| **10.2.5** | Prüfen Sie, dass der Quellcode der Anwendung und die Bibliotheken von Drittanbietern keinen bösartigen Code wie Salamitaktik-Angriffe, logische Umgehungen oder Logikbomben enthalten. | | | ✓ | 511 |
| **10.2.6** | Prüfen Sie, dass der Quellcode der Anwendung und die Bibliotheken von Drittanbietern keine Ostereier oder andere unerwünschte Funktionen enthalten. | | | ✓ | 507 |

## V10.3 Integrität der Anwendung

Nach Bereitstellung einer Anwendung kann immer noch bösartiger Code eingefügt werden. Anwendungen müssen sich vor gängigen Angriffen wie die Ausführung unsignierten Codes aus nicht vertrauenswürdigen Quellen und die Übernahme von Subdomänen schützen. Die Einhaltung der Anforderungen dieses Abschnitts sind operativ und fortlaufend zu prüfen.

| # | Beschreibung | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.3.1** | Prüfen Sie, dass Updates über sichere Kanäle bezogen und digital signiert werden müssen, wenn die Anwendung über eine automatische Client- oder Server Updatefunktion verfügt. Die digitale Signatur des Updates muss validiert werden, bevor das Update installiert wird. | ✓ | ✓ | ✓ | 16 |
| **10.3.2** | Prüfen Sie, dass die Anwendung einen Integritätsschutz, wie Code Signing oder Subresource Integrity verwendet. Die Anwendung darf keinen Code aus nicht vertrauenswürdigen Quellen laden oder ausführen, wie z. B. das Laden von Includes, Modulen, Plugins, Codes oder Bibliotheken aus nicht vertrauenswürdigen Quellen oder dem Internet. | ✓ | ✓ | ✓ | 353 |
| **10.3.3** | Prüfen Sie, ob die Anwendung Schutz vor der Übernahme von Subdomänen bietet, wenn die Anwendung auf DNS-Einträge oder DNS-Subdomänen angewiesen ist, z. B. abgelaufene Domänennamen, veraltete DNS-Pointer oder CNAMEs, abgelaufene Projekte in öffentlichen Quellcoderepositories oder vorübergehende Cloud-APIs, serverlose Funktionen oder Storage Buckets (autogen-bucket-id.cloud.example.com) oder Ähnliches. Die von den Anwendungen verwendeten DNS-Namen sind regelmäßig auf Ablauf oder Änderung zu überprüfen. | ✓ | ✓ | ✓ | 350 |

## Referenzen

Weitere Informationen finden Sie unter:

* [Hostile Subdomain Takeover, Detectify Labs](https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/)
* [Hijacking of abandoned subdomains part 2, Detectify Labs](https://labs.detectify.com/2014/12/08/hijacking-of-abandoned-subdomains-part-2/)
