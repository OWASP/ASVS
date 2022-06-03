# V2 Autenticación

## Objetivo de Control

La autenticación es el acto de establecer, o confirmar, a alguien (o algo) como auténtico y que las afirmaciones hechas por una persona o sobre un dispositivo son correctas, resistentes a la suplantación e impiden la recuperación o interceptación de contraseñas.

Cuando el ASVS fue lanzado por primera vez, "username + password" era la forma más común de autenticación fuera de los sistemas de alta seguridad. La autenticación multifactor (MFA) se aceptaba comúnmente en los círculos de seguridad, pero rara vez se requería en otros lugares. A medida que aumentaba el número de violación de contraseñas, la idea de que los nombres de usuario son de alguna manera confidenciales y las contraseñas desconocidas, hizo que muchos controles de seguridad fueran insostenibles. Por ejemplo, NIST 800-63 considera los nombres de usuario y la autenticación basada en conocimientos (KBA) como información pública, SMS y notificaciones por correo electrónico como ["restricted" authenticator types](https://pages.nist.gov/800-63-FAQ/#q-b1), y contraseñas como pre-violadas. Esta realidad hace que los autenticadores basados en el conocimiento, la recuperación de SMS y correo electrónico, el historial de contraseñas, la complejidad y los controles de rotación sean inútiles. Estos controles siempre han sido menos que útiles, a menudo obligando a los usuarios a llegar a contraseñas débiles cada pocos meses, pero con el lanzamiento de más de 5 billones de filtraciones de "username + password", es el momento de seguir adelante.

De todas los capítulos del ASVS, los que más cambiaron son Autenticación y Administración de sesiones. La adopción de una práctica moderna, efectiva y basada en evidencia será un desafío para muchos, y eso está perfectamente bien. Tenemos que comenzar ahora la transición a un futuro post-contraseña.

## NIST 800-63 - Estándar de autenticación moderno basado en evidencia

[NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) es un estándar moderno basado en la evidencia, y representa el mejor consejo disponible, independientemente de la aplicabilidad. El estándar es útil para todas las organizaciones de todo el mundo, pero es particularmente relevante para las agencias estadounidenses y para quienes trabajen con las agencias estadounidenses.

La terminología NIST 800-63 puede ser un poco confusa al principio, especialmente si solo estás acostumbrado a la autenticación de "username + password". Los avances en la autenticación moderna son necesarios, por lo que tenemos que introducir terminología que se convertirá en algo común en el futuro, pero entendemos la dificultad de entender hasta que la industria se asiente en estos nuevos términos. Se proporciona un glosario al final de este capítulo para mayor detalle. Hemos reformulado muchos requisitos para satisfacer la intención del requisito, en lugar de sólo su letra. Por ejemplo, el ASVS utiliza el término "contraseña" cuando NIST utiliza "secreto memorizado" en todo el estándar.

ASVS V2 Autenticación, V3 Administración de sesiones, y en menor medida, V4 Controles de acceso se han adaptado para que sean un subconjunto compatible de controles NIST 800-63b seleccionados, centrados en amenazas comunes y debilidades de autenticación comúnmente explotadas. Cuando se requiera el cumplimiento completo del NIST 800-63, consulte NIST 800-63.63.

### Seleccionando un nivel adecuado de NIST AAL

ASVS ha intentado mapear ASVS L1 con los requisitos NIST AAL1, N2 a AAL2, y L3 a AAL3. Sin embargo, el enfoque de ASVS Level 1 como controles "esenciales" puede no ser necesariamente el nivel AAL correcto para verificar una aplicación o API. Por ejemplo, si la aplicación es una aplicación de nivel 3 o tiene requisitos reglamentarios para ser AAL3, el nivel 3 debe elegirse en los capítulos V2 y V3 Administración de sesiones. La elección del nivel de afirmación de autenticación (AAL; Por sus siglas en inglés) compatible con NIST se debe realizar según las pautas NIST 800-63b como se establece en *Seleccionando AAL* en [NIST 800-63b Section 6.2](https://pages.nist.gov/800-63-3/sp800-63-3.html#AAL_CYOA).

## Leyenda

Las aplicaciones siempre pueden exceder los requisitos del nivel actual, especialmente si la autenticación moderna está en el roadmap de una aplicación. Anteriormente, el ASVS requería MFA obligatorio. NIST no requiere MFA obligatorio. Por lo tanto, hemos utilizado una designación opcional en este capítulo para indicar dónde el ASVS alienta pero no requiere un control. Las siguientes claves se utilizan en todo este estándar:

| Marcado | Descripción |
| :--: | :-- |
| | No requerido |
| o | Recomendado, pero no requerido |
| ✓ | Requerido |

## V2.1 Seguridad de Contraseña

Las contraseñas, llamadas "Secretos memorizados" por NIST 800-63, incluyen contraseñas, PIN, patrones de desbloqueo, elegir el gatito correcto u otro elemento de imagen y frases de contraseña. Generalmente se consideran "algo que sabes", y a menudo se utilizan como autenticadores de un solo factor. Hay desafíos significativos para el uso continuo de la autenticación de un solo factor, incluyendo miles de millones de nombres de usuario y contraseñas válidos divulgados en Internet, contraseñas predeterminadas o débiles, tablas arcoíris y diccionarios ordenados de las contraseñas más comunes.

Las aplicaciones deben incentivar el uso de autenticación multifactor y deben permitir a los usuarios re-usar los tokens que ya poseen, como tokens FIDO o U2F, o vincular a un proveedor de servicios de credenciales que proporcione autenticación multifactor.

Los proveedores de servicios de credenciales (CSPs; Por sus siglas en inglés) proporcionan identidad federada a los usuarios. Los usuarios a menudo tendrán más de una identidad con varios CSP, como una identidad empresarial con Azure AD, Okta, Ping Identity o Google, o la identidad del consumidor mediante Facebook, Twitter, Google o WeChat, por nombrar solo algunas alternativas comunes. Esta lista no es un respaldo de estas empresas o servicios, sino simplemente un estímulo para que los desarrolladores consideren la realidad de que muchos usuarios tienen muchas identidades establecidas. Las organizaciones deben considerar la integración con las identidades de usuario existentes, según el perfil de riesgo de la prueba de identidad del CSP. Por ejemplo, es poco probable que una organización gubernamental acepte una identidad de las redes sociales como un inicio de sesión para sistemas sensibles, ya que es fácil crear identidades falsas o desechadas, mientras que una compañía de juegos móviles bien puede necesitar integrarse con las principales plataformas de medios sociales para hacer crecer su base de jugadores activos.

| # | Descripción | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.1.1** | Verifique que las contraseñas del usuarios tienen al menos 12 caracteres de longitud (después de combinar varios espacios). ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.2** | Verifique que se permitan contraseñas de al menos 64 caracteres y que se denieguen contraseñas de más de 128 caracteres. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.3** | Verifique que no se realiza el truncamiento de contraseña. Sin embargo, varios espacios consecutivos pueden ser reemplazados por un solo espacio. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.4** | Verifique que cualquier carácter Unicode imprimible, incluidos los caracteres neutros del idioma, como espacios y Emojis esté permitido en las contraseñas. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.5** | Verifique que los usuarios pueden cambiar su contraseña. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.6** | Verifique que la funcionalidad de cambio de contraseña requiere la contraseña actual y nueva del usuario. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.7** | Verifique que las contraseñas enviadas durante el registro de la cuenta, el inicio de sesión y el cambio de contraseña se comprueban localmente contra un conjunto de contraseñas filtradas (como las 1,000 o 10,000 contraseñas más comunes que coinciden con la directiva de contraseñas del sistema) o mediante una API externa. Si se utiliza una API, una prueba de zero knowledge u otro mecanismo, asegúrese que la contraseña en texto plano no se envía ni se utiliza para verificar el estado de filtración de la contraseña. Si la contraseña esta filtrada, la aplicación debe exigir al usuario que establezca una nueva contraseña no filtrada. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.8** | Verifique que se proporciona un medidor de fortaleza de la contraseña para ayudar a los usuarios a establecer una contraseña más segura. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.9** | Verifique que no hay reglas de composición de contraseñas que limiten el tipo de caracteres permitidos. No debe haber ningún requisito para mayúsculas o minúsculas o números o caracteres especiales. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.10** | Verifique que no haya rotación periódica de credenciales o solicitud del historial de contraseñas. | ✓ | ✓ | ✓ | 263 | 5.1.1.2 |
| **2.1.11** | Verifique que se permite la funcionalidad "pegar", las aplicaciones auxiliares de contraseñas del browser y los administradores externos de contraseñas. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.12** | Verifique que el usuario puede elegir entre ver temporalmente toda la contraseña enmascarada o ver temporalmente el último caracter escrito de la contraseña en plataformas que no tienen esto como funcionalidad integrada. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |

Nota: El objetivo de permitir que el usuario vea su contraseña o vea el último carácter temporalmente es mejorar la facilidad de uso de la entrada de credenciales, especialmente en torno al uso de contraseñas más largas, frases de contraseña y administradores de contraseñas. Otra razón para incluir el requisito es para limitar o impedir informes de prueba que sugieren innecesariamente que las organizaciones invaliden el comportamiento de campo de contraseña de plataforma integrada para eliminar esta experiencia de seguridad moderna y fácil de usar.

## V2.2 Seguridad General del Autenticador

La agilidad del autenticador es esencial para aplicaciones preparadas para el futuro. Refactorice los verificadores de aplicaciones para permitir autenticadores adicionales según las preferencias del usuario, así como permitir la retirada de autenticadores obsoletos o inseguros de forma ordenada.

NIST considera el email y el SMS como [autenticadores de tipo "restringido"](https://pages.nist.gov/800-63-FAQ/#q-b1), y es probable que sean eliminados del NIST 800-63 y por lo tanto el ASVS en algún momento el futuro. Las aplicaciones deben planificar un roadmap que no requiera el uso de correo electrónico o SMS.

| # | Descripción | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.2.1** | Verifique que los controles anti-automatización son efectivos para mitigar las pruebas de credenciales filtradas, fuerza bruta y ataques de bloqueo de cuentas. Estos controles incluyen el bloqueo de las contraseñas filtradas más comunes, bloqueos suaves, limitación de velocidad, CAPTCHA, retrasos cada vez mayores entre intentos, restricciones de direcciones IP o restricciones basadas en riesgos, como la ubicación, el primer inicio de sesión en un dispositivo, los intentos recientes de desbloquear la cuenta o similares. Verifique que no sea posible realizar más de 100 intentos fallidos por hora en una sola cuenta. | ✓ | ✓ | ✓ | 307 | 5.2.2 / 5.1.1.2 / 5.1.4.2 / 5.1.5.2 |
| **2.2.2** | Verifique que el uso de autenticadores débiles (como SMS y correo electrónico) se limita a la verificación secundaria y la aprobación de transacciones y no como un reemplazo para métodos de autenticación más seguros. Verifique que se ofrezcan métodos más fuertes y no métodos débiles, que los usuarios sean conscientes de los riesgos o que se tomen las medidas adecuadas para limitar los riesgos de compromiso de la cuenta. | ✓ | ✓ | ✓ | 304 | 5.2.10 |
| **2.2.3** | Verifique que las notificaciones seguras se envían a los usuarios después de las actualizaciones de los detalles de autenticación, como restablecimientos de credenciales, cambios de correo electrónico o dirección, inicio de sesión desde ubicaciones desconocidas o de riesgo. Se prefiere el uso de notificaciones push - en lugar de SMS o correo electrónico - , pero en ausencia de notificaciones push, SMS o correo electrónico es aceptable siempre y cuando no se divulgue información confidencial en la notificación. | ✓ | ✓ | ✓ | 620 | |
| **2.2.4** | Verifique la resistencia a la suplantación contra el phishing, como el uso de la autenticación multifactor, los dispositivos criptográficos con intención (como las claves conectadas con un push para autenticarse) o en niveles AAL más altos, certificados del lado cliente. | | | ✓ | 308 | 5.2.5 |
| **2.2.5** | Verifique que donde se separan un proveedor de servicios de credenciales (CSP) y la aplicación que comprueba la autenticación, el TLS mutuamente autenticado está en su lugar entre los dos endpoints. | | | ✓ | 319 | 5.2.6 |
| **2.2.6** | Verifique la resistencia a la reproducción mediante el uso obligatorio de dispositivos de one-time password (OTP), autenticadores criptográficos o códigos de búsqueda. | | | ✓ | 308 | 5.2.8 |
| **2.2.7** | Verifique la intención de autenticarse exigiendo la entrada de un token de OTP o una acción iniciada por el usuario, como una pulsación de botón en un teclado de hardware FIDO. | | | ✓ | 308 | 5.2.9 |

## V2.3 Ciclo de Vida del Autenticador

Los autenticadores son contraseñas, tokens de software, tokens de hardware y dispositivos biométricos. El ciclo de vida de los autenticadores es fundamental para la seguridad de una aplicación: si alguien puede registrar automáticamente una cuenta sin evidencia de identidad, puede haber poca confianza en la aserción de identidad. Para sitios de redes sociales como Reddit, está perfectamente bien. Para los sistemas bancarios, un mayor enfoque en el registro y la emisión de credenciales y dispositivos es fundamental para la seguridad de la aplicación.

Nota: Las contraseñas no deben tener una duración máxima ni estar sujetas a la rotación de contraseñas. Las contraseñas deben comprobarse si han sido filtradas, no pedir que se reemplacen regularmente.

| # | Descripción | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.3.1** | Verifique que las contraseñas iniciales o los códigos de activación generados por el sistema DEBEN ser generados de forma aleatoreamente segura, DEBE tener al menos 6 caracteres de largo y PUEDE contener letras y números, y expirar después de un corto período de tiempo. Estos secretos iniciales no deben permitirse su re-utilización para convertirse en la contraseña a largo plazo. | ✓ | ✓ | ✓ | 330 | 5.1.1.2 / A.3 |
| **2.3.2** | Verifique que se admite la inscripción y el uso de dispositivos de autenticación proporcionados por el suscriptor, como tokens U2F o FIDO. | | ✓ | ✓ | 308 | 6.1.3 |
| **2.3.3** | Verifique que las instrucciones de renovación se envían con tiempo suficiente para renovar los autenticadores con límite de tiempo. | | ✓ | ✓ | 287 | 6.1.4 |

## V2.4 Almacenamiento de Credenciales

Los arquitectos y desarrolladores deben adherirse a esta sección al crear o refactorizar código. Esta sección solo se puede verificar completamente mediante la revisión del código fuente o mediante pruebas de unidad o integración seguras. Las pruebas de penetración no pueden identificar ninguno de estos problemas.

La lista de funciones de derivación aprobadas de one-way key se detalla en la sección 5.1.1.2 del NIST 800-63 B, y en [BSI Kryptographische Verfahren: Empfehlungen und Schlussell&auml;ngen (2018)](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile). El último algoritmo nacional o regional y los estándares de longitud de clave se pueden elegir en lugar de estas opciones.

Esta sección no se puede probar en penetración, por lo que los controles no se marcan como L1. Sin embargo, esta sección es de vital importancia para la seguridad de las credenciales si son robadas, por lo que si bifurca el ASVS para una arquitectura o directriz de codificación o lista de comprobación de revisión de código fuente, coloque estos controles de nuevo en L1 en su versión privada.

| # | Descripción | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.4.1** | Verifique que las contraseñas se almacenan en un forma tal que resisten ataques sin conexión. Las contraseñas DEBERÁN usar hash con salto mediante una derivación de llave de una sola vía aprobada o función de hash de contraseña. Las funciones derivación de llave y hash de contraseñas toman una contraseña, una salto y un factor de costo como entradas al generar un hash de contraseña. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.2** | Verifique que el salto tiene al menos 32 bits de longitud y que se elige arbitrariamente para minimizar las colisiones de valor de salto entre los hashes almacenados. Para cada credencial, se DEBE almacenar un único valor de salto y el hash resultante. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.3** | Verifique que si se utiliza PBKDF2, el recuento de iteraciones DEBE ser tan grande como el rendimiento del servidor de verificación lo permita, normalmente de al menos 100,000 iteraciones. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.4** | Verifique que si se utiliza bcrypt, el factor de trabajo DEBE ser tan grande como lo permita el rendimiento del servidor de verificación, con un mínimo de 10. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.5** | Verifique que se realiza una iteración adicional de una función de derivación de claves, utilizando un valor de salto que es secreto y que solo conoce el verificador. Genere el valor de salto utilizando un generador de bits aleatorios aprobado [SP 800-90Ar1] y proporcione al menos la fuerza de seguridad mínima especificada en la última revisión del SP 800-131A. El valor secreto del salto se almacenará por separado de las contraseñas hash (p. ej., en un dispositivo especializado como un módulo de seguridad de hardware). | | ✓ | ✓ | 916 | 5.1.1.2 |

Cuando se mencionan las normas estadounidenses, se puede utilizar una norma regional o local en lugar de la norma estadounidense o además de la norma estadounidense según sea necesario.

## V2.5 Recuperación de Credenciales

| # | Descripción | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.5.1** | Verifique que un secreto de activación o recuperación inicial generado por el sistema no se envíe en texto claro al usuario. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.2** | Verificar sugerencias de contraseña o autenticación basada en conocimientos (las llamadas "preguntas secretas") no están presentes. | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.3** | Verificar la recuperación de credenciales de contraseña no revela la contraseña actual de ninguna manera. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.4** | Verificar que las cuentas compartidas o predeterminadas no estén presentes (por ejemplo. "root", "admin", o "sa"). | ✓ | ✓ | ✓ | 16 | 5.1.1.2 / A.3 |
| **2.5.5** | Verifique que si se cambia o reemplaza un factor de autenticación, se notifica al usuario de este evento. | ✓ | ✓ | ✓ | 304 | 6.1.2.3 |
| **2.5.6** | Verifique la contraseña olvidada y otras rutas de recuperación utilizan un mecanismo de recuperación seguro, como OTP basado en el tiempo (TOTP) u otro token de software, mobile push u otro mecanismo de recuperación sin conexión. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.7** | Verifique que si se pierden factores de autenticación OTP o multifactor, esa evidencia de prueba de identidad se realiza al mismo nivel que durante la inscripción. | | ✓ | ✓ | 308 | 6.1.2.3 |

## V2.6 Verificador de Secretos de Look-up

Secretos de Look up (secretos de búsqueda) son listas generadas previamente de códigos secretos, similares a los números de autorización de transacción (TAN), los códigos de recuperación de redes sociales o una cuadrícula que contiene un conjunto de valores aleatorios. Estos se distribuyen de forma segura a los usuarios. Estos códigos de búsqueda se utilizan una vez y, una vez que se utilizan todos, se descarta la lista secreta de búsqueda. Este tipo de autenticador se considera "algo que tienes".

| # | Descripción | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.6.1** | Verifique que los secretos de búsqueda solo se pueden usar una vez. | | ✓ | ✓ | 308 | 5.1.2.2 |
| **2.6.2** | Verifique que los secretos de búsqueda tengan suficiente aleatoriedad (112 bits de entropía), o si menos de 112 bits de entropía, saltados con un única y aleatoria salto de 32 bits y hasheado con un hash aprobado de una sola vía. | | ✓ | ✓ | 330 | 5.1.2.2 |
| **2.6.3** | Verifique que los secretos de búsqueda son resistentes a los ataques sin conexión, como los valores predecibles. | | ✓ | ✓ | 310 | 5.1.2.2 |

## V2.7 Verificador Fuera de Banda

En el pasado, un verificador fuera de banda común habría sido un correo electrónico o SMS que contiene un enlace de restablecimiento de contraseña. Los atacantes utilizan este mecanismo débil para restablecer las cuentas que aún no controlan, como tomar el control de la cuenta de correo electrónico de una persona y volver a usar los vínculos de restablecimiento descubiertos. Hay mejores maneras de manejar la verificación fuera de banda.

Los autenticadores seguros fuera de banda son dispositivos físicos que pueden comunicarse con el verificador a través de un canal secundario seguro. Algunos ejemplos son las notificaciones push a dispositivos móviles. Este tipo de autenticador se considera "algo que tienes". Cuando un usuario desea autenticarse, la aplicación de verificación envía un mensaje al autenticador fuera de banda a través de una conexión al autenticador directa o indirectamente a través de un servicio de terceros. El mensaje contiene un código de autenticación (normalmente un número aleatorio de seis dígitos o un cuadro de diálogo de aprobación modal). La aplicación de comprobación espera a recibir el código de autenticación a través del canal principal y compara el hash del valor recibido con el hash del código de autenticación original. Si coinciden, el verificador fuera de banda puede suponer que el usuario se ha autenticado.

ASVS asume que sólo unos pocos desarrolladores desarrollarán nuevos autenticadores fuera de banda, como notificaciones push, y por lo tanto los siguientes controles ASVS se aplican a los verificadores, como la API de autenticación, las aplicaciones y las implementaciones de inicio de sesión único. Si está desarrollando un nuevo autenticador fuera de banda, por favor refiérase a NIST 800-63B &sect; 5.1.3.1.

No se permiten autenticadores inseguros fuera de banda, como el correo electrónico y VoIP. La autenticación RTC y SMS está actualmente "restringida" por NIST y debe estar en desuso en favor de las notificaciones push o similares. Si necesita utilizar la autenticación telefónica o sms fuera de banda, por favor consulte &sect; 5.1.3.3.

| # | Descripción | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.7.1** | Verifique que los autenticadores de texto sin cifrar fuera de banda tales como PSTN o SMS ("restringido por NIST") no se ofrecen de forma predeterminada, y que en primer lugar se ofrecen alternativas más sólidas, como las notificaciones push. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.2** | Verifique que el verificador fuera de banda expira después de 10 minutos, fuera de las solicitudes de autenticación de banda, códigos o tokens. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.3** | Verifique que las solicitudes de autenticación, los códigos o los tokens de verificador fuera de banda solo se pueden usar una vez y solo para la solicitud de autenticación original. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.4** | Verifique que el autenticador y el verificador fuera de banda se comuniquen a través de un canal independiente seguro. | ✓ | ✓ | ✓ | 523 | 5.1.3.2 |
| **2.7.5** | Verifique que el verificador fuera de banda conserva solo una versión hasheada del código de autenticación. | | ✓ | ✓ | 256 | 5.1.3.2 |
| **2.7.6** | Verifique que el código de autenticación inicial sea generado por un generador de números aleatorios seguro, que contiene al menos 20 bits de entropía (normalmente un número aleatorio digital de seis es suficiente). | | ✓ | ✓ | 310 | 5.1.3.2 |

## V2.8 Verificador de Una Sola Vez

Las contraseñas de una sola vez de un solo factor (OTPs) son tokens físicos o flexibles que muestran un desafío pseudoaleatorio que cambia continuamente. Estos dispositivos hacen que el phishing (suplantación) sea difícil, pero no imposible. Este tipo de autenticador se considera "algo que tienes". Los tokens multifactor son similares a los OTP de un solo factor, pero requieren un código PIN válido, desbloqueo biométrico, inserción USB o emparejamiento NFC o algún valor adicional (como calculadoras de firma de transacciones) que se introduzcan para crear el OTP final.

| # | Descripción | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.8.1** | Verifique que los OTP basados en el tiempo tienen una duración definida antes de expirar. | ✓ | ✓ | ✓ | 613 | 5.1.4.2 / 5.1.5.2 |
| **2.8.2** | Verifique que las claves simétricas utilizadas para comprobar los OTP enviados están altamente protegidas, por ejemplo, mediante el uso de un módulo de seguridad de hardware o almacenamiento seguro de claves basadas en el sistema operativo. | | ✓ | ✓ | 320 | 5.1.4.2 / 5.1.5.2|
| **2.8.3** | Verifique que los algoritmos criptográficos aprobados se utilizan en la generación, siembra y verificación de OTP. | | ✓ | ✓ | 326 | 5.1.4.2 / 5.1.5.2 |
| **2.8.4** | Verifique que el OTP basado en el tiempo se pueda utilizar solamente una vez dentro del período de validez. | | ✓ | ✓ | 287 | 5.1.4.2 / 5.1.5.2 |
| **2.8.5** | Verifique que si se reutiliza un token OTP multifactor basado en el tiempo durante el período de validez, se registra en logs y se rechaza con notificación segura enviada al titular del dispositivo. | | ✓ | ✓ | 287 | 5.1.5.2 |
| **2.8.6** | Verifique que el generador OTP de un solo factor físico pueda ser revocado en caso de robo u otra pérdida. Asegúrese de que la revocación es efectiva inmediatamente en todas las sesiones iniciadas, independientemente de la ubicación. | | ✓ | ✓ | 613 | 5.2.1 |
| **2.8.7** | Verifique que los autenticadores biométricos se limitan a usarlos solo como factores secundarios junto con algo que Ud. tiene y algo que Ud. sabe. | | o | ✓ | 308 | 5.2.3 |

## V2.9 Verificador Criptográfico

Las claves de seguridad criptográficas son tarjetas inteligentes o claves FIDO, donde el usuario tiene que conectar o emparejar el dispositivo criptográfico al equipo para completar la autenticación. Los verificadores envían un mensaje de desafío a los dispositivos o software criptográficos, y el dispositivo o software calcula una respuesta basada en una clave criptográfica almacenada de forma segura.

Los requisitos para los dispositivos y software criptográficos de un solo factor, y los dispositivos y software criptográficos multifactor son los mismos, ya que la verificación del autenticador criptográfico demuestra la posesión del factor de autenticación.

| # | Descripción | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.9.1** | Verifique que las claves criptográficas utilizadas en la verificación se almacenan de forma segura y protegidas contra la divulgación, como el uso de un módulo de plataforma segura (TPM) o un módulo de seguridad de hardware (HSM) o un servicio de sistema operativo que puede utilizar este almacenamiento seguro. | | ✓ | ✓ | 320 | 5.1.7.2 |
| **2.9.2** | Verifique que el mensaje de desafío tenga al menos 64 bits de longitud y sea estadísticamente único o sea único a lo largo de la vida útil del dispositivo criptográfico. | | ✓ | ✓ | 330 | 5.1.7.2 |
| **2.9.3** | Verifique que se utilizan algoritmos criptográficos aprobados en la generación, la semilla y la verificación. | | ✓ | ✓ | 327 | 5.1.7.2 |

## V2.10 Autenticación de Servicio

Esta categoría no es comprobable con test de penetración, por lo que no tiene ningún requisito L1. Sin embargo, si se utiliza en una arquitectura, codificación o revisión de código segura, suponga que el software (al igual que Java Key Store) es el requisito mínimo en L1. El almacenamiento de texto claro de los secretos no es aceptable bajo ninguna circunstancia.

| # | Descripción | L1 | L2 | L3 | CWE | [NIST &sect;](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.10.1** | Verifique que los secretos dentro del servicio no se basan en credenciales invariables, como contraseñas, claves de API o cuentas compartidas con acceso con privilegios. | | OS assisted | HSM | 287 | 5.1.1.1 |
| **2.10.2** | Verifique que si las contraseñas son necesarias para la autenticación de servicio, la cuenta de servicio utilizada no es una credencial predeterminada. (p. ej., root/root o admin/admin son predeterminados en algunos servicios durante la instalación). | | OS assisted | HSM | 255 | 5.1.1.1 |
| **2.10.3** | Verifique que las contraseñas se almacenan con suficiente protección para evitar ataques de recuperación sin conexión, incluido el acceso al sistema local. | | OS assisted | HSM | 522 | 5.1.1.1 |
| **2.10.4** | Verifique que las contraseñas, las integraciones con bases de datos y sistemas de terceros, las semillas y los secretos internos y las claves de API se administran de forma segura y no se incluyen en el código fuente ni se almacenan en los repositorios de código fuente. Dicho almacenamiento DEBE resistir ataques fuera de línea. Se recomienda el uso de un almacén de claves de software seguro (L1), TPM de hardware o un HSM (L3) para el almacenamiento de contraseñas. | | OS assisted | HSM | 798 | |

## Requisitos Adicionales de Agencias de EE.UU.

Las agencias de EEUU tienen requisitos obligatorios relativos al NIST 800-63. ASVS siempre ha sido casi el 80% de los controles que se aplican a casi el 100% de las aplicaciones, y no el último 20% de los controles avanzados o aquellos que tienen una aplicabilidad limitada. Como tal, el ASVS es un subconjunto estricto de NIST 800-63, especialmente para las clasificaciones IAL1/2 y AAL1/2, pero no es lo suficientemente completo, especialmente en lo que respecta a las clasificaciones IAL3/AAL3.

Instamos encarecidamente a las agencias de EEUU a que revisen e implementen NIST 800-63 en su totalidad.

## Glosario de términos

| Termino | Significado |
| -- | -- |
| CSP | Proveedor de servicios de credenciales también llamado proveedor de identidades |
| Authenticator | Código que autentica una contraseña, un token, MFA, una aserción federada, etc. |
| Verifier | "Una entidad que verifica la identidad del reclamante verificando la posesión y el control del reclamante de uno o dos autenticadores mediante un protocolo de autenticación. Para ello, es posible que el verificador también necesite validar las credenciales que vinculan el autenticador con el identificador del suscriptor y comprobar su estado" |
| OTP | Contraseña de una sola vez |
| SFA | Autenticadores de un solo factor, como algo que conoces (secretos memorizados, contraseñas, frases de contraseña, PIN), algo que eres (biometría, huellas dactilares, escaneos faciales) o algo que tienes (tokens OTP, un dispositivo criptográfico como una tarjeta inteligente) |
| MFA | Autenticación multifactor, que incluye dos o más factores individuales |

## Referencias

Para obtener más información, véase también:

* [NIST 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST 800-63 A - Enrollment and Identity Proofing](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST 800-63 B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST 800-63 C - Federation and Assertions](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [OWASP Cheat Sheet - Password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Forgot password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Cheat Sheet - Choosing and using security questions](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
