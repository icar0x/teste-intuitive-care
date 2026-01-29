COPY operadoras (registro_ans, cnpj, razao_social, modalidade, uf)
FROM '/path/despesas_enriquecidas.csv'
DELIMITER ','
CSV HEADER;

COPY despesas (registro_ans, ano, trimestre, valor_despesa)
FROM '/path/consolidado_despesas_validado.csv'
DELIMITER ','
CSV HEADER;
