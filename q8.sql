-- Tabela temporária para contar o número de diagnosticos tipo U.
WITH temp_atendimento  AS (
SELECT COUNT(*) AS diag_count
FROM ATENDIMENTO a
INNER JOIN DIAGNOSTICO d ON a.id = d.id_atendimento
WHERE a.tipo_atendimento = 'U'
GROUP BY a.id
)
SELECT AVG(diag_count) AS media_atendimentos_U
FROM temp_atendimento;

