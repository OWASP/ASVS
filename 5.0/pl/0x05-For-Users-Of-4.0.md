# Zmiany względem wersji 4.x

## Wprowadzenie

Użytkownikom zaznajomionym z wersją 4.x standardu może pomóc przegląd kluczowych zmian wprowadzonych w wersji 5.0, obejmujących treść, zakres oraz filozofię leżącą u podstaw standardu.

Z 286 wymagań wersji 4.0.3 jedynie 11 pozostało bez zmian, a 15 przeszło drobne korekty gramatyczne niezmieniające ich znaczenia. Łącznie 109 wymagań (38%) nie funkcjonuje już w wersji 5.0 jako odrębne wymagania — 50 zostało po prostu usuniętych, 28 usunięto jako duplikaty, a 31 scalono z innymi wymaganiami. Pozostałe zostały w jakiś sposób zrewidowane. Nawet wymagania, których treść nie uległa istotnej zmianie, mają inne identyfikatory ze względu na zmianę kolejności lub restrukturyzację.

Aby ułatwić przejście na wersję 5.0, udostępniono dokumenty mapujące, które pomagają prześledzić, jak wymagania wersji 4.x odpowiadają wymaganiom wersji 5.0. Mapowania te nie są powiązane z wersjonowaniem wydań i mogą być w razie potrzeby aktualizowane lub doprecyzowywane.

## Filozofia wymagań

### Zakres i ukierunkowanie

Wersja 4.x zawierała wymagania, które nie mieściły się w zamierzonym zakresie standardu — zostały one usunięte. Wykluczono również wymagania, które nie spełniały kryteriów zakresu wersji 5.0 lub nie były weryfikowalne.

### Nacisk na cele bezpieczeństwa zamiast mechanizmów

W wersji 4.x wiele wymagań koncentrowało się na konkretnych mechanizmach, a nie na leżących u ich podstaw celach bezpieczeństwa. W wersji 5.0 wymagania skupiają się na celach bezpieczeństwa, przywołując konkretne mechanizmy tylko wtedy, gdy stanowią jedyne praktyczne rozwiązanie, albo podając je jako przykłady lub wskazówki uzupełniające.

Podejście to uwzględnia fakt, że dany cel bezpieczeństwa można osiągnąć wieloma metodami, i pozwala uniknąć zbędnej nakazowości, która mogłaby ograniczać elastyczność organizacji.

Dodatkowo wymagania dotyczące tego samego problemu bezpieczeństwa zostały tam, gdzie było to zasadne, skonsolidowane.

### Udokumentowane decyzje dotyczące bezpieczeństwa

Choć koncepcja udokumentowanych decyzji dotyczących bezpieczeństwa może wydawać się w wersji 5.0 nowa, stanowi ona ewolucję wcześniejszych wymagań wersji 4.0 związanych ze stosowaniem polityk i modelowaniem zagrożeń. Wcześniej niektóre wymagania w sposób dorozumiany wymagały analizy niezbędnej do wdrożenia mechanizmów bezpieczeństwa, na przykład określenia dozwolonych połączeń sieciowych.

Aby zapewnić dostępność informacji niezbędnych do implementacji i weryfikacji, oczekiwania te są teraz jawnie zdefiniowane jako wymagania dotyczące dokumentacji — dzięki czemu są jasne, wykonalne i weryfikowalne.

## Zmiany strukturalne i nowe rozdziały

Kilka rozdziałów wersji 5.0 wprowadza zupełnie nową treść:

* OAuth i OIDC — ze względu na powszechne przyjęcie tych protokołów do delegowania dostępu i jednokrotnego logowania dodano dedykowane wymagania obejmujące różnorodne scenariusze, z jakimi mogą zetknąć się programiści. Obszar ten może z czasem przekształcić się w samodzielny standard, podobnie jak potraktowano wymagania dotyczące urządzeń mobilnych i IoT w poprzednich wersjach.
* WebRTC — wraz ze wzrostem popularności tej technologii jej specyficzne kwestie i wyzwania bezpieczeństwa są teraz omawiane w dedykowanej sekcji.

Dołożono również starań, aby rozdziały i sekcje były zorganizowane wokół spójnych zestawów powiązanych wymagań.

Ta restrukturyzacja doprowadziła do powstania dodatkowych rozdziałów:

* Tokeny samowystarczalne — wcześniej zgrupowane w ramach zarządzania sesją, obecnie są uznawane za odrębny mechanizm i fundament komunikacji bezstanowej (np. w OAuth i OIDC). Ze względu na ich specyficzne implikacje dla bezpieczeństwa poświęcono im dedykowany rozdział, wprowadzając w wersji 5.x kilka nowych wymagań.
* Bezpieczeństwo frontendu webowego — wraz z rosnącą złożonością aplikacji przeglądarkowych i upowszechnieniem architektur opartych wyłącznie na API wymagania dotyczące bezpieczeństwa frontendu zostały wydzielone do osobnego rozdziału.
* Bezpieczne kodowanie i architektura — zgrupowano tu nowe wymagania dotyczące ogólnych praktyk bezpieczeństwa, które nie pasowały do istniejących rozdziałów.

Pozostałe zmiany organizacyjne w wersji 5.0 wprowadzono w celu doprecyzowania intencji. Przykładowo wymagania dotyczące walidacji danych wejściowych przeniesiono do logiki biznesowej — co odzwierciedla ich rolę w egzekwowaniu reguł biznesowych — zamiast grupować je z sanityzacją i kodowaniem.

Dawny rozdział V1 Architektura został usunięty. Jego początkowa sekcja zawierała wymagania wykraczające poza zakres standardu, a kolejne sekcje rozdzielono pomiędzy właściwe rozdziały, usuwając duplikaty i doprecyzowując wymagania tam, gdzie było to konieczne.

## Usunięcie bezpośrednich mapowań do innych standardów

Bezpośrednie mapowania do innych standardów zostały usunięte z głównej części standardu. Celem jest przygotowanie mapowania z projektem OWASP Common Requirement Enumeration (CRE), który z kolei powiąże ASVS z szeregiem projektów OWASP i standardów zewnętrznych.

Bezpośrednie mapowania do CWE i NIST nie są już utrzymywane, co wyjaśniono poniżej.

### Ograniczenie powiązania z wytycznymi NIST Digital Identity Guidelines

Wytyczne NIST [Digital Identity Guidelines (SP 800-63)](https://pages.nist.gov/800-63-3/) od dawna służą jako punkt odniesienia dla mechanizmów uwierzytelniania i autoryzacji. W wersji 4.x niektóre rozdziały były ściśle dopasowane do struktury i terminologii NIST.

Choć wytyczne te pozostają ważnym punktem odniesienia, ścisłe dopasowanie rodziło trudności, w tym stosowanie mniej rozpoznawalnej terminologii, powielanie podobnych wymagań oraz niekompletne mapowania. Wersja 5.0 odchodzi od tego podejścia na rzecz większej przejrzystości i adekwatności.

### Odejście od Common Weakness Enumeration (CWE)

[Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) dostarcza użytecznej taksonomii słabości bezpieczeństwa oprogramowania. Jednak trudności takie jak istnienie CWE będących wyłącznie kategoriami, problemy z przypisaniem wymagania do pojedynczego CWE oraz obecność nieprecyzyjnych mapowań w wersji 4.x doprowadziły do decyzji o zaprzestaniu bezpośrednich mapowań CWE w wersji 5.0.

## Nowe podejście do definicji poziomów

Wersja 4.x opisywała poziomy jako L1 („Minimalny”), L2 („Standardowy”) i L3 („Zaawansowany”), sugerując, że wszystkie aplikacje przetwarzające dane wrażliwe powinny spełniać co najmniej L2.

Wersja 5.0 rozwiązuje kilka problemów związanych z tym podejściem, które opisano w kolejnych akapitach.

Od strony praktycznej: podczas gdy wersja 4.x używała symboli zaznaczenia jako wskaźników poziomu, wersja 5.x stosuje prostą liczbę we wszystkich formatach standardu, w tym Markdown, PDF, DOCX, CSV, JSON i XML. Dla zachowania zgodności wstecznej generowane są również starsze warianty plików CSV, JSON i XML, które nadal używają symboli zaznaczenia.

### Łatwiejszy poziom wejściowy

Opinie użytkowników wskazywały, że duża liczba wymagań poziomu 1 (~120) w połączeniu z określeniem go jako poziomu „minimalnego”, niewystarczającego dla większości aplikacji, zniechęcała do przyjęcia standardu. Wersja 5.0 obniża ten próg, definiując poziom 1 przede wszystkim wokół wymagań pierwszej warstwy obrony, co przekłada się na jaśniejsze i mniej liczne wymagania na tym poziomie. Ujmując to liczbowo: w wersji 4.0.3 istniało 128 wymagań L1 na łącznie 278 wymagań, co stanowiło 46%. W wersji 5.0.0 jest 70 wymagań L1 na łącznie 345 wymagań, co stanowi 20%.

### Złudzenie testowalności

Kluczowym czynnikiem doboru mechanizmów do poziomu 1 w wersji 4.x była ich przydatność do oceny w drodze zewnętrznych testów penetracyjnych „czarnoskrzynkowych”. Podejście to nie było jednak w pełni zgodne z przeznaczeniem poziomu 1 jako minimalnego zestawu mechanizmów bezpieczeństwa. Część użytkowników uważała, że poziom 1 nie wystarcza do zabezpieczenia aplikacji, inni z kolei uznawali go za zbyt trudny do przetestowania.

Opieranie się na testowalności jako kryterium jest zarówno względne, jak i miejscami mylące. To, że wymaganie jest testowalne, nie gwarantuje, że można je przetestować w sposób zautomatyzowany lub prosty. Co więcej, wymagania najłatwiejsze do przetestowania nie zawsze mają największy wpływ na bezpieczeństwo ani nie są najprostsze do wdrożenia.

W związku z tym w wersji 5.0 decyzje o poziomach podejmowano przede wszystkim na podstawie redukcji ryzyka, mając również na uwadze nakład pracy potrzebny do wdrożenia.

### Nie tylko kwestia ryzyka

Stosowanie nakazowych, opartych na ryzyku poziomów, które narzucają określony poziom pewnym aplikacjom, okazało się nadmiernie sztywne. W praktyce priorytetyzacja i wdrażanie mechanizmów bezpieczeństwa zależą od wielu czynników, obejmujących zarówno redukcję ryzyka, jak i nakład pracy wymagany do implementacji.

Dlatego zachęca się organizacje, aby dążyły do poziomu, który w ich ocenie powinny osiągnąć, biorąc pod uwagę własną dojrzałość oraz przekaz, jaki chcą kierować do swoich użytkowników.
