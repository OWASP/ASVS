# V9 Comunicação

## Objetivo de controle

Certifique-se de que uma aplicação verificado atenda aos seguintes requisitos de alto nível:

* Requer TLS ou criptografia forte, independente da sensibilidade do conteúdo.
* Siga as orientações mais recentes, incluindo:
  * Conselho de configuração
  * Algoritmos e cifras preferidos
* Evite algoritmos e cifras fracos ou prestes a serem obsoletos, exceto como último recurso
* Desabilite algoritmos e cifras obsoletos ou inseguros conhecidos.

Dentro desses requisitos:

* Mantenha-se atualizado com os conselhos recomendados do setor sobre a configuração segura do TLS, pois ele muda com frequência (geralmente devido a quebras catastróficas nos algoritmos e cifras existentes).
* Use as versões mais recentes das ferramentas de revisão de configuração TLS para configurar a ordem preferida e a seleção do algoritmo.
* Verifique a sua configuração periodicamente para garantir que a comunicação segura esteja sempre presente e eficaz.

## V9.1 Segurança de comunicação do cliente

Certifique-se de que todas as mensagens do cliente sejam enviadas por redes criptografadas, usando TLS 1.2 ou posterior.
Use ferramentas atualizadas para revisar a configuração do cliente regularmente.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.1.1** | Verifique se o TLS é usado para toda a conectividade do cliente e não retrocede para comunicações inseguras ou não criptografadas. ([C8](https://owasp.org/www-project-proactive-controls/#div-numbering)) | ✓ | ✓ | ✓ | 319 |
| **9.1.2** | Verifique, usando ferramentas de teste de TLS atualizadas, que somente conjuntos de cifras fortes estão ativados, com os conjuntos de cifras mais fortes definidos como preferenciais. | ✓ | ✓ | ✓ | 326 |
| **9.1.3** | Verifique se apenas as versões recomendadas mais recentes do protocolo TLS estão habilitadas, como TLS 1.2 e TLS 1.3. A versão mais recente do protocolo TLS deve ser a opção preferida. | ✓ | ✓ | ✓ | 326 |

## V9.2 Segurança de comunicação do servidor

As comunicações do servidor são mais que apenas HTTP. Conexões seguras de e para outros sistemas, como sistemas de monitoramento, ferramentas de gestão, acesso remoto e ssh, middleware, banco de dados, mainframes, parceiros ou sistemas de origem externa — devem estar em vigor. Tudo isso deve ser criptografado para evitar "difícil por fora, trivialmente fácil de interceptar por dentro".

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **9.2.1** | Verifique se as conexões de e para o servidor usam certificados TLS confiáveis. Onde certificados gerados internamente ou autoassinados são usados, o servidor deve ser configurado para confiar apenas em CAs internas específicas e certificados autoassinados específicos. Todos os outros devem ser rejeitados. | | ✓ | ✓ | 295 |
| **9.2.2** | Verifique se as comunicações criptografadas, como TLS, são usadas para todas as conexões de input e output, incluindo portas de gestão, monitoramento, autenticação, API ou chamadas de Web Service, banco de dados, nuvem, serverless, mainframe, externas e conexões de parceiros. O servidor não deve recorrer a protocolos inseguros ou não criptografados. | | ✓ | ✓ | 319 |
| **9.2.3** | Verifique se todas as conexões criptografadas com sistemas externos que envolvem informações ou funções confidenciais são autenticadas. | | ✓ | ✓ | 287 |
| **9.2.4** | Verifique se a revogação de certificação adequada, como o grampeamento do protocolo de status de certificado on-line (OCSP), está habilitada e configurada. | | ✓ | ✓ | 299 |
| **9.2.5** | Verifique se as falhas de conexão TLS de back-end são registradas. | | | ✓ | 544 |

## Referências

Para mais informações, consulte também:

* [OWASP – TLS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* [OWASP — Guia de Fixação](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)
* Notas sobre “Modos aprovados de TLS”:
  * No passado, a ASVS referia-se ao padrão americano FIPS 140-2, mas como um padrão global, a aplicação dos padrões americanos pode ser difícil, contraditória ou confusa.
  * Um método melhor para obter conformidade com a seção 9.1 seria revisar guias como [TLS do lado do servidor da Mozilla](https://wiki.mozilla.org/Security/Server_Side_TLS) ou [gerar configurações boas conhecidas](https:// mozilla.github.io/server-side-tls/ssl-config-generator/) e use ferramentas de avaliação TLS conhecidas e atualizadas para obter o nível de segurança desejado.
