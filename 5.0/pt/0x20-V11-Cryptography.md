# V11 Criptografia

## Objetivo de Controle

O objetivo deste capítulo é definir as melhores práticas para o uso geral da criptografia, bem como incutir uma compreensão fundamental dos princípios criptográficos e inspirar uma mudança em direção a abordagens mais resilientes e modernas. Ele incentiva o seguinte:

* Implementar sistemas criptográficos robustos que falhem de forma segura (fail securely), que se adaptem às ameaças em evolução e que sejam preparados para o futuro (future-proof).
* Utilizar mecanismos criptográficos que sejam ao mesmo tempo seguros e alinhados com as melhores práticas do setor.
* Manter um sistema seguro de gerenciamento de chaves criptográficas com controles de acesso e auditoria apropriados.
* Avaliar regularmente o cenário criptográfico para verificar novos riscos e adaptar algoritmos de acordo.
* Descobrir e gerenciar os casos de uso de criptografia ao longo de todo o ciclo de vida da aplicação para garantir que todos os ativos criptográficos sejam contabilizados e protegidos.

Além de delinear princípios gerais e melhores práticas, este documento também fornece informações técnicas mais detalhadas sobre os requisitos no Apêndice C - Padrões de Criptografia. Isso inclui algoritmos e modos que são considerados "aprovados" para os propósitos dos requisitos deste capítulo.

Requisitos que usam criptografia para resolver um problema separado, como gerenciamento de segredos ou segurança de comunicações, estarão em partes diferentes do padrão.

## V11.1 Inventário e Documentação Criptográfica

As aplicações precisam ser projetadas com uma forte arquitetura criptográfica para proteger os ativos de dados de acordo com sua classificação. Criptografar tudo é um desperdício; não criptografar nada é uma negligência legal. Um equilíbrio deve ser alcançado, geralmente durante o design da arquitetura ou o design de alto nível (high-level design), design sprints ou architectural spikes. Projetar a criptografia "no improviso" ou fazer adequações retroativas (retrofitting) custará inevitavelmente muito mais para implementar de forma segura do que construí-la desde o início.

É importante garantir que todos os ativos criptográficos sejam descobertos, inventariados e avaliados regularmente. Por favor, consulte o apêndice para mais informações sobre como isso pode ser feito.

A necessidade de proteger sistemas criptográficos no futuro contra o eventual surgimento da computação quântica também é fundamental. A Criptografia Pós-Quântica (Post-Quantum Cryptography - PQC) refere-se a algoritmos criptográficos projetados para permanecerem seguros contra ataques por computadores quânticos, que têm a expectativa de quebrar os algoritmos amplamente usados, como o RSA e a Criptografia de Curva Elíptica (ECC).

Por favor, consulte o apêndice para orientações atuais sobre primitivas PQC validadas e padrões.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **11.1.1** | Verifique se há uma política documentada para o gerenciamento de chaves criptográficas e um ciclo de vida da chave criptográfica que siga um padrão de gerenciamento de chaves como o NIST SP 800-57. Isso deve incluir a garantia de que as chaves não sejam supercompartilhadas (overshared) (por exemplo, com mais de duas entidades para segredos compartilhados e mais de uma entidade para chaves privadas). | 2 |
| **11.1.2** | Verifique se um inventário criptográfico é realizado, mantido, atualizado regularmente e se inclui todas as chaves criptográficas, algoritmos e certificados usados pela aplicação. Ele também deve documentar onde as chaves podem ou não ser usadas no sistema e os tipos de dados que podem ou não ser protegidos usando as chaves. | 2 |
| **11.1.3** | Verifique se mecanismos de descoberta criptográfica são empregados para identificar todas as instâncias de criptografia no sistema, incluindo operações de criptografia, hashing e assinatura. | 3 |
| **11.1.4** | Verifique se um inventário criptográfico é mantido. Ele deve incluir um plano documentado que descreve o caminho de migração para os novos padrões de criptografia, como a criptografia pós-quântica, a fim de reagir a ameaças futuras. | 3 |

## V11.2 Implementação Segura de Criptografia

Esta seção define os requisitos para a seleção, implementação e gerenciamento contínuo dos principais algoritmos criptográficos de uma aplicação. O objetivo é garantir que apenas primitivas criptográficas robustas e aceitas no setor sejam implantadas, em alinhamento com as normas vigentes (por exemplo, NIST, ISO/IEC) e melhores práticas. As organizações devem garantir que cada componente criptográfico seja selecionado com base em evidências revisadas por pares (peer-reviewed) e testes de segurança práticos.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **11.2.1** | Verifique se implementações validadas pela indústria (incluindo bibliotecas e implementações aceleradas por hardware) são usadas para operações criptográficas. | 2 |
| **11.2.2** | Verifique se a aplicação é projetada com agilidade criptográfica (crypto agility), de tal forma que números aleatórios, criptografia autenticada, MAC ou algoritmos de hash, comprimentos de chave, rodadas (rounds), cifras e modos possam ser reconfigurados, atualizados ou trocados a qualquer momento, para proteger contra quebras criptográficas. Da mesma forma, também deve ser possível substituir chaves e senhas e criptografar novamente os dados. Isso permitirá a realização de upgrades transparentes (seamless) para a criptografia pós-quântica (PQC), assim que implementações de alta garantia (high-assurance) de esquemas ou padrões aprovados de PQC estiverem amplamente disponíveis. | 2 |
| **11.2.3** | Verifique se todas as primitivas criptográficas utilizam um mínimo de 128 bits de segurança com base no algoritmo, no tamanho da chave e na configuração. Por exemplo, uma chave ECC de 256 bits fornece cerca de 128 bits de segurança, ao passo que o RSA requer uma chave de 3072 bits para alcançar 128 bits de segurança. | 2 |
| **11.2.4** | Verifique se todas as operações criptográficas têm tempo constante (constant-time), sem operações de 'curto-circuito' em comparações, cálculos ou retornos, para evitar o vazamento de informações. | 3 |
| **11.2.5** | Verifique se todos os módulos criptográficos falham com segurança (fail securely), e se os erros são tratados de maneira a não permitir o surgimento de vulnerabilidades, como ataques de Padding Oracle. | 3 |

## V11.3 Algoritmos de Criptografia

Os algoritmos de criptografia autenticada construídos em AES e CHACHA20 formam a espinha dorsal da prática criptográfica moderna.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **11.3.1** | Verifique se os modos de bloco inseguros (por exemplo, ECB) e os esquemas de preenchimento fracos (weak padding schemes, por exemplo, PKCS#1 v1.5) não são usados. | 1 |
| **11.3.2** | Verifique se apenas as cifras e modos aprovados, como o AES com GCM, são usados. | 1 |
| **11.3.3** | Verifique se os dados criptografados estão protegidos contra modificações não autorizadas preferencialmente através do uso de um método de criptografia autenticada aprovado ou da combinação de um método de criptografia aprovado com um algoritmo MAC aprovado. | 2 |
| **11.3.4** | Verifique se os nonces, vetores de inicialização e outros números de uso único (single-use numbers) não são usados para mais de um par de chave de criptografia e elemento de dado. O método de geração deve ser adequado ao algoritmo em uso. | 3 |
| **11.3.5** | Verifique se qualquer combinação de um algoritmo de criptografia com um algoritmo MAC está operando no modo encrypt-then-MAC (criptografa-depois-MAC). | 3 |

## V11.4 Hashing e Funções Baseadas em Hash

Os hashes criptográficos são usados em uma ampla variedade de protocolos criptográficos, como assinaturas digitais, HMAC, funções de derivação de chaves (KDF), geração aleatória de bits e armazenamento de senhas. A segurança do sistema criptográfico depende da força das funções hash subjacentes usadas. Esta seção descreve os requisitos para o uso de funções hash seguras em operações criptográficas.

Para o armazenamento de senhas, além do apêndice de criptografia, o [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms) também fornecerá contexto e orientações úteis.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **11.4.1** | Verifique se apenas funções hash aprovadas são usadas para casos de uso gerais de criptografia, incluindo assinaturas digitais, HMAC, KDF e geração aleatória de bits. Funções de hash não permitidas, como o MD5, não devem ser usadas para nenhum propósito criptográfico. | 1 |
| **11.4.2** | Verifique se as senhas são armazenadas usando uma função de derivação de chave aprovada e de processamento intensivo (também conhecida como "função de hash de senha"), com parâmetros configurados de acordo com a orientação atual. As configurações devem equilibrar segurança e desempenho a fim de tornar os ataques de força bruta suficientemente desafiadores para o nível exigido de segurança. | 2 |
| **11.4.3** | Verifique se as funções hash usadas em assinaturas digitais, como parte da autenticação de dados ou integridade de dados, são resistentes à colisão e possuem os comprimentos de bits adequados. Se for exigida a resistência à colisão, o tamanho da saída deverá ser de, no mínimo, 256 bits. Se apenas a resistência aos ataques de segunda pré-imagem (second pre-image attacks) for exigida, o tamanho da saída deverá ser de, no mínimo, 128 bits. | 2 |
| **11.4.4** | Verifique se a aplicação usa funções de derivação de chave aprovadas com parâmetros de key stretching (alongamento de chave) ao derivar chaves secretas de senhas. Os parâmetros em uso devem equilibrar segurança e desempenho para evitar que ataques de força bruta comprometam a chave criptográfica resultante. | 2 |

## V11.5 Valores Aleatórios

A Geração de Números Pseudoaleatórios Criptograficamente Segura (CSPRNG) é incrivelmente difícil de fazer da forma correta. Em geral, boas fontes de entropia dentro de um sistema esgotarão rapidamente se usadas em excesso, mas as fontes com menos aleatoriedade podem levar a chaves e segredos previsíveis.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **11.5.1** | Verifique se todos os números e strings aleatórios que se destinam a não serem adivinháveis devem ser gerados usando um gerador de números pseudoaleatórios criptograficamente seguro (CSPRNG) e têm pelo menos 128 bits de entropia. Note que UUIDs não respeitam esta condição. | 2 |
| **11.5.2** | Verifique se o mecanismo de geração de números aleatórios em uso foi projetado para funcionar de forma segura, mesmo sob alta demanda. | 3 |

## V11.6 Criptografia de Chave Pública

A Criptografia de Chave Pública será usada onde não for possível ou indesejável compartilhar uma chave secreta entre várias partes.

Como parte disso, existe a necessidade de mecanismos aprovados para a troca de chaves, como Diffie-Hellman e Curva Elíptica de Diffie-Hellman (ECDH), para garantir que o sistema criptográfico permaneça seguro contra ameaças modernas. O capítulo "Comunicação Segura" fornece os requisitos para o TLS, de forma que os requisitos nesta seção se destinam a situações em que a Criptografia de Chave Pública esteja sendo usada em casos de uso distintos do TLS.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **11.6.1** | Verifique se apenas modos de operação e algoritmos criptográficos aprovados são usados para geração de chaves, seeding, geração e verificação de assinatura digital. Os algoritmos de geração de chaves não devem gerar chaves inseguras que sejam vulneráveis a ataques conhecidos, por exemplo, as chaves RSA que são vulneráveis à fatoração de Fermat. | 2 |
| **11.6.2** | Verifique se os algoritmos criptográficos aprovados são usados para a troca de chaves (como o Diffie-Hellman), com foco em garantir que os mecanismos de troca de chaves utilizem parâmetros seguros. Isso evitará ataques ao processo de estabelecimento da chave que poderiam levar a ataques adversary-in-the-middle ou a quebras criptográficas. | 3 |

## V11.7 Criptografia de Dados Em Uso

Proteger os dados enquanto estão sendo processados é primordial. O uso de técnicas como criptografia completa de memória, criptografia de dados em trânsito e assegurar que os dados sejam criptografados o mais rápido possível após o uso, é recomendado.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **11.7.1** | Verifique se o uso de criptografia completa de memória está habilitado para proteger os dados sensíveis enquanto estiverem em uso, impedindo o acesso por usuários ou processos não autorizados. | 3 |
| **11.7.2** | Verifique se a minimização de dados garante a exposição de apenas a menor quantidade de dados durante o processamento, e assegure que os dados sejam criptografados imediatamente após o uso ou logo que for possível. | 3 |

## Referências

Para mais informações, veja também:

* [OWASP Web Security Testing Guide: Testing for Weak Cryptography](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography)
* [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
* [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)