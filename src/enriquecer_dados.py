import pandas as pd

# carregar despesas validadas
despesas = pd.read_csv(
    "data/processed/consolidado_despesas_validado.csv"
)

# carregar cadastro das operadoras
cadop = pd.read_csv(
    "data/raw/relatorio_cadop.csv",
    sep=";",
    encoding="latin1"
)

# renomear coluna para facilitar o join
cadop = cadop.rename(columns={
    "REGISTRO_OPERADORA": "Identificador"
})

# selecionar apenas colunas relevantes
cadop = cadop[
    [
        "Identificador",
        "CNPJ",
        "Razao_Social",
        "Modalidade",
        "UF"
    ]
]

# join (LEFT JOIN para não perder despesas)
df_final = despesas.merge(
    cadop,
    on="Identificador",
    how="left"
)

# salvar resultado final
df_final.to_csv(
    "data/processed/despesas_enriquecidas.csv",
    index=False
)

print("Enriquecimento concluído com sucesso!")
