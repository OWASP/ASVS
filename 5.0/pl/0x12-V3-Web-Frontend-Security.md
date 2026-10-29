# V3 Bezpieczeństwo frontendu webowego

## Cel kontrolny

Ta kategoria koncentruje się na wymaganiach chroniących przed atakami przeprowadzanymi za pośrednictwem frontendu webowego. Wymagania te nie mają zastosowania do rozwiązań działających w komunikacji maszyna–maszyna.

## V3.1 Dokumentacja bezpieczeństwa frontendu webowego

Ta sekcja wskazuje funkcje bezpieczeństwa przeglądarki, które powinny zostać określone w dokumentacji aplikacji.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **3.1.1** | Zweryfikuj, że dokumentacja aplikacji określa oczekiwane funkcje bezpieczeństwa, które muszą wspierać przeglądarki korzystające z aplikacji (takie jak HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP) oraz inne istotne mechanizmy bezpieczeństwa HTTP). Dokumentacja musi również definiować, jak aplikacja ma się zachować, gdy część tych funkcji jest niedostępna (na przykład ostrzec użytkownika lub zablokować dostęp). | 3 |

## V3.2 Niezamierzona interpretacja treści

Wyrenderowanie treści lub funkcjonalności w niewłaściwym kontekście może skutkować wykonaniem lub wyświetleniem złośliwej treści.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **3.2.1** | Zweryfikuj, że wdrożono mechanizmy bezpieczeństwa zapobiegające renderowaniu przez przeglądarki treści lub funkcjonalności z odpowiedzi HTTP w niewłaściwym kontekście (np. gdy API, plik przesłany przez użytkownika lub inny zasób jest żądany bezpośrednio). Możliwe mechanizmy obejmują: nieserwowanie treści, jeśli pola nagłówka żądania HTTP (takie jak Sec-Fetch-\*) nie wskazują właściwego kontekstu, użycie dyrektywy sandbox pola nagłówka Content-Security-Policy lub użycie typu dyspozycji attachment w polu nagłówka Content-Disposition. | 1 |
| **3.2.2** | Zweryfikuj, że treść przeznaczona do wyświetlenia jako tekst — a nie do wyrenderowania jako HTML — jest obsługiwana za pomocą bezpiecznych funkcji renderowania (takich jak createTextNode lub textContent), aby zapobiec niezamierzonemu wykonaniu treści takiej jak HTML lub JavaScript. | 1 |
| **3.2.3** | Zweryfikuj, że aplikacja unika DOM clobbering przy korzystaniu z JavaScript po stronie klienta poprzez jawne deklaracje zmiennych, ścisłą kontrolę typów, unikanie przechowywania zmiennych globalnych w obiekcie document oraz izolację przestrzeni nazw. | 3 |

## V3.3 Konfiguracja ciasteczek

Ta sekcja określa wymagania dotyczące bezpiecznej konfiguracji wrażliwych ciasteczek, aby zapewnić wyższy poziom pewności, że zostały utworzone przez samą aplikację, oraz zapobiec wyciekowi ich zawartości lub jej niewłaściwej modyfikacji.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **3.3.1** | Zweryfikuj, że ciasteczka mają ustawiony atrybut 'Secure', a jeśli nazwa ciasteczka nie używa przedrostka '\_\_Host-', musi używać przedrostka '\_\_Secure-'. | 1 |
| **3.3.2** | Zweryfikuj, że wartość atrybutu 'SameSite' każdego ciasteczka jest ustawiona stosownie do przeznaczenia ciasteczka, aby ograniczyć narażenie na ataki podmiany interfejsu użytkownika oraz przeglądarkowe ataki fałszowania żądań, powszechnie znane jako cross-site request forgery (CSRF). | 2 |
| **3.3.3** | Zweryfikuj, że nazwy ciasteczek mają przedrostek '\_\_Host-', chyba że ciasteczka są jawnie zaprojektowane do współdzielenia z innymi hostami. | 2 |
| **3.3.4** | Zweryfikuj, że jeśli wartość ciasteczka nie ma być dostępna dla skryptów po stronie klienta (jak token sesji), ciasteczko musi mieć ustawiony atrybut 'HttpOnly', a ta sama wartość (np. token sesji) musi być przekazywana klientowi wyłącznie poprzez pole nagłówka 'Set-Cookie'. | 2 |
| **3.3.5** | Zweryfikuj, że gdy aplikacja zapisuje ciasteczko, łączna długość nazwy i wartości ciasteczka nie przekracza 4096 bajtów. Zbyt duże ciasteczka nie zostaną zapisane przez przeglądarkę, a więc nie będą wysyłane z żądaniami, co uniemożliwi użytkownikowi korzystanie z funkcjonalności aplikacji zależnej od tego ciasteczka. | 3 |

## V3.4 Nagłówki mechanizmów bezpieczeństwa przeglądarki

Ta sekcja opisuje, które nagłówki bezpieczeństwa powinny być ustawiane w odpowiedziach HTTP, aby włączyć funkcje i ograniczenia bezpieczeństwa przeglądarki podczas obsługi odpowiedzi z aplikacji.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **3.4.1** | Zweryfikuj, że pole nagłówka Strict-Transport-Security jest dołączane do wszystkich odpowiedzi w celu wymuszenia polityki HTTP Strict Transport Security (HSTS). Maksymalny wiek (max-age) musi wynosić co najmniej 1 rok, a dla L2 i wyżej polityka musi obejmować również wszystkie subdomeny. | 1 |
| **3.4.2** | Zweryfikuj, że pole nagłówka Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin ma wartość stałą, ustaloną przez aplikację — a jeśli używana jest wartość pola nagłówka żądania HTTP Origin, jest ona walidowana względem listy dozwolonych zaufanych źródeł (origins). Gdy konieczne jest użycie 'Access-Control-Allow-Origin: *', zweryfikuj, że odpowiedź nie zawiera żadnych informacji wrażliwych. | 1 |
| **3.4.3** | Zweryfikuj, że odpowiedzi HTTP zawierają pole nagłówka odpowiedzi Content-Security-Policy definiujące dyrektywy zapewniające, że przeglądarka ładuje i wykonuje wyłącznie zaufaną treść lub zasoby, aby ograniczyć wykonanie złośliwego JavaScriptu. Jako minimum musi być stosowana polityka globalna zawierająca dyrektywy object-src 'none' i base-uri 'none' oraz definiująca listę dozwolonych albo używająca wartości nonce lub skrótów (hash). Dla aplikacji L3 musi być zdefiniowana polityka dla poszczególnych odpowiedzi z wartościami nonce lub skrótami. | 2 |
| **3.4.4** | Zweryfikuj, że wszystkie odpowiedzi HTTP zawierają pole nagłówka 'X-Content-Type-Options: nosniff'. Nakazuje ono przeglądarkom rezygnację ze sniffingu treści i zgadywania typu MIME dla danej odpowiedzi oraz wymaganie, aby wartość pola nagłówka Content-Type odpowiedzi odpowiadała docelowemu zasobowi. Na przykład odpowiedź na żądanie stylu jest akceptowana tylko wtedy, gdy Content-Type odpowiedzi to 'text/css'. Włącza to również funkcjonalność Cross-Origin Read Blocking (CORB) w przeglądarce. | 2 |
| **3.4.5** | Zweryfikuj, że aplikacja ustawia politykę referrer, aby zapobiec wyciekowi technicznie wrażliwych danych do usług stron trzecich poprzez pole nagłówka żądania HTTP 'Referer'. Można to zrobić za pomocą pola nagłówka odpowiedzi HTTP Referrer-Policy lub poprzez atrybuty elementów HTML. Dane wrażliwe mogą obejmować ścieżkę i parametry zapytania w URL, a dla wewnętrznych, niepublicznych aplikacji — również nazwę hosta. | 2 |
| **3.4.6** | Zweryfikuj, że aplikacja internetowa używa dyrektywy frame-ancestors pola nagłówka Content-Security-Policy w każdej odpowiedzi HTTP, aby zapewnić, że domyślnie nie może być osadzana, a osadzanie konkretnych zasobów jest dozwolone tylko wtedy, gdy to konieczne. Zwróć uwagę, że pole nagłówka X-Frame-Options, choć wspierane przez przeglądarki, jest przestarzałe i nie należy na nim polegać. | 2 |
| **3.4.7** | Zweryfikuj, że pole nagłówka Content-Security-Policy wskazuje lokalizację raportowania naruszeń. | 3 |
| **3.4.8** | Zweryfikuj, że wszystkie odpowiedzi HTTP inicjujące renderowanie dokumentu (takie jak odpowiedzi z Content-Type text/html) zawierają pole nagłówka Cross‑Origin‑Opener‑Policy z dyrektywą same-origin lub — w razie potrzeby — same-origin-allow-popups. Zapobiega to atakom nadużywającym współdzielonego dostępu do obiektów Window, takim jak tabnabbing czy zliczanie ramek (frame counting). | 3 |

## V3.5 Separacja źródeł w przeglądarce

Przyjmując po stronie serwera żądanie dotyczące wrażliwej funkcjonalności, aplikacja musi upewnić się, że żądanie zostało zainicjowane przez samą aplikację lub zaufaną stronę i nie zostało sfałszowane przez atakującego.

Wrażliwa funkcjonalność w tym kontekście może obejmować przyjmowanie formularzy od użytkowników uwierzytelnionych i nieuwierzytelnionych (np. żądanie uwierzytelnienia), operacje zmieniające stan lub funkcjonalność wymagającą znacznych zasobów (np. eksport danych).

Kluczowe zabezpieczenia to polityki bezpieczeństwa przeglądarki, takie jak Same Origin Policy dla JavaScriptu oraz logika SameSite dla ciasteczek. Innym powszechnym zabezpieczeniem jest mechanizm preflight CORS. Mechanizm ten jest krytyczny dla endpointów zaprojektowanych do wywoływania z innego źródła, ale może też być użytecznym mechanizmem zapobiegania fałszowaniu żądań dla endpointów, które nie są przeznaczone do wywoływania z innego źródła.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **3.5.1** | Zweryfikuj, że jeśli aplikacja nie opiera się na mechanizmie preflight CORS w celu zapobiegania niedozwolonym żądaniom cross-origin do wrażliwej funkcjonalności, żądania te są walidowane w celu potwierdzenia, że pochodzą z samej aplikacji. Można to zrobić poprzez stosowanie i walidację tokenów anti-forgery lub wymaganie dodatkowych pól nagłówka HTTP, które nie znajdują się na liście CORS-safelisted request-header fields. Ma to chronić przed przeglądarkowymi atakami fałszowania żądań, powszechnie znanymi jako cross-site request forgery (CSRF). | 1 |
| **3.5.2** | Zweryfikuj, że jeśli aplikacja opiera się na mechanizmie preflight CORS w celu zapobiegania niedozwolonemu użyciu wrażliwej funkcjonalności cross-origin, nie jest możliwe wywołanie tej funkcjonalności żądaniem, które nie wyzwala żądania preflight CORS. Może to wymagać sprawdzania wartości pól nagłówka żądania 'Origin' i 'Content-Type' lub użycia dodatkowego pola nagłówka spoza listy CORS-safelisted header-fields. | 1 |
| **3.5.3** | Zweryfikuj, że żądania HTTP do wrażliwej funkcjonalności używają odpowiednich metod HTTP, takich jak POST, PUT, PATCH lub DELETE, a nie metod zdefiniowanych w specyfikacji HTTP jako „bezpieczne”, takich jak HEAD, OPTIONS czy GET. Alternatywnie można zastosować ścisłą walidację pól nagłówka żądania Sec-Fetch-*, aby upewnić się, że żądanie nie pochodzi z niewłaściwego wywołania cross-origin, żądania nawigacji ani ładowania zasobu (np. źródła obrazu) tam, gdzie nie jest to oczekiwane. | 1 |
| **3.5.4** | Zweryfikuj, że odrębne aplikacje są hostowane na różnych nazwach hostów, aby wykorzystać ograniczenia zapewniane przez politykę same-origin — w tym zasady interakcji dokumentów lub skryptów załadowanych przez jedno źródło z zasobami innego źródła oraz oparte na nazwie hosta ograniczenia dotyczące ciasteczek. | 2 |
| **3.5.5** | Zweryfikuj, że wiadomości odbierane przez interfejs postMessage są odrzucane, jeśli źródło wiadomości nie jest zaufane lub jej składnia jest nieprawidłowa. | 2 |
| **3.5.6** | Zweryfikuj, że funkcjonalność JSONP nie jest włączona nigdzie w aplikacji, aby uniknąć ataków Cross-Site Script Inclusion (XSSI). | 3 |
| **3.5.7** | Zweryfikuj, że dane wymagające autoryzacji nie są umieszczane w odpowiedziach zasobów skryptowych, takich jak pliki JavaScript, aby zapobiec atakom Cross-Site Script Inclusion (XSSI). | 3 |
| **3.5.8** | Zweryfikuj, że uwierzytelnione zasoby (takie jak obrazy, wideo, skrypty i inne dokumenty) mogą być ładowane lub osadzane w imieniu użytkownika tylko wtedy, gdy jest to zamierzone. Można to osiągnąć poprzez ścisłą walidację pól nagłówka żądania HTTP Sec-Fetch-*, aby upewnić się, że żądanie nie pochodzi z niewłaściwego wywołania cross-origin, lub poprzez ustawienie restrykcyjnego pola nagłówka odpowiedzi HTTP Cross-Origin-Resource-Policy, nakazującego przeglądarce zablokowanie zwróconej treści. | 3 |

## V3.6 Integralność zasobów zewnętrznych

Ta sekcja zawiera wytyczne dotyczące bezpiecznego hostowania treści w serwisach stron trzecich.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **3.6.1** | Zweryfikuj, że zasoby po stronie klienta — takie jak biblioteki JavaScript, CSS czy fonty webowe — są hostowane zewnętrznie (np. w Content Delivery Network) tylko wtedy, gdy zasób jest statyczny i wersjonowany, a do walidacji jego integralności używana jest Subresource Integrity (SRI). Jeśli nie jest to możliwe, dla każdego zasobu powinna istnieć udokumentowana decyzja bezpieczeństwa to uzasadniająca. | 3 |

## V3.7 Pozostałe kwestie bezpieczeństwa przeglądarki

Ta sekcja obejmuje różne inne mechanizmy bezpieczeństwa oraz nowoczesne funkcje bezpieczeństwa przeglądarek wymagane dla bezpieczeństwa po stronie klienta.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **3.7.1** | Zweryfikuj, że aplikacja korzysta wyłącznie z technologii po stronie klienta, które są nadal wspierane i uznawane za bezpieczne. Przykłady technologii niespełniających tego wymagania to wtyczki NSAPI, Flash, Shockwave, ActiveX, Silverlight, NACL oraz aplety Javy po stronie klienta. | 2 |
| **3.7.2** | Zweryfikuj, że aplikacja automatycznie przekierowuje użytkownika na inną nazwę hosta lub domenę (niekontrolowaną przez aplikację) tylko wtedy, gdy cel przekierowania znajduje się na liście dozwolonych. | 2 |
| **3.7.3** | Zweryfikuj, że aplikacja wyświetla powiadomienie, gdy użytkownik jest przekierowywany na adres URL poza kontrolą aplikacji, z możliwością anulowania nawigacji. | 3 |
| **3.7.4** | Zweryfikuj, że domena najwyższego poziomu aplikacji (np. site.tld) została dodana do publicznej listy preload dla HTTP Strict Transport Security (HSTS). Zapewnia to, że użycie TLS dla aplikacji jest wbudowane bezpośrednio w główne przeglądarki, a nie zależy wyłącznie od pola nagłówka odpowiedzi Strict-Transport-Security. | 3 |
| **3.7.5** | Zweryfikuj, że aplikacja zachowuje się zgodnie z dokumentacją (np. ostrzega użytkownika lub blokuje dostęp), jeśli przeglądarka użyta do korzystania z aplikacji nie wspiera oczekiwanych funkcji bezpieczeństwa. | 3 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
* [OWASP DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)
