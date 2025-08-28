# V2 Validación y lógica de negocio

## Objetivo del control

Este capítulo tiene como objetivo garantizar que una aplicación verificada cumpla los siguientes objetivos de alto nivel:

* La información que recibe la aplicación cumple con las expectativas de negocio o funcionales.
* El flujo de lógica de negocio es secuencial, se procesa en orden y no se puede omitir.
* La lógica de negocio incluye límites y controles para detectar y prevenir ataques automatizados, como por ejemplo transferencias continuas de fondos pequeños o agregar de un millón de amigos a la vez.
* Los flujos de lógica de negocio de alto valor han considerado casos de abuso y actores maliciosos, cuentan con protección contra suplantación de identidad (spoofing), manipulación (tampering), divulgación de información (information disclosure) y ataques de elevación de privilegios.

## V2.1 Documentación de validación y lógica de negocio

La documentación de validación y lógica de negocio debe definir claramente los límites de la lógica de negocio, reglas de validación y la consistencia contextual de los elementos de datos combinados de modo que quede claro qué debe implementarse en la aplicación.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **2.1.1** | Verifique que la documentación de la aplicación defina las reglas de validación de entrada para comprobar la validez de los datos con respecto a la estructura esperada. Estos pueden ser formatos de datos comunes como números de tarjetas de crédito, direcciones de correo electrónico, números de teléfono, o incluso un formato de datos interno. | 1 |
| **2.1.2** | Verifique que la documentación de la aplicación defina cómo validar la consistencia lógica y contextual de los elementos de datos combinados, como por ejemplo verificar que el suburbio y el código postal (ZIP) coincidan. | 2 |
| **2.1.3** | Verifique que las expectativas sobre los límites y validaciones de la lógica de negocio estén documentadas, tanto por los límites por usuario como a nivel global en toda la aplicación. | 2 |

## V2.2 Validación de entradas

Los controles eficaces de validación de entrada refuerzan las expectativas de negocio o funcionales en cuanto al tipo de datos que la aplicación espera recibir. Esto garantiza una buena calidad de los datos y reduce la superficie de ataque. Sin embargo, no elimina ni reemplaza la necesidad de usar una codificación, parametrización o sanitización correctas al usar los datos en otro componente o al presentarlos para su salida.

En este contexto, la "entrada" podría provenir de una amplia variedad de fuentes, incluidos campos de formulario HTML, solicitudes REST, parámetros de URL, campos de encabezado HTTP, cookies, archivos en disco, bases de datos y API externas.

Un control de lógica de negocios podría verificar que una entrada particular sea un número menor que 100. Una expectativa funcional podría verificar que un número esté por debajo de un cierto umbral ya que ese número controla cuántas veces se realizará un bucle particular y un número alto podría llevar a un procesamiento excesivo y a una posible condición para denegación de servicio.

Si bien la validación de esquemas no es obligatoria explícitamente, podría ser el mecanismo más eficaz para una cobertura completa de la validación de las API HTTP u otras interfaces que utilizan JSON o XML.

Tenga en cuenta los siguientes puntos sobre la validación de esquemas:

* La "versión publicada" de la especificación de validación del esquema JSON se considera lista para producción, pero no estrictamente "estable". Al utilizar la validación del esquema JSON, asegúrese de que no haya incompatibilidades con las directrices de los requisitos a continuación.
* Cualquier librería de validación del esquema JSON en uso también deben supervisarse y actualizarse si es necesario una vez que se formalice el estándar.
* No se debe utilizar la validación de DTD y se debe deshabilitar la evaluación de DTD del framework para evitar problemas de ataques XXE contra DTD.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **2.2.1** | Verifique que la entrada esté validada para cumplir con las expectativas de negocio o funcionales para esa entrada. Esto debe, o bien, usar una validación positiva con una lista de valores permitidos, patrones, rangos, o basarse en la comparación de la entrada con una estructura esperada y límites lógicos según reglas predefinidas. Para L1, esto puede centrarse en la entrada utilizada para tomar decisiones de negocio o de seguridad específicas. Para L2 y superiores, esto debe aplicarse a todas las entradas. | 1 |
| **2.2.2** | Verifique que la aplicación esté diseñada para aplicar la validación de entrada en una capa de servicio confiable. Si bien la validación del lado del cliente mejora la usabilidad y debe fomentarse, no debe considerarse un control de seguridad. | 1 |
| **2.2.3** | Verifique que la aplicación garantice que las combinaciones de elementos de datos relacionados sean razonables según las reglas predefinidas. | 2 |

## V2.3 Seguridad de la lógica de negocio

Esta sección considera los requerimientos clave para garantizar que la aplicación haga cumplir los procesos de lógica de negocio de la manera correcta y no sea vulnerable a ataques que exploten la lógica y el flujo de la aplicación.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **2.3.1** | Verifique que la aplicación solo procese flujos de lógica de negocio para el mismo usuario en el orden de pasos secuencial esperado y sin omitir pasos. | 1 |
| **2.3.2** | Verifique que los límites de la lógica de negocio se implementen según la documentación de la aplicación para evitar que se exploten fallas de la lógica de negocio. | 2 |
| **2.3.3** | Verifique que las transacciones se estén utilizando a nivel de lógica de negocio de tal manera que, o una operación de lógica de negocio finaliza exitosamente en su totalidad o es reversada al estado correcto previo. | 2 |
| **2.3.4** | Verifique que se utilicen mecanismos de bloqueo a nivel de lógica de negocios para garantizar que recursos de cantidad limitada (como asientos de teatro o franjas horarias de entrega) no se puedan reservar dos veces mediante la manipulación de la lógica de la aplicación. | 2 |
| **2.3.5** | Verifique que los flujos de lógica de negocio de alto valor requieran la aprobación de múltiples usuarios para evitar acciones no autorizadas o accidentales. Esto podría incluir entre otras cosas, grandes transferencias monetarias, aprobaciones de contratos, acceso a información clasificada o anulaciones de seguridad en manufactura. | 3 |

## V2.4 Anti-automatización

Esta sección incluye controles anti-automatización para garantizar que se requieran interacciones similares a las humanas y se eviten solicitudes automatizadas excesivas.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **2.4.1** | Verifique que existan controles anti-automatización para proteger contra llamadas excesivas a funciones de la aplicación que podrían provocar una exfiltración de datos, creación de datos basura, agotamiento de cuotas, violaciones de límites de velocidad, denegación de servicio o uso excesivo de recursos valiosos. | 2 |
| **2.4.2** | Verificar que los flujos de lógica de negocio requieran tiempos humanos realistas, evitando envíos de transacciones excesivamente rápidos. | 3 |

## Referencias

Para obtener más información consulte:

* [OWASP Web Security Testing Guide: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Web Security Testing Guide: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README)
* Anti-automation can be achieved in many ways, including the use of the [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [JSON Schema](https://json-schema.org/specification.html)
