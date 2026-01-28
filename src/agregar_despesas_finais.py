import pandas as pd

# carregar dados enriquecidos
df = pd.read_csv("data/processed/despesas_enriquecidas.csv")

# remover registros sem Razão Social ou UF
df = df.dropna(subset=["Razao_Social", "UF"])

# garantir valor numérico
df["ValorDespesas"] = pd.to_numeric(df["ValorDespesas"], errors="coerce")

# agregação final
agrupado = (
    df
    .groupby(["Razao_Social", "UF"])["ValorDespesas"]
    .agg(
        Total="sum",
        Media_Trimestral="mean",
        Desvio_Padrao="std"
    )
    .reset_index()
)

# ordenar por total
agrupado = agrupado.sort_values(
    "Total",
    ascending=False
)

# salvar CSV final
agrupado.to_csv(
    "data/processed/despesas_agregadas.csv",
    index=False
)

print("Agregação final concluída com sucesso!")
