# Załącznik D: Zalecenia

## Wprowadzenie

Podczas przygotowywania wersji 5.0 Application Security Verification Standard (ASVS) stało się jasne, że istnieje szereg pozycji — zarówno istniejących, jak i nowo zaproponowanych — które nie powinny zostać włączone do wersji 5.0 jako wymagania. Wynikało to z faktu, że nie mieściły się w zakresie ASVS zgodnie z definicją przyjętą dla wersji 5.0, albo z przekonania, że choć stanowią dobry pomysł, nie mogą być obowiązkowe.

Nie chcąc całkowicie utracić tych pozycji, część z nich zebrano w niniejszym załączniku.

## Zalecane mechanizmy w zakresie standardu

Następujące pozycje mieszczą się w zakresie ASVS. Nie powinny być obowiązkowe, ale zdecydowanie zaleca się rozważenie ich jako elementu bezpiecznej aplikacji.

* Powinien być udostępniony miernik siły hasła, pomagający użytkownikom ustawić silniejsze hasło.
* Utwórz publicznie dostępny plik security.txt w katalogu głównym lub .well-known aplikacji, jasno wskazujący link lub adres e-mail do kontaktu z właścicielami w sprawach bezpieczeństwa.
* Walidacja danych wejściowych po stronie klienta powinna być wymuszana obok walidacji w zaufanej warstwie usługowej, ponieważ stwarza to dobrą okazję do wykrycia, że ktoś ominął mechanizmy po stronie klienta, próbując zaatakować aplikację.
* Zapobiegaj pojawianiu się przypadkowo dostępnych i wrażliwych stron w wyszukiwarkach, używając pliku robots.txt, pola nagłówka odpowiedzi X-Robots-Tag lub znacznika meta robots w HTML.
* Przy korzystaniu z GraphQL implementuj logikę autoryzacji w warstwie logiki biznesowej zamiast w warstwie GraphQL lub resolverów, aby uniknąć konieczności obsługi autoryzacji w każdym osobnym interfejsie.

Źródła:

* [Więcej informacji o security.txt wraz z linkiem do RFC](https://securitytxt.org/)

## Zasady bezpieczeństwa oprogramowania

Następujące pozycje znajdowały się wcześniej w ASVS, ale nie są tak naprawdę wymaganiami. Są to raczej zasady, które warto brać pod uwagę przy implementacji mechanizmów bezpieczeństwa — ich przestrzeganie prowadzi do solidniejszych mechanizmów. Obejmują one:

* Mechanizmy bezpieczeństwa powinny być scentralizowane, proste (ekonomia projektowania), weryfikowalnie bezpieczne i wielokrotnego użytku. Powinno to zapobiegać mechanizmom zduplikowanym, brakującym lub nieskutecznym.
* Wszędzie tam, gdzie to możliwe, używaj wcześniej napisanych i dobrze sprawdzonych implementacji mechanizmów bezpieczeństwa, zamiast polegać na implementowaniu mechanizmów od zera.
* Najlepiej, aby do dostępu do chronionych danych i zasobów używany był jeden mechanizm kontroli dostępu. Wszystkie żądania powinny przechodzić przez ten jeden mechanizm, aby uniknąć kopiuj-wklej lub niebezpiecznych ścieżek alternatywnych.
* Kontrola dostępu oparta na atrybutach lub funkcjach to zalecany wzorzec, w którym kod sprawdza uprawnienie użytkownika do funkcji lub elementu danych, a nie jedynie jego rolę. Uprawnienia nadal powinny być przydzielane z użyciem ról.

## Procesy bezpieczeństwa oprogramowania

Istnieje szereg procesów bezpieczeństwa, które zostały usunięte z ASVS 5.0, ale nadal są dobrym pomysłem. Projekt OWASP SAMM może być dobrym źródłem wiedzy o skutecznym wdrażaniu tych procesów. Pozycje wcześniej obecne w ASVS obejmują:

* Zweryfikuj stosowanie bezpiecznego cyklu wytwarzania oprogramowania, uwzględniającego bezpieczeństwo na wszystkich etapach rozwoju.
* Zweryfikuj stosowanie modelowania zagrożeń przy każdej zmianie projektowej lub planowaniu sprintu, aby identyfikować zagrożenia, planować środki zaradcze, ułatwiać właściwe reagowanie na ryzyko i ukierunkowywać testy bezpieczeństwa.
* Zweryfikuj, że wszystkie historyjki użytkownika i funkcje zawierają funkcjonalne ograniczenia bezpieczeństwa, takie jak „Jako użytkownik powinienem móc przeglądać i edytować swój profil. Nie powinienem móc przeglądać ani edytować profilu nikogo innego”.
* Zweryfikuj dostępność listy kontrolnej bezpiecznego kodowania, wymagań bezpieczeństwa, wytycznych lub polityki dla wszystkich programistów i testerów.
* Zweryfikuj, że istnieje ciągły proces zapewniający, że kod źródłowy aplikacji jest wolny od backdoorów, złośliwego kodu (np. ataki salami, bomby logiczne, bomby czasowe) oraz nieudokumentowanych lub ukrytych funkcji (np. easter eggi, niebezpieczne narzędzia debugowania). Spełnienie tej sekcji nie jest możliwe bez pełnego dostępu do kodu źródłowego, w tym bibliotek stron trzecich, dlatego jest prawdopodobnie odpowiednie wyłącznie dla aplikacji wymagających najwyższych poziomów bezpieczeństwa.
* Zweryfikuj, że istnieją mechanizmy wykrywania i reagowania na dryf konfiguracji we wdrożonych środowiskach. Może to obejmować użycie infrastruktury niezmiennej (immutable), automatyczne ponowne wdrażanie z bezpiecznej linii bazowej lub narzędzia wykrywania dryfu porównujące bieżący stan z zatwierdzonymi konfiguracjami.
* Zweryfikuj, że utwardzanie konfiguracji jest wykonywane dla wszystkich produktów, bibliotek, frameworków i usług stron trzecich zgodnie z ich indywidualnymi zaleceniami.

Źródła:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-project-threat-modeling/)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/securityengineering/sdl/)
