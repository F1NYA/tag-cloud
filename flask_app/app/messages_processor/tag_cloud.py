from flask_app.app.messages_processor.clusters import get_clusters
from flask_app.app.messages_processor.tokenizer import process_messages
from flask_app.app.messages_processor.vectorizer import create_vectorizer, vectorize


def get_cloud(users, clusters_number=12, cluster_size=7):
    vectorizer = create_vectorizer()
    processed_messages = [word for user in users for word in process_messages(user['messages'])]
    vectors = vectorize(processed_messages, vectorizer)
    return get_clusters(vectors, vectorizer, clusters_number, cluster_size)
