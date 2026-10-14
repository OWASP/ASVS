# V14 Ochrona danych

## Cel kontrolny

Aplikacje nie są w stanie przewidzieć wszystkich wzorców użycia i zachowań użytkowników, dlatego powinny wdrażać mechanizmy ograniczające nieautoryzowany dostęp do danych wrażliwych na urządzeniach klienckich.

Niniejszy rozdział zawiera wymagania związane z określeniem, jakie dane wymagają ochrony, jak należy je chronić, oraz konkretne mechanizmy do wdrożenia lub pułapki, których należy unikać.

Kolejną kwestią ochrony danych jest masowa ekstrakcja, modyfikacja lub nadmierne użycie. Wymagania każdego systemu będą zapewne bardzo różne, dlatego ustalenie, co jest „nienormalne”, musi uwzględniać model zagrożeń i ryzyko biznesowe. Z perspektywy ASVS wykrywanie tych problemów jest omawiane w rozdziale „Logowanie zdarzeń bezpieczeństwa i obsługa błędów”, a ustalanie limitów — w rozdziale „Walidacja i logika biznesowa”.

## V14.1 Dokumentacja ochrony danych

Kluczowym warunkiem wstępnym zdolności do ochrony danych jest skategoryzowanie, które dane należy uznać za wrażliwe. Prawdopodobnie wystąpi kilka różnych poziomów wrażliwości, a dla każdego z nich mechanizmy wymagane do ochrony danych będą inne.

Istnieją różne regulacje i przepisy dotyczące prywatności, które wpływają na to, jak aplikacje muszą podchodzić do przechowywania, wykorzystywania i przesyłania wrażliwych danych osobowych. Ta sekcja nie próbuje już powielać tego typu przepisów o ochronie danych czy prywatności, lecz koncentruje się na kluczowych kwestiach technicznych ochrony danych wrażliwych. Należy zapoznać się z lokalnymi przepisami i regulacjami oraz — w razie potrzeby — skonsultować się z wykwalifikowanym specjalistą ds. prywatności lub prawnikiem.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **14.1.1** | Zweryfikuj, że wszystkie dane wrażliwe tworzone i przetwarzane przez aplikację zostały zidentyfikowane i sklasyfikowane według poziomów ochrony. Obejmuje to dane, które są jedynie zakodowane i przez to łatwe do zdekodowania, takie jak ciągi Base64 lub jawny ładunek wewnątrz JWT. Poziomy ochrony muszą uwzględniać wszelkie regulacje i standardy ochrony danych i prywatności, z którymi aplikacja musi być zgodna. | 2 |
| **14.1.2** | Zweryfikuj, że wszystkie poziomy ochrony danych wrażliwych mają udokumentowany zestaw wymagań ochronnych. Musi on obejmować (między innymi) wymagania dotyczące ogólnego szyfrowania, weryfikacji integralności, retencji, sposobu logowania danych, kontroli dostępu do danych wrażliwych w logach, szyfrowania na poziomie bazy danych, prywatności i stosowanych technologii wzmacniających prywatność oraz inne wymagania poufności. | 2 |

## V14.2 Ogólna ochrona danych

Ta sekcja zawiera różnorodne praktyczne wymagania związane z ochroną danych. Większość dotyczy konkretnych problemów, takich jak niezamierzony wyciek danych, ale znajduje się tu również ogólne wymaganie wdrożenia mechanizmów ochronnych stosownie do poziomu ochrony wymaganego dla każdego elementu danych.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **14.2.1** | Zweryfikuj, że dane wrażliwe są wysyłane do serwera wyłącznie w treści komunikatu HTTP lub polach nagłówka, a URL i ciąg zapytania nie zawierają informacji wrażliwych, takich jak klucz API czy token sesji. | 1 |
| **14.2.2** | Zweryfikuj, że aplikacja zapobiega buforowaniu danych wrażliwych w komponentach serwerowych, takich jak moduły równoważenia obciążenia i pamięci podręczne aplikacji, albo zapewnia, że dane są bezpiecznie usuwane po użyciu. | 2 |
| **14.2.3** | Zweryfikuj, że zdefiniowane dane wrażliwe nie są wysyłane do stron niezaufanych (np. trackerów użytkowników), aby zapobiec niepożądanemu gromadzeniu danych poza kontrolą aplikacji. | 2 |
| **14.2.4** | Zweryfikuj, że mechanizmy dotyczące danych wrażliwych — związane z szyfrowaniem, weryfikacją integralności, retencją, sposobem logowania danych, kontrolą dostępu do danych wrażliwych w logach, prywatnością i technologiami wzmacniającymi prywatność — są wdrożone zgodnie z dokumentacją dla poziomu ochrony konkretnych danych. | 2 |
| **14.2.5** | Zweryfikuj, że mechanizmy buforowania są skonfigurowane tak, aby buforować wyłącznie odpowiedzi o oczekiwanym typie treści dla danego zasobu, niezawierające wrażliwej, dynamicznej treści. Serwer WWW powinien zwracać odpowiedź 404 lub 302 przy dostępie do nieistniejącego pliku, zamiast zwracać inny, istniejący plik. Powinno to zapobiegać atakom Web Cache Deception. | 3 |
| **14.2.6** | Zweryfikuj, że aplikacja zwraca wyłącznie minimalny zakres danych wrażliwych wymagany dla jej funkcjonalności — na przykład zwraca tylko część cyfr numeru karty płatniczej, a nie pełny numer. Jeśli kompletne dane są wymagane, powinny być maskowane w interfejsie użytkownika, chyba że użytkownik celowo je wyświetli. | 3 |
| **14.2.7** | Zweryfikuj, że informacje wrażliwe podlegają klasyfikacji retencji danych, zapewniającej automatyczne usuwanie danych przestarzałych lub zbędnych — według zdefiniowanego harmonogramu albo stosownie do sytuacji. | 3 |
| **14.2.8** | Zweryfikuj, że informacje wrażliwe są usuwane z metadanych plików przesyłanych przez użytkowników, chyba że użytkownik wyraził zgodę na ich przechowywanie. | 3 |

## V14.3 Ochrona danych po stronie klienta

Ta sekcja zawiera wymagania zapobiegające wyciekom danych w określony sposób po stronie klienta lub agenta użytkownika aplikacji.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **14.3.1** | Zweryfikuj, że uwierzytelnione dane są czyszczone z pamięci klienta, takiej jak DOM przeglądarki, po zakończeniu działania klienta lub sesji. Pomocne może być pole nagłówka odpowiedzi HTTP 'Clear-Site-Data', ale strona kliencka powinna również potrafić samodzielnie wyczyścić dane, jeśli połączenie z serwerem jest niedostępne w chwili kończenia sesji. | 1 |
| **14.3.2** | Zweryfikuj, że aplikacja ustawia wystarczające pola nagłówka odpowiedzi HTTP zapobiegające buforowaniu (tj. Cache-Control: no-store), aby dane wrażliwe nie były buforowane w przeglądarkach. | 2 |
| **14.3.3** | Zweryfikuj, że dane przechowywane w pamięci przeglądarki (takiej jak localStorage, sessionStorage, IndexedDB czy ciasteczka) nie zawierają danych wrażliwych, z wyjątkiem tokenów sesji. | 2 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [Serwis Security Headers do sprawdzania pól nagłówków bezpieczeństwa i anti-caching](https://securityheaders.com/)
* [Dokumentacja Mozilli o nagłówkach anti-caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [Australian Privacy Principle 11 - Security of personal information](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-11-app-11-security-of-personal-information)
* [Przegląd unijnego ogólnego rozporządzenia o ochronie danych (RODO)](https://www.edps.europa.eu/data-protection_en)
* [Europejski Inspektor Ochrony Danych — Internet Privacy Engineering Network](https://www.edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
* [Informacje o nagłówku „Clear-Site-Data”](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data)
* [White paper o Web Cache Deception](https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack-wp.pdf)
