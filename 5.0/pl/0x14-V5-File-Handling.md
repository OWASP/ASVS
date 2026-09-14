# V5 Obsługa plików

## Cel kontrolny

Korzystanie z plików może stwarzać dla aplikacji różnorodne ryzyka, w tym odmowę usługi, nieautoryzowany dostęp i wyczerpanie przestrzeni dyskowej. Niniejszy rozdział zawiera wymagania odnoszące się do tych ryzyk.

## V5.1 Dokumentacja obsługi plików

Ta sekcja zawiera wymaganie udokumentowania oczekiwanych cech plików przyjmowanych przez aplikację — jako niezbędnego warunku wstępnego dla opracowania i weryfikacji odpowiednich kontroli bezpieczeństwa.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **5.1.1** | Zweryfikuj, że dokumentacja definiuje dozwolone typy plików, oczekiwane rozszerzenia plików oraz maksymalny rozmiar (w tym rozmiar po rozpakowaniu) dla każdej funkcji przesyłania plików. Dodatkowo upewnij się, że dokumentacja określa, w jaki sposób pliki są czynione bezpiecznymi do pobierania i przetwarzania przez użytkowników końcowych — na przykład jak aplikacja zachowuje się po wykryciu złośliwego pliku. | 2 |

## V5.2 Przesyłanie plików i ich zawartość

Funkcjonalność przesyłania plików to główne źródło niezaufanych plików. Ta sekcja określa wymagania zapewniające, że obecność, liczba lub zawartość tych plików nie może zaszkodzić aplikacji.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **5.2.1** | Zweryfikuj, że aplikacja przyjmuje wyłącznie pliki o rozmiarze, który jest w stanie przetworzyć bez utraty wydajności lub ataku odmowy usługi. | 1 |
| **5.2.2** | Zweryfikuj, że gdy aplikacja przyjmuje plik — samodzielnie lub w archiwum takim jak plik zip — sprawdza, czy rozszerzenie pliku odpowiada oczekiwanemu rozszerzeniu, oraz waliduje, czy zawartość odpowiada typowi reprezentowanemu przez rozszerzenie. Obejmuje to między innymi sprawdzanie początkowych „magicznych bajtów”, ponowne przetwarzanie obrazów (image re-writing) oraz użycie wyspecjalizowanych bibliotek do walidacji zawartości plików. Dla L1 można skupić się wyłącznie na plikach używanych do podejmowania konkretnych decyzji biznesowych lub dotyczących bezpieczeństwa. Dla L2 i wyżej musi to dotyczyć wszystkich przyjmowanych plików. | 1 |
| **5.2.3** | Zweryfikuj, że aplikacja sprawdza pliki skompresowane (np. zip, gz, docx, odt) względem maksymalnego dozwolonego rozmiaru po dekompresji oraz maksymalnej liczby plików przed rozpakowaniem pliku. | 2 |
| **5.2.4** | Zweryfikuj, że egzekwowany jest przydział rozmiaru plików oraz maksymalna liczba plików na użytkownika, aby pojedynczy użytkownik nie mógł zapełnić przestrzeni dyskowej zbyt wieloma plikami lub plikami nadmiernie dużymi. | 3 |
| **5.2.5** | Zweryfikuj, że aplikacja nie pozwala na przesyłanie plików skompresowanych zawierających dowiązania symboliczne, chyba że jest to wyraźnie wymagane (w takim przypadku konieczne będzie wymuszenie listy dozwolonych plików, do których dowiązania mogą prowadzić). | 3 |
| **5.2.6** | Zweryfikuj, że aplikacja odrzuca przesyłane obrazy o rozmiarze w pikselach większym niż maksymalny dozwolony, aby zapobiec atakom pixel flood. | 3 |

## V5.3 Przechowywanie plików

Ta sekcja zawiera wymagania zapobiegające niewłaściwemu wykonywaniu plików po przesłaniu, służące wykrywaniu niebezpiecznej zawartości oraz uniemożliwiające wykorzystanie niezaufanych danych do kontrolowania miejsca przechowywania plików.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **5.3.1** | Zweryfikuj, że pliki przesłane lub wygenerowane na podstawie niezaufanych danych wejściowych i przechowywane w folderze publicznym nie są wykonywane jako kod programu po stronie serwera przy bezpośrednim dostępie żądaniem HTTP. | 1 |
| **5.3.2** | Zweryfikuj, że gdy aplikacja tworzy ścieżki plików dla operacji na plikach, używa danych generowanych wewnętrznie lub zaufanych zamiast nazw plików przesłanych przez użytkownika — a jeśli nazwy plików lub metadane plików od użytkownika muszą zostać użyte, stosowana jest ścisła walidacja i sanityzacja. Ma to chronić przed atakami path traversal, local i remote file inclusion (LFI, RFI) oraz server-side request forgery (SSRF). | 1 |
| **5.3.3** | Zweryfikuj, że przetwarzanie plików po stronie serwera, takie jak dekompresja, ignoruje informacje o ścieżce dostarczone przez użytkownika, aby zapobiec podatnościom takim jak zip slip. | 3 |

## V5.4 Pobieranie plików

Ta sekcja zawiera wymagania ograniczające ryzyka przy serwowaniu plików do pobrania, w tym ataki path traversal i wstrzyknięcia. Obejmuje również zapewnienie, że pliki nie zawierają niebezpiecznej zawartości.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **5.4.1** | Zweryfikuj, że aplikacja waliduje lub ignoruje nazwy plików przesłane przez użytkownika — w tym w parametrze JSON, JSONP lub URL — oraz określa nazwę pliku w polu nagłówka Content-Disposition w odpowiedzi. | 2 |
| **5.4.2** | Zweryfikuj, że serwowane nazwy plików (np. w polach nagłówków odpowiedzi HTTP lub załącznikach e-mail) są kodowane lub sanityzowane (np. zgodnie z RFC 6266) w celu zachowania struktury dokumentu i zapobieżenia atakom wstrzyknięcia. | 2 |
| **5.4.3** | Zweryfikuj, że pliki pozyskane z niezaufanych źródeł są skanowane przez skanery antywirusowe, aby zapobiec serwowaniu znanej złośliwej zawartości. | 2 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
* [Przykład wykorzystania dowiązań symbolicznych do odczytu dowolnych plików](https://hackerone.com/reports/1439593)
* [Wyjaśnienie „magicznych bajtów” w Wikipedii](https://en.wikipedia.org/wiki/List_of_file_signatures)
