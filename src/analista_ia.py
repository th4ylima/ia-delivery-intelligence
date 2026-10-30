
import pandas as pd
from pathlib import Path

# Localizar a base de dados
PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_CSV = PASTA_PROJETO / "data" / "pedidos.csv"


def coletar_indicadores():
    """Calcula indicadores a partir dos pedidos entregues."""

    df = pd.read_csv(ARQUIVO_CSV)

    entregues = df[df["status"] == "Entregue"]
    cancelados = df[df["status"] == "Cancelado"]

    total = len(df)

    indicadores = {
        "total_pedidos": total,
        "pedidos_entregues": len(entregues),
        "pedidos_cancelados": len(cancelados),
        "faturamento_entregues": round(
            float(entregues["valor_pedido"].sum()), 2
        ),
        "tempo_medio_entrega": round(
            float(entregues["tempo_entrega_min"].mean()), 1
        ) if len(entregues) > 0 else None,
        "taxa_cancelamento": round(
            len(cancelados) / total * 100, 1
        ) if total > 0 else 0,
    }

    return indicadores


def criar_prompt(indicadores):
    """Prepara instruções para uma IA analisar os indicadores."""

    prompt = f"""
Você é um analista de operações de delivery.

Analise os seguintes indicadores de pedidos fictícios:

- Total de pedidos: {indicadores['total_pedidos']}
- Pedidos entregues: {indicadores['pedidos_entregues']}
- Pedidos cancelados: {indicadores['pedidos_cancelados']}
- Faturamento dos pedidos entregues: R$ {indicadores['faturamento_entregues']:.2f}
- Tempo médio de entrega: {indicadores['tempo_medio_entrega']} minutos
- Taxa de cancelamento: {indicadores['taxa_cancelamento']}%

Responda em português, seguindo esta estrutura:
1. Resumo dos resultados.
2. Pontos que merecem atenção.
3. Recomendações práticas.
4. Limitações da análise.

Regras:
- Não invente dados nem causas que não foram demonstradas.
- Diferencie fatos de hipóteses.
- Informe que a amostra é pequena.
- Não afirme que uma causa foi comprovada sem evidências.
"""

    return prompt.strip()


if __name__ == "__main__":
    indicadores = coletar_indicadores()
    prompt = criar_prompt(indicadores)

    print("=" * 50)
    print("IA DELIVERY INTELLIGENCE")
    print("INDICADORES CALCULADOS")
    print("=" * 50)

    for nome, valor in indicadores.items():
        print(f"{nome}: {valor}")

    print("\nPROMPT PREPARADO PARA A IA:")
    print("-" * 50)
    print(prompt)
