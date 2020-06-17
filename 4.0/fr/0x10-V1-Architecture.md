# V1 : Architecture, conception et exigences en matière de modélisation des menaces

## Objectif de contrôle

L'architecture de sécurité est presque devenue un art perdu dans de nombreuses organisations. Les jours de l'architecte d'entreprise sont passés à l'ère des DevSecOps. Le domaine de la sécurité des applications doit rattraper son retard et adopter des principes de sécurité agiles tout en réintroduisant les principes de l'architecture de sécurité de pointe auprès des praticiens du logiciel. L'architecture n'est pas une implémentation, mais une façon de penser à un problème qui peut avoir plusieurs réponses différentes, et pas une seule réponse "correcte". Trop souvent, la sécurité est considérée comme rigide et exige que les développeurs corrigent le code d'une manière particulière, alors qu'ils connaissent peut-être un bien meilleur moyen de résoudre le problème. Il n'existe pas de solution unique et simple pour l'architecture, et prétendre le contraire est un mauvais service rendu au domaine du génie logiciel.

Une implémentation spécifique d'une application web est susceptible d'être révisée continuellement tout au long de sa vie, mais l'architecture globale ne changera probablement que rarement, mais évoluera lentement. L'architecture de sécurité est identique - nous avons besoin d'une authentification aujourd'hui, nous en aurons besoin demain, et nous en aurons besoin dans cinq ans. Si nous prenons des décisions judicieuses aujourd'hui, nous pouvons économiser beaucoup d'efforts, de temps et d'argent si nous sélectionnons et réutilisons des solutions conformes à l'architecture. Par exemple, il y a dix ans, l'authentification multifactorielle était rarement mise en œuvre.

Si les développeurs avaient investi dans un modèle de fournisseur d'identité unique et sécurisé, tel que l'identité fédérée SAML, le fournisseur d'identité pourrait être mis à jour pour intégrer de nouvelles exigences telles que la conformité NIST 800-63, sans pour autant modifier les interfaces de l'application d'origine. Si de nombreuses applications partageaient la même architecture de sécurité et donc le même composant, elles bénéficient toutes de cette mise à jour en même temps. Toutefois, SAML ne restera pas toujours la meilleure ou la plus appropriée des solutions d'authentification - il pourrait être nécessaire de le remplacer par d'autres solutions au fur et à mesure que les exigences changent. De telles modifications sont soit compliquées, si coûteuses qu'elles nécessitent une réécriture complète, soit carrément impossibles sans architecture de sécurité.

Dans ce chapitre, l'ASVS couvre les principaux aspects de toute architecture de sécurité solide : disponibilité, confidentialité, intégrité du traitement, non-répudiation et respect de la vie privée. Chacun de ces principes de sécurité doit être intégré et inné à toutes les applications. Il est essentiel de "tourner à gauche", en commençant par l'habilitation des développeurs avec des listes de contrôle de codage sécurisé, le mentorat et la formation, le codage et les tests, la construction, le déploiement, la configuration et les opérations, et en terminant par des tests indépendants de suivi pour s'assurer que tous les contrôles de sécurité sont présents et fonctionnels. La dernière étape était autrefois tout ce que nous faisions en tant qu'industrie, mais cela ne suffit plus lorsque les développeurs mettent le code en production des dizaines ou des centaines de fois par jour. Les professionnels de la sécurité des applications doivent se tenir au courant des techniques agiles, ce qui signifie adopter les outils des développeurs, apprendre à coder et travailler avec eux plutôt que de critiquer le projet des mois après que tout le monde est passé à autre chose.

## V1.1 Exigences relatives au cycle de vie du développement de logiciels sécurisés

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.1.1** | Vérifier l'utilisation d'un cycle de développement de logiciel sécurisé qui prend en compte la sécurité à tous les stades du développement. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **1.1.2** | Vérifier l'utilisation de la modélisation des menaces pour chaque modification de conception ou planification de sprint afin d'identifier les menaces, de planifier les contre-mesures, de faciliter les réponses appropriées aux risques et d'orienter les tests de sécurité. | | ✓ | ✓ | 1053 |
| **1.1.3** | Vérifiez que toutes les récits utilisateurs et les fonctionnalités contiennent des contraintes de sécurité fonctionnelles, telles que "En tant qu'utilisateur, je devrais pouvoir consulter et modifier mon profil. Je ne devrais pas pouvoir voir ou modifier le profil de quelqu'un d'autre" | | ✓ | ✓ | 1110 |
| **1.1.4** | Vérifier la documentation et la justification de toutes les frontières de confiance de la demande, de ses composantes et des flux de données importants. | | ✓ | ✓ | 1059 |
| **1.1.5** | Vérifier la définition et l'analyse de sécurité de l'architecture de haut niveau de l'application et de tous les services à distance connectés. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1059 |
| **1.1.6** | Vérifier la mise en œuvre de contrôles de sécurité centralisés, simples (économie de conception), vérifiés, sécurisés et réutilisables pour éviter les contrôles en double, manquants, inefficaces ou peu sûrs. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 637 |
| **1.1.7** | Vérifier que tous les développeurs et testeurs disposent d'une liste de contrôle de codage sécurisé, d'exigences de sécurité, de lignes directrices ou de politiques. | | ✓ | ✓ | 637 |
| **1.1.8** | Vérifier la disponibilité d'un fichier [security.txt](https://securitytxt.org/) accessible au public à la racine ou dans le répertoire .known de l'application, qui définit clairement un lien ou une adresse électronique permettant aux personnes de contacter les propriétaires pour des questions de sécurité. | | ✓ | ✓ | 1059 |

## V1.2 Exigences architecturales d'authentification

Lors de la conception de l'authentification, il importe peu que vous disposiez d'un matériel solide permettant une authentification multifactorielle si un attaquant peut réinitialiser un compte en appelant un centre d'appel et en répondant à des questions courantes. Lors de la vérification de l'identité, toutes les méthodes d'authentification doivent avoir la même force.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.2.1** | Vérifier que les communications entre les composants de l'application, y compris les API, les intergiciels et les couches de données, sont authentifiées et utilisent des comptes utilisateurs individuels. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 306 |
| **1.2.2** | Vérifiez que l'application utilise un mécanisme d'authentification unique et contrôlé qui est connu pour être sûr, qui peut être étendu pour inclure une authentification forte et qui dispose d'une journalisation et d'une surveillance suffisantes pour détecter les abus ou les violations de compte. | | ✓ | ✓ | 306 |
| **1.2.3** | Vérifier que toutes les méthodes d'authentification et les API de gestion de l'identité mettent en œuvre un contrôle de sécurité de l'authentification cohérent, de sorte qu'il n'y ait pas d'alternatives plus faibles par rapport au risque de l'application. | | ✓ | ✓ | 306 |

## V1.3 Exigences architecturales pour la gestion des sessions

Il s'agit d'un point de repère pour les futures exigences architecturales.

## V1.4 Exigences architecturales en matière de contrôle d'accès

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.4.1** | Vérifiez que des points d'application de confiance tels que les passerelles de contrôle d'accès, les serveurs et les fonctions sans serveur font respecter les contrôles d'accès. N'imposez jamais de contrôles d'accès au client. | | ✓ | ✓ | 602 |
| **1.4.2** | Vérifiez que la solution de contrôle d'accès choisie est suffisamment souple pour répondre aux besoins de l'application.  | | ✓ | ✓ | 284 |
| **1.4.3** | Vérifier l'application du principe du moindre privilège dans les fonctions, fichiers de données, URL, contrôleurs, services et autres ressources. Cela implique une protection contre l'usurpation et l'élévation des privilèges. | | ✓ | ✓ | 272 |
| **1.4.4** | Vérifier que les communications entre les composants de l'application, y compris les API, les intergiciels et les couches de données, sont effectuées avec le moins de privilèges possibles. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 272 |
| **1.4.5** | Vérifier que l'application utilise un mécanisme de contrôle d'accès unique et bien étudié pour accéder aux données et ressources protégées. Toutes les demandes doivent passer par ce mécanisme unique pour éviter le copier-coller ou les chemins alternatifs non sécurisés. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 284 |
| **1.4.6** | Vérifiez que le contrôle d'accès basé sur les attributs ou les caractéristiques est utilisé, c'est-à-dire que le code vérifie l'autorisation de l'utilisateur pour une caractéristique ou une donnée plutôt que son seul rôle. Les autorisations doivent tout de même être attribuées à l'aide de rôles. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 275 |

## V1.5 Exigences architecturales d'entrée et de sortie

Dans la version 4.0, nous avons abandonné le terme "côté serveur" ayant la connotation de limite de confiance. La limite de confiance est toujours un  enjeu - il est possible de contourner les décisions prises sur des navigateurs ou des appareils clients non fiables. Cependant, dans les déploiements architecturaux courants d'aujourd'hui, le point d'application de la confiance a considérablement changé. Par conséquent, lorsque le terme "couche de service de confiance" est utilisé dans l'ASVS, nous entendons par là tout point d'application de confiance, quel que soit son emplacement, tel qu'un microservice, un API sans serveur, côté serveur, un API de confiance sur un périphérique client qui a un démarrage sécurisé, des API partenaires ou externes, etc. 

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.5.1** | Vérifier que les exigences en matière d'entrée et de sortie définissent clairement la manière de traiter et d'exploiter les données en fonction du type, du contenu et de la conformité aux lois, règlements et autres politiques applicables.  | | ✓ | ✓ | 1029 |
| **1.5.2** | Vérifiez que la sérialisation n'est pas utilisée lorsque vous communiquez avec des clients non fiables. Si cela n'est pas possible, assurez-vous que des contrôles d'intégrité adéquats (et éventuellement un cryptage si des données sensibles sont envoyées) sont appliqués pour empêcher les attaques de désérialisation, y compris l'injection d'objets. | | ✓ | ✓ | 502 |
| **1.5.3** | Vérifiez que la validation des entrées est appliquée sur une couche de service de confiance. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 602 |
| **1.5.4** | Vérifiez que l'encodage de sortie se fait à proximité ou par l'interprète auquel il est destiné. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 116 |

## V1.6 Exigences en matière d'architecture cryptographique

Les applications doivent être conçues avec une architecture cryptographique solide pour protéger les données selon leur classification. Tout chiffrer est un gaspillage, ne rien chiffrer est une négligence légale. Un équilibre doit être trouvé, généralement lors de la conception architecturale ou de haut niveau, des sprints de conception ou des pics architecturaux. Concevoir la cryptographie au fur et à mesure ou l'adapter coûtera inévitablement beaucoup plus cher à mettre en œuvre de manière sécurisée que de l'intégrer dès le départ.

Les exigences architecturales sont intrinsèques à l'entièreté du code, et donc difficiles à unifier ou à intégrer dans les tests. Les exigences architecturales doivent être prises en compte dans les normes de codage, tout au long de la phase de codage, et doivent être examinées au cours de l'architecture de sécurité, des examens du code par les pairs, ou des rétrospectives.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.6.1** | Vérifier qu'il existe une politique explicite de gestion des clés cryptographiques et que le cycle de vie d'une clé cryptographique suit une norme de gestion des clés telle que NIST SP 800-57. | | ✓ | ✓ | 320 |
| **1.6.2** | Vérifier que les consommateurs de services cryptographiques protègent les clés et autres secrets en utilisant des coffres-forts de clés ou des alternatives basées sur l'API. | | ✓ | ✓ | 320 |
| **1.6.3** | Vérifiez que toutes les clés et tous les mots de passe sont remplaçables et font partie d'un processus bien défini de recryptage des données sensibles. | | ✓ | ✓ | 320 |
| **1.6.4** | Vérifier que les clés symétriques, les mots de passe ou les secrets d'API générés par les clients ou partagés avec eux ne sont utilisés que pour protéger des secrets à faible risque, comme le chiffrement du stockage local, ou des utilisations éphémères temporaires comme l'obscurcissement des paramètres. Le partage de secrets avec les clients est équivalent à du texte en clair et, d'un point de vue architectural, il doit être traité comme tel. | | ✓ | ✓ | 320 |

## V1.7 Erreurs, enregistrement et vérification des exigences architecturales

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.7.1** | Vérifier qu'un format de journalisation communs soit utilisés dans le système.  ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1009 |
| **1.7.2** | Vérifiez que les journaux sont transmis de manière sécurisée à un système de préférence distant pour analyse, détection, alerte et escalade. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

## V1.8 Exigences architecturales en matière de protection des données et de la vie privée

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.8.1** | Vérifier que toutes les données sensibles sont identifiées et classées en niveaux de protection. | | ✓ | ✓ | |
| **1.8.2** | Vérifier que tous les niveaux de protection sont associés à un ensemble d'exigences de protection, telles que des exigences de cryptage, d'intégrité, de conservation, de respect de la vie privée et d'autres exigences de confidentialité, et que celles-ci sont appliquées dans l'architecture. | | ✓ | ✓ | |

## V1.9 Exigences en matière d'architecture des communications

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.9.1** | Vérifier que l'application chiffre les communications entre les composants, en particulier lorsque ces composants se trouvent dans des conteneurs, systèmes, sites ou fournisseurs de cloud différents. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 319 |
| **1.9.2** | Vérifier que les composants de l'application vérifient l'authenticité de chaque partie d'un lien de communication afin de prévenir les attaques de type "man-in-the-middle". Par exemple, les composants d'application doivent valider les certificats et les chaînes TLS. | | ✓ | ✓ | 295 |

## V1.10 Exigences en matière d'architecture des logiciels malveillants

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.10.1** | Vérifier qu'un système de contrôle du code source est utilisé, avec des procédures pour s'assurer que les enregistrements sont accompagnés de tickets d'émission ou de modification. Le système de contrôle du code source doit disposer d'un contrôle d'accès et d'utilisateurs identifiables pour permettre la traçabilité de toute modification. | | ✓ | ✓ | 284 |

## V1.11 Exigences en matière d'architecture de la logique d'entreprise

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.11.1** | Vérifier la définition et la documentation de tous les composants de l'application en ce qui concerne la logique d'affaire ou de sécurité qu'ils fournissent. | | ✓ | ✓ | 1059 |
| **1.11.2** | Vérifiez que tous les flux de logique d'affaire de grande valeur, y compris l'authentification, la gestion de session et le contrôle d'accès, ne partagent pas un état non synchronisé. | | ✓ | ✓ | 362 |
| **1.11.3** | Vérifier que tous les flux de logique d'entreprise de grande valeur, y compris l'authentification, la gestion de session et le contrôle d'accès, sont sécurisés et résistants aux conditions de concurrence ("race condition") au temps de contrôle et au temps d'utilisation. | | | ✓ | 367 |

## V1.12 Téléchargement de fichiers sécurisés Exigences architecturales

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.12.1** | Vérifiez que les fichiers envoyés par l'utilisateur sont stockés en dehors de la racine du site web. | | ✓ | ✓ | 552 |
| **1.12.2** | Vérifiez que les fichiers envoyés par l'utilisateur - s'ils doivent être affichés ou téléchargés à partir de l'application - sont servis par des téléchargements en flux d'octets, ou à partir d'un domaine sans rapport, comme un seau de stockage de fichiers en nuage. Mettre en œuvre une politique de sécurité du contenu (CSP) appropriée pour réduire le risque de vecteurs XSS ou d'autres attaques provenant du fichier téléchargé. | | ✓ | ✓ | 646 |

## V1.13 Exigences architecturales de l'API

Il s'agit d'un point de repère pour les futures exigences architecturales.

## V1.14 Configuration des exigences architecturales

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.14.1** | Vérifier l'utilisation d'un compte à faible privilège pour tous les composants d'application, services et serveurs. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 250 |
| **1.14.2** | Vérifiez la séparation des composants de différents niveaux de confiance via des contrôles de sécurité bien définis, des règles de pare-feu, des passerelles API, des proxys inverses, des groupes de sécurité basés sur le cloud ou des mécanismes similaires. | | ✓ | ✓ | 923 |
| **1.14.3** | Vérifier que les signatures binaires, les connexions de confiance et les nœuds vérifiés sont utilisés pour déployer des binaires sur des dispositifs distants. | | ✓ | ✓ | 494 |
| **1.14.4** | Vérifier que le pipeline de construction signale les composants obsolètes ou peu sûrs et prend les mesures appropriées. | | ✓ | ✓ | 1104 |
| **1.14.5** | Vérifier que le pipeline de construction contient une étape de compilation pour créer automatiquement et vérifier le déploiement sécurisé de l'application, en particulier si l'infrastructure de l'application est définie par un logiciel, comme les scripts de construction d'un environnement en nuage. | | ✓ | ✓ | |
| **1.14.6** | Vérifier que les déploiements d'applications sont correctement sandboxés, conteneurisés et/ou isolés au niveau du réseau pour retarder et dissuader les attaquants d'attaquer d'autres applications, en particulier lorsqu'ils effectuent des actions sensibles ou dangereuses telles que la désérialisation. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |
| **1.14.7** | Vérifiez que l'application n'utilise pas de technologies côté client non prises en charge, peu sûres ou dépréciées telles que les plugins NSAPI, Flash, Shockwave, ActiveX, Silverlight, NACL ou les applets Java côté client. | | ✓ | ✓ | 477 |

## Références

Pour plus d'informations, voir aussi :

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
