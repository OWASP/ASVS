# V13 Konfiguracja

## Cel kontrolny

Domyślna konfiguracja aplikacji musi być bezpieczna do użytku w Internecie.

Niniejszy rozdział zawiera wytyczne dotyczące różnych konfiguracji niezbędnych do osiągnięcia tego celu, w tym stosowanych na etapie wytwarzania, budowania i wdrażania.

Omawiane tematy obejmują zapobieganie wyciekom danych, bezpieczne zarządzanie komunikacją między komponentami oraz ochronę sekretów.

## V13.1 Dokumentacja konfiguracji

Ta sekcja przedstawia wymagania dokumentacyjne dotyczące sposobu, w jaki aplikacja komunikuje się z usługami wewnętrznymi i zewnętrznymi, a także technik zapobiegania utracie dostępności wskutek niedostępności usług. Obejmuje również dokumentację związaną z sekretami.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **13.1.1** | Zweryfikuj, że wszystkie potrzeby komunikacyjne aplikacji są udokumentowane. Musi to obejmować usługi zewnętrzne, na których polega aplikacja, oraz przypadki, w których użytkownik końcowy może wskazać zewnętrzną lokalizację, z którą aplikacja następnie się połączy. | 2 |
| **13.1.2** | Zweryfikuj, że dla każdej usługi, z której korzysta aplikacja, dokumentacja definiuje maksymalną liczbę równoczesnych połączeń (np. limity puli połączeń) oraz zachowanie aplikacji po osiągnięciu tego limitu, w tym wszelkie mechanizmy awaryjne lub naprawcze, aby zapobiec warunkom odmowy usługi. | 3 |
| **13.1.3** | Zweryfikuj, że dokumentacja aplikacji definiuje strategie zarządzania zasobami dla każdego zewnętrznego systemu lub usługi, z których korzysta (np. bazy danych, uchwyty plików, wątki, połączenia HTTP). Powinno to obejmować procedury zwalniania zasobów, ustawienia limitów czasu, obsługę awarii oraz — tam, gdzie zaimplementowano logikę ponawiania — określenie limitów ponowień, opóźnień i algorytmów back-off. Dla synchronicznych operacji żądanie–odpowiedź HTTP powinna nakazywać krótkie limity czasu oraz wyłączenie ponowień albo ich ścisłe ograniczenie, aby zapobiec kaskadowym opóźnieniom i wyczerpaniu zasobów. | 3 |
| **13.1.4** | Zweryfikuj, że dokumentacja aplikacji definiuje sekrety krytyczne dla bezpieczeństwa aplikacji oraz harmonogram ich rotacji, na podstawie modelu zagrożeń organizacji i wymagań biznesowych. | 3 |

## V13.2 Konfiguracja komunikacji backendowej

Aplikacje współpracują z wieloma usługami, w tym API, bazami danych i innymi komponentami. Mogą one być uznawane za wewnętrzne dla aplikacji, lecz nieobjęte jej standardowymi mechanizmami kontroli dostępu, albo mogą być całkowicie zewnętrzne. W obu przypadkach konieczne jest skonfigurowanie aplikacji do bezpiecznej współpracy z tymi komponentami oraz — jeśli to wymagane — ochrona tej konfiguracji.

Uwaga: rozdział „Bezpieczna komunikacja” zawiera wytyczne dotyczące szyfrowania w tranzycie.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **13.2.1** | Zweryfikuj, że komunikacja między backendowymi komponentami aplikacji, które nie wspierają standardowego mechanizmu sesji użytkownika aplikacji — w tym API, oprogramowaniem pośredniczącym i warstwami danych — jest uwierzytelniana. Uwierzytelnianie musi wykorzystywać indywidualne konta usługowe, tokeny krótkoterminowe lub uwierzytelnianie oparte na certyfikatach, a nie niezmienne poświadczenia, takie jak hasła, klucze API czy konta współdzielone z dostępem uprzywilejowanym. | 2 |
| **13.2.2** | Zweryfikuj, że komunikacja między backendowymi komponentami aplikacji — w tym lokalnymi usługami lub usługami systemu operacyjnego, API, oprogramowaniem pośredniczącym i warstwami danych — odbywa się z użyciem kont o najmniejszych niezbędnych uprawnieniach. | 2 |
| **13.2.3** | Zweryfikuj, że jeśli do uwierzytelniania usługi musi być użyte poświadczenie, poświadczenie używane przez konsumenta nie jest poświadczeniem domyślnym (np. root/root lub admin/admin). | 2 |
| **13.2.4** | Zweryfikuj, że lista dozwolonych jest używana do zdefiniowania zewnętrznych zasobów lub systemów, z którymi aplikacja może się komunikować (np. dla żądań wychodzących, ładowania danych lub dostępu do plików). Lista ta może być zaimplementowana w warstwie aplikacji, na serwerze WWW, na zaporze albo jako kombinacja różnych warstw. | 2 |
| **13.2.5** | Zweryfikuj, że serwer WWW lub serwer aplikacyjny jest skonfigurowany z listą dozwolonych zasobów lub systemów, do których serwer może wysyłać żądania albo z których może ładować dane lub pliki. | 2 |
| **13.2.6** | Zweryfikuj, że tam, gdzie aplikacja łączy się z odrębnymi usługami, przestrzega udokumentowanej konfiguracji dla każdego połączenia — takiej jak maksymalna liczba połączeń równoległych, zachowanie po osiągnięciu maksymalnej dozwolonej liczby połączeń, limity czasu połączeń i strategie ponawiania. | 3 |

## V13.3 Zarządzanie sekretami

Zarządzanie sekretami to kluczowe zadanie konfiguracyjne zapewniające ochronę danych używanych w aplikacji. Szczegółowe wymagania dotyczące kryptografii znajdują się w rozdziale „Kryptografia”, natomiast ta sekcja koncentruje się na aspektach zarządzania sekretami i ich obsługi.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **13.3.1** | Zweryfikuj, że do bezpiecznego tworzenia, przechowywania, kontroli dostępu i niszczenia sekretów backendowych używane jest rozwiązanie do zarządzania sekretami, takie jak skarbiec kluczy (key vault). Sekrety mogą obejmować hasła, materiał klucza, integracje z bazami danych i systemami stron trzecich, klucze i ziarna tokenów opartych na czasie, inne sekrety wewnętrzne oraz klucze API. Sekrety nie mogą znajdować się w kodzie źródłowym aplikacji ani w artefaktach builda. Dla aplikacji L3 musi to być rozwiązanie wsparte sprzętowo, takie jak HSM. | 2 |
| **13.3.2** | Zweryfikuj, że dostęp do zasobów sekretnych jest zgodny z zasadą najmniejszych uprawnień. | 2 |
| **13.3.3** | Zweryfikuj, że wszystkie operacje kryptograficzne są wykonywane z użyciem izolowanego modułu bezpieczeństwa (takiego jak skarbiec lub sprzętowy moduł bezpieczeństwa), aby bezpiecznie zarządzać materiałem klucza i chronić go przed ekspozycją poza modułem bezpieczeństwa. | 3 |
| **13.3.4** | Zweryfikuj, że sekrety są skonfigurowane tak, aby wygasały i podlegały rotacji zgodnie z dokumentacją aplikacji. | 3 |

## V13.4 Niezamierzony wyciek informacji

Konfiguracje produkcyjne powinny być utwardzone tak, aby nie ujawniać zbędnych danych. Wiele z tych problemów rzadko jest oceniane jako istotne ryzyka, ale często są one łączone w łańcuchy z innymi podatnościami. Jeśli problemy te nie występują domyślnie, poprzeczka dla ataku na aplikację zostaje podniesiona.

Przykładowo ukrycie wersji komponentów serwerowych nie eliminuje potrzeby łatania wszystkich komponentów, a wyłączenie listowania katalogów nie usuwa potrzeby stosowania kontroli autoryzacji ani trzymania plików poza folderem publicznym — ale podnosi poprzeczkę.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **13.4.1** | Zweryfikuj, że aplikacja jest wdrażana albo bez jakichkolwiek metadanych kontroli wersji, w tym folderów .git lub .svn, albo w sposób uniemożliwiający dostęp do tych folderów zarówno z zewnątrz, jak i samej aplikacji. | 1 |
| **13.4.2** | Zweryfikuj, że tryby debugowania są wyłączone dla wszystkich komponentów w środowiskach produkcyjnych, aby zapobiec ekspozycji funkcji debugowania i wyciekowi informacji. | 2 |
| **13.4.3** | Zweryfikuj, że serwery WWW nie udostępniają klientom listowania katalogów, chyba że jest to wyraźnie zamierzone. | 2 |
| **13.4.4** | Zweryfikuj, że metoda HTTP TRACE nie jest wspierana w środowiskach produkcyjnych, aby uniknąć potencjalnego wycieku informacji. | 2 |
| **13.4.5** | Zweryfikuj, że dokumentacja (np. wewnętrznych API) oraz endpointy monitorowania nie są eksponowane, chyba że jest to wyraźnie zamierzone. | 2 |
| **13.4.6** | Zweryfikuj, że aplikacja nie ujawnia szczegółowych informacji o wersjach komponentów backendowych. | 3 |
| **13.4.7** | Zweryfikuj, że warstwa webowa jest skonfigurowana tak, aby serwować wyłącznie pliki o określonych rozszerzeniach, aby zapobiec niezamierzonemu wyciekowi informacji, konfiguracji i kodu źródłowego. | 3 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP Web Security Testing Guide: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing)
