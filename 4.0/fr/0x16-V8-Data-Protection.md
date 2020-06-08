# V8 : Exigences de vérification de la protection des données

## Objectif de contrôle

Il y a trois éléments clés pour une bonne protection des données : Confidentialité, intégrité et disponibilité (CIA). Cette norme suppose que la protection des données est appliquée sur un système fiable, tel qu'un serveur, qui a été renforcé et dispose de protections suffisantes.

Les applications doivent supposer que tous les dispositifs des utilisateurs sont compromis d'une manière ou d'une autre. Lorsqu'une application transmet ou stocke des informations sensibles sur des dispositifs non sécurisés, tels que des ordinateurs, des téléphones et des tablettes partagés, l'application est chargée de s'assurer que les données stockées sur ces dispositifs sont cryptées et ne peuvent pas être facilement obtenues, modifiées ou divulguées de manière illicite.

Assurez-vous qu'une application vérifiée satisfait aux exigences de haut niveau suivantes en matière de protection des données :

* Confidentialité : Les données doivent être protégées contre toute observation ou divulgation non autorisée, tant pendant leur transit que lors de leur stockage.
* Intégrité : Les données doivent être protégées contre toute création, modification ou suppression malveillante par des attaquants non autorisés.
* Disponibilité : Les données doivent être accessibles aux utilisateurs autorisés, selon les besoins.

## V8.1 Protection générale des données

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.1.1** | Vérifiez que l'application protège les données sensibles contre la mise en cache dans des composants du serveur tels que les équilibreurs de charge et les caches d'applications. | | ✓ | ✓ | 524 |
| **8.1.2** | Vérifier que toutes les copies en cache ou temporaires de données sensibles stockées sur le serveur sont protégées contre tout accès non autorisé ou purgées/invalidées après que l'utilisateur autorisé a accédé aux données sensibles. | | ✓ | ✓ | 524 |
| **8.1.3** | Vérifier que l'application minimise le nombre de paramètres dans une requête, tels que les champs cachés, les variables Ajax, les cookies et les valeurs d'en-tête. | | ✓ | ✓ | 233 |
| **8.1.4** | Vérifier que l'application peut détecter et alerter sur un nombre anormal de demandes, par exemple par IP, par utilisateur, par total par heure ou par jour, ou tout ce qui a un sens pour l'application. | | ✓ | ✓ | 770 |
| **8.1.5** | Vérifiez que des sauvegardes régulières des données importantes sont effectuées et que des tests de restauration des données sont effectués. | | | ✓ | 19 |
| **8.1.6** | Vérifiez que les sauvegardes sont stockées en toute sécurité pour éviter que les données ne soient volées ou corrompues. | | | ✓ | 19 |

## V8.2 Protection des données côté client

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.2.1** | Vérifiez que l'application définit suffisamment d'en-têtes anticaching pour que les données sensibles ne soient pas mises en cache dans les navigateurs modernes. | ✓ | ✓ | ✓ | 525 |
| **8.2.2** | Vérifiez que les données stockées dans le stockage côté client (telles que le stockage local HTML5, le stockage de session, IndexedDB, ou les cookies) ne contiennent pas de données sensibles ou d'IIP. | ✓ | ✓ | ✓ | 922 |
| **8.2.3** | Vérifiez que les données authentifiées sont effacées du stockage du client, tel que le DOM du navigateur, après la fin du client ou de la session. | ✓ | ✓ | ✓ | 922 |

## V8.3 Données privées sensibles

Cette section permet de protéger les données sensibles contre la création, la lecture, la mise à jour ou la suppression sans autorisation, notamment en cas de grandes quantités.

Le respect de cette section implique le respect du contrôle d'accès V4, et en particulier V4.2. Par exemple, la protection contre les mises à jour ou la divulgation non autorisées d'informations personnelles sensibles nécessite le respect de la V4.2.1. Veuillez vous conformer à cette section et à V4 pour une couverture complète.

Note : Les réglementations et les lois relatives à la protection de la vie privée, telles que "Australian Privacy Principles" APP-11 ou GDPR, ont une incidence directe sur la manière dont les applications doivent aborder la mise en œuvre du stockage, de l'utilisation et de la transmission des informations personnelles sensibles. Cela va de sanctions sévères à de simples conseils. Veuillez consulter vos lois et règlements locaux et, le cas échéant, un spécialiste ou un avocat qualifié en matière de protection de la vie privée.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.3.1** | Vérifiez que les données sensibles sont envoyées au serveur dans le corps ou les en-têtes du message HTTP, et que les paramètres de la chaîne de requête de tout verbe HTTP ne contiennent pas de données sensibles. | ✓ | ✓ | ✓ | 319 |
| **8.3.2** | Vérifier que les utilisateurs disposent d'une méthode pour supprimer ou exporter leurs données sur demande. | ✓ | ✓ | ✓ | 212 |
| **8.3.3** | Vérifier que les utilisateurs disposent d'un langage clair concernant la collecte et l'utilisation des informations personnelles fournies et que les utilisateurs ont donné leur consentement pour l'utilisation de ces données avant qu'elles ne soient utilisées de quelque manière que ce soit. | ✓ | ✓ | ✓ | 285 |
| **8.3.4** | Vérifier que toutes les données sensibles créées et traitées par l'application ont été identifiées, et s'assurer qu'une politique est en place sur la manière de traiter les données sensibles. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 200 |
| **8.3.5** | Vérifier que l'accès aux données sensibles est contrôlé (sans enregistrer les données sensibles elles-mêmes), si les données sont collectées en vertu des directives pertinentes sur la protection des données ou si l'enregistrement de l'accès est nécessaire. | | ✓ | ✓ | 532 |
| **8.3.6** | Vérifiez que les informations sensibles contenues dans la mémoire sont écrasées dès qu'elles ne sont plus nécessaires pour atténuer les attaques de vidage de la mémoire, en utilisant des zéros ou des données aléatoires. | | ✓ | ✓ | 226 |
| **8.3.7** | Vérifier que les informations sensibles ou privées qui doivent être cryptées, le sont à l'aide d'algorithmes approuvés qui assurent à la fois la confidentialité et l'intégrité. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 327 |
| **8.3.8** | Vérifier que les informations personnelles sensibles font l'objet d'une classification de conservation des données, de sorte que les données anciennes ou périmées soient supprimées automatiquement, selon un calendrier ou selon la situation. | | ✓ | ✓ | 285 |

Lorsqu'on envisage la protection des données, il faut avant tout tenir compte de l'extraction ou de la modification en masse ou de l'utilisation excessive. Par exemple, de nombreux systèmes de médias sociaux ne permettent aux utilisateurs que d'ajouter 100 nouveaux amis par jour, mais le système d'où proviennent ces demandes n'a pas d'importance. Une plateforme bancaire peut souhaiter bloquer plus de 5 transactions par heure en transférant plus de 1000 euros de fonds vers des institutions externes. Les exigences de chaque système sont susceptibles d'être très différentes, de sorte que la décision d'être "anormal" doit tenir compte du modèle de menace et du risque commercial. Les critères importants sont la capacité de détecter, de dissuader ou, de préférence, de bloquer ces actions anormales en masse.

## Références

Pour plus d'informations, voir aussi :

* [Consider using Security Headers website to check security and anti-caching headers](https://securityheaders.io)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [European Union General Data Protection Regulation (GDPR) overview](https://edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
