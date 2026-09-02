# Apêndice C: Padrões de Criptografia

O capítulo "Criptografia" vai além de simplesmente definir as melhores práticas. O seu objetivo é o de aprimorar a compreensão dos princípios de criptografia e incentivar a adoção de métodos de segurança modernos e mais resilientes. Este apêndice fornece informações técnicas detalhadas com relação a cada requisito, complementando os padrões abrangentes descritos no capítulo "Criptografia".

Este apêndice define o nível de aprovação para diferentes mecanismos criptográficos:

* Mecanismos Aprovados (Approved - A) podem ser usados em aplicações.
* Mecanismos Legados (Legacy mechanisms - L) não devem ser usados em aplicações, mas ainda podem ser usados apenas para compatibilidade com código ou aplicações legadas existentes. Embora o uso de tais mecanismos atualmente não seja considerado uma vulnerabilidade em si, eles devem ser substituídos por mecanismos mais seguros e à prova de futuro (future-proof) assim que possível.
* Mecanismos Não Permitidos (Disallowed mechanisms - D) não devem ser usados porque são atualmente considerados quebrados ou não fornecem segurança suficiente.

Esta lista pode ser anulada (overridden) no contexto de uma determinada aplicação por vários motivos, incluindo:

* novas evoluções no campo da criptografia;
* conformidade com regulamentação.

## Inventário e Documentação Criptográfica

Esta seção fornece informações adicionais
para V11.1 Inventário e Documentação Criptográfica.

É importante garantir que todos os ativos criptográficos, como algoritmos, chaves e certificados, sejam descobertos, inventariados e avaliados regularmente. Para o Nível 3, isso deve incluir o uso de varredura (scanning) estática e dinâmica para descobrir o uso da criptografia em uma aplicação. Ferramentas como SAST e DAST podem ajudar com isso, mas é possível que ferramentas dedicadas sejam necessárias para obter uma cobertura mais abrangente. Exemplos gratuitos de ferramentas incluem:

* [CryptoMon - Network Cryptography Monitor - using eBPF, written in python](https://github.com/Santandersecurityresearch/CryptoMon)
* [Cryptobom Forge Tool: Generating Comprehensive CBOMs from CodeQL Outputs](https://github.com/Santandersecurityresearch/cryptobom-forge)

## Forças Equivalentes dos Parâmetros Criptográficos

As forças de segurança relativas para vários sistemas criptográficos estão nesta tabela (do [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), p.71):

| Força de Segurança | Algoritmos de Chave Simétrica | Campo Finito | Fatoração de Inteiros | Curva Elíptica |
|--|--|--|--|--|
| <= 80 | 2TDEA | L = 1024 <br> N = 160 | k = 1024 | f = 160-223 |
| 112 | 3TDEA   | L = 2048 <br> N = 224 | k = 2048 | f = 224-255 |
| 128 | AES-128 | L = 3072 <br> N = 256 | k = 3072 | f = 256-383 |
| 192 | AES-192 | L = 7680 <br> N = 384 | k = 7680 | f = 384-511 |
| 256 | AES-256 | L = 15360 <br> N = 512 | k = 15360 | f = 512+ |

Exemplo de aplicações:

* Criptografia de Campo Finito: DSA, FFDH, MQV
* Criptografia de Fatoração de Inteiros: RSA
* Criptografia de Curva Elíptica: ECDSA, EdDSA, ECDH, MQV

Nota: observe que esta seção pressupõe que não exista computador quântico; se tal computador existisse, as estimativas para as últimas 3 colunas não seriam mais válidas.

## Valores Aleatórios

Esta seção fornece informações adicionais
para V11.5 Valores Aleatórios.

| Nome | Versão/Referência | Notas | Status |
|:---|:----|:----|:-:|
| `/dev/random` | Linux 4.8+ [(Oct 2016)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=818e607b57c94ade9824dad63a96c2ea6b21baf3), também encontrado no iOS, Android e outros sistemas operacionais POSIX baseados em Linux. Baseado na [RFC7539](https://datatracker.ietf.org/doc/html/rfc7539) | Utilizando stream ChaCha20. Encontrado no iOS [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)?language=objc) e Android [`Secure Random`](https://developer.android.com/reference/java/security/SecureRandom) com as configurações corretas fornecidas a cada um. | A |
| `/dev/urandom` | Arquivo especial do kernel do Linux para fornecer dados aleatórios | Fornece fontes de entropia de alta qualidade a partir de aleatoriedade de hardware | A |
| `AES-CTR-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | Conforme usado em implementações comuns, como a [Windows CNG API `BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) definida por [`BCRYPT_RNG_ALGORITHM`](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-algorithm-identifiers). | A |
| `HMAC-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `Hash-DRBG` | [NIST SP800-90A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf) | | A |
| `getentropy()` | [OpenBSD](https://man.openbsd.org/getentropy.2), disponível em [Linux glibc 2.25+](https://man7.org/linux/man-pages/man3/getentropy.3.html) e [macOS 10.12+](https://support.apple.com/en-gb/guide/security/seca0c73a75b/web) | Fornece bytes aleatórios seguros diretamente da fonte de entropia do kernel com uma API direta e mínima. É mais moderno e evita as armadilhas associadas às APIs mais antigas. | A |

A função hash subjacente usada com o HMAC-DRBG ou Hash-DRBG deve ser aprovada para este uso.

## Algoritmos de Cifra

Esta seção fornece informações adicionais
para V11.3 Algoritmos de Criptografia.

Os algoritmos de cifra aprovados estão listados em ordem de preferência.

| Algoritmos de Chave Simétrica | Referência | Status |
| ------ | ------ |:-:|
| AES-256 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | A |
| Salsa20 | [Salsa 20 specification](https://cr.yp.to/snuffle/spec.pdf) | A |
| XChaCha20 | [XChaCha20 Draft](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-xchacha-03) | A |
| XSalsa20 | [Extending the Salsa20 nonce](https://cr.yp.to/snuffle/xsalsa-20110204.pdf) | A |
| ChaCha20 | [RFC 8439](https://www.rfc-editor.org/info/rfc8439) | A |
| AES-192 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | A |
| AES-128 | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) | L |
| 2TDEA | | D |
| TDEA (3DES/3DEA) | | D |
| IDEA | | D |
| RC4 | | D |
| Blowfish| | D |
| ARC4 | | D |
| DES | | D |

### Modos de Cifra AES

Cifras de bloco, como o AES, podem ser usadas com diferentes modos de operação. Muitos modos de operação, como o Electronic codebook (ECB), são inseguros e não devem ser usados. Os modos de operação Galois/Counter Mode (GCM) e Counter with cipher block chaining message authentication code (CCM) fornecem criptografia autenticada e devem ser usados em aplicações modernas.

Os modos aprovados estão listados em ordem de preferência.

| Modo | Autenticado | Referência | Status | Restrição |
|--|--|--|:-:|--|
| GCM | Sim | [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A | |
| CCM | Sim | [NIST SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A | |
| CBC | Não | [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | L | |
| CCM-8 | Sim | | D | |
| ECB | Não | | D | |
| CFB | Não | | D | |
| OFB | Não | | D | |
| CTR | Não | | D | |

Notas:

* Todas as mensagens criptografadas devem ser autenticadas. Para QUALQUER uso do modo CBC, DEVE haver um algoritmo MAC de hash associado para validar a mensagem. Em geral, isso DEVE ser aplicado no método Encrypt-Then-Hash (mas o TLS 1.2 usa Hash-Then-Encrypt em seu lugar). Se isso não puder ser garantido, o CBC NÃO DEVE ser usado. A única aplicação onde a criptografia sem um algoritmo MAC é permitida é a criptografia de disco.
* Se o CBC for usado, deve-se garantir que a verificação do preenchimento (padding) seja realizada em tempo constante (constant time).
* Ao usar CCM-8, a tag MAC possui apenas 64 bits de segurança. Isso não está em conformidade com o requisito 6.2.9, que exige pelo menos 128 bits de segurança.
* Criptografia de disco é considerada fora do escopo para o ASVS. Portanto, este apêndice não lista nenhum método aprovado para criptografia de disco. Para este uso, a criptografia sem autenticação é geralmente aceita e os modos XTS, XEX e LRW são tipicamente usados.

### Empacotamento de Chaves (Key Wrapping)

O empacotamento de chave criptográfica (cryptographic key wrap) (e o correspondente desempacotamento de chave / key unwrap) é um método de proteger uma chave existente encapsulando-a (ou seja, empacotando-a) ao empregar um mecanismo de criptografia adicional, para que a chave original não seja exposta de forma óbvia, por exemplo, durante uma transferência. Esta chave adicional usada para proteger a chave original é referida como a chave de empacotamento (wrap key).

Essa operação pode ser realizada quando for desejável proteger chaves em locais considerados não confiáveis ou para enviar chaves sensíveis em redes não confiáveis ou dentro de aplicações.
No entanto, deve-se considerar seriamente a compreensão da natureza (ex., a identidade e o propósito) da chave original antes de se comprometer com um procedimento de empacotar/desempacotar (wrap/unwrap), pois isso pode ter repercussões tanto para os sistemas/aplicações de origem quanto de destino em termos de segurança e, especialmente, conformidade, o que pode incluir trilhas de auditoria da função de uma chave (ex., assinatura), bem como o armazenamento apropriado da chave.

Especificamente, o AES-256 DEVE ser usado para o empacotamento de chaves, seguindo o [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) e considerando provisões voltadas para o futuro contra a ameaça quântica. Os modos de cifra usando AES são os seguintes, em ordem de preferência:

| Empacotamento de Chave (Key Wrapping) | Referência | Status |
|--|--|:-:|
| KW | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |
| KWP | [NIST SP 800-38F](https://csrc.nist.gov/pubs/sp/800/38/f/final) | A |

AES-192 e AES-128 PODEM ser usados se o caso de uso exigir, mas sua motivação DEVE ser documentada no inventário de criptografia da entidade.

### Criptografia Autenticada

Com exceção da criptografia de disco, os dados criptografados devem ser protegidos contra modificação não autorizada utilizando alguma forma de esquema de criptografia autenticada (AE), geralmente usando um esquema de criptografia autenticada com dados associados (AEAD).

A aplicação deve, de preferência, usar um esquema AEAD aprovado. Alternativamente, ela pode combinar um esquema de cifra aprovado e um algoritmo MAC aprovado com uma construção Encrypt-then-MAC.

MAC-then-encrypt ainda é permitido para compatibilidade com aplicações legadas. É usado no TLS v1.2 com suítes de cifras (ciphers suites) antigas.

| Mecanismo AEAD | Referência | Status |
|---|---------|:-:|
|AES-GCM | [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | A |
|AES-CCM  | [SP 800-38C](https://csrc.nist.gov/pubs/sp/800/38/c/upd1/final) | A |
|ChaCha-Poly1305 | [RFC 7539](https://datatracker.ietf.org/doc/html/rfc7539) | A |
|AEGIS-256 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128 | [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|AEGIS-128L| [AEGIS: A Fast Authenticated Encryption Algorithm (v1.1)](https://competitions.cr.yp.to/round3/aegisv11.pdf) | A |
|Encrypt-then-MAC | | A |
|MAC-then-encrypt | | L |

## Funções Hash

Esta seção fornece informações adicionais
para V11.4 Hashing e Funções Baseadas em Hash.

### Funções Hash para Casos de Uso Gerais

A tabela a seguir lista as funções hash aprovadas em casos gerais de uso criptográfico, como assinaturas digitais:

* Funções hash aprovadas fornecem forte resistência à colisão e são adequadas para aplicações de alta segurança.
* Alguns desses algoritmos oferecem forte resistência a ataques quando usados com o gerenciamento adequado de chaves criptográficas, e por isso são adicionalmente aprovados para funções HMAC, KDF e RBG.
* Função hash com menos de 254 bits de saída possui resistência a colisão insuficiente e não deve ser usada para assinatura digital ou outras aplicações que requeiram resistência a colisão. Para outros usos, elas podem ser usadas para compatibilidade e verificação APENAS com sistemas legados, mas não devem ser usadas em novos designs.

| Função Hash | Referência | Status | Restrições |
| ------ | ----------- |:-:| ---------- |
| SHA3-512 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-512 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA3-384 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-384 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA3-256 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| SHA-512/256 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHA-256 |[FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | A | |
| SHAKE256 |[FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | A | |
| BLAKE2s | [BLAKE2: simpler, smaller, fast as MD5](https://eprint.iacr.org/2013/322) | A | |
| BLAKE2b | [BLAKE2: simpler, smaller, fast as MD5](https://eprint.iacr.org/2013/322) | A | |
| BLAKE3 | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf) | A | |
| SHA-224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Não adequado para HMAC, KDF, RBG, assinaturas digitais |
| SHA-512/224 | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | L | Não adequado para HMAC, KDF, RBG, assinaturas digitais |
| SHA3-224 | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) | L | Não adequado para HMAC, KDF, RBG, assinaturas digitais |
| SHA-1 | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | L | Não adequado para HMAC, KDF, RBG, assinaturas digitais |
| CRC (qualquer comprimento) |  | D |  |
| MD4 | [RFC 1320](https://www.rfc-editor.org/info/rfc1320) | D | |
| MD5 | [RFC 1321](https://www.rfc-editor.org/info/rfc1321) | D | |

### Funções Hash para Armazenamento de Senhas

Para o hashing seguro de senhas, funções hash dedicadas devem ser usadas. Estes algoritmos de hashing lento (slow-hashing) mitigam ataques de força bruta e de dicionário, aumentando a dificuldade computacional do crack de senhas.

| KDF        | Referência | Parâmetros Obrigatórios | Status |
| ---------- | --------- | ------------ |:-:|
| argon2id | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
|          |                                                     | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
|          |                                                     | t ≥ 3: m ≥ 12288 (12 MiB), p = 1 | A |
| scrypt   | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
|          |                                                     | p = 2: N ≥ 2^16 (64 MiB), r = 8  | A |
|          |                                                     | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8  | A |
| bcrypt | [A Future-Adaptable Password Scheme](https://www.researchgate.net/publication/2519476_A_Future-Adaptable_Password_Scheme) | cost ≥ 10 | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterações ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterações ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterações ≥ 1,300,000 | L |

As funções de derivação de chaves baseadas em senhas aprovadas podem ser usadas para armazenamento de senhas.

## Funções de Derivação de Chaves (KDFs)

### Funções de Derivação de Chaves Gerais

| KDF              | Referência                                                                                     | Status |
| ---------------- | -------- |:-:|
| HKDF             | [RFC 5869](https://www.rfc-editor.org/info/rfc5869)                                           | A      |
| TLS 1.2 PRF      | [RFC 5248](https://www.rfc-editor.org/info/rfc5248)                                           | L      |
| MD5-based KDFs   | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                           | D      |
| SHA-1-based KDFs | [RFC 3174](https://www.rfc-editor.org/info/rfc3174) & [RFC 6194](https://www.rfc-editor.org/info/rfc6194) | D      |

### Funções de Derivação de Chaves Baseadas em Senha

| KDF        | Referência | Parâmetros Obrigatórios | Status |
| ---------- | --------- | ------------ |:-:|
| argon2id   | [RFC 9106](https://www.rfc-editor.org/info/rfc9106) | t = 1: m ≥ 47104 (46 MiB), p = 1 | A |
|            |                                                     | t = 2: m ≥ 19456 (19 MiB), p = 1 | A |
| scrypt     | [RFC 7914](https://www.rfc-editor.org/info/rfc7914) | p = 1: N ≥ 2^17 (128 MiB), r = 8 | A |
|            |                                                     | p = 2: N ≥ 2^16 (64 MiB), r = 8  | A |
|            |                                                     | p ≥ 3: N ≥ 2^15 (32 MiB), r = 8  | A |
| PBKDF2-HMAC-SHA-512 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterações ≥ 210,000 | A |
| PBKDF2-HMAC-SHA-256 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterações ≥ 600,000 | A |
| PBKDF2-HMAC-SHA-1 | [NIST SP 800-132](https://csrc.nist.gov/pubs/sp/800/132/final), [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | iterações ≥ 1,300,000 | L |

## Mecanismos de Troca de Chaves

Esta seção fornece informações adicionais
para V11.6 Criptografia de Chave Pública.

### Esquemas KEX

Uma força de segurança de 112 bits ou superior DEVE ser garantida para todos os esquemas de Troca de Chaves, e sua implementação DEVE seguir as escolhas de parâmetros na tabela a seguir.

| Esquema | Parâmetros de Domínio | Forward Secrecy |Status |
|--|--|--|:-:|
| Diffie-Hellman de Campo Finito (FFDH) | L >= 3072 & N >= 256 | Sim | A |
| Diffie-Hellman de Curva Elíptica (ECDH) | f >= 256-383 | Sim | A |
| Transporte de chave criptografada com RSA-PKCS#1 v1.5 | | Não | D |

Onde os seguintes parâmetros são:

* k é o tamanho da chave para chaves RSA.
* L é o tamanho da chave pública e N é o tamanho da chave privada para criptografia de campo finito.
* f é o alcance (range) de tamanhos de chaves para ECC.

Nenhuma nova implementação DEVE usar qualquer esquema que NÃO esteja em conformidade com as diretrizes [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) & [B](https://csrc.nist.gov/pubs/sp/800/56/b/r2/final) e [NIST SP 800-77](https://csrc.nist.gov/pubs/sp/800/77/r1/final). Especificamente, o IKEv1 NÃO DEVE ser usado em produção.

### Grupos Diffie-Hellman

Os seguintes grupos são aprovados para implementações de troca de chaves Diffie-Hellman. As forças de segurança estão documentadas no [NIST SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final), Apêndice D, e no [NIST SP 800-57 Part 1 Rev.5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Grupo            | Status |
|------------------|:------:|
| P-224, secp224r1 | A      |
| P-256, secp256r1 | A      |
| P-384, secp384r1 | A      |
| P-521, secp521r1 | A      |
| K-233, sect233k1 | A      |
| K-283, sect283k1 | A      |
| K-409, sect409k1 | A      |
| K-571, sect571k1 | A      |
| B-233, sect233r1 | A      |
| B-283, sect283r1 | A      |
| B-409, sect409r1 | A      |
| B-571, sect571r1 | A      |
| Curve448         | A      |
| Curve25519       | A      |
| MODP-2048        | A      |
| MODP-3072        | A      |
| MODP-4096        | A      |
| MODP-6144        | A      |
| MODP-8192        | A      |
| ffdhe2048        | A      |
| ffdhe3072        | A      |
| ffdhe4096        | A      |
| ffdhe6144        | A      |
| ffdhe8192        | A      |

## Códigos de Autenticação de Mensagens (Message Authentication Codes - MAC)

Os Códigos de Autenticação de Mensagem (MACs) são constructos criptográficos usados para verificar a integridade e autenticidade de uma mensagem. Um MAC recebe uma mensagem e uma chave secreta como entradas (inputs) e produz uma tag de tamanho fixo (o valor MAC). Os MACs são amplamente utilizados em protocolos de comunicação segura (ex., TLS/SSL) para garantir que as mensagens trocadas entre as partes sejam autênticas e estejam intactas.

| Algoritmo MAC | Referência                                                                                 | Status |
| ----------    | --------------- |:-:|
| HMAC-SHA-256  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-384  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| HMAC-SHA-512  | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | A |
| KMAC128       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A |
| KMAC256       | [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)                             | A |
| BLAKE3 (modo keyed_hash) | [BLAKE3 one function, fast everywhere](https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf)  | A |
| AES-CMAC      | [RFC 4493](https://datatracker.ietf.org/doc/html/rfc4493) & [NIST SP 800-38B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf) | A |
| AES-GMAC      | [NIST SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)            | A |
| Poly1305-AES  | [The Poly1305-AES message-authentication code](https://cr.yp.to/mac/poly1305-20050329.pdf)                  | A |
| HMAC-SHA-1    | [RFC 2104](https://www.rfc-editor.org/info/rfc2104) & [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) | L |
| HMAC-MD5      | [RFC 1321](https://www.rfc-editor.org/info/rfc1321)                                | D      |

## Assinaturas Digitais

Os esquemas de assinatura DEVEM usar parâmetros e tamanhos de chave aprovados de acordo com o [NIST SP 800-57 Part 1](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).

| Algoritmo de Assinatura        | Referência                                                 | Status |
| ------------------------------ | ---------------------------------------------              | :-:    |
| EdDSA (Ed25519, Ed448)         | [RFC 8032](https://www.rfc-editor.org/info/rfc8032)        | A      |
| XEdDSA (Curve25519, Curve448)  | [XEdDSA](https://signal.org/docs/specifications/xeddsa/)   | A      |
| ECDSA (P-256, P-384, P-521)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-5/final)  | A      |
| RSA-RSSA-PSS                   | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | A      |
| RSA-SSA-PKCS#1 v1.5            | [RFC 8017](https://www.rfc-editor.org/info/rfc8017)        | D      |
| DSA (qualquer tamanho de chave)    | [FIPS 186-4](https://csrc.nist.gov/pubs/fips/186-4/final)  | D      |

## Padrões de Criptografia Pós-Quântica (Post-Quantum Encryption Standards)

As implementações de PQC devem estar em conformidade com [FIPS-203](https://csrc.nist.gov/pubs/fips/203/ipd)/[204](https://csrc.nist.gov/pubs/fips/204/ipd)/[205](https://csrc.nist.gov/pubs/fips/205/ipd), uma vez que há o mínimo de código fortalecido (hardened code) ou referência de implementação até o momento. https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards

O método de acordo de chaves TLS híbrido pós-quântico proposto [mlkem768x25519](https://datatracker.ietf.org/doc/draft-kwiatkowski-tls-ecdhe-mlkem/03/) é suportado pelos principais navegadores, como a [versão 132 do Firefox](https://www.mozilla.org/en-US/firefox/132.0/releasenotes/) e a [versão 131 do Chrome](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html). Ele pode ser usado em ambientes de teste criptográfico ou quando disponível em bibliotecas aprovadas pela indústria ou pelo governo.
