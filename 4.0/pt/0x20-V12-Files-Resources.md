# V12 Arquivos e Recursos

## Objetivo de controle

Certifique-se de que uma aplicação verificado atenda aos seguintes requisitos de alto nível:

* Dados de arquivos não confiáveis devem ser tratados adequadamente e de maneira segura.
* Dados de arquivos não confiáveis obtidos de fontes não confiáveis são armazenados fora da raiz da web e com permissões limitadas.

## V12.1 Carregamento de arquivo

Embora as bombas zip sejam eminentemente testáveis usando técnicas de teste de penetração, elas são consideradas L2 e acima para encorajar a consideração de design e desenvolvimento com testes manuais cuidadosos e para evitar testes de penetração manuais automatizados ou não qualificados de uma condição de negação de serviço.

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.1.1** | Verifique se a aplicação não aceitará arquivos grandes que possam encher o armazenamento ou causar uma negação de serviço. | ✓ | ✓ | ✓ | 400 |
| **12.1.2** | Verifique se a aplicação verifica os arquivos compactados (por exemplo, zip, gz, docx, odt) em relação ao tamanho máximo descompactado permitido e ao número máximo de arquivos antes de descompactar o arquivo. | | ✓ | ✓ | 409 |
| **12.1.3** | Verifique se uma cota de tamanho de arquivo e um número máximo de arquivos por usuário são aplicados para garantir que um único usuário não possa preencher o armazenamento com muitos arquivos ou arquivos excessivamente grandes. | | ✓ | ✓ | 770 |

## V12.2 Integridade do arquivo

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.2.1** | Verifique se os arquivos obtidos de fontes não confiáveis são validados como sendo do tipo esperado com base no conteúdo do arquivo. | | ✓ | ✓ | 434 |

## V12.3 Execução de Arquivo

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.3.1** | Verifique se os metadados de nome de arquivo enviados pelo usuário não são usados diretamente pelo sistema ou sistemas de arquivos de estrutura e se uma API de URL é usada para proteção contra travessia de caminho. | ✓ | ✓ | ✓ | 22 |
| **12.3.2** | Verifique se os metadados de nome de arquivo enviados pelo usuário são validados ou ignorados para impedir a divulgação, criação, atualização ou remoção de arquivos locais (LFI). | ✓ | ✓ | ✓ | 73 |
| **12.3.3** | Verifique se os metadados de nome de arquivo enviados pelo usuário são validados ou ignorados para evitar a divulgação ou execução de arquivos remotos por ataques de inclusão de arquivo remoto (RFI) ou falsificação de solicitação do lado do servidor (SSRF). | ✓ | ✓ | ✓ | 98 |
| **12.3.4** | Verifique se a aplicação protege contra download de arquivo reflexivo (RFD) validando ou ignorando nomes de arquivo enviados pelo usuário num parâmetro JSON, JSONP ou URL, o cabeçalho Content-Type de resposta deve ser definido como text/plain e o cabeçalho Content-Disposition deve ter um nome de arquivo fixo. | ✓ | ✓ | ✓ | 641 |
| **12.3.5** | Verifique se os metadados de arquivos não confiáveis não são usados diretamente com API ou bibliotecas do sistema, para proteger contra a injeção de comandos do sistema operacional. | ✓ | ✓ | ✓ | 78 |
| **12.3.6** | Verifique se a aplicação não inclui e executa funcionalidades de fontes não confiáveis, como redes de distribuição de conteúdos não verificados, bibliotecas JavaScript, bibliotecas de nó npm ou DLLs do lado do servidor. | | ✓ | ✓ | 829 |

## V12.4 Armazenamento de Arquivos

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.4.1** | Verifique se os arquivos obtidos de fontes não confiáveis são armazenados fora da raiz da web, com permissões limitadas.                                               | ✓ | ✓ | ✓ | 552 |
| **12.4.2** | Verifique se os arquivos obtidos de fontes não confiáveis são verificados por scanners antivírus para impedir o upload e a exibição de conteúdo malicioso conhecido. | ✓ | ✓ | ✓ | 509 |

## Download do arquivo V12.5

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.5.1** | Verifique se a camada da web está configurada para servir apenas arquivos com extensões de arquivo específicas para evitar informações não intencionais e vazamento de código-fonte. Por exemplo, arquivos de backup (por exemplo, .bak), arquivos de trabalho temporários (por exemplo, .swp), arquivos compactados (.zip, .tar.gz, etc) e outras extensões comumente usadas por editores devem ser bloqueados, a menos que necessário. | ✓ | ✓ | ✓ | 552 |
| **12.5.2** | Verifique se as solicitações diretas para arquivos carregados nunca serão executadas como conteúdo HTML/JavaScript. | ✓ | ✓ | ✓ | 434 |

## V12.6 Proteção SSRF

| # | Descrição | L1 | L2 | L3 | CWE |
| :---: | :--- | :---: | :---:| :---: | :---: |
| **12.6.1** | Verifique se o servidor da web ou de aplicações está configurado com uma lista de permissões de recursos ou sistemas para os quais o servidor pode enviar solicitações ou carregar dados/arquivos. | ✓ | ✓ | ✓ | 918 |

## Referências

Para mais informações, consulte também:

* [File Extension Handling for Sensitive Information](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
* [Reflective file download by Oren Hafif](https://www.trustwave.com/Resources/SpiderLabs-Blog/Reflected-File-Download---A-New-Web-Attack-Vector/)
* [OWASP Third Party JavaScript Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html)
