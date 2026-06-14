# V6 Autenticação

## Objetivo de Controle

Autenticação é o processo de estabelecer ou confirmar a autenticidade de um indivíduo ou dispositivo. Envolve a verificação de reivindicações (claims) feitas por uma pessoa ou sobre um dispositivo, garantindo a resistência à falsificação de identidade (impersonation) e evitando a recuperação ou interceptação de senhas.

O [NIST SP 800-63](https://pages.nist.gov/800-63-3/) é um padrão moderno, baseado em evidências, que é valioso para organizações em todo o mundo, mas é particularmente relevante para agências dos EUA e para aqueles que interagem com elas.

Embora muitos dos requisitos neste capítulo baseiem-se na segunda seção do padrão (conhecido como NIST SP 800-63B "Digital Identity Guidelines - Authentication and Lifecycle Management"), o capítulo foca em ameaças comuns e fraquezas de autenticação frequentemente exploradas. Ele não tenta cobrir de forma abrangente todos os pontos do padrão. Para casos em que a conformidade total com o NIST SP 800-63 for necessária, consulte o NIST SP 800-63.

Além disso, a terminologia do NIST SP 800-63 pode, às vezes, ser diferente, e este capítulo frequentemente usa uma terminologia mais comumente compreendida para melhorar a clareza.

Um recurso comum de aplicações mais avançadas é a capacidade de adaptar os estágios de autenticação exigidos com base em vários fatores de risco. Esse recurso é abordado no capítulo "Autorização", uma vez que esses mecanismos também precisam ser considerados para decisões de autorização.

## V6.1 Documentação de Autenticação

Esta seção contém requisitos que detalham a documentação de autenticação que deve ser mantida para uma aplicação. Isso é crucial para implementar e avaliar como os controles de autenticação relevantes devem ser configurados.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **6.1.1** | Verifique se a documentação da aplicação define como os controles, como limitação de taxa (rate limiting), antiautomação e resposta adaptativa, são usados para se defender contra ataques como preenchimento de credenciais (credential stuffing) e força bruta de senha. A documentação deve deixar claro como esses controles são configurados e impedir o bloqueio malicioso de contas (account lockout). | 1 |
| **6.1.2** | Verifique se uma lista de palavras específicas do contexto está documentada para impedir o seu uso em senhas. A lista pode incluir permutações de nomes da organização, nomes de produtos, identificadores de sistema, codinomes de projeto, nomes de departamentos ou funções, e similares. | 2 |
| **6.1.3** | Verifique se, caso a aplicação inclua vários caminhos de autenticação, todos estejam documentados juntamente com os controles de segurança e a força de autenticação que devem ser aplicados consistentemente em todos eles. | 2 |

## V6.2 Segurança de Senha

As senhas, chamadas de "Segredos Memorizados" (Memorized Secrets) pelo NIST SP 800-63, incluem senhas, frases secretas (passphrases), PINs, padrões de desbloqueio e escolher o gatinho correto ou outro elemento de imagem. Geralmente, são consideradas "algo que você sabe" e costumam ser usadas como um mecanismo de autenticação de fator único.

Como tal, esta seção contém requisitos para garantir que as senhas sejam criadas e tratadas de forma segura. A maioria dos requisitos é L1, pois eles são mais importantes nesse nível. Do L2 em diante, exigem-se mecanismos de autenticação multifator, onde as senhas podem ser um desses fatores.

Os requisitos nesta seção relacionam-se principalmente à [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) do [Guia do NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **6.2.1** | Verifique se as senhas definidas pelo usuário têm pelo menos 8 caracteres de comprimento, embora um mínimo de 15 caracteres seja fortemente recomendado. | 1 |
| **6.2.2** | Verifique se os usuários podem alterar sua senha. | 1 |
| **6.2.3** | Verifique se a funcionalidade de alteração de senha exige a senha atual e a nova senha do usuário. | 1 |
| **6.2.4** | Verifique se as senhas enviadas durante o registro da conta ou na alteração da senha são verificadas em um conjunto disponível de, pelo menos, as 3000 senhas mais comuns que correspondem à política de senha da aplicação, por exemplo, o comprimento mínimo. | 1 |
| **6.2.5** | Verifique se senhas de qualquer composição podem ser usadas, sem regras que limitem o tipo de caracteres permitidos. Não deve haver requisito para um número mínimo de letras maiúsculas ou minúsculas, números ou caracteres especiais. | 1 |
| **6.2.6** | Verifique se os campos de entrada de senha usam type=password para mascarar a entrada. As aplicações podem permitir que o usuário visualize temporariamente toda a senha mascarada ou o último caractere digitado da senha. | 1 |
| **6.2.7** | Verifique se a funcionalidade de "colar" (paste), ajudantes de senha de navegador e gerenciadores de senha externos são permitidos. | 1 |
| **6.2.8** | Verifique se a aplicação verifica a senha do usuário exatamente como recebida dele, sem nenhuma modificação como truncamento ou transformação de maiúsculas e minúsculas (case transformation). | 1 |
| **6.2.9** | Verifique se senhas de pelo menos 64 caracteres são permitidas. | 2 |
| **6.2.10** | Verifique se a senha de um usuário permanece válida até que seja descoberta como comprometida ou o usuário a troque. A aplicação não deve exigir a rotação periódica de credenciais. | 2 |
| **6.2.11** | Verifique se a lista documentada de palavras específicas do contexto é usada para evitar que senhas fáceis de adivinhar sejam criadas. | 2 |
| **6.2.12** | Verifique se as senhas enviadas durante o registro da conta ou alterações de senha são verificadas em relação a um conjunto de senhas vazadas (breached passwords). | 2 |

## V6.3 Segurança Geral de Autenticação

Esta seção contém requisitos gerais para a segurança dos mecanismos de autenticação, além de estabelecer as diferentes expectativas para os níveis. Aplicações L2 devem forçar o uso de autenticação multifator (MFA). Aplicações L3 devem usar autenticação baseada em hardware, executada em um ambiente de execução atestado e confiável (TEE). Isso pode incluir passkeys vinculadas a dispositivos (device-bound), autenticadores aplicados com Nível de Garantia (LoA) Alto do eIDAS, autenticadores com nível de garantia NIST Authenticator Assurance Level 3 (AAL3) ou um mecanismo equivalente.

Embora esta seja uma postura relativamente agressiva em relação à MFA, é fundamental elevar o padrão em torno disso para proteger os usuários, e qualquer tentativa de relaxar esses requisitos deve ser acompanhada de um plano claro sobre como os riscos em torno da autenticação serão mitigados, levando em consideração as orientações e pesquisas do NIST sobre o tópico.

Observe que, no momento do lançamento, o NIST SP 800-63 considera o e-mail como um mecanismo de autenticação [inaceitável](https://pages.nist.gov/800-63-FAQ/#q-b11) ([cópia arquivada](https://web.archive.org/web/20250330115328/https://pages.nist.gov/800-63-FAQ/#q-b11)).

Os requisitos nesta seção se relacionam a uma variedade de seções do [Guia do NIST](https://pages.nist.gov/800-63-3/sp800-63b.html), incluindo: [&sect; 4.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#421-permitted-authenticator-types), [&sect; 4.3.1](https://pages.nist.gov/800-63-3/sp800-63b.html#431-permitted-authenticator-types), [&sect; 5.2.2](https://pages.nist.gov/800-63-3/sp800-63b.html#522-rate-limiting-throttling) e [&sect; 6.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-612-post-enrollment-binding).

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **6.3.1** | Verifique se os controles para prevenir ataques, como preenchimento de credenciais e força bruta de senha, são implementados de acordo com a documentação de segurança da aplicação. | 1 |
| **6.3.2** | Verifique se contas de usuário padrão (ex., "root", "admin" ou "sa") não estão presentes na aplicação ou estão desativadas. | 1 |
| **6.3.3** | Verifique se um mecanismo de autenticação multifator ou uma combinação de mecanismos de autenticação de fator único deve ser usado para acessar a aplicação. Para o L3, um dos fatores deve ser um mecanismo de autenticação baseado em hardware que ofereça resistência contra comprometimento e falsificação (impersonation) contra ataques de phishing, enquanto verifica a intenção de autenticar por meio da exigência de uma ação iniciada pelo usuário (como o pressionamento de um botão em uma chave de hardware FIDO ou telefone celular). Relaxar qualquer uma das considerações neste requisito exige uma justificativa totalmente documentada e um conjunto abrangente de controles mitigadores. | 2 |
| **6.3.4** | Verifique se, caso a aplicação inclua vários caminhos de autenticação, não há caminhos não documentados e que os controles de segurança e a força de autenticação são impostos consistentemente. | 2 |
| **6.3.5** | Verifique se os usuários são notificados sobre tentativas suspeitas de autenticação (bem-sucedidas ou mal-sucedidas). Isso pode incluir tentativas de autenticação de um local ou cliente incomum, autenticação parcialmente bem-sucedida (apenas um dos múltiplos fatores), uma tentativa de autenticação após um longo período de inatividade ou uma autenticação bem-sucedida após várias tentativas malsucedidas. | 3 |
| **6.3.6** | Verifique se o e-mail não é usado como mecanismo de autenticação de fator único nem multifator. | 3 |
| **6.3.7** | Verifique se os usuários são notificados após atualizações de detalhes de autenticação, como redefinições de credenciais ou modificação do nome de usuário ou endereço de e-mail. | 3 |
| **6.3.8** | Verifique se usuários válidos não podem ser deduzidos de desafios de autenticação malsucedidos, como baseando-se em mensagens de erro, códigos de resposta HTTP ou diferentes tempos de resposta. A funcionalidade de registro e esquecimento de senha também deve ter essa proteção. | 3 |

## V6.4 Ciclo de Vida e Recuperação do Fator de Autenticação

Os fatores de autenticação podem incluir senhas, tokens de software, tokens de hardware e dispositivos biométricos. Lidar com o ciclo de vida desses mecanismos de forma segura é fundamental para a segurança de uma aplicação, e esta seção inclui requisitos relacionados a isso.

Os requisitos nesta seção relacionam-se principalmente à [&sect; 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecretver) ou [&sect; 6.1.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#replacement) do [Guia do NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **6.4.1** | Verifique se as senhas iniciais geradas pelo sistema ou códigos de ativação são gerados aleatoriamente de forma segura, seguem a política de senha existente e expiram após um curto período ou depois de serem usados inicialmente. Esses segredos iniciais não podem se tornar a senha de longo prazo. | 1 |
| **6.4.2** | Verifique se não estão presentes dicas de senha ou autenticação baseada em conhecimento (as chamadas "perguntas secretas"). | 1 |
| **6.4.3** | Verifique se um processo seguro para a redefinição de uma senha esquecida está implementado, o qual não ignora (bypass) nenhum mecanismo de autenticação multifator habilitado. | 2 |
| **6.4.4** | Verifique se, em caso de perda de um fator de autenticação multifator, a comprovação de identidade é realizada no mesmo nível que durante a inscrição (enrollment). | 2 |
| **6.4.5** | Verifique se as instruções de renovação para os mecanismos de autenticação que expiram são enviadas com tempo suficiente para serem realizadas antes que o antigo mecanismo expire, configurando lembretes automatizados se necessário. | 3 |
| **6.4.6** | Verifique se os usuários administrativos podem iniciar o processo de redefinição de senha para o usuário, mas que isso não permita que eles alterem ou escolham a senha do usuário. Isso evita uma situação em que eles conheçam a senha do usuário. | 3 |

## V6.5 Requisitos Gerais de Autenticação Multifator

Esta seção fornece orientações gerais que serão relevantes para vários métodos diferentes de autenticação multifator.

Os mecanismos incluem:

* Segredos de Consulta (Lookup Secrets)
* Senhas de Uso Único Baseadas em Tempo (TOTPs)
* Mecanismos Fora de Banda (Out-of-Band)

Os segredos de consulta são listas pré-geradas de códigos secretos, semelhantes a Números de Autorização de Transação (TAN), códigos de recuperação de mídia social ou uma grade contendo um conjunto de valores aleatórios. Este tipo de mecanismo de autenticação é considerado "algo que você possui" porque os códigos deliberadamente não são memoráveis, logo precisarão ser armazenados em algum lugar.

As Senhas de Uso Único Baseadas em Tempo (TOTPs) são tokens físicos ou de software que exibem um desafio pseudoaleatório de uso único em constante mudança. Este tipo de mecanismo de autenticação é considerado "algo que você possui". TOTPs multifator são semelhantes aos TOTPs de fator único, mas requerem a inserção de um código PIN válido, desbloqueio biométrico, inserção de USB, emparelhamento NFC ou algum valor adicional (como calculadoras de assinatura de transação) para criar a Senha de Uso Único (OTP) final.

Detalhes sobre os mecanismos out-of-band serão fornecidos na próxima seção.

Os requisitos nestas seções relacionam-se principalmente à [&sect; 5.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#-512-look-up-secrets), [&sect; 5.1.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-513-out-of-band-devices), [&sect; 5.1.4.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5142-single-factor-otp-verifiers), [&sect; 5.1.5.2](https://pages.nist.gov/800-63-3/sp800-63b.html#5152-multi-factor-otp-verifiers), [&sect; 5.2.1](https://pages.nist.gov/800-63-3/sp800-63b.html#521-physical-authenticators) e [&sect; 5.2.3](https://pages.nist.gov/800-63-3/sp800-63b.html#523-use-of-biometrics) do [Guia do NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **6.5.1** | Verifique se os segredos de consulta, solicitações ou códigos de autenticação out-of-band e senhas de uso único baseadas em tempo (TOTPs) podem ser usados com sucesso apenas uma vez. | 2 |
| **6.5.2** | Verifique se, quando armazenados no backend da aplicação, os segredos de consulta com menos de 112 bits de entropia (19 caracteres alfanuméricos aleatórios ou 34 dígitos aleatórios) recebem hash usando um algoritmo aprovado de hash para armazenamento de senhas que incorpore um salt aleatório de 32 bits. Uma função de hash padrão pode ser usada se o segredo tiver 112 bits de entropia ou mais. | 2 |
| **6.5.3** | Verifique se os segredos de consulta, código de autenticação out-of-band e sementes de senha de uso único baseada em tempo são gerados usando um Gerador de Números Pseudoaleatórios Criptograficamente Seguro (CSPRNG) para evitar valores previsíveis. | 2 |
| **6.5.4** | Verifique se os segredos de consulta e os códigos de autenticação out-of-band têm um mínimo de 20 bits de entropia (normalmente 4 caracteres alfanuméricos aleatórios ou 6 dígitos aleatórios são suficientes). | 2 |
| **6.5.5** | Verifique se as solicitações de autenticação out-of-band, códigos ou tokens, bem como as senhas de uso único baseadas em tempo (TOTPs) têm uma vida útil (lifetime) definida. As solicitações out-of-band devem ter uma vida útil máxima de 10 minutos e as TOTPs uma vida útil máxima de 30 segundos. | 2 |
| **6.5.6** | Verifique se qualquer fator de autenticação (incluindo dispositivos físicos) pode ser revogado em caso de roubo ou outra perda. | 3 |
| **6.5.7** | Verifique se os mecanismos de autenticação biométrica são usados ​​apenas como fatores secundários em conjunto com algo que você possui ou algo que você sabe. | 3 |
| **6.5.8** | Verifique se as senhas de uso único baseadas em tempo (TOTPs) são checadas com base em uma fonte de tempo de um serviço confiável e não de um tempo não confiável ou fornecido pelo cliente. | 3 |

## V6.6 Mecanismos de Autenticação Fora de Banda (Out-of-Band)

Geralmente, isso envolve o servidor de autenticação comunicando-se com um dispositivo físico por meio de um canal secundário seguro. Por exemplo, enviando notificações por push para dispositivos móveis. Esse tipo de mecanismo de autenticação é considerado "algo que você possui".

Mecanismos de autenticação out-of-band inseguros, como e-mail e VOIP, não são permitidos. A autenticação por PSTN e SMS é atualmente considerada um [mecanismo de autenticação "restrito"](https://pages.nist.gov/800-63-FAQ/#q-b01) pelo NIST e deve ser preterida em favor de Senhas de Uso Único Baseadas em Tempo (TOTPs), um mecanismo criptográfico, ou similar. A seção [&sect; 5.1.3.3](https://pages.nist.gov/800-63-3/sp800-63b.html#-5133-authentication-using-the-public-switched-telephone-network) do NIST SP 800-63B recomenda tratar os riscos de troca de dispositivo, troca de SIM, portabilidade de número ou outro comportamento anormal, caso a autenticação telefônica ou SMS out-of-band deva absolutamente ser suportada. Embora esta seção do ASVS não exija isso como um requisito, não tomar essas precauções para um aplicativo L2 sensível ou um aplicativo L3 deve ser visto como um sinal de alerta vermelho significativo.

Observe que o NIST também forneceu recentemente orientações que [desencorajam o uso de notificações push](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/#fig-3). Embora esta seção do ASVS não faça isso, é importante estar ciente dos riscos de "bombardeio de notificações push" (push bombing).

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **6.6.1** | Verifique se os mecanismos de autenticação usando a Rede Telefônica Pública Comutada (PSTN) para entregar Senhas de Uso Único (OTPs) via telefone ou SMS são oferecidos apenas quando o número de telefone foi validado previamente, se métodos alternativos e mais fortes (como Senhas de Uso Único Baseadas em Tempo) também são oferecidos e se o serviço fornece informações sobre seus riscos de segurança aos usuários. Para aplicações L3, telefone e SMS não devem estar disponíveis como opções. | 2 |
| **6.6.2** | Verifique se as solicitações de autenticação out-of-band, códigos ou tokens estão vinculados à solicitação de autenticação original para a qual foram gerados e não são utilizáveis para uma solicitação anterior ou subsequente. | 2 |
| **6.6.3** | Verifique se um mecanismo de autenticação out-of-band baseado em código está protegido contra ataques de força bruta usando limitação de taxa (rate limiting). Considere também o uso de um código com pelo menos 64 bits de entropia. | 2 |
| **6.6.4** | Verifique se, quando notificações push são usadas para autenticação multifator, a limitação de taxa é usada para evitar ataques de bombardeio de push (push bombing). A correspondência de números (number matching) também pode mitigar esse risco. | 3 |

## V6.7 Mecanismos de Autenticação Criptográfica

Mecanismos de autenticação criptográfica incluem smart cards ou chaves FIDO, onde o usuário precisa conectar ou emparelhar o dispositivo criptográfico ao computador para concluir a autenticação. O servidor de autenticação enviará um nonce de desafio ao dispositivo ou software criptográfico, e o dispositivo ou software calcula uma resposta baseada em uma chave criptográfica armazenada de forma segura. Os requisitos nesta seção fornecem orientações específicas de implementação para esses mecanismos, sendo que a orientação sobre algoritmos criptográficos é abordada no capítulo "Criptografia".

Quando chaves compartilhadas ou secretas são usadas para autenticação criptográfica, elas devem ser armazenadas usando os mesmos mecanismos de outros segredos do sistema, conforme documentado na seção "Gerenciamento de Segredos" no capítulo "Configuração".

Os requisitos nesta seção relacionam-se principalmente à [&sect; 5.1.7.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sfcdv) do [Guia do NIST](https://pages.nist.gov/800-63-3/sp800-63b.html).

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **6.7.1** | Verifique se os certificados usados para verificar afirmações (assertions) de autenticação criptográfica são armazenados de forma que os proteja contra modificações. | 3 |
| **6.7.2** | Verifique se o nonce de desafio tem pelo menos 64 bits de comprimento, e é estatisticamente único ou único durante toda a vida útil do dispositivo criptográfico. | 3 |

## V6.8 Autenticação com um Provedor de Identidade (Identity Provider)

Provedores de Identidade (IdPs) oferecem identidade federada para os usuários. Os usuários frequentemente terão mais de uma identidade em vários IdPs, como uma identidade corporativa usando o Azure AD, Okta, Ping Identity ou Google, ou identidade de consumidor usando Facebook, Twitter, Google ou WeChat, para citar apenas algumas alternativas comuns. Esta lista não é um endosso a essas empresas ou serviços, mas simplesmente um encorajamento para que os desenvolvedores considerem a realidade de que muitos usuários possuem várias identidades estabelecidas. As organizações devem considerar a integração com identidades de usuários existentes, de acordo com o perfil de risco da força da comprovação de identidade do IdP. Por exemplo, é improvável que uma organização governamental aceite uma identidade de mídia social como login para sistemas sensíveis, já que é fácil criar identidades falsas ou descartáveis, enquanto uma empresa de jogos para dispositivos móveis pode precisar se integrar com grandes plataformas de mídia social para expandir sua base ativa de jogadores.

O uso seguro de provedores de identidade externos exige configuração e verificação cuidadosas para prevenir a falsificação de identidade ou asserções forjadas. Esta seção fornece requisitos para mitigar esses riscos.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **6.8.1** | Verifique se, caso a aplicação suporte múltiplos provedores de identidade (IdPs), a identidade do usuário não pode ser falsificada (spoofed) por meio de outro provedor de identidade suportado (por exemplo, usando o mesmo identificador de usuário). A mitigação padrão seria a aplicação registrar e identificar o usuário usando uma combinação do ID do IdP (servindo como um namespace) e o ID do usuário no IdP. | 2 |
| **6.8.2** | Verifique se a presença e a integridade de assinaturas digitais em asserções de autenticação (por exemplo, em JWTs ou asserções SAML) são sempre validadas, rejeitando quaisquer asserções que não estejam assinadas ou possuam assinaturas inválidas. | 2 |
| **6.8.3** | Verifique se asserções SAML são processadas de maneira única e usadas apenas uma vez dentro do período de validade para prevenir ataques de repetição (replay attacks). | 2 |
| **6.8.4** | Verifique se, caso uma aplicação use um Provedor de Identidade (IdP) separado e espere uma força de autenticação, métodos ou atualidade específicos para funções específicas, a aplicação verifique isso usando as informações retornadas pelo IdP. Por exemplo, se o OIDC for usado, isso pode ser obtido validando as claims (reivindicações) do ID Token, como 'acr', 'amr' e 'auth_time' (se presentes). Se o IdP não fornecer essas informações, a aplicação deve ter uma abordagem de contingência documentada que assume que o mecanismo de autenticação de força mínima foi usado (por exemplo, autenticação de fator único usando nome de usuário e senha). | 2 |

## Referências

Para mais informações, veja também:

* [NIST SP 800-63 - Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST SP 800-63B - Authentication and Lifecycle Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST SP 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Web Security Testing Guide: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/04-Authentication_Testing)
* [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [OWASP Choosing and Using Security Questions Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
* [CISA Guidance on "Number Matching"](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf)
* [Details on the FIDO Alliance](https://fidoalliance.org/)