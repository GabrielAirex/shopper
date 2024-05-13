from IO_STEP import interface
from procedures import create_schema, create_data
import pandas as pd
import datetime
from dotenv import load_dotenv
import os

def main():
    io = interface.Conectar(server= os.environ.get("server_postgres"),
                            bd= os.environ.get("bpostgres")
)
    conn,cur = io.access(   user = os.environ.get("user_postgres"),
                            password = os.environ.get("password_postgres"),
                            host =  os.environ.get("host_postgres"),
                            port = os.environ.get("port_postgres"))
    
    list_of_schemas = ['clientes','produtos','lojas','produtoslojas','estoque','registrovendas','atributosproduto']
    today = datetime.date.today()
    formatted_date = today.strftime('%Y-%m-%d')
    for table in list_of_schemas:
        df = pd.read_sql(f"SELECT * FROM public.{table} ", conn)
        print(df)   
        df['extract_day'] = formatted_date
        output = interface.Conectar(server='gcp').insert_gcp(df,'airex-423021','data_warehouse_bronze',f'bronze_{table}',False,os.environ.get('credential_gcp_path'))


    
if __name__ == "__main__":
      main()