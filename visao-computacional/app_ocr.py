import os
import base64
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# 1. Configuração de ambiente (Busca na raiz)
load_dotenv(dotenv_path="../.env")
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Inicialização do Modelo
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", google_api_key=api_key)

def codificar_imagem(caminho_imagem):
    """Converte a imagem para Base64 para evitar erros de tipo."""
    with open(caminho_imagem, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def processar_ocr_inteligente(arquivo):
    if not os.path.exists(arquivo):
        print(f"❌ Arquivo {arquivo} não encontrado.")
        return

    # 3. Preparando os dados da imagem
    base64_image = codificar_imagem(arquivo)

    # 4. Prompt IDP (Foco na vaga da Kktech) [cite: 13]
    prompt = "Extraia os dados desta ficha cadastral para um JSON estruturado com os campos: nome, data, documento e resumo."

    # 5. Mensagem Multimodal Formatada corretamente
    mensagem = HumanMessage(
        content=[
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
            },
        ]
    )

    print(f"🚀 Processando {arquivo} com IA...")
    try:
        resposta = llm.invoke([mensagem])
        print("\n✅ JSON Extraído:")
        print(resposta.content)
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    processar_ocr_inteligente("teste_ficha_cadastral.jpg")