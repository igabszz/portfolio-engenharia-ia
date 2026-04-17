import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
# importação específica para o Google Gemini
from langchain_google_genai import ChatGoogleGenerativeAI

# carregar credenciais
load_dotenv(dotenv_path="../.env")
api_key = os.getenv("GOOGLE_API_KEY")

# conectar ao banco de dados SQLite (Seu lado DBA)
db = SQLDatabase.from_uri("sqlite:///vendas_corporativas.db")

# configurar a IA do Google (Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview", 
    google_api_key=api_key,
    temperature=0
)

# criar a corrente (chain) que faz o Text-to-SQL
# o verbose=True permite ver a query SQL sendo gerada no terminal
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

print("\n--- Agente de Dados (Gemini Edition) Ativo ---")
while True:
    pergunta = input("\nO que você deseja saber do banco? (ou 'sair'): ")
    if pergunta.lower() == 'sair':
        break
    try:
        # a IA vai ler sua pergunta, gerar o SQL e executar no SQLite
        resposta = db_chain.run(pergunta)
        print(f"\nResultado final: {resposta}")
    except Exception as e:
        print(f"Ocorreu um erro na interpretação: {e}")