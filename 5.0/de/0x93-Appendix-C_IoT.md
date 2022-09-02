# Appendix C: Internet of Things Verification Requirements

Dieser Abschnitt gehörte ursprünglich zum Hauptzweig, inzwischen hat das OWASP IoT-Team viel geleistet, so dass es keinen Sinn hat, zwei verschiedene Standards zu diesem Thema beizubehalten. Für die Version 4.0 verschieben wir diesen Abschnitt in den Anhang und empfehlen allen, lieber das OWASP IoT-Hauptprojekt zu verwenden.

## Ziel

Eingebettete/IoT-Geräte sollten:

* das selbe Maß an Sicherheitsmaßnahmen innerhalb des Geräts haben, wie es im Server zu finden ist. Sicherheitsmaßnahmen sollen in einer vertrauenswürdigen Umgebung durchgesetzt werden.
* Sensible Daten, die auf dem Gerät gespeichert sind, sollten auf sichere Weise unter Verwendung von hardwaregestütztem Speicher gespeichert werden.
* Alle vom Gerät übertragenen sensiblen Daten sollten auf der Transportschicht gesichert werden.

## Anforderungen an die Prüfung

| # | Description | L1 | L2 | L3 | Since |
| --- | --- | --- | --- | -- | -- |
| **C.1** | Prüfen Sie, dass die Debugging-Schnittstellen der Anwendungsschicht wie USB, UART und andere serielle Varianten deaktiviert oder durch ein komplexes Kennwort geschützt sind. | ✓ | ✓ | ✓ | 4.0 |
| **C.2** | Prüfen Sie, dass kryptographische Schlüssel und Zertifikate für jedes einzelne Gerät eindeutig sind. | ✓ | ✓ | ✓ | 4.0 |
| **C.3** | Prüfen Sie, dass Speicherschutzmaßnahmen wie ASLR und DEP durch das Betriebssystem aktiviert sind. | ✓ | ✓ | ✓ | 4.0 |
| **C.4** | Prüfen Sie, dass On-Chip-Debugging-Schnittstellen wie JTAG oder SWD deaktiviert sind, oder dass der verfügbare Schutzmechanismus aktiviert und entsprechend konfiguriert ist. | ✓ | ✓ | ✓ | 4.0 |
| **C.5** | Prüfen Sie, dass Trusted Execution implementiert und aktiviert ist, falls auf dem SoC oder der CPU des Geräts verfügbar. | ✓ | ✓ | ✓ | 4.0 |
| **C.6** | Prüfen Sie, dass sensible Daten, private Schlüssel und Zertifikate sicher in einem Secure Element, TPM, TEE (Trusted Execution Environment) gespeichert oder durch starke Kryptographie geschützt sind. | ✓ | ✓ | ✓ | 4.0 |
| **C.7** | Prüfen Sie, dass die Firmware-Anwendungen Daten während der Übertragung auf der Transportschicht schützen. | ✓ | ✓ | ✓ | 4.0 |
| **C.8** | Prüfen Sie, dass die Firmware- Anwendungen die digitale Signatur der Serververbindungen validieren. | ✓ | ✓ | ✓ | 4.0 |
| **C.9** | Prüfen Sie, dass drahtlose Kommunikationen gegenseitig authentifiziert sind. | ✓ | ✓ | ✓ | 4.0 |
| **C.10** | Prüfen Sie, dass die drahtlose Kommunikation über einen verschlüsselten Kanal gesendet wird. | ✓ | ✓ | ✓ | 4.0 |
| **C.11** | Prüfen Sie, dass alle verbotenen C-Funktionen durch die entsprechenden sicheren gleichwertigen Funktionen ersetzt wird. | ✓ | ✓ | ✓ | 4.0 |
| **C.12** | Prüfen Sie, dass jede Firmware ein automatisches Stücklistenmanagement führt, in der die Komponenten von Drittanbietern, die Versionierung und die veröffentlichten Schwachstellen katalogisiert sind. | ✓ | ✓ | ✓ | 4.0 |
| **C.13** | Prüfen Sie, alle Codes, einschließlich der Binärdateien, Bibliotheken und Frameworks von Drittanbietern auf hartkodierte Anmeldedaten (Backdoors). | ✓ | ✓ | ✓ | 4.0 |
| **C.14** | Prüfen Sie, dass die Anwendungs- und Firmware-Komponenten nicht für OS Command Injection anfällig sind, indem sie Shell Command Wrapper oder Skripte aufrufen, oder dass Sicherheitsmaßnahmen OS Command Injection verhindern. | ✓ | ✓ | ✓ | 4.0 |
| **C.15** | Prüfen Sie, dass die Firmware-Anwendungen die digitale Signatur an einen oder mehrere vertrauenswürdige Server pinnt. |  | ✓ | ✓ | 4.0 |
| **C.16** | Prüfen Sie das Vorhandensein von Merkmalen zur Verhinderung oder Erkennung von Manipulationen am Gerät. |  | ✓ | ✓ | 4.0 |
| **C.17** | Prüfen Sie, dass alle verfügbaren Technologien zum Schutz des geistigen Eigentums, die vom Chiphersteller zur Verfügung gestellt werden, aktiviert sind. |  | ✓ | ✓ | 4.0 |
| **C.18** | Prüfen Sie, dass Sicherheitsmaßnahmen vorhanden sind, um ein Reverse Engineering der Firmware (z.B. Entfernen von ausführlichen Debugging-Symbolen) zu verhindern. |  | ✓ | ✓ | 4.0 |
| **C.19** | Prüfen Sie, dass das Gerät die Signatur des Bootimages vor dem Laden validiert. |  | ✓ | ✓ | 4.0 |
| **C.20** | Prüfen Sie, dass der Firmware-Aktualisierungsprozess nicht anfällig für TOCTOU Race Conditions ist. |  | ✓ | ✓ | 4.0 |
| **C.21** | Prüfen Sie, dass das Gerät Code Signing verwendet und Firmware-Upgrade-Dateien vor der Installation validiert. |  | ✓ | ✓ | 4.0 |
| **C.22** | Prüfen Sie, dass das Gerät nicht auf alte Versionen (Anti-Rollback) von gültiger Firmware zurückgestuft werden kann. |  | ✓ | ✓ | 4.0 |
| **C.23** | Prüfen Sie die Verwendung eines kryptographisch sicheren Zufallszahlengenerators auf einem eingebetteten Gerät, z.B. unter Verwendung von Hardware. |  | ✓ | ✓ | 4.0 |
| **C.24** | Prüfen Sie, ob die Firmware automatische Firmware-Updates nach einem vordefinierten Zeitplan durchführen kann. |  | ✓ | ✓ | 4.0 |
| **C.25** | Prüfen Sie, dass das Gerät Firmware und sensible Daten löscht, wenn eine Manipulation oder der Empfang einer ungültigen Nachricht festgestellt wird. |  |  | ✓ | 4.0 |
| **C.26** | Prüfen Sie, dass nur Mikrocontroller verwendet werden, die das Deaktivieren von Debugging-Schnittstellen (z.B. JTAG, SWD) unterstützen. |  |  | ✓ | 4.0 |
| **C.27** | Prüfen Sie, dass nur Mikrocontroller verwendet werden, die einen wesentlichen Schutz vor De-Capping- und Seitenkanal-Angriffen bieten. |  |  | ✓ | 4.0 |
| **C.28** | Prüfen Sie, dass Leiterbahnen zur Übertragung sensibler Daten nicht auf den äußeren Schichten der Leiterplatte ausgesetzt sind. |  |  | ✓ | 4.0 |
| **C.29** | Prüfen Sie, dass die Kommunikation zwischen den Chips, z. B. die Kommunikation von Haupt- und Tochterplatine, verschlüsselt ist. |  |  | ✓ | 4.0 |
| **C.30** | Prüfen Sie, dass das Gerät Code Signing verwendet und den Code vor der Ausführung validiert. |  |  | ✓ | 4.0 |
| **C.31** | Prüfen Sie, dass sensible Informationen, die im Speicher gehalten werden, mit Nullen überschrieben werden, sobald sie nicht mehr benötigt werden. |  |  | ✓ | 4.0 |
| **C.32** | Prüfen Sie, dass die Firmware-Anwendungen Kernel-Container als Isolierung zwischen den Anwendungen verwenden. |  |  | ✓ | 4.0 |
| **C.33** | Prüfen Sie, dass sichere Compiler-Flags wie -fPIE, -fstack-protector-all, -Wl,- z,noexecstack, -Wl,-z,noexecheap für Firmware-Builds konfiguriert sind. |  |  | ✓ | 4.0 |
| **C.34** | Prüfen Sie, dass die Mikrocontroller mit Codeschutz konfiguriert sind (falls zutreffend). |  |  | ✓ | 4.0 |

## Referenzen

Weitere Informationen finden Sie unter:

* [OWASP Internet of Things Top 10](https://owasp.org/www-pdf-archive/OWASP-IoT-Top-10-2018-final.pdf)
* [OWASP Embedded Application Security Project](https://owasp.org/www-project-embedded-application-security/)
* [OWASP Internet of Things Project](https://owasp.org/www-project-internet-of-things/)
* [Trudy TCP Proxy Tool](https://github.com/praetorian-inc/trudy)
