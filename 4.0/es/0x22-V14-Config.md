# V14 : Requisitos de verificación de configuración

## Objetivo de Control

Asegúrese de que una aplicación verificada tiene:

 - Un entorno de compilación seguro, repetible y automatizable.
 - La aplicación no incluye la biblioteca de terceros reforzada, la dependencia y la administración de la configuración, de modo que la aplicación no incluya componentes obsoletos o no seguros.
 - Una configuración segura por defecto, de modo que los administradores y los usuarios tengan que debilitar la postura de seguridad predeterminada.

La configuración de la aplicación “desde fábrica” debe ser segura para estar en Internet, lo que significa una configuración segura desde la caja.

## V14.1 Compilación

Las pipelines de compilación son la base para la seguridad repetible - cada vez que se detecta algo inseguro, se puede resolver en el código fuente, compilar o implementar scripts y probarse automáticamente. Enfatizamos el uso de pipelines de compilación con comprobaciones automáticas de seguridad y chequeo de dependencia que alerten o interrumpen la compilación para evitar que los problemas de seguridad conocidos se implementen en producción. Los pasos manuales realizados de forma irregular directamente conducen a errores de seguridad evitables.

A medida que la industria se encamina hacia un modelo DevSecOps, es importante garantizar la disponibilidad continua y la integridad de la implementación y la configuración para lograr un estado "bueno conocido". En el pasado, si un sistema fuera hackeado, tardaría días o meses en demostrar que no se habían producido más intrusiones. Hoy en día, con la llegada de la infraestructura definida por software, las implementaciones rápidas de A/B con zero downtime y las compilaciones automatizadas en contenedores, es posible construir, hardenizar e implementar continuamente un reemplazo "bueno conocido" para cualquier sistema comprometido.

Si aún persisten modelos tradicionales, se deben tomar medidas manuales para hardenizar y hacer una copia de seguridad de esa configuración para permitir que los sistemas comprometidos se reemplacen rápidamente por sistemas de alta integridad y sin compromisos, de manera oportuna.

El cumplimiento de esta categoria ASVS requiere un sistema de compilación automatizado y acceso a scripts de compilación e implementación.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.1.1** | Compruebe que los procesos de compilación e implementación de aplicaciones se realizan de forma segura y repetible, como la automatización de CI/CD, la administración de configuración automatizada y los scripts de implementación automatizada. | | ✓ | ✓ | |
| **14.1.2** | Compruebe que los indicadores del compilador están configurados para habilitar todas las protecciones y advertencias de desbordamiento de búfer disponibles, incluida la aleatorización de la pila, la prevención de la ejecución de datos y para interrumpir la compilación si se encuentra un puntero no seguro, memoria, cadena de formato, entero o operaciones de cadena. | | ✓ | ✓ | 120 |
| **14.1.3** | Compruebe que la configuración del servidor está hardenizada según las recomendaciones del servidor de aplicaciones y los framewors en uso. | | ✓ | ✓ | 16 |
| **14.1.4** | Compruebe que la aplicación, la configuración y todas las dependencias se pueden volver a implementar mediante scripts de implementación automatizada, crearse a partir de un runbook documentado y probado en un tiempo razonable o restaurarse a partir de copias de seguridad de forma oportuna. | | ✓ | ✓ | |
| **14.1.5** | Compruebe que los administradores autorizados pueden verificar la integridad de todas las configuraciones relevantes para la seguridad para detectar una posible manipulación. | | | ✓ | |

## V14.2 Dependencias

La administración de dependencias es fundamental para el funcionamiento seguro de cualquier aplicación de cualquier tipo. No mantenerse al día con dependencias obsoletas o inseguras es la causa raíz de los ataques más grandes y costosos hasta la fecha.

**Nota:** En el nivel 1, el cumplimiento 14.2.1 se relaciona con observaciones o detecciones de bibliotecas y componentes del lado cliente y otros, en lugar del análisis de código estático en tiempo de compilación o análisis de dependencia más preciso. Estas técnicas más precisas podrían ser detectables por entrevistas, según sea necesario.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.2.1** | Compruebe que todos los componentes estén actualizados, preferiblemente utilizando un comprobador de dependencias durante el tiempo de compilación. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1026 |
| **14.2.2** | Compruebe que se eliminan todas las características innecesarias, documentación, ejemplos, configuraciones, las aplicaciones de ejemplo, documentación de plataforma y usuarios predeterminados o de ejemplo. | ✓ | ✓ | ✓ | 1002 |
| **14.2.3** | Compruebe que si los activos de la aplicación, como bibliotecas JavaScript, fuentes CSS o web, se hospedan externamente en una red de entrega de contenido (CDN) o un proveedor externo, se usa la integridad de subrecursos (SRI) para validar la integridad del recurso. | ✓ | ✓ | ✓ | 829 |
| **14.2.4** | Compruebe que los componentes de terceros provienen de repositorios predefinidos, de confianza y mantenidos continuamente. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 829 |
| **14.2.5** | Compruebe que se mantiene un catálogo de inventario de todas las bibliotecas de terceros en uso. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **14.2.6** | Compruebe que la superficie de ataque se reduce mediante sandboxing o encapsular bibliotecas de terceros para exponer solo el comportamiento necesario en la aplicación. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |

## V14.3 Requisitos de divulgación de seguridad no intencionales

Las configuraciones para la producción deben endurecerse contra ataques comunes, como consolas de depuración, elevar el nivel de defensa contra los ataques de secuencias de comandos entre sitios (XSS) e inclusión remota de archivos (RFI) y eliminar las "vulnerabilidades" de detección de información trivial que son el sello no deseado de muchos informes de pruebas de penetración. Muchos de estos problemas rara vez se clasifican como un riesgo significativo, pero se encadenan junto con otras vulnerabilidades. Si estos problemas no están presentes de forma predeterminada, se debe elevar el nivel de defensa antes de que la mayoría de los ataques puedan realizarse correctamente.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.3.1** | Compruebe que los mensajes de error del servidor web o de aplicaciones y del marco de trabajo están configurados para ofrecer al usuario respuestas personalizadas y procesables para eliminar cualquier divulgación de seguridad no intencionada. | ✓ | ✓ | ✓ | 209 |
| **14.3.2** | Compruebe que los modos de depuración del servidor web o de aplicaciones y del framework de aplicaciones están deshabilitados en producción para eliminar las características de depuración, las consolas de desarrollador y las divulgaciones de seguridad no deseadas. | ✓ | ✓ | ✓ | 497 |
| **14.3.3** | Compruebe que los encabezados HTTP o cualquier parte de la respuesta HTTP no exponen información detallada de la versión de los componentes del sistema. | ✓ | ✓ | ✓ | 200 |

## V14.4 Requisitos de encabezados de seguridad HTTP

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.4.1** | Compruebe que cada respuesta HTTP contiene un encabezado Content-Type. Y los tipos de contenido text/*, /+xml y application/xml también deben especificar un juego de caracteres seguro (por ejemplo, UTF-8, ISO-8859-1). | ✓ | ✓ | ✓ | 173 |
| **14.4.2** | Compruebe que todas las respuestas de API contienen un encabezado Content-Disposition: attachment; filename="api.json" (u otro nombre de archivo apropiado para el tipo de contenido). | ✓ | ✓ | ✓ | 116 |
| **14.4.3** | Compruebe que existe un encabezado de respuesta de Directiva de Seguridad de Contenido (CSP) que ayuda a mitigar el impacto de los ataques XSS como vulnerabilidades de inyección de HTML, DOM, JSON y JavaScript. | ✓ | ✓ | ✓ | 1021 |
| **14.4.4** | Compruebe que todas las respuestas contienen un encabezado X-Content-Type-Options: nosniff. | ✓ | ✓ | ✓ | 116 |
| **14.4.5** | Compruebe que se incluye un encabezado Strict-Transport-Security en todas las respuestas y para todos los subdominios, como Strict-Transport-Security: max-age-15724800; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **14.4.6** | Compruebe que se incluye un encabezado "Referrer-Policy" adecuado, como "no-referrer" o "same-origin". | ✓ | ✓ | ✓ | 116 |
| **14.4.7** | Compruebe que el contenido de una aplicación web no se puede incrustar en un sitio de terceros de forma predeterminada y que la inserción de los recursos exactos solo se permite cuando sea necesario mediante el uso adecuado de Content-Security-Polic: frame-ancestors y encabezados de respuesta X-Frame-Options. | ✓ | ✓ | ✓ | 346 |

## V14.5 Validar los requisitos de encabezado de solicitud HTTP

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.5.1** | Compruebe que el servidor de aplicaciones solo acepta los métodos HTTP que utiliza la aplicación/API, incluidas las pre-flight OPTIONS, y los Logs/alertas en cualquier solicitud que no sea válida para el contexto de la aplicación. | ✓ | ✓ | ✓ | 749 |
| **14.5.2** | Compruebe que el encabezado Origin proporcionado no se utiliza para las decisiones de autenticación o control de acceso, ya que un atacante puede cambiar fácilmente el encabezado Origin. | ✓ | ✓ | ✓ | 346 |
| **14.5.3** | Compruebe que el encabezado Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin utiliza una estricta lista de permisos de dominios y subdominios de confianza para que coincidan entre si, y no se permita el origen "nulo". | ✓ | ✓ | ✓ | 346 |
| **14.5.4** | Compruebe que la aplicación autentica los encabezados HTTP agregados por un proxy de confianza o dispositivos SSO, como un token de portador. | | ✓ | ✓ | 306 |

## Referencias

Para obtener más información, véase también:

* [OWASP Testing Guide 4.0: Testing for HTTP Verb Tampering]( https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* Agregar Contenido-Disposición a las respuestas de la API ayuda a prevenir muchos ataques basados en malentendidos sobre el tipo MIME entre el cliente y el servidor, y la opción "nombre de archivo" ayuda específicamente a prevenir [Reflected File Download attacks.](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Testing Guide 4.0: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Sandboxing third party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
