# V14 Configuração

## Objetivo de controle

Certifique-se de que uma aplicação verificado tenha:

* Um ambiente de construção seguro, repetível e automatizável.
* Biblioteca reforçada de terceiros, dependência e gestão de configuração de forma que componentes desatualizados ou inseguros não sejam incluídos pela aplicação.

A configuração da aplicação pronta para uso deve ser segura para estar na Internet, significando uma configuração segura pronta para uso.

## V14.1 Construir e Implantar

Os pipelines de compilação são a base para a segurança repetível — toda vez que algo inseguro é descoberto, ele pode ser resolvido no código-fonte, scripts de compilação ou implantação e testado automaticamente. Incentivamos fortemente o uso de pipelines de compilação com segurança automática e verificações de dependência que avisam ou interrompem a compilação para evitar que problemas de segurança conhecidos sejam implantados na produção. Etapas manuais executadas de forma irregular levam diretamente a erros de segurança evitáveis.

À medida que o setor se move para um modelo DevSecOps, é importante garantir a disponibilidade e a integridade contínuas da implantação e da configuração para atingir um estado "conhecido como bom". No passado, se um sistema fosse hackeado, levaria de dias a meses para provar que nenhuma outra intrusão havia ocorrido. Hoje, com o advento da infraestrutura definida por software, implantações rápidas de A/B com tempo de inatividade zero e compilações automatizadas em contêineres, é possível criar, fortalecer e implantar de forma automática e contínua uma substituição "boa" para qualquer sistema comprometido.

Se os modelos tradicionais ainda estiverem em vigor, devem ser tomadas medidas manuais para fortalecer e fazer backup dessa configuração para permitir que os sistemas comprometidos sejam rapidamente substituídos por sistemas não comprometidos de alta integridade em tempo hábil.

A conformidade com esta seção requer um sistema de compilação automatizado e acesso a scripts de compilação e implantação.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.1.1** | Verifique se os processos de criação e implantação da aplicação são executados de maneira segura e repetível, como automação de CI/CD, gestão de configuração automatizada e scripts de implantação automatizada. | | ✓ | ✓ | |
| **14.1.2** | Verifique se os sinalizadores do compilador estão configurados para habilitar todas as proteções e avisos de buffer overflow disponíveis, incluindo randomização de pilha, prevenção de execução de dados e para interromper a compilação se um ponteiro inseguro, memória, string de formato, número inteiro ou operações de string forem encontrados. | | ✓ | ✓ | 120 |
| **14.1.3** | Verifique se a configuração do servidor está protegida de acordo com as recomendações do servidor de aplicações e estruturas em uso. | | ✓ | ✓ | 16 |
| **14.1.4** | Verifique se a aplicação, a configuração e todas as dependências podem ser reimplantados usando scripts de implantação automatizados, criados a partir de um runbook documentado e testado num tempo razoável ou restaurados de backups em tempo hábil. | | ✓ | ✓ | |
| **14.1.5** | Verifique se os administradores autorizados podem verificar a integridade de todas as configurações relevantes para a segurança para detectar adulterações. | | | ✓ | |

## V14.2 Dependência

O gestão de dependência é crítico para a operação segura de qualquer aplicação de qualquer tipo. A falha em manter-se atualizado com dependências desatualizadas ou inseguras é a causa raiz dos maiores e mais caros ataques até hoje.

Nota: No Nível 1, a conformidade com 14.2.1 refere-se a observações ou detecções do lado do cliente e outras bibliotecas e componentes, em vez da análise de código estático ou análise de dependência mais precisa em tempo de compilação. Essas técnicas mais precisas podem ser descobertas por entrevistas, conforme necessário.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.2.1** | Verifique se todos os componentes estão atualizados, de preferência usando um verificador de dependência durante o tempo de construção ou compilação. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 1026 |
| **14.2.2** | Verifique se todos os recursos, documentação, aplicações de amostra e configurações desnecessários foram removidos. | ✓ | ✓ | ✓ | 1002 |
| **14.2.3** | Verifique se os ativos da aplicação, como bibliotecas JavaScript, CSS ou fontes da Web, são hospedados externamente numa rede de entrega de conteúdo (CDN) ou provedor externo, a integridade do subrecurso (SRI) é usada para validar a integridade do ativo. | ✓ | ✓ | ✓ | 829 |
| **14.2.4** | Verifique se os componentes de terceiros vêm de repositórios predefinidos, confiáveis e mantidos continuamente. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 829 |
| **14.2.5** | Verifique se uma lista de materiais de software (SBOM) é mantida para todas as bibliotecas de terceiros em uso. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | |
| **14.2.6** | Verifique se a superfície de ataque é reduzida por sandbox ou encapsulamento de bibliotecas de terceiros para expor apenas o comportamento necessário na aplicação. ([C2](https://owasp.org/www-project-proactive-controls/#div-numbering)) | | ✓ | ✓ | 265 |

## V14.3 Divulgação de segurança não intencional

As configurações para produção devem ser fortalecidas para proteger contra-ataques comuns, como consoles de depuração, aumentar o nível de ataques Cross-site Scripting (XSS) e Remote File Inclusion (RFI) e eliminar "vulnerabilidades" triviais de descoberta de informações que são as indesejadas marcas registradas de muitos relatórios de teste de penetração. Muitos desses problemas são raramente classificados como um risco significativo, mas estão encadeados com outras vulnerabilidades. Se esses problemas não estiverem presentes por padrão, ele eleva a fasquia antes que a maioria dos ataques seja bem-sucedida.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.3.1** | [EXCLUÍDO, DUPLICADO DE 7.4.1] | | | | |
| **14.3.2** | Verifique se os modos de depuração da estrutura da aplicação ou servidor da Web estão desativados na produção para eliminar recursos de depuração, consoles de desenvolvedor e divulgações de segurança não intencionais. | ✓ | ✓ | ✓ | 497 |
| **14.3.3** | Verifique se os cabeçalhos HTTP ou qualquer parte da resposta HTTP não expõe informações detalhadas sobre a versão dos componentes do sistema. | ✓ | ✓ | ✓ | 200 |

## V14.4 Cabeçalhos de segurança HTTP

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.4.1** | Verifique se cada resposta HTTP contém um cabeçalho Content-Type. Especifique também um conjunto de caracteres seguro (por exemplo, UTF-8, ISO-8859-1) se os tipos de conteúdo forem text/*, /+xml e application/xml. O conteúdo deve corresponder ao cabeçalho Content-Type fornecido. | ✓ | ✓ | ✓ | 173 |
| **14.4.2** | Verifique se todas as respostas da API contêm um anexo Content-Disposition:; cabeçalho filename="api.json" (ou outro nome de arquivo apropriado para o tipo de conteúdo). | ✓ | ✓ | ✓ | 116 |
| **14.4.3** | Verifique se um cabeçalho de resposta da política de segurança de conteúdo (CSP) está em vigor para ajudar a atenuar o impacto de ataques XSS, como HTML, DOM, JSON e vulnerabilidades de injeção de JavaScript. | ✓ | ✓ | ✓ | 1021 |
| **14.4.4** | Verifique se todas as respostas contêm um cabeçalho X-Content-Type-Options: nosniff. | ✓ | ✓ | ✓ | 116 |
| **14.4.5** | Verifique se um cabeçalho Strict-Transport-Security está incluído em todas as respostas e para todos os subdomínios, como Strict-Transport-Security: max-age=15724800; includeSubdomains. | ✓ | ✓ | ✓ | 523 |
| **14.4.6** | Verifique se um cabeçalho Referrer-Policy adequado está incluído para evitar a exposição de informações confidenciais na URL por meio do cabeçalho Referer para partes não confiáveis. | ✓ | ✓ | ✓ | 116 |
| **14.4.7** | Verifique se o conteúdo de uma aplicação da Web não pode ser incorporado num site de terceiros por padrão e se a incorporação dos recursos exatos só é permitida quando necessária usando a política de segurança de conteúdo adequada: resposta de ancestrais de quadro e opções de X-Frame cabeçalhos. | ✓ | ✓ | ✓ | 1021 |

## V14.5 Validação de cabeçalho de solicitação HTTP

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **14.5.1** | Verifique se o servidor de aplicações aceita apenas os métodos HTTP em uso pela aplicação/API, incluindo OPÇÕES pré-voo e logs/alertas em quaisquer solicitações que não sejam válidas para o contexto da aplicação. | ✓ | ✓ | ✓ | 749 |
| **14.5.2** | Verifique se o cabeçalho Origin fornecido não é usado para autenticação ou decisões de controle de acesso, pois o cabeçalho Origin pode ser facilmente alterado por um invasor. | ✓ | ✓ | ✓ | 346 |
| **14.5.3** | Verifique se o cabeçalho Access-Control-Allow-Origin de compartilhamento de recursos de origem cruzada (CORS) usa uma lista de permissão estrita de domínios e subdomínios confiáveis para correspondência e não oferece suporte à origem "nula". | ✓ | ✓ | ✓ | 346 |
| **14.5.4** | Verifique se os cabeçalhos HTTP adicionados por um proxy confiável ou dispositivos SSO, como um token de portador, são autenticados pela aplicação. | | ✓ | ✓ | 306 |

## Referências

Para mais informações, consulte também:

* [OWASP Web Security Testing Guide 4.1: Testing for HTTP Verb Tampering]( https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering.html)
* Adicionar disposição de conteúdo às respostas da API ajuda a evitar muitos ataques baseados em mal-entendidos no tipo MIME entre cliente e servidor, e a opção "nome do arquivo" especificamente ajuda a evitar [Reflected File Download attacks.](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hafif-Reflected-File-Download-A-New-Web-Attack-Vector.pdf)
* [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [Exploiting CORS misconfiguration for BitCoins and Bounties](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OWASP Web Security Testing Guide 4.1: Configuration and Deployment Management Testing](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README.html)
* [Sandboxing third party components](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html#sandboxing-content)
