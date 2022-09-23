import pandas as pd

novo_arquivo = pd.read_csv(filepath_or_buffer="novo_arquivo.csv",delimiter=";", header=1)

df_renomeado = novo_arquivo.rename(columns={'0':'coluna1','1':'coluna2','1.1':'coluna3'})

print(novo_arquivo)
print(df_renomeado)