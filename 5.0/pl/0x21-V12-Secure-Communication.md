# V12 Bezpieczna komunikacja

## Cel kontrolny

Niniejszy rozdział zawiera wymagania dotyczące konkretnych mechanizmów, które powinny chronić dane w tranzycie — zarówno między klientem użytkownika końcowego a usługą backendową, jak i między usługami wewnętrznymi i backendowymi.

Ogólne koncepcje promowane przez ten rozdział obejmują:

* Zapewnienie, że komunikacja jest szyfrowana na zewnątrz, a najlepiej również wewnętrznie.
* Konfigurowanie mechanizmów szyfrowania zgodnie z najnowszymi wytycznymi, w tym preferowanymi algorytmami i szyframi.
* Stosowanie podpisanych certyfikatów, aby komunikacja nie była przechwytywana przez strony nieuprawnione.

Oprócz przedstawienia ogólnych zasad i najlepszych praktyk ASVS dostarcza również bardziej szczegółowych informacji technicznych o sile kryptograficznej w Załączniku C — Standardy kryptograficzne.

## V12.1 Ogólne wytyczne bezpieczeństwa TLS

Ta sekcja zawiera wstępne wskazówki dotyczące zabezpieczania komunikacji TLS. Do bieżącego przeglądu konfiguracji TLS należy używać aktualnych narzędzi.

Choć stosowanie certyfikatów TLS typu wildcard nie jest samo w sobie niebezpieczne, kompromitacja certyfikatu wdrożonego we wszystkich posiadanych środowiskach (np. produkcyjnym, staging, deweloperskim i testowym) może prowadzić do kompromitacji poziomu bezpieczeństwa aplikacji, które go używają. Jeśli to możliwe, należy stosować właściwą ochronę, zarządzanie oraz odrębne certyfikaty TLS w różnych środowiskach.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **12.1.1** | Zweryfikuj, że włączone są wyłącznie najnowsze zalecane wersje protokołu TLS, takie jak TLS 1.2 i TLS 1.3. Najnowsza wersja protokołu TLS musi być opcją preferowaną. | 1 |
| **12.1.2** | Zweryfikuj, że włączone są wyłącznie zalecane zestawy szyfrów (cipher suites), z najsilniejszymi zestawami ustawionymi jako preferowane. Aplikacje L3 mogą wspierać wyłącznie zestawy szyfrów zapewniające utajnianie z wyprzedzeniem (forward secrecy). | 2 |
| **12.1.3** | Zweryfikuj, że aplikacja waliduje, iż certyfikaty klienckie mTLS są zaufane, zanim użyje tożsamości z certyfikatu do uwierzytelniania lub autoryzacji. | 2 |
| **12.1.4** | Zweryfikuj, że włączone i skonfigurowane jest właściwe odwoływanie certyfikatów, takie jak Online Certificate Status Protocol (OCSP) Stapling. | 3 |
| **12.1.5** | Zweryfikuj, że w ustawieniach TLS aplikacji włączone jest Encrypted Client Hello (ECH), aby zapobiec ujawnieniu wrażliwych metadanych, takich jak Server Name Indication (SNI), podczas procesu uzgadniania TLS. | 3 |

## V12.2 Komunikacja HTTPS z usługami skierowanymi na zewnątrz

Zapewnij, że cały ruch HTTP do usług skierowanych na zewnątrz, które udostępnia aplikacja, jest wysyłany w postaci zaszyfrowanej, z użyciem publicznie zaufanych certyfikatów.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **12.2.1** | Zweryfikuj, że TLS jest używany dla całej łączności między klientem a skierowanymi na zewnątrz usługami opartymi na HTTP i nie następuje powrót do komunikacji niebezpiecznej lub nieszyfrowanej. | 1 |
| **12.2.2** | Zweryfikuj, że usługi skierowane na zewnątrz używają publicznie zaufanych certyfikatów TLS. | 1 |

## V12.3 Ogólne bezpieczeństwo komunikacji między usługami

Komunikacja serwerowa (zarówno wewnętrzna, jak i zewnętrzna) to więcej niż tylko HTTP. Połączenia do i z innych systemów również muszą być bezpieczne — najlepiej z użyciem TLS.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **12.3.1** | Zweryfikuj, że szyfrowany protokół, taki jak TLS, jest używany dla wszystkich połączeń przychodzących i wychodzących do i z aplikacji, w tym systemów monitorowania, narzędzi zarządzania, zdalnego dostępu i SSH, oprogramowania pośredniczącego, baz danych, mainframe'ów, systemów partnerskich lub zewnętrznych API. Serwer nie może wracać do protokołów niebezpiecznych lub nieszyfrowanych. | 2 |
| **12.3.2** | Zweryfikuj, że klienci TLS walidują otrzymane certyfikaty przed rozpoczęciem komunikacji z serwerem TLS. | 2 |
| **12.3.3** | Zweryfikuj, że TLS lub inny odpowiedni mechanizm szyfrowania transportu jest używany dla całej łączności między wewnętrznymi usługami opartymi na HTTP w ramach aplikacji i nie następuje powrót do komunikacji niebezpiecznej lub nieszyfrowanej. | 2 |
| **12.3.4** | Zweryfikuj, że połączenia TLS między usługami wewnętrznymi używają zaufanych certyfikatów. Tam, gdzie stosowane są certyfikaty generowane wewnętrznie lub samopodpisane, usługa konsumująca musi być skonfigurowana tak, aby ufać wyłącznie konkretnym wewnętrznym urzędom certyfikacji (CA) i konkretnym certyfikatom samopodpisanym. | 2 |
| **12.3.5** | Zweryfikuj, że usługi komunikujące się wewnętrznie w ramach systemu (komunikacja intra-service) używają silnego uwierzytelniania, aby każdy endpoint był zweryfikowany. Muszą być stosowane silne metody uwierzytelniania, takie jak uwierzytelnianie klienta TLS, zapewniające tożsamość z użyciem infrastruktury klucza publicznego i mechanizmów odpornych na ataki powtórzeniowe. Dla architektur mikroserwisowych rozważ użycie service mesh w celu uproszczenia zarządzania certyfikatami i podniesienia poziomu bezpieczeństwa. | 3 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP - Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
* [Przewodnik Mozilli po konfiguracji TLS po stronie serwera](https://wiki.mozilla.org/Security/Server_Side_TLS)
* [Narzędzie Mozilli do generowania sprawdzonych konfiguracji TLS](https://ssl-config.mozilla.org/).
* [O-Saft — projekt OWASP do walidacji konfiguracji TLS](https://owasp.org/www-project-o-saft/)
