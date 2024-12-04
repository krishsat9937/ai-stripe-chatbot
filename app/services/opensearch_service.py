import openai

from datetime import datetime
from opensearchpy import OpenSearch
from app.utils.env_variables import OPENAI_API_KEY  # Import the OPENAI_API_KEY constant

client = OpenSearch(hosts=[{"host": "localhost", "port": 9200}])

def get_relevant_context(query_text, k=10):
    query_embedding = openai.embeddings.create(input=query_text, model="text-embedding-ada-002").data[0].embedding
    query_body = {
        "size": k,
        "query": {
            "knn": {
                "embedding": {
                    "vector": query_embedding,
                    "k": k
                }
            }
        }
    }
    response = client.search(index="conversation-history", body=query_body)
    return [{"message": hit["_source"]["message"], "sender": hit["_source"]["sender"]} for hit in response["hits"]["hits"]]


def save_message_to_opensearch(message, sender):
    if not message or not isinstance(message, str):
        raise ValueError("Message must be a non-empty string.")

    # Generate embedding
    embedding_response = openai.embeddings.create(
        input=message,
        model="text-embedding-ada-002"
    )
    embedding = embedding_response.data[0].embedding

    # Create document for OpenSearch
    doc = {
        "message": message,
        "embedding": embedding,
        "sender": sender,
        "timestamp": datetime.utcnow()
    }

    # Save to OpenSearch
    client.index(index="conversation-history", body=doc)