# V3 Sécurité du frontend Web

## Objectif de contrôle

Cette catégorie se concentre sur les exigences visant à protéger contre les attaques exécutées via un frontend web. Ces exigences ne s'appliquent pas aux solutions "machine-to-machine".

## V3.1 Documentation sur la sécurité du frontend Web

Cette section décrit les fonctionnalités de sécurité du navigateur qui doivent être spécifiées dans la documentation de l'application.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **3.1.1** | Vérifiez que la documentation de l'application indique les fonctionnalités de sécurité attendues que les navigateurs utilisant l'application doivent prendre en charge (telles que HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP) et autres mécanismes de sécurité HTTP pertinents). Elle doit également définir le comportement de l'application lorsque certaines de ces fonctionnalités ne sont pas disponibles (par exemple, avertir l'utilisateur ou bloquer l'accès). | 3 |

## V3.2 Interprétation non intentionnelle du contenu

Le rendu de contenu ou de fonctionnalité dans un contexte incorrect peut entraîner l'exécution ou l'affichage de contenu malveillant.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **3.2.1** | Vérifiez que des contrôles de sécurité sont en place pour empêcher les navigateurs d'afficher du contenu ou des fonctionnalités dans les réponses HTTP dans un contexte incorrect (par exemple, lorsqu'une API, un fichier téléchargé par l'utilisateur ou une autre ressource est demandée directement). Les contrôles possibles peuvent inclure : ne pas transmettre le contenu sauf si les champs d'en-tête de requête HTTP (tels que Sec-Fetch-\*) indiquent qu'il s'agit du contexte correct, utiliser la directive sandbox du champ d'en-tête Content-Security-Policy ou utiliser le type de disposition de pièce jointe dans le champ d'en-tête Content-Disposition. | 1 |
| **3.2.2** | Vérifiez que le contenu destiné à être affiché sous forme de texte, plutôt que rendu sous forme de HTML, est géré à l'aide de fonctions de rendu sécurisées (telles que createTextNode ou textContent) pour empêcher l'exécution involontaire de contenu tel que HTML ou JavaScript. | 1 |
| **3.2.3** | Vérifiez que l'application évite l'écrasement du DOM lors de l'utilisation de JavaScript côté client en utilisant des déclarations de variables explicites, en effectuant une vérification de type stricte, en évitant de stocker des variables globales sur l'objet document et en implémentant l'isolation de l'espace de nommage. | 3 |

## V3.3 Configuration des cookies

Cette section décrit les exigences de configuration sécurisée des cookies sensibles afin de fournir un niveau d'assurance plus élevé qu'ils ont été créés par l'application elle-même et d'empêcher que leur contenu ne fuite ou ne soit modifié de manière inappropriée.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **3.3.1** | Vérifiez que les cookies ont l'attribut « Secure » ​​défini et si le préfixe « \__Host- » n'est pas utilisé pour le nom du cookie, le préfixe « __Secure- » doit être utilisé pour le nom du cookie. | 1 |
| **3.3.2** | Vérifiez que la valeur de l'attribut « SameSite » de chaque cookie est définie en fonction de l'objectif du cookie, afin de limiter l'exposition aux attaques de réparation de l'interface utilisateur et aux attaques de falsification de requêtes basées sur le navigateur, communément appelées falsification de requêtes intersites (CSRF). | 2 |
| **3.3.3** | Vérifiez que les cookies ont le préfixe « __Host- » pour le nom du cookie, sauf s'ils sont explicitement conçus pour être partagés avec d'autres hôtes. | 2 |
| **3.3.4** | Vérifiez que si la valeur d'un cookie n'est pas censée être accessible aux scripts côté client (comme un jeton de session), le cookie doit avoir l'attribut « HttpOnly » défini et la même valeur (par exemple, un jeton de session) ne doit être transférée au client que via le champ d'en-tête « Set-Cookie ». | 2 |
| **3.3.5** | Vérifiez que lorsque l'application écrit un cookie, la longueur combinée du nom et de la valeur du cookie ne dépasse pas 4 096 octets. Les cookies trop volumineux ne seront pas stockés par le navigateur et ne seront donc pas envoyés avec les requêtes, empêchant ainsi l'utilisateur d'utiliser les fonctionnalités de l'application qui reposent sur ce cookie. | 3 |

## V3.4 En-têtes du mécanisme de sécurité du navigateur

Cette section décrit les en-têtes de sécurité qui doivent être définis sur les réponses HTTP pour activer les fonctionnalités et restrictions de sécurité du navigateur lors du traitement des réponses de l'application.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **3.4.1** | Vérifiez qu'un champ d'en-tête Strict-Transport-Security est inclus dans toutes les réponses afin d'appliquer une politique HTTP Strict Transport Security (HSTS). Une durée maximale d'au moins un an doit être définie, et pour les niveaux L2 et supérieurs, la politique doit également s'appliquer à tous les sous-domaines. | 1 |
| **3.4.2** | Vérifiez que le champ d'en-tête Access-Control-Allow-Origin du partage de ressources cross-origine (CORS) est une valeur fixe de l'application ou, si la valeur du champ d'en-tête de requête HTTP Origin est utilisée, qu'elle est validée par rapport à une liste d'origines approuvées. Si « Access-Control-Allow-Origin: * » doit être utilisé, vérifiez que la réponse ne contient aucune information sensible. | 1 |
| **3.4.3** | Vérifiez que les réponses HTTP incluent un champ d'en-tête de réponse Content-Security-Policy qui définit des directives garantissant que le navigateur charge et exécute uniquement du contenu ou des ressources fiables, afin de limiter l'exécution de JavaScript malveillant. Au minimum, une politique globale doit être utilisée, incluant les directives object-src 'none' et base-uri 'none', et définissant soit une lliste d’autorisations, soit des valeurs nonces ou des hachages. Pour une application L3, une politique par réponse avec des valeurs nonces ou des hachages doit être définie. | 2 |
| **3.4.4** | Vérifiez que toutes les réponses HTTP contiennent un champ d'en-tête « X-Content-Type-Options: nosniff ». Cela indique aux navigateurs de ne pas utiliser l'analyse de contenu ni la détection du type MIME pour la réponse donnée, et d'exiger que la valeur du champ d'en-tête « Content-Type » de la réponse corresponde à la ressource de destination. Par exemple, la réponse à une demande de style n'est acceptée que si le type de contenu de la réponse est « text/css ». Cela permet également au navigateur d'utiliser la fonctionnalité de blocage de lecture inter-origines (CORB). | 2 |
| **3.4.5** | Vérifiez que l'application définit une politique de référencement afin d'empêcher la fuite de données techniquement sensibles vers des services tiers via le champ d'en-tête de requête HTTP « Referer ». Cela peut être effectué via le champ d'en-tête de réponse HTTP « Referrer-Policy » ou via les attributs d'élément HTML. Les données sensibles peuvent inclure le chemin d'accès et les données de requête dans l'URL, et pour les applications internes non publiques, le nom d'hôte. | 2 |
| **3.4.6** | Vérifiez que l'application Web utilise la directive frame-ancestors du champ d'en-tête Content-Security-Policy pour chaque réponse HTTP afin de garantir qu'elle ne peut pas être intégrée par défaut et que l'intégration de ressources spécifiques n'est autorisée qu'en cas de nécessité. Notez que le champ d'en-tête X-Frame-Options, bien que pris en charge par les navigateurs, est obsolète et n'est pas forcément fiable. | 2 |
| **3.4.7** | Vérifiez que le champ d’en-tête Content-Security-Policy spécifie un emplacement pour signaler les violations. | 3 |
| **3.4.8** | Vérifiez que toutes les réponses HTTP qui lancent le rendu d'un document (comme les réponses de type text/html) incluent le champ d'en-tête 'Cross-Origin-Opener-Policy' avec la directive 'same-origin' ou s'ame-origin-allow-popups', selon les besoins. Cela empêche les attaques abusant de l'accès partagé aux objets Window, telles que le tabnabbing et le comptage d'images. | 3 |

## V3.5 Séparation de l'origine du navigateur

Lorsqu'elle accepte une demande d'accès à une fonctionnalité sensible du côté du serveur, l'application doit s'assurer que la demande est initiée par l'application elle-même ou par un tiers de confiance et qu'elle n'a pas été falsifiée par un attaquant.

Les fonctionnalités sensibles dans ce contexte peuvent inclure l'acceptation de soumission de formulaires pour des utilisateurs authentifiés et non authentifiés (comme une demande d'authentification), des opérations de changement d'état ou des fonctionnalités exigeantes en ressources (comme l'exportation de données).

Les principales protections sont les politiques de sécurité du navigateur, comme la politique de même origine pour JavaScript et la logique SameSite pour les cookies. Le mécanisme de requête de pré-vérification cross-origin CORS est une autre protection courante. Ce mécanisme est essentiel pour les "endpoints" conçus pour être appelés depuis une origine différente, mais il peut également constituer un mécanisme utile de prévention contre la falsification de requêtes pour les "endpoints" qui ne sont pas conçus pour être appelés depuis une origine différente.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **3.5.1** | Vérifiez que, si l'application ne s'appuie pas sur le mécanisme de requête de pré-vérification cross-origin CORS pour empêcher les requêtes inter-origines non autorisées d'utiliser des fonctionnalités sensibles, ces requêtes sont validées afin de garantir leur origine. Cela peut se faire en utilisant et en validant des jetons anti-falsification ou en exigeant des champs d'en-tête HTTP supplémentaires qui ne sont pas des champs d'en-tête de requête CORS safelist. Ceci permet de se protéger contre les attaques de falsification de requêtes basées sur le navigateur, communément appelées falsification de requêtes intersites (CSRF). | 1 |
| **3.5.2** | Vérifiez que, si l'application s'appuie sur le mécanisme de requête de pré-vérification cross-origin CORS pour empêcher l'utilisation inter-origines non autorisée de fonctionnalités sensibles, il est impossible d'appeler la fonctionnalité avec une requête qui ne déclenche pas de requête de pré-vérification cross-origin CORS. Cela peut nécessiter de vérifier les valeurs des champs d'en-tête de requête 'Origin' et 'Content-Type' ou d'utiliser un champ d'en-tête supplémentaire qui n'est pas un champ d'en-tête de la liste de sécurité CORS. | 1 |
| **3.5.3** | Vérifiez que les requêtes HTTP destinées aux fonctionnalités sensibles utilisent des méthodes HTTP appropriées, telles que POST, PUT, PATCH ou DELETE, et non des méthodes définies comme « sûres » par la spécification HTTP, telles que HEAD, OPTIONS ou GET. Une validation stricte des champs d'en-tête de requête Sec-Fetch-* peut également être utilisée pour garantir que la requête ne provient pas d'un appel inter-origines inapproprié, d'une requête de navigation ou d'un chargement de ressources (comme une source d'image) inattendu. | 1 |
| **3.5.4** | Vérifiez que des applications distinctes sont hébergées sur des noms d'hôte différents pour tirer parti des restrictions fournies par la politique de même origine, y compris la manière dont les documents ou scripts chargés par une origine peuvent interagir avec les ressources d'une autre origine et les restrictions basées sur le nom d'hôte sur les cookies. | 2 |
| **3.5.5** | Vérifiez que les messages reçus par l'interface postMessage sont rejetés si l'origine du message n'est pas digne de confiance ou si la syntaxe du message n'est pas valide. | 2 |
| **3.5.6** | Vérifiez que la fonctionnalité JSONP n'est activée nulle part dans l'application pour éviter les attaques Cross-Site Script Inclusion (XSSI). | 3 |
| **3.5.7** | Vérifiez que les données nécessitant une autorisation ne sont pas incluses dans les réponses des ressources de script, comme les fichiers JavaScript, pour empêcher les attaques par inclusion de script intersite (XSSI). | 3 |
| **3.5.8** | Vérifiez que les ressources authentifiées (telles que les images, les vidéos, les scripts et autres documents) peuvent être chargées ou intégrées pour le compte de l'utilisateur uniquement lorsque cela est prévu. Cela peut être réalisé en validant strictement les champs d'en-tête de requête HTTP Sec-Fetch-* afin de garantir que la requête ne provient pas d'un appel cross-origin inapproprié, ou en définissant un champ d'en-tête de réponse HTTP Cross-Origin-Resource-Policy restrictif pour indiquer au navigateur de bloquer le contenu renvoyé. | 3 |

## V3.6 Intégrité des ressources externes

Cette section fournit des conseils pour l’hébergement sécurisé de contenu sur des sites tiers.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **3.6.1** | Vérifiez que les ressources côté client, telles que les bibliothèques JavaScript, les feuilles de style CSS ou les polices web, sont hébergées en externe (par exemple, sur un réseau de diffusion de contenu) uniquement si la ressource est statique et versionnée, et si l'intégrité des sous-ressources (SRI) est utilisée pour valider l'intégrité de la ressource. Si cela n'est pas possible, une décision de sécurité documentée doit justifier cette décision pour chaque ressource. | 3 |

## V3.7 Autres considérations sur la sécurité du navigateur

Cette section comprend divers autres contrôles de sécurité et fonctionnalités de sécurité de navigateur modernes nécessaires pour la sécurité du navigateur côté client.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **3.7.1** | Vérifiez que l'application utilise uniquement des technologies côté client toujours prises en charge et considérées comme sécurisées. Parmi les technologies qui ne répondent pas à cette exigence figurent les plugins NSAPI, Flash, Shockwave, ActiveX, Silverlight, NACL ou les applets Java côté client. | 2 |
| **3.7.2** | Vérifiez que l'application redirigera automatiquement l'utilisateur vers un nom d'hôte ou un domaine différent (qui n'est pas contrôlé par l'application) uniquement lorsque la destination apparaît sur une liste d'autorisation. | 2 |
| **3.7.3** | Vérifiez que le domaine de premier niveau de l'application (par exemple, site.tld) ​​est ajouté à la liste de préchargement publique pour HTTP Strict Transport Security (HSTS). Cela garantit que l'utilisation de TLS pour l'application est intégrée directement dans les principaux navigateurs, plutôt que de dépendre uniquement du champ d'en-tête de réponse Strict-Transport-Security. | 3 |
| **3.7.4** | Vérifiez que l'application affiche une notification lorsque l'utilisateur est redirigé vers une URL hors du contrôle de l'application, avec une option pour annuler la navigation. | 3 |
| **3.7.5** | Vérifiez que l'application se comporte comme documenté (par exemple, en avertissant l'utilisateur ou en bloquant l'accès) si le navigateur utilisé pour accéder à l'application ne prend pas en charge les fonctionnalités de sécurité attendues. | 3 |

## Références

Pour plus d'informations, voir également :

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
* [OWASP DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)
