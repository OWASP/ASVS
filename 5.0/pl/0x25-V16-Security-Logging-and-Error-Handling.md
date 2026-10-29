# V16 Logowanie zdarzeń bezpieczeństwa i obsługa błędów

## Cel kontrolny

Logi bezpieczeństwa różnią się od logów błędów czy wydajności — służą do rejestrowania zdarzeń istotnych z punktu widzenia bezpieczeństwa, takich jak decyzje uwierzytelniania, decyzje kontroli dostępu oraz próby obejścia mechanizmów bezpieczeństwa, na przykład walidacji danych wejściowych czy walidacji logiki biznesowej. Ich celem jest wspieranie wykrywania, reagowania i dochodzeń poprzez dostarczanie ustrukturyzowanych danych o wysokiej wartości sygnałowej dla narzędzi analitycznych, takich jak systemy SIEM.

Logi nie powinny zawierać wrażliwych danych osobowych, chyba że wymaga tego prawo, a wszelkie logowane dane muszą być chronione jako zasób o wysokiej wartości. Logowanie nie może naruszać prywatności ani bezpieczeństwa systemu. Aplikacje muszą również zawodzić w sposób bezpieczny, unikając zbędnego ujawniania informacji lub zakłóceń.

Szczegółowe wskazówki implementacyjne znajdują się w ściągach OWASP wymienionych w sekcji źródeł.

## V16.1 Dokumentacja logowania zdarzeń bezpieczeństwa

Ta sekcja zapewnia jasny i kompletny inwentarz logowania w całym stosie technologicznym aplikacji. Jest to niezbędne dla skutecznego monitorowania bezpieczeństwa, reagowania na incydenty i zgodności.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **16.1.1** | Zweryfikuj, że istnieje inwentarz dokumentujący logowanie wykonywane na każdej warstwie stosu technologicznego aplikacji: jakie zdarzenia są logowane, formaty logów, gdzie logi są przechowywane, jak są wykorzystywane, jak kontrolowany jest do nich dostęp oraz jak długo są przechowywane. | 2 |

## V16.2 Ogólne logowanie

Ta sekcja zawiera wymagania zapewniające, że logi bezpieczeństwa mają spójną strukturę i zawierają oczekiwane metadane. Celem jest uczynienie logów odczytywalnymi maszynowo i możliwymi do analizy w systemach rozproszonych i różnych narzędziach.

Zdarzenia bezpieczeństwa w naturalny sposób często dotyczą danych wrażliwych. Jeśli takie dane są logowane bezrefleksyjnie, same logi stają się danymi klasyfikowanymi — a więc podlegają wymaganiom szyfrowania, ostrzejszym politykom retencji i potencjalnemu ujawnieniu podczas audytów.

Dlatego krytyczne jest logowanie wyłącznie tego, co niezbędne, oraz traktowanie danych z logów z taką samą starannością, jak innych zasobów wrażliwych.

Poniższe wymagania ustanawiają fundamenty dotyczące metadanych logowania, synchronizacji, formatu i kontroli.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **16.2.1** | Zweryfikuj, że każdy wpis logu zawiera niezbędne metadane (takie jak: kiedy, gdzie, kto, co), które pozwoliłyby na szczegółowe odtworzenie osi czasu w razie wystąpienia zdarzenia. | 2 |
| **16.2.2** | Zweryfikuj, że źródła czasu wszystkich komponentów logujących są zsynchronizowane oraz że znaczniki czasu w metadanych zdarzeń bezpieczeństwa używają UTC lub zawierają jawne przesunięcie strefy czasowej. UTC jest zalecane dla zapewnienia spójności w systemach rozproszonych i uniknięcia niejasności przy zmianach czasu letniego. | 2 |
| **16.2.3** | Zweryfikuj, że aplikacja zapisuje lub rozsyła logi wyłącznie do plików i usług udokumentowanych w inwentarzu logów. | 2 |
| **16.2.4** | Zweryfikuj, że logi mogą być odczytywane i korelowane przez używany procesor logów, najlepiej z zastosowaniem powszechnego formatu logowania. | 2 |
| **16.2.5** | Zweryfikuj, że przy logowaniu danych wrażliwych aplikacja egzekwuje logowanie zgodne z poziomem ochrony danych. Na przykład logowanie pewnych danych — takich jak poświadczenia czy dane płatnicze — może być niedozwolone. Inne dane, takie jak tokeny sesji, mogą być logowane wyłącznie w postaci zahaszowanej lub zamaskowanej, w całości lub częściowo. | 2 |

## V16.3 Zdarzenia bezpieczeństwa

Ta sekcja definiuje wymagania logowania zdarzeń istotnych dla bezpieczeństwa w aplikacji. Rejestrowanie tych zdarzeń jest krytyczne dla wykrywania podejrzanych zachowań, wspierania dochodzeń i wypełniania obowiązków zgodności.

Sekcja przedstawia typy zdarzeń, które powinny być logowane, ale nie próbuje podawać wyczerpujących szczegółów. Każda aplikacja ma unikalne czynniki ryzyka i kontekst operacyjny.

Zwróć uwagę, że choć ASVS obejmuje logowanie zdarzeń bezpieczeństwa, alarmowanie i korelacja (np. reguły SIEM czy infrastruktura monitorowania) pozostają poza zakresem i są obsługiwane przez systemy operacyjne i monitorujące.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **16.3.1** | Zweryfikuj, że wszystkie operacje uwierzytelniania są logowane, łącznie z próbami udanymi i nieudanymi. Powinny być również zbierane dodatkowe metadane, takie jak typ uwierzytelniania czy użyte czynniki. | 2 |
| **16.3.2** | Zweryfikuj, że nieudane próby autoryzacji są logowane. Dla L3 musi to obejmować logowanie wszystkich decyzji autoryzacyjnych, w tym logowanie dostępu do danych wrażliwych (bez logowania samych danych wrażliwych). | 2 |
| **16.3.3** | Zweryfikuj, że aplikacja loguje zdarzenia bezpieczeństwa zdefiniowane w dokumentacji, a także loguje próby obejścia mechanizmów bezpieczeństwa, takich jak walidacja danych wejściowych, logika biznesowa i ochrona przed automatyzacją. | 2 |
| **16.3.4** | Zweryfikuj, że aplikacja loguje nieoczekiwane błędy i awarie mechanizmów bezpieczeństwa, takie jak błędy TLS w backendzie. | 2 |

## V16.4 Ochrona logów

Logi to cenne artefakty śledcze i muszą być chronione. Jeśli logi można łatwo zmodyfikować lub usunąć, tracą integralność i stają się niewiarygodne w dochodzeniach po incydentach czy postępowaniach prawnych. Logi mogą ujawniać wewnętrzne zachowanie aplikacji lub wrażliwe metadane, co czyni je atrakcyjnym celem dla atakujących.

Ta sekcja definiuje wymagania zapewniające ochronę logów przed nieautoryzowanym dostępem, manipulacją i ujawnieniem oraz ich bezpieczne przesyłanie i przechowywanie w bezpiecznych, odizolowanych systemach.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **16.4.1** | Zweryfikuj, że wszystkie komponenty logujące odpowiednio kodują dane, aby zapobiec wstrzyknięciu do logów (log injection). | 2 |
| **16.4.2** | Zweryfikuj, że logi są chronione przed nieautoryzowanym dostępem i nie mogą być modyfikowane. | 2 |
| **16.4.3** | Zweryfikuj, że logi są bezpiecznie przesyłane do logicznie odseparowanego systemu do analizy, wykrywania, alarmowania i eskalacji. Celem jest zapewnienie, że w razie włamania do aplikacji logi nie zostaną skompromitowane. | 2 |

## V16.5 Obsługa błędów

Ta sekcja definiuje wymagania zapewniające, że aplikacje zawodzą w sposób kontrolowany i bezpieczny, bez ujawniania wrażliwych szczegółów wewnętrznych.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **16.5.1** | Zweryfikuj, że po wystąpieniu nieoczekiwanego lub wrażliwego z punktu widzenia bezpieczeństwa błędu konsumentowi zwracany jest komunikat ogólny, gwarantujący brak ekspozycji wrażliwych wewnętrznych danych systemowych, takich jak ślady stosu, zapytania, klucze tajne i tokeny. | 2 |
| **16.5.2** | Zweryfikuj, że aplikacja kontynuuje bezpieczne działanie, gdy dostęp do zasobu zewnętrznego zawiedzie — na przykład stosując wzorce takie jak circuit breaker czy kontrolowana degradacja (graceful degradation). | 2 |
| **16.5.3** | Zweryfikuj, że aplikacja zawodzi w sposób kontrolowany i bezpieczny, również przy wystąpieniu wyjątku, zapobiegając stanom fail-open, takim jak przetworzenie transakcji pomimo błędów logiki walidacji. | 2 |
| **16.5.4** | Zweryfikuj, że zdefiniowana jest procedura obsługi błędów „ostatniej szansy”, przechwytująca wszystkie nieobsłużone wyjątki. Ma to zarówno zapobiec utracie szczegółów błędów, które muszą trafić do plików logów, jak i zapewnić, że błąd nie wyłączy całego procesu aplikacji, prowadząc do utraty dostępności. | 3 |

Uwaga: niektóre języki (w tym Swift, Go oraz — poprzez powszechną praktykę projektową — wiele języków funkcyjnych) nie wspierają wyjątków ani procedur obsługi „ostatniej szansy”. W takim przypadku architekci i programiści powinni użyć wzorca właściwego dla danego języka lub frameworka, aby zapewnić, że aplikacje potrafią bezpiecznie obsługiwać zdarzenia wyjątkowe, nieoczekiwane lub związane z bezpieczeństwem.

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP Web Security Testing Guide: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README)
* [Sekcja OWASP Authentication Cheat Sheet o komunikatach błędów](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
* [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
* [OWASP Application Logging Vocabulary Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html)
