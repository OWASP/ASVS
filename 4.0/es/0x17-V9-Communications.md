# V9 : Requisitos de verificación de comunicaciones

## Objetivo de Control

Asegúrese de que una aplicación verificada cumple los siguientes requisitos de alto nivel:

 - Se usa siempre TLS o cifrado fuerte, independientemente de la sensibilidad de los datos que se transmiten 
 - Se usa la principal recomendación de configuración, más reciente, para habilitar y ordenar los algoritmos de cifrado preferidos.
 - Los algoritmos de cifrado débiles o que pronto quedarán en desuso se dejan como último recurso.
 - Se deshabilitan los algoritmos en desuso, o que se sabe son de cifrado inseguro.

Las principales recomendaciones de la industria, sobre la configuración segura de TLS, cambian con frecuencia, a menudo debido a fallas catastróficas en algoritmos de cifrado existentes. Utilice siempre las versiones más recientes de las herramientas de revisión de configuración TLS (como SSLyze u otros escáneres TLS) para configurar el orden y la selección de algoritmos preferidos. La configuración debe comprobarse periódicamente para garantizar que la configuración de comunicaciones seguras esté siempre presente y sea eficaz.

## V9.1 Requisitos de seguridad de las comunicaciones con los clientes

Todas las comunicaciones de cliente solo deben tener lugar a través de rutas de comunicación cifradas. En particular, el uso de TLS 1.2 o posterior es esencialmente requerido por los navegadores y motores de búsqueda modernos. La configuración debe revisarse periódicamente utilizando herramientas en línea para asegurarse de que las últimas prácticas principales están en su lugar.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.1.1** | Compruebe que se utiliza TLS protegido para toda la conectividad de cliente y no se recurre a protocolos inseguros o no cifrados. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | Compruebe con herramientas de prueba en línea o actualizadas que el TLS solo se habilita con algoritmos de cifrado y protocolos robustos, implementando de preferencia los algoritmos de cifrado más fuertes. | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | Compruebe que las versiones antiguas de protocolos SSL y TLS, algoritmos, cifrados y configuración están deshabilitadas, como SSLv2, SSLv3 o TLS 1.0 y TLS 1.1. La última versión de TLS debe ser el conjunto de cifrado preferido. | ✓ | ✓ | ✓ | 326 |


## V9.2 Requisitos de seguridad de las comunicaciones del servidor

Las comunicaciones de servidor son algo más que HTTP. Las conexiones seguras hacia y desde otros sistemas, como sistemas de supervisión, herramientas de administración, acceso remoto y ssh, middleware, bases de datos, mainframes, sistemas de origen externo o de socios, deben estar en su lugar. Todos estos deben ser cifrados para evitar "dureza exterior, trivialmente fácil de interceptar en el interior".

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.2.1** | Compruebe que las conexiones hacia y desde el servidor utilizan certificados TLS de confianza. Cuando se utilizan certificados generados internamente o autofirmados, el servidor debe configurarse para que solo confíe en las CA internas específicas y en los certificados autofirmados específicos. Todos los demás deben ser rechazados. | | ✓ | ✓ | 295 |
| **9.2.2** | Compruebe que las comunicaciones cifradas, como TLS, se utilizan para todas las conexiones entrantes y salientes, incluidos los puertos de administración, monitoreo, la autenticación, la API o las llamadas a servicios web, la base de datos, la nube, el serverless, el mainframe, ya sean externos o de conexiones de asociados. El servidor no debe volver a protocolos inseguros o no cifrados. | | ✓ | ✓ | 319 |
| **9.2.3** | Compruebe que se autentican todas las conexiones cifradas a sistemas externos que implican información o funciones confidenciales. | | ✓ | ✓ | 287 |
| **9.2.4** | Compruebe que la adecuada revocación de certificación, como el grapado del protocolo de estado de certificado en línea (OCSP), esté habilitada y configurada. | | ✓ | ✓ | 299 |
| **9.2.5** | Compruebe que se hace logging de errores de conexión TLS de back-end. | | | ✓ | 544 |

## Referencias

Para obtener más información, véase también:

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* [OWASP - Pinning Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Pinning_Cheat_Sheet.html)
* Notas sobre "Modos aprobados de TLS". En el pasado, el ASVS se refería a la norma estadounidense FIPS 140-2, pero como norma mundial, la aplicación de las normas estadounidenses puede ser difícil, contradictoria o confusa de aplicar. Un mejor método para lograr el cumplimiento de la versión 9.1.3 sería revisar las guías como [Mozilla's Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS) o [generate known good configurations](https://mozilla.github.io/server-side-tls/ssl-config-generator/), y utilizar herramientas de evaluación TLS conocidas, como sslyze, varios escáneres de vulnerabilidades o servicios de evaluación en línea TLS de confianza para obtener un nivel de seguridad deseado. En general, vemos que el incumplimiento de esta categoría es el uso de cifrados y algoritmos obsoletos o inseguros, la falta de secreto directo perfecto, protocolos SSL obsoletos o inseguros, cifrados preferidos débiles, etc.
