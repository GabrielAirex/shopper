import psycopg2
from google.oauth2 import service_account
from google.cloud import bigquery
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os

class Conectar:
    def __init__(self,server='',bd='',user='',password='',host='',port=''):
        self.connection = None
        self.cursor = None
        self.server = server
        self.banco = bd
        self.host = host
        self.port = port
        self.database = None
        self.user = user
        self.password = password
    def insert(self,database, schema, table, data_upload, columns, truncate_table=True):
            self.database = database
            print(self.host, self.port, self.database, self.user, self.password)
            string=f"host={self.host} dbname={self.database} user={self.user} password={self.password} port = {self.port}"
            print(string)

            if self.server == 'Postgres':
                self.connection =psycopg2.connect(host=f'{self.host}', database=f'{self.database}',user=f'{self.user}', password=f'{self.password}', port =f'{self.port}')
                print("cursor gerado")  
            self.database = database
            self.schema = schema
            self.table = table
            self.data_upload = data_upload
            self.columns = columns
            self.if_exist = truncate_table
            self.cursor = self.connection.cursor()

            self.table_path = self.schema + "." + self.table
            print(self.columns)
            self.create_table(self.table_path, self.columns)

            if truncate_table:
                self.truncate_table(self.table_path)

            dataset_size = len(self.data_upload)
            print(f"Inserindo {dataset_size} linhas.")

            columns_string = ','.join(self.columns)
            query = f"INSERT INTO {self.table_path} ({columns_string}) VALUES %s"
            execute_values(self.cursor, query, self.data_upload)
            self.connection.commit()
            print("Dados inseridos.")
    def create_table(self, table_path, columns, data_size=1000):
            print("Criando tabela, se necessário.")
            query = f"CREATE TABLE IF NOT EXISTS {table_path} (" + f" varchar({data_size}), ".join(
                columns) + f" varchar({data_size})) ;"
            self.cursor.execute(query)
            self.connection.commit()

    def truncate_table(self, table_path):
            print("Limpando tabela.")
            query = f"TRUNCATE TABLE {table_path}"
            self.cursor.execute(query)
            self.connection.commit()

    def close_connection(self):
        print("Fechando conexão")
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        
        
    def access(self,user ='', password='', host='', port='', database='',dns ='',charset='',return_con = True,key=''):
        self.user = user
        self.password = password
        self.port = port
        self.host = host
        self.database = database
        self.dns = dns
        self.charset =charset
        self.return_con = return_con
        self.key=key


        if self.server == 'Postgres':
            
            self.connection =psycopg2.connect(host=f'{self.host}', database=f'{self.database}',user=f'{self.user}', password=f'{self.password}', port =f'{self.port}')
            print("cursor gerado")
            self.cursor = self.connection.cursor()
            conn = [self.connection,self.cursor]
           
            if return_con:
                return conn
        if self.server == 'gcp':
            self.key = key
            self.key = os.environ.get('credential_gcp_path')
            CREDS = service_account.Credentials.from_service_account_file(self.key)
            self.connection = bigquery.Client(credentials=CREDS, project=CREDS.project_id)
            if return_con:
                return CREDS


    def insert_gcp(self,df,banco,schema,tabela,truncate_table=True,key=''):
        self.key = key
        self.truncate_table = truncate_table
        self.df = df
        CREDS = service_account.Credentials.from_service_account_file(self.key)
        self.banco = banco
        self.connection = bigquery.Client(credentials=CREDS, project=CREDS.project_id)
        print(self.connection)
        self.schema = schema
        self.tabela = tabela
        self.table_id = f'{self.banco}.{self.schema}.{self.tabela}'
        
        if truncate_table:
               job_config = bigquery.LoadJobConfig(
                source_format=bigquery.SourceFormat.CSV,
                autodetect=True,
                write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
    )
        else:
               job_config = bigquery.LoadJobConfig(
                source_format=bigquery.SourceFormat.CSV,
                autodetect=True,
                write_disposition = bigquery.WriteDisposition.WRITE_APPEND,
            )
        client = self.connection
        client.load_table_from_dataframe(self.df, self.table_id, job_config=job_config)
