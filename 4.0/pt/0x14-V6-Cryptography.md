# V6 Criptografia armazenada

## Objetivo de controle

Certifique-se de que uma aplicação verificado atenda aos seguintes requisitos de alto nível:

* Todos os módulos criptográficos falham de maneira segura e os erros são tratados corretamente.
* Um gerador de números aleatórios adequado é usado.
* O acesso às chaves é gerenciado com segurança.

## V6.1 Classificação de dados

O ativo mais importante são os dados processados, armazenados ou transmitidos por uma aplicação. Sempre realize uma avaliação de impacto na privacidade para classificar corretamente as necessidades de proteção de dados de quaisquer dados armazenados.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.1.1** | Verifique se os dados privados regulamentados são armazenados criptografados enquanto estão em repouso, como informações de identificação pessoal (PII), informações pessoais confidenciais ou dados avaliados que provavelmente estão sujeitos ao GDPR da UE. | | ✓ | ✓ | 311 |
| **6.1.2** | Verifique se os dados de saúde regulamentados são armazenados criptografados enquanto estão em repouso, como registros médicos, detalhes de dispositivos médicos ou registros de pesquisa anonimizados. | | ✓ | ✓ | 311 |
| **6.1.3** | Verifique se os dados financeiros regulamentados são armazenados criptografados enquanto estão inativos, como contas financeiras, inadimplência ou histórico de crédito, registros fiscais, histórico de pagamentos, beneficiários ou registros de pesquisa ou mercado anonimizados. | | ✓ | ✓ | 311 |

## V6.2 Algoritmos

Avanços recentes em criptografia significam que algoritmos e comprimentos de chave anteriormente seguros não são mais seguros ou suficientes para proteger os dados. Portanto, deve ser possível alterar os algoritmos.

Embora esta seção não seja facilmente testada quanto à penetração, os desenvolvedores devem considerá-la como obrigatória, mesmo que L1 esteja faltando na maioria dos itens.

| # | Descrição  L1 | L2 | L3 | CWE |
| :---: |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :---: | :---:| :---: | :---: |
| **6.2.1** | Verifique se todos os módulos criptográficos falham com segurança e se os erros são tratados de forma a não permitir ataques de Padding Oracle.  ✓ | ✓ | ✓ | 310 |
| **6.2.2** | Verifique se são usados algoritmos, modos e bibliotecas criptográficos comprovados pelo setor ou aprovados pelo governo, em vez de criptografia codificada personalizada. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | 327 |
| **6.2.3** | Verifique se o vetor de inicialização de criptografia, a configuração de cifra e os modos de bloqueio estão configurados com segurança usando as recomendações mais recentes. | ✓ | ✓ | 326 |
| **6.2.4** | Verifique se o número aleatório, algoritmos de criptografia ou hash, comprimentos de chave, rodadas, cifras ou modos podem ser reconfigurados, atualizados ou trocados a qualquer momento, para proteger contra quebras criptográficas. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 326 |
| **6.2.5** | Verifique se os modos de bloco inseguros conhecidos (ou seja, ECB, etc.), modos de preenchimento (ou seja, PKCS#1 v1.5, etc.), cifras com tamanhos de bloco pequenos (ou seja, Triple-DES, Blowfish, etc.) e algoritmos de hash fracos (ou seja, MD5, SHA1, etc.) não são usados, a menos que sejam necessários para compatibilidade com versões anteriores. | | ✓ | ✓ | 326 |
| **6.2.6** | Verifique se nonces, vetores de inicialização e outros números de uso único não devem ser usados mais de uma vez com uma determinada chave de criptografia. O método de geração deve ser apropriado para o algoritmo que está sendo usado. | | ✓ | ✓ | 326 |
| **6.2.7** | Verifique se os dados criptografados são autenticados por meio de assinaturas, modos de cifra autenticados ou HMAC para garantir que o texto cifrado não seja alterado por uma parte não autorizada. | | | ✓ | 326 |
| **6.2.8** | Verifique se todas as operações criptográficas são de tempo constante, sem operações de 'curto-circuito' em comparações, cálculos ou retornos, para evitar vazamento de informações. | | | ✓ | 385 |

## V6.3 Valores Aleatórios

A verdadeira geração de números pseudoaleatórios (PRNG) é incrivelmente difícil de acertar. Geralmente, boas fontes de entropia dentro de um sistema serão rapidamente esgotadas se usadas em excesso, mas fontes com menos aleatoriedade podem levar a chaves e segredos previsíveis.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.3.1** | Verifique se todos os números aleatórios, nomes de arquivos aleatórios, GUIDs aleatórios e strings aleatórias são gerados usando o gerador de números aleatórios criptograficamente seguro aprovado do módulo criptográfico quando esses valores aleatórios não devem ser adivinhados por um invasor. | | ✓ | ✓ | 338 |
| **6.3.2** | Verifique se os GUIDs aleatórios são criados usando o algoritmo GUID v4 e um gerador de números pseudo-aleatórios criptograficamente seguro (CSPRNG). GUIDs criados usando outros geradores de números pseudo-aleatórios podem ser previsíveis. | | ✓ | ✓ | 338 |
| **6.3.3** | Verifique se os números aleatórios são criados com a entropia adequada mesmo quando a aplicação está sob carga pesada ou se a aplicação se degrada normalmente nessas circunstâncias. | | | ✓ | 338 |

## V6.4 Gestão de segredo

Embora esta seção não seja facilmente testada quanto à penetração, os desenvolvedores devem considerá-la como obrigatória, mesmo que L1 esteja faltando na maioria dos itens.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **6.4.1** | Verifique se uma solução de gestão de segredos, como um cofre de chaves, é usada para criar, armazenar, controlar o acesso e destruir segredos com segurança. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 798 |
| **6.4.2** | Verifique se o material da chave não está exposto à aplicação, mas usa um módulo de segurança isolado como um cofre para operações criptográficas. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 320 |

## Referências

Para mais informações, consulte também:

* [Guia de teste OWASP 4.0: Teste para criptografia fraca](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/README.html)
* [Cheat Sheet OWASP: armazenamento criptográfico](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [FIPS 140-2](https://csrc.nist.gov/publications/detail/fips/140/2/final)
