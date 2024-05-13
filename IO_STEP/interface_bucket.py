from google.cloud import storage
import pyarrow.parquet as pq
from io import BytesIO
import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account
import json
from dotenv import load_dotenv
import os

class Bucket_interface:
    def __init__(self):
        credentials_path = os.environ.get('credential_gcp_path')
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)

    def output(self,df,bucket_name,destination_blob_name, content_type):
        self.df = df
        self.content_type = content_type
        self.bucket_name = bucket_name
        self.destination_blob_name =  destination_blob_name
        if self.content_type == 'application/octet-stream':
            parquet_buffer = BytesIO()
            self.df.to_parquet(parquet_buffer, index=False, engine='pyarrow')
            storage_client = storage.Client(credentials= self.credentials)
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_string(parquet_buffer.getvalue(), content_type=self.content_type)
        if self.content_type == 'application/json':
            modified_json = self.df.to_json(orient='records')
            storage_client = storage.Client(credentials=self.credentials)
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_string(modified_json, content_type= self.content_type)



 

    def input (self,bucket_name,destination_blob_name,arq_type):
        if arq_type == "parquet":
            storage_client = storage.Client(credentials= self.credentials)
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)
            buffer = BytesIO()
            blob.download_to_file(buffer)
            buffer.seek(0)  
            dataframe = pd.read_parquet(buffer)
            return dataframe
        if arq_type == "json":
            storage_client = storage.Client(credentials= self.credentials)
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)
            json_string = blob.download_as_text()
            json_data = json.loads(json_string)
            df = pd.json_normalize(json_data)
            return df








