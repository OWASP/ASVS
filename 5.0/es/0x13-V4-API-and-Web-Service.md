# V4 API y servicios web

## Objetivo de control

Se aplican varias consideraciones específicamente a las aplicaciones que exponen APIs para su uso por navegadores web u otros consumidores (normalmente mediante JSON, XML o GraphQL). Este capítulo cubre las configuraciones y mecanismos de seguridad relevantes que deben aplicarse.

Tenga en cuenta que también se aplican a las APIs las cuestiones de autenticación, gestión de sesiones y validación de entradas de otros capítulos, por lo que este capítulo no se puede sacar de contexto ni probar de forma aislada.

## V4.1 Seguridad genérica de servicios web

Esta sección aborda las consideraciones generales de seguridad de los servicios web y, en consecuencia, las prácticas básicas de higiene de los servicios web.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **4.1.1** | Verifique que cada respuesta HTTP con cuerpo de mensaje contenga un campo de cabecera Content-Type que coincida con el contenido real de la respuesta, incluyendo el parámetro charset para especificar una codificación de caracteres segura (por ejemplo, UTF-8, ISO-8859-1) de acuerdo con los tipos de medios de IANA, como "text/", "/+xml" y "/xml". | 1 |
| **4.1.2** | Verifique que solo los puntos finales orientados al usuario (destinados al acceso manual mediante navegador web) redirijan automáticamente de HTTP a HTTPS, mientras que otros servicios o puntos finales no implementen redirecciones transparentes. Esto evita una situación en la que un cliente esté enviando erroneamente solicitudes HTTP no cifradas, pero como las solicitudes se redirigen automáticamente a HTTPS, la filtración de datos sensibles pasa desapercibida. | 2 |
| **4.1.3** | Verifique que cualquier campo de cabecera HTTP utilizado por la aplicación y establecido por una capa intermedia, como un balanceador de carga, un proxy web o un servicio backend-for-frontend, no pueda ser sobrescrito por el usuario final. Los encabezados de ejemplo podrían incluir X-Real-IP, X-Forwarded-* o X-User-ID. | 2 |
| **4.1.4** | Verifique que solo se puedan utilizar los métodos HTTP que la aplicación o su API admiten explícitamente (incluido OPTIONS durante las solicitudes de preflight) y que se bloqueen los métodos no utilizados. | 3 |
| **4.1.5** | Verifique que se utilicen firmas digitales por mensaje para aportar una garantía adicional además de las protecciones de transporte para solicitudes o transacciones altamente sensibles o que atraviesen varios sistemas. | 3 |

## V4.2 Validación de la estructura de mensajes HTTP

Esta sección explica cómo debe validarse la estructura y los campos de cabecera de un mensaje HTTP para prevenir ataques como el smuggling de solicitudes, la división de respuestas, la inyección de cabeceras y la denegación de servicio mediante mensajes HTTP excesivamente largos.

Estos requisitos son relevantes para el procesamiento y la generación generales de mensajes HTTP, pero son especialmente importantes al convertir mensajes HTTP entre diferentes versiones de HTTP.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **4.2.1** | Verifique que todos los componentes de la aplicación (incluidos los balanceadores de carga, los firewalls y los servidores de aplicaciones) determinen los límites de los mensajes HTTP entrantes utilizando el mecanismo apropiado para la versión de HTTP para prevenir el smuggling de solicitudes HTTP. En HTTP/1.x, si existe un campo de cabecera Transfer-Encoding, el campo Content-Length debe ignorarse conforme a la RFC 2616. Cuando se utiliza HTTP/2 o HTTP/3, si existe un campo de cabecera Content-Length, el receptor debe asegurarse de que es consistente con la longitud de los marcos DATA. | 2 |
| **4.2.2** | Verifique que, al generar mensajes HTTP, el campo de cabecera Content-Length no entre en conflicto con la longitud del contenido según lo determinado por el encuadre del protocolo HTTP, para prevenir ataques de smuggling de solicitudes. | 3 |
| **4.2.3** | Verifique que la aplicación no envía ni acepta mensajes HTTP/2 o HTTP/3 con campos de cabecera específicos de la conexión, como Transfer-Encoding, para prevenir ataques de división de respuestas e inyección de cabeceras. | 3 |
| **4.2.4** | Verifique que la aplicación solo acepta solicitudes HTTP/2 y HTTP/3 en las que los campos de cabecera y sus valores no contienen ninguna secuencia CR (\r), LF (\n) ni CRLF (\r\n), para prevenir ataques de inyección de cabeceras. | 3 |
| **4.2.5** | Verifique que, si la aplicación (backend o frontend) construye y envía solicitudes, utiliza validación, saneamiento u otros mecanismos para evitar crear URIs (como para llamadas a API) o campos de cabecera HTTP de solicitud (como Authorization o Cookie) demasiado largos para que el componente receptor los acepte. Esto podría causar una denegación de servicio, por ejemplo al enviar una solicitud excesivamente larga (por ejemplo, una cabecera Cookie muy larga), que hace que el servidor responda siempre con un estado de error. | 3 |

## V4.3 GraphQL

GraphQL se está volviendo más común como forma de crear clientes ricos en datos que no están acoplados estrechamente a una variedad de servicios backend. Esta sección cubre las consideraciones de seguridad para GraphQL.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **4.3.1** | Verifique que se utilice una lista permitida de consultas, limitación de profundidad, limitación de cantidad o análisis de coste de consultas para prevenir la denegación de servicio (DoS) de GraphQL o de expresiones de la capa de datos como resultado de consultas anidadas y costosas. | 2 |
| **4.3.2** | Verifique que las consultas de introspección de GraphQL estén deshabilitadas en el entorno de producción a menos que la API de GraphQL esté pensada para ser utilizada por otras partes. | 2 |

## V4.4 WebSocket

WebSocket es un protocolo de comunicaciones que proporciona un canal de comunicación bidireccional simultáneo a través de una única conexión TCP. Fue estandarizado por la IETF como RFC 6455 en 2011 y es distinto de HTTP, aunque está diseñado para funcionar a través de los puertos HTTP 443 y 80.

Esta sección proporciona requisitos de seguridad clave para prevenir ataques relacionados con la seguridad de la comunicación y la gestión de sesiones que explotan específicamente este canal de comunicación en tiempo real.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **4.4.1** | Verifique que se utilice WebSocket sobre TLS (WSS) para todas las conexiones WebSocket. | 1 |
| **4.4.2** | Verifique que, durante el handshake inicial de WebSocket HTTP, el campo de cabecera Origin se compruebe con respecto a una lista de orígenes permitidos para la aplicación. | 2 |
| **4.4.3** | Verifique que, si no puede utilizarse la gestión de sesiones estándar de la aplicación, se utilizan tokens dedicados para ello, que cumplan los requisitos de seguridad relevantes de gestión de sesiones. | 2 |
| **4.4.4** | Verifique que los tokens dedicados de gestión de sesiones de WebSocket se obtengan o validen inicialmente a través de la sesión HTTPS autenticada previamente al transicionar una sesión HTTPS existente a un canal WebSocket. | 2 |

## Referencias

Para obtener más información, consulte también:

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* Recursos sobre autorización de GraphQL en [graphql.org](https://graphql.org/learn/authorization/) y [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods).
* [OWASP Web Security Testing Guide: GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [OWASP Web Security Testing Guide: Testing WebSockets](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)
