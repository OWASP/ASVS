# V15 Développement et architecture sécurisés

## Objectif du contrôle

De nombreuses exigences pour établir une architecture sécurisée et défendable dépendent d’une documentation claire des décisions prises concernant la mise en œuvre de contrôles de sécurité spécifiques et des composants utilisés dans l’application.

Ce chapitre présente les exigences générales de sécurité à prendre en compte lors de la conception et du développement d'applications. Ces exigences portent non seulement sur une architecture propre et la qualité du code, mais aussi sur les pratiques spécifiques d'architecture et de codage nécessaires à la sécurité des applications.

## V15.1 Documentation sur le développement et l'architecture sécurisés

De nombreuses exigences pour établir une architecture sécurisée et défendable dépendent d’une documentation claire des décisions prises concernant la mise en œuvre de contrôles de sécurité spécifiques et des composants utilisés dans l’application.

Cette section décrit les exigences en matière de documentation, notamment l’identification des composants considérés comme contenant des « fonctionnalités dangereuses » ou comme des « composants à risque ».

Un composant présentant une « fonctionnalité dangereuse » peut être un composant développé en interne ou par un tiers, effectuant des opérations telles que la désérialisation de données non fiables, l'analyse de fichiers bruts ou binaires, l'exécution de code dynamique ou la manipulation directe de la mémoire. Les vulnérabilités dans ces types d'opérations présentent un risque élevé de compromettre l'application et d'exposer potentiellement son infrastructure sous-jacente.

Un « composant à risque » est une bibliothèque tierce (c'est-à-dire non développée en interne) dont les contrôles de sécurité concernant ses processus de développement ou ses fonctionnalités sont absents ou mal implémentés. Il peut s'agir, par exemple, de composants mal entretenus, non pris en charge, en fin de vie ou présentant des antécédents de vulnérabilités importantes.

Cette section souligne également l’importance de définir des délais appropriés pour traiter les vulnérabilités des composants tiers.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **15.1.1** | Vérifiez que la documentation de l'application définit les délais de correction basés sur les risques pour les versions de composants tiers présentant des vulnérabilités et pour la mise à jour des bibliothèques en général, afin de minimiser les risques liés à ces composants. | 1 |
| **15.1.2** | Vérifiez qu'un catalogue d'inventaire, tel qu'une nomenclature logicielle (SBOM), est conservé pour toutes les bibliothèques tierces utilisées, y compris en vérifiant que les composants proviennent de référentiels prédéfinis, fiables et continuellement maintenus. | 2 |
| **15.1.3** | Vérifiez que la documentation de l'application identifie les fonctionnalités chronophages ou gourmandes en ressources. Elle doit notamment indiquer comment prévenir une perte de disponibilité due à une utilisation excessive de ces fonctionnalités et éviter que la génération d'une réponse ne prenne plus de temps que le délai d'expiration du consommateur. Les mesures de protection potentielles peuvent inclure le traitement asynchrone, l'utilisation de files d'attente et la limitation des processus parallèles par utilisateur et par application. | 2 |
| **15.1.4** | Vérifiez que la documentation de l’application met en évidence les bibliothèques tierces qui sont considérées comme des « composants à risque ». | 3 |
| **15.1.5** | Vérifiez que la documentation de l’application met en évidence les parties de l’application où des « fonctionnalités dangereuses » sont utilisées. | 3 |

## V15.2 Architecture de sécurité et dépendances

Cette section inclut les exigences relatives à la gestion des dépendances et des composants risqués, obsolètes ou non sécurisés.

Elle inclut également l'utilisation de techniques au niveau architectural telles que le sandboxing, l'encapsulation, la conteneurisation et l'isolation du réseau pour réduire l'impact de l'utilisation d'« opérations dangereuses » ou de « composants risqués » (tels que définis dans la section précédente) et éviter la perte de disponibilité due à une utilisation excessive de fonctionnalités exigeantes en ressources.

| # | Description | Niveau | 
| :---: | :--- | :---: |
| **15.2.1** | Vérifiez que l’application contient uniquement des composants qui n’ont pas dépassé les délais de mise à jour et de correction documentés. | 1 |
| **15.2.2** | Vérifiez que l'application a mis en œuvre des défenses contre la perte de disponibilité due à des fonctionnalités qui prennent du temps ou qui nécessitent des ressources, sur la base des décisions et stratégies de sécurité documentées à cet effet. | 2 |
| **15.2.3** | Vérifiez que l'environnement de production inclut uniquement les fonctionnalités nécessaires au fonctionnement de l'application et n'expose pas de fonctionnalités superflues telles que du code de test, des exemples d'extraits et des fonctionnalités de développement. | 2 |
| **15.2.4** | Vérifiez que les composants tiers et toutes leurs dépendances transitives sont inclus à partir du référentiel attendu, qu'il soit détenu en interne ou qu'il s'agisse d'une source externe, et qu'il n'y a aucun risque d'attaque par confusion de dépendances. | 3 |
| **15.2.5** | Vérifiez que l'application implémente des protections supplémentaires autour des parties documentées comme contenant des « fonctionnalités dangereuses » ou utilisant des bibliothèques tierces considérées comme des « composants à risque ». Cela peut inclure des techniques telles que le sandboxing, l'encapsulation, la conteneurisation ou l'isolation au niveau du réseau pour retarder et dissuader les attaquants qui compromettent une partie de l'application de se propager ailleurs. | 3 |

## V15.3 Développement défensif

Cette section couvre les types de vulnérabilités, notamment la jonglerie de types, la pollution de prototypes et autres, résultant de l'utilisation de modèles de codage non sécurisés dans un langage particulier. Certaines peuvent ne pas être pertinentes pour tous les langages, tandis que d'autres bénéficieront de correctifs spécifiques à chaque langage ou pourront être liées à la façon dont un langage ou un framework particulier gère une fonctionnalité telle que les paramètres HTTP. Elle aborde également le risque lié à l'absence de validation cryptographique des mises à jour d'applications.

Elle prend également en compte les risques liés à l'utilisation d'objets pour représenter des éléments de données, ainsi qu'à leur acceptation et leur renvoi via des API externes. Dans ce cas, l'application doit s'assurer que les champs de données non accessibles en écriture ne sont pas modifiés par l'utilisateur (affectation de masse) et que l'API sélectionne les champs de données renvoyés. Lorsque l'accès aux champs dépend des autorisations de l'utilisateur, il convient d'en tenir compte dans le contexte des exigences de contrôle d'accès au niveau des champs décrites dans le chapitre « Autorisation ».

| # | Description | Niveau |
| :---: | :--- | :---: |
| **15.3.1** | Vérifiez que l'application ne renvoie que le sous-ensemble requis de champs d'un objet de données. Par exemple, elle ne doit pas renvoyer un objet de données entier, car certains champs individuels ne doivent pas être accessibles aux utilisateurs. | 1 |
| **15.3.2** | Vérifiez que lorsque le backend de l'application effectue des appels vers des URL externes, il est configuré pour ne pas suivre les redirections, sauf s'il s'agit d'une fonctionnalité prévue. | 2 |
| **15.3.3** | Vérifiez que l'application dispose de contre-mesures pour se protéger contre les attaques d'affectation de masse en limitant les champs autorisés par contrôleur et action, par exemple, il n'est pas possible d'insérer ou de mettre à jour une valeur de champ lorsqu'elle n'était pas destinée à faire partie de cette action. | 2 |
| **15.3.4** | Vérifiez que tous les composants proxy et middleware transfèrent correctement l'adresse IP d'origine de l'utilisateur à l'aide de champs de données fiables qui ne peuvent pas être manipulés par l'utilisateur final, et que l'application et le serveur Web utilisent cette valeur correcte pour la journalisation et les décisions de sécurité telles que la limitation du débit, en tenant compte du fait que même l'adresse IP d'origine peut ne pas être fiable en raison d'adresses IP dynamiques, de VPN ou de pare-feu d'entreprise. | 2 |
| **15.3.5** | Vérifiez que l'application garantit explicitement que les variables sont du type correct et effectue des opérations d'égalité et de comparaison strictes. Cela permet d'éviter les vulnérabilités liées à la confusion de types, causées par des hypothèses du code de l'application sur le type d'une variable. | 2 |
| **15.3.6** | Vérifiez que le code JavaScript est écrit de manière à éviter la pollution du prototype, par exemple en utilisant Set() ou Map() au lieu de littéraux d'objet. | 2 |
| **15.3.7** | Vérifiez que l'application dispose de défenses contre les attaques de pollution des paramètres HTTP, en particulier si le framework d'application ne fait aucune distinction quant à la source des paramètres de requête (chaîne de requête, paramètres de corps, cookies ou champs d'en-tête). | 2 |

## V15.4 Concurrence sécurisée

Les problèmes de concurrence tels que les situations de concurrence, les vulnérabilités TOCTOU (Time-of-Check-to-Time-of-Use), les interblocages, les blocages en direct, la privation de threads et les synchronisations incorrectes peuvent entraîner des comportements imprévisibles et des risques de sécurité. Cette section présente diverses techniques et stratégies pour atténuer ces risques.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **15.4.1** | Vérifiez que les objets partagés dans le code multithread (tels que les caches, les fichiers ou les objets en mémoire accessibles par plusieurs threads) sont accessibles en toute sécurité à l'aide de types thread-safe et de mécanismes de synchronisation tels que des verrous ou des sémaphores pour éviter les conditions de concurrence et la corruption des données. | 3 |
| **15.4.2** | Vérifiez que les vérifications de l'état d'une ressource, comme son existence ou ses autorisations, et des actions qui en dépendent, sont effectuées en une seule opération atomique afin d'éviter les situations de concurrence entre le moment de la vérification et le moment de l'utilisation (TOCTOU). Par exemple, vérifier l'existence d'un fichier avant de l'ouvrir ou l'accès d'un utilisateur avant de l'accorder. | 3 |
| **15.4.3** | Vérifiez que les verrous sont utilisés de manière cohérente pour éviter que les threads ne se bloquent, que ce soit en s'attendant les uns les autres ou en réessayant sans fin, et que la logique de verrouillage reste dans le code responsable de la gestion de la ressource pour garantir que les verrous ne peuvent pas être modifiés par inadvertance ou de manière malveillante par des classes ou du code externes. | 3 |
| **15.4.4** | Vérifiez que les politiques d'allocation des ressources empêchent la saturation de threads en garantissant un accès équitable aux ressources, par exemple en exploitant les pools de threads, permettant aux threads de priorité inférieure de continuer dans un délai raisonnable. | 3 |

## Références

Pour plus d'informations, voir également :

* [OWASP Prototype Pollution Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [OWASP CycloneDX Bill of Materials Specification](https://owasp.org/www-project-cyclonedx/)
* [OWASP Web Security Testing Guide: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution)
