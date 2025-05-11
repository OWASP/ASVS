# V2 Validation et logique métier

## Objectif du contrôle

Assurez-vous qu'une application vérifiée satisfait aux exigences de haut niveau suivantes :

* Les entrées reçues par l'application correspondent aux attentes métier ou fonctionnelles.
* Le flux logique métier est séquentiel, traité dans l’ordre et ne peut pas être contourné.
* La logique métier inclut des limites et des contrôles pour détecter et prévenir les attaques automatisées, telles que les transferts continus de petits fonds et l'ajout d'un million d'amis un par un.
* Les flux logiques métier à haute valeur ajoutée ont pris en compte les cas d'abus et les acteurs malveillants, et disposent de protections contre l'usurpation d'identité, la falsification, la divulgation d'informations et les attaques par élévation de privilèges.

## V2.1 Validation et documentation de la logique métier

La documentation de validation et de logique métier doit définir clairement les limites de la logique métier, les règles de validation et la cohérence contextuelle des éléments de données combinés, afin qu'il soit clair ce qui doit être implémenté dans l'application.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **2.1.1** | Vérifiez que la documentation de l'application définit des règles de validation des entrées pour vérifier la validité des éléments de données par rapport à une structure attendue. Il peut s'agir de formats de données courants tels que des numéros de carte de crédit, des adresses e-mail ou des numéros de téléphone, ou d'un format de données interne. | 1 | v5.0.be-1.11.5 |
| **2.1.2** | Vérifiez que la documentation de l'application définit comment valider la cohérence logique et contextuelle des éléments de données combinés, par exemple en vérifiant que la banlieue et le code postal correspondent. | 2 | v5.0.be-1.11.6 |
| **2.1.3** | Vérifiez que les attentes en matière de limites et de validations de la logique métier sont documentées, y compris par utilisateur et globalement dans l'application. | 2 | v5.0.be-1.11.4 |

## V2.2 Validation des entrées

Des contrôles de validation des entrées efficaces permettront de respecter les attentes métier ou fonctionnelles concernant le type de données que l'application s'attend à recevoir. Cela garantira une bonne qualité des données et réduira la surface d'attaque. Cependant, cela ne supprime ni ne remplace la nécessité d'utiliser un codage, un paramétrage ou un nettoyage corrects lors de l'utilisation des données dans un autre composant ou pour leur présentation en sortie.

Dans ce contexte, les « entrées » peuvent provenir d'une grande variété de sources, notamment des champs de formulaire HTML, des requêtes REST, des paramètres d'URL, des champs d'en-tête HTTP, des cookies, des fichiers sur disque, des bases de données et des API externes.

Un contrôle de logique métier peut vérifier qu'une entrée particulière est un nombre inférieur à 100. Une attente fonctionnelle peut vérifier qu'un nombre est inférieur à un certain seuil, car ce nombre contrôle le nombre de fois qu'une boucle particulière aura lieu, et un nombre élevé pourrait entraîner un traitement excessif et une condition potentielle de déni de service.

Bien que la validation de schéma ne soit pas explicitement obligatoire, cela peut être le mécanisme le plus efficace pour une couverture de validation complète des API HTTP ou d'autres interfaces qui utilisent JSON ou XML.

Veuillez noter les points suivants concernant la validation du schéma :

* La « version publiée » de la spécification de validation du schéma JSON est considérée comme prête pour la production, et non comme « stable » à proprement parler. Lorsque vous utilisez la validation du schéma JSON, assurez-vous qu'il n'y a aucune lacune par rapport aux exigences ci-dessous.
* Toutes les bibliothèques de validation de schéma JSON utilisées doivent également être surveillées et mises à jour si nécessaire une fois la norme formalisée.
* La validation DTD ne doit pas être utilisée et l'évaluation DTD du framework doit être désactivée pour éviter les problèmes liés aux attaques XXE contre les DTD.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **2.2.1** | Vérifier que les entrées sont validées afin de respecter les attentes métier ou fonctionnelles. Cette validation doit être basée sur une liste de valeurs, de modèles et de plages autorisées, ou sur la comparaison des entrées avec une structure attendue et des limites logiques selon des règles prédéfinies. Pour le niveau 1, cette validation peut se concentrer sur les entrées utilisées pour prendre des décisions métier ou de sécurité spécifiques. À partir du niveau 2, elle doit s'appliquer à toutes les entrées. | 1 | v5.0.be-11.3.1 |
| **2.2.2** | Vérifiez que l'application est conçue pour appliquer la validation des entrées au niveau d'une couche de service de confiance. Bien que la validation côté client améliore la convivialité et doive être encouragée, elle ne doit pas être considérée comme un contrôle de sécurité. | 1 | v5.0.be-11.3.2 |
| **2.2.3** | Vérifiez que l’application garantit que les combinaisons d’éléments de données associés sont raisonnables selon les règles prédéfinies. | 2 | v5.0.be-11.3.3 |

## V2.3 Sécurité de la logique métier

Cette section examine les exigences clés pour garantir que l’application applique les processus de logique métier de manière correcte et n’est pas vulnérable aux attaques qui exploitent la logique et le flux de l’application.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **2.3.1** | Vérifiez que l’application traitera uniquement les flux de logique métier pour le même utilisateur dans l’ordre séquentiel attendu et sans sauter d’étapes. | 1 | v5.0.be-11.1.1 |
| **2.3.2** | Vérifiez que les limites de la logique métier sont implémentées conformément à la documentation de l'application, afin d'éviter que des failles de la logique métier ne soient exploitées. | 2 | v5.0.be-11.1.3 |
| **2.3.3** | Vérifiez que les transactions sont utilisées au niveau de la logique métier de telle sorte qu'une opération de logique métier réussisse dans son intégralité ou qu'elle soit restaurée à l'état correct précédent. | 2 | v5.0.be-11.1.9 |
| **2.3.4** | Vérifiez que les flux logiques métier à forte valeur ajoutée nécessitent l'approbation de plusieurs utilisateurs afin d'éviter toute action non autorisée ou accidentelle. Cela peut inclure, sans s'y limiter, les transferts monétaires importants, les approbations de contrats, l'accès à des informations classifiées ou les contournements de sécurité dans le secteur manufacturier. | 3 | v5.0.be-11.1.10 |

## V2.4 Anti-automatisation

Cette section comprend des contrôles anti-automatisation pour garantir que les interactions de type humain sont requises et que les demandes automatisées excessives sont évitées.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **2.4.1** | Vérifiez que des contrôles anti-automatisation sont en place pour protéger contre les appels excessifs aux fonctions d'application qui pourraient conduire à l'exfiltration de données, à la création de données inutiles, à l'épuisement des quotas, aux violations de limites de débit, au déni de service ou à la surutilisation de ressources coûteuses. | 2 | v5.0.be-11.2.2 |
| **2.4.2** | Vérifiez que les flux logiques métier nécessitent un timing humain réaliste, évitant ainsi des soumissions de transactions excessivement rapides. | 3 | v5.0.be-11.2.1 |

## Références

Pour plus d'informations, voir également :

* [OWASP Web Security Testing Guide 4.2: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Web Security Testing Guide 4.2: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README)
* Anti-automation can be achieved in many ways, including the use of the [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [JSON Schema](https://json-schema.org/specification.html)
