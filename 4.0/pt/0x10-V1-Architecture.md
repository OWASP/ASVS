# V1 Arquitetura, Design e Modelagem de Ameaças

## Objetivo de controle

A arquitetura de segurança quase se tornou uma arte perdida em muitas organizações. Os dias do arquiteto corporativo já passaram na era do DevSecOps. O campo de segurança de aplicações deve acompanhar e adotar princípios de segurança ágeis enquanto reintroduz os principais princípios de arquitetura de segurança para profissionais de software. A arquitetura não é uma implementação, mas uma maneira de pensar sobre um problema que tem potencialmente muitas respostas diferentes e nenhuma resposta "correta". Com muita frequência, a segurança é vista como inflexível e exigindo que os desenvolvedores corrijam o código de uma maneira específica, quando os desenvolvedores podem conhecer uma maneira muito melhor de resolver o problema. Não existe uma solução única e simples para a arquitetura, e fingir o contrário é um desserviço ao campo da engenharia de software.

É provável que uma implementação específica de uma aplicação da Web seja revisada continuamente ao longo da sua vida útil. A arquitetura geral raramente mudará, mas evoluirá lentamente. A arquitetura de segurança é idêntica - precisamos de autenticação hoje, exigiremos autenticação amanhã e precisaremos dela daqui a cinco anos. Se tomarmos decisões sensatas hoje, podemos economizar muito esforço, tempo e dinheiro se selecionarmos e reutilizarmos soluções compatíveis com a arquitetura. Por exemplo, uma década atrás, a autenticação multifator era raramente implementada.

Se os desenvolvedores tivessem investido num modelo único e seguro de provedor de identidade, como a identidade federada SAML, o provedor de identidade poderia ser atualizado para incorporar novos requisitos, como conformidade com NIST 800-63, sem alterar as interfaces da aplicação original. Se muitas aplicações compartilharem a mesma arquitetura de segurança e, assim, o mesmo componente, todos se beneficiarão dessa atualização de uma só vez. No entanto, o SAML nem sempre permanecerá como a melhor ou mais adequada solução de autenticação - pode ser necessário trocá-lo por outras soluções à medida que os requisitos mudam. Mudanças como essa são complicadas, tão caras que exigem uma reescrita completa ou totalmente impossíveis sem arquitetura de segurança.

Neste capítulo, o ASVS cobre os aspectos primários de qualquer arquitetura de segurança sólida: disponibilidade, confidencialidade, integridade de processamento, não repúdio e privacidade. Cada um desses princípios de segurança deve ser integrado e inato a todos os aplicativos. É fundamental "mudar para a esquerda", começando com a capacitação do desenvolvedor com listas de verificação de codificação segura, orientação e treinamento, codificação e teste, construção, implantação, configuração e operações e terminando com testes independentes de acompanhamento para garantir que todos os controles de segurança estão presentes e funcionais. A última etapa costumava ser tudo o que fazíamos como indústria, mas isso não é mais suficiente quando os desenvolvedores colocam o código em produção dezenas ou centenas de vezes por dia. Os profissionais de segurança de aplicativos devem acompanhar as técnicas ágeis, o que significa adotar ferramentas de desenvolvedor, aprender a codificar e trabalhar com desenvolvedores, em vez de criticar o projeto meses depois que todos os outros já partiram.

## V1.1 Ciclo de vida de desenvolvimento de software seguro

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.1.1** | Verifique o uso de um ciclo de vida de desenvolvimento de software seguro que aborde a segurança em todos os estágios de desenvolvimento. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **1.1.2** | Verifique o uso da modelagem de ameaças para cada alteração de design ou planejamento de sprint para identificar ameaças, planejar contramedidas, facilitar respostas apropriadas a riscos e orientar testes de segurança. | | ✓ | ✓ | 1053 |
| **1.1.3** | Verifique se todas as histórias e recursos do usuário contêm restrições de segurança funcionais, como "Como usuário, devo poder visualizar e editar meu perfil. Não devo visualizar ou editar o perfil de outra pessoa" | | ✓ | ✓ | 1110 |
| **1.1.4** | Verifique a documentação e justificativa de todos os limites de confiança, componentes e fluxos de dados significativos da aplicação. | | ✓ | ✓ | 1059 |
| **1.1.5** | Verifique a definição e a análise de segurança da arquitetura de alto nível da aplicação e de todos os serviços remotos conectados. ([C1](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1059 |
| **1.1.6** | Verifique a implementação de controles de segurança centralizados, simples (economia de design), verificados, seguros e reutilizáveis para evitar controles duplicados, ausentes, ineficazes ou inseguros. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 637 |
| **1.1.7** | Verifique a disponibilidade de uma lista de verificação de codificação segura, requisitos de segurança, diretriz ou política para todos os desenvolvedores e testadores. | | ✓ | ✓ | 637 |

## V1.2 Arquitetura de autenticação

Ao projetar a autenticação, não importa se você tem autenticação multifator habilitada para hardware forte se um invasor puder redefinir uma conta ligando para um call center e respondendo a perguntas comumente conhecidas. Ao provar a identidade, todos os caminhos de autenticação devem ter a mesma força.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.2.1** | Verifique o uso de contas exclusivas ou especiais de sistema operacional de baixo privilégio para todos os componentes de aplicações, serviços e servidores. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 250 |
| **1.2.2** | Verifique se as comunicações entre os componentes da aplicação, incluindo APIs, middleware e camadas de dados, são autenticadas. Os componentes devem ter os privilégios mínimos necessários. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 306 |
| **1.2.3** | Verifique se a aplicação usa um único mecanismo de autenticação verificado que é conhecido por ser seguro, pode ser estendido para incluir autenticação forte e tem registro e monitoramento suficientes para detectar abuso ou violações de conta. | | ✓ | ✓ | 306 |
| **1.2.4** | Verifique se todos os caminhos de autenticação e APIs de gestão de identidade implementam força de controle de segurança de autenticação consistente, de modo que não haja alternativas mais fracas pelo risco da aplicação. | | ✓ | ✓ | 306 |

## V1.3 Arquitetura de gestão de sessão

Este é um espaço reservado para futuros requisitos de arquitetura.

## V1.4 Arquitetura de controle de acesso

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.4.1** | Verifique se os pontos de imposição confiáveis, como gateways de controle de acesso, servidores e funções serverless, reforçam os controles de acesso. Nunca imponha controles de acesso no cliente. | | ✓ | ✓ | 602 |
| **1.4.2** | [EXCLUÍDO, NÃO ACIONÁVEL] | | | | |
| **1.4.3** | [EXCLUÍDO, DUPLICADO DE 4.1.3] | | | | |
| **1.4.4** | Verifique se a aplicação usa um mecanismo de controle de acesso único e bem testado para acessar dados e recursos protegidos. Todas as solicitações devem passar por esse mecanismo único para evitar copiar e colar ou caminhos alternativos inseguros. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 284 |
| **1.4.5** | Verifique se o controle de acesso baseado em atributo ou recurso é usado pelo qual o código verifica a autorização do usuário para um item de recurso/dado em vez de apenas sua função. As permissões ainda devem ser alocadas usando funções. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 275 |

## V1.5 Arquitetura de input e output

Na versão 4.0, deixamos de usar o termo "lado do servidor" como um termo de limite de confiança carregado. O limite de confiança ainda é preocupante - é possível ignorar a tomada de decisões em navegadores ou dispositivos clientes não confiáveis. No entanto, nas implantações arquitetônicas convencionais de hoje, o ponto de imposição de confiança mudou drasticamente. Portanto, onde o termo "camada de serviço confiável" é usado no ASVS, queremos dizer qualquer ponto de aplicação confiável, independentemente da localização, como um microsserviço, API serverless, lado do servidor, uma API confiável num dispositivo cliente com inicialização segura, parceiro ou APIs externas e assim por diante.

O termo "cliente não confiável" aqui refere-se a tecnologias do lado do cliente que renderizam a camada de apresentação, geralmente chamadas tecnologias de 'front-end'. O termo "serialização" aqui não se refere apenas ao envio de dados pela rede como uma matriz de valores ou à obtenção e leitura de uma estrutura JSON, mas também à passagem de objetos complexos que podem conter lógica.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.5.1** | Verifique se os requisitos de input e output definem claramente como lidar e processar dados com base no tipo, conteúdo e leis aplicáveis, regulamentos e outras conformidades com políticas. | | ✓ | ✓ | 1029 |
| **1.5.2** | Verifique se a serialização não é usada ao se comunicar com clientes não confiáveis. Se isso não for possível, certifique-se de que os controles de integridade adequados (e possivelmente a criptografia se dados confidenciais forem enviados) sejam aplicados para evitar ataques de desserialização, incluindo injeção de objeto. | | ✓ | ✓ | 502 |
| **1.5.3** | Verifique se a validação de input é aplicada numa camada de serviço confiável. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 602 |
| **1.5.4** | Verifique se a codificação de output ocorre perto ou pelo interpretador para o qual se destina. ([C4](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 116 |

## V1.6 Arquitetura Criptográfica

Aplicações precisam ser projetados com arquitetura criptográfica forte para proteger os ativos de dados conforme a sua classificação. Criptografar tudo é um desperdício, não criptografar nada é legalmente negligente. Um equilíbrio deve ser alcançado, geralmente durante o projeto arquitetônico ou de alto nível, sprints de design ou picos arquitetônicos. Projetar a criptografia à medida que avança ou adaptá-la inevitavelmente custará muito mais para implementar com segurança do que simplesmente incorporá-la desde o início.

Os requisitos de arquitetura são intrínsecos a toda a base de código e, assim, difíceis de unidade ou teste integrado. Os requisitos de arquitetura exigem consideração nos padrões de codificação, durante a fase de codificação, e devem ser revisados durante a arquitetura de segurança, revisões de código ou pares, ou retrospectivas.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.6.1** | Verifique se há uma política explícita para gestão de chaves criptográficas e se o ciclo de vida de uma chave criptográfica segue um padrão de gestão de chaves, como NIST SP 800-57. | | ✓ | ✓ | 320 |
| **1.6.2** | Verifique se os consumidores de serviços criptográficos protegem o material de chaves e outros segredos usando cofres de chaves ou alternativas baseadas em API. | | ✓ | ✓ | 320 |
| **1.6.3** | Verifique se todas as chaves e senhas são substituíveis e fazem parte de um processo bem definido para criptografar novamente dados confidenciais. | | ✓ | ✓ | 320 |
| **1.6.4** | Verifique se a arquitetura trata os segredos do lado do cliente, como chaves simétricas, senhas ou tokens de API, como inseguros e nunca os usa para proteger ou acessar dados confidenciais. | | ✓ | ✓ | 320 |

## V1.7 Erros, registro e arquitetura de auditoria

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.7.1** | Verifique se um formato e uma abordagem de log comuns são usados em todo o sistema. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 1009 |
| **1.7.2** | Verifique se os logs são transmitidos com segurança para um sistema preferencialmente remoto para análise, detecção, alerta e escalonamento. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

## V1.8 Proteção de Dados e Arquitetura de Privacidade

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.8.1** | Verifique se todos os dados confidenciais são identificados e classificados em níveis de proteção. | | ✓ | ✓ | |
| **1.8.2** | Verifique se todos os níveis de proteção têm um conjunto associado de requisitos de proteção, como requisitos de criptografia, requisitos de integridade, retenção, privacidade e outros requisitos de confidencialidade, e se eles são aplicados na arquitetura. | | ✓ | ✓ | |

## V1.9 Arquitetura de Comunicações

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.9.1** | Verifique se a aplicação criptografa as comunicações entre os componentes, especialmente quando esses componentes estão em contêineres, sistemas, sites ou provedores de nuvem diferentes. ([C3](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 319 |
| **1.9.2** | Verifique se os componentes da aplicação verificam a autenticidade de cada lado num link de comunicação para evitar ataques de pessoa no meio. Por exemplo, os componentes da aplicação devem validar cadeias e certificados TLS. | | ✓ | ✓ | 295 |

## V1.10 Arquitetura de software malicioso

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.10.1** | Verifique se um sistema de controle de código-fonte está em uso, com procedimentos para garantir que os check-ins sejam acompanhados de problemas ou tickets de alteração. O sistema de controle de código-fonte deve ter controle de acesso e usuários identificáveis para permitir a rastreabilidade de quaisquer alterações. | | ✓ | ✓ | 284 |

## V1.11 Arquitetura de lógica de negócios

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.11.1** | Verifique a definição e a documentação de todos os componentes da aplicação em termos de negócios ou funções de segurança que eles fornecem. | | ✓ | ✓ | 1059 |
| **1.11.2** | Verifique se todos os fluxos de lógica de negócios de alto valor, incluindo autenticação, gestão de sessão e controle de acesso, não compartilham estado não sincronizado. | | ✓ | ✓ | 362 |
| **1.11.3** | Verifique se todos os fluxos de lógica de negócios de alto valor, incluindo autenticação, gestão de sessão e controle de acesso, são thread-safe e resistentes a condições de corrida de tempo de verificação e tempo de uso. | | | ✓ | 367 |

## V1.12 Arquitetura segura de upload de arquivos

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.12.1** | [EXCLUÍDO, DUPLICADO DE 12.4.1] | | | | |
| **1.12.2** | Verifique se os arquivos carregados pelo usuário - se necessário para serem exibidos ou baixados da aplicação - são servidos por downloads de fluxo de octetos ou de um domínio não relacionado, como um depósito de armazenamento de arquivos em nuvem. Implemente uma Política de Segurança de Conteúdo (CSP) adequada para reduzir o risco de vetores XSS ou outros ataques do arquivo carregado. | | ✓ | ✓ | 646 |

## V1.13 Arquitetura da API

Este é um espaço reservado para futuros requisitos de arquitetura.

## V1.14 Arquitetura de configuração

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **1.14.1** | Verifique a segregação de componentes de diferentes níveis de confiança por meio de controles de segurança bem definidos, regras de firewall, gateways de API, proxies reversos, grupos de segurança baseados em nuvem ou mecanismos semelhantes. | | ✓ | ✓ | 923 |
| **1.14.2** | Verifique se as assinaturas binárias, conexões confiáveis e endpoints verificados são usados para implantar binários em dispositivos remotos. | | ✓ | ✓ | 494 |
| **1.14.3** | Verifique se o pipeline de construção avisa sobre componentes desatualizados ou inseguros e toma as ações apropriadas. | | ✓ | ✓ | 1104 |
| **1.14.4** | Verifique se o pipeline de construção contém uma etapa de construção para construir e verificar automaticamente a implantação segura da aplicação, especialmente se a infraestrutura da aplicação for definida por software, como scripts de construção do ambiente de nuvem. | | ✓ | ✓ | |
| **1.14.5** | Verifique se as implantações de aplicações são adequadamente protegidas, conteinerizadas e/ou isoladas no nível da rede para atrasar e impedir que invasores ataquem outras aplicações, especialmente quando estiverem executando ações confidenciais ou perigosas, como desserialização. ([C5](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |
| **1.14.6** | Verifique se a aplicação não usa tecnologias não suportadas, inseguras ou obsoletas do lado do cliente, como plug-ins NSAPI, Flash, Shockwave, ActiveX, Silverlight, NACL ou miniaplicações Java do lado do cliente. | | ✓ | ✓ | 477 |

## Referências

Para mais informações, consulte também:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/sdl/)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
