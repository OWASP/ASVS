# V7 Tratamento e registro de erros

## Objetivo de controle

O principal objetivo do tratamento e registro de erros é fornecer informações úteis para o usuário, administradores e equipes de resposta a incidentes. O objetivo não é criar grandes quantidades de logs, mas logs de alta qualidade, com mais sinal do que ruído descartado.

Logs de alta qualidade geralmente contêm dados confidenciais e devem ser protegidos conforme as leis ou diretivas locais de privacidade de dados. Isso deve incluir:

* Não coletar ou registrar informações confidenciais, a menos que seja especificamente necessário.
* Garantir que todas as informações registradas sejam tratadas com segurança e protegidas conforme a sua classificação de dados.
* Garantir que os logs não sejam armazenados para sempre, mas tenham um tempo de vida absoluto o mais curto possível.

Se os logs contiverem dados privados ou confidenciais, cuja definição varia de país para país, os logs se tornam algumas das informações mais confidenciais mantidas pela aplicação e, assim, muito atraentes para os invasores.

Também é importante garantir que a aplicação falhe com segurança e que erros não divulguem informações desnecessárias.

## V7.1 Conteúdo do registro

Registrar informações confidenciais é perigoso — os próprios logs se tornam classificados, o que significa que precisam ser criptografados, sujeitos a políticas de retenção e devem ser divulgados em auditorias de segurança. Certifique-se de que apenas as informações necessárias sejam mantidas em logs e, certamente, nenhum pagamento, credenciais (incluindo tokens de sessão), informações confidenciais ou de identificação pessoal.

V7.1 abrange OWASP Top 10 2017:A10. Como 2017:A10 e esta seção não são passíveis de teste de penetração, é importante para:

* Desenvolvedores devem garantir total conformidade com esta seção, como se todos os itens fossem marcados como L1
* Penetration testers para validar a conformidade total de todos os itens na V7.1 por meio de entrevista, capturas de tela ou afirmação

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.1.1** | Verifique se a aplicação não registra credenciais ou detalhes de pagamento. Os tokens de sessão devem ser armazenados apenas em logs num formato de hash irreversível. ([C9, C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 532 |
| **7.1.2** | Verifique se a aplicação não registra outros dados confidenciais conforme definido nas leis de privacidade locais ou na política de segurança relevante. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 532 |
| **7.1.3** | Verifique se a aplicação registra eventos relevantes de segurança, incluindo eventos de autenticação bem-sucedidos e com falha, falhas de controle de acesso, falhas de desserialização e falhas de validação de input. ([C5, C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 778 |
| **7.1.4** | Verifique se cada evento de log inclui as informações necessárias que permitem uma investigação detalhada da linha do tempo quando um evento ocorre. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 778 |

## V7.2 Processamento de Log

O registro oportuno é crítico para eventos de auditoria, triagem e escalonamento. Certifique-se de que os logs da aplicação estejam claros e possam ser facilmente monitorados e analisados localmente ou enviados para um sistema de monitoramento remoto.

V7.2 abrange OWASP Top 10 2017:A10. Como 2017:A10 e esta seção não são passíveis de teste de penetração, é importante para:

* Desenvolvedores devem garantir total conformidade com esta seção, como se todos os itens fossem marcados como L1
* Penetration testers para validar a conformidade total de todos os itens na V7.2 por entrevista, capturas de tela ou afirmação

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.2.1** | Verifique se todas as decisões de autenticação são registradas, sem armazenar senhas ou tokens de sessão confidenciais. Isso deve incluir solicitações com metadados relevantes necessários para investigações de segurança. | | ✓ | ✓ | 778 |
| **7.2.2** | Verifique se todas as decisões de controle de acesso podem ser registradas e todas as decisões com falha são registradas. Isso deve incluir solicitações com metadados relevantes necessários para investigações de segurança. | | ✓ | ✓ | 285 |

## V7.3 Proteção de Log

Logs que podem ser modificados ou excluídos trivialmente são inúteis para investigações e processos. A divulgação de logs pode expor detalhes internos sobre a aplicação ou os dados que ele contém. Deve-se tomar cuidado ao proteger os logs contra divulgação, modificação ou exclusão não autorizada.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.3.1** | Verifique se todos os componentes de log codificam os dados adequadamente para evitar a injeção de log. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 117 |
| **7.3.2** | [EXCLUÍDO, DUPLICADO DE 7.3.1] | | | | |
| **7.3.3** | Verifique se os logs de segurança estão protegidos contra acesso e modificação não autorizados. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 200 |
| **7.3.4** | Verifique se as fontes de horário estão sincronizadas com a hora e o fuso horário corretos. Considere fortemente o registro apenas em UTC se os sistemas forem globais para auxiliar na análise forense pós-incidente. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |

Observação: a codificação de log (7.3.1) é difícil de testar e revisar usando ferramentas dinâmicas automatizadas e testes de penetração, mas arquitetos, desenvolvedores e revisores de código-fonte devem considerá-la um requisito L1.

## V7.4 Tratamento de Erros

O objetivo do tratamento de erros é permitir que a aplicação forneça eventos relevantes de segurança para monitoramento, triagem e escalonamento. O objetivo não é criar logs. Ao registrar eventos relacionados à segurança, certifique-se de que haja uma finalidade para o registro e que ele possa ser distinguido pelo SIEM ou software de análise.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **7.4.1** | Verifique se uma mensagem genérica é exibida quando ocorre um erro inesperado ou sensível à segurança, possivelmente com uma ID exclusiva que a equipe de suporte pode usar para investigar. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 210 |
| **7.4.2** | Verifique se o tratamento de exceção (ou um equivalente funcional) é usado na base de código para contabilizar as condições de erro esperadas e inesperadas. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 544 |
| **7.4.3** | Verifique se um manipulador de erro de "último recurso" está definido para capturar todas as exceções não tratadas. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 431 |

Nota: Certas linguagens, como Swift e Go — e através da prática de design comum — muitas linguagens funcionais, não suportam exceções ou manipuladores de eventos de último recurso. Nesse caso, arquitetos e desenvolvedores devem usar um padrão, linguagem ou estrutura amigável para garantir que as aplicações possam manipular com segurança eventos excepcionais, inesperados ou relacionados à segurança.

## Referências

Para mais informações, consulte também:

* [OWASP Testing Guide 4.0 content: Testing for Error Handling](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/README.html)
* [OWASP Authentication Cheat Sheet section about error messages](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#authentication-and-error-messages)

