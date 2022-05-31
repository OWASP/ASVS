# V10 : Exigences de vérification des codes malveillants

## Objectif de contrôle

Assurez-vous que le code satisfait aux exigences de haut niveau suivantes :

* L'activité malveillante est traitée de manière sûre et appropriée pour ne pas affecter le reste de l'application.
* Il n'y a pas de bombes à retardement ou d'autres attaques basées sur le temps.
* Ne pas "téléphoner à la maison" vers des destinations malveillantes ou non autorisées.
* Il n'y a pas de portes dérobées, d'oeufs de Pâques, d'attaques au salami, de rootkits ou de code non autorisé pouvant être contrôlé par un attaquant.

Trouver un code malveillant est une preuve du négatif, qu'il est impossible de valider complètement. Il convient de tout mettre en œuvre pour s'assurer que le code ne comporte pas de code malveillant inhérent ou de fonctionnalité indésirable.

## V10.1 Contrôles de l'intégrité du code

La meilleure défense contre les codes malveillants est de "faire confiance, mais vérifier". L'introduction d'un code non autorisé ou malveillant dans un code est souvent une infraction pénale dans de nombreuses juridictions. Les politiques et les procédures doivent clairement définir les sanctions applicables aux codes malveillants.

Les principaux développeurs doivent régulièrement examiner les vérifications de code, en particulier celles qui peuvent concerner le temps d'accès, les E/S ou les fonctions réseau.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **10.1.1** | Vérifiez qu'un outil d'analyse de code est utilisé pour détecter les codes potentiellement malveillants, tels que les fonctions temporelles, les opérations de fichiers et les connexions réseau non sécurisées. | | | ✓ | 749 |

## V10.2 Recherche de code malveillant

Les codes malveillants sont extrêmement rares et difficiles à détecter. L'examen manuel ligne par ligne du code peut aider à rechercher des bombes logiques, mais même le plus expérimenté des examinateurs de code aura du mal à trouver un code malveillant même s'il sait qu'il existe.

Il n'est pas possible de se conformer à cette section sans un accès complet au code source, y compris aux bibliothèques de tiers.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **10.2.1** | Vérifiez que le code source de l'application et les bibliothèques tierces ne contiennent pas de "téléphone à la maison" ou de capacités de collecte de données non autorisées. Lorsque de telles fonctionnalités existent, obtenez l'autorisation de l'utilisateur pour leur fonctionnement avant de collecter des données. | | ✓ | ✓ | 359 |
| **10.2.2** | Vérifiez que l'application ne demande pas d'autorisations inutiles ou excessives pour les caractéristiques ou capteurs liés à la vie privée, tels que les contacts, les caméras, les microphones ou l'emplacement. | | ✓ | ✓ | 272 |
| **10.2.3** | Vérifiez que le code source de l'application et les bibliothèques tierces ne contiennent pas de portes dérobées, telles que des comptes ou des clés codées en dur ou supplémentaires non documentées, des obscurcissements de code, des blobs binaires non documentés, des rootkits, ou des fonctions de débogage anti-débogage, non sécurisées, ou encore des fonctionnalités obsolètes, non sécurisées ou cachées qui pourraient être utilisées de manière malveillante si elles étaient découvertes. | | | ✓ | 507 |
| **10.2.4** | Vérifiez que le code source de l'application et les bibliothèques tierces ne contiennent pas de bombes à retardement en recherchant les fonctions liées à la date et à l'heure. | | | ✓ | 511 |
| **10.2.5** | Vérifiez que le code source de l'application et les bibliothèques tierces ne contiennent pas de code malveillant, tel que des attaques de type salami, des contournements logiques ou des bombes logiques. | | | ✓ | 511 |
| **10.2.6** | Vérifiez que le code source de l'application et les bibliothèques tierces ne contiennent pas d'œufs de Pâques ou toute autre fonctionnalité potentiellement indésirable. | | | ✓ | 507 |

## V10.3 Contrôles d'intégrité des applications déployées

Une fois qu'une application est déployée, un code malveillant peut encore être inséré. Les applications doivent se protéger contre les attaques courantes, telles que l'exécution de code non signé provenant de sources non fiables et les rachats de sous-domaines.

La conformité à cette section est susceptible d'être opérationnelle et continue.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **10.3.1** | Vérifiez que si l'application dispose d'une fonction de mise à jour automatique du client ou du serveur, les mises à jour doivent être obtenues par des canaux sécurisés et signées numériquement. Le code de mise à jour doit valider la signature numérique de la mise à jour avant l'installation ou l'exécution de la mise à jour. | ✓ | ✓ | ✓ | 16 |
| **10.3.2** | Vérifiez que l'application utilise des protections d'intégrité, telles que la signature de code ou l'intégrité des sous-ressources. L'application ne doit pas charger ou exécuter du code provenant de sources non fiables, comme des includes de chargement, des modules, des plugins, du code ou des bibliothèques provenant de sources non fiables ou de l'Internet. | ✓ | ✓ | ✓ | 353 |
| **10.3.3** | Vérifiez que l'application est protégée contre les reprises de sous-domaines si elle repose sur des entrées DNS ou des sous-domaines DNS, tels que des noms de domaine expirés, des pointeurs DNS ou CNAME obsolètes, des projets expirés dans des dépôts de code source publics, ou des API de nuages transitoires, des fonctions sans serveur, ou des espaces de stockage (*autogen-bucket-id*.cloud.example.com) ou similaires. Les protections peuvent consister à s'assurer que les noms DNS utilisés par les applications sont régulièrement vérifiés pour détecter toute expiration ou modification. | ✓ | ✓ | ✓ | 350 |

## Références

* [Hostile Subdomain Takeover, Detectify Labs](https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/)
* [Hijacking of abandoned subdomains part 2, Detectify Labs](https://labs.detectify.com/2014/12/08/hijacking-of-abandoned-subdomains-part-2/)
