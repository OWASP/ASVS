# Czym jest ASVS?

Application Security Verification Standard (ASVS) definiuje wymagania bezpieczeństwa dla aplikacji internetowych i usług sieciowych. Stanowi cenne źródło wiedzy dla każdego, kto chce projektować, tworzyć i utrzymywać bezpieczne aplikacje lub oceniać ich bezpieczeństwo.

Niniejszy rozdział przedstawia kluczowe aspekty korzystania z ASVS, w tym jego zakres, strukturę poziomów opartych na priorytetach oraz główne przypadki użycia standardu.

## Zakres ASVS

Zakres ASVS wyznacza jego nazwa: Aplikacja, Bezpieczeństwo, Weryfikacja i Standard. Określa ona, które wymagania są uwzględnione, a które wykluczone — a nadrzędnym celem jest wskazanie zasad bezpieczeństwa, które muszą zostać spełnione. Zakres obejmuje również wymagania dotyczące dokumentacji, stanowiące fundament dla wymagań wdrożeniowych.

Dla atakujących pojęcie zakresu nie istnieje. Dlatego wymagania ASVS należy rozpatrywać łącznie z wytycznymi dotyczącymi innych aspektów cyklu życia aplikacji, w tym procesów CI/CD, hostingu oraz działań operacyjnych.

### Aplikacja

ASVS definiuje „aplikację” jako tworzony produkt programowy, w który muszą zostać wbudowane mechanizmy bezpieczeństwa. ASVS nie narzuca działań w ramach cyklu wytwarzania oprogramowania ani nie dyktuje, jak aplikacja ma być budowana w potoku CI/CD; zamiast tego określa efekty w zakresie bezpieczeństwa, które muszą zostać osiągnięte w samym produkcie.

Komponenty, które obsługują, modyfikują lub walidują ruch HTTP — takie jak zapory aplikacji internetowych (WAF), moduły równoważenia obciążenia czy serwery proxy — mogą być traktowane jako część aplikacji w tych konkretnych zastosowaniach, ponieważ niektóre mechanizmy bezpieczeństwa zależą bezpośrednio od nich lub mogą być przez nie realizowane. Komponenty te należy uwzględnić przy wymaganiach dotyczących odpowiedzi buforowanych w pamięci podręcznej, ograniczania częstotliwości żądań lub ograniczania połączeń przychodzących i wychodzących na podstawie źródła i celu.

Z drugiej strony ASVS zasadniczo wyklucza wymagania, które nie odnoszą się bezpośrednio do aplikacji lub których konfiguracja leży poza jej odpowiedzialnością. Przykładowo kwestie DNS są zazwyczaj zarządzane przez odrębny zespół lub funkcję w organizacji.

Podobnie — choć aplikacja odpowiada za sposób, w jaki przetwarza dane wejściowe i generuje dane wyjściowe — jeśli zewnętrzny proces wchodzi w interakcję z aplikacją lub jej danymi, pozostaje on poza zakresem ASVS. Na przykład tworzenie kopii zapasowych aplikacji lub jej danych jest zwykle zadaniem zewnętrznego procesu i nie jest kontrolowane przez aplikację ani jej twórców.

### Bezpieczeństwo

Każde wymaganie musi mieć wykazywalny wpływ na bezpieczeństwo. Brak danego wymagania musi skutkować mniej bezpieczną aplikacją, a jego wdrożenie musi zmniejszać prawdopodobieństwo lub skutki ryzyka bezpieczeństwa.

Wszystkie pozostałe kwestie, takie jak aspekty funkcjonalne, styl kodu czy wymagania wynikające z polityk, pozostają poza zakresem.

### Weryfikacja

Wymaganie musi być weryfikowalne, a weryfikacja musi kończyć się decyzją „spełnione” albo „niespełnione”.

### Standard

ASVS został zaprojektowany jako zbiór wymagań bezpieczeństwa, których wdrożenie oznacza zgodność ze standardem. Oznacza to, że wymagania ograniczają się do zdefiniowania celu bezpieczeństwa, który należy osiągnąć. Pozostałe powiązane informacje mogą być budowane na bazie ASVS lub powiązane z nim poprzez mapowania.

W szczególności — OWASP prowadzi wiele projektów, a ASVS celowo unika pokrywania się z treścią innych z nich. Przykładowo programista może zapytać: „jak wdrożyć dane wymaganie w mojej konkretnej technologii lub środowisku” — na to odpowiada projekt Cheat Sheet Series. Weryfikator może zapytać: „jak przetestować to wymaganie w tym środowisku” — na to odpowiada projekt Web Security Testing Guide.

Choć ASVS nie jest przeznaczony wyłącznie dla ekspertów ds. bezpieczeństwa, zakłada, że czytelnik dysponuje wiedzą techniczną pozwalającą zrozumieć treść lub umiejętnością samodzielnego zgłębienia poszczególnych zagadnień.

### Wymaganie

Słowo „wymaganie” jest używane w ASVS w ścisłym znaczeniu — opisuje to, co musi zostać osiągnięte, aby je spełnić. ASVS zawiera wyłącznie wymagania (must) i nie zawiera zaleceń (should) jako głównego warunku.

Innymi słowy, zalecenia — niezależnie od tego, czy stanowią tylko jedną z wielu możliwych opcji rozwiązania problemu, czy dotyczą stylu kodu — nie spełniają definicji wymagania.

Wymagania ASVS mają odnosić się do konkretnych zasad bezpieczeństwa, nie będąc przy tym nadmiernie związane z konkretną implementacją czy technologią, a jednocześnie samodzielnie wyjaśniać, dlaczego istnieją. Oznacza to również, że wymagania nie są budowane wokół określonej metody weryfikacji ani implementacji.

### Udokumentowane decyzje dotyczące bezpieczeństwa

W bezpieczeństwie oprogramowania wczesne zaplanowanie projektu zabezpieczeń oraz mechanizmów, które zostaną użyte, prowadzi do spójniejszej i bardziej niezawodnej implementacji w gotowym produkcie lub funkcjonalności.

Ponadto w przypadku niektórych wymagań implementacja będzie złożona i silnie zależna od potrzeb konkretnej aplikacji. Typowe przykłady to uprawnienia, walidacja danych wejściowych oraz mechanizmy ochronne wokół różnych poziomów danych wrażliwych.

Aby to uwzględnić — zamiast ogólnikowych stwierdzeń w rodzaju „wszystkie dane muszą być szyfrowane” lub prób objęcia jednym wymaganiem każdego możliwego przypadku użycia — wprowadzono wymagania dotyczące dokumentacji, które nakazują udokumentowanie podejścia twórcy aplikacji do tego typu mechanizmów oraz ich konfiguracji. Dokumentację można następnie ocenić pod kątem adekwatności, a rzeczywistą implementację porównać z nią, aby sprawdzić, czy odpowiada oczekiwaniom.

Wymagania te służą udokumentowaniu decyzji, które organizacja tworząca aplikację podjęła w kwestii sposobu wdrożenia określonych wymagań bezpieczeństwa.

Wymagania dotyczące dokumentacji znajdują się zawsze w pierwszej sekcji rozdziału (choć nie każdy rozdział je zawiera) i zawsze mają powiązane wymaganie wdrożeniowe, zgodnie z którym udokumentowane decyzje powinny zostać faktycznie wprowadzone w życie. Chodzi o to, że weryfikacja istnienia dokumentacji oraz weryfikacja rzeczywistej implementacji to dwie odrębne czynności.

Za włączeniem tych wymagań stoją dwa kluczowe powody. Pierwszy: wymaganie bezpieczeństwa często wiąże się z egzekwowaniem reguł — np. jakie typy plików można przesyłać, jakie mechanizmy kontroli biznesowej powinny być egzekwowane, jakie znaki są dozwolone w danym polu. Reguły te będą różne dla każdej aplikacji, dlatego ASVS nie może ich odgórnie zdefiniować — nie pomoże tu także ściąga ani bardziej szczegółowa odpowiedź. Podobnie, bez udokumentowania tych decyzji nie będzie możliwa weryfikacja wymagań, które je wdrażają.

Drugi powód: w przypadku niektórych wymagań istotne jest pozostawienie zespołowi tworzącemu aplikację elastyczności w podejściu do konkretnych wyzwań bezpieczeństwa. Przykładowo we wcześniejszych wersjach ASVS reguły wygasania sesji były bardzo restrykcyjnie zdefiniowane. W praktyce wiele aplikacji — zwłaszcza konsumenckich — stosuje znacznie łagodniejsze reguły i woli wdrożyć w zamian inne mechanizmy ograniczające ryzyko. Wymagania dotyczące dokumentacji jawnie dopuszczają taką elastyczność.

Oczywiście nie oczekuje się, że decyzje te będą podejmowane i dokumentowane przez poszczególnych programistów — to organizacja jako całość powinna je podejmować i zadbać o ich zakomunikowanie programistom, którzy następnie będą ich przestrzegać.

Dostarczanie programistom specyfikacji i projektów nowych funkcji to standardowy element wytwarzania oprogramowania. Podobnie oczekuje się, że programiści będą korzystać ze wspólnych komponentów i mechanizmów interfejsu użytkownika, zamiast każdorazowo podejmować własne decyzje. Rozszerzenie tej praktyki na bezpieczeństwo nie powinno więc dziwić ani budzić kontrowersji.

Istnieje również elastyczność co do sposobu realizacji. Decyzje dotyczące bezpieczeństwa mogą zostać udokumentowane w postaci dokumentu, do którego programiści mają się odwoływać. Alternatywnie mogą zostać udokumentowane i zaimplementowane we wspólnej bibliotece kodu, z której wszyscy programiści mają obowiązek korzystać. W obu przypadkach osiągany jest pożądany rezultat.

## Poziomy weryfikacji bezpieczeństwa aplikacji

ASVS definiuje trzy poziomy weryfikacji bezpieczeństwa, z których każdy kolejny zwiększa głębokość i złożoność. Ogólnym założeniem jest, aby organizacje zaczynały od pierwszego poziomu, aby zająć się najbardziej krytycznymi kwestiami bezpieczeństwa, a następnie przechodziły na wyższe poziomy stosownie do potrzeb organizacji i aplikacji. W dokumencie oraz w treści wymagań poziomy mogą być oznaczane jako L1, L2 i L3.

Każdy poziom ASVS wskazuje wymagania bezpieczeństwa, których spełnienie jest konieczne do jego osiągnięcia, przy czym wymagania pozostałych, wyższych poziomów mają charakter zaleceń.

Aby uniknąć duplikowania wymagań lub wymagań, które na wyższych poziomach tracą aktualność, niektóre wymagania obowiązują na określonym poziomie, lecz na wyższych poziomach mają bardziej rygorystyczne warunki.

### Ocena poziomów

Poziomy zostały zdefiniowane w drodze opartej na priorytetach oceny każdego wymagania, bazującej na doświadczeniu we wdrażaniu i testowaniu wymagań bezpieczeństwa. Główny nacisk położono na porównanie redukcji ryzyka z nakładem pracy potrzebnym do wdrożenia wymagania. Kolejnym kluczowym czynnikiem było utrzymanie niskiego progu wejścia.

Redukcja ryzyka uwzględnia stopień, w jakim wymaganie obniża poziom ryzyka bezpieczeństwa w aplikacji, biorąc pod uwagę klasyczne czynniki wpływu: poufność, integralność i dostępność, a także to, czy dane wymaganie stanowi podstawową warstwę obrony, czy raczej element obrony w głąb.

Rygorystyczne dyskusje zarówno nad kryteriami, jak i nad decyzjami o przypisaniu poziomów doprowadziły do podziału, który powinien sprawdzać się w zdecydowanej większości przypadków — przy założeniu, że nie będzie on w 100% dopasowany do każdej sytuacji. Oznacza to, że w pewnych przypadkach organizacje mogą zdecydować się na wcześniejsze nadanie priorytetu wymaganiom z wyższego poziomu, kierując się własną, specyficzną oceną ryzyka.

Rodzaje wymagań na poszczególnych poziomach można scharakteryzować następująco.

### Poziom 1

Ten poziom zawiera minimalny zestaw wymagań, które należy rozważyć przy zabezpieczaniu aplikacji, i stanowi krytyczny punkt wyjścia. Obejmuje około 20% wymagań ASVS. Celem tego poziomu jest ograniczenie liczby wymagań do minimum, aby obniżyć próg wejścia.

Są to na ogół wymagania krytyczne lub podstawowe, stanowiące pierwszą warstwę obrony przed powszechnymi atakami, które do wykorzystania nie wymagają innych podatności ani warunków wstępnych.

Oprócz wymagań pierwszej warstwy obrony znajdują się tu wymagania, których znaczenie na wyższych poziomach maleje — na przykład te dotyczące haseł. Są one ważniejsze na poziomie 1, ponieważ od wyższych poziomów zaczynają obowiązywać wymagania dotyczące uwierzytelniania wieloskładnikowego.

Poziom 1 niekoniecznie da się zweryfikować testem penetracyjnym prowadzonym przez zewnętrznego testera bez dostępu do dokumentacji lub kodu (tzw. testowanie „czarnoskrzynkowe”), choć mniejsza liczba wymagań powinna ułatwić weryfikację.

### Poziom 2

Do tego poziomu bezpieczeństwa powinna dążyć większość aplikacji. Około 50% wymagań ASVS należy do poziomu L2, co oznacza, że aby osiągnąć zgodność z L2, aplikacja musi wdrożyć około 70% wymagań ASVS (wszystkie wymagania L1 i L2).

Wymagania te dotyczą na ogół rzadszych ataków lub bardziej złożonych zabezpieczeń przed atakami powszechnymi. Mogą nadal stanowić pierwszą warstwę obrony albo wymagać spełnienia określonych warunków wstępnych, aby atak mógł się powieść.

### Poziom 3

Ten poziom powinien być celem aplikacji, które chcą wykazać najwyższy poziom bezpieczeństwa. Obejmuje ostatnie ~30% wymagań niezbędnych do pełnej zgodności.

Wymagania w tej grupie to na ogół mechanizmy obrony w głąb lub inne przydatne, lecz trudne we wdrożeniu zabezpieczenia.

### Który poziom osiągnąć

Poziomy oparte na priorytetach mają odzwierciedlać dojrzałość organizacji i aplikacji w obszarze bezpieczeństwa aplikacji. ASVS nie wskazuje odgórnie, na jakim poziomie powinna znajdować się dana aplikacja — to organizacja powinna przeanalizować swoje ryzyka i zdecydować, do jakiego poziomu jej zdaniem powinna dążyć, w zależności od wrażliwości aplikacji oraz, rzecz jasna, oczekiwań jej użytkowników.

Przykładowo start-up na wczesnym etapie rozwoju, gromadzący jedynie ograniczoną ilość danych wrażliwych, może zdecydować się skupić na poziomie 1 jako początkowym celu bezpieczeństwa, natomiast bankowi trudno będzie uzasadnić przed klientami cokolwiek poniżej poziomu 3 dla aplikacji bankowości internetowej.

## Jak korzystać z ASVS

### Struktura ASVS

ASVS składa się łącznie z około 350 wymagań podzielonych na 17 rozdziałów, z których każdy dzieli się dalej na sekcje.

Celem podziału na rozdziały i sekcje jest ułatwienie wyboru lub odfiltrowania rozdziałów i sekcji w zależności od tego, co jest istotne dla danej aplikacji. Przykładowo dla API działającego w komunikacji maszyna–maszyna wymagania rozdziału V3 dotyczące frontendów webowych nie będą miały zastosowania. Jeśli aplikacja nie korzysta z OAuth ani WebRTC, te rozdziały również można pominąć.

### Strategia wydań

Wydania ASVS są numerowane według wzorca „Major.Minor.Patch” (główne.poboczne.poprawka), a numery informują, co zmieniło się w danym wydaniu. W wydaniu głównym zmienia się pierwsza liczba, w wydaniu pobocznym — druga, a w poprawce — trzecia.

* Wydanie główne — pełna reorganizacja; zmianie mogło ulec niemal wszystko, łącznie z numeracją wymagań. Konieczna będzie ponowna ocena zgodności (na przykład 4.0.3 -> 5.0.0).
* Wydanie poboczne — wymagania mogą zostać dodane lub usunięte, ale ogólna numeracja pozostaje bez zmian. Ponowna ocena zgodności będzie konieczna, lecz powinna być łatwiejsza (na przykład 5.0.0 -> 5.1.0).
* Poprawka — wymagania mogą zostać usunięte (na przykład jako duplikaty lub nieaktualne) lub złagodzone, ale aplikacja zgodna z poprzednim wydaniem będzie zgodna również z poprawką (na przykład 5.0.0 -> 5.0.1).

Powyższe odnosi się wyłącznie do wymagań ASVS. Zmiany w tekście towarzyszącym i pozostałych treściach, takich jak załączniki, nie będą traktowane jako zmiany łamiące zgodność wsteczną.

### Elastyczność ASVS

Kilka z opisanych wyżej mechanizmów — takich jak wymagania dotyczące dokumentacji czy system poziomów — pozwala korzystać z ASVS w sposób bardziej elastyczny i dopasowany do organizacji.

Dodatkowo zdecydowanie zachęca się organizacje do tworzenia własnych forków standardu, dostosowanych do organizacji lub domeny.

### Forkowanie ASVS

Organizacje mogą czerpać korzyści z przyjęcia ASVS, wybierając jeden z trzech poziomów lub tworząc fork dostosowany do własnej domeny, który koryguje wymagania odpowiednio do poziomu ryzyka aplikacji. Tego typu forki są mile widziane, pod warunkiem zachowania identyfikowalności — tak aby spełnienie wymagania 4.1.1 oznaczało to samo we wszystkich wersjach.

Najlepiej, aby każda organizacja stworzyła własną, dopasowaną wersję ASVS, pomijając nieistotne sekcje (np. GraphQL, WebSockets, SOAP — jeśli nie są używane). Punktem wyjścia forka powinien być poziom 1 ASVS, z przejściem na poziomy 2 lub 3 stosownie do ryzyka aplikacji.

### Jak przywoływać wymagania ASVS

Każde wymaganie ma identyfikator w formacie `<rozdział>.<sekcja>.<wymaganie>`, gdzie każdy element jest liczbą. Na przykład: `1.11.3`.

* Wartość `<rozdział>` odpowiada rozdziałowi, z którego pochodzi wymaganie; na przykład wszystkie wymagania `1.#.#` pochodzą z rozdziału „Kodowanie i sanityzacja”.
* Wartość `<sekcja>` odpowiada sekcji w obrębie tego rozdziału, w której znajduje się wymaganie; na przykład wszystkie wymagania `1.2.#` znajdują się w sekcji „Zapobieganie wstrzyknięciom” rozdziału „Kodowanie i sanityzacja”.
* Wartość `<wymaganie>` identyfikuje konkretne wymaganie w obrębie rozdziału i sekcji, na przykład `1.2.5`, które w wersji 5.0.0 niniejszego standardu brzmi:

> Zweryfikuj, że aplikacja chroni przed wstrzyknięciem poleceń systemu operacyjnego oraz że wywołania systemowe używają sparametryzowanych zapytań systemowych lub stosują kontekstowe kodowanie danych wyjściowych wiersza poleceń.

Ponieważ identyfikatory mogą się zmieniać między wersjami standardu, w innych dokumentach, raportach lub narzędziach zaleca się stosowanie formatu: `v<wersja>-<rozdział>.<sekcja>.<wymaganie>`, gdzie „wersja” to znacznik wersji ASVS. Na przykład `v5.0.0-1.2.5` oznaczałoby konkretnie piąte wymaganie w sekcji „Zapobieganie wstrzyknięciom” rozdziału „Kodowanie i sanityzacja” z wersji 5.0.0. (Można to podsumować jako `v<wersja>-<identyfikator_wymagania>`.)

Uwaga: litera `v` poprzedzająca numer wersji w tym formacie powinna być zawsze mała.

Jeśli identyfikatory są używane bez elementu `v<wersja>`, należy przyjąć, że odnoszą się do najnowszej wersji Application Security Verification Standard. W miarę rozwoju i zmian standardu staje się to problematyczne — dlatego autorzy tekstów i programiści powinni uwzględniać element wersji.

Listy wymagań ASVS są udostępniane w formatach CSV, JSON i innych, które mogą być przydatne do celów referencyjnych lub programistycznych.

## Przypadki użycia ASVS

ASVS może służyć do oceny bezpieczeństwa aplikacji — temat ten został szerzej omówiony w kolejnym rozdziale. Zidentyfikowano jednak także szereg innych potencjalnych zastosowań ASVS (lub jego forka).

### Jako szczegółowe wytyczne architektury bezpieczeństwa

Jednym z częstszych zastosowań Application Security Verification Standard jest wykorzystanie go jako źródła wiedzy przez architektów bezpieczeństwa. Zasobów opisujących, jak budować bezpieczną architekturę aplikacji, jest niewiele — zwłaszcza w odniesieniu do nowoczesnych aplikacji. ASVS może wypełnić te luki, pozwalając architektom bezpieczeństwa dobierać lepsze mechanizmy dla typowych problemów, takich jak wzorce ochrony danych czy strategie walidacji danych wejściowych. Szczególnie przydatne będą tu wymagania dotyczące architektury i dokumentacji.

### Jako specjalistyczny przewodnik bezpiecznego kodowania

ASVS może posłużyć jako podstawa do przygotowania przewodnika bezpiecznego kodowania na etapie wytwarzania aplikacji, pomagając programistom pamiętać o bezpieczeństwie podczas tworzenia oprogramowania. Choć ASVS może stanowić bazę, organizacje powinny przygotować własne, konkretne wytyczne — jasne i ujednolicone, najlepiej opracowane na podstawie wskazówek inżynierów lub architektów bezpieczeństwa. W rozwinięciu tej praktyki zachęca się organizacje, aby tam, gdzie to możliwe, przygotowywały zatwierdzone mechanizmy bezpieczeństwa i biblioteki, do których wytyczne będą się odwoływać i z których będą korzystać programiści.

### Jako przewodnik dla zautomatyzowanych testów jednostkowych i integracyjnych

ASVS został zaprojektowany tak, aby był wysoce testowalny. Niektóre weryfikacje będą miały charakter techniczny, podczas gdy inne wymagania (np. architektoniczne i dotyczące dokumentacji) mogą wymagać przeglądu dokumentacji lub architektury. Budując testy jednostkowe i integracyjne, które testują i fuzzują konkretne, istotne przypadki nadużyć powiązane z wymaganiami weryfikowalnymi środkami technicznymi, łatwiej będzie sprawdzać przy każdym buildzie, czy te mechanizmy działają poprawnie. Przykładowo do zestawu testów kontrolera logowania można dodać testy parametru nazwy użytkownika pod kątem typowych domyślnych nazw użytkowników, enumeracji kont, ataków siłowych, wstrzyknięć LDAP i SQL oraz XSS. Analogicznie test parametru hasła powinien obejmować typowe hasła, długość hasła, wstrzyknięcie bajtu null, usunięcie parametru, XSS i inne.

### Do szkoleń z bezpiecznego wytwarzania oprogramowania

ASVS może również służyć do zdefiniowania cech bezpiecznego oprogramowania. Wiele kursów „bezpiecznego kodowania” to w istocie kursy etycznego hakowania z lekką domieszką wskazówek programistycznych. Niekoniecznie pomaga to programistom pisać bezpieczniejszy kod. Zamiast tego kursy bezpiecznego wytwarzania oprogramowania mogą opierać się na ASVS, z silnym naciskiem na pozytywne mechanizmy w nim opisane — zamiast na listę dziesięciu negatywnych rzeczy, których robić nie należy. Struktura ASVS zapewnia też logiczny układ do omawiania kolejnych zagadnień przy zabezpieczaniu aplikacji.

### Jako ramy wspierające zakup bezpiecznego oprogramowania

ASVS doskonale sprawdza się jako ramy wspierające zakup bezpiecznego oprogramowania lub usług programistycznych na zamówienie. Kupujący może po prostu postawić wymóg, aby nabywane oprogramowanie zostało wytworzone zgodnie z poziomem X ASVS, i zażądać od sprzedawcy wykazania, że oprogramowanie ten poziom spełnia.

## Stosowanie ASVS w praktyce

Różne zagrożenia mają różne motywacje. Niektóre branże dysponują unikalnymi zasobami informacyjnymi i technologicznymi oraz podlegają specyficznym dla danej domeny wymogom zgodności regulacyjnej.

Zdecydowanie zachęca się organizacje, aby dogłębnie przeanalizowały swoją unikalną charakterystykę ryzyka wynikającą z natury prowadzonej działalności i na podstawie tego ryzyka oraz wymagań biznesowych określiły odpowiedni poziom ASVS.
