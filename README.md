###### ├── API_EMULATOR
###### │   ├── api_emulator.py     ---- SIMULA UMA API, USADA EM UMA COMPUTE ENGINE
###### ├── IO_STEP                 ---- MEIOS DE ACESSAR BANCOS DE DADOS [ postgres, GCP ] , SFTP e BUCKETS, modulo usado para I/O Stream
###### │   ├── interface.py
###### │   ├── interface_bucket.py
###### │   ├── sftp_client.py
###### ├── SFTP_EMULATOR           ---- SIMULA UMA API, USADA EM UMA COMPUTE ENGINE
###### │   ├── ARQUIVO.CSV
###### |── settings.py
###### ├── cloud_functions          ---- FUNÇÕES PARA ETL
###### │   ├── extract_api.py
###### │   ├── extract_bucket_json.py
###### │   ├── extract_bucket_parquet.py
###### │   ├── extract_ftp.py
###### │   ├── extract_sql.py
###### │   ├── transform_bronze_to_silver_produtos.py
###### │   ├── transform_bronze_to_silver_vendas.py
###### ├── fles                    ---- ARQUIVOS PARA CRIAR SCHEMA E DADOS FICTICIOS AUTOMATICAMENTE
###### │   ├── data
###### │   │   ├── ARQUIVOS.JSON
###### │   ├── schemas
###### │   │   ├── ARQUIVOS.SQL
###### ├── procedures            ---- FUNÇÕES PARA CRIAR  SCHEMA E DADOS FICTICIOS AUTOMATICAMENTE
###### │   ├── create_data.py
###### │   ├── create_schema.py
###### ├── main.py              ---- ARQUIVO CRIAR PARA SCHEMA E DADOS FICTICIOS AUTOMATICAMENTE
