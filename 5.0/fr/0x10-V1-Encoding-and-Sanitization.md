# V1 Encodage et nettoyage

## Objectif du contrôle

Ce chapitre aborde les failles de sécurité les plus courantes des applications web liées au traitement non sécurisé de données non fiables. Ces failles peuvent entraîner diverses vulnérabilités techniques, où les données non fiables sont interprétées selon les règles syntaxiques de l'interpréteur concerné.

Pour les applications web modernes, il est toujours préférable d'utiliser des API plus sûres, telles que les requêtes paramétrées, l'échappement automatique ou les Framework de création de modèles. Dans le cas contraire, un encodage, un échappement ou une purification de sortie soigneusement effectués deviennent essentiels à la sécurité de l'application.

La validation des entrées constitue un mécanisme de défense en profondeur contre les contenus inattendus ou dangereux. Cependant, son objectif principal étant de garantir que le contenu entrant répond aux attentes fonctionnelles et métier, les exigences y afférentes sont décrites dans le chapitre « Validation et logique métier ».

## V1.1 Architecture d'encodage et de nettoyage

Les sections ci-dessous présentent les exigences spécifiques à la syntaxe ou à l'interpréteur pour traiter en toute sécurité les contenus non sécurisés afin d'éviter les failles de sécurité. Ces exigences précisent l'ordre et le lieu de traitement. Elles visent également à garantir que les données stockées conservent leur état d'origine et ne sont pas stockées sous une forme encodée ou échappée (par exemple, encodage HTML), afin d'éviter les problèmes de double encodage.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **1.1.1** | Vérifiez que l'entrée est décodée ou non échappée dans une forme canonique une seule fois, elle n'est décodée que lorsque des données codées sous cette forme sont attendues, et que cela est fait avant de traiter davantage l'entrée, par exemple, elle n'est pas effectuée après la validation ou la désinfection de l'entrée. | 2 |
| **1.1.2** | Vérifiez que l'application effectue l'encodage et l'échappement de sortie soit comme étape finale avant d'être utilisée par l'interpréteur pour lequel elle est destinée, soit par l'interpréteur lui-même. | 2 |

## V1.2 Prévention des injections

L'encodage ou l'échappement de sortie, effectué à proximité ou à proximité d'un contexte potentiellement dangereux, est essentiel à la sécurité de toute application. Généralement, l'encodage et l'échappement de sortie ne sont pas conservés, mais servent à sécuriser la sortie pour une utilisation immédiate dans l'interpréteur approprié. Une tentative d'exécution trop précoce peut entraîner une altération du contenu ou rendre l'encodage ou l'échappement inefficaces.

Dans de nombreux cas, les bibliothèques logicielles incluent des fonctions sûres ou plus sûres qui exécutent cela automatiquement, même s'il est nécessaire de s'assurer qu'elles sont correctes pour le contexte actuel.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **1.2.1** | Vérifiez que l'encodage de sortie d'une réponse HTTP, d'un document HTML ou d'un document XML est pertinent pour le contexte requis, comme l'encodage des caractères pertinents pour les éléments HTML, les attributs HTML, les commentaires HTML, les CSS ou les champs d'en-tête HTTP, pour éviter de modifier la structure du message ou du document. | 1 |
| **1.2.2** | Lors de la création dynamique d'URL, vérifiez que les données non fiables sont cenodées en fonction de leur contexte (par exemple, encodage d'URL ou encodage base64url pour les paramètres de requête ou de chemin). Assurez-vous que seuls les protocoles d'URL sûrs sont autorisés (par exemple, interdire javascript: ou data:). | 1 |
| **1.2.3** | Vérifiez que l'encodage ou l'échappement de sortie est utilisé lors de la création dynamique de contenu JavaScript (y compris JSON), pour éviter de modifier la structure du message ou du document (pour éviter l'injection JavaScript et JSON). | 1 |
| **1.2.4** | Vérifiez que la sélection de données ou les requêtes de base de données (par exemple, SQL, HQL, NoSQL, Cypher) utilisent des requêtes paramétrées, des ORM, des Framework d'entités ou sont protégées contre les injections SQL et autres attaques par injection de base de données. Ceci est également pertinent lors de l'écriture de procédures stockées. | 1 |
| **1.2.5** | Vérifiez que l’application protège contre l’injection de commandes du système d’exploitation et que les appels du système d’exploitation utilisent des requêtes du système d’exploitation paramétrées ou utilisent un encodage de sortie de ligne de commande contextuelle. | 1 |
| **1.2.6** | Vérifiez que l’application protège contre les vulnérabilités d’injection LDAP ou que des contrôles de sécurité spécifiques pour empêcher l’injection LDAP ont été mis en œuvre. | 2 |
| **1.2.7** | Vérifiez que l’application est protégée contre les attaques par injection XPath en utilisant la paramétrisation des requêtes ou des requêtes précompilées. | 2 |
| **1.2.8** | Vérifiez que les processeurs LaTeX sont configurés de manière sécurisée (par exemple, en n'utilisant pas l'indicateur « --shell-escape ») et qu'une liste blanche de commandes est utilisée pour empêcher les attaques par injection LaTeX. | 2 |
| **1.2.9** | Vérifiez que l'application échappe les caractères spéciaux dans les expressions régulières (généralement à l'aide d'une barre oblique inverse) pour éviter qu'ils ne soient mal interprétés comme des métacaractères. | 2 |
| **1.2.10** | Vérifiez que l'application est protégée contre les injections de formules et les fichiers CSV. Elle doit respecter les règles d'échappement définies dans les sections 2.6 et 2.7 de la RFC 4180 lors de l'exportation de contenu CSV. De plus, lors de l'exportation au format CSV ou vers d'autres formats de tableur (tels que XLS, XLSX ou ODF), les caractères spéciaux (notamment « = », « + », « - », « @ », « \t » (tabulation) et « \0 » (caractère null)) doivent être protégés par une apostrophe s'ils apparaissent en premier dans une valeur de champ. | 3 |

Remarque : L'utilisation de requêtes paramétrées ou l'échappement SQL ne sont pas toujours suffisants. Les parties de requête telles que les noms de table et de colonne (y compris les noms de colonne « ORDER BY ») ne peuvent pas être échappées. L'inclusion de données utilisateur échappées dans ces champs entraîne l'échec des requêtes ou une injection SQL.

## V1.3 Nettoyage

La protection idéale contre l'utilisation de contenu non fiable dans un contexte dangereux est d'utiliser un encodage ou un échappement spécifique au contexte, qui conserve la même signification sémantique du contenu dangereux mais le rend sûr pour une utilisation dans ce contexte particulier, comme expliqué plus en détail dans la section précédente.

Lorsque cela n'est pas possible, un nettoyage devient nécessaire, supprimant les caractères ou contenus potentiellement dangereux. Dans certains cas, cela peut modifier la signification sémantique de la saisie, mais pour des raisons de sécurité, il peut n'y avoir aucune autre solution.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **1.3.1** | Vérifiez que toutes les entrées HTML non fiables provenant d'éditeurs WYSIWYG ou similaires sont nettoyées à l'aide d'une bibliothèque ou d'une fonctionnalité de Framework de nettoyage HTML bien connue et sécurisée. | 1 |
| **1.3.2** | Vérifiez que l'application évite d'utiliser eval() ou d'autres fonctionnalités d'exécution de code dynamique telles que Spring Expression Language (SpEL). En l'absence d'alternative, toute saisie utilisateur incluse doit être nettoyée avant d'être exécutée. | 1 |
| **1.3.3** | Vérifiez que les données transmises à un contexte potentiellement dangereux sont préalablement nettoyées pour appliquer des mesures de sécurité, telles que l'autorisation uniquement des caractères sûrs pour ce contexte et la suppression des entrées trop longues. | 2 |
| **1.3.4** | Vérifiez que le contenu scriptable Scalable Vector Graphics (SVG) fourni par l'utilisateur est validé ou nettoyé pour contenir uniquement des balises et des attributs (tels que des graphiques de dessin) qui sont sûrs pour l'application, par exemple, ne contiennent pas de scripts et d'objets étrangers. | 2 |
| **1.3.5** | Vérifiez que l'application nettoie ou désactive le contenu du langage de modèle d'expression ou de script fourni par l'utilisateur, tel que les feuilles de style Markdown, CSS ou XSL, BBCode ou similaire. | 2 |
| **1.3.6** | Vérifiez que l'application protège contre les attaques de falsification de requête côté serveur (SSRF), en validant les données non fiables par rapport à une liste blanche de protocoles, de domaines, de chemins et de ports et en nettoyant les caractères potentiellement dangereux avant d'utiliser les données pour appeler un autre service. | 2 |
| **1.3.7** | Vérifiez que l'application se protège contre les attaques par injection de modèles en interdisant la création de modèles basés sur des entrées non fiables. En l'absence d'alternative, toute entrée non fiable incluse dynamiquement lors de la création du modèle doit être nettoyée ou rigoureusement validée. | 2 |
| **1.3.8** | Vérifiez que l’application nettoie correctement les entrées non fiables avant utilisation dans les requêtes Java Naming and Directory Interface (JNDI) et que JNDI est configuré de manière sécurisée pour empêcher les attaques par injection JNDI. | 2 |
| **1.3.9** | Vérifiez que l’application nettoie le contenu avant qu’il ne soit envoyé à memcache pour éviter les attaques par injection. | 2 |
| **1.3.10** | Vérifiez que les chaînes de format susceptibles d'être résolues de manière inattendue ou malveillante lors de leur utilisation sont nettoyées avant d'être traitées. | 2 |
| **1.3.11** | Vérifiez que l'application nettoie les entrées utilisateur avant de les transmettre aux systèmes de messagerie pour se protéger contre l'injection SMTP ou IMAP. | 2 |
| **1.3.12** | Vérifiez que les expressions régulières sont exemptes d'éléments provoquant un retour en arrière exponentiel et assurez-vous que les entrées non fiables sont nettoyées pour atténuer les attaques ReDoS ou Runaway Regex. | 3 |

## V1.4 Mémoire, chaîne et code non géré

Les exigences suivantes traitent des risques associés à une utilisation non sécurisée de la mémoire, qui s’appliquent généralement lorsque l’application utilise un langage système ou un code non managé.

Dans certains cas, il peut être possible d'y parvenir en définissant des indicateurs de compilateur qui activent les protections et les avertissements contre les dépassements de tampon, y compris la randomisation de la pile et la prévention de l'exécution des données, et qui interrompent la construction si des opérations de pointeur, de mémoire, de chaîne de format, d'entier ou de chaîne non sécurisées sont trouvées.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **1.4.1** | Vérifiez que l'application utilise une chaîne de mémoire sécurisée, une copie de mémoire plus sûre et une arithmétique de pointeur pour détecter ou empêcher les débordements de pile, de tampon ou de tas. | 2 |
| **1.4.2** | Vérifiez que les techniques de validation du signe, de la plage et de l’entrée sont utilisées pour éviter les dépassements d’entiers. | 2 |
| **1.4.3** | Vérifiez que la mémoire et les ressources allouées dynamiquement sont libérées et que les références ou les pointeurs vers la mémoire libérée sont supprimés ou définis sur null pour éviter les pointeurs suspendus et les vulnérabilités d'utilisation après libération. | 2 |

## V1.5 Désérialisation sécurisée

La conversion de données stockées ou transmises en objets applicatifs réels (désérialisation) a toujours été à l'origine de diverses vulnérabilités par injection de code. Il est important d'effectuer ce processus avec précaution et en toute sécurité pour éviter ce type de problèmes.

En particulier, certaines méthodes de désérialisation ont été identifiées par la documentation des langages de programmation ou des Framework comme étant non sécurisées et ne peuvent être sécurisées avec des données non fiables. Pour chaque mécanisme utilisé, une vérification rigoureuse doit être effectuée.

| # | Description | Niveau |
| :---: | :--- | :---: |
| **1.5.1** | Vérifiez que l'application configure les analyseurs XML pour utiliser une configuration restrictive et que les fonctionnalités non sécurisées telles que la résolution d'entités externes sont désactivées pour empêcher les attaques XML eXternal Entity (XXE). | 1 |
| **1.5.2** | Vérifiez que la désérialisation des données non fiables garantit une gestion sécurisée des entrées, par exemple en utilisant une liste blanche de types d'objets ou en limitant les types d'objets définis par le client, afin d'empêcher les attaques par désérialisation. Les mécanismes de désérialisation explicitement définis comme non sécurisés ne doivent pas être utilisés avec des entrées non fiables. | 2 |
| **1.5.3** | Vérifiez que les différents analyseurs utilisés dans l'application pour le même type de données (par exemple, les analyseurs JSON, les analyseurs XML, les analyseurs d'URL) effectuent l'analyse de manière cohérente et utilisent le même mécanisme d'encodage de caractères pour éviter des problèmes tels que les vulnérabilités d'interopérabilité JSON ou un comportement d'analyse d'URI ou de fichier différent exploité dans les attaques d'inclusion de fichiers à distance (RFI) ou de falsification de requête côté serveur (SSRF). | 3 |

## Références

Pour plus d'informations, voir également :

* [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
* [OWASP Web Security Testing Guide: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [RFC4180 - Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180#section-2)

Pour plus d'informations, notamment sur les problèmes de désérialisation ou d'analyse, veuillez consulter :

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai - A New Era of SSRF Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
