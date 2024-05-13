from IO_STEP import interface
from procedures import create_schema, create_data
import pandas as pd
import datetime
import os
from dotenv import load_dotenv

def main():
    conector = interface.Conectar(server= os.environ.get("server_gcp"),
                                bd= os.environ.get("bd_gcp")
    ).access()
    print(conector)
    

    today = datetime.date.today()
    formatted_date = today.strftime('%Y-%m-%d')

    df = pd.read_gbq(f'''
            SELECT 
    p.`ProdutoID`,
    p.`NomeProduto`,
    p.`DescriçãoProduto`,
    p.`Preço` AS `PreçoOriginal`,
    e.`LojaID`,
    e.`Quantidade` AS `QuantidadeEmEstoque`,
    ap.`NomeAtributo`,
    ap.`ValorAtributo`,
    pp.`average_price`,
    pp.`minimum_price`,
    pp.`maximum_price`,
    pp.`survey_date`,
    asen.`sentiment_label`,
    asen.`sentiment_score`,
    asen.`source`,
    asen.`text`,
    asen.`timestamp`
FROM 
    `airex-423021.data_warehouse_bronze.bronze_produtos` p
LEFT JOIN 
    `airex-423021.data_warehouse_bronze.bronze_estoque` e ON p.`ProdutoID` = e.`ProdutoID`
LEFT JOIN 
    `airex-423021.data_warehouse_bronze.bronze_atributosproduto` ap ON p.`ProdutoID` = ap.`ProdutoID`
LEFT JOIN 
    `airex-423021.data_warehouse_bronze.pesquisa_de_preço` pp ON p.`ProdutoID` = pp.`product_id`
LEFT JOIN 
    `airex-423021.data_warehouse_bronze.analise_de_sentimento` asen ON p.`ProdutoID` = asen.`product_id`


            ''',project_id='airex-423021',credentials=conector)
    print(df)   
    df['extract_day'] = formatted_date
    
    output = interface.Conectar(server='gcp').insert_gcp(df,'airex-423021','data_warehouse_silver',f'silver_produtos',False,os.environ.get('credential_gcp_path'))


    
if __name__ == "__main__":
      main()