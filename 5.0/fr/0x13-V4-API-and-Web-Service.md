# V4 API et service Web

## Objectif de contrôle

Plusieurs considérations s'appliquent spécifiquement aux applications exposant des API destinées aux navigateurs web ou à d'autres consommateurs (généralement via JSON, XML ou GraphQL). Ce chapitre présente les configurations et mécanismes de sécurité pertinents à appliquer.

Notez que les problèmes d’authentification, de gestion de session et de validation des entrées des autres chapitres s’appliquent également aux API. Ce chapitre ne peut donc pas être sorti de son contexte ni testé de manière isolée.

## V4.1 Sécurité du service Web générique

Cette section aborde les considérations générales sur la sécurité des services Web et, par conséquent, les pratiques d’hygiène de base des services Web.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **4.1.1** | Vérifiez que chaque réponse HTTP avec un corps de message contient un champ d'en-tête Content-Type qui correspond au contenu réel de la réponse, y compris le paramètre charset pour spécifier un codage de caractères sécurisé (par exemple, UTF-8, ISO-8859-1) conformément aux types de médias IANA, tels que « text/ », « /+xml » et « /xml ». | 1 |
| **4.1.2** | Vérifiez que seuls les terminaux utilisateurs (destinés à l'accès manuel via un navigateur web) redirigent automatiquement de HTTP vers HTTPS, tandis que les autres services ou terminaux n'implémentent pas de redirections transparentes. Cela permet d'éviter qu'un client envoie par erreur des requêtes HTTP non chiffrées, mais que, comme ces requêtes sont automatiquement redirigées vers HTTPS, la fuite de données sensibles passe inaperçue. | 2 |
| **4.1.3** | Vérifiez que tout champ d'en-tête HTTP utilisé par l'application et défini par une couche intermédiaire, telle qu'un équilibreur de charge, un proxy web ou un service backend-for-frontend, ne peut pas être remplacé par l'utilisateur final. Les exemples d'en-têtes peuvent inclure X-Real-IP, X-Forwarded-*, ou X-User-ID. | 2 |
| **4.1.4** | Vérifiez que seules les méthodes HTTP explicitement prises en charge par l'application ou son API (y compris les OPTIONS lors des demandes de contrôle en amont) peuvent être utilisées et que les méthodes inutilisées sont bloquées. | 3 |
| **4.1.5** | Vérifier que les signatures numériques par message sont utilisées pour fournir une assurance supplémentaire en plus des protections de transport pour les demandes ou les transactions qui sont très sensibles ou qui traversent un certain nombre de systèmes. | 3 |

## V4.2 Validation de la structure des messages HTTP

Cette section explique comment la structure et les champs d'en-tête d'un message HTTP doivent être validés afin de prévenir les attaques telles que la contrebande de requêtes, le fractionnement de réponses, l'injection d'en-têtes et le déni de service via des messages HTTP trop longs.

Ces exigences sont pertinentes pour le traitement et la génération de messages HTTP généraux, mais sont particulièrement importantes lors de la conversion de messages HTTP entre différentes versions HTTP.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **4.2.1** | Vérifiez que tous les composants de l'application (y compris les équilibreurs de charge, les pares-feux et les serveurs d'applications) déterminent les limites des messages HTTP entrants à l'aide du mécanisme approprié à la version HTTP afin d'empêcher la contrebande de requêtes HTTP. Dans HTTP/1.x, si un champ d'en-tête Transfer-Encoding est présent, l'en-tête Content-Length doit être ignoré conformément à la RFC 2616. Avec HTTP/2 ou HTTP/3, si un champ d'en-tête Content-Length est présent, le récepteur doit s'assurer qu'il est cohérent avec la longueur des trames DATA. | 2 |
| **4.2.2** | Vérifier que, lors de la génération de messages HTTP, le champ d'en-tête Content-Length n'entre pas en conflit avec la longueur du contenu déterminée par le cadrage du protocole HTTP, afin d'empêcher les attaques de type « request smuggling ». | 3 |
| **4.2.3** | Vérifiez que l'application n'envoie ni n'accepte de messages HTTP/2 ou HTTP/3 avec des champs d'en-tête spécifiques à la connexion, tels que Transfer-Encoding, afin d'éviter les attaques par fractionnement de la réponse et par injection d'en-tête. | 3 |
| **4.2.4** | Vérifiez que l'application n'accepte que les requêtes HTTP/2 et HTTP/3 dont les champs et valeurs d'en-tête ne contiennent pas de séquences CR (\r), LF (\n) ou CRLF (\r\n), afin d'éviter les attaques par injection d'en-tête. | 3 |
| **4.2.5** | Vérifiez que, si l'application (backend ou frontend) construit et envoie des requêtes, elle utilise des mécanismes de validation, d'assainissement ou autres pour éviter de créer des URI (comme pour les appels API) ou des champs d'en-tête de requête HTTP (comme Authorization ou Cookie) qui sont trop longs pour être acceptés par le composant récepteur. Cela pourrait entraîner un déni de service, par exemple lors de l'envoi d'une requête trop longue (par exemple, un long champ d'en-tête de cookie), ce qui fait que le serveur répond toujours avec un statut d'erreur. | 3 |

## V4.3 GraphQL

GraphQL est de plus en plus utilisé pour créer des clients riches en données, peu couplés à divers services backend. Cette section aborde les considérations de sécurité pour GraphQL.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **4.3.1** | Vérifiez qu'une liste d'autorisation de requête, une limitation de profondeur, une limitation de quantité ou une analyse des coûts de requête est utilisée pour empêcher le déni de service (DoS) de GraphQL ou d'expression de la couche données en raison de requêtes imbriquées coûteuses. | 2 |
| **4.3.2** | Vérifiez que les requêtes d’introspection GraphQL sont désactivées dans l’environnement de production, sauf si l’API GraphQL est destinée à être utilisée par d’autres parties. | 2 |

## V4.4 WebSocket

WebSocket est un protocole de communication qui fournit un canal de communication bidirectionnel simultané via une seule connexion TCP. Il a été normalisé par l'IETF sous la RFC 6455 en 2011 et se distingue de HTTP, bien qu'il soit conçu pour fonctionner sur les ports HTTP 443 et 80.

Cette section fournit les principales exigences de sécurité pour empêcher les attaques liées à la sécurité des communications et à la gestion des sessions qui exploitent spécifiquement ce canal de communication en temps réel.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **4.4.1** | Vérifiez que WebSocket sur TLS (WSS) est utilisé pour toutes les connexions WebSocket. | 1 |
| **4.4.2** | Vérifiez que, lors de la négociation HTTP WebSocket initiale, le champ d’en-tête 'Origin' est vérifié par rapport à une liste d’origines autorisées pour l’application. | 2 |
| **4.4.3** | Vérifiez que, si la gestion de session standard de l'application ne peut pas être utilisée, des jetons dédiés sont utilisés à cet effet, qui sont conformes aux exigences de sécurité de gestion de session pertinentes. | 2 |
| **4.4.4** | Vérifiez que les jetons de gestion de session WebSocket dédiés sont initialement obtenus ou validés via la session HTTPS précédemment authentifiée lors de la transition d'une session HTTPS existante vers un canal WebSocket. | 2 |

## Références

Pour plus d'informations, voir également :

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* Resources on GraphQL Authorization from [graphql.org](https://graphql.org/learn/authorization/) and [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods).
* [OWASP Web Security Testing Guide: GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [OWASP Web Security Testing Guide: Testing WebSockets](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)
