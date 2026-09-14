# V9 Tokeny samowystarczalne

## Cel kontrolny

Pojęcie tokena samowystarczalnego pojawia się już w pierwotnym RFC 6749 OAuth 2.0 z 2012 roku. Odnosi się do tokena zawierającego dane lub oświadczenia, na których usługa odbierająca będzie polegać przy podejmowaniu decyzji bezpieczeństwa. Należy go odróżnić od prostego tokena zawierającego wyłącznie identyfikator, na podstawie którego usługa odbierająca wyszukuje dane lokalnie. Najczęstsze przykłady tokenów samowystarczalnych to JSON Web Tokens (JWT) oraz asercje SAML.

Stosowanie tokenów samowystarczalnych stało się bardzo powszechne, również poza OAuth i OIDC. Jednocześnie bezpieczeństwo tego mechanizmu opiera się na zdolności walidacji integralności tokena oraz zapewnieniu, że token jest ważny w danym kontekście. W procesie tym istnieje wiele pułapek, a niniejszy rozdział szczegółowo opisuje mechanizmy, które aplikacje powinny wdrożyć, aby ich uniknąć.

## V9.1 Źródło i integralność tokena

Ta sekcja zawiera wymagania zapewniające, że token został wytworzony przez zaufaną stronę i nie został zmanipulowany.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **9.1.1** | Zweryfikuj, że tokeny samowystarczalne są walidowane z użyciem ich podpisu cyfrowego lub kodu MAC w celu ochrony przed manipulacją, zanim zawartość tokena zostanie zaakceptowana. | 1 |
| **9.1.2** | Zweryfikuj, że do tworzenia i weryfikacji tokenów samowystarczalnych w danym kontekście mogą być używane wyłącznie algorytmy z listy dozwolonych. Lista dozwolonych musi zawierać dopuszczone algorytmy — najlepiej wyłącznie symetryczne albo wyłącznie asymetryczne — i nie może zawierać algorytmu 'None'. Jeśli muszą być wspierane zarówno algorytmy symetryczne, jak i asymetryczne, konieczne będą dodatkowe mechanizmy zapobiegające pomyleniu kluczy (key confusion). | 1 |
| **9.1.3** | Zweryfikuj, że materiał klucza używany do walidacji tokenów samowystarczalnych pochodzi z zaufanych, wstępnie skonfigurowanych źródeł dla danego wystawcy tokena, uniemożliwiając atakującym wskazanie niezaufanych źródeł i kluczy. Dla JWT i innych struktur JWS nagłówki takie jak 'jku', 'x5u' i 'jwk' muszą być walidowane względem listy dozwolonych zaufanych źródeł. | 1 |

## V9.2 Zawartość tokena

Przed podjęciem decyzji bezpieczeństwa na podstawie zawartości tokena samowystarczalnego konieczna jest walidacja, że token został przedstawiony w swoim okresie ważności oraz że jest przeznaczony do użytku przez usługę odbierającą i w celu, w jakim został przedstawiony. Pomaga to uniknąć niebezpiecznego użycia krzyżowego między różnymi usługami lub z różnymi typami tokenów od tego samego wystawcy.

Szczegółowe wymagania dla OAuth i OIDC omówiono w dedykowanym rozdziale.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **9.2.1** | Zweryfikuj, że jeśli w danych tokena obecny jest przedział czasu ważności, token i jego zawartość są akceptowane tylko wtedy, gdy czas weryfikacji mieści się w tym przedziale. Na przykład dla JWT muszą być weryfikowane oświadczenia 'nbf' i 'exp'. | 1 |
| **9.2.2** | Zweryfikuj, że usługa odbierająca token waliduje, czy token jest właściwego typu i przeznaczony do zamierzonego celu, zanim zaakceptuje jego zawartość. Na przykład do decyzji autoryzacyjnych mogą być akceptowane wyłącznie tokeny dostępu, a do potwierdzania uwierzytelnienia użytkownika — wyłącznie tokeny ID. | 2 |
| **9.2.3** | Zweryfikuj, że usługa akceptuje wyłącznie tokeny przeznaczone do użytku z tą usługą (audience). Dla JWT można to osiągnąć, walidując oświadczenie 'aud' względem listy dozwolonych zdefiniowanej w usłudze. | 2 |
| **9.2.4** | Zweryfikuj, że jeśli wystawca tokenów używa tego samego klucza prywatnego do wystawiania tokenów dla różnych odbiorców (audiences), wystawiane tokeny zawierają ograniczenie odbiorcy jednoznacznie identyfikujące zamierzonych odbiorców. Zapobiegnie to ponownemu użyciu tokena z niezamierzonym odbiorcą. Jeśli identyfikator odbiorcy jest przydzielany dynamicznie, wystawca tokenów musi walidować tych odbiorców, aby upewnić się, że nie prowadzi to do podszywania się pod odbiorcę. | 2 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP JSON Web Token Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)
