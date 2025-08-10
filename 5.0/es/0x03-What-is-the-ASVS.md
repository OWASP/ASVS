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

## Como usar el ASVS

### La estructura del ASVS

El ASVS consta de un total de aproximadamente 350 requerimientos divididos en 17 capítulos, cada uno de los cuales se subdivide en secciones.

El objetivo de la división en capítulos y secciones es simplificar la selección o el filtrado de capítulos y secciones según su relevancia para la aplicación. Por ejemplo, para una API máquina a máquina los requerimientos del capítulo V3 relacionados con las interfaces web no serán relevantes. Si no se utiliza OAuth ni WebRTC, estos capítulos también pueden ignorarse.

### Estrategia de versiones

Las versiones de ASVS siguen el patrón "Mayor.Menor.Parche" y los números indican qué ha cambiado en la versión. En una versión mayor, cambia el primer número; en una menor, el segundo; y en una versión de parche, cambia el tercer número.

* Versión mayor: Reorganización completa; prácticamente todo puede haber cambiado, incluyendo la numeración de los requerimientos. Será necesaria una reevaluación para verificar su cumplimiento (por ejemplo, 4.0.3 -> 5.0.0).
* Versión menor: Se pueden añadir o eliminar requerimientos, pero la numeración general se mantendrá. Será necesaria una reevaluación para verificar su cumplimiento, pero debería ser más sencilla (por ejemplo, 5.0.0 -> 5.1.0).
* Versión de parche: Requerimientos podrían eliminarse (por ejemplo, si son duplicados u obsoletos) o hacerse menos estrictos, pero una aplicación que cumplió con la versión anterior también cumplirá con la versión de parche (por ejemplo, 5.0.0 -> 5.0.1).

Lo anterior se relaciona específicamente con los requerimientos del ASVS. Los cambios en el texto circundante y otros contenidos, como los apéndices, no se considerarán cambios mayores.

### Flexibilidad en el ASVS

Varios de los puntos descritos anteriormente, como los requerimientos de documentación y el mecanismo de niveles, permiten utilizar el ASVS de forma más flexible y específica para cada organización.

Además, se recomienda encarecidamente a las organizaciones crear una versión específica para su organización o dominio que ajuste los requerimientos en función de las características y los niveles de riesgo específicos de sus aplicaciones. Sin embargo, es importante mantener la trazabilidad para que el cumplimiento del requisito 4.1.1 se aplique de forma uniforme en todas las versiones.

Idealmente, cada organización debería crear su propio ASVS personalizado omitiendo las secciones irrelevantes (por ejemplo, GraphQL, WebSockets o SOAP si no se utilizan). Una versión del ASVS específico para cada organización también es un buen lugar para proporcionar una guía de implementación específica para cada organización, detallando las librerias o los recursos que se pueden utilizar para cumplir con los requerimientos.

### Cómo referenciar los requerimientos del ASVS

Cada requerimiento tiene un identificador con el formato `<capítulo>.<sección>.<requerimiento>`, donde cada elemento es un número. Por ejemplo, `1.11.3`.

* El valor `<capítulo>` corresponde al capítulo del que proviene el requerimiento; por ejemplo, todos los requerimientos `1.#.#` pertenecen al capítulo 'Codificación y Sanitización'.
* El valor `<sección>` corresponde a la sección dentro de ese capítulo donde aparece el requerimiento; por ejemplo, todos los requerimientos `1.2.#` se encuentran en la sección 'Prevención de Inyecciones' del capítulo 'Codificación y Sanitización'.
* El valor `<requerimiento>` identifica el requerimiento específico dentro del capítulo y la sección; por ejemplo, `1.2.5`, que a partir de la versión 5.0.0 de este estándar es:

> Verifique que la aplicación protege contra la inyección de comandos del sistema operativo (OS command injection) y que las llamadas del sistema operativo (system calls) utilicen consultas del sistema operativo parametrizadas o utilicen codificación de salida de línea de comandos contextual.

Dado que los identificadores pueden cambiar entre versiones del estándar, es preferible que otros documentos, informes o herramientas utilicen el siguiente formato: `v<versión>-<capítulo>.<sección>.<requerimiento>`, donde: 'versión' es la etiqueta de versión de ASVS. Por ejemplo: `v5.0.0-1.2.5` se entendería como el quinto requerimiento de la sección 'Prevención de inyecciones' del capítulo 'Codificación y Sanitización' de la versión 5.0.0. (Esto podría resumirse como `v<versión>-<identificador_de_requerimiento>`).

Nota: La `v` que precede al número de versión en el formato debe escribirse siempre en minúscula.

Si se utilizan identificadores sin incluir el elemento `v<versión>`, se debe asumir que se refieren al contenido más reciente del Estándar para la Verificación de Seguridad de Aplicaciones (ASVS). A medida que el estándar evoluciona y cambia esto se vuelve problemático por lo que los desarrolladores deberían incluir el elemento de versión.

Las listas de requerimientos del ASVS están disponibles en CSV, JSON y otros formatos que pueden resultar útiles como referencia o uso programático.

### Hacer una copia del ASVS (forking)

Las organizaciones pueden beneficiarse de la adopción del ASVS eligiendo uno de los tres niveles o creando una copia (fork) específica para cada dominio que ajuste los requerimientos según el nivel de riesgo de sus aplicaciones. Se recomienda este tipo de copia siempre que mantenga la trazabilidad para que el cumplimiento del requisito 4.1.1 sea igual en todas las versiones.

Idealmente, cada organización debería crear su propio ASVS personalizado, omitiendo las secciones irrelevantes (por ejemplo, GraphQL, Websockets, SOAP, si no se utilizan). La copia (fork) debería comenzar con el nivel L1 de ASVS como base, y avanzar a los niveles L2 o L3 según el riesgo de la aplicación.

## Casos de uso para el ASVS

El ASVS puede utilizarse para evaluar la seguridad de una aplicación, tema que se explora con más profundidad en el siguiente capítulo. Sin embargo, se han identificado otros usos potenciales para el ASVS (o una versión específica).

### Como una guía detallada sobre arquitectura de seguridad

Uno de los usos más comunes del Estándar para la Verificación de Seguridad de Aplicaciones (ASVS) es como recurso para arquitectos de seguridad. Existen recursos limitados para construir una arquitectura de aplicaciones segura especialmente con aplicaciones modernas. El ASVS puede utilizarse para subsanar estas deficiencias permitiendo a los arquitectos de seguridad elegir mejores controles para problemas comunes como patrones de protección de datos y estrategias de validación de entradas. Los requerimientos de arquitectura y documentación serán especialmente útiles para esto.

### Como referencia especializada en codificación segura

El ASVS puede utilizarse como base para preparar una referencia de codificación segura durante el desarrollo de aplicaciones, lo que ayuda a los desarrolladores a garantizar que tengan en cuenta la seguridad al crear software. Si bien el ASVS puede ser la base, las organizaciones deben elaborar su propia guía específica, clara y unificada, idealmente basada en la orientación de ingenieros o arquitectos de seguridad. Además, se anima a las organizaciones, siempre que sea posible, a preparar mecanismos y librerias de seguridad aprobados que puedan ser referenciados en la guía y utilizados por los desarrolladores.

### Como guía para pruebas unitarias y de integración automatizadas

El ASVS está diseñado para ser altamente testeable. Algunas verificaciones serán técnicas, mientras que otros requerimientos (como los de arquitectura y documentación) pueden requerir una revisión de la documentación o la arquitectura. Al crear pruebas unitarias y de integración que prueben y analicen casos de abuso específicos y relevantes relacionados con los requerimientos que sean verificables técnicamente, debería ser más fácil verificar el correcto funcionamiento de estos controles en cada compilación. Por ejemplo, se pueden crear pruebas adicionales para el conjunto de pruebas de un controlador de inicio de sesión, probando el parámetro de nombre de usuario para nombres de usuario predeterminados comunes, enumeración de cuentas, fuerza bruta, inyección de LDAP, SQL y XSS. De igual forma, una prueba del parámetro de contraseña debe incluir contraseñas comunes, longitud de contraseña, inyección de bytes nulos, eliminación del parámetro, XSS, etc.

### Para una formación en desarrollo seguro

El ASVS también puede utilizarse para definir las características del software seguro. Muchos cursos de “codificación segura” son simplemente cursos de hacking ético con algunos consejos de programación. Esto no necesariamente ayuda a los desarrolladores a escribir código más seguro. En cambio, los cursos de desarrollo seguro pueden utilizar el ASVS con un enfoque especial en los mecanismos positivos que se encuentran en él en lugar de en las 10 principales desventajas que no se deben hacer. La estructura del ASVS también proporciona una estructura lógica para explicar los diferentes temas al proteger una aplicación.

### Como marco para orientar la adquisición de software seguro

El ASVS es un excelente marco para facilitar la adquisición segura de software o la contratación de servicios de desarrollo a medida. El comprador puede simplemente exigir que el software que desea adquirir se desarrolle según el nivel X del ASVS y solicitar al vendedor que demuestre que el software cumple dicho nivel.

## Aplicación del ASVS en la práctica

Cada amenaza tiene su propia motivación. Algunas industrias cuentan con activos de información y tecnología únicos y requerimientos de cumplimiento normativo específicos de cada sector.

Se recomienda encarecidamente a las organizaciones que analicen en profundidad sus características de riesgo específicas según la naturaleza de su negocio y, en función de ese riesgo y los requerimientos del negocio, determinen el nivel de ASVS adecuado.
