import pandas as pd
from glob import glob
import os
import re

class Criar_data:
    def __init__(self,io):

        self.io = io
        

    def play(self):
        all_json_files = [file
                      for path, subdir, files in os.walk('/home/aires/desafio_shopper/files/data')
                      for file in glob(os.path.join(path, '*.json'))]
        all_json_files = sorted(all_json_files)
        print(all_json_files)

        for json_file in all_json_files:
                with open(json_file,'r') as arq_json:
                    json_data = arq_json.read()
                df= pd.read_json(json_data)
                print(df)
                vetor_upload = df.values.tolist()
                tabela = re.findall(r'DATA_([^\.]+)\.json', json_file)[0].lower()
                try:
                    self.io.insert( database = 'postgres'
                                ,schema = 'public'
                                ,table = tabela
                                ,data_upload = vetor_upload
                                ,columns = df.columns
                                ,truncate_table= False)
                except:
                     pass
