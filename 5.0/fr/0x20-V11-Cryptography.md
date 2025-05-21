# V11 Cryptographie

## Objectif du contrôle

L'objectif de ce chapitre est de définir les meilleures pratiques pour l'utilisation générale de la cryptographie, mais aussi d'inculquer une compréhension fondamentale des principes cryptographiques et d'encourager une évolution vers des approches plus résilientes et modernes. Il encourage les actions suivantes :

* Mise en œuvre de systèmes cryptographiques robustes, sécurisés, adaptables à l'évolution des menaces et pérennes.
* Utilisation de mécanismes cryptographiques sécurisés et conformes aux meilleures pratiques du secteur.
* Maintien d'un système de gestion des clés cryptographiques sécurisé, avec des contrôles d'accès et des audits appropriés.
* Évaluation régulière du paysage cryptographique pour identifier les nouveaux risques et adapter les algorithmes en conséquence.
* Identification et gestion des cas d'utilisation cryptographiques tout au long du cycle de vie de l'application afin de garantir la prise en compte et la sécurité de tous les actifs cryptographiques.

Outre les principes généraux et les bonnes pratiques, ce document fournit également des informations techniques plus détaillées sur les exigences de l'annexe V – Normes de cryptographie. Cela inclut les algorithmes et les modes considérés comme « approuvés » aux fins des exigences de ce chapitre.

Les exigences qui utilisent la cryptographie pour résoudre un problème distinct, comme la gestion des secrets ou la sécurité des communications, figureront dans différentes parties de la norme.

## V11.1 Inventaire et documentation cryptographiques

Les applications doivent être conçues avec une architecture cryptographique robuste afin de protéger les données conformément à leur classification. Chiffrer tout est un gaspillage, et ne rien chiffrer est une négligence juridique. Un équilibre doit être trouvé, généralement lors de la conception architecturale ou de haut niveau, des sprints de conception ou des pics d'architecture. Concevoir la cryptographie au fur et à mesure ou la moderniser coûtera inévitablement beaucoup plus cher à mettre en œuvre de manière sécurisée que de l'intégrer dès le départ.

Il est important de veiller à ce que tous les actifs cryptographiques soient régulièrement découverts, inventoriés et évalués. Veuillez consulter l'annexe pour plus d'informations sur la procédure à suivre.

Il est également crucial de pérenniser les systèmes cryptographiques face à l'essor futur de l'informatique quantique. La cryptographie post-quantique (PQC) désigne les algorithmes cryptographiques conçus pour résister aux attaques des ordinateurs quantiques, qui sont susceptibles de casser des algorithmes largement utilisés tels que RSA et la cryptographie à courbe elliptique (ECC).

Veuillez consulter l'annexe pour obtenir des conseils actualisés sur les primitives et les normes PQC approuvées.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.1.1** | Vérifiez qu’il existe une politique documentée pour la gestion des clés cryptographiques et un cycle de vie des clés cryptographiques qui suit une norme de gestion des clés telle que NIST SP 800-57.Cela devrait inclure la garantie que les clés ne sont pas trop partagées (par exemple, avec plus de deux entités pour les secrets partagés et plus d’une entité pour les clés privées). | 2 | v5.0.be-1.6.1 |
| **11.1.2** | Vérifiez qu'un inventaire cryptographique est réalisé, maintenu et régulièrement mis à jour, et qu'il inclut toutes les clés, algorithmes et certificats cryptographiques utilisés par l'application. Il doit également documenter les emplacements du système où les clés peuvent ou non être utilisées, ainsi que les types de données qui peuvent ou non être protégées par ces clés. | 2 | v5.0.be-1.6.4 |
| **11.1.3** | Vérifiez que les mécanismes de découverte cryptographique sont utilisés pour identifier toutes les instances de cryptographie dans le système, y compris les opérations de chiffrement, de hachage et de signature. | 3 | v5.0.be-1.6.5 |
| **11.1.4** | Vérifier la tenue d'un inventaire cryptographique. Celui-ci doit inclure un plan documenté décrivant la migration vers de nouvelles normes cryptographiques, telles que la cryptographie post-quantique, afin de réagir aux menaces futures. | 3 | v5.0.be-6.9.1 |

## V11.2 Mise en œuvre de la cryptographie sécurisée

Cette section définit les exigences relatives à la sélection, à la mise en œuvre et à la gestion continue des algorithmes cryptographiques de base d'une application. L'objectif est de garantir que seules des primitives cryptographiques robustes et reconnues par l'industrie soient déployées, conformément aux normes en vigueur (par exemple, NIST, ISO/IEC) et aux meilleures pratiques. Les organisations doivent s'assurer que chaque composant cryptographique est sélectionné sur la base de preuves validées par des pairs et de tests de sécurité pratiques.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.2.1** | Vérifiez que les implémentations validées par l’industrie (y compris les bibliothèques et les implémentations accélérées par le matériel) sont utilisées pour les opérations cryptographiques. | 2 | v5.0.be-6.2.2 |
| **11.2.2** | Vérifiez que l'application est conçue avec une agilité cryptographique, de sorte que les nombres aléatoires, le chiffrement authentifié, le MAC ou les algorithmes de hachage, les longueurs de clés, les tours, les chiffrements et les modes puissent être reconfigurés, mis à niveau ou échangés à tout moment, afin de se protéger contre les failles cryptographiques. De même, il doit être possible de remplacer les clés et les mots de passe, ainsi que de rechiffrer les données. Cela permettra des mises à niveau transparentes vers la cryptographie post-quantique (PQC), une fois que des implémentations hautement sécurisées de schémas ou de normes PQC approuvés seront largement disponibles. | 2 | v5.0.be-6.2.4 |
| **11.2.3** | Vérifiez que toutes les primitives cryptographiques utilisent un minimum de 128 bits de sécurité en fonction de l'algorithme, de la taille de la clé et de la configuration. Par exemple, une clé ECC de 256 bits offre environ 128 bits de sécurité, tandis que RSA nécessite une clé de 3072 bits pour atteindre 128 bits de sécurité. | 2 | v5.0.be-6.2.9 |
| **11.2.4** | Vérifiez que toutes les opérations cryptographiques sont à temps constant, sans opérations de « court-circuit » dans les comparaisons, les calculs ou les retours, pour éviter toute fuite d'informations. | 3 | v5.0.be-6.2.8 |
| **11.2.5** | Vérifiez que tous les modules cryptographiques échouent en toute sécurité et que les erreurs sont gérées de manière à ne pas permettre de vulnérabilités, telles que les attaques Padding Oracle. | 3 | v5.0.be-6.2.1 |

## V11.3 Algorithmes de chiffrement

Les algorithmes de cryptage authentifiés basés sur AES et CHACHA20 constituent l’épine dorsale de la pratique cryptographique moderne.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.3.1** | Vérifiez que les modes de bloc non sécurisés (par exemple, ECB) et les schémas de remplissage faibles (par exemple, PKCS#1 v1.5) ne sont pas utilisés. | 1 | v5.0.be-6.5.1 |
| **11.3.2** | Vérifiez que seuls les chiffrements et modes approuvés tels que AES avec GCM sont utilisés. | 1 | v5.0.be-6.5.2 |
| **11.3.3** | Vérifiez que les données chiffrées sont protégées contre toute modification non autorisée, de préférence en utilisant une méthode de chiffrement authentifiée approuvée ou en combinant une méthode de chiffrement approuvée avec un algorithme MAC approuvé. | 2 | v5.0.be-6.5.4 |
| **11.3.4** | Vérifiez que les nonces, les vecteurs d'initialisation et autres nombres à usage unique ne sont pas utilisés pour plus d'une paire clé de chiffrement/élément de données. La méthode de génération doit être adaptée à l'algorithme utilisé. | 3 | v5.0.be-6.5.3 |
| **11.3.5** | Vérifiez que toute combinaison d'un algorithme de chiffrement et d'un algorithme MAC fonctionne en mode chiffrement puis MAC. | 3 | v5.0.be-6.5.5 |

## V11.4 Hachage et fonctions basées sur le hachage

Les hachages cryptographiques sont utilisés dans une grande variété de protocoles cryptographiques, tels que les signatures numériques, HMAC, les fonctions de dérivation de clés (KDF), la génération de bits aléatoires et le stockage de mots de passe. La sécurité d'un système cryptographique dépend des fonctions de hachage sous-jacentes utilisées. Cette section décrit les exigences relatives à l'utilisation de fonctions de hachage sécurisées dans les opérations cryptographiques.

Pour le stockage des mots de passe, ainsi que pour l'annexe sur la cryptographie, la [OWASP Password Storage Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms) fournira également un contexte et des conseils utiles.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.4.1** | Vérifiez que seules les fonctions de hachage approuvées sont utilisées pour les cas d'utilisation cryptographiques généraux, notamment les signatures numériques, HMAC, KDF et la génération de bits aléatoires. Les fonctions de hachage non autorisées, telles que MD5, ne doivent pas être utilisées à des fins cryptographiques. | 1 | v5.0.be-6.6.1 |
| **11.4.2** | Vérifiez que les mots de passe sont stockés à l'aide d'une fonction de dérivation de clés approuvée et gourmande en ressources de calcul (également appelée « fonction de hachage de mots de passe »), dont les paramètres sont configurés conformément aux directives en vigueur. Ces paramètres doivent équilibrer sécurité et performances afin de rendre les attaques par force brute suffisamment difficiles pour le niveau de sécurité requis. | 2 | v5.0.be-6.6.2 |
| **11.4.3** | Vérifiez que les fonctions de hachage utilisées dans les signatures numériques, dans le cadre de l'authentification ou de l'intégrité des données, sont résistantes aux collisions et possèdent des longueurs de bits appropriées. Si la résistance aux collisions est requise, la longueur de sortie doit être d'au moins 256 bits. Si seule la résistance aux attaques de seconde pré-image est requise, la longueur de sortie doit être d'au moins 128 bits. | 2 | v5.0.be-6.6.3 |
| **11.4.4** | Vérifiez que l'application utilise des fonctions de dérivation de clés approuvées avec des paramètres d'extension de clés lors de la dérivation de clés secrètes à partir de mots de passe. Les paramètres utilisés doivent concilier sécurité et performances afin d'empêcher les attaques par force brute de compromettre la clé cryptographique obtenue. | 2 | v5.0.be-6.6.4 |

## V11.5 Valeurs aléatoires

La génération de nombres pseudo-aléatoires cryptographiquement sécurisée (CSPRNG) est extrêmement difficile à mettre en œuvre. En général, les bonnes sources d'entropie d'un système s'épuisent rapidement si elles sont surexploitées, tandis que des sources moins aléatoires peuvent conduire à des clés et des secrets prévisibles.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.5.1** | Vérifiez que tous les nombres et chaînes aléatoires destinés à être non devinables doivent être générés à l'aide d'un générateur de nombres pseudo-aléatoires cryptographiquement sécurisé (CSPRNG) et posséder au moins 128 bits d'entropie. Notez que les UUID ne respectent pas cette condition. | 2 | v5.0.be-6.3.1 |
| **11.5.2** | Vérifiez que le mécanisme de génération de nombres aléatoires utilisé est conçu pour fonctionner en toute sécurité, même en cas de forte demande. | 3 | v5.0.be-6.3.3 |

## V11.6 Cryptographie à clé publique

La cryptographie à clé publique sera utilisée lorsqu'il est impossible ou non souhaitable de partager une clé secrète entre plusieurs parties.

Dans ce contexte, des mécanismes d'échange de clés approuvés, tels que Diffie-Hellman et Elliptic Curve Diffie-Hellman (ECDH), sont nécessaires pour garantir la sécurité du cryptosystème face aux menaces modernes. Le chapitre « Communication sécurisée » décrit les exigences pour TLS. Les exigences de cette section sont donc destinées aux situations où la cryptographie à clé publique est utilisée dans des cas d'utilisation autres que TLS.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.6.1** | Vérifiez que seuls des algorithmes et modes opératoires cryptographiques approuvés sont utilisés pour la génération et l'amorçage des clés, ainsi que pour la génération et la vérification des signatures numériques. Les algorithmes de génération de clés ne doivent pas générer de clés non sécurisées, telles que les clés RSA, vulnérables à la factorisation de Fermat. | 2 | v5.0.be-6.7.2 |
| **11.6.2** | Vérifiez que des algorithmes cryptographiques approuvés sont utilisés pour l'échange de clés (tels que Diffie-Hellman), en veillant à ce que les mécanismes d'échange de clés utilisent des paramètres sécurisés. Cela permettra d'éviter les attaques contre le processus d'établissement des clés, susceptibles de conduire à des attaques de type « adversaire du milieu » ou à des failles cryptographiques. | 3 | v5.0.be-6.7.1 |

## V11.7 Cryptographie des données en cours d'utilisation

La protection des données pendant leur traitement est primordiale. Des techniques telles que le chiffrement intégral de la mémoire, le chiffrement des données en transit et la garantie d'un chiffrement des données le plus rapide possible après utilisation sont recommandées.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **11.7.1** | Vérifiez que le cryptage complet de la mémoire est utilisé pour protéger les données sensibles pendant leur utilisation, empêchant ainsi l'accès par des utilisateurs ou des processus non autorisés. | 3 | v5.0.be-6.8.1 |
| **11.7.2** | Vérifiez que la minimisation des données garantit que la quantité minimale de données est exposée pendant le traitement et assurez-vous que les données sont cryptées immédiatement après utilisation ou dès que possible. | 3 | v5.0.be-6.8.2 |

## Références

Pour plus d'informations, voir également :

* [OWASP Testing Guide 4.0: Testing for Weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/README.html)
* [OWASP Cheat Sheet: Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
