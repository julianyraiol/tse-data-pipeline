# tse-data-pipeline

Baixa e processa os arquivos referentes candidatos nas eleições de 1994 a 2020

Fonte: [Tribunal Superior Eleitoral](https://www.tse.jus.br/hotsites/pesquisas-eleitorais/candidatos.html)

### Estrutura do projeto

```
|-- processing
|   |-- mapping
|   |-- elasticsearch_interface.py
|   |-- main.py
|
|-- tse_candidatos
|   |-- data
|   |-- tse_candidatos
|       | -- spiders
|           | -- candidatos.py
|           | -- processing.py
|
|       | -- items.py
|       | -- middlewares.py
|       | -- pipelines.py
|       | -- settings.py
|
|-- Pipfile
|-- Pipfile.lock
|-- README.md
`-- docker-compose.yml
```

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
$ pipenv shell
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
```

### Para persistir os dados no elasticsearch

Execute o docker-compose para criar uma instância local do elasticsearch. Ele ficará rodando na endereço: http://localhost:9200/. 

```bash
$ docker-compose up -d
```

Após isso, no diretório raiz, execute o seguinte comando para criar um index no elasticsearch.

```bash
$ python3 -m processing.main
```
