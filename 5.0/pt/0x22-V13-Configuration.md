# V13 Configuração

## Objetivo de Controle

A configuração padrão da aplicação deve ser segura para uso na Internet.

Este capítulo fornece orientações sobre as diversas configurações necessárias para atingir isso, incluindo as que são aplicadas durante as fases de desenvolvimento, build e implantação (deployment).

Os tópicos abordados incluem prevenção de vazamento de dados, o gerenciamento seguro da comunicação entre os componentes e a proteção de segredos.

## V13.1 Documentação da Configuração

Esta seção descreve os requisitos de documentação sobre como a aplicação se comunica com serviços internos e externos, bem como as técnicas utilizadas para impedir a perda de disponibilidade provocada pela inacessibilidade de serviços. Também abrange a documentação relacionada aos segredos.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **13.1.1** | Verifique se todas as necessidades de comunicação para a aplicação estão documentadas. Isso deve incluir os serviços externos dos quais a aplicação depende e os casos onde um usuário final poderia ser capaz de fornecer um local (endereço) externo ao qual a aplicação irá se conectar. | 2 |
| **13.1.2** | Verifique se, para cada serviço que a aplicação utiliza, a documentação define o número máximo de conexões concorrentes (ex., limites do pool de conexões) e como a aplicação se comporta quando o limite for atingido, incluindo qualquer mecanismo de contingência ou de recuperação, para evitar as condições de negação de serviço. | 3 |
| **13.1.3** | Verifique se a documentação da aplicação define estratégias de gerenciamento de recursos para todos os sistemas ou serviços externos que utiliza (ex., bancos de dados, manipuladores de arquivos (file handles), threads, conexões HTTP). Isso deve incluir procedimentos de liberação de recursos, configurações de timeout, tratamento de falhas e, onde houver lógica de repetição (retry) implementada, a especificação de limites de repetição, atrasos (delays) e algoritmos de back-off. Para operações síncronas de requisição e resposta (request–response) via HTTP, isso deve exigir timeouts curtos e desativar as repetições ou limitá-las rigorosamente, a fim de evitar atrasos em cascata e o esgotamento de recursos. | 3 |
| **13.1.4** | Verifique se a documentação da aplicação define quais segredos são críticos para a segurança da aplicação e estabelece um cronograma de rotação para eles, baseado no modelo de ameaças da organização e nos requisitos de negócio. | 3 |

## V13.2 Configuração da Comunicação Backend

As aplicações interagem com vários serviços, incluindo APIs, bancos de dados ou outros componentes. Eles podem ser considerados internos à aplicação, mas não incluídos nos mecanismos padrão de controle de acesso dela, ou podem ser totalmente externos. Em ambos os casos, é necessário configurar a aplicação para interagir de forma segura com esses componentes e, se necessário, proteger essa configuração.

Nota: O capítulo "Comunicação Segura" fornece orientações sobre criptografia em trânsito.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **13.2.1** | Verifique se as comunicações entre os componentes de backend da aplicação que não suportam o mecanismo padrão de sessão de usuário da aplicação, incluindo APIs, middleware e camadas de dados, são autenticadas. A autenticação deve usar contas de serviço individuais, tokens de curta duração ou autenticação baseada em certificados, e não credenciais imutáveis, como senhas, chaves de API ou contas compartilhadas com acesso privilegiado. | 2 |
| **13.2.2** | Verifique se as comunicações entre os componentes de backend da aplicação, incluindo serviços locais ou do sistema operacional, APIs, middleware e camadas de dados, são realizadas com contas que possuem apenas os privilégios mínimos necessários. | 2 |
| **13.2.3** | Verifique se, quando uma credencial precisa ser usada para autenticação de serviço, a credencial utilizada pelo consumidor não é uma credencial padrão (ex., root/root ou admin/admin). | 2 |
| **13.2.4** | Verifique se uma lista de permissões (allowlist) é usada para definir os recursos ou sistemas externos com os quais a aplicação tem permissão para se comunicar (ex., para requisições de saída (outbound requests), cargas de dados ou acesso a arquivos). Essa allowlist pode ser implementada na camada da aplicação, no servidor web, no firewall ou por uma combinação de diferentes camadas. | 2 |
| **13.2.5** | Verifique se o servidor web ou de aplicação está configurado com uma allowlist de recursos ou sistemas para os quais o servidor pode enviar requisições ou dos quais pode carregar dados ou arquivos. | 2 |
| **13.2.6** | Verifique se, quando a aplicação se conecta a serviços distintos, ela segue a configuração documentada para cada conexão, como o número máximo de conexões paralelas, o comportamento ao atingir o máximo de conexões permitidas, os timeouts de conexão e as estratégias de repetição (retry). | 3 |

## V13.3 Gerenciamento de Segredos

O gerenciamento de segredos é uma tarefa de configuração essencial para garantir a proteção dos dados usados na aplicação. Requisitos específicos de criptografia podem ser encontrados no capítulo "Criptografia", mas esta seção foca nos aspectos de gerenciamento e manuseio de segredos.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **13.3.1** | Verifique se uma solução de gerenciamento de segredos, como um cofre de chaves (key vault), é usada para criar, armazenar, controlar o acesso e destruir com segurança os segredos de backend. Isso pode incluir senhas, material de chaves, integrações com bancos de dados e sistemas de terceiros, chaves e sementes (seeds) para tokens baseados em tempo, outros segredos internos e chaves de API. Os segredos não devem ser incluídos no código-fonte da aplicação nem nos artefatos de build. Para uma aplicação L3, isso deve envolver uma solução baseada em hardware, como um HSM. | 2 |
| **13.3.2** | Verifique se o acesso aos ativos secretos adere ao princípio do menor privilégio (least privilege). | 2 |
| **13.3.3** | Verifique se todas as operações criptográficas são realizadas usando um módulo de segurança isolado (como um cofre (vault) ou um módulo de segurança de hardware (HSM)) para gerenciar e proteger com segurança o material de chaves contra exposição fora do módulo de segurança. | 3 |
| **13.3.4** | Verifique se os segredos são configurados para expirar e serem rotacionados com base na documentação da aplicação. | 3 |

## V13.4 Vazamento de Informações Não Intencionais (Unintended Information Leakage)

As configurações de produção devem ser reforçadas (hardened) para evitar a divulgação de dados desnecessários. Muitos desses problemas raramente são classificados como riscos significativos, mas costumam ser encadeados com outras vulnerabilidades. Se esses problemas não estiverem presentes por padrão, isso eleva a barreira para atacar uma aplicação.

Por exemplo, ocultar a versão dos componentes do lado do servidor não elimina a necessidade de aplicar patches em todos os componentes, e desativar a listagem de diretórios não elimina a necessidade de usar controles de autorização ou de manter os arquivos fora da pasta pública, mas eleva a barreira.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **13.4.1** | Verifique se a aplicação é implantada (deployed) sem nenhum metadado de controle de versão, incluindo as pastas .git ou .svn, ou de forma que essas pastas fiquem inacessíveis tanto externamente quanto para a própria aplicação. | 1 |
| **13.4.2** | Verifique se os modos de depuração (debug) estão desativados em todos os componentes nos ambientes de produção, para evitar a exposição de recursos de depuração e o vazamento de informações. | 2 |
| **13.4.3** | Verifique se os servidores web não expõem listagens de diretórios (directory listings) aos clientes, a menos que isso seja explicitamente intencional. | 2 |
| **13.4.4** | Verifique se o uso do método HTTP TRACE não é suportado em ambientes de produção, para evitar possível vazamento de informações. | 2 |
| **13.4.5** | Verifique se a documentação (como a de APIs internas) e os endpoints de monitoramento não são expostos, a menos que isso seja explicitamente intencional. | 2 |
| **13.4.6** | Verifique se a aplicação não expõe informações detalhadas de versão dos componentes de backend. | 3 |
| **13.4.7** | Verifique se a camada web (web tier) está configurada para servir apenas arquivos com extensões específicas, a fim de evitar o vazamento não intencional de informações, configurações e código-fonte. | 3 |

## Referências

Para mais informações, veja também:

* [OWASP Web Security Testing Guide: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing)
