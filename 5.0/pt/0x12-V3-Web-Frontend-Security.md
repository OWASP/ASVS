# V3 Segurança de Frontend Web

## Objetivo de Controle

Esta categoria concentra-se em requisitos projetados para proteger contra ataques executados via um frontend web. Estes requisitos não se aplicam a soluções máquina a máquina (machine-to-machine).

## V3.1 Documentação de Segurança de Frontend Web

Esta seção descreve os recursos de segurança do navegador que devem ser especificados na documentação da aplicação.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **3.1.1** | Verifique se a documentação da aplicação declara os recursos de segurança esperados que os navegadores que usam a aplicação devem suportar (como HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP) e outros mecanismos de segurança HTTP relevantes). Deve também definir como a aplicação deve se comportar quando alguns desses recursos não estiverem disponíveis (como avisar o usuário ou bloquear o acesso). | 3 |

## V3.2 Interpretação Não Intencional de Conteúdo

Renderizar conteúdo ou funcionalidade em um contexto incorreto pode resultar na execução ou exibição de conteúdo malicioso.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **3.2.1** | Verifique se há controles de segurança em vigor para evitar que navegadores renderizem conteúdo ou funcionalidades de respostas HTTP em um contexto incorreto (por exemplo, quando uma API, um arquivo enviado pelo usuário ou outro recurso é solicitado diretamente). Possíveis controles poderiam incluir: não servir o conteúdo a menos que campos de cabeçalho da requisição HTTP (como Sec-Fetch-\*) indiquem que é o contexto correto, usar a diretiva sandbox do campo de cabeçalho Content-Security-Policy ou usar o tipo de disposição attachment no campo de cabeçalho Content-Disposition. | 1 |
| **3.2.2** | Verifique se o conteúdo que deve ser exibido como texto, e não renderizado como HTML, é processado usando funções de renderização seguras (como createTextNode ou textContent) para evitar a execução não intencional de conteúdo como HTML ou JavaScript. | 1 |
| **3.2.3** | Verifique se a aplicação evita a sobrescrita do DOM (DOM clobbering) ao usar JavaScript no lado do cliente (client-side), empregando declarações explícitas de variáveis, realizando verificação estrita de tipo, evitando armazenar variáveis globais no objeto document e implementando isolamento de namespace. | 3 |

## V3.3 Configuração de Cookies

Esta seção descreve os requisitos para configurar cookies sensíveis com segurança, a fim de fornecer um maior nível de garantia de que foram criados pela própria aplicação e para evitar que seus conteúdos vazem ou sejam modificados inadequadamente.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **3.3.1** | Verifique se os cookies possuem o atributo 'Secure' definido, e caso o prefixo '\__Host-' não seja usado no nome do cookie, o prefixo '__Secure-' deve ser usado para o nome do cookie. | 1 |
| **3.3.2** | Verifique se o valor do atributo 'SameSite' de cada cookie é configurado de acordo com o propósito do cookie, para limitar a exposição a ataques de distorção de interface de usuário (user interface redress) e ataques de falsificação de requisição baseados em navegador, comumente conhecidos como falsificação de requisição entre sites (Cross-Site Request Forgery - CSRF). | 2 |
| **3.3.3** | Verifique se os cookies possuem o prefixo '__Host-' para o nome do cookie, a menos que sejam explicitamente projetados para serem compartilhados com outros hosts. | 2 |
| **3.3.4** | Verifique se o valor de um cookie não deve ser acessível a scripts do lado do cliente (como um token de sessão), o cookie deve ter o atributo 'HttpOnly' definido e o mesmo valor (ex. token de sessão) deve ser transferido ao cliente apenas através do campo de cabeçalho 'Set-Cookie'. | 2 |
| **3.3.5** | Verifique se quando a aplicação grava um cookie, o comprimento combinado do nome e do valor do cookie não ultrapassa 4096 bytes. Cookies excessivamente grandes não serão armazenados pelo navegador e, portanto, não serão enviados com requisições, impedindo o usuário de utilizar as funcionalidades da aplicação que dependem desse cookie. | 3 |

## V3.4 Cabeçalhos de Mecanismos de Segurança do Navegador

Esta seção descreve quais cabeçalhos de segurança devem ser definidos nas respostas HTTP para habilitar os recursos e as restrições de segurança do navegador ao processar as respostas da aplicação.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **3.4.1** | Verifique se o campo de cabeçalho Strict-Transport-Security está incluído em todas as respostas para forçar uma política HTTP Strict Transport Security (HSTS). A validade máxima (maximum age) de pelo menos 1 ano deve ser definida e, para L2 e superior, a política também deve se aplicar a todos os subdomínios. | 1 |
| **3.4.2** | Verifique se o campo de cabeçalho Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin possui um valor fixo atribuído pela aplicação ou, se o valor do campo de cabeçalho Origin da requisição HTTP for usado, ele é validado com base em uma lista de permissões (allowlist) de origens confiáveis. Quando 'Access-Control-Allow-Origin: *' precisar ser usado, verifique se a resposta não inclui informações sensíveis. | 1 |
| **3.4.3** | Verifique se as respostas HTTP incluem um campo de cabeçalho de resposta Content-Security-Policy que define diretivas para garantir que o navegador apenas carregue e execute conteúdos ou recursos confiáveis, a fim de limitar a execução de JavaScript malicioso. Como mínimo, uma política global deve ser usada, a qual inclui as diretivas object-src 'none' e base-uri 'none', e define uma lista de permissões ou usa nonces ou hashes. Para uma aplicação L3, deve ser definida uma política por resposta com nonces ou hashes. | 2 |
| **3.4.4** | Verifique se todas as respostas HTTP contêm um campo de cabeçalho 'X-Content-Type-Options: nosniff'. Isso instrui os navegadores a não utilizarem a adivinhação do tipo MIME (content sniffing) para a resposta dada, e exige que o valor do campo de cabeçalho Content-Type da resposta corresponda ao recurso de destino. Por exemplo, a resposta para a requisição de um estilo só é aceita se o Content-Type da resposta for 'text/css'. Isso também permite o uso da funcionalidade Cross-Origin Read Blocking (CORB) pelo navegador. | 2 |
| **3.4.5** | Verifique se a aplicação define uma política de referência (referrer policy) para evitar o vazamento de dados tecnicamente sensíveis para serviços de terceiros através do campo de cabeçalho HTTP da requisição 'Referer'. Isso pode ser feito usando o campo de cabeçalho de resposta HTTP Referrer-Policy ou por meio de atributos de elemento HTML. Dados sensíveis podem incluir caminho e dados de consulta na URL e, para aplicações internas não públicas, o nome do host (hostname) também. | 2 |
| **3.4.6** | Verifique se a aplicação web usa a diretiva frame-ancestors do campo de cabeçalho Content-Security-Policy para toda resposta HTTP para garantir que ela não possa ser incorporada (embedded) por padrão, e que a incorporação de recursos específicos seja permitida apenas quando necessário. Note que o campo de cabeçalho X-Frame-Options, embora suportado por navegadores, está obsoleto e não deve ser confiado. | 2 |
| **3.4.7** | Verifique se o campo de cabeçalho Content-Security-Policy especifica um local para relatar violações. | 3 |
| **3.4.8** | Verifique se todas as respostas HTTP que iniciam a renderização de um documento (como respostas com Content-Type text/html) incluem o campo de cabeçalho Cross‑Origin‑Opener‑Policy com a diretiva same-origin ou a diretiva same-origin-allow-popups, conforme exigido. Isso evita ataques que abusam do acesso compartilhado a objetos Window, como tabnabbing e contagem de frames (frame counting). | 3 |

## V3.5 Separação de Origem no Navegador

Ao aceitar uma solicitação de funcionalidade sensível no lado do servidor, a aplicação precisa garantir que a solicitação seja iniciada pela própria aplicação ou por uma parte confiável e não tenha sido forjada por um atacante.

Funcionalidades sensíveis neste contexto podem incluir o recebimento de posts de formulários para usuários autenticados e não autenticados (como uma solicitação de autenticação), operações que mudam o estado (state-changing) ou funcionalidades que demandam recursos (como exportação de dados).

As principais proteções aqui são as políticas de segurança do navegador, como a Same Origin Policy (Política de Mesma Origem) para JavaScript e também a lógica do SameSite para cookies. Outra proteção comum é o mecanismo de CORS preflight. Esse mecanismo será fundamental para os endpoints projetados para serem chamados de uma origem diferente, mas também pode ser um mecanismo útil de prevenção contra falsificação de solicitações para endpoints que não foram projetados para serem chamados de uma origem diferente.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **3.5.1** | Verifique se, caso a aplicação não dependa do mecanismo de CORS preflight para impedir que requisições cross-origin não permitidas usem funcionalidades sensíveis, essas requisições sejam validadas para garantir que sejam originadas na própria aplicação. Isso pode ser feito usando e validando tokens antifalsificação ou exigindo campos de cabeçalho HTTP adicionais que não sejam campos de cabeçalho listados como seguros (CORS-safelisted). O objetivo é defender contra ataques de falsificação de solicitações baseadas no navegador, conhecidos como falsificação de solicitação entre sites (Cross-Site Request Forgery - CSRF). | 1 |
| **3.5.2** | Verifique se, caso a aplicação dependa do mecanismo de CORS preflight para evitar o uso cross-origin não permitido de funcionalidades sensíveis, não seja possível chamar a funcionalidade com uma solicitação que não acione uma requisição de CORS-preflight. Isso pode exigir a verificação dos valores dos campos de cabeçalho de requisição 'Origin' e 'Content-Type' ou o uso de um campo de cabeçalho extra que não seja CORS-safelisted. | 1 |
| **3.5.3** | Verifique se as solicitações HTTP a funcionalidades sensíveis usam métodos HTTP apropriados como POST, PUT, PATCH ou DELETE, e não métodos definidos pela especificação HTTP como "seguros" (safe), como HEAD, OPTIONS ou GET. Alternativamente, uma validação estrita dos campos de cabeçalho de requisição Sec-Fetch-* pode ser usada para garantir que a solicitação não tenha se originado de uma chamada cross-origin inadequada, de uma solicitação de navegação ou do carregamento de um recurso (como fonte de imagem) onde isso não é esperado. | 1 |
| **3.5.4** | Verifique se as aplicações distintas estão hospedadas em hostnames diferentes para aproveitar as restrições fornecidas pela política de mesma origem (same-origin policy), incluindo a forma como os documentos ou scripts carregados por uma origem podem interagir com os recursos de outra origem e as restrições baseadas no hostname dos cookies. | 2 |
| **3.5.5** | Verifique se as mensagens recebidas pela interface postMessage são descartadas caso a origem da mensagem não seja confiável, ou se a sintaxe da mensagem for inválida. | 2 |
| **3.5.6** | Verifique se a funcionalidade JSONP não está habilitada em nenhuma parte da aplicação para evitar ataques de Inclusão de Script Entre Sites (Cross-Site Script Inclusion - XSSI). | 3 |
| **3.5.7** | Verifique se os dados que requerem autorização não estão incluídos em respostas de recursos de script, como arquivos JavaScript, para evitar ataques de Inclusão de Script Entre Sites (Cross-Site Script Inclusion - XSSI). | 3 |
| **3.5.8** | Verifique se os recursos autenticados (como imagens, vídeos, scripts e outros documentos) podem ser carregados ou incorporados (embedded) em nome do usuário apenas quando pretendido. Isso pode ser alcançado através da validação estrita dos campos de cabeçalho de requisição HTTP Sec-Fetch-* para garantir que a requisição não se originou de uma chamada cross-origin inapropriada, ou através da definição de um campo de cabeçalho restritivo de resposta HTTP Cross-Origin-Resource-Policy para instruir o navegador a bloquear o conteúdo retornado. | 3 |

## V3.6 Integridade de Recursos Externos

Esta seção fornece orientações para a hospedagem segura de conteúdo em sites de terceiros.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **3.6.1** | Verifique se ativos do lado do cliente (client-side assets), como bibliotecas JavaScript, CSS ou fontes da web (web fonts), são hospedados externamente (ex., em uma Content Delivery Network - CDN) apenas se o recurso for estático e versionado, e se a Integridade de Sub-recurso (Subresource Integrity - SRI) for usada para validar a integridade do ativo. Se isso não for possível, deve haver uma decisão de segurança documentada para justificar isso para cada recurso. | 3 |

## V3.7 Outras Considerações de Segurança do Navegador

Esta seção inclui vários outros controles de segurança e recursos de segurança de navegadores modernos exigidos para a segurança do navegador do lado do cliente (client-side).

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **3.7.1** | Verifique se a aplicação usa apenas tecnologias do lado do cliente (client-side) que ainda são suportadas e consideradas seguras. Exemplos de tecnologias que não atendem a este requisito incluem plug-ins NSAPI, Flash, Shockwave, ActiveX, Silverlight, NACL ou miniaplicativos (applets) Java do lado do cliente. | 2 |
| **3.7.2** | Verifique se a aplicação redirecionará automaticamente o usuário para um hostname ou domínio diferente (que não seja controlado pela aplicação) apenas se o destino constar em uma lista de permissões (allowlist). | 2 |
| **3.7.3** | Verifique se a aplicação exibe uma notificação quando o usuário está sendo redirecionado para um URL fora do controle da aplicação, com a opção de cancelar a navegação. | 3 |
| **3.7.4** | Verifique se o domínio de nível superior da aplicação (ex., site.tld) é adicionado à lista pública de pré-carregamento (preload list) para o HTTP Strict Transport Security (HSTS). Isso garante que o uso de TLS para a aplicação seja integrado diretamente aos principais navegadores, em vez de depender apenas do campo de cabeçalho de resposta Strict-Transport-Security. | 3 |
| **3.7.5** | Verifique se a aplicação se comporta conforme o documentado (como avisar o usuário ou bloquear o acesso) caso o navegador usado para acessar a aplicação não suporte os recursos de segurança esperados. | 3 |

## Referências

Para mais informações, veja também:

* [Set-Cookie __Host- prefix details](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes)
* [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
* [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [HSTS Browser Preload List submission form](https://hstspreload.org/)
* [OWASP DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)