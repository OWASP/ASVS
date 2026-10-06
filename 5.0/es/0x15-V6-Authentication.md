# V6 Autenticación

## Objetivo del Control

La autenticación es el proceso de establecer o confirmar la autenticidad de una persona o dispositivo. Implica verificar las afirmaciones realizadas por una persona o sobre un dispositivo, garantizar la resistencia a la suplantación de identidad y evitar la recuperación o interceptación de contraseñas.

[NIST SP 800-63](https://pages.nist.gov/800-63-3/) es un estándar moderno basado en evidencia que resulta valioso para organizaciones de todo el mundo, pero es especialmente relevante para los organismos de Estados Unidos y quienes interactúan con ellos.

Aunque muchos de los requerimientos de este capítulo se basan en la segunda sección del estándar (conocida como NIST SP 800-63B, "Directrices de identidad digital - Autenticación y gestión del ciclo de vida"), el capítulo se centra en amenazas comunes y debilidades de autenticación que se explotan con frecuencia. No pretende abarcar exhaustivamente todos los puntos del estándar. Cuando sea necesario cumplir íntegramente con NIST SP 800-63, consulte NIST SP 800-63.

Además, la terminología de NIST SP 800-63 puede diferir en ocasiones, y este capítulo utiliza con frecuencia términos más ampliamente conocidos para mejorar la claridad.

Una característica habitual de las aplicaciones más avanzadas es la capacidad de adaptar las etapas de autenticación requeridas según diversos factores de riesgo. Esta característica se aborda en el capítulo "Autorización", ya que estos mecanismos también deben tenerse en cuenta al tomar decisiones de autorización.

## V6.1 Documentación de Autenticación

Esta sección contiene requerimientos que detallan la documentación de autenticación que debería mantenerse para una aplicación. Esto es fundamental para implementar y evaluar cómo deberían configurarse los controles de autenticación pertinentes.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **6.1.1** | Verificar que la documentación de la aplicación defina cómo se utilizan controles como la limitación de tasa, la prevención de la automatización y la respuesta adaptativa para defenderse de ataques como el relleno de credenciales (credential stuffing) y la fuerza bruta de contraseñas. La documentación debe dejar claro cómo se configuran estos controles y cómo evitan el bloqueo malicioso de cuentas. | 1 |
| **6.1.2** | Verificar que se documente una lista de palabras específicas del contexto para impedir su uso en las contraseñas. La lista podría incluir permutaciones de nombres de organizaciones, nombres de productos, identificadores de sistemas, nombres en clave de proyectos, nombres de departamentos o roles y otros similares. | 2 |
| **6.1.3** | Verificar que, si la aplicación incluye múltiples vías de autenticación, todas estén documentadas junto con los controles de seguridad y la robustez de autenticación que deben aplicarse de manera uniforme en todas ellas. | 2 |

## V6.2 Seguridad de las Contraseñas

Las contraseñas, denominadas "secretos memorizados" por NIST SP 800-63, incluyen contraseñas, frases de contraseña, PINs, patrones de desbloqueo y la selección del gatito correcto u otro elemento de una imagen. Generalmente se consideran "algo que sabe" y suelen utilizarse como mecanismo de autenticación de un solo factor.

Por ello, esta sección contiene requerimientos para garantizar que las contraseñas se creen y gestionen de forma segura. La mayoría de los requerimientos son de nivel 1 (L1), ya que son más importantes en ese nivel. A partir del nivel 2 (L2), se requieren mecanismos de autenticación multifactor, en los que las contraseñas pueden ser uno de los factores.

Los requerimientos de esta sección se relacionan principalmente con la [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) de las [directrices de NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **6.2.1** | Verificar que las contraseñas establecidas por los usuarios tengan al menos 8 caracteres, aunque se recomienda encarecidamente un mínimo de 15 caracteres. | 1 |
| **6.2.2** | Verificar que los usuarios puedan cambiar su contraseña. | 1 |
| **6.2.3** | Verificar que la funcionalidad de cambio de contraseña requiera la contraseña actual y la nueva contraseña del usuario. | 1 |
| **6.2.4** | Verificar que las contraseñas enviadas durante el registro de una cuenta o el cambio de contraseña se comparen con un conjunto disponible de, al menos, las 3000 contraseñas más comunes que cumplan la política de contraseñas de la aplicación, por ejemplo, la longitud mínima. | 1 |
| **6.2.5** | Verificar que puedan utilizarse contraseñas de cualquier composición, sin reglas que limiten el tipo de caracteres permitidos. No debe exigirse un número mínimo de letras mayúsculas o minúsculas, números o caracteres especiales. | 1 |
| **6.2.6** | Verificar que los campos de entrada de contraseñas utilicen type=password para enmascarar lo que se introduce. Las aplicaciones pueden permitir que el usuario vea temporalmente toda la contraseña enmascarada o el último carácter introducido de la contraseña. | 1 |
| **6.2.7** | Verificar que se permitan la funcionalidad de "pegar", los asistentes de contraseñas del navegador y los gestores de contraseñas externos. | 1 |
| **6.2.8** | Verificar que la aplicación compruebe la contraseña del usuario exactamente como la recibe, sin modificaciones como truncamientos o conversiones entre mayúsculas y minúsculas. | 1 |
| **6.2.9** | Verificar que se permitan contraseñas de al menos 64 caracteres. | 2 |
| **6.2.10** | Verificar que la contraseña de un usuario siga siendo válida hasta que se descubra que ha sido comprometida o que el usuario la cambie. La aplicación no debe exigir la rotación periódica de credenciales. | 2 |
| **6.2.11** | Verificar que se utilice la lista documentada de palabras específicas del contexto para impedir la creación de contraseñas fáciles de adivinar. | 2 |
| **6.2.12** | Verificar que las contraseñas enviadas durante el registro de una cuenta o los cambios de contraseña se comparen con un conjunto de contraseñas filtradas. | 2 |

## V6.3 Seguridad General de la Autenticación

Esta sección contiene requerimientos generales para la seguridad de los mecanismos de autenticación y establece las distintas expectativas para cada nivel. Las aplicaciones de nivel 2 (L2) deben exigir el uso de autenticación multifactor (MFA). Las aplicaciones de nivel 3 (L3) deben utilizar autenticación basada en hardware, realizada en un entorno de ejecución confiable (TEE) con atestación. Esto podría incluir claves de acceso (passkeys) vinculadas al dispositivo, autenticadores que cumplan el nivel de garantía (LoA) alto de eIDAS, autenticadores con nivel 3 de garantía del autenticador de NIST (AAL3) o un mecanismo equivalente.

Aunque esta postura respecto a la MFA es relativamente exigente, es fundamental elevar el nivel de protección de los usuarios. Cualquier intento de flexibilizar estos requerimientos debería ir acompañado de un plan claro sobre cómo se mitigarán los riesgos relacionados con la autenticación, teniendo en cuenta las directrices y la investigación de NIST sobre el tema.

Tenga en cuenta que, en el momento de la publicación, NIST SP 800-63 considera el correo electrónico [no aceptable](https://pages.nist.gov/800-63-FAQ/#q-b11) como mecanismo de autenticación ([copia archivada](https://web.archive.org/web/20250330115328/https://pages.nist.gov/800-63-FAQ/#q-b11)).

Los requerimientos de esta sección se relacionan con varias secciones de las [directrices de NIST](https://pages.nist.gov/800-63-3/sp800-63b.html), entre ellas: [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling) y [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding).

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **6.3.1** | Verificar que los controles para prevenir ataques como el relleno de credenciales (credential stuffing) y la fuerza bruta de contraseñas se implementen de acuerdo con la documentación de seguridad de la aplicación. | 1 |
| **6.3.2** | Verificar que las cuentas de usuario predeterminadas (por ejemplo, "root", "admin" o "sa") no estén presentes en la aplicación o estén deshabilitadas. | 1 |
| **6.3.3** | Verificar que, para acceder a la aplicación, sea obligatorio utilizar un mecanismo de autenticación multifactor o una combinación de mecanismos de autenticación de un solo factor. Para el nivel 3 (L3), uno de los factores debe ser un mecanismo de autenticación basado en hardware que ofrezca resistencia al compromiso y a la suplantación de identidad frente a ataques de phishing, y que verifique la intención de autenticarse al exigir una acción iniciada por el usuario (como pulsar un botón en una llave de hardware FIDO o en un teléfono móvil). Flexibilizar cualquiera de las consideraciones de este requerimiento exige una justificación completamente documentada y un conjunto integral de controles de mitigación. | 2 |
| **6.3.4** | Verificar que, si la aplicación incluye múltiples vías de autenticación, no existan vías sin documentar y que los controles de seguridad y la robustez de autenticación se apliquen de manera uniforme. | 2 |
| **6.3.5** | Verificar que se notifique a los usuarios sobre los intentos de autenticación sospechosos (exitosos o fallidos). Esto puede incluir intentos de autenticación desde una ubicación o un cliente inusuales, autenticaciones parcialmente exitosas (solo uno de varios factores), un intento de autenticación tras un largo período de inactividad o una autenticación exitosa después de varios intentos fallidos. | 3 |
| **6.3.6** | Verificar que el correo electrónico no se utilice como mecanismo de autenticación de un solo factor ni multifactor. | 3 |
| **6.3.7** | Verificar que se notifique a los usuarios después de actualizar los datos de autenticación, por ejemplo, tras restablecer las credenciales o modificar el nombre de usuario o la dirección de correo electrónico. | 3 |
| **6.3.8** | Verificar que no se pueda deducir qué usuarios son válidos a partir de desafíos de autenticación fallidos, por ejemplo, basándose en mensajes de error, códigos de respuesta HTTP o diferencias en los tiempos de respuesta. Las funcionalidades de registro y recuperación de contraseñas olvidadas también deben contar con esta protección. | 3 |

## V6.4 Ciclo de Vida y Recuperación de los Factores de Autenticación

Los factores de autenticación pueden incluir contraseñas, tokens de software, tokens de hardware y dispositivos biométricos. Gestionar de forma segura el ciclo de vida de estos mecanismos es fundamental para la seguridad de una aplicación, y esta sección incluye requerimientos al respecto.

Los requerimientos de esta sección se relacionan principalmente con la [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) o la [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) de las [directrices de NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **6.4.1** | Verificar que las contraseñas iniciales o los códigos de activación generados por el sistema se generen de forma aleatoria y segura, cumplan la política de contraseñas existente y caduquen tras un período breve o después de su primer uso. No debe permitirse que estos secretos iniciales se conviertan en la contraseña a largo plazo. | 1 |
| **6.4.2** | Verificar que no existan pistas de contraseñas ni autenticación basada en conocimiento (las denominadas "preguntas secretas"). | 1 |
| **6.4.3** | Verificar que se implemente un proceso seguro para restablecer una contraseña olvidada que no eluda ningún mecanismo de autenticación multifactor habilitado. | 2 |
| **6.4.4** | Verificar que, si se pierde un factor de autenticación multifactor, se compruebe la identidad mediante evidencias con el mismo nivel de exigencia que durante la inscripción. | 2 |
| **6.4.5** | Verificar que las instrucciones de renovación de los mecanismos de autenticación que caducan se envíen con tiempo suficiente para llevarlas a cabo antes de que caduque el mecanismo anterior, configurando recordatorios automáticos si es necesario. | 3 |
| **6.4.6** | Verificar que los usuarios administradores puedan iniciar el proceso de restablecimiento de contraseña para el usuario, pero que esto no les permita cambiar ni elegir su contraseña. Esto evita que puedan conocer la contraseña del usuario. | 3 |

## V6.5 Requerimientos Generales de Autenticación Multifactor

Esta sección ofrece directrices generales que serán pertinentes para diversos métodos de autenticación multifactor.

Los mecanismos incluyen:

* Secretos de consulta
* Contraseñas de un solo uso basadas en el tiempo (TOTPs)
* Mecanismos fuera de banda

Los secretos de consulta son listas pregeneradas de códigos secretos, similares a los números de autorización de transacciones (TAN), los códigos de recuperación de redes sociales o una cuadrícula que contiene un conjunto de valores aleatorios. Este tipo de mecanismo de autenticación se considera "algo que tiene", ya que los códigos están diseñados para no ser memorizables y, por lo tanto, deben almacenarse en algún lugar.

Las contraseñas de un solo uso basadas en el tiempo (TOTPs) son tokens físicos o de software que muestran un desafío seudoaleatorio de un solo uso que cambia continuamente. Este tipo de mecanismo de autenticación se considera "algo que tiene". Las TOTPs multifactor son similares a las TOTPs de un solo factor, pero requieren introducir un código PIN válido, realizar un desbloqueo biométrico, insertar un dispositivo USB o emparejar mediante NFC, o introducir algún valor adicional (como en las calculadoras de firma de transacciones) para crear la contraseña de un solo uso (OTP) final.

En la siguiente sección se proporcionan detalles sobre los mecanismos fuera de banda.

Los requerimientos de estas secciones se relacionan principalmente con la [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), la [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), la [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), la [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), la [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators) y la [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) de las [directrices de NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **6.5.1** | Verificar que los secretos de consulta, las solicitudes o los códigos de autenticación fuera de banda y las contraseñas de un solo uso basadas en el tiempo (TOTPs) solo puedan utilizarse con éxito una vez. | 2 |
| **6.5.2** | Verificar que, al almacenarse en el backend de la aplicación, se aplique a los secretos de consulta con menos de 112 bits de entropía (19 caracteres alfanuméricos aleatorios o 34 dígitos aleatorios) un algoritmo de hash aprobado para el almacenamiento de contraseñas que incorpore una sal aleatoria de 32 bits. Puede utilizarse una función de hash estándar si el secreto tiene 112 bits de entropía o más. | 2 |
| **6.5.3** | Verificar que los secretos de consulta, los códigos de autenticación fuera de banda y las semillas de las contraseñas de un solo uso basadas en el tiempo se generen mediante un generador de números seudoaleatorios criptográficamente seguro (CSPRNG) para evitar valores predecibles. | 2 |
| **6.5.4** | Verificar que los secretos de consulta y los códigos de autenticación fuera de banda tengan un mínimo de 20 bits de entropía (normalmente bastan 4 caracteres alfanuméricos aleatorios o 6 dígitos aleatorios). | 2 |
| **6.5.5** | Verificar que las solicitudes, los códigos o los tokens de autenticación fuera de banda, así como las contraseñas de un solo uso basadas en el tiempo (TOTPs), tengan una duración de validez definida. Las solicitudes fuera de banda deben tener una duración máxima de validez de 10 minutos y las TOTP, de 30 segundos. | 2 |
| **6.5.6** | Verificar que cualquier factor de autenticación (incluidos los dispositivos físicos) pueda revocarse en caso de robo u otra pérdida. | 3 |
| **6.5.7** | Verificar que los mecanismos de autenticación biométrica solo se utilicen como factores secundarios junto con algo que tiene o algo que sabe. | 3 |
| **6.5.8** | Verificar que las contraseñas de un solo uso basadas en el tiempo (TOTPs) se comprueben utilizando una fuente de tiempo de un servicio confiable y no una hora no confiable o proporcionada por el cliente. | 3 |

## V6.6 Mecanismos de Autenticación fuera de Banda

Esto suele implicar que el servidor de autenticación se comunique con un dispositivo físico a través de un canal secundario seguro. Por ejemplo, mediante el envío de notificaciones push a dispositivos móviles. Este tipo de mecanismo de autenticación se considera "algo que tiene".

No se permiten mecanismos de autenticación fuera de banda inseguros, como el correo electrónico y VOIP. NIST considera actualmente la autenticación mediante PSTN y SMS como [mecanismos de autenticación "restringidos"](https://pages.nist.gov/800-63-FAQ/#q-b01), y deberían dejar de utilizarse en favor de contraseñas de un solo uso basadas en el tiempo (TOTPs), un mecanismo criptográfico u otro similar. La [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network) de NIST SP 800-63B recomienda abordar los riesgos de sustitución del dispositivo, cambio de SIM, portabilidad del número u otros comportamientos anómalos si es absolutamente necesario admitir la autenticación fuera de banda por teléfono o SMS. Aunque esta sección de ASVS no lo establece como requerimiento obligatorio, no tomar estas precauciones en una aplicación sensible de nivel 2 (L2) o en una aplicación de nivel 3 (L3) debería considerarse una señal de alerta importante.

Tenga en cuenta que NIST también ha publicado recientemente directrices que [desaconsejan el uso de notificaciones push](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/#fig-3). Aunque esta sección de ASVS no lo hace, es importante conocer los riesgos del "bombardeo de notificaciones push" (push bombing).

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **6.6.1** | Verificar que los mecanismos de autenticación que utilizan la red telefónica pública conmutada (PSTN) para entregar contraseñas de un solo uso (OTPs) por teléfono o SMS solo se ofrezcan cuando el número de teléfono se haya validado previamente, también se ofrezcan métodos alternativos más robustos (como las contraseñas de un solo uso basadas en el tiempo) y el servicio informe a los usuarios sobre sus riesgos de seguridad. En las aplicaciones de nivel 3 (L3), el teléfono y los SMS no deben estar disponibles como opciones. | 2 |
| **6.6.2** | Verificar que las solicitudes, los códigos o los tokens de autenticación fuera de banda estén vinculados a la solicitud de autenticación original para la que se generaron y no puedan utilizarse para una anterior o posterior. | 2 |
| **6.6.3** | Verificar que los mecanismos de autenticación fuera de banda basados en códigos estén protegidos contra ataques de fuerza bruta mediante la limitación de tasa. Considerar también el uso de un código con al menos 64 bits de entropía. | 2 |
| **6.6.4** | Verificar que, cuando se utilicen notificaciones push para la autenticación multifactor, se aplique limitación de tasa para prevenir ataques de bombardeo de notificaciones push (push bombing). La coincidencia de números también puede mitigar este riesgo. | 3 |

## V6.7 Mecanismo de Autenticación Criptográfica

Los mecanismos de autenticación criptográfica incluyen tarjetas inteligentes o llaves FIDO, en los que el usuario debe conectar o emparejar el dispositivo criptográfico con el equipo para completar la autenticación. El servidor de autenticación enviará un nonce de desafío al dispositivo o software criptográfico, que calculará una respuesta basada en una clave criptográfica almacenada de forma segura. Los requerimientos de esta sección proporcionan directrices específicas para la implementación de estos mecanismos, mientras que las directrices sobre algoritmos criptográficos se abordan en el capítulo "Criptografía".

Cuando se utilicen claves compartidas o secretas para la autenticación criptográfica, estas deberían almacenarse utilizando los mismos mecanismos que los demás secretos del sistema, tal como se documenta en la sección "Gestión de secretos" del capítulo "Configuración".

Los requerimientos de esta sección se relacionan principalmente con la [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) de las [directrices de NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **6.7.1** | Verificar que los certificados utilizados para verificar las aserciones de autenticación criptográfica se almacenen de manera que queden protegidos contra modificaciones. | 3 |
| **6.7.2** | Verificar que el nonce de desafío tenga una longitud de al menos 64 bits y sea estadísticamente único o único durante toda la vida útil del dispositivo criptográfico. | 3 |

## V6.8 Autenticación con un Proveedor de Identidad

Los proveedores de identidad (IdPs) proporcionan identidad federada a los usuarios. A menudo, los usuarios tienen más de una identidad con varios IdPs, como una identidad empresarial mediante Azure AD, Okta, Ping Identity o Google, o una identidad de consumidor mediante Facebook, Twitter, Google o WeChat, por mencionar solo algunas alternativas comunes. Esta lista no constituye un respaldo a estas empresas o servicios, sino una invitación a que los desarrolladores tengan en cuenta que muchos usuarios ya disponen de varias identidades establecidas. Las organizaciones deberían considerar la integración con las identidades existentes de los usuarios según el perfil de riesgo asociado a la robustez de la comprobación de identidad del IdP. Por ejemplo, es poco probable que un organismo gubernamental acepte una identidad de redes sociales para iniciar sesión en sistemas sensibles, ya que es fácil crear identidades falsas o desechables, mientras que una empresa de juegos móviles puede necesitar integrarse con las principales plataformas de redes sociales para aumentar su base de jugadores activos.

El uso seguro de proveedores de identidad externos requiere una configuración y una verificación cuidadosas para evitar la suplantación de identidad o la falsificación de aserciones. Esta sección proporciona requerimientos para abordar estos riesgos.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **6.8.1** | Verificar que, si la aplicación admite múltiples proveedores de identidad (IdPs), no se pueda suplantar la identidad del usuario mediante otro proveedor de identidad admitido (por ejemplo, utilizando el mismo identificador de usuario). La mitigación habitual sería que la aplicación registre e identifique al usuario mediante una combinación del ID del IdP (que actúa como espacio de nombres) y el ID del usuario en el IdP. | 2 |
| **6.8.2** | Verificar que siempre se validen la presencia y la integridad de las firmas digitales de las aserciones de autenticación (por ejemplo, en JWTs o aserciones SAML), y que se rechace cualquier aserción sin firma o con una firma no válida. | 2 |
| **6.8.3** | Verificar que las aserciones SAML se procesen y utilicen una sola vez dentro de su período de validez para prevenir ataques de repetición. | 2 |
| **6.8.4** | Verificar que, si una aplicación utiliza un proveedor de identidad (IdP) independiente y exige una robustez, unos métodos o una antigüedad de autenticación específicos para determinadas funciones, la aplicación lo verifique mediante la información devuelta por el IdP. Por ejemplo, si se utiliza OIDC, esto podría lograrse validando declaraciones del token de ID (ID Token) como 'acr', 'amr' y 'auth_time' (si están presentes). Si el IdP no proporciona esta información, la aplicación debe contar con un procedimiento alternativo documentado que asuma que se utilizó el mecanismo de autenticación de menor robustez (por ejemplo, autenticación de un solo factor con nombre de usuario y contraseña). | 2 |

## Referencias

Para obtener más información, consulte también:

* [NIST SP 800-63 - Directrices de identidad digital](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST SP 800-63B - Autenticación y gestión del ciclo de vida](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [Preguntas frecuentes de NIST SP 800-63](https://pages.nist.gov/800-63-FAQ/)
* [Guía de pruebas de seguridad web de OWASP: Pruebas de autenticación](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/04-Authentication_Testing)
* [Hoja de referencia de OWASP sobre almacenamiento de contraseñas](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [Hoja de referencia de OWASP sobre contraseñas olvidadas](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [Hoja de referencia de OWASP sobre selección y uso de preguntas de seguridad](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
* [Directrices de CISA sobre la "coincidencia de números"](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
* [Información sobre la Alianza FIDO](https://fidoalliance.org/)
