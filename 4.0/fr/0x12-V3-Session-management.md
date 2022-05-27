# V3 Gestion des sessions

## Objectif de contrôle

L'un des principaux composants de toute application Web ou API à état est le mécanisme par lequel elle contrôle et maintient l'état d'un utilisateur ou d'un appareil qui interagit avec elle. La gestion de session transforme un protocole sans état en protocole avec état, ce qui est essentiel pour différencier les différents utilisateurs ou appareils.

Assurez-vous qu'une application vérifiée répond aux exigences de haut niveau suivantes en matière de gestion de session :

* Les sessions sont uniques pour chaque individu et ne peuvent être devinées ou partagées.
* Les sessions sont invalidées lorsqu'elles ne sont plus nécessaires et temporisées pendant les périodes d'inactivité.

Comme indiqué précédemment, ces exigences ont été adaptées pour constituer un sous-ensemble conforme de contrôles NIST 800-63b sélectionnés, axés sur les menaces communes et les faiblesses d'authentification couramment exploitées. Les exigences de vérification antérieures ont été supprimées, dédupliées ou, dans la plupart des cas, adaptées pour être fortement alignées sur l'intention des exigences obligatoires du [NIST 800-63b] (https://pages.nist.gov/800-63-3/sp800-63b.html).


## Exigences de vérification de la sécurité

## V3.1 Sécurité fondamentale de la gestion des sessions

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.1.1** | Vérifiez que l'application ne révèle jamais les jetons de session dans les paramètres URL. | ✓ | ✓ | ✓ | 598 | |

## V3.2 Liaison de session

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.2.1** | Vérifiez que l'application génère un nouveau jeton de session lors de l'authentification de l'utilisateur. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 384 | 7.1 |
| **3.2.2** | Vérifiez que les jetons de session possèdent au moins 64 bits d'entropie. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 331 | 7.1 |
| **3.2.3** | Vérifiez que l'application ne stocke les jetons de session dans le navigateur qu'à l'aide de méthodes sécurisées telles que les cookies sécurisés de manière appropriée (voir section 3.4) ou le stockage de session HTML 5. | ✓ | ✓ | ✓ | 539 | 7.1 |
| **3.2.4** | Vérifiez que les jetons de session sont générés à l'aide d'algorithmes cryptographiques approuvés. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 331 | 7.1 |

TLS ou un autre canal de transport sécurisé est obligatoire pour la gestion des sessions. Ce point est traité dans le chapitre sur la sécurité des communications.

## V3.3 Clôture de la session

Les délais d'inactivité des sessions ont été alignés sur la norme NIST 800-63, qui autorise des délais d'inactivité des sessions beaucoup plus longs que ceux traditionnellement autorisés par les normes de sécurité. Les organisations doivent examiner le tableau ci-dessous et si un délai plus long est souhaitable en fonction du risque de l'application, la valeur NIST doit être la limite supérieure des délais d'inactivité de la session.

Dans ce contexte, L1 est IAL1/AAL1, L2 est IAL2/AAL3, L3 est IAL3/AAL3. Pour IAL2/AAL2 et IAL3/AAL3, plus le délai d'inactivité est court, plus la limite inférieure des délais d'inactivité pour être déconnecté ou réauthentifié pour reprendre la session est basse.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.3.1** | Vérifiez que la déconnexion et l'expiration invalident le jeton de session, de sorte que le bouton retour ou une partie fiable en aval ne reprenne pas une session authentifiée, y compris entre parties fiables. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 613 | 7.1 |
| **3.3.2** | Si les authentificateurs permettent aux utilisateurs de rester connectés, vérifiez que la réauthentification a lieu périodiquement, à la fois lors d'une utilisation active et après une période d'inactivité. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | 30 jours | 12 heures ou 30 minutes d'inactivité, 2FA en option | 12 heures ou 15 minutes d'inactivité, avec 2FA | 613 | 7.2 |
| **3.3.3** | Vérifiez que l'application offre la possibilité de mettre fin à toutes les autres sessions actives après un changement de mot de passe réussi (y compris un changement par réinitialisation/récupération du mot de passe), et que cette option est effective pour l'application, la connexion fédérée (si elle est présente) et toutes les parties fiables. | | ✓ | ✓ | 613 | |
| **3.3.4** | Vérifiez que les utilisateurs sont en mesure d'afficher et (après avoir saisi à nouveau les informations d'identification) de se déconnecter de toutes les sessions et de tous les dispositifs actuellement actifs. | | ✓ | ✓ | 613 | 7.1 |

## V3.4 Gestion de la session basée sur les cookies

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.4.1** | Vérifiez que les jetons de session basés sur les cookies possèdent l'attribut "Secure". ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 614 | 7.1.1 |
| **3.4.2** | Vérifiez que les jetons de session basés sur les cookies ont l'attribut "HttpOnly" défini. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1004 | 7.1.1 |
| **3.4.3** | Vérifiez que les jetons de session basés sur les cookies utilisent l'attribut "SameSite" pour limiter l'exposition aux attaques par falsification de requête intersite. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.4** | Vérifiez que les jetons de session basés sur les cookies utilisent le préfixe "__Host-" afin que les cookies ne soient envoyés qu'à l'hôte qui a initialement défini le cookie. | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.5** | Vérifiez que si l'application est publiée sous un nom de domaine avec d'autres applications qui définissent ou utilisent des cookies de session susceptibles de divulguer les cookies de session, définissez l'attribut de chemin dans les jetons de session basés sur les cookies en utilisant le chemin le plus précis possible. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |

## V3.5 Gestion des sessions par jeton

La gestion de session basée sur des jetons comprend JWT, OAuth, SAML et les clés API. Parmi celles-ci, les clés API sont connues pour être faibles et ne devraient pas être utilisées dans un nouveau code.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.5.1** | Vérifiez que l'application permet aux utilisateurs de révoquer les jetons OAuth qui forment des relations de confiance avec les applications liées. | | ✓ | ✓ | 290 | 7.1.2 |
| **3.5.2** | Vérifiez que l'application utilise des jetons de session plutôt que des secrets et des clés API statiques, sauf dans le cas d'implémentations anciennes. | | ✓ | ✓ | 798 | |
| **3.5.3** | Vérifiez que les jetons de session sans état utilisent des signatures numériques, un chiffrement et d'autres contre-mesures pour se protéger contre les attaques par falsification, enveloppement, rejeu, chiffrement nul et substitution de clé. | | ✓ | ✓ | 345 | |

## V3.6 Ré-authentification fédérée

Cette section concerne ceux qui écrivent le code de la partie utilisatrice (RP) ou du fournisseur de services d'accréditation (CSP). Si vous vous appuyez sur un code mettant en œuvre ces fonctionnalités, assurez-vous que ces questions sont traitées correctement.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.6.1** | Vérifiez que les parties utilisatrices (RP) spécifient la durée maximale d'authentification aux fournisseurs de services d'authentification (CSP) et que les CSP réauthentifient l'utilisateur s'il n'a pas utilisé de session pendant cette période. | | | ✓ | 613 | 7.2.1 |
| **3.6.2** | Vérifier que les fournisseurs de services d'accréditation (CSP) informent les parties utilisatrices (RP) du dernier événement d'authentification, afin de permettre aux RP de déterminer s'ils doivent réauthentifier l'utilisateur. | | | ✓ | 613 | 7.2.1 |

## V3.7 Défenses contre les exploits de gestion de session

Il existe un petit nombre d'attaques de gestion de session, dont certaines sont liées à l'expérience utilisateur (UX) des sessions. Auparavant, sur la base des exigences de la norme ISO 27002, l'ASVS exigeait le blocage de plusieurs sessions simultanées. Le blocage des sessions simultanées n'est plus approprié, non seulement parce que les utilisateurs modernes ont de nombreux appareils ou que l'application est une API sans session de navigateur, mais aussi parce que dans la plupart de ces implémentations, le dernier authentificateur gagne, ce qui est souvent l'attaquant. Cette section fournit des conseils de premier plan pour dissuader, retarder et détecter les attaques de gestion de session à l'aide de code.

### Description de l'attaque semi-ouverte

Début 2018, plusieurs institutions financières ont été compromises en utilisant ce que les attaquants ont appelé des "attaques semi-ouvertes". Ce terme est resté dans le secteur. Les attaquants ont frappé plusieurs institutions avec différentes bases de code propriétaires, et il semble même que différentes bases de code au sein des mêmes institutions. L'attaque semi-ouverte exploite un défaut de conception commun à de nombreux systèmes d'authentification, de gestion de session et de contrôle d'accès existants.

Les attaquants lancent une attaque semi-ouverte en tentant de verrouiller, de réinitialiser ou de récupérer un justificatif d'identité. Un modèle populaire de gestion de session réutilise les objets/modèles de session du profil de l'utilisateur entre un code non authentifié, semi-authentifié (réinitialisation du mot de passe, oubli du nom d'utilisateur) et entièrement authentifié. Ce modèle de conception alimente un objet ou un jeton de session valide contenant le profil de la victime, y compris les hachages de mots de passe et les rôles. Si les contrôles d'accès des contrôleurs ou des routeurs ne vérifient pas correctement que l'utilisateur est entièrement connecté, l'attaquant pourra agir comme l'utilisateur. Les attaques peuvent consister à changer le mot de passe de l'utilisateur par une valeur connue, à mettre à jour l'adresse électronique pour effectuer une réinitialisation valide du mot de passe, à désactiver l'authentification multifactorielle ou à inscrire un nouveau dispositif MFA, à révéler ou à modifier les clés API, etc.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.7.1** | Vérifiez que l'application garantit une session de connexion complète et valide ou exige une réauthentification ou une vérification secondaire avant d'autoriser toute transaction sensible ou modification de compte. | ✓ | ✓ | ✓ | 306 | |

## Références

Pour plus d'informations, voir également :

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#Directives)
