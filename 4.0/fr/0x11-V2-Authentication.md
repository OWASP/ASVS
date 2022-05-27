# V2 Authentication

## Objectif des contrôles

L'authentification est l'action d'établir, ou de confirmer, que quelqu'un (ou quelque chose) est authentique et que les déclarations faites par une personne ou à propos d'un dispositif sont correctes, résistantes à l'usurpation d'identité et empêchent la récupération ou l'interception des mots de passe.

Lorsque l'ASVS a été publié pour la première fois, le nom d'utilisateur et le mot de passe étaient la forme d'authentification la plus courante en dehors des systèmes de haute sécurité. L'authentification multifactorielle (MFA) était communément acceptée dans les cercles de sécurité, mais rarement requise ailleurs. Avec l'augmentation du nombre de violations de mots de passe, l'idée que les noms d'utilisateur sont en quelque sorte confidentiels et les mots de passe inconnus a rendu de nombreux contrôles de sécurité intenables. Par exemple, le NIST 800-63 considère que les noms d'utilisateur et l'authentification basée sur la connaissance (KBA) sont des informations publiques, que les notifications par SMS et par e-mail sont des types d'[authentification "restreints"] (https://pages.nist.gov/800-63-FAQ/#q-b1) et que les mots de passe sont déjà divulgués. Cette réalité rend inutiles les authentificateurs basés sur la connaissance, la récupération des SMS et des e-mails, l'historique des mots de passe, leur complexité et les contrôles de rotation. Ces contrôles ont toujours été moins qu'utiles, obligeant souvent les utilisateurs à inventer des mots de passe faibles tous les quelques mois, mais avec la publication de plus de 5 milliards de violations de noms d'utilisateur et de mots de passe, il est temps de passer à autre chose.

De tous les chapitres de l'ASVS, celui sur l'authentification et la gestion des sessions est celui qui a le plus changé. L'adoption d'une pratique de pointe efficace et fondée sur des preuves sera difficile pour beaucoup, et c'est tout à fait normal. Nous devons commencer dès maintenant la transition vers un avenir post-mots de passe.

## NIST 800-63 - Norme d'authentification moderne et fondée sur des preuves

[NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) est une norme moderne, fondée sur des preuves, et représente les meilleurs conseils disponibles, indépendamment de leur applicabilité. La norme est utile pour toutes les organisations du monde entier, mais elle est particulièrement pertinente pour les agences américaines et celles qui traitent avec elles.

La terminologie NIST 800-63 peut être un peu déroutante au début, surtout si vous n'êtes habitué qu'à l'authentification par nom d'utilisateur + mot de passe. Des progrès dans l'authentification moderne sont nécessaires, nous devons donc introduire une terminologie qui deviendra monnaie courante à l'avenir, mais nous comprenons la difficulté de comprendre jusqu'à ce que l'industrie s'accorde sur ces nouveaux termes. Nous avons fourni un glossaire à la fin de ce chapitre pour vous aider. Nous avons reformulé de nombreuses exigences pour satisfaire l'intention de l'exigence, plutôt que la lettre de l'exigence. Par exemple, l'ASVS utilise le terme « mot de passe » lorsque le NIST utilise le « secret mémorisé » tout au long de cette norme.

L'authentification ASVS V2, la gestion de session V3 et, dans une moindre mesure, les contrôles d'accès V4 ont été adaptés pour constituer un sous-ensemble conforme de contrôles NIST 800-63b sélectionnés, axés sur les menaces communes et les faiblesses d'authentification couramment exploitées. Lorsque la conformité totale au NIST 800-63 est requise, veuillez consulter le NIST 800-63.

### Sélection d'un niveau NIST AAL approprié

La norme de vérification de la sécurité des applications a essayé de faire correspondre le niveau L1 de l'ASVS aux exigences de l'AAL1 du NIST, le niveau L2 à l'AAL2 et le niveau L3 à l'AAL3. Cependant, l'approche du niveau 1 de l'ASVS en tant que contrôles "essentiels" n'est pas nécessairement le niveau AAL correct pour vérifier une application ou une API. Par exemple, si l'application est une application de niveau 3 ou a des exigences réglementaires pour être AAL3, le niveau 3 devrait être choisi dans les chapitres V2 et V3 Gestion de session. Le choix du niveau d'assertion d'authentification (AAL) conforme au NIST doit être effectué selon les directives du NIST 800-63b, comme indiqué dans *Selecting AAL*. dans [NIST 800-63b Section 6.2](https://pages.nist.gov/800-63-3/sp800-63-3.html#AAL_CYOA).

## Légende

Les applications peuvent toujours dépasser les exigences du niveau actuel, surtout si l'authentification moderne est sur la feuille de route d'une application. Auparavant, l'ASVS exigeait une MFA obligatoire. Le NIST n'exige pas de MFA obligatoire. Par conséquent, nous avons utilisé une désignation facultative dans ce chapitre pour indiquer où l'ASVS encourage, mais n'exige pas un contrôle. Les clés suivantes sont utilisées tout au long de cette norme :

| Mark | Description |
| :--: | :-- |
| | Not required |
| o | Recommended, but not required |
| ✓ | Required |

## V2.1 Sécurité des mots de passe

Les mots de passe, appelés "secrets mémorisés" par le NIST 800-63, comprennent les mots de passe, les codes PIN, les modèles de déverrouillage, le choix du bon chaton ou d'un autre élément d'image, et les phrases de passe. Ils sont généralement considérés comme "quelque chose que vous connaissez" et sont souvent utilisés comme authentifiant à facteur unique. Des défis importants se posent à l'utilisation continue de l'authentification à facteur unique, notamment les milliards de noms d'utilisateur et de mots de passe valides divulgués sur Internet, les mots de passe par défaut ou faibles, les rainbow tables et les dictionnaires ordonnés des mots de passe les plus courants.

Les applications doivent fortement encourager les utilisateurs à s'inscrire à l'authentification multifactorielle et leur permettre de réutiliser les jetons qu'ils possèdent déjà, tels que les jetons FIDO ou U2F, ou de se relier à un fournisseur de services d'accréditation qui fournit une authentification multifactorielle.

Les fournisseurs de services d'accréditation (CSP) fournissent une identité fédérée aux utilisateurs. Les utilisateurs auront souvent plus d'une identité auprès de plusieurs CSP, comme une identité d'entreprise utilisant Azure AD, Okta, Ping Identity ou Google, ou une identité de consommateur utilisant Facebook, Twitter, Google ou WeChat, pour ne citer que quelques alternatives courantes. Cette liste n'est pas une approbation de ces sociétés ou services, mais simplement un encouragement pour les développeurs à considérer la réalité que de nombreux utilisateurs ont plusieurs identités établies. Les organisations devraient envisager d'intégrer les identités existantes des utilisateurs, en fonction du profil de risque de la force de preuve d'identité du CSP. Par exemple, il est peu probable qu'une organisation gouvernementale accepte une identité de média social comme identifiant pour des systèmes sensibles, car il est facile de créer de fausses identités ou de jeter des identités, alors qu'une société de jeux mobiles pourrait bien avoir besoin d'intégrer les principales plateformes de média social pour accroître sa base de joueurs actifs.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.1.1** | Vérifiez que les mots de passe de l'ensemble des utilisateurs comportent au moins 12 caractères (après combinaison de plusieurs espaces). ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.2** | Vérifiez que les mots de passe d'au moins 64 caractères sont autorisés, et que les mots de passe de plus de 128 caractères sont refusés. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.3** | Vérifiez que la troncature du mot de passe n'est pas effectuée. Toutefois, les espaces multiples consécutifs peuvent être remplacés par un espace unique. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.4** | Vérifiez que tous les caractères Unicode imprimables, y compris les caractères neutres du point de vue de la langue tels que les espaces et les Emojis, sont autorisés dans les mots de passe. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.5** | Vérifier que les utilisateurs peuvent changer leur mot de passe. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.6** | Vérifiez que la fonctionnalité de changement de mot de passe nécessite le mot de passe actuel et le nouveau mot de passe de l'utilisateur. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.7** | Vérifiez que les mots de passe soumis lors de l'enregistrement du compte, de la connexion et du changement de mot de passe sont comparés à un ensemble de mots de passe violés, soit localement (comme les 1 000 ou 10 000 mots de passe les plus courants qui correspondent à la politique de mot de passe du système), soit en utilisant une API externe. En cas d'utilisation d'une API, une preuve de connaissance nulle ou un autre mécanisme doit être utilisé pour garantir que le mot de passe en texte clair n'est pas envoyé ou utilisé pour vérifier l'état de violation du mot de passe. Si le mot de passe est violé, l'application doit demander à l'utilisateur de définir un nouveau mot de passe non violé. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.8** | Vérifiez qu'un indicateur de force du mot de passe est fourni pour aider les utilisateurs à définir un mot de passe plus fort. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.9** | Vérifiez qu'il n'existe pas de règles de composition des mots de passe limitant le type de caractères autorisés. Il ne devrait pas y avoir d'exigence concernant les majuscules ou les minuscules, les chiffres ou les caractères spéciaux. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.10** | Vérifiez qu'il n'existe aucune exigence de rotation périodique des justificatifs ou d'historique des mots de passe. | ✓ | ✓ | ✓ | 263 | 5.1.1.2 |
| **2.1.11** | Vérifiez que la fonction "coller", les assistants de mot de passe du navigateur et les gestionnaires de mot de passe externes sont autorisés. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.12** | Vérifiez que l'utilisateur peut choisir de visualiser temporairement l'intégralité du mot de passe masqué ou le dernier caractère tapé du mot de passe sur les plateformes qui ne disposent pas de cette fonctionnalité intégrée. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |

Remarque : l'objectif de permettre à l'utilisateur de visualiser son mot de passe ou de voir temporairement le dernier caractère est d'améliorer la convivialité de la saisie des informations d'identification, notamment en ce qui concerne l'utilisation de mots de passe plus longs, de phrases de passe et de gestionnaires de mots de passe. Une autre raison d'inclure cette exigence est de dissuader ou d'empêcher les rapports de test d'exiger inutilement des organisations qu'elles modifient le comportement du champ de mot de passe de la plate-forme intégrée pour supprimer cette expérience de sécurité moderne et conviviale.

## V2.2 Sécurité générale des authentificateurs

L'agilité de l'authentificateur est essentielle pour les applications à l'épreuve du temps. Refactorisez les vérificateurs d'application pour autoriser des authentificateurs supplémentaires selon les préférences de l'utilisateur, ainsi que pour autoriser le retrait des authentificateurs obsolètes ou dangereux de manière ordonnée.

Le NIST considère l'email et le SMS comme des types d'[authentifiants "restreints"] (https://pages.nist.gov/800-63-FAQ/#q-b1), et il est probable qu'ils seront retirés du NIST 800-63 et donc de l'ASVS à un moment donné dans le futur. Les applications doivent prévoir une feuille de route qui ne nécessite pas l'utilisation de l'email ou du SMS.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.2.1** | Vérifiez que les contrôles anti-automatisation sont efficaces pour atténuer les tests d'identifiants violés, la force brute et les attaques de verrouillage de compte. Ces contrôles incluent le blocage des mots de passe violés les plus courants, les verrouillages logiciels, la limitation du débit, CAPTCHA, les délais sans cesse croissants entre les tentatives, les restrictions d'adresse IP ou les restrictions basées sur les risques telles que l'emplacement, la première connexion sur un appareil, les tentatives récentes de déverrouillage du compte, ou similaire. Vérifiez que pas plus de 100 tentatives infructueuses par heure ne sont possibles sur un seul compte. | ✓ | ✓ | ✓ | 307 | 5.2.2 / 5.1.1.2 / 5.1.4.2 / 5.1.5.2 |
| **2.2.2** | Vérifiez que l'utilisation d'authentificateurs faibles (tels que les SMS et les e-mails) est limitée à la vérification secondaire et à l'approbation des transactions et ne remplace pas des méthodes d'authentification plus sûres. Vérifiez que des méthodes plus fortes sont proposées avant les méthodes faibles, que les utilisateurs sont conscients des risques ou que des mesures appropriées sont en place pour limiter les risques de compromission des comptes. | ✓ | ✓ | ✓ | 304 | 5.2.10 |
| **2.2.3** | Vérifiez que des notifications sécurisées sont envoyées aux utilisateurs après la mise à jour des informations d'authentification, telles que la réinitialisation des informations d'identification, les changements d'adresse ou d'adresse électronique, la connexion à partir de lieux inconnus ou risqués. L'utilisation de notifications push - plutôt que de SMS ou d'email - est préférable, mais en l'absence de notifications push, les SMS ou les emails sont acceptables tant qu'aucune information sensible n'est divulguée dans la notification. | ✓ | ✓ | ✓ | 620 | |
| **2.2.4** | Vérifiez la résistance à l'usurpation d'identité contre le hameçonnage, comme l'utilisation d'une authentification multifactorielle, de dispositifs cryptographiques avec intention (tels que des clés connectées avec un bouton pour s'authentifier), ou à des niveaux AAL plus élevés, de certificats côté client. | | | ✓ | 308 | 5.2.5 |
| **2.2.5** | Vérifiez que lorsqu'un fournisseur de services d'authentification (CSP) et l'application vérifiant l'authentification sont séparés, un protocole TLS mutuellement authentifié est en place entre les deux points d'extrémité. | | | ✓ | 319 | 5.2.6 |
| **2.2.6** | Vérifier la résistance au rejeu par l'utilisation obligatoire de dispositifs de mots de passe à usage unique (OTP), d'authentifiants cryptographiques ou de codes de consultation. | | | ✓ | 308 | 5.2.8 |
| **2.2.7** | Vérifier l'intention d'authentification en exigeant la saisie d'un jeton OTP ou une action initiée par l'utilisateur, comme la pression d'un bouton sur une clé matérielle FIDO. | | | ✓ | 308 | 5.2.9 |

## V2.3 Cycle de vie de l'authentificateur

Les authentificateurs sont des mots de passe, des jetons logiciels, des jetons matériels et des dispositifs biométriques. Le cycle de vie des authentificateurs est essentiel à la sécurité d'une application. Si n'importe qui peut s'enregistrer sur un compte sans preuve d'identité, la confiance dans l'affirmation d'identité est faible. Pour les sites de médias sociaux comme Reddit, c'est parfaitement acceptable. Pour les systèmes bancaires, une plus grande attention portée à l'enregistrement et à l'émission d'informations d'identification et de dispositifs est essentielle à la sécurité de l'application.

Note : Les mots de passe ne doivent pas avoir une durée de vie maximale ni être soumis à une rotation. Les mots de passe doivent être vérifiés en cas de violation, et non remplacés régulièrement.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.3.1** | Vérifier les mots de passe initiaux ou les codes d'activation générés par le système DEVRAIENT être générés de manière aléatoire et sécurisée, devraient comporter au moins 6 caractères, et PEUVENT contenir des lettres et des chiffres, et expirer après une courte période de temps. Ces secrets initiaux ne doivent pas être autorisés à devenir le mot de passe à long terme. | ✓ | ✓ | ✓ | 330 | 5.1.1.2 / A.3 |
| **2.3.2** | Vérifiez que l'inscription et l'utilisation de dispositifs d'authentification fournis par l'utilisateur sont prises en charge, tels que les jetons U2F ou FIDO. | | ✓ | ✓ | 308 | 6.1.3 |
| **2.3.3** | Vérifiez que les instructions de renouvellement sont envoyées avec suffisamment de temps pour renouveler les authentificateurs à durée limitée. | | ✓ | ✓ | 287 | 6.1.4 |

## V2.4 Stockage des identifiants

Les architectes et les développeurs doivent adhérer à cette section lors de la construction ou de la refonte du code. Cette section ne peut être entièrement vérifiée qu'au moyen d'un examen du code source ou de tests unitaires ou d'intégration sécurisés. Les tests d'intrusion ne peuvent identifier aucun de ces problèmes.

La liste des fonctions de dérivation de clés unidirectionnelles approuvées est détaillée dans la section 5.1.1.2 de la norme NIST 800-63 B, et dans [BSI Kryptographische Verfahren : Empfehlungen und Schlussell&auml;ngen (2018)] (https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile). Les dernières normes nationales ou régionales en matière d'algorithme et de longueur de clé peuvent être choisies à la place de ces choix.

Cette section ne peut pas être testée avec des tests d'intrusion, donc les contrôles ne sont pas marqués comme L1. Cependant, cette section est d'une importance vitale pour la sécurité des informations d'identification si elles sont volées, donc si vous bifurquez l'ASVS pour une directive d'architecture ou de codage ou une liste de contrôle de révision du code source, veuillez replacer ces contrôles en L1 dans votre version privée.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.4.1** | Vérifiez que les mots de passe sont stockés sous une forme qui résiste aux attaques hors ligne. Les mots de passe DOIVENT être salés et hachés à l'aide d'une fonction approuvée de dérivation de clé ou de hachage de mot de passe à sens unique. Les fonctions de dérivation de clé et de hachage de mot de passe prennent en entrée un mot de passe, un sel et un facteur de coût pour générer un hachage de mot de passe. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.2** | Vérifiez que le sel a une longueur d'au moins 32 bits et qu'il est choisi de manière arbitraire pour minimiser les collisions de valeurs de sel parmi les hachages stockés. Pour chaque justificatif, une valeur de sel unique et le hachage résultant DOIVENT être stockés. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.3** | Vérifiez que si PBKDF2 est utilisé, le nombre d'itérations DEVRAIT être aussi élevé que les performances du serveur de vérification le permettent, généralement au moins 100 000 itérations. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.4** | Vérifiez que si bcrypt est utilisé, le facteur de travail DEVRAIT être aussi grand que les performances du serveur de vérification le permettent, avec un minimum de 10. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.5** | Vérifier qu'une itération supplémentaire d'une fonction de dérivation de clé est effectuée, en utilisant une valeur de sel qui est secrète et connue seulement du vérificateur. Générer la valeur de sel à l'aide d'un générateur de bits aléatoires approuvé [SP 800-90Ar1] et fournir au moins la force de sécurité minimale spécifiée dans la dernière révision de SP 800-131A. La valeur secrète du sel DOIT être stockée séparément des mots de passe hachés (par exemple, dans un dispositif spécialisé tel qu'un module de sécurité matériel). | | ✓ | ✓ | 916 | 5.1.1.2 |

Lorsque les normes américaines sont mentionnées, une norme régionale ou locale peut être utilisée à la place ou en plus de la norme américaine, selon les besoins.

## V2.5 Récupération des identifiants

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.5.1** | Vérifiez qu'un secret d'activation initiale ou de récupération généré par le système n'est pas envoyé en clair à l'utilisateur. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.2** | Vérifiez que les indices de mot de passe ou l'authentification basée sur la connaissance (les "questions secrètes") ne sont pas présents. | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.3** | La récupération des justificatifs de mot de passe ne révèle en aucun cas le mot de passe actuel. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.4** | Vérifiez que les comptes partagés ou par défaut ne sont pas présents (par exemple, "root", "admin" ou "sa"). | ✓ | ✓ | ✓ | 16 | 5.1.1.2 / A.3 |
| **2.5.5** | Vérifiez que si un facteur d'authentification est modifié ou remplacé, l'utilisateur est informé de cet événement. | ✓ | ✓ | ✓ | 304 | 6.1.2.3 |
| **2.5.6** | La vérification du mot de passe oublié et les autres voies de récupération utilisent un mécanisme de récupération sécurisé, tel qu'un OTP basé sur le temps (TOTP) ou un autre jeton logiciel, un push mobile ou un autre mécanisme de récupération hors ligne. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.7** | Vérifiez qu'en cas de perte des facteurs d'authentification OTP ou multifactorielle, la preuve d'identité est effectuée au même niveau que lors de l'inscription. | | ✓ | ✓ | 308 | 6.1.2.3 |

## V2.6 Vérificateur de secret de secours

Les secrets de secours sont des listes pré-générées de codes secrets, similaires aux numéros d'autorisation de transaction (TAN), aux codes de récupération des médias sociaux ou à une grille contenant un ensemble de valeurs aléatoires. Ceux-ci sont distribués en toute sécurité aux utilisateurs. Ces codes de secours sont utilisés une seule fois, et une fois tous utilisés, la liste secrète de secours est supprimée. Ce type d'authentificateur est considéré comme "quelque chose que vous avez".

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.6.1** | Vérifier que les secrets de secours ne peuvent être utilisés qu'une seule fois. | | ✓ | ✓ | 308 | 5.1.2.2 |
| **2.6.2** | Vérifiez que les secrets de secours ont un caractère aléatoire suffisant (112 bits d'entropie) ou, s'ils ont moins de 112 bits d'entropie, qu'ils sont salés avec un sel unique et aléatoire de 32 bits et hachés avec un hachage à sens unique approuvé. | | ✓ | ✓ | 330 | 5.1.2.2 |
| **2.6.3** | Vérifiez que les secrets de secours sont résistants aux attaques hors ligne, telles que les valeurs prévisibles. | | ✓ | ✓ | 310 | 5.1.2.2 |

## V2.7 Vérificateur hors bande

Dans le passé, un vérificateur hors bande commun aurait été un email ou un SMS contenant un lien de réinitialisation du mot de passe. Les attaquants utilisent ce mécanisme faible pour réinitialiser les comptes qu'ils ne contrôlent pas encore, par exemple en prenant le contrôle du compte de messagerie d'une personne et en réutilisant les liens de réinitialisation découverts. Il existe de meilleures façons de gérer la vérification hors bande.

Les authentificateurs hors bande sécurisés sont des dispositifs physiques qui peuvent communiquer avec le vérificateur par un canal secondaire sécurisé. Les exemples incluent les notifications push sur les appareils mobiles. Ce type d'authentificateur est considéré comme "quelque chose que vous avez". Lorsqu'un utilisateur souhaite s'authentifier, l'application de vérification envoie un message à l'authentificateur hors bande via une connexion à l'authentificateur directement ou indirectement par le biais d'un service tiers. Le message contient un code d'authentification (généralement un nombre aléatoire à six chiffres ou un dialogue d'approbation modal). L'application de vérification attend de recevoir le code d'authentification par le canal primaire et compare le hachage de la valeur reçue au hachage du code d'authentification original. S'ils correspondent, le vérificateur hors bande peut supposer que l'utilisateur s'est authentifié.

L'ASVS part du principe que seuls quelques développeurs mettront au point de nouveaux authentificateurs hors bande, tels que les notifications push, et donc que les contrôles ASVS suivants s'appliquent aux vérificateurs, tels que les API d'authentification, les applications et les implémentations d'authentification unique. Si vous développez un nouvel authentificateur hors bande, veuillez vous référer à NIST 800-63B &sect ; 5.1.3.1.

Les authentificateurs hors bande non sûrs, tels que l'email et la voix sur IP, ne sont pas autorisés. L'authentification par téléphone et par SMS est actuellement "restreinte" par le NIST et devrait être dépréciée en faveur des notifications push ou similaires. Si vous avez besoin d'utiliser l'authentification hors bande par téléphone ou SMS, veuillez vous reporter à &sect ; 5.1.3.3.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.7.1** | Vérifiez que les authentificateurs en texte clair hors bande (NIST "restreint"), tels que les SMS ou le PSTN, ne sont pas proposés par défaut, et que des alternatives plus solides telles que les notifications push sont proposées en premier. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.2** | Vérifiez que le vérificateur hors bande expire les demandes d'authentification hors bande, les codes ou les jetons après 10 minutes. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.3** | Vérifiez que les demandes d'authentification, les codes ou les jetons du vérificateur hors bande ne sont utilisables qu'une seule fois, et uniquement pour la demande d'authentification initiale. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.4** | Vérifier que l'authentificateur et le vérificateur hors bande communiquent sur un canal indépendant sécurisé. | ✓ | ✓ | ✓ | 523 | 5.1.3.2 |
| **2.7.5** | Vérifiez que le vérificateur hors bande ne conserve qu'une version hachée du code d'authentification. | | ✓ | ✓ | 256 | 5.1.3.2 |
| **2.7.6** | Vérifiez que le code d'authentification initiale est généré par un générateur de nombres aléatoires sécurisé, contenant au moins 20 bits d'entropie (généralement, un nombre aléatoire numérique de six est suffisant). | | ✓ | ✓ | 310 | 5.1.3.2 |

## V2.8 Vérificateur unique

Les mots de passe à usage unique (OTP) à facteur unique sont des jetons physiques ou logiciels qui affichent un défi à usage unique pseudo-aléatoire changeant en permanence. Ces dispositifs rendent le phishing (usurpation d'identité) difficile, mais pas impossible. Ce type d'authentifiant est considéré comme "quelque chose que vous avez". Les jetons multifacteurs sont similaires aux OTP à facteur unique, mais nécessitent la saisie d'un code PIN valide, le déverrouillage biométrique, l'insertion d'une clé USB ou le couplage NFC ou une valeur supplémentaire (comme les calculateurs de signature de transaction) pour créer l'OTP final.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.8.1** | Vérifiez que les OTP basés sur le temps ont une durée de vie définie avant d'expirer. | ✓ | ✓ | ✓ | 613 | 5.1.4.2 / 5.1.5.2 |
| **2.8.2** | Vérifiez que les clés symétriques utilisées pour vérifier les OTP soumises sont hautement protégées, par exemple en utilisant un module de sécurité matériel ou un système d'exploitation sécurisé pour le stockage des clés. | | ✓ | ✓ | 320 | 5.1.4.2 / 5.1.5.2|
| **2.8.3** | Vérifier que des algorithmes cryptographiques approuvés sont utilisés pour la génération, l'ensemencement et la vérification des OTP. | | ✓ | ✓ | 326 | 5.1.4.2 / 5.1.5.2 |
| **2.8.4** | Vérifiez que l'OTP basé sur le temps ne peut être utilisé qu'une seule fois pendant la période de validité. | | ✓ | ✓ | 287 | 5.1.4.2 / 5.1.5.2 |
| **2.8.5** | Vérifiez que si un jeton OTP multifacteur basé sur le temps est réutilisé pendant la période de validité, il est enregistré et rejeté, et des notifications sécurisées sont envoyées au détenteur du dispositif. | | ✓ | ✓ | 287 | 5.1.5.2 |
| **2.8.6** | Vérifiez que le générateur d'OTP à facteur unique physique peut être révoqué en cas de vol ou autre perte. Assurez-vous que la révocation est immédiatement effective pour toutes les sessions connectées, quel que soit le lieu. | | ✓ | ✓ | 613 | 5.2.1 |
| **2.8.7** | Vérifiez que les authentificateurs biométriques ne peuvent être utilisés que comme facteurs secondaires en conjonction avec une chose que vous avez ou une chose que vous connaissez. | | o | ✓ | 308 | 5.2.3 |

## V2.9 Vérificateur cryptographique

Les clés cryptographiques de sécurité sont des cartes à puce ou des clés FIDO, pour lesquelles l'utilisateur doit brancher ou coupler le dispositif cryptographique à l'ordinateur pour compléter l'authentification. Les vérificateurs envoient un nonce de défi aux dispositifs cryptographiques ou au logiciel, et le dispositif ou le logiciel calcule une réponse sur la base d'une clé cryptographique stockée de manière sécurisée.

Les exigences applicables aux dispositifs et logiciels cryptographiques à facteur unique et aux dispositifs et logiciels cryptographiques à facteurs multiples sont les mêmes, car la vérification de l'authentifiant cryptographique prouve la possession du facteur d'authentification.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.9.1** | Vérifiez que les clés cryptographiques utilisées dans la vérification sont stockées de manière sécurisée et protégées contre la divulgation, par exemple à l'aide d'un module de plateforme de confiance (TPM) ou d'un module de sécurité matériel (HSM), ou d'un service de système d'exploitation qui peut utiliser ce stockage sécurisé. | | ✓ | ✓ | 320 | 5.1.7.2 |
| **2.9.2** | Vérifiez que le nonce de défi a une longueur d'au moins 64 bits et qu'il est statistiquement unique ou unique pendant la durée de vie du dispositif cryptographique. | | ✓ | ✓ | 330 | 5.1.7.2 |
| **2.9.3** | Vérifier que des algorithmes cryptographiques approuvés sont utilisés pour la génération, l'ensemencement et la vérification. | | ✓ | ✓ | 327 | 5.1.7.2 |

## V2.10 Authentification des services

Cette section ne peut pas faire l'objet d'un test d'intrusion et n'a donc pas d'exigences de niveau L1. Cependant, si elle est utilisée dans le cadre d'une revue d'architecture, de codage ou de code sécurisé, veuillez supposer que le logiciel (tout comme Java Key Store) est l'exigence minimale à L1. Le stockage en texte clair des secrets n'est en aucun cas acceptable.

| # | Description | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.10.1** | Vérifiez que les secrets intra-services ne reposent pas sur des informations d'identification immuables telles que des mots de passe, des clés API ou des comptes partagés avec un accès privilégié. | | OS assisted | HSM | 287 | 5.1.1.1 |
| **2.10.2** | Vérifiez que si des mots de passe sont requis pour l'authentification des services, le compte de service utilisé n'est pas un identifiant par défaut. (par exemple, root/root ou admin/admin sont utilisés par défaut dans certains services lors de l'installation). | | OS assisted | HSM | 255 | 5.1.1.1 |
| **2.10.3** | Vérifiez que les mots de passe sont stockés avec une protection suffisante pour empêcher les attaques de récupération hors ligne, y compris l'accès au système local. | | OS assisted | HSM | 522 | 5.1.1.1 |
| **2.10.4** | Vérifiez que les mots de passe, les intégrations avec des bases de données et des systèmes tiers, les graines et les secrets internes, ainsi que les clés API sont gérés de manière sécurisée et ne sont pas inclus dans le code source ou stockés dans des dépôts de code source. Un tel stockage DEVRAIT résister aux attaques hors ligne. L'utilisation d'un magasin de clés logiciel sécurisé (L1), d'un TPM matériel ou d'un HSM (L3) est recommandée pour le stockage des mots de passe. | | OS assisted | HSM | 798 | |

## Exigences supplémentaires de l'agence américaine

Les agences américaines ont des exigences obligatoires concernant la norme NIST 800-63. La norme de vérification de la sécurité des applications a toujours porté sur les 80 % de contrôles qui s'appliquent à presque 100 % des applications, et non sur les derniers 20 % de contrôles avancés ou ceux qui ont une applicabilité limitée. En tant que tel, l'ASVS est un sous-ensemble strict du NIST 800-63, en particulier pour les classifications IAL1/2 et AAL1/2, mais n'est pas suffisamment complet, notamment en ce qui concerne les classifications IAL3/AAL3.

Nous demandons instamment aux agences gouvernementales américaines de revoir et d'appliquer la norme NIST 800-63 dans son intégralité.

## Glossaire

| Terme | Signification |
| -- | -- |
| CSP | Fournisseur de services d'accréditation, également appelé fournisseur d'identité. |
| Authentificateur | Code qui authentifie un mot de passe, un jeton, un MFA, une assertion fédérée, etc. |
| Vérificateur | "Entité qui vérifie l'identité du demandeur en vérifiant la possession et le contrôle par ce dernier d'un ou deux authentifiants à l'aide d'un protocole d'authentification. Pour ce faire, le vérificateur peut également avoir besoin de valider les informations d'identification qui relient le ou les authentificateurs à l'identifiant de l'abonné et de vérifier leur état. " |
| OTP | One-time password |
| SFA | Authentificateurs à facteur unique, tels que quelque chose que vous connaissez (secrets mémorisés, mots de passe, phrases de passe, PIN), quelque chose que vous êtes (biométrie, empreintes digitales, scans du visage) ou quelque chose que vous avez (jetons OTP, un dispositif cryptographique tel qu'une carte à puce)., |
| MFA | L'authentification multifactorielle, qui comprend deux facteurs uniques ou plus. |

## Références

Pour plus d'informations, voir également :

* [NIST 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST 800-63 A - Enrollment and Identity Proofing](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST 800-63 B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST 800-63 C - Federation and Assertions](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [OWASP Cheat Sheet - Password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Forgot password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Choosing and using security questions](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
