from IO_STEP import interface
from procedures import create_schema, create_data
from dotenv import load_dotenv
import os
import pandas as pd


def main ():
    print("Main iniciada")
    load_dotenv()
    io = interface.Conectar(server= os.environ.get("server_postgres"),
                            bd= os.environ.get("bpostgres"),
                            user = os.environ.get("user_postgres"),
                            password = os.environ.get("password_postgres"),
                            host = os.environ.get("host_postgres"),
                            port = os.environ.get("port_postgres"))

    create_schema.Criar_schemas(all = True, io = io).play() 
    create_data.Criar_data(io).play()

if __name__ == "__main__":
      main()