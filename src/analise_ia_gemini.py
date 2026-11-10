
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from analista_ia import coletar_indicadores, criar_prompt


# Localização do projeto
PASTA_PROJETO = Path(__file__).resolve().parent.parent

# Carrega a chave da API
load_dotenv(PASTA_PROJETO / ".env")


def gerar_analise():
    """
    Coleta indicadores, envia para o Gemini,
    recebe a análise e salva o relatório.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "Chave GEMINI_API_KEY não encontrada no arquivo .env."
        )

    # Coleta os indicadores
    indicadores = coletar_indicadores()

    # Prepara o prompt
    prompt = criar_prompt(indicadores)

    # Conecta ao Gemini
    client = genai.Client(api_key=api_key)

    # Gera a análise
    resposta = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    analise = resposta.text

    if not analise:
        raise ValueError("O Gemini não retornou uma análise.")

    # Cria a pasta de relatórios, se necessário
    pasta_relatorios = PASTA_PROJETO / "reports"
    pasta_relatorios.mkdir(exist_ok=True)

    # Salva o relatório
    arquivo_relatorio = (
        pasta_relatorios / "analise_gemini.md"
    )

    with open(
        arquivo_relatorio,
        "w",
        encoding="utf-8"
    ) as arquivo:
        arquivo.write(
            "# Análise de Delivery com Inteligência Artificial\n\n"
        )
        arquivo.write(analise)

    return analise
