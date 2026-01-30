Teste Técnico – Pipeline de Dados (ANS)

O foco do projeto foi resolver o problema de forma simples, organizada e bem documentada, priorizando clareza e decisões técnicas conscientes, em vez de soluções complexas ou artificiais.

🎯 O que este projeto faz
De forma resumida, o projeto:
Processa dados contábeis trimestrais da ANS
Filtra despesas relacionadas a eventos e sinistros
Consolida dados de múltiplos trimestres
Trata inconsistências comuns em dados reais
Enriquecer os dados com informações cadastrais das operadoras
Gera análises agregadas
Modela os dados e consultas em SQL para análise posterior

🛠 Tecnologias utilizadas

Python 
Linguagem principal utilizada para todo o pipeline de dados.
Pandas
Biblioteca usada para leitura, tratamento, validação e agregação dos dados em CSV.
SQL
Utilizado para modelagem dos dados e criação de consultas analíticas.

🗂 Organização do repositório
teste-intuitive-care/
│
├── data/
│   ├── raw/                  # Dados brutos
│   │   ├── extracted/        # CSVs extraídos dos arquivos ZIP
│   │   └── relatorio_cadop.csv
│   │
│   └── processed/            # Dados tratados e consolidados
│       ├── consolidado_despesas.csv
│       ├── consolidado_despesas_validado.csv
│       ├── despesas_enriquecidas.csv
│       └── despesas_agregadas.csv
│
├── src/                      # Scripts do pipeline
│   ├── extract_zips.py
│   ├── consolidar_despesas.py
│   ├── validar_dados.py
│   ├── enriquecer_dados.py
│   └── agregar_despesas_finais.py
│
├── sql/                      # Modelagem e consultas SQL
│   ├── schema.sql
│   ├── load.sql
│   └── queries.sql
│
└── README.md

🔄 Como o pipeline funciona

O fluxo de dados segue a seguinte lógica:
Extração dos arquivos ZIP disponibilizados pela ANS
Leitura dos arquivos CSV, considerando separador e encoding
Filtragem das despesas relevantes
Consolidação dos dados dos diferentes trimestres
Validação e limpeza dos dados
Enriquecimento com o cadastro das operadoras
Agregação final para análise
Esse fluxo foi dividido em scripts separados para facilitar leitura, manutenção e entendimento.

🧠 Principais decisões técnicas

Uso do Python com Pandas
Escolhido pela praticidade e clareza na manipulação de dados em CSV.
Tratamento dos dados antes do SQL
Optou-se por limpar, validar e consolidar os dados em Python, reduzindo a complexidade das consultas SQL.
Uso do REG_ANS como identificador
Os arquivos contábeis não possuem CNPJ ou Razão Social. O REG_ANS foi a única chave consistente para relacionar os dados financeiros com o cadastro das operadoras.
LEFT JOIN no enriquecimento
Garantiu que nenhuma despesa fosse descartada por ausência de cadastro.
Priorização do escopo
O foco foi o pipeline de dados e a análise. API e frontend não foram implementados para evitar uma solução superficial.

🗄 SQL
A etapa de SQL foi desenvolvida com foco em modelagem e análise, utilizando como base os arquivos CSV gerados pelo pipeline em Python.
Foram definidas tabelas separando:
Dados cadastrais das operadoras
Dados financeiros consolidados
As consultas SQL presentes no projeto permitem:
Analisar o total de despesas por operadora
Comparar despesas por UF
Calcular médias e agregações
O SQL foi escrito de forma genérica, podendo ser adaptado para diferentes bancos relacionais com ajustes mínimos.
