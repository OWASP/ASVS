# Utiliser l'ASVS

L'ASVS a deux objectifs principaux :

* aider les organisations à développer et à maintenir des applications sécurisées.
* permettre aux fournisseurs de services de sécurité, aux vendeurs d'outils de sécurité et aux consommateurs d'aligner leurs exigences et leurs offres.

## Niveaux de vérification de la sécurité des applications

La norme de vérification de la sécurité des applications définit trois niveaux de vérification de la sécurité, chacun d'eux étant plus approfondi.

* Le niveau 1 de l'ASVS est destiné aux niveaux d'assurance faibles, et peut être testé en profondeur.
* Le niveau 2 de l'ASVS est destiné aux applications qui contiennent des données sensibles, ce qui nécessite une protection et constitue le niveau recommandé pour la plupart des applications
* Le niveau 3 de l'ASVS est destiné aux applications les plus critiques - les applications qui effectuent des transactions de grande valeur, qui contiennent des données médicales sensibles, ou toute application qui requiert le plus haut niveau de confiance.

Chaque niveau ASVS contient une liste d'exigences de sécurité. Chacune de ces exigences peut également être mise en correspondance avec des caractéristiques et des capacités de sécurité spécifiques qui doivent être intégrées dans les logiciels par les développeurs.

![Niveaux ASVS](../images/asvs_40_levels.png "ASVS Levels")

Figure 1 - Niveaux de vérification de la sécurité des applications OWASP 4.0

Le niveau 1 est le seul qui soit entièrement adéquat pour des tests d'intrusions fait par des humains. Tous les autres niveaux nécessitent l'accès à la documentation, au code source, à la configuration et aux personnes impliquées dans le processus de développement. Cependant, même si le niveau 1 permet de réaliser des tests de "boîte noire" (pas de documentation et pas de source), ce n'est pas une activité d'assurance efficace et doit être activement découragée. Les attaquants malveillants ont beaucoup de temps, la plupart des tests de pénétration sont terminés en quelques semaines. Les défenseurs doivent mettre en place des contrôles de sécurité, protéger, trouver et résoudre toutes les faiblesses, et détecter et répondre aux acteurs malveillants dans un délai raisonnable. Les acteurs malveillants disposent essentiellement d'un temps infini et n'ont besoin que d'une seule défense poreuse, d'une seule faiblesse ou d'une détection manquante pour réussir. Les tests de la boîte noire, souvent effectués en fin de développement, rapidement ou pas du tout, sont totalement incapables de faire face à cette asymétrie.

Au cours des 30 dernières années, les tests en boîte noire ont prouvé à maintes reprises qu'ils passaient à côté de problèmes de sécurité critiques qui ont directement conduit à des violations de plus en plus massives. Nous encourageons vivement l'utilisation d'un large éventail de mesures d'assurance et de vérification de la sécurité, notamment le remplacement des tests de pénétration par des tests de pénétration (hybrides) de niveau 1 basés sur le code source, avec un accès complet aux développeurs et à la documentation tout au long du processus de développement. Les régulateurs financiers ne tolèrent pas les audits financiers externes sans accès aux livres, aux échantillons de transactions ou aux personnes effectuant les contrôles. L'industrie et les gouvernements doivent exiger le même niveau de transparence dans le domaine du génie logiciel.

Nous encourageons fortement l'utilisation d'outils de sécurité, mais dans le cadre du processus de développement lui-même, tels que les outils DAST et SAST utilisés en permanence par le pipeline de construction pour trouver facilement des problèmes de sécurité qui ne devraient jamais être présents.

Les outils automatisés et les scanners en ligne ne permettent pas de réaliser plus de la moitié des ASVS sans assistance humaine. Si une automatisation complète des tests pour chaque construction est nécessaire, on utilise alors une combinaison de tests unitaires et d'intégration personnalisés, ainsi que des scans en ligne initiés par la construction. Les failles de la logique métier et les tests de contrôle d'accès ne sont possibles qu'avec l'aide d'une personne. Ces tests doivent être transformés en tests unitaires et d'intégration.

## Comment utiliser cette norme

L'une des meilleures façons d'utiliser la norme de vérification de la sécurité des applications est de l'utiliser comme plan directeur pour créer une liste de contrôle de codage sécurisé spécifique à votre application, plate-forme ou organisation. En adaptant l'ASVS à vos cas d'utilisation, vous pourrez mieux vous concentrer sur les exigences de sécurité les plus importantes pour vos projets et vos environnements.

### Niveau 1 - Premières étapes, automatisé, ou vue de l'ensemble du portefeuille

Une application atteint le niveau 1 de l'ASVS si elle se défend de manière adéquate contre les vulnérabilités de sécurité des applications qui sont faciles à découvrir, et qui figurent dans le Top 10 de l'OWASP et d'autres listes de contrôle similaires.

Le niveau 1 est le strict minimum que toutes les applications devraient s'efforcer d'atteindre. Il est également utile comme première étape dans un effort en plusieurs phases ou lorsque les applications ne stockent pas ou ne traitent pas de données sensibles et n'ont donc pas besoin des contrôles plus rigoureux du niveau 2 ou 3. Les contrôles de niveau 1 peuvent être vérifiés soit automatiquement par des outils, soit simplement manuellement sans accès au code source. Nous considérons que le niveau 1 est le minimum requis pour toutes les applications.

Les menaces pour l'application proviendront très probablement d'attaquants qui utilisent des techniques simples et peu exigeantes pour identifier des vulnérabilités faciles à trouver et à exploiter. En revanche, un attaquant déterminé dépensera une énergie concentrée pour cibler spécifiquement l'application. Si les données traitées par votre application ont une valeur élevée, vous voudrez rarement vous arrêter à un examen de niveau 1.

### Niveau 2 - La plupart des demandes

Une application atteint le niveau 2 (ou norme) de l'ASVS si elle se défend adéquatement contre la plupart des risques associés aux logiciels d'aujourd'hui.

Le niveau 2 garantit que les contrôles de sécurité sont en place, efficaces et utilisés au sein de l'application. Le niveau 2 est généralement approprié pour les applications qui traitent des transactions interentreprises importantes, y compris celles qui traitent des informations sur les soins de santé, mettent en œuvre des fonctions critiques ou sensibles, traitent d'autres actifs sensibles, ou les secteurs où l'intégrité est une facette essentielle pour protéger leur activité, comme le secteur des jeux pour contrecarrer les tricheurs et les pirates.

Les menaces pesant sur les applications de niveau 2 seront généralement des attaquants compétents et motivés qui se concentrent sur des cibles spécifiques en utilisant des outils et des techniques très pratiques et efficaces pour découvrir et exploiter les faiblesses des applications.

### Niveau 3 - Haute valeur, haute assurance ou haute sécurité

Le niveau 3 de l'ASVS est le plus haut niveau de vérification au sein de l'ASVS. Ce niveau est généralement réservé aux applications qui nécessitent des niveaux de vérification de sécurité importants, comme celles qui peuvent se trouver dans les domaines de l'armée, de la santé et de la sécurité, des infrastructures critiques, etc.

Les organisations peuvent exiger le niveau 3 de l'ASVS pour les applications qui remplissent des fonctions critiques, où une défaillance pourrait avoir un impact significatif sur les opérations de l'organisation, et même sur sa capacité de survie. Des exemples de conseils sur l'application de l'ASVS niveau 3 sont fournis ci-dessous. Une application atteint le niveau 3 ASVS (ou avancé) si elle se défend de manière adéquate contre les vulnérabilités de sécurité des applications avancées et si elle démontre également les principes d'une bonne conception de la sécurité.

Une application au niveau 3 ASVS nécessite une analyse plus approfondie de l'architecture, du codage et des tests que tous les autres niveaux. Une application sécurisée est modulaire de manière significative (pour faciliter la résilience, l'évolutivité et, surtout, les couches de sécurité), et chaque module (séparé par une connexion réseau et/ou une instance physique) prend en charge ses propres responsabilités en matière de sécurité (défense en profondeur), qui doivent être correctement documentés. Les responsabilités comprennent des contrôles pour garantir la confidentialité (par exemple, le cryptage), l'intégrité (par exemple, les transactions, la validation des entrées), la disponibilité (par exemple, gérer la charge avec élégance), l'authentification (y compris entre les systèmes), la non-répudiation, l'autorisation et l'audit (journalisation).

## Application de l'ASVS en pratique

Les différentes menaces ont des motivations différentes. Certains secteurs d'activité disposent d'atouts uniques en matière d'information et de technologie et ont des exigences de conformité réglementaire spécifiques à leur domaine.

Les organisations sont fortement encouragées à examiner en profondeur leurs caractéristiques de risque uniques en fonction de la nature de leur activité, et à déterminer le niveau ASVS approprié en fonction de ce risque et des exigences commerciales.
