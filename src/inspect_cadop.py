import pandas as pd

df = pd.read_csv(
    "data/raw/relatorio_cadop.csv",
    sep=";",
    encoding="latin1",
    nrows=5
)

print(list(df.columns))
