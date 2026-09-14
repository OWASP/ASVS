# Ocena i certyfikacja

## Stanowisko OWASP wobec certyfikacji ASVS i znaków zaufania

OWASP, jako neutralna wobec dostawców organizacja non-profit, nie certyfikuje żadnych dostawców, weryfikatorów ani oprogramowania. Żadne poświadczenie, znak zaufania ani certyfikat deklarujący zgodność z ASVS nie jest oficjalnie zatwierdzony przez OWASP, dlatego organizacje powinny zachować ostrożność wobec deklaracji certyfikacji ASVS składanych przez strony trzecie.

Organizacje mogą oferować usługi poświadczające, o ile nie twierdzą, że posiadają oficjalną certyfikację OWASP.

## Jak weryfikować zgodność z ASVS

ASVS celowo nie narzuca dokładnego sposobu weryfikacji zgodności na poziomie przewodnika testowania. Warto jednak podkreślić kilka kluczowych kwestii.

### Raportowanie weryfikacji

Tradycyjne raporty z testów penetracyjnych zgłaszają problemy „przez wyjątek”, wymieniając wyłącznie niespełnione wymagania. Natomiast raport certyfikacyjny ASVS powinien zawierać zakres, podsumowanie wszystkich sprawdzonych wymagań, wymagania, przy których odnotowano wyjątki, oraz wskazówki dotyczące rozwiązania problemów. Niektóre wymagania mogą nie mieć zastosowania (np. zarządzanie sesją w bezstanowych API) — musi to zostać odnotowane w raporcie.

### Zakres weryfikacji

Organizacja tworząca aplikację z reguły nie wdroży wszystkich wymagań, ponieważ część z nich może być nieistotna lub mniej znacząca ze względu na funkcjonalność aplikacji. Weryfikator powinien jasno określić zakres weryfikacji, w tym poziom, który organizacja stara się osiągnąć, oraz wymagania, które zostały uwzględnione. Zakres powinien być opisany z perspektywy tego, co uwzględniono, a nie tego, co pominięto. Weryfikator powinien również przedstawić opinię o zasadności wykluczenia wymagań, które nie zostały wdrożone.

Powinno to pozwolić odbiorcy raportu z weryfikacji zrozumieć jej kontekst i podjąć świadomą decyzję o poziomie zaufania, jakim może obdarzyć aplikację.

Organizacje certyfikujące mogą wybierać własne metody testowania, ale powinny ujawnić je w raporcie, a testy powinny być w miarę możliwości powtarzalne. Do weryfikacji poszczególnych aspektów, takich jak walidacja danych wejściowych, mogą być stosowane różne metody — np. ręczne testy penetracyjne lub analiza kodu źródłowego — w zależności od aplikacji i wymagań.

### Mechanizmy weryfikacji

Weryfikacja poszczególnych wymagań ASVS może wymagać zastosowania szeregu różnych technik. Poza testami penetracyjnymi (z użyciem prawidłowych danych uwierzytelniających, aby uzyskać pełne pokrycie aplikacji) weryfikacja wymagań ASVS może wymagać dostępu do dokumentacji, kodu źródłowego, konfiguracji oraz osób zaangażowanych w proces wytwórczy — zwłaszcza przy weryfikacji wymagań L2 i L3. Standardową praktyką jest dostarczanie solidnych dowodów ustaleń wraz ze szczegółową dokumentacją, która może obejmować dokumenty robocze, zrzuty ekranu, skrypty i logi z testów. Samo uruchomienie zautomatyzowanego narzędzia bez gruntownych testów jest niewystarczające do certyfikacji, ponieważ każde wymaganie musi zostać w sposób weryfikowalny przetestowane.

Wykorzystanie automatyzacji do weryfikacji wymagań ASVS to temat budzący nieustanne zainteresowanie. Warto zatem doprecyzować kilka kwestii związanych z testowaniem automatycznym i czarnoskrzynkowym.

#### Rola zautomatyzowanych narzędzi do testowania bezpieczeństwa

Zautomatyzowane narzędzia do testowania bezpieczeństwa, takie jak narzędzia dynamicznej i statycznej analizy bezpieczeństwa aplikacji (DAST i SAST), poprawnie wdrożone w potoku budowania, mogą być w stanie zidentyfikować niektóre problemy bezpieczeństwa, które nigdy nie powinny wystąpić. Jednak bez starannej konfiguracji i dostrojenia nie zapewnią wymaganego pokrycia, a poziom szumu uniemożliwi zidentyfikowanie i wyeliminowanie rzeczywistych problemów bezpieczeństwa.

Choć narzędzia te mogą pokryć niektóre z bardziej podstawowych i prostych wymagań technicznych, na przykład dotyczących kodowania danych wyjściowych czy sanityzacji, należy koniecznie zaznaczyć, że nie będą one w stanie w pełni zweryfikować wielu bardziej złożonych wymagań ASVS ani tych dotyczących logiki biznesowej i kontroli dostępu.

W przypadku mniej oczywistych wymagań automatyzacja nadal może być wykorzystana, ale konieczne będzie napisanie weryfikacji specyficznych dla danej aplikacji. Mogą one przypominać testy jednostkowe i integracyjne, z których organizacja być może już korzysta. Możliwe zatem, że istniejącą infrastrukturę automatyzacji testów da się wykorzystać do napisania testów specyficznych dla ASVS. Choć będzie to wymagało krótkoterminowej inwestycji, długoterminowe korzyści z możliwości ciągłej weryfikacji tych wymagań ASVS będą znaczące.

Podsumowując: testowalne za pomocą automatyzacji != uruchomienie gotowego narzędzia z półki.

#### Rola testów penetracyjnych

Choć poziom L1 w wersji 4.0 był zoptymalizowany pod kątem testowania „czarnoskrzynkowego” (bez dokumentacji i bez kodu źródłowego), już wtedy standard jasno wskazywał, że nie jest to skuteczne działanie poświadczające i powinno być aktywnie odradzane.

Testowanie bez dostępu do niezbędnych dodatkowych informacji jest niewydajnym i nieskutecznym mechanizmem weryfikacji bezpieczeństwa, ponieważ pomija możliwość przeglądu kodu źródłowego, identyfikacji zagrożeń i brakujących mechanizmów oraz przeprowadzenia znacznie dokładniejszego testu w krótszym czasie.

Zdecydowanie zachęca się do przeprowadzania testów penetracyjnych opartych na dokumentacji lub kodzie źródłowym (hybrydowych), z pełnym dostępem do twórców aplikacji i jej dokumentacji, zamiast tradycyjnych testów penetracyjnych. Będzie to z pewnością konieczne do zweryfikowania wielu wymagań ASVS.
