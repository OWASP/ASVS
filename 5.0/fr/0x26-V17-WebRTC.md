# V17 WebRTC

## Objectif du contrôle

La communication Web en temps réel (WebRTC) permet l'échange de voix, de vidéo et de données en temps réel dans les applications modernes. Avec l'adoption croissante de cette technologie, la sécurisation de l'infrastructure WebRTC devient cruciale. Cette section présente les exigences de sécurité pour les acteurs qui développent, hébergent ou intègrent des systèmes WebRTC.

Le marché du WebRTC peut être classé en trois segments :

1. Développeurs de produits : Fournisseurs propriétaires et open source qui créent et fournissent des produits et solutions WebRTC. Leur objectif est de développer des technologies WebRTC robustes et sécurisées, utilisables par d'autres.

2. Plateformes de communication en tant que service (CPaaS) : fournisseurs proposant des API, des SDK et l'infrastructure ou les plateformes nécessaires pour exploiter les fonctionnalités WebRTC. Les fournisseurs CPaaS peuvent utiliser des produits de la première catégorie ou développer leur propre logiciel WebRTC pour offrir ces services.

3. Fournisseurs de services : organisations qui exploitent les produits de développeurs ou de fournisseurs CPaaS, ou qui développent leurs propres solutions WebRTC. Elles créent et implémentent des applications pour les conférences en ligne, la santé, l'apprentissage en ligne et d'autres domaines où la communication en temps réel est essentielle.

Les exigences de sécurité décrites ici s'adressent principalement aux développeurs de produits, aux CPaaS et aux fournisseurs de services qui :

* utilisent des solutions open source pour développer leurs applications WebRTC ;
* utilisent des produits WebRTC commerciaux au sein de leur infrastructure ;
* utilisent des solutions WebRTC développées en interne ou intègrent divers composants dans une offre de services cohérente.

Il est important de noter que ces exigences de sécurité ne s'appliquent pas aux développeurs qui utilisent exclusivement les SDK et les API fournis par les fournisseurs CPaaS. Pour ces développeurs, les fournisseurs CPaaS sont généralement responsables de la plupart des problèmes de sécurité sous-jacents à leurs plateformes, et une norme de sécurité générique comme ASVS peut ne pas répondre pleinement à leurs besoins.

## V17.1 Serveur TURN

Cette section définit les exigences de sécurité pour les systèmes utilisant leurs propres serveurs TURN (Traversal Using Relays around NAT). Les serveurs TURN contribuent au relais des médias dans les environnements réseau restrictifs, mais peuvent présenter des risques en cas de mauvaise configuration. Ces contrôles se concentrent sur le filtrage sécurisé des adresses et la protection contre l'épuisement des ressources.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **17.1.1** | Vérifiez que le service TURN (Traversal Using Relays around NAT) autorise uniquement l'accès aux adresses IP non réservées à des fins spécifiques (par exemple, réseaux internes, diffusion, bouclage). Notez que cela s'applique aux adresses IPv4 et IPv6. | 2 | v5.0.be-53.1.1 |
| **17.1.2** | Vérifiez que le service Traversal Using Relays around NAT (TURN) n'est pas susceptible d'épuiser ses ressources lorsque des utilisateurs légitimes tentent d'ouvrir un grand nombre de ports sur le serveur TURN. | 3 | v5.0.be-53.1.2 |

## V17.2 Média

Ces exigences s'appliquent uniquement aux systèmes hébergeant leurs propres serveurs multimédias WebRTC, tels que les unités de transfert sélectif (SFU), les unités de contrôle multipoint (MCU), les serveurs d'enregistrement ou les serveurs de passerelle. Les serveurs multimédias gèrent et distribuent les flux multimédias, ce qui rend leur sécurité essentielle pour protéger les communications entre homologues. La protection des flux multimédias est primordiale dans les applications WebRTC pour prévenir les écoutes clandestines, les falsifications et les attaques par déni de service susceptibles de compromettre la confidentialité des utilisateurs et la qualité des communications.

En particulier, il est nécessaire de mettre en œuvre des protections contre les attaques par saturation, telles que la limitation du débit, la validation des horodatages, l'utilisation d'horloges synchronisées pour correspondre aux intervalles en temps réel et la gestion des tampons afin d'éviter les débordements et de maintenir une synchronisation correcte. Si les paquets d'une session multimédia spécifique arrivent trop rapidement, les paquets excédentaires doivent être rejetés. Il est également important de protéger le système contre les paquets malformés en implémentant la validation des entrées, en gérant en toute sécurité les dépassements d'entiers, en prévenant les dépassements de tampon et en utilisant d'autres techniques robustes de gestion des erreurs.

Les systèmes qui s'appuient uniquement sur la communication multimédia peer-to-peer entre navigateurs Web, sans l'intervention de serveurs multimédias intermédiaires, sont exclus de ces exigences de sécurité spécifiques liées aux médias.

Cette section traite de l'utilisation de la sécurité de la couche de transport des datagrammes (DTLS) dans le contexte de WebRTC. L'exigence relative à la mise en place d'une politique documentée de gestion des clés cryptographiques est décrite dans le chapitre « Cryptographie ». Des informations sur les méthodes cryptographiques approuvées sont disponibles dans l'annexe Cryptographie de l'ASVS ou dans des documents tels que NIST SP 800-52 Rev. 2 ou BSI TR-02102-2 (version 2025-01).

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **17.2.1** | Vérifiez que la clé du certificat Datagram Transport Layer Security (DTLS) est gérée et protégée conformément à la politique documentée de gestion des clés cryptographiques. | 2 | v5.0.be-53.2.1 |
| **17.2.2** | Vérifiez que le serveur multimédia est configuré pour utiliser et prendre en charge les suites de chiffrement DTLS (Datagram Transport Layer Security) approuvées et un profil de protection sécurisé pour l'extension DTLS pour l'établissement de clés pour le protocole de transport en temps réel sécurisé (DTLS-SRTP). | 2 | v5.0.be-53.2.2 |
| **17.2.3** | Vérifiez que l'authentification SRTP (Secure Real-time Transport Protocol) est vérifiée sur le serveur multimédia pour empêcher les attaques par injection RTP (Real-time Transport Protocol) d'entraîner une condition de déni de service ou l'insertion de médias audio ou vidéo dans les flux multimédias. | 2 | v5.0.be-53.2.4 |
| **17.2.4** | Vérifiez que le serveur multimédia est en mesure de continuer à traiter le trafic multimédia entrant lorsqu'il rencontre des paquets SRTP (Secure Real-time Transport Protocol) mal formés. | 2 | v5.0.be-53.2.7 |
| **17.2.5** | Vérifiez que le serveur multimédia est en mesure de continuer à traiter le trafic multimédia entrant pendant un flot de paquets SRTP (Secure Real-time Transport Protocol) provenant d'utilisateurs légitimes. | 3 | v5.0.be-53.2.5 |
| **17.2.6** | Vérifiez que le serveur multimédia n'est pas sensible à la vulnérabilité de condition de concurrence « ClientHello » dans Datagram Transport Layer Security (DTLS) en vérifiant si le serveur multimédia est publiquement connu comme étant vulnérable ou en effectuant le test de condition de concurrence. | 3 | v5.0.be-53.2.3 |
| **17.2.7** | Vérifiez que tous les mécanismes d'enregistrement audio ou vidéo associés au serveur multimédia sont en mesure de continuer à traiter le trafic multimédia entrant pendant un flot de paquets SRTP (Secure Real-time Transport Protocol) provenant d'utilisateurs légitimes. | 3 | v5.0.be-53.2.6 |
| **17.2.8** | Vérifiez que le certificat Datagram Transport Layer Security (DTLS) est vérifié par rapport à l'attribut d'empreinte digitale du protocole de description de session (SDP), en mettant fin au flux multimédia si la vérification échoue, pour garantir l'authenticité du flux multimédia. | 3 | v5.0.be-53.2.8 |

## V17.3 Signalisation

Cette section définit les exigences pour les systèmes qui exploitent leurs propres serveurs de signalisation WebRTC. La signalisation coordonne les communications pair à pair et doit être résiliente face aux attaques susceptibles de perturber l'établissement ou le contrôle des sessions.

Pour garantir une signalisation sécurisée, les systèmes doivent gérer correctement les entrées malformées et rester disponibles sous charge.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **17.3.1** | Vérifiez que le serveur de signalisation est capable de continuer à traiter les messages de signalisation entrants légitimes lors d'une attaque par saturation. Cela peut être réalisé en implémentant une limitation de débit au niveau de la signalisation. | 2 | v5.0.be-53.3.1 |
| **17.3.2** | Vérifiez que le serveur de signalisation est capable de continuer à traiter les messages de signalisation légitimes en cas de message mal formé susceptible de provoquer un déni de service. Cela peut inclure la validation des entrées, la gestion sécurisée des dépassements d'entiers, la prévention des dépassements de tampon et l'utilisation d'autres techniques robustes de gestion des erreurs. | 2 | v5.0.be-53.3.2 |

## Références

Pour plus d'informations, voir également :

* Le WebRTC DTLS ClientHello DoS est mieux documenté ici : [Enable Security's blog post aimed at security professionals](https://www.enablesecurity.com/blog/novel-dos-vulnerability-affecting-webrtc-media-servers/) et ici [white paper aimed at WebRTC developers](https://www.enablesecurity.com/blog/webrtc-hello-race-conditions-paper/)
* [RFC 3550 - RTP: A Transport Protocol for Real-Time Applications](https://www.rfc-editor.org/rfc/rfc3550)
* [RFC 3711 - The Secure Real-time Transport Protocol (SRTP)](https://datatracker.ietf.org/doc/html/rfc3711)
* [RFC 5764 - Datagram Transport Layer Security (DTLS) Extension to Establish Keys for the Secure Real-time Transport Protocol (SRTP))](https://datatracker.ietf.org/doc/html/rfc5764)
* [RFC 8825 - Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/info/rfc8825)
* [RFC 8826 - Security Considerations for WebRTC](https://www.rfc-editor.org/info/rfc8826)
* [RFC 8827 - WebRTC Security Architecture](https://www.rfc-editor.org/info/rfc8827)
* [DTLS-SRTP Protection Profiles](https://www.iana.org/assignments/srtp-protection/srtp-protection.xhtml)
