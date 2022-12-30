# V6 Exigences de vérification de la cryptographie stockée

## Objectif de contrôle

Assurez-vous qu'une application vérifiée satisfait aux exigences de haut niveau suivantes :

* Tous les modules cryptographiques échouent de manière sécurisée et que les erreurs sont traitées correctement.
* Un générateur de nombres aléatoires approprié est utilisé.
* L'accès aux clés est géré de manière sécurisée.

## V6.1 Classification des données

L'actif le plus important est constitué par les données traitées, stockées ou transmises par une application. Il faut toujours procéder à une évaluation de l'impact sur la vie privée afin de classer correctement les besoins en matière de protection des données de toute donnée stockée.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.1.1** | Vérifier que les données privées réglementées sont stockées sous forme chiffrée pendant le repos, comme les informations d'identification personnelle (IIP), les informations personnelles sensibles ou les données considérées comme susceptibles d'être soumises à la GDPR de l'UE. | | ✓ | ✓ | 311 |
| **6.1.2** | Vérifier que les données de santé réglementées sont stockées de manière chiffrée pendant le repos, comme les dossiers médicaux, les détails des dispositifs médicaux ou les dossiers de recherche désanonymisés. | | ✓ | ✓ | 311 |
| **6.1.3** | Vérifiez que les données financières réglementées sont stockées de manière chiffrée lorsqu'elles sont au repos, telles que les comptes financiers, les défauts ou les antécédents de crédit, les dossiers fiscaux, l'historique des salaires, les bénéficiaires ou les dossiers de marché ou de recherche désanonymisés. | | ✓ | ✓ | 311 |

## V6.2 Algorithmes

Les récents progrès de la cryptographie signifient que des algorithmes et des longueurs de clé auparavant sûrs ne sont plus sûrs ou suffisants pour protéger les données. Il devrait donc être possible de modifier les algorithmes.

Bien que cette section ne soit pas facilement testée lors des tests d'intrusions, les développeurs devraient considérer toute cette section comme obligatoire même si la L1 est absente de la plupart des éléments.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.2.1** | Vérifiez que tous les modules cryptographiques échouent en toute sécurité, et que les erreurs sont traitées de manière à ne pas permettre les attaques de type "Padding Oracle". | ✓ | ✓ | ✓ | 310 |
| **6.2.2** | Vérifiez que des algorithmes, des bibliothèques cryptographiques et des modes éprouvés par l'industrie ou approuvés par le gouvernement sont utilisés, au lieu de la cryptographie codée sur mesure. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 327 |
| **6.2.3** | Vérifiez que le vecteur d'initialisation du chiffrement, la configuration du chiffrement et les modes de blocage sont configurés de manière sécurisée en utilisant les derniers conseils. | | ✓ | ✓ | 326 |
| **6.2.4** | Vérifiez que les algorithmes de chiffrement ou de hachage, les longueurs de clé, le nombre de rondes, les chiffrements ou les modes, peuvent être reconfigurés, mis à niveau ou échangés à tout moment, pour se protéger contre les failles cryptographiques. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 326 |
| **6.2.5** | Vérifiez que les modes de blocs non sécurisés connus (c'est-à-dire ECB, etc.), les modes de remplissage (c'est-à-dire PKCS#1 v1.5, etc.), les chiffrements avec des blocs de petites tailles (c'est-à-dire Triple-DES, Blowfish, etc.) et les algorithmes de hachage faibles (c'est-à-dire MD5, SHA1, etc.) ne sont pas utilisés, sauf si cela est nécessaire pour la rétrocompatibilité. | | ✓ | ✓ | 326 |
| **6.2.6** | Vérifiez que les nonces, vecteurs d'initialisation et autres numéros à usage unique ne doivent pas être utilisés plus d'une fois avec une clé de chiffrement donnée. La méthode de génération doit être appropriée à l'algorithme utilisé. | | ✓ | ✓ | 326 |
| **6.2.7** | Vérifier que les données chiffrées sont authentifiées par des signatures, des modes de chiffrement authentifiés ou le [HMAC](https://en.wikipedia.org/wiki/HMAC) pour s'assurer que le texte chiffré n'est pas altéré par une partie non autorisée. | | | ✓ | 326 |
| **6.2.8** | Vérifiez que toutes les opérations cryptographiques sont à temps constant, sans opérations de "court-circuit" dans les comparaisons, les calculs ou les retours, afin d'éviter les fuites d'informations. | | | ✓ | 385 |

## V6.3 Valeurs aléatoires

La véritable génération de nombres pseudo-aléatoires (PRNG) est incroyablement difficile à réaliser. En général, les bonnes sources d'entropie au sein d'un système seront rapidement épuisées si elles sont trop utilisées, mais des sources moins aléatoires peuvent conduire à des clés et des secrets prévisibles.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.3.1** | Vérifiez que tous les nombres aléatoires, noms de fichiers aléatoires, GUIDs aléatoires et chaînes aléatoires sont générés en utilisant le générateur de nombres aléatoires sécurisé cryptographiquement approuvé par le module cryptographique lorsque ces valeurs aléatoires sont destinées à ne pas être devinées par un attaquant. | | ✓ | ✓ | 338 |
| **6.3.2** | Vérifiez que les GUID aléatoires sont créés en utilisant l'algorithme GUID v4, et un générateur de nombres pseudo-aléatoires sécurisé cryptographiquement (CSPRNG). Les GUID créés à l'aide d'autres générateurs de nombres pseudo-aléatoires peuvent être prévisibles. | | ✓ | ✓ | 338 |
| **6.3.3** | Vérifiez que les nombres aléatoires sont créés avec une entropie correcte même lorsque l'application est soumise à une forte charge, ou que l'application se dégrade gracieusement dans de telles circonstances. | | | ✓ | 338 |

## V6.4 Gestion du secret

Bien que cette section ne soit pas facilement testée, les développeurs devraient considérer toute cette section comme obligatoire même si la L1 est absente de la plupart des éléments.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.4.1** | Vérifiez qu'une solution de gestion des secrets, telle qu'un coffre fort de clés, est utilisé pour créer, stocker, contrôler l'accès aux secrets et les détruire en toute sécurité. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 798 |
| **6.4.2** | Vérifiez que le matériel clé ne soit pas exposé à l'application mais utilise plutôt un module de sécurité isolé comme un coffre-fort pour les opérations cryptographiques. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 320 |

## Références

Pour plus d'informations, voir aussi :

* [OWASP Testing Guide 4.0: Testing for weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/README.html)
* [OWASP Cheat Sheet: Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-2](https://csrc.nist.gov/publications/detail/fips/140/2/final)
