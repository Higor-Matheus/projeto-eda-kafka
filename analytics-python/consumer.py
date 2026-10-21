from kafka import KafkaConsumer
import json
import pandas as pd

consumer = KafkaConsumer(
    "vendas",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

dados = []

for msg in consumer:

    venda = msg.value

    print(venda)

    dados.append(venda)

    if len(dados) >= 5:

        df = pd.DataFrame(dados)

        df.to_csv(
            "vendas.csv",
            index=False
        )

        print("CSV criado.")

        break