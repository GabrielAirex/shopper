import requests
import pandas as pd
from IO_STEP import interface_bucket
import datetime
from dotenv import load_dotenv
import os

def main():
    api_url =   os.environ.get("api_url")

    response = requests.get(api_url)

    if response.status_code == 200:
        data = []
        events = response.json()
        print("Dados dos Eventos:")
        for event in events:
            data.append(event)
        df = pd.json_normalize(data)
        print(df)
        today = datetime.date.today()
        formatted_date = today.strftime('%Y-%m-%d')
        interface_bucket.Bucket_interface().output(df,'data_lake_desafio',f'analise_de_sentimentos/analise_de_sentimento_{formatted_date}','application/json')

    else:
        print("Falha na requisição:", response.status_code)

if __name__ == "__main__":
    main()