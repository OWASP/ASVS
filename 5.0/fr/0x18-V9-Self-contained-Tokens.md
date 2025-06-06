# V9 Jetons autonomes

## Objectif de contrôle

Le concept de jeton autonome est mentionné dans la RFC 6749 OAuth 2.0 originale de 2012. Il désigne un jeton contenant des données ou des revendications sur lesquelles un service récepteur s'appuie pour prendre des décisions de sécurité. Il convient de le distinguer d'un simple jeton contenant uniquement un identifiant, qu'un service récepteur utilise pour rechercher des données localement. Les exemples les plus courants de jetons autonomes sont les jetons Web JSON (JWT) et les assertions SAML.

L'utilisation de jetons autonomes est devenue très répandue, même en dehors d'OAuth et d'OIDC. Parallèlement, la sécurité de ce mécanisme repose sur la capacité à valider l'intégrité du jeton et à garantir sa validité dans un contexte particulier. Ce processus présente de nombreux pièges, et ce chapitre détaille les mécanismes que les applications devraient mettre en place pour les éviter.

## V9.1 Source et intégrité du jeton

Cette section comprend des exigences visant à garantir que le jeton a été produit par une partie de confiance et n’a pas été falsifié.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **9.1.1** | Vérifiez que les jetons autonomes sont validés à l'aide de leur signature numérique ou MAC pour les protéger contre toute falsification avant d'accepter le contenu du jeton. | 1 |
| **9.1.2** | Vérifiez que seuls les algorithmes d'une liste blanche peuvent être utilisés pour créer et vérifier des jetons autonomes, dans un contexte donné. La liste blanche doit inclure les algorithmes autorisés, idéalement symétriques ou asymétriques, et ne doit pas inclure l'algorithme « Aucun ». Si les algorithmes symétriques et asymétriques doivent être pris en charge, des contrôles supplémentaires seront nécessaires pour éviter toute confusion de clés. | 1 |
| **9.1.3** | Vérifiez que les clés utilisées pour valider les jetons autonomes proviennent de sources préconfigurées et fiables pour l'émetteur du jeton, empêchant ainsi les attaquants de spécifier des sources et des clés non fiables. Pour les JWT et autres structures JWS, les en-têtes tels que « jku », « x5u » et « jwk » doivent être validés par rapport à une liste blanche de sources fiables. | 1 |

## V9.2 Contenu du jeton

Avant de prendre des décisions de sécurité basées sur le contenu d'un jeton autonome, il est nécessaire de vérifier que le jeton a été présenté pendant sa période de validité et qu'il est destiné à être utilisé par le service destinataire et pour l'usage pour lequel il a été présenté. Cela permet d'éviter toute utilisation croisée non sécurisée entre différents services ou avec différents types de jetons provenant du même émetteur.

Les exigences spécifiques pour OAuth et OIDC sont couvertes dans le chapitre dédié.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **9.2.1** | Vérifiez que, si une période de validité est indiquée dans les données du jeton, celui-ci et son contenu ne sont acceptés que si la date de vérification est comprise dans cette période. Par exemple, pour les JWT, les revendications « nbf » et « exp » doivent être vérifiées. | 1 |
| **9.2.2** | Vérifiez que le service recevant un jeton valide le type de jeton et son utilisation avant d'en accepter le contenu. Par exemple, seuls les jetons d'accès peuvent être acceptés pour les décisions d'autorisation, et seuls les jetons d'identification peuvent être utilisés pour prouver l'authentification des utilisateurs. | 2 |
| **9.2.3** | Vérifiez que le service accepte uniquement les jetons destinés à être utilisés avec ce service (audience). Pour les JWT, cela peut être réalisé en validant la revendication « aud » par rapport à une liste blanche définie dans le service. | 2 |
| **9.2.4** | Si un émetteur de jetons utilise la même clé privée pour émettre des jetons destinés à différents publics, vérifiez que les jetons émis contiennent une restriction d'audience identifiant de manière unique les publics visés. Cela empêchera la réutilisation d'un jeton avec un public non prévu. Si l'identifiant d'audience est provisionné dynamiquement, l'émetteur de jetons doit valider ces audiences afin de garantir qu'elles n'entraînent pas d'usurpation d'identité. | 2 |

## Références

Pour plus d'informations, voir également :

* [OWASP JSON Web Token Cheat Sheet for Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) (but has useful general guidance)
