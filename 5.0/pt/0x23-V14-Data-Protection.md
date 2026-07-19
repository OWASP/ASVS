# V14 Proteção de Dados

## Objetivo de Controle

As aplicações não conseguem contabilizar todos os padrões de uso e comportamentos dos usuários e devem, portanto, implementar controles para limitar o acesso não autorizado a dados sensíveis nos dispositivos dos clientes.

Este capítulo inclui requisitos relacionados a definir quais dados precisam ser protegidos, como eles devem ser protegidos e mecanismos específicos a serem implementados ou armadilhas a serem evitadas.

Outra consideração para a proteção de dados é a extração em massa, modificação ou uso excessivo. Os requisitos de cada sistema provavelmente serão muito diferentes, de modo que determinar o que é "anormal" deve levar em consideração o modelo de ameaças e o risco de negócios. Do ponto de vista do ASVS, a detecção desses problemas é tratada no capítulo "Registro de Segurança e Tratamento de Erros" e o estabelecimento de limites é tratado no capítulo "Validação e Lógica de Negócios".

## V14.1 Documentação de Proteção de Dados

Um pré-requisito essencial para conseguir proteger os dados é categorizar quais dados devem ser considerados sensíveis. Provavelmente haverá diferentes níveis de sensibilidade e, para cada nível, os controles necessários para proteger os dados nesse nível serão diferentes.

Existem vários regulamentos e leis de privacidade que afetam a forma como as aplicações devem abordar o armazenamento, uso e transmissão de informações pessoais sensíveis. Esta seção não tenta mais duplicar esses tipos de proteção de dados ou legislação de privacidade, mas foca em considerações técnicas chave para proteger dados sensíveis. Por favor, consulte as leis e regulamentos locais, e consulte um especialista em privacidade qualificado ou um advogado, conforme necessário.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **14.1.1** | Verifique se todos os dados sensíveis criados e processados pela aplicação foram identificados e classificados em níveis de proteção. Isso inclui dados que são apenas codificados e, portanto, facilmente decodificados, como strings Base64 ou a carga (payload) em texto simples (plaintext) dentro de um JWT. Os níveis de proteção precisam levar em consideração quaisquer regulamentações e normas de proteção de dados e privacidade com os quais a aplicação é obrigada a cumprir. | 2 |
| **14.1.2** | Verifique se todos os níveis de proteção de dados sensíveis têm um conjunto documentado de requisitos de proteção. Isso deve incluir (mas não se limitar a) requisitos relacionados a criptografia geral, verificação de integridade, retenção, como os dados devem ser registrados (logged), controles de acesso a dados sensíveis em registros, criptografia em nível de banco de dados, tecnologias de privacidade e melhoria de privacidade a serem usadas e outros requisitos de confidencialidade. | 2 |

## V14.2 Proteção Geral de Dados

Esta seção contém vários requisitos práticos relacionados à proteção de dados. A maioria é específica a problemas particulares, como o vazamento de dados não intencional, mas há também um requisito geral para implementar controles de proteção baseados no nível de proteção exigido para cada item de dados.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **14.2.1** | Verifique se dados sensíveis são enviados ao servidor apenas no corpo da mensagem HTTP ou em campos de cabeçalho, e que a URL e a query string (string de consulta) não contenham informações sensíveis, como uma chave de API ou um token de sessão. | 1 |
| **14.2.2** | Verifique se a aplicação evita que dados sensíveis sejam armazenados em cache em componentes do servidor, como balanceadores de carga e caches de aplicação, ou garante que os dados sejam eliminados com segurança após o uso. | 2 |
| **14.2.3** | Verifique se dados sensíveis definidos não são enviados a partes não confiáveis (por exemplo, rastreadores de usuário/user trackers) para prevenir a coleta indesejada de dados fora do controle da aplicação. | 2 |
| **14.2.4** | Verifique se os controles em torno de dados sensíveis relacionados à criptografia, verificação de integridade, retenção, como os dados devem ser registrados (logged), controles de acesso em torno de dados sensíveis em logs, tecnologias de privacidade e melhoria de privacidade, são implementados conforme definido na documentação para o nível de proteção de dados específico. | 2 |
| **14.2.5** | Verifique se os mecanismos de cache são configurados para armazenar em cache apenas respostas que possuam o content type (tipo de conteúdo) esperado para aquele recurso e não contenham conteúdo dinâmico e sensível. O servidor web deve retornar uma resposta 404 ou 302 quando um arquivo inexistente for acessado, em vez de retornar um arquivo válido diferente. Isso deve evitar ataques de Engano de Cache Web (Web Cache Deception attacks). | 3 |
| **14.2.6** | Verifique se a aplicação retorna apenas os dados sensíveis mínimos necessários para a funcionalidade da aplicação. Por exemplo, retornar apenas alguns dos dígitos de um número de cartão de crédito e não o número completo. Se os dados completos forem exigidos, eles deverão ser mascarados na interface do usuário a menos que o usuário os visualize especificamente. | 3 |
| **14.2.7** | Verifique se as informações sensíveis estão sujeitas à classificação de retenção de dados, garantindo que os dados desatualizados ou desnecessários sejam excluídos automaticamente, em um cronograma definido ou conforme a situação exigir. | 3 |
| **14.2.8** | Verifique se as informações sensíveis são removidas dos metadados de arquivos enviados por usuários, a menos que o usuário tenha consentido com o armazenamento. | 3 |

## V14.3 Proteção de Dados no Lado do Cliente (Client-side)

Esta seção contém requisitos para prevenir que dados vazem de maneiras específicas no lado do cliente ou agente do usuário (user agent) de uma aplicação.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **14.3.1** | Verifique se os dados autenticados são apagados do armazenamento do cliente, como o DOM do navegador, após o cliente ou a sessão ser finalizada. O campo de cabeçalho de resposta HTTP 'Clear-Site-Data' pode ajudar com isso, mas o lado do cliente também deve conseguir limpar os dados se a conexão com o servidor não estiver disponível quando a sessão for encerrada. | 1 |
| **14.3.2** | Verifique se a aplicação define campos de cabeçalho de resposta HTTP anticanche adequados (ex., Cache-Control: no-store) para que dados sensíveis não sejam cacheados em navegadores. | 2 |
| **14.3.3** | Verifique se os dados armazenados no armazenamento do navegador (como localStorage, sessionStorage, IndexedDB ou cookies) não contêm dados sensíveis, com exceção de tokens de sessão. | 2 |

## Referências

Para mais informações, veja também:

* [Consider using the Security Headers website to check security and anti-caching header fields](https://securityheaders.com/)
* [Documentation about anti-caching headers by Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
* [OWASP Secure Headers project](https://owasp.org/www-project-secure-headers/)
* [OWASP Privacy Risks Project](https://owasp.org/www-project-top-10-privacy-risks/)
* [OWASP User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [Australian Privacy Principle 11 - Security of personal information](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-11-app-11-security-of-personal-information)
* [European Union General Data Protection Regulation (GDPR) overview](https://www.edps.europa.eu/data-protection_en)
* [European Union Data Protection Supervisor - Internet Privacy Engineering Network](https://www.edps.europa.eu/data-protection/ipen-internet-privacy-engineering-network_en)
* [Information on the "Clear-Site-Data" header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data)
* [White paper on Web Cache Deception](https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack-wp.pdf)