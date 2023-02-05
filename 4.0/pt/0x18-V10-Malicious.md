# V10 Código malicioso

## Objetivo de controle

Certifique-se de que o código satisfaça os seguintes requisitos de alto nível:

* A atividade maliciosa é tratada de forma segura e adequada para não afetar o restante da aplicação.
* Não possui bombas-relógio ou outros ataques baseados no tempo.
* Não "telefone para casa" para destinos maliciosos ou não autorizados.
* Não possui portas traseiras, ovos de Páscoa, ataques de salame, rootkits ou código não autorizado que possa ser controlado por um invasor.

Encontrar um código malicioso é a prova da negativa, impossível de validar completamente. Devem ser envidados os melhores esforços para garantir que o código não tenha código malicioso inerente ou funcionalidade indesejada.

## V10.1 Integridade do código

A melhor defesa contra códigos maliciosos é "confiar, mas verificar". A introdução de código não autorizado ou malicioso no código costuma ser uma ofensa criminal em muitas jurisdições. Políticas e procedimentos devem tornar claras as sanções relativas a códigos maliciosos.

Os principais desenvolvedores devem revisar regularmente os check-ins de código, especialmente aqueles que podem acessar funções de tempo, E/S ou rede.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.1.1** | Verifique se uma ferramenta de análise de código está em uso e pode detectar códigos potencialmente maliciosos, como funções de tempo, operações de arquivo inseguras e conexões de rede. | | | ✓ | 749 |

## V10.2 Pesquisa de código malicioso

O código malicioso é extremamente raro e difícil de detectar. A revisão manual do código linha por linha pode ajudar a procurar por bombas lógicas, mas mesmo o revisor de código mais experiente terá dificuldade em encontrar código malicioso, mesmo que saiba que ele existe.

A conformidade com esta seção não é possível sem acesso completo ao código-fonte, incluindo bibliotecas de terceiros.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.2.1** | Verifique se o código-fonte da aplicação e as bibliotecas de terceiros não contêm recursos não autorizados de telefone residencial ou coleta de dados. Onde tal funcionalidade existir, obtenha a permissão do usuário para que ela opere antes de coletar quaisquer dados. | | ✓ | ✓ | 359 |
| **10.2.2** | Verifique se a aplicação não solicita permissões desnecessárias ou excessivas para recursos ou sensores relacionados à privacidade, como contatos, câmeras, microfones ou localização. | | ✓ | ✓ | 272 |
| **10.2.3** | Verifique se o código-fonte da aplicação e as bibliotecas de terceiros não contêm backdoors, como contas ou chaves codificadas ou adicionais não documentadas, ofuscação de código, blobs binários não documentados, rootkits ou antidepuração, recursos de depuração inseguros ou de outra forma fora de data, funcionalidade insegura ou oculta que pode ser usada maliciosamente se descoberta. | | | ✓ | 507 |
| **10.2.4** | Verifique se o código-fonte da aplicação e as bibliotecas de terceiros não contêm bombas-relógio procurando por funções relacionadas a data e hora. | | | ✓ | 511 |
| **10.2.5** | Verifique se o código-fonte da aplicação e as bibliotecas de terceiros não contêm código mal-intencionado, como ataques de salame, desvios lógicos ou bombas lógicas. | | | ✓ | 511 |
| **10.2.6** | Verifique se o código-fonte da aplicação e as bibliotecas de terceiros não contêm ovos de Páscoa ou qualquer outra funcionalidade potencialmente indesejada. | | | ✓ | 507 |

## V10.3 Integridade da aplicação

Depois que uma aplicação é implantado, o código malicioso ainda pode ser inserido. as aplicações precisam se proteger contra-ataques comuns, como a execução de código não assinado de fontes não confiáveis e invasões de subdomínio.

O cumprimento desta seção provavelmente será operacional e contínuo.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **10.3.1** | Verifique se a aplicação possui um recurso de atualização automática de cliente ou servidor, as atualizações devem ser obtidas por canais seguros e assinadas digitalmente. O código de atualização deve validar a assinatura digital da atualização antes de instalar ou executar a atualização. | ✓ | ✓ | ✓ | 16 |
| **10.3.2** | Verifique se a aplicação emprega proteções de integridade, como assinatura de código ou integridade de sub-recurso. A aplicação não deve carregar ou executar código de fontes não confiáveis, como carregamento de inclusões, módulos, plug-ins, códigos ou bibliotecas de fontes não confiáveis ou da Internet. | ✓ | ✓ | ✓ | 353 |
| **10.3.3** | Verifique se a aplicação tem proteção contra invasões de subdomínio se a aplicação depender de inputs DNS ou subdomínios DNS, como nomes de domínio expirados, ponteiros DNS ou CNAMEs desatualizados, projetos expirados em repositórios públicos de código-fonte ou APIs de nuvem temporárias, funções serverless, ou depósitos de armazenamento (*autogen-bucket-id*.cloud.example.com) ou similar. As proteções podem incluir a garantia de que os nomes DNS usados pelas aplicações sejam verificados regularmente quanto à expiração ou alteração. | ✓ | ✓ | ✓ | 350 |

## Referências

Para mais informações, consulte também:

* [Hostile Subdomain Takeover, Detectify Labs](https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/)
* [Hijacking of abandoned subdomains part 2, Detectify Labs](https://labs.detectify.com/2014/12/08/hijacking-of-abandoned-subdomains-part-2/)
