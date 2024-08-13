import pandas as pd
import os

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Caminho para o arquivo CSV
file_path = os.getenv('PATH_DADOS_BRUTOS_23')+"ProcessaMesa.csv"
new_file_path = os.getenv('PATH_DADOS_23')

# Carregar o arquivo CSV sem cabeçalho, usando ";" como delimitador
df = pd.read_csv(file_path, header=0, delimiter=';')

# Adicionar a nova coluna "classe" na segunda posição
def classify(row):
    classificacao = row['control']
    if classificacao.startswith('ti_'):
        return 'TINTAS'
    elif classificacao.startswith('br_'):
        return 'BRANCAS'
    else:
        return None

df['classe'] = df.apply(classify, axis=1)

# Remover linhas onde a coluna "classe" é None
df = df.dropna(subset=['classe'])

# Reorganizar as colunas para que "classe" esteja na segunda posição
cols = df.columns.tolist()
cols.insert(1, cols.pop(cols.index('classe')))
df = df[cols]

# Salvar o dataframe com o novo cabeçalho
output_path = new_file_path + 'ProcessaMesa.csv'
df.to_csv(output_path, index=False, sep=';')

print(f'Arquivo salvo como {output_path}')
