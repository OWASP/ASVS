# Conseils aux utilisateurs de la version 4.0

Les utilisateurs de la version 4.0 de la norme peuvent trouver utile de voir certains des changements clés dans le contenu de la version 5.0 ainsi que certains changements dans la portée et la philosophie qui ont eu lieu pendant le développement de cette dernière version.

##  Quoi de neuf dans la version 5.0

Les sections suivantes tentent de couvrir les changements les plus importants

### Renumérotation et réorganisation complètes

Presque toutes les exigences ont été modifiées d'une manière ou d'une autre et même celles qui n'ont pas été modifiées ou déplacées subiront des changements de numérotation suite à une réorganisation ou à d'autres déplacements d'exigences.

Les mappages fournis devraient aider à déterminer si et où les exigences de la version 4.0 ont été intégrées à la version 5.0.

### Moins de couplage avec les directives du NIST sur l'identité numérique

Les [Directives sur l'identité numérique (SP 800-63)](https://pages.nist.gov/800-63-3/) du NIST a été et demeure une excellente norme, fondée sur des données probantes, pour les contrôles clés liés à l'authentification et à l'autorisation. Certains chapitres de la version 4.0 étaient étroitement liés à ces lignes directrices, notamment en termes de structure et de terminologie.

Bien que ces lignes directrices et leurs améliorations futures demeurent une référence importante et la base de nombreuses exigences, leur couplage strict a engendré des difficultés qui ont conduit à la décision d'abandonner cette approche. Parmi ces difficultés figuraient une terminologie moins largement reconnue, la duplication d'exigences très similaires dans des situations très légèrement différentes, et le fait que la cartographie était incomplète par rapport à ce qui était perçu comme pertinent pour les ASVS.

### S'éloigner de l'énumération des faiblesses communes (CWE)

L'[énumération des faiblesses communes (CWE)](https://cwe.mitre.org/) provenant du MITRE est un moyen utile de cartographier les différentes faiblesses de sécurité des logiciels. Son utilisation présente certaines difficultés, notamment concernant certains CWE qui ne sont que des catégories et ne devraient pas être utilisés pour la cartographie, la difficulté de cartographier certaines exigences existantes vers un seul CWE, et également le fait que certains mappages étaient flous ou inexacts dans la version 4.0 d'ASVS.

La solution a été de supprimer CWE (et tout autre mappage) dans le but de mapper plutôt vers le projet OWASP Énumération des exigences communes (En anglais : CRE pour Common Requirement Enumeration) qui mappera ASVS vers une variété d'autres projets OWASP et normes externes.

### Concentrez-vous sur l'objectif, pas sur le mécanisme

Dans la version 4.0, de nombreuses exigences étaient axées sur un mécanisme particulier plutôt que sur l'objectif de sécurité à atteindre. Dans la version 5.0, à moins qu'il n'existe qu'un seul mécanisme réaliste pour atteindre l'objectif, les exigences se concentrent sur l'objectif de sécurité et incluent des mécanismes spécifiques à titre d'exemple ou renvoient à d'autres directives.

### Documenter les décisions de sécurité

Pour certaines exigences, la mise en œuvre sera complexe et très spécifique aux besoins de l'application. Parmi les exemples courants figurent les autorisations, la validation des entrées et les contrôles de protection des différents niveaux de données sensibles. Pour tenir compte de cela, plutôt que de formuler des affirmations générales telles que « toutes les données doivent être chiffrées » ou de tenter de couvrir tous les cas d'utilisation possibles dans une exigence, nous avons des exigences qui imposent que l'approche et la configuration du développeur de l'application concernant ces types de contrôles soient documentées afin de pouvoir en vérifier la pertinence, puis de comparer la mise en œuvre réelle à la documentation pour évaluer si elle répond aux attentes.

<!--

### TODO: add more items

We set out to ensure that the ASVS 4.0 Level 1 is a comprehensive superset of PCI DSS 3.2.1 Sections 6.5, for application design, coding, testing, secure code reviews, and penetration tests. This necessitated covering buffer overflow and unsafe memory operations in V5, and unsafe memory-related compilation flags in V14, in addition to existing industry-leading application and web service verification requirements.

We have completed the shift of the ASVS from monolithic server-side-only controls, to providing security controls for all modern applications and APIs. In the days of functional programming, server-less API, mobile, cloud, containers, CI/CD and DevSecOps, federation and more, we cannot continue to ignore modern application architecture. Modern applications are designed very differently from those built when the original ASVS was released in 2009. The ASVS must always look far into the future so that we provide sound advice for our primary audience - developers. We have clarified or dropped any requirement that assumes that applications are executed on systems owned by a single organization.

Due to the size of the ASVS 4.0, as well as our desire to become the baseline ASVS for all other ASVS efforts, we have retired the mobile chapter, in favor of the Mobile Application Security Verification Standard (MASVS). We have also retired the Internet of Things appendix, in favor of the IoT Security Verification Standard (ISVS). We thank both the OWASP Mobile Team and OWASP IoT Project Team for their support of the ASVS, and look forward to working with them in the future to provide complementary standards.

Lastly, we have de-duped and retired less impactful controls. Over time, the ASVS started being a comprehensive set of controls, but not all controls equally contribute to producing secure software. This effort to eliminate low-impact items could go further. In a future edition of the ASVS, the Common Weakness Scoring System (CWSS) will help prioritize further those controls that are truly important and those that should be retired.

As of version 4.0, the ASVS will focus solely on being the leading web apps and service standard, covering traditional and modern application architecture, agile security practices and DevSecOps culture.
-->

## Justification supplémentaire de l'approche du changement de niveau

La version 4.0 de l'ASVS décrit les niveaux comme L1 - « Minimum », L2 - « Standard » et L3 - « Avancé », ce qui implique que toutes les applications traitant des données sensibles doivent être au moins L2.

Nous avons rencontré quelques difficultés avec cette approche et les utilisateurs de la version 4.0 pourraient trouver le contexte suivant sur le changement d’approche par niveaux informatif en plus de la justification du chapitre précédent.

### Haute barrière à l’entrée

Le niveau 1 de la version 4.0 comportait plus de 100 exigences, tout comme le niveau 2, et il n'en restait que quelques-unes pour le niveau 3. Cela signifiait que même le niveau 1 nécessitait un effort considérable, auquel cas l'utilisateur était informé qu'il s'agissait du niveau « minimum » et que pour atteindre un niveau de sécurité « standard », 100 exigences supplémentaires étaient requises. Les retours des utilisateurs et de la communauté ASVS ont clairement montré que cela constituait un frein à l'adoption d'ASVS par les applications.

### L'erreur de la testabilité

L'une des principales motivations derrière l'intégration des contrôles dans la version 4.0 de L1 était la possibilité de les vérifier à l'aide de tests de type « boîte noire », ce qui n'était pas tout à fait conforme au concept de L1 comme contrôles de sécurité minimaux. D'un côté, les utilisateurs d'ASVS estimaient que L1 n'était pas suffisant pour une application sécurisée, tandis que de l'autre, ils se plaignaient de la difficulté de tester ASVS.

De plus, la testabilité est relative et parfois trompeuse. Ce n'est pas parce qu'une chose est testable qu'elle l'est forcément de manière automatisée ou triviale. Enfin, les exigences les plus testables ne sont pas forcément celles qui ont l'impact le plus important sur la sécurité ou qui sont les plus faciles à mettre en œuvre.

### Pas seulement une question de risque

L'utilisation de niveaux prescriptifs, basés sur les risques, imposant qu'une application donnée atteigne un certain niveau, semble rétrospectivement excessivement arbitraire. En réalité, l'ordre de mise en œuvre des contrôles de sécurité dépendra de facteurs tels que la réduction des risques et les efforts de mise en œuvre.
