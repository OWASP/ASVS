# V3 Gestão de sessão

## Objetivo de controle

Um dos principais componentes de qualquer aplicação baseada na Web ou API com estado é o mecanismo pelo qual ele controla e mantém o estado de um usuário ou dispositivo que interage com ele. A gestão de sessão altera um protocolo sem estado para com estado, o que é crítico para diferenciar diferentes usuários ou dispositivos.

Certifique-se de que uma aplicação verificado atenda aos seguintes requisitos de gestão de sessão de alto nível:

* As sessões são únicas para cada indivíduo e não podem ser adivinhadas ou compartilhadas.
* As sessões são invalidadas quando não são mais necessárias e expiram durante períodos de inatividade.

Conforme observado anteriormente, esses requisitos foram adaptados para serem um subconjunto compatível de controles NIST 800-63b selecionados, focados em ameaças comuns e vulnerabilidades de autenticação comumente exploradas. Os requisitos de verificação anteriores foram retirados, desduplicados ou, geralmente, adaptados para serem fortemente alinhados com a intenção dos [NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) requisitos.

## Requisitos de verificação de segurança

## V3.1 Fundamentos de Segurança de Gestão de Sessão

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.1.1** | Verifique se a aplicação nunca revela tokens de sessão em parâmetros de URL. | ✓ | ✓ | ✓ | 598 | |

## V3.2 Ligação de Sessão

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.2.1** | Verifique se a aplicação gera um novo token de sessão na autenticação do usuário. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 384 | 7.1 |
| **3.2.2** | Verifique se os tokens de sessão possuem pelo menos 64 bits de entropia. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 331 | 7.1 |
| **3.2.3** | Verifique se a aplicação armazena apenas tokens de sessão no navegador usando métodos seguros, como cookies devidamente protegidos (consulte a seção 3.4) ou armazenamento de sessão HTML 5. | ✓ | ✓ | ✓ | 539 | 7.1 |
| **3.2.4** | Verifique se os tokens de sessão são gerados usando algoritmos criptográficos aprovados. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 331 | 7.1 |

O TLS ou outro canal de transporte seguro é obrigatório para a gestão de sessão. Isso é abordado no capítulo Segurança das Comunicações.

## V3.3 Encerramento da Sessão

Os session timeouts foram alinhados com o NIST 800-63, que permite session timeouts muito mais longos do que os tradicionalmente permitidos pelos padrões de segurança. As organizações devem revisar a tabela abaixo e, se um tempo limite mais longo for desejável com base no risco da aplicação, o valor NIST deve ser o limite superior dos tempos limite de inatividade da sessão.

L1 neste contexto é IAL1/AAL1, L2 é IAL2/AAL3, L3 é IAL3/AAL3. Para IAL2/AAL2 e IAL3/AAL3, o tempo limite de inatividade mais curto é o limite inferior de tempos de inatividade para ser desconectado ou autenticado novamente para retomar a sessão.

| # | Descrição  L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html)
| :---: |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :---: | :---:| :---: | :---: | :---: |
| **3.3.1** | Verifique se o logoff e a expiração invalidam o token de sessão, de modo que o botão Voltar ou uma parte confiável downstream não retome uma sessão autenticada, inclusive entre partes confiáveis. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering))              | ✓ | ✓ | ✓ | 613 | 7.1 |
| **3.3.2** | Se os autenticadores permitirem que os usuários permaneçam conectados, verifique se a reautenticação ocorre periodicamente quando usados ativamente ou após um período ocioso. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering))                                   | 30 dias | 12 horas ou 30 minutos de inatividade, 2FA opcional | 12 horas ou 15 minutos de inatividade, com 2FA | 613 | 7.2 |
| **3.3.3** | Verifique se a aplicação oferece a opção de encerrar todas as outras sessões ativas após uma alteração de senha bem-sucedida (incluindo alteração por redefinição/recuperação de senha) e se isso é eficaz na aplicação, no login federado (se houver) e em quaisquer partes confiáveis. | | ✓ | ✓ | 613 | |
| **3.3.4** | Verifique se os usuários podem visualizar e (tendo inserido novamente as credenciais de login) fazer logoff de qualquer ou de todas as sessões e dispositivos ativos no momento.                                                                                                         | | ✓ | ✓ | 613 | 7.1 |

## V3.4 Gestão de sessão baseado em cookies

| # | Descrição | L1 | L2 | L3 | CWE  | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: |:----:| :---: |
| **3.4.1** | Verifique se os tokens de sessão baseados em cookie têm o atributo 'Seguro' definido. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 614  | 7.1.1 |
| **3.4.2** | Verifique se os tokens de sessão baseados em cookie têm o atributo 'HttpOnly' definido. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1004 | 7.1.1 |
| **3.4.3** | Verifique se os tokens de sessão baseados em cookies utilizam o atributo 'SameSite' para limitar a exposição a ataques de falsificação de solicitação entre sites. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ |  16  | 7.1.1 |
| **3.4.4** | Verifique se os tokens de sessão baseados em cookie usam o prefixo "__Host-" para que os cookies sejam enviados apenas para o host que inicialmente definiu o cookie. | ✓ | ✓ | ✓ |  16  | 7.1.1 |
| **3.4.5** | Verifique se a aplicação é publicado sob um nome de domínio com outras aplicações que definem ou usam cookies de sessão que podem divulgar os cookies de sessão, defina o atributo path em tokens de sessão baseados em cookie usando o caminho mais preciso possível. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ |  16  | 7.1.1 |

## V3.5 Gestão de sessão baseado em token

A gestão de sessão baseado em token inclui chaves JWT, OAuth, SAML e API. Destas, as chaves de API são conhecidas por serem fracas e não devem ser usadas em novos códigos.

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.5.1** | Verifique se a aplicação permite que os usuários revoguem tokens OAuth que formam relacionamentos de confiança coma aplicaçãos vinculados. | | ✓ | ✓ | 290 | 7.1.2 |
| **3.5.2** | Verifique se a aplicação usa tokens de sessão em vez de chaves e segredos de API estáticos, exceto com implementações herdadas. | | ✓ | ✓ | 798 | |
| **3.5.3** | Verifique se os tokens de sessão sem estado usam assinaturas digitais, criptografia e outras contramedidas para proteger contra adulteração, envelopamento, repetição, cifra nula e ataques de substituição de chave. | | ✓ | ✓ | 345 | |

## V3.6 Reautenticação federada

Esta seção se refere àqueles que escrevem códigos de Parte Confiável (RP) ou Provedor de Serviços de Credenciais (CSP). Se depender do código que implementa esses recursos, certifique-se de que esses problemas sejam tratados corretamente.

| # | Descrição  L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :---: | :---:| :---: | :---: | :---: |
| **3.6.1** | Verifique se as Partes Confiáveis (RPs) especificam o tempo máximo de autenticação para Provedores de Serviços de Credenciais (CSPs) e se os CSPs autenticam novamente o usuário se eles não tiverem usado uma sessão dentro desse período. | | | ✓ | 613 | 7.2.1 |
| **3.6.2** | Verifique se os provedores de serviços de credenciais (CSPs) informam as partes confiáveis (RPs) sobre o último evento de autenticação, para permitir que os RPs determinem se precisam autenticar novamente o usuário.                     | | | ✓ | 613 | 7.2.1 |

## V3.7 Defesas contra exploits de gestão de sessão

Há um pequeno número de ataques de gestão de sessão, alguns relacionados à experiência do usuário (UX) das sessões. Anteriormente, com base nos requisitos da ISO 27002, o ASVS exigia o bloqueio de várias sessões simultâneas. Bloquear sessões simultâneas não é mais apropriado, não apenas porque os usuários modernos têm muitos dispositivos ou a aplicação é uma API sem uma sessão do navegador, mas na maioria dessas implementações, o último autenticador vence, que geralmente é o invasor. Esta seção fornece orientações importantes sobre dissuasão, atraso e detecção de ataques de gestão de sessão usando código.

### Descrição do ataque semi-aberto

No início de 2018, várias instituições financeiras foram comprometidas usando o que os invasores chamaram "ataques semiabertos". Este termo ficou preso na indústria. Os invasores atingiram várias instituições com diferentes bases de código proprietárias e, de fato, parecem diferentes bases de código dentro das mesmas instituições. O ataque semiaberto está explorando uma falha de padrão de design comumente encontrada em muitos sistemas existentes de autenticação, gestão de sessão e controle de acesso.

Os invasores iniciam um ataque semiaberto tentando bloquear, redefinir ou recuperar uma credencial. Um padrão de design de gestão de sessão popular reutiliza objetos/modelos de sessão de perfil de usuário entre código não autenticado, parcialmente autenticado (redefinições de senha, nome de usuário esquecido) e totalmente autenticado. Esse padrão de design preenche um objeto ou token de sessão válido contendo o perfil da vítima, incluindo hashes de senha e funções. Se as verificações de controle de acesso em controladores ou roteadores não verificarem corretamente se o usuário está totalmente conectado, o invasor poderá agir como o usuário. Os ataques podem incluir alterar a senha do usuário para um valor conhecido, atualizar o endereço de e-mail para executar uma redefinição de senha válida, desabilitar a autenticação multifator ou registrar um novo dispositivo MFA, revelar ou alterar chaves de API e assim por diante.

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **3.7.1** | Verifique se a aplicação garante uma sessão de login completa e válida ou requer reautenticação ou verificação secundária antes de permitir transações confidenciais ou modificações de conta. | ✓ | ✓ | ✓ | 306 | |

## Referências

Para mais informações, consulte também:

* [OWASP Testing Guide 4.0: Session Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/README.html)
* [Cheat Sheet de gestão de sessão OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
* [Detalhes do prefixo Set-Cookie __Host-](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#Directives)
