# V15 Codage et architecture sécurisés

## Objectif du contrôle

De nombreuses exigences ASVS concernent soit un domaine de sécurité particulier, comme l'authentification ou l'autorisation, soit un type de fonctionnalité applicative spécifique, comme la journalisation ou la gestion de fichiers.

Ce chapitre présente toutefois des exigences de sécurité plus générales à prendre en compte lors de la conception et du développement d'applications. Il ne s'agit pas seulement d'une architecture propre et de la qualité du code, mais plutôt des pratiques d'architecture et de codage spécifiques à suivre pour sécuriser l'application.

## V15.1 Documentation sur le codage et l'architecture sécurisés

De nombreuses exigences pour établir une architecture sécurisée et défendable dépendent d'une documentation claire des décisions prises concernant la mise en œuvre de contrôles de sécurité spécifiques et des composants utilisés dans l'application.

Cette section décrit les exigences de documentation à cet égard, notamment l'identification des composants considérés comme contenant des « fonctionnalités dangereuses » ou des « composants à risque ».

Un composant à « fonctionnalité dangereuse » peut être un composant développé en interne ou un composant tiers effectuant des opérations telles que la désérialisation de données non fiables, l'analyse de fichiers bruts ou binaires, l'exécution de code dynamique ou la manipulation directe de la mémoire. Il existe un risque élevé qu'une vulnérabilité dans ces types d'opérations compromette l'application utilisant la fonctionnalité et expose potentiellement son infrastructure sous-jacente.

Un « composant à risque » est une bibliothèque tierce (c'est-à-dire non développée en interne) dont les contrôles de sécurité concernant ses processus de développement ou ses fonctionnalités sont absents ou mal implémentés. Par exemple, les composants mal entretenus, non pris en charge ou en fin de vie présentent un historique de vulnérabilités importantes.

Cette section souligne également l’importance de définir des délais appropriés pour traiter les vulnérabilités des composants tiers.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **15.1.1** | Vérifiez que la documentation de l'application définit les délais de correction basés sur les risques pour les versions de composants tiers présentant des vulnérabilités et pour la mise à jour des bibliothèques en général, afin de minimiser les risques liés à ces composants. | 1 | v5.0.be-1.10.5 |
| **15.1.2** | Vérifiez qu'un catalogue d'inventaire, tel qu'une nomenclature logicielle (SBOM), est conservé pour toutes les bibliothèques tierces utilisées, y compris en vérifiant que les composants proviennent de référentiels prédéfinis, fiables et continuellement maintenus. | 2 | v5.0.be-1.10.2 |
| **15.1.3** | Vérifiez que la documentation de l'application identifie les fonctionnalités chronophages ou gourmandes en ressources. Elle doit notamment indiquer comment prévenir une perte de disponibilité due à une utilisation excessive de ces fonctionnalités et éviter que la génération d'une réponse ne prenne plus de temps que le délai d'expiration du consommateur. Les mesures de protection potentielles peuvent inclure le traitement asynchrone, l'utilisation de files d'attente et la limitation des processus parallèles par utilisateur et par application. | 2 | v5.0.be-1.10.6 |
| **15.1.4** | Vérifiez que la documentation de l’application met en évidence les bibliothèques tierces qui sont considérées comme des « composants à risque ». | 3 | v5.0.be-1.10.3 |
| **15.1.5** | Vérifiez que la documentation de l’application met en évidence les parties de l’application où des « fonctionnalités dangereuses » sont utilisées. | 3 | v5.0.be-1.10.4 |

## V15.2 Architecture de sécurité et dépendances

Cette section inclut les exigences relatives à la gestion des dépendances et des composants risqués, obsolètes ou non sécurisés.

Elle inclut également l'utilisation de techniques architecturales telles que le sandboxing, l'encapsulation, la conteneurisation et l'isolation réseau pour réduire l'impact de l'utilisation d'« opérations dangereuses » ou de « composants risqués » (tels que définis dans la section précédente) et prévenir la perte de disponibilité due à une utilisation excessive de fonctionnalités gourmandes en ressources.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **15.2.1** | Vérifiez que l’application contient uniquement des composants qui n’ont pas dépassé les délais de mise à jour et de correction documentés. | 1 | v5.0.be-10.6.1 |
| **15.2.2** | Vérifiez que l'application a mis en œuvre des défenses contre la perte de disponibilité due à des fonctionnalités qui prennent du temps ou qui nécessitent des ressources, sur la base des décisions et stratégies de sécurité documentées à cet effet. | 2 | v5.0.be-10.6.4 |
| **15.2.3** | Vérifiez que l'environnement de production inclut uniquement les fonctionnalités nécessaires au fonctionnement de l'application et n'expose pas de fonctionnalités superflues telles que du code de test, des exemples d'extraits et des fonctionnalités de développement. | 2 | v5.0.be-14.1.9 |
| **15.2.4** | Vérifiez que les composants tiers et toutes leurs dépendances transitives sont inclus à partir du référentiel attendu, qu'il soit détenu en interne ou qu'il s'agisse d'une source externe, et qu'il n'y a aucun risque d'attaque par confusion de dépendances. | 3 | v5.0.be-10.6.2 |
| **15.2.5** | Vérifiez que l'application implémente des protections supplémentaires autour des parties documentées comme contenant des « fonctionnalités dangereuses » ou utilisant des bibliothèques tierces considérées comme des « composants à risque ». Cela peut inclure des techniques telles que le sandboxing, l'encapsulation, la conteneurisation ou l'isolation au niveau du réseau pour retarder et dissuader les attaquants qui compromettent une partie de l'application de se propager ailleurs. | 3 | v5.0.be-10.6.3 |

## V15.3 Codage défensif

Cette section aborde les types de vulnérabilités, notamment le jonglage de types, la pollution de prototypes et d'autres, résultant de l'utilisation de modèles de codage non sécurisés dans un langage spécifique. Certaines peuvent ne pas être pertinentes pour tous les langages, tandis que d'autres bénéficieront de correctifs spécifiques à chaque langage ou peuvent être liées à la façon dont un langage ou un framework particulier gère une fonctionnalité telle que les paramètres HTTP. Elle aborde également le risque lié à l'absence de validation cryptographique des mises à jour d'applications.

Elle aborde également les risques associés à l'utilisation d'objets pour représenter des éléments de données, ainsi qu'à leur acceptation et leur renvoi via des API externes. Dans ce cas, l'application doit s'assurer que les champs de données non accessibles en écriture ne sont pas modifiés par l'utilisateur (affectation de masse) et que l'API sélectionne les champs de données renvoyés. Lorsque l'accès aux champs dépend des autorisations d'un utilisateur, cela doit être pris en compte dans le contexte de l'exigence de contrôle d'accès au niveau des champs décrite dans le chapitre « Autorisation ».

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **15.3.1** | Vérifiez que l'application ne renvoie que le sous-ensemble requis de champs d'un objet de données. Par exemple, elle ne doit pas renvoyer un objet de données entier, car certains champs individuels ne doivent pas être accessibles aux utilisateurs. | 1 | v5.0.be-10.4.5 |
| **15.3.2** | Vérifiez que lorsque le backend de l'application effectue des appels vers des URL externes, il est configuré pour ne pas suivre les redirections, sauf s'il s'agit d'une fonctionnalité prévue. | 2 | v5.0.be-10.4.8 |
| **15.3.3** | Vérifiez que l'application dispose de contre-mesures pour se protéger contre les attaques d'affectation de masse en limitant les champs autorisés par contrôleur et action, par exemple, il n'est pas possible d'insérer ou de mettre à jour une valeur de champ lorsqu'elle n'était pas destinée à faire partie de cette action. | 2 | v5.0.be-10.4.4 |
| **15.3.4** | Vérifiez que tous les composants proxy et middleware transfèrent correctement l'adresse IP d'origine de l'utilisateur à l'aide de champs de données fiables qui ne peuvent pas être manipulés par l'utilisateur final et que l'application et le serveur Web utilisent cette valeur correcte pour la journalisation et les décisions de sécurité telles que la limitation du débit, en tenant compte du fait que même l'adresse IP d'origine peut ne pas être fiable en raison d'adresses IP dynamiques, de VPN ou de pare-feu d'entreprise. | 2 | v5.0.be-10.4.6 |
| **15.3.5** | Vérifiez que l'application garantit explicitement que les variables sont du type correct et effectue des opérations d'égalité et de comparaison strictes. Cela permet d'éviter les vulnérabilités liées à la confusion de types, causées par des hypothèses du code de l'application sur le type d'une variable. | 2 | v5.0.be-10.4.1 |
| **15.3.6** | Vérifiez que le code JavaScript est écrit de manière à éviter la pollution du prototype, par exemple en utilisant Set() ou Map() au lieu de littéraux d'objet. | 2 | v5.0.be-10.4.3 |
| **15.3.7** | Vérifiez que l'application dispose de défenses contre les attaques de pollution des paramètres HTTP, en particulier si le framework d'application ne fait aucune distinction quant à la source des paramètres de requête (chaîne de requête, paramètres de corps, cookies ou champs d'en-tête). | 2 | v5.0.be-10.4.7 |

## V15.4 Concurrence sécurisée

Les problèmes de concurrence tels que les situations de concurrence, les vulnérabilités TOCTOU (Time-of-Check-to-Time-of-Use), les interblocages, les blocages en direct, la privation de threads et les synchronisations incorrectes peuvent entraîner des comportements imprévisibles et des risques de sécurité. Cette section présente diverses techniques et stratégies pour atténuer ces risques.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **15.4.1** | Vérifiez que les objets partagés dans le code multithread (tels que les caches, les fichiers ou les objets en mémoire accessibles par plusieurs threads) sont accessibles en toute sécurité à l'aide de types thread-safe et de mécanismes de synchronisation tels que des verrous ou des sémaphores pour éviter les conditions de concurrence et la corruption des données. | 3 | v5.0.be-10.7.1, v5.0.be-10.7.2 |
| **15.4.2** | Vérifiez que les vérifications de l'état d'une ressource, comme son existence ou ses autorisations, et des actions qui en dépendent, sont effectuées en une seule opération atomique afin d'éviter les situations de concurrence entre le moment de la vérification et le moment de l'utilisation (TOCTOU). Par exemple, vérifier l'existence d'un fichier avant de l'ouvrir ou l'accès d'un utilisateur avant de l'accorder. | 3 | v5.0.be-10.7.3 |
| **15.4.3** | Vérifiez que les verrous sont utilisés de manière cohérente pour éviter que les threads ne se bloquent, que ce soit en s'attendant les uns les autres ou en réessayant sans fin, et que la logique de verrouillage reste dans le code responsable de la gestion de la ressource pour garantir que les verrous ne peuvent pas être modifiés par inadvertance ou de manière malveillante par des classes ou du code externes. | 3 | v5.0.be-10.7.4, v5.0.be-10.7.6  |
| **15.4.4** | Vérifiez que les politiques d'allocation des ressources empêchent la famine de threads en garantissant un accès équitable aux ressources, par exemple en exploitant les pools de threads, permettant aux threads de priorité inférieure de continuer dans un délai raisonnable. | 3 | v5.0.be-10.7.5 |

## Références

Pour plus d'informations, voir également :

* [Reference on Protecting against DOM Clobbering](https://domclob.xyz/domc_wiki/indicators/patterns.html#secure-patterns--guidelines)
* [OWASP Prototype Pollution Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [Software Component Verification Standard V2 L1-3 requirements](https://github.com/OWASP/Software-Component-Verification-Standard/blob/master/en/0x11-V2-Software_Bill_of_Materials.md)
* [OWASP Testing Guide: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution)
