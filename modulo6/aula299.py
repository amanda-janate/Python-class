"""Variaveis de ambiente"""
# para terminal:
#   $env:SENHA="teste" -> define uma variavel de ambiente
#   dir env: -> lista todas as variaveis de ambiente

# import os

# senha = os.getenv('SENHA')

# print(senha)
import os
from dotenv import load_dotenv

load_dotenv()  # carregar arquivo .env da raiz do projeto

# print(os.environ)
print(os.getenv('DB_PASSWORD'))
