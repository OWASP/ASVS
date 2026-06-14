# Apêndice D: Recomendações

## Introdução

Durante a preparação da versão 5.0 do Application Security Verification Standard (ASVS), ficou claro que havia uma série de itens existentes e novos sugeridos que não deveriam ser incluídos como requisitos na versão 5.0. Isso pode ter ocorrido porque eles não estavam no escopo do ASVS de acordo com a definição da versão 5.0 ou, alternativamente, porque embora se sentisse que eram uma boa ideia, não poderiam ser tornados obrigatórios.

Não querendo perder todos esses itens inteiramente, alguns foram capturados neste apêndice.

## Mecanismos recomendados, dentro do escopo

Os itens a seguir estão no escopo do ASVS. Eles não devem ser tornados obrigatórios, mas é altamente recomendável considerá-los como parte de uma aplicação segura.

* Um medidor de força de senha (password strength meter) deve ser fornecido para ajudar os usuários a definir uma senha mais forte.
* Crie um arquivo security.txt publicamente disponível na raiz ou diretório .well-known da aplicação que defina claramente um link ou endereço de e-mail para as pessoas entrarem em contato com os proprietários sobre problemas de segurança.
* A validação de entrada no lado do cliente (client-side) deve ser aplicada, além da validação em uma camada de serviço confiável, pois isso fornece uma boa oportunidade para descobrir quando alguém burlou os controles no lado do cliente na tentativa de atacar a aplicação.
* Evite que páginas acidentalmente acessíveis e sensíveis apareçam nos mecanismos de busca usando um arquivo robots.txt, o cabeçalho de resposta X-Robots-Tag ou uma meta tag html robots.
* Ao usar GraphQL, implemente a lógica de autorização na camada de lógica de negócios (business logic layer) em vez da camada do GraphQL ou do resolver para evitar a necessidade de tratar a autorização em cada interface separada.

Referências:

* [More information on security.txt including a link to the RFC](https://securitytxt.org/)

## Princípios de Segurança de Software

Os itens a seguir estavam anteriormente no ASVS, mas na verdade não são requisitos. Em vez disso, são princípios a serem considerados ao implementar controles de segurança que, quando seguidos, levarão a controles mais robustos. Eles incluem:

* Os controles de segurança devem ser centralizados, simples (economia de design), sabidamente seguros e reutilizáveis. Isso deve evitar controles duplicados, ausentes ou ineficazes.
* Sempre que possível, use implementações de controle de segurança previamente escritas e bem examinadas (well-vetted), em vez de depender da implementação de controles a partir do zero.
* Idealmente, um único mecanismo de controle de acesso deve ser usado para acessar dados e recursos protegidos. Todas as requisições devem passar por esse único mecanismo para evitar caminhos alternativos do tipo copiar e colar ou inseguros.
* O controle de acesso baseado em atributos ou recursos (feature-based) é um padrão recomendado pelo qual o código verifica a autorização do usuário para um recurso ou item de dados, em vez de apenas sua função (role). As permissões ainda devem ser alocadas usando as roles.

## Processos de Segurança de Software

Existem vários processos de segurança que foram removidos do ASVS 5.0, mas ainda são uma boa ideia. O projeto OWASP SAMM pode ser uma boa fonte sobre como implementar efetivamente esses processos. Os itens que estavam anteriormente no ASVS incluem:

* Verifique o uso de um ciclo de vida de desenvolvimento de software seguro que aborde a segurança em todas as etapas do desenvolvimento.
* Verifique o uso de modelagem de ameaças (threat modeling) para cada mudança de design ou planejamento de sprint para identificar ameaças, planejar contramedidas, facilitar respostas apropriadas a riscos e guiar testes de segurança.
* Verifique se todas as histórias de usuários (user stories) e funcionalidades (features) contêm restrições funcionais de segurança, como "Como usuário, eu devo ser capaz de visualizar e editar meu perfil. Eu não devo ser capaz de visualizar ou editar o perfil de mais ninguém."
* Verifique a disponibilidade de uma lista de verificação de codificação segura, requisitos de segurança, diretrizes ou políticas para todos os desenvolvedores e testadores.
* Verifique se existe um processo contínuo para garantir que o código-fonte da aplicação esteja livre de backdoors, código malicioso (por exemplo, ataques salami, bombas lógicas, bombas-relógio) e recursos não documentados ou ocultos (por exemplo, Easter eggs, ferramentas de depuração inseguras). Estar em conformidade com esta seção não é possível sem acesso total ao código-fonte, incluindo bibliotecas de terceiros, e portanto, provavelmente é adequado apenas para aplicações que exigem os mais altos níveis de segurança.
* Verifique se existem mecanismos para detectar e responder ao desvio de configuração (configuration drift) em ambientes implantados. Isso pode incluir o uso de infraestrutura imutável (immutable infrastructure), reimplantação automatizada a partir de uma base segura (secure baseline) ou ferramentas de detecção de desvio que comparam o estado atual em relação a configurações aprovadas.
* Verifique se o fortalecimento de configurações (configuration hardening) é executado em todos os produtos de terceiros, bibliotecas, frameworks e serviços conforme suas recomendações individuais.

Referências:

* [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
* [OWASP Threat modeling](https://owasp.org/www-community/Application_Threat_Modeling)
* [OWASP Software Assurance Maturity Model Project](https://owasp.org/www-project-samm/)
* [Microsoft SDL](https://www.microsoft.com/en-us/securityengineering/sdl/)