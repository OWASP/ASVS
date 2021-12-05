# V4 : Requisitos de verificación de control de acceso

## Objetivo de Control

La autorización es el concepto de permitir el acceso a los recursos solo a aquellos a los que se les permite utilizarlos. Asegúrese de que una aplicación verificada cumple los siguientes requisitos de alto nivel:

 - Las personas que acceden a los recursos tienen credenciales válidas para hacerlo. 

 - Los usuarios están asociados a un conjunto bien definido de roles y privilegios. 

 - Los metadatos de roles y permisos están protegidos contra la reproducción o la manipulación.

## Requisitos de verificación de seguridad

## V4.1 Diseño de Control General de Acceso

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.1.1** | Compruebe que la aplicación aplica las reglas de control de acceso en una capa de servicio de confianza, especialmente si el control de acceso del lado cliente está presente y podría ser bypaseado. | ✓ | ✓ | ✓ | 602 |
| **4.1.2** | Compruebe que todos los atributos de usuario y datos y la información de directiva utilizada por los controles de acceso no pueden ser manipulados por los usuarios finales a menos que se autorice específicamente. | ✓ | ✓ | ✓ | 639 |
| **4.1.3** | Compruebe que existe el principio de privilegios mínimos: los usuarios solo deben poder acceder a funciones, archivos de datos, direcciones URL, controladores, servicios y otros recursos, para los que poseen una autorización específica. Esto implica protección contra la suplantación y elevación de privilegios. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |
| **4.1.4** | Compruebe que existe el principio de denegación predeterminada, mediante el cual los nuevos usuarios/roles comienzan con permisos mínimos o sin permisos y los usuarios/roles no reciben acceso a nuevas características hasta que se asigna explícitamente el acceso. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 276 |
| **4.1.5** | Compruebe que los controles de acceso fallan de forma segura, incluso cuando se produce una excepción. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |

## V4.2 Control de acceso a nivel de operación

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.2.1** | Compruebe que los datos confidenciales y las API están protegidos contra ataques de referencia insegura directa de objetos (IDOR) dirigidos a la creación, lectura, actualización y eliminación de registros, como la creación o actualización del registro de otra persona, la visualización de los registros de todos o la eliminación de todos los registros. | ✓ | ✓ | ✓ | 639 |
| **4.2.2** | Compruebe que la aplicación o el framework de trabajo aplica un mecanismo anti-CSRF seguro para proteger la funcionalidad autenticada, y eficaz anti-automatización o anti-CSRF protege la funcionalidad no autenticada. | ✓ | ✓ | ✓ | 352 |

## V4.3 Otras consideraciones de control de acceso

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **4.3.1** | Verifique que las interfaces administrativas utilicen la autenticación multifactor adecuada para evitar el uso no autorizado. | ✓ | ✓ | ✓ | 419 |
| **4.3.2** | Compruebe que la exploración de directorios está deshabilitada a menos que se desee deliberadamente. Además, las aplicaciones no deben permitir la detección o divulgación de metadatos de archivos o directorios, como `Thumbs.db`, `.DS_Store`, `.git` o `.svn`. | ✓ | ✓ | ✓ | 548 |
| **4.3.3** | Compruebe que la aplicación tiene autorización adicional (como la autenticación de paso a paso o adaptación) para sistemas de menor valor y/ o segregación de tareas para aplicaciones de alto valor para aplicar controles antifraude según el riesgo de aplicación y fraudes previos. | | ✓ | ✓ | 732 |

## Referencias

Para obtener más información, véase también:

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Access Control](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
* [OWASP CSRF Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [OWASP REST Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
