# V1 Codificação e Sanitização

## Objetivo de Controle

Este capítulo aborda as fraquezas de segurança de aplicações web mais comuns relacionadas ao processamento inseguro de dados não confiáveis. Tais fraquezas podem resultar em várias vulnerabilidades técnicas, onde dados não confiáveis são interpretados de acordo com as regras de sintaxe do interpretador relevante.

Para aplicações web modernas, é sempre melhor usar APIs mais seguras, como consultas parametrizadas, auto-escaping ou frameworks de template. Caso contrário, a codificação de saída, o escaping ou a sanitização realizados de forma cuidadosa tornam-se críticos para a segurança da aplicação.

A validação de entrada serve como um mecanismo de defesa em profundidade para proteger contra conteúdo inesperado ou perigoso. No entanto, como seu objetivo principal é garantir que o conteúdo recebido corresponda às expectativas funcionais e de negócios, os requisitos relacionados a isso podem ser encontrados no capítulo "Validação e Lógica de Negócios" (Validation and Business Logic).

## V1.1 Arquitetura de Codificação e Sanitização

Nas seções abaixo, são fornecidos requisitos específicos de sintaxe ou específicos de interpretador para o processamento seguro de conteúdo inseguro, a fim de evitar vulnerabilidades de segurança. Os requisitos nesta seção cobrem a ordem em que esse processamento deve ocorrer e onde ele deve ser realizado. Eles também visam garantir que, sempre que os dados forem armazenados, eles permaneçam em seu estado original e não sejam armazenados em formato codificado ou com escape (por exemplo, codificação HTML), para evitar problemas de codificação dupla (double encoding).

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **1.1.1** | Verifique se a entrada é decodificada ou desescapada (unescaped) para uma forma canônica apenas uma vez, se é decodificada apenas quando os dados codificados nessa forma são esperados, e se isso é feito antes de processar a entrada posteriormente (por exemplo, não é realizado após a validação ou sanitização da entrada). | 2 |
| **1.1.2** | Verifique se a aplicação realiza a codificação e o escaping de saída como uma etapa final antes de ser usada pelo interpretador ao qual se destina, ou pelo próprio interpretador. | 2 |

## V1.2 Prevenção de Injeção

A codificação ou escaping de saída, realizada próxima ou adjacente a um contexto potencialmente perigoso, é crítica para a segurança de qualquer aplicação. Normalmente, a codificação e o escaping de saída não são persistidos, mas são usados para tornar a saída segura para uso imediato no interpretador apropriado. Tentar realizar isso muito cedo pode resultar em conteúdo malformado ou tornar a codificação ou o escaping ineficazes.

Em muitos casos, as bibliotecas de software incluem funções seguras ou mais seguras que realizam isso automaticamente, embora seja necessário garantir que elas estejam corretas para o contexto atual.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **1.2.1** | Verifique se a codificação de saída para uma resposta HTTP, documento HTML ou documento XML é relevante para o contexto exigido, como codificar os caracteres relevantes para elementos HTML, atributos HTML, comentários HTML, CSS ou campos de cabeçalho HTTP, para evitar alterar a mensagem ou a estrutura do documento. | 1 |
| **1.2.2** | Verifique se, ao construir URLs dinamicamente, os dados não confiáveis são codificados de acordo com seu contexto (por exemplo, codificação de URL ou codificação base64url para parâmetros de consulta ou de caminho). Garanta que apenas protocolos de URL seguros sejam permitidos (por exemplo, proibir javascript: ou data:). | 1 |
| **1.2.3** | Verifique se a codificação ou escaping de saída é usado ao construir conteúdo JavaScript dinamicamente (incluindo JSON), para evitar a alteração da mensagem ou da estrutura do documento (para evitar a injeção de JavaScript e JSON). | 1 |
| **1.2.4** | Verifique se a seleção de dados ou consultas a bancos de dados (por exemplo, SQL, HQL, NoSQL, Cypher) usam consultas parametrizadas, ORMs, entity frameworks ou são de outra forma protegidas contra injeção de SQL e outros ataques de injeção de banco de dados. Isso também é relevante ao escrever procedimentos armazenados (stored procedures). | 1 |
| **1.2.5** | Verifique se a aplicação protege contra injeção de comando no sistema operacional (OS) e se as chamadas de sistema operacional usam consultas de OS parametrizadas ou usam codificação de saída de linha de comando contextual. | 1 |
| **1.2.6** | Verifique se a aplicação protege contra vulnerabilidades de injeção de LDAP, ou se controles de segurança específicos para prevenir a injeção de LDAP foram implementados. | 2 |
| **1.2.7** | Verifique se a aplicação é protegida contra ataques de injeção de XPath através do uso de parametrização de consultas ou consultas pré-compiladas. | 2 |
| **1.2.8** | Verifique se os processadores LaTeX estão configurados com segurança (como não usar a flag "--shell-escape") e se uma lista de permissões (allowlist) de comandos é usada para evitar ataques de injeção LaTeX. | 2 |
| **1.2.9** | Verifique se a aplicação escapa caracteres especiais em expressões regulares (geralmente usando uma barra invertida) para evitar que sejam mal interpretados como metacaracteres. | 2 |
| **1.2.10** | Verifique se a aplicação está protegida contra injeção de CSV e Fórmulas. A aplicação deve seguir as regras de escaping definidas na RFC 4180 seções 2.6 e 2.7 ao exportar conteúdo CSV. Adicionalmente, ao exportar para CSV ou outros formatos de planilha (como XLS, XLSX ou ODF), caracteres especiais (incluindo '=', '+', '-', '@', '\t' (tab) e '\0' (caractere nulo)) devem ser escapados com uma aspa simples se aparecerem como o primeiro caractere em um valor de campo. | 3 |

Nota: O uso de consultas parametrizadas ou o escape de SQL nem sempre é suficiente. Partes da consulta, como nomes de tabelas e colunas (incluindo nomes de colunas "ORDER BY"), não podem ser escapadas. A inclusão de dados escapados fornecidos pelo usuário nesses campos resulta em falhas nas consultas ou injeção de SQL.

## V1.3 Sanitização

A proteção ideal contra o uso de conteúdo não confiável em um contexto inseguro é usar codificação ou escaping específicos do contexto, o que mantém o mesmo significado semântico do conteúdo inseguro, mas o torna seguro para uso naquele contexto específico, conforme discutido com mais detalhes na seção anterior.

Onde isso não for possível, a sanitização se torna necessária, removendo caracteres ou conteúdos potencialmente perigosos. Em alguns casos, isso pode alterar o significado semântico da entrada, mas, por razões de segurança, pode não haver alternativa.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **1.3.1** | Verifique se todas as entradas HTML não confiáveis provenientes de editores WYSIWYG ou similares são sanitizadas usando uma biblioteca de sanitização HTML conhecida e segura ou um recurso de framework. | 1 |
| **1.3.2** | Verifique se a aplicação evita o uso de eval() ou de outros recursos de execução dinâmica de código, como a Spring Expression Language (SpEL). Onde não houver alternativa, qualquer entrada do usuário a ser incluída deve ser sanitizada antes de ser executada. | 1 |
| **1.3.3** | Verifique se os dados que estão sendo passados para um contexto potencialmente perigoso são sanitizados previamente para aplicar medidas de segurança, como permitir apenas caracteres seguros para esse contexto e cortar entradas muito longas (trimming). | 2 |
| **1.3.4** | Verifique se o conteúdo de script Scalable Vector Graphics (SVG) fornecido pelo usuário é validado ou sanitizado para conter apenas tags e atributos (como gráficos de desenho) que são seguros para a aplicação, por exemplo, não conter scripts e foreignObject. | 2 |
| **1.3.5** | Verifique se a aplicação sanitiza ou desabilita o conteúdo fornecido pelo usuário para linguagens de template com suporte a scripts ou expressões, como Markdown, folhas de estilo CSS ou XSL, BBCode ou similares. | 2 |
| **1.3.6** | Verifique se a aplicação protege contra ataques de Falsificação de Solicitação do Lado do Servidor (Server-side Request Forgery - SSRF), validando dados não confiáveis em relação a uma lista de permissões (allowlist) de protocolos, domínios, caminhos e portas, e sanitizando caracteres potencialmente perigosos antes de usar os dados para chamar outro serviço. | 2 |
| **1.3.7** | Verifique se a aplicação protege contra ataques de injeção de template não permitindo que templates sejam criados com base em entradas não confiáveis. Onde não houver alternativa, qualquer entrada não confiável sendo incluída dinamicamente durante a criação do template deve ser sanitizada ou estritamente validada. | 2 |
| **1.3.8** | Verifique se a aplicação sanitiza apropriadamente as entradas não confiáveis antes de usá-las em consultas do Java Naming and Directory Interface (JNDI) e se o JNDI está configurado com segurança para evitar ataques de injeção JNDI. | 2 |
| **1.3.9** | Verifique se a aplicação sanitiza o conteúdo antes de ser enviado ao memcache para prevenir ataques de injeção. | 2 |
| **1.3.10** | Verifique se as format strings (strings de formatação), que podem ser resolvidas de maneira inesperada ou maliciosa quando usadas, são sanitizadas antes de serem processadas. | 2 |
| **1.3.11** | Verifique se a aplicação sanitiza a entrada do usuário antes de passá-la aos sistemas de e-mail para proteger contra injeção SMTP ou IMAP. | 2 |
| **1.3.12** | Verifique se as expressões regulares estão livres de elementos que causam retrocesso exponencial (exponential backtracking) e certifique-se de que a entrada não confiável seja sanitizada para mitigar ataques de ReDoS ou Runaway Regex. | 3 |

## V1.4 Memória, String e Código Não Gerenciado (Unmanaged Code)

Os requisitos a seguir abordam os riscos associados ao uso inseguro de memória, que geralmente se aplicam quando a aplicação usa uma linguagem de sistemas ou código não gerenciado (unmanaged code).

Em alguns casos, é possível conseguir isso definindo flags do compilador que habilitam proteções e avisos contra estouro de buffer (buffer overflow), incluindo randomização de pilha e prevenção de execução de dados, e que quebram a build se operações inseguras de ponteiro, memória, format string, inteiros ou strings forem encontradas.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **1.4.1** | Verifique se a aplicação usa aritmética de ponteiros, cópia de memória mais segura e strings com segurança de memória para detectar ou prevenir estouros de pilha (stack), buffer ou heap. | 2 |
| **1.4.2** | Verifique se técnicas de validação de sinal, intervalo e entrada são usadas para evitar estouros de inteiros (integer overflows). | 2 |
| **1.4.3** | Verifique se a memória e os recursos alocados dinamicamente são liberados e se as referências ou ponteiros para a memória liberada são removidos ou definidos como nulos (null) para evitar ponteiros pendentes (dangling pointers) e vulnerabilidades de uso após a liberação (use-after-free). | 2 |

## V1.5 Desserialização Segura

A conversão de dados de uma representação armazenada ou transmitida em objetos reais da aplicação (desserialização) tem sido historicamente a causa de várias vulnerabilidades de injeção de código. É importante executar esse processo com cuidado e segurança para evitar esses tipos de problemas.

Em particular, certos métodos de desserialização foram identificados pela documentação da linguagem de programação ou do framework como inseguros e não podem se tornar seguros com dados não confiáveis. Para cada mecanismo em uso, deve-se realizar uma diligência cuidadosa.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **1.5.1** | Verifique se a aplicação configura parsers XML para usar uma configuração restritiva e se recursos inseguros, como a resolução de entidades externas, estão desabilitados para prevenir ataques de Entidade Externa XML (XML eXternal Entity - XXE). | 1 |
| **1.5.2** | Verifique se a desserialização de dados não confiáveis impõe tratamento seguro de entrada, como o uso de uma lista de permissões (allowlist) de tipos de objetos ou a restrição de tipos de objetos definidos pelo cliente, para evitar ataques de desserialização. Mecanismos de desserialização explicitamente definidos como inseguros não devem ser usados com entradas não confiáveis. | 2 |
| **1.5.3** | Verifique se diferentes parsers usados na aplicação para o mesmo tipo de dado (por exemplo, parsers JSON, parsers XML, parsers de URL), realizam o parsing de forma consistente e usam o mesmo mecanismo de codificação de caracteres para evitar problemas como vulnerabilidades de Interoperabilidade JSON ou comportamento diferente na análise de URI ou arquivos sendo explorados em ataques de Inclusão Remota de Arquivo (RFI) ou Falsificação de Solicitação do Lado do Servidor (SSRF). | 3 |

## Referências

Para mais informações, veja também:

* [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
* [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
* [OWASP Web Security Testing Guide: Client-Side Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing)
* [OWASP Java Encoding Project](https://owasp.org/owasp-java-encoder/)
* [DOMPurify - Client-side HTML Sanitization Library](https://github.com/cure53/DOMPurify)
* [RFC4180 - Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180#section-2)

Para obter mais informações, especificamente sobre problemas de desserialização ou parsing, consulte:

* [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
* [An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
* [Orange Tsai - A New Era of SSRF Exploiting URL Parser In Trending Programming Languages](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
