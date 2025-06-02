# V14 Protection de la donnée

## Objectif du contrôle

Les applications ne peuvent pas prendre en compte tous les modèles d’utilisation et comportements des utilisateurs et doivent donc mettre en œuvre des contrôles pour limiter l’accès non autorisé aux données sensibles sur les appareils clients.

Ce chapitre comprend les exigences relatives à la définition des données à protéger, de la manière dont elles doivent être protégées et des mécanismes spécifiques à mettre en œuvre ou des pièges à éviter.

Un autre élément à prendre en compte pour la protection des données est l'extraction massive, la modification ou l'utilisation excessive. Les exigences de chaque système étant probablement très différentes, déterminer ce qui est « anormal » doit tenir compte du modèle de menace et du risque métier. Du point de vue d'ASVS, la détection de ces problèmes est traitée dans le chapitre « Journalisation de sécurité et gestion des erreurs », et la définition de limites dans le chapitre « Validation et logique métier ».

## V14.1 Documentation sur la protection des données

Une condition préalable essentielle à la protection des données est de catégoriser les données considérées comme sensibles. Il existe probablement plusieurs niveaux de sensibilité, et pour chaque niveau, les contrôles requis pour protéger les données seront différents.

Il existe diverses réglementations et lois sur la confidentialité qui régissent la manière dont les applications doivent gérer le stockage, l'utilisation et la transmission des informations personnelles sensibles. Cette section ne vise plus à reproduire ces types de législation sur la protection des données ou la confidentialité, mais se concentre plutôt sur les considérations techniques clés pour la protection des données sensibles. Veuillez consulter les lois et réglementations locales et, si nécessaire, consulter un spécialiste de la confidentialité ou un avocat qualifié.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **14.1.1** | Vérifiez que toutes les données sensibles créées et traitées par l'application ont été identifiées et classées selon leur niveau de protection. Cela inclut les données uniquement codées et donc facilement déchiffrables, telles que les chaînes Base64 ou la charge utile en texte clair d'un JWT. Les niveaux de protection doivent tenir compte des réglementations et normes de protection des données et de confidentialité auxquelles l'application est tenue de se conformer. | 2 | v5.0.be-1.8.1 |
| **14.1.2** | Vérifier que tous les niveaux de protection des données sensibles sont assortis d'un ensemble documenté d'exigences de protection. Cela doit inclure (sans s'y limiter) les exigences relatives au chiffrement général, à la vérification de l'intégrité, à la conservation, à la journalisation des données, aux contrôles d'accès aux données sensibles dans les journaux, au chiffrement au niveau de la base de données, aux technologies de confidentialité et de renforcement de la confidentialité à utiliser, ainsi qu'aux autres exigences de confidentialité. | 2 | v5.0.be-1.8.2 |

## V14.2 Protection générale des données

Cette section présente diverses exigences pratiques relatives à la protection des données. La plupart sont spécifiques à des problématiques particulières, telles que les fuites involontaires de données, mais il existe également une exigence générale de mise en œuvre de contrôles de protection en fonction du niveau de protection requis pour chaque donnée.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **14.2.1** | Vérifiez que les données sensibles sont uniquement envoyées au serveur dans les champs de corps ou d’en-tête du message HTTP, et que l’URL et la chaîne de requête ne contiennent pas d’informations sensibles, telles qu’une clé API ou un jeton de session. | 1 | v5.0.be-8.1.11 |
| **14.2.2** | Vérifiez que l’application empêche la mise en cache des données sensibles dans les composants du serveur, tels que les équilibreurs de charge et les caches d’application, ou garantit que les données sont purgées en toute sécurité après utilisation. | 2 | v5.0.be-8.1.1 |
| **14.2.3** | Vérifiez que les données sensibles définies ne sont pas envoyées à des parties non fiables (par exemple, des trackers d'utilisateurs) pour empêcher la collecte indésirable de données en dehors du contrôle de l'application. | 2 | v5.0.be-8.1.8 |
| **14.2.4** | Vérifiez que les contrôles autour des données sensibles liés au chiffrement, à la vérification de l'intégrité, à la conservation, à la manière dont les données doivent être enregistrées, aux contrôles d'accès autour des données sensibles dans les journaux, à la confidentialité et aux technologies d'amélioration de la confidentialité, sont mis en œuvre comme défini dans la documentation pour le niveau de protection des données spécifiques. | 2 | v5.0.be-8.1.9 |
| **14.2.5** | Vérifiez que les mécanismes de mise en cache sont configurés pour ne mettre en cache que les réponses dont le type de contenu est conforme à la ressource et qui ne contiennent pas de contenu sensible et dynamique. Le serveur web doit renvoyer une réponse 404 ou 302 lors de l'accès à un fichier inexistant plutôt qu'un fichier valide différent. Cela devrait empêcher les attaques par empoisonnement de cache web. | 3 | v5.0.be-8.1.7 |
| **14.2.6** | Vérifiez que l'application ne renvoie que les données sensibles minimales requises pour son fonctionnement. Par exemple, ne renvoyez que certains chiffres d'un numéro de carte de crédit, et non le numéro complet. Si les données complètes sont requises, elles doivent être masquées dans l'interface utilisateur, sauf si l'utilisateur les consulte spécifiquement. | 3 | v5.0.be-8.1.10 |
| **14.2.7** | Vérifiez que les informations sensibles sont soumises à une classification de conservation des données, en veillant à ce que les données obsolètes ou inutiles soient supprimées automatiquement, selon un calendrier défini ou selon les besoins de la situation. | 3 | v5.0.be-8.3.8 |
| **14.2.8** | Vérifiez que les informations sensibles sont supprimées des métadonnées des fichiers soumis par l'utilisateur, sauf si le stockage est autorisé par l'utilisateur. | 3 | v5.0.be-8.3.9 |

## V14.3 Protection des données côté client

Cette section contient des exigences empêchant la fuite de données de manière spécifique du côté client ou de l'agent utilisateur d'une application.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **14.3.1** | Vérifiez que les données authentifiées sont effacées du stockage client, comme le DOM du navigateur, après la fin du client ou de la session. Le champ d'en-tête de réponse HTTP « Clear-Site-Data » peut être utile, mais le côté client devrait également pouvoir effectuer la correction si la connexion au serveur n'est pas disponible à la fin de la session. | 1 | v5.0.be-8.2.3 |
| **14.3.2** | Vérifiez que l'application définit suffisamment de champs d'en-tête de réponse HTTP anti-caching (c'est-à-dire Cache-Control : no-store) afin que les données sensibles ne soient pas mises en cache dans les navigateurs. | 2 | v5.0.be-8.2.1 |
| **14.3.3** | Vérifiez que les données stockées dans le stockage du navigateur (telles que localStorage, sessionStorage, IndexedDB ou les cookies) ne contiennent pas de données sensibles, à l'exception des jetons de session. | 2 | v5.0.be-8.2.2 |

## Références

Pour plus d'informations, voir également :

* [Consider using the Security Headers website to check security and anti-caching header fields](https://securityheaders.com/)
* [Documentation about anti-caching headers by Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [Australian Privacy Principle 11 - Security of personal information](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-11-app-11-security-of-personal-information)
* [European Union General Data Protection Regulation (GDPR) overview](https://www.edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://www.edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
* [Information on the "Clear-Site-Data" header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data)
* [White paper on Web Cache Deception](https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack-wp.pdf)
