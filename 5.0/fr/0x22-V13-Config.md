# V13 Configuration

## Objectif du contrôle

La configuration initiale de l'application doit être sécurisée pour une utilisation sur Internet.

Ce chapitre fournit des conseils sur les différentes configurations nécessaires à cet effet, notamment celles à appliquer lors du développement de l'application, ainsi que celles appliquées lors de la compilation et du déploiement.

Cela inclut des sujets tels que la prévention des fuites de données, la gestion sécurisée des communications entre les différents composants et la protection des secrets.

## V13.1 Documentation de configuration

Cette section décrit les exigences de documentation relatives à la communication de l'application avec les services internes et externes, ainsi que les techniques à employer pour éviter toute perte de disponibilité due à l'inaccessibilité de ces services. Elle aborde également la documentation relative aux secrets.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **13.1.1** | Vérifiez que tous les besoins de communication de l'application sont documentés. Cela doit inclure les services externes dont l'application dépend et les cas où un utilisateur final pourrait fournir un emplacement externe auquel l'application se connectera. | 2 | v5.0.be-1.14.7 |
| **13.1.2** | Vérifiez que pour chaque service utilisé par l'application, la documentation définit le nombre maximal de connexions simultanées (par exemple, les limites du pool de connexions) et le comportement de l'application lorsque cette limite est atteinte, y compris les mécanismes de secours ou de récupération, pour éviter les conditions de déni de service. | 3 | v5.0.be-1.14.8 |
| **13.1.3** | Vérifiez que la documentation de l'application définit des stratégies de gestion des ressources pour chaque système ou service externe utilisé (par exemple, bases de données, descripteurs de fichiers, threads, connexions HTTP). Cela doit inclure les procédures de libération des ressources, les paramètres de délai d'expiration, la gestion des échecs et l'implémentation de la logique de nouvelle tentative, en spécifiant les limites de nouvelle tentative, les délais et les algorithmes de retour arrière. Pour les opérations de requête-réponse HTTP synchrones, la documentation doit imposer des délais d'expiration courts et soit désactiver les nouvelles tentatives, soit les limiter strictement afin d'éviter les retards en cascade et l'épuisement des ressources. | 3 | v5.0.be-1.14.9 |
| **13.1.4** | Vérifiez que la documentation de l'application définit les secrets essentiels à la sécurité de l'application et un calendrier de rotation de ceux-ci, en fonction du modèle de menace et des exigences commerciales de l'organisation. | 3 | v5.0.be-1.14.10 |

## V13.2 Configuration de la communication backend

Les applications doivent interagir avec plusieurs services, notamment des API, des bases de données ou d'autres composants. Ces services peuvent être considérés comme internes à l'application, mais non inclus dans les mécanismes de contrôle d'accès standard de l'application, ou être entièrement externes. Dans les deux cas, il sera nécessaire de configurer l'application pour interagir en toute sécurité avec ces composants et, si nécessaire, de protéger cette configuration.

Notez que le chapitre « Communication sécurisée » fournit des conseils pour le chiffrement en transit.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **13.2.1** | Vérifiez que les communications entre les composants de l'application back-end qui ne prennent pas en charge le mécanisme de session utilisateur standard de l'application, notamment les API, les intergiciels et les couches de données, sont authentifiées. L'authentification doit utiliser des comptes de service individuels, des jetons à court terme ou une authentification par certificat, et non des identifiants immuables tels que des mots de passe, des clés API ou des comptes partagés avec accès privilégié. | 2 | v5.0.be-14.7.1 |
| **13.2.2** | Vérifiez que les communications entre les composants de l'application back-end, y compris les services locaux ou du système d'exploitation, les API, les intergiciels et les couches de données, sont effectuées avec des comptes dotés des privilèges les moins nécessaires. | 2 | v5.0.be-14.7.5 |
| **13.2.3** | Vérifiez que si des informations d’identification doivent être utilisées pour l’authentification du service, les informations d’identification utilisées par le consommateur ne sont pas des informations d’identification par défaut (par exemple, root/root ou admin/admin). | 2 | v5.0.be-14.7.2 |
| **13.2.4** | Vérifiez qu'une liste blanche est utilisée pour définir les ressources ou systèmes externes avec lesquels l'application est autorisée à communiquer (par exemple, pour les requêtes sortantes, les chargements de données ou l'accès aux fichiers). Cette liste blanche peut être implémentée au niveau de la couche applicative, du serveur web, du pare-feu ou d'une combinaison de différentes couches. | 2 | v5.0.be-14.7.3 |
| **13.2.5** | Vérifiez que le serveur Web ou d’application est configuré avec une liste autorisée de ressources ou de systèmes vers lesquels le serveur peut envoyer des requêtes ou charger des données ou des fichiers. | 2 | v5.0.be-14.7.4 |
| **13.2.6** | Vérifiez que lorsque l'application se connecte à des services distincts, elle suit la configuration documentée pour chaque connexion, comme le nombre maximal de connexions parallèles, le comportement lorsque le nombre maximal de connexions autorisées est atteint, les délais d'expiration de connexion et les stratégies de nouvelle tentative. | 3 | v5.0.be-14.7.6 |

## V13.3 Gestion du secret

La gestion des secrets est une tâche de configuration essentielle pour garantir la protection des données utilisées dans l'application. Les exigences spécifiques en matière de cryptographie sont décrites dans le chapitre « Cryptographie », mais cette section se concentre sur les aspects de gestion et de traitement des secrets.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **13.3.1** | Vérifiez qu'une solution de gestion des secrets, telle qu'un coffre-fort de clés, est utilisée pour créer, stocker, contrôler l'accès et détruire en toute sécurité les secrets back-end. Ceux-ci peuvent inclure des mots de passe, du matériel de clé, des intégrations avec des bases de données et des systèmes tiers, des clés et des semences pour des jetons temporels, d'autres secrets internes et des clés API. Les secrets ne doivent pas être inclus dans le code source de l'application ni dans les artefacts de build. Pour une application L3, cela doit impliquer une solution matérielle telle qu'un HSM. | 2 | v5.0.be-14.8.1 |
| **13.3.2** | Vérifiez que l’accès aux ressources secrètes respecte le principe du moindre privilège. | 2 | v5.0.be-14.8.4 |
| **13.3.3** | Vérifiez que toutes les opérations cryptographiques sont effectuées à l'aide d'un module de sécurité isolé (tel qu'un coffre-fort ou un module de sécurité matériel) pour gérer et protéger en toute sécurité le matériel clé contre toute exposition en dehors du module de sécurité. | 3 | v5.0.be-14.8.2 |
| **13.3.4** | Vérifiez que les secrets sont configurés pour expirer et être renouvelés en fonction de la documentation de l'application. | 3 | v5.0.be-14.8.3 |

## V13.4 Fuite d'informations involontaire

Les configurations de production doivent être renforcées afin d'éviter la divulgation de données inutiles. Nombre de ces problèmes sont rarement considérés comme un risque significatif, mais ils sont liés à d'autres vulnérabilités. Si ces problèmes ne sont pas présents par défaut, la barre est plus haute pour les attaques contre une application.

Par exemple, masquer la version des composants côté serveur ne résout pas le besoin de corriger tous les composants, et désactiver la liste des dossiers n'élimine pas le besoin d'utiliser des contrôles d'autorisation ou de garder les fichiers loin du dossier public, mais cela place la barre plus haut.

| # | Description | Niveau | #v5.0.be |
| :---: | :--- | :---: | :---: |
| **13.4.1** | Vérifiez que l'application est déployée soit sans aucune métadonnée de contrôle de source, y compris les dossiers .git ou .svn, soit de manière à ce que ces dossiers soient inaccessibles à la fois en externe et à l'application elle-même. | 1 | v5.0.be-14.1.11 |
| **13.4.2** | Vérifiez que les modes de débogage sont désactivés pour tous les composants dans les environnements de production afin d’éviter l’exposition des fonctionnalités de débogage et la fuite d’informations. | 2 | v5.0.be-14.3.2 |
| **13.4.3** | Vérifiez que les serveurs Web n’exposent pas les listes de répertoires aux clients, sauf si cela est explicitement prévu. | 2 | v5.0.be-14.3.4 |
| **13.4.4** | Vérifiez que l’utilisation de la méthode HTTP TRACE n’est pas prise en charge dans les environnements de production, afin d’éviter toute fuite d’informations potentielle. | 2 | v5.0.be-14.3.6 |
| **13.4.5** | Vérifiez que la documentation (comme pour les API internes) et les points de terminaison de surveillance ne sont pas exposés, sauf si cela est explicitement prévu. | 2 | v5.0.be-14.1.6 |
| **13.4.6** | Vérifiez que l’application n’expose pas d’informations de version détaillées des composants backend. | 3 | v5.0.be-14.3.3 |
| **13.4.7** | Vérifiez que le niveau Web est configuré pour servir uniquement les fichiers avec des extensions de fichier spécifiques afin d’éviter toute fuite involontaire d’informations, de configuration et de code source. | 3 | v5.0.be-14.3.5 |

## Références

Pour plus d'informations, voir également :

* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
