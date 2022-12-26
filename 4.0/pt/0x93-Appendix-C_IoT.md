# Apêndice C: Requisitos de verificação da Internet of Things

Este capítulo estava originalmente no ramo principal, mas com o trabalho que a equipe OWASP IoT tem feito, não faz sentido manter dois tópicos diferentes sobre o assunto. Para a versão 4.0, estamos movendo isso para o Apêndice e instamos todos que precisam disso a usar o [projeto OWASP IoT] principal (https://owasp.org/www-project-internet-of-things/)

## Objetivo de controle

Os dispositivos integrados/IoT devem:

* Tenha o mesmo nível de controles de segurança no dispositivo encontrado no servidor, aplicando controles de segurança em um ambiente confiável.
* Os dados confidenciais armazenados no dispositivo devem ser feitos de maneira segura, usando armazenamento com suporte de hardware, como elementos seguros.
* Todos os dados confidenciais transmitidos do dispositivo devem utilizar a segurança da camada de transporte.

## Requisitos de verificação de segurança

| # | Descrição | L1 | L2 | L3 | Desde |
| --- | --- | --- | --- | -- | -- |
| **C.1** | Verifique se as interfaces de depuração da camada de aplicação, como USB, UART e outras variantes seriais, estão desativadas ou protegidas por uma senha complexa. | ✓ | ✓ | ✓ | 4.0 |
| **C.2** | Verifique se as chaves e certificados criptográficos são exclusivos para cada dispositivo individual. | ✓ | ✓ | ✓ | 4.0 |
| **C.3** | Verifique se os controles de proteção de memória, como ASLR e DEP, estão ativados pelo sistema operacional integrado/IoT, se aplicável. | ✓ | ✓ | ✓ | 4.0 |
| **C.4** | Verifique se as interfaces de depuração no chip, como JTAG ou SWD, estão desabilitadas ou se o mecanismo de proteção disponível está habilitado e configurado adequadamente. | ✓ | ✓ | ✓ | 4.0 |
| **C.5** | Verifique se a execução confiável está implementada e habilitada, se disponível no dispositivo SoC ou CPU. | ✓ | ✓ | ✓ | 4.0 |
| **C.6** | Verifique se dados confidenciais, chaves privadas e certificados estão armazenados com segurança em um Elemento Seguro, TPM, TEE (Ambiente de Execução Confiável) ou protegidos por criptografia forte. | ✓ | ✓ | ✓ | 4.0 |
| **C.7** | Verifique se as aplicações de firmware protegem os dados em trânsito usando a segurança da camada de transporte. | ✓ | ✓ | ✓ | 4.0 |
| **C.8** | Verifique se as aplicações de firmware validam a assinatura digital das conexões do servidor. | ✓ | ✓ | ✓ | 4.0 |
| **C.9** | Verifique se as comunicações sem fio são mutuamente autenticadas. | ✓ | ✓ | ✓ | 4.0 |
| **C.10** | Verifique se as comunicações sem fio são enviadas por um canal criptografado. | ✓ | ✓ | ✓ | 4.0 |
| **C.11** | Verifique se qualquer uso de funções C proibidas é substituído pelas funções equivalentes seguras apropriadas. | ✓ | ✓ | ✓ | 4.0 |
| **C.12** | Verifique se cada firmware mantém uma lista de materiais de software catalogando componentes de terceiros, versões e vulnerabilidades publicadas. | ✓ | ✓ | ✓ | 4.0 |
| **C.13** | Verifique se todos os códigos, incluindo binários, bibliotecas e estruturas de terceiros, são revisados ​​quanto a credenciais codificadas (backdoors). | ✓ | ✓ | ✓ | 4.0 |
| **C.14** | Verifique se os componentes da aplicação e do firmware não são suscetíveis à injeção de comando do sistema operacional, invocando wrappers de comando shell, scripts ou se os controles de segurança impedem a injeção de comando do sistema operacional. | ✓ | ✓ | ✓ | 4.0 |
| **C.15** | Verifique se as aplicações de firmware fixam a assinatura digital em servidores confiáveis. | | ✓ | ✓ | 4.0 |
| **C.16** | Verifique a presença de recursos de resistência e/ou detecção de violação. | | ✓ | ✓ | 4.0 |
| **C.17** | Verifique se todas as tecnologias de proteção de propriedade intelectual disponíveis fornecidas pelo fabricante do chip estão ativadas. | | ✓ | ✓ | 4.0 |
| **C.18** | Verifique se os controles de segurança estão em vigor para impedir a engenharia reversa do firmware (por exemplo, remoção de símbolos de depuração detalhados). | | ✓ | ✓ | 4.0 |
| **C.19** | Verifique se o dispositivo valida a assinatura da imagem de inicialização antes de carregar. | | ✓ | ✓ | 4.0 |
| **C.20** | Verifique se o processo de atualização do firmware não é vulnerável a ataques de tempo de verificação versus tempo de uso. | | ✓ | ✓ | 4.0 |
| **C.21** | Verifique se o dispositivo usa assinatura de código e valida os arquivos de atualização do firmware antes da instalação. | | ✓ | ✓ | 4.0 |
| **C.22** | Verifique se o dispositivo não pode ser rebaixado para versões antigas (anti-reversão) de firmware válido. | | ✓ | ✓ | 4.0 |
| **C.23** | Verifique o uso do gerador de números pseudoaleatórios criptograficamente seguro no dispositivo incorporado (por exemplo, usando geradores de números aleatórios fornecidos por chip). | | ✓ | ✓ | 4.0 |
| **C.24** | Verifique se o firmware pode executar atualizações automáticas de firmware em um cronograma predefinido. | | ✓ | ✓ | 4.0 |
| **C.25** | Verifique se o dispositivo limpa o firmware e os dados confidenciais após a detecção de adulteração ou recebimento de mensagem inválida. | | | ✓ | 4.0 |
| **C.26** | Verifique se apenas os microcontroladores que suportam a desativação de interfaces de depuração (por exemplo, JTAG, SWD) são usados. | | | ✓ | 4.0 |
| **C.27** | Verifique se apenas os microcontroladores que fornecem proteção substancial contra ataques de decapagem e de canal lateral são usados. | | | ✓ | 4.0 |
| **C.28** | Verifique se os traços sensíveis não estão expostos às camadas externas da placa de circuito impresso. | | | ✓ | 4.0 |
| **C.29** | Verifique se a comunicação entre chips está criptografada (por exemplo, comunicação da placa principal para a placa filha). | | | ✓ | 4.0 |
| **C.30** | Verifique se o dispositivo usa assinatura de código e valida o código antes da execução. | | | ✓ | 4.0 |
| **C.31** | Verifique se as informações confidenciais mantidas na memória são substituídas por zeros assim que não são mais necessárias. | | | ✓ | 4.0 |
| **C.32** | Verifique se as aplicações de firmware utilizam contêineres de kernel para isolamento entre aplicações. | | | ✓ | 4.0 |
| **C.33** | Verifique se os sinalizadores de compilador seguro, como -fPIE, -fstack-protector-all, -Wl,-z,noexecstack, -Wl,-z,noexecheap, estão configurados para compilações de firmware. | | | ✓ | 4.0 |
| **C.34** | Verifique se os microcontroladores estão configurados com proteção de código (se aplicável). | | | ✓ | 4.0 |

## Referências

Para mais informações, consulte também:

* [OWASP Internet of Things Top 10](https://owasp.org/www-pdf-archive/OWASP-IoT-Top-10-2018-final.pdf)
* [Projeto OWASP Embedded Application Security](https://owasp.org/www-project-embedded-application-security/)
* [Projeto Internet of Things OWASP](https://owasp.org/www-project-internet-of-things/)
* [Trudy TCP Proxy Tool](https://github.com/praetorian-inc/trudy)
