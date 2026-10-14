# V6 Uwierzytelnianie

## Cel kontrolny

Uwierzytelnianie to proces ustalania lub potwierdzania autentyczności osoby lub urządzenia. Obejmuje weryfikację deklaracji składanych przez osobę lub dotyczących urządzenia, zapewnienie odporności na podszywanie się oraz zapobieganie odzyskaniu lub przechwyceniu haseł.

[NIST SP 800-63](https://pages.nist.gov/800-63-3/) to nowoczesny, oparty na dowodach standard, wartościowy dla organizacji na całym świecie, lecz szczególnie istotny dla agencji rządowych USA i podmiotów z nimi współpracujących.

Choć wiele wymagań tego rozdziału opiera się na drugiej części tego standardu (znanej jako NIST SP 800-63B „Digital Identity Guidelines - Authentication and Lifecycle Management”), rozdział koncentruje się na powszechnych zagrożeniach i często wykorzystywanych lukach w uwierzytelnianiu. Nie próbuje wyczerpująco pokryć każdego punktu standardu. W przypadkach, gdy konieczna jest pełna zgodność z NIST SP 800-63, należy sięgnąć do NIST SP 800-63.

Dodatkowo terminologia NIST SP 800-63 może się miejscami różnić — w tym rozdziale często stosowana jest terminologia powszechniej rozumiana, aby poprawić przejrzystość.

Częstą cechą bardziej zaawansowanych aplikacji jest zdolność dostosowywania wymaganych etapów uwierzytelniania w zależności od różnych czynników ryzyka. Funkcja ta została omówiona w rozdziale „Autoryzacja”, ponieważ mechanizmy te muszą być brane pod uwagę również przy decyzjach autoryzacyjnych.

## V6.1 Dokumentacja uwierzytelniania

Ta sekcja zawiera wymagania określające dokumentację uwierzytelniania, która powinna być utrzymywana dla aplikacji. Jest to kluczowe dla wdrożenia i oceny właściwej konfiguracji odpowiednich mechanizmów uwierzytelniania.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **6.1.1** | Zweryfikuj, że dokumentacja aplikacji definiuje, w jaki sposób mechanizmy takie jak ograniczanie częstotliwości żądań, ochrona przed automatyzacją i odpowiedź adaptacyjna są wykorzystywane do obrony przed atakami takimi jak credential stuffing i łamanie haseł metodą siłową. Dokumentacja musi jasno określać, jak mechanizmy te są skonfigurowane i jak zapobiegają złośliwemu blokowaniu kont. | 1 |
| **6.1.2** | Zweryfikuj, że udokumentowana jest lista słów specyficznych dla kontekstu, których użycie w hasłach ma być blokowane. Lista może obejmować permutacje nazw organizacji, nazw produktów, identyfikatorów systemów, kryptonimów projektów, nazw działów lub ról i podobne. | 2 |
| **6.1.3** | Zweryfikuj, że jeśli aplikacja udostępnia wiele ścieżek uwierzytelniania, wszystkie są udokumentowane wraz z mechanizmami bezpieczeństwa i siłą uwierzytelniania, które muszą być spójnie egzekwowane we wszystkich tych ścieżkach. | 2 |

## V6.2 Bezpieczeństwo haseł

Hasła — nazywane w NIST SP 800-63 „zapamiętanymi sekretami” (Memorized Secrets) — obejmują hasła, frazy hasłowe, kody PIN, wzory odblokowania oraz wskazywanie właściwego kotka lub innego elementu obrazkowego. Są na ogół uznawane za czynnik „coś, co wiesz” i często używane jako mechanizm uwierzytelniania jednoskładnikowego.

W związku z tym ta sekcja zawiera wymagania zapewniające, że hasła są tworzone i obsługiwane w sposób bezpieczny. Większość wymagań ma poziom L1, ponieważ na tym poziomie są najistotniejsze. Od L2 wzwyż wymagane są mechanizmy uwierzytelniania wieloskładnikowego, w których hasła mogą być jednym ze składników.

Wymagania tej sekcji odnoszą się głównie do [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) [wytycznych NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **6.2.1** | Zweryfikuj, że hasła ustawiane przez użytkowników mają co najmniej 8 znaków długości, przy czym zdecydowanie zaleca się minimum 15 znaków. | 1 |
| **6.2.2** | Zweryfikuj, że użytkownicy mogą zmienić swoje hasło. | 1 |
| **6.2.3** | Zweryfikuj, że funkcja zmiany hasła wymaga podania obecnego i nowego hasła użytkownika. | 1 |
| **6.2.4** | Zweryfikuj, że hasła przesyłane podczas rejestracji konta lub zmiany hasła są sprawdzane względem dostępnego zbioru co najmniej 3000 najpopularniejszych haseł spełniających politykę haseł aplikacji, np. minimalną długość. | 1 |
| **6.2.5** | Zweryfikuj, że można używać haseł o dowolnej kompozycji, bez reguł ograniczających dozwolone typy znaków. Nie może istnieć wymóg minimalnej liczby wielkich lub małych liter, cyfr ani znaków specjalnych. | 1 |
| **6.2.6** | Zweryfikuj, że pola wprowadzania hasła używają type=password w celu maskowania wpisywanej treści. Aplikacje mogą pozwalać użytkownikowi na tymczasowe wyświetlenie całego zamaskowanego hasła lub ostatnio wpisanego znaku. | 1 |
| **6.2.7** | Zweryfikuj, że dozwolone są funkcja „wklej”, przeglądarkowe pomocniki haseł oraz zewnętrzne menedżery haseł. | 1 |
| **6.2.8** | Zweryfikuj, że aplikacja weryfikuje hasło użytkownika dokładnie w postaci otrzymanej od użytkownika, bez żadnych modyfikacji, takich jak obcinanie czy zmiana wielkości liter. | 1 |
| **6.2.9** | Zweryfikuj, że dozwolone są hasła o długości co najmniej 64 znaków. | 2 |
| **6.2.10** | Zweryfikuj, że hasło użytkownika pozostaje ważne, dopóki nie zostanie wykryta jego kompromitacja lub użytkownik sam go nie zmieni. Aplikacja nie może wymagać okresowej rotacji poświadczeń. | 2 |
| **6.2.11** | Zweryfikuj, że udokumentowana lista słów specyficznych dla kontekstu jest używana, aby zapobiegać tworzeniu łatwych do odgadnięcia haseł. | 2 |
| **6.2.12** | Zweryfikuj, że hasła przesyłane podczas rejestracji konta lub zmiany hasła są sprawdzane względem zbioru haseł ujawnionych w wyciekach. | 2 |

## V6.3 Ogólne bezpieczeństwo uwierzytelniania

Ta sekcja zawiera ogólne wymagania dotyczące bezpieczeństwa mechanizmów uwierzytelniania oraz określa różne oczekiwania dla poszczególnych poziomów. Aplikacje L2 muszą wymuszać stosowanie uwierzytelniania wieloskładnikowego (MFA). Aplikacje L3 muszą używać uwierzytelniania sprzętowego, realizowanego w atestowanym, zaufanym środowisku wykonawczym (TEE). Może to obejmować passkeys powiązane z urządzeniem, mechanizmy uwierzytelniające o wysokim poziomie pewności eIDAS (LoA High), mechanizmy o poziomie pewności NIST Authenticator Assurance Level 3 (AAL3) lub równoważne rozwiązania.

Choć jest to stosunkowo agresywne stanowisko w sprawie MFA, podniesienie poprzeczki w tym obszarze jest krytyczne dla ochrony użytkowników, a każda próba złagodzenia tych wymagań powinna iść w parze z jasnym planem ograniczania ryzyk związanych z uwierzytelnianiem, uwzględniającym wytyczne i badania NIST w tym zakresie.

Warto zauważyć, że w chwili wydania NIST SP 800-63 uznaje e-mail za [niedopuszczalny](https://pages.nist.gov/800-63-FAQ/#q-b11) mechanizm uwierzytelniania ([kopia archiwalna](https://web.archive.org/web/20250330115328/https://pages.nist.gov/800-63-FAQ/#q-b11)).

Wymagania tej sekcji odnoszą się do różnych części [wytycznych NIST](https://pages.nist.gov/800-63-3/sp800-63b.html), w tym: [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling) oraz [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding).

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **6.3.1** | Zweryfikuj, że mechanizmy zapobiegające atakom takim jak credential stuffing i łamanie haseł metodą siłową są wdrożone zgodnie z dokumentacją bezpieczeństwa aplikacji. | 1 |
| **6.3.2** | Zweryfikuj, że domyślne konta użytkowników (np. „root”, „admin” lub „sa”) nie występują w aplikacji lub są wyłączone. | 1 |
| **6.3.3** | Zweryfikuj, że do uzyskania dostępu do aplikacji musi być używany mechanizm uwierzytelniania wieloskładnikowego albo kombinacja mechanizmów jednoskładnikowych. Dla L3 jednym ze składników musi być sprzętowy mechanizm uwierzytelniania, zapewniający odporność na kompromitację i podszywanie się w atakach phishingowych oraz weryfikujący zamiar uwierzytelnienia poprzez wymaganie działania zainicjowanego przez użytkownika (takiego jak naciśnięcie przycisku na kluczu sprzętowym FIDO lub telefonie komórkowym). Złagodzenie któregokolwiek z warunków tego wymagania wymaga w pełni udokumentowanego uzasadnienia oraz kompleksowego zestawu mechanizmów ograniczających ryzyko. | 2 |
| **6.3.4** | Zweryfikuj, że jeśli aplikacja udostępnia wiele ścieżek uwierzytelniania, nie istnieją ścieżki nieudokumentowane, a mechanizmy bezpieczeństwa i siła uwierzytelniania są egzekwowane spójnie. | 2 |
| **6.3.5** | Zweryfikuj, że użytkownicy są powiadamiani o podejrzanych próbach uwierzytelnienia (udanych lub nieudanych). Może to obejmować próby uwierzytelnienia z nietypowej lokalizacji lub klienta, uwierzytelnienie częściowo udane (tylko jeden z wielu składników), próbę uwierzytelnienia po długim okresie bezczynności lub udane uwierzytelnienie po kilku nieudanych próbach. | 3 |
| **6.3.6** | Zweryfikuj, że e-mail nie jest używany jako mechanizm uwierzytelniania — ani jednoskładnikowego, ani wieloskładnikowego. | 3 |
| **6.3.7** | Zweryfikuj, że użytkownicy są powiadamiani po zmianach danych uwierzytelniania, takich jak resety poświadczeń lub modyfikacja nazwy użytkownika bądź adresu e-mail. | 3 |
| **6.3.8** | Zweryfikuj, że na podstawie nieudanych prób uwierzytelnienia nie można wywnioskować istnienia prawidłowych użytkowników — na przykład na podstawie komunikatów o błędach, kodów odpowiedzi HTTP lub różnych czasów odpowiedzi. Ochronę tę musi mieć również funkcjonalność rejestracji i odzyskiwania zapomnianego hasła. | 3 |

## V6.4 Cykl życia i odzyskiwanie czynników uwierzytelniania

Czynniki uwierzytelniania mogą obejmować hasła, tokeny programowe, tokeny sprzętowe oraz urządzenia biometryczne. Bezpieczna obsługa cyklu życia tych mechanizmów jest krytyczna dla bezpieczeństwa aplikacji — ta sekcja zawiera wymagania z tym związane.

Wymagania tej sekcji odnoszą się głównie do [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) lub [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) [wytycznych NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **6.4.1** | Zweryfikuj, że generowane przez system hasła początkowe lub kody aktywacyjne są generowane w sposób bezpiecznie losowy, zgodne z obowiązującą polityką haseł oraz wygasają po krótkim czasie lub po pierwszym użyciu. Te początkowe sekrety nie mogą stać się hasłem długoterminowym. | 1 |
| **6.4.2** | Zweryfikuj, że nie występują podpowiedzi do haseł ani uwierzytelnianie oparte na wiedzy (tzw. „pytania bezpieczeństwa”). | 1 |
| **6.4.3** | Zweryfikuj, że wdrożony jest bezpieczny proces resetowania zapomnianego hasła, który nie omija żadnych włączonych mechanizmów uwierzytelniania wieloskładnikowego. | 2 |
| **6.4.4** | Zweryfikuj, że w razie utraty składnika uwierzytelniania wieloskładnikowego przeprowadzane jest potwierdzenie tożsamości na tym samym poziomie, co podczas rejestracji. | 2 |
| **6.4.5** | Zweryfikuj, że instrukcje odnowienia dla wygasających mechanizmów uwierzytelniania są wysyłane z wyprzedzeniem wystarczającym na ich wykonanie przed wygaśnięciem starego mechanizmu, z konfiguracją automatycznych przypomnień w razie potrzeby. | 3 |
| **6.4.6** | Zweryfikuj, że użytkownicy administracyjni mogą zainicjować proces resetowania hasła użytkownika, ale nie mogą przy tym zmienić ani wybrać hasła użytkownika. Zapobiega to sytuacji, w której znaliby hasło użytkownika. | 3 |

## V6.5 Ogólne wymagania uwierzytelniania wieloskładnikowego

Ta sekcja zawiera ogólne wytyczne istotne dla różnych metod uwierzytelniania wieloskładnikowego.

Mechanizmy te obejmują:

* Sekrety odszukiwane (lookup secrets)
* Hasła jednorazowe oparte na czasie (TOTP)
* Mechanizmy pozapasmowe (out-of-band)

Sekrety odszukiwane to wstępnie wygenerowane listy tajnych kodów, podobne do numerów autoryzacji transakcji (TAN), kodów odzyskiwania w mediach społecznościowych lub siatki zawierającej zestaw losowych wartości. Ten typ mechanizmu uwierzytelniania jest uznawany za „coś, co masz”, ponieważ kody są celowo niemożliwe do zapamiętania i muszą być gdzieś przechowywane.

Hasła jednorazowe oparte na czasie (TOTP) to tokeny fizyczne lub programowe wyświetlające stale zmieniające się, pseudolosowe wyzwanie jednorazowe. Ten typ mechanizmu uwierzytelniania jest uznawany za „coś, co masz”. Wieloskładnikowe TOTP są podobne do jednoskładnikowych, ale wymagają podania prawidłowego kodu PIN, odblokowania biometrycznego, włożenia USB lub sparowania NFC, albo dodatkowej wartości (jak w kalkulatorach podpisywania transakcji), aby utworzyć ostateczne hasło jednorazowe (OTP).

Szczegóły mechanizmów pozapasmowych zostaną przedstawione w kolejnej sekcji.

Wymagania tych sekcji odnoszą się głównie do [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators) oraz [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) [wytycznych NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **6.5.1** | Zweryfikuj, że sekrety odszukiwane, pozapasmowe żądania lub kody uwierzytelniania oraz hasła jednorazowe oparte na czasie (TOTP) mogą zostać skutecznie użyte tylko raz. | 2 |
| **6.5.2** | Zweryfikuj, że sekrety odszukiwane o entropii mniejszej niż 112 bitów (19 losowych znaków alfanumerycznych lub 34 losowe cyfry), przechowywane w backendzie aplikacji, są haszowane zatwierdzonym algorytmem haszowania do przechowywania haseł, wykorzystującym 32-bitową losową sól. Jeśli sekret ma entropię 112 bitów lub więcej, można użyć standardowej funkcji skrótu. | 2 |
| **6.5.3** | Zweryfikuj, że sekrety odszukiwane, pozapasmowe kody uwierzytelniania oraz ziarna haseł jednorazowych opartych na czasie są generowane przy użyciu kryptograficznie bezpiecznego generatora liczb pseudolosowych (CSPRNG), aby uniknąć przewidywalnych wartości. | 2 |
| **6.5.4** | Zweryfikuj, że sekrety odszukiwane i pozapasmowe kody uwierzytelniania mają entropię co najmniej 20 bitów (zwykle wystarczą 4 losowe znaki alfanumeryczne lub 6 losowych cyfr). | 2 |
| **6.5.5** | Zweryfikuj, że pozapasmowe żądania, kody lub tokeny uwierzytelniania, a także hasła jednorazowe oparte na czasie (TOTP), mają zdefiniowany czas życia. Żądania pozapasmowe muszą mieć maksymalny czas życia 10 minut, a TOTP — maksymalnie 30 sekund. | 2 |
| **6.5.6** | Zweryfikuj, że każdy czynnik uwierzytelniania (w tym urządzenia fizyczne) może zostać unieważniony w przypadku kradzieży lub innej utraty. | 3 |
| **6.5.7** | Zweryfikuj, że biometryczne mechanizmy uwierzytelniania są używane wyłącznie jako czynniki drugorzędne, łącznie z czynnikiem „coś, co masz” lub „coś, co wiesz”. | 3 |
| **6.5.8** | Zweryfikuj, że hasła jednorazowe oparte na czasie (TOTP) są sprawdzane na podstawie źródła czasu z zaufanej usługi, a nie czasu niezaufanego lub dostarczonego przez klienta. | 3 |

## V6.6 Pozapasmowe mechanizmy uwierzytelniania

Zwykle polega to na komunikacji serwera uwierzytelniania z urządzeniem fizycznym poprzez bezpieczny kanał dodatkowy — na przykład wysyłaniu powiadomień push na urządzenia mobilne. Ten typ mechanizmu uwierzytelniania jest uznawany za „coś, co masz”.

Niebezpieczne pozapasmowe mechanizmy uwierzytelniania, takie jak e-mail i VOIP, są niedozwolone. Uwierzytelnianie przez PSTN i SMS jest obecnie uznawane przez NIST za mechanizmy [„ograniczone”](https://pages.nist.gov/800-63-FAQ/#q-b01) i powinno być wycofywane na rzecz haseł jednorazowych opartych na czasie (TOTP), mechanizmu kryptograficznego lub podobnego. NIST SP 800-63B [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network) zaleca zajęcie się ryzykami podmiany urządzenia, zmiany karty SIM, przeniesienia numeru lub innych nietypowych zachowań, jeśli uwierzytelnianie pozapasmowe przez telefon lub SMS absolutnie musi być wspierane. Choć ta sekcja ASVS nie czyni z tego wymagania, brak tych środków ostrożności w przypadku wrażliwej aplikacji L2 lub aplikacji L3 należy traktować jako istotny sygnał ostrzegawczy.

Warto zauważyć, że NIST wydał również niedawno wytyczne, które [odradzają stosowanie powiadomień push](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/#fig-3). Choć ta sekcja ASVS tego nie robi, należy mieć świadomość ryzyk związanych z „push bombingiem”.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **6.6.1** | Zweryfikuj, że mechanizmy uwierzytelniania wykorzystujące publiczną komutowaną sieć telefoniczną (PSTN) do dostarczania haseł jednorazowych (OTP) przez telefon lub SMS są oferowane wyłącznie wtedy, gdy numer telefonu został wcześniej zweryfikowany, oferowane są także alternatywne, silniejsze metody (takie jak hasła jednorazowe oparte na czasie), a usługa informuje użytkowników o związanych z nimi ryzykach bezpieczeństwa. Dla aplikacji L3 telefon i SMS nie mogą być dostępne jako opcje. | 2 |
| **6.6.2** | Zweryfikuj, że pozapasmowe żądania, kody lub tokeny uwierzytelniania są powiązane z pierwotnym żądaniem uwierzytelnienia, dla którego zostały wygenerowane, i nie mogą być użyte dla żądania wcześniejszego ani późniejszego. | 2 |
| **6.6.3** | Zweryfikuj, że pozapasmowy mechanizm uwierzytelniania oparty na kodach jest chroniony przed atakami siłowymi poprzez ograniczanie częstotliwości żądań. Rozważ również użycie kodu o entropii co najmniej 64 bitów. | 2 |
| **6.6.4** | Zweryfikuj, że tam, gdzie do uwierzytelniania wieloskładnikowego używane są powiadomienia push, stosowane jest ograniczanie częstotliwości żądań, aby zapobiec atakom push bombing. Ryzyko to może ograniczyć również dopasowanie numeru (number matching). | 3 |

## V6.7 Kryptograficzny mechanizm uwierzytelniania

Kryptograficzne mechanizmy uwierzytelniania obejmują karty inteligentne lub klucze FIDO, gdzie użytkownik musi podłączyć lub sparować urządzenie kryptograficzne z komputerem, aby dokończyć uwierzytelnianie. Serwer uwierzytelniania wysyła wyzwanie (challenge nonce) do urządzenia lub oprogramowania kryptograficznego, a urządzenie lub oprogramowanie oblicza odpowiedź na podstawie bezpiecznie przechowywanego klucza kryptograficznego. Wymagania tej sekcji zawierają wskazówki implementacyjne dla tych mechanizmów; wytyczne dotyczące algorytmów kryptograficznych omówiono w rozdziale „Kryptografia”.

Tam, gdzie do uwierzytelniania kryptograficznego używane są klucze współdzielone lub tajne, powinny być one przechowywane z użyciem tych samych mechanizmów, co inne sekrety systemowe — zgodnie z sekcją „Zarządzanie sekretami” w rozdziale „Konfiguracja”.

Wymagania tej sekcji odnoszą się głównie do [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) [wytycznych NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **6.7.1** | Zweryfikuj, że certyfikaty używane do weryfikacji kryptograficznych asercji uwierzytelniania są przechowywane w sposób chroniący je przed modyfikacją. | 3 |
| **6.7.2** | Zweryfikuj, że wyzwanie (nonce) ma długość co najmniej 64 bitów i jest statystycznie unikalne lub unikalne w całym cyklu życia urządzenia kryptograficznego. | 3 |

## V6.8 Uwierzytelnianie z dostawcą tożsamości

Dostawcy tożsamości (IdP) zapewniają użytkownikom tożsamość federacyjną. Użytkownicy często mają więcej niż jedną tożsamość u wielu dostawców — na przykład tożsamość firmową w Azure AD, Okta, Ping Identity lub Google albo tożsamość konsumencką w serwisach Facebook, Twitter, Google czy WeChat, żeby wymienić tylko kilka popularnych opcji. Lista ta nie stanowi rekomendacji tych firm ani usług, a jedynie zachętę dla programistów, aby uwzględniali fakt, że wielu użytkowników posiada wiele ustanowionych tożsamości. Organizacje powinny rozważyć integrację z istniejącymi tożsamościami użytkowników, stosownie do profilu ryzyka i siły potwierdzania tożsamości danego IdP. Przykładowo mało prawdopodobne jest, aby organizacja rządowa zaakceptowała tożsamość z mediów społecznościowych jako login do systemów wrażliwych — łatwo bowiem tworzyć tożsamości fałszywe lub jednorazowe — podczas gdy firma produkująca gry mobilne może jak najbardziej potrzebować integracji z głównymi platformami społecznościowymi, aby powiększać bazę aktywnych graczy.

Bezpieczne korzystanie z zewnętrznych dostawców tożsamości wymaga starannej konfiguracji i weryfikacji, aby zapobiec podszywaniu się pod tożsamość lub sfałszowanym asercjom. Ta sekcja zawiera wymagania odnoszące się do tych ryzyk.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **6.8.1** | Zweryfikuj, że jeśli aplikacja wspiera wielu dostawców tożsamości (IdP), tożsamości użytkownika nie można podrobić za pośrednictwem innego wspieranego dostawcy (np. używając tego samego identyfikatora użytkownika). Standardowym środkiem zaradczym jest rejestrowanie i identyfikowanie użytkownika przez aplikację na podstawie kombinacji identyfikatora IdP (pełniącego rolę przestrzeni nazw) oraz identyfikatora użytkownika w ramach danego IdP. | 2 |
| **6.8.2** | Zweryfikuj, że obecność i integralność podpisów cyfrowych na asercjach uwierzytelniania (na przykład na tokenach JWT lub asercjach SAML) jest zawsze walidowana, z odrzucaniem wszelkich asercji niepodpisanych lub z nieprawidłowymi podpisami. | 2 |
| **6.8.3** | Zweryfikuj, że asercje SAML są przetwarzane w sposób unikalny i używane tylko raz w okresie ważności, aby zapobiec atakom powtórzeniowym. | 2 |
| **6.8.4** | Zweryfikuj, że jeśli aplikacja korzysta z odrębnego dostawcy tożsamości (IdP) i oczekuje określonej siły, metod lub aktualności uwierzytelnienia dla konkretnych funkcji, weryfikuje to na podstawie informacji zwróconych przez IdP. Na przykład przy użyciu OIDC można to osiągnąć poprzez walidację oświadczeń tokena ID, takich jak 'acr', 'amr' i 'auth_time' (jeśli występują). Jeśli IdP nie dostarcza tych informacji, aplikacja musi mieć udokumentowane podejście awaryjne zakładające, że użyto mechanizmu uwierzytelniania o minimalnej sile (na przykład jednoskładnikowego z nazwą użytkownika i hasłem). | 2 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [NIST SP 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST SP 800-63B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST SP 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Web Security Testing Guide: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/04-Authentication_Testing)
* [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Choosing and Using Security Questions Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
* [Wytyczne CISA dotyczące „dopasowania numeru” (Number Matching)](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
* [Informacje o FIDO Alliance](https://fidoalliance.org/)
