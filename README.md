# tse-data-pipeline

Baixa e processa os arquivos referentes candidatos nas eleições de 1994 a 2020

Fonte: [Tribunal Superior Eleitoral](https://www.tse.jus.br/hotsites/pesquisas-eleitorais/candidatos.html)

### Setup
Este projeto requer **Python 3.+** e a instalação do [**Pipenv**](https://pipenv-fork.readthedocs.io/en/latest/install.html), arquivo que contém as dependências do projeto. Para instalá-lo, execute: 

```bash
pip install pipenv
```

Caso, haja algum problema durante a instação do pacote, veja a documentação da ferramenta.

### Configuração o projeto

Faça o clone deste projeto e execute o arquivo **Pipenv**:

```bash
$ git clone https://github.com/julianyraiol/tse-data-pipeline.git
$ cd tse-data-pipeline
$ pipenv install
$ pienv shell
```

### Para executar o crawler

Esta etapa realiza o download dos arquivos referente aos candidatos.

No seu terminal, já tendo executado o arquivo de instalação, execute o seguinte comando:

```bash
$ scrapy crawl candidatos
```

Os arquivos estarão armazenados napasta **data**.

Para extrair os arquivos, basta executar o seguinte comando:

```bash
$ scrapy crawl processing

run
python3 -m processing.main
