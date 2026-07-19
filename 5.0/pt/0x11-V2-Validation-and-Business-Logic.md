# V2 Validação e Lógica de Negócios

## Objetivo de Controle

Este capítulo tem como objetivo garantir que uma aplicação verificada atenda aos seguintes objetivos de alto nível:

* A entrada recebida pela aplicação corresponde às expectativas de negócios ou funcionais.
* O fluxo da lógica de negócios é sequencial, processado em ordem e não pode ser burlado (bypassed).
* A lógica de negócios inclui limites e controles para detectar e prevenir ataques automatizados, como transferências contínuas de pequenos fundos ou a adição de um milhão de amigos, um de cada vez.
* Fluxos de lógica de negócios de alto valor consideraram casos de abuso e atores mal-intencionados, e possuem proteções contra ataques de falsificação (spoofing), adulteração (tampering), divulgação de informações e elevação de privilégios.

## V2.1 Documentação de Validação e Lógica de Negócios

A documentação da lógica de negócios e da validação deve definir claramente os limites da lógica de negócios, regras de validação e consistência contextual de itens de dados combinados, para que fique claro o que precisa ser implementado na aplicação.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **2.1.1** | Verifique se a documentação da aplicação define regras de validação de entrada para saber como verificar a validade de itens de dados em relação a uma estrutura esperada. Pode ser formatos de dados comuns, como números de cartão de crédito, endereços de e-mail, números de telefone, ou pode ser um formato de dados interno. | 1 |
| **2.1.2** | Verifique se a documentação da aplicação define como validar a consistência lógica e contextual de itens de dados combinados, como verificar se o bairro e o CEP (ZIP code) correspondem. | 2 |
| **2.1.3** | Verifique se as expectativas em relação aos limites da lógica de negócios e às validações estão documentadas, incluindo tanto as restrições por usuário quanto as aplicadas globalmente em toda a aplicação. | 2 |

## V2.2 Validação de Entrada

Controles eficazes de validação de entrada aplicam expectativas de negócios ou funcionais em torno do tipo de dado que a aplicação espera receber. Isso garante boa qualidade de dados e reduz a superfície de ataque. No entanto, isso não remove ou substitui a necessidade de usar codificação, parametrização ou sanitização corretas ao usar os dados em outro componente ou ao apresentá-los na saída.

Neste contexto, "entrada" pode vir de uma ampla variedade de fontes, incluindo campos de formulário HTML, requisições REST, parâmetros de URL, campos de cabeçalho HTTP, cookies, arquivos no disco, bancos de dados e APIs externas.

Um controle da lógica de negócios pode verificar se uma entrada específica é um número menor que 100. Uma expectativa funcional pode verificar se um número está abaixo de um determinado limite, já que esse número controla quantas vezes um determinado loop ocorrerá, e um número alto pode levar a processamento excessivo e uma possível condição de negação de serviço (Denial of Service).

Embora a validação de esquema não seja explicitamente obrigatória, ela pode ser o mecanismo mais eficaz para cobertura total de validação de APIs HTTP ou outras interfaces que usam JSON ou XML.

Por favor, observe os seguintes pontos sobre Validação de Esquema (Schema Validation):

* A "versão publicada" da especificação de validação do JSON Schema é considerada pronta para produção, mas não é estritamente falando "estável". Ao usar a validação do JSON Schema, garanta que não haja lacunas com a orientação nos requisitos abaixo.
* Quaisquer bibliotecas de validação JSON Schema em uso também devem ser monitoradas e atualizadas se necessário assim que o padrão for formalizado.
* A validação de DTD não deve ser usada, e a avaliação de DTD no framework deve ser desativada, para evitar problemas com ataques XXE contra DTDs.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **2.2.1** | Verifique se a entrada é validada para impor expectativas funcionais ou de negócios para aquela entrada. Isso deve usar validação positiva em relação a uma lista de permissões (allowlist) de valores, padrões e intervalos, ou ser baseado na comparação da entrada com uma estrutura esperada e limites lógicos de acordo com regras predefinidas. Para L1, o foco pode ser na entrada que é usada para tomar decisões específicas de negócios ou segurança. Para L2 e superior, isso deve se aplicar a todas as entradas. | 1 |
| **2.2.2** | Verifique se a aplicação é projetada para aplicar a validação de entrada em uma camada de serviço confiável. Embora a validação no lado do cliente (client-side validation) melhore a usabilidade e deva ser incentivada, não se deve confiar nela como um controle de segurança. | 1 |
| **2.2.3** | Verifique se a aplicação garante que combinações de itens de dados relacionados sejam razoáveis de acordo com as regras predefinidas. | 2 |

## V2.3 Segurança da Lógica de Negócios

Esta seção considera os principais requisitos para garantir que a aplicação imponha os processos de lógica de negócios da maneira correta e não seja vulnerável a ataques que explorem a lógica e o fluxo da aplicação.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **2.3.1** | Verifique se a aplicação processará fluxos da lógica de negócios para o mesmo usuário apenas na ordem sequencial de etapas esperada e sem pular etapas. | 1 |
| **2.3.2** | Verifique se os limites da lógica de negócios são implementados conforme a documentação da aplicação para evitar que falhas da lógica de negócios sejam exploradas. | 2 |
| **2.3.3** | Verifique se as transações estão sendo usadas no nível da lógica de negócios, de tal forma que uma operação da lógica de negócios tenha sucesso na sua totalidade ou seja revertida (rolled back) para o estado correto anterior. | 2 |
| **2.3.4** | Verifique se mecanismos de bloqueio (locking) no nível da lógica de negócios são usados para garantir que recursos de quantidade limitada (como assentos de teatro ou horários de entrega) não possam ser reservados duplamente pela manipulação da lógica da aplicação. | 2 |
| **2.3.5** | Verifique se fluxos de lógica de negócios de alto valor exigem aprovação multiusuário para evitar ações não autorizadas ou acidentais. Isso pode incluir, mas não se limita a, grandes transferências financeiras, aprovações de contratos, acesso a informações confidenciais ou anulações de segurança (safety overrides) na manufatura. | 3 |

## V2.4 Antiautomação

Esta seção inclui controles de antiautomação para garantir que interações semelhantes a ações humanas sejam necessárias e que solicitações automatizadas excessivas sejam evitadas.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **2.4.1** | Verifique se há controles de antiautomação em vigor para proteger contra chamadas excessivas a funções da aplicação que podem levar a exfiltração de dados, criação de dados lixo (garbage-data), esgotamento de cotas, violações de limite de taxa (rate-limit), negação de serviço ou uso excessivo de recursos caros. | 2 |
| **2.4.2** | Verifique se os fluxos da lógica de negócios requerem temporização humana realista, evitando envios de transações excessivamente rápidos. | 3 |

## Referências

Para mais informações, veja também:

* [OWASP Web Security Testing Guide: Input Validation Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README.html)
* [OWASP Web Security Testing Guide: Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README)
* Anti-automation can be achieved in many ways, including the use of the [OWASP Automated Threats to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
* [JSON Schema](https://json-schema.org/specification.html)