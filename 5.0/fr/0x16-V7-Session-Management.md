# V7 Gestion des sessions

## Objectif du contrôle

Les mécanismes de gestion de session permettent aux applications de corréler les interactions entre utilisateurs et appareils au fil du temps, même avec des protocoles de communication sans état (comme HTTP). Les applications modernes peuvent utiliser plusieurs jetons de session aux caractéristiques et objectifs distincts. Un système de gestion de session sécurisé empêche les attaquants d'obtenir, d'utiliser ou d'abuser de la session d'une victime. Les applications gérant des sessions doivent garantir le respect des exigences de gestion de session de haut niveau suivantes :

* Les sessions sont uniques à chaque individu et ne peuvent être ni devinées ni partagées.
* Les sessions sont invalidées lorsqu'elles ne sont plus nécessaires et expirent en cas d'inactivité.

De nombreuses exigences de ce chapitre concernent des contrôles sélectionnés [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/), axés sur les menaces courantes et les faiblesses d'authentification couramment exploitées.

Notez que les exigences relatives aux détails d’implémentation spécifiques de certains mécanismes de gestion de session peuvent être ailleurs :

* Les cookies HTTP sont un mécanisme courant de sécurisation des jetons de session. Les exigences de sécurité spécifiques aux cookies sont décrites dans le chapitre « Sécurité de l'interface web ».
* Les jetons autonomes sont fréquemment utilisés pour maintenir les sessions. Les exigences de sécurité spécifiques sont décrites dans le chapitre « Jetons autonomes ».

## V7.1 Documentation sur la gestion des sessions

Il n'existe pas de modèle unique convenant à toutes les applications. Il est donc impossible de définir des limites universelles et applicables à tous les cas. Une analyse des risques, accompagnée de décisions de sécurité documentées relatives à la gestion des sessions, doit être réalisée avant la mise en œuvre et les tests. Cela garantit que le système de gestion des sessions est adapté aux exigences spécifiques de l'application.

Que le mécanisme de session choisi soit avec ou sans état, l'analyse doit être complète et documentée afin de démontrer que la solution sélectionnée est capable de satisfaire à toutes les exigences de sécurité pertinentes. L'interaction avec les mécanismes d'authentification unique (SSO) utilisés doit également être prise en compte.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.1.1** | Vérifiez que le délai d'inactivité de la session de l'utilisateur et la durée de vie maximale absolue de la session sont documentés, sont appropriés en combinaison avec d'autres contrôles et que la documentation inclut une justification de tout écart par rapport aux exigences de réauthentification NIST SP 800-63B. | 2 | v5.0.be-1.3.1 |
| **7.1.2** | Vérifiez que la documentation définit le nombre de sessions simultanées (parallèles) autorisées pour un compte ainsi que les comportements et actions prévus à entreprendre lorsque le nombre maximal de sessions actives est atteint. | 2 | v5.0.be-1.3.2 |
| **7.1.3** | Vérifiez que tous les systèmes qui créent et gèrent des sessions utilisateur dans le cadre d'un écosystème de gestion des identités fédérées (tels que les systèmes SSO) sont documentés avec des contrôles pour coordonner la durée de vie des sessions, la résiliation et toute autre condition nécessitant une réauthentification. | 2 | v5.0.be-1.3.3 |

## V7.2 Sécurité fondamentale de la gestion des sessions

Cette section satisfait aux exigences essentielles des sessions sécurisées en vérifiant que les jetons de session sont générés et validés de manière sécurisée.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.2.1** | Vérifiez que l’application effectue toutes les vérifications des jetons de session à l’aide d’un service back-end de confiance. | 1 | v5.0.be-3.1.2 |
| **7.2.2** | Vérifiez que l'application utilise des jetons autonomes ou de référence générés dynamiquement pour la gestion des sessions, c'est-à-dire sans utiliser de secrets et de clés d'API statiques. | 1 | v5.0.be-3.1.3 |
| **7.2.3** | Vérifiez que si des jetons de référence sont utilisés pour représenter les sessions utilisateur, ils sont uniques et générés à l'aide d'un générateur de nombres pseudo-aléatoires cryptographiquement sécurisé (CSPRNG) et possèdent au moins 128 bits d'entropie. | 1 | v5.0.be-3.1.4 |
| **7.2.4** | Vérifiez que l’application génère un nouveau jeton de session lors de l’authentification de l’utilisateur, y compris la réauthentification, et met fin au jeton de session actuel. | 1 | v5.0.be-3.1.5 |

## V7.3 Délai d'expiration de la session

Les mécanismes de temporisation de session servent à minimiser les risques de détournement de session et autres formes d'abus. Les temporisations doivent respecter des décisions de sécurité documentées.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.3.1** | Vérifiez qu’il existe un délai d’inactivité tel que la réauthentification soit appliquée conformément à l’analyse des risques et aux décisions de sécurité documentées. | 2 | v5.0.be-3.3.5 |
| **7.3.2** | Vérifiez qu'il existe une durée de vie maximale absolue de la session de sorte que la réauthentification soit appliquée conformément à l'analyse des risques et aux décisions de sécurité documentées. | 2 | v5.0.be-3.3.2 |

## V7.4 Fin de session

La fin de session peut être gérée soit par l'application elle-même, soit par le fournisseur d'authentification unique (SSO) si ce dernier gère la session à sa place. Il peut être nécessaire de déterminer si le fournisseur d'authentification unique est concerné par les exigences de cette section, car certaines peuvent être contrôlées par lui.

La fin de session doit entraîner une réauthentification et être effective dans l'ensemble de l'application, de la connexion fédérée (si présente) et de toutes les parties utilisatrices.

Pour les mécanismes de session avec état, la terminaison implique généralement l'invalidation de la session sur le serveur principal. Dans le cas de jetons autonomes, des mesures supplémentaires sont nécessaires pour révoquer ou bloquer ces jetons, car ils pourraient sinon rester valides jusqu'à leur expiration.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.4.1** | Vérifiez que lorsque la fin de session est déclenchée (par exemple, déconnexion ou expiration), l'application interdit toute utilisation ultérieure de la session. Pour les jetons de référence ou les sessions avec état, cela implique l'invalidation des données de session au niveau du backend de l'application. Les applications utilisant des jetons autonomes nécessiteront une solution, comme la gestion d'une liste des jetons terminés, l'interdiction des jetons produits avant une date et une heure spécifiques à chaque utilisateur ou la rotation d'une clé de signature spécifique à chaque utilisateur. | 1 | v5.0.be-3.8.1 |
| **7.4.2** | Vérifiez que l'application met fin à toutes les sessions actives lorsqu'un compte utilisateur est désactivé ou supprimé (par exemple, lorsqu'un employé quitte l'entreprise). | 1 | v5.0.be-3.8.4 |
| **7.4.3** | Vérifiez que l'application offre la possibilité de mettre fin à toutes les autres sessions actives après une modification ou une suppression réussie de tout facteur d'authentification (y compris la modification du mot de passe via une réinitialisation ou une récupération et, le cas échéant, une mise à jour des paramètres MFA). | 2 | v5.0.be-3.8.2 |
| **7.4.4** | Vérifiez que toutes les pages nécessitant une authentification disposent d’un accès facile et visible à la fonctionnalité de déconnexion. | 2 | v5.0.be-3.8.3 |
| **7.4.5** | Vérifiez que les administrateurs d’applications sont en mesure de mettre fin aux sessions actives pour un utilisateur individuel ou pour tous les utilisateurs. | 2 | v5.0.be-3.8.5 |

## V7.5 Défenses contre les abus de session

Cette section décrit les exigences visant à atténuer le risque posé par les sessions actives détournées ou utilisées abusivement par des vecteurs s'appuyant sur l'existence et les capacités des sessions utilisateur actives. Par exemple, l'exécution de contenu malveillant pour forcer un navigateur authentifié à effectuer une action en utilisant la session de la victime.

Veuillez noter que les instructions spécifiques au niveau dans le chapitre « Authentification » doivent être prises en compte lors de l'examen des exigences de cette section.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.5.1** | Vérifiez que l'application nécessite une réauthentification complète avant d'autoriser les modifications des attributs de compte sensibles qui peuvent affecter l'authentification, tels que l'adresse e-mail, le numéro de téléphone, la configuration MFA ou d'autres informations utilisées dans la récupération de compte. | 2 | v5.0.be-3.7.1 |
| **7.5.2** | Vérifiez que les utilisateurs peuvent afficher et (après s'être authentifiés à nouveau avec au moins un facteur) terminer une ou toutes les sessions actuellement actives. | 2 | v5.0.be-3.7.2 |
| **7.5.3** | Vérifiez que l’application nécessite une authentification supplémentaire avec au moins un facteur ou une vérification secondaire avant d’effectuer des transactions ou des opérations hautement sensibles. | 3 | v5.0.be-3.7.3 |

## V7.6 Réauthentification fédérée

Cette section s'adresse aux rédacteurs de code de partie utilisatrice (RP) ou de fournisseur d'identité (IdP). Ces exigences découlent de la norme [NIST SP 800-63C](https://pages.nist.gov/800-63-4/sp800-63c.html) relative à la fédération et aux assertions.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **7.6.1** | Vérifiez que la durée de vie et la fin de la session entre les parties de confiance (RP) et les fournisseurs d'identité (IdP) se comportent comme documenté, en exigeant une réauthentification si nécessaire, par exemple lorsque le temps maximal entre les événements d'authentification IdP est atteint. | 2 | v5.0.be-3.6.1 |
| **7.6.2** | Vérifiez que la création d'une session nécessite soit le consentement de l'utilisateur, soit une action explicite, empêchant ainsi la création de nouvelles sessions d'application sans interaction de l'utilisateur. | 2 | v5.0.be-3.6.3 |

## Références

Pour plus d'informations, voir également :

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
