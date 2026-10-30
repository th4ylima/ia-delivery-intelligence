
import pandas as pd
from pathlib import Path

# Localizar o arquivo de pedidos
PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_CSV = PASTA_PROJETO / "data" / "pedidos.csv"

# Ler os dados
df = pd.read_csv(ARQUIVO_CSV)

# Separar pedidos entregues e cancelados
entregues = df[df["status"] == "Entregue"]
cancelados = df[df["status"] == "Cancelado"]

# Calcular indicadores
total_pedidos = len(df)
total_entregues = len(entregues)
total_cancelados = len(cancelados)

faturamento = entregues["valor_pedido"].sum()
tempo_medio = entregues["tempo_entrega_min"].mean()

taxa_cancelamento = (
    total_cancelados / total_pedidos * 100
    if total_pedidos > 0 else 0
)

# Mostrar resultados
print("=" * 40)
print("  IA DELIVERY INTELLIGENCE")
print("  RELATORIO DE ANALISE")
print("=" * 40)

print(f"Total de pedidos: {total_pedidos}")
print(f"Pedidos entregues: {total_entregues}")
print(f"Pedidos cancelados: {total_cancelados}")
print(f"Faturamento dos pedidos entregues: R$ {faturamento:.2f}")
print(f"Tempo medio de entrega: {tempo_medio:.1f} minutos")
print(f"Taxa de cancelamento: {taxa_cancelamento:.1f}%")
