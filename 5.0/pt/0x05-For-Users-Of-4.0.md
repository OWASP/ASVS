# Alterações em Relação à Versão 4.x

## Introdução

Os usuários familiarizados com a versão 4.x do padrão podem achar útil revisar as principais alterações introduzidas na versão 5.0, incluindo atualizações de conteúdo, escopo e filosofia subjacente.

Dos 286 requisitos da versão 4.0.3, apenas 11 permanecem inalterados, enquanto 15 passaram por pequenos ajustes gramaticais sem alterar seu significado. No total, 109 requisitos (38%) não são mais requisitos separados na versão 5.0, com 50 simplesmente sendo excluídos, 28 removidos como duplicados e 31 mesclados em outros requisitos. O restante foi revisado de alguma forma. Mesmo os requisitos que não foram substancialmente modificados têm identificadores diferentes devido à reordenação ou reestruturação.

Para facilitar a adoção da versão 5.0, documentos de mapeamento são fornecidos para ajudar os usuários a rastrear como os requisitos da versão 4.x correspondem aos da versão 5.0. Estes mapeamentos não estão vinculados ao versionamento de lançamentos e podem ser atualizados ou esclarecidos conforme necessário.

## Filosofia dos Requisitos

### Escopo e Foco

A versão 4.x incluía requisitos que não se alinhavam com o escopo pretendido do padrão; estes foram removidos. Requisitos que não atendiam aos critérios de escopo para a versão 5.0 ou não eram verificáveis também foram excluídos.

### Ênfase nos Objetivos de Segurança Sobre os Mecanismos

Na versão 4.x, muitos requisitos se concentravam em mecanismos específicos, em vez dos objetivos de segurança subjacentes. Na versão 5.0, os requisitos estão centrados nas metas de segurança, fazendo referência a mecanismos particulares apenas quando são a única solução prática, ou fornecendo-os como exemplos ou orientação complementar.

Essa abordagem reconhece que podem existir vários métodos para atingir um determinado objetivo de segurança e evita uma prescritividade desnecessária que poderia limitar a flexibilidade organizacional.

Além disso, requisitos que abordam a mesma preocupação de segurança foram consolidados quando apropriado.

### Decisões de Segurança Documentadas

Embora o conceito de decisões de segurança documentadas possa parecer novo na versão 5.0, ele é uma evolução de requisitos anteriores relacionados à aplicação de políticas e modelagem de ameaças na versão 4.0. Anteriormente, alguns requisitos exigiam implicitamente análises para informar a implementação de controles de segurança, como a determinação de conexões de rede permitidas.

Para garantir que as informações necessárias estejam disponíveis para implementação e verificação, essas expectativas agora são explicitamente definidas como requisitos de documentação, tornando-os claros, acionáveis e verificáveis.

## Mudanças Estruturais e Novos Capítulos

Vários capítulos na versão 5.0 introduzem conteúdo totalmente novo:

* OAuth e OIDC – Dada a ampla adoção desses protocolos para delegação de acesso e logon único (single sign-on), requisitos dedicados foram adicionados para abordar os diversos cenários que os desenvolvedores podem encontrar. Essa área pode eventualmente evoluir para um padrão autônomo, semelhante ao tratamento dos requisitos de Mobile e IoT em versões anteriores.
* WebRTC – À medida que essa tecnologia ganha popularidade, suas considerações e desafios de segurança exclusivos agora são abordados em uma seção dedicada.

Esforços também foram feitos para garantir que capítulos e seções sejam organizados em torno de conjuntos coerentes de requisitos relacionados.

Esta reestruturação levou à criação de capítulos adicionais:

* Tokens Autocontidos (Self-contained Tokens) – Anteriormente agrupados no gerenciamento de sessão, os tokens autocontidos agora são reconhecidos como um mecanismo distinto e um elemento fundamental para comunicação sem estado (como no OAuth e OIDC). Devido às suas implicações de segurança exclusivas, eles são abordados em um capítulo dedicado, com alguns novos requisitos introduzidos na versão 5.x.
* Segurança de Frontend Web – Com a crescente complexidade das aplicações baseadas em navegador e a ascensão de arquiteturas exclusivas de API (API-only), os requisitos de segurança de frontend foram separados em seu próprio capítulo.
* Codificação e Arquitetura Seguras – Novos requisitos que abordam práticas gerais de segurança que não se encaixavam nos capítulos existentes foram agrupados aqui.

Outras mudanças organizacionais na versão 5.0 foram feitas para esclarecer a intenção. Por exemplo, os requisitos de validação de entrada foram movidos para o lado da lógica de negócios, refletindo seu papel na aplicação de regras de negócios, em vez de serem agrupados com sanitização e codificação.

O antigo capítulo de Arquitetura (V1) foi removido. Sua seção inicial continha requisitos que estavam fora do escopo, enquanto as seções subsequentes foram redistribuídas para capítulos relevantes, com requisitos desduplicados e esclarecidos conforme necessário.

## Remoção de Mapeamentos Diretos para Outros Padrões

Mapeamentos diretos para outros padrões foram removidos do corpo principal do padrão. O objetivo é preparar um mapeamento com o projeto OWASP Common Requirement Enumeration (CRE), que, por sua vez, vinculará o ASVS a uma série de projetos da OWASP e padrões externos.

Mapeamentos diretos para CWE e NIST não são mais mantidos, conforme explicado abaixo.

### Redução do Acoplamento com as Diretrizes de Identidade Digital do NIST

As [Diretrizes de Identidade Digital do NIST (SP 800-63)](https://pages.nist.gov/800-63-3/) servem há muito tempo como referência para controles de autenticação e autorização. Na versão 4.x, certos capítulos estavam intimamente alinhados com a estrutura e terminologia do NIST.

Embora estas diretrizes continuem sendo uma referência importante, o alinhamento estrito introduziu desafios, incluindo terminologia menos amplamente reconhecida, duplicação de requisitos semelhantes e mapeamentos incompletos. A versão 5.0 se afasta dessa abordagem para melhorar a clareza e a relevância.

### Afastamento da Common Weakness Enumeration (CWE)

A [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) fornece uma taxonomia útil de fraquezas na segurança de software. No entanto, desafios como CWEs exclusivas de categoria, dificuldades em mapear requisitos para uma única CWE e a presença de mapeamentos imprecisos na versão 4.x levaram à decisão de descontinuar os mapeamentos diretos de CWE na versão 5.0.

## Repensando as Definições de Nível

A versão 4.x descrevia os níveis como L1 ("Mínimo"), L2 ("Padrão") e L3 ("Avançado"), com a implicação de que todas as aplicações que lidam com dados sensíveis deveriam atender pelo menos ao L2.

A versão 5.0 aborda vários problemas com essa abordagem, que são descritos nos parágrafos a seguir.

Como uma questão prática, enquanto a versão 4.x usava marcas de seleção (tick marks) para indicadores de nível, a 5.x usa um número simples em todos os formatos do padrão, incluindo markdown, PDF, DOCX, CSV, JSON e XML. Para compatibilidade com versões anteriores, versões legadas das saídas CSV, JSON e XML que ainda usam marcas de seleção também são geradas.

### Nível de Entrada Mais Fácil

O feedback indicou que o grande número de requisitos do Nível 1 (~120), combinado com a sua designação como o nível "mínimo" que não é bom o suficiente para a maioria das aplicações, desencorajava a adoção. A versão 5.0 visa diminuir essa barreira definindo o Nível 1 principalmente em torno de requisitos de primeira camada de defesa, resultando em requisitos mais claros e em menor número nesse nível. Para demonstrar isso numericamente, na versão 4.0.3 havia 128 requisitos L1 em um total de 278 requisitos, representando 46%. Na 5.0.0, existem 70 requisitos L1 de um total de 345 requisitos, representando 20%.

### A Falácia da Testabilidade

Um fator-chave na seleção de controles para o Nível 1 na versão 4.x era a sua adequação para avaliação através de testes de intrusão externos tipo "caixa preta" (black box). No entanto, esta abordagem não estava totalmente alinhada com a intenção do Nível 1 como o conjunto mínimo de controles de segurança. Alguns usuários argumentaram que o Nível 1 era insuficiente para proteger as aplicações, enquanto outros o consideravam muito difícil de testar.

Confiar na testabilidade como um critério é algo relativo e, por vezes, enganoso. O fato de um requisito ser testável não garante que ele possa ser testado de maneira automatizada ou direta. Além disso, os requisitos mais facilmente testáveis nem sempre são aqueles com o maior impacto de segurança ou os mais simples de implementar.

Sendo assim, na versão 5.0, as decisões de nível foram tomadas principalmente com base na redução de risco e também mantendo em mente o esforço para implementar.

### Não se Trata Apenas de Risco

O uso de níveis prescritivos e baseados em risco que exigem um nível específico para certas aplicações provou ser excessivamente rígido. Na prática, a priorização e a implementação de controles de segurança dependem de vários fatores, incluindo a redução de risco e o esforço necessário para a implementação.

Portanto, as organizações são encorajadas a alcançar o nível que acreditam que deveriam alcançar com base em sua maturidade e na mensagem que desejam transmitir aos seus usuários.
