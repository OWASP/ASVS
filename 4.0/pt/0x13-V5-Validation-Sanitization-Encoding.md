# V5 Validação, Sanitização e Codificação

## Objetivo de controle

A falha de segurança da aplicação da Web mais comum é a falha em validar adequadamente a input proveniente do cliente ou do ambiente antes de usá-la diretamente sem qualquer codificação de output. Essa fraqueza leva a quase todas as vulnerabilidades significativas em aplicaçãos da Web, como Cross-Site Scripting (XSS), injeção de SQL, interpreter injection, ataques de localidade/Unicode, ataques de sistema de arquivos e buffer overflows.

Certifique-se de que uma aplicação verificado atenda aos seguintes requisitos de alto nível:

* Validação de input e arquitetura de codificação de output têm um pipeline acordado para evitar ataques de injeção.
* Os dados de input são fortemente digitados, validados, com intervalo ou comprimento verificados, ou, na pior das hipóteses, higienizados ou filtrados.
* Os dados de output são codificados ou escapados conforme o contexto dos dados o mais próximo possível do interpretador.

Com a arquitetura moderna de aplicações da Web, a codificação de output é mais importante do que nunca. É difícil fornecer validação de input robusta em determinados cenários, portanto, o uso de API mais segura, como consultas parametrizadas, estruturas de modelo de escape automático ou codificação de output cuidadosamente escolhida, é fundamental para a segurança da aplicação.

## V5.1 Validação de input

Controles de validação de input implementados adequadamente, usando listas de permissões positivas e digitação forte de dados, podem eliminar mais de 90% de todos os ataques de injeção. As verificações de comprimento e alcance podem reduzir isso ainda mais. Construir a validação de input segura é necessário durante a arquitetura da aplicação, sprints de design, codificação e testes de unidade e integração. Embora muitos desses itens não possam ser encontrados em testes de penetração, os resultados de não implementá-los são geralmente encontrados em V5.3 — Codificação de output e requisitos de prevenção de injeção. Desenvolvedores e revisores de código seguro são recomendados para tratar esta seção como se L1 fosse necessário para todos os itens para evitar injeções.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.1.1** | Verifique se a aplicação possui defesas contra ataques de poluição de parâmetro HTTP, principalmente se a estrutura da aplicação não fizer distinção sobre a origem dos parâmetros de solicitação (GET, POST, cookies, cabeçalhos ou variáveis de ambiente). | ✓ | ✓ | ✓ | 235 |
| **5.1.2** | Verifique se as estruturas protegem contra ataques de atribuição de parâmetros em massa ou se a aplicação possui contramedidas para proteger contra atribuição de parâmetros não segura, como marcar campos como privados ou similares. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 915 |
| **5.1.3** | Verifique se todas as inputs (campos de formulário HTML, solicitações REST, parâmetros de URL, cabeçalhos HTTP, cookies, arquivos em lote, feeds RSS, etc.) são validadas usando validação positiva (listas de permissão). ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.4** | Verifique se os dados estruturados são fortemente digitados e validados em relação a um esquema definido, incluindo caracteres permitidos, comprimento e padrão (por exemplo, números de cartão de crédito, endereços de e-mail, números de telefone ou validação de que dois campos relacionados são razoáveis, como verificar o subúrbio e o CEP /correspondência de código postal). ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 20 |
| **5.1.5** | Verifique se os redirecionamentos e encaminhamentos de URL permitem apenas destinos que aparecem numa lista de permissões ou exibem um aviso ao redirecionar para conteúdo potencialmente não confiável. | ✓ | ✓ | ✓ | 601 |

## V5.2 Sanitização e Sandbox

| # | Descrição  L1 | L2 | L3 | CWE |
| :---: |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :---: | :---:| :---: | :---: |
| **5.2.1** | Verifique se todos os inputs de HTML não confiáveis de editores WYSIWYG ou similares foram devidamente sanitizadas com uma biblioteca, ou recurso de estrutura do higienizador de HTML. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.2.2** | Verifique se os dados não estruturados são limpos para impor medidas de segurança, como caracteres e comprimento permitidos.                                                                                                                                     | ✓ | ✓ | ✓ | 138 |
| **5.2.3** | Verifique se a aplicação limpa a input do usuário antes de passar para os sistemas de e-mail para proteger contra injeção de SMTP ou IMAP.                                                                                                                       | ✓ | ✓ | ✓ | 147 |
| **5.2.4** | Verifique se a aplicação evita o uso de eval() ou outros recursos dinâmicos de execução de código. Onde não houver alternativa, qualquer input do usuário incluída deve ser limpa ou protegida antes de ser executada.                                           | ✓ | ✓ | ✓ | 95 |
| **5.2.5** | Verifique se a aplicação protege contra-ataques de injeção de modelo, garantindo que qualquer input do usuário incluída seja limpa ou protegida.                                                                                                                 | ✓ | ✓ | ✓ | 94 |
| **5.2.6** | Verifique se a aplicação protege contra-ataques SSRF, validando ou limpando dados não confiáveis, ou metadados de arquivos HTTP, como nomes de arquivos e campos de input de URL, e usa listas de permissão de protocolos, domínios, caminhos e portas.           | ✓ | ✓ | ✓ | 918 |
| **5.2.7** | Verifique se a aplicação sanitiza, desativa ou coloca em área restrita o conteúdo de scripts Scalable Vector Graphics (SVG) fornecido pelo usuário, especialmente no que se refere a XSS resultante de scripts embutidos e ao ForeignObject.                     | ✓ | ✓ | ✓ | 159 |
| **5.2.8** | Verifique se a aplicação sanitiza, desativa ou coloca em sandbox o conteúdo de linguagem de modelo de expressão ou script fornecido pelo usuário, como folhas de estilo Markdown, CSS ou XSL, BBCode ou similares.                                               | ✓ | ✓ | ✓ | 94 |

## V5.3 Codificação de Output e Prevenção de Injeção

A codificação de output próxima ou adjacente ao interpretador em uso é crítica para a segurança de qualquer aplicação. Normalmente, a codificação de output não é mantida, mas usada para tornar a output segura no contexto de output apropriado para uso imediato. Deixar de codificar a output resultará numa aplicação injetável e insegura.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.3.1** | Verifique se a codificação de output é relevante para o interpretador e o contexto necessários. Por exemplo, use codificadores especificamente para valores HTML, atributos HTML, JavaScript, parâmetros de URL, cabeçalhos HTTP, SMTP e outros conforme o contexto exigir, especialmente de inputs não confiáveis (por exemplo, nomes com Unicode ou apóstrofes, como ねこ ou O'Hara) . ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 116 |
| **5.3.2** | Verifique se a codificação de output preserva o conjunto de caracteres e localidade escolhidos pelo usuário, de forma que qualquer ponto de caractere Unicode seja válido e manipulado com segurança. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 176 |
| **5.3.3** | Verifique se o escape de output sensível ao contexto, de preferência automatizado — ou, na pior das hipóteses, manual — protege contra XSS refletido, armazenado e baseado em DOM. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 79 |
| **5.3.4** | Verifique se a seleção de dados ou consultas de banco de dados (por exemplo, SQL, HQL, ORM, NoSQL) usam consultas parametrizadas, ORMs, estruturas de entidade ou estão protegidas contra ataques de injeção de banco de dados. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.5** | Verifique se onde mecanismos parametrizados ou mais seguros não estão presentes, a codificação de output específica do contexto é usada para proteger contra ataques de injeção, como o uso de escape SQL para proteger contra injeção SQL. ([C3, C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 89 |
| **5.3.6** | Verifique se a aplicação protege contra ataques de injeção JSON, ataques de avaliação JSON e avaliação de expressão JavaScript. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 830 |
| **5.3.7** | Verifique se a aplicação protege contra vulnerabilidades de injeção de LDAP ou se foram implementados controles de segurança específicos para impedir a injeção de LDAP. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 90 |
| **5.3.8** | Verifique se a aplicação protege contra injeção de comando do SO e se as chamadas do sistema operacional usam consultas de SO parametrizadas ou usam codificação de output de linha de comando contextual. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 78 |
| **5.3.9** | Verifique se a aplicação protege contra ataques de inclusão de arquivo local (LFI) ou inclusão de arquivo remoto (RFI). | ✓ | ✓ | ✓ | 829 |
| **5.3.10** | Verifique se a aplicação protege contra ataques de injeção XPath ou injeção XML. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 643 |

Observação: usar consultas parametrizadas ou escapar do SQL nem sempre é suficiente; nomes de tabelas e colunas, ORDER BY e assim por diante, não podem ser ignorados. A inclusão de dados fornecidos pelo usuário com escape nesses campos resulta em consultas com falha ou injeção de SQL.

Observação: o formato SVG permite explicitamente o script ECMA em quase todos os contextos, portanto, pode não ser possível bloquear completamente todos os vetores SVG XSS. Se o upload de SVG for necessário, é altamente recomendável servir esses arquivos carregados como texto/sem formatação ou usar um domínio de conteúdo fornecido pelo usuário separado para evitar que o XSS bem-sucedido assuma o controle da aplicação.

## V5.4 Memória, String e Código Não Gerenciado

Os requisitos a seguir serão aplicados apenas quando a aplicação usar uma linguagem de sistema ou código não gerenciado.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **5.4.1** | Verifique se a aplicação usa cadeia de memória segura, cópia de memória mais segura e aritmética de ponteiro para detectar ou evitar estouros de pilha, buffer ou heap. | | ✓ | ✓ | 120 |
| **5.4.2** | Verifique se as strings de formato não aceitam inputs potencialmente hostis e são constantes. | | ✓ | ✓ | 134 |
| **5.4.3** | Verifique se as técnicas de validação de sinal, intervalo e input são usadas para evitar estouros de número inteiro. | | ✓ | ✓ | 190 |

## V5.5 Prevenção de desserialização

| # | Descrição  L1 | L2 | L3 | CWE |
| :---: |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :---: | :---:| :---: | :---: |
| **5.5.1** | Verifique se os objetos serializados usam verificações de integridade ou são criptografados para impedir a criação de objetos hostis ou adulteração de dados. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering))                                                   | ✓ | ✓ | ✓ | 502 |
| **5.5.2** | Verifique se a aplicação restringe corretamente os analisadores de XML para usar apenas a configuração mais restritiva possível e para garantir que recursos não seguros, como a resolução de entidades externas, sejam desabilitados para evitar ataques de XML eXternal Entity (XXE). | ✓ | ✓ | ✓ | 611 |
| **5.5.3** | Verifique se a desserialização de dados não confiáveis é evitada ou protegida em código personalizado e bibliotecas de terceiros (como analisadores JSON, XML e YAML).                                                                                                                  | ✓ | ✓ | ✓ | 502 |
| **5.5.4** | Verifique se, ao analisar JSON em navegadores ou back-ends baseados em JavaScript, JSON.parse é usado para analisar o documento JSON. Não use eval() para analisar JSON.                                                                                                                | ✓ | ✓ | ✓ | 95 |

## Referências

Para mais informações, consulte também:

* [OWASP Testing Guide 4.0: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Cheat Sheet: Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution.html)
* [OWASP LDAP Injection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Testing Guide 4.0: Client Side Testing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client_Side_Testing/)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [XML External Entity (XXE) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)

Para obter mais informações sobre escape automático, consulte:

* [Reducing XSS by way of Automatic Context-Aware Escaping in Template Systems](https://googleonlinesecurity.blogspot.com/2009/03/reducing-xss-by-way-of-automatic.html)
* [AngularJS Strict Contextual Escaping](https://docs.angularjs.org/api/ng/service/$sce)
* [AngularJS ngBind](https://docs.angularjs.org/api/ng/directive/ngBind)
* [Angular Sanitization](https://angular.io/guide/security#sanitization-and-security-contexts)
* [Angular Security](https://angular.io/guide/security)
* [ReactJS Escaping](https://reactjs.org/docs/introducing-jsx.html#jsx-prevents-injection-attacks)
* [Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

Para obter mais informações sobre desserialização, consulte:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [OWASP Deserialization of Untrusted Data Guide](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)

