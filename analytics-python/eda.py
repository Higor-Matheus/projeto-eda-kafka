import pandas as pd

df = pd.read_csv("vendas.csv")

print("\nDADOS")
print(df)

print("\nTOTAL FATURADO")
print(df["Valor"].sum())

print("\nMEDIA")
print(df["Valor"].mean())

print("\nAGRUPAMENTO")

print(
    df.groupby("Produto")["Valor"]
      .sum()
)