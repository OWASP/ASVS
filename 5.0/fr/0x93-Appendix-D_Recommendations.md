# Annexe D : Recommandations

## Introduction

Lors de la préparation de la version 5.0 de la norme de vérification de la sécurité des applications (ASVS), il est apparu clairement que plusieurs éléments, existants ou nouvellement proposés, ne devaient pas être inclus comme exigences dans la version 5.0. Cela peut s'expliquer par le fait qu'ils n'entraient pas dans le champ d'application de l'ASVS selon la définition de la version 5.0, ou bien par le fait que, malgré leur pertinence, ils ne pouvaient être rendus obligatoires.

Ne voulant pas perdre tous ces éléments entièrement, certains ont été capturés dans cette annexe.

## Mécanismes de périmètre recommandés

Les éléments suivants sont concernés par ASVS. Ils ne devraient pas être rendus obligatoires, mais il est fortement recommandé de les prendre en compte dans le cadre d'une application sécurisée.

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
* Dans la mesure du possible, utilisez des implémentations de contrôle de sécurité préalablement écrites et bien contrôlées plutôt que de vous fier à la mise en œuvre de contrôles à partir de zéro.
* Idéalement, un mécanisme de contrôle d'accès unique devrait être utilisé pour accéder aux données et ressources protégées. Toutes les requêtes devraient transiter par ce mécanisme unique afin d'éviter les copier-coller ou les chemins alternatifs non sécurisés.
* Le contrôle d'accès basé sur les attributs ou les fonctionnalités est un modèle recommandé : le code vérifie l'autorisation de l'utilisateur pour une fonctionnalité ou un élément de données, plutôt que simplement son rôle. Les autorisations doivent toujours être attribuées à l'aide de rôles.

## Processus de sécurité des logiciels

Plusieurs processus de sécurité ont été supprimés d'ASVS 5.0, mais restent pertinents. Le projet OWASP SAMM pourrait être une bonne source d'inspiration pour une mise en œuvre efficace de ces processus. Parmi les éléments précédemment présents dans ASVS, on peut citer :

* Vérifier l'utilisation d'un cycle de vie sécurisé pour le développement de logiciels qui prend en compte la sécurité à tous les stades du développement.
* Vérifier l'utilisation de la modélisation des menaces pour chaque changement de conception ou planification de sprint afin d'identifier les menaces, de planifier les contre-mesures, de faciliter les réponses appropriées aux risques et d'orienter les tests de sécurité.
* Vérifier que toutes les histoires d'utilisateurs et les caractéristiques contiennent des contraintes de sécurité fonctionnelles, telles que "En tant qu'utilisateur, je devrais être en mesure de voir et de modifier mon profil. Je ne dois pas pouvoir consulter ou modifier le profil de quelqu'un d'autre"
* Vérifier la disponibilité d'une liste de contrôle de codage sécurisé, d'exigences de sécurité, de lignes directrices ou d'une politique pour tous les développeurs et les testeurs.
* Vérifier l'existence d'un processus permanent visant à garantir que le code source de l'application est exempt de portes dérobées, de codes malveillants (attaques par salami, bombes logiques, bombes à retardement) et de caractéristiques non documentées ou cachées (œufs de Pâques, outils de débogage non sécurisés). Il n'est pas possible de se conformer à cette section sans un accès complet au code source, y compris aux bibliothèques tierces, et cela ne convient donc probablement qu'aux applications exigeant les niveaux de sécurité les plus élevés.
* Vérifier que des mécanismes sont en place pour détecter les dérives de configuration dans les environnements déployés et y répondre. Il peut s'agir de l'utilisation d'une infrastructure immuable, d'un redéploiement automatisé à partir d'une base sécurisée ou d'outils de détection de dérive qui comparent l'état actuel aux configurations approuvées.
* Vérifier que le durcissement de la configuration est effectué sur tous les produits tiers, les bibliothèques,

Références:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/securityengineering/sdl/)
