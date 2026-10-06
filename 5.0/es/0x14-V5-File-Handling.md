# V5 Manejo de Archivos

## Objetivo del Control

El uso de archivos puede presentar diversos riesgos para la aplicación, entre ellos la denegación de servicio, el acceso no autorizado y el agotamiento del almacenamiento. Este capítulo incluye requerimientos para abordar estos riesgos.

## V5.1 Documentación del Manejo de Archivos

Esta sección incluye un requerimiento para documentar las características esperadas de los archivos que acepta la aplicación, como condición previa necesaria para desarrollar y verificar los controles de seguridad pertinentes.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **5.1.1** | Verifique que la documentación defina los tipos de archivo permitidos, las extensiones de archivo esperadas y el tamaño máximo (incluido el tamaño descomprimido) para cada funcionalidad de carga. Además, asegúrese de que la documentación especifique cómo se garantiza que los archivos sean seguros para que los usuarios finales los descarguen y procesen, por ejemplo, cómo se comporta la aplicación cuando se detecta un archivo malicioso. | 2 |

## V5.2 Carga y Contenido de Archivos

La funcionalidad de carga de archivos es una fuente principal de archivos no confiables. Esta sección describe los requerimientos para garantizar que la presencia, el volumen o el contenido de estos archivos no puedan dañar la aplicación.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **5.2.1** | Verifique que la aplicación solo acepte archivos de un tamaño que pueda procesar sin causar una pérdida de rendimiento ni un ataque de denegación de servicio. | 1 |
| **5.2.2** | Verifique que, cuando la aplicación acepta un archivo, ya sea de forma individual o dentro de un archivo comprimido (como un zip), compruebe que la extensión del archivo coincide con una extensión esperada y valide que el contenido corresponde al tipo representado por la extensión. Esto incluye, entre otras cosas, la comprobación de los 'magic bytes' iniciales, la reescritura de imágenes y el uso de bibliotecas especializadas para la validación del contenido de los archivos. Para el nivel 1 (L1), esto puede centrarse únicamente en los archivos que se utilizan para tomar decisiones específicas de negocio o de seguridad. A partir del nivel 2 (L2), debe aplicarse a todos los archivos que se acepten. | 1 |
| **5.2.3** | Verifique que la aplicación compruebe, antes de descomprimirlos, que los archivos comprimidos (por ejemplo, zip, gz, docx, odt) no superen el tamaño máximo permitido una vez descomprimidos ni el número máximo de archivos. | 2 |
| **5.2.4** | Verifique que se aplique una cuota de espacio y un número máximo de archivos por usuario, para garantizar que un solo usuario no pueda llenar el almacenamiento con demasiados archivos o con archivos excesivamente grandes. | 3 |
| **5.2.5** | Verifique que la aplicación no permita cargar archivos comprimidos que contengan enlaces simbólicos (symlinks), a menos que se requiera expresamente. En ese caso, será necesario aplicar una lista de permitidos (allowlist) con los archivos a los que pueden apuntar los enlaces simbólicos. | 3 |
| **5.2.6** | Verifique que la aplicación rechace las imágenes cargadas cuyas dimensiones en píxeles superen el máximo permitido, para evitar ataques de saturación de píxeles (pixel flood). | 3 |

## V5.3 Almacenamiento de Archivos

Esta sección incluye requerimientos para evitar que los archivos se ejecuten de forma indebida tras su carga, para detectar contenido peligroso y para evitar que datos no confiables se utilicen para controlar dónde se almacenan los archivos.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **5.3.1** | Verifique que los archivos cargados o generados a partir de entradas no confiables y almacenados en una carpeta pública no se ejecuten como código de programa del lado del servidor cuando se acceda a ellos directamente mediante una solicitud HTTP. | 1 |
| **5.3.2** | Verifique que, cuando la aplicación crea rutas de archivo para operaciones con archivos, utilice datos generados internamente o confiables en lugar de los nombres de archivo enviados por el usuario. Si es necesario utilizar nombres o metadatos de archivo enviados por el usuario, deben aplicarse una validación y una sanitización estrictas. Esto protege contra ataques de path traversal, inclusión de archivos locales o remotos (LFI, RFI) y Server-side Request Forgery (SSRF). | 1 |
| **5.3.3** | Verifique que el procesamiento de archivos del lado del servidor, como la descompresión de archivos, ignore la información de rutas proporcionada por el usuario, para evitar vulnerabilidades como zip slip. | 3 |

## V5.4 Descarga de Archivos

Esta sección contiene requerimientos para mitigar los riesgos al servir archivos para su descarga, incluidos los ataques de path traversal y de inyección. También incluye asegurar que los archivos no contengan contenido peligroso.

| # | Descripción | Nivel |
| :---: | :--- | :---: |
| **5.4.1** | Verifique que la aplicación valide o ignore los nombres de archivo enviados por el usuario, incluidos los que llegan en un parámetro JSON, JSONP o de URL, y que especifique un nombre de archivo en el campo de encabezado Content-Disposition de la respuesta. | 2 |
| **5.4.2** | Verifique que los nombres de archivo servidos (por ejemplo, en los campos de encabezado de respuestas HTTP o en archivos adjuntos de correo electrónico) estén codificados o sanitizados (por ejemplo, siguiendo la RFC 6266) para preservar la estructura del documento y evitar ataques de inyección. | 2 |
| **5.4.3** | Verifique que los archivos obtenidos de fuentes no confiables se analicen con antivirus para evitar servir contenido malicioso conocido. | 2 |

## Referencias

Para obtener más información consulte también:

* [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
* [Ejemplo de uso de enlaces simbólicos para la lectura arbitraria de archivos](https://hackerone.com/reports/1439593)
* [Explicación de los "Magic Bytes" en Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures)
