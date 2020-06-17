# V12 : Exigences de vérification des dossiers et des ressources

## Objectif de contrôle

Assurez-vous qu'une application vérifiée satisfait aux exigences de haut niveau suivantes :

* Les données des fichiers non fiables doivent être traitées en conséquence et de manière sécurisée.
* Les données de fichiers non fiables obtenues à partir de sources non fiables sont stockées en dehors de la racine web et avec des permissions limitées.

## V12.1 Exigences pour le téléchargement de fichiers

Bien que les bombes zip soient facilement testables à l'aide de techniques de test de pénétration, elles sont considérées comme L2 et au-dessus pour encourager la prise en compte de la conception et du développement avec des tests manuels minutieux, et pour éviter que les tests de pénétration manuels ou automatisés engendre une condition de déni de service.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.1.1** | Vérifiez que la demande n'accepte pas de fichiers volumineux qui pourraient remplir l'espace de stockage ou provoquer un déni de service. | ✓ | ✓ | ✓ | 400 |
| **12.1.2** | Vérifiez que les fichiers compressés sont contrôlés pour détecter les "bombes zip" - de petits fichiers d'entrée qui se décompresseront en fichiers énormes, épuisant ainsi les limites de stockage des fichiers. | | ✓ | ✓ | 409 |
| **12.1.3** | Vérifiez qu'un quota de taille de fichier et un nombre maximum de fichiers par utilisateur sont appliqués pour s'assurer qu'un seul utilisateur ne peut pas remplir le stockage avec trop de fichiers, ou des fichiers excessivement gros. | | ✓ | ✓ | 770 |

## V12.2 Exigences en matière d'intégrité des fichiers

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.2.1** | Vérifiez que les fichiers obtenus de sources non fiables sont validés comme étant du type attendu en fonction du contenu du fichier. | | ✓ | ✓ | 434 |

## V12.3 Exigences relatives à l'exécution des fichiers

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.3.1** | Vérifiez que les métadonnées de nom de fichier soumises par l'utilisateur ne sont pas utilisées directement par les systèmes de fichiers du système ou du cadre et qu'une API URL est utilisée pour protéger contre la traversée du chemin (path traversal). | ✓ | ✓ | ✓ | 22 |
| **12.3.2** | Vérifier que les métadonnées de nom de fichier soumises par l'utilisateur sont validées ou ignorées pour empêcher la divulgation, la création, la mise à jour ou la suppression de fichiers locaux (LFI). | ✓ | ✓ | ✓ | 73 |
| **12.3.3** | Vérifier que les métadonnées de nom de fichier soumises par l'utilisateur sont validées ou ignorées pour empêcher la divulgation ou l'exécution de fichiers distants (RFI), qui peuvent également conduire à des SSRF.  | ✓ | ✓ | ✓ | 98 |
| **12.3.4** | Vérifiez que l'application protège contre le téléchargement de fichiers réfléchis (RFD) en validant ou en ignorant les noms de fichiers soumis par les utilisateurs dans un paramètre JSON, JSONP ou URL, l'en-tête Content-Type de la réponse doit être défini sur text/plain, et l'en-tête Content-Disposition doit avoir un nom de fichier fixe. | ✓ | ✓ | ✓ | 641 |
| **12.3.5** | Vérifier que les métadonnées de fichiers non fiables ne sont pas utilisées directement avec l'API système ou les bibliothèques, pour se protéger contre l'injection de commandes du système d'exploitation. | ✓ | ✓ | ✓ | 78 |
| **12.3.6** | Vérifiez que l'application n'inclut pas et n'exécute pas de fonctionnalités provenant de sources non fiables, telles que des réseaux de distribution de contenu non vérifiés, des bibliothèques JavaScript, des bibliothèques node npm ou des DLL côté serveur. | | ✓ | ✓ | 829 |

## V12.4 Exigences en matière de stockage des fichiers

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.4.1** | Vérifiez que les fichiers obtenus de sources non fiables sont stockés en dehors de la racine web, avec des permissions limitées, de préférence avec une validation forte. | ✓ | ✓ | ✓ | 922 |
| **12.4.2** | Vérifiez que les fichiers obtenus de sources non fiables sont analysés par des scanners antivirus pour empêcher le téléchargement de contenus malveillants connus. | ✓ | ✓ | ✓ | 509 |

## V12.5 Exigences de téléchargement des fichiers

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.5.1** | Vérifiez que l'application web est configuré pour ne servir que les fichiers ayant des extensions de fichier spécifiques afin d'éviter les informations involontaires et les fuites de code source. Par exemple, les fichiers de sauvegarde (par exemple .bak), les fichiers de travail temporaires (par exemple .swp), les fichiers compressés (.zip, .tar.gz, etc) et les autres extensions couramment utilisées par les éditeurs doivent être bloqués, sauf si cela est nécessaire. | ✓ | ✓ | ✓ | 552 |
| **12.5.2** | Vérifiez que les demandes directes aux fichiers téléchargés ne seront jamais exécutées en tant que contenu HTML/JavaScript. | ✓ | ✓ | ✓ | 434 |

## V12.6 Exigences de protection des SSRF

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.6.1** | Vérifiez que le serveur web ou d'application est configuré avec une liste blanche de ressources ou de systèmes à partir desquels le serveur peut envoyer des requêtes ou charger des données/fichiers. | ✓ | ✓ | ✓ | 918 |

## Références

Pour plus d'informations, voir aussi :

* [File Extension Handling for Sensitive Information](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
* [Reflective file download by Oren Hafif](https://www.trustwave.com/Resources/SpiderLabs-Blog/Reflected-File-Download---A-New-Web-Attack-Vector/)
* [OWASP Third Party JavaScript Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html)
