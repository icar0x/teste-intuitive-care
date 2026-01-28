import pandas as pd
import os

path = "data/raw/extracted"

for file in os.listdir(path):
    if file.endswith(".csv"):
        file_path = os.path.join(path, file)
        print("\nArquivo:", file)

        try:
            df = pd.read_csv(
                file_path,
                sep=";",          # ← separador
                encoding="latin1",  # ← muito comum em dados públicos
                nrows=5
            )
            print("Colunas:", list(df.columns))

        except Exception as e:
            print("Erro ao ler arquivo:", e)
