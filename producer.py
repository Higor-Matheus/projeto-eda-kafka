import time
import requests
from kafka import KafkaProducer
import json

# Configuração do Produtor Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC_NAME = 'posts-stream'

def fetch_and_publish():
    print("Buscando dados da API pública (JSONPlaceholder)...")
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()[:10]  # Pegamos apenas 10 registros para manter simples e leve

    for post in posts:
        # Criando o evento estruturado
        event = {
            "evento_id": post["id"],
            "usuario_id": post["userId"],
            "titulo": post["title"],
            "conteudo": post["body"],
            "timestamp": time.time()
        }
        
        producer.send(TOPIC_NAME, value=event)
        print(f"[PRODUCER] Publicado post ID: {post['id']}")
        time.sleep(1) # Simula um fluxo contínuo de eventos

    producer.flush()
    print("Todos os eventos foram publicados com sucesso!")

if __name__ == "__main__":
    fetch_and_publish()