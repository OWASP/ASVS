# ¿Qué es el ASVS?

El Estándar para la Verificación de Seguridad de Aplicaciones (ASVS) define los requerimientos de seguridad para aplicaciones y servicios web, constituye un recurso valioso para quienes desean diseñar, desarrollar y mantener aplicaciones seguras o evaluar su seguridad.

Este capítulo describe los aspectos esenciales del uso del ASVS, incluyendo su alcance, la estructura de sus niveles basados en prioridad y los principales casos de uso del estándar.

## Alcance del ASVS

El alcance del ASVS se define por su nombre: Aplicación, Seguridad, Verificación y Estándar. Establece qué requerimientos se incluyen o excluyen con el objetivo general de identificar los principios de seguridad que deben cumplirse. El alcance también considera los requerimientos de documentación, los cuales sirven de base para los requerimientos de implementación.

No existe algo como el alcance para los atacantes. Por lo tanto, los requerimientos del ASVS deben evaluarse junto con orientación en otros aspectos del ciclo de vida de las aplicaciones incluyendo los procesos de CI/CD, el alojamiento y las actividades operativas.

### Aplicación

ASVS define una "aplicación" como el producto de software en desarrollo, en el que deben integrarse controles de seguridad. ASVS no prescribe las actividades del ciclo de vida del desarrollo ni dicta cómo debe construirse la aplicación mediante un flujo (pipeline) de CI/CD; en cambio, especifica los resultados de seguridad que deben lograrse dentro del propio producto.

Los componentes que sirven, modifican o validan el tráfico HTTP, como los firewalls de aplicaciones web (WAF), los balanceadores de carga o los proxies, pueden considerarse parte de la aplicación para esos fines específicos, ya que algunos controles de seguridad dependen directamente de ellos o pueden implementarse a través de ellos. Estos componentes deben considerarse para los requerimientos relacionados con las respuestas en caché, la limitación de velocidad (rate limit) o la restricción de las conexiones entrantes y salientes según el origen y el destino.

Por el contrario, ASVS generalmente excluye los requerimientos que no son directamente relevantes para la aplicación o cuya configuración escapa a su responsabilidad. Por ejemplo, los problemas de DNS suelen ser gestionados por un equipo o función independiente.

De igual forma, si bien la aplicación es responsable de cómo consume entradas y produce salidas, si un proceso externo interactúa con la aplicación o sus datos, se considera fuera del alcance de ASVS. Por ejemplo, la copia de seguridad de la aplicación o sus datos suele ser responsabilidad de un proceso externo y no está controlada por la aplicación ni por sus desarrolladores.

### Seguridad

Todo requerimiento debe tener un impacto demostrable en la seguridad. La ausencia de un requerimiento debe resultar en una aplicación menos segura, y su implementación debe reducir la probabilidad o el impacto de un riesgo de seguridad.

Todas las demás consideraciones, como aspectos funcionales, estilo de código o requerimientos de políticas, quedan fuera del alcance.

### Verificación

El requerimiento debe ser verificable y la verificación debe resultar en una decisión de "reprobado" o "aprobado".

### Estándar

El ASVS está diseñado como un conjunto de requerimientos de seguridad que deben implementarse para cumplir con el estándar. Esto significa que los requerimientos se limitan a definir el objetivo de seguridad para lograrlo. Otra información relacionada puede construirse sobre el ASVS o vincularse mediante mapeos.

En concreto, OWASP cuenta con numerosos proyectos y el ASVS evita deliberadamente solaparse con el contenido de otros proyectos. Por ejemplo, los desarrolladores pueden preguntarse: "¿Cómo implemento un requerimiento particular en mi tecnología o entorno específico?", lo cual debería abordarse en el proyecto Cheat Sheet Series. Los verificadores pueden preguntarse: "¿Cómo pruebo este requerimiento en este entorno?", lo cual debería abordarse en el proyecto Web Security Testing Guide.

Si bien el ASVS no está destinado únicamente a expertos en seguridad, se espera que el lector tenga conocimientos técnicos para comprender el contenido o la capacidad de investigar conceptos específicos.

### Requerimiento

El término requerimiento se utiliza específicamente en ASVS ya que describe lo que debe lograrse para satisfacerlo. ASVS solo contiene requerimientos (deben) y no recomendaciones (deberían) como condición principal.

En otras palabras, las recomendaciones, ya sean una de las muchas opciones posibles para resolver un problema o consideraciones de estilo de código, no cumplen la definición de requerimiento.

Los requerimientos de ASVS buscan abordar principios de seguridad específicos sin ser demasiado específicos de la implementación o la tecnología, y al mismo tiempo, justifican por sí mismos su existencia. Esto también significa que los requerimientos no se basan en un método de verificación o implementación en particular.

### Decisiones de seguridad documentadas

En seguridad de software, planear desde el principio el diseño de seguridad y los mecanismos que se utilizarán permitirá una implementación más consistente y fiable en el producto terminado o funcionalidad.

Además, para ciertos requerimientos, la implementación será compleja y muy específica a las necesidades de la aplicación. Ejemplos comunes incluyen permisos, validación de entradas y controles de protección para diferentes niveles de datos sensibles.

Para tener esto en cuenta, en lugar de afirmaciones generales como "todos los datos deben estar cifrados" o intentar abarcar todos los posibles casos de uso en un requerimiento, se incluyeron requerimientos de documentación que exigen que el enfoque del desarrollador de la aplicación y las configuraciones para este tipo de controles se documenten. Esto puede revisarse para comprobar su idoneidad y, posteriormente, la implementación real puede compararse con la documentación para evaluar si cumple con las expectativas.

Estos requerimientos tienen como objetivo documentar las decisiones que la organización que desarrolla la aplicación ha tomado con respecto a cómo implementar ciertos requerimientos de seguridad.

Los requerimientos de documentación siempre se encuentran en la primera sección de un capítulo (aunque no todos los capítulos los incluyen) y siempre tienen un requerimiento de implementación relacionado donde las decisiones documentadas deben implementarse. La cuestión es que verificar que la documentación esté disponible y que la implementación cumple con ella, son dos actividades independientes.

Hay dos factores clave para incluir estos requerimientos. El primero es que un requerimiento de seguridad suele implicar la aplicación de reglas, por ejemplo, ¿qué tipos de archivos son permitidos para cargar?, ¿qué controles de negocio deben aplicarse?, ¿cuáles son los caracteres permitidos para un campo específico?. Estas reglas varían según la aplicación y, por lo tanto, el ASVS no puede definirlas de forma prescriptiva, ni una hoja de referencia (cheat sheet) o una respuesta más detallada servirá de ayuda en este caso. De igual manera, sin documentar estas decisiones no es posible hacer la verificación de los requerimientos que las implementan.

El segundo factor es que, para ciertos requerimientos, es importante proporcionar flexibilidad al desarrollo de aplicaciones en cuanto a cómo abordar desafíos de seguridad específicos. Por ejemplo, en versiones anteriores del ASVS, las reglas de tiempo de expiración (timeout) de sesión eran muy prescriptivas. En la práctica, muchas aplicaciones, especialmente las orientadas al consumidor, tienen reglas mucho más flexibles y prefieren implementar otros controles de mitigación. Por lo tanto los requerimientos de documentación permiten explícitamente esta flexibilidad.

Claramente, no se espera que los desarrolladores individuales tomen y documenten estas decisiones, sino que sea la organización en su conjunto la que las tome y se asegure de comunicarlas a los desarrolladores, quienes a su vez se asegurarán de seguirlas.

Proporcionar a los desarrolladores especificaciones y diseños para nuevas características y funcionalidades es parte integral del desarrollo de software. De igual manera, se espera que los desarrolladores utilicen componentes y mecanismos de interfaz de usuario comunes en lugar de simplemente tomar sus propias decisiones en cada ocasión. Por lo tanto, extender esto a la seguridad no debería considerarse sorprendente ni controvertido.

También existe flexibilidad en cuanto a cómo lograr esto. Las decisiones de seguridad pueden documentarse en un documento literal, al que se espera que los desarrolladores se refieran. Alternativamente, las decisiones de seguridad pueden documentarse e implementarse en una librería de código común que todos los desarrolladores estén obligados a usar. En ambos casos, se logra el resultado deseado.

## Niveles de verificación de seguridad de aplicaciones

El ASVS define tres niveles de verificación de seguridad, cada uno de los cuales aumenta en profundidad y complejidad. El objetivo general es que las organizaciones comiencen con el primer nivel para abordar las preocupaciones de seguridad más críticas y luego avancen a los niveles superiores según las necesidades de la organización y la aplicación. Los niveles pueden presentarse como L1, L2 y L3 en el documento y en los textos de requerimientos.

Cada nivel del ASVS indica los requerimientos de seguridad que se deben cumplir para ese nivel, y los requerimientos restantes de nivel superior se presentan como recomendaciones.

Para evitar requerimientos duplicados o requerimientos que ya no son relevantes en niveles superiores, algunos requerimientos se aplican a un nivel específico, pero tienen condiciones más estrictas para los niveles superiores.

### Evaluación de niveles

Los niveles se definen mediante una evaluación por prioridades de cada requerimiento basada en la experiencia en la implementación y prueba de requerimientos de seguridad. El enfoque principal es comparar la reducción de riesgos con el esfuerzo necesario para implementar el requerimiento. Otro factor clave es mantener una barrera de entrada baja.

La reducción de riesgos considera hasta qué punto el requerimiento reduce el nivel de riesgo de seguridad dentro de la aplicación, considerando los factores de impacto clásicos de Confidencialidad, Integridad y Disponibilidad así como considerar si se trata de una capa primaria de defensa o si se trata de defensa en profundidad (defense in depth).

Los rigurosos debates sobre los criterios y las decisiones de nivelación han dado como resultado una asignación que debería ser válida en la gran mayoría de los casos, pero se acepta que puede no ser totalmente adecuada para todas las situaciones. Esto significa que, en ciertos casos, las organizaciones podrían desear priorizar los requerimientos de un nivel superior con antelación basándose en sus propias consideraciones de riesgos.

Los tipos de requerimientos en cada nivel podrían caracterizarse de la siguiente manera.

### Nivel 1 (L1)

Este nivel contiene los requerimientos mínimos a considerar para asegurar una aplicación y representa un punto de partida crucial. Este nivel abarca aproximadamente el 20 % de los requerimientos de ASVS. El objetivo de este nivel tener la menor cantidad de requerimientos posible y así minimizar las barreras de entrada.

Estos requerimientos son generalmente críticos o básicos, requerimientos de primera capa de defensa para prevenir ataques comunes que no requieren otras vulnerabilidades o condiciones previas para ser explotables.

Además de los requerimientos de la primera capa de defensa, algunos requerimientos tienen menor impacto en niveles superiores, como los requerimientos relacionados con las contraseñas. Estos son más importantes para el Nivel 1, ya que a partir de niveles superiores, los requerimientos de autenticación multifactor cobran relevancia.

El Nivel 1 no es necesariamente susceptible de pruebas de penetración por parte de un evaluador externo sin acceso interno a la documentación o el código (como las pruebas de "caja negra"), aunque la menor cantidad de requerimientos debería facilitar su verificación.

### Nivel 2 (L2)

La mayoría de las aplicaciones deberían esforzarse por alcanzar este nivel de seguridad. Alrededor del 50% de los requerimientos del ASVS son de nivel L2, lo que significa que una aplicación debe implementar alrededor del 70% de los requerimientos del ASVS (todos los requerimientos de nivel L1 y L2) para cumplir con el nivel L2.

Estos requerimientos generalmente se refieren a ataques menos comunes o a protecciones más complejas contra ataques comunes. Pueden seguir siendo una primera capa de defensa o requerir ciertas condiciones previas para que el ataque tenga éxito.

### Nivel 3 (L3)

Este nivel debería ser el objetivo para las aplicaciones que buscan demostrar los más altos niveles de seguridad y proporciona aproximadamente el 30% restante de los requerimientos que deben cumplirse.

Los requerimientos de esta sección suelen ser mecanismos de defensa en profundidad u otros controles útiles pero difíciles de implementar.

### ¿Qué nivel alcanzar?

Los niveles basados en prioridades buscan reflejar la madurez de la seguridad de aplicaciones tanto de la organización como de la aplicación. En lugar de que el ASVS establezca de forma prescriptiva el nivel de seguridad que debe alcanzar una aplicación, una organización debe analizar sus riesgos y decidir que nivel considera que debería alcanzar en función de la sensibilidad de la aplicación y, por supuesto, de las expectativas de sus usuarios.

Por ejemplo, una startup en fase inicial que solo recopila datos sensibles limitados podría optar por el Nivel 1 para sus objetivos iniciales de seguridad pero un banco podría tener dificultades para justificar ante sus clientes un nivel inferior al 3 para su aplicación de banca en línea.

## How to use the ASVS

### The structure of the ASVS

The ASVS is made up of a total of around 350 requirements which are divided into 17 chapters, each of which is further divided into sections.

The aim of the chapter and section division is to simplify choosing or filtering out chapters and sections based on the what is relevant for the application. For example, for a machine-to-machine API, the requirements in chapter V3 related to web frontends will not be relevant. If there is no use of OAuth or WebRTC, then those chapters can be ignored as well.

### Release strategy

ASVS releases follow the pattern "Major.Minor.Patch" and the numbers provide information on what has changed within the release. In a major release, the first number will change, in a minor release, the second number will change, and in a patch release, the third number will change.

* Major release - Full reorganization, almost everything may have changed, including requirement numbers. Reevaluation for compliance will be necessary (for example, 4.0.3 -> 5.0.0).
* Minor release - Requirements may be added or removed, but overall numbering will stay the same. Reevaluation for compliance will be necessary, but should be easier (for example, 5.0.0 -> 5.1.0).
* Patch release - Requirements may be removed (for example, if they are duplicates or outdated) or made less stringent, but an application that complied with the previous release will comply with the patch release as well (for example, 5.0.0 -> 5.0.1).

The above specifically relates to the requirements in the ASVS. Changes to surrounding text and other content such as the appendices will not be considered to be a breaking change.

### Flexibility with the ASVS

Several of the points described above, such as documentation requirements and the levels mechanism, provide the ability to use the ASVS in a more flexible and organization-specific way.

Additionally, organizations are strongly encouraged to create an organization- or domain-specific fork that adjusts requirements based on the specific characteristics and risk levels of their applications. However, it is important to maintain traceability so that passing requirement 4.1.1 means the same across all versions.

Ideally, each organization should create its own tailored ASVS, omitting irrelevant sections (e.g., GraphQL, WebSockets, SOAP, if unused). An organization-specific ASVS version or supplement is also a good place to provide organization-specific implementation guidance, detailing libraries or resources to use when complying with requirements.

### How to Reference ASVS Requirements

Each requirement has an identifier in the format `<chapter>.<section>.<requirement>`, where each element is a number. For example, `1.11.3`.

* The `<chapter>` value corresponds to the chapter from which the requirement comes; for example, all `1.#.#` requirements are from the 'Encoding and Sanitization' chapter.
* The `<section>` value corresponds to the section within that chapter where the requirement appears, for example: all `1.2.#` requirements are in the 'Injection Prevention' section of the 'Encoding and Sanitization' chapter.
* The `<requirement>` value identifies the specific requirement within the chapter and section, for example, `1.2.5` which as of version 5.0.0 of this standard is:

> Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding.

Since the identifiers may change between versions of the standard, it is preferable for other documents, reports, or tools to use the following format: `v<version>-<chapter>.<section>.<requirement>`, where: 'version' is the ASVS version tag. For example: `v5.0.0-1.2.5` would be understood to mean specifically the 5th requirement in the 'Injection Prevention' section of the 'Encoding and Sanitization' chapter from version 5.0.0. (This could be summarized as `v<version>-<requirement_identifier>`.)

Note: The `v` preceding the version number in the format should always be lowercase.

If identifiers are used without including the `v<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. As the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

ASVS requirement lists are made available in CSV, JSON, and other formats which may be useful for reference or programmatic use.

### Forking the ASVS

Organizations can benefit from adopting ASVS by choosing one of the three levels or by creating a domain-specific fork that adjusts requirements per application risk level. This type of fork is encouraged, provided that it maintains traceability so that passing requirement 4.1.1 means the same across all versions.

Ideally, each organization should create its own tailored ASVS, omitting irrelevant sections (e.g., GraphQL, Websockets, SOAP, if unused). Forking should start with ASVS Level 1 as a baseline, advancing to Levels 2 or 3 based on the application’s risk.

## Use cases for the ASVS

The ASVS can be used to assess the security of an application and this is explored in more depth in the next chapter. However, several other potential uses for the ASVS (or a forked version) have been identified.

### As Detailed Security Architecture Guidance

One of the more common uses for the Application Security Verification Standard is as a resource for security architects. There are limited resources available for how to build a secure application architecture, especially with modern applications. ASVS can be used to fill in those gaps by allowing security architects to choose better controls for common problems, such as data protection patterns and input validation strategies. The architecture and documentation requirements will be particularly useful for this.

### As a Specialized Secure Coding Reference

The ASVS can be used as a basis for preparing a secure coding reference during application development, helping developers to make sure that they keep security in mind when they build software. Whilst the ASVS can be the base, organizations should prepare their own specific guidance which is clear and unified and ideally be prepared based on guidance from security engineers or security architects. As an extension to this, organizations are encouraged wherever possible to prepare approved security mechanisms and libraries that can be referenced in the guidance and used by developers.

### As a Guide for Automated Unit and Integration Tests

The ASVS is designed to be highly testable. Some verifications will be technical where as other requirements (such as the architectural and documentation requirements) may require documentation or architecture review. By building unit and integration tests that test and fuzz for specific and relevant abuse cases related to the requirements that are verifiable by technical means, it should be easier to check that these controls are operating correctly on each build. For example, additional tests can be crafted for the test suite for a login controller, testing the username parameter for common default usernames, account enumeration, brute forcing, LDAP and SQL injection, and XSS. Similarly, a test on the password parameter should include common passwords, password length, null byte injection, removing the parameter, XSS, and more.

### For Secure Development Training

ASVS can also be used to define the characteristics of secure software. Many “secure coding” courses are simply ethical hacking courses with a light smear of coding tips. This may not necessarily help developers to write more secure code. Instead, secure development courses can use the ASVS with a strong focus on the positive mechanisms found in the ASVS, rather than the Top 10 negative things not to do. The ASVS structure also provides a logical structure for walking through the different topics when securing an application.

### As a Framework for Guiding the Procurement of Secure Software

The ASVS is a great framework to help with secure software procurement or procurement of custom development services. The buyer can simply set a requirement that the software they wish to procure must be developed at ASVS level X, and request that the seller proves that the software satisfies ASVS level X.

## Applying ASVS in Practice

Different threats have different motivations. Some industries have unique information and technology assets and domain-specific regulatory compliance requirements.

Organizations are strongly encouraged to look deeply at their unique risk characteristics based on the nature of their business, and based upon that risk and business requirements determine the appropriate ASVS level.
