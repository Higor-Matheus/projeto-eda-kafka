using Confluent.Kafka;
using System.Text.Json;

var config = new ProducerConfig
{
    BootstrapServers = "localhost:9092"
};

using var producer =
    new ProducerBuilder<Null, string>(config)
    .Build();

var vendas = new[]
{
    new { Produto = "Mouse", Valor = 80 },
    new { Produto = "Teclado", Valor = 150 },
    new { Produto = "Monitor", Valor = 900 },
    new { Produto = "Mouse", Valor = 90 },
    new { Produto = "Notebook", Valor = 3500 }
};

foreach (var venda in vendas)
{
    await producer.ProduceAsync(
        "vendas",
        new Message<Null, string>
        {
            Value = JsonSerializer.Serialize(venda)
        });

    Console.WriteLine($"Enviado: {venda.Produto}");
}