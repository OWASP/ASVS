# V5 Exigences de validation, d'assainissement et de vérification de l'encodage

## Objectif de contrôle

La faiblesse la plus courante en matière de sécurité des applications web est l'incapacité à valider correctement les données provenant du client ou de l'environnement avant de les utiliser directement sans aucun encodage de sortie. Cette faiblesse est à l'origine de presque toutes les vulnérabilités importantes des applications web, telles que le Cross-Site Scripting (XSS), l'injection SQL, l'injection d'interpréteur, les attaques locales/Unicode, les attaques de système de fichiers et les débordements de mémoire tampon.

Assurez-vous qu'une application vérifiée satisfait aux exigences de haut niveau suivantes :

* La validation des entrées et l'architecture de codage des sorties ont un pipeline convenu pour prévenir les attaques par injection.
* Les données d'entrée sont fortement typées, validées, vérifiées en plage ou en longueur ou au pire, aseptisées ou filtrées.
* Les données de sortie sont codées ou échappées selon le contexte des données, aussi près que possible de l'interpréteur.

Avec l'architecture moderne des applications web, l'encodage des données de sortie est plus important que jamais. Il est difficile de fournir une validation robuste des entrées dans certains scénarios, de sorte que l'utilisation d'API plus sûres telles que les requêtes paramétrées, les frameworks de modélisation d'échappement automatique ou un encodage de sortie soigneusement choisi sont essentiels pour la sécurité de l'application.

## V5.1 Exigences de validation des entrées

Des contrôles de validation des entrées correctement mis en œuvre, utilisant une liste d'autorisation positive et un fort typage des données, peuvent éliminer plus de 90 % de toutes les attaques par injection. Les contrôles de longueur et de portée peuvent encore réduire ce phénomène. Il est nécessaire de mettre en place une validation d'entrée sécurisée pendant l'architecture de l'application, les sprints de conception, le codage et les tests unitaires et d'intégration. Bien que nombre de ces éléments ne puissent être trouvés dans les tests de pénétration, les résultats de leur non-implantation se trouvent généralement dans la version 5.3 - Exigences en matière de codage de sortie et de prévention des injections. Il est recommandé aux développeurs et aux réviseurs de codes sécurisés de traiter cette section comme si la L1 était requise pour tous les éléments afin de prévenir les injections.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.1.1** | Vérifiez que l'application dispose de défenses contre les attaques de pollution des paramètres HTTP, en particulier si le cadre de l'application ne fait aucune distinction quant à la source des paramètres de la requête (GET, POST, cookies, en-têtes ou variables d'environnement). | ✓ | ✓ | ✓ | 235 |
| **5.1.2** | Vérifiez que les cadriciels protègent contre les attaques par assignation massive de paramètres, ou que l'application dispose de contre-mesures pour protéger contre l'assignation dangereuse de paramètres, comme le marquage des champs privés ou similaires. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 915 |
| **5.1.3** | Vérifiez que toutes les entrées (champs de formulaire HTML, requêtes REST, paramètres URL, en-têtes HTTP, cookies, fichiers batch, flux RSS, etc) sont validées par une validation positive (liste d'autorisation). ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.4** | Vérifier que les données structurées sont fortement typées et validées par rapport à un schéma défini comprenant les caractères, la longueur et le modèle autorisés (par exemple, numéros de carte de crédit ou de téléphone, ou valider que deux champs connexes sont raisonnables, comme vérifier la correspondance entre la banlieue et le code postal). ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.5** | Vérifiez que les redirections et les transferts d'URL n'autorisent que les destinations prévues, ou affichez un avertissement lors d'une redirection vers un contenu potentiellement non fiable. | ✓ | ✓ | ✓ | 601 |

## V5.2 Exigences en matière d'assainissement et de « bac à sable »

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.2.1** | Vérifiez que toutes les entrées HTML non fiables provenant d'éditeurs WYSIWYG ou similaires sont correctement assainies avec une bibliothèque ou une fonction de framework de nettoyage HTML. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.2.2** | Vérifiez que les données non structurées sont assainies afin d'appliquer les mesures de sécurité telles que les caractères et la longueur autorisés. | ✓ | ✓ | ✓ | 138 |
| **5.2.3** | Vérifiez que l'application assainit les entrées de l'utilisateur avant de passer aux systèmes de messagerie pour protéger contre l'injection SMTP ou IMAP. | ✓ | ✓ | ✓ | 147 |
| **5.2.4** | Vérifiez que l'application évite l'utilisation de eval() ou d'autres fonctions d'exécution de code dynamique. Lorsqu'il n'y a pas d'alternative, toute entrée utilisateur incluse doit être assainie ou mise en sandbox avant d'être exécutée. | ✓ | ✓ | ✓ | 95 |
| **5.2.5** | Vérifiez que l'application protège contre les attaques par injection de modèles en veillant à ce que toute entrée de l'utilisateur incluse soit aseptisée ou mise en bac à sable. | ✓ | ✓ | ✓ | 94 |
| **5.2.6** | Vérifier que l'application protège contre les attaques SSRF, en validant ou en assainissant les données non fiables ou les métadonnées de fichiers HTTP, comme les noms de fichiers et les champs de saisie d'URL, utiliser la liste d'autorisation des protocoles, domaines, chemins et ports. | ✓ | ✓ | ✓ | 918 |
| **5.2.7** | Vérifiez que l'application assainit, désactive ou met en place une isolation (sandbox) pour le contenu scriptable fourni par l'utilisateur (Scalable Vector Graphics - SVG), en particulier en ce qui concerne les XSS résultant de scripts natifs au code présent et foreignObject. | ✓ | ✓ | ✓ | 159 |
| **5.2.8** | Vérifiez que l'application assainit, désactive ou met en sandbox le contenu des scripts ou des modèles d'expression fournis par l'utilisateur, tels que les feuilles de style Markdown, CSS ou XSL, le BBCode ou autres. | ✓ | ✓ | ✓ | 94 |

## V5.3 Exigences en matière d'encodage de sortie et de prévention des injections

L'encodage de la sortie à proximité de l'interprète utilisé est essentiel pour la sécurité de toute application. Généralement, l'encodage de sortie n'est pas persistant, mais utilisé pour rendre la sortie sûre dans le contexte de sortie approprié pour une utilisation immédiate. Le défaut d'encodage de la sortie entraînera une application non sécurisée, injectable et dangereuse.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.3.1** | Vérifiez que l'encodage de sortie est pertinent pour l'interprète et le contexte requis. Par exemple, utilisez des encodeurs spécifiques pour les valeurs HTML, les attributs HTML, JavaScript, les paramètres URL, les en-têtes HTTP, SMTP et autres selon le contexte, en particulier à partir d'entrées non fiables (par exemple les noms avec Unicode ou apostrophes, comme ねこ ou O'Hara). ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.3.2** | Vérifiez que l'encodage de sortie préserve le jeu de caractères et la langue choisis par l'utilisateur, de sorte que tout point de caractère Unicode soit valide et traité en toute sécurité. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 176 |
| **5.3.3** | Vérifiez que l'encodage des sorties en fonction du contexte, de préférence automatisé - ou au pire, manuel - protège contre le XSS réfléchi, stocké et basé sur le DOM. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 79 |
| **5.3.4** | Vérifier que la sélection de données ou les requêtes de base de données (par exemple SQL, HQL, ORM, NoSQL) utilisent des requêtes paramétrées, des ORM, des cadres d'entités, ou sont autrement protégées contre les attaques par injection de base de données. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.5** | Vérifiez que, lorsque des mécanismes paramétrés ou plus sûrs ne sont pas présents, un encodage de sortie spécifique au contexte est utilisé pour se protéger contre les attaques par injection, comme l'utilisation de l'échappement SQL pour se protéger contre l'injection SQL. ([C3, C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.6** | Vérifiez que l'application se protège contre les attaques par injection de JSON, les attaques par évaluation de JSON et les évaluations d'expressions JavaScript. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 830 |
| **5.3.7** | Vérifiez que l'application protège contre les vulnérabilités de LDAP Injection, ou que des contrôles de sécurité spécifiques pour empêcher des injections LDAP ont été mis en place. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 90 |
| **5.3.8** | Vérifiez que l'application protège contre l'injection de commandes du système d'exploitation et que les appels du système d'exploitation utilisent des requêtes paramétrées du système d'exploitation ou utilisent l'encodage contextuel de la sortie de la ligne de commande. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 78 |
| **5.3.9** | Vérifiez que l'application protège contre les attaques par inclusion de fichier local (LFI) ou par inclusion de fichier distant (RFI). | ✓ | ✓ | ✓ | 829 |
| **5.3.10** | Vérifiez que l'application protège contre les attaques par injection XPath ou par injection XML. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 643 |

Note : L'utilisation de requêtes paramétrées ou l'échappement du SQL n'est pas toujours suffisant ; les noms de tables et de colonnes, ORDER BY, etc. ne peuvent pas être échappés. L'inclusion de données échappées fournies par l'utilisateur dans ces champs entraîne l'échec des requêtes ou de l'injection SQL.

Note : Le format SVG autorise explicitement le script ECMA dans presque tous les contextes, de sorte qu'il peut ne pas être possible de bloquer complètement tous les vecteurs XSS SVG. Si un téléchargement SVG est nécessaire, nous recommandons fortement soit de servir ces fichiers téléchargés en tant que texte/plain, soit d'utiliser un domaine de contenu distinct fourni par l'utilisateur pour empêcher que le XSS ne prenne le relais de l'application.

## V5.4 Exigences en matière de mémoire, de chaînes de caractères et de code non géré

Les exigences suivantes ne s'appliquent que lorsque l'application utilise un langage système ou un code non géré.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.4.1** | Vérifiez que l'application utilise une chaîne de caractères à mémoire sécurisée, une copie mémoire sécurisée et l'arithmétique des pointeurs pour détecter ou empêcher les débordements de pile, de mémoire tampon ou de tas. | | ✓ | ✓ | 120 |
| **5.4.2** | Vérifiez que les chaînes de format ne prennent pas d'entrée potentiellement hostile, et sont constantes. | | ✓ | ✓ | 134 |
| **5.4.3** | Vérifiez que les techniques de validation des signes, des plages et des entrées sont utilisées pour éviter les débordements d'entiers. | | ✓ | ✓ | 190 |

## V5.5 Exigences de prévention de la désérialisation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.5.1** | Vérifiez que les objets sérialisés utilisent des contrôles d'intégrité ou sont chiffrés pour empêcher la création d'objets hostiles ou la falsification de données. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 502 |
| **5.5.2** | Vérifiez que l'application restreint correctement les analyseurs XML pour n'utiliser que la configuration la plus restrictive possible et pour s'assurer que les fonctions dangereuses telles que la résolution d'entités externes sont désactivées pour empêcher les XXE.  | ✓ | ✓ | ✓ | 611 |
| **5.5.3** | Vérifiez que la désérialisation des données non fiables est évitée ou protégée à la fois dans le code personnalisé et les bibliothèques tierces (comme les analyseurs JSON, XML et YAML).  | ✓ | ✓ | ✓ | 502 |
| **5.5.4** | Vérifiez que lors de l'analyse de JSON dans les navigateurs ou les backends basés sur JavaScript, JSON.parse est utilisé pour analyser le document JSON. N'utilisez pas eval() pour analyser JSON. | ✓ | ✓ | ✓ | 95 |

## Références

Pour plus d'informations, voir aussi :

* [OWASP Testing Guide 4.0: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Cheat Sheet: Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution.html)
* [OWASP LDAP Injection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client Side Testing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client_Side_Testing/)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [XML External Entity (XXE) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)

Pour plus d'informations sur l'évasion automatique, veuillez consulter

* [Reducing XSS by way of Automatic Context-Aware Escaping in Template Systems](https://googleonlinesecurity.blogspot.com/2009/03/reducing-xss-by-way-of-automatic.html)
* [AngularJS Strict Contextual Escaping](https://docs.angularjs.org/api/ng/service/$sce)
* [AngularJS ngBind](https://docs.angularjs.org/api/ng/directive/ngBind)
* [Angular Sanitization](https://angular.io/guide/security#sanitization-and-security-contexts)
* [Angular Security](https://angular.io/guide/security)
* [ReactJS Escaping](https://reactjs.org/docs/introducing-jsx.html#jsx-prevents-injection-attacks)
* [Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

Pour plus d'informations sur la désérialisation, veuillez consulter

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [OWASP Deserialization of Untrusted Data Guide](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)
