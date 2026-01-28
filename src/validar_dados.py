import pandas as pd

df = pd.read_csv("data/processed/consolidado_despesas.csv")

# remover identificadores vazios
df = df.dropna(subset=["Identificador"])

# converter valor para numérico
df["ValorDespesas"] = pd.to_numeric(df["ValorDespesas"], errors="coerce")

# manter apenas valores positivos
df = df[df["ValorDespesas"] > 0]

# validar trimestre
df = df[df["Trimestre"].isin(["1", "2", "3", "4"])]

# salvar
df.to_csv(
    "data/processed/consolidado_despesas_validado.csv",
    index=False
)

print("Validação concluída!")
