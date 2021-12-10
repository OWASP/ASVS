# V12 Archivos y Recursos

## Objetivo de Control

Asegúrese de que una aplicación verificada cumple los siguientes requisitos de alto nivel:

* Los datos de archivo que no son de confianza deben manejarse en consecuencia de una manera segura.
* Los datos de archivos que no son de confianza obtenidos de fuentes no confiables se almacenan fuera de la raíz web y con permisos limitados.

## V12.1 Carga de Archivos

Aunque las bombas zip son eminentemente comprobables utilizando técnicas de prueba de penetración, se consideran L2 y superiores para fomentar la consideración de diseño y desarrollo con pruebas manuales cuidadosas, y para evitar pruebas de penetración automatizadas o del tipo manual pero no calificadas de una condición de denegación de servicio.

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.1.1** | Verifique que la aplicación no aceptará archivos grandes que puedan llenar el almacenamiento o provocar una denegación de servicio. | ✓ | ✓ | ✓ | 400 |
| **12.1.2** | Verifique que la aplicación compruebe los archivos comprimidos (p. ej. zip, gz, docx, odt) contra el tamaño máximo sin comprimir permitido y con el número máximo de archivos antes de descomprimir el archivo. | | ✓ | ✓ | 409 |
| **12.1.3** | Verifique que se aplica una cuota de tamaño de archivo y un número máximo de archivos por usuario para asegurarse de que un solo usuario no puede llenar el almacenamiento con demasiados archivos o archivos excesivamente grandes. | | ✓ | ✓ | 770 |

## V12.2 Integridad de Archivos

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.2.1** | Verifique que los archivos obtenidos de orígenes que no son de confianza se validan para que sean del tipo esperado en función del contenido del archivo. | | ✓ | ✓ | 434 |

## V12.3 Ejecución de Archivos

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.3.1** | Verifique que los metadatos del nombre de archivo enviados por el usuario no se utilizan directamente por los sistemas de archivos del sistema o del marco de trabajo y que se utiliza una API de dirección URL para proteger contra el recorrido de ruta de acceso. | ✓ | ✓ | ✓ | 22 |
| **12.3.2** | Verifique que los metadatos del nombre de archivo enviados por el usuario se validan o ignoran para evitar la divulgación, creación, actualización o eliminación de archivos locales (LFI). | ✓ | ✓ | ✓ | 73 |
| **12.3.3** | Verifique que los metadatos del nombre de archivo enviados por el usuario se validan o omiten para evitar la divulgación o ejecución de archivos remotos a través de ataques de inclusión remota de archivos (RFI) o falsificación de solicitudes del lado del servidor (SSRF). | ✓ | ✓ | ✓ | 98 |
| **12.3.4** | Verifique que la aplicación protege contra la descarga de archivos reflectantes (RFD) validando o ignorando los nombres de archivo enviados por el usuario en un parámetro JSON, JSONP o URL, el encabezado Content-Type de respuesta debe establecerse en text/plain y el encabezado Content-Disposition debe tener un nombre de archivo fijo. | ✓ | ✓ | ✓ | 641 |
| **12.3.5** | Verifique que los metadatos de archivos que no son de confianza no se utilizan directamente con la API del sistema o las bibliotecas, para proteger contra la inyección de comandos del sistema operativo. | ✓ | ✓ | ✓ | 78 |
| **12.3.6** | Verifique que la aplicación no incluye ni ejecuta funcionalidad desde orígenes que no son de confianza, como redes de distribución de contenido no verificadas, bibliotecas de JavaScript, bibliotecas node npm o archivos DLL server-side. | | ✓ | ✓ | 829 |

## V12.4 Almacenamiento de Archivos

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.4.1** | Verifique que los archivos obtenidos de fuentes no confiables se almacenen fuera de la raíz web, con permisos limitados. | ✓ | ✓ | ✓ | 552 |
| **12.4.2** | Verifique que los escáneres antivirus analicen los archivos obtenidos de fuentes no confiables para evitar la carga y el servicio de contenido malicioso conocido. | ✓ | ✓ | ✓ | 509 |

## V12.5 Descarga de Archivos

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.5.1** | Verifique que la capa web está configurado para transmitir solo archivos con extensiones específicas, para evitar la filtración accidental de información o código fuente. Por ejemplo, los archivos de copia de seguridad (p. ej. .bak), los archivos de trabajo temporales (p. ej. .swp), los archivos comprimidos (.zip, .tar.gz, etc.) y otras extensiones utilizadas comúnmente por los editores deben bloquearse a menos que sea necesario. | ✓ | ✓ | ✓ | 552 |
| **12.5.2** | Verifique que las solicitudes directas a los archivos cargados nunca se ejecutarán como contenido HTML/JavaScript. | ✓ | ✓ | ✓ | 434 |

## V12.6 Protección SSRF

| # | Descripción | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.6.1** | Verifique que el servidor web o de aplicaciones está configurado con una lista de permisos de recursos o sistemas a los que el servidor puede enviar solicitudes o cargar datos o archivos. | ✓ | ✓ | ✓ | 918 |

## Referencias

Para obtener más información, véase también:

* [File Extension Handling for Sensitive Information](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
* [Reflective file download by Oren Hafif](https://www.trustwave.com/Resources/SpiderLabs-Blog/Reflected-File-Download---A-New-Web-Attack-Vector/)
* [OWASP Third Party JavaScript Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html)
