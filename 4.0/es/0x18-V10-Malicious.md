# V10 Código Malicioso

## Objetivo de Control

Asegúrese de que el código cumple los siguientes requisitos de alto nivel:

 * La actividad maliciosa se controla de forma segura y adecuada para no afectar al resto de la aplicación.
 * No tiene bombas de tiempo u otros ataques basados en el tiempo.
 * No permite "llamar a casa" a destinos maliciosos o no autorizados. 
 * No tiene puertas traceras, huevos de pascua, salami attacks, rootkits o código no autorizado que pueda ser controlado por un atacante.

Encontrar código malicioso es una prueba de lo negativo, que es imposible de validar por completo. Se deben realizar los mejores esfuerzos para asegurarse de que el código fuente no contiene código malicioso o funcionalidades no deseadas.

## V10.1 Integridad de Código

La mejor defensa contra el código malintencionado es "confiar, pero verificar". Introducir código no autorizado o malicioso en el código fuente es a menudo un delito en muchas jurisdicciones. Las políticas y procedimientos deben dejar claras las sanciones relativas al código malintencionado.

Los lideres de áreas de desarrolladores deben revisar regularmente las comprobaciones de código, especialmente aquellas que podrían tener acceso a las funciones de tiempo, I/O o funciones de red.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **10.1.1** | Verifique que se está utilizando una herramienta de análisis de código que puede detectar código potencialmente malintencionado, como funciones de tiempo, operaciones de archivos no seguras y conexiones de red. | | | ✓ | 749 |

## V10.2 Búsqueda de Código Malicioso

El código malicioso es extremadamente raro y es difícil de detectar. La revisión manual línea por línea de código puede ayudar a buscar bombas lógicas, pero incluso el revisor de código más experimentado tendrá problemas para encontrar código malicioso, incluso si supiera que existe.

Cumplir con esta sección no es posible sin acceso completo al código fuente, incluidas las bibliotecas de terceros.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **10.2.1** | Verifique que el código fuente de la aplicación y las bibliotecas de terceros no contienen capacidades no autorizadas de recopilación de datos o de “llamadas a casa”. Cuando detecte dicha funcionalidad, obtenga el permiso explicito del usuario para que sea operado así,  antes de recopilar cualquier dato. | | ✓ | ✓ | 359 |
| **10.2.2** | Verifique que la aplicación no solicite permisos innecesarios o excesivos para funciones o sensores relacionados con la privacidad, como contactos, cámaras, micrófonos o ubicación. | | ✓ | ✓ | 272 |
| **10.2.3** | Verifique que el código fuente de la aplicación y las bibliotecas de terceros no contienen puertas traseras, como cuentas, claves o código ofuscado, blobs binarios no documentados, rootkits o anti-depuración, características de depuración inseguras o de otro modo funcionalidades desactualizadas, inseguras u ocultas que podrían usarse maliciosamente si se descubren. | | | ✓ | 507 |
| **10.2.4** | Verifique que el código fuente de la aplicación y las bibliotecas de terceros no contienen bombas de tiempo mediante la búsqueda de funciones relacionadas con la fecha y la hora. | | | ✓ | 511 |
| **10.2.5** | Verifique que el código fuente de la aplicación y las bibliotecas de terceros no contienen código malintencionado, como salami attacks, logic bypasses o bombas lógicas. | | | ✓ | 511 |
| **10.2.6** | Verifique que el código fuente de la aplicación y las bibliotecas de terceros no contienen huevos de pascua ni ninguna otra funcionalidad potencialmente no deseada. | | | ✓ | 507 |

## V10.3 Integridad de Aplicación

Una vez que se implementa una aplicación, todavía se puede insertar código malintencionado. Las aplicaciones deben protegerse contra ataques comunes, como la ejecución de código sin firmar desde orígenes que no son de confianza y tomas de control de subdominios.

Cumplir con esta categoría, es probable que sea una tarea operativa y continua.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **10.3.1** | Verifique si la aplicación tiene una característica de actualización automática de cliente o servidor, las actualizaciones deben obtenerse a través de canales seguros y firmados digitalmente. El código de actualización debe validar la firma digital de la actualización antes de instalar o ejecutar la actualización. | ✓ | ✓ | ✓ | 16 |
| **10.3.2** | Verifique que la aplicación emplea protecciones de integridad, como la firma de código o la integridad de subrecursos. La aplicación no debe cargar ni ejecutar código de fuentes que no sean de confianza, como la carga de includes, plugins, módulos, código o bibliotecas de fuentes que no sean de confianza o de Internet. | ✓ | ✓ | ✓ | 353 |
| **10.3.3** | Verifique que la aplicación tiene protección contra takeovers de subdominios si la aplicación se basa en entradas DNS o subdominios DNS, como nombres de dominio expirados, punteros DNS obsoletos o CNAME, proyectos expirados en repositorios de código fuente públicos o API de nube transitorias, funciones serverless o buckets de almacenamiento (*autogen-bucket-id*.cloud.example.com) o similares. Las protecciones pueden incluir asegurarse de que los nombres DNS utilizados por las aplicaciones se comprueban regularmente para comprobar su caducidad o cambio. | ✓ | ✓ | ✓ | 350 |

## Referencias

* [Hostile Subdomain Takeover, Detectify Labs](https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/)
* [Hijacking of abandoned subdomains part 2, Detectify Labs](https://labs.detectify.com/2014/12/08/hijacking-of-abandoned-subdomains-part-2/)
