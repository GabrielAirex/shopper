from IO_STEP import interface_bucket,interface
import pandas as pd
import datetime
from dotenv import load_dotenv
import os

def main():
    today = datetime.date.today()
    formatted_date = today.strftime('%Y-%m-%d')
    df = interface_bucket.Bucket_interface().input('data_lake_desafio',f'analise_de_sentimentos/analise_de_sentimento_{formatted_date}',"json")
    df['extract_day'] = formatted_date

    df.columns = [col.replace('.', '_') for col in df.columns]
    print(df)
    io = interface.Conectar(server='gcp').insert_gcp(df,'airex-423021','data_warehouse_bronze','analise_de_sentimento',False,os.environ.get('credential_gcp_path'))



if __name__ == "__main__":
    main()