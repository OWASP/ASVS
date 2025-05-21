# Annexe V : Standards cryptographiques

Le chapitre « Cryptographie » va au-delà de la simple définition des bonnes pratiques. Il vise à améliorer la compréhension des principes de cryptographie et à encourager l'adoption de méthodes de sécurité plus résilientes et modernes. Cette annexe fournit des informations techniques détaillées sur chaque exigence, en complément des normes générales décrites dans le chapitre « Cryptographie ».

Cette annexe définit le niveau d'approbation des différents mécanismes cryptographiques :

* Les mécanismes *Approuvés* (A) peuvent être utilisés dans les applications.
* Les mécanismes *Hérités* (L) ne doivent pas être utilisés dans les applications, mais peuvent néanmoins être utilisés uniquement pour assurer la compatibilité avec les applications ou le code existants. Bien que l'utilisation de ces mécanismes ne soit pas actuellement considérée comme une vulnérabilité en soi, ils doivent être remplacés par des mécanismes plus sûrs et évolutifs dès que possible.
* Les mécanismes *Interdits* (D) ne doivent pas être utilisés car ils sont actuellement considérés comme défectueux ou n'offrent pas une sécurité suffisante.

Cette liste peut être modifiée dans le contexte d'une application donnée pour diverses raisons, notamment :

* nouvelles évolutions dans le domaine de la cryptographie ;
* conformité à la réglementation.

## Inventaire et documentation cryptographiques

Cette section fournit des informations complémentaires sur l'inventaire et la documentation cryptographiques V11.1.

Il est important de s'assurer que tous les actifs cryptographiques, tels que les algorithmes, les clés et les certificats, sont régulièrement découverts, inventoriés et évalués. Pour le niveau 3, cela devrait inclure l'utilisation d'analyses statiques et dynamiques pour découvrir l'utilisation de la cryptographie dans une application. Des outils tels que SAST et DAST peuvent être utiles, mais des outils dédiés pourraient être nécessaires pour une couverture plus complète. Voici quelques exemples d'outils gratuits :

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

## Forces équivalentes des paramètres cryptographiques

Les niveaux de sécurité relatifs des différents systèmes cryptographiques sont présentés dans ce tableau (extrait de [NIST SP 800-57 Partie 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), p.71) :

| Force de sécurité | Algorithmes à clés symétriques | Corps finis | Factorisation d'entiers | Courbe elliptique |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA   | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

Exemples d'applications :

* Cryptographie à corps finis : DSA, FFDH, MQV
* Cryptographie à factorisation entière : RSA
* Cryptographie à courbes elliptiques : ECDSA, EdDSA, ECDH, MQV

Remarque : cette section suppose qu'aucun ordinateur quantique n'existe ; si un tel ordinateur existait, les estimations des trois dernières colonnes ne seraient plus valides.

## Valeurs aléatoires

Cette section fournit des informations supplémentaires sur les valeurs aléatoires de la version 11.5.

| Nom | Version/Référence | Notes | Statut |
|:-:|:-:|:-:|:-:|
| `/dev/random` | Linux 4.8+ [(oct. 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3), également présent dans iOS, Android et d'autres systèmes d'exploitation POSIX basés sur Linux. Basé sur [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) | Utilise le flux ChaCha20. Trouvé dans iOS [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) et Android [`Secure Random`](https://developer.android.com/reference/java/security/SecureRandom) avec les paramètres corrects fournis pour chacun. | A |
| `/dev/urandom` | Fichier spécial du noyau Linux pour fournir des données aléatoires | Fournit des sources d'entropie de haute qualité à partir du caractère aléatoire matériel | A |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | Tel qu'utilisé dans les implémentations courantes, telles que [l'API Windows CNG `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) définie par [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers). | A |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2), disponible sous [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) et [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) | Fournit des octets aléatoires sécurisés directement depuis la source d'entropie du noyau, grâce à une API simple et minimale. Plus moderne, elle évite les pièges des anciennes API. | A |

La fonction de hachage sous-jacente utilisée avec HMAC-DRBG ou Hash-DRBG doit être approuvée pour cette utilisation.

## Algorithmes de chiffrement

Cette section fournit des informations supplémentaires sur les algorithmes de chiffrement V11.3.

Les algorithmes de chiffrement approuvés sont classés par ordre de préférence.

| Algorithmes à clé symétrique | Référence | Statut |
|--|--|--|
| AES-256 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | A |
| Salsa20 | [Salsa 20 specification](https://cr.yp.to/snuffle/spec.pdf) | A |
| XChaCha20 | [XChaCha20 Draft](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-xchacha-03) | A |
| XSalsa20 | [Extending the Salsa20 nonce](https://cr.yp.to/snuffle/xsalsa-20110204.pdf) | A |
| ChaCha20 | [RFC 8439](https://www.rfc-editor.org/info/rfc8439) | A |
| AES-192 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | A |
| AES-128 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | L |
| 2TDEA | | D |
| TDEA (3DES/3DEA) | | D |
| IDEA | | D |
| RC4 | | D |
| Blowfish| | D |
| ARC4 | | D |
| DES | | D |

### Modes de chiffrement AES

Les chiffrements modernes utilisent différents modes, notamment AES, à diverses fins. Nous décrivons ici les exigences relatives aux modes de chiffrement AES. Certains modes AES ne sont approuvés que pour le chiffrement par blocs au niveau du disque.

| Mode | Authentifié | Référence | Statut | Restriction |
|--|--|--|--|--|
| GCM | Yes | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A | |
| CCM | Yes | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A | |
| CBC | No | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | A | |
| XTS | No | [NIST SP 800-38E](https://csrc.nist.gov/pubs/sp/800/38/e/final) | A | Pour le chiffrement de bloc au niveau du disque uniquement. |
| XEX | No | [Rogaway 2004](https://doi.org/10.1007/978-3-540-30539-2_2) | A | Pour le chiffrement de bloc au niveau du disque uniquement. |
| LRW | No | [Liskov, Rivest, and Wagner 2005](https://doi.org/10.1007/s00145-010-9073-y) | A | Pour le chiffrement de bloc au niveau du disque uniquement. |
| ECB | No | | D | |
| CFB | No | | D | |
| OFB | No | | D | |
| CTR | No | | D | |
| CCM-8 | Yes | | D | |

Les modes approuvés sont classés par ordre de préférence.

Remarques :

* Tous les messages chiffrés doivent être authentifiés. Par conséquent, toute utilisation du mode CBC nécessite une fonction de hachage ou un MAC associé pour valider le message. En général, cette fonction doit être appliquée à la méthode « Chiffrer puis hacher » (mais TLS 1.2 utilise plutôt la méthode « Hash-Then-Encrypt »). Si cela ne peut être garanti, le CBC NE DOIT PAS être utilisé.
* Lors de l'utilisation de CCM-8, la balise MAC ne dispose que de 64 bits de sécurité. Ceci n'est pas conforme à l'exigence 6.2.9 qui exige au moins 128 bits de sécurité.

### Enveloppement de clé

L'encapsulation (et le déchiffrement) d'une clé cryptographique est une méthode de protection d'une clé existante par encapsulation (c'est-à-dire par encapsulation) grâce à un mécanisme de chiffrement supplémentaire, afin que la clé d'origine ne soit pas exposée de manière visible, par exemple lors d'un transfert. Cette clé supplémentaire, utilisée pour protéger la clé d'origine, est appelée clé d'encapsulation.

Cette opération peut être effectuée lorsqu'il est souhaitable de protéger des clés dans des emplacements jugés non fiables, ou d'envoyer des clés sensibles sur des réseaux non fiables ou au sein d'applications.

Cependant, il est important de bien comprendre la nature (par exemple, l'identité et la finalité) de la clé d'origine avant de s'engager dans une procédure d'encapsulation/déchiffrement, car cela peut avoir des répercussions sur les systèmes/applications sources et cibles en termes de sécurité, et notamment de conformité, ce qui peut inclure des pistes d'audit de la fonction d'une clé (par exemple, la signature) ainsi qu'un stockage approprié des clés.

Plus précisément, AES-256 doit être utilisé pour l'encapsulation des clés, conformément à la norme NIST SP 800-38F (https://csrc.nist.gov/pubs/sp/800/38/f/final) et en tenant compte des dispositions prospectives contre la menace quantique. Les modes de chiffrement utilisant AES sont les suivants, par ordre de préférence :

| Enveloppement de clé | Référence | Statut |
|--|--|--|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |

AES-192 et AES-128 PEUVENT être utilisés si le cas d'utilisation l'exige, mais leur motivation DOIT être documentée dans l'inventaire cryptographique de l'entité.

### Chiffrement authentifié

À l'exception du chiffrement du disque, les données chiffrées doivent être protégées contre toute modification non autorisée à l'aide d'un schéma de chiffrement authentifié (AE), généralement un schéma de chiffrement authentifié avec données associées (AEAD).

L'application doit de préférence utiliser un schéma AEAD approuvé. Elle peut également combiner un schéma de chiffrement approuvé et un algorithme MAC approuvé avec une construction « Chiffrer puis MAC ».

La méthode « MAC puis chiffrer » est toujours autorisée pour des raisons de compatibilité avec les applications existantes. Elle est utilisée dans TLS v1.2 avec les anciennes suites de chiffrement.

| Mécanisme AEAD | Référence | Statut |
|--------------------------|---------|-----|
|AES-GCM | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A |
|AES-CCM  | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A |
|ChaCha-Poly1305 | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539) | A |
|Encrypt-then-MAC | | A |
|MAC-then-encrypt | | L -

## Fonctions de hachage

Cette section fournit des informations supplémentaires sur le hachage V11.4 et les fonctions basées sur le hachage.

### Fonctions de hachage pour les cas d'utilisation généraux

Le tableau suivant répertorie les fonctions de hachage approuvées pour les cas d'utilisation cryptographiques généraux, tels que les signatures numériques :

* Les fonctions de hachage approuvées offrent une forte résistance aux collisions et conviennent aux applications de haute sécurité.
* Certains de ces algorithmes offrent une forte résistance aux attaques lorsqu'ils sont utilisés avec une gestion appropriée des clés cryptographiques. Ils sont donc également approuvés pour les fonctions HMAC, KDF et RBG.
* Les fonctions de hachage dont le résultat est inférieur à 254 bits présentent une résistance aux collisions insuffisante et ne doivent pas être utilisées pour la signature numérique ou d'autres applications nécessitant une résistance aux collisions. Pour d'autres utilisations, elles peuvent être utilisées à des fins de compatibilité et de vérification UNIQUEMENT avec les systèmes existants, mais ne doivent pas être utilisées dans les nouvelles conceptions.

| Fonction de hachage | Référence | Statut | Restrictions |
| -------------- | ------------------------------------------------------------- |--|--|
| SHA3-512 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-512 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA3-384 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-384 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA3-256 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-512/256 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA-256 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHAKE256 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| BLAKE2s | [BLAKE2: simpler, smaller, fast as MD5](https://eprint.iacr.org/2013/322) | A | |
| BLAKE2b | [BLAKE2: simpler, smaller, fast as MD5](https://eprint.iacr.org/2013/322) | A | |
| BLAKE3 | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf) | A | |
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Ne convient pas aux signatures numériques HMAC, KDF, RBG |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Ne convient pas aux signatures numériques HMAC, KDF, RBG |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | L | Ne convient pas aux signatures numériques HMAC, KDF, RBG |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L | Ne convient pas aux signatures numériques HMAC, KDF, RBG |
| CRC (any length) |  | D |  |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) | D | |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D | |

### Fonctions de hachage pour le stockage des mots de passe

Pour un hachage sécurisé des mots de passe, des fonctions de hachage dédiées doivent être utilisées. Ces algorithmes de hachage lent atténuent les attaques par force brute et par dictionnaire en augmentant la difficulté de calcul du craquage des mots de passe.

| KDF | Référence | Paramètres requis | Statut |
| --- | --------- | ------------------- | ------ |
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1<br>t = 2: m ≥ 19456 (19 MiB), p = 1<br>t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A |
| scrypt | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8<br>p = 2: N ≥ 2^16 (64 MiB), r = 8<br>p ≥ 3: N ≥ 2^15 (32 MiB), r = 8 | A |
| bcrypt | [A Future-Adaptable Password Scheme](https://www.researchgate.net/publication/2519476_A_Future-Adaptable_Password_Scheme) | cost ≥ 10 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterations ≥ 1,300,000 | L |

Les fonctions de dérivation de clés basées sur des mots de passe approuvées peuvent être utilisées pour le stockage des mots de passe.

## Mécanismes d'échange de clés

Cette section fournit des informations complémentaires sur la cryptographie à clé publique V11.6.

### KEX Schemes

Une force de sécurité de 112 bits ou plus DOIT être garantie pour tous les schémas d'échange de clés, et leur mise en œuvre DOIT suivre les choix de paramètres dans le tableau suivant.

| Schéma | Paramètres du domaine | Confidentialité persistante | Statut |
|--|--|--|--|
| Diffie-Hellman à corps finis (FFDH) | L >= 3072 & N >= 256 | Oui | A |
| Courbe elliptique Diffie-Hellman (ECDH) | f >= 256-383 | Oui | A |
| Transport de clés cryptées avec RSA-PKCS#1 v1.5 | k >= 3072 | Non | L |

Où les paramètres suivants sont :

* k est la taille de la clé RSA.
* L est la taille de la clé publique et N est la taille de la clé privée pour la cryptographie à corps finis.
* f est la plage de tailles de clés pour ECC.

Toute nouvelle implémentation NE DOIT PAS utiliser de schéma non conforme aux normes [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) et [B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) et [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final). Plus précisément, IKEv1 NE DOIT PAS être utilisé en production.

### Groupes Diffie-Hellman

Les groupes suivants sont approuvés et DOIVENT être utilisés pour les implémentations de Diffie-Hellman KEX. Les groupes IKEv2 sont fournis à titre de référence ([NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final)). Des groupes équivalents peuvent être utilisés dans d'autres protocoles. Cette liste est classée par ordre décroissant de sécurité. Les niveaux de sécurité sont décrits dans [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final), l'annexe D et [NIST SP 800-57 Partie 1 Rév. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Groupe | Schéma | Paramètres | Bits de sécurité | Statut |
|--|--|--|--|--|
| 21 | ECC | groupe ECP aléatoire 521-bit | 260 | A |
| 32 | ECC | Curve448 | 224 | A |
| 18 | MODP | Groupe MODP 8192-bit | 192 < 200 | A |
| 20 | ECC | groupe ECP aléatoire 384-bit | 192 | A |
| 17 | MODP | Groupe MODP 6144-bit | 128 < 176 | A |
| 16 | MODP | Groupe MODP 4096-bit | 128 < 152 | A |
| 31 | ECC | Curve25519 | 128 | A |
| 19 | ECC | groupe ECP aléatoire 256-bit | 128 | A |
| 15 | MODP | Groupe MODP 3072-bit | 128 | A |
| 14 | MODP | Groupe MODP 2048-bit | 112 | A |

## Codes d'authentification des messages (MAC)

Les codes d'authentification de message (MAC) sont des structures cryptographiques permettant de vérifier l'intégrité et l'authenticité d'un message. Un MAC prend en entrée un message et une clé secrète et génère une étiquette de taille fixe (la valeur MAC). Les MAC sont largement utilisés dans les protocoles de communication sécurisés (par exemple, TLS/SSL) pour garantir l'authenticité et l'intégrité des messages échangés entre les parties.

| Algorithme MAC | Référence | Statut | Restrictions |
| --------------| ----------------------------------------------------------------------------------------- | -------| ------------ |
| HMAC-SHA-256  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A | |
| HMAC-SHA-384  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A | |
| HMAC-SHA-512  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A | |
| KMAC128       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A | |
| KMAC256       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A | |
| BLAKE3        | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf)  | A | |
| AES-CMAC      | [RFC 4493](https://datatracker.ietf.org/doc/html/rfc4493) et [NIST SP 800-38B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf) | A | |
| AES-GMAC      | [NIST SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)            | A | |
| Poly1305-AES  | [The Poly1305-AES message-authentication code](https://cr.yp.to/mac/poly1305-20050329.pdf)                  | A | |
| HMAC-SHA-1    | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | L | |
| HMAC-MD5      | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                | D      | |

## Signatures numériques

Les schémas de signature DOIVENT utiliser des tailles de clés et des paramètres approuvés conformément à la norme [NIST SP 800-57 Partie 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Algorithme de signature        | Référence                                                  | Statut |
| ------------------------------ | ---------------------------------------------------------- | ------ |
| EdDSA (Ed25519, Ed448)         | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)        | A      |
| XEdDSA (Curve25519, Curve448)  | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)   | A      |
| ECDSA (P-256, P-384, P-521)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)  | A      |
| RSA-RSSA-PSS                   | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | A      |
| RSA-SSA-PKCS#1 v1.5            | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | D      |
| DSA (n'importe quelle taille de clé)             | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)  | D      |

## Normes de chiffrement post-quantique

Les implémentations PQC doivent être conformes à la norme [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd)/[204](https://csrc.nist.gov/pubs/fips/204/ipd)/[205](https://csrc.nist.gov/pubs/fips/205/ipd), car il existe encore un code renforcé minimal et une référence d'implémentation minimale. https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards

Les groupes d'échange de clés TLS hybrides proposés qui sont spécifiés dans [draft-tls-westerbaan-xyber768x00-03](https://www.ietf.org/archive/id/draft-tls-westerbaan-xyber768d00-03.txt) et pris en charge par les principaux navigateurs tels que [Firefox version 132](https://www.ietf.org/archive/id/draft-tls-westerbaan-xyber768d00-03.txt) et [Chrome version 131](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html) PEUVENT être utilisés dans des environnements de test cryptographique et/ou lorsqu'ils sont disponibles dans des bibliothèques approuvées par l'industrie ou le gouvernement.
