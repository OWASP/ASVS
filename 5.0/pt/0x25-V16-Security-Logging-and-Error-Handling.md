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

Esta seção define os requisitos para garantir que os logs estejam protegidos contra acesso não autorizado, adulteração e divulgação, e que sejam transmitidos com segurança e armazenados em sistemas seguros e isolados.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **16.4.1** | Verifique se todos os componentes de logging codificam os dados apropriadamente para evitar a injeção em logs (log injection). | 2 |
| **16.4.2** | Verifique se os logs estão protegidos contra o acesso não autorizado e não podem ser modificados. | 2 |
| **16.4.3** | Verifique se os logs são transmitidos com segurança para um sistema logicamente separado, para análise, detecção, alerta e escalonamento (escalation). O objetivo é garantir que, se a aplicação for violada, os logs não sejam comprometidos. | 2 |

## V16.5 Tratamento de Erros

Esta seção define os requisitos para garantir que as aplicações falhem de forma controlada e segura (fail gracefully and securely), sem divulgar detalhes internos sensíveis.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **16.5.1** | Verifique se uma mensagem genérica é retornada ao consumidor quando ocorre um erro inesperado ou sensível à segurança, garantindo que nenhum dado sensível interno do sistema seja exposto, como stack traces, consultas (queries), chaves secretas e tokens. | 2 |
| **16.5.2** | Verifique se a aplicação continua a operar com segurança quando o acesso a recursos externos falha, por exemplo, usando padrões (patterns) como disjuntores (circuit breakers) ou degradação controlada (graceful degradation). | 2 |
| **16.5.3** | Verifique se a aplicação falha de forma controlada e segura (fails gracefully and securely), inclusive quando ocorre uma exceção, prevenindo condições de fail-open (falha aberta), como o processamento de uma transação apesar de erros resultantes da lógica de validação. | 2 |
| **16.5.4** | Verifique se um manipulador de erros de "última instância" (last resort) é definido e captura todas as exceções não tratadas. Isso serve tanto para evitar a perda de detalhes de erro que devem ir para os arquivos de log quanto para garantir que um erro não derrube todo o processo da aplicação, levando a uma perda de disponibilidade. | 3 |

Nota: Determinadas linguagens (incluindo Swift, Go e, por prática comum de design, muitas linguagens funcionais) não suportam exceções nem manipuladores de eventos de última instância. Nesse caso, arquitetos e desenvolvedores devem usar um padrão, uma linguagem ou uma forma compatível com o framework para garantir que as aplicações consigam lidar com segurança com eventos excepcionais, inesperados ou relacionados à segurança.

## Referências

Para mais informações, veja também:

* [OWASP Web Security Testing Guide: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)
* [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
* [OWASP Application Logging Vocabulary Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html)
