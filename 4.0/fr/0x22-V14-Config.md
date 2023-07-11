# V14 Exigences de vérification de la configuration

## Objectif de contrôle

Assurez-vous qu'une application vérifiée satisfait :

* Un environnement de construction sécurisé, reproductible et automatisable.
* Une gestion des dépendances étroite et une configuration renforcée, de sorte que les composants obsolètes ou non sécurisés ne soient pas inclus dans l'application.

La configuration de l'application "out of the box" doit être sûre pour être sur Internet, ce qui signifie une configuration "out of the box".

## V14.1 Exigences sur les constructions

Les pipelines de construction sont la base d'une sécurité reproductible : chaque fois qu'un élément non sécurisé est découvert, il peut être résolu dans le code source, les scripts de construction ou de déploiement, et testé automatiquement. Nous encourageons fortement l'utilisation de pipelines de compilation avec des contrôles de sécurité et de dépendance automatiques qui avertissent ou interrompent la compilation afin d'éviter que des problèmes de sécurité connus ne soient déployés en production. Les étapes manuelles effectuées de manière irrégulière conduisent directement à des erreurs de sécurité évitables.

Alors que l'industrie se dirige vers un modèle DevSecOps, il est important de garantir la disponibilité et l'intégrité continues du déploiement et de la configuration pour atteindre un état "known good". Dans le passé, si un système était piraté, il fallait des jours, voire des mois, pour prouver qu'aucune autre intrusion n'avait eu lieu. Aujourd'hui, avec l'avènement des infrastructures définies par logiciel, des déploiements A/B rapides sans aucun temps d'arrêt, et des constructions automatisées conteneurisées, il est possible de construire, de durcir et de déployer automatiquement et en continu un "known good" en remplacement de tout système compromis.

Si les modèles traditionnels sont toujours en place, des mesures manuelles doivent être prises pour renforcer et sauvegarder cette configuration afin de permettre le remplacement rapide des systèmes compromis par des systèmes à haute intégrité et sans compromis, et ce dans les meilleurs délais.

La conformité à cette section nécessite un système de construction automatisé et l'accès à des scripts de construction et de déploiement.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.1.1** | Vérifier que les processus de construction et de déploiement des applications sont effectués de manière sûre et répétable, comme l'automatisation des CI / CD, la gestion automatisée de la configuration et les scripts de déploiement automatisés. | | ✓ | ✓ | |
| **14.1.2** | Vérifiez que les drapeaux du compilateur sont configurés pour activer toutes les protections et les avertissements disponibles contre les débordements de mémoire tampon, y compris la randomisation de la pile, la prévention de l'exécution des données, et pour casser la compilation si un pointeur, une mémoire, une chaîne de format, un entier ou une chaîne de caractères dangereux sont trouvés. | | ✓ | ✓ | 120 |
| **14.1.3** | Vérifiez que la configuration du serveur est durcie conformément aux recommandations du serveur d'application et des frameworks utilisés. | | ✓ | ✓ | 16 |
| **14.1.4** | Vérifier que l'application, la configuration et toutes les dépendances peuvent être redéployées à l'aide de scripts de déploiement automatisés, construites à partir d'un runbook documenté et testé dans un délai raisonnable, ou restaurées à partir de sauvegardes en temps utile. | | ✓ | ✓ | |
| **14.1.5** | Vérifier que les administrateurs autorisés peuvent vérifier l'intégrité de toutes les configurations pertinentes pour la sécurité afin de détecter les altérations. | | | ✓ | |

## V14.2 Exigences sur les dépendances

La gestion des dépendances est essentielle au bon fonctionnement de toute application, quel que soit son type. L'incapacité à se tenir à jour avec des dépendances obsolètes ou peu sûres est la cause première des attaques les plus importantes et les plus coûteuses à ce jour.

Remarque : au niveau 1, la conformité à la norme 14.2.1 concerne les observations ou les détections de bibliothèques et de composants côté client et autres, plutôt que l'analyse statique du code de construction ou l'analyse des dépendances, plus précise. Ces techniques plus précises pourraient être découvertes par des entretiens, le cas échéant.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.2.1** | Vérifiez que tous les composants sont à jour, de préférence en utilisant un vérificateur de dépendances pendant le temps de construction ou de compilation. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1026 |
| **14.2.2** | Vérifiez que toutes les fonctionnalités, la documentation, les applications d'exemple et les configurations inutiles sont supprimées. | ✓ | ✓ | ✓ | 1002 |
| **14.2.3** | Vérifier que si les actifs d'application, tels que les bibliothèques JavaScript, les feuilles de style CSS ou les polices web, sont hébergés en externe sur un réseau de diffusion de contenu (CDN) ou un fournisseur externe, l'intégrité des sous-ressources (SRI) est utilisée pour valider l'intégrité de l'actif. | ✓ | ✓ | ✓ | 829 |
| **14.2.4** | Vérifier que les composants tiers proviennent de dépôts prédéfinis, fiables et continuellement entretenus. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 829 |
| **14.2.5** | Vérifier qu'un catalogue d'inventaire de toutes les bibliothèques tierces en service est tenu à jour. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **14.2.6** | Vérifiez que la surface d'attaque est réduite en mettant en bac à sable ou en encapsulant des bibliothèques tierces pour n'exposer que le comportement requis dans l'application. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |

## V14.3 Exigences de divulgation involontaire de renseignements sur la sécurité

Les configurations de production devraient être renforcées pour se protéger contre les attaques courantes, telles que les consoles de débogage, relever la barre pour les attaques de type "cross-site scripting" (XSS) et "remote file inclusion" (RFI), et pour éliminer les "vulnérabilités" triviales de découverte d'informations qui sont la marque indésirable de nombreux rapports de tests de pénétration. Nombre de ces problèmes sont rarement considérés comme un risque important, mais ils sont liés à d'autres vulnérabilités. Si ces problèmes ne sont pas présents par défaut, elle place la barre plus haute avant que la plupart des attaques puissent réussir.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.3.1** | [SUPPRIMÉ, DOUBLON AVEC L'EXIGENCE 7.4.1] | | | | |
| **14.3.2** | Vérifier que les modes de débogage du serveur web ou d'application et du cadre d'application sont désactivés en production afin d'éliminer les fonctionnalités de débogage, les consoles de développement et les divulgations de sécurité non intentionnelles. | ✓ | ✓ | ✓ | 497 |
| **14.3.3** | Vérifiez que les en-têtes HTTP ou toute partie de la réponse HTTP n'exposent pas d'informations détaillées sur la version des composants du système. | ✓ | ✓ | ✓ | 200 |

## V14.4 Exigences relatives aux en-têtes de sécurité HTTP

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.4.1** | Vérifiez que chaque réponse HTTP contient un en-tête Content-Type. Les types de contenu text/*, */*+xml et application/xml doivent également spécifier un jeu de caractères sûr (par exemple, UTF-8, ISO-8859-1). | ✓ | ✓ | ✓ | 173 |
| **14.4.2** | Vérifiez que toutes les réponses de l'API contiennent Content-Disposition : attachment ; filename="api.json" (ou tout autre nom de fichier approprié pour le type de contenu). | ✓ | ✓ | ✓ | 116 |
| **14.4.3** | Vérifier qu'une politique de sécurité du contenu (CSP) est en place pour aider à atténuer l'impact des attaques XSS comme les vulnérabilités d'injection HTML, DOM, JSON et JavaScript. | ✓ | ✓ | ✓ | 1021 |
| **14.4.4** | Vérifiez que toutes les réponses contiennent X-Content-Type-Options: nosniff. | ✓ | ✓ | ✓ | 116 |
| **14.4.5** | Vérifiez que l'en-tête Strict-Transport-Security est inclus dans toutes les réponses et pour tous les sous-domaines, comme Strict-Transport-Security : max-age=15724800 ; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **14.4.6** | Vérifiez qu'un en-tête "Referrer-Policy" approprié est inclus, tel que "no-referrer" ou "same-origin". | ✓ | ✓ | ✓ | 116 |
| **14.4.7** | Vérifier que le contenu d'une application web ne peut pas être intégré par défaut dans un site tiers et que l'intégration des ressources exactes n'est autorisée que si nécessaire en utilisant un en-tête approprié tel "Content-Security-Policy: frame-ancestors" ou "X-Frame-Options". | ✓ | ✓ | ✓ | 1021 |

## V14.5 Exigences sur la validation des en-têtes de requête HTTP

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.5.1** | Vérifiez que le serveur d'application accepte seulement les méthodes HTTP utilisées par l'application/API (incluant les requetes de type OPTIONS), et les journalise/alertes sur toutes les demandes qui sont invalades pour le contexte de l'application. | ✓ | ✓ | ✓ | 749 |
| **14.5.2** | Vérifiez que l'en-tête Origin fourni n'est pas utilisé pour les décisions d'authentification ou de contrôle d'accès, car l'en-tête Origin peut facilement être modifié par un attaquant. | ✓ | ✓ | ✓ | 346 |
| **14.5.3** | Vérifiez que l'en-tête "Cross-Origin Resource Sharing" (CORS) Access-Control-Allow-Origin utilise une liste d'autorisation stricte de domaines et sous-domaines de confiance pour la comparaison avec l'origine "null" et ne la prend pas en charge. | ✓ | ✓ | ✓ | 346 |
| **14.5.4** | Vérifiez que les en-têtes HTTP ajoutés par un proxy de confiance ou des dispositifs SSO, tels qu'un jeton au porteur, sont authentifiés par l'application. | | ✓ | ✓ | 306 |

## Références

Pour plus d'informations, voir aussi :

* [OWASP Web Security Testing Guide 4.1: Testing for HTTP Verb Tampering]( https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* Adding Content-Disposition to API responses helps prevent many attacks based on misunderstanding on the MIME type between client and server, and the "filename" option specifically helps prevent [Reflected File Download attacks.](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Sandboxing third party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
