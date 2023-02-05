# V8 Proteção de Dados

## Objetivo de controle

Existem três elementos-chave para uma boa proteção de dados: Confidencialidade, Integridade e Disponibilidade (CIA). Este padrão assume que a proteção de dados é aplicada num sistema confiável, como um servidor, reforçado e possui proteções suficientes.

As aplicações devem assumir que todos os dispositivos do usuário estão comprometidos de alguma forma. Quando uma aplicação transmite ou armazena informações confidenciais em dispositivos inseguros, como computadores, telefones e tablets compartilhados, a aplicação é responsável por garantir que os dados armazenados nesses dispositivos sejam criptografados e não possam ser facilmente obtidos, alterados ou divulgados de forma ilícita.

Certifique-se de que uma aplicação verificado atenda aos seguintes requisitos de proteção de dados de alto nível:

* Confidencialidade: Os dados devem ser protegidos contra observação ou divulgação não autorizada, tanto em trânsito quanto quando armazenados.
* Integridade: os dados devem ser protegidos contra criação, alteração ou exclusão maliciosa por invasores não autorizados.
* Disponibilidade: Os dados devem estar disponíveis para usuários autorizados conforme necessário.

## V8.1 Proteção Geral de Dados

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **8.1.1** | Verifique se a aplicação protege os dados confidenciais de serem armazenados em cache nos componentes do servidor, como balanceadores de carga e caches de aplicações. | | ✓ | ✓ | 524 |
| **8.1.2** | Verifique se todas as cópias em cache ou temporárias de dados confidenciais armazenados no servidor estão protegidas contra acesso não autorizado ou eliminadas/invalidadas depois que o usuário autorizado acessa os dados confidenciais. | | ✓ | ✓ | 524 |
| **8.1.3** | Verifique se a aplicação minimiza o número de parâmetros numa solicitação, como campos ocultos, variáveis Ajax, cookies e valores de cabeçalho. | | ✓ | ✓ | 233 |
| **8.1.4** | Verifique se a aplicação pode detectar e alertar sobre números anormais de solicitações, como por IP, usuário, total por hora ou dia ou o que fizer sentido para a aplicação. | | ✓ | ✓ | 770 |
| **8.1.5** | Verifique se os backups regulares de dados importantes são executados e se a restauração de teste de dados é realizada. | | | ✓ | 19 |
| **8.1.6** | Verifique se os backups são armazenados com segurança para evitar que os dados sejam roubados ou corrompidos. | | | ✓ | 19 |

## V8.2 Proteção de dados do lado do cliente

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **8.2.1** | Verifique se a aplicação define cabeçalhos anti-cache suficientes para que dados confidenciais não sejam armazenados em cache em navegadores modernos. | ✓ | ✓ | ✓ | 525 |
| **8.2.2** | Verifique se os dados armazenados no armazenamento do navegador (como localStorage, sessionStorage, IndexedDB ou cookies) não contêm dados confidenciais. | ✓ | ✓ | ✓ | 922 |
| **8.2.3** | Verifique se os dados autenticados foram apagados do armazenamento do cliente, como o DOM do navegador, após o término do cliente ou da sessão. | ✓ | ✓ | ✓ | 922 |

## V8.3 Dados privados confidenciais

Esta seção ajuda a proteger dados confidenciais de serem criados, lidos, atualizados ou excluídos sem autorização, especialmente em grandes quantidades.

A conformidade com esta seção implica conformidade com o Controle de acesso V4 e, em particular, V4.2. Por exemplo, para proteger contra atualizações não autorizadas ou divulgação de informações pessoais confidenciais, é necessário aderir à V4.2.1. Por favor, cumpra esta seção e V4 para cobertura completa.

Observação: os regulamentos e as leis de privacidade, como os princípios de privacidade australianos APP-11 ou GDPR, afetam diretamente como as aplicações devem abordar a implementação de armazenamento, uso e transmissão de informações pessoais confidenciais. Isso varia de penalidades severas a conselhos simples. Consulte as leis e regulamentos locais e consulte um especialista em privacidade ou advogado qualificado, conforme necessário.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **8.3.1** | Verifique se os dados confidenciais são enviados ao servidor no corpo ou nos cabeçalhos da mensagem HTTP e se os parâmetros da string de consulta de qualquer verbo HTTP não contêm dados confidenciais. | ✓ | ✓ | ✓ | 319 |
| **8.3.2** | Verifique se os usuários têm um método para remover ou exportar os seus dados sob demanda. | ✓ | ✓ | ✓ | 212 |
| **8.3.3** | Verifique se os usuários recebem uma linguagem clara sobre a coleta e o uso das informações pessoais fornecidas e se os usuários forneceram consentimento para o uso desses dados antes de serem usados de qualquer forma. | ✓ | ✓ | ✓ | 285 |
| **8.3.4** | Verifique se todos os dados confidenciais criados e processados pela aplicação foram identificados e certifique-se de que haja uma política sobre como lidar com dados confidenciais. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 200 |
| **8.3.5** | Verifique se o acesso a dados confidenciais é auditado (sem registrar os próprios dados confidenciais), se os dados forem coletados conforme as diretivas de proteção de dados relevantes ou se o registro de acesso for necessário. | | ✓ | ✓ | 532 |
| **8.3.6** | Verifique se as informações confidenciais contidas na memória são substituídas assim que não são mais necessárias para mitigar ataques de despejo de memória, usando zeros ou dados aleatórios. | | ✓ | ✓ | 226 |
| **8.3.7** | Verifique se as informações confidenciais ou privadas que devem ser criptografadas estão criptografadas usando algoritmos aprovados que fornecem confidencialidade e integridade. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 327 |
| **8.3.8** | Verifique se as informações pessoais confidenciais estão sujeitas à classificação de retenção de dados, de modo que os dados antigos ou desatualizados sejam excluídos automaticamente, de acordo com a programação ou conforme a situação exigir. | | ✓ | ✓ | 285 |

Ao considerar a proteção de dados, uma consideração primária deve ser a extração em massa ou modificação, ou uso excessivo. Por exemplo, muitos sistemas de mídia social permitem apenas que os usuários adicionem 100 novos amigos por dia, mas de qual sistema essas solicitações vieram não é importante. Uma plataforma bancária pode querer bloquear mais de 5 transações por hora, transferindo mais de 1000 euros de fundos para instituições externas. É provável que os requisitos de cada sistema sejam muito diferentes, portanto, decidir sobre "anormal" deve considerar o modelo de ameaça e o risco comercial. Critérios importantes são a capacidade de detectar, impedir ou, preferencialmente, bloquear tais ações em massa anormais.

## Referências

Para mais informações, consulte também:

* [Consider using Security Headers website to check security and anti-caching headers](https://securityheaders.io)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [European Union General Data Protection Regulation (GDPR) overview](https://edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
