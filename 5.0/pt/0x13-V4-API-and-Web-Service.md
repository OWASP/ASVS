# V4 API e Web Service

## Objetivo de Controle

Diversas considerações se aplicam especificamente a aplicações que expõem APIs para uso por navegadores web ou outros consumidores (comumente usando JSON, XML ou GraphQL). Este capítulo abrange as configurações e os mecanismos de segurança relevantes que devem ser aplicados.

Note que as preocupações com autenticação, gerenciamento de sessão e validação de entrada de outros capítulos também se aplicam a APIs, portanto, este capítulo não pode ser tirado de contexto ou testado isoladamente.

## V4.1 Segurança Genérica de Web Service

Esta seção aborda considerações gerais de segurança de web services e, consequentemente, práticas básicas de higiene de web services.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **4.1.1** | Verifique se toda resposta HTTP com um corpo de mensagem contém um campo de cabeçalho Content-Type que corresponda ao conteúdo real da resposta, incluindo o parâmetro charset para especificar uma codificação de caracteres segura (ex., UTF-8, ISO-8859-1) de acordo com os Tipos de Mídia da IANA, como "text/", "/+xml" e "/xml". | 1 |
| **4.1.2** | Verifique se apenas endpoints voltados ao usuário (destinados ao acesso manual por navegador web) redirecionam automaticamente de HTTP para HTTPS, enquanto outros serviços ou endpoints não implementam redirecionamentos transparentes. Isso serve para evitar uma situação em que um cliente envia erroneamente requisições HTTP não criptografadas, mas como as requisições são redirecionadas automaticamente para HTTPS, o vazamento de dados sensíveis passa despercebido. | 2 |
| **4.1.3** | Verifique se qualquer campo de cabeçalho HTTP usado pela aplicação e definido por uma camada intermediária, como um balanceador de carga, um proxy web ou um serviço backend-for-frontend, não pode ser substituído (overridden) pelo usuário final. Exemplos de cabeçalhos podem incluir X-Real-IP, X-Forwarded-* ou X-User-ID. | 2 |
| **4.1.4** | Verifique se apenas os métodos HTTP explicitamente suportados pela aplicação ou por sua API (incluindo OPTIONS durante requisições preflight) podem ser usados e se os métodos não utilizados estão bloqueados. | 3 |
| **4.1.5** | Verifique se assinaturas digitais por mensagem são usadas para fornecer garantia adicional, além das proteções de transporte, para requisições ou transações que são altamente sensíveis ou que atravessam vários sistemas. | 3 |

## V4.2 Validação da Estrutura da Mensagem HTTP

Esta seção explica como a estrutura e os campos de cabeçalho de uma mensagem HTTP devem ser validados para evitar ataques como falsificação de requisição (request smuggling), divisão de resposta (response splitting), injeção de cabeçalho e negação de serviço por meio de mensagens HTTP excessivamente longas.

Esses requisitos são relevantes para o processamento e a geração geral de mensagens HTTP, mas são especialmente importantes ao converter mensagens HTTP entre diferentes versões do HTTP.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **4.2.1** | Verifique se todos os componentes da aplicação (incluindo balanceadores de carga, firewalls e servidores de aplicação) determinam os limites das mensagens HTTP de entrada usando o mecanismo apropriado para a versão do HTTP, a fim de evitar falsificação de requisição HTTP (HTTP request smuggling). No HTTP/1.x, se um campo de cabeçalho Transfer-Encoding estiver presente, o cabeçalho Content-Length deve ser ignorado conforme a RFC 2616. Ao usar HTTP/2 ou HTTP/3, se um campo de cabeçalho Content-Length estiver presente, o receptor deve garantir que seja consistente com o comprimento dos frames DATA. | 2 |
| **4.2.2** | Verifique se, ao gerar mensagens HTTP, o campo de cabeçalho Content-Length não entra em conflito com o comprimento do conteúdo determinado pelo enquadramento (framing) do protocolo HTTP, a fim de evitar ataques de request smuggling. | 3 |
| **4.2.3** | Verifique se a aplicação não envia nem aceita mensagens HTTP/2 ou HTTP/3 com campos de cabeçalho específicos da conexão, como Transfer-Encoding, para evitar ataques de response splitting e injeção de cabeçalho. | 3 |
| **4.2.4** | Verifique se a aplicação aceita apenas requisições HTTP/2 e HTTP/3 onde os campos de cabeçalho e valores não contêm nenhuma sequência CR (\r), LF (\n) ou CRLF (\r\n), para evitar ataques de injeção de cabeçalho. | 3 |
| **4.2.5** | Verifique se, caso a aplicação (backend ou frontend) construa e envie requisições, ela usa validação, sanitização ou outros mecanismos para evitar a criação de URIs (como para chamadas de API) ou campos de cabeçalho de requisição HTTP (como Authorization ou Cookie) que sejam longos demais para serem aceitos pelo componente receptor. Isso poderia causar uma negação de serviço, como ao enviar uma requisição excessivamente longa (ex., um campo de cabeçalho de cookie longo), resultando no servidor sempre respondendo com um status de erro. | 3 |

## V4.3 GraphQL

O GraphQL está se tornando mais comum como uma forma de criar clientes ricos em dados que não são fortemente acoplados a uma variedade de serviços de backend. Esta seção aborda as considerações de segurança para o GraphQL.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **4.3.1** | Verifique se uma lista de permissões (allowlist) de consultas, limitação de profundidade, limitação de quantidade ou análise de custo de consulta é usada para evitar Negação de Serviço (DoS) de expressão na camada de dados ou GraphQL como resultado de consultas aninhadas e custosas. | 2 |
| **4.3.2** | Verifique se as consultas de introspecção do GraphQL estão desabilitadas no ambiente de produção, a menos que a API do GraphQL seja destinada a ser usada por terceiros. | 2 |

## V4.4 WebSocket

O WebSocket é um protocolo de comunicações que fornece um canal de comunicação bidirecional simultâneo em uma única conexão TCP. Ele foi padronizado pela IETF como RFC 6455 em 2011 e é distinto do HTTP, embora seja projetado para funcionar nas portas HTTP 443 e 80.

Esta seção fornece os principais requisitos de segurança para prevenir ataques relacionados à segurança da comunicação e ao gerenciamento de sessão que exploram especificamente esse canal de comunicação em tempo real.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **4.4.1** | Verifique se o WebSocket over TLS (WSS) é usado para todas as conexões WebSocket. | 1 |
| **4.4.2** | Verifique se, durante o handshake inicial do WebSocket HTTP, o campo de cabeçalho Origin é verificado em relação a uma lista de origens permitidas para a aplicação. | 2 |
| **4.4.3** | Verifique se, caso o gerenciamento de sessão padrão da aplicação não possa ser usado, tokens dedicados estão sendo usados para isso, os quais cumprem os requisitos de segurança relevantes de Gerenciamento de Sessão. | 2 |
| **4.4.4** | Verifique se os tokens dedicados de gerenciamento de sessão do WebSocket são inicialmente obtidos ou validados por meio da sessão HTTPS previamente autenticada ao fazer a transição de uma sessão HTTPS existente para um canal WebSocket. | 2 |

## Referências

Para mais informações, veja também:

* [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
* Recursos sobre Autorização GraphQL em [graphql.org](https://graphql.org/learn/authorization/) e [Apollo](https://www.apollographql.com/docs/apollo-server/security/authentication/#authorization-methods).
* [OWASP Web Security Testing Guide: GraphQL Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL)
* [OWASP Web Security Testing Guide: Testing WebSockets](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets)
