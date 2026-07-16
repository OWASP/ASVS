# Modifications par rapport à la version 4.x

## Introduction

Les utilisateurs familiarisés avec la version 4.x du référentiel trouveront utile de consulter les principales modifications apportées à la version 5.0, notamment les mises à jour de contenu, de périmètre et de philosophie sous-jacente.

Sur les 286 exigences de la version 4.0.3, seules 11 restent inchangées, tandis que 15 ont subi des ajustements grammaticaux mineurs sans altérer leur sens. Au total, 109 exigences (38 %) ne sont plus des exigences distinctes dans la version 5.0 : 50 ont été simplement supprimées, 28 ont été supprimées car doublons et 31 ont été fusionnées avec d'autres exigences. Les autres ont été révisées. Même les exigences n'ayant pas subi de modifications substantielles ont des identifiants différents à la suite d'une réorganisation ou une restructuration.

Pour faciliter l'adoption de la version 5.0, des documents de correspondance sont fournis pour aider les utilisateurs à identifier les correspondances entre les exigences de la version 4.x et celles de la version 5.0. Ces correspondances ne sont pas liées au numéro de version et peuvent être mises à jour ou clarifiées si nécessaire.

## Philosophie des exigences

### Périmètre et orientation

La version 4.x incluait des exigences qui ne correspondaient pas au périmètre prévu du référentiel ; celles-ci ont été supprimées. Les exigences qui ne répondaient pas aux critères du périmètre de la version 5.0 ou qui n'étaient pas vérifiables ont également été exclues.

### Priorité aux objectifs de sécurité plutôt qu'aux mécanismes

Dans la version 4.x, de nombreuses exigences se concentraient sur des mécanismes spécifiques plutôt que sur les objectifs de sécurité sous-jacents. Dans la version 5.0, les exigences sont centrées sur les objectifs de sécurité, ne référençant des mécanismes particuliers que lorsqu'ils constituent la seule solution pratique, ou les fournissant à titre d'exemple ou de conseil complémentaire.

Cette approche reconnaît que plusieurs méthodes peuvent exister pour atteindre un objectif de sécurité donné et évite toute prescription inutile susceptible de limiter la flexibilité organisationnelle.

De plus, les exigences traitant d'une même préoccupation de sécurité ont été consolidées lorsque cela était opportun.

### Décisions de sécurité documentées

Bien que le concept de décisions de sécurité documentées puisse paraître nouveau dans la version 5.0, il s'agit d'une évolution des exigences antérieures liées à l'application des politiques et à la modélisation des menaces dans la version 4.0. Auparavant, certaines exigences exigeaient implicitement une analyse pour éclairer la mise en œuvre des contrôles de sécurité, comme la détermination des connexions réseau autorisées.

Afin de garantir la disponibilité des informations nécessaires à la mise en œuvre et à la vérification, ces attentes sont désormais explicitement définies comme des exigences de documentation, ce qui les rend claires, actionnables et vérifiables.

## Modifications structurelles et nouveaux chapitres

Plusieurs chapitres de la version 5.0 introduisent du contenu entièrement nouveau :

* OAuth et OIDC – Compte tenu de l’adoption généralisée de ces protocoles pour la délégation d’accès et l’authentification unique, des exigences spécifiques ont été ajoutées pour répondre aux divers scénarios rencontrés par les développeurs. Ce domaine pourrait à terme évoluer vers une norme autonome, similaire à la gestion des exigences mobiles et IoT dans les versions précédentes.
* WebRTC – Avec la popularité croissante de cette technologie, ses considérations et défis de sécurité spécifiques sont désormais abordés dans une section dédiée.

Des efforts ont également été déployés pour garantir que les chapitres et sections soient organisés autour d’ensembles cohérents d’exigences connexes.

Cette restructuration a conduit à la création de chapitres supplémentaires :

* Jetons autonomes – Auparavant regroupés sous la rubrique « gestion de session », les jetons autonomes sont désormais reconnus comme un mécanisme distinct et un élément fondamental de la communication sans état (comme dans OAuth et OIDC). En raison de leurs implications spécifiques en matière de sécurité, elles sont traitées dans un chapitre dédié, avec l'introduction de nouvelles exigences dans la version 5.x.
* Sécurité du frontend web – Avec la complexité croissante des applications basées sur un navigateur et l'essor des architectures exclusivement basées sur des API, les exigences de sécurité du frontend ont été séparées dans un chapitre dédié.
* Codage et architecture sécurisés – Les nouvelles exigences concernant les pratiques de sécurité générales qui ne cadraient pas avec les chapitres existants ont été regroupées ici.

D'autres modifications organisationnelles ont été apportées à la version 5.0 afin de clarifier l'intention. Par exemple, les exigences de validation des entrées ont été déplacées avec la logique métier, reflétant ainsi leur rôle dans l'application des règles métier, plutôt que d'être regroupées avec le nettoyage et l'encodage.

L'ancien chapitre « Architecture » ​​de la version 1 a été supprimé. Sa section initiale contenait des exigences hors du périmètre, tandis que les sections suivantes ont été redistribuées aux chapitres concernés, les exigences étant dédupliquées et clarifiées si nécessaire.

## Suppression des correspondances directes avec d'autres normes

Les correspondances directes avec d'autres normes ont été supprimées du corps du référentiel. L'objectif est de préparer une correspondance avec le projet OWASP Common Requirement Enumeration (CRE), qui reliera ASVS à divers projets OWASP et normes externes.

Les correspondances directes avec CWE et NIST ne sont plus maintenues, comme expliqué ci-dessous.

### Couplage réduit avec les directives du NIST sur l'identité numérique

Les directives du NIST sur l'identité numérique (SP 800-63) (https://pages.nist.gov/800-63-3/) servent depuis longtemps de référence pour les contrôles d'authentification et d'autorisation. Dans la version 4.x, certains chapitres étaient étroitement alignés sur la structure et la terminologie du NIST.

Si ces directives demeurent une référence importante, un alignement strict a engendré des difficultés, notamment une terminologie moins reconnue, la duplication d'exigences similaires et des correspondances incomplètes. La version 5.0 s'éloigne de cette approche pour plus de clarté et de pertinence.

### S'éloigner de l'énumération des faiblesses communes (CWE)

L'[Énumération des Faiblesses Communes (CWE)](https://cwe.mitre.org/) fournit une taxonomie utile des faiblesses de sécurité logicielle. Cependant, des défis tels que les CWE par catégorie, les difficultés de correspondance des exigences à une CWE unique et la présence de mappages imprécis dans la version 4.x ont conduit à la décision d'abandonner les mappages CWE directs dans la version 5.0.

## Repenser les définitions de niveaux

La version 4.x décrivait les niveaux comme L1 (« Minimum »), L2 (« Standard ») et L3 (« Avancé »), ce qui implique que toutes les applications manipulant des données sensibles doivent au moins atteindre le niveau L2.

La version 5.0 corrige plusieurs problèmes liés à cette approche, décrits dans les paragraphes suivants.

En pratique, alors que la version 4.x utilisait des graduations pour les indicateurs de niveau, la version 5.x utilise un simple numéro pour tous les formats du référentiel, notamment Markdown, PDF, DOCX, CSV, JSON et XML. Pour des raisons de rétrocompatibilité, les anciennes versions des sorties CSV, JSON et XML utilisant encore des graduations sont également générées.

### Niveau d'entrée simplifié

Les retours ont indiqué que le nombre important d'exigences de niveau 1 (environ 120), combiné à sa désignation comme niveau « minimum », insuffisant pour la plupart des applications, freinait l'adoption. La version 5.0 vise à lever cet obstacle en définissant le niveau 1 principalement autour des exigences de défense de première couche, ce qui se traduit par des exigences plus claires et moins nombreuses à ce niveau. À titre d'exemple, la version 4.0.3 comptait 128 exigences de niveau 1 sur un total de 278, soit 46 %. La version 5.0.0 compte 70 exigences de niveau 1 sur un total de 345, soit 20 %.

### L'illusion de la testabilité

Un facteur clé dans le choix des contrôles de niveau 1 dans la version 4.x était leur aptitude à être évalués par des tests d'intrusion externes de type « boîte noire ». Cependant, cette approche n'était pas totalement conforme à l'objectif du niveau 1 en tant qu'ensemble minimal de contrôles de sécurité. Certains utilisateurs ont fait valoir que le niveau 1 était insuffisant pour sécuriser les applications, tandis que d’autres ont trouvé qu’il était trop difficile à tester.

S'appuyer sur la testabilité comme critère est à la fois relatif et parfois trompeur. Le fait qu'une exigence soit testable ne garantit pas qu'elle puisse être testée de manière automatisée ou simple. De plus, les exigences les plus facilement testables ne sont pas toujours celles qui ont le plus grand impact sur la sécurité ou les plus simples à mettre en œuvre.

Par conséquent, dans la version 5.0, les décisions de niveau ont été prises principalement en fonction de la réduction des risques et en tenant compte de l'effort de mise en œuvre.

### Pas seulement une question de risque

L'utilisation de niveaux prescriptifs, basés sur les risques, imposant un niveau spécifique à certaines applications s'est avérée trop rigide. En pratique, la priorisation et la mise en œuvre des contrôles de sécurité dépendent de multiples facteurs, notamment la réduction des risques et les efforts nécessaires à leur mise en œuvre.

Par conséquent, les organisations sont encouragées à atteindre le niveau qu'elles estiment devoir atteindre en fonction de leur maturité et du message qu'elles souhaitent transmettre à leurs utilisateurs.
