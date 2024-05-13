import pandas as pd
from io import StringIO, BytesIO
from google.cloud import storage
import pyarrow.parquet as pq
from IO_STEP import sftp_client
from IO_STEP import interface_bucket
import datetime
from dotenv import load_dotenv
import os


def main():
    hostname =  os.environ.get("host_sftp")  
    port = os.environ.get("port_sftp")                        
    username = os.environ.get("user_sftp")    
    password =  os.environ.get("user_password")          
    print("iniciado o script")
    today = datetime.date.today()
    formatted_date = today.strftime('%Y-%m-%d')
    file_path = f'/home/gabrielafonsofreitas/SFTP_EMULATOR/Marketplace_Price_Survey_{formatted_date}.csv'

    sftp = sftp_client.sftp_connection(hostname, username,  os.environ.get('key_ssh_path'), port)

    print("Conectado")
    with sftp.open(file_path, mode='r') as file_handle:
        csv_data = file_handle.read()

    csv_str = csv_data.decode('utf-8')

    data = StringIO(csv_str)
    df = pd.read_csv(data)
    #print(df)
    sftp.close()
    today = datetime.date.today()
    formatted_date = today.strftime('%Y-%m-%d')
    interface_bucket.Bucket_interface().output(df,'data_lake_desafio',f'pesquisas_de_precos/pesquisa_de_preco_{formatted_date}','application/octet-stream')

    #df = interface_bucket.Bucket_interface().input('data_lake_desafio','csv_parket')
    print(df)

if __name__ == "__main__":
    main()