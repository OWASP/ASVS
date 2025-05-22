# Utilisation de l'ASVS

Le référentiel de vérification de la sécurité des applications (ASVS) définit les exigences de sécurité pour les applications et services Web modernes, en se concentrant sur les aspects qui sont sous le contrôle des développeurs d'applications.

L'ASVS est utile à toute personne souhaitant développer et maintenir des applications sécurisées, ou évaluer leur sécurité. Ce chapitre aborde les aspects clés de l'utilisation de l'ASVS, notamment les niveaux de priorité et les différents cas d'utilisation de la norme.

## Niveaux de vérification de la sécurité des applications

L'ASVS définit trois niveaux de vérification de sécurité, chaque niveau augmentant en profondeur et en complexité. Chaque niveau ASVS indique les exigences de sécurité requises pour l'atteindre (les autres restant à titre de recommandations). L'objectif général est que les organisations commencent par le niveau le plus bas, puis progressent vers les niveaux supérieurs.

### Critères d'évaluation du niveau

L'approche de définition des niveaux pour la version 5.0 a été définie après de nombreuses discussions au sein du groupe de travail, sur la base des retours des utilisateurs d'ASVS et en s'appuyant sur les principes de la version 5.0 évoqués au chapitre précédent. La version 5.0 évalue chaque exigence par priorité, en s'appuyant sur l'expérience acquise dans la mise en œuvre des exigences de sécurité. Suivant cette approche, chaque exigence a été évaluée selon les critères suivants.

#### Réduction des risques

Dans quelle mesure cette exigence réduit-elle le risque de sécurité au sein de l'application ? Cela prend en compte les facteurs d'impact classiques de confidentialité, d'intégrité et de disponibilité, ainsi que la question de savoir s'il s'agit d'une première couche de défense ou d'une défense en profondeur.

En général, les exigences qui entraînent la plus grande réduction des risques se situent au niveau 1 ou au niveau 2, tandis que les exigences qui sont toujours utiles mais qui sont soit de nature défensive, soit liées à un domaine ou à un problème plus spécialisé se situent au niveau 3.

#### Efforts de mise en œuvre

Bien que l'ASVS soit considérée comme une norme de vérification, il n'y a rien à vérifier tant que l'exigence n'a pas été implémentée dans l'application. Certaines exigences sont clairement plus complexes à mettre en œuvre et à maintenir que d'autres, et il est important d'en tenir compte lors de la définition de la priorité relative d'une exigence.

Bien qu’il existe encore des contrôles plus difficiles à mettre en œuvre qui offrent une réduction des risques suffisamment importante pour être classés au niveau 1, les exigences plus complexes seront classées au niveau 2 ou au niveau 3.

#### Faible barrière à l'entrée

D'après les retours d'expérience sur l'utilisation (ou la non-utilisation) des versions précédentes d'ASVS dans l'industrie, le principal problème identifié était le double tranchant du niveau 1, qui comporte un grand nombre d'exigences (environ 120), tout en étant considéré comme le niveau « minimum » insuffisant pour la plupart des applications. Cette situation semblait conduire les organisations soit à abandonner avant même de commencer, soit à tenter de mettre en œuvre un sous-ensemble d'exigences sans atteindre le niveau 1, réduisant ainsi le sentiment d'accomplissement et de progrès.

À cette fin, il a été décidé que le niveau 1 comporterait un maximum d'environ 70 exigences parmi les plus prioritaires. Cela semblait être un bon compromis entre atteignabilité et niveau de sécurité élevé, les autres exigences étant reléguées au niveau 2 ou 3. Pour y parvenir, des décisions difficiles ont été prises quant à ce qui serait intégré au niveau 1 et ce qui ne le serait pas. L'objectif était d'obtenir un niveau 1 satisfaisant et atteignable plutôt qu'un niveau 1 parfait qui ne l'est pas.

#### Meilleur équilibre des niveaux

Dans la version 4.0, les niveaux 1 et 2 comptaient chacun environ 120 exigences, et le niveau 3 environ 30. La version 5.0 répartit les exigences de manière plus équilibrée entre les niveaux, en essayant de répartir les exigences des niveaux 2 et 3 de manière plus homogène. L'objectif est de rendre le niveau 2 plus atteignable et réaliste, tout en réservant le niveau 3 aux applications souhaitant démontrer le plus haut niveau de sécurité.

### Définition des niveaux

Sur la base des critères ci-dessus, les exigences de la version 5.0 ont été réparties en trois niveaux. Bien que l'analyse comparative basée sur ces facteurs indique une part de jugement dans la répartition, les discussions rigoureuses autour des critères et des décisions de nivellement ont abouti à une répartition qui devrait s'appliquer à la grande majorité des cas, tout en admettant qu'elle ne soit pas forcément adaptée à toutes les situations.

Cela signifie que dans certains cas, les organisations peuvent souhaiter prioriser les exigences d’un niveau supérieur plus tôt en fonction de leurs propres considérations de risque spécifiques.

Les types d’exigences à chaque niveau peuvent être caractérisés comme suit.

#### Exigences de niveau 1

Il s'agit généralement d'exigences critiques ou élémentaires de première couche de défense pour prévenir les attaques courantes, qui ne nécessitent pas d'autres vulnérabilités ou conditions préalables. Ces exigences sont soit relativement simples à mettre en œuvre, soit suffisamment importantes pour justifier l'effort.

Le niveau 1 n’est pas nécessairement testable par pénétration pour des humains, bien que le nombre réduit d’exigences devrait faciliter la vérification.

#### Exigences de niveau 2

Ces exigences concernent généralement des attaques moins courantes ou des protections plus complexes contre des attaques courantes. Elles peuvent néanmoins constituer une première couche de défense ou nécessiter certaines conditions préalables pour que l'attaque réussisse.

#### Exigences de niveau 3

Les exigences de cette section concernent généralement des mécanismes de défense en profondeur ou d'autres contrôles utiles, mais difficiles à mettre en œuvre. Elles peuvent également concerner des attaques beaucoup plus spécifiques ou pertinentes uniquement dans certaines circonstances.

### Quel niveau atteindre

En adoptant une évaluation prioritaire de chaque exigence, les niveaux reflètent davantage la maturité de l'organisation et de l'application en matière de sécurité applicative. Plutôt que d'imposer un niveau de sécurité normatif pour une application, l'organisation doit déterminer le niveau qu'elle estime nécessaire, en fonction de la sensibilité de l'application et, bien sûr, des attentes de ses utilisateurs.

Par exemple, une startup en phase de démarrage qui ne collecte que des données sensibles limitées peut décider que le niveau 1 est suffisant, mais une banque peut avoir du mal à justifier auprès de ses clients un niveau inférieur au niveau 3 pour son application bancaire en ligne.

## Comment se référencer aux exigences ASVS

Chaque exigence a un identifiant au format `<chapitre>.<section>.<exigence>` où chaque élément est un nombre, par exemple : `1.11.3`.

* La valeur `<chapitre>` correspond au chapitre d'où provient l'exigence, par exemple : toutes les exigences `1.#.#` sont issues du chapitre `Architecture`.
* La valeur `<section>` correspond à la section de ce chapitre où l'exigence apparaît, par exemple : toutes les exigences `1.11.#` se trouvent dans la section `Business Logic Architecture` du chapitre `Architecture`.
* La valeur `<requirement>` identifie l'exigence spécifique dans le chapitre et la section, par exemple : `1.11.3` qui, à partir de la version 4.0.2 de cette norme, est :

> Vérifier que tous les flux de logique métier de grande valeur, y compris l'authentification, la gestion de session et le contrôle d'accès, sont sécurisés et résistants aux conditions de concurrence ("race condition") au temps de contrôle et au temps d'utilisation.

Les identifiants peuvent changer entre les versions de la norme, il est donc préférable que d'autres documents, rapports ou outils utilisent le format : `v<version>-<chapter>.<section>.<requirement>`, où : 'version' est la balise de version ASVS. Par exemple : `v4.0.3-1.11.3` serait compris comme signifiant spécifiquement la 3ème exigence dans la section 'Business Logic Architecture' du chapitre 'Architecture' de la version 4.0.2. (Cela pourrait être résumé comme `v<version>-<requirement_identifier>`.)

Remarque : Le `v` précédant la partie version doit être en minuscule.

Si les identifiants sont utilisés sans inclure l'élément `v<version>`, ils doivent être supposés faire référence au dernier contenu de la norme de vérification de la sécurité des applications. De toute évidence, à mesure que la norme se développe et change, cela devient problématique, c'est pourquoi les rédacteurs ou les développeurs doivent inclure l'élément de version.

Les listes d'exigences ASVS sont mises à disposition au format CSV, JSON et d'autres formats qui peuvent être utiles pour une utilisation de référence ou de programmation.

## Fork de l'ASVS

Les organisations peuvent tirer profit de l'adoption d'ASVS en choisissant l'un des trois niveaux ou en créant un fork spécifique au domaine qui ajuste les exigences en fonction du niveau de risque applicatif. Nous encourageons ce fork, à condition qu'il préserve la traçabilité afin que le respect de l'exigence 4.1.1 soit identique pour toutes les versions.

Idéalement, chaque organisation devrait créer son propre ASVS personnalisé, en supprimant les sections inutiles (par exemple, GraphQL, Websockets, SOAP, si elles ne sont pas utilisées). Le fork devrait commencer par le niveau 1 d'ASVS comme référence, puis progresser vers les niveaux 2 ou 3 en fonction du risque de l'application.

## Utilisations de l'ASVS

L'ASVS peut être utilisé pour évaluer la sécurité d'une application, ce point étant approfondi dans le chapitre suivant. Cependant, nous avons identifié plusieurs autres utilisations potentielles de l'ASVS (ou d'une version dérivée).

### En tant que guide détaillé sur l'architecture de sécurité

L'une des utilisations les plus courantes de la norme de vérification de la sécurité des applications est celle de ressource pour les architectes de sécurité. L'architecture de sécurité des applications de Sherwood (SABSA) manque de nombreuses informations nécessaires à une analyse approfondie de l'architecture de sécurité des applications. L'ASVS peut combler ces lacunes en permettant aux architectes de sécurité de choisir de meilleurs contrôles pour les problèmes courants, tels que les modèles de protection des données et les stratégies de validation des entrées.

### En tant que liste de contrôle de codage sécurisé spécialisée

L'ASVS peut servir de liste de contrôle pour le développement d'applications sécurisées, aidant ainsi les développeurs à prendre en compte la sécurité lors de la création de logiciels. Cette liste de contrôle doit être unifiée, claire et applicable à toutes les équipes de développement. Idéalement, elle doit être élaborée sur la base des conseils d'ingénieurs ou d'architectes sécurité.

### En tant que guide pour les tests unitaires et d'intégration automatisés

L'ASVS est conçu pour être hautement testable, à l'exception des exigences d'architecture et de documentation. En créant des tests unitaires et d'intégration qui testent et analysent les cas d'abus spécifiques et pertinents, il devrait être plus facile de vérifier les contrôles mis en œuvre à chaque build. Par exemple, des tests supplémentaires peuvent être créés pour la suite de tests d'un contrôleur de connexion, testant le paramètre username pour les noms d'utilisateur par défaut courants, l'énumération des comptes, les attaques par force brute, l'injection LDAP et SQL, et les attaques XSS. De même, un test sur le paramètre password doit inclure les mots de passe courants, la longueur des mots de passe, l'injection d'octets nuls, la suppression du paramètre, les attaques XSS, etc.

### Pour une formation au développement sécurisé

L'ASVS peut également servir à définir les caractéristiques d'un logiciel sécurisé. De nombreux cours de « développement sécurisé » se résument à des formations de piratage éthique, avec quelques conseils de programmation. Cela n'aide pas forcément les développeurs à écrire du code plus sécurisé. Les cours de développement sécurisé peuvent plutôt utiliser l'ASVS en mettant l'accent sur les contrôles proactifs qu'il contient, plutôt que sur les 10 principes négatifs à éviter.

### En tant que moteur de la sécurité des applications agiles

ASVS peut être utilisé dans un processus de développement agile comme cadre pour définir les tâches spécifiques à mettre en œuvre par l'équipe afin de sécuriser le produit. Une approche possible consiste à commencer par le niveau 1, vérifier l'application ou le système spécifique conformément aux exigences ASVS du niveau spécifié, identifier les contrôles manquants et générer des tickets/tâches spécifiques dans le backlog. Cela facilite la priorisation des tâches spécifiques (ou le grooming) et rend la sécurité visible dans le processus agile. Cette approche peut également servir à prioriser les tâches d'audit et de revue au sein de l'organisation. Une exigence ASVS spécifique peut entraîner une revue, une refactorisation ou un audit pour un membre de l'équipe, et apparaître comme une « dette » dans le backlog qui devra être traitée ultérieurement.

### En tant que cadre pour guider l'approvisionnement en logiciels sécurisés

ASVS est un excellent cadre pour faciliter l'achat sécurisé de logiciels ou de services de développement personnalisés. L'acheteur peut simplement exiger que le logiciel qu'il souhaite acquérir soit développé au niveau ASVS X et demander au vendeur de prouver que le logiciel satisfait à ce niveau. Ce cadre est particulièrement efficace en combinaison avec l'annexe au contrat de logiciels sécurisés de l'OWASP.

## Application de l'ASVS dans la pratique

Les menaces varient selon les motivations. Certains secteurs disposent de ressources informatiques et technologiques uniques et d'exigences réglementaires spécifiques.

Il est fortement recommandé aux organisations d’examiner en profondeur leurs caractéristiques de risque uniques en fonction de la nature de leur activité et, en fonction de ce risque et des exigences commerciales, de déterminer le niveau ASVS approprié.
