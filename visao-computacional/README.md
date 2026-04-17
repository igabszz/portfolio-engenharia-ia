# 👁️ Vision AI & OCR Inteligente (IDP)

Este módulo faz parte do meu portfólio de Engenharia de IA e foca na extração inteligente de dados de documentos não estruturados (IDP), atendendo aos requisitos de automação e visão computacional.

### 🛠️ Tecnologias e Modelos
* **Modelo:** Google Gemini 3 Flash (Multimodal).
* **Orquestração:** LangChain.
* **Processamento de Imagem:** Base64 Encoding e Pillow.

### 🚀 Funcionalidades
* **OCR Avançado:** Supera o OCR tradicional ao entender o contexto do documento, não apenas os caracteres.
* **Extração Estruturada:** Converte imagens de fichas cadastrais e relatórios técnicos diretamente em JSON.
* **Resiliência de Dados:** Tratamento de imagens complexas (incluindo assinaturas e metadados).

### 📋 Como Executar
1. Certifique-se de que o `.env` na raiz contém a `GOOGLE_API_KEY`.
2. Instale as dependências: `pip install Pillow python-dotenv langchain-google-genai`.
3. Execute: `python app_ocr.py`.