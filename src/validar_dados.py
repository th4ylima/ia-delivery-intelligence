
import pandas as pd
from pathlib import Path

# Localizar a base de pedidos
PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_CSV = PASTA_PROJETO / "data" / "pedidos.csv"

df = pd.read_csv(ARQUIVO_CSV)

print("=" * 45)
print(" IA DELIVERY INTELLIGENCE")
print(" VERIFICACAO DA QUALIDADE DOS DADOS")
print("=" * 45)

problemas = 0

# 1. Verificar valores ausentes
valores_ausentes = int(df.isnull().sum().sum())

if valores_ausentes > 0:
    print(f"[ALERTA] Existem {valores_ausentes} valores ausentes.")
    problemas += 1
else:
    print("[OK] Nenhum valor ausente encontrado.")

# 2. Verificar pedidos duplicados
duplicados = int(df["pedido_id"].duplicated().sum())

if duplicados > 0:
    print(f"[ALERTA] Existem {duplicados} IDs de pedidos duplicados.")
    problemas += 1
else:
    print("[OK] Nenhum ID de pedido duplicado.")

# 3. Verificar valores de pedidos
valores_invalidos = int((df["valor_pedido"] <= 0).sum())

if valores_invalidos > 0:
    print(f"[ALERTA] Existem {valores_invalidos} valores de pedido inválidos.")
    problemas += 1
else:
    print("[OK] Todos os valores de pedido são positivos.")

# 4. Verificar status
status_validos = {"Entregue", "Cancelado"}
status_invalidos = int((~df["status"].isin(status_validos)).sum())

if status_invalidos > 0:
    print(f"[ALERTA] Existem {status_invalidos} status desconhecidos.")
    problemas += 1
else:
    print("[OK] Todos os status são reconhecidos.")

print("-" * 45)

if problemas == 0:
    print("RESULTADO: Nenhum problema detectado nas verificacoes.")
else:
    print(f"RESULTADO: {problemas} tipo(s) de problema detectado(s).")

print(f"Total de registros analisados: {len(df)}")
