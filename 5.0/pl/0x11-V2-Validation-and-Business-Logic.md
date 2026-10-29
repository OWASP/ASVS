# V2 Walidacja i logika biznesowa

## Cel kontrolny

Celem tego rozdziału jest zapewnienie, że weryfikowana aplikacja spełnia następujące cele wysokopoziomowe:

* Dane wejściowe otrzymywane przez aplikację odpowiadają oczekiwaniom biznesowym lub funkcjonalnym.
* Przepływ logiki biznesowej jest sekwencyjny, przetwarzany w kolejności i nie może zostać ominięty.
* Logika biznesowa zawiera limity i mechanizmy pozwalające wykrywać zautomatyzowane ataki i im zapobiegać — takie jak ciągłe drobne przelewy środków czy dodawanie miliona znajomych pojedynczo.
* Przepływy logiki biznesowej o wysokiej wartości uwzględniają przypadki nadużyć i złośliwych aktorów oraz posiadają zabezpieczenia przed atakami podszywania się (spoofing), manipulacji (tampering), ujawnienia informacji oraz eskalacji uprawnień.

## V2.1 Dokumentacja walidacji i logiki biznesowej

Dokumentacja walidacji i logiki biznesowej powinna jasno definiować limity logiki biznesowej, reguły walidacji oraz kontekstową spójność powiązanych danych, tak aby było jasne, co należy zaimplementować w aplikacji.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **2.1.1** | Zweryfikuj, że dokumentacja aplikacji definiuje reguły walidacji danych wejściowych określające, jak sprawdzać poprawność danych względem oczekiwanej struktury. Mogą to być powszechne formaty danych, takie jak numery kart płatniczych, adresy e-mail, numery telefonów, lub wewnętrzny format danych. | 1 |
| **2.1.2** | Zweryfikuj, że dokumentacja aplikacji definiuje sposób walidacji logicznej i kontekstowej spójności powiązanych danych — na przykład sprawdzenie, czy dzielnica i kod pocztowy do siebie pasują. | 2 |
| **2.1.3** | Zweryfikuj, że oczekiwania dotyczące limitów i walidacji logiki biznesowej są udokumentowane, zarówno dla poszczególnych użytkowników, jak i globalnie dla całej aplikacji. | 2 |

## V2.2 Walidacja danych wejściowych

Skuteczne mechanizmy walidacji danych wejściowych wymuszają oczekiwania biznesowe lub funkcjonalne wobec typu danych, które aplikacja spodziewa się otrzymać. Zapewnia to dobrą jakość danych i zmniejsza powierzchnię ataku. Nie eliminuje jednak ani nie zastępuje konieczności stosowania poprawnego kodowania, parametryzacji lub sanityzacji przy użyciu danych w innym komponencie lub przy prezentowaniu ich na wyjściu.

W tym kontekście „dane wejściowe” mogą pochodzić z bardzo różnych źródeł, w tym z pól formularzy HTML, żądań REST, parametrów URL, pól nagłówków HTTP, ciasteczek, plików na dysku, baz danych i zewnętrznych API.

Mechanizm logiki biznesowej może sprawdzać, czy dane wejściowe są liczbą mniejszą niż 100. Oczekiwanie funkcjonalne może sprawdzać, czy liczba znajduje się poniżej pewnego progu — jeśli liczba ta steruje tym, ile razy wykona się dana pętla, wysoka wartość mogłaby prowadzić do nadmiernego przetwarzania i potencjalnej odmowy usługi.

Choć walidacja schematem nie jest jawnie wymagana, może być najskuteczniejszym mechanizmem pełnego pokrycia walidacją API HTTP lub innych interfejsów używających JSON lub XML.

Należy zwrócić uwagę na następujące kwestie dotyczące walidacji schematem:

* „Opublikowana wersja” specyfikacji walidacji JSON Schema jest uznawana za gotową do użytku produkcyjnego, ale nie jest, ściśle rzecz biorąc, „stabilna”. Korzystając z walidacji JSON Schema, należy upewnić się, że nie ma rozbieżności ze wskazówkami zawartymi w poniższych wymaganiach.
* Używane biblioteki walidacji JSON Schema powinny być monitorowane i w razie potrzeby aktualizowane po sformalizowaniu standardu.
* Nie należy używać walidacji DTD, a przetwarzanie DTD we frameworkach powinno zostać wyłączone, aby uniknąć problemów z atakami XXE wymierzonymi w DTD.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **2.2.1** | Zweryfikuj, że dane wejściowe są walidowane w celu wymuszenia oczekiwań biznesowych lub funkcjonalnych wobec tych danych. Walidacja powinna opierać się na podejściu pozytywnym — z użyciem listy dozwolonych wartości, wzorców i zakresów — albo na porównaniu danych wejściowych z oczekiwaną strukturą i limitami logicznymi według wcześniej zdefiniowanych reguł. Dla L1 można skupić się na danych wejściowych używanych do podejmowania konkretnych decyzji biznesowych lub dotyczących bezpieczeństwa. Dla L2 i wyżej powinno to obejmować wszystkie dane wejściowe. | 1 |
| **2.2.2** | Zweryfikuj, że aplikacja została zaprojektowana tak, aby wymuszać walidację danych wejściowych na poziomie zaufanej warstwy usługowej. Walidacja po stronie klienta poprawia użyteczność i należy do niej zachęcać, ale nie wolno na niej polegać jako na mechanizmie bezpieczeństwa. | 1 |
| **2.2.3** | Zweryfikuj, że aplikacja zapewnia, iż kombinacje powiązanych danych są sensowne według wcześniej zdefiniowanych reguł. | 2 |

## V2.3 Bezpieczeństwo logiki biznesowej

Ta sekcja obejmuje kluczowe wymagania zapewniające, że aplikacja egzekwuje procesy logiki biznesowej we właściwy sposób i nie jest podatna na ataki wykorzystujące logikę i przepływ aplikacji.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **2.3.1** | Zweryfikuj, że aplikacja przetwarza przepływy logiki biznesowej dla tego samego użytkownika wyłącznie w oczekiwanej, sekwencyjnej kolejności kroków, bez ich pomijania. | 1 |
| **2.3.2** | Zweryfikuj, że limity logiki biznesowej są zaimplementowane zgodnie z dokumentacją aplikacji, aby zapobiec wykorzystaniu błędów logiki biznesowej. | 2 |
| **2.3.3** | Zweryfikuj, że na poziomie logiki biznesowej stosowane są transakcje — tak aby operacja logiki biznesowej albo powiodła się w całości, albo została wycofana do poprzedniego poprawnego stanu. | 2 |
| **2.3.4** | Zweryfikuj, że na poziomie logiki biznesowej stosowane są mechanizmy blokad zapewniające, że zasoby o ograniczonej liczbie (takie jak miejsca w teatrze czy okna dostawy) nie mogą zostać zarezerwowane podwójnie poprzez manipulację logiką aplikacji. | 2 |
| **2.3.5** | Zweryfikuj, że przepływy logiki biznesowej o wysokiej wartości wymagają zatwierdzenia przez wielu użytkowników, aby zapobiec nieautoryzowanym lub przypadkowym działaniom. Może to obejmować między innymi duże przelewy pieniężne, zatwierdzanie umów, dostęp do informacji niejawnych lub nadpisywanie zabezpieczeń w procesach produkcyjnych. | 3 |

## V2.4 Ochrona przed automatyzacją

Ta sekcja obejmuje mechanizmy ochrony przed automatyzacją, zapewniające wymuszanie interakcji o charakterze ludzkim i zapobieganie nadmiernym żądaniom zautomatyzowanym.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **2.4.1** | Zweryfikuj, że wdrożono mechanizmy ochrony przed automatyzacją, chroniące przed nadmiernymi wywołaniami funkcji aplikacji, które mogłyby prowadzić do eksfiltracji danych, tworzenia danych-śmieci, wyczerpania przydziałów, przekroczenia limitów częstotliwości, odmowy usługi lub nadużywania kosztownych zasobów. | 2 |
| **2.4.2** | Zweryfikuj, że przepływy logiki biznesowej wymagają realistycznego, ludzkiego tempa działania, uniemożliwiając nadmiernie szybkie przesyłanie transakcji. | 3 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP Web Security Testing Guide: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Web Security Testing Guide: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README)
* Ochronę przed automatyzacją można osiągnąć na wiele sposobów, w tym z wykorzystaniem projektu [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [JSON Schema](https://json-schema.org/specification.html)
