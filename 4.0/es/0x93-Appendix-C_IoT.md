# Apéndice C: Requisitos de verificación de Internet de las cosas

Esta capítulo estaba originalmente en la rama principal, pero con el trabajo que el equipo de IoT de OWASP ha realizado, no tiene sentido mantener dos subprocesos diferentes en el tema. Para la versión 4.0, estamos trasladando esto al Apéndice, e instamos a todos los que lo requieran, a utilizar más bien el proyecto principal de [OWASP IoT project](https://owasp.org/www-project-internet-of-things/)

## Objetivo de Control

Los dispositivos integrados/IoT deben:

* Tener el mismo nivel de controles de seguridad dentro del dispositivo que se encuentra en el servidor, aplicando controles de seguridad en un entorno de confianza.
* Los datos confidenciales almacenados en el dispositivo deben realizarse de forma segura mediante el almacenamiento respaldado por hardware, como elementos seguros.
* Todos los datos confidenciales transmitidos desde el dispositivo deben utilizar la seguridad de la capa de transporte.

## Requisitos de verificación de seguridad

| # | Description | L1 | L2 | L3 | Desde |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **C.1** | Verifique que las interfaces de depuración de capa de aplicación, como USB, UART y otras variantes seriales, estén deshabilitadas o protegidas por una contraseña compleja. | ✓ | ✓ | ✓ | 4.0 |
| **C.2** | Verifique que las claves criptográficas y los certificados son únicos para cada dispositivo individual. | ✓ | ✓ | ✓ | 4.0 |
| **C.3** | Verifique que los controles de protección de memoria como ASLR y DEP están habilitados por el sistema operativo integrado/IoT, si procede. | ✓ | ✓ | ✓ | 4.0 |
| **C.4** | Verifique que las interfaces de depuración en chip como JTAG o SWD estén deshabilitadas o que el mecanismo de protección disponible esté habilitado y configurado adecuadamente. | ✓ | ✓ | ✓ | 4.0 |
| **C.5** | Verifique que la ejecución de confianza está implementada y habilitada, si está disponible en el SoC o CPU del dispositivo. | ✓ | ✓ | ✓ | 4.0 |
| **C.6** | Verifique que los datos confidenciales, las claves privadas y los certificados se almacenan de forma segura en un elemento seguro, TPM, TEE (Trusted Execution Environment) o se protegen mediante criptografía segura. | ✓ | ✓ | ✓ | 4.0 |
| **C.7** | Verifique que las aplicaciones de firmware protegen los datos en tránsito mediante la seguridad de la capa de transporte. | ✓ | ✓ | ✓ | 4.0 |
| **C.8** | Verifique que las aplicaciones de firmware validan la firma digital de las conexiones de servidor. | ✓ | ✓ | ✓ | 4.0 |
| **C.9** | Verifique que las comunicaciones inalámbricas se autentiquen mutuamente. | ✓ | ✓ | ✓ | 4.0 |
| **C.10** | Verifique que las comunicaciones inalámbricas se envíen a través de un canal cifrado. | ✓ | ✓ | ✓ | 4.0 |
| **C.11** | Verifique que cualquier uso de funciones C prohibidas se sustituye por las funciones equivalentes seguras adecuadas. | ✓ | ✓ | ✓ | 4.0 |
| **C.12** | Verifique que cada firmware mantiene una lista de materiales de software que cataloga componentes de terceros, control de versiones y vulnerabilidades publicadas. | ✓ | ✓ | ✓ | 4.0 |
| **C.13** | Verifique que todo el código, incluidos los archivos binarios de terceros, las bibliotecas y los marcos de trabajo, se revisen para las credenciales codificadas de forma hardcoded (backdoors). | ✓ | ✓ | ✓ | 4.0 |
| **C.14** | Verifique que la aplicación y los componentes de firmware no son susceptibles a la inyección de comandos del sistema operativo invocando contenedores de comandos de shell, scripts o que los controles de seguridad impiden la inyección de comandos del sistema operativo. | ✓ | ✓ | ✓ | 4.0 |
| **C.15** | Verifique que las aplicaciones de firmware anclan la firma digital a un servidor de confianza. | | ✓ | ✓ | 4.0 |
| **C.16** | Verifique la presencia de la resistencia a la manipulación y/o las características de detección de manipulaciones. | | ✓ | ✓ | 4.0 |
| **C.17** | Verifique que las tecnologías de protección de propiedad intelectual disponibles proporcionadas por el fabricante del chip estén habilitadas. | | ✓ | ✓ | 4.0 |
| **C.18** | Verifique que los controles de seguridad estén en su lugar para obstaculizar la ingeniería inversa del firmware (por ejemplo, remueva los símbolos de depuración detallados). | | ✓ | ✓ | 4.0 |
| **C.19** | Verifique que el dispositivo valide la firma de la imagen de arranque antes de cargarla. | | ✓ | ✓ | 4.0 |
| **C.20** | Verifique que el proceso de actualización del firmware no es vulnerable a los ataques de tiempo de comprobación frente a los ataques de time-of-check vs time-of-use. | | ✓ | ✓ | 4.0 |
| **C.21** | Verifique que el dispositivo utiliza la firma de código y valida los archivos de actualización de firmware antes de instalar. | | ✓ | ✓ | 4.0 |
| **C.22** | Verifique que el dispositivo no se pueda degradar a las versiones antiguas (anti-rollback) del firmware válido. | | ✓ | ✓ | 4.0 |
| **C.23** | Verifique el uso del generador de números pseudoaleatorios criptográficamente seguro en un dispositivo integrado (p. ej., utilizando generadores de números aleatorios proporcionados por chip). | | ✓ | ✓ | 4.0 |
| **C.24** | Verifique que el firmware pueda realizar actualizaciones automáticas de firmware según una programación predefinida. | | ✓ | ✓ | 4.0 |
| **C.25** | Verifique que el dispositivo borra el firmware y los datos confidenciales al detectar la manipulación o la recepción de mensajes no válidos. | | | ✓ | 4.0 |
| **C.26** | Verifique que solo se utilicen microcontroladores que admitan la desactivación de interfaces de depuración (por ejemplo, JTAG, SWD). | | | ✓ | 4.0 |
| **C.27** | Verifique que solo se utilizan microcontroladores que proporcionan una protección sustancial contra ataques de des encapsulación (decapping) y de canal lateral. | | | ✓ | 4.0 |
| **C.28** | Verifique que las trazas sensibles no estén expuestas a las capas externas. | | | ✓ | 4.0 |
| **C.29** | Verifique que la comunicación entre chips esté cifrada (p. ej., comunicación de la placa principal a la placa hija). | | | ✓ | 4.0 |
| **C.30** | Verifique que el dispositivo usa código firmado y valida el código antes de la ejecución. | | | ✓ | 4.0 |
| **C.31** | Verifique que la información confidencial mantenida en la memoria se sobrescribe con ceros tan pronto como ya no sea necesaria. | | | ✓ | 4.0 |
| **C.32** | Verifique que las aplicaciones de firmware utilizan contenedores de kernel para el aislamiento entre aplicaciones. | | | ✓ | 4.0 |
| **C.33** | Verifique que los indicadores seguros del compilador como -fPIE, -fstack-protector-all, -Wl,-z,noexecstack, -Wl,-z,noexecheap están configurados para compilaciones de firmware. | | | ✓ | 4.0 |
| **C.34** | Verifique que los microcontroladores estén configurados con protección de código (si corresponde). | | | ✓ | 4.0 |

## Referencias

Para obtener más información, véase también:

* [OWASP Internet of Things Top 10](https://owasp.org/www-pdf-archive/OWASP-IoT-Top-10-2018-final.pdf)
* [OWASP Embedded Application Security Project](https://owasp.org/www-project-embedded-application-security/)
* [OWASP Internet of Things Project](https://owasp.org/www-project-internet-of-things/)
* [Trudy TCP Proxy Tool](https://github.com/praetorian-inc/trudy)
