# V16 Journalisation de sécurité et gestion des erreurs

## Objectif de contrôle

Les journaux de sécurité se distinguent des journaux d'erreurs ou de performances et servent à enregistrer les événements liés à la sécurité, tels que les décisions d'authentification, les décisions de contrôle d'accès et les tentatives de contournement des contrôles de sécurité, comme la validation des entrées ou la validation de la logique métier. Leur objectif est de faciliter la détection, la réponse et l'investigation en fournissant des données structurées et à haut potentiel aux outils d'analyse tels que les SIEM.

Les journaux ne doivent pas contenir de données personnelles sensibles, sauf obligation légale, et toutes les données enregistrées doivent être protégées comme des ressources de grande valeur. La journalisation ne doit pas compromettre la confidentialité ni la sécurité du système. Les applications doivent également être sécurisées, évitant toute divulgation ou interruption inutile.

Pour des conseils de mise en œuvre détaillés, consultez les aide-mémoire de l'OWASP dans la section Références.

## V16.1 Documentation sur la journalisation de sécurité

Cette section garantit un inventaire clair et complet de la journalisation de l'ensemble de la pile applicative. Ceci est essentiel pour une surveillance efficace de la sécurité, une réponse aux incidents et une conformité optimale.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **16.1.1** | Vérifiez qu'il existe un inventaire documentant la journalisation effectuée à chaque couche de la pile technologique de l'application, les événements enregistrés, les formats de journal, l'endroit où cette journalisation est stockée, la manière dont elle est utilisée, la manière dont l'accès à celle-ci est contrôlé et la durée de conservation des journaux. | 2 |

## V16.2 Journalisation générale

Cette section décrit les exigences visant à garantir que les journaux de sécurité sont structurés de manière cohérente et contiennent les métadonnées attendues. L'objectif est de rendre les journaux lisibles et analysables par machine sur tous les systèmes et outils distribués.

Les événements de sécurité impliquent souvent des données sensibles. Si ces données sont enregistrées sans surveillance, les journaux eux-mêmes deviennent classifiés et donc soumis à des exigences de chiffrement, à des politiques de conservation plus strictes et à une divulgation potentielle lors des audits.

Il est donc essentiel de ne consigner que ce qui est nécessaire et de traiter les données des journaux avec le même soin que les autres ressources sensibles.

Les exigences ci-dessous établissent les exigences fondamentales pour la journalisation des métadonnées, la synchronisation, le format et le contrôle.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **16.2.1** | Vérifiez que chaque entrée de journal inclut les métadonnées nécessaires (telles que quand, où, qui, quoi) qui permettraient une enquête détaillée sur la chronologie lorsqu'un événement se produit. | 2 |
| **16.2.2** | Vérifiez que les sources de temps de tous les composants de journalisation sont synchronisées et que les horodatages des métadonnées des événements de sécurité utilisent le temps UTC ou incluent un décalage horaire explicite. L'UTC est recommandé pour garantir la cohérence entre les systèmes distribués et éviter toute confusion lors du passage à l'heure d'été. | 2 |
| **16.2.3** | Vérifiez que l’application stocke ou diffuse uniquement les journaux vers les fichiers et services documentés dans l’inventaire des journaux. | 2 |
| **16.2.4** | Vérifiez que les journaux peuvent être lus et corrélés par le processeur de journaux utilisé, de préférence en utilisant un format de journalisation commun. | 2 |
| **16.2.5** | Vérifiez que l'application applique la journalisation en fonction du niveau de protection des données lors de la journalisation de données sensibles. Par exemple, certaines données, comme les identifiants ou les informations de paiement, peuvent être interdites. D'autres données, comme les jetons de session, ne peuvent être enregistrées que par hachage ou masquage, en totalité ou en partie. | 2 |

## V16.3 Événements de sécurité

Cette section définit les exigences relatives à la journalisation des événements de sécurité au sein de l'application. La capture de ces événements est essentielle pour détecter les comportements suspects, faciliter les enquêtes et respecter les obligations de conformité.

Cette section décrit les types d'événements à journaliser, sans toutefois prétendre à l'exhaustivité. Chaque application présente des facteurs de risque et un contexte opérationnel spécifiques.

Notez que si ASVS inclut la journalisation des événements de sécurité, les alertes et la corrélation (par exemple, les règles SIEM ou l'infrastructure de surveillance) sont considérées comme hors de portée et sont gérées par les systèmes opérationnels et de surveillance.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **16.3.1** | Vérifiez que toutes les opérations d'authentification sont enregistrées, y compris les tentatives réussies et infructueuses. Des métadonnées supplémentaires, telles que le type d'authentification ou les facteurs utilisés, doivent également être collectées. | 2 |
| **16.3.2** | Vérifier que les tentatives d'autorisation infructueuses sont consignées. Pour le niveau 3, cela doit inclure la journalisation de toutes les décisions d'autorisation, y compris lors de l'accès à des données sensibles (sans journalisation des données sensibles elles-mêmes). | 2 |
| **16.3.3** | Vérifiez que l'application enregistre les événements de sécurité définis dans la documentation et enregistre également les tentatives de contournement des contrôles de sécurité, tels que la validation des entrées, la logique métier et l'anti-automatisation. | 2 |
| **16.3.4** | Vérifiez que l’application enregistre les erreurs inattendues et les échecs de contrôle de sécurité tels que les échecs TLS du backend. | 2 |

## V16.4 Protection des journaux

Les journaux sont des artefacts d'investigation précieux et doivent être protégés. S'ils peuvent être facilement modifiés ou supprimés, ils perdent leur intégrité et deviennent peu fiables pour les enquêtes sur les incidents ou les procédures judiciaires. Ils peuvent exposer le comportement interne des applications ou des métadonnées sensibles, ce qui en fait une cible de choix pour les attaquants.

Cette section définit les exigences visant à garantir la protection des journaux contre les accès non autorisés, les falsifications et les divulgations, ainsi que leur transmission et leur stockage sécurisés dans des systèmes sécurisés et isolés.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **16.4.1** | Vérifiez que tous les composants de journalisation codent correctement les données pour empêcher l’injection de journaux. | 2 |
| **16.4.2** | Vérifiez que les journaux sont protégés contre tout accès non autorisé et ne peuvent pas être modifiés. | 2 |
| **16.4.3** | Vérifiez que les journaux sont transmis de manière sécurisée à un système logique distinct pour analyse, détection, alerte et remontée des informations. L'objectif est de garantir qu'en cas de violation de l'application, les journaux ne seront pas compromis. | 2 |

## V16.5 Gestion des erreurs

Cette section définit les exigences visant à garantir que les applications échouent de manière élégante et sécurisée sans divulguer de détails internes sensibles.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **16.5.1** | Vérifiez qu'un message générique est renvoyé au consommateur lorsqu'une erreur inattendue ou sensible à la sécurité se produit, garantissant ainsi l'absence d'exposition de données système internes sensibles telles que les traces de pile, les requêtes, les clés secrètes et les jetons. | 2 |
| **16.5.2** | Vérifiez que l'application continue de fonctionner en toute sécurité lorsque l'accès aux ressources externes échoue, par exemple, en utilisant des modèles tels que des disjoncteurs ou une dégradation progressive. | 2 | v5.0.be-7.4.4 |
| **16.5.3** | Vérifiez que l'application échoue de manière élégante et sécurisée, y compris lorsqu'une exception se produit, en évitant les conditions d'échec d'ouverture telles que le traitement d'une transaction malgré les erreurs résultant de la logique de validation. | 2 |
| **16.5.4** | Vérifiez qu'un gestionnaire d'erreurs de « dernier recours » est défini pour intercepter toutes les exceptions non gérées. Cela permet d'éviter la perte des informations d'erreur qui doivent être consignées dans les fichiers journaux et de garantir qu'une erreur ne paralyse pas l'ensemble du processus applicatif, entraînant une perte de disponibilité. | 3 |

Remarque : Certains langages (dont Swift, Go et, par des pratiques de conception courantes, de nombreux langages fonctionnels) ne prennent pas en charge les exceptions ni les gestionnaires d'événements de dernier recours. Dans ce cas, les architectes et les développeurs doivent utiliser une méthode compatible avec les modèles, les langages ou les frameworks pour garantir que les applications peuvent gérer en toute sécurité les événements exceptionnels, inattendus ou liés à la sécurité.

## Références

Pour plus d'informations, voir également :

* [OWASP Web Security Testing Guide: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
* [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
* [OWASP Application Logging Vocabulary Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html)
