# V3 Seguridad en frontend web

## Objetivo del control

Esta categoría se centra en los requerimientos diseñados para proteger en contra de ataques ejecutados a través de una interfaz web. Estos requerimientos no se aplican a las soluciones máquina a máquina.

## V3.1 Documentación de seguridad en Frontend Web

Esta sección describe las características de seguridad del navegador que deben especificarse en la documentación de la aplicación.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **3.1.1** | Verifique que la documentación de la aplicación especifique las funciones de seguridad que deben admitir los navegadores que la utilizan (como HTTPS, Seguridad de Transporte Estricta HTTP (HSTS), Política de Seguridad de Contenido (CSP) y otros mecanismos de seguridad HTTP relevantes). También debe definir cómo debe comportarse la aplicación cuando algunas de estas funciones no estén disponibles (como advertir al usuario o bloquear el acceso). | 3 |

## V3.2 Interpretación de contenido no intencionado

Renderizar contenido o funcionalidad en un contexto incorrecto puede provocar que se ejecute o muestre contenido malicioso.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **3.2.1** | Verifique que existan controles de seguridad para evitar que los navegadores muestren contenido o funcionalidades en respuestas HTTP en un contexto incorrecto (por ejemplo, cuando se solicita directamente una API, un archivo cargado por el usuario u otro recurso). Entre los posibles controles se incluyen: no mostrar el contenido a menos que los campos del encabezado de la solicitud HTTP (como Sec-Fetch-\*) indiquen que se trata del contexto correcto, usar la directiva de espacio aislado (sandbox) del campo de encabezado Content-Security-Policy o usar el tipo de disposición de adjuntos en el campo de encabezado Content-Disposition. | 1 |
| **3.2.2** | Verifique que el contenido que se pretende mostrar como texto, en lugar de renderizarse como HTML, se gestione mediante funciones de renderizado seguras (como createTextNode o textContent) para evitar la ejecución no deseada de contenido como HTML o JavaScript. | 1 |
| **3.2.3** | Verifique que la aplicación evite dañar el DOM al usar JavaScript del lado del cliente empleando declaraciones de variables explícitas, realizando una verificación de tipos estricta, evitando almacenar variables globales en el objeto del documento e implementando el aislamiento del espacio de nombres. (namespace) | 3 |

## V3.3 Configuración de Cookies

En esta sección se describen los requisitos para configurar de forma segura las cookies sensibles para proporcionar un mayor nivel de garantía de que fueron creadas por la propia aplicación y para evitar que sus contenidos se filtren o se modifiquen de forma inapropiada.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **3.3.1** | Verifique que las cookies tengan establecido el atributo 'Secure', y si no se utiliza el prefijo '\__Host-' para el nombre de la cookie, se debe usar el prefijo '__Secure-' para el nombre de la cookie. | 1 |
| **3.3.2** | Verifique que el valor del atributo 'SameSite' de cada cookie se establezca de acuerdo con la finalidad de la cookie para limitar la exposición a ataques de redireccionamiento de la interfaz de usuario y ataques de falsificación de solicitudes en el navegador, comúnmente conocidos como cross-site request forgery (CSRF). | 2 |
| **3.3.3** | Verifique que las cookies tengan el prefijo '__Host-' en el nombre, a menos que estén diseñadas explícitamente para compartirse con otros hosts. | 2 |
| **3.3.4** | Verifique que, si el valor de una cookie no está destinado a ser accesible para scripts del lado del cliente (como un token de sesión), la cookie debe tener establecido el atributo 'HttpOnly' y el mismo valor (p. ej., token de sesión) solo debe transferirse al cliente mediante el campo de encabezado 'Set-Cookie'. | 2 |
| **3.3.5** | Verifique que, cuando la aplicación escribe una cookie, la longitud combinada del nombre y el valor de la cookie no supere los 4096 bytes. Las cookies excesivamente grandes no serán almacenadas por el navegador y, por tanto, no se enviarán con las peticiones, impidiendo que el usuario utilice la funcionalidad de la aplicación que depende de esa cookie. | 3 |

## V3.4 Encabezados del mecanismo de seguridad del navegador

Esta sección describe qué encabezados de seguridad se deben configurar en las respuestas HTTP para habilitar las funciones y restricciones de seguridad del navegador al manejar respuestas de la aplicación.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **3.4.1** | Verifique que se incluya un campo de encabezado Strict-Transport-Security en todas las respuestas para aplicar una política de HTTP Strict Transport Security (HSTS). Debe definirse una antigüedad máxima de al menos 1 año, y para L2 en adelante, la política también debe aplicarse a todos los subdominios. | 1 |
| **3.4.2** | Verifique que el campo de encabezado Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin tenga un valor fijo establecido por la aplicación, o, si se utiliza el valor del campo de encabezado de solicitud HTTP Origin, este se valide frente a una lista de permitidos de orígenes confiables. Cuando sea necesario utilizar 'Access-Control-Allow-Origin: *', verifique que la respuesta no incluya información sensible. | 1 |
| **3.4.3** | Verifique que las respuestas HTTP incluyan un campo de encabezado de respuesta Content-Security-Policy que defina directivas para garantizar que el navegador solo cargue y ejecute contenido o recursos confiables, con el fin de limitar la ejecución de JavaScript malicioso. Como mínimo, debe utilizarse una política global que incluya las directivas object-src 'none' y base-uri 'none' y defina una lista de permitidos o utilice nonces o hashes. Para una aplicación L3, debe definirse una política por respuesta con nonces o hashes. | 2 |
| **3.4.4** | Verifique que todas las respuestas HTTP contengan el campo de encabezado 'X-Content-Type-Options: nosniff'. Esto indica a los navegadores que no utilicen análisis de contenido ni inferencia de tipo MIME para la respuesta dada, y que exijan que el valor del campo de encabezado Content-Type coincida con el recurso de destino. Por ejemplo, la respuesta a una petición de estilo solo se acepta si su Content-Type es 'text/css'. Esto también habilita el uso de la funcionalidad Cross-Origin Read Blocking (CORB) por parte del navegador. | 2 |
| **3.4.5** | Verifique que la aplicación establezca una política de referencia para prevenir la filtración de datos técnicamente sensibles a servicios de terceros mediante el campo de encabezado HTTP 'Referer'. Esto puede hacerse usando el campo de encabezado de respuesta HTTP Referrer-Policy o mediante atributos de elementos HTML. Los datos sensibles podrían incluir la ruta y los datos de consulta de la URL, y en aplicaciones internas no públicas también el nombre del host. | 2 |
| **3.4.6** | Verifique que la aplicación web utilice la directiva frame-ancestors del campo de encabezado Content-Security-Policy en cada respuesta HTTP para garantizar que no pueda incrustarse de forma predeterminada y que la incrustación de recursos específicos solo se permita cuando sea necesario. Tenga en cuenta que el campo de encabezado X-Frame-Options, aunque es compatible con los navegadores, está obsoleto y no debe dependerse de él. | 2 |
| **3.4.7** | Verifique que el campo de encabezado Content-Security-Policy especifique una ubicación para informar de las violaciones. | 3 |
| **3.4.8** | Verifique que todas las respuestas HTTP que inicien un renderizado de documento (como las respuestas con Content-Type text/html) incluyan el campo de encabezado Cross‑Origin‑Opener‑Policy con la directiva same-origin o same-origin-allow-popups según corresponda. Esto evita ataques que aprovechan el acceso compartido a objetos Window, como tabnabbing y frame counting. | 3 |

## V3.5 Separación de origen del navegador

Cuando se acepta una solicitud para una funcionalidad sensible en el lado del servidor, la aplicación debe asegurarse de que la solicitud la inicia la propia aplicación o una parte de confianza y de que no ha sido falsificada por un atacante.

En este contexto, la funcionalidad sensible podría incluir aceptar publicaciones de formularios para usuarios autenticados y no autenticados (como una solicitud de autenticación), operaciones que cambian el estado o funcionalidades que requieren muchos recursos (como la exportación de datos).

La protección clave aquí son las políticas de seguridad del navegador, como la Política de mismo origen (Same Origin Policy) para JavaScript y también la lógica SameSite para las cookies. Otra protección habitual es el mecanismo de precarga de CORS (CORS preflight). Este mecanismo será crítico para los endpoints diseñados para ser llamados desde un origen diferente, pero también puede ser un mecanismo útil de prevención de falsificación de solicitudes para endpoints que no están diseñados para ser llamados desde un origen diferente.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **3.5.1** | Verifique que, si la aplicación no depende del mecanismo de precarga de CORS para prevenir solicitudes entre orígenes no permitidas para utilizar funcionalidades sensibles, estas solicitudes se validen para asegurar que proceden de la propia aplicación. Esto puede hacerse mediante el uso y la validación de tokens anti-falsificación o requiriendo campos adicionales del encabezado HTTP que no sean campos de encabezado de solicitud de lista segura de CORS. Esto tiene como objetivo defenderse contra ataques de falsificación de solicitudes en el navegador, comúnmente conocidos como cross-site request forgery (CSRF). | 1 |
| **3.5.2** | Verifique que, si la aplicación depende del mecanismo de precarga de CORS para prevenir el uso no permitido de funcionalidades sensibles entre orígenes, no sea posible llamar a la funcionalidad con una solicitud que no active una solicitud de precarga de CORS. Esto puede requerir comprobar los valores de los campos de encabezado 'Origin' y 'Content-Type' o utilizar un campo de encabezado adicional que no sea un campo de cabecera de lista segura de CORS. | 1 |
| **3.5.3** | Verifique que las solicitudes HTTP a funcionalidades sensibles utilicen métodos HTTP apropiados, como POST, PUT, PATCH o DELETE, y no métodos definidos por la especificación HTTP como "seguros", como HEAD, OPTIONS o GET. Alternativamente, se puede utilizar una validación estricta de los campos de encabezado de solicitud Sec-Fetch-* para garantizar que la solicitud no se originó en una llamada entre orígenes inapropiada, una solicitud de navegación o una carga de recursos (como una fuente de imagen) cuando no se espera. | 1 |
| **3.5.4** | Verifique que las aplicaciones separadas se hospeden en nombres de host distintos para aprovechar las restricciones proporcionadas por la política de mismo origen, incluidas la forma en que los documentos o scripts cargados por un origen pueden interactuar con recursos de otro origen y las restricciones basadas en el nombre de host de las cookies. | 2 |
| **3.5.5** | Verifique que los mensajes recibidos por la interfaz postMessage se descarten si el origen del mensaje no es de confianza o si la sintaxis del mensaje es inválida. | 2 |
| **3.5.6** | Verifique que la funcionalidad JSONP no esté habilitada en ninguna parte de la aplicación para evitar ataques de Inclusión de Scripts entre Sitios (XSSI). | 3 |
| **3.5.7** | Verifique que los datos que requieren autorización no se incluyan en las respuestas de recursos de script, como archivos JavaScript, para prevenir ataques de Inclusión de Scripts entre Sitios (XSSI). | 3 |
| **3.5.8** | Verifique que los recursos autenticados (como imágenes, vídeos, scripts y otros documentos) solo puedan cargarse o incrustarse en nombre del usuario cuando sea necesario. Esto puede lograrse mediante una validación estricta de los campos de encabezado HTTP Sec-Fetch-* para garantizar que la solicitud no se originó en una llamada entre orígenes inapropiada, o mediante el establecimiento de un campo de encabezado HTTP Cross-Origin-Resource-Policy restrictivo para indicar al navegador que bloquee el contenido devuelto. | 3 |

## V3.6 Integridad de los recursos externos

Esta sección proporciona orientación para el alojamiento seguro de contenido en sitios de terceros.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **3.6.1** | Verifique que los activos del lado del cliente, como bibliotecas de JavaScript, CSS o fuentes web, solo se alojan externamente (por ejemplo, en una Red de Entrega de Contenidos, CDN) si el recurso es estático y versionado y se utiliza Integridad de Subrecursos (Subresource Integrity, SRI) para validar la integridad del activo. Si esto no es posible, debe existir una decisión de seguridad documentada que justifique esta excepción para cada recurso. | 3 |

## V3.7 Otras consideraciones de seguridad del navegador

Esta sección incluye varios controles de seguridad y funciones modernas de seguridad de navegadores, necesarias para la seguridad del navegador del lado del cliente.


| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **3.7.1** | Verifique que la aplicación solo utilice tecnologías del lado del cliente que sigan teniendo soporte y se consideren seguras. Entre las tecnologías que no cumplen este requisito se incluyen complementos NSAPI, Flash, Shockwave, ActiveX, Silverlight, NACL o applets Java del lado del cliente. | 2 |
| **3.7.2** | Verifique que la aplicación solo redirija automáticamente al usuario a un nombre de host o dominio diferente (que no esté controlado por la aplicación) cuando el destino aparezca en una lista de permitidos (allowlist). | 2 |
| **3.7.3** | Verifique que la aplicación muestre una notificación cuando el usuario vaya a ser redirigido a una URL fuera del control de la aplicación, con una opción para cancelar la navegación. | 3 |
| **3.7.4** | Verifique que el dominio de nivel superior de la aplicación (por ejemplo, site.tld) se añada a la lista pública de precarga para HTTP Strict Transport Security (HSTS). Esto garantiza que el uso de TLS para la aplicación esté integrado directamente en los navegadores principales, en lugar de depender solo del campo de encabezado de respuesta Strict-Transport-Security. | 3 |
| **3.7.5** | Verifique que la aplicación se comporte según lo documentado (por ejemplo, advirtiendo al usuario o bloqueando el acceso) si el navegador utilizado para acceder a la aplicación no admite las funciones de seguridad esperadas. | 3 |

## Referencias

Para obtener más información consulte:

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
* [OWASP DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)
