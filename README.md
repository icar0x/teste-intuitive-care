📌 Contexto

Este projeto foi desenvolvido como parte de um teste técnico para vaga de estágio, com o objetivo de avaliar a capacidade de trabalhar com dados reais, tomar decisões técnicas fundamentadas e documentar o processo.

Os dados utilizados são públicos e disponibilizados pela ANS (Agência Nacional de Saúde Suplementar), o que implica lidar com arquivos inconsistentes, diferentes formatos e ausência de padronização.

🎯 Objetivo

O objetivo do projeto é:

Coletar dados de demonstrações contábeis da ANS

Identificar e consolidar despesas relacionadas a eventos/sinistros

Tratar e validar inconsistências nos dados

Enriquecer os dados com informações cadastrais das operadoras

Gerar análises agregadas sobre as despesas das operadoras de planos de saúde

🗂 Estrutura do Projeto
teste-intuitive-care/
│
├── data/
│   ├── raw/                    # Dados brutos (ZIPs e CSVs originais)
│   │   ├── extracted/          # Arquivos extraídos dos ZIPs
│   │   └── relatorio_cadop.csv # Cadastro das operadoras
│   │
│   └── processed/              # Dados processados
│       ├── consolidado_despesas.csv
│       ├── consolidado_despesas_validado.csv
│       ├── despesas_enriquecidas.csv
│       └── despesas_agregadas.csv
│
├── src/                        # Scripts Python
│   ├── extract_zips.py
│   ├── inspect_csvs.py
│   ├── consolidar_despesas.py
│   ├── validar_dados.py
│   ├── enriquecer_dados.py
│   └── agregar_despesas_finais.py
│
└── README.md

🔄 Fluxo de Processamento dos Dados

O pipeline de dados segue o seguinte fluxo:

Arquivos ZIP da ANS
   ↓
Extração dos arquivos
   ↓
Leitura de CSVs com formatos inconsistentes
   ↓
Filtragem de despesas (eventos/sinistros)
   ↓
Consolidação por trimestre
   ↓
Validação dos dados
   ↓
Enriquecimento com cadastro das operadoras
   ↓
Agregação e análise final

🧩 Etapas Desenvolvidas
1️⃣ Extração dos Arquivos

Os arquivos ZIP referentes aos últimos trimestres foram extraídos automaticamente para garantir organização e reprodutibilidade do processo.

Decisão técnica:
A extração automatizada reduz erros manuais e facilita a reexecução do pipeline.

2️⃣ Leitura e Inspeção dos CSVs

Os arquivos extraídos apresentaram:

Separador ;

Encoding latin1

Estrutura contábil não padronizada

Foi adotada uma leitura flexível para evitar falhas de parsing.

Trade-off:
Priorizar robustez na leitura em vez de assumir um formato CSV padrão.

3️⃣ Consolidação das Despesas

Foram filtrados apenas os registros relacionados a despesas, eventos e sinistros, com base em palavras-chave na coluna de descrição contábil.

Como os arquivos não possuem CNPJ ou Razão Social, foi utilizado o identificador REG_ANS como chave primária.

Decisão técnica:
O vínculo com CNPJ e Razão Social é realizado posteriormente por meio do cadastro oficial das operadoras.

4️⃣ Validação dos Dados

Foram aplicadas regras básicas de qualidade:

Remoção de identificadores vazios

Conversão de valores para tipo numérico

Exclusão de valores negativos ou inválidos

Validação do trimestre

Trade-off:
Optou-se por remover registros inválidos para garantir consistência das análises.

5️⃣ Enriquecimento dos Dados

Os dados consolidados foram enriquecidos com o arquivo relatorio_cadop.csv, adicionando:

CNPJ

Razão Social

Modalidade

UF

Foi utilizado LEFT JOIN para evitar perda de registros financeiros.

Decisão técnica:
Registros sem correspondência no cadastro são mantidos, com campos nulos.

6️⃣ Agregação Final

Os dados enriquecidos foram agregados por:

Razão Social

UF

Foram calculadas:

Soma total das despesas

Média trimestral

Desvio padrão das despesas

Os resultados foram ordenados do maior para o menor valor total.

📊 Arquivos Gerados

consolidado_despesas.csv – dados consolidados brutos

consolidado_despesas_validado.csv – dados após validação

despesas_enriquecidas.csv – dados com informações cadastrais

despesas_agregadas.csv – resultado analítico final

🧠 Considerações e Limitações

Os dados públicos apresentam inconsistências naturais

Nem todas as operadoras possuem correspondência no cadastro

O projeto prioriza simplicidade, clareza e manutenibilidade (KISS)

▶️ Como Executar o Projeto
1️⃣ Instalar dependências
pip install pandas

2️⃣ Executar os scripts (ordem sugerida)
python src/extract_zips.py
python src/consolidar_despesas.py
python src/validar_dados.py
python src/enriquecer_dados.py
python src/agregar_despesas_finais.py
