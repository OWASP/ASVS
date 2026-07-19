# Avaliação e Certificação

## A Postura da OWASP sobre Certificações e Selos de Confiança do ASVS

A OWASP, sendo uma organização sem fins lucrativos e neutra em relação a fornecedores, não certifica nenhum fornecedor, verificador ou software. Qualquer garantia, selo de confiança ou certificação que alegue conformidade com o ASVS não é oficialmente endossado pela OWASP, portanto, as organizações devem ser cautelosas com alegações de certificação do ASVS feitas por terceiros.

As organizações podem oferecer serviços de garantia (assurance services), desde que não aleguem certificação oficial da OWASP.

## Como Verificar a Conformidade com o ASVS

O ASVS deliberadamente não é prescritivo sobre exatamente como verificar a conformidade no nível de um guia de testes. No entanto, é importante destacar alguns pontos-chave.

### Relatório de Verificação

Os relatórios tradicionais de testes de intrusão (penetration testing) relatam problemas "por exceção", listando apenas as falhas. No entanto, um relatório de certificação do ASVS deve incluir o escopo, um resumo de todos os requisitos verificados, os requisitos onde foram observadas exceções e orientações sobre como resolver os problemas. Alguns requisitos podem não ser aplicáveis (por exemplo, gerenciamento de sessão em APIs sem estado/stateless), e isso deve ser observado no relatório.

### Escopo da Verificação

Uma organização que desenvolve uma aplicação geralmente não implementará todos os requisitos, pois alguns podem ser irrelevantes ou menos significativos com base na funcionalidade da aplicação. O verificador deve deixar o escopo da verificação claro, incluindo qual Nível a organização está tentando alcançar e quais requisitos foram incluídos. Isso deve ser feito sob a perspectiva do que foi incluído, em vez do que não foi incluído. Eles também devem fornecer uma opinião sobre a justificativa para a exclusão dos requisitos que não foram implementados.

Isso deve permitir que o consumidor de um relatório de verificação entenda o contexto da verificação e tome uma decisão informada sobre o nível de confiança que pode depositar na aplicação.

As organizações certificadoras podem escolher seus métodos de teste, mas devem divulgá-los no relatório, e idealmente, isso deve ser repetível. Diferentes métodos, como testes manuais de intrusão ou análise de código-fonte, podem ser usados para verificar aspectos como validação de entrada, dependendo da aplicação e dos requisitos.

### Mecanismos de Verificação

Existem diversas técnicas diferentes que podem ser necessárias para verificar requisitos específicos do ASVS. Além dos testes de intrusão (usando credenciais válidas para obter cobertura total da aplicação), a verificação dos requisitos do ASVS pode exigir acesso à documentação, ao código-fonte, às configurações e às pessoas envolvidas no processo de desenvolvimento. Especialmente para verificar os requisitos L2 e L3. É prática padrão fornecer evidências robustas das descobertas com documentação detalhada, que pode incluir documentos de trabalho, capturas de tela (screenshots), scripts e logs de testes. Apenas executar uma ferramenta automatizada sem testes minuciosos é insuficiente para a certificação, pois cada requisito deve ser comprovadamente testado.

O uso de automação para verificar requisitos do ASVS é um tópico de constante interesse. Portanto, é importante esclarecer alguns pontos relacionados a testes automatizados e testes de caixa preta (black box).

#### O Papel das Ferramentas de Teste de Segurança Automatizado

Quando ferramentas automatizadas de teste de segurança, como as ferramentas DAST (Dynamic Application Security Testing) e SAST (Static Application Security Testing), são implementadas corretamente no pipeline de construção (build), elas podem ser capazes de identificar alguns problemas de segurança que nunca deveriam existir. No entanto, sem configuração e ajuste cuidadosos, elas não fornecerão a cobertura exigida, e o nível de ruído impedirá que problemas reais de segurança sejam identificados e mitigados.

Embora isso possa fornecer cobertura para alguns dos requisitos técnicos mais básicos e diretos, como os relacionados à codificação ou sanitização de saída, é fundamental notar que essas ferramentas serão incapazes de verificar inteiramente muitos dos requisitos mais complicados do ASVS ou aqueles que se relacionam à lógica de negócios e ao controle de acesso.

Para requisitos menos diretos, é provável que a automação ainda possa ser utilizada, mas verificações específicas da aplicação precisarão ser escritas para alcançar isso. Estas podem ser semelhantes aos testes de unidade e de integração que a organização já pode estar usando. Portanto, pode ser possível usar essa infraestrutura de automação de testes existente para escrever esses testes específicos do ASVS. Embora fazer isso exija investimento de curto prazo, os benefícios de longo prazo de ser capaz de verificar continuamente esses requisitos do ASVS serão significativos.

Em resumo, testável usando automação != executar uma ferramenta pronta para uso (off the shelf).

#### O Papel do Teste de Intrusão

Enquanto o L1 na versão 4.0 foi otimizado para a ocorrência de testes "caixa preta" (sem documentação e sem código-fonte), mesmo na época o padrão era claro de que esta não é uma atividade de garantia eficaz e deve ser ativamente desencorajada.

Testar sem acesso a informações adicionais necessárias é um mecanismo ineficiente e ineficaz para verificação de segurança, pois perde a possibilidade de revisar o código-fonte, identificar ameaças e controles ausentes, e realizar um teste muito mais completo em um prazo mais curto.

É fortemente encorajado realizar testes de intrusão guiados por documentação ou código-fonte (híbridos), que tenham acesso total aos desenvolvedores da aplicação e à documentação da aplicação, em vez de testes de intrusão tradicionais. Isso certamente será necessário para verificar muitos dos requisitos do ASVS.