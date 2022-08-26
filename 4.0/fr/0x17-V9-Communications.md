# V9 Exigences de vérification des communications

## Objectif de contrôle

Assurez-vous qu'une demande vérifiée satisfait aux exigences de haut niveau suivantes :

* Le TLS ou le cryptage fort est toujours utilisé, quelle que soit la sensibilité des données transmises
* Suivez les conseils les plus récents, incluant:
  * les conseils de configuration
  * les algorithmes et les cryptogrammes préférés
* Les algorithmes et les chiffres faibles ou bientôt obsolètes sont commandés en dernier recours
* Les algorithmes et les chiffres non sécurisés, dépréciés ou connus, sont désactivés.

Dans ces exigences :

* Les principaux conseils de l'industrie sur la configuration sécurisée de TLS changent fréquemment, souvent en raison de ruptures catastrophiques dans les algorithmes et les cryptogrammes existants.
* Utilisez toujours les versions les plus récentes des outils de révision de la configuration TLS (tels que SSLyze ou d'autres scanners TLS) pour configurer l'ordre et la sélection d'algorithme préférés.
* La configuration doit être vérifiée périodiquement pour s'assurer que la configuration des communications sécurisées est toujours présente et efficace.

## V9.1 Exigences de sécurité des communications des clients

Toutes les communications avec les clients ne doivent avoir lieu que sur des voies de communication cryptées. En particulier, l'utilisation de TLS 1.2 ou d'une version ultérieure est pratiquement obligatoire pour les navigateurs et les moteurs de recherche modernes. 
La configuration doit être régulièrement revue à l'aide d'outils en ligne afin de s'assurer que les dernières pratiques de pointe sont en place.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.1.1** | Vérifiez que le TLS sécurisé est utilisé pour toutes les connexions des clients et ne revient pas à des protocoles non sécurisés ou non chiffrés. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | Vérifiez à l'aide d'outils de test TLS en ligne ou actualisés que seuls les algorithmes, les chiffrages et les protocoles puissants sont activés, les algorithmes et les chiffrages les plus puissants étant définis de préférence. | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | Vérifiez que seules les dernières versions recommandées du protocole TLS sont activées, telles que TLS 1.2 et TLS 1.3. La dernière version du protocole TLS doit être l'option préférée. | ✓ | ✓ | ✓ | 326 |

## V9.2 Exigences de sécurité des communications du serveur

Les communications entre serveurs ne se limitent pas à HTTP. Des connexions sécurisées vers et depuis d'autres systèmes, tels que les systèmes de surveillance, les outils de gestion, l'accès à distance et ssh, les intergiciels, les bases de données, les ordinateurs centraux, les systèmes partenaires ou sources externes -- doivent être en place. Toutes ces connexions doivent être cryptées pour éviter "d'être difficiles à l'extérieur et trivialement faciles à intercepter à l'intérieur".

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.2.1** | Vérifiez que les connexions vers et depuis le serveur utilisent des certificats TLS de confiance. Lorsque des certificats générés en interne ou auto-signés sont utilisés, le serveur doit être configuré pour ne faire confiance qu'à des AC internes spécifiques et à des certificats auto-signés spécifiques. Tous les autres doivent être rejetés. | | ✓ | ✓ | 295 |
| **9.2.2** | Vérifier que les communications chiffrées telles que TLS sont utilisées pour toutes les connexions entrantes et sortantes, y compris pour les ports de gestion, la surveillance, l'authentification, les appels d'API ou de service web, les connexions de base de données, de nuage, sans serveur, d'ordinateur central, externes et de partenaires. Le serveur ne doit pas se rabattre sur des protocoles non sécurisés ou non chiffrés. | | ✓ | ✓ | 319 |
| **9.2.3** | Vérifiez que toutes les connexions chiffrées à des systèmes externes qui impliquent des informations ou des fonctions sensibles sont authentifiées. | | ✓ | ✓ | 287 |
| **9.2.4** | Vérifiez que la révocation de certification appropriée, telle que le protocol OCSP (Online Certificate Status Protocol), est activée et configurée. | | ✓ | ✓ | 299 |
| **9.2.5** | Vérifiez que les échecs de connexion TLS en arrière-plan sont enregistrés. | | | ✓ | 544 |

## Références

Pour plus d'informations, voir aussi :

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* [OWASP - Pinning Guide](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)
* Remarques sur les « modes approuvés de TLS ». 
    * Dans le passé, l'ASVS faisait référence à la norme américaine FIPS 140-2, mais en tant que norme mondiale, l'application des normes américaines peut être difficile, contradictoire ou déroutante à appliquer. 
    * Une meilleure méthode pour atteindre la conformité avec 9.1.3 consisterait à examiner des guides tels que [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) ou  [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), et utiliser des outils d'évaluation TLS connus, tels que sslyze, divers scanners de vulnérabilité ou des services d'évaluation TLS en ligne fiables pour obtenir le niveau de sécurité souhaité.
