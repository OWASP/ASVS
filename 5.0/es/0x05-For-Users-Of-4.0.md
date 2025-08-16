# Cambios en comparación con la versión v4.x

## Introducción

Los usuarios familiarizados con la versión 4.x del estándar pueden encontrar útil revisar los cambios clave introducidos en la versión 5.0, incluyendo actualizaciones de contenido, alcance y filosofía subyacente.

De los 286 requerimientos de la versión 4.0.3 solo 11 permanecen sin cambios, mientras que 15 han sufrido pequeños ajustes gramaticales sin alterar su significado. En total, 109 requerimientos (38%) ya no son requerimientos independientes en la versión 5.0, con 50 simplemente eliminados, 28 se eliminaron por duplicados y 31 se fusionaron con otros requerimientos. El resto se ha revisado de alguna manera. Incluso los requerimientos que no se modificaron sustancialmente tienen identificadores diferentes debido a reordenación o reestructuración.

Para facilitar la adopción de la versión 5.0, se proporcionan documentos de mapeo para ayudar a los usuarios a rastrear cómo se corresponden los requerimientos de la versión 4.x con los de la versión 5.0. Estos mapeos no están vinculados al versionamiento y pueden actualizarse o aclararse según sea necesario.

## Filosofía de los requerimientos

### Alcance y enfoque

La versión 4.x incluía requerimientos que no se ajustaban al alcance previsto del estándar; estos se han eliminado. También se han excluido los requerimientos que no cumplían los criterios de alcance de la versión 5.0 o que no eran verificables.

### Énfasus en metas de Seguridad por sobre mecanismos

En la versión 4.x, muchos requerimientos se centraban en mecanismos específicos en lugar de en los objetivos de seguridad subyacentes. En la versión 5.0, los requerimientos se centran en los objetivos de seguridad, haciendo referencia a mecanismos concretos solo cuando constituyen la única solución práctica o proporcionándolos como ejemplos o guía complementaria.

Este enfoque reconoce que pueden existir múltiples métodos para lograr un objetivo de seguridad determinado y evita la prescripción innecesaria que podría limitar la flexibilidad organizativa.

Además, se han consolidado los requerimientos que abordan el mismo problema de seguridad cuando corresponde.

### Decisiones de seguridad documentadas

Si bien el concepto de decisiones de seguridad documentadas puede parecer nuevo en la versión 5.0, representa una evolución de los requerimientos anteriores relacionados con la aplicación de políticas y el modelado de amenazas (threat modeling) de la versión 4.0. Anteriormente, algunos requerimientos exigían implícitamente un análisis para fundamentar la implementación de controles de seguridad, como por ejemplo la determinación de las conexiones de red permitidas.

Para garantizar que la información necesaria esté disponible para la implementación y la verificación, estas expectativas ahora se definen explícitamente como requerimientos de documentación, lo que las hace claras, viables y verificables.

## Cambios estructurales y nuevos capítulos

Varios capítulos de la versión 5.0 introducen contenido completamente nuevo:

* OAuth y OIDC - Dada la adopción generalizada de estos protocolos para la delegación de acceso y el inicio de sesión único (single sign-on), se han añadido requerimientos específicos para abordar los diversos escenarios que pueden encontrar los desarrolladores. Esta área podría eventualmente convertirse en un estándar independiente, similar al tratamiento de los requerimientos para dispositivos móviles e IoT en versiones anteriores.
* WebRTC - A medida que esta tecnología gana popularidad, sus consideraciones y desafíos de seguridad únicos se abordan ahora en una sección dedicada.

También se han realizado esfuerzos para garantizar que los capítulos y secciones se organicen en torno a conjuntos coherentes de requerimientos relacionados.

Esta reestructuración ha dado lugar a la creación de capítulos adicionales:

* Tokens auto-contenidos - Anteriormente agrupados bajo gestión de sesiones, los tokens auto-contenidos ahora se reconocen como un mecanismo independiente y un elemento fundamental para la comunicación sin estado (stateless) (como en OAuth y OIDC). Debido a sus singulares implicaciones de seguridad se abordan en un capítulo específico, con algunos requerimientos nuevos introducidos en la versión 5.x.
* Seguridad del Frontend web - Con la creciente complejidad de las aplicaciones basadas en navegador y el auge de las arquitecturas basadas únicamente en API, los requerimientos de seguridad del frontend se han separado en un capítulo propio.
* Codificación y arquitectura seguras - Se han agrupado aquí los nuevos requerimientos que abordan prácticas generales de seguridad que no encajaban en los capítulos existentes.

Se realizaron otros cambios organizativos en la versión 5.0 para aclarar la intención. Por ejemplo, los requerimientos de validación de entrada se trasladaron junto con lógica de negocio, reflejando su función en la aplicación de las reglas de negocio en lugar de agruparse con sanitización y codificación.

Se eliminó el antiguo capítulo "Arquitectura V1". Su sección inicial contenía requerimientos que estaban fuera del alcance, mientras que las secciones posteriores se redistribuyeron a los capítulos pertinentes, con los requerimientos deduplicados y aclarados según fuera necesario.

## Eliminación de mapeos directos a otros estándares

Se han eliminado del cuerpo principal del estándar los mapeos directos a otros estándares. El objetivo es preparar un mapeo con el proyecto de Enumeración de Requerimientos Comunes (CRE) de OWASP, que a su vez vinculará ASVS con diversos proyectos de OWASP y estándares externos.

Los mapeos directos a CWE y NIST ya no se mantienen, como se explica a continuación.

### Reducción del acoplamiento con las directrices de identidad digital del NIST

Las [Directrices de Identidad Digital (SP 800-63)](https://pages.nist.gov/800-63-3/) del NIST han servido durante mucho tiempo como referencia para los controles de autenticación y autorización. En la versión 4.x, ciertos capítulos se ajustaron estrechamente a la estructura y terminología del NIST.

Si bien estas directrices siguen siendo una referencia importante, su estricta alineación generó desafíos como una terminología menos reconocida, la duplicación de requerimientos similares y mapeos incompletos. La versión 5.0 se aleja de este enfoque para mejorar la claridad y la relevancia.

### Alejándose de la Enumeración de Debilidades Comunes (Common Weakness Enumeration CWE) 

La [Enumeración de Debilidades Comunes (CWE)](https://cwe.mitre.org/) proporciona una taxonomía útil de las debilidades de seguridad del software. Sin embargo, desafíos como las CWE solo por categoría, dificultades para asignar requerimientos a una única CWE y la presencia de mapeos imprecisos en la versión 4.x han llevado a la decisión de suspender los mapeos directos de CWE en la versión 5.0.

## Repensando las definiciones de niveles

La versión 4.x describía los niveles como 1 ("Mínimo"), 2 ("Estándar") y 3 ("Avanzado"), lo que implicaba que todas las aplicaciones que manejan datos sensibles debían cumplir al menos con el nivel 2.

La versión 5.0 soluciona varios problemas con este enfoque y que se describen en los siguientes párrafos.

En la práctica, mientras que la versión 4.x utilizaba marcas de verificación para los indicadores de nivel, la versión 5.x utiliza un número simple en todos los formatos del estándar, incluyendo Markdown, PDF, DOCX, CSV, JSON y XML. Para garantizar la compatibilidad con versiones anteriores, también se generan versiones anteriores de las salidas CSV, JSON y XML que aún utilizan marcas de verificación.

### Nivel de entrada mas fácil.

Los comentarios de retroalimentación indicaron que una gran cantidad de requerimientos de Nivel 1 (aproximadamente 120), junto con su designación como el nivel "mínimo", era insuficiente para la mayoría de las aplicaciones y desalentaba su adopción. La versión 5.0 busca reducir esta barrera definiendo el Nivel 1 principalmente en torno a los requerimientos de defensa de primera capa, lo que resulta en menos requerimientos pero más claros en ese nivel. Para demostrarlo numéricamente, en la v4.0.3 había 128 requerimientos de Nivel 1 de un total de 278, lo que representa un 46%. En la versión 5.0.0 hay 70 requerimientos de Nivel 1 de un total de 345, lo que representa un 20%.

### La falacia de la testabilidad (Testability)

Un factor clave en la selección de los controles de Nivel 1 en la versión 4.x fue su idoneidad para la evaluación mediante pruebas de penetración externas de "caja negra". Sin embargo, este enfoque no se ajustaba plenamente al propósito del Nivel 1 como conjunto mínimo de controles de seguridad. Algunos usuarios argumentaron que el Nivel 1 era insuficiente para proteger las aplicaciones mientras que otros lo consideraron demasiado difícil de probar.

Considerar la testabilidad como criterio es relativo y, en ocasiones, engañoso. El hecho de que un requerimiento sea testable no garantiza que pueda probarse de forma automatizada o sencilla. Además, los requerimientos más fáciles de probar no siempre son aquellos con mayor impacto en la seguridad ni los más sencillos de implementar.

Por lo tanto, en la versión 5.0, las decisiones de nivel se tomaron principalmente en función de la reducción de riesgos y teniendo en cuenta el esfuerzo de implementación.

### No solo acerca del riesgo

El uso de niveles prescriptivos basados en el riesgo que exigen un nivel específico para ciertas aplicaciones ha demostrado ser excesivamente rígido. En la práctica, la priorización e implementación de los controles de seguridad dependen de múltiples factores, incluyendo tanto la reducción del riesgo como el esfuerzo requerido para su implementación.

Por lo tanto, se anima a las organizaciones a alcanzar el nivel que consideren necesario en función de su madurez y del mensaje que desean transmitir a sus usuarios.
