# V12 Secure Communication

## Objectif du contrôle

Ce chapitre comprend les exigences relatives aux mécanismes spécifiques qui doivent être mis en place pour protéger les données en transit, à la fois entre un client utilisateur final et un service backend, ainsi qu'entre les services internes et backend.

Les concepts généraux promus par ce chapitre comprennent :

* S’assurer que les communications ne sont pas interceptées par des parties non autorisées grâce à l’utilisation de certificats signés.
* Configurer les mécanismes de chiffrement selon les dernières directives, y compris les algorithmes et chiffrements préférés.
* Vérifier que les communications ne sont pas interceptées par une partie non autorisée à l'aide de certificats signés.

En plus de décrire les principes généraux et les meilleures pratiques, l'ASVS fournit également des informations techniques plus approfondies sur la force cryptographique dans l'annexe V - Normes de cryptographie.

## V12.1 Conseils généraux de sécurité TLS

Cette section fournit des conseils initiaux sur la sécurisation des communications TLS. Des outils à jour doivent être utilisés pour vérifier régulièrement la configuration TLS.

Bien que l'utilisation de certificats TLS génériques ne soit pas intrinsèquement dangereuse, la compromission d'un certificat déployé dans tous les environnements (par exemple, production, préproduction, développement et test) peut compromettre la sécurité des applications qui l'utilisent. Une protection et une gestion appropriées, ainsi que l'utilisation de certificats TLS distincts dans différents environnements, sont recommandées si possible.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **12.1.1** | Vérifiez que seules les dernières versions recommandées du protocole TLS sont activées, telles que TLS 1.2 et TLS 1.3. La dernière version du protocole TLS doit être privilégiée. | 1 |
| **12.1.2** | Vérifiez que seules les suites de chiffrement recommandées sont activées, les suites de chiffrement les plus puissantes étant définies comme préférées. Les applications L3 doivent uniquement prendre en charge les suites de chiffrement assurant la confidentialité persistante. | 2 |
| **12.1.3** | Vérifiez que l’application valide que les certificats clients mTLS sont approuvés avant d’utiliser l’identité du certificat pour l’authentification ou l’autorisation. | 2 |
| **12.1.4** | Vérifiez que la révocation de certification appropriée, telle que l'agrafage du protocole OCSP (Online Certificate Status Protocol), est activée et configurée. | 3 |
| **12.1.5** | Vérifiez que Encrypted Client Hello (ECH) est activé dans les paramètres TLS de l'application pour empêcher l'exposition de métadonnées sensibles, telles que l'indication du nom du serveur (SNI), pendant les processus de négociation TLS. | 3 |

## V12.2 Communication HTTPS avec des services externes

Assurez-vous que tout le trafic HTTP vers les services externes exposés par l'application est envoyé chiffré, avec des certificats de confiance publique.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **12.2.1** | Vérifiez que TLS est utilisé pour toute connectivité entre un client et des services externes basés sur HTTP, et ne recourt pas à des communications non sécurisées ou non chiffrées. | 1 |
| **12.2.2** | Vérifiez que les services externes utilisent des certificats TLS publiquement approuvés. | 1 |

## V12.3 Sécurité des communications entre services généraux

Les communications serveur (internes et externes) ne se limitent pas au protocole HTTP. Les connexions vers et depuis d'autres systèmes doivent également être sécurisées, idéalement via TLS.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **12.3.1** | Vérifiez qu'un protocole chiffré tel que TLS est utilisé pour toutes les connexions entrantes et sortantes vers et depuis l'application, y compris les systèmes de surveillance, les outils de gestion, l'accès à distance et SSH, les intergiciels, les bases de données, les mainframes, les systèmes partenaires ou les API externes. Le serveur ne doit pas recourir à des protocoles non sécurisés ou non chiffrés. | 2 |
| **12.3.2** | Vérifiez que les clients TLS valident les certificats reçus avant de communiquer avec un serveur TLS. | 2 |
| **12.3.3** | Vérifiez que TLS ou un autre mécanisme de chiffrement de transport approprié est utilisé pour toute connectivité entre les services internes basés sur HTTP au sein de l'application et ne revient pas à des communications non sécurisées ou non chiffrées. | 2 |
| **12.3.4** | Vérifiez que les connexions TLS entre les services internes utilisent des certificats de confiance. Lorsque des certificats générés en interne ou auto-signés sont utilisés, le service consommateur doit être configuré pour n'approuver que des autorités de certification internes spécifiques et des certificats auto-signés spécifiques. | 2 |
| **12.3.5** | Vérifiez que les services communiquant en interne au sein d'un système (communications intra-services) utilisent une authentification forte pour garantir la vérification de chaque point de terminaison. Des méthodes d'authentification forte, telles que l'authentification client TLS, doivent être utilisées pour garantir l'identité, en utilisant une infrastructure à clé publique et des mécanismes résistants aux attaques par rejeu. Pour les architectures de microservices, envisagez d'utiliser un maillage de services pour simplifier la gestion des certificats et renforcer la sécurité. | 3 |

## Références

Pour plus d'informations, voir également :

* [OWASP - Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
* [Mozilla's Server Side TLS configuration guide](https://wiki.mozilla.org/Security/Server_Side_TLS)
* [Mozilla's tool to generate known good TLS configurations](https://ssl-config.mozilla.org/).
* [O-Saft - OWASP Project to validate TLS configuration](https://owasp.org/www-project-o-saft/)
