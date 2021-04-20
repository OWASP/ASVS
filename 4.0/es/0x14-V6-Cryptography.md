# V6 : Requisitos de verificación de criptografía almacenada

## Objetivo de Control

Asegúrese de que una aplicación verificada cumple los siguientes requisitos de alto nivel:

 - Todos los módulos criptográficos fallan de forma segura y que los errores se gestionan correctamente. 
 - Se utiliza un generador de números aleatorios adecuado. 
 - El acceso a las claves se administra de forma segura.

## V6.1 Clasificación de datos

El activo más importante son los datos procesados, almacenados o transmitidos por una aplicación. Realice siempre una evaluación de impacto en la privacidad para clasificar correctamente las necesidades de protección de datos de los datos almacenados.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.1.1** | Compruebe que los datos privados regulados se almacenan cifrados mientras están en reposo, como información de identificación personal (PII), información personal confidencial o datos evaluados que puedan estar sujetos al RGPD de la UE. | | ✓ | ✓ | 311 |
| **6.1.2** | Verifique que los datos de salud regulados se almacenen cifrados mientras están en reposo, como registros médicos, detalles de dispositivos médicos o registros de investigación anonimizados. | | ✓ | ✓ | 311 |
| **6.1.3** | Verifique que los datos financieros regulados se almacenen cifrados mientras están en reposo, como cuentas financieras, impagos o historial de crédito, registros fiscales, historial de pagos, beneficiarios o registros de mercado o de investigación anonimizados. | | ✓ | ✓ | 311 |

## V6.2 Algoritmos

Los avances recientes en criptografía significan que los algoritmos y longitudes de clave previamente seguros ya no son seguros o suficientes para proteger los datos. Por lo tanto, debe ser posible cambiar algoritmos.

Aunque esta sección no se prueba fácilmente con penetración, los desarrolladores deben considerar toda esta sección como obligatoria aunque falta L1 de la mayoría de los elementos.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.2.1** | Compruebe que todos los módulos criptográficos fallan de forma segura y que los errores se gestionan de forma que no se habilitan los ataques de Padding Oráculo. | ✓ | ✓ | ✓ | 310 |
| **6.2.2** | Verifique que se utilicen algoritmos, modos y bibliotecas criptográficas probados por la industria o aprobados por el gobierno, en lugar de criptografía codificada personalizada. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 327 |
| **6.2.3** | Compruebe que los modos de vector de inicialización de cifrado, configuración de cifrado y bloque están configurados de forma segura mediante los últimos consejos vigentes. | | ✓ | ✓ | 326 |
| **6.2.4** | Verifique que los algoritmos de número aleatorio, cifrado o hash, longitudes de clave, rondas, cifrados o modos, se puedan reconfigurar, actualizar o intercambiar en cualquier momento, para protegerse contra roturas criptográficas. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 326 |
| **6.2.5** | Compruebe que los modos de bloque inseguros conocidos (e.g., ECB, etc.), los modos de relleno (es decir, PKCS#1 v1.5, etc.), los cifrados con tamaños de bloque pequeños (es decir, Triple-DES, Blowfish, etc.) y los algoritmos de hashing débiles (es decir, MD5, SHA1, etc.) no se utilizan a menos que sea necesario para la compatibilidad con versiones anteriores. | | ✓ | ✓ | 326 |
| **6.2.6** | Compruebe que los nonces, los vectores de inicialización y otros números de uso único no se deben usar más de una vez con una clave de cifrado determinada. El método de generación debe ser adecuado para el algoritmo que se está utilizando. | | ✓ | ✓ | 326 |
| **6.2.7** | Verifique que los datos cifrados se autentiquen a través de firmas, modos de cifrado autenticados o [HMAC](https://en.wikipedia.org/wiki/HMAC) para asegurarse de que el texto cifrado no sea alterado por una parte no autorizada. | | | ✓ | 326 |
| **6.2.8** | Compruebe que todas las operaciones criptográficas son de tiempo constante, sin operaciones de "cortocircuito" en comparaciones, cálculos o devoluciones, para evitar fugas de información. | | | ✓ | 385 |

## V6.3 Valores Random

True Pseudo-random Number Generation (PRNG) es increíblemente difícil de acercar. Generalmente, las buenas fuentes de entropía dentro de un sistema se agotarán rápidamente si se utilizan en exceso, pero las fuentes con menos aleatoriedad pueden conducir a claves y secretos predecibles.

| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.3.1** | Compruebe que todos los números aleatorios, nombres de archivo aleatorios, GUID aleatorios y cadenas aleatorias se generan utilizando el generador de números aleatorios criptográficamente seguro aprobado por el módulo criptográfico cuando estos valores aleatorios están destinados a no ser adivinables por un atacante. | | ✓ | ✓ | 338 |
| **6.3.2** | Compruebe que los GUID aleatorios se crean mediante el algoritmo GUID v4 y un generador de números pseudoaleatorio (CSPRNG) criptográficamente seguro. Los GUID creados con otros generadores de números pseudoaleatorios pueden ser predecibles. | | ✓ | ✓ | 338 |
| **6.3.3** | Compruebe que los números aleatorios se crean con la entropía adecuada incluso cuando la aplicación está bajo carga pesada, o que la aplicación se degrada correctamente en tales circunstancias. | | | ✓ | 338 |

## V6.4 Administración de secretos

Bien que cette section ne soit pas facilement testée, les développeurs devraient considérer toute cette section comme obligatoire même si la L1 est absente de la plupart des éléments.
| # | Description | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.4.1** | Compruebe que una solución de administración de secretos, como un almacén de claves, se utiliza para crear, almacenar, controlar el acceso y destruir secretos de forma segura. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 798 |
| **6.4.2** | Compruebe que el material de claves no está expuesto a la aplicación, sino que utiliza un módulo de seguridad aislado como un almacén para operaciones criptográficas. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 320 |

## Referencias

Para obtener más información, véase también:

* [OWASP Testing Guide 4.0: Testing for weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/README.html)
* [OWASP Cheat Sheet: Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-2](https://csrc.nist.gov/publications/detail/fips/140/2/final)
