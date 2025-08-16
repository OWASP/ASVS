# Evaluación y certificación

## Postura de OWASP sobre las certificaciones y marcas de confianza de ASVS

OWASP, como organización sin fines de lucro independiente de proveedores, no certifica a ningún proveedor, verificador ni software. Ninguna garantía, marca de confianza o certificación que afirme conformidad con ASVS cuenta con el respaldo oficial de OWASP, por lo que las organizaciones deben ser cautelosas con las afirmaciones de terceros sobre la certificación ASVS.

Las organizaciones pueden ofrecer servicios de garantía, siempre y cuando no afirmen contar con la certificación oficial de OWASP.

## Cómo verificar el cumplimiento de ASVS

El ASVS es deliberadamente no prescriptivo sobre cómo verificar el cumplimiento a nivel de una guía de pruebas. Sin embargo, es importante destacar algunos puntos clave.

### Informes de verificación

Las pruebas de penetración tradicionales informan los problemas por “excepción”, enumerando únicamente los fallos. Sin embargo, un informe de certificación de ASVS debe incluir el alcance, un resumen de todos los requerimientos comprobados, los requerimientos donde se detectaron excepciones y una guía para la solución de problemas. Algunos requerimientos pueden no ser aplicables (por ejemplo, la gestión de sesiones en API sin estado), lo cual debe indicarse en el informe.

### Alcance de la verificación

Una organización que desarrolla una aplicación generalmente no implementará todos los requerimientos ya que algunos pueden ser irrelevantes o menos significativos según la funcionalidad de la aplicación. El verificador debe aclarar el alcance de la verificación, incluyendo el nivel que la organización intenta alcanzar y los requerimientos incluidos. Esto debe hacerse desde la perspectiva de lo incluido, no de lo que no se incluyó. También debe emitir una opinión sobre la justificación de la exclusión de los requerimientos no implementados.

Esto debería permitir al usuario de un informe de verificación comprender el contexto de la verificación y tomar una decisión informada sobre el nivel de confianza que puede depositar en la aplicación.

Las organizaciones certificadoras pueden elegir sus métodos de prueba pero deben divulgarlos en el informe, que idealmente debería ser repetible. Se pueden utilizar diferentes métodos, como pruebas de penetración manuales o análisis de código fuente, para verificar aspectos como la validación de entradas según la aplicación y los requerimientos.

### Mecanismos de verificación

Existen diversas técnicas que pueden ser necesarias para verificar requerimientos específicos de ASVS. Además de las pruebas de penetración (utilizando credenciales válidas para obtener una cobertura completa en la aplicación), la verificación de los requerimientos de ASVS puede requerir acceso a la documentación, el código fuente, la configuración y al personal involucrado en el proceso de desarrollo, especialmente para verificar los requerimientos de nivel L2 y L3. Es práctica habitual proporcionar evidencia sólida de los hallazgos con documentación detallada, que puede incluir documentos de trabajo, capturas de pantalla, scripts y logs de las pruebas. La simple ejecución de una herramienta automatizada sin pruebas exhaustivas no es suficiente para la certificación ya que cada requerimiento debe probarse de forma verificable.

El uso de la automatización para verificar los requerimientos de ASVS es un tema de constante interés. Por lo tanto, es importante aclarar algunos puntos relacionados con las pruebas automatizadas y de caja negra.

#### El papel de las herramientas de pruebas de seguridad automatizadas

Cuando las herramientas de pruebas de seguridad automatizadas, como las de Pruebas de Seguridad Dinámicas y Estáticas (DAST y SAST) se implementan correctamente en pipeline de construcción (build pipeline), podrían identificar algunos problemas de seguridad que no existen. Sin embargo, sin una configuración y un ajuste cuidadosos, no proporcionarán la cobertura necesaria y el nivel de ruido impedirá que los problemas de seguridad reales se identifiquen y mitiguen.

Si bien esto puede cubrir algunos de los requerimientos técnicos más básicos y directos, como los relacionados con la codificación o la sanitización de la salida, es fundamental tener en cuenta que estas herramientas no podrán verificar por completo muchos de los requerimientos más complejos de ASVS ni los relacionados con la lógica de negocio y de control de accesos.

Para requerimientos menos sencillos es probable que se pueda seguir utilizando la automatización pero será necesario escribir verificaciones específicas de la aplicación para lograrlo. Estas pueden ser similares a las pruebas unitarias y de integración que la organización ya esté utilizando. Por lo tanto, es posible utilizar esta infraestructura de automatización de pruebas existente para escribir estas pruebas específicas de ASVS. Si bien esto requerirá una inversión a corto plazo, los beneficios a largo plazo de poder verificar continuamente los requerimientos de ASVS serán significativos.

En resumen, capacidad de probar usando automatización != ejecutar una herramienta adquirida. 

#### El papel de las pruebas de penetración

Si bien el nivel L1 en la versión 4.0 se optimizó para realizar pruebas de "caja negra" (sin documentación ni código fuente), incluso entonces, el estándar dejaba claro que no se trata de una actividad de aseguramiento eficaz y que debería desaconsejarse encarecidamente.

Realizar pruebas sin acceso a la información adicional necesaria es un mecanismo ineficiente e ineficaz para la verificación de la seguridad ya que desaprovecha la posibilidad de revisar el código fuente, identificar amenazas y controles faltantes, y realizar una prueba mucho más exhaustiva en un plazo más corto.

Se recomienda enormemente realizar pruebas de penetración basadas en documentación o código fuente (híbridas), que permiten el acceso completo a los desarrolladores y a la documentación de la aplicación en lugar de las pruebas de penetración tradicionales. Esto será sin duda necesario para verificar muchos de los requerimientos de ASVS.
