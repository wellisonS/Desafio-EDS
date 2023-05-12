SELECT p1.nome, p1.id, p1.cpf, p1.nome_mae, p1.dt_atualizacao
FROM stg_prontuario.PACIENTE p1
INNER JOIN (
  SELECT nome, id, cpf, MAX(dt_atualizacao) AS data_atualizacao
  FROM stg_prontuario.PACIENTE
  GROUP BY nome, id, cpf
  HAVING COUNT(*) > 1
) p2 ON p1.nome = p2.nome AND p1.id = p2.id AND p1.cpf = p2.cpf AND p1.dt_atualizacao = p2.data_atualizacao;
