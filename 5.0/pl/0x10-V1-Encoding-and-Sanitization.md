# V1 Kodowanie i sanityzacja

## Cel kontrolny

Niniejszy rozdział dotyczy najczęstszych słabości bezpieczeństwa aplikacji internetowych związanych z niebezpiecznym przetwarzaniem niezaufanych danych. Słabości te mogą prowadzić do różnych podatności technicznych, w których niezaufane dane są interpretowane zgodnie z regułami składni właściwego interpretera.

W nowoczesnych aplikacjach internetowych najlepiej zawsze korzystać z bezpieczniejszych API, takich jak zapytania parametryzowane, automatyczne escapowanie czy frameworki szablonów. W przeciwnym razie starannie wykonane kodowanie danych wyjściowych, escapowanie lub sanityzacja stają się krytyczne dla bezpieczeństwa aplikacji.

Walidacja danych wejściowych pełni rolę mechanizmu obrony w głąb, chroniącego przed nieoczekiwaną lub niebezpieczną treścią. Ponieważ jednak jej głównym celem jest zapewnienie, że przychodząca treść odpowiada oczekiwaniom funkcjonalnym i biznesowym, powiązane z nią wymagania znajdują się w rozdziale „Walidacja i logika biznesowa”.

## V1.1 Architektura kodowania i sanityzacji

W poniższych sekcjach przedstawiono wymagania — specyficzne dla danej składni lub interpretera — dotyczące bezpiecznego przetwarzania niebezpiecznej treści w celu uniknięcia podatności. Wymagania w tej sekcji obejmują kolejność, w jakiej przetwarzanie powinno następować, oraz miejsce, w którym powinno się odbywać. Mają one również zapewnić, że przechowywane dane pozostają w swojej pierwotnej postaci i nie są zapisywane w formie zakodowanej ani escapowanej (np. kodowanie HTML), aby zapobiec problemom podwójnego kodowania.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **1.1.1** | Zweryfikuj, że dane wejściowe są dekodowane lub pozbawiane escapowania do postaci kanonicznej tylko raz, że dekodowanie następuje wyłącznie wtedy, gdy oczekiwane są dane zakodowane w tej formie, oraz że odbywa się to przed dalszym przetwarzaniem danych wejściowych — na przykład nie jest wykonywane po walidacji lub sanityzacji danych wejściowych. | 2 |
| **1.1.2** | Zweryfikuj, że aplikacja wykonuje kodowanie i escapowanie danych wyjściowych jako ostatni krok przed ich użyciem przez interpreter, dla którego są przeznaczone, albo że wykonuje je sam interpreter. | 2 |

## V1.2 Zapobieganie wstrzyknięciom

Kodowanie lub escapowanie danych wyjściowych, wykonywane blisko potencjalnie niebezpiecznego kontekstu lub bezpośrednio przy nim, jest krytyczne dla bezpieczeństwa każdej aplikacji. Zazwyczaj kodowanie i escapowanie danych wyjściowych nie jest utrwalane — służy do uczynienia danych wyjściowych bezpiecznymi do natychmiastowego użycia we właściwym interpreterze. Próba wykonania tego zbyt wcześnie może skutkować zniekształceniem treści lub uczynić kodowanie bądź escapowanie nieskutecznym.

W wielu przypadkach biblioteki oprogramowania zawierają bezpieczne lub bezpieczniejsze funkcje, które wykonują to automatycznie — należy jednak upewnić się, że są one właściwe dla bieżącego kontekstu.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **1.2.1** | Zweryfikuj, że kodowanie danych wyjściowych dla odpowiedzi HTTP, dokumentu HTML lub dokumentu XML jest właściwe dla wymaganego kontekstu — na przykład kodowanie odpowiednich znaków dla elementów HTML, atrybutów HTML, komentarzy HTML, CSS lub pól nagłówków HTTP — aby uniknąć zmiany struktury komunikatu lub dokumentu. | 1 |
| **1.2.2** | Zweryfikuj, że przy dynamicznym budowaniu adresów URL niezaufane dane są kodowane zgodnie z ich kontekstem (np. kodowanie URL lub base64url dla parametrów zapytania lub ścieżki). Upewnij się, że dozwolone są wyłącznie bezpieczne protokoły URL (np. zablokowane są javascript: lub data:). | 1 |
| **1.2.3** | Zweryfikuj, że przy dynamicznym budowaniu treści JavaScript (w tym JSON) stosowane jest kodowanie lub escapowanie danych wyjściowych, aby uniknąć zmiany struktury komunikatu lub dokumentu (aby zapobiec wstrzyknięciom JavaScript i JSON). | 1 |
| **1.2.4** | Zweryfikuj, że wybieranie danych i zapytania do baz danych (np. SQL, HQL, NoSQL, Cypher) używają zapytań parametryzowanych, ORM-ów, frameworków encji lub są w inny sposób chronione przed wstrzyknięciem SQL i innymi atakami wstrzyknięcia do baz danych. Dotyczy to również pisania procedur składowanych. | 1 |
| **1.2.5** | Zweryfikuj, że aplikacja chroni przed wstrzyknięciem poleceń systemu operacyjnego oraz że wywołania systemowe używają sparametryzowanych zapytań systemowych lub stosują kontekstowe kodowanie danych wyjściowych wiersza poleceń. | 1 |
| **1.2.6** | Zweryfikuj, że aplikacja chroni przed podatnościami wstrzyknięcia LDAP lub że wdrożono dedykowane mechanizmy bezpieczeństwa zapobiegające wstrzyknięciu LDAP. | 2 |
| **1.2.7** | Zweryfikuj, że aplikacja jest chroniona przed atakami wstrzyknięcia XPath poprzez parametryzację zapytań lub użycie zapytań prekompilowanych. | 2 |
| **1.2.8** | Zweryfikuj, że procesory LaTeX są skonfigurowane bezpiecznie (np. bez użycia flagi "--shell-escape") oraz że stosowana jest lista dozwolonych poleceń, aby zapobiec atakom wstrzyknięcia LaTeX. | 2 |
| **1.2.9** | Zweryfikuj, że aplikacja escapuje znaki specjalne w wyrażeniach regularnych (zazwyczaj za pomocą ukośnika wstecznego), aby zapobiec ich błędnej interpretacji jako metaznaków. | 2 |
| **1.2.10** | Zweryfikuj, że aplikacja jest chroniona przed wstrzyknięciem CSV i formuł. Aplikacja musi przestrzegać reguł escapowania zdefiniowanych w RFC 4180, sekcje 2.6 i 2.7, podczas eksportu treści CSV. Dodatkowo przy eksporcie do CSV lub innych formatów arkuszy kalkulacyjnych (takich jak XLS, XLSX czy ODF) znaki specjalne (w tym '=', '+', '-', '@', '\t' (tabulator) oraz '\0' (znak null)) muszą być escapowane pojedynczym cudzysłowem, jeśli występują jako pierwszy znak wartości pola. | 3 |

Uwaga: użycie zapytań parametryzowanych lub escapowanie SQL nie zawsze wystarcza. Części zapytania, takie jak nazwy tabel i kolumn (w tym nazwy kolumn w „ORDER BY”), nie mogą być escapowane. Umieszczenie escapowanych danych pochodzących od użytkownika w tych miejscach skutkuje błędnymi zapytaniami lub wstrzyknięciem SQL.

## V1.3 Sanityzacja

Idealną ochroną przed użyciem niezaufanej treści w niebezpiecznym kontekście jest zastosowanie kodowania lub escapowania właściwego dla kontekstu, które zachowuje semantykę niebezpiecznej treści, czyniąc ją jednocześnie bezpieczną do użycia w danym kontekście — co omówiono szerzej w poprzedniej sekcji.

Tam, gdzie nie jest to możliwe, konieczna staje się sanityzacja, czyli usuwanie potencjalnie niebezpiecznych znaków lub treści. W niektórych przypadkach może to zmienić semantykę danych wejściowych, jednak ze względów bezpieczeństwa może nie być alternatywy.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **1.3.1** | Zweryfikuj, że wszystkie niezaufane dane wejściowe HTML pochodzące z edytorów WYSIWYG lub podobnych są sanityzowane przy użyciu znanej i bezpiecznej biblioteki sanityzacji HTML lub funkcji frameworka. | 1 |
| **1.3.2** | Zweryfikuj, że aplikacja unika użycia eval() oraz innych funkcji dynamicznego wykonywania kodu, takich jak Spring Expression Language (SpEL). Tam, gdzie nie ma alternatywy, wszelkie dołączane dane wejściowe użytkownika muszą zostać zsanityzowane przed wykonaniem. | 1 |
| **1.3.3** | Zweryfikuj, że dane przekazywane do potencjalnie niebezpiecznego kontekstu są wcześniej sanityzowane w celu wymuszenia środków bezpieczeństwa — na przykład dopuszczania wyłącznie znaków bezpiecznych dla tego kontekstu oraz przycinania zbyt długich danych wejściowych. | 2 |
| **1.3.4** | Zweryfikuj, że dostarczana przez użytkownika skryptowalna treść Scalable Vector Graphics (SVG) jest walidowana lub sanityzowana tak, aby zawierała wyłącznie znaczniki i atrybuty bezpieczne dla aplikacji (np. rysujące grafikę), a nie zawierała skryptów ani elementu foreignObject. | 2 |
| **1.3.5** | Zweryfikuj, że aplikacja sanityzuje lub wyłącza dostarczaną przez użytkownika treść skryptowalną lub treść języków szablonów wyrażeń, taką jak Markdown, arkusze stylów CSS lub XSL, BBCode i podobne. | 2 |
| **1.3.6** | Zweryfikuj, że aplikacja chroni przed atakami Server-side Request Forgery (SSRF), walidując niezaufane dane względem listy dozwolonych protokołów, domen, ścieżek i portów oraz sanityzując potencjalnie niebezpieczne znaki przed użyciem danych do wywołania innej usługi. | 2 |
| **1.3.7** | Zweryfikuj, że aplikacja chroni przed atakami wstrzyknięcia szablonu, nie pozwalając na budowanie szablonów na podstawie niezaufanych danych wejściowych. Tam, gdzie nie ma alternatywy, wszelkie niezaufane dane wejściowe dołączane dynamicznie podczas tworzenia szablonu muszą zostać zsanityzowane lub ściśle zwalidowane. | 2 |
| **1.3.8** | Zweryfikuj, że aplikacja odpowiednio sanityzuje niezaufane dane wejściowe przed użyciem w zapytaniach Java Naming and Directory Interface (JNDI) oraz że JNDI jest skonfigurowane bezpiecznie, aby zapobiec atakom wstrzyknięcia JNDI. | 2 |
| **1.3.9** | Zweryfikuj, że aplikacja sanityzuje treść przed wysłaniem jej do memcache, aby zapobiec atakom wstrzyknięcia. | 2 |
| **1.3.10** | Zweryfikuj, że ciągi formatujące, które mogą zostać rozwiązane w nieoczekiwany lub złośliwy sposób, są sanityzowane przed przetworzeniem. | 2 |
| **1.3.11** | Zweryfikuj, że aplikacja sanityzuje dane wejściowe użytkownika przed przekazaniem ich do systemów pocztowych, aby chronić przed wstrzyknięciem SMTP lub IMAP. | 2 |
| **1.3.12** | Zweryfikuj, że wyrażenia regularne są wolne od elementów powodujących wykładniczy backtracking, oraz upewnij się, że niezaufane dane wejściowe są sanityzowane w celu ograniczenia ataków ReDoS lub Runaway Regex. | 3 |

## V1.4 Pamięć, ciągi znaków i kod niezarządzany

Poniższe wymagania dotyczą ryzyk związanych z niebezpiecznym użyciem pamięci, które na ogół mają zastosowanie, gdy aplikacja korzysta z języka systemowego lub kodu niezarządzanego.

W niektórych przypadkach można to osiągnąć, ustawiając flagi kompilatora, które włączają zabezpieczenia i ostrzeżenia przed przepełnieniem bufora — w tym randomizację stosu i zapobieganie wykonywaniu danych — oraz przerywają build w razie wykrycia niebezpiecznych operacji na wskaźnikach, pamięci, ciągach formatujących, liczbach całkowitych lub ciągach znaków.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **1.4.1** | Zweryfikuj, że aplikacja używa bezpiecznych pamięciowo ciągów znaków, bezpieczniejszego kopiowania pamięci i arytmetyki wskaźników, aby wykrywać przepełnienia stosu, bufora lub sterty albo im zapobiegać. | 2 |
| **1.4.2** | Zweryfikuj, że stosowane są techniki walidacji znaku, zakresu i danych wejściowych, aby zapobiegać przepełnieniom liczb całkowitych. | 2 |
| **1.4.3** | Zweryfikuj, że dynamicznie alokowana pamięć i zasoby są zwalniane, a referencje lub wskaźniki do zwolnionej pamięci są usuwane lub ustawiane na null, aby zapobiec wiszącym wskaźnikom i podatnościom typu use-after-free. | 2 |

## V1.5 Bezpieczna deserializacja

Konwersja danych z postaci przechowywanej lub przesyłanej do rzeczywistych obiektów aplikacji (deserializacja) historycznie bywała przyczyną różnych podatności wstrzyknięcia kodu. Proces ten należy przeprowadzać ostrożnie i bezpiecznie, aby uniknąć tego typu problemów.

W szczególności niektóre metody deserializacji zostały wskazane w dokumentacji języków programowania lub frameworków jako niebezpieczne i nie da się ich uczynić bezpiecznymi dla niezaufanych danych. Dla każdego stosowanego mechanizmu należy przeprowadzić staranną analizę due diligence.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **1.5.1** | Zweryfikuj, że aplikacja konfiguruje parsery XML z użyciem restrykcyjnej konfiguracji oraz że niebezpieczne funkcje, takie jak rozwiązywanie encji zewnętrznych, są wyłączone, aby zapobiec atakom XML eXternal Entity (XXE). | 1 |
| **1.5.2** | Zweryfikuj, że deserializacja niezaufanych danych wymusza bezpieczną obsługę danych wejściowych — na przykład poprzez listę dozwolonych typów obiektów lub ograniczenie typów obiektów definiowanych przez klienta — aby zapobiec atakom deserializacji. Mechanizmy deserializacji jawnie określone jako niebezpieczne nie mogą być używane z niezaufanymi danymi wejściowymi. | 2 |
| **1.5.3** | Zweryfikuj, że różne parsery używane w aplikacji dla tego samego typu danych (np. parsery JSON, parsery XML, parsery URL) parsują dane w spójny sposób i używają tego samego mechanizmu kodowania znaków, aby uniknąć problemów takich jak podatności JSON Interoperability lub wykorzystanie odmiennego parsowania URI bądź plików w atakach Remote File Inclusion (RFI) lub Server-side Request Forgery (SSRF). | 3 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
* [OWASP Web Security Testing Guide: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [DOMPurify — biblioteka sanityzacji HTML po stronie klienta](https://github.com/cure53/DOMPurify)
* [RFC 4180 — Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180#section-2)

Więcej informacji, w szczególności o problemach deserializacji i parsowania:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai — A New Era of SSRF: Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
