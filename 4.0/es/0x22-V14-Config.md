# V14 Configuración

## Objetivo de Control

Asegúrese de que una aplicación verificada tiene:

* Un entorno de compilación seguro, repetible y automatizable.
* La aplicación no incluye la biblioteca de terceros reforzada, la dependencia y la administración de la configuración, de modo que la aplicación no incluya componentes obsoletos o no seguros.

La configuración de la aplicación "desde fábrica" debe ser segura para estar en Internet, lo que significa una configuración segura desde la caja.

## V14.1 Compilación y Despliegue

Las pipelines de compilación son la base para la seguridad repetible - cada vez que se detecta algo inseguro, se puede resolver en el código fuente, compilar o desplegar scripts y probarse automáticamente. Enfatizamos el uso de pipelines de compilación con comprobaciones automáticas de seguridad y chequeo de dependencia que alerten o interrumpen la compilación para evitar que los problemas de seguridad conocidos se implementen en producción. Los pasos manuales realizados de forma irregular directamente conducen a errores de seguridad evitables.

A medida que la industria se encamina hacia un modelo DevSecOps, es importante garantizar la disponibilidad continua y la integridad de la implementación y la configuración para lograr un estado "bueno conocido". En el pasado, si un sistema fuera hackeado, tardaría días o meses en demostrar que no se habían producido más intrusiones. Hoy en día, con la llegada de la infraestructura definida por software, las implementaciones rápidas de A/B con zero downtime y las compilaciones automatizadas en contenedores, es posible compilar, hardenizar y desplegar continuamente un reemplazo "bueno conocido" para cualquier sistema comprometido.

Si aún persisten modelos tradicionales, se deben tomar medidas manuales para hardenizar y hacer una copia de seguridad de esa configuración para permitir que los sistemas comprometidos se reemplacen rápidamente por sistemas de alta integridad y sin compromisos, de manera oportuna.

El cumplimiento de esta categoria ASVS requiere un sistema de compilación automatizado y acceso a scripts de compilación e implementación.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.1.1** | Verifique que los procesos de compilación y despliegue de aplicaciones se realizan de forma segura y repetible, como la automatización de CI/CD, la administración de configuración automatizada y los scripts de despliegue automatizado. | | ✓ | ✓ | |
| **14.1.2** | Verifique que los indicadores del compilador están configurados para habilitar todas las protecciones y advertencias de desbordamiento de búfer disponibles, incluida la aleatorización de la pila, la prevención de la ejecución de datos y para interrumpir la compilación si se encuentra un puntero no seguro, memoria, cadena de formato, entero u operaciones de cadena. | | ✓ | ✓ | 120 |
| **14.1.3** | Verifique que la configuración del servidor está hardenizada según las recomendaciones del servidor de aplicaciones y los framewors en uso. | | ✓ | ✓ | 16 |
| **14.1.4** | Verifique que la aplicación, la configuración y todas las dependencias se pueden volver a implementar mediante scripts de implementación automatizada, crearse a partir de un runbook documentado y probado en un tiempo razonable o restaurarse a partir de copias de seguridad de forma oportuna. | | ✓ | ✓ | |
| **14.1.5** | Verifique que los administradores autorizados pueden verificar la integridad de todas las configuraciones relevantes para la seguridad para detectar una posible manipulación. | | | ✓ | |

## V14.2 Dependencias

La administración de dependencias es fundamental para el funcionamiento seguro de cualquier aplicación de cualquier tipo. No mantenerse al día con dependencias obsoletas o inseguras es la causa raíz de los ataques más grandes y costosos hasta la fecha.

Nota: En el nivel 1, el cumplimiento 14.2.1 se relaciona con observaciones o detecciones de bibliotecas y componentes del lado cliente y otros, en lugar del análisis de código estático en tiempo de compilación o análisis de dependencia más preciso. Estas técnicas más precisas podrían ser detectables por entrevistas, según sea necesario.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.2.1** | Verifique que todos los componentes estén actualizados, preferiblemente utilizando un comprobador de dependencias durante el tiempo de compilación. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1026 |
| **14.2.2** | Verifique que se eliminen todas las funciones, documentación, aplicaciones de muestra y configuraciones innecesarias. | ✓ | ✓ | ✓ | 1002 |
| **14.2.3** | Verifique que si los activos de la aplicación, como bibliotecas JavaScript, fuentes CSS o web, se hospedan externamente en una red de entrega de contenido (CDN) o un proveedor externo, se usa la integridad de subrecursos (SRI) para validar la integridad del activo. | ✓ | ✓ | ✓ | 829 |
| **14.2.4** | Verifique que los componentes de terceros provienen de repositorios predefinidos, de confianza y mantenidos continuamente. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 829 |
| **14.2.5** | Verifique que se mantenga una Lista de materiales de software (SBOM; por sus siglas en inglés) de todas las bibliotecas de terceros en uso. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **14.2.6** | Verifique que la superficie de ataque se reduce mediante sandboxing o encapsular bibliotecas de terceros para exponer solo el comportamiento necesario en la aplicación. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |

## V14.3 Divulgación de Seguridad Involuntaria

Las configuraciones para la producción deben endurecerse contra ataques comunes, como consolas de depuración, elevar el nivel de defensa contra los ataques de secuencias de comandos entre sitios (XSS) e inclusión remota de archivos (RFI) y eliminar las "vulnerabilidades" de detección de información trivial que son el sello no deseado de muchos informes de pruebas de penetración. Muchos de estos problemas rara vez se clasifican como un riesgo significativo, pero se encadenan junto con otras vulnerabilidades. Si estos problemas no están presentes de forma predeterminada, se debe elevar el nivel de defensa antes de que la mayoría de los ataques puedan realizarse exitosamente.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.3.1** | [ELIMINADO, DUPLICADO DE 7.4.1] | | | | |
| **14.3.2** | Verifique que los modos de depuración del servidor web o de aplicaciones y del framework de aplicaciones están deshabilitados en producción para eliminar las características de depuración, las consolas de desarrollador y las divulgaciones de seguridad no deseadas. | ✓ | ✓ | ✓ | 497 |
| **14.3.3** | Verifique que los encabezados HTTP o cualquier parte de la respuesta HTTP no exponen información detallada de la versión de los componentes del sistema. | ✓ | ✓ | ✓ | 200 |

## V14.4 Encabezados de Seguridad HTTP

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.4.1** | Verifique que cada respuesta HTTP contenga un encabezado de tipo de contenido. También especifique un conjunto de caracteres seguro (p. ej., UTF-8, ISO-8859-1) si los tipos de contenido son texto/*, /+xml y aplicación/xml. El contenido debe coincidir con el encabezado de tipo de contenido proporcionado. | ✓ | ✓ | ✓ | 173 |
| **14.4.2** | Verifique que todas las respuestas de API contienen un encabezado Content-Disposition: attachment; filename="api.json" (u otro nombre de archivo apropiado para el tipo de contenido). | ✓ | ✓ | ✓ | 116 |
| **14.4.3** | Verifique que existe un encabezado de respuesta de Directiva de Seguridad de Contenido (CSP) que ayuda a mitigar el impacto de los ataques XSS como vulnerabilidades de inyección de HTML, DOM, JSON y JavaScript. | ✓ | ✓ | ✓ | 1021 |
| **14.4.4** | Verifique que todas las respuestas contienen un encabezado X-Content-Type-Options: nosniff. | ✓ | ✓ | ✓ | 116 |
| **14.4.5** | Verifique que se incluye un encabezado Strict-Transport-Security en todas las respuestas y para todos los subdominios, como Strict-Transport-Security: max-age-15724800; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **14.4.6** | Verifique que se incluya adecuadamente un encabezado de Referrer-Policy para evitar exponer información confidencial en la URL a través del encabezado de referencia a partes que no son de confianza. | ✓ | ✓ | ✓ | 116 |
| **14.4.7** | Verifique que el contenido de una aplicación web no se puede incrustar en un sitio de terceros de forma predeterminada y que la inserción de los recursos exactos solo se permite cuando sea necesario mediante el uso adecuado de Content-Security-Polic: frame-ancestors y encabezados de respuesta X-Frame-Options. | ✓ | ✓ | ✓ | 1021 |

## V14.5 Validación de Encabezado de Solicitud HTTP

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.5.1** | Verifique que el servidor de aplicaciones solo acepta los métodos HTTP que utiliza la aplicación/API, incluidas las pre-flight OPTIONS, y los Logs/alertas en cualquier solicitud que no sea válida para el contexto de la aplicación. | ✓ | ✓ | ✓ | 749 |
| **14.5.2** | Verifique que el encabezado Origin proporcionado no se utiliza para las decisiones de autenticación o control de acceso, ya que un atacante puede cambiar fácilmente el encabezado Origin. | ✓ | ✓ | ✓ | 346 |
| **14.5.3** | Verifique que el encabezado Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin utiliza una estricta lista de permisos de dominios y subdominios de confianza para que coincidan entre si, y no se permita el origen "nulo". | ✓ | ✓ | ✓ | 346 |
| **14.5.4** | Verifique que la aplicación autentica los encabezados HTTP agregados por un proxy de confianza o dispositivos SSO, como un token de portador. | | ✓ | ✓ | 306 |

## Referencias

Para obtener más información, véase también:

* [OWASP Web Security Testing Guide 4.1: Testing for HTTP Verb Tampering]( https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* Adding Content-Disposition to API responses helps prevent many attacks based on misunderstanding on the MIME type between client and server, and the "filename" option specifically helps prevent [Reflected File Download attacks.](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Sandboxing third party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
