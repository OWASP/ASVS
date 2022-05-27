# V1 Architecture, conception et modélisation des menaces

## Objectif des contrôles

L'architecture de sécurité est presque devenue un art perdu dans de nombreuses organisations. L'époque de l'architecte d'entreprise est révolue à l'ère du DevSecOps. Le domaine de la sécurité des applications doit rattraper son retard et adopter les principes de la sécurité agile tout en réintroduisant les principes de l'architecture de sécurité aux praticiens du logiciel. L'architecture n'est pas une mise en œuvre, mais une façon de penser à un problème qui a potentiellement de nombreuses réponses différentes, et pas une seule réponse "correcte". Trop souvent, la sécurité est considérée comme inflexible et exigeant que les développeurs corrigent le code d'une manière particulière, alors que ces derniers connaissent peut-être une bien meilleure façon de résoudre le problème. Il n'existe pas de solution unique et simple pour l'architecture, et prétendre le contraire est un mauvais service rendu au domaine du génie logiciel.

Une mise en œuvre spécifique d'une application web est susceptible d'être révisée en permanence tout au long de sa durée de vie, mais l'architecture globale ne changera probablement que rarement, mais évoluera lentement. L'architecture de sécurité est identique : nous avons besoin d'une authentification aujourd'hui, nous en aurons besoin demain, et nous en aurons besoin dans cinq ans. Si nous prenons des décisions judicieuses aujourd'hui, nous pouvons économiser beaucoup d'efforts, de temps et d'argent si nous sélectionnons et réutilisons des solutions conformes à l'architecture. Par exemple, il y a dix ans, l'authentification multifactorielle était rarement mise en œuvre.

Si les développeurs avaient investi dans un modèle de fournisseur d'identité unique et sécurisé, tel que l'identité fédérée SAML, le fournisseur d'identité pouvait être mis à jour pour intégrer de nouvelles exigences telles que la conformité à la norme NIST 800-63, sans modifier les interfaces de l'application d'origine. Si de nombreuses applications partagent la même architecture de sécurité et donc ce même composant, elles bénéficient toutes de cette mise à jour en même temps. Cependant, SAML ne restera pas toujours la meilleure solution d'authentification ou la plus adaptée - il faudra peut-être la remplacer par d'autres solutions en fonction de l'évolution des besoins. Les changements de ce type sont soit compliqués, soit si coûteux qu'ils nécessitent une réécriture complète, soit carrément impossibles sans architecture de sécurité.

Dans ce chapitre, l'ASVS couvre les principaux aspects de toute architecture de sécurité solide : disponibilité, confidentialité, intégrité du traitement, non-répudiation et vie privée. Chacun de ces principes de sécurité doit être intégré et être inné dans toutes les applications. Il est essentiel de "passer à gauche", en commençant par l'habilitation des développeurs avec des listes de contrôle de codage sécurisé, le mentorat et la formation, le codage et les tests, la construction, le déploiement, la configuration et les opérations, et en terminant par des tests indépendants de suivi pour s'assurer que tous les contrôles de sécurité sont présents et fonctionnels. La dernière étape était autrefois tout ce que nous faisions en tant qu'industrie, mais ce n'est plus suffisant lorsque les développeurs mettent du code en production des dizaines ou des centaines de fois par jour. Les professionnels de la sécurité des applications doivent suivre les techniques agiles, ce qui signifie adopter des outils de développement, apprendre à coder et travailler avec les développeurs plutôt que de critiquer le projet des mois après que tout le monde soit passé à autre chose.

## V1.1 Cycle de vie du développement sécurisé de logiciel

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.1.1** | Vérifier l'utilisation d'un cycle de vie de développement logiciel sécurisé qui prend en compte la sécurité à tous les stades du développement. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **1.1.2** | Vérifier l'utilisation de la modélisation des menaces pour chaque changement de conception ou planification de sprint afin d'identifier les menaces, de prévoir des contre-mesures, de faciliter les réponses appropriées aux risques et de guider les tests de sécurité. | | ✓ | ✓ | 1053 |
| **1.1.3** | Vérifiez que toutes les "user stories" et fonctionnalités contiennent des contraintes de sécurité fonctionnelles, telles que "En tant qu'utilisateur, je devrais pouvoir afficher et modifier mon profil. Je ne devrais pas pouvoir afficher ou modifier le profil de quelqu'un d'autre" | | ✓ | ✓ | 1110 |
| **1.1.4** | Vérifiez la documentation et la justification de toutes les limites de confiance, composants et flux de données significatifs de l'application. | | ✓ | ✓ | 1059 |
| **1.1.5** | Vérifier la définition et l'analyse de la sécurité de l'architecture de haut niveau de l'application et de tous les services distants connectés. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1059 |
| **1.1.6** | Vérifiez la mise en œuvre de contrôles de sécurité centralisés, simples (économie de conception), vérifiés, sécurisés et réutilisables pour éviter les contrôles en double, manquants, inefficaces ou non sécurisés. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 637 |
| **1.1.7** | Vérifiez la disponibilité d'une liste de contrôle de développement sécurisé, d'exigences de sécurité, de directives ou de politiques pour tous les développeurs et testeurs. | | ✓ | ✓ | 637 |

## V1.2 Architecture d'authentification

Lors de la conception de l'authentification, peu importe que vous disposiez d'une authentification multifacteur puissante activée par le matériel si un attaquant peut réinitialiser un compte en appelant un centre d'appels et en répondant aux questions les plus courantes. Lors de la preuve d'identité, toutes les voies d'authentification doivent avoir la même force.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.2.1** | Vérifiez l'utilisation de comptes de système d'exploitation uniques ou spéciaux à faibles privilèges pour tous les composants, services et serveurs d'application. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 250 |
| **1.2.2** | Vérifier que les communications entre les composants de l'application, y compris les API, les intergiciels et les couches de données, sont authentifiées. Les composants doivent disposer du minimum de privilèges nécessaires. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 306 |
| **1.2.3** | Vérifiez que l'application utilise un seul mécanisme d'authentification vérifié, connu pour être sûr, qui peut être étendu pour inclure une authentification forte et qui dispose d'une journalisation et d'une surveillance suffisantes pour détecter les abus ou les violations de compte. | | ✓ | ✓ | 306 |
| **1.2.4** | Vérifier que toutes les chemins d'authentification et les API de gestion des identités mettent en œuvre une force de contrôle de sécurité d'authentification cohérente, de sorte qu'il n'existe pas d'alternatives plus faibles par rapport au risque de l'application. | | ✓ | ✓ | 306 |

## V1.3 Architecture de gestion de session

Il s'agit d'un espace réservé pour les exigences architecturales futures.

## V1.4 Architecture de contrôle d'accès

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.4.1** | Vérifiez que les points d'application de confiance, tels que les passerelles de contrôle d'accès, les serveurs et les fonctions sans serveur, appliquent les contrôles d'accès. Ne jamais appliquer les contrôles d'accès sur le client. | | ✓ | ✓ | 602 |
| **1.4.2** | [DELETED, NOT ACTIONABLE] | | | | |
| **1.4.3** | [DELETED, DUPLICATE OF 4.1.3] | | | | |
| **1.4.4** | Vérifiez que l'application utilise un mécanisme de contrôle d'accès unique et éprouvé pour accéder aux données et ressources protégées. Toutes les demandes doivent passer par ce mécanisme unique pour éviter les copier-coller ou les chemins alternatifs non sécurisés. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 284 |
| **1.4.5** | Vérifiez que le contrôle d'accès basé sur les attributs ou les fonctionnalités est utilisé, le code vérifiant l'autorisation de l'utilisateur pour une fonctionnalité/un élément de données plutôt que pour son seul rôle. Les autorisations doivent toujours être attribuées à l'aide de rôles. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 275 |

## V1.5 Architecture d'entrée et de sortie

Dans la version 4.0, nous avons abandonné le terme "côté serveur" en tant que limite de confiance chargée. La frontière de confiance est toujours concernée - il est possible de contourner les décisions prises sur des navigateurs ou des périphériques clients non fiables. Cependant, dans les déploiements architecturaux courants d'aujourd'hui, le point d'application de la confiance a radicalement changé. Par conséquent, lorsque le terme "couche de service de confiance" est utilisé dans l'ASVS, nous entendons tout point d'application de confiance, indépendamment de l'emplacement, comme un microservice, une API sans serveur, côté serveur, une API de confiance sur un dispositif client qui a un démarrage sécurisé, des API partenaires ou externes, et ainsi de suite.

Le terme "client non fiable" désigne ici les technologies côté client qui rendent la couche de présentation, communément appelées technologies "front-end". Le terme "sérialisation" fait ici référence non seulement à l'envoi de données sur le fil comme un tableau de valeurs ou à la prise et la lecture d'une structure JSON, mais aussi au passage d'objets complexes pouvant contenir de la logique.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.5.1** | Vérifiez que les exigences d'entrée et de sortie définissent clairement la manière de traiter et de manipuler les données en fonction de leur type, de leur contenu et des lois, réglementations et autres règles applicables. | | ✓ | ✓ | 1029 |
| **1.5.2** | Vérifiez que la sérialisation n'est pas utilisée lors de la communication avec des clients non fiables. Si cela n'est pas possible, assurez-vous que des contrôles d'intégrité adéquats (et éventuellement un chiffrement si des données sensibles sont envoyées) sont appliqués pour empêcher les attaques par désérialisation, y compris l'injection d'objets. | | ✓ | ✓ | 502 |
| **1.5.3** | Vérifiez que la validation des entrées est appliquée sur une couche de service de confiance. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 602 |
| **1.5.4** | Vérifiez que l'encodage de sortie se produit près de ou par l'interpréteur auquel il est destiné. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 116 |

## V1.6 Architecture cryptographique

Les applications doivent être conçues avec une architecture cryptographique forte pour protéger les données en fonction de leur classification. Tout chiffrer est un gaspillage, ne rien chiffrer est une négligence légale. Un équilibre doit être trouvé, généralement pendant la conception architecturale ou de haut niveau, les sprints de conception ou les pics d'architecture. Concevoir la cryptographie au fur et à mesure ou la mettre à niveau coûtera inévitablement beaucoup plus cher à mettre en œuvre de manière sécurisée que de l'intégrer dès le départ.

Les exigences architecturales sont intrinsèques à l'ensemble de la base de code, et donc difficiles à tester par unité ou par intégration. Les exigences architecturales doivent être prises en compte dans les normes de codage, tout au long de la phase de codage, et doivent être examinées au cours de l'architecture de sécurité, des examens par les pairs ou du code, ou des rétrospectives.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.6.1** | Vérifiez qu'il existe une politique explicite de gestion des clés cryptographiques et que le cycle de vie des clés cryptographiques suit une norme de gestion des clés telle que NIST SP 800-57. | | ✓ | ✓ | 320 |
| **1.6.2** | Vérifier que les consommateurs de services cryptographiques protègent les clés et autres secrets en utilisant des coffres-forts ou des alternatives basées sur l'API. | | ✓ | ✓ | 320 |
| **1.6.3** | Vérifiez que toutes les clés et tous les mots de passe sont remplaçables et qu'ils font partie d'un processus bien défini de re-chiffrement des données sensibles. | | ✓ | ✓ | 320 |
| **1.6.4** | Vérifiez que l'architecture traite les secrets côté client - tels que les clés symétriques, les mots de passe ou les jetons d'API - comme non sécurisés et ne les utilise jamais pour protéger ou accéder à des données sensibles. | | ✓ | ✓ | 320 |

## V1.7 Erreurs, journalisation et architecture d'audit

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.7.1** | Vérifiez qu'un format et une approche de journalisation communs sont utilisés dans tout le système. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1009 |
| **1.7.2** | Vérifiez que les journaux sont transmis de manière sécurisée à un système de préférence distant pour l'analyse, la détection, l'alerte et l'escalade. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

## V1.8 Architecture de protection des données et de la vie privée

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.8.1** | Vérifier que toutes les données sensibles sont identifiées et classées en niveaux de protection. | | ✓ | ✓ | |
| **1.8.2** | Vérifier que tous les niveaux de protection sont associés à un ensemble d'exigences de protection, telles que des exigences de chiffrement, d'intégrité, de conservation, de confidentialité et autres, et que celles-ci sont appliquées dans l'architecture. | | ✓ | ✓ | |

## V1.9 Architecture des communications

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.9.1** | Vérifiez que l'application chiffre les communications entre les composants, en particulier lorsque ces composants se trouvent dans des conteneurs, des systèmes, des sites ou des fournisseurs de cloud différents. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 319 |
| **1.9.2** | Vérifiez que les composants applicatifs vérifient l'authenticité de chaque côté d'une liaison de communication afin d'empêcher les attaques de type "Man In the Middle". Par exemple, les composants applicatifs doivent valider les certificats et les chaînes TLS. | | ✓ | ✓ | 295 |

## V1.10 Architecture des logiciels malveillants

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.10.1** | Vérifier qu'un système de contrôle du code source est utilisé, avec des procédures permettant de s'assurer que les enregistrements sont accompagnés de problèmes ou de tickets de changement. Le système de contrôle du code source doit comporter un contrôle d'accès et des utilisateurs identifiables afin de permettre la traçabilité de toute modification. | | ✓ | ✓ | 284 |

## V1.11 Architecture de la logique d'entreprise

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.11.1** | Vérifier la définition et la documentation de tous les composants applicatifs en fonction des fonctions commerciales ou de sécurité qu'ils assurent. | | ✓ | ✓ | 1059 |
| **1.11.2** | Vérifiez que tous les flux logiques de grande valeur, y compris l'authentification, la gestion des sessions et le contrôle d'accès, ne partagent pas un état non synchronisé. | | ✓ | ✓ | 362 |
| **1.11.3** | Vérifiez que tous les flux logiques de grande valeur, y compris l'authentification, la gestion des sessions et le contrôle d'accès, sont thread safe et résistants aux conditions de course de temps de vérification et de temps d'utilisation. | | | ✓ | 367 |

## V1.12 Architecture pour le téléchargement sécurisé de fichiers

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.12.1** | [DELETED, DUPLICATE OF 12.4.1] | | | | |
| **1.12.2** | Vérifiez que les fichiers téléchargés par l'utilisateur - s'ils doivent être affichés ou téléchargés à partir de l'application - sont servis soit par des téléchargements de flux d'octets, soit à partir d'un domaine non lié, tel qu'un Object Storage (exemple : S3) dans le cloud. Implémentez une politique de sécurité du contenu (CSP) appropriée pour réduire le risque de vecteurs XSS ou d'autres attaques à partir du fichier téléchargé. | | ✓ | ✓ | 646 |

## V1.13 Architecture des API

Il s'agit d'un espace réservé pour les futures exigences architecturales.

## V1.14 Architecture de configuration

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.14.1** | Vérifiez la séparation des composants de différents niveaux de confiance grâce à des contrôles de sécurité bien définis, des règles de pare-feu, des passerelles API, des proxys inverses, des groupes de sécurité basés sur le cloud ou des mécanismes similaires. | | ✓ | ✓ | 923 |
| **1.14.2** | Vérifiez que des signatures binaires, des connexions approuvées et des points de terminaison vérifiés sont utilisés pour déployer des binaires sur des appareils distants. | | ✓ | ✓ | 494 |
| **1.14.3** | Vérifiez que le pipeline de compilation signale les composants périmés ou non sécurisés et prend les mesures appropriées. | | ✓ | ✓ | 1104 |
| **1.14.4** | Vérifiez que le pipeline de construction contient une étape de construction pour construire et vérifier automatiquement le déploiement sécurisé de l'application, en particulier si l'infrastructure de l'application est définie par logiciel, comme les scripts de construction de l'environnement cloud. | | ✓ | ✓ | |
| **1.14.5** | Vérifiez que les déploiements d'applications sont correctement protégés par des bacs à sable, des conteneurs et/ou des isolations au niveau du réseau afin de retarder et de dissuader les attaquants d'attaquer d'autres applications, en particulier lorsqu'ils effectuent des actions sensibles ou dangereuses telles que la désérialisation. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |
| **1.14.6** | Vérifiez que l'application n'utilise pas de technologies côté client non prises en charge, non sécurisées ou obsolètes, telles que les plugins NSAPI, Flash, Shockwave, ActiveX, Silverlight, NACL ou les applets Java côté client. | | ✓ | ✓ | 477 |

## Références

Pour plus d'informations, voir également :

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
