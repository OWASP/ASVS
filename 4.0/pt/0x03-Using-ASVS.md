# Usando o ASVS

A ASVS tem dois objetivos principais:

* ajudar as organizações a desenvolver e manter aplicações seguros.
* permitir que fornecedores de serviços de segurança, fornecedores de ferramentas de segurança e consumidores alinhem seus requisitos e ofertas.

## Níveis do Application Security Verification

O Application Security Verification Standard define três níveis de verificação de segurança, com cada nível aumentando em profundidade.

* O nível 1 do ASVS é para níveis de garantia baixos e é completamente testável quanto à penetração
* ASVS Nível 2 é para aplicações que contêm dados confidenciais, que requerem proteção e é o nível recomendado para a maioria das aplicações
* O nível 3 do ASVS é para as aplicações mais críticos - aplicações que executam transações de alto valor, contêm dados médicos confidenciais ou qualquer aplicação que exija o mais alto nível de confiança.

Cada nível ASVS contém uma lista de requisitos de segurança. Cada um desses requisitos também pode ser mapeado para recursos e capacidades específicos de segurança que devem ser incorporados ao software pelos desenvolvedores.

![Níveis ASVS](https://raw.githubusercontent.com/OWASP/ASVS/master/4.0/images/asvs_40_levels.png "Níveis ASVS")

Figura 1 - Níveis 4.0 do Padrão de Application Security Verification OWASP

O nível 1 é o único nível que é completamente testável por penetração usando humanos. Todos os outros requerem acesso à documentação, código-fonte, configuração e pessoas envolvidas no processo de desenvolvimento. No entanto, mesmo que L1 permita a ocorrência de testes de "black box" (sem documentação e sem fonte), não é uma atividade de garantia eficaz e deve ser ativamente desencorajada. Os atacantes mal-intencionados têm muito tempo, a maioria dos testes de penetração termina em algumas semanas. Os defensores precisam incorporar controles de segurança, proteger, encontrar e resolver todos os pontos fracos, detectar e responder a agentes mal-intencionados num tempo razoável. Atores mal-intencionados têm tempo essencialmente infinito e requerem apenas uma única defesa porosa, uma única fraqueza ou detecção ausente para serem bem-sucedidos. O teste black box, muitas vezes realizado no final do desenvolvimento, rapidamente, ou não, são completamente incapazes de lidar com essa assimetria.

Ao longo dos últimos 30 anos, os testes black box provaram repetidas vezes perder problemas críticos de segurança que levaram diretamente a violações cada vez mais massivas. Incentivamos fortemente o uso de uma ampla gama de garantia e verificação de segurança, incluindo a substituição de testes de penetração por testes de penetração conduzidos por código-fonte (híbridos) no Nível 1, com acesso total aos desenvolvedores e à documentação durante todo o processo de desenvolvimento. Os reguladores financeiros não toleram auditorias financeiras externas sem acesso aos livros contábeis, amostras de transações ou pessoas que executam os controles. A indústria e os governos devem exigir o mesmo padrão de transparência no campo da engenharia de software.

Incentivamos fortemente o uso de ferramentas de segurança no próprio processo de desenvolvimento. As ferramentas DAST e SAST podem ser usadas continuamente pelo pipeline de construção para facilitar a localização de problemas de segurança que nunca deveriam estar presentes.

Ferramentas automatizadas e varreduras online não conseguem concluir mais da metade do ASVS sem assistência humana. Se for necessária uma automação de teste abrangente para cada compilação, será usada uma combinação de testes personalizados de unidade e integração, com varreduras online iniciadas por compilação. Falhas de lógica de negócios e testes de controle de acesso só são possíveis com assistência humana. Estes devem ser transformados em testes de unidade e integração.

## Como usar este padrão

Uma das melhores maneiras de usar o Application Security Verification Standard é usá-lo como um modelo para criar uma Lista de Verificação de Codificação Segura específica para sua aplicação, plataforma ou organização. Adaptar o ASVS aos seus casos de uso aumentará o foco nos requisitos de segurança mais importantes para seus projetos e ambientes.

### Nível 1 - Primeiras etapas, automatizada ou visão completa do portfólio

Uma aplicação atinge o nível 1 do ASVS se se defender adequadamente contra vulnerabilidades de segurança de aplicações que são fáceis de descobrir e incluídas no OWASP Top 10 e outras listas de verificação semelhantes.

O nível 1 é o mínimo que todas as aplicações devem buscar. Também é útil como uma primeira etapa num esforço multifásico ou quando as aplicações não armazenam ou manipulam dados confidenciais e, assim, não precisam de controles mais rigorosos de nível 2 ou 3. Os controles de nível 1 podem ser verificados automaticamente por ferramentas ou simplesmente manualmente, sem acesso ao código-fonte. Consideramos o Nível 1 o mínimo exigido para todas as aplicações.

Ameaças à aplicação provavelmente virão de invasores que usam técnicas simples e de baixo esforço para identificar vulnerabilidades fáceis de encontrar e explorar. Isso contrasta com um invasor determinado que gastará energia focada para atingir especificamente a aplicação. Se os dados processados pela sua aplicação tiverem alto valor, raramente irá parar numa revisão de nível 1.

### Nível 2 - A maioria das aplicações

Uma aplicação atinge o nível 2 (ou padrão) do ASVS se se defender adequadamente contra a maioria dos riscos associados ao software atualmente.

O nível 2 garante que os controles de segurança estejam em vigor, sejam eficazes e sejam usados na aplicação. O nível 2 é normalmente apropriado para aplicações que lidam com transações business-to-business significativas, incluindo aquelas que processam informações de assistência médica, implementam funções críticas, ou confidenciais de negócios, ou processam outros ativos confidenciais, ou setores onde a integridade é uma faceta crítica para proteger os seus negócios, como a indústria de jogos para impedir trapaceiros e hacks de jogos.

Ameaças aas aplicações de nível 2 normalmente são invasores habilidosos e motivados com foco em alvos específicos usando ferramentas e técnicas que são altamente praticadas e eficazes na descoberta e exploração de pontos fracos nas aplicações.

### Nível 3 - Alto valor, alta garantia ou alta segurança

ASVS Nível 3 é o mais alto nível de verificação no ASVS. Este nível é normalmente reservado para aplicações que requerem níveis significativos de verificação de segurança, como aqueles que podem ser encontrados em áreas militares, de saúde e segurança, infraestrutura crítica, etc.

As organizações podem exigir ASVS Nível 3 para aplicações que executam funções críticas, onde a falha pode afetar significativamente as operações da organização e até mesmo a sua capacidade de sobrevivência. Um exemplo de orientação sobre a aplicação do ASVS Nível 3 é fornecido abaixo. Uma aplicação atinge o Nível 3 do ASVS (ou Avançado) se defender adequadamente contra vulnerabilidades de segurança de aplicações avançados e também demonstrar princípios de um bom design de segurança.

Uma aplicação no nível 3 do ASVS requer uma análise mais aprofundada da arquitetura, codificação e teste do que todos os outros níveis. Uma aplicação seguro é modularizado de forma significativa (para facilitar a resiliência, escalabilidade e, primeiro, camadas de segurança), e cada módulo (separado por conexão de rede e/ou instância física) cuida das suas próprias responsabilidades de segurança (defesa em profundidade), que precisam ser devidamente documentados. As responsabilidades incluem controles para garantir a confidencialidade (por exemplo, criptografia), integridade (por exemplo, transações, validação de input), disponibilidade (por exemplo, manipulação de carga normalmente), autenticação (incluindo entre sistemas), autorização e auditoria (logging).

## Aplicando ASVS na Prática

Ameaças diferentes têm motivações diferentes. Alguns setores têm informações exclusivas e ativos de tecnologia e requisitos de conformidade regulamentar específicos do domínio.

As organizações são fortemente encorajadas a analisar profundamente as suas características de risco exclusivas com base na natureza dos seus negócios e, com base nesse risco e nos requisitos de negócios, determinar o nível ASVS apropriado.

## Como fazer referência aos requisitos ASVS

Cada requisito possui um identificador no formato `<chapter>.<section>.<requirement>` onde cada elemento é um número, por exemplo: `1.11.3`.
- O valor `<chapter>` corresponde ao capítulo de onde vem o requisito, por exemplo: todos os requisitos `1.#.#` são do capítulo `Arquitetura`.
- O valor `<section>` corresponde à seção dentro desse capítulo onde o requisito aparece, por exemplo: todos os requisitos `1.11.#` estão na seção `Arquitetura de lógica de negócios` do capítulo `Arquitetura`.
- O valor `<requirement>` identifica o requisito específico no capítulo e seção, por exemplo: `1.11.3` que a partir da versão 4.0.3 desta norma é:

> Verifique se todos os fluxos de lógica de negócios de alto valor, incluindo autenticação, gestão de sessão e controle de acesso, são thread-safe e resistentes a condições de corrida de tempo de verificação e tempo de uso.

Os identificadores podem mudar entre as versões do padrão, portanto, é preferível que outros documentos, relatórios ou ferramentas usem o formato: `v<version>-<chapter>.<section>.<requirement>`, onde: 'versão' é a tag de versão ASVS. Por exemplo: `v4.0.3-1.11.3` seria entendido como significando especificamente o 3.º requisito na seção 'Arquitetura de lógica de negócios' do capítulo 'Arquitetura' da versão 4.0.3. (Isto pode ser resumido como `v<version>-<requirement_identifier>`.)

Nota: O `v` que precede a parte da versão deve ser minúsculo.

Se os identificadores forem usados sem incluir o elemento `v<version>`, eles devem ser assumidos para se referir ao conteúdo mais recente do Application Security Verification Standard. Obviamente, à medida que o padrão cresce e muda, isso se torna problemático, e é por isso que escritores ou desenvolvedores devem incluir o elemento de versão.

As listas de requisitos ASVS são disponibilizadas em CSV, JSON e outros formatos que podem ser úteis para referência ou uso programático.