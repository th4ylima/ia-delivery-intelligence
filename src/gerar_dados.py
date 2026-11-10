
import random
from pathlib import Path

import pandas as pd


# =====================================================
# CONFIGURAÇÕES
# =====================================================

PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_DADOS = PASTA_PROJETO / "data"
ARQUIVO_CSV = PASTA_DADOS / "pedidos.csv"

TOTAL_NOVOS_PEDIDOS = 300
ID_INICIAL = 1006

random.seed(42)


# =====================================================
# GERAÇÃO DOS PEDIDOS SINTÉTICOS
# =====================================================

def gerar_pedido(pedido_id):

    restaurantes = [
        "Burger House",
        "Pizza Central",
        "Sushi Express",
        "Taco Mex",
        "Green Food",
        "Chicken House"
    ]

    restaurante = random.choice(restaurantes)

    faixas_precos = {
        "Burger House": (25, 75),
        "Pizza Central": (35, 100),
        "Sushi Express": (45, 120),
        "Taco Mex": (20, 65),
        "Green Food": (25, 70),
        "Chicken House": (25, 80)
    }

    valor_minimo, valor_maximo = faixas_precos[restaurante]

    valor_pedido = round(
        random.uniform(valor_minimo, valor_maximo), 2
    )

    tempo_entrega = random.randint(20, 75)

    status = random.choices(
        ["Entregue", "Cancelado"],
        weights=[85, 15],
        k=1
    )[0]

    return {
        "pedido_id": pedido_id,
        "restaurante": restaurante,
        "valor_pedido": valor_pedido,
        "tempo_entrega_min": tempo_entrega,
        "status": status
    }


# =====================================================
# EXECUÇÃO
# =====================================================

def gerar_dados():

    PASTA_DADOS.mkdir(
        parents=True,
        exist_ok=True
    )

    if ARQUIVO_CSV.exists():

        df_existente = pd.read_csv(ARQUIVO_CSV)

        print(
            f"Base atual encontrada: {len(df_existente)} pedidos."
        )

    else:

        df_existente = pd.DataFrame(
            columns=[
                "pedido_id",
                "restaurante",
                "valor_pedido",
                "tempo_entrega_min",
                "status"
            ]
        )

    pedidos_existentes = set(
        pd.to_numeric(
            df_existente["pedido_id"],
            errors="coerce"
        ).dropna().astype(int)
    )

    novos_pedidos = []

    for pedido_id in range(
        ID_INICIAL,
        ID_INICIAL + TOTAL_NOVOS_PEDIDOS
    ):

        if pedido_id not in pedidos_existentes:
            novos_pedidos.append(
                gerar_pedido(pedido_id)
            )

    if novos_pedidos:

        df_novos = pd.DataFrame(novos_pedidos)

        df_final = pd.concat(
            [df_existente, df_novos],
            ignore_index=True
        )

        df_final.to_csv(
            ARQUIVO_CSV,
            index=False,
            encoding="utf-8-sig"
        )

        print(
            f"{len(novos_pedidos)} novos pedidos adicionados."
        )

    else:

        df_final = df_existente

        print(
            "Os 300 pedidos adicionais já foram gerados."
        )

    print("\nRESUMO DA BASE")
    print("-----------------------------")
    print(f"Total de pedidos: {len(df_final)}")
    print(f"Restaurantes: {df_final['restaurante'].nunique()}")
    print("\nPedidos por status:")
    print(df_final["status"].value_counts())
    print("-----------------------------")
    print(f"\nArquivo salvo em: {ARQUIVO_CSV}")


if __name__ == "__main__":
    gerar_dados()
