
import subprocess
import sys
from pathlib import Path

# Identificar a pasta do projeto
PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_SRC = PASTA_PROJETO / "src"

# Scripts que serão executados
scripts = [
    "gerar_dados.py",
    "validar_dados.py",
    "analisar_dados.py",
]

print("=" * 45)
print(" IA DELIVERY INTELLIGENCE")
print(" PIPELINE AUTOMATIZADO")
print("=" * 45)

for nome_script in scripts:
    caminho_script = PASTA_SRC / nome_script

    print(f"\nExecutando: {nome_script}")

    resultado = subprocess.run(
        [sys.executable, str(caminho_script)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if resultado.returncode != 0:
        print(f"ERRO ao executar {nome_script}:")
        print(resultado.stderr)
        sys.exit(resultado.returncode)

    print(resultado.stdout)

print("\nPipeline concluído com sucesso!")