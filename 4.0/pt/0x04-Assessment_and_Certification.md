# Avaliação e Certificação

## Postura da OWASP em certificações ASVS e marcas de confiança

A OWASP, como uma organização sem fins lucrativos neutra em termos de fornecedores, atualmente não certifica nenhum fornecedor, verificador ou software.

Todas essas afirmações de garantia, marcas de confiança ou certificações não são oficialmente examinadas, registradas ou certificadas pela OWASP, portanto, uma organização que confia em tal visão precisa ser cautelosa com a confiança depositada em qualquer terceiro ou marca de confiança que reivindique a certificação ASVS.

Isso não deve inibir as organizações de oferecer tais serviços de garantia, desde que não reivindiquem a certificação OWASP oficial.

## Orientação para organizações certificadoras

O Application Security Verification Standard pode ser usado como uma verificação de livro aberto da aplicação, incluindo acesso aberto e irrestrito a recursos-chave, como arquitetos e desenvolvedores, documentação do projeto, código-fonte, acesso autenticado a sistemas de teste (incluindo acesso a uma ou mais contas em cada função), especialmente para verificações L2 e L3.

Historicamente, os testes de penetração e as revisões de código seguro incluíram problemas “por exceção”, ou seja, apenas os testes com falha aparecem no relatório final. Uma organização certificadora deve incluir em qualquer relatório o escopo da verificação (especialmente se um componente-chave estiver fora do escopo, como a autenticação SSO), um resumo das descobertas da verificação, incluindo testes aprovados e reprovados, com indicações claras de como resolver o problema testes falhados.

Certos requisitos de verificação podem não ser aplicáveis à aplicação em teste. Por exemplo, se você fornecer uma API de camada de serviço sem estado sem uma implementação de cliente para seus clientes, muitos dos requisitos do V3 Session Management não serão diretamente aplicáveis. Nesses casos, uma organização certificadora ainda pode reivindicar conformidade total com a ASVS, mas deve indicar claramente em qualquer relatório um motivo para a não aplicabilidade de tais requisitos de verificação excluídos.

Manter papéis de trabalho detalhados, capturas de tela ou filmes, scripts para explorar um problema de maneira confiável e repetida e registros eletrônicos de teste, como interceptar logs de proxy e notas associadas, como uma lista de limpeza, é considerado uma prática padrão da indústria e pode ser realmente útil como prova das descobertas para os desenvolvedores mais duvidosos. Não basta simplesmente rodar uma ferramenta e reportar as falhas; isso não fornece (de forma alguma) evidência suficiente de que todos os problemas em um nível de certificação foram testados e testados exaustivamente. Em caso de disputa, deve haver evidência de garantia suficiente para demonstrar que cada requisito verificado foi de fato testado.

### Método de teste

As organizações certificadoras são livres para escolher o(s) método(s) de ensaio apropriado(s), mas devem indicá-los em um relatório.

Dependendo da aplicação em teste e do requisito de verificação, diferentes métodos de teste podem ser usados para obter a mesma confiança nos resultados. Por exemplo, validar a eficácia dos mecanismos de verificação de input de uma aplicação pode ser analisado com um teste de penetração manual ou por análises de código-fonte.

#### O papel das ferramentas automatizadas de teste de segurança

O uso de ferramentas automatizadas de teste de penetração é incentivado para fornecer o máximo de cobertura possível.

Não é possível concluir totalmente a verificação ASVS usando apenas ferramentas automatizadas de teste de penetração. Embora a grande maioria dos requisitos em L1 possa ser realizada usando testes automatizados, a maioria geral dos requisitos não é passível de testes de penetração automatizados.

Observe que as linhas entre testes automatizados e manuais se tornaram indistintas à medida que o setor de segurança de aplicações amadureceu. As ferramentas automatizadas geralmente são ajustadas manualmente por especialistas e os testadores manuais geralmente utilizam uma ampla variedade de ferramentas automatizadas.

#### O papel do teste de penetração

Na versão 4.0, decidimos tornar o L1 completamente testável sem acesso ao código-fonte, documentação ou desenvolvedores. Dois itens de registro, que são necessários para cumprir o OWASP Top 10 2017 A10, exigirão entrevistas, capturas de tela ou outra coleta de evidências, assim como no OWASP Top 10 2017. No entanto, testar sem acesso às informações necessárias não é um método ideal de verificação de segurança, pois perde a possibilidade de revisar a fonte, identificar ameaças e controles ausentes e realizar um teste muito mais completo em um período de tempo menor.

Sempre que possível, é necessário acesso a desenvolvedores, documentação, código e acesso a uma aplicação de teste com dados que não sejam de produção ao realizar uma avaliação L2 ou L3. Os testes de penetração feitos nesses níveis requerem esse nível de acesso, que chamamos de "revisões híbridas" ou "testes de penetração híbridos".

## Outros usos para o ASVS

Além de ser usado para avaliar a segurança de uma aplicação, identificamos vários outros usos potenciais para o ASVS.

### Conforme orientação detalhada da arquitetura de segurança

Um dos usos mais comuns do Application Security Verification Standard é como um recurso para arquitetos de segurança. A Sherwood Applied Business Security Architecture (SABSA) carece de uma grande quantidade de informações necessárias para concluir uma revisão completa da arquitetura de segurança da aplicação. O ASVS pode ser usado para preencher essas lacunas, permitindo que os arquitetos de segurança escolham melhores controles para problemas comuns, como padrões de proteção de dados e estratégias de validação de input.

### Como um substituto para listas de verificação de codificação segura prontas para uso

Muitas organizações podem se beneficiar da adoção do ASVS, escolhendo um dos três níveis ou bifurcando o ASVS e alterando o que é necessário para cada nível de risco de aplicação de uma maneira específica de domínio. Incentivamos esse tipo de bifurcação, desde que a rastreabilidade seja mantida, de modo que, se uma aplicação passou no requisito 4.1, isso significa o mesmo para cópias bifurcadas e para o padrão à medida que ele evolui.

### Como um guia para testes automatizados de unidade e integração

O ASVS foi projetado para ser altamente testável, com a única exceção dos requisitos de arquitetura e código malicioso. Ao criar testes de unidade e integração que testam casos de fuzz e abuso específicos e relevantes, a aplicação torna-se quase autoverificável a cada compilação. Por exemplo, testes adicionais podem ser criados para o conjunto de testes para um controlador de login, testando o parâmetro username para nomes de usuários padrão comuns, enumeração de contas, força bruta, injeção de LDAP e SQL e XSS. Da mesma forma, um teste no parâmetro de senha deve incluir senhas comuns, tamanho da senha, injeção de byte nulo, remoção do parâmetro, XSS e muito mais.

### Para treinamento de desenvolvimento seguro

ASVS também pode ser usado para definir características de software seguro. Muitos cursos de “codificação segura” são simplesmente cursos de hacking ético com uma leve mancha de dicas de codificação. Isso pode não necessariamente ajudar os desenvolvedores a escrever um código mais seguro. Em vez disso, os cursos de desenvolvimento seguro podem usar o ASVS com um forte foco nos controles proativos encontrados no ASVS, em vez das 10 principais coisas negativas a não fazer.

### Como um driver para segurança de aplicações ágeis

O ASVS pode ser usado em um processo de desenvolvimento ágil como um framework para definir tarefas específicas que precisam ser implementadas pela equipe para ter um produto seguro. Uma abordagem pode ser: Começando com o Nível 1, verifique a aplicação ou sistema específico de acordo com os requisitos ASVS para o nível especificado, encontre quais controles estão faltando e crie tickets/tarefas específicos no backlog. Isso ajuda na priorização de tarefas específicas (ou preparação) e torna a segurança visível no processo ágil. Isso também pode ser usado para priorizar tarefas de auditoria e revisão na organização, onde um requisito específico do ASVS pode ser um driver para revisão, refatoração ou auditoria para um membro específico da equipe e visível como "dívida" no backlog que precisa ser feito eventualmente .

### Como uma estrutura para orientar a aquisição de software seguro

O ASVS é uma ótima estrutura para ajudar na aquisição segura de software ou na aquisição de serviços de desenvolvimento personalizados. O comprador pode simplesmente definir um requisito de que o software que deseja adquirir deve ser desenvolvido no nível X da ASVS e solicitar que o vendedor comprove que o software atende ao nível X da ASVS. Isso funciona bem quando combinado com o Anexo do Contrato de Software Seguro OWASP.
