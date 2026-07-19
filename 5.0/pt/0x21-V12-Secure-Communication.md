# V12 Comunicação Segura

## Objetivo de Controle

Este capítulo inclui requisitos relacionados aos mecanismos específicos que devem estar em vigor para proteger dados em trânsito, tanto entre um cliente (usuário final) e um serviço backend, quanto entre serviços internos e os de backend.

Os conceitos gerais promovidos por este capítulo incluem:

* Garantir que as comunicações sejam criptografadas externamente e, idealmente, internamente também.
* Configurar mecanismos de criptografia utilizando as diretrizes mais recentes, incluindo os algoritmos e cifras preferidos.
* Assegurar que as comunicações não sejam interceptadas por partes não autorizadas através do uso de certificados assinados.

Além de delinear princípios gerais e melhores práticas, o ASVS também fornece informações técnicas aprofundadas sobre a força criptográfica no Apêndice C - Padrões de Criptografia.

## V12.1 Orientação Geral de Segurança TLS

Esta seção fornece orientações iniciais sobre como proteger as comunicações TLS. Ferramentas atualizadas devem ser utilizadas para revisar a configuração TLS de maneira contínua.

Embora o uso de certificados curinga (wildcard certificates) para o TLS não seja inerentemente inseguro, o comprometimento de um certificado que é implantado em todos os ambientes proprietários (ex., produção, homologação, desenvolvimento e testes) pode levar ao comprometimento da postura de segurança das aplicações que o utilizam. A proteção adequada, o gerenciamento e o uso de certificados TLS distintos em diferentes ambientes devem ser empregados, sempre que possível.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **12.1.1** | Verifique se apenas as versões mais recentes recomendadas do protocolo TLS estão habilitadas, como TLS 1.2 e TLS 1.3. A versão mais recente do protocolo TLS deve ser a opção preferida. | 1 |
| **12.1.2** | Verifique se apenas as suites de criptografia recomendadas estão habilitadas, com as suites mais fortes definidas como preferidas. As aplicações L3 devem suportar exclusivamente cipher suites (suites de cifras) que forneçam forward secrecy (sigilo de encaminhamento perfeito). | 2 |
| **12.1.3** | Verifique se a aplicação valida se os certificados de cliente mTLS são confiáveis antes de usar a identidade do certificado para autenticação ou autorização. | 2 |
| **12.1.4** | Verifique se a revogação adequada de certificado, como o Online Certificate Status Protocol (OCSP) Stapling, está habilitada e configurada. | 3 |
| **12.1.5** | Verifique se o Encrypted Client Hello (ECH) está habilitado nas configurações TLS da aplicação para evitar a exposição de metadados sensíveis, como o Server Name Indication (SNI), durante os processos de handshake TLS. | 3 |

## V12.2 Comunicação HTTPS com Serviços Voltados Para a Internet (External Facing Services)

Garanta que todo o tráfego HTTP para serviços voltados externamente expostos pela aplicação seja enviado com criptografia, utilizando certificados confiáveis publicamente.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **12.2.1** | Verifique se o TLS é usado em todas as conectividades entre um cliente e serviços HTTP voltados externamente, e não faz retrocesso (fallback) para comunicações inseguras ou não criptografadas. | 1 |
| **12.2.2** | Verifique se os serviços voltados externamente utilizam certificados TLS que são publicamente confiáveis. | 1 |

## V12.3 Segurança da Comunicação Geral Serviço-a-Serviço

As comunicações dos servidores (tanto as internas quanto as externas) envolvem muito mais do que apenas HTTP. As conexões de e para outros sistemas também devem ser seguras, utilizando idealmente o TLS.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **12.3.1** | Verifique se um protocolo criptografado como o TLS é usado para todas as conexões de entrada e de saída da aplicação, incluindo os sistemas de monitoramento, ferramentas de gerenciamento, acesso remoto e SSH, middleware, bancos de dados, mainframes, sistemas de parceiros ou APIs externas. O servidor não deve retornar a protocolos inseguros ou não criptografados. | 2 |
| **12.3.2** | Verifique se os clientes TLS validam os certificados recebidos antes de se comunicarem com um servidor TLS. | 2 |
| **12.3.3** | Verifique se o TLS ou outro mecanismo adequado de criptografia de transporte é utilizado em todas as conectividades entre os serviços internos baseados em HTTP na aplicação, e não faz retrocesso (fallback) para comunicações inseguras ou não criptografadas. | 2 |
| **12.3.4** | Verifique se as conexões TLS entre os serviços internos utilizam certificados confiáveis. Onde certificados autoassinados (self-signed) ou gerados internamente forem utilizados, o serviço consumidor deve ser configurado para confiar apenas em CAs internas específicas e em certificados autoassinados específicos. | 2 |
| **12.3.5** | Verifique se os serviços que se comunicam internamente em um sistema (comunicações intra-serviço) usam autenticação forte para garantir a verificação de cada endpoint. Métodos de autenticação fortes, como a autenticação de cliente TLS, devem ser empregados para assegurar a identidade, usando infraestrutura de chave pública e mecanismos que são resistentes a ataques de repetição (replay attacks). Para as arquiteturas de microserviços, considere o uso de uma malha de serviços (service mesh) para simplificar o gerenciamento de certificados e aprimorar a segurança. | 3 |

## Referências

Para mais informações, veja também:

* [OWASP - Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
* [Mozilla's Server Side TLS configuration guide](https://wiki.mozilla.org/Security/Server_Side_TLS)
* [Mozilla's tool to generate known good TLS configurations](https://ssl-config.mozilla.org/).
* [O-Saft - OWASP Project to validate TLS configuration](https://owasp.org/www-project-o-saft/)
