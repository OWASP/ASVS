# V3 : Exigences de vérification de la gestion des sessions

## Objectif de contrôle

L'une des composantes essentielles de toute application web ou API à état est le mécanisme par lequel elle contrôle et maintient l'état pour un utilisateur ou un dispositif qui interagit avec elle. La gestion de session transforme un protocole sans état en protocole avec état, ce qui est essentiel pour différencier les différents utilisateurs ou appareils.

Assurez-vous qu'une application vérifiée satisfait aux exigences de gestion de session de haut niveau suivantes :

* Les sessions sont uniques à chaque individu et ne peuvent être devinées ou partagées.
* Les sessions sont invalidées lorsqu'elles ne sont plus nécessaires et sont interrompues pendant les périodes d'inactivité.

Comme indiqué précédemment, ces exigences ont été adaptées pour constituer un sous-ensemble conforme de contrôles NIST 800-63b sélectionnés, axés sur les menaces communes et les faiblesses d'authentification couramment exploitées. Les exigences de vérification précédentes ont été supprimées, réduites ou, dans la plupart des cas, adaptées pour être fortement alignées sur l'intention des exigences obligatoires [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html).

## Exigences de vérification de sécurité

## V3.1 Exigences fondamentales en matière de gestion des sessions

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.1.1** | Vérifiez que l'application ne révèle jamais les jetons de session dans les paramètres d'URL ou les messages d'erreur.  | ✓ | ✓ | ✓ | 598 | |

## V3.2 Exigences contraignantes de la session

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.2.1** | Vérifiez que l'application génère un nouveau jeton de session sur l'authentification de l'utilisateur. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 384 | 7.1 |
| **3.2.2** | Vérifiez que les jetons de session possèdent au moins 64 bits d'entropie. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 331 | 7.1 |
| **3.2.3** | Vérifiez que l'application ne stocke que des jetons de session dans le navigateur en utilisant des méthodes sûres telles que les cookies correctement sécurisés (voir section 3.4) ou le stockage de session HTML 5. | ✓ | ✓ | ✓ | 539 | 7.1 |
| **3.2.4** | Vérifiez que les jetons de session sont générés à l'aide d'algorithmes cryptographiques approuvés. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 331 | 7.1 |

Le TLS ou un autre canal de transport sécurisé est obligatoire pour la gestion des sessions. Cette question est traitée dans le chapitre sur la sécurité des communications.

## V3.3 Exigences en matière de déconnexion et de temporisation des sessions

Les durées de session ont été alignées sur la norme NIST 800-63, qui autorise des durées de session beaucoup plus longues que celles traditionnellement autorisées par les normes de sécurité. Les organisations doivent examiner le tableau ci-dessous, et si un délai plus long est souhaitable en fonction du risque de l'application, la valeur NIST doit être la limite supérieure des délais d'inactivité de la session.

Dans ce contexte, la valeur L1 est IAL1/AAL1, la valeur L2 est IAL2/AAL3, la valeur L3 est IAL3/AAL3. Pour IAL2/AAL2 et IAL3/AAL3, le délai d'inactivité le plus court est la limite inférieure des délais d'inactivité pour être déconnecté ou ré-authentifié pour reprendre la session.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.3.1** | Vérifiez que la déconnexion et l'expiration invalident le jeton de session. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 613 | 7.1 |
| **3.3.2** | Si les authentificateurs permettent aux utilisateurs de rester connectés, vérifiez que la ré-authentification a lieu périodiquement, que ce soit en cas d'utilisation active ou après une période d'inactivité. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | 30 jours | 12 heures ou 30 minutes d'inactivité, 2FA facultatif | 12 heures ou 15 minutes d'inactivité, avec 2FA | 613 | 7.2 |
| **3.3.3** | Vérifiez que l'application offre la possibilité de mettre fin à toutes les autres sessions actives après un changement de mot de passe réussi (y compris le changement par réinitialisation/récupération du mot de passe), et que cette option est effective dans toute l'application, la connexion fédérée (si elle existe) et toute partie qui se fie à elle. | | ✓ | ✓ | 613 | |
| **3.3.4** | Vérifiez que les utilisateurs sont en mesure de consulter et (après avoir saisi à nouveau leurs identifiants de connexion) de se déconnecter d'une ou de toutes les sessions et de tous les dispositifs actuellement actifs. | | ✓ | ✓ | 613 | 7.1 |

## V3.4 Gestion de session basée sur les cookies

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.4.1** | Vérifiez que les jetons de session basés sur des cookies ont l'attribut "Secure". ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 614 | 7.1.1 |
| **3.4.2** | Vérifiez que les jetons de session basés sur des cookies ont l'attribut "HttpOnly". ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1004 | 7.1.1 |
| **3.4.3** | Vérifiez que les jetons de session basés sur des cookies utilisent l'attribut "SameSite" pour limiter l'exposition aux attaques de contrefaçon par requête intersite. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.4** | Vérifiez que les jetons de session basés sur les cookies utilisent le préfixe "__Host" (voir références) pour assurer la confidentialité des cookies de session. | ✓ | ✓ | ✓ | 16 | 7.1.1 |
| **3.4.5** | Vérifiez que si la demande est publiée sous un nom de domaine avec d'autres applications qui définissent ou utilisent des cookies de session susceptibles de les remplacer ou de les divulguer, définissez l'attribut de chemin dans les jetons de session basés sur les cookies en utilisant le chemin le plus précis possible. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 16 | 7.1.1 |

## V3.5 Gestion de session à jetons

La gestion des sessions basée sur des jetons comprend les clés JWT, OAuth, SAML et API. Parmi celles-ci, les clés API sont connues pour être faibles et ne doivent pas être utilisées dans un nouveau code.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.5.1** | Vérifiez que l'application ne valide pas les jetons OAuth et refresh -- par eux-même -- comme la présence de l'abonné et permet aux utilisateurs de mettre fin aux relations de confiance avec les applications liées.  | | ✓ | ✓ | 290 | 7.1.2 |
| **3.5.2** | Vérifiez que l'application utilise des jetons de session plutôt que des secrets et des clés d'API statiques, sauf dans le cas d'anciennes implémentations(legacy). | | ✓ | ✓ | 798 | |
| **3.5.3** | Vérifiez que les jetons de session sans état utilisent les signatures numériques, le cryptage et d'autres contre-mesures pour se protéger contre les attaques par altération, mise sous enveloppe, rediffusion, chiffrement nul et substitution de clé. | | ✓ | ✓ | 345 | |

## V3.6 Re-authentification d'une fédération ou d'une assertion

Cette section concerne les personnes qui écrivent le code de la partie de relais (RP) ou du fournisseur de services d'accréditation (CSP). Si vous comptez sur un code mettant en œuvre ces caractéristiques, assurez-vous que ces questions sont traitées correctement.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.6.1** | Vérifier que les parties qui se fient à la procédure précisent le délai maximal d'authentification aux fournisseurs de services d'authentification (CSP) et que ces derniers ré-authentifient l'abonné s'ils n'ont pas utilisé de session pendant cette période. | | | ✓ | 613 | 7.2.1 |
| **3.6.2** | Vérifier que les fournisseurs de services d'accréditation (CSP) informent les parties ayant fait confiance au dernier événement d'authentification, afin de permettre aux RP de déterminer s'ils doivent ré-authentifier l'utilisateur. | | | ✓ | 613 | 7.2.1 |

## V3.7 Défenses contre l'exploitation de la gestion des sessions

Il existe un petit nombre d'attaques de gestion de session, dont certaines sont liées à l'expérience utilisateur (UX) des sessions. Auparavant, sur la base des exigences de la norme ISO 27002, l'ASVS exigeait le blocage de plusieurs sessions simultanées. Le blocage de sessions simultanées n'est plus approprié, non seulement parce que les utilisateurs modernes disposent de nombreux appareils ou que l'application est une API sans session de navigateur, mais aussi parce que dans la plupart de ces implémentations, le dernier authentificateur gagne, qui est souvent l'attaquant. Cette section fournit des conseils de premier plan sur la dissuasion, le retard et la détection des attaques de gestion de session à l'aide de code.

### Description de l'attaque semi-ouverte

Au début de 2018, plusieurs institutions financières ont été compromises par ce que les attaquants ont appelé des "attaques à demi ouvertes". Ce terme est resté dans l'industrie. Les attaquants ont frappé plusieurs institutions avec des bases de code propriétaires différentes, et en effet il semble que les bases de code soient différentes au sein des mêmes institutions. L'attaque semi-ouverte exploite un défaut de conception communément rencontré dans de nombreux systèmes d'authentification, de gestion de session et de contrôle d'accès existants.

Les attaquants lancent une attaque à demi-ouverte en essayant de verrouiller, de réinitialiser ou de récupérer un justificatif d'identité. Un modèle de gestion de session très répandu réutilise les objets/modèles de session de profil utilisateur entre le code non authentifié, semi-authentifié (réinitialisation du mot de passe, nom d'utilisateur oublié) et entièrement authentifié. Ce modèle remplit un objet de session ou un jeton valide contenant le profil de la victime, y compris les hachages de mots de passe et les rôles. Si les contrôles d'accès dans les contrôleurs ou les routeurs ne vérifient pas correctement que l'utilisateur est bien connecté, l'attaquant pourra agir en tant qu'utilisateur. Les attaques peuvent inclure la modification du mot de passe de l'utilisateur à une valeur connue, la mise à jour de l'adresse électronique pour effectuer une réinitialisation de mot de passe valide, la désactivation de l'authentification multifactorielle ou l'inscription d'un nouveau dispositif d'AMF, la révélation ou la modification des clés API, etc.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.7.1** | Vérifier que l'application garantit une session de connexion complète et valide ou exige une nouvelle authentification ou une vérification secondaire avant d'autoriser toute transaction sensible ou modification de compte. | ✓ | ✓ | ✓ | 306 | |

## Références

Pour plus d'informations, voir aussi :

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#Directives)
