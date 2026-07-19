# O que é o ASVS?

O Padrão de Verificação de Segurança de Aplicações (Application Security Verification Standard - ASVS) define requisitos de segurança para aplicações e serviços web, e é um recurso valioso para qualquer pessoa que tenha como objetivo projetar, desenvolver e manter aplicações seguras ou avaliar sua segurança.

Este capítulo descreve os aspectos essenciais do uso do ASVS, incluindo seu escopo, a estrutura de seus níveis baseados em prioridade e os principais casos de uso para o padrão.

## Escopo do ASVS

O escopo do ASVS é definido pelo seu nome: Aplicação (Application), Segurança (Security), Verificação (Verification) e Padrão (Standard). Ele estabelece quais requisitos são incluídos ou excluídos, com o objetivo geral de identificar os princípios de segurança que devem ser alcançados. O escopo também considera os requisitos de documentação, que servem como base para os requisitos de implementação.

Não existe o conceito de escopo para atacantes. Portanto, os requisitos do ASVS devem ser avaliados em conjunto com as diretrizes para outros aspectos do ciclo de vida da aplicação, incluindo processos de CI/CD, hospedagem e atividades operacionais.

### Aplicação

O ASVS define uma "aplicação" como o produto de software em desenvolvimento, no qual controles de segurança devem ser integrados. O ASVS não prescreve atividades do ciclo de vida de desenvolvimento ou dita como a aplicação deve ser construída através de um pipeline de CI/CD; em vez disso, ele especifica os resultados de segurança que devem ser alcançados dentro do próprio produto.

Componentes que servem, modificam ou validam tráfego HTTP, como Web Application Firewalls (WAFs), balanceadores de carga ou proxies, podem ser considerados parte da aplicação para esses propósitos específicos, pois alguns controles de segurança dependem diretamente deles ou podem ser implementados através deles. Estes componentes devem ser considerados para requisitos relacionados a respostas em cache, limitação de taxa (rate limiting) ou restrição de conexões de entrada e saída com base na origem e no destino.

Por outro lado, o ASVS geralmente exclui requisitos que não são diretamente relevantes para a aplicação ou onde a configuração está fora da responsabilidade da aplicação. Por exemplo, problemas de DNS são tipicamente gerenciados por uma equipe ou função separada.

Da mesma forma, embora a aplicação seja responsável por como ela consome entradas e produz saídas, se um processo externo interage com a aplicação ou seus dados, ele é considerado fora do escopo do ASVS. Por exemplo, o backup da aplicação ou de seus dados geralmente é responsabilidade de um processo externo e não é controlado pela aplicação ou por seus desenvolvedores.

### Segurança

Todo requisito deve ter um impacto demonstrável na segurança. A ausência de um requisito deve resultar em uma aplicação menos segura, e a implementação do requisito deve reduzir a probabilidade ou o impacto de um risco de segurança.

Todas as outras considerações, como aspectos funcionais, estilo de código ou requisitos de política, estão fora do escopo.

### Verificação

O requisito deve ser verificável, e a verificação deve resultar em uma decisão de "falha" (fail) ou "aprovação" (pass).

### Padrão

O ASVS foi projetado para ser uma coleção de requisitos de segurança a serem implementados para estar em conformidade com o padrão. Isso significa que os requisitos se limitam a definir a meta de segurança para alcançar isso. Outras informações relacionadas podem ser construídas sobre o ASVS ou vinculadas por meio de mapeamentos.

Especificamente, a OWASP tem muitos projetos, e o ASVS evita deliberadamente a sobreposição com o conteúdo de outros projetos. Por exemplo, desenvolvedores podem ter a dúvida: "como implemento um requisito específico na minha tecnologia ou ambiente particular?", e isso deve ser coberto pelo projeto Cheat Sheet Series. Verificadores podem ter a dúvida: "como testo este requisito neste ambiente?", e isso deve ser coberto pelo projeto Web Security Testing Guide (WSTG).

Embora o ASVS não seja destinado apenas ao uso por especialistas em segurança, espera-se que o leitor tenha conhecimento técnico para entender o conteúdo ou a capacidade de pesquisar conceitos específicos.

### Requisito

A palavra requisito é usada especificamente no ASVS pois descreve o que deve ser alcançado para satisfazê-lo. O ASVS contém apenas requisitos (deve / must) e não contém recomendações (deveria / should) como condição principal.

Em outras palavras, recomendações, sejam elas apenas uma das muitas opções possíveis para resolver um problema ou considerações de estilo de código, não satisfazem a definição para serem um requisito.

Os requisitos do ASVS pretendem abordar princípios específicos de segurança sem serem muito específicos a implementações ou tecnologias, e ao mesmo tempo, sendo autoexplicativos quanto ao motivo de existirem. Isso também significa que os requisitos não são construídos em torno de um método de verificação ou implementação particular.

### Decisões de segurança documentadas

Na segurança de software, planejar o design de segurança e os mecanismos a serem usados logo no início levará a uma implementação mais consistente e confiável no produto ou funcionalidade final.

Além disso, para certos requisitos, a implementação será complicada e muito específica às necessidades de uma aplicação. Exemplos comuns incluem permissões, validação de entrada e controles de proteção em torno de diferentes níveis de dados sensíveis.

Para levar isso em conta, em vez de afirmações generalistas como "todos os dados devem ser criptografados" ou tentar cobrir todos os casos de uso possíveis em um requisito, foram incluídos requisitos de documentação que exigem que a abordagem e a configuração do desenvolvedor da aplicação para esses tipos de controles sejam documentadas. Isso pode então ser revisado quanto à adequação, e a implementação real pode ser comparada à documentação para avaliar se a implementação corresponde às expectativas.

Estes requisitos têm o objetivo de documentar as decisões que a organização que desenvolve a aplicação tomou em relação a como implementar determinados requisitos de segurança.

Os requisitos de documentação estão sempre na primeira seção de um capítulo (embora nem todo capítulo os tenha) e sempre têm um requisito de implementação relacionado onde as decisões documentadas devem realmente ser colocadas em prática. O ponto aqui é que verificar se a documentação está em vigor e se a implementação real ocorreu são duas atividades separadas.

Existem dois motivadores principais para incluir esses requisitos. O primeiro motivador é que um requisito de segurança muitas vezes envolverá a aplicação de regras, por exemplo, que tipo de arquivos são permitidos para upload, quais controles de negócios devem ser aplicados, quais são os caracteres permitidos para um campo específico. Essas regras serão diferentes para cada aplicação e, portanto, o ASVS não pode definir prescritivamente quais devem ser, nem um cheat sheet ou uma resposta mais detalhada ajudará neste caso. Da mesma forma, sem que essas decisões sejam documentadas, não será possível realizar a verificação dos requisitos que implementam essas decisões.

O segundo motivador é que, para certos requisitos, é importante fornecer ao desenvolvimento da aplicação flexibilidade sobre como abordar desafios de segurança particulares. Por exemplo, em versões anteriores do ASVS, as regras de timeout de sessão eram muito prescritivas. Na prática, muitas aplicações, especialmente aquelas voltadas para o consumidor, têm regras muito mais flexíveis e preferem implementar outros controles de mitigação em seu lugar. Os requisitos de documentação, portanto, permitem explicitamente flexibilidade em torno disso.

Claramente, não se espera que desenvolvedores individuais tomem e documentem essas decisões, mas sim que a organização como um todo tome essas decisões e garanta que sejam comunicadas aos desenvolvedores, que então se certificam de segui-las.

Fornecer aos desenvolvedores especificações e designs para novos recursos e funcionalidades é uma parte padrão do desenvolvimento de software. Da mesma forma, espera-se que os desenvolvedores usem componentes comuns e mecanismos de interface de usuário em vez de apenas tomar suas próprias decisões a cada vez. Sendo assim, estender isso para a segurança não deve ser visto como algo surpreendente ou controverso.

Também há flexibilidade sobre como alcançar isso. Decisões de segurança podem ser documentadas em um documento literal, ao qual se espera que os desenvolvedores consultem. Alternativamente, as decisões de segurança podem ser documentadas e implementadas em uma biblioteca de código comum que todos os desenvolvedores são obrigados a usar. Em ambos os casos, o resultado desejado é alcançado.

## Níveis de Verificação de Segurança de Aplicações

O ASVS define três níveis de verificação de segurança, com cada nível aumentando em profundidade e complexidade. O objetivo geral é que as organizações comecem pelo primeiro nível para lidar com as preocupações de segurança mais críticas e, em seguida, avancem para os níveis mais altos de acordo com as necessidades da organização e da aplicação. Os níveis podem ser apresentados como L1, L2 e L3 no documento e nos textos dos requisitos.

Cada nível do ASVS indica os requisitos de segurança que são obrigatórios para atingir aquele nível, com os requisitos restantes dos níveis superiores servindo como recomendações.

A fim de evitar requisitos duplicados ou requisitos que não são mais relevantes em níveis mais altos, alguns requisitos se aplicam a um nível específico, mas têm condições mais rigorosas para níveis superiores.

### Avaliação de Nível

Os níveis são definidos por uma avaliação baseada em prioridade de cada requisito, fundamentada na experiência de implementação e teste de requisitos de segurança. O foco principal é comparar a redução de risco com o esforço para implementar o requisito. Outro fator-chave é manter uma barreira de entrada baixa.

A redução de risco considera até que ponto o requisito reduz o nível de risco de segurança dentro da aplicação, levando em conta os clássicos fatores de impacto de Confidencialidade, Integridade e Disponibilidade (CIA), bem como considerando se esta é uma camada primária de defesa ou se seria considerada defesa em profundidade (defense in depth).

As discussões rigorosas em torno dos critérios e das decisões de nivelamento resultaram em uma alocação que deve ser verdadeira para a grande maioria dos casos, embora se aceite que pode não ser 100% adequada para todas as situações. Isso significa que, em certos casos, as organizações podem desejar priorizar requisitos de um nível mais alto mais cedo, com base em suas próprias considerações de risco específicas.

Os tipos de requisitos em cada nível podem ser caracterizados da seguinte forma.

### Nível 1

Este nível contém os requisitos mínimos a serem considerados ao proteger uma aplicação e representa um ponto de partida crítico. Este nível contém cerca de 20% dos requisitos do ASVS. O objetivo para este nível é ter o menor número possível de requisitos, para diminuir a barreira de entrada.

Esses requisitos geralmente são críticos ou básicos, requisitos de primeira camada de defesa para prevenir ataques comuns que não requerem outras vulnerabilidades ou pré-condições para serem exploráveis.

Além dos requisitos de primeira camada de defesa, alguns requisitos têm um impacto menor em níveis mais altos, como os requisitos relacionados a senhas. Eles são mais importantes para o Nível 1, pois a partir de níveis mais altos, os requisitos de autenticação multifator (MFA) tornam-se relevantes.

O Nível 1 não é necessariamente testável por intrusão (penetration test) por um testador externo sem acesso interno a documentação ou código (como em testes do tipo "caixa preta" ou "black box"), embora o menor número de requisitos deva torná-lo mais fácil de verificar.

### Nível 2

A maioria das aplicações deveria se esforçar para atingir este nível de segurança. Cerca de 50% dos requisitos no ASVS são L2, o que significa que uma aplicação precisa implementar cerca de 70% dos requisitos no ASVS (todos os requisitos L1 e L2) a fim de estar em conformidade com o L2.

Esses requisitos geralmente se relacionam com ataques menos comuns ou proteções mais complicadas contra ataques comuns. Eles ainda podem ser uma primeira camada de defesa ou podem exigir certas pré-condições para que o ataque seja bem-sucedido.

### Nível 3

Este nível deve ser a meta para aplicações que buscam demonstrar os mais altos níveis de segurança e fornece os cerca de 30% finais dos requisitos a serem cumpridos.

Os requisitos nesta seção geralmente são mecanismos de defesa em profundidade ou outros controles úteis, mas difíceis de implementar.

### Qual nível alcançar

Os níveis baseados em prioridade destinam-se a fornecer um reflexo da maturidade de segurança de aplicações da organização e da aplicação. Em vez de o ASVS afirmar de forma prescritiva em qual nível uma aplicação deve estar, uma organização deve analisar seus riscos e decidir em qual nível acredita que deve estar, dependendo da sensibilidade da aplicação e, claro, das expectativas dos usuários da aplicação.

Por exemplo, uma startup em estágio inicial que coleta apenas dados sensíveis limitados pode decidir se concentrar no Nível 1 para seus objetivos de segurança iniciais, mas um banco pode ter dificuldade em justificar qualquer coisa inferior ao Nível 3 aos seus clientes para sua aplicação de internet banking.

## Como usar o ASVS

### A estrutura do ASVS

O ASVS é composto por um total de cerca de 350 requisitos, que são divididos em 17 capítulos, cada um dos quais é subdividido em seções.

O objetivo da divisão de capítulos e seções é simplificar a escolha ou filtragem de capítulos e seções com base no que é relevante para a aplicação. Por exemplo, para uma API máquina a máquina (machine-to-machine), os requisitos do capítulo V3 relacionados a frontends web não serão relevantes. Se não houver uso de OAuth ou WebRTC, esses capítulos também podem ser ignorados.

### Estratégia de Lançamento

Os lançamentos do ASVS seguem o padrão "Major.Minor.Patch" (Maior.Menor.Correção) e os números fornecem informações sobre o que mudou na versão. Em uma versão principal (major), o primeiro número mudará; em uma versão menor (minor), o segundo número mudará; e em uma versão de correção (patch), o terceiro número mudará.

* Major release (Lançamento Maior) - Reorganização completa, quase tudo pode ter mudado, incluindo os números dos requisitos. A reavaliação de conformidade será necessária (por exemplo, 4.0.3 -> 5.0.0).
* Minor release (Lançamento Menor) - Requisitos podem ser adicionados ou removidos, mas a numeração geral permanecerá a mesma. A reavaliação de conformidade será necessária, mas deve ser mais fácil (por exemplo, 5.0.0 -> 5.1.0).
* Patch release (Lançamento de Correção) - Requisitos podem ser removidos (por exemplo, se forem duplicados ou desatualizados) ou tornados menos rigorosos, mas uma aplicação que estava em conformidade com o lançamento anterior também estará em conformidade com a versão de correção (por exemplo, 5.0.0 -> 5.0.1).

O acima relaciona-se especificamente aos requisitos do ASVS. Mudanças no texto ao redor e em outros conteúdos, como os apêndices, não serão consideradas uma mudança com quebra de compatibilidade (breaking change).

### Flexibilidade com o ASVS

Vários dos pontos descritos acima, como requisitos de documentação e o mecanismo de níveis, fornecem a capacidade de usar o ASVS de forma mais flexível e específica da organização.

Além disso, as organizações são fortemente encorajadas a criar um fork (ramificação) específico da organização ou do domínio que ajuste os requisitos com base nas características e níveis de risco específicos de suas aplicações. No entanto, é importante manter a rastreabilidade para que ser aprovado no requisito 4.1.1 signifique o mesmo em todas as versões.

O ideal é que cada organização crie seu próprio ASVS personalizado, omitindo seções irrelevantes (por exemplo, GraphQL, WebSockets, SOAP, se não forem usados). Uma versão ou suplemento do ASVS específico da organização também é um bom lugar para fornecer orientações de implementação específicas da organização, detalhando bibliotecas ou recursos a serem usados ao cumprir os requisitos.

### Como Referenciar os Requisitos do ASVS

Cada requisito tem um identificador no formato `<capítulo>.<seção>.<requisito>`, onde cada elemento é um número. Por exemplo, `1.11.3`.

* O valor `<capítulo>` corresponde ao capítulo do qual o requisito se origina; por exemplo, todos os requisitos `1.#.#` são do capítulo 'Codificação e Sanitização' (Encoding and Sanitization).
* O valor `<seção>` corresponde à seção dentro daquele capítulo onde o requisito aparece, por exemplo: todos os requisitos `1.2.#` estão na seção 'Prevenção de Injeção' (Injection Prevention) do capítulo 'Codificação e Sanitização'.
* O valor `<requisito>` identifica o requisito específico dentro do capítulo e seção, por exemplo, `1.2.5` que a partir da versão 5.0.0 deste padrão é:

> Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding.
*(Verifique se a aplicação protege contra injeção de comando no sistema operacional (OS) e se as chamadas de sistema operacional usam consultas de OS parametrizadas ou usam codificação de saída de linha de comando contextual).*

Como os identificadores podem mudar entre versões do padrão, é preferível que outros documentos, relatórios ou ferramentas usem o seguinte formato: `v<versão>-<capítulo>.<seção>.<requisito>`, onde: 'versão' é a tag da versão do ASVS. Por exemplo: `v5.0.0-1.2.5` seria entendido como especificamente o 5º requisito na seção 'Prevenção de Injeção' do capítulo 'Codificação e Sanitização' da versão 5.0.0. (Isso poderia ser resumido como `v<versão>-<identificador_do_requisito>`.)

Nota: A letra `v` que precede o número da versão no formato deve sempre ser minúscula.

Se os identificadores forem usados sem incluir o elemento `v<versão>`, deve-se presumir que eles se referem ao conteúdo mais recente do Application Security Verification Standard. À medida que o padrão cresce e muda, isso se torna problemático, e é por isso que escritores ou desenvolvedores devem incluir o elemento de versão.

As listas de requisitos do ASVS são disponibilizadas em formatos CSV, JSON e outros que podem ser úteis para referência ou uso programático.

### Fazendo Fork do ASVS

As organizações podem se beneficiar da adoção do ASVS escolhendo um dos três níveis ou criando um fork específico do domínio que ajusta os requisitos de acordo com o nível de risco da aplicação. Esse tipo de fork é encorajado, desde que mantenha a rastreabilidade para que a aprovação no requisito 4.1.1 signifique o mesmo em todas as versões.

Idealmente, cada organização deve criar seu próprio ASVS adaptado, omitindo seções irrelevantes (por exemplo, GraphQL, WebSockets, SOAP, se não forem usados). O forking deve começar com o Nível 1 do ASVS como base, avançando para os Níveis 2 ou 3 com base no risco da aplicação.

## Casos de uso para o ASVS

O ASVS pode ser usado para avaliar a segurança de uma aplicação, e isso é explorado mais a fundo no próximo capítulo. No entanto, vários outros usos potenciais para o ASVS (ou uma versão em fork) foram identificados.

### Como Guia Detalhado de Arquitetura de Segurança

Um dos usos mais comuns do Application Security Verification Standard é como um recurso para arquitetos de segurança. Existem recursos limitados disponíveis sobre como construir uma arquitetura de aplicação segura, especialmente para aplicações modernas. O ASVS pode ser usado para preencher essas lacunas, permitindo que os arquitetos de segurança escolham melhores controles para problemas comuns, como padrões de proteção de dados e estratégias de validação de entrada. Os requisitos de arquitetura e documentação serão particularmente úteis para isso.

### Como Referência Especializada de Codificação Segura

O ASVS pode ser usado como base para preparar uma referência de codificação segura durante o desenvolvimento de aplicações, ajudando os desenvolvedores a garantirem que mantenham a segurança em mente ao construir software. Embora o ASVS possa ser a base, as organizações devem preparar suas próprias diretrizes específicas, que sejam claras e unificadas, e idealmente preparadas com base na orientação de engenheiros de segurança ou arquitetos de segurança. Como extensão a isso, as organizações são encorajadas, sempre que possível, a preparar mecanismos de segurança e bibliotecas aprovadas que possam ser referenciadas nas diretrizes e usadas pelos desenvolvedores.

### Como Guia para Testes Automatizados de Unidade e Integração

O ASVS foi projetado para ser altamente testável. Algumas verificações serão técnicas, enquanto outros requisitos (como os requisitos arquitetônicos e de documentação) podem exigir revisão de documentação ou de arquitetura. Ao construir testes de unidade e de integração que testem e façam fuzzing para casos de abuso específicos e relevantes relacionados aos requisitos que são verificáveis por meios técnicos, deve ser mais fácil verificar se esses controles estão operando corretamente em cada build. Por exemplo, testes adicionais podem ser elaborados para a suíte de testes de um controlador de login, testando o parâmetro de nome de usuário para nomes de usuário padrão comuns, enumeração de contas, força bruta, injeção de LDAP e SQL e XSS. Da mesma forma, um teste no parâmetro de senha deve incluir senhas comuns, comprimento de senha, injeção de byte nulo, remoção do parâmetro, XSS e muito mais.

### Para Treinamento de Desenvolvimento Seguro

O ASVS também pode ser usado para definir as características de um software seguro. Muitos cursos de “codificação segura” são simplesmente cursos de hacking ético com uma leve camada de dicas de codificação. Isso pode não necessariamente ajudar os desenvolvedores a escreverem códigos mais seguros. Em vez disso, cursos de desenvolvimento seguro podem usar o ASVS com um forte foco nos mecanismos positivos encontrados no ASVS, em vez das 10 principais coisas negativas que não se deve fazer (Top 10). A estrutura do ASVS também fornece uma estrutura lógica para percorrer os diferentes tópicos ao proteger uma aplicação.

### Como Framework para Guiar a Aquisição de Software Seguro

O ASVS é um excelente framework para ajudar na aquisição de software seguro ou na aquisição de serviços de desenvolvimento sob medida. O comprador pode simplesmente estabelecer um requisito de que o software que deseja adquirir deve ser desenvolvido no nível X do ASVS e solicitar que o vendedor comprove que o software satisfaz o nível X do ASVS.

## Aplicando o ASVS na Prática

Ameaças diferentes têm motivações diferentes. Algumas indústrias possuem ativos de informação e tecnologia únicos, bem como requisitos de conformidade regulatória específicos de domínio.

As organizações são fortemente encorajadas a analisar profundamente suas características únicas de risco com base na natureza de seus negócios e, com base nesse risco e nos requisitos de negócios, determinar o nível apropriado do ASVS.