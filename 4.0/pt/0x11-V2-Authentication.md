# V2 Autenticação

## Objetivo de controle

Autenticação é o ato de estabelecer ou confirmar que alguém (ou algo) é autêntico e que as afirmações feitas por uma pessoa ou sobre um dispositivo são corretas, resistentes à representação e impedem a recuperação ou interceptação de senhas.

Quando o ASVS foi lançado pela primeira vez, nome de usuário + senha era a forma mais comum de autenticação fora dos sistemas de alta segurança. A autenticação multifator (MFA) era comumente aceita nos círculos de segurança, mas raramente exigida em outros lugares. À medida que o número de violações de senha aumentava, a ideia de que os nomes de usuário são de alguma forma confidenciais e as senhas desconhecidas tornou muitos controles de segurança insustentáveis. Por exemplo, o NIST 800-63 considera nomes de usuário e autenticação baseada em conhecimento (KBA) como informações públicas, SMS e notificações por e-mail como [tipos de autenticadores "restritos"](https://pages.nist.gov/800-63-FAQ/#q-b1) e senhas como pré-violadas. Essa realidade torna os autenticadores baseados em conhecimento, a recuperação de SMS e e-mail, o histórico de senhas, a complexidade e os controles de rotação inúteis. Esses controles sempre foram menos úteis,

De todos os capítulos do ASVS, os capítulos de autenticação e gestão de sessão foram os que mais mudaram. A adoção de práticas de liderança eficazes e baseadas em evidências será um desafio para muitos, e isso é perfeitamente aceitável. Temos que começar a transição para um futuro pós-senha agora.

## NIST 800-63 — Padrão de autenticação moderno e baseado em evidências

[NIST 800-63b](https://pages.nist.gov/800-63-3/sp800-63b.html) é um padrão moderno baseado em evidências e representa o melhor conselho disponível, independentemente da aplicabilidade. O padrão é útil para todas as organizações em todo o mundo, mas é particularmente relevante para as agências dos EUA e aquelas que lidam com agências dos EUA.

A terminologia NIST 800-63 pode ser um pouco confusa no início, especialmente se estiver acostumado apenas com autenticação de nome de usuário + senha. Avanços na autenticação moderna são necessários, por isso temos que introduzir uma terminologia que se tornará comum no futuro, mas entendemos a dificuldade de compreensão até que o setor se estabeleça nesses novos termos. Fornecemos um glossário no final deste capítulo para ajudar. Reformulamos muitos requisitos para satisfazer a intenção do requisito, em vez da letra do requisito. Por exemplo, o ASVS usa o termo "senha" quando o NIST usa "segredo memorizado" neste padrão.

Autenticação ASVS V2, gestão de sessão V3 e, em menor grau, controles de acesso V4 foram adaptados para ser um subconjunto compatível de controles NIST 800-63b selecionados, focados em ameaças comuns e vulnerabilidades de autenticação comumente exploradas. Quando a conformidade total com o NIST 800-63 for necessária, consulte o NIST 800-63.

### Selecionando um nível NIST AAL apropriado

O Application Security Verification Standard tentou mapear os requisitos ASVS L1 para NIST AAL1, L2 para AAL2 e L3 para AAL3. No entanto, a abordagem do ASVS Nível 1 como controles "essenciais" pode não ser necessariamente o nível AAL correto para verificar uma aplicação ou API. Por exemplo, se a aplicação for uma aplicação de Nível 3 ou tiver requisitos regulatórios para ser AAL3, o Nível 3 deve ser escolhido nos capítulos V2 e V3 Gestão de Sessões. A escolha do Nível de Asserção de Autenticação (AAL) compatível com NIST deve ser realizada conforme as diretrizes NIST 800-63b, conforme estabelecido em *Selecionar AAL* na [Seção 6.2 do NIST 800-63b](https://pages.nist.gov/800 -63-3/sp800-63-3.html#AAL_CYOA).

## Legenda

As aplicações sempre podem exceder os requisitos do nível atual, especialmente se a autenticação moderna estiver no roteiro de uma aplicação. Anteriormente, o ASVS exigia MFA obrigatório. O NIST não requer MFA obrigatório. Portanto, usamos uma designação opcional neste capítulo para indicar onde o ASVS incentiva, mas não requer um controle. As seguintes chaves são usadas ao longo deste padrão:

| Marcar | Descrição |
| :--: | :-- |
| | Não é necessário |
| o | Recomendado, mas não obrigatório |
| ✓ | Obrigatório |

## V2.1 Segurança de senha

As senhas, chamadas "Memorized Secrets" pelo NIST 800-63, incluem senhas, PINs, padrões de desbloqueio, escolha o gatinho correto ou outro elemento de imagem e frases secretas. Eles são geralmente considerados "algo que você conhece" e frequentemente usados como autenticadores de fator único. Existem desafios significativos para o uso contínuo da autenticação de fator único, incluindo bilhões de nomes de usuários e senhas válidos divulgados na Internet, senhas padrão ou fracas, tabelas arco-íris e dicionários ordenados das senhas mais comuns.

As aplicações devem incentivar fortemente os usuários a se inscreverem na autenticação multifator e devem permitir que os usuários reutilizem tokens que já possuem, como tokens FIDO ou U2F, ou se conectem a um provedor de serviços de credencial que forneça autenticação multifator.

Provedores de serviços de credenciais (CSPs) fornecem identidade federada para usuários. Os usuários geralmente têm mais de uma identidade com vários CSPs, como uma identidade corporativa usando Azure AD, Okta, Ping Identity ou Google, ou identidade de consumidor usando Facebook, Twitter, Google ou WeChat, para citar apenas algumas alternativas comuns. Esta lista não é um endosso dessas empresas ou serviços, mas simplesmente um incentivo para que os desenvolvedores considerem a realidade de que muitos usuários têm muitas identidades estabelecidas. As organizações devem considerar a integração com identidades de usuário existentes, conforme o perfil de risco da força de comprovação de identidade do CSP. Por exemplo, é improvável que uma organização governamental aceite uma identidade de mídia social como um login para sistemas confidenciais, pois é fácil criar identidades falsas ou jogar fora,

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.1.1** | Verifique se as senhas definidas pelo usuário têm pelo menos 12 caracteres (após a combinação de vários espaços). ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.2** | Verifique se senhas com pelo menos 64 caracteres são permitidas e se senhas com mais de 128 caracteres são negadas. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.3** | Verifique se o truncamento de senha não é executado. No entanto, vários espaços consecutivos podem ser substituídos por um único espaço. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.4** | Verifique se qualquer caractere Unicode imprimível, incluindo caracteres neutros de idioma, como espaços e Emojis, são permitidos em senhas. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.5** | Verifique se os usuários podem alterar suas senhas. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.6** | Verifique se a funcionalidade de alteração de senha requer a senha atual e nova do usuário. | ✓ | ✓ | ✓ | 620 | 5.1.1.2 |
| **2.1.7** | Verifique se as senhas enviadas durante o registro da conta, login e alteração de senha são verificadas em relação a um conjunto de senhas violadas localmente (como as 1.000 ou 10.000 senhas mais comuns que correspondem à política de senha do sistema) ou usando uma API externa. Se estiver usando uma API, uma prova de conhecimento zero ou outro mecanismo deve ser usado para garantir que a senha de texto simples não seja enviada ou usada na verificação do status de violação da senha. Se a senha for violada, a aplicação deve exigir que o usuário defina uma nova senha não violada. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.8** | Verifique se um medidor de força da senha é fornecido para ajudar os usuários a definir uma senha mais forte. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.9** | Verifique se não há regras de composição de senha limitando o tipo de caracteres permitidos. Não deve haver nenhum requisito para letras maiúsculas ou minúsculas, números ou caracteres especiais. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.10** | Verifique se não há rotação periódica de credenciais ou requisitos de histórico de senha. | ✓ | ✓ | ✓ | 263 | 5.1.1.2 |
| **2.1.11** | Verifique se a funcionalidade "colar", auxiliares de senha do navegador e gerenciadores de senha externos são permitidos. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |
| **2.1.12** | Verifique se o usuário pode optar por visualizar temporariamente toda a senha mascarada ou visualizar temporariamente o último caractere digitado da senha em plataformas que não possuem essa funcionalidade integrada. | ✓ | ✓ | ✓ | 521 | 5.1.1.2 |

Nota: O objetivo de permitir que o usuário visualize a sua senha ou veja o último caractere temporariamente é melhorar a usabilidade do input de credenciais, particularmente em relação ao uso de senhas mais longas, frases secretas e gerenciadores de senhas. Outro motivo para incluir o requisito é impedir ou evitar relatórios de teste que exigem desnecessariamente que as organizações substituam o comportamento do campo de senha da plataforma integrada para remover essa experiência de segurança moderna e amigável.

## V2.2 Segurança geral do autenticador

A agilidade do autenticador é essencial para aplicações preparados para o futuro. Refatore os verificadores de aplicações para permitir autenticadores adicionais conforme as preferências do usuário, bem como permitir a retirada de autenticadores obsoletos ou inseguros de maneira ordenada.

O NIST considera e-mail e SMS como [tipos de autenticador "restritos"](https://pages.nist.gov/800-63-FAQ/#q-b1) e provavelmente serão removidos do NIST 800-63 e, assim, o ASVS em algum momento no futuro. As candidaturas devem planear um roteiro que não implique a utilização de email ou SMS.

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.2.1** | Verifique se os controles antiautomação são eficazes na mitigação de testes de credenciais violadas, força bruta e ataques de bloqueio de conta. Esses controles incluem o bloqueio das senhas violadas mais comuns, bloqueios suaves, limitação de taxa, CAPTCHA, atrasos cada vez maiores entre tentativas, restrições de endereço IP ou restrições baseadas em risco, como localização, primeiro login num dispositivo, tentativas recentes de desbloquear a conta, ou similar. Verifique se não é possível mais de 100 tentativas com falha por hora numa única conta. | ✓ | ✓ | ✓ | 307 | 5.2.2 / 5.1.1.2 / 5.1.4.2 / 5.1.5.2 |
| **2.2.2** | Verifique se o uso de autenticadores fracos (como SMS e e-mail) é limitado a verificação secundária e aprovação de transações e não como substituto para métodos de autenticação mais seguros. Verifique se métodos mais fortes são oferecidos antes de métodos fracos, se os usuários estão cientes dos riscos ou se as medidas adequadas estão em vigor para limitar os riscos de comprometimento da conta. | ✓ | ✓ | ✓ | 304 | 5.2.10 |
| **2.2.3** | Verifique se as notificações seguras são enviadas aos usuários após atualizações nos detalhes de autenticação, como redefinições de credenciais, alterações de e-mail ou endereço, login de locais desconhecidos ou arriscados. O uso de notificações push — em vez de SMS ou e-mail — é preferível, mas na ausência de notificações push, SMS ou e-mail é aceitável, desde que nenhuma informação confidencial seja divulgada na notificação. | ✓ | ✓ | ✓ | 620 | |
| **2.2.4** | Verifique a resistência à representação contra phishing, como o uso de autenticação multifator, dispositivos criptográficos com intenção (como chaves conectadas com um push para autenticar) ou em níveis AAL mais altos, certificados do lado do cliente. | | | ✓ | 308 | 5.2.5 |
| **2.2.5** | Verifique se onde um Provedor de Serviços de Credenciais (CSP) e a aplicação que verifica a autenticação estão separados, o TLS mutuamente autenticado está em vigor entre os dois pontos de extremidade. | | | ✓ | 319 | 5.2.6 |
| **2.2.6** | Verifique a resistência à reprodução por meio do uso obrigatório de dispositivos de senhas descartáveis (OTP), autenticadores criptográficos ou códigos de pesquisa. | | | ✓ | 308 | 5.2.8 |
| **2.2.7** | Verifique a intenção de autenticação exigindo a input de um token OTP ou ação iniciada pelo usuário, como pressionar um botão numa chave de hardware FIDO. | | | ✓ | 308 | 5.2.9 |

## V2.3 Ciclo de vida do autenticador

Autenticadores são senhas, soft tokens, tokens de hardware e dispositivos biométricos. O ciclo de vida dos autenticadores é crítico para a segurança de uma aplicação — se qualquer pessoa pode registrar uma conta sem evidência de identidade, pode haver pouca confiança na declaração de identidade. Para sites de mídia social como o Reddit, tudo bem. Para sistemas bancários, um maior foco no registro e emissão de credenciais e dispositivos é fundamental para a segurança da aplicação.

Observação: as senhas não devem ter um tempo de vida máximo ou estar sujeitas à rotação de senha. As senhas devem ser verificadas quanto a violação, não substituídas regularmente.

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.3.1** | Verifique se as senhas iniciais ou os códigos de ativação gerados pelo sistema DEVEM ser gerados aleatoriamente de forma segura, DEVEM ter pelo menos 6 caracteres e PODEM conter letras e números e expiram após um curto período de tempo. Esses segredos iniciais não devem ser permitidos para se tornar a senha de longo prazo. | ✓ | ✓ | ✓ | 330 | 5.1.1.2 / A.3 |
| **2.3.2** | Verifique se há suporte para inscrição e uso de dispositivos de autenticação fornecidos pelo usuário, como tokens U2F ou FIDO. | | ✓ | ✓ | 308 | 6.1.3 |
| **2.3.3** | Verifique se as instruções de renovação são enviadas com tempo suficiente para renovar os autenticadores com limite de tempo. | | ✓ | ✓ | 287 | 6.1.4 |

## V2.4 Armazenamento de credenciais

Arquitetos e desenvolvedores devem aderir a esta seção ao criar ou refatorar o código. Esta seção só pode ser totalmente verificada usando a revisão do código-fonte ou por meio de testes seguros de unidade, ou integração. O teste de penetração não consegue identificar nenhum desses problemas.

A lista de funções de derivação de chave unidirecional aprovadas é detalhada na seção 5.1.1.2 do NIST 800-63 B e em [BSI Kryptographische Verfahren: Empfehlungen und Schlussellängen (2018)](https://www.bsi.bund.de/ SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile). O algoritmo nacional ou regional mais recente e os padrões de comprimento de chave podem ser escolhidos no lugar dessas opções.

Esta seção não pode ser testada quanto à penetração, então os controles não são marcados como L1. No entanto, esta seção é de vital importância para a segurança das credenciais se forem roubadas, portanto, se for bifurcar o ASVS para uma arquitetura ou diretriz de codificação, ou lista de verificação de revisão de código-fonte, coloque esses controles de volta em L1 na sua versão privada.

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.4.1** | Verifique se as senhas são armazenadas de forma resistente a ataques off-line. As senhas DEVEM ser salted e hash usando uma derivação de chave unidirecional aprovada ou função de hashing de senha. As funções de derivação de chave e hash de senha usam uma senha, um sal e um fator de custo como inputs ao gerar um hash de senha. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.2** | Verifique se o sal tem pelo menos 32 bits de comprimento e é escolhido arbitrariamente para minimizar as colisões de valor de sal entre os hashes armazenados. Para cada credencial, um valor salt único e o hash resultante DEVEM ser armazenados. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.3** | Verifique se PBKDF2 é usado, a contagem de iteração DEVE ser tão grande quanto o desempenho do servidor de verificação permitir, normalmente pelo menos 100.000 iterações. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.4** | Verifique se o bcrypt é usado, o fator de trabalho DEVE ser tão grande quanto o desempenho do servidor de verificação permitir, com um mínimo de 10. ([C6](https://owasp.org/www-project-proactive-controls/#div -numeração)) | | ✓ | ✓ | 916 | 5.1.1.2 |
| **2.4.5** | Verifique se uma iteração adicional de uma função de derivação de chave é executada, usando um valor salt que é secreto e conhecido apenas pelo verificador. Gere o valor salt usando um gerador de bit aleatório aprovado [SP 800-90Ar1] e forneça pelo menos a segurança mínima especificada na última revisão do SP 800-131A. O valor salt secreto DEVERÁ ser armazenado separadamente das senhas com hash (por exemplo, num dispositivo especializado como um módulo de segurança de hardware). | | ✓ | ✓ | 916 | 5.1.1.2 |

Quando os padrões dos EUA são mencionados, um padrão regional ou local pode ser usado no lugar, ou em adição ao padrão dos EUA, conforme necessário.

## V2.5 Recuperação de credenciais

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.5.1** | Verifique se um segredo inicial de ativação ou recuperação gerado pelo sistema não é enviado em texto não criptografado ao usuário. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.2** | Verifique se dicas de senha ou autenticação baseada em conhecimento (as chamadas "perguntas secretas") não estão presentes. | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.3** | Verifique se a recuperação da credencial de senha não revela a senha atual de forma alguma. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.4** | Verifique se contas compartilhadas ou padrão não estão presentes (por exemplo, "root", "admin" ou "sa"). | ✓ | ✓ | ✓ | 16 | 5.1.1.2 / A.3 |
| **2.5.5** | Verifique se um fator de autenticação é alterado ou substituído, o usuário é notificado sobre esse evento. | ✓ | ✓ | ✓ | 304 | 6.1.2.3 |
| **2.5.6** | Verifique a senha esquecida e outros caminhos de recuperação usam um mecanismo de recuperação seguro, como OTP baseado em tempo (TOTP) ou outro token flexível, push móvel ou outro mecanismo de recuperação offline. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 640 | 5.1.1.2 |
| **2.5.7** | Verifique se os fatores de autenticação OTP ou multifator são perdidos, se a prova de identidade é realizada no mesmo nível que durante o registro. | | ✓ | ✓ | 308 | 6.1.2.3 |

## Verificador secreto de pesquisa V2.6

Os segredos de pesquisa são listas pré-geradas de códigos secretos, como números de autorização de transação (TAN), códigos de recuperação de mídia social ou uma grade contendo um conjunto de valores aleatórios. Estes são distribuídos de forma segura para os usuários. Esses códigos de pesquisa são usados uma vez e, uma vez usados, a lista secreta de pesquisa é descartada. Esse tipo de autenticador é considerado "algo que você tem".

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.6.1** | Verifique se os segredos de pesquisa podem ser usados apenas uma vez. | | ✓ | ✓ | 308 | 5.1.2.2 |
| **2.6.2** | Verifique se os segredos de pesquisa têm aleatoriedade suficiente (112 bits de entropia) ou, se tiverem menos de 112 bits de entropia, salteados com um sal exclusivo e aleatório de 32 bits e hash com um hash unidirecional aprovado. | | ✓ | ✓ | 330 | 5.1.2.2 |
| **2.6.3** | Verifique se os segredos de pesquisa são resistentes a ataques offline, como valores previsíveis. | | ✓ | ✓ | 310 | 5.1.2.2 |

## V2.7 Verificador fora de banda

No passado, um verificador comum fora de banda seria um e-mail ou SMS contendo um link de redefinição de senha. Os invasores usam esse mecanismo fraco para redefinir contas que ainda não controlam, como assumir o controle da conta de e-mail de uma pessoa e reutilizar qualquer link de redefinição descoberto. Existem maneiras melhores de lidar com a verificação fora da banda.

Autenticadores seguros fora da banda são dispositivos físicos que podem se comunicar com o verificador por um canal secundário seguro. Os exemplos incluem notificações push para dispositivos móveis. Esse tipo de autenticador é considerado "algo que você tem". Quando um usuário deseja autenticar, a aplicação de verificação envia uma mensagem para o autenticador fora de banda por meio de uma conexão com o autenticador direta ou indiretamente por um serviço terceirizado. A mensagem contém um código de autenticação (normalmente um número aleatório de seis dígitos ou uma caixa de diálogo de aprovação modal). A aplicação verificador espera receber o código de autenticação por meio do canal primário e compara o hash do valor recebido com o hash do código de autenticação original. Se forem iguais, o verificador fora da banda pode presumir que o usuário foi autenticado.

O ASVS assume que apenas alguns desenvolvedores desenvolverão novos autenticadores fora de banda, como notificações push e, assim, os seguintes controles ASVS se aplicam a verificadores, como API de autenticação, aplicações e implementações de logon único. Se estiver desenvolvendo um novo autenticador fora de banda, consulte NIST 800-63B § 5.1.3.1.

Autenticadores inseguros fora de banda, como e-mail e VOIP, não são permitidos. A autenticação PSTN e SMS são atualmente "restritas" pelo NIST e devem ser substituídas em favor de notificações por push ou similares. Se você precisar usar autenticação fora de banda por telefone ou SMS, consulte o § 5.1.3.3.

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.7.1** | Verifique se os autenticadores de texto não criptografado fora da banda (NIST "restrito"), como SMS ou PSTN, não são oferecidos por padrão e alternativas mais fortes, como notificações por push, são oferecidas primeiro. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.2** | Verifique se o verificador fora de banda expira solicitações, códigos ou tokens de autenticação fora de banda após 10 minutos. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.3** | Verifique se as solicitações, códigos ou tokens de autenticação do verificador fora de banda podem ser usados apenas uma vez e apenas para a solicitação de autenticação original. | ✓ | ✓ | ✓ | 287 | 5.1.3.2 |
| **2.7.4** | Verifique se o autenticador e o verificador fora da banda se comunicam por um canal independente seguro. | ✓ | ✓ | ✓ | 523 | 5.1.3.2 |
| **2.7.5** | Verifique se o verificador fora da banda retém apenas uma versão com hash do código de autenticação. | | ✓ | ✓ | 256 | 5.1.3.2 |
| **2.7.6** | Verifique se o código de autenticação inicial é gerado por um gerador de número aleatório seguro, contendo pelo menos 20 bits de entropia (normalmente, um número aleatório de seis dígitos é suficiente). | | ✓ | ✓ | 310 | 5.1.3.2 |

## V2.8 Verificador Único

Senhas únicas de fator único (OTPs) são tokens físicos ou flexíveis que exibem um desafio único pseudoaleatório em constante mudança. Esses dispositivos tornam o phishing (personificação) difícil, mas não impossível. Esse tipo de autenticador é considerado "algo que você tem". Os tokens multifatores são semelhantes aos OTPs de fator único, mas exigem a inserção de um código PIN válido, desbloqueio biométrico, inserção USB ou emparelhamento NFC, ou algum valor adicional (como calculadoras de assinatura de transação) para criar o OTP final.

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.8.1** | Verifique se os OTPs baseados em tempo têm um tempo de vida definido antes de expirar. | ✓ | ✓ | ✓ | 613 | 5.1.4.2 / 5.1.5.2 |
| **2.8.2** | Verifique se as chaves simétricas usadas para verificar os OTPs enviados são altamente protegidas, por exemplo, usando um módulo de segurança de hardware ou armazenamento de chave baseado em sistema operacional seguro. | | ✓ | ✓ | 320 | 5.1.4.2 / 5.1.5.2|
| **2.8.3** | Verifique se algoritmos criptográficos aprovados são usados na geração, propagação e verificação de OTPs. | | ✓ | ✓ | 326 | 5.1.4.2 / 5.1.5.2 |
| **2.8.4** | Verifique se o OTP baseado em tempo pode ser usado apenas uma vez no período de validade. | | ✓ | ✓ | 287 | 5.1.4.2 / 5.1.5.2 |
| **2.8.5** | Verifique se um token OTP multifator baseado em tempo é reutilizado durante o período de validade, ele é registrado e rejeitado com notificações seguras sendo enviadas ao proprietário do dispositivo. | | ✓ | ✓ | 287 | 5.1.5.2 |
| **2.8.6** | Verifique se o gerador OTP físico de fator único pode ser revogado em caso de roubo ou outra perda. Assegure-se de que a revogação entre em vigor imediatamente nas sessões de login, independentemente do local. | | ✓ | ✓ | 613 | 5.2.1 |
| **2.8.7** | Verifique se os autenticadores biométricos estão limitados ao uso apenas como fatores secundários em conjunto com algo que você possui e algo que você conhece. | | o | ✓ | 308 | 5.2.3 |

## V2.9 Verificador Criptográfico

As chaves de segurança criptográficas são cartões inteligentes ou chaves FIDO, nas quais o usuário deve conectar ou emparelhar o dispositivo criptográfico ao computador para concluir a autenticação. Os verificadores enviam um nonce de desafio para os dispositivos criptográficos ou software, e o dispositivo ou software calcula uma resposta com base numa chave criptográfica armazenada com segurança.

Os requisitos para dispositivos e software criptográficos de fator único e dispositivos e software criptográficos multifatores são os mesmos, pois a verificação do autenticador criptográfico prova a posse do fator de autenticação.

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.9.1** | Verifique se as chaves criptográficas usadas na verificação são armazenadas com segurança e protegidas contra divulgação, como o uso de um Módulo de plataforma confiável (TPM) ou Módulo de segurança de hardware (HSM) ou um serviço de sistema operacional que pode usar esse armazenamento seguro. | | ✓ | ✓ | 320 | 5.1.7.2 |
| **2.9.2** | Verifique se o nonce de desafio tem pelo menos 64 bits de comprimento e é estatisticamente exclusivo ou exclusivo durante a vida útil do dispositivo criptográfico. | | ✓ | ✓ | 330 | 5.1.7.2 |
| **2.9.3** | Verifique se os algoritmos criptográficos aprovados são usados na geração, propagação e verificação. | | ✓ | ✓ | 327 | 5.1.7.2 |

## V2.10 Autenticação de Serviço

Esta seção não é passível de teste de penetração, portanto, não possui nenhum requisito L1. No entanto, se usado numa arquitetura, codificação ou revisão de código seguro, assuma que o software (assim como Java Key Store) é o requisito mínimo em L1. O armazenamento de segredos em texto não criptografado não é aceitável em nenhuma circunstância.

| # | Descrição | L1 | L2 | L3 | CWE | [NIST §](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| :---: | :--- | :---: | :---:| :---: | :---: | :---: |
| **2.10.1** | Verifique se os segredos intra-serviço não dependem de credenciais imutáveis, como senhas, chaves de API ou contas compartilhadas com acesso privilegiado. | | SO assistido | HSM | 287 | 5.1.1.1 |
| **2.10.2** | Verifique se as senhas são necessárias para autenticação de serviço, a conta de serviço usada não é uma credencial padrão. (por exemplo, root/root ou admin/admin são padrão em alguns serviços durante a instalação). | | SO assistido | HSM | 255 | 5.1.1.1 |
| **2.10.3** | Verifique se as senhas são armazenadas com proteção suficiente para evitar ataques de recuperação offline, incluindo acesso ao sistema local. | | SO assistido | HSM | 522 | 5.1.1.1 |
| **2.10.4** | Verifique se senhas, integrações com bancos de dados e sistemas de terceiros, sementes e segredos internos e chaves de API são gerenciados com segurança e não incluídos no código-fonte ou armazenados em repositórios de código-fonte. Esse armazenamento DEVE resistir a ataques offline. O uso de um armazenamento de chave de software seguro (L1), TPM de hardware ou um HSM (L3) é recomendado para armazenamento de senha. | | SO assistido | HSM | 798 | |

## Requisitos adicionais da agência dos EUA

As agências dos EUA têm requisitos obrigatórios relativos ao NIST 800-63. O Application Security Verification Standard sempre foi sobre os 80% dos controles que se aplicam a quase 100% das aplicações, e não os últimos 20% dos controles avançados ou aqueles que têm aplicabilidade limitada. Como tal, o ASVS é um subconjunto estrito do NIST 800-63, especialmente para as classificações IAL1/2 e AAL1/2, mas não é suficientemente abrangente, particularmente no que diz respeito às classificações IAL3/AAL3.

Nós instamos fortemente as agências governamentais dos EUA a revisar e implementar o NIST 800-63 na sua totalidade.

## Glossário de termos

| Termo | Significado |
| -- | -- |
| PSC | Provedor de Serviços de Credencial também chamado de Provedor de Identidade |
| Autenticador | Código que autentica uma senha, token, MFA, declaração federada e assim por diante. |
| Verificador | "Uma entidade que verifica a identidade do reclamante verificando a posse e o controle do reclamante de um ou dois autenticadores usando um protocolo de autenticação. Para fazer isso, o verificador também pode precisar validar as credenciais que vinculam o(s) autenticador(es) ao identificador do assinante e verificar o seu estado" |
| OTP | Senha de uso único |
| SFA | Autenticadores de fator único, como algo que conheça (segredos memorizados, senhas, senhas, PINs), algo que você é (biometria, impressão digital, digitalizações faciais) ou algo que possui (tokens OTP, um dispositivo criptográfico como um cartão inteligente) , |
| AMF | Autenticação multifator, que inclui dois ou mais fatores únicos |

## Referências

Para mais informações, consulte também:

* [NIST 800-63 — Diretrizes de identidade digital](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-3.pdf)
* [NIST 800-63 A — Inscrição e prova de identidade](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63a.pdf)
* [NIST 800-63 B — Autenticação e gestão do ciclo de vida](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
* [NIST 800-63 C — Federação e Asserções](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63c.pdf)
* [NIST 800-63 FAQ](https://pages.nist.gov/800-63-FAQ/)
* [OWASP Testing Guide 4.0: Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
* [Cheat Sheet OWASP — Armazenamento de senha](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP Cheat Sheet — Esqueci a senha](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
* [Cheat Sheet OWASP — Escolhendo e usando perguntas de segurança](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)