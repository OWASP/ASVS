# V7 Zarządzanie sesją

## Cel kontrolny

Mechanizmy zarządzania sesją pozwalają aplikacjom korelować interakcje użytkowników i urządzeń w czasie, nawet przy korzystaniu z bezstanowych protokołów komunikacyjnych (takich jak HTTP). Nowoczesne aplikacje mogą używać wielu tokenów sesji o odmiennych cechach i przeznaczeniu. Bezpieczny system zarządzania sesją to taki, który uniemożliwia atakującym pozyskanie, wykorzystanie lub inne nadużycie sesji ofiary. Aplikacje utrzymujące sesje muszą zapewnić spełnienie następujących wysokopoziomowych wymagań zarządzania sesją:

* Sesje są unikalne dla każdej osoby i nie mogą być odgadnięte ani współdzielone.
* Sesje są unieważniane, gdy nie są już potrzebne, oraz wygasają po okresach bezczynności.

Wiele wymagań tego rozdziału odnosi się do wybranych mechanizmów [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/), koncentrując się na powszechnych zagrożeniach i często wykorzystywanych lukach w uwierzytelnianiu.

Warto zauważyć, że wymagania dotyczące konkretnych szczegółów implementacyjnych niektórych mechanizmów zarządzania sesją znajdują się w innych miejscach:

* Ciasteczka HTTP to powszechny mechanizm zabezpieczania tokenów sesji. Szczegółowe wymagania bezpieczeństwa dla ciasteczek znajdują się w rozdziale „Bezpieczeństwo frontendu webowego”.
* Tokeny samowystarczalne są często używane jako sposób utrzymywania sesji. Szczegółowe wymagania bezpieczeństwa znajdują się w rozdziale „Tokeny samowystarczalne”.

## V7.1 Dokumentacja zarządzania sesją

Nie istnieje jeden wzorzec pasujący do wszystkich aplikacji. Nie jest zatem możliwe zdefiniowanie uniwersalnych granic i limitów odpowiednich dla wszystkich przypadków. Warunkiem wstępnym implementacji i testowania musi być analiza ryzyka wraz z udokumentowanymi decyzjami bezpieczeństwa dotyczącymi obsługi sesji. Zapewnia to dopasowanie systemu zarządzania sesją do konkretnych wymagań aplikacji.

Niezależnie od tego, czy wybrano mechanizm sesji stanowy, czy „bezstanowy”, analiza musi być kompletna i udokumentowana, aby wykazać, że wybrane rozwiązanie jest w stanie spełnić wszystkie istotne wymagania bezpieczeństwa. Należy również uwzględnić interakcję z ewentualnie używanymi mechanizmami jednokrotnego logowania (SSO).

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **7.1.1** | Zweryfikuj, że limit czasu bezczynności sesji użytkownika oraz bezwzględny maksymalny czas życia sesji są udokumentowane, odpowiednie w połączeniu z innymi mechanizmami, a dokumentacja zawiera uzasadnienie wszelkich odstępstw od wymagań ponownego uwierzytelniania NIST SP 800-63B. | 2 |
| **7.1.2** | Zweryfikuj, że dokumentacja definiuje, ile równoczesnych (równoległych) sesji jest dozwolonych dla jednego konta, a także zamierzone zachowania i działania podejmowane po osiągnięciu maksymalnej liczby aktywnych sesji. | 2 |
| **7.1.3** | Zweryfikuj, że wszystkie systemy tworzące i zarządzające sesjami użytkowników w ramach ekosystemu federacyjnego zarządzania tożsamością (takie jak systemy SSO) są udokumentowane wraz z mechanizmami koordynacji czasów życia sesji, ich kończenia oraz wszelkich innych warunków wymagających ponownego uwierzytelnienia. | 2 |

## V7.2 Podstawowe bezpieczeństwo zarządzania sesją

Ta sekcja realizuje zasadnicze wymagania bezpiecznych sesji poprzez weryfikację, że tokeny sesji są bezpiecznie generowane i walidowane.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **7.2.1** | Zweryfikuj, że aplikacja wykonuje całą weryfikację tokenów sesji z użyciem zaufanej usługi backendowej. | 1 |
| **7.2.2** | Zweryfikuj, że aplikacja używa do zarządzania sesją tokenów samowystarczalnych albo referencyjnych, generowanych dynamicznie — tj. nie używa statycznych sekretów i kluczy API. | 1 |
| **7.2.3** | Zweryfikuj, że jeśli do reprezentowania sesji użytkowników używane są tokeny referencyjne, są one unikalne, generowane przy użyciu kryptograficznie bezpiecznego generatora liczb pseudolosowych (CSPRNG) i mają entropię co najmniej 128 bitów. | 1 |
| **7.2.4** | Zweryfikuj, że aplikacja generuje nowy token sesji przy uwierzytelnieniu użytkownika, w tym przy ponownym uwierzytelnieniu, oraz unieważnia dotychczasowy token sesji. | 1 |

## V7.3 Wygasanie sesji

Mechanizmy wygasania sesji służą minimalizacji okna czasowego dla przejęcia sesji i innych form jej nadużycia. Limity czasowe muszą odpowiadać udokumentowanym decyzjom bezpieczeństwa.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **7.3.1** | Zweryfikuj, że istnieje limit czasu bezczynności, po którym wymuszane jest ponowne uwierzytelnienie, zgodnie z analizą ryzyka i udokumentowanymi decyzjami bezpieczeństwa. | 2 |
| **7.3.2** | Zweryfikuj, że istnieje bezwzględny maksymalny czas życia sesji, po którym wymuszane jest ponowne uwierzytelnienie, zgodnie z analizą ryzyka i udokumentowanymi decyzjami bezpieczeństwa. | 2 |

## V7.4 Kończenie sesji

Kończenie sesji może być obsługiwane przez samą aplikację albo przez dostawcę SSO, jeśli to on zarządza sesją zamiast aplikacji. Rozważając wymagania tej sekcji, może być konieczne rozstrzygnięcie, czy dostawca SSO znajduje się w zakresie weryfikacji, ponieważ część z nich może być kontrolowana przez dostawcę.

Zakończenie sesji powinno skutkować koniecznością ponownego uwierzytelnienia i być skuteczne w całej aplikacji, logowaniu federacyjnym (jeśli występuje) oraz u wszystkich stron ufających.

Dla stanowych mechanizmów sesji zakończenie zwykle polega na unieważnieniu sesji w backendzie. W przypadku tokenów samowystarczalnych wymagane są dodatkowe środki unieważnienia lub zablokowania tych tokenów — w przeciwnym razie mogą one pozostać ważne aż do wygaśnięcia.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **7.4.1** | Zweryfikuj, że po wyzwoleniu zakończenia sesji (np. wylogowanie lub wygaśnięcie) aplikacja uniemożliwia dalsze korzystanie z sesji. Dla tokenów referencyjnych lub sesji stanowych oznacza to unieważnienie danych sesji w backendzie aplikacji. Aplikacje używające tokenów samowystarczalnych będą potrzebowały rozwiązania takiego jak utrzymywanie listy zakończonych tokenów, odrzucanie tokenów wystawionych przed określoną dla każdego użytkownika datą i godziną lub rotacja klucza podpisującego dla każdego użytkownika. | 1 |
| **7.4.2** | Zweryfikuj, że aplikacja kończy wszystkie aktywne sesje, gdy konto użytkownika zostaje wyłączone lub usunięte (np. gdy pracownik odchodzi z firmy). | 1 |
| **7.4.3** | Zweryfikuj, że aplikacja daje możliwość zakończenia wszystkich pozostałych aktywnych sesji po udanej zmianie lub usunięciu dowolnego czynnika uwierzytelniania (w tym zmianie hasła poprzez reset lub odzyskiwanie oraz — jeśli występuje — zmianie ustawień MFA). | 2 |
| **7.4.4** | Zweryfikuj, że wszystkie strony wymagające uwierzytelnienia mają łatwy i widoczny dostęp do funkcji wylogowania. | 2 |
| **7.4.5** | Zweryfikuj, że administratorzy aplikacji mają możliwość kończenia aktywnych sesji pojedynczego użytkownika lub wszystkich użytkowników. | 2 |

## V7.5 Obrona przed nadużyciem sesji

Ta sekcja zawiera wymagania ograniczające ryzyko stwarzane przez aktywne sesje, które zostały przejęte lub są nadużywane poprzez wektory bazujące na istnieniu i możliwościach aktywnych sesji użytkowników. Przykładem jest wykorzystanie wykonania złośliwej treści do zmuszenia uwierzytelnionej przeglądarki ofiary do wykonania akcji z użyciem jej sesji.

Rozważając wymagania tej sekcji, należy wziąć pod uwagę wytyczne dla poszczególnych poziomów z rozdziału „Uwierzytelnianie”.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **7.5.1** | Zweryfikuj, że aplikacja wymaga pełnego ponownego uwierzytelnienia przed zezwoleniem na modyfikację wrażliwych atrybutów konta, które mogą wpływać na uwierzytelnianie — takich jak adres e-mail, numer telefonu, konfiguracja MFA lub inne informacje używane przy odzyskiwaniu konta. | 2 |
| **7.5.2** | Zweryfikuj, że użytkownicy mogą przeglądać i (po ponownym uwierzytelnieniu co najmniej jednym czynnikiem) kończyć dowolne lub wszystkie aktualnie aktywne sesje. | 2 |
| **7.5.3** | Zweryfikuj, że aplikacja wymaga dodatkowego uwierzytelnienia co najmniej jednym czynnikiem lub weryfikacji wtórnej przed wykonaniem wysoce wrażliwych transakcji lub operacji. | 3 |

## V7.6 Ponowne uwierzytelnianie federacyjne

Ta sekcja dotyczy osób tworzących kod strony ufającej (Relying Party, RP) lub dostawcy tożsamości (IdP). Wymagania te wywodzą się z [NIST SP 800-63C](https://pages.nist.gov/800-63-4/sp800-63c.html) dotyczącego federacji i asercji.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **7.6.1** | Zweryfikuj, że czas życia i kończenie sesji między stronami ufającymi (RP) a dostawcami tożsamości (IdP) zachowują się zgodnie z dokumentacją, wymagając ponownego uwierzytelnienia w razie potrzeby — na przykład po osiągnięciu maksymalnego czasu między zdarzeniami uwierzytelnienia w IdP. | 2 |
| **7.6.2** | Zweryfikuj, że utworzenie sesji wymaga zgody użytkownika albo jego jawnego działania, uniemożliwiając tworzenie nowych sesji aplikacji bez interakcji użytkownika. | 2 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP Web Security Testing Guide: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/06-Session_Management_Testing)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
