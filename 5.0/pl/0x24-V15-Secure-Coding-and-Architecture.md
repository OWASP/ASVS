# V15 Bezpieczne kodowanie i architektura

## Cel kontrolny

Wiele wymagań ASVS dotyczy konkretnego obszaru bezpieczeństwa, takiego jak uwierzytelnianie czy autoryzacja, albo odnosi się do konkretnego typu funkcjonalności aplikacji, jak logowanie zdarzeń czy obsługa plików.

Niniejszy rozdział zawiera ogólne wymagania bezpieczeństwa, które należy uwzględnić przy projektowaniu i tworzeniu aplikacji. Wymagania te koncentrują się nie tylko na czystej architekturze i jakości kodu, lecz również na konkretnych praktykach architektonicznych i programistycznych niezbędnych dla bezpieczeństwa aplikacji.

## V15.1 Dokumentacja bezpiecznego kodowania i architektury

Wiele wymagań dotyczących ustanowienia bezpiecznej i możliwej do obrony architektury zależy od jasnej dokumentacji decyzji podjętych w sprawie implementacji konkretnych mechanizmów bezpieczeństwa oraz komponentów używanych w aplikacji.

Ta sekcja przedstawia wymagania dokumentacyjne, w tym identyfikację komponentów uznawanych za zawierające „niebezpieczną funkcjonalność” lub będące „komponentami ryzykownymi”.

Komponent z „niebezpieczną funkcjonalnością” może być komponentem tworzonym wewnętrznie lub zewnętrznym, wykonującym operacje takie jak deserializacja niezaufanych danych, parsowanie surowych plików lub danych binarnych, dynamiczne wykonywanie kodu czy bezpośrednia manipulacja pamięcią. Podatności w tego typu operacjach niosą wysokie ryzyko kompromitacji aplikacji i potencjalnego wystawienia jej infrastruktury.

„Komponent ryzykowny” to biblioteka strony trzeciej (tj. nietworzona wewnętrznie) z brakującymi lub słabo zaimplementowanymi mechanizmami bezpieczeństwa w procesach jej rozwoju lub funkcjonalności. Przykłady obejmują komponenty słabo utrzymywane, niewspierane, będące u kresu cyklu życia lub mające historię istotnych podatności.

Ta sekcja podkreśla również wagę zdefiniowania odpowiednich ram czasowych usuwania podatności w komponentach stron trzecich.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **15.1.1** | Zweryfikuj, że dokumentacja aplikacji definiuje oparte na ryzyku ramy czasowe naprawy dla wersji komponentów stron trzecich z podatnościami oraz ogólnie dla aktualizacji bibliotek, aby zminimalizować ryzyko związane z tymi komponentami. | 1 |
| **15.1.2** | Zweryfikuj, że utrzymywany jest katalog inwentaryzacyjny, taki jak software bill of materials (SBOM), obejmujący wszystkie używane biblioteki stron trzecich, w tym weryfikację, że komponenty pochodzą ze wstępnie zdefiniowanych, zaufanych i stale utrzymywanych repozytoriów. | 2 |
| **15.1.3** | Zweryfikuj, że dokumentacja aplikacji identyfikuje funkcjonalność czasochłonną lub zasobożerną. Musi to obejmować sposób zapobiegania utracie dostępności wskutek nadużywania tej funkcjonalności oraz unikania sytuacji, w której budowanie odpowiedzi trwa dłużej niż limit czasu konsumenta. Potencjalne obrony mogą obejmować przetwarzanie asynchroniczne, użycie kolejek oraz ograniczanie procesów równoległych dla każdego użytkownika i każdej aplikacji. | 2 |
| **15.1.4** | Zweryfikuj, że dokumentacja aplikacji wskazuje biblioteki stron trzecich uznawane za „komponenty ryzykowne”. | 3 |
| **15.1.5** | Zweryfikuj, że dokumentacja aplikacji wskazuje części aplikacji, w których używana jest „niebezpieczna funkcjonalność”. | 3 |

## V15.2 Architektura bezpieczeństwa i zależności

Ta sekcja zawiera wymagania dotyczące postępowania z ryzykownymi, przestarzałymi lub niebezpiecznymi zależnościami i komponentami poprzez zarządzanie zależnościami.

Obejmuje również stosowanie technik na poziomie architektury — takich jak sandboxing, enkapsulacja, konteneryzacja i izolacja sieciowa — w celu ograniczenia skutków używania „niebezpiecznych operacji” lub „komponentów ryzykownych” (zdefiniowanych w poprzedniej sekcji) oraz zapobiegania utracie dostępności wskutek nadużywania funkcjonalności zasobożernej.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **15.2.1** | Zweryfikuj, że aplikacja zawiera wyłącznie komponenty, które nie przekroczyły udokumentowanych ram czasowych aktualizacji i naprawy. | 1 |
| **15.2.2** | Zweryfikuj, że aplikacja wdrożyła obrony przed utratą dostępności wskutek funkcjonalności czasochłonnej lub zasobożernej, zgodnie z udokumentowanymi decyzjami bezpieczeństwa i strategiami w tym zakresie. | 2 |
| **15.2.3** | Zweryfikuj, że środowisko produkcyjne zawiera wyłącznie funkcjonalność wymaganą do działania aplikacji i nie eksponuje zbędnej funkcjonalności, takiej jak kod testowy, przykładowe fragmenty czy funkcjonalność deweloperska. | 2 |
| **15.2.4** | Zweryfikuj, że komponenty stron trzecich i wszystkie ich zależności przechodnie pochodzą z oczekiwanego repozytorium — wewnętrznego lub zewnętrznego — oraz że nie istnieje ryzyko ataku dependency confusion. | 3 |
| **15.2.5** | Zweryfikuj, że aplikacja wdraża dodatkowe zabezpieczenia wokół części aplikacji udokumentowanych jako zawierające „niebezpieczną funkcjonalność” lub używające bibliotek stron trzecich uznawanych za „komponenty ryzykowne”. Może to obejmować techniki takie jak sandboxing, enkapsulacja, konteneryzacja lub izolacja na poziomie sieci, aby opóźnić i zniechęcić atakujących, którzy skompromitowali jedną część aplikacji, przed przemieszczaniem się (pivoting) w inne jej miejsca. | 3 |

## V15.3 Kodowanie defensywne

Ta sekcja obejmuje typy podatności — w tym type juggling, prototype pollution i inne — wynikające ze stosowania niebezpiecznych wzorców kodowania w danym języku. Część z nich może nie dotyczyć wszystkich języków, inne będą miały poprawki specyficzne dla języka albo będą związane ze sposobem, w jaki dany język lub framework obsługuje funkcję taką jak parametry HTTP. Sekcja uwzględnia również ryzyko braku kryptograficznej walidacji aktualizacji aplikacji.

Rozważa również ryzyka związane z używaniem obiektów do reprezentowania elementów danych oraz przyjmowaniem i zwracaniem ich przez zewnętrzne API. W takim przypadku aplikacja musi zapewnić, że pola danych, które nie powinny być zapisywalne, nie są modyfikowane danymi od użytkownika (mass assignment), a API selektywnie dobiera zwracane pola danych. Tam, gdzie dostęp do pól zależy od uprawnień użytkownika, należy to rozważać w kontekście wymagania kontroli dostępu na poziomie pól z rozdziału „Autoryzacja”.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **15.3.1** | Zweryfikuj, że aplikacja zwraca wyłącznie wymagany podzbiór pól obiektu danych. Na przykład nie powinna zwracać całego obiektu danych, ponieważ niektóre pojedyncze pola nie powinny być dostępne dla użytkowników. | 1 |
| **15.3.2** | Zweryfikuj, że tam, gdzie backend aplikacji wykonuje wywołania do zewnętrznych URL-i, jest skonfigurowany tak, aby nie podążać za przekierowaniami, chyba że jest to funkcjonalność zamierzona. | 2 |
| **15.3.3** | Zweryfikuj, że aplikacja posiada środki zaradcze chroniące przed atakami mass assignment poprzez ograniczanie dozwolonych pól dla każdego kontrolera i akcji — np. nie jest możliwe wstawienie lub aktualizacja wartości pola, które nie miało być częścią danej akcji. | 2 |
| **15.3.4** | Zweryfikuj, że wszystkie komponenty proxy i oprogramowania pośredniczącego przekazują oryginalny adres IP użytkownika poprawnie, z użyciem zaufanych pól danych niepodlegających manipulacji przez użytkownika końcowego, a aplikacja i serwer WWW używają tej poprawnej wartości do logowania zdarzeń i decyzji bezpieczeństwa, takich jak ograniczanie częstotliwości żądań — mając na uwadze, że nawet oryginalny adres IP może nie być wiarygodny ze względu na dynamiczne IP, VPN-y czy zapory korporacyjne. | 2 |
| **15.3.5** | Zweryfikuj, że aplikacja jawnie zapewnia, iż zmienne są właściwego typu, oraz wykonuje operacje ścisłej równości i porównania. Ma to na celu uniknięcie podatności type juggling lub type confusion, wynikających z założeń kodu aplikacji co do typu zmiennej. | 2 |
| **15.3.6** | Zweryfikuj, że kod JavaScript jest pisany w sposób zapobiegający prototype pollution — na przykład z użyciem Set() lub Map() zamiast literałów obiektowych. | 2 |
| **15.3.7** | Zweryfikuj, że aplikacja posiada obrony przed atakami HTTP parameter pollution, w szczególności jeśli framework aplikacji nie rozróżnia źródła parametrów żądania (ciąg zapytania, parametry treści, ciasteczka czy pola nagłówka). | 2 |

## V15.4 Bezpieczna współbieżność

Problemy współbieżności — takie jak wyścigi (race conditions), podatności time-of-check to time-of-use (TOCTOU), zakleszczenia (deadlocks), uwięzienia (livelocks), zagłodzenie wątków (thread starvation) czy niewłaściwa synchronizacja — mogą prowadzić do nieprzewidywalnego zachowania i ryzyk bezpieczeństwa. Ta sekcja zawiera różne techniki i strategie pomagające ograniczyć te ryzyka.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **15.4.1** | Zweryfikuj, że obiekty współdzielone w kodzie wielowątkowym (takie jak pamięci podręczne, pliki czy obiekty w pamięci używane przez wiele wątków) są używane w sposób bezpieczny, z zastosowaniem typów bezpiecznych wątkowo i mechanizmów synchronizacji, takich jak blokady czy semafory, aby uniknąć wyścigów i uszkodzenia danych. | 3 |
| **15.4.2** | Zweryfikuj, że sprawdzenia stanu zasobu — takie jak jego istnienie czy uprawnienia — oraz zależne od nich działania są wykonywane jako pojedyncza operacja atomowa, aby zapobiec wyścigom time-of-check to time-of-use (TOCTOU). Przykłady: sprawdzenie istnienia pliku przed jego otwarciem albo weryfikacja dostępu użytkownika przed jego przyznaniem. | 3 |
| **15.4.3** | Zweryfikuj, że blokady są używane konsekwentnie, aby wątki nie utykały — czy to czekając na siebie nawzajem, czy ponawiając próby w nieskończoność — oraz że logika blokowania pozostaje w kodzie odpowiedzialnym za zarządzanie zasobem, aby blokady nie mogły być nieumyślnie lub złośliwie modyfikowane przez zewnętrzne klasy lub kod. | 3 |
| **15.4.4** | Zweryfikuj, że polityki alokacji zasobów zapobiegają zagłodzeniu wątków poprzez zapewnienie sprawiedliwego dostępu do zasobów — na przykład z wykorzystaniem pul wątków — pozwalając wątkom o niższym priorytecie na wykonanie w rozsądnym czasie. | 3 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP Prototype Pollution Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [OWASP CycloneDX Bill of Materials Specification](https://owasp.org/www-project-cyclonedx/)
* [OWASP Web Security Testing Guide: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution)
