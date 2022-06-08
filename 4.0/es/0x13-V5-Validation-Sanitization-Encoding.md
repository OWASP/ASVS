# V5 Validación, Desinfección y Codificación

## Objetivo de Control

La debilidad más común de la seguridad de la aplicación web es la falta de validación adecuada de la entrada procedente del cliente o del entorno antes de usarla directamente sin ninguna codificación de salida (output encoding). Esta debilidad conduce a casi todas las vulnerabilidades significativas en aplicaciones web, como el scripting entre sitios (XSS), la inyección de SQL, la inyección del intérprete, los ataques de configuración regional/Unicode, los ataques del sistema de archivos y los desbordamientos de búfer.

Asegúrese de que una aplicación verificada cumple los siguientes requisitos de alto nivel:

* La validación de entrada y la arquitectura de codificación de salida tienen un canal acordado para evitar ataques de inyección.
* Los datos de entrada están fuertemente tipados, validados, de rango o longitud comprobados, o en el peor de los casos, desinfectados o filtrados.
* Los datos de salida se codifican o escapan según el contexto de los datos lo más cerca posible del intérprete.

Con la arquitectura moderna de aplicaciones web, la codificación de salida es más importante que nunca. Es difícil proporcionar una validación de entrada sólida en determinados escenarios, por lo que el uso de una API más segura, como consultas parametrizadas, frameworks de plantillas de auto-escaping automático o codificación de salida cuidadosamente elegida, es fundamental para la seguridad de la aplicación.

## V5.1 Validación de Entrada

Controles de validación de entrada implementados correctamente, utilizando listas de permisos positivas y un fuerte tipado de datos, puede eliminar más del 90% de todos los ataques de inyección. Las comprobaciones de longitud y rango pueden reducir esto aún más. Se requiere la creación de validación de entrada segura durante la arquitectura de la aplicación, los sprints de diseño, la codificación y las pruebas de unidad e integración. Aunque muchos de estos elementos no se pueden encontrar en las pruebas de penetración, los resultados de no implementarlos se encuentran generalmente en V5.3 - Codificación de Salida y Requisitos de Prevención de Inyección. Se recomienda a los desarrolladores y revisores de código seguro que traten esta sección como si se requiriera L1 para todos los elementos para prevenir inyecciones.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.1.1** | Verifique que la aplicación tiene defensas contra los ataques de contaminación de parámetros HTTP, especialmente si el marco de la aplicación no hace ninguna distinción sobre el origen de los parámetros de solicitud (GET, POST, cookies, encabezados o variables de entorno). | ✓ | ✓ | ✓ | 235 |
| **5.1.2** | Verifique que los frameworks protegen contra ataques de asignación de parámetros masivos o que la aplicación tiene contramedidas para proteger contra la asignación de parámetros no seguros, como marcar campos privados o similares. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 915 |
| **5.1.3** | Verifique que todas las entradas (campos de formulario HTML, solicitudes REST, parámetros de URL, encabezados HTTP, cookies, archivos por lotes, fuentes RSS, etc.) se validan mediante validación positiva (lista de permitidos). ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.4** | Verifique que las estructuras de datos están fuertemente tipados y validados con un esquema definido que incluya caracteres permitidos, longitud y patrón (p. ej., números de tarjeta de crédito, direcciones de correo electrónico, números de teléfono, o validar que dos campos relacionados son razonables, como comprobar que el suburbio y el código postal coinciden). ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.5** | Verifique que las redirecciones y reenvíos de URL solo permiten destinos que aparecen en una lista de permitidos, o muestra una advertencia al redirigir a contenido potencialmente no confiable. | ✓ | ✓ | ✓ | 601 |

## V5.2 Requisitos de Sanitización y Sandboxing

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.2.1** | Verifique que todas las entradas HTML que no son de confianza de los editores WYSIWYG o similares se sanitizan correctamente con una biblioteca de sanitización HTML o una función de marco de trabajo. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.2.2** | Verifique que los datos no estructurados están sanitizados para aplicar medidas de seguridad, como caracteres permitidos y longitud. | ✓ | ✓ | ✓ | 138 |
| **5.2.3** | Verifique que la aplicación sanitiza la entrada del usuario antes de pasar a los sistemas de correo para protegerse contra la inyección SMTP o IMAP. | ✓ | ✓ | ✓ | 147 |
| **5.2.4** | Verifique que la aplicación evita el uso de eval() u otras características de ejecución de código dinámico. Cuando no hay alternativa, cualquier entrada de usuario debe sanitizarse, y ponerlo en sandbox antes de ejecutarse. | ✓ | ✓ | ✓ | 95 |
| **5.2.5** | Verifique que la aplicación protege contra ataques de inyección de plantilla asegurándose que cualquier entrada de usuario que se incluya está sanitizada o en un lugar controlado. | ✓ | ✓ | ✓ | 94 |
| **5.2.6** | Verifique que la aplicación protege contra ataques SSRF, validando o desinfectando datos que no son de confianza o metadatos de archivos HTTP, como nombres de archivo y campos de entrada de URL, y utiliza listas de protocolos permitidos, dominios, rutas de acceso y puertos. | ✓ | ✓ | ✓ | 918 |
| **5.2.7** | Verifique que la aplicación desinfecta, deshabilita o pone en sandbox el contenido proporcionado por el usuario, con scripts de gráficos vectoriales escalables (SVG; por sus siglas en inglés) especialmente en lo que se refiere a XSS resultante de scripts en línea y foreignObject. | ✓ | ✓ | ✓ | 159 |
| **5.2.8** | Verifique que la aplicación desinfecta, deshabilita o pone en sandbox el contenido proporcionado por el usuario, con expresiones en lenguaje de plantilla o script como Markdown, CSS o las hojas de estilo XSL, BBCode o similares. | ✓ | ✓ | ✓ | 94 |

## V5.3 Codificación de Salida y Prevención de Inyección

La codificación de salida cercana o adyacente al intérprete en uso es fundamental para la seguridad de cualquier aplicación. Normalmente, la codificación de salida no se conserva, pero se usa para hacer que la salida sea segura en el contexto de salida adecuado para su uso inmediato. Si no se codifica la salida, se producirá una aplicación insegura, inyectable e insegura.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.3.1** | Verifique que la codificación de salida es relevante para el intérprete y el contexto requerido. Por ejemplo, utilice codificadores específicamente para valores HTML, atributos HTML, JavaScript, parámetros de URL, encabezados HTTP, SMTP y otros según lo requiera el contexto, especialmente a partir de entradas que no sean de confianza (por ejemplo, nombres con Unicode o apóstrofes, como ねこ u O'Hara). ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.3.2** | Verifique que la codificación de salida conserva el juego de caracteres y la configuración regional elegidos por el usuario, de modo que cualquier punto de caracteres Unicode sea válido y se maneje de forma segura. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 176 |
| **5.3.3** | Verifique que el escape de salida basado en contexto, preferiblemente automatizado - o en el peor de los casos, manual - protege contra XSS reflejado, almacenado y basado en DOM. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 79 |
| **5.3.4** | Verifique que la selección de datos o las consultas de base de datos (por ejemplo, SQL, HQL, ORM, NoSQL) utilizan consultas parametrizadas, ORM, marcos de entidades o están protegidas de los ataques de inyección de base de datos. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.5** | Verifique donde los mecanismos parametrizados o más seguros no están presentes, la codificación de la salida en el contexto específico se utiliza para proteger contra ataques de inyección, como el uso de escape SQL para proteger contra la inyección SQL. ([C3, C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.6** | Verifique que la aplicación protege contra ataques de inyección de JSON, ataques de "eval" en JSON y evaluación de expresiones de JavaScript. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 830 |
| **5.3.7** | Verifique que la aplicación protege contra vulnerabilidades de inyección LDAP o que se han implementado controles de seguridad específicos para evitar la inyección LDAP. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 90 |
| **5.3.8** | Verifique que la aplicación protege contra la inyección de comandos del sistema operativo y que las llamadas al sistema operativo utilizan consultas de sistema operativo parametrizadas o utilicen codificación de salida de línea de comandos contextual. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 78 |
| **5.3.9** | Verifique que la aplicación protege contra ataques de inclusión de archivos locales (LFI) o de inclusión remota de archivos (RFI). | ✓ | ✓ | ✓ | 829 |
| **5.3.10** | Verifique que la aplicación protege contra ataques de inyección XPath o de inyección XML. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 643 |

Nota: El uso de consultas parametrizadas o el escape de SQL no siempre es suficiente; los nombres de tabla y columna, ORDER BY, etc., no se pueden escapar. La inclusión de datos proporcionados por el usuario con escape en estos campos da como resultado consultas con errores o inyección SQL.

Nota: El formato SVG permite explícitamente el script ECMA en casi todos los contextos, por lo que puede que no sea posible bloquear todos los vectores SVG XSS completamente. Si se requiere la carga SVG, se recomienda encarecidamente que se sirvan estos archivos cargados como texto/sin formato o que utilicen un dominio de contenido proporcionado por un usuario independiente para evitar que un XSS exitoso tome el control de la aplicación.

## V5.4 Memoria, Cadena y Código No Administrado

Los siguientes requisitos solo se aplicarán cuando la aplicación utilice un lenguaje de sistemas o código no administrado.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.4.1** | Verifique que la aplicación utiliza cadenas de memoria segura, copia de memoria más segura y aritmética de puntero para detectar o evitar desbordamientos de pila, búffer o heap. | | ✓ | ✓ | 120 |
| **5.4.2** | Verifique que las cadenas de formato no toman entradas potencialmente hostiles y son constantes. | | ✓ | ✓ | 134 |
| **5.4.3** | Verifique que se utilizan técnicas de validación de signos, intervalos y entradas para evitar desbordamientos de enteros. | | ✓ | ✓ | 190 |

## V5.5 Prevención de Deserialización

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.5.1** | Verifique que los objetos serializados utilizan comprobaciones de integridad o están cifrados para evitar la creación de objetos hostiles o la manipulación de datos. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 502 |
| **5.5.2** | Verifique que la aplicación restringe correctamente los analizadores XML para que solo usen la configuración más restrictiva posible y para asegurarse de que las características no seguras, como la resolución de entidades externas, están deshabilitadas para evitar ataques XML eXternal Entity (XXE). | ✓ | ✓ | ✓ | 611 |
| **5.5.3** | Verifique que la deserialización de datos que no son de confianza se evita o está protegida tanto en código personalizado como en bibliotecas de terceros (como analizadores JSON, XML y YAML). | ✓ | ✓ | ✓ | 502 |
| **5.5.4** | Verifique que al analizar JSON en exploradores o backends basados en JavaScript, JSON.parse se utiliza para analizar el documento JSON. No utilice eval() para analizar JSON. | ✓ | ✓ | ✓ | 95 |

## Referencias

Para obtener más información, véase también:

* [OWASP Testing Guide 4.0: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Cheat Sheet: Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution.html)
* [OWASP LDAP Injection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client Side Testing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client_Side_Testing/)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [XML External Entity (XXE) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)

Para obtener más información sobre el escape automático, consulte:

* [Reducing XSS by way of Automatic Context-Aware Escaping in Template Systems](https://googleonlinesecurity.blogspot.com/2009/03/reducing-xss-by-way-of-automatic.html)
* [AngularJS Strict Contextual Escaping](https://docs.angularjs.org/api/ng/service/$sce)
* [AngularJS ngBind](https://docs.angularjs.org/api/ng/directive/ngBind)
* [Angular Sanitization](https://angular.io/guide/security#sanitization-and-security-contexts)
* [Angular Template Security](https://angular.io/guide/template-syntax#content-security)
* [ReactJS Escaping](https://reactjs.org/docs/introducing-jsx.html#jsx-prevents-injection-attacks)
* [Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

Para obtener más información sobre la deserialización, consulte:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [OWASP Deserialization of Untrusted Data Guide](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)
