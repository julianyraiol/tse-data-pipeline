from processing.elasticsearch_interface import ElasticConnection
from processing.mapping.candidatos import candidatos_map


def create_index_candidatos():
    es_client = ElasticConnection()
    es_client.create_index("candidatos", candidatos_map)


def ingest_index_candidatos():
    pass


if __name__ == '__main__':
    create_index_candidatos()
