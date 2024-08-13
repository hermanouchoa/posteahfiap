import pandas as pd
import os

from unidecode import unidecode # pip install Unidecode
from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Caminho para o arquivo CSV
file_path = os.getenv('PATH_DADOS_BRUTOS_23')
new_file_path = os.getenv('PATH_DADOS_23')

mapeamento_pais = {
    "Alemanha, Republica Democratica": "Alemanha",
    "Alemanha, Republica Democratica da": "Alemanha",
    "Cayman, Ilhas": "Ilhas Cayman",
    "Coreia do Sul, Republica da": "Coreia do Sul",
    "Coreia,  Republica Sul": "Coreia do Sul",
    "Coreia, Republica Sul": "Coreia do Sul",
    "Dominica, Ilha de": "Ilha de Dominica",
    "Eslovaca,  Republica": "Republica Eslovaca",
    "Falkland (Malvinas)": "Falkland (Ilhas Malvinas)",
    "Marshall, Ilhas": "Ilhas Marshall",
    "Russia,  Federacao da": "Russia",
    "Taiwan (FORMOSA)": "Taiwan (Formosa)",
    "Tcheca, Republica": "Republica Tcheca",
    "Tcheca,  Republica": "Republica Tcheca",
    "Turcas e Caicos, ilhas": "Ilhas Turcas e Caicos",
    "Coreia do Norte, Republica": "Coreia do Norte",
    "Coreia do Sul, Republica": "Coreia do Sul",
    "italia": "Italia",
    "Cocos (Keeling), Ilhas": "Ilhas Cocos (Keeling)"
}

# Mapeamento de arquivos para a classe
mapeamento_classe = {
    "ExpEspumantes.csv": "Espumantes",
    "ExpSuco.csv": "Suco de Uva",
    "ExpUva.csv": "Uvas Frescas",
    "ExpVinho.csv": "Vinhos de Mesa"
}

arquivos_com_prefixo = []
for arquivo in os.listdir(file_path):
    if arquivo.startswith("Exp") and arquivo.endswith('.csv'):
        arquivos_com_prefixo.append(arquivo)
        print("file")
        print(arquivo)

        # Carregar o arquivo CSV sem cabeçalho, usando ";" como delimitador
        df = pd.read_csv(file_path + arquivo, header=0, delimiter=';')
    
        # Contar o número de colunas
        num_columns = df.shape[1]

        # Ajustar o cabeçalho com base no número de pares "kg, valor"
        num_pairs = (num_columns - 2) // 2
        header = ['index', 'pais']
        
        for year in range(1970, 1970 + num_pairs):
            header.append(f'kg_{year}')
            header.append(f'valor_{year}')
        
        # Adicionar o cabeçalho ao dataframe
        df.columns = header

        # Remover aspas e caracteres especiais
        for column in df.columns:
            df[column] = df[column].map(lambda x: unidecode(str(x)).replace('"', '').replace("'", ''))

        # Ajustar os valores da coluna "pais"
        df['pais'] = df['pais'].replace(mapeamento_pais)

        # Adicionar a coluna 'classe' com base no nome do arquivo
        df['classe'] = mapeamento_classe.get(arquivo, 'Desconhecido')

        # Reorganizar as colunas para que 'classe' seja a segunda
        cols = ['index', 'classe', 'pais'] + header[3:]
        df = df[cols]

        # Salvar o dataframe com o novo cabeçalho
        output_path = new_file_path + arquivo
        df.to_csv(output_path, index=False, sep=';')

        print(f'Arquivo salvo como {output_path}')
