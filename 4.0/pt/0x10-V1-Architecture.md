# V4 Controle de Acesso

## Objetivo de controle

Autorização é o conceito de permitir acesso a recursos apenas para aqueles autorizados a usá-los. Certifique-se de que uma aplicação verificado atenda aos seguintes requisitos de alto nível:

* As pessoas que acessam recursos possuem credenciais válidas para fazê-lo.
* Os usuários estão associados a um conjunto bem definido de funções e privilégios.
* Os metadados de função e permissão são protegidos contra repetição ou adulteração.

## Requisitos de verificação de segurança

## V4.1 Projeto de controle de acesso geral

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.1.1** | Verifique se a aplicação impõe regras de controle de acesso numa camada de serviço confiável, especialmente se o controle de acesso do lado do cliente estiver presente e puder ser ignorado. | ✓ | ✓ | ✓ | 602 |
| **4.1.2** | Verifique se todos os atributos de usuário e dados e as informações de política usadas pelos controles de acesso não podem ser manipulados pelos usuários finais, a menos que especificamente autorizados. | ✓ | ✓ | ✓ | 639 |
| **4.1.3** | Verifique se existe o princípio do menor privilégio - os usuários só devem poder acessar funções, arquivos de dados, URLs, controladores, serviços e outros recursos, para os quais possuam autorização específica. Isso implica proteção contra falsificação e elevação de privilégio. ([C7](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |
| **4.1.4** | [EXCLUÍDO, DUPLICADO DE 4.1.3] | | | | |
| **4.1.5** | Verifique se os controles de acesso falham com segurança, inclusive quando ocorre uma exceção. ([C10](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 285 |

## V4.2 Controle de acesso de nível de operação

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.2.1** | Verifique se os dados confidenciais e as APIs estão protegidos contra ataques Insecure Direct Object Reference (IDOR) direcionados à criação, leitura, atualização e exclusão de registros, como criar ou atualizar o registro de outra pessoa, visualizar os registros de todos ou excluir todos os registros. | ✓ | ✓ | ✓ | 639 |
| **4.2.2** | Verifique se a aplicação ou estrutura impõe um forte mecanismo anti-CSRF para proteger a funcionalidade autenticada e se a antiautomação ou anti-CSRF eficaz protege a funcionalidade não autenticada. | ✓ | ✓ | ✓ | 352 |

## V4.3 Outras considerações de controle de acesso

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **4.3.1** | Verifique se as interfaces administrativas usam autenticação multifator apropriada para impedir o uso não autorizado. | ✓ | ✓ | ✓ | 419 |
| **4.3.2** | Verifique se a navegação no diretório está desativada, a menos que seja deliberadamente desejada. Além disso, as aplicações não devem permitir a descoberta ou divulgação de metadados de arquivo ou diretório, como pastas Thumbs.db, .DS_Store, .git ou .svn. | ✓ | ✓ | ✓ | 548 |
| **4.3.3** | Verifique se a aplicação possui autorização adicional (como intensificação ou autenticação adaptativa) para sistemas de baixo valor e/ou segregação de funções para aplicações de alto valor para impor controles antifraude de acordo com o risco da aplicação e fraudes anteriores. | | ✓ | ✓ | 732 |

## Referências

Para mais informações, consulte também:

* [OWASP Testing Guide 4.0: Authorization](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/05-Authorization_Testing/README.html)
* [OWASP Cheat Sheet: Access Control](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
* [OWASP CSRF Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [OWASP REST Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
