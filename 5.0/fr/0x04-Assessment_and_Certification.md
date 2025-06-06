# Évaluation et certification

## Position de l'OWASP sur les certifications et marques de confiance ASVS

L'OWASP, en tant qu'organisation à but non lucratif neutre, ne certifie actuellement aucun vendeur, vérificateur ou logiciel. Toutes ces assertions d'assurance, marques de confiance ou certifications ne sont pas officiellement vérifiées, enregistrées ou certifiées par l'OWASP, de sorte qu'une organisation qui s'appuie sur ce point de vue doit être prudente quant à la confiance placée dans une tierce partie ou une marque de confiance revendiquant la certification ASVS.

Cela ne devrait pas empêcher les organisations d'offrir de tels services d'assurance, tant qu'elles ne revendiquent pas la certification officielle de l'OWASP.

## Comment vérifier la conformité ASVS

L'ASVS n'est volontairement pas prescriptif quant à la manière précise de vérifier la conformité au niveau d'un guide de tests. Il est toutefois important de souligner certains points clés.

### Rapport de vérification

Les tests d'intrusion traditionnels signalent les problèmes « par exception », en ne listant que les échecs. Cependant, un rapport de certification ASVS doit inclure le périmètre, un résumé de toutes les exigences vérifiées, les exigences pour lesquelles des exceptions ont été constatées et des conseils pour résoudre les problèmes. Certaines exigences peuvent ne pas être applicables (par exemple, la gestion des sessions dans les API sans état), et cela doit être mentionné dans le rapport.

### Portée de la vérification

Une organisation développant une application n'implémentera généralement pas toutes les exigences, certaines pouvant être non pertinentes ou moins importantes selon les fonctionnalités de l'application. Le vérificateur doit préciser le périmètre de la vérification, notamment le niveau que l'organisation souhaite atteindre et les exigences incluses. Il doit s'agir de ce qui a été inclus plutôt que de ce qui ne l'a pas été. Il doit également fournir un avis sur les raisons justifiant l'exclusion des exigences non implémentées.

Cela devrait permettre au consommateur d’un rapport de vérification de comprendre le contexte de la vérification et de prendre une décision éclairée sur le niveau de confiance qu’il peut accorder à l’application.

Les organismes de certification peuvent choisir leurs méthodes de test, mais devraient les indiquer dans le rapport,et elle devraient idéalement être reproductibles. Différentes méthodes, comme les tests d'intrusion manuels ou l'analyse du code source, peuvent être utilisées pour vérifier des aspects tels que la validation des entrées, selon l'application et les exigences.

### Mécanismes de vérification

Plusieurs techniques différentes peuvent être utilisées pour vérifier une même exigences ASVS. Outre les tests d'intrusion (utilisant des "credentials" valides pour une couverture complète de l'application), la vérification des exigences ASVS peut nécessiter l'accès à la documentation, au code source, à la configuration et aux personnes impliquées dans le processus de développement. Ceci est particulièrement vrai pour la vérification des exigences L2 et L3. Il est courant de fournir des preuves solides des résultats au moyen d'une documentation détaillée, pouvant inclure des documents de travail, des captures d'écran, des scripts et des journaux de tests. L'exécution d'un outil automatisé sans tests approfondis ne suffit pas à obtenir la certification, car chaque exigence doit être testée de manière vérifiable.

L'utilisation de l'automatisation pour vérifier les exigences ASVS est un sujet qui suscite un intérêt constant. Il est donc important de clarifier certains points relatifs aux tests automatisés et en boîte noire.

#### Le rôle des outils de test de sécurité automatisés

Lorsque des outils de tests de sécurité automatisés, tels que les tests de sécurité dynamiques et statiques des applications (DAST et SAST), sont correctement implémentés dans le pipeline de développement, ils peuvent identifier des problèmes de sécurité qui ne devraient jamais exister. Cependant, sans une configuration et un réglage minutieux, ils n'offriront pas la couverture requise et leur niveau de bruit empêchera l'identification et la résolution des véritables problèmes de sécurité.

Bien que cela puisse couvrir certaines des exigences techniques les plus basiques et les plus simples, telles que celles relatives à l'encodage ou à l'assainissement de sortie, il est essentiel de noter que ces outils ne seront pas entièrement en mesure de vérifier bon nombre des exigences ASVS les plus complexes ou celles liées à la logique métier et au contrôle d'accès.

Pour les exigences moins simples, l'automatisation reste probablement envisageable, mais des vérifications spécifiques à l'application devront être écrites pour y parvenir. Ces vérifications peuvent être similaires aux tests unitaires et d'intégration déjà utilisés par l'organisation. Il est donc possible d'utiliser l'infrastructure d'automatisation des tests existante pour écrire ces tests spécifiques à ASVS. Bien que cela nécessite un investissement à court terme, les avantages à long terme de la vérification continue des exigences ASVS seront significatifs.

En résumé, testable en utilisant l'automatisation != exécuter un outil sur étagère.

#### Le rôle des tests de pénétration

Bien que L1 dans la version 4.0 ait été optimisé pour les tests de « boîte noire » (sans documentation et sans source), même dans ce cas, le standard était clair sur le fait qu'il ne s'agissait pas d'une activité d'assurance efficace et qu'elle devait être activement découragée.

Les tests sans accès aux informations supplémentaires nécessaires constituent un mécanisme sous-productifs et inefficaces de vérification de la sécurité, car ils ne permettent pas d’examiner le code source, d’identifier les menaces et les contrôles manquants, et d’effectuer un test beaucoup plus approfondi dans un délai plus court.

Il est fortement encouragé d'effectuer des tests d'intrusion basés sur la documentation ou le code source (hybrides), avec un accès complet aux développeurs et à la documentation de l'application, plutôt que des tests d'intrusion traditionnels. Cela sera certainement nécessaire pour vérifier de nombreuses exigences ASVS.
