# Evaluación y Certificación

## Postura de OWASP sobre Certificaciones ASVS y Marcas de Confianza

OWASP, como una organización neutral para el proveedor sin fines de lucro, actualmente no certifica ningún proveedor, verificador o software.

Todas esas afirmaciones de garantía, marcas de confianza o certificaciones no son examinadas, registradas o certificadas oficialmente por OWASP, por lo que una organización que se base en esa opinión debe tener cuidado con la confianza depositada en cualquier tercero o marca de confianza que reclame la certificación ASVS.

Esto no debe impedir que las organizaciones ofrezcan tales servicios de garantía, siempre y cuando no reclamen la certificación oficial de OWASP.

## Orientación para las Organizaciones Certificadoras

ASVS se puede utilizar como una verificación de libro abierto de la aplicación, incluido el acceso abierto y sin restricciones a recursos clave como arquitectos, desarrolladores, documentación del proyecto, código fuente, acceso autenticado a sistemas de prueba (incluido el acceso a una o más cuentas en cada rol), especialmente para verificaciones de nivel L2 y L3.

Históricamente, las pruebas de penetración y las revisiones de código seguro han incluido cuestiones "por excepción", es decir, las pruebas fallidas aparecen en el informe final. Una organización certificadora debe incluir en cualquier informe el alcance de la verificación (especialmente si un componente clave está fuera del ámbito, como la autenticación SSO), un resumen de los resultados de la verificación, incluidas las pruebas pasadas y erróneas, con indicaciones claras de cómo resolver las pruebas con errores.

Ciertos requisitos de verificación pueden no ser aplicables al software bajo prueba. Por ejemplo, si proporciona una API de capa de servicio stateless sin una implementación de cliente a sus consumidores, muchos de los requisitos de V3 Administración de Sesiones no son directamente aplicables. En tales casos, una organización certificadora todavía puede reclamar el cumplimiento completo de ASVS, pero debe indicar claramente en cualquier informe una razón para la inaplicabilidad de dichos requisitos de verificación excluidos.

Mantener documentos de trabajo detallados, capturas de pantalla o películas, guiones para explotar de forma fiable y repetidamente un problema, y registros electrónicos de pruebas, como interceptar registros de proxy y notas asociadas, como una lista de limpieza, se considera práctica estándar de la industria y puede ser realmente útil como pruebas de los hallazgos para los desarrolladores más dudosos. No basta con simplemente ejecutar una herramienta e informar sobre los errores; esto no proporciona (en absoluto) pruebas suficientes de que todas las cuestiones a nivel de certificación han sido probadas y probadas a fondo. En caso de controversia, debe haber pruebas de garantía suficientes para demostrar que todos y cada uno de los requisitos verificados han sido probados.

### Método de Pruebas

Las organizaciones de certificación son libres de elegir los métodos de prueba adecuados, pero deben indicarlas en un informe.

Dependiendo de la aplicación sometida a prueba y del requisito de verificación, se pueden utilizar diferentes métodos de prueba para obtener una confianza similar en los resultados. Por ejemplo, la validación de la eficacia de los mecanismos de verificación de entrada de una aplicación puede analizarse con una prueba de penetración manual o mediante análisis de código fuente.

#### El Rol de las Herramientas Automatizadas de Pruebas de Seguridad

Se recomienda el uso de herramientas de pruebas de penetración automatizadas para proporcionar la mayor cobertura posible.

No es posible completar en su totalidad la verificación de ASVS utilizando solo herramientas de pruebas de penetración automatizadas. Si bien una gran mayoría de los requisitos en N1 se pueden realizar mediante pruebas automatizadas, la mayoría general de los requisitos no son susceptibles a las pruebas de penetración automatizadas.

Tenga en cuenta que las líneas entre las pruebas automatizadas y manuales se han difuminado a medida que la industria de seguridad de aplicaciones madura. Las herramientas automatizadas a menudo son ajustadas manualmente por expertos y los probadores manuales a menudo aprovechan una amplia variedad de herramientas automatizadas.

#### El rol de las Pruebas de Penetración

En la versión 4.0, decidimos hacer L1 completamente verificable con pruebas de penetración sin acceso al código fuente, documentación o desarrolladores. Dos elementos de logging, que están obligados a cumplir con OWASP Top 10 2017 A10, requerirán entrevistas, capturas de pantalla u otra captura de evidencia, al igual que lo hacen en el Top 10 2017 de OWASP. Sin embargo, las pruebas sin acceso a la información necesaria no son un método ideal de verificación de seguridad, ya que pierde la posibilidad de revisar el origen, identificar las amenazas y los controles que faltan, y realizar una prueba mucho más exhaustiva en un plazo más corto.

Siempre que sea posible, se requiere acceso a los desarrolladores, documentación, código y acceso a una aplicación de prueba con datos que no sean de producción al realizar una evaluación L2 o L3. Las pruebas de penetración realizadas a estos niveles requieren este nivel de acceso, que llamamos "revisiones híbridas" o "pruebas de penetración híbrida".

## Otros usos para ASVS

Además de utilizarse para evaluar la seguridad de una aplicación, hemos identificado una serie de otros usos potenciales para ASVS.

### Como una Guía Detallada de la Arquitectura de Seguridad

Uno de los usos más comunes para el estándar de verificación de seguridad en aplicaciones es como un recurso para los arquitectos de seguridad. A la arquitectura de seguridad empresarial aplicada de Sherwood (SABSA) le falta una gran cantidad de información que es necesaria para completar una revisión exhaustiva de la arquitectura de seguridad en aplicaciones. ASVS se puede utilizar para llenar esas lagunas al permitir que los arquitectos de seguridad elijan mejores controles para problemas comunes, como patrones de protección de datos y estrategias de validación de entradas.

### Como un Reemplazo de Listas de Verificación de Codificación Segura Listas para Usar

Muchas organizaciones pueden beneficiarse de la adopción de ASVS, eligiendo uno de los tres niveles, o bifurcando ASVS y cambiando lo que se requiere para cada nivel de riesgo de aplicación de una manera específica del dominio. Animamos a este tipo de bifurcación siempre y cuando se mantenga la trazabilidad, de modo que si una aplicación ha pasado el requisito 4.1, esto significa lo mismo para las copias bifurcadas que el estándar a medida que evoluciona.

### Como una Guía para Pruebas Automatizadas de Unidad e Integración

El ASVS está diseñado para ser altamente comprobable, con la única excepción de los requisitos de código arquitectónico y malicioso. Mediante la creación de pruebas de unidad e integración que prueban casos de fuzz y abuso específicos y relevantes, la aplicación se vuelve casi autocomprobación con todas y cada una de las compilaciones. Por ejemplo, se pueden crear pruebas adicionales para el conjunto de pruebas para un controlador de inicio de sesión, probando el parámetro username para los nombres de usuario predeterminados comunes, la enumeración de la cuenta, el forzamiento bruto, la inyección LDAP y SQL, y XSS. Del mismo modo, una prueba en el parámetro de contraseña debe incluir contraseñas comunes, longitud de contraseña, inyección de bytes nulos, eliminación del parámetro, XSS y más.

### Para la Formación en Desarrollo Seguro

ASVS también se puede utilizar para definir las características del software seguro. Muchos cursos de "codificación segura" son simplemente cursos de hacking ético con un ligero barniz de tips de codificación. Esto no necesariamente ayuda a los desarrolladores a escribir código más seguro. En su lugar, los cursos de desarrollo seguro pueden utilizar el ASVS con un fuerte enfoque en los controles proactivos que provee, en lugar de las 10 cosas negativas que no se deben hacer.

### Como un Conductor para la Seguridad de Aplicaciones Ágiles

ASVS se puede utilizar en un proceso de desarrollo ágil como framework para definir tareas específicas que el equipo debe implementar para tener un producto seguro. Un enfoque podría ser: A partir del nivel 1, compruebe la aplicación o el sistema específico según los requisitos de ASVS para el nivel especificado, busque qué controles faltan y genere tickets/tareas específicas en el "backlog". Esto ayuda a priorizar tareas específicas (o refinamiento) y hace que la seguridad sea visible en el proceso ágil. Esto también se puede utilizar para priorizar las tareas de auditoría y revisión en la organización, donde un requisito específico de ASVS puede ser un impulsor para la revisión, refactorización o auditoría para un miembro específico del equipo y visible como "deuda" en el backlog que debe ser hecho eventualmente.

### Como Marco de Trabajo para Orientar la Adquisición de Software Seguro

ASVS es un gran marco para ayudar con la adquisición segura de software o la adquisición de servicios de desarrollo personalizados. El comprador puede simplemente establecer un requisito de que el software que desea adquirir debe desarrollarse en el nivel X de ASVS, y solicitar que el vendedor demuestre que el software cumple con el nivel X de ASVS. Esto funciona bien cuando se combina con el anexo OWASP del contrato de software seguro.
