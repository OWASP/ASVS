# V11 Kryptografia

## Cel kontrolny

Celem tego rozdziału jest zdefiniowanie najlepszych praktyk ogólnego stosowania kryptografii, a także zaszczepienie fundamentalnego zrozumienia zasad kryptograficznych i zainspirowanie zwrotu ku bardziej odpornym i nowoczesnym podejściom. Rozdział zachęca do:

* Wdrażania solidnych systemów kryptograficznych, które zawodzą w sposób bezpieczny, adaptują się do ewoluujących zagrożeń i są przygotowane na przyszłość.
* Stosowania mechanizmów kryptograficznych, które są zarówno bezpieczne, jak i zgodne z najlepszymi praktykami branżowymi.
* Utrzymywania bezpiecznego systemu zarządzania kluczami kryptograficznymi z odpowiednią kontrolą dostępu i audytem.
* Regularnej oceny krajobrazu kryptograficznego w celu analizy nowych ryzyk i odpowiedniego dostosowywania algorytmów.
* Wykrywania i zarządzania przypadkami użycia kryptografii w całym cyklu życia aplikacji, aby wszystkie zasoby kryptograficzne były zewidencjonowane i zabezpieczone.

Oprócz przedstawienia ogólnych zasad i najlepszych praktyk dokument zawiera również bardziej szczegółowe informacje techniczne o wymaganiach w Załączniku C — Standardy kryptograficzne. Obejmuje to algorytmy i tryby uznawane za „zatwierdzone” na potrzeby wymagań tego rozdziału.

Wymagania wykorzystujące kryptografię do rozwiązania odrębnego problemu — takiego jak zarządzanie sekretami czy bezpieczeństwo komunikacji — znajdują się w innych częściach standardu.

## V11.1 Inwentarz kryptograficzny i dokumentacja

Aplikacje muszą być projektowane z silną architekturą kryptograficzną, chroniącą zasoby danych stosownie do ich klasyfikacji. Szyfrowanie wszystkiego jest marnotrawstwem; nieszyfrowanie niczego to prawne zaniedbanie. Należy znaleźć równowagę — zwykle na etapie projektowania architektury lub projektu wysokopoziomowego, sprintów projektowych albo tzw. architectural spikes. Projektowanie kryptografii „na bieżąco” lub jej późniejsze doszywanie nieuchronnie będzie kosztować znacznie więcej niż wbudowanie jej od samego początku.

Ważne jest zapewnienie, że wszystkie zasoby kryptograficzne są regularnie wykrywane, inwentaryzowane i oceniane. Więcej informacji o tym, jak można to zrobić, znajduje się w załączniku.

Krytyczna jest również potrzeba zabezpieczenia systemów kryptograficznych na przyszłość — wobec nadciągającej ery komputerów kwantowych. Kryptografia postkwantowa (Post-Quantum Cryptography, PQC) odnosi się do algorytmów kryptograficznych zaprojektowanych tak, aby pozostały bezpieczne wobec ataków komputerów kwantowych, które — jak się oczekuje — złamią powszechnie stosowane algorytmy, takie jak RSA i kryptografia krzywych eliptycznych (ECC).

Aktualne wytyczne dotyczące zweryfikowanych prymitywów i standardów PQC znajdują się w załączniku.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **11.1.1** | Zweryfikuj, że istnieje udokumentowana polityka zarządzania kluczami kryptograficznymi oraz cykl życia klucza kryptograficznego zgodny ze standardem zarządzania kluczami, takim jak NIST SP 800-57. Powinno to obejmować zapewnienie, że klucze nie są nadmiernie współdzielone (na przykład z więcej niż dwoma podmiotami dla sekretów współdzielonych i więcej niż jednym podmiotem dla kluczy prywatnych). | 2 |
| **11.1.2** | Zweryfikuj, że inwentarz kryptograficzny jest wykonywany, utrzymywany, regularnie aktualizowany i obejmuje wszystkie klucze kryptograficzne, algorytmy oraz certyfikaty używane przez aplikację. Musi on również dokumentować, gdzie klucze mogą i nie mogą być używane w systemie, oraz typy danych, które mogą i nie mogą być chronione tymi kluczami. | 2 |
| **11.1.3** | Zweryfikuj, że stosowane są mechanizmy wykrywania kryptografii, identyfikujące wszystkie wystąpienia kryptografii w systemie, w tym operacje szyfrowania, haszowania i podpisywania. | 3 |
| **11.1.4** | Zweryfikuj, że utrzymywany jest inwentarz kryptograficzny. Musi on obejmować udokumentowany plan określający ścieżkę migracji do nowych standardów kryptograficznych, takich jak kryptografia postkwantowa, aby móc reagować na przyszłe zagrożenia. | 3 |

## V11.2 Bezpieczna implementacja kryptografii

Ta sekcja definiuje wymagania dotyczące wyboru, implementacji i bieżącego zarządzania podstawowymi algorytmami kryptograficznymi aplikacji. Celem jest zapewnienie, że wdrażane są wyłącznie solidne, akceptowane branżowo prymitywy kryptograficzne, zgodne z aktualnymi standardami (np. NIST, ISO/IEC) i najlepszymi praktykami. Organizacje muszą zapewnić, że każdy komponent kryptograficzny jest wybierany na podstawie recenzowanych dowodów i praktycznych testów bezpieczeństwa.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **11.2.1** | Zweryfikuj, że do operacji kryptograficznych używane są implementacje zweryfikowane branżowo (w tym biblioteki i implementacje akcelerowane sprzętowo). | 2 |
| **11.2.2** | Zweryfikuj, że aplikacja została zaprojektowana z zachowaniem zwinności kryptograficznej (crypto agility) — tak aby algorytmy liczb losowych, szyfrowania uwierzytelnionego, MAC lub haszowania, długości kluczy, liczby rund, szyfry i tryby mogły być w dowolnym momencie rekonfigurowane, aktualizowane lub wymieniane, w celu ochrony przed złamaniami kryptograficznymi. Analogicznie musi istnieć możliwość wymiany kluczy i haseł oraz ponownego zaszyfrowania danych. Pozwoli to na płynne przejście na kryptografię postkwantową (PQC), gdy szeroko dostępne staną się wysokopewne implementacje zatwierdzonych schematów lub standardów PQC. | 2 |
| **11.2.3** | Zweryfikuj, że wszystkie prymitywy kryptograficzne zapewniają co najmniej 128 bitów bezpieczeństwa, biorąc pod uwagę algorytm, rozmiar klucza i konfigurację. Na przykład 256-bitowy klucz ECC zapewnia około 128 bitów bezpieczeństwa, podczas gdy RSA wymaga klucza 3072-bitowego, aby osiągnąć 128 bitów bezpieczeństwa. | 2 |
| **11.2.4** | Zweryfikuj, że wszystkie operacje kryptograficzne są wykonywane w czasie stałym, bez operacji „skracających” (short-circuit) w porównaniach, obliczeniach i zwracanych wartościach, aby uniknąć wycieku informacji. | 3 |
| **11.2.5** | Zweryfikuj, że wszystkie moduły kryptograficzne zawodzą w sposób bezpieczny, a błędy są obsługiwane tak, aby nie umożliwiały podatności, takich jak ataki Padding Oracle. | 3 |

## V11.3 Algorytmy szyfrowania

Algorytmy szyfrowania uwierzytelnionego zbudowane na AES i CHACHA20 stanowią kręgosłup nowoczesnej praktyki kryptograficznej.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **11.3.1** | Zweryfikuj, że nie są używane niebezpieczne tryby blokowe (np. ECB) ani słabe schematy dopełnienia (np. PKCS#1 v1.5). | 1 |
| **11.3.2** | Zweryfikuj, że używane są wyłącznie zatwierdzone szyfry i tryby, takie jak AES z GCM. | 1 |
| **11.3.3** | Zweryfikuj, że zaszyfrowane dane są chronione przed nieautoryzowaną modyfikacją — najlepiej z użyciem zatwierdzonej metody szyfrowania uwierzytelnionego albo poprzez połączenie zatwierdzonej metody szyfrowania z zatwierdzonym algorytmem MAC. | 2 |
| **11.3.4** | Zweryfikuj, że wartości nonce, wektory inicjujące i inne liczby jednorazowe nie są używane dla więcej niż jednej pary klucz szyfrujący–element danych. Metoda ich generowania musi być odpowiednia dla stosowanego algorytmu. | 3 |
| **11.3.5** | Zweryfikuj, że każda kombinacja algorytmu szyfrowania i algorytmu MAC działa w trybie encrypt-then-MAC. | 3 |

## V11.4 Haszowanie i funkcje oparte na skrótach

Skróty kryptograficzne są wykorzystywane w bardzo wielu protokołach kryptograficznych, takich jak podpisy cyfrowe, HMAC, funkcje wyprowadzania klucza (KDF), generowanie losowych bitów oraz przechowywanie haseł. Bezpieczeństwo systemu kryptograficznego jest tylko tak silne, jak leżące u jego podstaw funkcje skrótu. Ta sekcja przedstawia wymagania dotyczące stosowania bezpiecznych funkcji skrótu w operacjach kryptograficznych.

W kwestii przechowywania haseł — obok załącznika kryptograficznego — użyteczny kontekst i wskazówki zapewnia również [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms).

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **11.4.1** | Zweryfikuj, że dla ogólnych kryptograficznych przypadków użycia — w tym podpisów cyfrowych, HMAC, KDF i generowania losowych bitów — używane są wyłącznie zatwierdzone funkcje skrótu. Niedozwolone funkcje skrótu, takie jak MD5, nie mogą być używane do żadnych celów kryptograficznych. | 1 |
| **11.4.2** | Zweryfikuj, że hasła są przechowywane z użyciem zatwierdzonej, wymagającej obliczeniowo funkcji wyprowadzania klucza (znanej też jako „funkcja haszowania haseł”), z parametrami skonfigurowanymi zgodnie z aktualnymi wytycznymi. Ustawienia powinny równoważyć bezpieczeństwo i wydajność tak, aby ataki siłowe były wystarczająco trudne dla wymaganego poziomu bezpieczeństwa. | 2 |
| **11.4.3** | Zweryfikuj, że funkcje skrótu używane w podpisach cyfrowych, jako element uwierzytelniania danych lub ich integralności, są odporne na kolizje i mają odpowiednie długości bitowe. Jeśli wymagana jest odporność na kolizje, długość wyjścia musi wynosić co najmniej 256 bitów. Jeśli wymagana jest wyłącznie odporność na ataki drugiego przeciwobrazu (second pre-image), długość wyjścia musi wynosić co najmniej 128 bitów. | 2 |
| **11.4.4** | Zweryfikuj, że aplikacja używa zatwierdzonych funkcji wyprowadzania klucza z parametrami rozciągania klucza (key stretching) przy wyprowadzaniu kluczy tajnych z haseł. Stosowane parametry muszą równoważyć bezpieczeństwo i wydajność, aby ataki siłowe nie mogły skompromitować wynikowego klucza kryptograficznego. | 2 |

## V11.5 Wartości losowe

Kryptograficznie bezpieczne generowanie liczb pseudolosowych (CSPRNG) jest niezwykle trudne do poprawnego zrealizowania. Zasadniczo dobre źródła entropii w systemie szybko się wyczerpują przy nadużywaniu, natomiast źródła o mniejszej losowości mogą prowadzić do przewidywalnych kluczy i sekretów.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **11.5.1** | Zweryfikuj, że wszystkie liczby losowe i ciągi znaków, które mają być nieodgadywalne, są generowane przy użyciu kryptograficznie bezpiecznego generatora liczb pseudolosowych (CSPRNG) i mają entropię co najmniej 128 bitów. Zwróć uwagę, że UUID-y nie spełniają tego warunku. | 2 |
| **11.5.2** | Zweryfikuj, że stosowany mechanizm generowania liczb losowych został zaprojektowany do bezpiecznego działania nawet pod dużym obciążeniem. | 3 |

## V11.6 Kryptografia klucza publicznego

Kryptografia klucza publicznego znajduje zastosowanie tam, gdzie współdzielenie klucza tajnego między wieloma stronami nie jest możliwe lub pożądane.

W ramach tego istnieje potrzeba stosowania zatwierdzonych mechanizmów wymiany kluczy, takich jak Diffie-Hellman i Elliptic Curve Diffie-Hellman (ECDH), aby kryptosystem pozostał bezpieczny wobec współczesnych zagrożeń. Rozdział „Bezpieczna komunikacja” zawiera wymagania dotyczące TLS, dlatego wymagania tej sekcji są przeznaczone dla sytuacji, w których kryptografia klucza publicznego jest wykorzystywana w przypadkach użycia innych niż TLS.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **11.6.1** | Zweryfikuj, że do generowania kluczy i zasilania generatora (seeding) oraz do generowania i weryfikacji podpisów cyfrowych używane są wyłącznie zatwierdzone algorytmy kryptograficzne i tryby działania. Algorytmy generowania kluczy nie mogą generować kluczy niebezpiecznych, podatnych na znane ataki — na przykład kluczy RSA podatnych na faktoryzację Fermata. | 2 |
| **11.6.2** | Zweryfikuj, że do wymiany kluczy używane są zatwierdzone algorytmy kryptograficzne (takie jak Diffie-Hellman), ze szczególnym naciskiem na to, aby mechanizmy wymiany kluczy używały bezpiecznych parametrów. Zapobiegnie to atakom na proces ustanawiania klucza, które mogłyby prowadzić do ataków typu adversary-in-the-middle lub złamań kryptograficznych. | 3 |

## V11.7 Kryptografia danych w użyciu

Ochrona danych podczas ich przetwarzania jest sprawą nadrzędną. Zalecane są techniki takie jak pełne szyfrowanie pamięci, szyfrowanie danych w tranzycie oraz zapewnienie, że dane są szyfrowane możliwie najszybciej po użyciu.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **11.7.1** | Zweryfikuj, że stosowane jest pełne szyfrowanie pamięci, chroniące dane wrażliwe w trakcie użycia i uniemożliwiające dostęp nieuprawnionym użytkownikom lub procesom. | 3 |
| **11.7.2** | Zweryfikuj, że minimalizacja danych zapewnia, iż podczas przetwarzania eksponowana jest minimalna ilość danych, oraz upewnij się, że dane są szyfrowane natychmiast po użyciu lub najszybciej, jak to wykonalne. | 3 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP Web Security Testing Guide: Testing for Weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography)
* [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
