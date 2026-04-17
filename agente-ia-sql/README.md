# 🤖 AI-SQL-Agent: Interface em Linguagem Natural para Bancos de Dados

Este projeto implementa um **Agente de IA** capaz de traduzir perguntas em português para consultas SQL estruturadas, utilizando o modelo **Gemini 3 Flash**.

### 🚀 Funcionalidades
* **Text-to-SQL:** Converte linguagem natural em queries executáveis.
* **Segurança de Dados:** Gestão de credenciais via variáveis de ambiente (.env).
* **Interação Dinâmica:** Loop de perguntas e respostas via terminal.

### 🛠️ Tecnologias Utilizadas
* **Python** para automação e lógica de backend.
* **LangChain** para orquestração da LLM e do banco de dados.
* **Google Gemini 3 Flash** como motor de processamento de linguagem.
* **SQLite** para persistência e demonstração de dados relacionais.

### 📋 Pré-requisitos
1. Clone o repositório.
2. Crie um arquivo `.env` na raiz com sua `GOOGLE_API_KEY`.
3. Instale as dependências: `pip install -r requirements.txt`.

### 🛡️ Nota de Segurança
Como especialista em **Administração de Banco de Dados**, este agente foi configurado para operar em ambientes controlados. Em produção, recomenda-se o uso de credenciais com permissões de **Read-Only** para garantir a integridade dos dados.