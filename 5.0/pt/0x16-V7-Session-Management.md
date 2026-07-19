# V7 Gerenciamento de Sessão

## Objetivo de Controle

Os mecanismos de gerenciamento de sessão permitem que as aplicações correlacionem as interações do usuário e do dispositivo ao longo do tempo, mesmo ao usar protocolos de comunicação sem estado (como o HTTP). Aplicações modernas podem usar vários tokens de sessão com características e propósitos distintos. Um sistema de gerenciamento de sessão seguro é aquele que impede que invasores obtenham, utilizem ou, de outra forma, abusem da sessão de uma vítima. Aplicações que mantêm sessões devem garantir que os seguintes requisitos de alto nível de gerenciamento de sessão sejam atendidos:

* As sessões são exclusivas de cada indivíduo e não podem ser adivinhadas ou compartilhadas.
* As sessões são invalidadas quando não são mais necessárias e expiram durante períodos de inatividade.

Muitos dos requisitos neste capítulo estão relacionados aos controles selecionados do [NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/), concentrando-se em ameaças comuns e fraquezas de autenticação frequentemente exploradas.

Observe que os requisitos para detalhes de implementação específicos de determinados mecanismos de gerenciamento de sessão podem ser encontrados em outras partes:

* Cookies HTTP são um mecanismo comum para proteger tokens de sessão. Os requisitos específicos de segurança para cookies podem ser encontrados no capítulo "Segurança de Frontend Web" (Web Frontend Security).
* Tokens autocontidos (Self-contained tokens) são frequentemente usados como uma forma de manter sessões. Requisitos de segurança específicos podem ser encontrados no capítulo "Tokens Autocontidos" (Self-contained Tokens).

## V7.1 Documentação de Gerenciamento de Sessão

Não existe um padrão único que atenda a todas as aplicações. Portanto, não é viável definir fronteiras e limites universais que sirvam para todos os casos. Uma análise de risco com decisões de segurança documentadas relacionadas ao tratamento de sessões deve ser conduzida como um pré-requisito para implementação e teste. Isso garante que o sistema de gerenciamento de sessão seja adaptado aos requisitos específicos da aplicação.

Independentemente de ser escolhido um mecanismo de sessão stateful ou "stateless" (sem estado), a análise deve ser completa e documentada para demonstrar que a solução selecionada é capaz de satisfazer todos os requisitos de segurança relevantes. A interação com quaisquer mecanismos de Single Sign-on (SSO) em uso também deve ser considerada.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **7.1.1** | Verifique se o tempo limite de inatividade da sessão do usuário e o tempo de vida (lifetime) máximo absoluto da sessão estão documentados, são apropriados em combinação com outros controles e se a documentação inclui justificativa para quaisquer desvios dos requisitos de reautenticação do NIST SP 800-63B. | 2 |
| **7.1.2** | Verifique se a documentação define quantas sessões concorrentes (paralelas) são permitidas para uma conta, bem como os comportamentos e as ações pretendidas a serem tomadas quando o número máximo de sessões ativas for alcançado. | 2 |
| **7.1.3** | Verifique se todos os sistemas que criam e gerenciam sessões de usuário como parte de um ecossistema de gerenciamento de identidade federada (como sistemas SSO) estão documentados juntamente com os controles para coordenar tempos de vida das sessões, encerramento e quaisquer outras condições que exijam reautenticação. | 2 |

## V7.2 Segurança Fundamental do Gerenciamento de Sessão

Esta seção atende aos requisitos essenciais de sessões seguras verificando se os tokens de sessão são gerados e validados com segurança.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **7.2.1** | Verifique se a aplicação realiza toda a verificação do token de sessão usando um serviço de backend confiável. | 1 |
| **7.2.2** | Verifique se a aplicação usa tokens autocontidos ou de referência gerados dinamicamente para o gerenciamento de sessão, ou seja, não usando chaves e segredos estáticos de API. | 1 |
| **7.2.3** | Verifique se, caso tokens de referência sejam usados para representar sessões de usuário, eles são únicos e gerados usando um gerador de números pseudoaleatórios criptograficamente seguro (CSPRNG) e possuem pelo menos 128 bits de entropia. | 1 |
| **7.2.4** | Verifique se a aplicação gera um novo token de sessão no momento da autenticação do usuário, incluindo a reautenticação, e encerra o token de sessão atual. | 1 |

## V7.3 Tempo Limite de Sessão (Session Timeout)

Mecanismos de timeout (tempo limite) de sessão servem para minimizar a janela de oportunidade para sequestro de sessão (session hijacking) e outras formas de abuso de sessão. Os timeouts devem satisfazer as decisões de segurança documentadas.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **7.3.1** | Verifique se existe um tempo limite (timeout) de inatividade de modo que a reautenticação seja forçada de acordo com a análise de risco e as decisões de segurança documentadas. | 2 |
| **7.3.2** | Verifique se existe um tempo de vida (lifetime) máximo absoluto para a sessão, de forma que a reautenticação seja forçada de acordo com a análise de risco e as decisões de segurança documentadas. | 2 |

## V7.4 Encerramento da Sessão

O encerramento da sessão pode ser tratado pela própria aplicação ou pelo provedor de SSO, caso o provedor de SSO esteja lidando com o gerenciamento de sessão em vez da aplicação. Pode ser necessário decidir se o provedor de SSO está no escopo ao considerar os requisitos nesta seção, pois alguns deles podem ser controlados pelo provedor.

O encerramento da sessão deve resultar na exigência de reautenticação e ser eficaz em toda a aplicação, login federado (se presente) e quaisquer relying parties (partes confiáveis).

Para mecanismos de sessão stateful, o encerramento normalmente envolve a invalidação da sessão no backend. No caso de tokens autocontidos, medidas adicionais são necessárias para revogar ou bloquear esses tokens, pois de outra forma eles poderiam permanecer válidos até a expiração.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **7.4.1** | Verifique se, quando o encerramento da sessão é acionado (como em caso de logout ou expiração), a aplicação proíbe qualquer uso adicional da sessão. Para tokens de referência ou sessões stateful, isso significa invalidar os dados da sessão no backend da aplicação. As aplicações que usam tokens autocontidos precisarão de uma solução como manter uma lista de tokens encerrados, proibir tokens produzidos antes de uma data e hora por usuário ou rotacionar a chave de assinatura por usuário. | 1 |
| **7.4.2** | Verifique se a aplicação encerra todas as sessões ativas quando uma conta de usuário é desativada ou excluída (como quando um funcionário deixa a empresa). | 1 |
| **7.4.3** | Verifique se a aplicação fornece a opção de encerrar todas as outras sessões ativas após uma mudança ou remoção bem-sucedida de qualquer fator de autenticação (incluindo alteração de senha via redefinição ou recuperação e, se presente, atualização de configurações de MFA). | 2 |
| **7.4.4** | Verifique se todas as páginas que requerem autenticação têm um acesso fácil e visível à funcionalidade de logout. | 2 |
| **7.4.5** | Verifique se os administradores da aplicação conseguem encerrar sessões ativas para um usuário individual ou para todos os usuários. | 2 |

## V7.5 Defesas Contra o Abuso de Sessão

Esta seção fornece requisitos para mitigar o risco representado por sessões ativas que sejam sequestradas ou abusadas por meio de vetores que dependem da existência e das capacidades das sessões de usuário ativas. Por exemplo, usando a execução de conteúdo malicioso para forçar um navegador de vítima autenticado a executar uma ação utilizando a sessão da vítima.

Note que a orientação específica por nível no capítulo "Autenticação" (Authentication) deve ser levada em consideração ao avaliar os requisitos desta seção.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **7.5.1** | Verifique se a aplicação exige uma reautenticação completa antes de permitir modificações em atributos sensíveis da conta que possam afetar a autenticação, como endereço de e-mail, número de telefone, configuração de MFA ou outras informações usadas na recuperação da conta. | 2 |
| **7.5.2** | Verifique se os usuários são capazes de visualizar e (tendo se autenticado novamente com pelo menos um fator) encerrar qualquer ou todas as sessões ativas no momento. | 2 |
| **7.5.3** | Verifique se a aplicação exige uma autenticação posterior com pelo menos um fator ou verificação secundária antes de executar transações ou operações altamente confidenciais. | 3 |

## V7.6 Reautenticação Federada

Esta seção se relaciona àqueles que escrevem o código da Relying Party (RP) ou do Provedor de Identidade (IdP). Esses requisitos são derivados do [NIST SP 800-63C](https://pages.nist.gov/800-63-4/sp800-63c.html) para Federação e Asserções.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **7.6.1** | Verifique se o tempo de vida e o encerramento da sessão entre Relying Parties (RPs) e Provedores de Identidade (IdPs) se comportam conforme o documentado, exigindo a reautenticação conforme necessário, como, por exemplo, quando o tempo máximo entre os eventos de autenticação do IdP é atingido. | 2 |
| **7.6.2** | Verifique se a criação de uma sessão requer o consentimento do usuário ou uma ação explícita, prevenindo a criação de novas sessões na aplicação sem interação do usuário. | 2 |

## Referências

Para mais informações, veja também:

* [OWASP Web Security Testing Guide: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/06-Session_Management_Testing)
* [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
