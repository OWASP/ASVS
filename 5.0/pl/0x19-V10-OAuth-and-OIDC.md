# V10 OAuth i OIDC

## Cel kontrolny

OAuth2 (w tym rozdziale nazywany OAuth) to branżowy standard delegowanej autoryzacji. Przykładowo z użyciem OAuth aplikacja kliencka może uzyskać dostęp do API (zasobów serwera) w imieniu użytkownika, o ile użytkownik ją do tego upoważnił.

Sam OAuth nie został zaprojektowany do uwierzytelniania użytkowników. Framework OpenID Connect (OIDC) rozszerza OAuth, dodając nad nim warstwę tożsamości użytkownika. OIDC zapewnia wsparcie dla funkcji obejmujących ustandaryzowane informacje o użytkowniku, jednokrotne logowanie (SSO) oraz zarządzanie sesją. Ponieważ OIDC jest rozszerzeniem OAuth, wymagania OAuth z tego rozdziału mają zastosowanie również do OIDC.

W OAuth zdefiniowane są następujące role:

* Klient OAuth to aplikacja, która próbuje uzyskać dostęp do zasobów serwera (np. wywołując API z użyciem wystawionego tokena dostępu). Klient OAuth jest często aplikacją serwerową.
    * Klient poufny (confidential client) to klient zdolny do zachowania poufności poświadczeń, których używa do uwierzytelniania się wobec serwera autoryzacji.
    * Klient publiczny (public client) nie jest zdolny do zachowania poufności poświadczeń służących do uwierzytelniania wobec serwera autoryzacji. Dlatego zamiast się uwierzytelniać (np. parametrami 'client_id' i 'client_secret'), jedynie się identyfikuje (parametrem 'client_id').
* Serwer zasobów OAuth (resource server, RS) to serwerowe API udostępniające zasoby klientom OAuth.
* Serwer autoryzacji OAuth (authorization server, AS) to aplikacja serwerowa wystawiająca tokeny dostępu klientom OAuth. Tokeny te pozwalają klientom OAuth uzyskiwać dostęp do zasobów RS — w imieniu użytkownika końcowego albo we własnym imieniu klienta OAuth. AS jest często odrębną aplikacją, ale (jeśli to właściwe) może być zintegrowany z odpowiednim RS.
* Właściciel zasobu (resource owner, RO) to użytkownik końcowy, który upoważnia klientów OAuth do uzyskania ograniczonego dostępu do zasobów hostowanych na serwerze zasobów w jego imieniu. Właściciel zasobu wyraża zgodę na tę delegowaną autoryzację poprzez interakcję z serwerem autoryzacji.

W OIDC zdefiniowane są następujące role:

* Strona ufająca (relying party, RP) to aplikacja kliencka żądająca uwierzytelnienia użytkownika końcowego za pośrednictwem dostawcy OpenID. Pełni rolę klienta OAuth.
* Dostawca OpenID (OpenID Provider, OP) to serwer autoryzacji OAuth zdolny do uwierzytelnienia użytkownika końcowego i dostarczający stronie ufającej oświadczenia OIDC. OP może być dostawcą tożsamości (IdP), ale w scenariuszach federacyjnych OP i dostawca tożsamości (u którego uwierzytelnia się użytkownik końcowy) mogą być różnymi aplikacjami serwerowymi.

OAuth i OIDC zostały pierwotnie zaprojektowane dla aplikacji stron trzecich. Obecnie są często używane również przez aplikacje własne (first-party). Jednak w scenariuszach first-party — takich jak uwierzytelnianie i zarządzanie sesją — protokół wprowadza dodatkową złożoność, która może rodzić nowe wyzwania bezpieczeństwa.

OAuth i OIDC mogą być stosowane w wielu typach aplikacji, ale ASVS i wymagania tego rozdziału koncentrują się na aplikacjach internetowych i API.

Ponieważ OAuth i OIDC można traktować jako logikę zbudowaną na technologiach webowych, ogólne wymagania z pozostałych rozdziałów zawsze mają zastosowanie, a tego rozdziału nie można rozpatrywać w oderwaniu od kontekstu.

Niniejszy rozdział odzwierciedla aktualne najlepsze praktyki dla OAuth2 i OIDC, zgodne ze specyfikacjami dostępnymi pod adresami <https://oauth.net/2/> oraz <https://openid.net/developers/specs/>. Nawet jeśli RFC są uznawane za dojrzałe, są często aktualizowane — dlatego stosując wymagania tego rozdziału, ważne jest trzymanie się najnowszych wersji. Więcej szczegółów w sekcji źródeł.

Zważywszy na złożoność tego obszaru, dla bezpiecznego rozwiązania OAuth lub OIDC absolutnie kluczowe jest korzystanie z uznanych, branżowych serwerów autoryzacji oraz stosowanie zalecanej konfiguracji bezpieczeństwa.

Terminologia użyta w tym rozdziale jest zgodna z RFC OAuth i specyfikacjami OIDC, przy czym terminologia OIDC jest używana wyłącznie w wymaganiach specyficznych dla OIDC; w pozostałych przypadkach stosowana jest terminologia OAuth.

W kontekście OAuth i OIDC termin „token” w tym rozdziale odnosi się do:

* Tokenów dostępu, które mogą być konsumowane wyłącznie przez RS i mogą być tokenami referencyjnymi walidowanymi poprzez introspekcję albo tokenami samowystarczalnymi walidowanymi z użyciem materiału klucza.
* Tokenów odświeżania, które mogą być konsumowane wyłącznie przez serwer autoryzacji, który je wystawił.
* Tokenów ID OIDC, które mogą być konsumowane wyłącznie przez klienta, który zainicjował przepływ autoryzacji.

Poziomy ryzyka niektórych wymagań tego rozdziału zależą od tego, czy klient jest klientem poufnym, czy uznawany jest za klienta publicznego. Ponieważ silne uwierzytelnianie klienta ogranicza wiele wektorów ataku, kilka wymagań może zostać złagodzonych przy stosowaniu klienta poufnego w aplikacjach L1.

## V10.1 Ogólne bezpieczeństwo OAuth i OIDC

Ta sekcja obejmuje ogólne wymagania architektoniczne mające zastosowanie do wszystkich aplikacji korzystających z OAuth lub OIDC.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **10.1.1** | Zweryfikuj, że tokeny są wysyłane wyłącznie do komponentów, które ściśle ich potrzebują. Na przykład przy stosowaniu wzorca backend-for-frontend dla przeglądarkowych aplikacji JavaScript tokeny dostępu i odświeżania mogą być dostępne wyłącznie dla backendu. | 2 |
| **10.1.2** | Zweryfikuj, że klient akceptuje wartości od serwera autoryzacji (takie jak kod autoryzacyjny lub token ID) tylko wtedy, gdy wartości te pochodzą z przepływu autoryzacji zainicjowanego przez tę samą sesję agenta użytkownika i tę samą transakcję. Wymaga to, aby sekrety generowane przez klienta — takie jak 'code_verifier' z proof key for code exchange (PKCE), 'state' lub 'nonce' OIDC — były nieodgadywalne, specyficzne dla transakcji oraz bezpiecznie powiązane zarówno z klientem, jak i z sesją agenta użytkownika, w której transakcja została rozpoczęta. | 2 |

## V10.2 Klient OAuth

Te wymagania określają obowiązki aplikacji klienckich OAuth. Klientem może być na przykład backend serwera WWW (często działający jako Backend For Frontend, BFF), integracja usługi backendowej albo frontendowa aplikacja typu Single Page Application (SPA, zwana też aplikacją przeglądarkową).

Zasadniczo klienci backendowi są uznawani za klientów poufnych, a klienci frontendowi — za klientów publicznych. Jednak aplikacje natywne działające na urządzeniu użytkownika końcowego mogą być uznane za poufne przy stosowaniu dynamicznej rejestracji klienta OAuth.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **10.2.1** | Zweryfikuj, że jeśli używany jest przepływ kodu (code flow), klient OAuth posiada ochronę przed przeglądarkowymi atakami fałszowania żądań — powszechnie znanymi jako cross-site request forgery (CSRF) — wyzwalającymi żądania tokenów, poprzez użycie mechanizmu proof key for code exchange (PKCE) albo sprawdzanie parametru 'state' wysłanego w żądaniu autoryzacji. | 2 |
| **10.2.2** | Zweryfikuj, że jeśli klient OAuth może współpracować z więcej niż jednym serwerem autoryzacji, posiada obronę przed atakami mix-up. Na przykład może wymagać, aby serwer autoryzacji zwracał wartość parametru 'iss', i walidować ją w odpowiedzi autoryzacji oraz odpowiedzi tokena. | 2 |
| **10.2.3** | Zweryfikuj, że klient OAuth żąda w żądaniach do serwera autoryzacji wyłącznie wymaganych zakresów (scopes) lub innych parametrów autoryzacji. | 3 |

## V10.3 Serwer zasobów OAuth

W kontekście ASVS i tego rozdziału serwer zasobów to API. Aby zapewnić bezpieczny dostęp, serwer zasobów musi:

* Zwalidować token dostępu zgodnie z formatem tokena i właściwymi specyfikacjami protokołu, np. walidacją JWT lub introspekcją tokena OAuth.
* Jeśli token jest ważny — egzekwować decyzje autoryzacyjne na podstawie informacji z tokena dostępu oraz przyznanych uprawnień. Na przykład serwer zasobów musi zweryfikować, że klient (działający w imieniu RO) jest uprawniony do dostępu do żądanego zasobu.

Wymienione tu wymagania są zatem specyficzne dla OAuth lub OIDC i powinny być realizowane po walidacji tokena, a przed wykonaniem autoryzacji na podstawie informacji z tokena.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **10.3.1** | Zweryfikuj, że serwer zasobów akceptuje wyłącznie tokeny dostępu przeznaczone do użytku z tą usługą (audience). Odbiorca może być zawarty w ustrukturyzowanym tokenie dostępu (np. oświadczenie 'aud' w JWT) albo sprawdzany z użyciem endpointu introspekcji tokenów. | 2 |
| **10.3.2** | Zweryfikuj, że serwer zasobów egzekwuje decyzje autoryzacyjne na podstawie oświadczeń z tokena dostępu definiujących delegowaną autoryzację. Jeśli obecne są oświadczenia takie jak 'sub', 'scope' i 'authorization_details', muszą one stanowić część decyzji. | 2 |
| **10.3.3** | Zweryfikuj, że jeśli decyzja kontroli dostępu wymaga zidentyfikowania unikalnego użytkownika na podstawie tokena dostępu (JWT lub powiązanej odpowiedzi introspekcji tokena), serwer zasobów identyfikuje użytkownika na podstawie oświadczeń, których nie można przypisać ponownie innym użytkownikom. Zwykle oznacza to użycie kombinacji oświadczeń 'iss' i 'sub'. | 2 |
| **10.3.4** | Zweryfikuj, że jeśli serwer zasobów wymaga określonej siły, metod lub aktualności uwierzytelnienia, weryfikuje, czy przedstawiony token dostępu spełnia te ograniczenia — na przykład, jeśli występują, z użyciem oświadczeń OIDC odpowiednio 'acr', 'amr' i 'auth_time'. | 2 |
| **10.3.5** | Zweryfikuj, że serwer zasobów zapobiega użyciu skradzionych tokenów dostępu lub ich powtórzeniu (przez strony nieuprawnione), wymagając tokenów dostępu ograniczonych do nadawcy (sender-constrained) — z użyciem Mutual TLS dla OAuth 2 albo OAuth 2 Demonstration of Proof of Possession (DPoP). | 3 |

## V10.4 Serwer autoryzacji OAuth

Te wymagania określają obowiązki serwerów autoryzacji OAuth, w tym dostawców OpenID.

Dla uwierzytelniania klienta dozwolona jest metoda 'self_signed_tls_client_auth', z zastrzeżeniem warunków wstępnych wymaganych przez [sekcję 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) dokumentu [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705).

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **10.4.1** | Zweryfikuj, że serwer autoryzacji waliduje URI przekierowania na podstawie specyficznej dla klienta listy dozwolonych wstępnie zarejestrowanych URI, stosując porównanie dokładne (exact string comparison). | 1 |
| **10.4.2** | Zweryfikuj, że jeśli serwer autoryzacji zwraca kod autoryzacyjny w odpowiedzi autoryzacji, kod ten może zostać użyty tylko raz w żądaniu tokena. Przy drugim poprawnym żądaniu z kodem autoryzacyjnym, który został już użyty do wystawienia tokena dostępu, serwer autoryzacji musi odrzucić żądanie tokena oraz unieważnić wszystkie wystawione tokeny powiązane z tym kodem autoryzacyjnym. | 1 |
| **10.4.3** | Zweryfikuj, że kod autoryzacyjny jest krótkotrwały. Maksymalny czas życia może wynosić do 10 minut dla aplikacji L1 i L2 oraz do 1 minuty dla aplikacji L3. | 1 |
| **10.4.4** | Zweryfikuj, że dla danego klienta serwer autoryzacji zezwala wyłącznie na użycie grantów, których ten klient potrzebuje. Zwróć uwagę, że granty 'token' (przepływ Implicit) oraz 'password' (przepływ Resource Owner Password Credentials) nie mogą być już używane. | 1 |
| **10.4.5** | Zweryfikuj, że serwer autoryzacji ogranicza ryzyko ataków powtórzeniowych na tokeny odświeżania dla klientów publicznych, najlepiej z użyciem tokenów odświeżania ograniczonych do nadawcy, tj. Demonstrating Proof of Possession (DPoP) lub tokenów dostępu powiązanych z certyfikatem z użyciem mutual TLS (mTLS). Dla aplikacji L1 i L2 można stosować rotację tokenów odświeżania. Jeśli stosowana jest rotacja, serwer autoryzacji musi unieważnić token odświeżania po użyciu oraz odwołać wszystkie tokeny odświeżania dla danej autoryzacji, jeśli przedstawiony zostanie token odświeżania już użyty i unieważniony. | 1 |
| **10.4.6** | Zweryfikuj, że jeśli używany jest grant kodu, serwer autoryzacji ogranicza ryzyko ataków przechwycenia kodu autoryzacyjnego, wymagając proof key for code exchange (PKCE). Dla żądań autoryzacji serwer autoryzacji musi wymagać prawidłowej wartości 'code_challenge' i nie może akceptować wartości 'code_challenge_method' równej 'plain'. Dla żądania tokena musi wymagać walidacji parametru 'code_verifier'. | 2 |
| **10.4.7** | Zweryfikuj, że jeśli serwer autoryzacji wspiera nieuwierzytelnioną dynamiczną rejestrację klientów, ogranicza ryzyko złośliwych aplikacji klienckich. Musi walidować metadane klienta, takie jak wszelkie rejestrowane URI, zapewnić zgodę użytkownika oraz ostrzec użytkownika przed przetworzeniem żądania autoryzacji z niezaufaną aplikacją kliencką. | 2 |
| **10.4.8** | Zweryfikuj, że tokeny odświeżania mają bezwzględny termin wygaśnięcia, również wtedy, gdy stosowane jest przesuwne wygasanie tokenów odświeżania. | 2 |
| **10.4.9** | Zweryfikuj, że tokeny odświeżania i referencyjne tokeny dostępu mogą zostać odwołane przez uprawnionego użytkownika z poziomu interfejsu użytkownika serwera autoryzacji, aby ograniczyć ryzyko złośliwych klientów lub skradzionych tokenów. | 2 |
| **10.4.10** | Zweryfikuj, że klient poufny jest uwierzytelniany dla żądań kanałem zwrotnym (backchannel) od klienta do serwera autoryzacji, takich jak żądania tokenów, pushed authorization requests (PAR) oraz żądania odwołania tokenów. | 2 |
| **10.4.11** | Zweryfikuj, że konfiguracja serwera autoryzacji przypisuje klientowi OAuth wyłącznie wymagane zakresy. | 2 |
| **10.4.12** | Zweryfikuj, że dla danego klienta serwer autoryzacji zezwala wyłącznie na wartość 'response_mode', której ten klient potrzebuje — na przykład poprzez walidację tej wartości przez serwer autoryzacji względem wartości oczekiwanych albo użycie pushed authorization request (PAR) lub JWT-secured Authorization Request (JAR). | 3 |
| **10.4.13** | Zweryfikuj, że grant typu 'code' jest zawsze używany łącznie z pushed authorization requests (PAR). | 3 |
| **10.4.14** | Zweryfikuj, że serwer autoryzacji wystawia wyłącznie tokeny dostępu ograniczone do nadawcy (Proof-of-Possession) — z tokenami dostępu powiązanymi z certyfikatem z użyciem mutual TLS (mTLS) albo tokenami powiązanymi z DPoP (Demonstration of Proof of Possession). | 3 |
| **10.4.15** | Zweryfikuj, że dla klienta serwerowego (niewykonywanego na urządzeniu użytkownika końcowego) serwer autoryzacji zapewnia, że wartość parametru 'authorization_details' pochodzi z backendu klienta i nie została zmanipulowana przez użytkownika — na przykład poprzez wymaganie użycia pushed authorization request (PAR) lub JWT-secured Authorization Request (JAR). | 3 |
| **10.4.16** | Zweryfikuj, że klient jest poufny, a serwer autoryzacji wymaga stosowania silnych metod uwierzytelniania klienta (opartych na kryptografii klucza publicznego i odpornych na ataki powtórzeniowe), takich jak mutual TLS ('tls_client_auth', 'self_signed_tls_client_auth') lub private key JWT ('private_key_jwt'). | 3 |

## V10.5 Klient OIDC

Ponieważ strona ufająca OIDC działa jako klient OAuth, zastosowanie mają również wymagania z sekcji „Klient OAuth”.

Zwróć uwagę, że sekcja „Uwierzytelnianie z dostawcą tożsamości” w rozdziale „Uwierzytelnianie” również zawiera istotne wymagania ogólne.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **10.5.1** | Zweryfikuj, że klient (jako strona ufająca) ogranicza ryzyko ataków powtórzeniowych na token ID — na przykład zapewniając, że oświadczenie 'nonce' w tokenie ID odpowiada wartości 'nonce' wysłanej w żądaniu uwierzytelnienia do dostawcy OpenID (w OAuth2 nazywanym żądaniem autoryzacji wysyłanym do serwera autoryzacji). | 2 |
| **10.5.2** | Zweryfikuj, że klient jednoznacznie identyfikuje użytkownika na podstawie oświadczeń tokena ID — zwykle oświadczenia 'sub' — których nie można przypisać ponownie innym użytkownikom (w zakresie danego dostawcy tożsamości). | 2 |
| **10.5.3** | Zweryfikuj, że klient odrzuca próby podszycia się złośliwego serwera autoryzacji pod inny serwer autoryzacji za pośrednictwem metadanych serwera autoryzacji. Klient musi odrzucić metadane serwera autoryzacji, jeśli URL wystawcy w tych metadanych nie odpowiada dokładnie wstępnie skonfigurowanemu URL wystawcy oczekiwanemu przez klienta. | 2 |
| **10.5.4** | Zweryfikuj, że klient waliduje, iż token ID jest przeznaczony do użytku przez tego klienta (audience), sprawdzając, że oświadczenie 'aud' z tokena jest równe wartości 'client_id' klienta. | 2 |
| **10.5.5** | Zweryfikuj, że przy korzystaniu z wylogowania kanałem zwrotnym OIDC (back-channel logout) strona ufająca ogranicza ryzyko odmowy usługi poprzez wymuszone wylogowanie oraz pomylenia różnych JWT (cross-JWT confusion) w przepływie wylogowania. Klient musi zweryfikować, że token wylogowania ma poprawny typ o wartości 'logout+jwt', zawiera oświadczenie 'event' z poprawną nazwą elementu oraz nie zawiera oświadczenia 'nonce'. Zwróć uwagę, że zalecany jest również krótki czas wygaśnięcia (np. 2 minuty). | 2 |

## V10.6 Dostawca OpenID

Ponieważ dostawcy OpenID działają jako serwery autoryzacji OAuth, zastosowanie mają również wymagania z sekcji „Serwer autoryzacji OAuth”.

Zwróć uwagę, że przy stosowaniu przepływu tokena ID (a nie przepływu kodu) tokeny dostępu nie są wystawiane i wiele wymagań dla serwera autoryzacji OAuth nie ma zastosowania.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **10.6.1** | Zweryfikuj, że dostawca OpenID zezwala wyłącznie na wartości 'code', 'ciba', 'id_token' lub 'id_token code' dla trybu odpowiedzi. Zwróć uwagę, że 'code' jest preferowane względem 'id_token code' (przepływ hybrydowy OIDC), a 'token' (jakikolwiek przepływ Implicit) nie może być używany. | 2 |
| **10.6.2** | Zweryfikuj, że dostawca OpenID ogranicza ryzyko odmowy usługi poprzez wymuszone wylogowanie — uzyskując jawne potwierdzenie od użytkownika końcowego lub, jeśli występują, walidując parametry żądania wylogowania (zainicjowanego przez stronę ufającą), takie jak 'id_token_hint'. | 2 |

## V10.7 Zarządzanie zgodami

Te wymagania obejmują weryfikację zgody użytkownika przez serwer autoryzacji. Bez właściwej weryfikacji zgody użytkownika złośliwy aktor może uzyskać uprawnienia w imieniu użytkownika poprzez podszywanie się lub socjotechnikę.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **10.7.1** | Zweryfikuj, że serwer autoryzacji zapewnia, iż użytkownik wyraża zgodę na każde żądanie autoryzacji. Jeśli tożsamości klienta nie można zapewnić, serwer autoryzacji musi zawsze jawnie prosić użytkownika o zgodę. | 2 |
| **10.7.2** | Zweryfikuj, że gdy serwer autoryzacji prosi użytkownika o zgodę, przedstawia wystarczające i jasne informacje o tym, czego zgoda dotyczy. Tam, gdzie ma to zastosowanie, powinno to obejmować charakter żądanych autoryzacji (zwykle na podstawie zakresu, serwera zasobów, szczegółów autoryzacji Rich Authorization Requests (RAR)), tożsamość autoryzowanej aplikacji oraz czas życia tych autoryzacji. | 2 |
| **10.7.3** | Zweryfikuj, że użytkownik może przeglądać, modyfikować i odwoływać zgody, których udzielił za pośrednictwem serwera autoryzacji. | 2 |

## Źródła

Więcej informacji o OAuth można znaleźć pod adresami:

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

Dla wymagań ASVS związanych z OAuth wykorzystywane są następujące RFC — opublikowane oraz w statusie draft:

* [RFC6749 The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
* [RFC6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)
* [RFC6819 OAuth 2.0 Threat Model and Security Considerations](https://datatracker.ietf.org/doc/html/rfc6819)
* [RFC7636 Proof Key for Code Exchange by OAuth Public Clients](https://datatracker.ietf.org/doc/html/rfc7636)
* [RFC7591 OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591)
* [RFC8628 OAuth 2.0 Device Authorization Grant](https://datatracker.ietf.org/doc/html/rfc8628)
* [RFC8707 Resource Indicators for OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc8707)
* [RFC9068 JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
* [RFC9126 OAuth 2.0 Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126)
* [RFC9207 OAuth 2.0 Authorization Server Issuer Identification](https://datatracker.ietf.org/doc/html/rfc9207)
* [RFC9396 OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)
* [RFC9449 OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)
* [RFC9700 Best Current Practice for OAuth 2.0 Security](https://datatracker.ietf.org/doc/html/rfc9700)
* [draft OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)<!-- recheck on release -->
* [draft The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12)<!-- recheck on release -->

Więcej informacji o OpenID Connect można znaleźć pod adresami:

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
