# V8 Autorização

## Objetivo de Controle

A autorização garante que o acesso seja concedido apenas aos consumidores permitidos (usuários, servidores e outros clientes). Para aplicar o Princípio do Menor Privilégio (Principle of Least Privilege - POLP), aplicações verificadas devem atender aos seguintes requisitos de alto nível:

* Documentar regras de autorização, incluindo fatores de tomada de decisão e contextos ambientais.
* Os consumidores devem ter acesso apenas aos recursos permitidos por seus direitos definidos.

## V8.1 Documentação de Autorização

A documentação abrangente de autorização é essencial para garantir que as decisões de segurança sejam aplicadas de forma consistente, passíveis de auditoria e alinhadas com as políticas organizacionais. Isso reduz o risco de acesso não autorizado, tornando os requisitos de segurança claros e acionáveis ​​para desenvolvedores, administradores e testadores.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **8.1.1** | Verifique se a documentação de autorização define regras para restringir o acesso em nível de função e específico a dados com base nas permissões do consumidor e nos atributos do recurso. | 1 |
| **8.1.2** | Verifique se a documentação de autorização define regras para restrições de acesso em nível de campo (tanto para leitura quanto escrita) com base nas permissões do consumidor e atributos do recurso. Note que essas regras podem depender de outros valores de atributos do objeto de dados relevante, como estado ou status. | 2 |
| **8.1.3** | Verifique se a documentação da aplicação define os atributos ambientais e contextuais (incluindo, mas não se limitando a, hora do dia, localização do usuário, endereço IP ou dispositivo) que são usados na aplicação para tomar decisões de segurança, incluindo as pertinentes à autenticação e autorização. | 3 |
| **8.1.4** | Verifique se a documentação de autenticação e autorização define como fatores ambientais e contextuais são usados na tomada de decisões, além da autorização em nível de função, específica a dados e em nível de campo. Isso deve incluir os atributos avaliados, os limites de risco e as ações tomadas (ex., permitir, desafiar, negar, autenticação step-up). | 3 |

## V8.2 Design Geral de Autorização

A implementação de controles de autorização granulares no nível de função, dados e campos garante que os consumidores possam acessar apenas o que lhes foi explicitamente concedido.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **8.2.1** | Verifique se a aplicação garante que o acesso em nível de função seja restrito a consumidores com permissões explícitas. | 1 |
| **8.2.2** | Verifique se a aplicação garante que o acesso específico a dados seja restrito a consumidores com permissões explícitas a itens de dados específicos para mitigar referência direta insegura a objeto (IDOR) e autorização em nível de objeto quebrada (BOLA). | 1 |
| **8.2.3** | Verifique se a aplicação garante que o acesso em nível de campo seja restrito a consumidores com permissões explícitas a campos específicos para mitigar autorização em nível de propriedade de objeto quebrada (BOPLA). | 2 |
| **8.2.4** | Verifique se os controles de segurança adaptativos baseados nos atributos ambientais e contextuais do consumidor (como hora do dia, localização, endereço IP ou dispositivo) são implementados para decisões de autenticação e autorização, conforme definido na documentação da aplicação. Esses controles devem ser aplicados quando o consumidor tentar iniciar uma nova sessão e também durante uma sessão existente. | 3 |

## V8.3 Autorização em Nível de Operação

A aplicação imediata de mudanças de autorização na camada (tier) apropriada da arquitetura de uma aplicação é crucial para evitar ações não autorizadas, especialmente em ambientes dinâmicos.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **8.3.1** | Verifique se a aplicação impõe as regras de autorização em uma camada de serviço confiável e não depende de controles que um consumidor não confiável possa manipular, como JavaScript no lado do cliente. | 1 |
| **8.3.2** | Verifique se as alterações aos valores sobre os quais as decisões de autorização são tomadas são aplicadas imediatamente. Nos casos onde as mudanças não podem ser aplicadas imediatamente (como quando se depende de dados em tokens autocontidos), deve haver controles mitigadores para alertar quando um consumidor realizar uma ação para a qual ele não está mais autorizado a fazer, e para reverter a mudança. Note que essa alternativa não mitigaria o vazamento de informações. | 3 |
| **8.3.3** | Verifique se o acesso a um objeto é baseado nas permissões do sujeito (ex., consumidor) originador, não nas permissões de qualquer intermediário ou serviço atuando em nome deles. Por exemplo, se um consumidor chama um web service usando um token autocontido para autenticação, e o serviço então solicita dados de um serviço diferente, o segundo serviço usará o token do consumidor, em vez de um token machine-to-machine do primeiro serviço, para tomar decisões de permissão. | 3 |

## V8.4 Outras Considerações sobre Autorização

Considerações adicionais de autorização, particularmente para interfaces administrativas e ambientes multilocatário (multi-tenant), ajudam a evitar acessos não autorizados.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **8.4.1** | Verifique se aplicações multilocatário (multi-tenant) usam controles cruzados de inquilinos (cross-tenant) para garantir que as operações do consumidor nunca afetem inquilinos com os quais eles não têm permissão para interagir. | 2 |
| **8.4.2** | Verifique se o acesso a interfaces administrativas incorpora várias camadas de segurança, incluindo a verificação contínua da identidade do consumidor, avaliação da postura de segurança do dispositivo e análise de risco contextual, garantindo que a localização da rede ou endpoints confiáveis não sejam os únicos fatores para a autorização, embora possam reduzir a probabilidade de acesso não autorizado. | 3 |

## Referências

Para mais informações, veja também:

* [OWASP Web Security Testing Guide: Authorization](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/05-Authorization_Testing)
* [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)