# V5 Gestion des fichiers

## Objectif du contrôle

L'utilisation de fichiers peut présenter divers risques pour l'application, notamment le déni de service, l'accès non autorisé et l'épuisement de l'espace de stockage. Ce chapitre présente les exigences pour gérer ces risques.

## V5.1 Documentation sur la gestion des fichiers

Cette section comprend l’obligation de documenter les caractéristiques attendues des fichiers acceptés par l’application, comme condition préalable nécessaire au développement et à la vérification des contrôles de sécurité pertinents.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **5.1.1** | Vérifiez que la documentation définit les types de fichiers autorisés, les extensions de fichiers attendues et la taille maximale (y compris la taille décompressée) pour chaque fonctionnalité de téléchargement. De plus, assurez-vous que la documentation précise comment les fichiers sont sécurisés pour le téléchargement et le traitement des utilisateurs finaux, par exemple le comportement de l'application lorsqu'un fichier malveillant est détecté.| 2 |

## V5.2 Téléchargement de fichiers et contenu

La fonctionnalité de téléchargement de fichiers est une source majeure de fichiers non fiables. Cette section décrit les exigences permettant de garantir que la présence, le volume ou le contenu de ces fichiers ne nuisent pas à l'application.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **5.2.1** | Vérifiez que l'application n'acceptera que des fichiers d'une taille qu'elle peut traiter sans provoquer de perte de performances ou d'attaque par déni de service. | 1 |
| **5.2.2** | Vérifiez que lorsque l'application accepte un fichier, seul ou dans une archive telle qu'un fichier zip, elle vérifie si l'extension de fichier correspond à une extension attendue et que le contenu correspond au type représenté par l'extension. Cela inclut, sans s'y limiter, la vérification des « octets magiques » initiaux, la réécriture d'images et l'utilisation de bibliothèques spécialisées pour la validation du contenu des fichiers. Pour le niveau L1, cela peut se concentrer uniquement sur les fichiers utilisés pour prendre des décisions commerciales ou de sécurité spécifiques. À partir du niveau L2, cela doit s'appliquer à tous les fichiers acceptés. | 1 |
| **5.2.3** | Vérifiez que l'application vérifie les fichiers compressés (par exemple, zip, gz, docx, odt) par rapport à la taille maximale autorisée non compressée et au nombre maximal de fichiers avant de décompresser le fichier. | 2 |
| **5.2.4** | Vérifiez qu'un quota de taille de fichier et un nombre maximal de fichiers par utilisateur sont appliqués pour garantir qu'un seul utilisateur ne puisse pas remplir le stockage avec trop de fichiers ou des fichiers excessivement volumineux. | 3 |
| **5.2.5** | Vérifiez que l'application n'autorise pas le téléchargement de fichiers compressés contenant des liens symboliques, sauf si cela est spécifiquement requis (auquel cas il sera nécessaire d'appliquer une liste d'autorisation des fichiers vers lesquels il est possible de créer des liens symboliques).| 3 |
| **5.2.6** | Vérifiez que l'application a rejeté les images téléchargées avec une taille de pixel supérieure au maximum autorisé, afin d'éviter les attaques par inondation de pixels.| 3 |

## V5.3 Stockage de fichiers

Cette section comprend des exigences visant à empêcher l'exécution inappropriée des fichiers après leur téléchargement, à détecter le contenu dangereux et à éviter que des données non fiables ne soient utilisées pour contrôler l'emplacement de stockage des fichiers.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **5.3.1** | Vérifiez que les fichiers téléchargés ou générés par une entrée non fiable et stockés dans un dossier public ne sont pas exécutés en tant que code de programme côté serveur lorsqu'ils sont accessibles directement avec une requête HTTP. | 1 |
| **5.3.2** | Vérifiez que lorsque l'application crée des chemins d'accès pour les opérations sur les fichiers, elle utilise des données générées en interne ou fiables plutôt que des noms de fichiers soumis par l'utilisateur. Si des noms de fichiers ou des métadonnées de fichiers soumis par l'utilisateur doivent être utilisés, une validation et un nettoyage stricts doivent être appliqués. Ceci permet de se protéger contre les attaques par traversée de chemin, l'inclusion de fichiers locaux ou distants (LFI, RFI) et la falsification de requêtes côté serveur (SSRF). | 1 |
| **5.3.3** | Vérifiez que le traitement des fichiers côté serveur, comme la décompression des fichiers, ignore les informations de chemin fournies par l'utilisateur pour éviter les vulnérabilités telles que le glissement zip. | 3 |

## V5.4 Téléchargement de fichier

Cette section décrit les exigences visant à atténuer les risques liés au téléchargement de fichiers, notamment les attaques par traversée de chemin et par injection. Elle s'assure également qu'ils ne contiennent pas de contenu dangereux.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **5.4.1** | Vérifiez que l’application valide ou ignore les noms de fichiers soumis par l’utilisateur, y compris dans un paramètre JSON, JSONP ou URL et spécifie un nom de fichier dans le champ d’en-tête Content-Disposition de la réponse. | 2 |
| **5.4.2** | Vérifiez que les noms de fichiers servis (par exemple, dans les champs d'en-tête de réponse HTTP ou les pièces jointes aux e-mails) sont codés ou nettoyés (par exemple, conformément à la RFC 6266) pour préserver la structure du document et empêcher les attaques par injection. | 2 |
| **5.4.3** | Vérifiez que les fichiers obtenus à partir de sources non fiables sont analysés par des scanners antivirus pour empêcher la diffusion de contenu malveillant connu. | 2 |

## Références

Pour plus d'informations, voir également :

* [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
* [Example of using symlinks for arbitrary file read](https://hackerone.com/reports/1439593)
* [Explanation of "Magic Bytes" from Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures)
