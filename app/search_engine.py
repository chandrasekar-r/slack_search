from elasticsearch import Elasticsearch
from config.config import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT

es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT}])

def search_questions(query):
    search_body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["question", "answer"]
            }
        }
    }

    try:
        results = es.search(index="questions_answers", body=search_body)
        return results['hits']['hits']
    except Exception as e:
        print(f"Error searching questions: {e}")
        return []

