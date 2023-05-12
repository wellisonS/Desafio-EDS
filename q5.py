import csv
import psycopg2

# Configurações de conexão com o banco de dados
database = "nome_do_banco"  # Nome do banco de dados
user = "usuario"  # Usuário do banco de dados
password = "senha"  # Senha do banco de dados
host = "localhost"  # Endereço do servidor do banco de dados
port = "5432"  # Porta do servidor do banco de dados

# Nome do arquivo CSV a ser importado
csv_file = "caminho/arquivo.csv"

# Nome da tabela no schema de staging
table_name = "nome_da_tabela"

# Estabelece a conexão com o banco de dados
conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

# Abre o arquivo CSV e realiza a importação para a tabela
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Pula o cabeçalho do arquivo CSV
    for row in reader:
        # Insere cada linha do arquivo CSV na tabela do banco de dados
        sql = f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(row))})"
        cursor.execute(sql, row)

# Realiza o commit e fecha a conexão com o banco de dados
conn.commit()
conn.close()

print("Importação concluída com sucesso!")



