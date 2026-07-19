# V16 Registro de Segurança e Tratamento de Erros

## Objetivo de Controle

Os logs (registros) de segurança são distintos de logs de erro ou de desempenho e são usados para registrar eventos relevantes para a segurança, como decisões de autenticação, decisões de controle de acesso e tentativas de burlar os controles de segurança, como a validação de entrada ou a validação da lógica de negócios. O seu propósito é o de apoiar a detecção, resposta e investigação, fornecendo dados estruturados e de alto sinal (high-signal) para ferramentas de análise, como SIEMs.

Os logs não devem incluir dados pessoais sensíveis a menos que exigido legalmente, e quaisquer dados registrados devem ser protegidos como um ativo de alto valor. O registro (logging) não deve comprometer a privacidade ou a segurança do sistema. As aplicações também devem falhar de forma segura (fail securely), evitando divulgação ou interrupção desnecessária.

Para orientações detalhadas de implementação, consulte as OWASP Cheat Sheets na seção de referências.

## V16.1 Documentação de Registros de Segurança (Security Logging)

Esta seção garante um inventário claro e completo dos logs em toda a pilha da aplicação (application stack). Isso é essencial para o monitoramento eficaz da segurança, para a resposta a incidentes e a conformidade.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **16.1.1** | Verifique se existe um inventário documentando o registro (logging) realizado em cada camada da pilha de tecnologia da aplicação, quais eventos estão sendo registrados, os formatos dos logs, onde esse log é armazenado, como é utilizado, como o acesso a ele é controlado, e por quanto tempo os logs são mantidos. | 2 |

## V16.2 Registro (Logging) Geral

Esta seção fornece requisitos para garantir que os logs de segurança sejam estruturados de forma consistente e contenham os metadados esperados. O objetivo é tornar os logs legíveis por máquina e analisáveis em sistemas e ferramentas distribuídas.

Naturalmente, os eventos de segurança envolvem frequentemente dados sensíveis. Se tais dados forem registrados sem consideração, os próprios logs se tornam classificados e, portanto, sujeitos a requisitos de criptografia, políticas de retenção mais rigorosas e potencial divulgação durante as auditorias.

Portanto, é crítico registrar apenas o que é necessário e tratar os dados de log com o mesmo cuidado com outros ativos sensíveis.

Os requisitos abaixo estabelecem os requisitos fundamentais para os metadados de logs, para a sincronização, para o formato e seu controle.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **16.2.1** | Verifique se cada entrada de log (log entry) inclui os metadados necessários (como quando, onde, quem, o que) que permitiriam uma investigação detalhada da linha do tempo quando um evento acontecer. | 2 |
| **16.2.2** | Verifique se as fontes de tempo para todos os componentes de registro estão sincronizadas, e que os carimbos de data/hora (timestamps) nos metadados do evento de segurança usem UTC ou incluam o deslocamento explícito (offset) do fuso horário. O UTC é recomendado para garantir a consistência através de sistemas distribuídos e para prevenir confusões durante as transições do horário de verão. | 2 |
| **16.2.3** | Verifique se a aplicação apenas armazena ou transmite os logs para os arquivos e serviços que estejam documentados no inventário de logs. | 2 |
| **16.2.4** | Verifique se os logs podem ser lidos e correlacionados pelo processador de log que está em uso, preferencialmente usando um formato de log comum. | 2 |
| **16.2.5** | Verifique se, ao registrar os dados sensíveis, a aplicação impõe o logging baseado no nível de proteção daquele dado. Por exemplo, pode não ser permitido logar determinados dados, como credenciais ou detalhes de pagamento. Outros dados, como os tokens de sessão, podem ser logados apenas ao estarem em hash ou mascarados, de forma total ou parcial. | 2 |

## V16.3 Eventos de Segurança

Esta seção define os requisitos para registrar os eventos de relevância de segurança dentro da aplicação. Capturar estes eventos é essencial para detectar comportamentos suspeitos, apoiar investigações e cumprir as obrigações de compliance.

Esta seção descreve os tipos de eventos que devem ser registrados, mas não tenta fornecer detalhes exaustivos. Toda aplicação possui fatores de risco e o contexto operacional únicos.

Observe que, embora o ASVS inclua o registro (logging) de eventos de segurança no escopo, o alerta (alerting) e a correlação (ex., regras de SIEM ou infraestrutura de monitoramento) são considerados fora do escopo e são tratados por sistemas operacionais e de monitoramento.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **16.3.1** | Verifique se todas as operações de autenticação são registradas, incluindo as tentativas bem e malsucedidas. Metadados adicionais, como o tipo de autenticação ou os fatores usados, também deverão ser coletados. | 2 |
| **16.3.2** | Verifique se as tentativas falhas de autorização são registradas. Para o L3, isto deve incluir o registro de todas as decisões da autorização, incluindo o registro quando os dados sensíveis são acessados (sem registrar os dados sensíveis em si). | 2 |
| **16.3.3** | Verifique se a aplicação registra os eventos de segurança que foram definidos na documentação e que também registre as tentativas de ignorar (bypass) os controles de segurança, tais como a validação da entrada, a lógica de negócios e as medidas antiautomação. | 2 |
| **16.3.4** | Verifique se a aplicação registra os erros inesperados e as falhas dos controles de segurança, tais como falhas do TLS no backend. | 2 |

## V16.4 Proteção de Logs

Os logs são artefatos forenses valiosos e devem ser protegidos. Se os logs puderem ser facilmente modificados ou excluídos, eles perdem a integridade e tornam-se não confiáveis para as investigações de incidentes ou procedimentos legais. Os logs podem expor o comportamento interno de aplicações ou metadados sensíveis, tornando-os um alvo atraente para os atacantes.

Esta seção define os requisitos a fim de garantir que os logs estejam protegidos contra acessos não autorizados, adulterações e as suas divulgações, e que sejam transmitidos de forma segura e armazenados e sistemas seguros e isolados.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **16.4.1** | Verifique se todos os componentes de logging codificam os dados apropriadamente para evitar a injeção em logs (log injection). | 2 |
| **16.4.2** | Verifique se os logs estão protegidos contra o acesso não autorizado e não podem ser modificados. | 2 |
| **16.4.3** | Verifique se os logs são transmitidos de forma segura para um sistema logicamente isolado e separado para análise, detecção, alerta e encaminhamento (escalation). O objetivo é garantir que, caso a aplicação for invadida, os logs não sejam comprometidos. | 2 |

## V16.5 Tratamento de Erros

Esta seção define os requisitos para garantir que as aplicações apresentem falhas em forma harmoniosa e contínua de modo seguro (fail gracefully and securely), sem divulgação dos detalhes internos e sensíveis.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **16.5.1** | Verifique se uma mensagem genérica é retornada ao consumidor perante as falhas quando ocorre um erro inesperado e de impacto na segurança, garantindo assim nenhuma exposição nos dados sensíveis do sistema interno (ex: como stack traces, comandos em queries, senhas chaves dos sistemas de processos, e os tokens em aberto). | 2 |
| **16.5.2** | Verifique se a aplicação continuará a atuar e no processamento em modos segurança perante os eventos das falhas através os acessos na bases dos recursos os de formatos externo e/ou externos a, e no o através a exemplo das chamadas aos os na do dos de processos em do padrões na (patterns) nas das sobre de as os do e com as nos referidos de a no como os a em as os do de de do e "circuit a e a de do breakers" a e na (disjuntores de de da circuitos) as a ou de de em de a degradação e e a harmoniosa da do de (graceful o da degradation). | 2 |
| **16.5.3** | Verifique se a aplicação a a o falha o e a as e e de da da de da de forma as de da de a de de a harmoniosa a o de a de da a e a segura a de da as da (fails e as e as de gracefully da e a de and a as de de securely), as de a a o incluindo as a as o de quando a as e da a a ocorre o a a as uma a a as da a e de a exceção, o de e a da da da prevenindo da de a as a da condições de da as a da o a de da a da de da "fail-open" o da da (falhar a da de de de a de de e de aberto) e a de da as de de como da e a a o a da de processar a de a a as uma da a a a transação de as da a da as apesar a de as de as a da dos de a de da da erros o de de as as resultantes a e da as da a da a lógica de de a da as de de da a a validação da a da as. | 2 |
| **16.5.4** | Verifique se a a a um a a de da de manipulador o a de de a a da as de o as erro a e da as as "de a da as de da as da última o de a da da as de as da a instância" a de de de a as de as (last as a de de as as da as resort) de as de as as as a é as a de a da as de definido da o a a o o que a de de de as as as irá a da a as as capturar da de a a de da as as todas de da as de as a a de de as a da a exceções o a de as de as as de de as da a as não de de da a da de a tratadas. de as de a a de Isto a as da a é a a o as as a a da de a tanto a de de as as a de para as as a de a evitar a a a de de a de as as de a a de de da perder de o de a da da da a as da a detalhes da a a de a do de a a o de da de da a de de as da a as de erro o a da as as da as da que a as as as de as a as de da de devem a de a de de a ir da as da da da de de a de a as de de para da da da de de os o as de arquivos de da de da da de da log, de a de de o a de de e as as a quanto a as da da de as as para as de de de a a as a a de a as as de a garantir as de a as da a que as a da as da a de da da de a um de da a o erro da da da de as de de a a a as as as não de de as a a de o derrube as da a o de o de as as a da da de de todo de da da de de de o as da a de da da a de de de da a processo da a a as de de as da as a as as as a de aplicação, a de de da de o da a a as a a de levando da a da as a da de a de de de da uma da de a as a a de de perda a da de da a as de as a as da de de as disponibilidade a a as a a as da de as a. | 3 |

Nota: Determinadas a da as linguagens da da as as, as a as da as de as a (incluindo da de a o da a a Swift, da da da as Go e, a a as de da as da de da de através da da as as a as as a as as a de de de de de de a de as prática de de da de comum de da a as de as as de a as a de de as da as design, de a a as a da a as a muitas da a as de a de de da as a as as a as da as linguagens a de da a da da a de as a da de funcionais, da de da de) de as a a não a a as de de a suportam a de as as a as as de exceções a a a de a de de a de da a de de ou as as de da da a as da de da manipuladores a da da da as a de de de eventos as a da de de de as as da da a as as a de as a de as as última da a a as de as instância de da da de de da da de as as a de a as da da de de a a. as a Neste a de as de de de a caso de a as de a de a da, as da de da arquitetos a as de da da de de a as e a as a de a desenvolvedores de da da a as da as devem a de a da as da a as de a usar da as de a da de da as de de a de de a da da de um da a a da as de padrão a da as de a da as da as a as, as a a linguagem a de a as a da da ou a da as da de da a um da da a da da a a da de de a de da as da da de modo a a a a da a de a a da da de da a amigável as de a da da a a ao de as de as a framework as as as da de as as de a da da da a as de as a a de da para a de as as da as as da as as garantir a as de a da a as a a da as as a da a que a as as as aplicações de de de a a de da da as a as da possam de as as de a de as de de a as as a a a a de as a lidar da de as da de a de da a de a de as de de forma a as as da as a de da a de a de de as segura da a da as com as de as as a eventos as a da de excepcionais a a de a de a da de as as, a a a de a as de as inesperados a a de a a ou a as de da a a as a de de as a da relacionados as da a de da da de a da as da a segurança a da a.

## Referências

Para mais informações, veja também:

* [OWASP Web Security Testing Guide: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
* [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
* [OWASP Application Logging Vocabulary Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html)