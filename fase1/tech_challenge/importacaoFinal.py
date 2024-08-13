import pandas as pd
import glob
import os

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Diretório onde os arquivos CSV estão localizados
#file_path = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dados\\'
file_path = os.getenv('PATH_DADOS_23')

# Padrão para encontrar os arquivos CSV que começam com "Exp"
padrao_arquivos = os.path.join(file_path, 'Imp*.csv')

# Lista para armazenar os novos dados
todos_dados = []

# Encontra todos os arquivos que correspondem ao padrão
arquivos_csv = glob.glob(padrao_arquivos)

# Itera sobre cada arquivo CSV encontrado
for arquivo_csv in arquivos_csv:
    print(f'Lendo o arquivo {arquivo_csv}')
    
    # Lê o arquivo CSV
    df = pd.read_csv(arquivo_csv, delimiter=';')
    
    # Itera sobre cada linha do dataframe
    for index, row in df.iterrows():
        classe = row['classe']
        pais = row['pais']
        
        # Itera sobre cada ano no dataframe
        for ano in range(1970, 2020):
            valor_col = f'valor_{ano}'
            kg_col = f'kg_{ano}'
            
            # Verifica se as colunas existem no dataframe
            if valor_col in df.columns and kg_col in df.columns:
                valor = row[valor_col]
                kg = row[kg_col]
                
                # Adiciona a nova linha de dados na lista
                todos_dados.append([classe, pais, ano, kg, valor])

# Cria um novo dataframe com os dados transformados
novo_df = pd.DataFrame(todos_dados, columns=['classe', 'pais', 'ano', 'kg', 'valor'])

# Converte a coluna 'ano' para o formato de data (primeiro dia do ano)
novo_df['ano'] = pd.to_datetime(novo_df['ano'], format='%Y')

# Salva o novo dataframe em um arquivo CSV
output_file_path = os.path.join(file_path+"\\final\\", 'ImportacaoFinal.csv')
novo_df.to_csv(output_file_path, index=False, sep=';')