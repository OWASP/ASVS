# Préface

Bienvenue dans la version 5.0 du référentiel de vérification de la sécurité des applications (ASVS)!

## Introduction

L'ASVS est un effort communautaire visant à établir un cadre d'exigences et de contrôles de sécurité qui se concentre sur la définition des contrôles de sécurité fonctionnels et non fonctionnels requis lors de la conception, du développement et du test d'applications et de services web modernes.

ASVS Version 5.0 is the culmination of a huge amount of effort from the leaders, working group and other community members to update and improve this important standard.

Our goal for this version has been to make the ASVS easier to use whilst also making it more clearly focused on a particular scope and covering new, important areas of application developement.

## Les objectifs clés de la version 5.0 de l'ASVS

La version 5.0 a été conçue en gardant à l'esprit un certain nombre de principles "clés".


### Ensemble clair d'exigences

L’ensemble des exigences pour la version 5.0 a été préparé sur la base des considérations suivantes.

* Déduplication agressive des exigences pour éviter que les contrôles ou les concepts ne soient divisés en plusieurs endroits.
* Clarification d'un texte d'exigence peu clair ou non exploitable.
* Ajout de nouvelles exigences pour couvrir des domaines particulièrement préoccupants tels que les autorisations, les jetons et la cryptographie.
* Ajout de nouveaux chapitres et sections pour les domaines qui peuvent ne pas s'appliquer à toutes les applications mais qui sont toujours sensibles à la sécurité, tels que OAuth et WebSockets.

### Clarifier la portée du référentiel

Il est important que toutes les exigences soient pertinentes par rapport au champ d’application défini de la norme et qu’elles soient formulées d’une manière cohérente avec l’objectif de la norme.

Les directives à cet effet étaient les suivantes :

* S’assurer que toutes les exigences sont dans le cadre d’une application ou d’un service Web.
* Vérifier que les exigences sont formulées conformément au nom ASVS, en particulier :
    * Application - Les exigences se situent au niveau de l'application et relèvent de la responsabilité des développeurs d'applications.
    * Sécurité – Des exigences sont clairement nécessaires pour que l’application soit sécurisée.
    * Vérification – Les exigences sont formulées de manière à avoir un objectif clair et vérifiable.
    * Norme - Cohérence et structure claires des exigences, comme on pourrait s'y attendre d'une norme.

### Meilleur niveau de définitions

Les niveaux de la version 5.0 visent à rendre l'ASVS plus facile à adopter tout en expliquant clairement pourquoi les exigences ont été attribuées à des niveaux spécifiques.

Ceci inclut :

* Rendre la justification du niveau plus claire et mettre l’accent sur la priorité (en tenant compte de la réduction des risques et des efforts de mise en œuvre).
* Avoir un nombre réaliste d’exigences de niveau 1 afin d’avoir une barrière à l’entrée plus basse.
* Un meilleur équilibre entre le nombre d’exigences du niveau 2 et du niveau 3 pour permettre une progression plus fluide.

### Rationalisation du document

Pour rendre le document plus facile à utiliser, il faut notamment garder les exigences réelles au premier plan et éviter tout contenu narratif inutile, tout en conservant les explications clés.

Ceci inclut :

* Éviter trop de texte explicatif ou supplémentaire autour des exigences, sauf lorsque cela est spécifiquement nécessaire.
* Au lieu d’exigences trop verbeuses, gardez-les abstraites et faites référence à des aide-mémoire pertinents ou à d’autres documents dans le texte explicatif.
* Maintenir les mappages à l'écart des exigences principales, mais plutôt les séparer pour qu'ils soient gérés et maintenus séparément.

## La convivialité pour favoriser l'adoption

Nous espérons que cette augmentation de la convivialité entraînera une augmentation correspondante de l’adoption par les organisations qui souhaitent améliorer la sécurité de leur application ou la cohérence et la rigueur de leurs évaluations de sécurité.

Vous trouverez plus de détails sur l’utilisation de la norme dans les chapitres suivants.
