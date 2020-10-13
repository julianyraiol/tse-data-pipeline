from processing.elasticsearch_interface import ElasticConnection
from processing.mapping.candidatos import candidatos_map

import json
import pandas as pd
from elasticsearch import Elasticsearch, helpers


def create_index_candidatos():
    es_client = ElasticConnection()
    es_client.create_index("candidatos", candidatos_map)


def ingest_index_candidatos():
    es_client = ElasticConnection()

    years = [i for i in range(2014, 2022, 2)]

    for year in years:
        file_path_csv = 'tse_candidatos/data/{}/consulta_cand_{}_BRASIL.csv'.format(str(year), str(year))
        file_path_json = 'tse_candidatos/data/{}/consulta_cand_{}_BRASIL.json'.format(str(year), str(year))

        df = pd.read_csv(file_path_csv, sep=';', encoding="latin-1", dtype='unicode')
        df.to_json(file_path_json, orient="records")

        with open(file_path_json, 'r') as j:
            contents = json.loads(j.read())

        helpers.bulk(es_client.client, contents, index="candidatos")


if __name__ == '__main__':
    #create_index_candidatos()
    ingest_index_candidatos()
