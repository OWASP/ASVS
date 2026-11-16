# V15 Codificação e Arquitetura Seguras

## Objetivo de Controle

Muitos requisitos do ASVS se relacionam a uma área particular da segurança, como autenticação ou autorização, ou dizem respeito a um tipo particular de funcionalidade de aplicação, como o registro (logging) ou manipulação de arquivos.

Este capítulo fornece requisitos gerais de segurança a serem considerados ao projetar e desenvolver aplicações. Esses requisitos não focam apenas na arquitetura limpa (clean architecture) e qualidade de código, mas também em práticas de arquitetura e codificação específicas necessárias para a segurança da aplicação.

## V15.1 Documentação de Codificação e Arquitetura Seguras

Muitos requisitos para o estabelecimento de uma arquitetura segura e defensável dependem da documentação clara de decisões feitas a respeito da implementação de controles de segurança específicos e os componentes usados dentro da aplicação.

Esta seção descreve os requisitos de documentação, incluindo a identificação de componentes que se considera conter "funcionalidade perigosa" ou ser um "componente de risco".

Um componente com "funcionalidade perigosa" (dangerous functionality) pode ser um componente desenvolvido internamente ou de terceiros que realiza operações como desserialização de dados não confiáveis, parsing de arquivos raw ou de dados binários, execução dinâmica de código ou manipulação direta de memória. As vulnerabilidades nesses tipos de operações apresentam alto risco de comprometer a aplicação e, potencialmente, de expor a infraestrutura subjacente.

Um "componente de risco" (risky component) é uma biblioteca de terceiros (ou seja, não desenvolvida internamente) em que faltam controles de segurança, ou eles estão mal implementados, em torno de seus processos de desenvolvimento ou de sua funcionalidade. Exemplos incluem componentes com manutenção deficiente, sem suporte, em estágio de fim de vida útil (end-of-life) ou com histórico de vulnerabilidades significativas.

Esta seção também enfatiza a importância de se definir prazos de tempo apropriados para lidar com vulnerabilidades em componentes terceiros.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **15.1.1** | Verifique se a documentação da aplicação define prazos de correção baseados em risco para as versões de componentes de terceiros com vulnerabilidades e para a atualização de bibliotecas em geral, a fim de minimizar o risco proveniente desses componentes. | 1 |
| **15.1.2** | Verifique se um catálogo de inventário, como uma lista de materiais de software (Software Bill of Materials - SBOM), é mantido para todas as bibliotecas de terceiros em uso, incluindo a verificação de que os componentes vêm de repositórios predefinidos, confiáveis e continuamente mantidos. | 2 |
| **15.1.3** | Verifique se a documentação da aplicação identifica funcionalidades que consomem muito tempo ou exigem muitos recursos. Isso deve incluir como evitar a perda de disponibilidade devido ao uso excessivo dessa funcionalidade e como evitar uma situação em que a construção de uma resposta leve mais tempo do que o timeout do consumidor. As defesas possíveis podem incluir processamento assíncrono, uso de filas e limitação de processos paralelos por usuário e por aplicação. | 2 |
| **15.1.4** | Verifique se a documentação da aplicação destaca as bibliotecas de terceiros consideradas "componentes de risco" (risky components). | 3 |
| **15.1.5** | Verifique se a documentação da aplicação destaca as partes da aplicação em que "funcionalidade perigosa" (dangerous functionality) é utilizada. | 3 |

## V15.2 Arquitetura de Segurança e Dependências

Esta seção inclui requisitos para lidar com dependências e componentes arriscados, desatualizados ou inseguros por meio do gerenciamento de dependências (dependency management).

Também inclui o uso de técnicas em nível de arquitetura, como sandboxing, encapsulamento, conteinerização e isolamento de rede, para reduzir o impacto do uso de "operações perigosas" (dangerous operations) ou de "componentes de risco" (conforme definidos na seção anterior) e prevenir a perda de disponibilidade causada pelo uso excessivo de funcionalidades que demandam muitos recursos.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **15.2.1** | Verifique se a aplicação contém apenas componentes que não ultrapassaram os prazos documentados de atualização e correção. | 1 |
| **15.2.2** | Verifique se a aplicação implementou defesas contra a perda de disponibilidade causada por funcionalidades que consomem muito tempo ou exigem muitos recursos, com base nas decisões e estratégias de segurança documentadas para isso. | 2 |
| **15.2.3** | Verifique se o ambiente de produção inclui apenas as funcionalidades necessárias para o funcionamento da aplicação e não expõe funcionalidades estranhas (extraneous functionality), como código de teste, trechos de exemplo (sample snippets) e funcionalidades de desenvolvimento. | 2 |
| **15.2.4** | Verifique se os componentes de terceiros e todas as suas dependências transitivas são incluídos a partir do repositório esperado, seja de propriedade interna ou uma fonte externa, e se não há risco de um ataque de confusão de dependência (dependency confusion). | 3 |
| **15.2.5** | Verifique se a aplicação implementa proteções adicionais em torno das partes da aplicação documentadas como contendo "funcionalidade perigosa" ou que utilizam bibliotecas de terceiros consideradas "componentes de risco". Isso pode incluir técnicas como sandboxing, encapsulamento, conteinerização ou isolamento em nível de rede, para retardar e dificultar a ação de atacantes que comprometam uma parte da aplicação e tentem pivotar para outras partes dela. | 3 |

## V15.3 Codificação Defensiva

Esta seção cobre tipos de vulnerabilidades, incluindo type juggling, prototype pollution e outras, que resultam do uso de padrões de codificação inseguros em uma linguagem específica. Algumas podem não ser relevantes para todas as linguagens, enquanto outras terão correções específicas por linguagem ou podem estar relacionadas à forma como uma determinada linguagem ou framework lida com um recurso, como os parâmetros HTTP. Também considera o risco de não validar criptograficamente as atualizações da aplicação.

Também considera os riscos associados ao uso de objetos para representar itens de dados e ao aceitar e retornar esses itens por meio de APIs externas. Nesse caso, a aplicação deve garantir que os campos de dados que não devem ser graváveis (writable) não sejam modificados por entrada do usuário (mass assignment) e que a API seja seletiva quanto aos campos de dados que são retornados. Quando o acesso a um campo depende das permissões do usuário, isso deve ser considerado no contexto do requisito de controle de acesso em nível de campo do capítulo Autorização.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **15.3.1** | Verifique se a aplicação retorna apenas o subconjunto necessário de campos de um objeto de dados. Por exemplo, ela não deve retornar um objeto de dados inteiro, pois alguns campos individuais não devem estar acessíveis aos usuários. | 1 |
| **15.3.2** | Verifique se, nos casos em que o backend da aplicação faz chamadas a URLs externas, ele esteja configurado para não seguir redirecionamentos, a menos que isso seja uma funcionalidade intencional. | 2 |
| **15.3.3** | Verifique se a aplicação possui contramedidas para se proteger contra ataques de atribuição em massa (mass assignment) limitando os campos permitidos por controlador (controller) e ação, por ex., não é possível inserir ou atualizar o valor de um campo quando isso não foi projetado para fazer parte daquela ação. | 2 |
| **15.3.4** | Verifique se todos os componentes de proxy e middleware transferem o endereço IP original do usuário corretamente usando campos de dados confiáveis que não possam ser manipulados pelo usuário final, e a aplicação e o servidor web usam este valor correto para decisões de logging e de segurança como limitação de taxa (rate limiting), levando em conta que mesmo o endereço IP original pode não ser confiável devido a IPs dinâmicos, VPNs ou firewalls corporativos. | 2 |
| **15.3.5** | Verifique se a aplicação garante explicitamente que as variáveis são do tipo correto e realiza operações de comparação e de igualdade estritas (strict equality and comparator operations). Isso é para evitar vulnerabilidades de confusão de tipos (type confusion) ou type juggling causadas pelo código da aplicação fazer uma suposição sobre um tipo de variável. | 2 |
| **15.3.6** | Verifique se o código JavaScript é escrito de uma forma que evita a poluição de protótipo (prototype pollution), por exemplo, usando Set() ou Map() em vez de objetos literais. | 2 |
| **15.3.7** | Verifique se a aplicação possui defesas contra ataques de poluição de parâmetros HTTP (HTTP parameter pollution attacks), particularmente se o framework da aplicação não faz distinção sobre a fonte (source) dos parâmetros de requisição (query string, body parameters, cookies ou campos de cabeçalho). | 2 |

## V15.4 Concorrência Segura

Problemas de concorrência (concurrency) tais como as condições de corrida (race conditions), vulnerabilidades do tipo de tempo-de-verificação-para-o-tempo-de-uso (time-of-check to time-of-use - TOCTOU), deadlocks (bloqueios), livelocks, thread starvation e sincronização inadequada podem levar a comportamento imprevisível e riscos de segurança. Esta seção inclui várias técnicas e estratégias para ajudar a mitigar esses riscos.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **15.4.1** | Verifique se objetos compartilhados em códigos multi-thread (como caches, arquivos ou objetos na memória acessados por várias threads) são acessados ​​de forma segura usando tipos thread-safe e mecanismos de sincronização como locks (travas) ou semáforos para evitar condições de corrida e corrupção de dados. | 3 |
| **15.4.2** | Verifique se as checagens no estado de um recurso, como sua existência ou permissões, e as ações que dependem delas são executadas como uma operação atômica única para evitar as condições de corrida do tipo time-of-check to time-of-use (TOCTOU). Por exemplo, checando se um arquivo existe antes de abri-lo, ou verificando o acesso de um usuário antes de concedê-lo. | 3 |
| **15.4.3** | Verifique se bloqueios (locks) são usados ​​consistentemente para evitar que as threads fiquem presas, seja esperando umas pelas outras ou tentando novamente (retrying) sem parar, e se a lógica de travamento permanece dentro do código responsável por gerenciar o recurso para garantir que os bloqueios não possam ser modificados inadvertidamente ou maliciosamente por classes ou código externo. | 3 |
| **15.4.4** | Verifique se as políticas de alocação de recursos previnem o thread starvation ao garantir o acesso justo (fair access) aos recursos, como, por exemplo, pelo aproveitamento de pools de threads, permitindo que as threads de menor prioridade procedam dentro de um tempo razoável. | 3 |

## Referências

Para mais informações, veja também:

* [OWASP Prototype Pollution Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html)
* [OWASP Mass Assignment Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
* [OWASP CycloneDX Bill of Materials Specification](https://owasp.org/www-project-cyclonedx/)
* [OWASP Web Security Testing Guide: Testing for HTTP Parameter Pollution](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution)