
import os
from glob import glob





class Criar_schemas:
    def __init__(self,all,io,cherry_pick = False, schemas = []):
        self.all = all
        self.cherry_pick = cherry_pick
        self.schemas = schemas
        self.conn,self.cur = io.access(

                            user = 'postgres',
                            password = 'Yzs0({8uXK)-zz=d',
                            host = '35.232.71.116',
                            port = '5432')

    def play(self):

        if self.all:

            all_sql_files = [file
                      for path, subdir, files in os.walk('/home/aires/desafio_shopper/files/schemas')
                      for file in glob(os.path.join(path, '*.SQL'))]
            all_sql_files = sorted(all_sql_files)
            print(all_sql_files)
            
            for sql_file in all_sql_files:
                try:
                    with open(sql_file,'r') as arq_sql:
                        create_table = arq_sql.read()
                    print(create_table)
                    self.cur.execute(create_table)
                    self.conn.commit()
                except:
                    pass

        print("Todos os schemas foram criados")





   