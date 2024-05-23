# Automação: Obter dados de locais através do GoogleMaps
Este projeto automatiza a obtenção de dados de estabelecimentos comerciais utilizando o Google Maps. O script acessa uma base de dados em uma planilha no formato `.CSV`, mas também pode ser adaptado para outros formatos como `.XLSX`, `.parquet`, entre outros. Ele busca os estabelecimentos no Google Maps e coleta informações como Nome, Telefone, Endereço, Redes Sociais, WhatsApps, Site, Horário de Funcionamento, e informações adicionais como acessibilidade e tipos de cardápios. Após a coleta, os dados são armazenados em uma nova planilha.

## Funcionamento
O script identifica e coleta as informações desejadas através de TAGs HTML, reconhecendo padrões específicos no Google Maps. Se o código parar de funcionar devido a mudanças nas TAGs do Google Maps, basta inspecionar o site, encontrar a nova TAG correspondente e atualizar o código.

## Requisitos
* Python
* Pandas
* Playwright

## Como usar o script
### 1. Clonar o Repositório
Clone este repositório:
`git clone https://github.com/thiagodmagalhaes/GoogleMaps.git`

### 2. Instalar as Dependências
Navegue até a pasta do projeto e instale as bibliotecas necessárias:
 * `cd GoogleMaps`
 * `pip install playwright `
 * `pip install pandas`

### 3. Preparar os Dados
Vá até a pasta GoogleContats/app/dados. Nessa pasta, há um arquivo chamado `EMPRESAS_PESQUISA.csv` que contém duas colunas: `Nome` e `Endereço`. Altere os nomes e endereços para os estabelecimentos que deseja coletar informações e salve o arquivo.

**OBS.: O `NOME` E `ENDEREÇO` NA PLANILHA DEVEM ESTAR TODOS EM LETRAS MAIÚSCULA**


### 4. Executar o Script
Abra o terminal e navegue até a pasta `app`:
* `cd GoogleContats`
* `cd app`
  
Dentro da pasta app execute o comando: `python main.py`

O código será executado e você verá a execução através do navegador Chromium.

Após a execução os dados serãos salvos em uma nova planilha localizada na pasta `dados/qualificados/EMPRESAS_PESQUISA2.csv`

## Observações
* Este é um método programático para coletar dados de estabelecimentos comerciais. Certifique-se de seguir as políticas de uso do Google Maps.
* Caso precise atualizar as TAGs HTML, inspecione o site do Google Maps e ajuste o código conforme necessário.

