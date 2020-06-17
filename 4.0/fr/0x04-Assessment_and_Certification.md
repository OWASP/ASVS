# Évaluation et certification

## Position de l'OWASP sur les certifications et marques de confiance ASVS

L'OWASP, en tant qu'organisation à but non lucratif neutre, ne certifie actuellement aucun vendeur, vérificateur ou logiciel.

Toutes ces assertions d'assurance, marques de confiance ou certifications ne sont pas officiellement vérifiées, enregistrées ou certifiées par l'OWASP, de sorte qu'une organisation qui s'appuie sur ce point de vue doit être prudente quant à la confiance placée dans une tierce partie ou une marque de confiance revendiquant la certification ASVS.

Cela ne devrait pas empêcher les organisations d'offrir de tels services d'assurance, tant qu'elles ne revendiquent pas la certification officielle de l'OWASP.

## Directives pour les organismes de certification

La norme de vérification de la sécurité des applications peut être utilisée comme une vérification à livre ouvert de l'application, comprenant un accès ouvert et sans entrave aux ressources clés telles que les architectes et les développeurs, la documentation du projet, le code source, l'accès authentifié aux systèmes de test (y compris l'accès à un ou plusieurs comptes dans chaque rôle), en particulier pour les vérifications de L2 et L3.

Historiquement, les tests de pénétration et les examens de code sécurisé ont inclus des questions "par exception" - c'est-à-dire que seuls les tests échoués apparaissent dans le rapport final. Un organisme de certification doit inclure dans tout rapport la portée de la vérification (en particulier si un élément clé est hors de portée, comme l'authentification du SSO), un résumé des résultats de la vérification, y compris les tests réussis et les tests échoués, avec des indications claires sur la manière de résoudre les tests échoués.

Certaines exigences de vérification peuvent ne pas être applicables à l'application testée. Par exemple, si vous fournissez à vos clients une API de couche de service sans état sans implémentation client, de nombreuses exigences de la gestion de session V3 ne sont pas directement applicables. Dans de tels cas, un organisme de certification peut toujours prétendre à une conformité totale aux ASVS, mais doit clairement indiquer dans tout rapport une raison de non-applicabilité de ces exigences de vérification exclues.

La conservation de documents de travail détaillés, de captures d'écran ou de films, de scripts permettant d'exploiter un problème de manière fiable et répétée, ainsi que d'enregistrements électroniques des tests, tels que l'interception de journaux de proxy et de notes associées comme une liste de nettoyage, est considérée comme une pratique standard de l'industrie et peut être vraiment utile comme preuve des résultats pour les développeurs les plus douteux. Il ne suffit pas de faire fonctionner un outil et de signaler les échecs ; cela ne prouve pas (du tout) que tous les problèmes à un niveau de certification ont été testés et éprouvés de manière approfondie. En cas de litige, il doit y avoir suffisamment de preuves d'assurance pour démontrer que chaque exigence vérifiée a bien été testée.

### Méthode de test

Les organismes certificateurs sont libres de choisir la ou les méthodes d'essai appropriées, mais doivent les indiquer dans un rapport.

Selon l'application testée et l'exigence de vérification, différentes méthodes de test peuvent être utilisées pour obtenir une confiance similaire dans les résultats. Par exemple, la validation de l'efficacité des mécanismes de vérification des entrées d'une application peut être analysée soit par un test d'intrusion manuel, soit par des analyses du code source.

#### Le rôle des outils de test de sécurité automatisés

L'utilisation d'outils automatisés de test de pénétration est encouragée afin d'assurer une couverture aussi large que possible.

Il n'est pas possible d'effectuer une vérification complète de l'ASVS en utilisant uniquement des outils de test de pénétration automatisés. Alors qu'une grande majorité des exigences de la L1 peuvent être réalisées à l'aide de tests automatisés, la majorité globale des exigences ne se prête pas à l'utilisation de tests d'intrusion automatisés.

Veuillez noter que les limites entre les tests automatisés et manuels se sont estompées au fur et à mesure que le secteur de la sécurité des applications a évolué. Les outils automatisés sont souvent réglés manuellement par des experts et les testeurs manuels utilisent souvent une grande variété d'outils automatisés.

#### Le rôle des tests de pénétration

Dans la version 4.0, nous avons décidé de rendre la L1 entièrement testable par pénétration sans accès au code source, à la documentation ou aux développeurs. Deux éléments d'enregistrement, qui doivent être conformes au Top 10 2017 A10 de l'OWASP, nécessiteront des entretiens, des captures d'écran ou d'autres collectes de preuves, tout comme dans le Top 10 2017 de l'OWASP. Cependant, les tests sans accès aux informations nécessaires ne constituent pas une méthode idéale de vérification de la sécurité, car ils laissent de côté la possibilité d'examiner la source, d'identifier les menaces et les contrôles manquants, et de réaliser un test beaucoup plus approfondi dans un délai plus court. 

Dans la mesure du possible, l'accès aux développeurs, à la documentation, au code et l'accès à une application de test avec des données de non-production, est nécessaire lors de l'exécution d'une évaluation de niveau 2 ou 3. Les tests de pénétration effectués à ces niveaux nécessitent ce niveau d'accès, que nous appelons "examens hybrides" ou "tests de pénétration hybrides". 

## Autres utilisations de l'ASVS

En plus de servir à l'évaluation de la sécurité d'une application, nous avons identifié plusieurs autres potentielles utilisations de l'ASVS.

### Guide pour les tests unitaires et d'intégration automatisés

L'ASVS est conçu pour être hautement testable, à la seule exception des exigences en matière d'architecture et de code malveillant. Grâce à des tests unitaires et d'intégration qui permettent de détecter des variantes et des cas d'abus spécifiques et pertinents, l'application se vérifie pratiquement d'elle-même à chaque nouvelle itération. Par exemple, des tests supplémentaires peuvent être élaborés pour la suite de tests d'un contrôleur de connexion, en testant le paramètre de nom d'utilisateur pour les noms d'utilisateur communs par défaut, l'énumération des comptes, l'énumération exhaustive (brute-force), l'injection LDAP et SQL, et XSS. De plus, un test sur le paramètre du mot de passe devrait inclure les mots de passe communs, la longueur du mot de passe, l'injection d'octets nuls, la suppression du paramètre, XSS, et plus encore.

### Pour la formation au développement sécurisé

L'ASVS peut également être utilisé pour définir les caractéristiques des logiciels sécurisés. De nombreux cours de "codage sécurisé" sont simplement des cours de piratage éthique avec une légère trace de conseils de codage. Cela n'aide pas nécessairement les développeurs à écrire un code plus sûr. Les cours de développement sécurisé peuvent plutôt utiliser l'ASVS en mettant l'accent sur les contrôles proactifs qu'il contient, plutôt que sur les dix principales erreurs à ne pas faire.

### En tant que pilote pour la sécurité des applications agiles

L'ASVS peut être utilisé dans un processus de développement agile comme cadre pour définir les tâches spécifiques qui doivent être mises en œuvre par l'équipe pour avoir un produit sécurisé. Une approche pourrait être : En commençant par le niveau 1, vérifier l'application ou le système spécifique selon les exigences de l'ASVS pour le niveau spécifié, trouver les contrôles manquants et soulever des tickets/tâches spécifiques dans le backlog. Cela permet de hiérarchiser les tâches spécifiques (ou grooming) et de rendre la sécurité visible dans le processus agile. Cela peut également être utilisé pour hiérarchiser les tâches d'audit et de révision dans l'organisation, où une exigence ASVS spécifique peut être un moteur de révision, de remaniement ou d'audit pour un membre spécifique de l'équipe et être visible en tant que "dette" dans le backlog qui doit finalement être fait.

### Comme cadre pour guider l'acquisition de logiciels sécurisés

L'ASVS est un cadre idéal pour aider à sécuriser l'acquisition de logiciels ou de services de développement personnalisés. L'acheteur peut simplement exiger que le logiciel qu'il souhaite acquérir soit développé au niveau X de l'ASVS, et demander au vendeur de prouver que le logiciel satisfait au niveau X de l'ASVS. Cette procédure fonctionne bien lorsqu'elle est combinée avec l'annexe du contrat de logiciel sécurisé de l'OWASP.
