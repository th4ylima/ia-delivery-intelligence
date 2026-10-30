
import pandas as pd
from pathlib import Path

# Caminho da pasta principal do projeto
PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_DADOS = PASTA_PROJETO / "data"
ARQUIVO_CSV = PASTA_DADOS / "pedidos.csv"

# Criar a pasta de dados, caso não exista
PASTA_DADOS.mkdir(parents=True, exist_ok=True)

# Dados fictícios para nosso projeto
pedidos = [
    {
        "pedido_id": 1001,
        "restaurante": "Burger House",
        "valor_pedido": 45.90,
        "tempo_entrega_min": 32,
        "status": "Entregue"
    },
    {
        "pedido_id": 1002,
        "restaurante": "Pizza Central",
        "valor_pedido": 68.50,
        "tempo_entrega_min": 55,
        "status": "Entregue"
    },
    {
        "pedido_id": 1003,
        "restaurante": "Sushi Express",
        "valor_pedido": 72.00,
        "tempo_entrega_min": 48,
        "status": "Cancelado"
    },
    {
        "pedido_id": 1004,
        "restaurante": "Burger House",
        "valor_pedido": 39.90,
        "tempo_entrega_min": 28,
        "status": "Entregue"
    },
    {
        "pedido_id": 1005,
        "restaurante": "Pizza Central",
        "valor_pedido": 54.00,
        "tempo_entrega_min": 62,
        "status": "Entregue"
    },
]

df = pd.DataFrame(pedidos)

# Salvar os dados em um arquivo CSV
df.to_csv(ARQUIVO_CSV, index=False, encoding="utf-8-sig")

print("Base de pedidos criada com sucesso!")
print(f"Arquivo salvo em: {ARQUIVO_CSV}")
print(f"Quantidade de pedidos: {len(df)}")
print("\nPrévia dos dados:")
print(df.to_string(index=False))