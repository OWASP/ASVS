# V8 Protección de Datos

## Objetivo de Control

Hay tres elementos clave para una protección de datos sólida: Confidencialidad, Integridad y Disponibilidad (CIA; por sus siglas en inglés). Este estándar supone que la protección de datos se aplica en un sistema de confianza, como un servidor, que se ha reforzado y tiene suficientes protecciones.

Las aplicaciones tienen que asumir que todos los dispositivos de usuario están comprometidos de alguna manera. Cuando una aplicación transmite o almacena información confidencial en dispositivos inseguros, como ordenadores compartidos, teléfonos y tabletas, la aplicación es responsable de garantizar que los datos almacenados en estos dispositivos estén cifrados y no puedan obtenerse, modificarse o divulgarse de forma ilícita.

Asegúrese de que una aplicación verificada cumple los siguientes requisitos de protección de datos de alto nivel:

 * Confidencialidad: Los datos deben protegerse de la observación o divulgación no autorizada tanto en tránsito como cuando se almacenan. 
 * Integridad: Los datos deben protegerse de ser creados, alterados o eliminados maliciosamente por atacantes no autorizados. 
 * Disponibilidad: los datos deben estar disponibles para los usuarios autorizados según sea necesario.

## V8.1 Protección General de Datos

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.1.1** | Verifique que la aplicación protege los datos confidenciales de la caché en componentes del servidor, como balanceadores de carga y cachés de aplicaciones. | | ✓ | ✓ | 524 |
| **8.1.2** | Verifique que todas las copias almacenadas en caché o temporales de datos confidenciales almacenados en el servidor están protegidas contra el acceso no autorizado o purgadas/invalidadas después de que el usuario autorizado acceda a los datos confidenciales. | | ✓ | ✓ | 524 |
| **8.1.3** | Verifique que la aplicación minimiza el número de parámetros de una solicitud, como campos ocultos, variables Ajax, cookies y valores de encabezado. | | ✓ | ✓ | 233 |
| **8.1.4** | Verifique que la aplicación puede detectar y alertar sobre números anormales de solicitudes, como por IP, usuario, total por hora o día, o lo que tenga sentido para la aplicación. | | ✓ | ✓ | 770 |
| **8.1.5** | Verifique que se realizan copias de seguridad periódicas de datos importantes y que se realizan pruebas de la restauración de datos. | | | ✓ | 19 |
| **8.1.6** | Verifique que las copias de seguridad se almacenan de forma segura para evitar que los datos sean robados o se dañen. | | | ✓ | 19 |

## V8.2 Protección de datos del lado del cliente

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.2.1** | Verifique que la aplicación establece suficientes encabezados anti-almacenamiento en caché para que los datos confidenciales no se almacenen en caché en los navegadores modernos. | ✓ | ✓ | ✓ | 525 |
| **8.2.2** | Verifique que los datos almacenados en el almacenamiento del navegador (como localStorage, sessionStorage, IndexedDB o cookies) no contengan datos confidenciales. | ✓ | ✓ | ✓ | 922 |
| **8.2.3** | Verifique que los datos autenticados se borran del almacenamiento del cliente, como el DOM del explorador, después de que se termine el cliente o la sesión. | ✓ | ✓ | ✓ | 922 |

## V8.3 Datos Privados Confidenciales

Esta sección ayuda a proteger los datos confidenciales de la creación, lectura, actualización o eliminación sin autorización, especialmente en cantidades masivas.

El cumplimiento de esta sección implica el cumplimiento del control de acceso V4 y, en particular, del V4.2. Por ejemplo, para protegerse contra actualizaciones no autorizadas o divulgación de información personal confidencial requiere el cumplimiento de V4.2.1. Por favor, cumpla con esta categoría y V4 para la cobertura completa.

Nota: Las regulaciones y leyes de privacidad, como los Principios de Privacidad de Australia APP-11 o GDPR, afectan directamente a la forma en que las aplicaciones deben abordar la implementación del almacenamiento, el uso y la transmisión de información personal confidencial. Esto va desde sanciones severas hasta simples consejos. Consulte sus leyes y regulaciones locales y consulte a un especialista en privacidad o abogado calificado según sea necesario.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **8.3.1** | Verifique que los datos confidenciales se envían al servidor en el cuerpo o encabezados del mensaje HTTP y que los parámetros de cadena de consulta de cualquier verbo HTTP no contienen datos confidenciales. | ✓ | ✓ | ✓ | 319 |
| **8.3.2** | Verifique que los usuarios tienen un método para eliminar o exportar sus datos sobre demanda (on demand). | ✓ | ✓ | ✓ | 212 |
| **8.3.3** | Verifique que se proporciona a los usuarios un lenguaje claro con respecto a la recopilación y el uso de la información personal suministrada y que los usuarios han proporcionado el consentimiento de aceptación para el uso de esos datos antes de que se utilicen de alguna manera. | ✓ | ✓ | ✓ | 285 |
| **8.3.4** | Verifique que se han identificado todos los datos confidenciales creados y procesados por la aplicación, y asegúrese de que existe una política sobre cómo tratar los datos confidenciales. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 200 |
| **8.3.5** | Verifique que el acceso a los datos confidenciales se audita (sin registrar los datos confidenciales en sí), si los datos se recopilan en las directivas de protección de datos pertinentes o donde se requiere el registro del acceso. | | ✓ | ✓ | 532 |
| **8.3.6** | Verifique que la información confidencial contenida en la memoria se sobrescribe tan pronto como ya no sea necesaria para mitigar los ataques de volcado de memoria, utilizando ceros o datos aleatorios. | | ✓ | ✓ | 226 |
| **8.3.7** | Verifique que la información confidencial o privada que se requiere que se cifre, se cifra mediante algoritmos aprobados que proporcionan confidencialidad e integridad. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 327 |
| **8.3.8** | Verifique que la información personal confidencial está sujeta a la clasificación de retención de datos, de forma que los datos antiguos o desactualizados se eliminen automáticamente, según una programación o según la situación lo requiera. | | ✓ | ✓ | 285 |

Al considerar la protección de datos, una consideración principal debe ser la extracción masiva o la modificación o el uso excesivo. Por ejemplo, muchos sistemas de redes sociales solo permiten a los usuarios agregar 100 nuevos amigos por día, pero el sistema del que provienen estas solicitudes no es importante. Una plataforma bancaria podría querer bloquear más de 5 transacciones por hora transfiriendo más de 1000 euros de fondos a instituciones externas. Es probable que los requisitos de cada sistema sean muy diferentes, por lo que decidirse por "anormal" debe tener en cuenta el modelo de amenaza y el riesgo empresarial. Los criterios importantes son la capacidad de detectar, disuadir o preferentemente bloquear tales acciones masivas anormales.

## Referencias

Para obtener más información, véase también:

* [Consider using Security Headers website to check security and anti-caching headers](https://securityheaders.io)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [European Union General Data Protection Regulation (GDPR) overview](https://edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
