# Qu'est-ce que l'ASVS ?

Le Référentiel de vérification de la sécurité des applications (ASVS) définit des exigences de sécurité pour les applications et services web. Elle constitue une ressource précieuse pour quiconque souhaite concevoir, développer et maintenir des applications sécurisées ou évaluer leur sécurité.

Ce chapitre décrit les aspects essentiels de l'utilisation de l'ASVS, notamment son champ d'application, la structure de ses niveaux de priorité et ses principaux cas d'utilisation.

## Portée de l'ASVS

La portée de l'ASVS est définie par son nom : Application, Sécurité, Vérification et Référentiel. Elle établit les exigences incluses ou exclues, avec pour objectif principal d'identifier les principes de sécurité à respecter. Elle prend également en compte les exigences de documentation, qui servent de base aux exigences de mise en œuvre.

Il n'existe aucune portée pour les attaquants. Par conséquent, les exigences de l'ASVS doivent être évaluées parallèlement aux recommandations relatives aux autres aspects du cycle de vie des applications, notamment les processus CI/CD, l'hébergement et les activités opérationnelles.

### Application

ASVS définit une « application » comme le produit logiciel en cours de développement, dans lequel des contrôles de sécurité doivent être intégrés. ASVS ne prescrit pas les activités du cycle de développement ni la manière dont l'application doit être construite via un pipeline CI/CD ; il spécifie plutôt les résultats de sécurité à atteindre au sein même du produit.

Les composants qui traitent, modifient ou valident le trafic HTTP, tels que les pares-feux d'applications web (WAF), les équilibreurs de charge ou les proxys, peuvent être considérés comme faisant partie de l'application à ces fins spécifiques, car certains contrôles de sécurité en dépendent directement ou peuvent être implémentés par leur intermédiaire. Ces composants doivent être pris en compte pour les exigences liées aux réponses mises en cache, à la limitation du débit ou à la restriction des connexions entrantes et sortantes en fonction de la source et de la destination.

À l'inverse, ASVS exclut généralement les exigences qui ne concernent pas directement l'application ou dont la configuration ne relève pas de sa responsabilité. Par exemple, les problèmes DNS sont généralement gérés par une équipe ou une fonction distincte.

De même, si l'application est responsable de la manière dont elle consomme les entrées et produit les sorties, l'interaction d'un processus externe avec l'application ou ses données est considérée comme hors du champ d'application d'ASVS. Par exemple, la sauvegarde de l'application ou de ses données relève généralement de la responsabilité d'un processus externe et n'est pas contrôlée par l'application ou ses développeurs.

### Sécurité

Chaque exigence doit avoir un impact démontrable sur la sécurité. L'absence d'exigence doit entraîner une application moins sécurisée, et sa mise en œuvre doit réduire la probabilité ou l'impact d'un risque de sécurité.

Toutes les autres considérations, telles que les aspects fonctionnels, le style de code ou les exigences de politique, sont hors du champ d'application.

### Vérification

L'exigence doit être vérifiable et la vérification doit aboutir à une décision d'échec ou de réussite.

### Référentiel

L'ASVS est conçue comme un recueil d'exigences de sécurité à mettre en œuvre pour se conformer au référentiel. Cela signifie que les exigences se limitent à la définition de l'objectif de sécurité à atteindre. D'autres informations connexes peuvent être intégrées à l'ASVS ou reliées par des mappings.

Plus précisément, l'OWASP comporte de nombreux projets, et l'ASVS évite délibérément tout chevauchement avec le contenu d'autres projets. Par exemple, les développeurs peuvent se demander : « Comment implémenter une exigence particulière dans ma technologie ou mon environnement ? » Cette question devrait être traitée par le projet « Cheat-Sheets ». Les vérificateurs peuvent se demander : « Comment tester cette exigence dans cet environnement ? » Cette question devrait être traitée par le projet « Web Security Testing Guide ».

Bien que l'ASVS ne soit pas uniquement destiné aux experts en sécurité, il attend du lecteur des connaissances techniques pour comprendre le contenu ou la capacité à rechercher des concepts spécifiques.

### Exigence

Le terme « exigence » est utilisé spécifiquement dans l'ASVS car il décrit ce qui doit être accompli pour la satisfaire. L'ASVS ne contient que des exigences (doit) et ne contient pas de recommandations (devrait) comme condition principale.

En d'autres termes, les recommandations, qu'elles constituent une solution parmi d'autres ou des considérations de style de code, ne répondent pas à la définition d'une exigence.

Les exigences de l'ASVS visent à répondre à des principes de sécurité spécifiques sans être trop spécifiques à une implémentation ou à une technologie, tout en étant explicites quant à leur raison d'être. Cela signifie également que les exigences ne sont pas construites autour d'une méthode de vérification ou d'une implémentation particulière.

### Décisions de sécurité documentées

En matière de sécurité logicielle, planifier la conception de la sécurité et les mécanismes à utiliser en amont permettra une implémentation plus cohérente et fiable du produit fini ou de la fonctionnalité.

De plus, pour certaines exigences, la mise en œuvre sera complexe et très spécifique aux besoins de l'application. Parmi les exemples courants, on peut citer les autorisations, la validation des entrées et les contrôles de protection autour de différents niveaux de données sensibles.

Pour tenir compte de cela, plutôt que de formuler des affirmations générales telles que « toutes les données doivent être chiffrées » ou de tenter de couvrir tous les cas d'utilisation possibles dans une exigence, des exigences de documentation ont été incluses, exigeant que l'approche et la configuration du développeur d'applications pour ces types de contrôles soient documentées. Ceci peut ensuite être vérifié pour en vérifier la pertinence, puis la mise en œuvre réelle peut être comparée à la documentation afin d'évaluer si elle répond aux attentes.

Ces exigences visent à documenter les décisions prises par l'organisation développant l'application concernant la mise en œuvre de certaines exigences de sécurité.

Les exigences de documentation figurent toujours dans la première section d'un chapitre (bien que tous les chapitres n'en disposent pas) et sont toujours associées à une exigence de mise en œuvre, où les décisions documentées doivent être effectivement mises en œuvre. L'essentiel est de distinguer la vérification de la documentation et de la mise en œuvre effective.

L'inclusion de ces exigences repose sur deux facteurs clés. Le premier est qu'une exigence de sécurité implique souvent l'application de règles, par exemple concernant les types de fichiers autorisés à être téléchargés, les contrôles métier à appliquer et les caractères autorisés pour un champ particulier. Ces règles diffèrent d'une application à l'autre ; par conséquent, l'ASVS ne peut pas les définir de manière prescriptive, et un aide-mémoire ou une réponse plus détaillée ne serait d'aucune utilité dans ce cas précis. De même, sans documentation de ces décisions, il sera impossible de vérifier les exigences qui les mettent en œuvre.

Le deuxième facteur est que, pour certaines exigences, il est important d'offrir au développement d'applications une certaine flexibilité quant à la manière de répondre à des défis de sécurité particuliers. Par exemple, dans les versions précédentes d'ASVS, les règles d'expiration de session étaient très strictes. En pratique, de nombreuses applications, notamment celles destinées aux utilisateurs, ont des règles beaucoup plus souples et préfèrent mettre en œuvre d'autres contrôles d'atténuation. Les exigences de documentation permettent donc explicitement cette flexibilité.

Il est clair que les développeurs ne sont pas censés prendre et documenter ces décisions individuellement, mais que l'organisation dans son ensemble les prend et s'assure qu'elles sont communiquées aux développeurs, qui s'assurent ensuite de les respecter.

Fournir aux développeurs des spécifications et des conceptions pour de nouvelles fonctionnalités est une étape standard du développement logiciel. De même, les développeurs sont censés utiliser des composants et des mécanismes d'interface utilisateur communs plutôt que de prendre leurs propres décisions à chaque fois. Par conséquent, étendre ce principe à la sécurité ne devrait pas être perçu comme surprenant ou controversé.

La manière d'y parvenir est également flexible. Les décisions de sécurité peuvent être documentées dans un document littéral, auquel les développeurs sont tenus de se référer. Alternativement, elles peuvent être documentées et implémentées dans une bibliothèque de code commune que tous les développeurs sont tenus d'utiliser. Dans les deux cas, le résultat souhaité est atteint.

## Niveaux de vérification de la sécurité des applications

L'ASVS définit trois niveaux de vérification de la sécurité, chaque niveau augmentant en profondeur et en complexité. L'objectif général est que les organisations commencent par le premier niveau pour répondre aux préoccupations de sécurité les plus critiques, puis progressent vers les niveaux supérieurs en fonction des besoins de l'organisation et des applications. Les niveaux peuvent être présentés comme L1, L2 et L3 dans le document et dans les textes d'exigences.

Chaque niveau ASVS indique les exigences de sécurité à atteindre à partir de ce niveau, les exigences des niveaux supérieurs restants étant des recommandations.

Afin d'éviter les doublons ou les exigences obsolètes aux niveaux supérieurs, certaines exigences s'appliquent à un niveau particulier, mais sont soumises à des conditions plus strictes pour les niveaux supérieurs.

### Évaluation des niveaux

Les niveaux sont définis par une évaluation de priorité de chaque exigence, basée sur l'expérience de mise en œuvre et de test des exigences de sécurité. L'accent est mis principalement sur la balance entre la réduction des risques et les efforts nécessaires à la mise en œuvre de l'exigence. Un autre facteur clé est de maintenir une faible barrière à l'entrée.

La réduction des risques évalue dans quelle mesure l'exigence réduit le niveau de risque de sécurité au sein de l'application, en tenant compte des facteurs d'impact classiques de confidentialité, d'intégrité et de disponibilité, et en déterminant s'il s'agit d'une couche de défense principale ou d'une défense en profondeur.

Les discussions rigoureuses autour des critères et des décisions de nivellement ont abouti à une répartition qui devrait s'appliquer à la grande majorité des cas, tout en admettant qu'elle ne soit pas parfaitement adaptée à toutes les situations. Cela signifie que, dans certains cas, les organisations peuvent souhaiter prioriser les exigences d'un niveau supérieur en amont, en fonction de leurs propres considérations de risque.

Les types d'exigences à chaque niveau peuvent être caractérisés comme suit.

### Niveau 1

Ce niveau contient les exigences minimales à prendre en compte pour sécuriser une application et constitue un point de départ essentiel. Il comprend environ 20 % des exigences de l'ASVS. L'objectif est de réduire au minimum les exigences afin de réduire les obstacles à l'entrée.

Ces exigences sont généralement critiques ou basiques, et constituent la première couche de défense pour prévenir les attaques courantes. Elles ne nécessitent pas d'autres vulnérabilités ou conditions préalables pour être exploitables.

Outre les exigences de la première couche de défense, certaines exigences ont moins d'impact aux niveaux supérieurs, comme celles relatives aux mots de passe. Celles-ci sont plus importantes pour le Niveau 1, car à partir de ces niveaux, les exigences d'authentification multifacteur deviennent pertinentes.

Le Niveau 1 n'est pas nécessairement testable par un testeur externe sans accès interne à la documentation ou au code (comme les tests « boîte noire »), bien que le nombre réduit d'exigences devrait faciliter sa vérification.

### Niveau 2

La plupart des applications devraient s'efforcer d'atteindre ce niveau de sécurité. Environ 50 % des exigences de l'ASVS sont de niveau 2, ce qui signifie qu'une application doit implémenter environ 70 % des exigences de l'ASVS (l'ensemble des exigences de niveau 1 et 2) pour être conforme à ce niveau.

Ces exigences concernent généralement des attaques moins courantes ou des protections plus complexes contre les attaques courantes. Elles peuvent constituer une première couche de défense ou nécessiter certaines conditions préalables pour que l'attaque réussisse.

### Niveau 3

Ce niveau doit être l'objectif des applications souhaitant démontrer les plus hauts niveaux de sécurité et représente environ 30 % des exigences à respecter.

Les exigences de cette section concernent généralement des mécanismes de défense en profondeur ou d'autres contrôles utiles, mais difficiles à mettre en œuvre.

### Quel niveau atteindre ?

Les niveaux de priorité visent à refléter la maturité de l'organisation et de l'application en matière de sécurité applicative. Plutôt que d'imposer un niveau de sécurité normatif pour une application, l'organisation doit analyser ses risques et déterminer le niveau qu'elle estime approprié, en fonction de la sensibilité de l'application et, bien sûr, des attentes de ses utilisateurs.

Par exemple, une jeune start-up qui ne collecte que des données sensibles limitées peut décider de se concentrer sur le niveau 1 pour ses objectifs de sécurité initiaux, tandis qu'une banque peut avoir du mal à justifier auprès de ses clients un niveau inférieur au niveau 3 pour son application de banque en ligne.

## Comment utiliser l'ASVS ?

### Structure de l'ASVS

L'ASVS comprend environ 350 exigences, réparties en 17 chapitres, chacun étant lui-même subdivisé en sections.

L'objectif de cette division est de simplifier la sélection ou le filtrage des chapitres et sections en fonction de leur pertinence pour l'application. Par exemple, pour une API machine-to-machine, les exigences du chapitre V3 relatives aux interfaces web ne seront pas pertinentes. Si OAuth ou WebRTC n'est pas utilisé, ces chapitres peuvent également être ignorés.

### Stratégie de publication

Les publications ASVS suivent le modèle « Majeure.Mineure.Correctif » et les numéros indiquent les modifications apportées. Pour une publication majeure, le premier numéro change, pour une publication mineure, le deuxième, et pour une publication corrective, le troisième.

* Publication majeure : Réorganisation complète, presque tout peut avoir changé, y compris les numéros d'exigences. Une réévaluation de conformité sera nécessaire (par exemple, 4.0.3 -> 5.0.0).
* Publication mineure : Des exigences peuvent être ajoutées ou supprimées, mais la numérotation globale reste inchangée. Une réévaluation de conformité sera nécessaire, mais devrait être plus simple (par exemple, 5.0.0 -> 5.1.0).
* Publication corrective : Des exigences peuvent être supprimées (par exemple, si elles sont dupliquées ou obsolètes) ou assouplies, mais une application conforme à la publication précédente sera également conforme à la publication corrective (par exemple, 5.0.0 -> 5.0.1).

Les informations ci-dessus concernent spécifiquement les exigences de l'ASVS. Les modifications apportées au texte environnant et à d'autres contenus, tels que les annexes, ne seront pas considérées comme des modifications majeures.

### Flexibilité avec l'ASVS

Plusieurs points décrits ci-dessus, tels que les exigences de documentation et le mécanisme de niveaux, permettent une utilisation de l'ASVS plus flexible et plus spécifique à l'organisation.

De plus, il est fortement encouragé aux organisations de créer un fork spécifique à l'organisation ou au domaine, afin d'ajuster les exigences en fonction des caractéristiques et des niveaux de risque de leurs applications. Cependant, il est important de maintenir une traçabilité afin que la conformité à l'exigence 4.1.1 soit identique pour toutes les versions.

Idéalement, chaque organisation devrait créer son propre ASVS personnalisé, en supprimant les sections non pertinentes (par exemple, GraphQL, WebSockets, SOAP, si elles ne sont pas utilisées). Une version ou un supplément ASVS spécifique à l'organisation est également un bon support pour fournir des conseils d'implémentation spécifiques à l'organisation, détaillant les bibliothèques ou les ressources à utiliser pour se conformer aux exigences.

### Comment référencer les exigences de l'ASVS ?

Chaque exigence possède un identifiant au format `<chapitre>.<section>.<exigence>`, où chaque élément est un numéro. Par exemple, « 1.11.3 ».

* La valeur `<chapitre>` correspond au chapitre d'où provient l'exigence ; par exemple, toutes les exigences `1.#.#` proviennent du chapitre 'Encodage et nettoyage'.
* La valeur `<section>` correspond à la section de ce chapitre où apparaît l'exigence ; par exemple, toutes les exigences `1.2.#` se trouvent dans la section 'Prévention des injections' du chapitre 'Encodage et nettoyage'.
* La valeur `<exigence>` identifie l'exigence spécifique au sein du chapitre et de la section, par exemple, `1.2.5` qui, dans la version 5.0.0 de ce référentiel, est :

> Vérifiez que l'application protège contre l'injection de commandes du système d'exploitation et que les appels du système d'exploitation utilisent des requêtes OS paramétrées ou un encodage contextuel de la sortie de ligne de commande.

Les identifiants pouvant varier d'une version à l'autre du référentiel, il est préférable, pour les autres documents, rapports ou outils, d'utiliser le format suivant : `v<version>-<chapter>.<section>.<requirement>`, où 'version' correspond à la balise de version ASVS. Par exemple, 'v5.0.0-1.2.5' désigne spécifiquement la 5ème exigence de la section 'Prévention des injections' du chapitre 'Encodage et nettoyage' de la version 5.0.0. (Ceci pourrait être résumé par `v<version>-<identifiant_exigence>`.)

Remarque : Le `v` précédant le numéro de version dans le format doit toujours être en minuscule.

Si des identifiants sont utilisés sans inclure l'élément `v<version>`, ils doivent être considérés comme faisant référence au contenu le plus récent du Référentiel de vérification de la sécurité des applications. À mesure que le référentiel évolue, cela devient problématique ; c'est pourquoi les rédacteurs et les développeurs doivent inclure l'élément « version ».

Les listes d'exigences de l'ASVS sont disponibles aux formats CSV, JSON et autres, utiles à des fins de référence ou d'utilisation programmatique.

### Forker l'ASVS

Les organisations peuvent tirer profit de l'adoption d'ASVS en choisissant l'un des trois niveaux ou en créant un fork spécifique au domaine qui ajuste les exigences en fonction du niveau de risque applicatif. Ce type de fork est encouragé, à condition de garantir la traçabilité de l'exigence 4.1.1, garantissant ainsi la même cohérence pour toutes les versions.

Idéalement, chaque organisation devrait créer son propre ASVS personnalisé, en supprimant les sections non pertinentes (par exemple, GraphQL, Websockets, SOAP, si elles ne sont pas utilisées). Le fork doit commencer par le niveau 1 d'ASVS comme référence, puis progresser vers les niveaux 2 ou 3 en fonction du risque de l'application.

## Cas d'utilisation de l'ASVS

L'ASVS peut être utilisé pour évaluer la sécurité d'une application, ce point étant approfondi dans le chapitre suivant. Cependant, plusieurs autres utilisations potentielles de l'ASVS (ou d'une version dérivée) ont été identifiées.

### En tant que conseil détaillé sur l'architecture de sécurité

L'une des utilisations les plus courantes du Référentiel de vérification de la sécurité des applications (ASVS) est de servir de ressource aux architectes de sécurité. Les ressources disponibles pour construire une architecture applicative sécurisée sont limitées, notamment pour les applications modernes. L'ASVS peut combler ces lacunes en permettant aux architectes de sécurité de choisir de meilleurs contrôles pour les problèmes courants, tels que les modèles de protection des données et les stratégies de validation des entrées. Les exigences en matière d'architecture et de documentation seront particulièrement utiles à cet égard.

### Référence spécialisée en developpement sécurisé

L'ASVS peut servir de base à la préparation d'une référence de développement sécurisé lors du développement d'applications, aidant ainsi les développeurs à prendre en compte la sécurité lors de la création de logiciels. Bien que l'ASVS puisse servir de base, les organisations doivent élaborer leurs propres directives claires et unifiées, idéalement basées sur les recommandations des ingénieurs ou architectes de sécurité. De plus, les organisations sont encouragées, dans la mesure du possible, à préparer des mécanismes et bibliothèques de sécurité approuvés, référencés dans les directives et utilisables par les développeurs.

### Guide pour les tests unitaires et d'intégration automatisés

L'ASVS est conçu pour être hautement testable. Certaines vérifications seront techniques, tandis que d'autres exigences (telles que les exigences d'architecture et de documentation) pourront nécessiter une revue de documentation ou d'architecture. En créant des tests unitaires et d'intégration qui testent et analysent par fuzzing des cas d'abus spécifiques et pertinents liés aux exigences, vérifiables par des moyens techniques, il devrait être plus facile de vérifier le bon fonctionnement de ces contrôles à chaque build. Par exemple, des tests supplémentaires peuvent être créés pour la suite de tests d'un contrôleur de connexion afin de tester la présence de valeur par défaut courante pour le paramètre username, l'énumération des comptes, le force brute, l'injection LDAP et SQL, et les attaques XSS. De même, un test sur le paramètre password doit inclure les mots de passe courants, la longueur des mots de passe, l'injection d'octets nuls, la suppression du paramètre, les attaques XSS, etc.

### Pour la formation au développement sécurisé

L'ASVS peut également servir à définir les caractéristiques d'un logiciel sécurisé. De nombreux cours de « codage sécurisé » se résument à des cours de piratage éthique, avec quelques conseils de codage. Cela n'aide pas forcément les développeurs à écrire du code plus sécurisé. Les cours de développement sécurisé peuvent plutôt utiliser l'ASVS en mettant l'accent sur ses mécanismes positifs, plutôt que sur les 10 principes négatifs à éviter. La structure de l'ASVS offre également une structure logique pour aborder les différents sujets liés à la sécurisation d'une application.

### En tant que cadre pour l'approvisionnement des logiciels sécurisés

L'ASVS est un cadre idéal pour faciliter l'approvisionnement des logiciels sécurisés ou l'acquisition de services de développement de développement sur mesure. L'acheteur peut simplement exiger que le logiciel qu'il souhaite acquérir soit développé au niveau X de l'ASVS et demander au vendeur de prouver que le logiciel satisfait à ce niveau.

## Appliquer l'ASVS en pratique

Les menaces varient selon les motivations. Certains secteurs disposent de ressources informatiques et technologiques spécifiques et d'exigences de conformité réglementaire spécifiques à leur domaine.

Il est fortement recommandé aux organisations d'analyser en profondeur les caractéristiques de risque spécifiques à leur activité et de déterminer le niveau d'ASVS approprié en fonction de ces risques et des exigences métier.
