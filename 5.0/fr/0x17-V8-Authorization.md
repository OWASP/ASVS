# V8 Autorisation

## Objectif de contrôle

L'autorisation garantit que l'accès est accordé uniquement aux utilisateurs autorisés (utilisateurs, serveurs et autres clients). Pour appliquer le principe du moindre privilège (POLP), les applications vérifiées doivent répondre aux exigences générales suivantes :

* Documenter les règles d'autorisation des documents, y compris les facteurs de prise de décision et les contextes environnementaux.
* Les consommateurs ne devraient avoir accès qu'aux ressources autorisées par leurs droits définis.

## V8.1 Documentation d'autorisation

Une documentation exhaustive des autorisations est essentielle pour garantir que les décisions de sécurité sont appliquées de manière cohérente, vérifiables et conformes aux politiques de l'organisation. Cela réduit le risque d'accès non autorisé en clarifiant les exigences de sécurité et en les rendant applicables aux développeurs, administrateurs et testeurs.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **8.1.1** | Vérifiez que la documentation d’autorisation définit des règles de restriction de l’accès au niveau de la fonction et aux données en fonction des autorisations du consommateur et des attributs des ressources. | 1 |
| **8.1.2** | Vérifiez que la documentation d'autorisation définit les règles de restriction d'accès au niveau des champs (lecture et écriture) en fonction des autorisations des consommateurs et des attributs des ressources. Notez que ces règles peuvent dépendre d'autres valeurs d'attributs de l'objet de données concerné, telles que l'état ou le statut. | 2 |
| **8.1.3** | Vérifiez que la documentation de l'application définit les attributs environnementaux et contextuels (y compris, mais sans s'y limiter, l'heure de la journée, l'emplacement de l'utilisateur, l'adresse IP ou l'appareil) qui sont utilisés dans l'application pour prendre des décisions de sécurité, y compris celles relatives à l'authentification et à l'autorisation. | 3 |
| **8.1.4** | Vérifier que la documentation d'authentification et d'autorisation définit l'utilisation des facteurs environnementaux et contextuels dans la prise de décision, en plus des autorisations au niveau des fonctions, des données et des champs. Cela doit inclure les attributs évalués, les seuils de risque et les actions entreprises (par exemple, autorisation, contestation, refus, renforcement de l'authentification). | 3 |

## V8.2 Conception d'autorisation générale

La mise en œuvre de contrôles d’autorisation granulaires aux niveaux de la fonction, des données et des champs garantis que les consommateurs ne pourront accéder qu’à ce qui leur a été explicitement accordé.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **8.2.1** | Vérifiez que l’application garantit que l’accès basé sur la fonction est limité aux consommateurs disposant d’autorisations explicites. | 1 |
| **8.2.2** | Vérifiez que l'application garantit que l'accès spécifique aux données est limité aux consommateurs disposant d'autorisations explicites sur des éléments de données spécifiques afin d'atténuer les références d'objet directes non sécurisées (IDOR) et les autorisations de niveau d'objet rompues (BOLA). | 1 |
| **8.2.3** | Vérifiez que l'application garantit que l'accès au niveau du champ est limité aux consommateurs disposant d'autorisations explicites sur des champs spécifiques afin d'atténuer les problèmes d'autorisation au niveau de la propriété d'objet (BOPLA). | 2 |
| **8.2.4** | Vérifiez que les contrôles de sécurité adaptatifs basés sur les attributs environnementaux et contextuels du consommateur (tels que l'heure, la localisation, l'adresse IP ou l'appareil) sont mis en œuvre pour les décisions d'authentification et d'autorisation, comme défini dans la documentation de l'application. Ces contrôles doivent être appliqués lorsque le consommateur tente de démarrer une nouvelle session et également pendant une session existante. | 3 |

## V8.3 Autorisation par opération

L'application immédiate des modifications d'autorisation dans le niveau approprié de l'architecture d'une application est essentielle pour empêcher les actions non autorisées, en particulier dans les environnements dynamiques.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **8.3.1** | Vérifier que l'application applique les règles d'autorisations au niveau de la couche service de confiance et ne s’appuie pas sur des contrôles qu’un consommateur non approuvé pourrait manipuler, comme JavaScript côté client. | 1 |
| **8.3.2** | Vérifiez que les modifications apportées aux valeurs sur lesquelles reposent les décisions d'autorisation sont appliquées immédiatement. Lorsque les modifications ne peuvent pas être appliquées immédiatement (par exemple, en s'appuyant sur des données de jetons autonomes), des contrôles d'atténuation doivent être mis en place pour alerter un consommateur lorsqu'il effectue une action alors qu'il n'est plus autorisé à le faire et annuler la modification. Notez que cette solution alternative ne limiterait pas les fuites d'informations. | 3 |
| **8.3.3** | Vérifiez que l'accès à un objet repose sur les autorisations du sujet d'origine (par exemple, le consommateur), et non sur celles d'un intermédiaire ou d'un service agissant en son nom. Par exemple, si un consommateur appelle un service web à l'aide d'un jeton d'authentification autonome, et que ce service demande ensuite des données à un autre service, ce dernier utilisera le jeton du consommateur, plutôt qu'un jeton inter-machine du premier service, pour prendre les décisions d'autorisation. | 3 |

## V8.4 Autres considérations relatives à l'autorisation

Des considérations supplémentaires concernant l’autorisation, en particulier pour les interfaces administratives et les environnements multi-tenants, aident à empêcher tout accès non autorisé.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **8.4.1** | Vérifiez que les applications multi-tenants utilisent des contrôles inter-tenants pour garantir que les opérations des consommateurs n'affecteront jamais les tenants avec lesquels ils ne sont pas autorisés à interagir. | 2 |
| **8.4.2** | Vérifiez que l'accès aux interfaces administratives intègre plusieurs couches de sécurité, notamment la vérification continue de l'identité du consommateur, l'évaluation de la posture de sécurité des appareils et l'analyse contextuelle des risques, garantissant que l'emplacement du réseau ou les endpoints approuvés ne sont pas les seuls facteurs d'autorisation, même s'ils peuvent réduire la probabilité d'accès non autorisé. | 3 |

## Références

Pour plus d'informations, voir également :

* [OWASP Web Security Testing Guide: Authorization](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/05-Authorization_Testing)
* [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
