import requests
import psycopg2

# Configurações de conexão com o banco de dados
database = "nome_do_banco"  # Nome do banco de dados
user = "usuario"  # Usuário do banco de dados
password = "senha"  # Senha do banco de dados
host = "localhost"  # Endereço do servidor do banco de dados
port = "5432"  # Porta do servidor do banco de dados

# URL da API REST
api_url = "https://exemplo.com/api/procedimentos"

# Nome da tabela no schema de staging
table_name = "nome_da_tabela"

# Estabelece a conexão com o banco de dados
conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

# Faz a solicitação HTTP para a API REST
response = requests.get(api_url)
data = response.json()

# Percorre os procedimentos médicos e insere na tabela do banco de dados
for item in data:
    values = [item['coluna1'], item['coluna2'], item['coluna3']]  # Substitua pelas colunas corretas da API
    placeholders = ','.join(['%s'] * len(values))
    sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.execute(sql, values)

# Realiza o commit e fecha a conexão com o banco de dados
conn.commit()
conn.close()

print("Importação concluída com sucesso!")
