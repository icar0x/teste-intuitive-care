CREATE TABLE operadoras (
    registro_ans INTEGER PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social TEXT,
    modalidade TEXT,
    uf CHAR(2)
);

CREATE TABLE despesas (
    id SERIAL PRIMARY KEY,
    registro_ans INTEGER,
    ano INTEGER,
    trimestre INTEGER,
    valor_despesa NUMERIC(15,2),
    FOREIGN KEY (registro_ans) REFERENCES operadoras (registro_ans)
);

CREATE INDEX idx_despesas_registro_ans ON despesas (registro_ans);
CREATE INDEX idx_despesas_ano_trimestre ON despesas (ano, trimestre);
