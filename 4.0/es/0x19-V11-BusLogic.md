# V11 : Requisitos de verificación de lógica de negocio

## Objetivo de Control

Asegúrese de que una aplicación verificada cumple los siguientes requisitos de alto nivel:
 - El flujo de lógica de negocios es secuencial, se procesa en orden y no se puede omitir.
 - La lógica empresarial incluye límites para detectar y prevenir ataques automatizados, como transferencias continuas de montos pequeños, o agregar un millón de amigos de uno en uno, etc.
 - Los flujos de lógica de negocios de alto valor han considerado casos de abuso y actores malintencionados, y tienen protecciones contra la suplantación, manipulación, repudio, divulgación de información y elevación de ataques de privilegios (STRIDE).

## V11.1 Requisitos de seguridad de la lógica de negocio

La seguridad de la lógica de negocio es tan individual en todas las aplicaciones, que ningún checklist se puede aplicar. La seguridad de la lógica empresarial debe diseñarse para proteger contra amenazas externas probables: no se puede agregar mediante firewalls de aplicaciones web ni comunicaciones seguras. Recomendamos el uso de modelado de amenazas durante los sprints de diseño, por ejemplo, utilizando la herramienta Cornucopia OWASP o herramientas similares.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **11.1.1** | Compruebe que la aplicación solo procesará flujos de lógica de negocio para el mismo usuario en orden de pasos secuenciales y sin omitir pasos.| ✓ | ✓ | ✓ | 841 |
| **11.1.2** | Compruebe que la aplicación solo procesará flujos de lógica de negocios con todos los pasos que se procesan en tiempo humano realista, es decir, las transacciones no se submiten demasiado rápido.| ✓ | ✓ | ✓ | 799 |
| **11.1.3** | Compruebe que la aplicación tiene límites adecuados para acciones o transacciones de negocio específicas, y que se aplican correctamente en base a los usuarios. | ✓ | ✓ | ✓ | 770 |
| **11.1.4** | Compruebe que la aplicación tiene suficientes controles anti-automatización para detectar y proteger contra la exfiltración de datos, las excesivas solicitudes de lógica empresarial, los excesivos uploads de archivos o los ataques de denegación de servicio. | ✓ | ✓ | ✓ | 770 |
| **11.1.5** | Compruebe que la aplicación tiene límites de lógica empresarial o validación para protegerse contra riesgos o amenazas empresariales probables, identificados mediante el modelado de amenazas o metodologías similares. | ✓ | ✓ | ✓ | 841 |
| **11.1.6** | Verifique que la aplicación no tenga problemas de "Time Of Check to Time Of Use" (TOCTOU) u otras race conditions para operaciones sensibles. | | ✓ | ✓ | 367 |
| **11.1.7** | Compruebe que la aplicación supervisa eventos o actividades inusuales desde una perspectiva de lógica de negocios. Por ejemplo, los intentos de realizar acciones fuera de servicio o acciones que un usuario normal nunca intentaría. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 754 |
| **11.1.8** | Compruebe que la aplicación tiene alertas configurables cuando se detectan ataques automatizados o actividad inusual. | | ✓ | ✓ | 390 |

## Referencias

Para obtener más información, véase también:

* [OWASP Testing Guide 4.0: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README.html)
* Anti-automation can be achieved in many ways, including the use of [OWASP AppSensor](https://github.com/jtmelton/appsensor) and [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP AppSensor](https://github.com/jtmelton/appsensor) can also help with Attack Detection and Response.
* [OWASP Cornucopia](https://owasp.org/www-project-cornucopia/)
