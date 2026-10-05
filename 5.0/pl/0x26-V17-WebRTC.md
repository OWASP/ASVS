# V17 WebRTC

## Cel kontrolny

Web Real-Time Communication (WebRTC) umożliwia wymianę głosu, wideo i danych w czasie rzeczywistym w nowoczesnych aplikacjach. Wraz ze wzrostem adopcji zabezpieczenie infrastruktury WebRTC staje się krytyczne. Ta sekcja zawiera wymagania bezpieczeństwa dla interesariuszy, którzy tworzą, hostują lub integrują systemy WebRTC.

Rynek WebRTC można z grubsza podzielić na trzy segmenty:

1. Twórcy produktów: dostawcy rozwiązań własnościowych i open source, którzy tworzą i dostarczają produkty oraz rozwiązania WebRTC. Koncentrują się na rozwijaniu solidnych i bezpiecznych technologii WebRTC, z których mogą korzystać inni.

2. Communication Platforms as a Service (CPaaS): dostawcy oferujący API, SDK oraz niezbędną infrastrukturę lub platformy umożliwiające funkcjonalność WebRTC. Dostawcy CPaaS mogą korzystać z produktów pierwszej kategorii albo rozwijać własne oprogramowanie WebRTC, aby świadczyć te usługi.

3. Dostawcy usług: organizacje, które wykorzystują produkty twórców produktów lub dostawców CPaaS albo rozwijają własne rozwiązania WebRTC. Tworzą i wdrażają aplikacje do konferencji online, ochrony zdrowia, e-learningu i innych dziedzin, w których komunikacja w czasie rzeczywistym jest kluczowa.

Przedstawione tu wymagania bezpieczeństwa są skierowane przede wszystkim do twórców produktów, dostawców CPaaS i dostawców usług, którzy:

* Wykorzystują rozwiązania open source do budowy swoich aplikacji WebRTC.
* Używają komercyjnych produktów WebRTC jako części swojej infrastruktury.
* Korzystają z tworzonych wewnętrznie rozwiązań WebRTC lub integrują różne komponenty w spójną ofertę usługową.

Warto zaznaczyć, że te wymagania bezpieczeństwa nie dotyczą programistów, którzy korzystają wyłącznie z SDK i API dostarczanych przez dostawców CPaaS. W ich przypadku to dostawcy CPaaS zwykle odpowiadają za większość podstawowych kwestii bezpieczeństwa swoich platform, a ogólny standard bezpieczeństwa, taki jak ASVS, może nie w pełni odpowiadać ich potrzebom.

## V17.1 Serwer TURN

Ta sekcja definiuje wymagania bezpieczeństwa dla systemów, które utrzymują własne serwery TURN (Traversal Using Relays around NAT). Serwery TURN pomagają w przekazywaniu mediów w restrykcyjnych środowiskach sieciowych, ale przy błędnej konfiguracji mogą stwarzać ryzyka. Te mechanizmy koncentrują się na bezpiecznym filtrowaniu adresów i ochronie przed wyczerpaniem zasobów.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **17.1.1** | Zweryfikuj, że usługa Traversal Using Relays around NAT (TURN) zezwala na dostęp wyłącznie do adresów IP, które nie są zarezerwowane do celów specjalnych (np. sieci wewnętrzne, broadcast, loopback). Zwróć uwagę, że dotyczy to zarówno adresów IPv4, jak i IPv6. | 2 |
| **17.1.2** | Zweryfikuj, że usługa Traversal Using Relays around NAT (TURN) nie jest podatna na wyczerpanie zasobów, gdy uprawnieni użytkownicy próbują otworzyć dużą liczbę portów na serwerze TURN. | 3 |

## V17.2 Media

Te wymagania dotyczą wyłącznie systemów, które hostują własne serwery mediów WebRTC, takie jak Selective Forwarding Units (SFU), Multipoint Control Units (MCU), serwery nagrywające lub serwery bramek. Serwery mediów obsługują i dystrybuują strumienie mediów, przez co ich bezpieczeństwo jest krytyczne dla ochrony komunikacji między uczestnikami. Ochrona strumieni mediów jest w aplikacjach WebRTC sprawą nadrzędną — zapobiega podsłuchowi, manipulacji i atakom odmowy usługi, które mogłyby naruszyć prywatność użytkowników i jakość komunikacji.

W szczególności konieczne jest wdrożenie zabezpieczeń przed atakami zalewowymi (flood), takich jak ograniczanie częstotliwości żądań, walidacja znaczników czasu, użycie zsynchronizowanych zegarów do dopasowania interwałów czasu rzeczywistego oraz zarządzanie buforami w celu zapobiegania przepełnieniom i utrzymania właściwego taktowania. Jeśli pakiety danej sesji medialnej napływają zbyt szybko, nadmiarowe pakiety powinny być odrzucane. Ważna jest również ochrona systemu przed zniekształconymi pakietami poprzez walidację danych wejściowych, bezpieczną obsługę przepełnień liczb całkowitych, zapobieganie przepełnieniom bufora oraz stosowanie innych solidnych technik obsługi błędów.

Systemy opierające się wyłącznie na komunikacji medialnej peer-to-peer między przeglądarkami, bez udziału pośredniczących serwerów mediów, są wyłączone z tych specyficznych wymagań dotyczących mediów.

Ta sekcja odnosi się do użycia Datagram Transport Layer Security (DTLS) w kontekście WebRTC. Wymaganie dotyczące posiadania udokumentowanej polityki zarządzania kluczami kryptograficznymi znajduje się w rozdziale „Kryptografia”. Informacje o zatwierdzonych metodach kryptograficznych można znaleźć w Załączniku kryptograficznym ASVS albo w dokumentach takich jak NIST SP 800‑52 Rev. 2 lub BSI TR‑02102‑2 (wersja 2025‑01).

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **17.2.1** | Zweryfikuj, że klucz certyfikatu Datagram Transport Layer Security (DTLS) jest zarządzany i chroniony zgodnie z udokumentowaną polityką zarządzania kluczami kryptograficznymi. | 2 |
| **17.2.2** | Zweryfikuj, że serwer mediów jest skonfigurowany do używania i wspierania zatwierdzonych zestawów szyfrów Datagram Transport Layer Security (DTLS) oraz bezpiecznego profilu ochrony dla rozszerzenia DTLS służącego ustanawianiu kluczy dla Secure Real-time Transport Protocol (DTLS-SRTP). | 2 |
| **17.2.3** | Zweryfikuj, że uwierzytelnianie Secure Real-time Transport Protocol (SRTP) jest sprawdzane na serwerze mediów, aby zapobiec sytuacji, w której ataki wstrzyknięcia Real-time Transport Protocol (RTP) prowadzą do odmowy usługi albo wstawienia treści audio lub wideo do strumieni mediów. | 2 |
| **17.2.4** | Zweryfikuj, że serwer mediów jest w stanie kontynuować przetwarzanie przychodzącego ruchu medialnego po napotkaniu zniekształconych pakietów Secure Real-time Transport Protocol (SRTP). | 2 |
| **17.2.5** | Zweryfikuj, że serwer mediów jest w stanie kontynuować przetwarzanie przychodzącego ruchu medialnego podczas zalewu pakietami Secure Real-time Transport Protocol (SRTP) od uprawnionych użytkowników. | 3 |
| **17.2.6** | Zweryfikuj, że serwer mediów nie jest podatny na podatność „ClientHello” Race Condition w Datagram Transport Layer Security (DTLS) — sprawdzając, czy serwer mediów jest publicznie znany jako podatny, albo wykonując test wyścigu. | 3 |
| **17.2.7** | Zweryfikuj, że wszelkie mechanizmy nagrywania audio lub wideo powiązane z serwerem mediów są w stanie kontynuować przetwarzanie przychodzącego ruchu medialnego podczas zalewu pakietami Secure Real-time Transport Protocol (SRTP) od uprawnionych użytkowników. | 3 |
| **17.2.8** | Zweryfikuj, że certyfikat Datagram Transport Layer Security (DTLS) jest sprawdzany względem atrybutu fingerprint Session Description Protocol (SDP), z zakończeniem strumienia mediów w razie niepowodzenia sprawdzenia, aby zapewnić autentyczność strumienia mediów. | 3 |

## V17.3 Sygnalizacja

Ta sekcja definiuje wymagania dla systemów, które utrzymują własne serwery sygnalizacyjne WebRTC. Sygnalizacja koordynuje komunikację peer-to-peer i musi być odporna na ataki mogące zakłócić ustanawianie lub kontrolę sesji.

Aby zapewnić bezpieczną sygnalizację, systemy muszą obsługiwać zniekształcone dane wejściowe w sposób kontrolowany i pozostawać dostępne pod obciążeniem.

| # | Opis | Poziom |
| :---: | :--- | :---: |
| **17.3.1** | Zweryfikuj, że serwer sygnalizacyjny jest w stanie kontynuować przetwarzanie prawidłowych przychodzących komunikatów sygnalizacyjnych podczas ataku zalewowego. Powinno to być osiągnięte poprzez wdrożenie ograniczania częstotliwości żądań na poziomie sygnalizacji. | 2 |
| **17.3.2** | Zweryfikuj, że serwer sygnalizacyjny jest w stanie kontynuować przetwarzanie prawidłowych komunikatów sygnalizacyjnych po napotkaniu zniekształconego komunikatu sygnalizacyjnego, który mógłby spowodować odmowę usługi. Może to obejmować walidację danych wejściowych, bezpieczną obsługę przepełnień liczb całkowitych, zapobieganie przepełnieniom bufora oraz stosowanie innych solidnych technik obsługi błędów. | 2 |

## Źródła

Więcej informacji można znaleźć w następujących materiałach:

* Podatność WebRTC DTLS ClientHello DoS najlepiej dokumentują [wpis na blogu Enable Security skierowany do specjalistów bezpieczeństwa](https://www.enablesecurity.com/blog/novel-dos-vulnerability-affecting-webrtc-media-servers/) oraz powiązany [white paper skierowany do programistów WebRTC](https://www.enablesecurity.com/blog/webrtc-hello-race-conditions-paper/)
* [RFC 3550 - RTP: A Transport Protocol for Real-Time Applications](https://www.rfc-editor.org/rfc/rfc3550)
* [RFC 3711 - The Secure Real-time Transport Protocol (SRTP)](https://datatracker.ietf.org/doc/html/rfc3711)
* [RFC 5764 - Datagram Transport Layer Security (DTLS) Extension to Establish Keys for the Secure Real-time Transport Protocol (SRTP))](https://datatracker.ietf.org/doc/html/rfc5764)
* [RFC 8825 - Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/info/rfc8825)
* [RFC 8826 - Security Considerations for WebRTC](https://www.rfc-editor.org/info/rfc8826)
* [RFC 8827 - WebRTC Security Architecture](https://www.rfc-editor.org/info/rfc8827)
* [DTLS-SRTP Protection Profiles](https://www.iana.org/assignments/srtp-protection/srtp-protection.xhtml)
