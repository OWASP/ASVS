# V7 : Requisitos de verificación de logging y manejo de errores

## Objetivo de Control

El objetivo principal del control y registro de errores es proporcionar información útil para el usuario, los administradores y los equipos de respuesta a incidentes. El objetivo no es crear cantidades masivas de registros, sino registros de alta calidad, con más señal que el ruido descartado.

Los registros de alta calidad a menudo contendrán datos confidenciales y deben protegerse según las leyes o directivas locales de privacidad de datos. Esto debe incluir:

 * No recopilar o registrar información confidencial a menos que sea específicamente necesario.
 * Garantizar que toda la información registrada se maneje de forma segura y protegida según su clasificación de datos.
 * Asegurarse de que los registros no se almacenan para siempre, pero tienen una duración absoluta que es lo más corta posible.

Si los registros contienen datos privados o confidenciales, la definición de cuyos varían de un país a otro, los registros se convierten en parte de la información más sensible de la aplicación y, por lo tanto, son muy atractivos para los atacantes por derecho propio.

También es importante asegurarse de que la aplicación falla de forma segura y que los errores no revelan información innecesaria.

## V7.1 Exigences relatives au contenu des journaux

Logging de información confidencial es peligroso: los registros se clasifican a sí mismos, lo que significa que deben cifrarse, estar sujetos a políticas de retención y deben divulgarse en las auditorías de seguridad. Asegúrese de que solo la información necesaria se mantiene en logs, y ciertamente no se registre información de pagos, credenciales (incluidos los tokens de sesión), información confidencial o de identificación personal.

V7.1 cubre OWASP Top 10 2017:A10. Como 2017:A10 y esta sección no son comprobables por penetración, es importante para:

 * Desarrolladores para asegurar el cumplimiento total de esta sección, como si todos los elementos estuvieran marcados.
 * Como probadores de penetración L1 para validar el cumplimiento completo de todos los elementos en V7.1 a través de entrevistas, capturas de pantalla o aserción.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.1.1** | Compruebe que la aplicación no registra las credenciales ni los detalles de pago. Los tokens de sesión solo deben almacenarse en registros de forma irreversible y hasheados. ([C9, C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 532 |
| **7.1.2** | Compruebe que la aplicación no registra otros datos confidenciales tal como se definen en las leyes de privacidad locales o la política de seguridad pertinente. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 532 |
| **7.1.3** | Compruebe que la aplicación registra eventos relevantes para la seguridad, incluidos los eventos de autenticación correctos y con errores, los errores de control de acceso, los errores de deserialización y los errores de validación de entrada. ([C5, C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 778 |
| **7.1.4** | Compruebe que cada evento de registro incluye la información necesaria que permitiría una investigación detallada de la escala de tiempo cuando se produce un evento. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 778 |

## V7.2 Requisitos de procesamiento del Log

El registro oportuno es fundamental para los eventos de auditoría, el triage y la escalada. Asegúrese de que los registros de la aplicación estén claros y se puedan monitorear y analizar fácilmente localmente o enviar el registro a un sistema de monitoreo remoto.

V7.2 cubre OWASP Top 10 2017:A10. Como 2017:A10 y esta sección no son comprobables por penetración, es importante para:

 * Desarrolladores para asegurar el cumplimiento total de esta categoría, como si todos los elementos estuvieran marcados como L1.
 * Probadores de penetración para validar el cumplimiento completo de todos los elementos en V7.2 a través de entrevistas, capturas de pantalla o aserción.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.2.1** | Compruebe que se registran todas las decisiones de autenticación, sin almacenar tokens o contraseñas de sesión confidenciales. Esto debe incluir solicitudes con los metadatos relevantes necesarios para las investigaciones de seguridad. | | ✓ | ✓ | 778 |
| **7.2.2** | Compruebe que se pueden registrar todas las decisiones de control de acceso y que se registran todas las decisiones erróneas. Esto debe incluir solicitudes con los metadatos pertinentes necesarios para las investigaciones de seguridad. | | ✓ | ✓ | 285 |

## V7.3 Requisitos de protección de Logs

Los registros que se pueden modificar o eliminar trivialmente son inútiles para investigaciones y procesamientos. La divulgación de registros puede exponer detalles internos sobre la aplicación o los datos que contiene. Se debe tener cuidado al proteger los registros de la divulgación, modificación o eliminación no autorizadas.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.3.1** | Compruebe que la aplicación encodea adecuadamente los datos proporcionados por el usuario para evitar la inyección de registros. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 117 |
| **7.3.2** | Compruebe que todos los eventos están protegidos contra la inyección cuando se ven en el software de visualización de Logs. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 117 |
| **7.3.3** | Compruebe que los registros de seguridad están protegidos contra el acceso y la modificación no autorizados. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 200 |
| **7.3.4** | Compruebe que la fuente donde se lee el tiempo están sincronizados con la hora y la zona horaria correctas. Considere firmemente el registro solo en UTC si los sistemas son globales para ayudar con el análisis forense posterior al incidente. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

**Nota:** La codificación de registros (7.3.1) es difícil de probar y revisar mediante herramientas dinámicas automatizadas y pruebas de penetración, pero los arquitectos, desarrolladores y revisores de código fuente deben considerarlo un requisito de L1.

## V7.4 Control de Errores

El propósito del control de errores es permitir que la aplicación proporcione eventos relevantes para la seguridad para el monitoreo, el triage y la escalada. El propósito no es crear registros. Al registrar eventos relacionados con la seguridad, asegúrese de que hay un propósito para el registro y que se puede distinguir por SIEM o software de análisis.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.4.1** | Compruebe que se muestra un mensaje genérico cuando se produce un error inesperado o sensible a la seguridad, potencialmente con un identificador único que el personal de soporte técnico puede usar para investigar. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 210 |
| **7.4.2** | Compruebe que el control de excepciones (o un equivalente funcional) se utiliza en todo el código base para tener en cuenta las condiciones de error esperadas e inesperadas. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 544 |
| **7.4.3** | Compruebe que se define un controlador de errores de "último recurso" que detectará todas las excepciones no controladas. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 431 |

**Nota:** Ciertos idiomas, como Swift and Go - y a través de la práctica de diseño común - muchos lenguajes funcionales, no admiten excepciones o controladores de eventos de último recurso. En este caso, los arquitectos y desarrolladores deben usar una forma amigable de patrón, lenguaje o marco de trabajo para garantizar que las aplicaciones puedan controlar de forma segura eventos excepcionales, inesperados o relacionados con la seguridad.

## Referencias

Para obtener más información, véase también:

* [OWASP Testing Guide 4.0 content: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README.html)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
