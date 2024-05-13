from IO_STEP import interface_bucket,interface
import pandas as pd
import datetime
from dotenv import load_dotenv
import os

def main():
    today = datetime.date.today()
    formatted_date = today.strftime('%Y-%m-%d')
    df = interface_bucket.Bucket_interface().input('data_lake_desafio',f'pesquisas_de_precos/pesquisa_de_preco_{formatted_date}',"parquet")
    df['extract_day'] = formatted_date
    io = interface.Conectar(server='gcp').insert_gcp(df,'airex-423021','data_warehouse_bronze','pesquisa_de_preço',True,os.environ.get('credential_gcp_path'))



if __name__ == "__main__":
    main()