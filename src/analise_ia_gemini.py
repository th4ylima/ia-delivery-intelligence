import os
from dotenv import load_dotenv
from google import genai

from analista_ia import coletar_indicadores, criar_prompt

# Carrega a chave protegida
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("[ERRO] Chave da API não encontrada.")
    raise SystemExit

try:
    # Coleta os indicadores do projeto
    indicadores = coletar_indicadores()

    # Prepara o prompt para a IA
    prompt = criar_prompt(indicadores)

    # Conecta à Gemini
    client = genai.Client(api_key=api_key)

    print("\nEnviando indicadores para a inteligência artificial...")

    resposta = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    print("\n========== ANÁLISE DA IA ==========\n")
    print(resposta.text)

    # Salva a análise em um relatório
    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/analise_gemini.md",
        "w",
        encoding="utf-8"
    ) as arquivo:
        arquivo.write("# Análise de Delivery com Inteligência Artificial\n\n")
        arquivo.write(resposta.text)

    print("\n[OK] Relatório salvo em reports/analise_gemini.md")

except Exception as erro:
    print("\n[ERRO] Não foi possível realizar a análise.")
    print(erro)