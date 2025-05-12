# Annexe X : Recommandations

## Introduction

Lors de la préparation de la version 5.0 de la norme de vérification de la sécurité des applications (ASVS), nous avons constaté que plusieurs éléments, existants ou nouvellement suggérés, ne faisaient pas partie des exigences de la version 5.0. Cela peut s'expliquer par le fait qu'ils n'étaient pas couverts par la définition de l'ASVS 5.0, ou que nous ne pensions pas pouvoir les rendre obligatoires, même si nous les trouvions judicieux.

Nous ne voulions pas supprimer complètement ces éléments, c'est pourquoi nous avons tenté d'en inclure certains dans cette annexe.

## Mécanismes recommandés et concernés

Les éléments suivants sont concernés par ASVS. Nous ne pensons pas qu'ils devraient être rendus obligatoires, mais nous recommandons fortement de les considérer comme faisant partie d'une application sécurisée.

* Un indicateur de sécurité des mots de passe devrait être fourni pour aider les utilisateurs à définir un mot de passe plus fort.
* Créez un fichier security.txt accessible au public à la racine ou dans le répertoire .well-known de l'application, définissant clairement un lien ou une adresse e-mail permettant de contacter les propriétaires en cas de problème de sécurité.
* La validation des entrées côté client devrait être appliquée en plus de la validation au niveau d'une couche de service de confiance, car cela permet de détecter si un utilisateur a contourné les contrôles côté client pour tenter d'attaquer l'application.
* Empêchez l'affichage de pages sensibles et accessibles accidentellement dans les moteurs de recherche à l'aide d'un fichier robots.txt, de l'en-tête de réponse X-Robots-Tag ou d'une balise méta HTML robots.
* Lorsque vous utilisez GraphQL, implémentez la logique d'autorisation au niveau de la couche logique métier plutôt que dans la couche GraphQL ou du résolveur afin d'éviter de gérer l'autorisation sur chaque interface distincte.

Références :

* [Plus d'informations sur security.txt, y compris un lien vers la RFC](https://securitytxt.org/)

## Principes de sécurité des logiciels

Les éléments suivants figuraient déjà dans ASVS, mais ne constituent pas de véritables exigences. Il s'agit plutôt de principes à prendre en compte lors de la mise en œuvre de contrôles de sécurité, dont le respect permettra de renforcer la robustesse. Parmi ceux-ci :

* Les contrôles de sécurité doivent être centralisés, simples (économie de conception), vérifiables et réutilisables. Cela permet d'éviter les contrôles dupliqués, manquants ou inefficaces.
* Dans la mesure du possible, utilisez des implémentations de contrôles de sécurité déjà écrites et validées plutôt que de vous fier à vos propres implémentations.
* Idéalement, un mécanisme de contrôle d'accès unique devrait être utilisé pour accéder aux données et ressources protégées. Toutes les requêtes devraient transiter par ce mécanisme unique afin d'éviter les copier-coller ou les chemins alternatifs non sécurisés.
* Le contrôle d'accès basé sur les attributs ou les fonctionnalités est un modèle recommandé : le code vérifie l'autorisation de l'utilisateur pour une fonctionnalité ou un élément de données, plutôt que simplement son rôle. Les autorisations doivent toujours être attribuées à l'aide de rôles.

## Processus de sécurité des logiciels

Plusieurs processus de sécurité ont été supprimés d'ASVS 5.0, mais restent pertinents. Le projet OWASP SAMM pourrait être une bonne source d'inspiration pour une mise en œuvre efficace de ces processus. Parmi les éléments précédemment présents dans ASVS, on peut citer :

* Vérifier l'utilisation d'un cycle de développement logiciel sécurisé intégrant la sécurité à toutes les étapes du développement.
* Vérifier l'utilisation de la modélisation des menaces pour chaque modification de conception ou planification de sprint afin d'identifier les menaces, de planifier des contre-mesures, de faciliter les réponses aux risques appropriées et de guider les tests de sécurité.
* Vérifier que tous les user stories et fonctionnalités contiennent des contraintes de sécurité fonctionnelles, telles que : « En tant qu'utilisateur, je dois pouvoir consulter et modifier mon profil. Je ne dois pas pouvoir consulter ni modifier le profil d'autrui. »
* Vérifier la disponibilité d'une liste de contrôle de codage sécurisé, d'exigences de sécurité, de directives ou de politiques pour tous les développeurs et testeurs. * Vérifier l'existence d'un processus continu garantissant que le code source de l'application est exempt de portes dérobées, de code malveillant (par exemple, attaques salami, bombes logiques, bombes à retardement) et de fonctionnalités non documentées ou cachées (par exemple, œufs de Pâques, outils de débogage non sécurisés). Le respect de cette section est impossible sans un accès complet au code source, y compris aux bibliothèques tierces, et ne convient donc probablement qu'aux applications exigeant les niveaux de sécurité les plus élevés.
* Vérifier la mise en place de mécanismes permettant de détecter et de gérer les dérives de configuration dans les environnements déployés. Cela peut inclure l'utilisation d'une infrastructure immuable, un redéploiement automatisé à partir d'une base de référence sécurisée ou des outils de détection des dérives comparant l'état actuel aux configurations approuvées.
* Vérifier que le renforcement de la configuration est appliqué à tous les produits, bibliothèques, frameworks et services tiers, conformément à leurs recommandations individuelles.

Références:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/securityengineering/sdl/)
