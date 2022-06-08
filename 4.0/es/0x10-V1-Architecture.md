# V1 Arquitectura, Diseño y Modelado de Amenazas

## Objetivo de Control

La arquitectura de seguridad casi se ha convertido en un arte perdido en muchas organizaciones. Los días del arquitecto empresarial han pasado en la era de DevSecOps. El campo de la seguridad de las aplicaciones debe ponerse al día y adoptar principios de seguridad ágiles, al tiempo que reintroduce los principios de arquitectura de seguridad líderes a los profesionales del software. La arquitectura no es una implementación, sino una forma de pensar sobre un problema que tiene potencialmente muchas respuestas diferentes, y no solo una respuesta "correcta". Con demasiada frecuencia, la seguridad se ve como inflexible y exigente que los desarrolladores corrijan el código de una manera particular, cuando los desarrolladores pueden conocer una manera mucho mejor de resolver el problema. No hay una solución única y sencilla para la arquitectura, y pretender lo contrario es un flaco favor al campo de la ingeniería de software.

Es probable que una implementación específica de una aplicación web se revise continuamente a lo largo de su vida útil, pero es probable que la arquitectura general rara vez cambie, pero evoluciona lentamente. La arquitectura de seguridad es idéntica: necesitamos autenticación hoy, necesitaremos autenticación mañana y la necesitaremos dentro de cinco años. Si tomamos decisiones acertadas hoy en día, podemos ahorrar mucho esfuerzo, tiempo y dinero si seleccionamos y reutilizamos soluciones que cumplen con la arquitectura. Por ejemplo, hace una década, la autenticación multifactor rara vez se implementaba.

Si los desarrolladores hubieran invertido en un único modelo de proveedor de identidad seguro, como la identidad federada SAML, el proveedor de identidades podría actualizarse para incorporar nuevos requisitos, como el cumplimiento de NIST 800-63, sin cambiar las interfaces de la aplicación original. Si muchas aplicaciones compartían la misma arquitectura de seguridad y, por lo tanto, ese mismo componente, todas se benefician de esta actualización a la vez. Sin embargo, SAML no siempre permanecerá como la mejor o más adecuada solución de autenticación: es posible que deba intercambiarse para otras soluciones a medida que cambian los requisitos. Cambios como este son complicados y costosos como para requerir una reescritura completa, o totalmente imposible sin arquitectura de seguridad.

En este capítulo, el ASVS cubre los aspectos principales de cualquier arquitectura de seguridad sólida: disponibilidad, confidencialidad, integridad del procesamiento, no repudio y privacidad. Cada uno de estos principios de seguridad debe estar integrado y ser innato para todas las aplicaciones. Es fundamental "desplazar a la izquierda", comenzando con la habilitación del desarrollador con listas de verificación de codificación seguras, tutoría y capacitación, codificación y pruebas, creación, implementación, configuración y operaciones, y terminando con pruebas independientes de seguimiento para asegurar que todos los controles de seguridad están presentes y funcionales. El último paso solía ser todo lo que hacíamos como industria, pero ya no es suficiente cuando los desarrolladores insertan código en producción decenas o cientos de veces al día. Los profesionales de la seguridad de las aplicaciones deben mantenerse al día con técnicas ágiles, lo que significa adoptar herramientas de desarrollo, aprender a codificar, y trabajar con desarrolladores en lugar de criticar el proyecto meses después de que todos los demás siguieron adelante.

## V1.1 Ciclo de Vida de Desarrollo de Software Seguro

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.1.1** | Verifique el uso de un ciclo de vida de desarrollo de software seguro que aborde la seguridad en todas las etapas del desarrollo. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **1.1.2** | Verifique el uso del modelado de amenazas para cada cambio de diseño o planificación de sprint para identificar amenazas, planificar contramedidas, facilitar respuestas de riesgo adecuadas y guiar las pruebas de seguridad. | | ✓ | ✓ | 1053 |
| **1.1.3** | Verifique que todas las historias y características de usuario contienen restricciones de seguridad funcionales, como por ejemplo: "Como usuario, debería poder ver y editar mi perfil. No debería ser capaz de ver o editar el perfil de nadie más" | | ✓ | ✓ | 1110 |
| **1.1.4** | Verifique la documentación y la justificación de todos los límites de confianza, componentes y flujos de datos significativos de la aplicación. | | ✓ | ✓ | 1059 |
| **1.1.5** | Verifique la definición y el análisis de seguridad de la arquitectura de alto nivel de la aplicación y todos los servicios remotos conectados. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1059 |
| **1.1.6** | Verifique la implementación de controles de seguridad centralizados, simples (economía del diseño), comprobados, seguros y reutilizables para evitar controles duplicados, faltantes, ineficaces o inseguros. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 637 |
| **1.1.7** | Verifique la disponibilidad de una lista de comprobación de codificación segura, requisitos de seguridad, directriz o directiva para todos los desarrolladores y evaluadores. | | ✓ | ✓ | 637 |

## V1.2 Arquitectura de Autenticación

Al diseñar la autenticación, no importa si tiene una autenticación multifactor habilitada para hardware fuerte si un atacante puede restablecer una cuenta llamando a un centro de llamadas y respondiendo a preguntas conocidas. Al probar la identidad, todas las vías de autenticación deben tener la misma fuerza.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.2.1** | Verifique el uso de cuentas de sistema operativo únicas o especiales con privilegios bajos para todos los componentes, servicios y servidores de la aplicación. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 250 |
| **1.2.2** | Verifique que las comunicaciones entre los componentes de la aplicación, incluidas las API, el middleware y las capas de datos, se autentican. Los componentes deben tener los mínimos privilegios necesarios. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 306 |
| **1.2.3** | Verifique que la aplicación utiliza un único mecanismo de autenticación comprobado que se sabe que es seguro, se puede ampliar para incluir una autenticación segura y tiene suficiente logging y supervisión para detectar abuso de cuenta o brechas. | | ✓ | ✓ | 306 |
| **1.2.4** | Verifique que todas las vías de autenticación y las API de administración de identidades implementan una fortaleza coherente del control de seguridad de autenticación, de modo que no haya alternativas más débiles por el riesgo de la aplicación. | | ✓ | ✓ | 306 |

## V1.3 Arquitectura de Gestión de Sesiones

Este es un marcador de posición para los requisitos arquitectónicos futuros.

## V1.4 Arquitectura de Control de Acceso

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.4.1** | Verifique que los puntos de cumplimiento de confianza, tales como puertas de enlace de control de acceso, servidores y funciones serverless, exijan controles de acceso. Nunca aplique controles de acceso en el cliente. | | ✓ | ✓ | 602 |
| **1.4.2** | [ELIMINADO, NO ACCIONABLE] | | | | |
| **1.4.3** | [ELIMINADO, DUPLICADO CON 4.1.3] | | | | |
| **1.4.4** | Verifique que la aplicación utilice un mecanismo de control de acceso único y bien comprobado para acceder a datos y recursos protegidos. Todas las solicitudes deben pasar por este único mecanismo para evitar copiar y pegar o rutas alternativas inseguras. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 284 |
| **1.4.5** | Verifique que se utiliza el control de acceso basado en atributos o entidades mediante el cual el código comprueba la autorización del usuario para un elemento de característica o datos en lugar de solo su rol. Los permisos deben asignarse mediante roles. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 275 |

## V1.5 Arquitectura de Entradas y Salidas

En 4.0, nos hemos alejado del término "server-side" como un término límite de confianza cargado. El límite de confianza sigue siendo relativo a - tomar decisiones sobre navegadores que no son de confianza o dispositivos cliente que son "bypassable". Sin embargo, en las implementaciones arquitectónicas convencionales de hoy en día, el punto de aplicación de la confianza ha cambiado drásticamente. Por lo tanto, cuando el término "trusted service layer" se utiliza en el ASVS, nos referimos a cualquier punto de aplicación de confianza, independientemente de la ubicación, como un microservicio, serverless API, server-side, una API de confianza en un dispositivo cliente que tiene secure boot, partner o API externas, etc.

El término "untrusted client" aquí se refiere a las tecnologías del lado del cliente que representan la capa de presentación, comúnmente referida como tecnologías 'front-end'. El término "serialization" aquí no sólo se refiere a enviar datos a través de las comunicaciones, como una matriz de valores o tomar y leer una estructura JSON, sino también pasar objetos complejos que pueden contener lógica.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.5.1** | Verifique que los requisitos de entrada y salida definan claramente cómo manejar y procesar datos en función del tipo, contenido y las leyes, regulaciones y otras leyes aplicables, reglamentos y otras normas de cumplimiento de políticas. | | ✓ | ✓ | 1029 |
| **1.5.2** | Verifique que no se usa serialización al comunicarse con clientes que no son de confianza. Si esto no es posible, asegúrese de que se apliquen controles de integridad adecuados (y posiblemente cifrado si se envían datos confidenciales) para evitar ataques de deserialización, incluida la inyección de objetos. | | ✓ | ✓ | 502 |
| **1.5.3** | Verifique que la validación de datos de entrada (input) se aplica en una capa de servicio de confianza. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 602 |
| **1.5.4** | Verifique que la codificación de salida (output encode) se produce cerca o en el intérprete para el que está destinada. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 116 |

## V1.6 Arquitectura Criptográfica

Las aplicaciones deben diseñarse con una arquitectura criptográfica sólida para proteger los activos de datos según su clasificación. Cifrar todo es un desperdicio, no cifrar nada es una negligencia legal. Se debe lograr un equilibrio, generalmente durante el diseño arquitectónico o de alto nivel, los "sprints" de diseño o los "spikes" arquitectónicos. Diseñar criptografía sobre la marcha o modernizarla inevitablemente costará mucho más implementar de forma segura que simplemente construirla desde el principio.

Los requisitos arquitectónicos son intrínsecos a toda la base de código y, por lo tanto, son difíciles de unir o integrar la prueba. Los requisitos arquitectónicos requieren consideración en los estándares de codificación, a lo largo de la fase de codificación, y deben revisarse durante la arquitectura de seguridad, las revisiones de pares o código, o las retrospectivas.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.6.1** | Verifique que existe una política explícita para la administración de claves criptográficas y que un ciclo de vida de clave criptográfica sigue un estándar de administración de claves como NIST SP 800-57. | | ✓ | ✓ | 320 |
| **1.6.2** | Verifique que los consumidores de servicios criptográficos protegen el material clave y otros secretos mediante el uso de almacenes de claves o alternativas basadas en API. | | ✓ | ✓ | 320 |
| **1.6.3** | Verifique que todas las claves y contraseñas son reemplazables y forman parte de un proceso bien definido para volver a cifrar los datos confidenciales. | | ✓ | ✓ | 320 |
| **1.6.4** | Verifique que la arquitectura trata los secretos del lado cliente (como claves simétricas, contraseñas o tokens de API) como inseguros y nunca los usa para proteger o acceder a datos confidenciales. | | ✓ | ✓ | 320 |

## V1.7 Arquitectura de Errores, Logging y Auditoría

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.7.1** | Verifique que se utilice un formato común y un enfoque de logging en todo el sistema. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1009 |
| **1.7.2** | Verifique que los registros de log se transmitan de forma segura a un sistema preferentemente remoto para análisis, detección, alertas y escalamiento. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

## V1.8 Arquitectura de Protección de Datos y Privacidad

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.8.1** | Verifique que todos los datos confidenciales se identifiquen y clasifiquen en niveles de protección. | | ✓ | ✓ | |
| **1.8.2** | Verifique que todos los niveles de protección tienen un conjunto asociado de requisitos de protección, como los requisitos de cifrado, los requisitos de integridad, la retención, la privacidad y otros requisitos de confidencialidad, y que estos se aplican en la arquitectura. | | ✓ | ✓ | |

## V1.9 Arquitectura de Comunicaciones

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.9.1** | Verifique que la aplicación cifra las comunicaciones entre componentes, especialmente cuando estos componentes se encuentran en contenedores, sistemas, sitios o proveedores de nube diferentes. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 319 |
| **1.9.2** | Verifique que los componentes de la aplicación verifiquen la autenticidad de cada lado en un vínculo de comunicación para evitar ataques de "persona en el medio". Por ejemplo, los componentes de la aplicación deben validar certificados y cadenas TLS. | | ✓ | ✓ | 295 |

## V1.10 Arquitectura de Software Malicioso

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.10.1** | Verifique que un sistema de control de código fuente está en uso, con procedimientos para garantizar que los check-ins están respaldados tickets de issues o solicitudes de cambio. El sistema de control de código fuente debe tener control de acceso y usuarios identificables para permitir la trazabilidad de cualquier cambio. | | ✓ | ✓ | 284 |

## V1.11 Arquitectura de la Lógica de Negocio

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.11.1** | Verifique la definición y documentación de todos los componentes de la aplicación en términos de las funciones de negocio o de seguridad que proporcionan. | | ✓ | ✓ | 1059 |
| **1.11.2** | Verifique que todos los flujos de lógica de negocio de alto valor, incluida la autenticación, la administración de sesiones y el control de acceso, no compartan estados no sincronizados. | | ✓ | ✓ | 362 |
| **1.11.3** | Verifique que todos los flujos de lógica de negocio de alto valor, incluida la autenticación, la administración de sesiones y el control de acceso, sean seguros para subprocesos y resistentes a condiciones de carrera time-of-check y time-of-use (race conditions). | | | ✓ | 367 |

## V1.12 Arquitectura de Carga Segura de Archivos

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.12.1** | [ELIMINADO, DUPLICADO CON 12.4.1] | | | | |
| **1.12.2** | Verifique que los archivos subidos por el usuario, -si es necesario que se muestren o descarguen desde la aplicación-, se hace mediante descargas de secuencias de octetos o desde un dominio no relacionado, como un almacenamiento de archivos en la nube. Implemente una directiva de seguridad de contenido (CSP) adecuada para reducir el riesgo de vectores XSS u otros ataques desde el archivo cargado. | | ✓ | ✓ | 646 |

## V1.13 Arquitectura de API

Este es un marcador de posición para los requisitos arquitectónicos futuros.

## V1.14 Arquitectura de Configuración

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.14.1** | Verifique la segregación de componentes de diferentes niveles de confianza a través de controles de seguridad bien definidos, reglas de corta fuego, pasarelas de API, proxies reversos, grupos de seguridad basados en nube, o mecanismos similares. | | ✓ | ✓ | 923 |
| **1.14.2** | Verifique que las firmas binarias, las conexiones de confianza y los puntos de conexión verificados se usan para el despliegue de archivos binarios a dispositivos remotos. | | ✓ | ✓ | 494 |
| **1.14.3** | Verifique que el canal de compilación advierte de componentes obsoletos o inseguros y realiza las acciones adecuadas. | | ✓ | ✓ | 1104 |
| **1.14.4** | Verifique que el canal de compilación contiene un paso para compilar y comprobar automáticamente el despliegue seguro de la aplicación, especialmente si la infraestructura de la aplicación está definida por software, como los scripts de compilación del entorno en la nube. | | ✓ | ✓ | |
| **1.14.5** | Verifique que los despliegues de aplicaciones sean en sandbox, contenedores y/o aislados a nivel de red para retrasar e impedir que los atacantes vulneren otras aplicaciones, especialmente cuando realizan acciones sensibles o peligrosas, como la deserialización. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |
| **1.14.6** | Verifique que la aplicación no utiliza tecnologías del lado cliente no compatibles, inseguras o en desuso, como NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL o client-side java applets. | | ✓ | ✓ | 477 |

## Referencias

Para obtener más información, consulte también:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
