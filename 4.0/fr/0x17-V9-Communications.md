# V9 : Exigences de vérification des communications

## Objectif de contrôle

Assurez-vous qu'une demande vérifiée satisfait aux exigences de haut niveau suivantes :

* Le TLS ou le cryptage fort est toujours utilisé, quelle que soit la sensibilité des données transmises
* Les conseils de configuration les plus récents et les plus importants sont utilisés pour activer et ordonner les algorithmes et les chiffres préférés
* Les algorithmes et les chiffres faibles ou bientôt obsolètes sont commandés en dernier recours
* Les algorithmes et les chiffres non sécurisés, dépréciés ou connus, sont désactivés.

Les principaux conseils de l'industrie sur la configuration sécurisée de TLS changent fréquemment, souvent en raison de ruptures catastrophiques dans les algorithmes et les chiffres existants. Utilisez toujours les versions les plus récentes des outils de révision de la configuration TLS (tels que SSLyze ou d'autres scanners TLS) pour configurer l'ordre et la sélection d'algorithme préférés. La configuration doit être vérifiée périodiquement pour s'assurer que la configuration des communications sécurisées est toujours présente et efficace.

## V9.1 Exigences de sécurité des communications des clients

Toutes les communications avec les clients ne doivent avoir lieu que sur des voies de communication cryptées. En particulier, l'utilisation de TLS 1.2 ou d'une version ultérieure est pratiquement obligatoire pour les navigateurs et les moteurs de recherche modernes. La configuration doit être régulièrement revue à l'aide d'outils en ligne afin de s'assurer que les dernières pratiques de pointe sont en place.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.1.1** | Vérifiez que le TLS sécurisé est utilisé pour toutes les connexions des clients et ne revient pas à des protocoles non sécurisés ou non chiffrés. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | Vérifiez à l'aide d'outils de test TLS en ligne ou actualisés que seuls les algorithmes, les chiffrages et les protocoles puissants sont activés, les algorithmes et les chiffrages les plus puissants étant définis de préférence. | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | Vérifiez que les anciennes versions des protocoles SSL et TLS, des algorithmes, des chiffres et de la configuration sont désactivées, comme SSLv2, SSLv3, ou TLS 1.0 et TLS 1.1. La dernière version de TLS doit être la suite de chiffrement préférée. | ✓ | ✓ | ✓ | 326 |
| **9.1.4** | Pour les applications de client lourd, vérifiez que l'application utilise son propre magasin de certificats, ou qu'elle épingle le certificat ou la clé publique du terminal, et qu'elle n'établira pas de connexion avec des terminaux qui offrent un certificat ou une clé différente, même si elle est signée par une AC de confiance. | | | ✓ | 295 |

## V9.2 Exigences de sécurité des communications du serveur

Les communications entre serveurs ne se limitent pas à HTTP. Des connexions sécurisées vers et depuis d'autres systèmes, tels que les systèmes de surveillance, les outils de gestion, l'accès à distance et ssh, les intergiciels, les bases de données, les ordinateurs centraux, les systèmes partenaires ou sources externes -- doivent être en place. Toutes ces connexions doivent être cryptées pour éviter "d'être difficiles à l'extérieur et trivialement faciles à intercepter à l'intérieur".

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.2.1** | Vérifiez que les connexions vers et depuis le serveur utilisent des certificats TLS de confiance. Lorsque des certificats générés en interne ou auto-signés sont utilisés, le serveur doit être configuré pour ne faire confiance qu'à des AC internes spécifiques et à des certificats auto-signés spécifiques. Tous les autres doivent être rejetés. | | ✓ | ✓ | 295 |
| **9.2.2** | Vérifier que les communications cryptées telles que TLS sont utilisées pour toutes les connexions entrantes et sortantes, y compris pour les ports de gestion, la surveillance, l'authentification, les appels d'API ou de service web, les connexions de base de données, de nuage, sans serveur, d'ordinateur central, externes et de partenaires. Le serveur ne doit pas se rabattre sur des protocoles non sécurisés ou non chiffrés. | | ✓ | ✓ | 319 |
| **9.2.3** | Vérifiez que toutes les connexions cryptées à des systèmes externes qui impliquent des informations ou des fonctions sensibles sont authentifiées. | | ✓ | ✓ | 287 |
| **9.2.4** | Vérifiez que la révocation de certification appropriée, telle que le protocol OCSP (Online Certificate Status Protocol), est activée et configurée. | | ✓ | ✓ | 299 |
| **9.2.5** | Vérifiez que les échecs de connexion TLS en arrière-plan sont enregistrés. | | | ✓ | 544 |

## Références

Pour plus d'informations, voir aussi :

*  [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
*  [OWASP - Pinning Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Pinning_Cheat_Sheet.html)
*  Notes on “Approved modes of TLS”. In the past, the ASVS referred to the US standard FIPS 140-2, but as a global standard, applying US standards can be difficult, contradictory, or confusing to apply. A better method of achieving compliance with 9.1.3 would be to review guides such as [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) or  [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), and use known TLS evaluation tools, such as sslyze, various vulnerability scanners or trusted TLS online assessment services to obtain a desired level of security. In general, we see non-compliance for this section being the use of outdated or insecure ciphers and algorithms, the lack of perfect forward secrecy, outdated or insecure SSL protocols, weak preferred ciphers, and so on.
