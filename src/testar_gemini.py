import os
from dotenv import load_dotenv
from google import genai

# Carrega a chave armazenada no arquivo .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("[ERRO] Chave da API não encontrada.")
else:
    try:
        client = genai.Client(api_key=api_key)

        resposta = client.models.generate_content(
            model="gemini-3.8-flash",
            contents="Responda apenas: Conexão com a Gemini API realizada com sucesso!"
        )

        print("\n[SUCESSO] Resposta da inteligência artificial:")
        print(resposta.text)

    except Exception as erro:
        print("\n[ERRO] Não foi possível conectar à Gemini API.")
        print(erro)