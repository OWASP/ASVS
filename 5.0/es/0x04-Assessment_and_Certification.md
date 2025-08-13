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

There are a number of different techniques which may be needed to verify specific ASVS requirements. Aside from penetration testing (using valid credentials to get full application coverage), verifying ASVS requirements may require access to documentation, source code, configuration, and the people involved in the development process. Especially for verifying L2 and L3 requirements. It is standard practice to provide robust evidence of findings with detailed documentation, which may include work papers, screenshots, scripts, and testing logs. Merely running an automated tool without thorough testing is insufficient for certification, as each requirement must be verifiably tested.

The use of automation to verify ASVS requirements is a topic that is constantly of interest. It is therefore important to clarify some points related to automated and black box testing.

#### El papel de las herramientas de pruebas de seguridad automatizadas

When automated security testing tools such as Dynamic and Static Application Security Testing tools (DAST and SAST) are correctly implemented in the build pipeline, they may be able to identify some security issues that should never exist. However, without careful configuration and tuning they will not provide the required coverage and the level of noise will prevent real security issues from being identified and mitigated.

Whilst this may provide coverage of some of the more basic and straightforward technical requirements such as those relating to output encoding or sanitization, it is critical to note that these tools will be unable entirely to verify many of the more complicated ASVS requirements or those that relate to business logic and access control.

For less straightforward requirements, it is likely that automation can still be utilized but application specific verifications will need to be written to achieve this. These may be similar to unit and integration tests that the organization may already be using. It may therefore be possible to use this existing test automation infrastructure to write these ASVS specific tests. Whilst doing this will require short term investment, the long term benefits being able to continually verify these ASVS requirements will be significant.

In summary, testable using automation != running an off the shelf tool.

#### El papel de las pruebas de penetración

Whilst L1 in version 4.0 was optimized for "black box" (no documentation and no source) testing to occur, even then the standard was clear that it is not an effective assurance activity and should be actively discouraged.

Testing without access to necessary additional information is an inefficient and ineffective mechanism for security verification, as it misses out on the possibility of reviewing the source, identifying threats and missing controls, and performing a far more thorough test in a shorter timeframe.

It is strongly encouraged to perform documentation or source code-led (hybrid) penetration testing, which have full access to the application developers and the application's documentation, rather than traditional penetration tests. This will certainly be necessary in order to verify many of the ASVS requirements.
