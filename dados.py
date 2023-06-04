import mysql.connector
import csv


# Conectar ao banco de dados
mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Criar objeto cursor
mycursor = mydb.cursor()

# Executar consulta SQL
mycursor.execute("SELECT Cidade, COUNT(*) AS Quantidade FROM posts GROUP BY Cidade")

# Obter resultados da consulta
results = mycursor.fetchall()

# Criar dicionário de mapeamento entre códigos do IBGE e nomes das cidades
municipios = {}
with open('municipios.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        codigo_ibge = row['COD']
        nome = row['NOME']
        municipios[codigo_ibge] = nome

# Função para mostrar quantas vezes cada cidade repetiu
def repeticoes():
    # Exibir resultados
    for row in results:
        codigo_ibge = row[0]
        nome_cidade = municipios.get(codigo_ibge)
        quantidade = row[1]
        print(f"{nome_cidade}: {quantidade} vezes")

# Função para mostrar o nome de todas as cidades que aparecem
def mostrar_cidades():
    cidades = []
    repeticoes = []
    for row in results:
        codigo_ibge = row[0]
        nome_cidade = municipios.get(codigo_ibge)
        if nome_cidade:
            cidades.append(f'{nome_cidade}')
            repeticoes.append(row[1])
    return cidades, repeticoes

# Chamada das funções
repeticoes()
print("---")
cidades_array, repeticoes_array = mostrar_cidades()
print(cidades_array)
print(repeticoes_array)
