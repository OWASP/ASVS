# V4 Exigences de vérification du contrôle d'accès

## Objectif de contrôle

L'autorisation est le concept qui consiste à ne permettre l'accès aux ressources qu'à ceux qui sont autorisés à les utiliser. Assurez-vous qu'une application vérifiée satisfait aux exigences de haut niveau suivantes :

* Les personnes qui accèdent aux ressources possèdent une autorisation valide pour le faire.
* Les utilisateurs sont associés à un ensemble bien défini de rôles et de privilèges.
* Les métadonnées relatives aux rôles et aux autorisations sont protégées contre toute rediffusion ou altération.

## Exigences de vérification de la sécurité

## V4.1 Conception générale du contrôle d'accès

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.1.1** | Vérifiez que l'application applique les règles de contrôle d'accès sur une couche de service de confiance, en particulier si le contrôle d'accès côté client est présent et pourrait être contourné. | ✓ | ✓ | ✓ | 602 |
| **4.1.2** | Vérifier que tous les attributs des utilisateurs et des données et les informations sur les politiques utilisées par les contrôles d'accès ne peuvent être manipulés par les utilisateurs finaux, sauf autorisation spécifique. | ✓ | ✓ | ✓ | 639 |
| **4.1.3** | Vérifier que le principe du moindre privilège existe - les utilisateurs ne doivent pouvoir accéder qu'aux fonctions, fichiers de données, URL, contrôleurs, services et autres ressources pour lesquels ils possèdent une autorisation spécifique. Cela implique une protection contre l'usurpation et l'élévation des privilèges. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |
| **4.1.4** | [SUPPRIMÉ, DOUBLON AVEC L'EXIGENCE 4.1.3] | | | | |
| **4.1.5** | Vérifier que les contrôles d'accès échouent de manière sûre, y compris lorsqu'une exception se produit. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |

## V4.2 Contrôle d'accès au niveau des opérations

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.2.1** | Vérifier que les données sensibles et les API sont protégées contre les attaques par référence directe à un objet (IDOR) non sécurisées visant la création, la lecture, la mise à jour et la suppression d'enregistrements, telles que la création ou la mise à jour de l'enregistrement de quelqu'un d'autre, la consultation de tous les enregistrements ou la suppression de tous les enregistrements. | ✓ | ✓ | ✓ | 639 |
| **4.2.2** | Vérifiez que l'application ou le cadriciel applique un mécanisme anti-CSRF fort pour protéger les fonctionnalités authentifiées, et qu'une anti-automation ou un anti-CSRF efficace protège les fonctionnalités non authentifiées. | ✓ | ✓ | ✓ | 352 |

## V4.3 Autres considérations relatives au contrôle d'accès

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.3.1** | Vérifier que les interfaces administratives utilisent une authentification multifactorielle appropriée pour empêcher toute utilisation non autorisée. | ✓ | ✓ | ✓ | 419 |
| **4.3.2** | Vérifiez que la navigation dans les répertoires est désactivée, sauf si vous le souhaitez délibérément. En outre, les applications ne doivent pas permettre la découverte ou la divulgation de métadonnées de fichiers ou de répertoires, tels que les dossiers Thumbs.db, .DS_Store, .git ou .svn. | ✓ | ✓ | ✓ | 548 |
| **4.3.3** | Vérifier que la demande dispose d'une autorisation supplémentaire (telle qu'une authentification renforcée ou adaptative) pour les systèmes à faible valeur, et/ou d'une séparation des tâches pour les demandes à valeur élevée afin de faire appliquer les contrôles anti-fraude en fonction du risque de fraude de la demande et de la fraude passée. | | ✓ | ✓ | 732 |

## Références

Pour plus d'informations, voir aussi :

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Access Control](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
* [OWASP CSRF Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [OWASP REST Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
