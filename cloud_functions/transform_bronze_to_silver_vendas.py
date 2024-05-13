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
                rv.VendaID,
                rv.DataVenda,
                rv.Quantidade,
                c.Nome AS NomeCliente,
                c.Email AS EmailCliente,
                c.Telefone AS TelefoneCliente,
                c.`Endereço` AS EnderecoCliente,
                p.NomeProduto,
                p.`DescriçãoProduto`,
                p.`Preço` AS PrecoOriginal,
                pl.`PreçoEspecial`,
                pl.`CondiçõesEspeciais`,
                pl.Promocao,
                l.NomeLoja,
                l.`Descrição` AS DescricaoLoja,
                l.`EndereçoLoja`
            FROM 
                `airex-423021.data_warehouse_bronze.bronze_registrovendas` rv
            JOIN 
                `airex-423021.data_warehouse_bronze.bronze_clientes` c ON rv.ClienteID = c.ClienteID
            JOIN 
                `airex-423021.data_warehouse_bronze.bronze_produtos` p ON rv.ProdutoID = p.ProdutoID
            JOIN 
                `airex-423021.data_warehouse_bronze.bronze_lojas` l ON rv.LojaID = l.LojaID
            JOIN 
                `airex-423021.data_warehouse_bronze.bronze_produtoslojas` pl ON rv.ProdutoID = pl.ProdutoID AND rv.LojaID = pl.LojaID

            ''',project_id='airex-423021',credentials=conector)
    print(df)   
    df['extract_day'] = formatted_date
    output = interface.Conectar(server='gcp').insert_gcp(df,'airex-423021','data_warehouse_silver',f'silver_registro_vendas',False,os.environ.get('credential_gcp_path'))


    
if __name__ == "__main__":
      main()