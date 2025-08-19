# V1 Codificación (encoding) y Sanitización

## Objetivo del control

Este capítulo aborda las fallas de seguridad más comunes en aplicaciones web relacionadas con el procesamiento inseguro de datos no confiables. Estas fallas pueden generar diversas vulnerabilidades técnicas donde los datos no confiables se interpretan según las reglas sintácticas del intérprete correspondiente.

Para las aplicaciones web modernas siempre es recomendable utilizar APIs más seguras como consultas parametrizadas, escape automático o frameworks de plantillas. De lo contrario una codificación, escape o sanitización de salida meticulosos se vuelve crucial para la seguridad de la aplicación.

La validación de entrada sirve como mecanismo de defensa en profundidad para protegerse contra contenido inesperado o peligroso. Sin embargo, dado que su objetivo principal es garantizar que el contenido entrante cumpla con las expectativas funcionales y de negocio, los requerimientos relacionados se pueden encontrar en el capítulo "Validación y lógica de negocio".

## V1.1 Arquitectura de codificación y sanitización

En las secciones siguientes se proporcionan requerimientos específicos de sintaxis o de intérprete para procesar de forma segura contenido inseguro y evitar vulnerabilidades de seguridad. Los requerimientos de esta sección abarcan el orden en que debe realizarse este procesamiento y cuando debe hacerse. También buscan garantizar que, siempre que se almacenen datos, estos permanezcan en su estado original y no se almacenen en formato codificado o de escape (por ejemplo, codificación HTML) para evitar problemas de doble codificación.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **1.1.1** | Verifique que la entrada se decodifique o se deshaga del escape en una forma canónica solo una vez, que solo se decodifique cuando se esperan datos codificados y que esto se haga antes de procesar la entrada, por ejemplo, no se realiza después de la validación o sanitización de la entrada. | 2 |
| **1.1.2** | Verifique que la aplicación realice la codificación y el escape de las salidas como paso final antes de ser utilizada por el intérprete para el cual está destinada o por el intérprete mismo. | 2 |

## V1.2 Prevención de inyección

La codificación o el escape de las salidas, realizados cerca de o junto a un contexto potencialmente peligroso, son fundamentales para la seguridad de cualquier aplicación. Normalmente la codificación y el escape de salida no se almacenan sino que se utilizan para construir la salida de manera segura para su uso inmediato en el intérprete adecuado. Intentar realizar esto demasiado pronto puede generar contenido malformado o invalidar la codificación o el escape.

En muchos casos, las librerias de software incluyen funciones seguras que realizan esto automáticamente, aunque es necesario garantizar que sean correctas para el contexto actual.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **1.2.1** | Verifique que la codificación de salida para una respuesta HTTP, un documento HTML o un documento XML sea relevante para el contexto requerido, como la codificación de los caracteres relevantes para elementos HTML, atributos HTML, comentarios HTML, CSS o encabezados HTTP para evitar cambiar la estructura del mensaje o del documento. | 1 |
| **1.2.2** | Verifique que, al crear URLs de manera dinámica, los datos no confiables se codifiquen según su contexto (ej., codificación de URL o codificación base64 para parámetros de consulta (query params) o ruta (path params)). Asegúrese que solo se permitan protocolos de URL seguros (ej., no permitir javascript: ni data:). | 1 |
| **1.2.3** | Verifique que se utilice codificación o escape de salida al crear dinámicamente contenido JavaScript (incluido JSON), para evitar cambiar el mensaje o la estructura del documento (para evitar la inyección de JavaScript y JSON). | 1 |
| **1.2.4** | Verifique que la selección de datos o las consultas a bases de datos (ej. SQL, HQL, NoSQL, Cypher) utilicen consultas parametrizadas, ORM, framework de entidades o en caso contrario, que estén protegidas contra la inyección de SQL y otros ataques de inyección en bases de datos. Esto también es relevante al escribir procedimientos almacenados. | 1 |
| **1.2.5** | Verifique que la aplicación proteja contra la inyección de comandos del sistema operativo y que las llamadas del sistema operativo utilicen consultas parametrizadas del sistema operativo o utilicen codificación de salida de línea de comandos contextual. | 1 |
| **1.2.6** | Verifique que la aplicación proteja contra vulnerabilidades de inyección LDAP o que se hayan implementado controles de seguridad específicos para prevenir la inyección LDAP. | 2 |
| **1.2.7** | Verifique que la aplicación esté protegida contra ataques de inyección XPath mediante el uso de parametrización de consultas o consultas precompiladas. | 2 |
| **1.2.8** | Verifique que los procesadores LaTeX estén configurados de forma segura (por ejemplo, no utilizando el indicador "--shell-escape") y que se utilice una lista de comandos permitidos para evitar ataques de inyección de LaTeX. | 2 |
| **1.2.9** | Verifique que la aplicación escape caracteres especiales en expresiones regulares (normalmente usando una barra invertida, backslash) para evitar que se malinterpreten como metacaracteres. | 2 |
| **1.2.10** | Verifique que la aplicación esté protegida contra inyección d CSV y fórmulas. La aplicación debe seguir las reglas de escape definidas en las secciones 2.6 y 2.7 de RFC 4180 al exportar contenido CSV. Además, al exportar a CSV u otros formatos de hoja de cálculo (como XLS, XLSX u ODF), los caracteres especiales (incluidos '=', '+', '-', '@', '\t' (tabulador) y '\0' (carácter nulo)) deben escaparse con una comilla simple si aparecen como primer carácter en un valor de campo. | 3 |

Nota: Usar consultas parametrizadas o escapar SQL no siempre es suficiente. Partes de la consulta como nombres de tablas y columnas (incluidos los nombres de columna "ORDER BY"), no se pueden escapar. Incluir datos escapados proporcionados por el usuario en estos campos puede provocar consultas fallidas o una inyección SQL.

## V1.3 Sanitización

La protección ideal contra el uso de contenido no confiable en un contexto inseguro es utilizar codificación o escape específico del contexto, que mantiene el mismo significado semántico del contenido inseguro pero lo hace seguro para su uso en ese contexto particular como se analiza con más detalle en la sección anterior.

Cuando esto no es posible, se requiere sanitización, eliminando caracteres o contenido potencialmente peligrosos. En algunos casos, esto puede cambiar el significado semántico de la entrada, pero por razones de seguridad, puede que no haya alternativa.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **1.3.1** | Verifique que toda la entrada HTML no confiable de editores WYSIWYG o similares se desinfecte mediante una biblioteca o un framework de desinfección de HTML conocido y seguro. | 1 |
| **1.3.2** | Verifique que la aplicación evite el uso de eval() u otras funciones de ejecución dinámica de código, como Spring Expression Language (SpEL). Si no hay alternativa, cualquier entrada del usuario que se incluya debe sanitizarse antes de ejecutarse. | 1 |
| **1.3.3** | Verifique que los datos que se envían a un contexto potencialmente peligroso se desinfecten de antemano para aplicar medidas de seguridad, como permitir únicamente caracteres que sean seguros para este contexto y recortar las entradas que sean demasiado largas. | 2 |
| **1.3.4** | Verifique que el contenido de gráficos vectoriales escalables (SVG) que se pueda crear mediante scripts proporcionados por el usuario esté validado o desinfectado para que contenga únicamente etiquetas y atributos (como gráficos de dibujo) que sean seguros para la aplicación, por ejemplo, que no contengan scripts ni 'foreignObject'. | 2 |
| **1.3.5** | Verifique que la aplicación desinfecte o deshabilite el contenido del lenguaje de plantillas de expresión o scripts proporcionado por el usuario, tal como Markdown, hojas de estilo CSS o XSL, BBCode o similares. | 2 |
| **1.3.6** | Verifique que la aplicación proteja contra ataques de Server-side Request Forgery (SSRF), validando datos no confiables contra una lista blanca de protocolos, dominios, rutas y puertos, y desinfectando caracteres potencialmente peligrosos antes de usar los datos para llamar a otro servicio. | 2 |
| **1.3.7** | Verifique que la aplicación proteja contra ataques de inyección de plantillas, impidiendo la creación de plantillas basadas en datos no confiables. Si no hay alternativa, cualquier dato no confiable que se incluya dinámicamente durante la creación de plantillas debe desinfectarse o validarse estrictamente. | 2 |
| **1.3.8** | Verifique que la aplicación desinfecte adecuadamente las entradas no confiables antes de usarlas en consultas de Java Naming and Directory Interface (JNDI) y que JNDI esté configurado de forma segura para evitar ataques de inyección de JNDI. | 2 |
| **1.3.9** | Verifique que la aplicación desinfecte el contenido antes de enviarlo a memcache para evitar ataques de inyección. | 2 |
| **1.3.10** | Verifique que las cadenas de formato que podrían resolverse de manera inesperada o maliciosa cuando se utilizan, se desinfecten antes de procesarlas. | 2 |
| **1.3.11** | Verifique que la aplicación desinfecte la entrada del usuario antes de pasarla a los sistemas de correo para protegerse contra la inyección de SMTP o IMAP. | 2 |
| **1.3.12** | Verifique que las expresiones regulares estén libres de elementos que provoquen un retroceso (backtracking) exponencial y asegúrese de que las entradas no confiables estén desinfectadas para mitigar los ataques ReDoS o Runaway Regex. | 3 |

## V1.4 Memoria, Cadenas y código no gestionado

The following requirements address risks associated with unsafe memory use, which generally apply when the application uses a systems language or unmanaged code.

In some cases, it may be possible to achieve this by setting compiler flags that enable buffer overflow protections and warnings, including stack randomization and data execution prevention, and that break the build if unsafe pointer, memory, format string, integer, or string operations are found.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **1.4.1** | Verify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows. | 2 |
| **1.4.2** | Verify that sign, range, and input validation techniques are used to prevent integer overflows. | 2 |
| **1.4.3** | Verify that dynamically allocated memory and resources are released, and that references or pointers to freed memory are removed or set to null to prevent dangling pointers and use-after-free vulnerabilities. | 2 |

## V1.5 Deserialización segura

The conversion of data from a stored or transmitted representation into actual application objects (deserialization) has historically been the cause of various code injection vulnerabilities. It is important to perform this process carefully and safely to avoid these types of issues.

In particular, certain methods of deserialization have been identified by programming language or framework documentation as insecure and cannot be made safe with untrusted data. For each mechanism in use, careful due diligence should be performed.

| # | Descripcion | Nivel |
| :---: | :--- | :---: |
| **1.5.1** | Verify that the application configures XML parsers to use a restrictive configuration and that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks. | 1 |
| **1.5.2** | Verify that deserialization of untrusted data enforces safe input handling, such as using an allowlist of object types or restricting client-defined object types, to prevent deserialization attacks. Deserialization mechanisms that are explicitly defined as insecure must not be used with untrusted input. | 2 |
| **1.5.3** | Verify that different parsers used in the application for the same data type (e.g., JSON parsers, XML parsers, URL parsers), perform parsing in a consistent way and use the same character encoding mechanism to avoid issues such as JSON Interoperability vulnerabilities or different URI or file parsing behavior being exploited in Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks. | 3 |

## Referencias

Para más información consulte también:

* [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
* [OWASP Web Security Testing Guide: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [RFC4180 - Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180#section-2)

Para obtener más información, específicamente sobre problemas de deserialización o análisis (parsing), consulte:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai - A New Era of SSRF Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
