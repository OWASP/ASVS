# V10 Oauth et OIDC

## Objectif de contrôle

OAuth2 (appelé OAuth dans ce chapitre) est un framework standard pour l'autorisation déléguée. Par exemple, grâce à OAuth, une application cliente peut accéder aux API (ressources serveur) au nom d'un utilisateur, à condition que ce dernier l'ait autorisée.

OAuth n'est pas conçu pour l'authentification dOauth et OIDCes utilisateurs. Le framework OpenID Connect (OIDC) étend OAuth en ajoutant une couche d'identité utilisateur. OIDC prend en charge des fonctionnalités telles que la standardisation des informations utilisateur, l'authentification unique (SSO) et la gestion des sessions. OIDC étant une extension d'OAuth, les exigences OAuth décrites dans ce chapitre s'appliquent également à OIDC.

Les rôles suivants sont définis dans OAuth :

* Le client OAuth est l'application qui tente d'accéder aux ressources du serveur (par exemple, en appelant une API à l'aide du jeton d'accès émis). Il s'agit souvent d'une application côté serveur.
    * Un client confidentiel est un client capable de maintenir la confidentialité des informations d’identification qu’il utilise pour s’authentifier auprès du serveur d’autorisation.
    * Un client public n'est pas en mesure de préserver la confidentialité des informations d'identification nécessaires à l'authentification auprès du serveur d'autorisation. Par conséquent, au lieu de s'authentifier (par exemple, à l'aide des paramètres « client_id » et « client_secret »), il s'identifie uniquement (à l'aide du paramètre « client_id »).
* Le serveur de ressources OAuth (RS) est l’API du serveur qui expose les ressources aux clients OAuth.
* Le serveur d'autorisation OAuth (AS) est une application serveur qui émet des jetons d'accès aux clients OAuth. Ces jetons permettent aux clients OAuth d'accéder aux ressources RS, soit pour le compte d'un utilisateur final, soit pour leur propre compte. L'AS est souvent une application distincte, mais (le cas échéant) il peut être intégré à un RS approprié.
* Le propriétaire de la ressource (RO) est l'utilisateur final qui autorise les clients OAuth à obtenir en son nom un accès limité aux ressources hébergées sur le serveur de ressources. Le propriétaire de la ressource consent à cette autorisation déléguée en interagissant avec le serveur d'autorisation.

Les rôles suivants sont définis dans OIDC :

* La partie de confiance (RP) est l'application cliente qui demande l'authentification de l'utilisateur final via le fournisseur OpenID. Elle joue le rôle de client OAuth.
* Le fournisseur OpenID (OP) est un AS OAuth capable d'authentifier l'utilisateur final et de fournir des revendications OIDC à un RP. L'OP peut être le fournisseur d'identité (IdP), mais dans les scénarios fédérés, l'OP et le fournisseur d'identité (où l'utilisateur final s'authentifie) peuvent être des applications serveur différentes.

OAuth et OIDC ont été initialement conçus pour les applications tierces. Aujourd'hui, ils sont également souvent utilisés par les applications propriétaires. Cependant, lorsqu'ils sont utilisés dans des scénarios propriétaires, comme l'authentification et la gestion de session, le protocole ajoute une certaine complexité, ce qui peut engendrer de nouveaux défis de sécurité.

OAuth et OIDC peuvent être utilisés pour de nombreux types d'applications, mais l'accent d'ASVS et les exigences de ce chapitre portent sur les applications Web et les API.

Étant donné que OAuth et OIDC peuvent être considérés comme une logique au-dessus des technologies Web, les exigences générales des autres chapitres s'appliquent toujours et ce chapitre ne peut pas être sorti de son contexte.

Ce chapitre présente les meilleures pratiques actuelles pour OAuth2 et OIDC, conformément aux spécifications disponibles sur <https://oauth.net/2/> et <https://openid.net/developers/specs/>. Même si les RFC sont considérées comme matures, elles sont fréquemment mises à jour. Il est donc important de se conformer aux dernières versions lors de l'application des exigences de ce chapitre. Consultez la section Références pour plus de détails.

Compte tenu de la complexité du domaine, il est essentiel qu’une solution OAuth ou OIDC sécurisée utilise des serveurs d’autorisation standard bien connus du secteur et applique la configuration de sécurité recommandée.

La terminologie utilisée dans ce chapitre est conforme aux RFC OAuth et aux spécifications OIDC ; mais notez que la terminologie OIDC n'est utilisée que pour les exigences spécifiques à OIDC, sinon, la terminologie OAuth est utilisée.

Dans le contexte d'OAuth et d'OIDC, le terme « jeton » dans ce chapitre fait référence à :

* Les jetons d'accès, qui ne peuvent être consommés que par le serveur de sécurité (RS) et qui peuvent être des jetons de référence validés par introspection ou des jetons autonomes validés à l'aide d'un matériau clé.
* jetons de rafraîchissement, qui ne seront consommés que par le serveur d'autorisation qui a émis le jeton.
* jetons d'identification OIDC, qui ne doivent être consommés que par le client qui a déclenché le flux d'autorisation.

Les niveaux de risque pour certaines exigences de ce chapitre varient selon que le client est confidentiel ou public. L'utilisation d'une authentification client forte limitant de nombreux vecteurs d'attaque, certaines exigences peuvent être assouplies lors de l'utilisation d'un client confidentiel pour les applications L1.

## V10.1 Sécurité générique OAuth et OIDC

Cette section couvre les exigences architecturales génériques qui s’appliquent à toutes les applications utilisant OAuth ou OIDC.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **10.1.1** | Vérifiez que les jetons sont envoyés uniquement aux composants qui en ont absolument besoin. Par exemple, lors de l'utilisation d'un modèle backend-for-frontend pour les applications JavaScript basées sur un navigateur, les jetons d'accès et d'actualisation ne doivent être accessibles qu'au backend. | 2 |
| **10.1.2** | Vérifiez que le client n'accepte les valeurs du serveur d'autorisation (telles que le code d'autorisation ou le jeton d'identification) que si elles résultent d'un flux d'autorisation initié par la même session d'agent utilisateur et la même transaction. Cela nécessite que les secrets générés par le client, tels que la clé de preuve pour l'échange de codes (PKCE) « code_verifier », « state » ou le nonce OIDC, ne puissent être devinés, soient spécifiques à la transaction et soient liés de manière sécurisée au client et à la session d'agent utilisateur au cours de laquelle la transaction a été initiée. | 2 |

## V10.2 Client OAuth

Ces exigences détaillent les responsabilités des applications clientes OAuth. Le client peut être, par exemple, un serveur web back-end (souvent utilisé comme back-end pour front-end, BFF), une intégration de service back-end ou une application monopage front-end (SPA, également appelée application basée sur un navigateur).

En général, les clients back-end sont considérés comme confidentiels et les clients front-end comme publics. Cependant, les applications natives exécutées sur l'appareil de l'utilisateur final peuvent être considérées comme confidentielles lorsqu'elle s'enregistrent dynamiquement des clients OAuth.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **10.2.1** | Vérifiez que, si le flux de code est utilisé, le client OAuth dispose d'une protection contre les attaques de falsification de requêtes basées sur le navigateur, communément appelées falsification de requêtes intersites (CSRF), qui déclenchent des demandes de jetons, soit en utilisant la fonctionnalité de clé de preuve pour l'échange de code (PKCE), soit en vérifiant le paramètre « state » envoyé dans la demande d'autorisation. | 2 |
| **10.2.2** | Vérifiez que, si le client OAuth peut interagir avec plusieurs serveurs d'autorisation, il dispose d'une protection contre les attaques par confusion. Par exemple, il peut exiger que le serveur d'autorisation renvoie la valeur du paramètre « iss » et la valide dans la réponse d'autorisation et la réponse du jeton. | 2 |
| **10.2.3** | Vérifiez que le client OAuth demande uniquement les portées requises (ou d’autres paramètres d’autorisation) dans les requêtes adressées au serveur d’autorisation. | 3 |

## V10.3 Serveur de ressources OAuth

Dans le contexte d'ASVS et de ce chapitre, le serveur de ressources est une API. Pour fournir un accès sécurisé, le serveur de ressources doit :

* Valider le jeton d'accès, conformément au format du jeton et aux spécifications du protocole, par exemple, validation JWT ou introspection du jeton OAuth.
* S'il est valide, appliquer les décisions d'autorisation en fonction des informations du jeton d'accès et des autorisations accordées. Par exemple, le serveur de ressources doit vérifier que le client (agissant au nom du RO) est autorisé à accéder à la ressource demandée.

Par conséquent, les exigences répertoriées ici sont spécifiques à OAuth ou OIDC et doivent être exécutées après la validation du jeton et avant d'effectuer l'autorisation basée sur les informations du jeton.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **10.3.1** | Vérifiez que le serveur de ressources accepte uniquement les jetons d'accès destinés à être utilisés avec ce service (audience). L'audience peut être incluse dans un jeton d'accès structuré (comme la revendication « aud » dans JWT) ou vérifiée à l'aide du point de terminaison d'introspection de jeton. | 2 |
| **10.3.2** | Vérifiez que le serveur de ressources applique les décisions d'autorisation en fonction des revendications du jeton d'accès définissant l'autorisation déléguée. Si des revendications telles que « sub », « scope » et « authorization_details » sont présentes, elles doivent être prises en compte dans la décision. | 2 |
| **10.3.3** | Vérifiez que si une décision de contrôle d'accès nécessite l'identification d'un utilisateur unique à partir d'un jeton d'accès (JWT ou réponse d'introspection de jeton associé), le serveur de ressources identifie l'utilisateur à partir de revendications non réattribuables à d'autres utilisateurs. En général, cela implique l'utilisation d'une combinaison de revendications « iss » et « sub ». | 2 |
| **10.3.4** | Si le serveur de ressources requiert une force d'authentification, des méthodes ou une date d'expiration spécifiques, vérifiez que le jeton d'accès présenté respecte ces contraintes. Par exemple, s'il est présent, utilisez les revendications OIDC « acr », « amr » et « auth_time » respectivement. | 2 |
| **10.3.5** | Vérifiez que le serveur de ressources empêche l'utilisation de jetons d'accès volés ou la relecture de jetons d'accès (de parties non autorisées) en exigeant des jetons d'accès limités par l'expéditeur, soit Mutual TLS pour OAuth 2, soit OAuth 2 Demonstration of Proof of Possession (DPoP). | 3 |

## V10.4 Serveur d'autorisation OAuth

Ces exigences détaillent les responsabilités des serveurs d’autorisation OAuth, y compris les fournisseurs OpenID.

Pour l'authentification client, la méthode « self_signed_tls_client_auth » est autorisée avec les prérequis requis par la [section 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) de la [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705).

| # | Description | Niveau |
| :---: | :--- | :---: |
| **10.4.1** | Vérifiez que le serveur d'autorisation valide les URI de redirection en fonction d'une liste d'autorisation spécifique au client d'URI préenregistrés à l'aide d'une comparaison de chaînes exacte. | 1 |
| **10.4.2** | Vérifiez que, si le serveur d'autorisation renvoie le code d'autorisation dans la réponse, celui-ci ne peut être utilisé qu'une seule fois pour une demande de jeton. Pour la deuxième demande valide avec un code d'autorisation déjà utilisé pour émettre un jeton d'accès, le serveur d'autorisation doit rejeter la demande de jeton et révoquer tous les jetons émis liés au code d'autorisation. | 1 |
| **10.4.3** | Vérifiez que le code d'autorisation est de courte durée. La durée de vie maximale peut atteindre 10 minutes pour les applications L1 et L2 et 1 minute pour les applications L3. | 1 |
| **10.4.4** | Vérifiez que, pour un client donné, le serveur d'autorisation autorise uniquement l'utilisation des autorisations nécessaires à ce client. Notez que les autorisations « token » (flux implicite) et « password » (flux d'informations d'identification du propriétaire de la ressource) ne doivent plus être utilisées. | 1 |
| **10.4.5** | Vérifiez que le serveur d'autorisation atténue les attaques par rejeu de jetons d'actualisation pour les clients publics, de préférence en utilisant des jetons d'actualisation limités par l'expéditeur, par exemple des jetons DPoP (Demonstrating Proof of Possession) ou des jetons d'accès liés à un certificat utilisant le protocole TLS mutuel (mTLS). Pour les applications L1 et L2, la rotation des jetons d'actualisation peut être utilisée. Si cette rotation est utilisée, le serveur d'autorisation doit invalider le jeton d'actualisation après utilisation et révoquer tous les jetons d'actualisation de cette autorisation si un jeton d'actualisation déjà utilisé et invalidé est fourni. | 1 |
| **10.4.6** | Vérifiez que, si l'octroi de code est utilisé, le serveur d'autorisation atténue les attaques par interception de code en exigeant une clé de preuve pour l'échange de code (PKCE). Pour les demandes d'autorisation, le serveur d'autorisation doit exiger une valeur « code_challenge » valide et ne doit pas accepter une valeur « plain » pour « code_challenge_method ». Pour une demande de jeton, il doit exiger la validation du paramètre « code_verifier ». | 2 |
| **10.4.7** | Vérifiez que si le serveur d'autorisation prend en charge l'enregistrement dynamique des clients non authentifiés, il réduit le risque d'applications clientes malveillantes. Il doit valider les métadonnées clientes, telles que les URI enregistrés, garantir le consentement de l'utilisateur et l'avertir avant de traiter une demande d'autorisation avec une application cliente non approuvée. | 2 |
| **10.4.8** | Vérifiez que les jetons d’actualisation ont une expiration absolue, y compris si l’expiration du jeton d’actualisation glissant est appliquée. | 2 |
| **10.4.9** | Vérifiez que les jetons d'actualisation et les jetons d'accès de référence peuvent être révoqués par un utilisateur autorisé à l'aide de l'interface utilisateur du serveur d'autorisation, afin d'atténuer le risque de clients malveillants ou de jetons volés. | 2 |
| **10.4.10** | Vérifiez que le client confidentiel est authentifié pour les demandes de canal arrière client-serveur autorisé telles que les demandes de jeton, les demandes d'autorisation poussée (PAR) et les demandes de révocation de jeton. | 2 |
| **10.4.11** | Vérifiez que le client confidentiel est authentifié pour les demandes de canal arrière client-serveur autorisé telles que les demandes de jeton, les demandes d'autorisation poussée (PAR) et les demandes de révocation de jeton. | 2 |
| **10.4.12** | Vérifiez que, pour un client donné, le serveur d'autorisation autorise uniquement la valeur « response_mode » dont ce client a besoin. Par exemple, en vérifiant cette valeur par rapport aux valeurs attendues ou en utilisant une requête d'autorisation poussée (PAR) ou une requête d'autorisation sécurisée par JWT (JAR). | 3 |
| **10.4.13** | Vérifiez que le type d'Autorisation « code » est toujours utilisé avec les demandes d'autorisation poussées (PAR). | 3 |
| **10.4.14** | Vérifiez que le serveur d'autorisation émet uniquement des jetons d'accès limités à l'expéditeur (preuve de possession), soit avec des jetons d'accès liés au certificat utilisant TLS mutuel (mTLS), soit avec des jetons d'accès liés au DPoP (démonstration de preuve de possession). | 3 |
| **10.4.15** | Vérifiez que, pour un client côté serveur (non exécuté sur l'appareil de l'utilisateur final), le serveur d'autorisation garantit que la valeur du paramètre « authorization_details » provient du backend client et que l'utilisateur ne l'a pas altérée. Par exemple, en exigeant l'utilisation d'une demande d'autorisation poussée (PAR) ou d'une demande d'autorisation sécurisée par JWT (JAR). | 3 |
| **10.4.16** | Vérifiez que le client est confidentiel et que le serveur d'autorisation requiert l'utilisation de méthodes d'authentification client fortes (basées sur la cryptographie à clé publique et résistantes aux attaques par relecture), telles que TLS mutuel ('tls_client_auth', 'self_signed_tls_client_auth') ou JWT à clé privée ('private_key_jwt'). | 3 |

## V10.5 Client OIDC

Étant donné que la partie utilisatrice d'OIDC agit en tant que client OAuth, les exigences de la section « Client OAuth » s'appliquent également.

Notez que la section « Authentification avec un fournisseur d’identité » du chapitre « Authentification » contient également des exigences générales pertinentes.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **10.5.1** | Vérifiez que le client (en tant que partie utilisatrice) atténue les attaques par rejeu de jeton d'identification. Par exemple, en vous assurant que la valeur « nonce » du jeton d'identification correspond à la valeur « nonce » envoyée dans la demande d'authentification au fournisseur OpenID (appelée demande d'autorisation envoyée au serveur d'autorisation dans OAuth2). | 2 |
| **10.5.2** | Vérifiez que le client identifie de manière unique l'utilisateur à partir des revendications de jeton d'identification, généralement la revendication « sub », qui ne peut pas être réaffectée à d'autres utilisateurs (pour la portée d'un fournisseur d'identité). | 2 |
| **10.5.3** | Vérifiez que le client rejette les tentatives d'un serveur d'autorisation malveillant d'usurper l'identité d'un autre serveur d'autorisation via ses métadonnées. Le client doit rejeter les métadonnées du serveur d'autorisation si l'URL de l'émetteur figurant dans ces métadonnées ne correspond pas exactement à l'URL d'émetteur préconfigurée attendue par le client. | 2 |
| **10.5.4** | Vérifiez que le client valide que le jeton d'identification est destiné à être utilisé pour ce client (audience) en vérifiant que la revendication « aud » du jeton est égale à la valeur « client_id » pour le client. | 2 |
| **10.5.5** | Vérifiez que, lors de l'utilisation de la déconnexion du canal arrière OIDC, la partie utilisatrice atténue les risques de déni de service liés à la déconnexion forcée et à la confusion entre JWT dans le flux de déconnexion. Le client doit vérifier que le jeton de déconnexion est correctement typé avec la valeur « logout+jwt », qu'il contient la revendication « event » avec le nom de membre correct et qu'il ne contient pas de revendication « nonce ». Il est également recommandé d'utiliser une expiration courte (par exemple, 2 minutes). | 2 |

## V10.6 Fournisseur OpenID

Étant donné que les fournisseurs OpenID agissent comme des serveurs d'autorisation OAuth, les exigences de la section « Serveur d'autorisation OAuth » s'appliquent également.

Notez que si vous utilisez le flux de jeton d'identification (et non le flux de code), aucun jeton d'accès n'est émis et de nombreuses exigences pour OAuth AS ne sont pas applicables.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **10.6.1** | Vérifiez que le fournisseur OpenID n'autorise que les valeurs « code », « ciba », « id_token » ou « id_token code » pour le mode de réponse. Notez que « code » est préférable à « id_token code » (flux hybride OIDC) et que « token » (tout flux implicite) ne doit pas être utilisé. | 2 |
| **10.6.2** | Vérifiez que le fournisseur OpenID atténue les risques de déni de service liés à la déconnexion forcée. Pour ce faire, obtenez une confirmation explicite de l'utilisateur final ou, le cas échéant, validez les paramètres de la requête de déconnexion (initiée par la partie utilisatrice), comme « id_token_hint ». | 2 |

## V10.7 Gestion du consentement

Ces exigences couvrent la vérification du consentement de l'utilisateur par le serveur d'autorisation. Sans vérification appropriée du consentement de l'utilisateur, un acteur malveillant peut obtenir des autorisations au nom de l'utilisateur par usurpation d'identité ou ingénierie sociale.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **10.7.1** | Vérifiez que le serveur d'autorisation garantit le consentement de l'utilisateur à chaque demande d'autorisation. Si l'identité du client ne peut être garantie, le serveur d'autorisation doit toujours demander explicitement le consentement de l'utilisateur. | 2 |
| **10.7.2** | Vérifiez que lorsque le serveur d'autorisation demande le consentement de l'utilisateur, il fournit des informations claires et suffisantes sur ce qui est consenti. Le cas échéant, ces informations doivent inclure la nature des autorisations demandées (généralement en fonction de la portée, du serveur de ressources et des détails d'autorisation RAR), l'identité de l'application autorisée et la durée de vie de ces autorisations. | 2 |
| **10.7.3** | Vérifiez que l’utilisateur peut consulter, modifier et révoquer les consentements qu’il a accordés via le serveur d’autorisation. | 2 |

## Références

Pour plus d'informations, voir également :

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

Pour les exigences liées à OAuth dans ASVS, les RFC publiées et à l'état de projet suivantes sont utilisées :

* [RFC6749 The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
* [RFC6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)
* [RFC6819 OAuth 2.0 Threat Model and Security Considerations](https://datatracker.ietf.org/doc/html/rfc6819)
* [RFC7636 Proof Key for Code Exchange by OAuth Public Clients](https://datatracker.ietf.org/doc/html/rfc7636)
* [RFC7591 OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591)
* [RFC8628 OAuth 2.0 Device Authorization Grant](https://datatracker.ietf.org/doc/html/rfc8628)
* [RFC8707 Resource Indicators for OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc8707)
* [RFC9068 JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
* [RFC9126 OAuth 2.0 Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126)
* [RFC9207 OAuth 2.0 Authorization Server Issuer Identification](https://datatracker.ietf.org/doc/html/rfc9207)
* [RFC9396 OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)
* [RFC9449 OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)
* [RFC9700 Best Current Practice for OAuth 2.0 Security](https://datatracker.ietf.org/doc/html/rfc9700)
* [draft OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)<!-- recheck on release -->
* [draft The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12)<!-- recheck on release -->

Pour plus d'informations sur OpenID Connect, veuillez consulter :

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
