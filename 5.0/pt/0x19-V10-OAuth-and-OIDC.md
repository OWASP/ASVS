# V10 OAuth e OIDC

## Objetivo de Controle

O OAuth2 (referido como OAuth neste capítulo) é um framework padrão da indústria para autorização delegada. Por exemplo, usando o OAuth, uma aplicação cliente pode obter acesso a APIs (recursos do servidor) em nome de um usuário, desde que o usuário tenha autorizado a aplicação cliente a fazer isso.

Por si só, o OAuth não é projetado para autenticação de usuários. O framework OpenID Connect (OIDC) estende o OAuth adicionando uma camada de identidade de usuário sobre o OAuth. O OIDC fornece suporte para recursos que incluem informações de usuário padronizadas, Single Sign-On (SSO) e gerenciamento de sessão. Como o OIDC é uma extensão do OAuth, os requisitos de OAuth neste capítulo também se aplicam ao OIDC.

Os seguintes papéis (roles) são definidos no OAuth:

* O cliente OAuth é a aplicação que tenta obter acesso aos recursos do servidor (ex., chamando uma API usando o token de acesso emitido). O cliente OAuth geralmente é uma aplicação do lado do servidor (server-side).
    * Um cliente confidencial é um cliente capaz de manter a confidencialidade das credenciais que usa para se autenticar no servidor de autorização.
    * Um cliente público não é capaz de manter a confidencialidade das credenciais para autenticação no servidor de autorização. Portanto, em vez de se autenticar (ex., usando parâmetros 'client_id' e 'client_secret'), ele apenas se identifica (usando um parâmetro 'client_id').
* O servidor de recursos OAuth (Resource Server - RS) é a API do servidor que expõe os recursos aos clientes OAuth.
* O servidor de autorização OAuth (Authorization Server - AS) é uma aplicação de servidor que emite tokens de acesso aos clientes OAuth. Esses tokens de acesso permitem que os clientes OAuth acessem os recursos do RS, seja em nome de um usuário final ou em nome próprio do cliente OAuth. O AS é frequentemente uma aplicação separada, mas (se apropriado) pode ser integrado a um RS adequado.
* O proprietário do recurso (Resource Owner - RO) é o usuário final que autoriza os clientes OAuth a obter acesso limitado aos recursos hospedados no servidor de recursos em seu nome. O proprietário do recurso consente com esta autorização delegada interagindo com o servidor de autorização.

Os seguintes papéis são definidos no OIDC:

* A Relying Party (RP - Parte Confiável) é a aplicação cliente que solicita a autenticação do usuário final através do Provedor OpenID. Ela assume o papel de um cliente OAuth.
* O Provedor OpenID (OpenID Provider - OP) é um AS do OAuth que é capaz de autenticar o usuário final e fornecer as claims (reivindicações) OIDC a uma RP. O OP pode ser o provedor de identidade (IdP), mas em cenários federados, o OP e o provedor de identidade (onde o usuário final se autentica) podem ser aplicações de servidor diferentes.

O OAuth e o OIDC foram inicialmente projetados para aplicações de terceiros. Hoje, eles são frequentemente usados por aplicações próprias (first-party) também. No entanto, quando usados em cenários first-party, como autenticação e gerenciamento de sessão, o protocolo adiciona certa complexidade, o que pode introduzir novos desafios de segurança.

O OAuth e o OIDC podem ser usados para muitos tipos de aplicações, mas o foco para o ASVS e os requisitos neste capítulo está em aplicações web e APIs.

Como o OAuth e o OIDC podem ser considerados uma lógica acima das tecnologias web, os requisitos gerais de outros capítulos sempre se aplicam, e este capítulo não pode ser tirado de contexto.

Este capítulo aborda as melhores práticas atuais para OAuth2 e OIDC, alinhadas com as especificações encontradas em <https://oauth.net/2/> e <https://openid.net/developers/specs/>. Mesmo que as RFCs sejam consideradas maduras, elas são atualizadas com frequência. Portanto, é importante alinhar-se com as versões mais recentes ao aplicar os requisitos neste capítulo. Veja a seção de referências para mais detalhes.

Dada a complexidade da área, é de vital importância para uma solução segura de OAuth ou OIDC o uso de servidores de autorização conhecidos e padrão da indústria, além de aplicar a configuração de segurança recomendada.

A terminologia usada neste capítulo se alinha com as RFCs do OAuth e as especificações do OIDC, mas note que a terminologia do OIDC é usada apenas para requisitos específicos do OIDC; caso contrário, a terminologia do OAuth é usada.

No contexto do OAuth e OIDC, o termo "token" neste capítulo refere-se a:

* Tokens de acesso (Access tokens), que devem ser consumidos apenas pelo RS e podem ser tokens de referência validados via introspecção (introspection) ou tokens autocontidos (self-contained tokens) validados usando algum material criptográfico.
* Tokens de atualização (Refresh tokens), que devem ser consumidos apenas pelo servidor de autorização que emitiu o token.
* Tokens de ID OIDC (ID Tokens), que devem ser consumidos apenas pelo cliente que iniciou o fluxo de autorização.

Os níveis de risco para alguns dos requisitos neste capítulo dependem de o cliente ser um cliente confidencial ou considerado um cliente público. Uma vez que o uso de autenticação forte de cliente mitiga muitos vetores de ataque, alguns requisitos podem ser relaxados ao usar um cliente confidencial para aplicações de Nível 1 (L1).

## V10.1 Segurança Genérica de OAuth e OIDC

Esta seção cobre os requisitos arquitetônicos genéricos que se aplicam a todas as aplicações usando OAuth ou OIDC.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **10.1.1** | Verifique se os tokens são enviados apenas aos componentes que estritamente necessitam deles. Por exemplo, ao usar o padrão backend-for-frontend para aplicações JavaScript baseadas no navegador, os tokens de acesso e de atualização devem estar acessíveis apenas para o backend. | 2 |
| **10.1.2** | Verifique se o cliente apenas aceita valores do servidor de autorização (como o authorization code ou ID Token) se esses valores resultarem de um fluxo de autorização que foi iniciado pela mesma sessão do user agent e transação. Isso exige que segredos gerados pelo cliente, como o 'code_verifier' do proof key for code exchange (PKCE), o 'state' ou o 'nonce' do OIDC, não sejam adivinháveis, sejam específicos para a transação e estejam vinculados de forma segura tanto ao cliente quanto à sessão do user agent na qual a transação foi iniciada. | 2 |

## V10.2 Cliente OAuth

Estes requisitos detalham as responsabilidades das aplicações cliente OAuth. O cliente pode ser, por exemplo, um backend de servidor web (muitas vezes atuando como um Backend For Frontend, BFF), uma integração de serviço backend ou um Frontend Single Page Application (SPA, também conhecida como aplicação baseada em navegador).

Em geral, os clientes de backend são considerados clientes confidenciais e os clientes de frontend são considerados clientes públicos. No entanto, as aplicações nativas em execução no dispositivo do usuário final podem ser consideradas confidenciais ao usar o registro dinâmico de cliente (dynamic client registration) do OAuth.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **10.2.1** | Verifique se, caso o code flow seja usado, o cliente OAuth tem proteção contra ataques de falsificação de requisição baseados em navegador, comumente conhecidos como falsificação de requisição entre sites (Cross-Site Request Forgery - CSRF), que disparam solicitações de token, seja usando a funcionalidade proof key for code exchange (PKCE) ou verificando o parâmetro 'state' que foi enviado na solicitação de autorização. | 2 |
| **10.2.2** | Verifique se, caso o cliente OAuth possa interagir com mais de um servidor de autorização, ele possui uma defesa contra ataques de confusão (mix-up attacks). Por exemplo, ele pode exigir que o servidor de autorização retorne o valor do parâmetro 'iss' e validá-lo na resposta de autorização e na resposta de token. | 2 |
| **10.2.3** | Verifique se o cliente OAuth solicita apenas os escopos (ou outros parâmetros de autorização) necessários nas solicitações ao servidor de autorização. | 3 |

## V10.3 Servidor de Recursos OAuth

No contexto do ASVS e deste capítulo, o servidor de recursos (resource server) é uma API. Para fornecer acesso seguro, o servidor de recursos deve:

* Validar o token de acesso, de acordo com o formato do token e as especificações relevantes do protocolo, por exemplo, validação de JWT ou introspecção de token OAuth.
* Se for válido, aplicar decisões de autorização com base nas informações do token de acesso e nas permissões que foram concedidas. Por exemplo, o servidor de recursos precisa verificar se o cliente (agindo em nome do RO) está autorizado a acessar o recurso solicitado.

Portanto, os requisitos listados aqui são específicos de OAuth ou OIDC e devem ser executados após a validação do token e antes de realizar a autorização baseada em informações contidas no token.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **10.3.1** | Verifique se o servidor de recursos aceita apenas tokens de acesso que são destinados para uso com aquele serviço (audiência). A audiência (audience) pode ser incluída em um token de acesso estruturado (como a claim 'aud' no JWT), ou pode ser verificada usando o endpoint de introspecção do token. | 2 |
| **10.3.2** | Verifique se o servidor de recursos impõe decisões de autorização baseadas em claims do token de acesso que definem a autorização delegada. Se claims como 'sub', 'scope' e 'authorization_details' estiverem presentes, eles devem fazer parte da decisão. | 2 |
| **10.3.3** | Verifique se, caso uma decisão de controle de acesso exija a identificação de um usuário único a partir de um token de acesso (JWT ou resposta de introspecção de token relacionada), o servidor de recursos identifica o usuário a partir de claims que não possam ser reatribuídas a outros usuários. Normalmente, isso significa usar uma combinação das claims 'iss' e 'sub'. | 2 |
| **10.3.4** | Verifique se, caso o servidor de recursos exija força, métodos ou atualidade de autenticação específicos, ele verifica se o token de acesso apresentado satisfaz essas restrições. Por exemplo, se presentes, usando as claims OIDC 'acr', 'amr' e 'auth_time', respectivamente. | 2 |
| **10.3.5** | Verifique se o servidor de recursos impede o uso de tokens de acesso roubados ou a repetição (replay) de tokens de acesso (de partes não autorizadas) exigindo tokens de acesso restritos ao remetente (sender-constrained access tokens), seja via Mutual TLS para OAuth 2 ou OAuth 2 Demonstration of Proof of Possession (DPoP). | 3 |

## V10.4 Servidor de Autorização OAuth

Estes requisitos detalham as responsabilidades dos servidores de autorização OAuth, incluindo os Provedores OpenID.

Para autenticação do cliente, o método 'self_signed_tls_client_auth' é permitido de acordo com os pré-requisitos exigidos pela [seção 2.2](https://datatracker.ietf.org/doc/html/rfc8705#name-self-signed-certificate-mut) da [RFC 8705](https://datatracker.ietf.org/doc/html/rfc8705).

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **10.4.1** | Verifique se o servidor de autorização valida as URIs de redirecionamento (redirect URIs) com base em uma lista de permissões específica do cliente contendo URIs pré-registradas, usando comparação exata de strings. | 1 |
| **10.4.2** | Verifique se, caso o servidor de autorização retorne o código de autorização (authorization code) na resposta de autorização, este possa ser usado apenas uma vez para uma solicitação de token. Para a segunda solicitação válida com um código de autorização que já foi usado para emitir um token de acesso, o servidor de autorização deve rejeitar a solicitação de token e revogar quaisquer tokens emitidos relacionados ao código de autorização. | 1 |
| **10.4.3** | Verifique se o código de autorização tem vida útil curta. A vida útil máxima pode ser de até 10 minutos para aplicações L1 e L2 e de até 1 minuto para aplicações L3. | 1 |
| **10.4.4** | Verifique se, para um determinado cliente, o servidor de autorização permite apenas o uso de tipos de concessão (grants) que este cliente precisa utilizar. Note que os grants 'token' (Implicit flow) e 'password' (Resource Owner Password Credentials flow) não devem mais ser usados. | 1 |
| **10.4.5** | Verifique se o servidor de autorização mitiga os ataques de replay de token de atualização (refresh token) para clientes públicos, preferencialmente usando tokens de atualização restritos ao remetente (sender-constrained), ou seja, Demonstrating Proof of Possession (DPoP) ou Tokens de Acesso Vinculados a Certificado usando mutual TLS (mTLS). Para aplicações L1 e L2, a rotação de token de atualização (refresh token rotation) pode ser usada. Se a rotação de token de atualização for usada, o servidor de autorização deve invalidar o token de atualização após o uso e revogar todos os tokens de atualização para aquela autorização se um token de atualização já usado e invalidado for fornecido. | 1 |
| **10.4.6** | Verifique se, caso o grant do tipo 'code' seja usado, o servidor de autorização mitiga os ataques de interceptação do código de autorização exigindo o proof key for code exchange (PKCE). Para solicitações de autorização, o servidor de autorização deve exigir um valor 'code_challenge' válido e não deve aceitar o valor 'code_challenge_method' como 'plain'. Para uma solicitação de token, ele deve exigir a validação do parâmetro 'code_verifier'. | 2 |
| **10.4.7** | Verifique se, caso o servidor de autorização suporte registro dinâmico de cliente não autenticado (unauthenticated dynamic client registration), ele mitiga o risco de aplicações clientes maliciosas. Ele deve validar os metadados do cliente, como quaisquer URIs registradas, garantir o consentimento do usuário e avisar o usuário antes de processar uma solicitação de autorização com uma aplicação cliente não confiável. | 2 |
| **10.4.8** | Verifique se os tokens de atualização possuem uma expiração absoluta, inclusive se a expiração contínua (sliding expiration) de token de atualização for aplicada. | 2 |
| **10.4.9** | Verifique se os tokens de atualização e os tokens de acesso de referência podem ser revogados por um usuário autorizado usando a interface do usuário do servidor de autorização, para mitigar o risco de clientes maliciosos ou tokens roubados. | 2 |
| **10.4.10** | Verifique se o cliente confidencial é autenticado para as solicitações backchannel entre o cliente e o servidor de autorização, como solicitações de token, solicitações de autorização enviadas por push (PAR) e solicitações de revogação de token. | 2 |
| **10.4.11** | Verifique se a configuração do servidor de autorização atribui apenas os escopos (scopes) necessários ao cliente OAuth. | 2 |
| **10.4.12** | Verifique se, para um determinado cliente, o servidor de autorização permite apenas o valor de 'response_mode' que este cliente precisa utilizar. Por exemplo, fazendo com que o servidor de autorização valide esse valor em relação aos valores esperados ou usando solicitações de autorização enviadas por push (PAR) ou JWT-secured Authorization Request (JAR). | 3 |
| **10.4.13** | Verifique se o grant type 'code' é sempre usado em conjunto com as pushed authorization requests (PAR). | 3 |
| **10.4.14** | Verifique se o servidor de autorização emite apenas tokens de acesso restritos ao remetente (sender-constrained - Proof-of-Possession), seja com tokens de acesso vinculados a certificados usando mutual TLS (mTLS) ou tokens de acesso vinculados a DPoP (Demonstration of Proof of Possession). | 3 |
| **10.4.15** | Verifique se, para um cliente no lado do servidor (server-side, que não é executado no dispositivo do usuário final), o servidor de autorização garante que o valor do parâmetro 'authorization_details' provenha do backend do cliente e que o usuário não o tenha adulterado. Por exemplo, exigindo o uso de uma pushed authorization request (PAR) ou JWT-secured Authorization Request (JAR). | 3 |
| **10.4.16** | Verifique se o cliente é confidencial e o servidor de autorização exige o uso de métodos de autenticação de cliente fortes (baseados em criptografia de chave pública e resistentes a ataques de replay), como mutual TLS ('tls_client_auth', 'self_signed_tls_client_auth') ou JWT de chave privada ('private_key_jwt'). | 3 |

## V10.5 Cliente OIDC

Como a Relying Party (Parte Confiável) do OIDC age como um cliente OAuth, os requisitos da seção "Cliente OAuth" também se aplicam.

Note que a seção "Autenticação com um Provedor de Identidade" no capítulo "Autenticação" também contém requisitos gerais relevantes.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **10.5.1** | Verifique se o cliente (como Relying Party) mitiga os ataques de replay do ID Token. Por exemplo, garantindo que a claim 'nonce' no ID Token corresponda ao valor 'nonce' enviado na solicitação de autenticação para o Provedor OpenID (no OAuth2 referido como a solicitação de autorização enviada ao servidor de autorização). | 2 |
| **10.5.2** | Verifique se o cliente identifica o usuário de forma única a partir das claims do ID Token, geralmente a claim 'sub', a qual não pode ser reatribuída a outros usuários (no escopo de um provedor de identidade). | 2 |
| **10.5.3** | Verifique se o cliente rejeita as tentativas de um servidor de autorização malicioso de se passar por outro servidor de autorização através de metadados do servidor de autorização. O cliente deve rejeitar os metadados do servidor de autorização se o URL do emissor (issuer) nos metadados do servidor de autorização não corresponder exatamente ao URL do emissor pré-configurado esperado pelo cliente. | 2 |
| **10.5.4** | Verifique se o cliente valida se o ID Token tem a intenção de ser usado para aquele cliente (audiência), verificando se a claim 'aud' do token é igual ao valor 'client_id' para o cliente. | 2 |
| **10.5.5** | Verifique se, ao usar o logout back-channel do OIDC, a Relying Party mitiga a negação de serviço através de logout forçado e confusão cruzada de JWT (cross-JWT confusion) no fluxo de logout. O cliente deve verificar se o token de logout está digitado corretamente com um valor de 'logout+jwt', se contém a claim 'event' com o nome de membro correto e se não contém uma claim 'nonce'. Note que também é recomendado ter uma expiração curta (por exemplo, 2 minutos). | 2 |

## V10.6 Provedor OpenID

Como os Provedores OpenID agem como servidores de autorização OAuth, os requisitos da seção "Servidor de Autorização OAuth" também se aplicam.

Note que, se estiver usando o fluxo ID Token (não o fluxo de código), nenhum token de acesso é emitido e muitos dos requisitos para OAuth AS não são aplicáveis.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **10.6.1** | Verifique se o Provedor OpenID permite apenas os valores 'code', 'ciba', 'id_token' ou 'id_token code' para o modo de resposta (response mode). Note que 'code' é preferível a 'id_token code' (o fluxo Híbrido OIDC) e 'token' (qualquer fluxo Implícito) não deve ser usado. | 2 |
| **10.6.2** | Verifique se o Provedor OpenID mitiga a negação de serviço através de logout forçado. Obtendo a confirmação explícita do usuário final ou, se presente, validando os parâmetros na solicitação de logout (iniciada pela Relying Party), como o 'id_token_hint'. | 2 |

## V10.7 Gerenciamento de Consentimento

Estes requisitos abrangem a verificação do consentimento do usuário pelo servidor de autorização. Sem a verificação adequada do consentimento do usuário, um ator malicioso pode obter permissões em nome do usuário através de falsificação ou engenharia social.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **10.7.1** | Verifique se o servidor de autorização garante que o usuário consente com cada solicitação de autorização. Se a identidade do cliente não puder ser assegurada, o servidor de autorização deve sempre solicitar explicitamente o consentimento do usuário. | 2 |
| **10.7.2** | Verifique se, quando o servidor de autorização solicita o consentimento do usuário, ele apresenta informações suficientes e claras sobre ao que se está consentindo. Quando aplicável, isso deve incluir a natureza das autorizações solicitadas (geralmente com base no escopo, servidor de recursos, detalhes de autorização do Rich Authorization Requests - RAR), a identidade da aplicação autorizada e a vida útil dessas autorizações. | 2 |
| **10.7.3** | Verifique se o usuário pode revisar, modificar e revogar os consentimentos que o usuário concedeu através do servidor de autorização. | 2 |

## Referências

Para obter mais informações sobre o OAuth, consulte:

* [oauth.net](https://oauth.net/)
* [OWASP OAuth 2.0 Protocol Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)

Para requisitos relacionados ao OAuth no ASVS, são utilizadas as seguintes RFCs, publicadas e em status de rascunho (draft):

* [RFC6749 The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
* [RFC6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)
* [RFC6819 OAuth 2.0 Threat Model and Security Considerations](https://datatracker.ietf.org/doc/html/rfc6819)
* [RFC7636 Proof Key for Code Exchange by OAuth Public Clients](https://datatracker.ietf.org/doc/html/rfc7636)
* [RFC7591 OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591)
* [RFC8628 OAuth 2.0 Device Authorization Grant](https://datatracker.ietf.org/doc/html/rfc8628)
* [RFC8707 Resource Indicators for OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc8707)
* [RFC9068 JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
* [RFC9126 OAuth 2.0 Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126)
* [RFC9207 OAuth 2.0 Authorization Server Issuer Identification](https://datatracker.ietf.org/doc/html/rfc9207)
* [RFC9396 OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)
* [RFC9449 OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)
* [RFC9700 Best Current Practice for OAuth 2.0 Security](https://datatracker.ietf.org/doc/html/rfc9700)
* [draft OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)<!-- recheck on release -->
* [draft The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12)<!-- recheck on release -->

Para obter mais informações sobre o OpenID Connect, consulte:

* [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
* [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html)
