# V7 Traitement des erreurs et exigences de vérification de l'enregistrement

## Objectif de contrôle

L'objectif premier du traitement et de la journalisation des erreurs est de fournir des informations utiles à l'utilisateur, aux administrateurs et aux équipes de réponse aux incidents. L'objectif n'est pas de créer des quantités massives de journaux, mais des journaux de haute qualité, avec plus de signal que de bruit rejeté.

Les journaux de haute qualité contiennent souvent des données sensibles et doivent être protégés conformément aux lois ou directives locales en matière de confidentialité des données. Cela devrait inclure :

* Ne pas collecter ou enregistrer des informations sensibles, sauf si cela est spécifiquement requis.
* Veiller à ce que toutes les informations enregistrées soient traitées de manière sûre et protégées conformément à leur classification.
* Veiller à ce que les journaux ne soient pas conservés éternellement, mais qu'ils aient une durée de vie absolue aussi courte que possible.

Si les journaux contiennent des données privées ou sensibles, dont la définition varie d'un pays à l'autre, les journaux deviennent parmis les informations les plus sensibles détenues par l'application et donc très attrayantes pour les attaquants en soi.

Il est également important de s'assurer que l'application échoue en toute sécurité et que les erreurs ne divulguent pas d'informations inutiles.

## V7.1 Exigences relatives au contenu des journaux

L'enregistrement d'informations sensibles est dangereux : les journaux deviennent eux-mêmes classifiés, ce qui signifie qu'ils doivent être cryptés, faire l'objet de politiques de conservation et être divulgués lors d'audits de sécurité. Assurez-vous que seules les informations nécessaires sont conservées dans les journaux, et certainement pas les paiements, les justificatifs d'identité (y compris les jetons de session), les informations sensibles ou identifiables personnellement.

V7.1 couvre le Top 10 de l'OWASP 2017:A10. Comme 2017:A10 et cette section ne sont pas testables tests d'intrusions, il est important pour :

* Les développeurs de s'assurer de la conformité totale avec cette section, comme si tous les éléments étaient marqués comme L1
* Tests de pénétration de valider la conformité totale de tous les éléments de la V7.1 par le biais d'un entretien, de captures d'écran ou d'une affirmation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.1.1** | Vérifiez que la demande n'enregistre pas les références ou les détails de paiement. Les jetons de session ne doivent être stockés dans les journaux que sous une forme hachée et irréversible. ([C9, C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 532 |
| **7.1.2** | Vérifiez que l'application n'enregistre pas d'autres données sensibles telles que définies par les lois locales sur la protection de la vie privée ou la politique de sécurité pertinente. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 532 |
| **7.1.3** | Vérifiez que l'application enregistre les événements pertinents pour la sécurité, y compris les événements d'authentification réussis et échoués, les échecs de contrôle d'accès, les échecs de désérialisation et les échecs de validation des entrées. ([C5, C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 778 |
| **7.1.4** | Vérifiez que chaque événement consigné dans le journal contient les informations nécessaires pour permettre une enquête détaillée sur la chronologie de l'événement. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 778 |

## V7.2 Exigences de traitement des journaux

Il est essentiel d'enregistrer en temps utile les événements de vérification, le triage et l'escalade. Assurez-vous que les journaux de l'application sont clairs et peuvent être facilement surveillés et analysés, soit localement, soit envoyés à un système de surveillance à distance.

V7.2 couvre le Top 10 de l'OWASP 2017:A10. Comme 2017:A10 et cette section ne sont pas testables, il est important pour :

* Les développeurs de s'assurer de la conformité totale avec cette section, comme si tous les éléments étaient marqués comme L1
* Tests de pénétration de valider la conformité totale de tous les éléments de la V7.2 par le biais d'un entretien, de captures d'écran ou d'une affirmation

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.2.1** | Vérifiez que toutes les décisions d'authentification sont consignées, sans stocker d'identifiants de session ou de mots de passe sensibles. Cela devrait inclure les demandes avec les métadonnées pertinentes nécessaires aux enquêtes de sécurité.  | | ✓ | ✓ | 778 |
| **7.2.2** | Vérifiez que toutes les décisions de contrôle d'accès peuvent être enregistrées et que toutes les décisions qui ont échoué sont enregistrées. Cela devrait inclure les demandes avec les métadonnées pertinentes nécessaires aux enquêtes de sécurité. | | ✓ | ✓ | 285 |

## V7.3 Exigences en matière de protection des journaux

Les journaux qui peuvent être trivialement modifiés ou supprimés sont inutiles pour les enquêtes et les poursuites. La divulgation des journaux peut révéler des détails internes sur l'application ou les données qu'elle contient. Il convient de prendre des précautions pour protéger les journaux contre toute divulgation, modification ou suppression non autorisée.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.3.1** | Vérifiez que l'application encode correctement les données fournies par l'utilisateur pour éviter l'injection de logs. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 117 |
| **7.3.2** | [SUPPRIMÉ, DOUBLON AVEC L'EXIGENCE 7.3.1] | | | | |
| **7.3.3** | Vérifiez que les journaux de sécurité sont protégés contre tout accès et toute modification non autorisés. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 200 |
| **7.3.4** | Vérifiez que les sources de temps sont synchronisées avec l'heure et le fuseau horaire corrects. Envisager sérieusement de n'enregistrer les données qu'en UTC si les systèmes sont globaux pour faciliter l'analyse criminalistique post-incident. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

Remarque : L'encodage des journaux (7.3.1) est difficile à tester et à examiner à l'aide d'outils dynamiques automatisés et de tests de pénétration, mais les architectes, les développeurs et les réviseurs de code source devraient le considérer comme une exigence de niveau 1.

## V7.4 Traitement des erreurs

L'objectif du traitement des erreurs est de permettre à l'application de fournir des événements pertinents pour la sécurité en vue de la surveillance, du triage et de l'escalade. L'objectif n'est pas de créer des journaux. Lorsque vous enregistrez des événements liés à la sécurité, assurez-vous que le journal a un but et qu'il peut être distingué par le SIEM ou un logiciel d'analyse.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.4.1** | Vérifiez qu'un message générique s'affiche lorsqu'une erreur inattendue ou sensible à la sécurité se produit, éventuellement avec un identifiant unique que le personnel de soutien peut utiliser pour enquêter.  ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 210 |
| **7.4.2** | Vérifiez que le traitement des exceptions est utilisé dans toute le code source pour tenir compte des conditions d'erreur prévues et imprévues. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 544 |
| **7.4.3** | Vérifiez qu'un gestionnaire d'erreurs de "dernier recours" est défini, qui prendra en compte toutes les exceptions non traitées. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 431 |

Note : Certains langages, tels que Swift et Go - et selon la pratique courante de conception - de nombreux langages fonctionnels, ne prennent pas en charge les exceptions ou les gestionnaires d'événements de dernier recours. Dans ce cas, les architectes et les développeurs doivent utiliser un modèle, un langage ou un cadre convivial pour s'assurer que les applications peuvent gérer en toute sécurité des événements exceptionnels, inattendus ou liés à la sécurité.

## Références

Pour plus d'informations, voir aussi :

* [OWASP Testing Guide 4.0 content: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README.html)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
