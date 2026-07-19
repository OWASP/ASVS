# V9 Tokens Autocontidos (Self-contained Tokens)

## Objetivo de Controle

O conceito de um token autocontido (self-contained token) é mencionado no RFC 6749 original do OAuth 2.0 de 2012. Refere-se a um token contendo dados ou claims (reivindicações) nos quais um serviço receptor se baseará para tomar decisões de segurança. Isso deve ser diferenciado de um token simples contendo apenas um identificador, o qual um serviço receptor usa para pesquisar os dados localmente. Os exemplos mais comuns de tokens autocontidos são os JSON Web Tokens (JWTs) e as asserções SAML.

O uso de tokens autocontidos tornou-se muito difundido, mesmo fora do OAuth e OIDC. Ao mesmo tempo, a segurança desse mecanismo depende da capacidade de validar a integridade do token e de garantir que o token seja válido para um contexto particular. Existem muitas armadilhas com este processo, e este capítulo fornece detalhes específicos sobre os mecanismos que as aplicações devem ter para evitá-las.

## V9.1 Origem e Integridade do Token

Esta seção inclui requisitos para garantir que o token tenha sido produzido por uma parte confiável e não tenha sido adulterado.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **9.1.1** | Verifique se os tokens autocontidos são validados usando sua assinatura digital ou MAC para proteger contra adulteração antes de aceitar o conteúdo do token. | 1 |
| **9.1.2** | Verifique se apenas algoritmos em uma lista de permissões (allowlist) podem ser usados para criar e verificar tokens autocontidos para um determinado contexto. A lista de permissões deve incluir os algoritmos permitidos, idealmente apenas algoritmos simétricos ou assimétricos, e não deve incluir o algoritmo 'None'. Se ambos, simétricos e assimétricos, precisarem ser suportados, controles adicionais serão necessários para evitar a confusão de chaves (key confusion). | 1 |
| **9.1.3** | Verifique se o material criptográfico (key material) que é usado para validar tokens autocontidos vem de fontes confiáveis pré-configuradas para o emissor do token, evitando que atacantes especifiquem fontes e chaves não confiáveis. Para JWTs e outras estruturas JWS, cabeçalhos como 'jku', 'x5u' e 'jwk' devem ser validados contra uma lista de permissões de fontes confiáveis. | 1 |

## V9.2 Conteúdo do Token

Antes de tomar decisões de segurança baseadas no conteúdo de um token autocontido, é necessário validar se o token foi apresentado dentro de seu período de validade e se destina-se ao uso pelo serviço receptor e para o propósito para o qual foi apresentado. Isso ajuda a evitar o uso cruzado inseguro (cross-usage) entre diferentes serviços ou com diferentes tipos de token do mesmo emissor.

Requisitos específicos para OAuth e OIDC são abordados no capítulo dedicado.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **9.2.1** | Verifique se, caso haja um intervalo de tempo de validade presente nos dados do token, o token e seu conteúdo sejam aceitos apenas se o tempo de verificação estiver dentro deste intervalo de tempo de validade. Por exemplo, para JWTs, as claims 'nbf' e 'exp' devem ser verificadas. | 1 |
| **9.2.2** | Verifique se o serviço que recebe um token valida que o token seja do tipo correto e tenha o propósito pretendido antes de aceitar os conteúdos do token. Por exemplo, apenas tokens de acesso (access tokens) podem ser aceitos para decisões de autorização e apenas ID Tokens podem ser usados para provar a autenticação do usuário. | 2 |
| **9.2.3** | Verifique se o serviço apenas aceita tokens que são destinados ao uso com esse serviço (audiência). Para JWTs, isso pode ser alcançado validando a claim 'aud' em relação a uma lista de permissões definida no serviço. | 2 |
| **9.2.4** | Verifique se, caso um emissor de token use a mesma chave privada para emitir tokens para públicos diferentes, os tokens emitidos contenham uma restrição de audiência (audience restriction) que identifique unicamente as audiências pretendidas. Isso evitará que um token seja reutilizado com um público não intencional. Se o identificador de audiência for provisionado dinamicamente, o emissor do token deverá validar essas audiências para garantir que não resultem em falsificação de audiência (audience impersonation). | 2 |

## Referências

Para mais informações, veja também:

* [OWASP JSON Web Token Cheat Sheet for Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) (embora tenha orientações gerais úteis)