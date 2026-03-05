import pandas as pd

df = pd.read_csv('clientes.csv')

#mostrar todas as colunas do DataFrame
pd.set_option('display.width', None)
print(df.head())

#Remover dados
df.drop(labels='pais', axis=1, inplace=True)  #coluna
df.drop(labels=2, axis=0, inplace=True)  #linha

# Normalizar campos de texto
df['nome'] = df['nome'].str.title()  

df['endereco'] = df['endereco'].str.lower() #tudo minúsculo

df['estado'] = df['estado'].str.upper() #tudo maiúsculo

# Converter tipos de dados
df['idade'] = df['idade'].astype(int)

print('Normalizar textos' , df.head())

#Tratar valores nulos
df_fillna = df.fillna(0)  #substituir por 0
df_dropna = df.dropna()  #remover linhas com valores nulos  
df_dropna4 = df.dropna(thresh=4)  #remover linhas com menos de 4 valores não nulos
df = df.dropna(subset=['cpf'])  #remover linhas onde a coluna 'cpf' tem valor nulo

print('Valores nulos: \n', df.isnull().sum())
print('qtd de registros nulos com filna: \n', df_fillna.isnull().sum())
print('qtd de registros nulos com dropna: \n', df_dropna.isnull().sum())
print('qtd de registros nulos com dropna4: \n', df_dropna4.isnull().sum())
print('qtd de registros nulos com CPF: \n', df.isnull().sum())

df.fillna(value={'estado': 'desconecido'}, inplace=True)  #substituir valores nulos na coluna 'estado' por 'desconecido'
df['endereço'] = df['endereco'].fillna('endereço não informado')  #substituir valores nulos na coluna 'endereco' por 'endereço não informado'
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())  #substituir valores nulos na coluna 'idade' pela média da coluna

#tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')  #converter a coluna 'data_nascimento' para formato datetime,

#Tratar dados duplicados
print('Qtd registros atual:' , df.shape[0])
df.drop_duplicates()  #remover linhas duplicadas
df.drop_duplicates(subset=['cpf'], inplace=True)  #remover linhas duplicadas com base na coluna 'cpf', mantendo a primeira ocorrência
print('Qtd registros após remover duplicados:' , len(df))

print('dados Limpos:\n', df)

#Salvar o DataFrame limpo em um novo arquivo CSV
df['data'] = df['data_corrigida']  #substituir a coluna 'data' pela coluna 'data_corrigida'
df['idade'] = df['idade_corrigida']  #substituir a coluna 'idade' pela coluna 'idade_corrigida'

df_salvar = df[['nome', 'cpf', 'data', 'idade', 'endereco', 'estado']]  #selecionar as colunas para salvar
df_salvar.to_csv('clientes_limpos.csv', index=False)

print('novo DataFrame: \n', pd.read_csv('clientes_limpos.csv'))

git init
git add .
git commit -m "Projeto de limpeza de dados de clientes em Python"
