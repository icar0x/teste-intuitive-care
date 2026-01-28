import pandas as pd
import os

path = "data/raw/extracted"
dados = []

keywords = ["EVENTO", "SINISTRO", "ASSIST", "DESPESA"]

for file in os.listdir(path):
    if file.endswith(".csv"):
        file_path = os.path.join(path, file)

        df = pd.read_csv(
            file_path,
            sep=";",
            encoding="latin1"
        )

        # filtrar apenas despesas
        df_filtrado = df[
            df["DESCRICAO"]
            .str.upper()
            .str.contains("|".join(keywords), na=False)
        ]

        # extrair ano e trimestre do nome do arquivo
        trimestre = file[0]
        ano = file[-8:-4]

        df_final = pd.DataFrame({
            "Identificador": df_filtrado["REG_ANS"],
            "Ano": ano,
            "Trimestre": trimestre,
            "ValorDespesas": df_filtrado["VL_SALDO_FINAL"]
        })

        dados.append(df_final)

# consolidar tudo
df_consolidado = pd.concat(dados, ignore_index=True)

# salvar
os.makedirs("data/processed", exist_ok=True)
df_consolidado.to_csv(
    "data/processed/consolidado_despesas.csv",
    index=False
)

print("CSV consolidado gerado com sucesso!")
