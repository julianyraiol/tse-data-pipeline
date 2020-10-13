from elasticsearch import Elasticsearch


class ElasticConnection:
    def __init__(self):
        self.client = Elasticsearch("localhost:9200")

    def post(self, index, document):
        document = self.client.index(index=index, body=document, refresh=True)
        return document

    def create_index(self, index, mappings):
        return self.client.indices.create(index=index, body=mappings)

    def delete_index(self, index):
        return self.client.indices.delete(index=index)

    def index_exists(self, index):
        return self.client.indices.exists(index=index)
