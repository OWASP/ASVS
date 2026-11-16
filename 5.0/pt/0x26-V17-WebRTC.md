# V17 WebRTC

## Objetivo de Controle

A Comunicação em Tempo Real pela Web (Web Real-Time Communication - WebRTC) possibilita a troca de voz, vídeo e dados em tempo real em aplicações modernas. À medida que a adoção aumenta, a proteção da infraestrutura WebRTC torna-se crítica. Esta seção fornece os requisitos de segurança para as partes interessadas (stakeholders) que desenvolvem, hospedam ou integram os sistemas WebRTC.

O mercado de WebRTC pode ser categorizado em geral em três segmentos:

1. Desenvolvedores de Produtos (Product Developers): Fornecedores proprietários ou de código aberto que criam e fornecem soluções e produtos WebRTC. O foco principal é o desenvolvimento de tecnologias WebRTC robustas e seguras que possam ser utilizadas por outras partes.

2. Plataformas de Comunicação como Serviço (CPaaS): Provedores que oferecem APIs, SDKs e a infraestrutura ou as plataformas necessárias para viabilizar funcionalidades WebRTC. Os provedores de CPaaS podem usar produtos da primeira categoria ou desenvolver seu próprio software WebRTC para oferecer esses serviços.

3. Provedores de Serviço (Service Providers): Organizações que aproveitam produtos de desenvolvedores de produtos ou de provedores de CPaaS, ou que desenvolvem suas próprias soluções WebRTC. Elas criam e implementam aplicações para conferências online, saúde, e-learning e outras áreas em que a comunicação em tempo real é fundamental.

Os requisitos de segurança descritos aqui são voltados principalmente a Desenvolvedores de Produtos, CPaaS e Provedores de Serviço que:

* Utilizam soluções de código aberto (open-source) para construir suas aplicações WebRTC.
* Usam produtos comerciais de WebRTC como parte de sua infraestrutura.
* Usam soluções WebRTC desenvolvidas internamente ou integram diversos componentes em uma oferta de serviço coesa.

É importante observar que esses requisitos de segurança não se aplicam a desenvolvedores que usam exclusivamente SDKs e APIs fornecidos por fornecedores de CPaaS. Para esses desenvolvedores, os provedores de CPaaS são tipicamente responsáveis pela maior parte das preocupações de segurança subjacentes em suas plataformas, e um padrão de segurança genérico como o ASVS pode não atender totalmente às suas necessidades.

## V17.1 Servidor TURN

Esta seção define os requisitos de segurança para sistemas que operam seus próprios servidores TURN (Traversal Using Relays around NAT). Os servidores TURN auxiliam na retransmissão de mídia em ambientes de rede restritivos, mas podem representar riscos se configurados incorretamente. Esses controles se concentram na filtragem segura de endereços e na proteção contra o esgotamento de recursos.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **17.1.1** | Verifique se o serviço Traversal Using Relays around NAT (TURN) permite acesso apenas aos endereços IP que não são reservados a propósitos especiais (por exemplo, redes internas, broadcast, loopback). Note que isso se aplica tanto aos endereços IPv4 quanto aos IPv6. | 2 |
| **17.1.2** | Verifique se o serviço Traversal Using Relays around NAT (TURN) não é suscetível ao esgotamento de recursos quando usuários legítimos tentam abrir um grande número de portas no servidor TURN. | 3 |

## V17.2 Mídia

Esses requisitos se aplicam apenas aos sistemas que hospedam seus próprios servidores de mídia WebRTC, como Unidades de Encaminhamento Seletivo (Selective Forwarding Units - SFUs), Unidades de Controle Multiponto (Multipoint Control Units - MCUs), servidores de gravação ou servidores de gateway. Os servidores de mídia manipulam e distribuem os streams de mídia, tornando a segurança desses componentes crítica para a proteção da comunicação entre os pares. A salvaguarda dos streams de mídia é fundamental nas aplicações WebRTC para evitar espionagem (eavesdropping), adulteração e ataques de negação de serviço (denial-of-service) que podem comprometer a privacidade do usuário e a qualidade da comunicação.

Em especial, é necessário implementar proteções contra ataques de inundação (flood attacks), tais como limitação de taxa (rate limiting), validação de registros de tempo (timestamps), uso de relógios sincronizados para equiparar intervalos em tempo real e o gerenciamento de buffers para evitar overflow (transbordamento) e manter a sincronia adequada. Se os pacotes de uma sessão de mídia específica chegarem muito rapidamente, os pacotes em excesso deverão ser descartados. Também é importante proteger o sistema de pacotes malformados implementando a validação de entrada, tratando falhas de integer overflow (estouro de número inteiro) de forma segura, impedindo ataques de buffer overflow e empregando outras técnicas robustas de tratamento de erros.

Sistemas que dependem puramente da comunicação de mídia peer-to-peer (ponto a ponto) entre navegadores web, sem o envolvimento ou mediação através de servidores de mídia intermediários, estão excluídos desses requisitos de segurança específicos de mídia.

Esta seção refere-se ao uso de Datagram Transport Layer Security (DTLS) no contexto do WebRTC. Um requisito relacionado a possuir uma política documentada para o gerenciamento de chaves criptográficas pode ser encontrado no capítulo "Criptografia". Informações sobre métodos criptográficos aprovados podem ser encontradas no Apêndice de Criptografia do ASVS ou em documentos como o NIST SP 800‑52 Rev. 2 ou BSI TR‑02102‑2 (Versão 2025‑01).

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **17.2.1** | Verifique se a chave para o certificado Datagram Transport Layer Security (DTLS) é gerenciada e protegida com base na política documentada para o gerenciamento de chaves criptográficas. | 2 |
| **17.2.2** | Verifique se o servidor de mídia está configurado para usar e suportar cipher suites aprovadas do Datagram Transport Layer Security (DTLS) e um perfil de proteção seguro para a Extensão DTLS de estabelecimento de chaves do Secure Real-time Transport Protocol (DTLS-SRTP). | 2 |
| **17.2.3** | Verifique se a autenticação do Secure Real-time Transport Protocol (SRTP) é verificada no servidor de mídia, para evitar que ataques de injeção de Real-time Transport Protocol (RTP) levem a uma condição de negação de serviço ou à inserção de mídia de áudio ou vídeo nos fluxos de mídia (media streams). | 2 |
| **17.2.4** | Verifique se o servidor de mídia consegue continuar processando o tráfego de mídia recebido ao encontrar pacotes Secure Real-time Transport Protocol (SRTP) malformados. | 2 |
| **17.2.5** | Verifique se o servidor de mídia consegue continuar processando o tráfego de mídia recebido durante uma inundação (flood) de pacotes Secure Real-time Transport Protocol (SRTP) de usuários legítimos. | 3 |
| **17.2.6** | Verifique se o servidor de mídia não é suscetível à vulnerabilidade de condição de corrida (race condition) "ClientHello" no Datagram Transport Layer Security (DTLS), verificando se o servidor de mídia é publicamente conhecido como vulnerável ou realizando o teste de condição de corrida. | 3 |
| **17.2.7** | Verifique se quaisquer mecanismos de gravação de áudio ou vídeo associados ao servidor de mídia conseguem continuar processando o tráfego de mídia recebido durante uma inundação (flood) de pacotes Secure Real-time Transport Protocol (SRTP) de usuários legítimos. | 3 |
| **17.2.8** | Verifique se o certificado do Datagram Transport Layer Security (DTLS) é verificado em relação ao atributo de impressão digital (fingerprint) do Session Description Protocol (SDP), encerrando o fluxo de mídia se a verificação falhar, a fim de garantir a autenticidade do fluxo de mídia. | 3 |

## V17.3 Sinalização

Esta seção define os requisitos para sistemas que operam seus próprios servidores de sinalização WebRTC. A sinalização coordena a comunicação ponto a ponto (peer-to-peer) e deve ser resiliente contra ataques que podem interromper o estabelecimento ou o controle da sessão.

Para garantir uma sinalização segura, os sistemas devem tratar entradas malformadas de forma controlada (gracefully) e permanecer disponíveis sob carga.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **17.3.1** | Verifique se o servidor de sinalização consegue continuar o processamento de mensagens de sinalização de entrada legítimas durante um ataque de inundação (flood attack). Isso deve ser alcançado implementando a limitação de taxa (rate limiting) no nível de sinalização. | 2 |
| **17.3.2** | Verifique se o servidor de sinalização consegue continuar o processamento de mensagens de sinalização legítimas ao encontrar uma mensagem de sinalização malformada que poderia causar uma condição de negação de serviço. Isso poderia incluir a implementação da validação da entrada (input validation), do tratamento seguro contra estouros de número inteiro (integer overflows), prevenindo estouros de buffer (buffer overflows) e o uso de outras técnicas robustas de tratamento de erros. | 2 |

## Referências

Para mais informações, veja também:

* O DoS de ClientHello do DTLS no WebRTC está mais bem documentado no [post do blog da Enable Security voltado a profissionais de segurança](https://www.enablesecurity.com/blog/novel-dos-vulnerability-affecting-webrtc-media-servers/) e no [white paper associado voltado a desenvolvedores WebRTC](https://www.enablesecurity.com/blog/webrtc-hello-race-conditions-paper/)
* [RFC 3550 - RTP: A Transport Protocol for Real-Time Applications](https://www.rfc-editor.org/rfc/rfc3550)
* [RFC 3711 - The Secure Real-time Transport Protocol (SRTP)](https://datatracker.ietf.org/doc/html/rfc3711)
* [RFC 5764 - Datagram Transport Layer Security (DTLS) Extension to Establish Keys for the Secure Real-time Transport Protocol (SRTP))](https://datatracker.ietf.org/doc/html/rfc5764)
* [RFC 8825 - Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/info/rfc8825)
* [RFC 8826 - Security Considerations for WebRTC](https://www.rfc-editor.org/info/rfc8826)
* [RFC 8827 - WebRTC Security Architecture](https://www.rfc-editor.org/info/rfc8827)
* [DTLS-SRTP Protection Profiles](https://www.iana.org/assignments/srtp-protection/srtp-protection.xhtml)