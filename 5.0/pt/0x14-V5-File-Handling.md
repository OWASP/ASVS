# V5 Manipulação de Arquivos

## Objetivo de Controle

O uso de arquivos pode apresentar uma variedade de riscos à aplicação, incluindo negação de serviço, acesso não autorizado e esgotamento de armazenamento. Este capítulo inclui requisitos para abordar esses riscos.

## V5.1 Documentação de Manipulação de Arquivos

Esta seção inclui um requisito para documentar as características esperadas dos arquivos aceitos pela aplicação, como uma pré-condição necessária para desenvolver e verificar verificações de segurança relevantes.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **5.1.1** | Verifique se a documentação define os tipos de arquivos permitidos, as extensões de arquivo esperadas e o tamanho máximo (incluindo o tamanho descompactado) para cada recurso de upload. Além disso, certifique-se de que a documentação especifique como os arquivos são tornados seguros para que os usuários finais façam download e os processem, como, por exemplo, o comportamento da aplicação quando um arquivo malicioso é detectado. | 2 |

## V5.2 Upload de Arquivo e Conteúdo

A funcionalidade de upload de arquivo é uma fonte primária de arquivos não confiáveis. Esta seção descreve os requisitos para garantir que a presença, o volume ou o conteúdo desses arquivos não possam prejudicar a aplicação.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **5.2.1** | Verifique se a aplicação aceitará apenas arquivos de um tamanho que possa processar sem causar perda de desempenho ou um ataque de negação de serviço. | 1 |
| **5.2.2** | Verifique se, quando a aplicação aceita um arquivo, seja individualmente ou dentro de um arquivo compactado como um zip, ela verifica se a extensão do arquivo corresponde a uma extensão esperada e valida se o conteúdo corresponde ao tipo representado pela extensão. Isso inclui, mas não se limita a, verificar os 'magic bytes' (bytes mágicos) iniciais, realizar a reescrita de imagem e usar bibliotecas especializadas para validação de conteúdo de arquivo. Para L1, o foco pode ser apenas nos arquivos que são usados para tomar decisões específicas de negócios ou segurança. Para L2 e superior, isso deve se aplicar a todos os arquivos sendo aceitos. | 1 |
| **5.2.3** | Verifique se a aplicação verifica os arquivos compactados (ex., zip, gz, docx, odt) em relação ao tamanho máximo não compactado permitido e em relação ao número máximo de arquivos antes de descompactar o arquivo. | 2 |
| **5.2.4** | Verifique se uma cota de tamanho de arquivo e um número máximo de arquivos por usuário são aplicados para garantir que um único usuário não possa encher o armazenamento com muitos arquivos ou arquivos excessivamente grandes. | 3 |
| **5.2.5** | Verifique se a aplicação não permite o upload de arquivos compactados contendo links simbólicos (symlinks), a menos que isso seja especificamente exigido (nesse caso, será necessário impor uma lista de permissões dos arquivos que podem ser vinculados via symlink). | 3 |
| **5.2.6** | Verifique se a aplicação rejeita imagens enviadas com um tamanho de pixel maior que o máximo permitido, para evitar ataques de inundação de pixels (pixel flood). | 3 |

## V5.3 Armazenamento de Arquivos

Esta seção inclui requisitos para evitar que arquivos sejam executados indevidamente após o upload, para detectar conteúdo perigoso e para evitar que dados não confiáveis sejam usados para controlar onde os arquivos estão sendo armazenados.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **5.3.1** | Verifique se os arquivos carregados ou gerados por entrada não confiável e armazenados em uma pasta pública não são executados como código de programa no lado do servidor quando acessados diretamente por uma requisição HTTP. | 1 |
| **5.3.2** | Verifique se, quando a aplicação cria caminhos de arquivo para operações de arquivo, em vez de usar nomes de arquivo enviados pelo usuário, ela usa dados gerados internamente ou confiáveis. Se os nomes de arquivo enviados pelo usuário ou os metadados do arquivo precisarem ser usados, validação e sanitização estritas devem ser aplicadas. Isso visa proteger contra ataques de path traversal, inclusão de arquivo local ou remoto (LFI, RFI) e falsificação de solicitação do lado do servidor (SSRF). | 1 |
| **5.3.3** | Verifique se o processamento de arquivos no lado do servidor, como a descompactação de arquivos, ignora as informações de caminho fornecidas pelo usuário para evitar vulnerabilidades como zip slip. | 3 |

## V5.4 Download de Arquivos

Esta seção contém requisitos para mitigar riscos ao servir arquivos a serem baixados, incluindo ataques de path traversal e injeção. Isso também inclui certificar-se de que eles não contêm conteúdo perigoso.

| # | Descrição | Nível |
| :---: | :--- | :---: |
| **5.4.1** | Verifique se a aplicação valida ou ignora os nomes de arquivo enviados pelo usuário, inclusive em um JSON, JSONP ou parâmetro de URL, e especifica um nome de arquivo no campo de cabeçalho Content-Disposition na resposta. | 2 |
| **5.4.2** | Verifique se os nomes de arquivos servidos (por exemplo, em campos de cabeçalho de resposta HTTP ou anexos de e-mail) são codificados ou sanitizados (por exemplo, seguindo a RFC 6266) para preservar a estrutura do documento e prevenir ataques de injeção. | 2 |
| **5.4.3** | Verifique se os arquivos obtidos de fontes não confiáveis são verificados por scanners antivírus para evitar a veiculação de conteúdo malicioso conhecido. | 2 |

## Referências

Para mais informações, veja também:

* [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
* [Example of using symlinks for arbitrary file read](https://hackerone.com/reports/1439593)
* [Explanation of "Magic Bytes" from Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures)
