# V4 API i usługi sieciowe

## Cel kontrolny

Szereg kwestii dotyczy w szczególności aplikacji udostępniających API do użytku przez przeglądarki internetowe lub innych konsumentów (zwykle z użyciem JSON, XML lub GraphQL). Niniejszy rozdział obejmuje odpowiednie konfiguracje i mechanizmy bezpieczeństwa, które należy zastosować.

Należy pamiętać, że kwestie uwierzytelniania, zarządzania sesją i walidacji danych wejściowych z pozostałych rozdziałów również dotyczą API — tego rozdziału nie można więc wyrywać z kontekstu ani testować w izolacji.

## V4.1 Ogólne bezpieczeństwo usług sieciowych

Ta sekcja dotyczy ogólnych kwestii bezpieczeństwa usług sieciowych, a co za tym idzie — podstawowych praktyk higieny usług sieciowych.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **4.1.1** | Zweryfikuj, że każda odpowiedź HTTP z treścią komunikatu zawiera pole nagłówka Content-Type odpowiadające rzeczywistej zawartości odpowiedzi, wraz z parametrem charset określającym bezpieczne kodowanie znaków (np. UTF-8, ISO-8859-1) zgodnie z IANA Media Types, np. dla "text/", "/+xml" i "/xml". | 1 |
| **4.1.2** | Zweryfikuj, że wyłącznie endpointy skierowane do użytkownika (przeznaczone do ręcznego dostępu przez przeglądarkę) automatycznie przekierowują z HTTP na HTTPS, natomiast pozostałe usługi i endpointy nie stosują przezroczystych przekierowań. Ma to zapobiec sytuacji, w której klient błędnie wysyła nieszyfrowane żądania HTTP, lecz — ponieważ żądania są automatycznie przekierowywane na HTTPS — wyciek danych wrażliwych pozostaje niewykryty. | 2 |
| **4.1.3** | Zweryfikuj, że żadne pole nagłówka HTTP używane przez aplikację i ustawiane przez warstwę pośredniczącą — taką jak moduł równoważenia obciążenia, proxy webowe lub usługa backend-for-frontend — nie może zostać nadpisane przez użytkownika końcowego. Przykładowe nagłówki to X-Real-IP, X-Forwarded-* lub X-User-ID. | 2 |
| **4.1.4** | Zweryfikuj, że mogą być używane wyłącznie metody HTTP jawnie wspierane przez aplikację lub jej API (w tym OPTIONS podczas żądań preflight), a metody nieużywane są blokowane. | 3 |
| **4.1.5** | Zweryfikuj, że dla żądań lub transakcji wysoce wrażliwych albo przechodzących przez wiele systemów stosowane są podpisy cyfrowe dla poszczególnych komunikatów, zapewniające dodatkową pewność ponad zabezpieczenia warstwy transportowej. | 3 |

## V4.2 Walidacja struktury komunikatów HTTP

Ta sekcja wyjaśnia, jak należy walidować strukturę i pola nagłówków komunikatu HTTP, aby zapobiegać atakom takim jak request smuggling, response splitting, wstrzyknięcie nagłówków oraz odmowa usługi poprzez nadmiernie długie komunikaty HTTP.

Wymagania te dotyczą ogólnego przetwarzania i generowania komunikatów HTTP, ale są szczególnie istotne przy konwersji komunikatów HTTP między różnymi wersjami protokołu.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **4.2.1** | Zweryfikuj, że wszystkie komponenty aplikacji (w tym moduły równoważenia obciążenia, zapory i serwery aplikacyjne) wyznaczają granice przychodzących komunikatów HTTP przy użyciu mechanizmu właściwego dla danej wersji HTTP, aby zapobiec atakom HTTP request smuggling. W HTTP/1.x, jeśli obecne jest pole nagłówka Transfer-Encoding, nagłówek Content-Length musi zostać zignorowany zgodnie z RFC 2616. W HTTP/2 i HTTP/3, jeśli obecne jest pole nagłówka Content-Length, odbiorca musi upewnić się, że jest ono spójne z długością ramek DATA. | 2 |
| **4.2.2** | Zweryfikuj, że przy generowaniu komunikatów HTTP pole nagłówka Content-Length nie stoi w sprzeczności z długością treści wynikającą z ramkowania protokołu HTTP, aby zapobiec atakom request smuggling. | 3 |
| **4.2.3** | Zweryfikuj, że aplikacja nie wysyła ani nie akceptuje komunikatów HTTP/2 lub HTTP/3 z polami nagłówka specyficznymi dla połączenia, takimi jak Transfer-Encoding, aby zapobiec atakom response splitting i wstrzyknięcia nagłówków. | 3 |
| **4.2.4** | Zweryfikuj, że aplikacja akceptuje wyłącznie żądania HTTP/2 i HTTP/3, w których pola nagłówków i ich wartości nie zawierają sekwencji CR (\r), LF (\n) ani CRLF (\r\n), aby zapobiec atakom wstrzyknięcia nagłówków. | 3 |
| **4.2.5** | Zweryfikuj, że jeśli aplikacja (backend lub frontend) buduje i wysyła żądania, stosuje walidację, sanityzację lub inne mechanizmy zapobiegające tworzeniu URI (np. dla wywołań API) lub pól nagłówka żądania HTTP (np. Authorization lub Cookie), które są zbyt długie, aby zostały zaakceptowane przez komponent odbierający. Mogłoby to spowodować odmowę usługi — na przykład wysłanie nadmiernie długiego żądania (np. długiego pola nagłówka cookie) skutkujące tym, że serwer zawsze odpowiada statusem błędu. | 3 |

## V4.3 GraphQL

GraphQL staje się coraz popularniejszym sposobem tworzenia bogatych w dane klientów, które nie są ściśle powiązane z różnorodnymi usługami backendowymi. Ta sekcja obejmuje kwestie bezpieczeństwa GraphQL.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **4.3.1** | Zweryfikuj, że stosowana jest lista dozwolonych zapytań, ograniczanie głębokości, ograniczanie liczby lub analiza kosztu zapytań, aby zapobiec odmowie usługi (DoS) na poziomie GraphQL lub wyrażeń warstwy danych w wyniku kosztownych, zagnieżdżonych zapytań. | 2 |
| **4.3.2** | Zweryfikuj, że zapytania introspekcyjne GraphQL są wyłączone w środowisku produkcyjnym, chyba że API GraphQL jest przeznaczone do użytku przez strony trzecie. | 2 |

## V4.4 WebSocket

WebSocket to protokół komunikacyjny zapewniający jednoczesny, dwukierunkowy kanał komunikacji przez pojedyncze połączenie TCP. Został ustandaryzowany przez IETF jako RFC 6455 w 2011 roku i jest odrębny od HTTP, mimo że został zaprojektowany do działania na portach HTTP 443 i 80.

Ta sekcja zawiera kluczowe wymagania bezpieczeństwa zapobiegające atakom związanym z bezpieczeństwem komunikacji i zarządzaniem sesją, które wykorzystują specyfikę tego kanału komunikacji w czasie rzeczywistym.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **4.4.1** | Zweryfikuj, że dla wszystkich połączeń WebSocket używany jest WebSocket over TLS (WSS). | 1 |
| **4.4.2** | Zweryfikuj, że podczas początkowego uzgadniania HTTP WebSocket pole nagłówka Origin jest sprawdzane względem listy źródeł dozwolonych dla aplikacji. | 2 |
| **4.4.3** | Zweryfikuj, że jeśli nie można użyć standardowego zarządzania sesją aplikacji, stosowane są w tym celu dedykowane tokeny zgodne z odpowiednimi wymaganiami bezpieczeństwa zarządzania sesją. | 2 |
| **4.4.4** | Zweryfikuj, że dedykowane tokeny zarządzania sesją WebSocket są początkowo uzyskiwane lub walidowane poprzez wcześniej uwierzytelnioną sesję HTTPS podczas przechodzenia z istniejącej sesji HTTPS na kanał WebSocket. | 2 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* Materiały o autoryzacji w GraphQL z [graphql.org](https://graphql.org/learn/authorization/) oraz [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods).
* [OWASP Web Security Testing Guide: GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [OWASP Web Security Testing Guide: Testing WebSockets](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)
