SELECT
    o.razao_social,
    SUM(d.valor_despesa) AS total_despesas
FROM despesas d
JOIN operadoras o ON o.registro_ans = d.registro_ans
GROUP BY o.razao_social
ORDER BY total_despesas DESC;

SELECT
    o.uf,
    SUM(d.valor_despesa) AS total_despesas
FROM despesas d
JOIN operadoras o ON o.registro_ans = d.registro_ans
GROUP BY o.uf
ORDER BY total_despesas DESC;

SELECT
    o.razao_social,
    AVG(d.valor_despesa) AS media_trimestral
FROM despesas d
JOIN operadoras o ON o.registro_ans = d.registro_ans
GROUP BY o.razao_social
ORDER BY media_trimestral DESC;

SELECT
    o.razao_social,
    SUM(d.valor_despesa) AS total_despesas
FROM despesas d
JOIN operadoras o ON o.registro_ans = d.registro_ans
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;
