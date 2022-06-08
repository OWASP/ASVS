# V9 Comunicación

## Objetivo de Control

Asegúrese de que una aplicación verificada cumpla con los siguientes requisitos de alto nivel:

* Requiere TLS o cifrado fuerte, independientemente de la sensibilidad del contenido.
* Siga la guía más reciente, que incluye:
  * Consejos de configuración
  * Algoritmos y cifrados preferidos
* Evite los algoritmos y cifrados débiles o que pronto quedarán obsoletos, excepto como último recurso
* Deshabilite los algoritmos en desuso, o que se sabe son de cifrado inseguro.

Dentro de estos requisitos:

* Manténgase actualizado con los consejos recomendados por la industria sobre la configuración segura de TLS, ya que cambia con frecuencia (a menudo debido a fallas catastróficas en los algoritmos y cifrados existentes).
* Utilice las versiones más recientes de las herramientas de revisión de la configuración de TLS para configurar el orden preferido y la selección de algoritmos.
* Verifique su configuración periódicamente para asegurarse de que la comunicación segura esté siempre presente y sea efectiva.

## V9.1 Seguridad de la Comunicación del Cliente

Asegúrese de que todos los mensajes de los clientes se envíen a través de redes cifradas, utilizando TLS 1.2 o posterior.
Utilice herramientas actualizadas para revisar la configuración del cliente de forma regular.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.1.1** | Verifique que TLS se utilice para toda la conectividad del cliente y que no recurra a comunicaciones inseguras o no cifradas. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | Verifique con herramientas de prueba TLS actualizadas que solo estén habilitados los conjuntos de cifrado fuertes, con los conjuntos de cifrado más fuertes configurados como preferidos. | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | Verifique que solo estén habilitadas las últimas versiones recomendadas del protocolo TLS, como TLS 1.2 y TLS 1.3. La última versión del protocolo TLS debería ser la opción preferida. | ✓ | ✓ | ✓ | 326 |

## V9.2 Seguridad de la Comunicación del Servidor

Las comunicaciones de servidor son algo más que HTTP. Las conexiones seguras hacia y desde otros sistemas, como sistemas de supervisión, herramientas de administración, acceso remoto y ssh, middleware, bases de datos, mainframes, sistemas de origen externo o de socios, deben estar en su lugar. Todos estos deben ser cifrados para evitar "dureza exterior, trivialmente fácil de interceptar en el interior".

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.2.1** | Verifique que las conexiones hacia y desde el servidor utilizan certificados TLS de confianza. Cuando se utilizan certificados generados internamente o autofirmados, el servidor debe configurarse para que solo confíe en las CA internas específicas y en los certificados autofirmados específicos. Todos los demás deben ser rechazados. | | ✓ | ✓ | 295 |
| **9.2.2** | Verifique que las comunicaciones cifradas, como TLS, se utilizan para todas las conexiones entrantes y salientes, incluidos los puertos de administración, monitoreo, la autenticación, la API o las llamadas a servicios web, la base de datos, la nube, el serverless, el mainframe, ya sean externos o de conexiones de asociados. El servidor no debe volver a protocolos inseguros o no cifrados. | | ✓ | ✓ | 319 |
| **9.2.3** | Verifique que se autentican todas las conexiones cifradas a sistemas externos que implican información o funciones confidenciales. | | ✓ | ✓ | 287 |
| **9.2.4** | Verifique que la adecuada revocación de certificación, como la comprobación de Online Certificate Status Protocol (OCSP), esté habilitada y configurada. | | ✓ | ✓ | 299 |
| **9.2.5** | Verifique que se hace logging de errores de conexión TLS de back-end. | | | ✓ | 544 |

## Referencias

Para obtener más información, véase también:

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* [OWASP - Pinning Guide](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)
* Notas sobre "Modos aprobados de TLS":
    * En el pasado, la ASVS se refería al estándar estadounidense FIPS 140-2, pero como estándar global, aplicar los estándares estadounidenses puede ser difícil, contradictorio o confuso de aplicar.
    * Un mejor método para lograr el cumplimiento de la sección 9.1 sería revisar guías como [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) o [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), y utilice herramientas de evaluación de TLS conocidas y actualizadas para obtener el nivel de seguridad deseado.
