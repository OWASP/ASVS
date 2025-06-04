# V6 Authentification

## Objectif du contrôle

L'authentification est le processus permettant d'établir ou de confirmer l'authenticité d'une personne ou d'un appareil. Elle consiste à vérifier les déclarations d'une personne ou d'un appareil, à garantir la résistance à l'usurpation d'identité et à empêcher la récupération ou l'interception des mots de passe.

Le [NIST SP 800-63](https://pages.nist.gov/800-63-3/) est une norme moderne, fondée sur des preuves, qui est précieuse pour les organisations du monde entier, mais qui est particulièrement pertinente pour les agences américaines et celles qui interagissent avec les agences américaines.

Bien que de nombreuses exigences de ce chapitre soient basées sur la deuxième section de la norme (appelée NIST SP 800-63B « Directives relatives à l'identité numérique - Authentification et gestion du cycle de vie »), ce chapitre se concentre sur les menaces courantes et les faiblesses d'authentification fréquemment exploitées. Il ne prétend pas couvrir tous les points de la norme de manière exhaustive. Pour les cas où une conformité totale à la norme NIST SP 800-63 est nécessaire, veuillez vous référer à cette dernière.

De plus, la terminologie du NIST SP 800-63 peut parfois différer, et ce chapitre utilise souvent une terminologie plus communément comprise pour améliorer la clarté.

Une fonctionnalité commune aux applications plus avancées est la possibilité d'adapter les étapes d'authentification requises en fonction de divers facteurs de risque. Cette fonctionnalité est abordée dans le chapitre « Autorisation », car ces mécanismes doivent également être pris en compte dans les décisions d'autorisation.

## V6.1 Documentation d'authentification

Cette section détaille les exigences relatives à la documentation d'authentification à conserver pour une application. Elle est essentielle à la mise en œuvre et à l'évaluation de la configuration des contrôles d'authentification pertinents.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **6.1.1** | Vérifiez que la documentation de l'application définit comment les contrôles, tels que la limitation de débit, l'anti-automatisation et la réponse adaptative, sont utilisés pour se défendre contre les attaques telles que le « credential stuffing » et la force brute des mots de passe. La documentation doit expliquer clairement comment ces contrôles sont configurés et empêcher le verrouillage malveillant des comptes. | 1 |
| **6.1.2** | Vérifiez qu'une liste de mots spécifiques au contexte est documentée afin d'empêcher leur utilisation dans les mots de passe. Cette liste peut inclure des permutations de noms d'organisations, de produits, d'identifiants de systèmes, de noms de codes de projets, de noms de services ou de rôles, etc. | 2 |
| **6.1.3** | Vérifiez que, si l'application inclut plusieurs voies d'authentification, celles-ci sont toutes documentées avec les contrôles de sécurité et la force d'authentification qui doivent être appliqués de manière cohérente. | 2 |

## V6.2 Sécurité des mots de passe

Les mots de passe, appelés « secrets mémorisés » par la norme NIST SP 800-63, comprennent les mots de passe, les phrases de passe, les codes PIN, les schémas de déverrouillage et le choix du chaton ou d'un autre élément d'image. Ils sont généralement considérés comme « quelque chose que vous connaissez » et sont souvent utilisés comme mécanisme d'authentification à facteur unique.

Cette section contient donc des exigences visant à garantir la création et la gestion sécurisées des mots de passe. La plupart des exigences sont de niveau 1, car elles sont les plus importantes à ce niveau. À partir du niveau 2, des mécanismes d'authentification multifacteur sont requis, les mots de passe pouvant être l'un de ces facteurs.

Les exigences de cette section concernent principalement le chapitre [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) du [Guide du NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Niveau |
| :---: | :--- | :---: |
| **6.2.1** | Vérifiez que les mots de passe définis par l'utilisateur comportent au moins 8 caractères, bien qu'un minimum de 15 caractères soit fortement recommandé. | 1 |
| **6.2.2** | Vérifiez que les utilisateurs peuvent modifier leur mot de passe. | 1 |
| **6.2.3** | Vérifiez que la fonctionnalité de changement de mot de passe nécessite le mot de passe actuel et le nouveau mot de passe de l'utilisateur. | 1 |
| **6.2.4** | Vérifiez que les mots de passe soumis lors de l'enregistrement du compte ou du changement de mot de passe sont vérifiés par rapport à un ensemble disponible d'au moins 3 000 mots de passe principaux qui correspondent à la politique de mot de passe de l'application, par exemple la longueur minimale. | 1 |
| **6.2.5** | Vérifiez que les mots de passe peuvent être utilisés, quelle que soit leur composition, sans restriction quant au type de caractères autorisés. Aucun nombre minimal de majuscules ou de minuscules, de chiffres ou de caractères spéciaux ne doit être exigé. | 1 |
| **6.2.6** | Vérifiez que les champs de saisie du mot de passe utilisent type=password pour masquer la saisie. Les applications peuvent permettre à l'utilisateur d'afficher temporairement l'intégralité du mot de passe masqué ou le dernier caractère saisi. | 1 |
| **6.2.7** | Vérifiez que la fonctionnalité « coller », les assistants de mot de passe du navigateur et les gestionnaires de mots de passe externes sont autorisés. | 1 |
| **6.2.8** | Vérifiez que l'application vérifie le mot de passe de l'utilisateur exactement tel qu'il a été reçu de l'utilisateur, sans aucune modification telle qu'une troncature ou une transformation de casse. | 1 |
| **6.2.9** | Vérifiez que les mots de passe d’au moins 64 caractères sont autorisés. | 2 |
| **6.2.10** | Vérifiez que le mot de passe d'un utilisateur reste valide jusqu'à ce qu'il soit découvert comme compromis ou qu'il soit renouvelé. L'application ne doit pas exiger de renouvellement périodique des identifiants. | 2 |
| **6.2.11** | Vérifiez que la liste documentée de mots spécifiques au contexte est utilisée pour éviter la création de mots de passe faciles à deviner. | 2 |
| **6.2.12** | Vérifiez que les mots de passe soumis lors de l'enregistrement du compte ou des modifications de mot de passe sont vérifiés par rapport à un ensemble de mots de passe violés. | 2 |

## V6.3 Sécurité générale de l'authentification

Cette section contient les exigences générales relatives à la sécurité des mécanismes d'authentification et définit les différentes attentes en matière de niveaux. Les applications L2 doivent recourir à l'authentification multifacteur (MFA). Les applications L3 doivent utiliser une authentification matérielle, réalisée dans un environnement d'exécution certifié et approuvé (TEE). Cela peut inclure des clés d'accès liées à l'appareil, des authentificateurs eIDAS à niveau d'assurance élevé (LoA), des authentificateurs avec l'assurance NIST Authenticator Assurance Level 3 (AAL3) ou un mécanisme équivalent.

Bien qu'il s'agisse d'une position relativement agressive sur l'authentification multifacteur, il est essentiel de relever la barre à ce sujet pour protéger les utilisateurs, et toute tentative d'assouplissement de ces exigences doit être accompagnée d'un plan clair sur la manière dont les risques liés à l'authentification seront atténués, en tenant compte des orientations et des recherches du NIST sur le sujet.

Veuillez noter qu'au moment de la publication, la norme NIST SP 800-63 considère l'email comme [non acceptable](https://pages.nist.gov/800-63-FAQ/#q-b11) comme mécanisme d'authentification ([copie archivée](https://web.archive.org/web/20250330115328/https://pages.nist.gov/800-63-FAQ/#q-b11)).

Les exigences de cette section concernent diverses sections du [Guide du NIST](https://pages.nist.gov/800-63-3/sp800-63b.html), incluant : [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling), et [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding).

| # | Description | Niveau |
| :---: | :--- | :---: |
| **6.3.1** | Vérifiez que les contrôles visant à empêcher les attaques telles que le bourrage d'informations d'identification et la force brute des mots de passe sont mis en œuvre conformément à la documentation de sécurité de l'application. | 1 |
| **6.3.2** | Vérifiez que les comptes d’utilisateur par défaut (par exemple, « root », « admin » ou « sa ») ne sont pas présents dans l’application ou sont désactivés. | 1 |
| **6.3.3** | Vérifiez que l’application exige que les utilisateurs utilisent un mécanisme d’authentification multifacteur ou une combinaison de mécanismes d’authentification à facteur unique. | 2 |
| **6.3.4** | Vérifiez que, si l’application inclut plusieurs voies d’authentification, il n’existe aucune voie non documentée et que les contrôles de sécurité et la force d’authentification sont appliqués de manière cohérente. | 2 |
| **6.3.5** | Vérifiez que les utilisateurs sont informés des tentatives d'authentification suspectes (réussies ou non). Il peut s'agir de tentatives d'authentification provenant d'un emplacement ou d'un client inhabituel, d'une authentification partiellement réussie (un seul facteur parmi plusieurs), d'une tentative d'authentification après une longue période d'inactivité ou d'une authentification réussie après plusieurs tentatives infructueuses. | 3 |
| **6.3.6** | Vérifiez que le courrier électronique n’est pas utilisé comme mécanisme d’authentification à facteur unique ou à facteurs multiples. | 3 |
| **6.3.7** | Vérifiez que les utilisateurs sont avertis après les mises à jour des détails d'authentification, telles que les réinitialisations d'informations d'identification ou la modification du nom d'utilisateur ou de l'adresse e-mail. | 3 |
| **6.3.8** | Vérifiez que les utilisateurs valides ne peuvent pas être déduits d'échecs d'authentification, par exemple en se basant sur des messages d'erreur, des codes de réponse HTTP ou des temps de réponse différents. Les fonctionnalités d'inscription et de mot de passe oublié doivent également bénéficier de cette protection. | 3 |

## V6.4 Cycle de vie et récupération du facteur d'authentification

Les facteurs d'authentification peuvent inclure des mots de passe, des jetons logiciels, des jetons matériels et des dispositifs biométriques. La gestion sécurisée du cycle de vie de ces mécanismes est essentielle à la sécurité d'une application, et cette section présente les exigences y afférentes.

Les exigences de cette section concernent principalement les chapitres [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) ou [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) of [Guide du NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Niveau |
| :---: | :--- | :---: |
| **6.4.1** | Vérifiez que les mots de passe initiaux ou les codes d'activation générés par le système sont générés de manière aléatoire et sécurisée, qu'ils respectent la politique de mots de passe en vigueur et qu'ils expirent après une courte période ou après leur première utilisation. Ces secrets initiaux ne doivent pas devenir des mots de passe permanents. | 1 |
| **6.4.2** | Vérifiez que les indices de mot de passe ou l'authentification basée sur les connaissances (appelées « questions secrètes ») ne sont pas présents. | 1 |
| **6.4.3** | Vérifiez qu'un processus sécurisé de réinitialisation d'un mot de passe oublié est mis en œuvre, qui ne contourne aucun mécanisme d'authentification multifacteur activé. | 2 |
| **6.4.4** | Vérifiez que si un facteur d'authentification multifacteur est perdu, la preuve de vérification d'identité est effectuée au même niveau que lors de l'inscription. | 2 |
| **6.4.5** | Vérifiez que les instructions de renouvellement des mécanismes d'authentification qui expirent sont envoyées avec suffisamment de temps pour être exécutées avant l'expiration de l'ancien mécanisme d'authentification, en configurant des rappels automatiques si nécessaire. | 3 |
| **6.4.6** | Vérifiez que les administrateurs peuvent initier la réinitialisation du mot de passe de l'utilisateur, mais que cela ne leur permet pas de modifier ou de choisir son mot de passe. Cela évite qu'ils ne connaissent le mot de passe de l'utilisateur. | 3 |

## V6.5 Exigences générales en matière d'authentification multifacteur

Cette section fournit des conseils généraux qui seront pertinents pour différentes méthodes d’authentification multifactorielle.

Les mécanismes comprennent :

* Recherche de secrets
* Mots de passe à usage unique (TOTP)
* Mécanismes hors bande

Les secrets de recherche sont des listes pré-générées de codes secrets, similaires aux numéros d'autorisation de transaction (TAN), aux codes de récupération des réseaux sociaux ou à une grille contenant un ensemble de valeurs aléatoires. Ce type de mécanisme d'authentification est considéré comme « quelque chose que vous possédez », car les codes sont volontairement non mémorisables et doivent donc être stockés quelque part.

Les mots de passe à usage unique temporaires (TOTP) sont des jetons physiques ou logiciels qui affichent un code pseudo-aléatoire à usage unique et changeant en permanence. Ce type de mécanisme d'authentification est considéré comme « quelque chose que vous possédez ». Les TOTP multifactoriels sont similaires aux TOTP monofactoriels, mais nécessitent la saisie d'un code PIN valide, d'un déverrouillage biométrique, d'une clé USB ou d'un appairage NFC, ou d'une valeur supplémentaire (comme des calculateurs de signature de transaction) pour créer le mot de passe à usage unique (OTP) final.

Des détails sur les mécanismes hors bande seront fournis dans la section suivante.

Les exigences de ces sections concernent principalement les chapitres [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators), et [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) du [Guide du NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Niveau |
| :---: | :--- | :---: |
| **6.5.1** | Vérifiez que les secrets de recherche, les demandes ou codes d'authentification hors bande et les mots de passe à usage unique basés sur le temps (TOTP) ne peuvent être utilisés avec succès qu'une seule fois. | 2 |
| **6.5.2** | Vérifiez que, lors de leur stockage dans le backend de l'application, les secrets de recherche comportant moins de 112 bits d'entropie (19 caractères alphanumériques aléatoires ou 34 chiffres aléatoires) sont hachés avec un algorithme de hachage de stockage de mots de passe approuvé, intégrant un sel aléatoire de 32 bits. Une fonction de hachage standard peut être utilisée si le secret comporte 112 bits d'entropie ou plus. | 2 |
| **6.5.3** | Vérifiez que les secrets de recherche, le code d'authentification hors bande et les mots de passe à usage unique basés sur le temps sont générés à l'aide d'un générateur de nombres pseudo-aléatoires cryptographiquement sécurisé (CSPRNG) pour éviter les valeurs prévisibles. | 2 |
| **6.5.4** | Vérifiez que les secrets de recherche et les codes d'authentification hors bande ont un minimum de 20 bits d'entropie (généralement 4 caractères alphanumériques aléatoires ou 6 chiffres aléatoires suffisent). | 2 |
| **6.5.5** | Vérifiez que les requêtes, codes ou jetons d'authentification hors bande, ainsi que les mots de passe à usage unique (TOTP), ont une durée de vie définie. Les requêtes hors bande doivent avoir une durée de vie maximale de 10 minutes et les TOTP, de 30 secondes. | 2 |
| **6.5.6** | Vérifiez que tout facteur d’authentification (y compris les appareils physiques) peut être révoqué en cas de vol ou autre perte. | 3 |
| **6.5.7** | Vérifiez que les mécanismes d’authentification biométrique ne sont utilisés que comme facteurs secondaires, avec quelque chose que vous possédez ou quelque chose que vous savez. | 3 |
| **6.5.8** | Vérifiez que les mots de passe à usage unique basés sur le temps (TOTP) sont vérifiés en fonction d'une source temporelle provenant d'un service de confiance et non d'une heure non fiable ou fournie par le client. | 3 |

## V6.6 Mécanismes d'authentification hors bande

Cela implique généralement que le serveur d'authentification communique avec un appareil physique via un canal secondaire sécurisé. Par exemple, l'envoi de notifications push aux appareils mobiles. Ce type de mécanisme d'authentification est considéré comme « quelque chose que vous possédez ».

Les mécanismes d'authentification hors bande non sécurisés tels que le courrier électronique et la VoIP ne sont pas autorisés. L'authentification PSTN et SMS est actuellement considérée comme des [mécanismes d'authentification « restreints »](https://pages.nist.gov/800-63-FAQ/#q-b01) par le NIST et devrait être déconseillée au profit des mots de passe à usage unique basés sur le temps (TOTP), d'un mécanisme cryptographique ou similaire. La norme NIST SP 800-63B [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network) recommande de traiter les risques d'échange d'appareil, de changement de carte SIM, de portage de numéro ou d'autres comportements anormaux, si l'authentification hors bande par téléphone ou SMS doit absolument être prise en charge. Bien que cette section ASVS n'impose pas cela comme une exigence, le fait de ne pas prendre ces précautions pour une application L2 sensible ou une application L3 doit être considéré comme un signal d'alarme important.

Notez que le NIST a également récemment publié des directives [déconseillant l'utilisation des notifications push](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/#fig-3). Bien que cette section ASVS ne le fasse pas, il est important d'être conscient des risques de « push bombing ».

| # | Description | Niveau |
| :---: | :--- | :---: |
| **6.6.1** | Vérifier que les mécanismes d'authentification utilisant le réseau téléphonique public commuté (RTPC) pour la transmission de mots de passe à usage unique (OTP) par téléphone ou SMS ne sont proposés que lorsque le numéro de téléphone a été préalablement validé. D'autres méthodes plus robustes (telles que les mots de passe à usage unique à durée déterminée) sont également proposées, et que le service informe les utilisateurs des risques de sécurité qu'elles présentent. Pour les applications de niveau 3, le téléphone et les SMS ne doivent pas être disponibles. | 2 |
| **6.6.2** | Vérifiez que les demandes d’authentification hors bande, les codes ou les jetons sont liés à la demande d’authentification d’origine pour laquelle ils ont été générés et ne sont pas utilisables pour une demande précédente ou ultérieure. | 2 |
| **6.6.3** | Vérifiez qu'un mécanisme d'authentification hors bande basé sur du code est protégé contre les attaques par force brute grâce à la limitation du débit. Envisagez également d'utiliser un code avec au moins 64 bits d'entropie. | 2 |
| **6.6.4** | Vérifiez que, lorsque les notifications push sont utilisées pour l'authentification multifacteur, la limitation du débit est appliquée afin d'empêcher les attaques de type « push bombing ». La correspondance des numéros peut également atténuer ce risque. | 3 |

## V6.7 Mécanisme d'authentification cryptographique

Les mécanismes d'authentification cryptographique incluent les cartes à puce ou les clés FIDO. L'utilisateur doit connecter ou appairer le dispositif cryptographique à l'ordinateur pour finaliser l'authentification. Le serveur d'authentification envoie un nonce de défi au dispositif ou au logiciel cryptographique, qui calcule une réponse à partir d'une clé cryptographique stockée de manière sécurisée. Les exigences de cette section fournissent des conseils spécifiques à la mise en œuvre de ces mécanismes, les conseils sur les algorithmes cryptographiques étant traités dans le chapitre « Cryptographie ».

Lorsque des clés partagées ou secrètes sont utilisées pour l'authentification cryptographique, elles doivent être stockées à l'aide des mêmes mécanismes que les autres secrets système, comme documenté dans la section « Gestion des secrets » du chapitre « Configuration ».

Les exigences de cette section concernent principalement le chapitre [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) du [Guide du NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Description | Niveau |
| :---: | :--- | :---: |
| **6.7.1** | Vérifiez que les certificats utilisés pour vérifier les assertions d’authentification cryptographique sont stockés de manière à les protéger contre toute modification. | 3 |
| **6.7.2** | Vérifiez que le nonce de défi a une longueur d'au moins 64 bits et qu'il est statistiquement unique ou unique sur toute la durée de vie du périphérique cryptographique. | 3 |

## V6.8 Authentification avec un fournisseur d'identité

Les fournisseurs d'identité (IdP) fournissent une identité fédérée aux utilisateurs. Ces derniers possèdent souvent plusieurs identités auprès de plusieurs IdP, comme une identité d'entreprise utilisant Azure AD, Okta, Ping Identity ou Google, ou une identité grand public utilisant Facebook, Twitter, Google ou WeChat, pour ne citer que quelques alternatives courantes. Cette liste ne constitue pas une recommandation pour ces entreprises ou services, mais simplement un encouragement aux développeurs à prendre en compte le fait que de nombreux utilisateurs possèdent de nombreuses identités établies. Les organisations devraient envisager l'intégration avec les identités utilisateur existantes, en fonction du profil de risque lié à la fiabilité de la vérification d'identité de l'IdP. Par exemple, il est peu probable qu'une organisation gouvernementale accepte une identité de réseau social comme identifiant pour des systèmes sensibles, car il est facile de créer de fausses identités ou des identités jetables, tandis qu'une entreprise de jeux mobiles pourrait avoir besoin de s'intégrer aux principales plateformes de réseaux sociaux pour développer sa base de joueurs actifs.

L'utilisation sécurisée de fournisseurs d'identité externes nécessite une configuration et une vérification rigoureuses afin d'éviter l'usurpation d'identité ou la falsification d'assertions. Cette section décrit les exigences pour gérer ces risques.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **6.8.1** | Vérifiez que, si l'application prend en charge plusieurs fournisseurs d'identité (IdP), l'identité de l'utilisateur ne peut pas être usurpée via un autre fournisseur d'identité pris en charge (par exemple, en utilisant le même identifiant utilisateur). La mesure standard consisterait à ce que l'application enregistre et identifie l'utilisateur à l'aide d'une combinaison de l'ID du fournisseur d'identité (servant d'espace de noms) et de l'ID de l'utilisateur dans le fournisseur d'identité. | 2 |
| **6.8.2** | Vérifiez que la présence et l'intégrité des signatures numériques sur les assertions d'authentification (par exemple sur les assertions JWT ou SAML) sont toujours validées, en rejetant toutes les assertions non signées ou ayant des signatures non valides. | 2 |
| **6.8.3** | Vérifiez que les assertions SAML sont traitées de manière unique et utilisées une seule fois au cours de la période de validité pour éviter les attaques par relecture. | 2 |
| **6.8.4** | Si une application utilise un fournisseur d'identité (IdP) distinct et attend une force, des méthodes ou une date d'authentification spécifiques pour des fonctions spécifiques, vérifiez que l'application les vérifie à l'aide des informations renvoyées par l'IdP. Par exemple, si OIDC est utilisé, cela peut être réalisé en validant les revendications de jeton d'identification telles que « acr », « amr » et « auth_time » (le cas échéant). Si l'IdP ne fournit pas ces informations, l'application doit disposer d'une approche de secours documentée qui suppose que le mécanisme d'authentification de force minimale a été utilisé (par exemple, une authentification à facteur unique avec nom d'utilisateur et mot de passe). | 2 |

## Références

Pour plus d'informations, voir également :

* [NIST SP 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST SP 800-63B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST SP 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Web Security Testing Guide: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/04-Authentication_Testing)
* [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Choosing and Using Security Questions Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
* [CISA Guidance on "Number Matching"](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
* [Details on the FIDO Alliance](https://fidoalliance.org/)
