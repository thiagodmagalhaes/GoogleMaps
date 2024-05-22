import pandas as pd 
from Google import GoogleMaps



# Carregando a planilha e armazenando em "dados"
dados = pd.read_csv(r"dados\EMPRESAS_PESQUISA.csv", sep=";", encoding='utf-8', dtype=str)

# Montando os dados em um DataFrame
df = pd.DataFrame(dados)
df = df.dropna(subset=["NOME FANTASIA"])

# contador para salvar as alterações em um determinado período
contador = 0
estabelecimentos=[]

# Para cada Informação dentro de dados pesquise no google maps.
for info in df.values:
    
    # Verificando Endereço.
    print("Verificando dados de:\n", info[0], info[1])
    
    try:
        dados_geolocalizacao = GoogleMaps.buscar_geolocalizacao(info[0], info[1])
        print(dados_geolocalizacao)
        
        if dados_geolocalizacao !=  None:
            estabelecimentos.append(dados_geolocalizacao)
        else:
            pass
        
        print(estabelecimentos)
        
        # Salvando os dados em um arquivo CSV
        #if(contador % 10 == 0):
        pd.DataFrame(estabelecimentos).to_csv(r"dados\qualificados\EMPRESAS_PESQUISA2.csv", sep=";", index=False)
        
        print("sucesso")
        
    except Exception as e:
        print(e)


