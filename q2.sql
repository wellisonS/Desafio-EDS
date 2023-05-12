-- Copiar os dados de pacientes do hospital A para a tabela PACIENTE
INSERT INTO stg_prontuario.PACIENTE   (id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao) 
SELECT id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM stg_hospital_a.PACIENTE;

-- Copiar os dados de pacientes do hospital B para a tabela PACIENTE
INSERT INTO stg_prontuario.PACIENTE (id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao)
SELECT id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM stg_hospital_b.PACIENTE;

-- Copiar os dados de pacientes do hospital C para a tabela PACIENTE
INSERT INTO stg_prontuario.PACIENTE   (id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao)
SELECT id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM stg_hospital_c.PACIENTE;
