# V8 Autoryzacja

## Cel kontrolny

Autoryzacja zapewnia, że dostęp jest przyznawany wyłącznie uprawnionym konsumentom (użytkownikom, serwerom i innym klientom). Aby wymusić zasadę najmniejszych uprawnień (Principle of Least Privilege, POLP), weryfikowane aplikacje muszą spełniać następujące wysokopoziomowe wymagania:

* Reguły autoryzacji są udokumentowane, wraz z czynnikami decyzyjnymi i kontekstami środowiskowymi.
* Konsumenci powinni mieć dostęp wyłącznie do zasobów dozwolonych przez zdefiniowane dla nich uprawnienia.

## V8.1 Dokumentacja autoryzacji

Kompleksowa dokumentacja autoryzacji jest niezbędna, aby decyzje bezpieczeństwa były stosowane spójnie, audytowalne i zgodne z politykami organizacji. Zmniejsza to ryzyko nieautoryzowanego dostępu, czyniąc wymagania bezpieczeństwa jasnymi i wykonalnymi dla programistów, administratorów i testerów.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **8.1.1** | Zweryfikuj, że dokumentacja autoryzacji definiuje reguły ograniczania dostępu na poziomie funkcji oraz dostępu do konkretnych danych na podstawie uprawnień konsumenta i atrybutów zasobu. | 1 |
| **8.1.2** | Zweryfikuj, że dokumentacja autoryzacji definiuje reguły ograniczeń dostępu na poziomie pól (zarówno odczytu, jak i zapisu) na podstawie uprawnień konsumenta i atrybutów zasobu. Zwróć uwagę, że reguły te mogą zależeć od innych wartości atrybutów danego obiektu danych, takich jak stan lub status. | 2 |
| **8.1.3** | Zweryfikuj, że dokumentacja aplikacji definiuje atrybuty środowiskowe i kontekstowe (w tym między innymi porę dnia, lokalizację użytkownika, adres IP lub urządzenie), które są używane w aplikacji do podejmowania decyzji bezpieczeństwa, w tym dotyczących uwierzytelniania i autoryzacji. | 3 |
| **8.1.4** | Zweryfikuj, że dokumentacja uwierzytelniania i autoryzacji definiuje, w jaki sposób czynniki środowiskowe i kontekstowe są wykorzystywane w podejmowaniu decyzji, obok autoryzacji na poziomie funkcji, konkretnych danych i pól. Powinno to obejmować oceniane atrybuty, progi ryzyka oraz podejmowane działania (np. zezwól, zażądaj potwierdzenia, odmów, uwierzytelnianie stopniowe). | 3 |

## V8.2 Ogólny projekt autoryzacji

Wdrożenie granularnych mechanizmów autoryzacji na poziomie funkcji, danych i pól zapewnia, że konsumenci mogą uzyskać dostęp wyłącznie do tego, co zostało im jawnie przyznane.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **8.2.1** | Zweryfikuj, że aplikacja zapewnia ograniczenie dostępu na poziomie funkcji do konsumentów posiadających jawne uprawnienia. | 1 |
| **8.2.2** | Zweryfikuj, że aplikacja zapewnia ograniczenie dostępu do konkretnych danych do konsumentów posiadających jawne uprawnienia do konkretnych elementów danych, aby ograniczyć ryzyko insecure direct object reference (IDOR) oraz broken object level authorization (BOLA). | 1 |
| **8.2.3** | Zweryfikuj, że aplikacja zapewnia ograniczenie dostępu na poziomie pól do konsumentów posiadających jawne uprawnienia do konkretnych pól, aby ograniczyć ryzyko broken object property level authorization (BOPLA). | 2 |
| **8.2.4** | Zweryfikuj, że adaptacyjne mechanizmy bezpieczeństwa oparte na atrybutach środowiskowych i kontekstowych konsumenta (takich jak pora dnia, lokalizacja, adres IP lub urządzenie) są wdrożone dla decyzji uwierzytelniania i autoryzacji, zgodnie z dokumentacją aplikacji. Mechanizmy te muszą być stosowane zarówno gdy konsument próbuje rozpocząć nową sesję, jak i w trakcie istniejącej sesji. | 3 |

## V8.3 Autoryzacja na poziomie operacji

Natychmiastowe stosowanie zmian autoryzacji w odpowiedniej warstwie architektury aplikacji jest kluczowe dla zapobiegania nieautoryzowanym działaniom, zwłaszcza w środowiskach dynamicznych.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **8.3.1** | Zweryfikuj, że aplikacja egzekwuje reguły autoryzacji w zaufanej warstwie usługowej i nie polega na mechanizmach, którymi niezaufany konsument mógłby manipulować, takich jak JavaScript po stronie klienta. | 1 |
| **8.3.2** | Zweryfikuj, że zmiany wartości, na podstawie których podejmowane są decyzje autoryzacyjne, są stosowane natychmiast. Tam, gdzie zmian nie da się zastosować natychmiast (na przykład przy poleganiu na danych w tokenach samowystarczalnych), muszą istnieć mechanizmy kompensujące, które alarmują, gdy konsument wykonuje działanie, do którego nie jest już uprawniony, i wycofują zmianę. Zwróć uwagę, że ta alternatywa nie ograniczy wycieku informacji. | 3 |
| **8.3.3** | Zweryfikuj, że dostęp do obiektu opiera się na uprawnieniach pierwotnego podmiotu (np. konsumenta), a nie na uprawnieniach pośrednika lub usługi działającej w jego imieniu. Na przykład jeśli konsument wywołuje usługę sieciową, uwierzytelniając się tokenem samowystarczalnym, a usługa następnie żąda danych od innej usługi, druga usługa użyje do decyzji o uprawnieniach tokena konsumenta, a nie tokena maszyna–maszyna pierwszej usługi. | 3 |

## V8.4 Pozostałe kwestie autoryzacji

Dodatkowe kwestie autoryzacji — w szczególności dotyczące interfejsów administracyjnych i środowisk wielodostępnych — pomagają zapobiegać nieautoryzowanemu dostępowi.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **8.4.1** | Zweryfikuj, że aplikacje wielodostępne stosują mechanizmy separacji między najemcami, zapewniające, że operacje konsumenta nigdy nie wpłyną na najemców, z którymi nie ma on uprawnień do interakcji. | 2 |
| **8.4.2** | Zweryfikuj, że dostęp do interfejsów administracyjnych obejmuje wiele warstw bezpieczeństwa, w tym ciągłą weryfikację tożsamości konsumenta, ocenę stanu bezpieczeństwa urządzenia oraz kontekstową analizę ryzyka — zapewniając, że lokalizacja sieciowa lub zaufane endpointy nie są jedynymi czynnikami autoryzacji, nawet jeśli zmniejszają prawdopodobieństwo nieautoryzowanego dostępu. | 3 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP Web Security Testing Guide: Authorization](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/05-Authorization_Testing)
* [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
