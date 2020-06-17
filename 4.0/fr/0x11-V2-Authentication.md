# V2 : Exigences de vérification de l'authentification

## Objectif de contrôle

L'authentification est l'acte qui consiste à établir ou à confirmer qu'une personne (ou quelque chose) est authentique et que les affirmations faites par une personne ou au sujet d'un dispositif sont correctes, résistantes à l'usurpation d'identité et empêchent la récupération ou l'interception des mots de passe.

Lorsque l'ASVS a été publiée pour la première fois, le nom d'utilisateur + mot de passe était la forme d'authentification la plus courante en dehors des systèmes de haute sécurité. L'authentification à facteurs multiples (MFA) était communément acceptée dans les cercles de sécurité mais rarement requise ailleurs. Avec l'augmentation du nombre de brèches de mots de passe, l'idée que les noms d'utilisateur sont en quelque sorte confidentiels et les mots de passe inconnus, a rendu de nombreux contrôles de sécurité inefficaces. Par exemple, le NIST 800-63 considère les noms d'utilisateur et l'authentification basée sur la connaissance (KBA) comme des informations publiques, les notifications par SMS et par courrier électronique comme des [types d'authentificateurs "restreints"](https://pages.nist.gov/800-63-FAQ/#q-b1), et les mots de passe comme des préviolations. Cette réalité rend inutiles les authentificateurs basés sur la connaissance, la récupération de SMS et de courriels, l'historique des mots de passe, la complexité et les contrôles de rotation. Ces contrôles ont toujours été peu utiles, obligeant souvent les utilisateurs à trouver des mots de passe faibles tous les quelques mois, mais avec la publication de plus de 5 milliards de violations de noms d'utilisateur et de mots de passe, il est temps de passer à autre chose.

De toutes les sections de l'ASVS, ce sont les chapitres sur l'authentification et la gestion des sessions qui ont le plus changé. L'adoption de pratiques de pointe efficaces et fondées sur des preuves sera un défi pour beaucoup, et c'est tout à fait normal. Nous devons commencer dès maintenant la transition vers un avenir post-mot de passe.

## NIST 800-63 - Norme d'authentification moderne et fondée sur des preuves

[NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) est une norme moderne, basée sur des preuves, et représente le meilleur conseil disponible, indépendamment de son applicabilité. La norme est utile à toutes les organisations du monde entier, mais elle est particulièrement pertinente pour les agences américaines et celles qui traitent avec des agences américaines.

  La terminologie de la norme NIST 800-63 peut être un peu déroutante au début, surtout si vous n'êtes habitué qu'à l'authentification par nom d'utilisateur + mot de passe. Des progrès en matière d'authentification moderne sont nécessaires, nous devons donc introduire une terminologie qui deviendra courante à l'avenir, mais nous comprenons la difficulté de compréhension jusqu'à ce que l'industrie s'habitue à ces nouveaux termes. Nous avons fourni un glossaire à la fin de ce chapitre pour vous aider. Nous avons reformulé de nombreuses exigences afin de satisfaire l'intention, plutôt que sa forme. Par exemple, l'ASVS utilise le terme "mot de passe" alors que le NIST utilise "secret mémorisé" tout au long de cette norme.

L'authentification ASVS V2, la gestion de session V3 et, dans une moindre mesure, les contrôles d'accès V4 ont été adaptés pour constituer un sous-ensemble conforme de certains contrôles NIST 800-63b, axés sur les menaces communes et les faiblesses d'authentification couramment exploitées. Lorsque la conformité totale à la norme NIST 800-63 est requise, veuillez consulter la norme NIST 800-63.

### Sélection d'un niveau NIST AAL approprié

La norme de vérification de la sécurité des applications a tenté de faire correspondre les exigences ASVS L1 à celles du NIST AAL1, L2 à AAL2, et L3 à AAL3. Cependant, l'approche du niveau 1 ASVS en tant que contrôles "essentiels" n'est pas nécessairement le niveau AAL correct pour vérifier une application ou une API. Par exemple, si l'application est une application de niveau 3 ou a des exigences réglementaires pour être AAL3, le niveau 3 doit être choisi dans les sections V2 et V3 Gestion des sessions. Le choix du niveau d'affirmation d'authentification (AAL) conforme aux normes NIST doit être effectué conformément aux directives NIST 800-63b, comme indiqué dans la section *Selecting AAL* du [NIST 800-63b Section 6.2](https://pages.nist.gov/800-63-3/sp800-63-3.html#AAL_CYOA).

## Légende

Les applications peuvent toujours dépasser les exigences du niveau actuel, surtout si l'authentification moderne figure sur la feuille de route d'une application. Auparavant, l'ASVS exigeait une AMF obligatoire. Le NIST n'exige pas d'AMF obligatoire. C'est pourquoi nous avons utilisé une désignation optionnelle dans ce chapitre pour indiquer les cas où l'ASVS encourage mais n'exige pas de contrôle. Les clés suivantes sont utilisées tout au long de cette norme :

| Marque | Description |
| :---: | :---: |
| | Non requis |
| o | Recommandé, mais pas obligatoire |
| ✓ | Obligatoire |

## V2.1 Exigences en matière de sécurité des mots de passe

Les mots de passe, appelés "Memorized Secrets" par NIST 800-63, comprennent les mots de passe, les codes PIN, les motifs de déverrouillage, le choix du chaton correct ou d'un autre élément d'image, et les phrases de passe. Ils sont généralement considérés comme "quelque chose que vous savez" et sont souvent utilisés comme des authentificateurs à facteur unique. L'utilisation continue de l'authentification à un facteur unique pose des problèmes importants, notamment les milliards de noms d'utilisateur et de mots de passe valides divulgués sur l'internet, les mots de passe par défaut ou faibles, les tables arc-en-ciel et les dictionnaires ordonnés des mots de passe les plus courants.

Les applications devraient fortement encourager les utilisateurs à s'inscrire à l'authentification multifactorielle, et devraient permettre aux utilisateurs de réutiliser les jetons qu'ils possèdent déjà, tels que les jetons FIDO ou U2F, ou de se relier à un fournisseur de services d'accréditation qui fournit une authentification multifactorielle.

Les fournisseurs de services d'accréditation (CSP) fournissent une identité fédérée aux utilisateurs. Les utilisateurs auront souvent plus d'une identité avec plusieurs CSP, comme une identité d'entreprise utilisant Azure AD, Okta, Ping Identity ou Google, ou une identité de consommateur utilisant Facebook, Twitter, Google ou WeChat, pour ne citer que quelques alternatives courantes. Cette liste n'est pas une approbation de ces entreprises ou services, mais simplement un encouragement pour les développeurs à prendre en compte la réalité que de nombreux utilisateurs ont plusieurs identités établies. Les organisations devraient envisager de s'intégrer aux identités des utilisateurs existants, conformément au profil de risque de la force du CSP en matière de vérification d'identité. Par exemple, il est peu probable qu'une organisation gouvernementale accepte une identité de média social comme identifiant pour des systèmes sensibles, car il est facile de créer de fausses identités ou de jeter des identités, alors qu'une société de jeux pour mobiles pourrait bien avoir besoin de s'intégrer aux principales plateformes de médias sociaux pour accroître sa base de joueurs actifs.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.1.1** | Vérifiez que les mots de passe définis par l'utilisateur comportent au moins 12 caractères. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.2** | Vérifiez que les mots de passe de 64 caractères ou plus sont autorisés. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.3** | Vérifiez que le mot de passe n'est pas tronqué. Toutefois, des espaces multiples consécutifs peuvent être remplacés par un seul espace. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.4** | Vérifiez que tout caractère Unicode imprimable, y compris les caractères neutres comme les espaces et les Emojis, sont autorisés dans les mots de passe. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.5** | Vérifier que les utilisateurs peuvent changer leur mot de passe. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.6** | Vérifiez que la fonctionnalité de changement de mot de passe nécessite le mot de passe actuel et le nouveau mot de passe de l'utilisateur. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.7** | Vérifiez que les mots de passe soumis lors de l'enregistrement du compte, de la connexion et de la modification du mot de passe sont vérifiés par rapport à un ensemble de mots de passe non respectés, soit localement (comme les 1 000 ou 10 000 mots de passe les plus courants qui correspondent à la politique du système en matière de mots de passe), soit en utilisant une API externe. En cas d'utilisation d'une API, il convient d'utiliser un mécanisme de vérification de l'absence de connaissance ou un autre mécanisme pour s'assurer que le mot de passe en texte clair n'est pas envoyé ou utilisé pour vérifier l'état de violation du mot de passe. En cas de violation du mot de passe, l'application doit demander à l'utilisateur de définir un nouveau mot de passe non violé. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.8** | Vérifiez qu'un compteur de force de mot de passe est fourni pour aider les utilisateurs à définir un mot de passe plus fort. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.9** | Vérifiez qu'il n'existe pas de règles de composition des mots de passe limitant le type de caractères autorisés. Il ne doit pas y avoir restrictions sur l'utilisation de majuscules ou de minuscules, de chiffres ou de caractères spéciaux. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.10** | Vérifiez qu'il n'y a pas d'exigences en matière de rotation périodique du mots de passe ou d'historique des mots de passe. | ✓ | ✓ | ✓ | 263 | 5.1.1.2 |
| **2.1.11** | Vérifiez que la fonction "coller", les aides de mot de passe du navigateur et les gestionnaires de mots de passe externes sont autorisés. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.12** | Vérifiez que l'utilisateur peut choisir soit de visualiser temporairement la totalité du mot de passe masqué, soit de visualiser temporairement le dernier caractère tapé du mot de passe sur les plateformes qui n'ont pas cette fonctionnalité en natif. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |

Note : L'objectif de permettre à l'utilisateur de visualiser son mot de passe ou de voir temporairement le dernier caractère est d'améliorer la facilité d'utilisation de la saisie des données d'identification, notamment en ce qui concerne l'utilisation de mots de passe plus longs, de phrases de passe et de gestionnaires de mots de passe. Une autre raison d'inclure cette exigence est de dissuader ou d'empêcher les rapports de test exigeant inutilement des organisations de passer outre le comportement du champ de mot de passe de la plate-forme native pour supprimer cette expérience de sécurité moderne et conviviale.

## V2.2 Exigences générales relatives aux authentificateurs

L'agilité des authentificateurs est essentielle pour que les applications soient à l'épreuve du temps. Les vérificateurs d'applications Refactor permettent d'ajouter des authentificateurs supplémentaires en fonction des préférences de l'utilisateur, et de mettre à la retraite de manière ordonnée les authentificateurs obsolètes ou dangereux.

Le NIST considère le courrier électronique et les SMS comme des [types d'authentificateurs "restreints"](https://pages.nist.gov/800-63-FAQ/#q-b1), et il est probable qu'ils soient retirés du NIST 800-63 et donc de l'ASVS à un moment donné dans le futur. Les applications devraient prévoir une feuille de route qui ne nécessite pas l'utilisation du courrier électronique ou des SMS.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.2.1** | Vérifiez que les contrôles anti-automatisation sont efficaces pour atténuer les attaques par violation des tests d'accréditation, par énumération exhaustive (brute-force) et par verrouillage de compte. Ces contrôles comprennent le blocage des mots de passe les plus courants, les verrouillages progressifs, la limitation de débit, les CAPTCHA, les délais toujours plus longs entre les tentatives, les restrictions d'adresse IP ou les restrictions basées sur le risque telles que l'emplacement, la première connexion sur un appareil, les tentatives récentes de déverrouillage du compte, ou autres. Vérifiez qu'il n'y a pas plus de 100 tentatives infructueuses par heure sur un seul compte. | ✓ | ✓ | ✓ | 307 | 5.2.2 / 5.1.1.2 / 5.1.4.2 / 5.1.5.2 |
| **2.2.2** | Vérifier que l'utilisation d'authentificateurs faibles (tels que les SMS et les e-mails) se limite à la vérification secondaire et à l'approbation des transactions et ne remplace pas les méthodes d'authentification plus sûres. Vérifiez que les méthodes plus fortes sont proposées avant les méthodes faibles, que les utilisateurs sont conscients des risques, ou que des mesures appropriées sont en place pour limiter les risques de compromission du compte. | ✓ | ✓ | ✓ | 304 | 5.2.10 |
| **2.2.3** | Vérifier que des notifications sécurisées sont envoyées aux utilisateurs après la mise à jour des détails d'authentification, tels que la réinitialisation de l'identifiant, le changement d'adresse électronique ou d'adresse, la connexion à partir d'un lieu inconnu ou risqué. L'utilisation de notifications "push" - plutôt que de SMS ou d'e-mail - est préférable, mais en l'absence de notifications "push", les SMS ou les e-mails sont acceptables tant qu'aucune information sensible n'est divulguée dans la notification. | ✓ | ✓ | ✓ | 620 | |
| **2.2.4** | Vérifier la résistance à l'usurpation d'identité contre le phishing, comme l'utilisation de l'authentification multifactorielle, les dispositifs cryptographiques avec intention (comme les clés connectées avec un "push to authenticate"), ou à des niveaux AAL supérieurs, les certificats côté client. | | | ✓ | 308 | 5.2.5 |
| **2.2.5** | Vérifier que lorsqu'un fournisseur de services d'accréditation (CSP) et l'application vérifiant l'authentification sont séparés, un TLS mutuellement authentifié est en place entre les deux points terminaux. | | | ✓ | 319 | 5.2.6 |
| **2.2.6** | Vérifier la résistance au attaque de rejeu par l'utilisation obligatoire de dispositifs OTP, d'authentificateurs cryptographiques ou de codes de consultation. | | | ✓ | 308 | 5.2.8 |
| **2.2.7** | Vérifier l'intention d'authentification en exigeant l'entrée d'un jeton OTP ou une action initiée par l'utilisateur telle qu'une pression sur un bouton d'une clé matérielle FIDO. | | | ✓ | 308 | 5.2.9 |

## V2.3 Exigences relatives au cycle de vie des authentificateurs

Les authentificateurs sont les mots de passe, les jetons logiciels, les jetons matériels et les dispositifs biométriques. Le cycle de vie des authentificateurs est essentiel pour la sécurité d'une application - si quelqu'un peut s'enregistrer lui-même sur un compte sans preuve d'identité, il ne peut guère faire confiance à l'affirmation de son identité. Pour les sites de médias sociaux comme Reddit, c'est tout à fait normal. Pour les systèmes bancaires, il est essentiel de mettre davantage l'accent sur l'enregistrement et la délivrance de justificatifs d'identité et de dispositifs pour assurer la sécurité de l'application.

Remarque : les mots de passe ne doivent pas avoir une durée de vie maximale ni être soumis à une rotation. Les mots de passe doivent être vérifiés et non remplacés régulièrement.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.3.1** | Vérifier que les mots de passe ou codes d'activation initiaux générés par le système DOIVENT être générés de manière aléatoire et sécurisée, DOIVENT comporter au moins 6 caractères, PEUVENT contenir des lettres et des chiffres, et expirent après une courte période de temps. Ces secrets initiaux ne doivent pas être autorisés à devenir le mot de passe à long terme. | ✓ | ✓ | ✓ | 330 | 5.1.1.2 / A.3 |
| **2.3.2** | Vérifiez que l'inscription et l'utilisation de dispositifs d'authentification fournis par l'abonné sont prises en charge, comme les jetons U2F ou FIDO. | | ✓ | ✓ | 308 | 6.1.3 |
| **2.3.3** | Vérifier que les instructions de renouvellement sont envoyées suffisamment tôt pour renouveler les authentificateurs à durée déterminée. | | ✓ | ✓ | 287 | 6.1.4 |

## V2.4 Exigences en matière de stockage des identifiants

Les architectes et les développeurs doivent se conformer à cette section lorsqu'ils construisent ou remanient du code. Cette section ne peut être entièrement vérifiée qu'en utilisant la révision du code source ou par des tests unitaires ou d'intégration sécurisés. Les tests d'intrusions ne peuvent pas identifier l'un de ces problèmes.

La liste des fonctions de dérivation de clés à sens unique approuvées est détaillée dans la section 5.1.1.2 de la norme NIST 800-63 B, et dans [BSI Kryptographische Verfahren : Empfehlungen und Schlussell&auml;ngen (2018)](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile). Ces choix peuvent être remplacés par les derniers algorithmes nationaux ou régionaux et les dernières normes de longueur de clé.

Cette section ne peut pas être soumise à un test de pénétration, les contrôles ne sont donc pas marqués comme L1. Cependant, cette section est d'une importance vitale pour la sécurité des données d'identifications en cas de vol. Si vous bifurquez l'ASVS pour une directive sur l'architecture ou le codage ou une liste de contrôle pour l'examen du code source, veuillez replacer ces contrôles en L1 dans votre version privée.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.4.1** | Vérifiez que les mots de passe sont stockés sous une forme qui résiste aux attaques hors ligne. Les mots de passe DOIVENT être salés et hachés en utilisant une fonction approuvée à sens unique ou de hachage de mot de passe. Les fonctions de dérivation de clé et de hachage de mot de passe prennent un mot de passe, un sel et un facteur de coût (ex. : nombre d’itération algorithmique) comme intrants lors de la génération d'un hachage de mot de passe. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.2** | Vérifiez que le sel a une longueur d'au moins 32 bits et qu'il est choisi arbitrairement pour minimiser les collisions de la valeur du sel parmi les hashs stockés. Pour chaque authentifiant, une valeur de sel unique et le hachage qui en résulte DOIVENT être stockés. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.3** | Vérifiez que si le PBKDF2 est utilisé, le nombre d'itérations DOIT être aussi important que les performances du serveur de vérification le permettent, généralement au moins 100 000 itérations. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.4** | Vérifiez que si bcrypt est utilisé, le facteur de travail DOIT être aussi important que les performances du serveur de vérification le permettent, généralement au moins 13. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.5** | Vérifier qu'une itération supplémentaire d'une fonction de dérivation clé est effectuée, en utilisant une valeur de sel qui est secrète et connue uniquement du vérificateur. Générer la valeur de sel en utilisant un générateur de bits aléatoires approuvé [SP 800-90Ar1] et fournir au moins la sécurité minimale spécifiée dans la dernière révision de la norme SP 800-131A. La valeur de sel secrète DOIT être stockée séparément des mots de passe hachés (par exemple, dans un dispositif spécialisé comme un module de sécurité matériel). | | ✓ | ✓ | 916 | 5.1.1.2 |

Lorsque des normes américaines sont mentionnées, une norme régionale ou locale peut être utilisée à la place ou en plus de la norme américaine, selon les besoins.

## V2.5 Exigences en matière de récupération des identifiants

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.5.1** | Vérifiez que si un secret d'activation initiale ou de récupération du système est envoyé à l'utilisateur, il est à usage unique, limité dans le temps et aléatoire. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.2** | Vérifier que les indices de mot de passe ou l'authentification basée sur la connaissance (dites "questions secrètes") ne sont pas présents. | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.3** | Vérifiez que la récupération du mot de passe ne révèle en aucune façon le mot de passe actuel. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.4** | Vérifiez que les comptes partagés ou par défaut ne sont pas présents (par exemple "root", "admin" ou "sa"). | ✓ | ✓ | ✓ | 16 | 5.1.1.2 / A.3 |
| **2.5.5** | Vérifier que si un facteur d'authentification est modifié ou remplacé, l'utilisateur est informé de cet événement. | ✓ | ✓ | ✓ | 304 | 6.1.2.3 |
| **2.5.6** | Vérifier les mots de passe oubliés, et les autres chemins de récupération utilisent un mécanisme de récupération sécurisé, tel que TOTP ou autre soft token, mobile push, ou un autre mécanisme de récupération hors ligne. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.7** | Vérifier qu'en cas de perte des facteurs d'authentification OTP ou multi-facteurs, la preuve d'identité est effectuée au même niveau que lors de l'inscription. | | ✓ | ✓ | 308 | 6.1.2.3 |

## V2.6 Exigences relatives aux vérificateurs des secrets

Les tables d’authentifications secrètes sont des listes prégénérées de codes secrets, similaires aux numéros d'autorisation de transaction (TAN), aux codes de récupération des médias sociaux ou à une grille contenant un ensemble de valeurs aléatoires. Ils sont distribués aux utilisateurs en toute sécurité. Ces codes de recherche sont utilisés une fois, et une fois qu'ils sont tous utilisés, la liste secrète de recherche est jetée. Ce type d'authentificateur est considéré comme "quelque chose que vous avez".

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.6.1** | Vérifiez que les secrets de la table d’authentification ne peuvent être utilisés qu'une seule fois. | | ✓ | ✓ | 308 | 5.1.2.2 |
| **2.6.2** | Vérifiez que les secrets de la table d’authentification ont un caractère aléatoire suffisant (112 bits d'entropie) ou, s'ils ont moins de 112 bits d'entropie, qu'ils sont salés avec un sel unique et aléatoire de 32 bits et hachés avec un hachage unidirectionnel approuvé. | | ✓ | ✓ | 330 | 5.1.2.2 |
| **2.6.3** | Vérifiez que les secrets de la table d’authentification résistent aux attaques hors ligne, comme les valeurs prévisibles. | | ✓ | ✓ | 310 | 5.1.2.2 |

## V2.7 Exigences relatives aux vérificateurs hors bande

Dans le passé, un vérificateur hors bande courant aurait été un courriel ou un SMS contenant un lien de réinitialisation de mot de passe. Les attaquants utilisent ce faible mécanisme pour réinitialiser des comptes qu'ils ne contrôlent pas encore, par exemple en prenant le compte de courrier électronique d'une personne et en réutilisant tout lien de réinitialisation découvert. Il existe de meilleurs moyens de gérer la vérification hors bande.

Les authentificateurs hors bande sécurisés sont des dispositifs physiques qui peuvent communiquer avec le vérificateur par un canal secondaire sécurisé. Les notifications "push" vers les appareils mobiles en sont des exemples. Ce type d'authentificateur est considéré comme "quelque chose que vous avez". Lorsqu'un utilisateur souhaite s'authentifier, l'application de vérification envoie un message à l'authentificateur hors bande via une connexion à l'authentificateur directement ou indirectement par le biais d'un service tiers. Le message contient un code d'authentification (généralement un nombre aléatoire de six chiffres ou un dialogue d'approbation modale). L'application de vérification attend de recevoir le code d'authentification par le canal principal et compare le hachage de la valeur reçue au hachage du code d'authentification original. En cas de correspondance, le vérificateur hors bande peut supposer que l'utilisateur s'est authentifié.

L'ASVS suppose que seuls quelques développeurs développeront de nouveaux authentificateurs hors bande, tels que les notifications "push", et donc que les contrôles suivants de l'ASVS s'appliquent aux vérificateurs, tels que l'API d'authentification, les applications et les mises en œuvre de l'authentification unique. Si vous développez un nouvel authentificateur hors bande, veuillez vous référer à NIST 800-63B  5.1.3.1.

Les authentificateurs hors bande dangereux tels que le courrier électronique et la voix sur IP ne sont pas autorisés. Les authentifications PSTN et SMS sont actuellement "restreintes" par le NIST et devraient être interdites au profit des notifications "push" ou similaires. Si vous devez utiliser l'authentification hors bande par téléphone ou SMS, veuillez consulter  5.1.3.3.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.7.1** | Vérifiez que les authentificateurs de texte en clair hors bande (NIST "restreint"), tels que les SMS ou le PSTN, ne sont pas proposés par défaut, et que des alternatives plus fortes, telles que les notifications "push", sont proposées en premier lieu. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.2** | Vérifiez que le vérificateur hors bande expire les demandes d'authentification, les codes ou les jetons hors bande après 10 minutes. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.3** | Vérifiez que les demandes d'authentification, codes ou jetons hors bande du vérificateur ne sont utilisables qu'une seule fois, et uniquement pour la demande d'authentification originale. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.4** | Vérifier que l'authentificateur et le vérificateur hors bande communiquent sur un canal indépendant sécurisé. | ✓ | ✓ | ✓ | 523 | 5.1.3.2 |
| **2.7.5** | Vérifiez que le vérificateur hors bande ne conserve qu'une version hachée du code d'authentification. | | ✓ | ✓ | 256 | 5.1.3.2 |
| **2.7.6** | Vérifiez que le code d'authentification initial est généré par un générateur de nombres aléatoires sécurisé, contenant au moins 20 bits d'entropie (en général, un nombre aléatoire de six chiffres est suffisant). | | ✓ | ✓ | 310 | 5.1.3.2 |

## V2.8 Exigences relatives aux vérificateurs uniques à facteur unique ou à facteurs multiples

Les mots de passe à usage unique (OTP) sont des jetons physiques ou logiciels qui affichent un défi pseudo-aléatoire à usage unique en constante évolution. Ces dispositifs rendent le phishing (usurpation d'identité) difficile, mais pas impossible. Ce type d'authentifiant est considéré comme "quelque chose que vous avez". Les jetons multi-facteurs sont similaires aux OTP à facteur unique, mais nécessitent un code PIN valide, un déverrouillage biométrique, une insertion USB ou un appariement NFC ou une valeur supplémentaire (comme les calculatrices de signature de transaction) à saisir pour créer l'OTP final.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.8.1** | Vérifier que les OTP basées sur le temps ont une durée de vie définie avant d'expirer. | ✓ | ✓ | ✓ | 613 | 5.1.4.2 / 5.1.5.2 |
| **2.8.2** | Vérifier que les clés symétriques utilisées pour vérifier les OTP soumises sont hautement protégées, par exemple en utilisant un module de sécurité matériel ou un stockage de clés basé sur un système d'exploitation sécurisé. | | ✓ | ✓ | 320 | 5.1.4.2 / 5.1.5.2|
| **2.8.3** | Vérifier que des algorithmes cryptographiques approuvés sont utilisés dans la génération, dans la préparation et dans la vérification des OTP. | | ✓ | ✓ | 326 | 5.1.4.2 / 5.1.5.2 |
| **2.8.4** | Vérifiez que l'OTP basé sur le temps ne peut être utilisé qu'une seule fois pendant la période de validité. | | ✓ | ✓ | 287 | 5.1.4.2 / 5.1.5.2 |
| **2.8.5** | Vérifier que si un jeton OTP multi-facteur basé sur le temps est réutilisé pendant la période de validité, il est enregistré et rejeté avec des notifications sécurisées envoyées au détenteur du dispositif. | | ✓ | ✓ | 287 | 5.1.5.2 |
| **2.8.6** | Vérifier que le générateur OTP physique à facteur unique peut être révoqué en cas de vol ou autre perte. S'assurer que la révocation est immédiatement effective pour toutes les sessions connectées, quel que soit le lieu. | | ✓ | ✓ | 613 | 5.2.1 |
| **2.8.7** | Vérifiez que les authentificateurs biométriques sont limités à une utilisation en tant que facteurs secondaires en conjonction avec quelque chose que vous avez et quelque chose que vous connaissez. | | o | ✓ | 308 | 5.2.3 |

## V2.9 Exigences relatives aux vérificateurs de logiciels et d'appareils cryptographiques

Les clés de sécurité cryptographiques sont des cartes à puce ou des clés FIDO, où l'utilisateur doit brancher ou apparier le dispositif cryptographique à l'ordinateur pour compléter l'authentification. Les vérificateurs envoient un défi aux dispositifs ou logiciels cryptographiques, et le dispositif ou le logiciel calcule une réponse basée sur une clé cryptographique stockée en toute sécurité.

Les exigences relatives aux dispositifs et logiciels cryptographiques à facteur unique et aux dispositifs et logiciels cryptographiques à facteurs multiples sont les mêmes, car la vérification de l'authentificateur cryptographique prouve la possession du facteur d'authentification.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.9.1** | Vérifier que les clés cryptographiques utilisées dans la vérification sont stockées de manière sûre et protégées contre la divulgation, par exemple en utilisant un TPM ou un HSM, ou un service OS qui peut utiliser ce stockage sécurisé. | | ✓ | ✓ | 320 | 5.1.7.2 |
| **2.9.2** | Vérifiez que le nonce de défi est d'une longueur d'au moins 64 bits, et statistiquement unique ou non pendant la durée de vie du dispositif cryptographique. | | ✓ | ✓ | 330 | 5.1.7.2 |
| **2.9.3** | Vérifier que des algorithmes cryptographiques approuvés sont utilisés dans la génération, la préparation et la vérification. | | ✓ | ✓ | 327 | 5.1.7.2 |

## V2.10 Exigences d'authentification des services

Cette section n'est pas testable par tests d'intrusions, et n'a donc aucune exigence de L1. Toutefois, si elle est utilisée dans une architecture, un codage ou une révision de code sécurisé, veuillez supposer que le logiciel (tout comme le Java Key Store) est l'exigence minimale de la L1. Le stockage de secrets en texte clair n'est en aucun cas acceptable.

| # | Description | L1 | L2 | L3 | CWE | [NIST](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.10.1** | Vérifiez que les secrets d'intégration ne reposent pas sur des mots de passe immuables, tels que les clés API ou les comptes privilégiés partagés. | | OS assisté | HSM | 287 | 5.1.1.1 |
| **2.10.2** | Vérifiez que si des mots de passe sont requis, l'authentification ne soit pas avec un compte par défaut. | | OS assisté | HSM | 255 | 5.1.1.1 |
| **2.10.3** | Vérifiez que les mots de passe sont stockés avec une protection suffisante pour empêcher les attaques de récupération hors ligne, y compris l'accès au système local. | | Assistance du système d'exploitation | HSM | 522 | 5.1.1.1 |
| **2.10.4** | Vérifier que les mots de passe, les intégrations avec les bases de données et les systèmes tiers, les seeds et les secrets internes, ainsi que les clés API sont gérés de manière sécurisée et ne sont pas inclus dans le code source ou stockés dans des dépôts de code source. Ce type de stockage DEVRAIT résister aux attaques hors ligne. L'utilisation d'un stockage de clés logiciel sécurisé (L1), d'un module de plate-forme de confiance (TPM) ou d'un module de sécurité matériel (L3) est recommandée pour le stockage des mots de passe. | | OS assisté | HSM | 798 | |

## Exigences supplémentaires des agences américaines

Les agences américaines ont des exigences obligatoires concernant le NIST 800-63. La norme de vérification de la sécurité des applications a toujours été d'environ 80% des contrôles qui s'appliquent à près de 100% des applications, et non les derniers 20% des contrôles avancés ou ceux qui ont une applicabilité limitée. En tant que telle, l'ASVS est un sous-ensemble strict de la norme NIST 800-63, en particulier pour les classifications IAL1/2 et AAL1/2, mais elle n'est pas suffisamment complète, notamment en ce qui concerne les classifications IAL3/AAL3.

Nous demandons instamment aux agences gouvernementales américaines de revoir et de mettre en œuvre la norme NIST 800-63 dans son intégralité.

## Glossaire des termes

| Terme | Signification |
| -- | -- |
| CSP | Credential Service Provider également appelé fournisseur d'identité |
| Authenticator | Code qui authentifie un mot de passe, un jeton, un MFA, une affirmation fédérée, etc. |
| Vérificateur | "Entité qui vérifie l'identité du demandeur en vérifiant la possession et le contrôle par le demandeur d'un ou deux authentificateurs au moyen d'un protocole d'authentification. Pour ce faire, le vérificateur peut également avoir besoin de valider les références qui lient le ou les authentificateurs à l'identifiant de l'abonné et vérifier leur statut" |
| OTP | Mot de passe unique |
| SFA | Les authentificateurs à facteur unique, tels que quelque chose que vous connaissez (secrets mémorisés, mots de passe, phrases de passe, codes PIN), quelque chose que vous êtes (biométrie, empreintes digitales, scanners du visage), ou quelque chose que vous avez (jetons OTP, un dispositif cryptographique tel qu'une carte à puce), |
| MFA | Authentification multifactorielle, qui comprend deux ou plusieurs facteurs uniques |

## Références

Pour plus d'informations, voir aussi :

* [NIST 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST 800-63 A - Enrollment and Identity Proofing](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST 800-63 B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST 800-63 C - Federation and Assertions](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [OWASP Cheat Sheet - Password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Forgot password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Choosing and using security questions](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
