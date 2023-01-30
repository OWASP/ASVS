# V11 Lógica de Negócios

## Objetivo de controle

Certifique-se de que uma aplicação verificado atenda aos seguintes requisitos de alto nível:

* O fluxo da lógica de negócios é sequencial, processado em ordem e não pode ser ignorado.
* A lógica de negócios inclui limites para detectar e prevenir ataques automatizados, como pequenas transferências contínuas de fundos ou adição de um milhão de amigos, um por vez, e assim por diante.
* Os fluxos de lógica de negócios de alto valor consideraram casos de abuso e atores mal-intencionados com proteções contra falsificação, adulteração, divulgação de informações e ataques de elevação de privilégio.

## V11.1 Segurança da Lógica de Negócios

A segurança da lógica de negócios é tão individual para cada aplicação que nenhuma lista de verificação será aplicada. A segurança da lógica de negócios deve ser projetada para proteger contra prováveis ameaças externas - ela não pode ser adicionada usando firewalls de aplicações da Web ou comunicações seguras. Recomendamos o uso de modelagem de ameaças durante os sprints de design, por exemplo, usando o OWASP Cornucopia ou ferramentas semelhantes.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **11.1.1** | Verifique se a aplicação processará apenas fluxos de lógica de negócios para o mesmo usuário em ordem sequencial de etapas e sem pular etapas. | ✓ | ✓ | ✓ | 841 |
| **11.1.2** | Verifique se a aplicação processará apenas fluxos de lógica de negócios com todas as etapas sendo processadas em tempo humano realista, ou seja, as transações não são enviadas muito rapidamente. | ✓ | ✓ | ✓ | 799 |
| **11.1.3** | Verifique se a aplicação tem limites apropriados para ações ou transações de negócios específicas que são aplicadas corretamente por usuário. | ✓ | ✓ | ✓ | 770 |
| **11.1.4** | Verifique se a aplicação possui controles antiautomação para proteção contra chamadas excessivas, como exfiltração de dados em massa, solicitações de lógica de negócios, uploads de arquivos ou ataques de negação de serviço. | ✓ | ✓ | ✓ | 770 |
| **11.1.5** | Verifique se a aplicação tem limites de lógica de negócios ou validação para proteger contra prováveis riscos ou ameaças de negócios, identificados usando modelagem de ameaças ou metodologias semelhantes. | ✓ | ✓ | ✓ | 841 |
| **11.1.6** | Verifique se a aplicação não sofre de problemas de "Time Of Check to Time Of Use" (TOCTOU) ou outras condições de corrida para operações confidenciais. | | ✓ | ✓ | 367 |
| **11.1.7** | Verifique se a aplicação monitora eventos ou atividades incomuns de uma perspectiva de lógica de negócios. Por exemplo, tentativas de executar ações fora de ordem ou ações que um usuário normal nunca tentaria. ([C9](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 754 |
| **11.1.8** | Verifique se a aplicação possui alertas configuráveis quando ataques automatizados ou atividades incomuns são detectados. | | ✓ | ✓ | 390 |

## Referências

Para mais informações, consulte também:

* [OWASP Web Security Testing Guide 4.1: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README.html)
* A antiautomação pode ser alcançada de várias maneiras, incluindo o uso de [OWASP AppSensor](https://github.com/jtmelton/appsensor) e [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP AppSensor](https://github.com/jtmelton/appsensor) pode também ajudar com Detecção e Respostas de Ataques.
* [OWASP Cornucopia](https://owasp.org/www-project-cornucopia/)
