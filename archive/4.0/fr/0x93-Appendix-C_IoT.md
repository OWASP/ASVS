# Annexe C : Exigences de vérification de l'Internet des objets

Cette section était à l'origine dans la branche principale, mais avec le travail effectué par l'équipe IoT OWASP, il n'est pas logique de maintenir deux fils de discussion différents sur le sujet. Pour la version 4.0, nous la déplaçons vers l'annexe, et nous invitons tous ceux qui le souhaitent à utiliser plutôt la branche principale [OWASP IoT project](https://owasp.org/www-project-internet-of-things/)

## Objectif de contrôle

Les dispositifs embarqués/implantés devraient :

* Avoir le même niveau de contrôle de sécurité dans le dispositif que dans le serveur, en appliquant les contrôles de sécurité dans un environnement de confiance.
* Les données sensibles stockées sur l'appareil doivent l'être de manière sécurisée en utilisant un stockage sauvegardé par du matériel tel que des éléments sécurisés.
* Toutes les données sensibles transmises par le dispositif doivent utiliser la couche de transport de sécurité.

## Exigences de vérification de la sécurité

| # | Description | L1 | L2 | L3 | Depuis
| :---: | :--- | :---: | :---: | :---: | :---: |
| **C.1** | Vérifiez que les interfaces de débogage de la couche application telles que les interfaces USB, UART et autres variantes série sont désactivées ou protégées par un mot de passe complexe. | ✓ | ✓ | ✓ | 4.0 |
| **C.2** | Vérifier que les clés et certificats cryptographiques sont uniques à chaque appareil. | ✓ | ✓ | ✓ | 4.0 |
| **C.3** | Vérifiez que les contrôles de protection de la mémoire tels que ASLR et DEP sont activés par le système d'exploitation embarqué/OT, le cas échéant. | ✓ | ✓ | ✓ | 4.0 |
| **C.4** | Vérifiez que les interfaces de débogage sur puce telles que JTAG ou SWD sont désactivées ou que le mécanisme de protection disponible est activé et configuré de manière appropriée. | ✓ | ✓ | ✓ | 4.0 |
| **C.5** | Vérifiez que l'exécution de confiance est mise en œuvre et activée, si elle est disponible sur le SoC ou le CPU de l'appareil. | ✓ | ✓ | ✓ | 4.0 |
| **C.6** | Vérifier que les données sensibles, les clés privées et les certificats sont stockés de manière sécurisée dans un élément sécurisé, TPM, TEE (Trusted Execution Environment), ou protégés par une cryptographie forte. | ✓ | ✓ | ✓ | 4.0 |
| **C.7** | Vérifiez que les applications du microprogramme protègent les données en transit en utilisant la sécurité de la couche transport. | ✓ | ✓ | ✓ | 4.0 |
| **C.8** | Vérifiez que les applications du microprogramme valident la signature numérique des connexions au serveur. | ✓ | ✓ | ✓ | 4.0 |
| **C.9** | Vérifiez que les communications sans fil sont mutuellement authentifiées. | ✓ | ✓ | ✓ | 4.0 |
| **C.10** | Vérifiez que les communications sans fil sont envoyées sur un canal crypté.  | ✓ | ✓ | ✓ | 4.0 |
| **C.11** | Vérifier que toute utilisation de fonctions C interdites est remplacée par les fonctions équivalentes sûres appropriées. | ✓ | ✓ | ✓ | 4.0 |
| **C.12** | Vérifiez que chaque microprogramme tient à jour une nomenclature des logiciels cataloguant les composants tiers, le versionnage et les vulnérabilités publiées. | ✓ | ✓ | ✓ | 4.0 |
| **C.13** | Vérifier que tous les codes, y compris les binaires de tiers, les bibliothèques, les cadres sont examinés pour les références codées en dur (backdoors). | ✓ | ✓ | ✓ | 4.0 |
| **C.14** | Vérifiez que les composants de l'application et du micrologiciel ne sont pas susceptibles de recevoir l'OS Command Injection en invoquant des enveloppes de commandes shell, des scripts, ou que les contrôles de sécurité empêchent l'OS Command Injection. | ✓ | ✓ | ✓ | 4.0 |
| **C.15** | Vérifiez que les applications du microprogramme fixent la signature numérique à un ou plusieurs serveurs de confiance. | | ✓ | ✓ | 4.0 |
| **C.16** | Vérifier la présence de dispositifs de résistance et/ou de détection de l'altération. | | ✓ | ✓ | 4.0 |
| **C.17** | Vérifiez que toutes les technologies de protection de la propriété intellectuelle disponibles fournies par le fabricant de la puce sont activées. | | ✓ | ✓ | 4.0 |
| **C.18** | Vérifiez que des contrôles de sécurité sont en place pour empêcher l'ingénierie inverse des microprogrammes (par exemple, suppression des symboles de débogage verbeux). | | ✓ | ✓ | 4.0 |
| **C.19** | Vérifiez que le périphérique valide la signature de l'image de démarrage avant le chargement. | | ✓ | ✓ | 4.0 |
| **C.20** | Vérifiez que le processus de mise à jour du microprogramme n'est pas vulnérable aux attaques par heure de contrôle ou par heure d'utilisation. | | ✓ | ✓ | 4.0 |
| **C.21** | Vérifiez que l'appareil utilise la signature de code et valide les fichiers de mise à jour du micrologiciel avant l'installation. | | ✓ | ✓ | 4.0 |
| **C.22** | Vérifiez que l'appareil ne peut pas être rétrogradé vers d'anciennes versions (anti-rollback) de firmware valide. | | ✓ | ✓ | 4.0 |
| **C.23** | Vérifier l'utilisation d'un générateur de nombres pseudo-aléatoires cryptographiquement sécurisé sur un dispositif intégré (par exemple, en utilisant des générateurs de nombres aléatoires fournis par des puces). | | ✓ | ✓ | 4.0 |
| **C.24** | Vérifiez que le microprogramme peut effectuer des mises à jour automatiques selon un calendrier prédéfini. | | ✓ | ✓ | 4.0 |
| **C.25** | Vérifiez que l'appareil efface le micrologiciel et les données sensibles dès la détection d'une altération ou la réception d'un message non valide. | | | ✓ | 4.0 |
| **C.26** | Vérifiez que seuls les microcontrôleurs qui prennent en charge la désactivation des interfaces de débogage (par exemple JTAG, SWD) sont utilisés. | | | ✓ | 4.0 |
| **C.27** | Vérifiez que seuls les microcontrôleurs qui offrent une protection substantielle contre le décapuchonnage et les attaques des canaux latéraux sont utilisés. | | | ✓ | 4.0 |
| **C.28** | Vérifier que les traces sensibles ne sont pas exposées aux couches extérieures du circuit imprimé. | | | ✓ | 4.0 |
| **C.29** | Vérifiez que la communication entre les puces est cryptée (par exemple, communication de carte principale à carte fille). | | | ✓ | 4.0 |
| **C.30** | Vérifiez que l'appareil utilise la signature de code et valide le code avant l'exécution. | | | ✓ | 4.0 |
| **C.31** | Vérifiez que les informations sensibles conservées en mémoire sont écrasées par des zéros dès qu'elles ne sont plus nécessaires. | | | ✓ | 4.0 |
| **C.32** | Vérifiez que les applications de microprogrammes utilisent des conteneurs de noyau pour l'isolation entre les applications. | | | ✓ | 4.0 |
| **C.33** | Vérifiez que les drapeaux de compilateurs sécurisés tels que -fPIE, -fstack-protector-all, -Wl,-z,noexecstack, -Wl,-z,noexecheap sont configurés pour les constructions de microprogrammes. | | | ✓ | 4.0 |
| **C.34** | Vérifiez que les microcontrôleurs sont configurés avec une protection par code (le cas échéant). | | | ✓ | 4.0 |

## Références

Pour plus d'informations, voir aussi :

* [OWASP Internet of Things Top 10](https://owasp.org/www-pdf-archive/OWASP-IoT-Top-10-2018-final.pdf)
* [OWASP Embedded Application Security Project](https://owasp.org/www-project-embedded-application-security/)
* [OWASP Internet of Things Project](https://owasp.org/www-project-internet-of-things/)
* [Trudy TCP Proxy Tool](https://github.com/praetorian-inc/trudy)
