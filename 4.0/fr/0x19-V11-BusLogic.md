# V11 : Exigences de vérification de la logique d'entreprise

## Objectif de contrôle

Assurez-vous qu'une demande vérifiée satisfait aux exigences de haut niveau suivantes :

* Le flux logique de l'entreprise est séquentiel, traité dans l'ordre, et ne peut être contourné.
* La logique métier comprend des limites pour détecter et prévenir les attaques automatisées, comme les petits transferts de fonds continus, ou l'ajout d'un million d'amis un à la fois, etc.
* Les flux de logique commerciale de grande valeur ont pris en compte les cas d'abus et les acteurs malveillants, et disposent de protections contre l'usurpation, l'altération, la répudiation, la divulgation d'informations et les attaques par élévation de privilèges.

## V11.1 Exigences de sécurité de la logique d'entreprise

La sécurité de la logique commerciale est tellement individuelle à chaque demande qu'aucune liste de contrôle ne s'appliquera jamais. La sécurité de la logique d'entreprise doit être conçue pour protéger contre les menaces externes probables - elle ne peut pas être ajoutée en utilisant des pare-feu d'applications web ou des communications sécurisées. Nous recommandons l'utilisation de la modélisation des menaces lors des sprints de conception, par exemple en utilisant l'OWASP Cornucopia ou des outils similaires.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **11.1.1** | Vérifier que l'application traitera seulement les flux de logique métier pour un utilisateur dans l'ordre séquentiel des étapes et sans sauter d'étapes.| ✓ | ✓ | ✓ | 841 |
| **11.1.2** | Vérifier que l'application traitera seulement les flux de logiques métier, toutes les étapes étant traitées en temps humain réaliste, c'est-à-dire que les transactions ne sont pas soumises trop rapidement (effectuer par un robot).| ✓ | ✓ | ✓ | 799 |
| **11.1.3** | Vérifiez que l'application comporte des limites appropriées pour des actions ou des transactions commerciales spécifiques qui sont correctement exécutées par utilisateur. | ✓ | ✓ | ✓ | 770 |
| **11.1.4** | Vérifiez que l'application dispose de contrôles anti-automatisation suffisants pour détecter et protéger contre l'exfiltration de données, les demandes excessives de logique métiers, les téléchargements excessifs de fichiers ou les attaques par déni de service. | ✓ | ✓ | ✓ | 770 |
| **11.1.5** | Vérifier que l'application a des limites ou une validation de la logique métier pour se protéger contre les risques ou les menaces commerciales probables, identifiés à l'aide de la modélisation des menaces ou de méthodologies similaires. | ✓ | ✓ | ✓ | 841 |
| **11.1.6** | Vérifiez que la demande ne souffre pas de problèmes de "temps de contrôle au moment de l'utilisation" (TOCTOU) ou d'autres situation de compétition (race condition) pour les opérations sensibles. | | ✓ | ✓ | 367 |
| **11.1.7** | Vérifiez que les moniteurs de demande ne présentent pas d'événements ou d'activités inhabituels du point de vue de la logique métier. Par exemple, des tentatives d'effectuer des actions hors service ou des actions qu'un utilisateur normal ne tenterait jamais. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 754 |
| **11.1.8** | Vérifiez que l'application dispose d'alertes configurables lorsque des attaques automatisées ou une activité inhabituelle sont détectées. | | ✓ | ✓ | 390 |

## Références

Pour plus d'informations, voir aussi :

* [OWASP Testing Guide 4.0: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README.html)
* Anti-automation can be achieved in many ways, including the use of [OWASP AppSensor](https://github.com/jtmelton/appsensor) and [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP AppSensor](https://github.com/jtmelton/appsensor) can also help with Attack Detection and Response.
* [OWASP Cornucopia](https://owasp.org/www-project-cornucopia/)
