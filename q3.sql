SELECT nome, id, cpf, COUNT(*) AS quantidade_duplicados
FROM stg_prontuario.PACIENTE
GROUP BY nome, id, cpf
HAVING COUNT(*) > 1;