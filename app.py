
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com as mensagens dos níveis do reservatório
niveis = [
    "Nivel 1 - Muito baixo (CRITICO)",
    "Nivel 2 - Baixo",
    "Nivel 3 - Medio",
    "Nivel 4 - Alto",
    "Nivel 5 - Muito alto (ALERTA)"
]

# Função para definir a cor de cada nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Função para exibir a situação do reservatório
def exibir_situacao(nivel):
    if 1 <= nivel <= len(niveis):
        cor = definir_cor(nivel)
        print(cor + niveis[nivel - 1] + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Nivel invalido!" + Style.RESET_ALL)

# Programa principal
print("=== MONITORAMENTO DO RESERVATORIO ===\n")

# Simulação das leituras do reservatório
leituras = [3, 2, 1, 2, 3, 4, 5]

for numero, nivel in enumerate(leituras, start=1):
    print(f"Leitura {numero}: ", end="")
    exibir_situacao(nivel)
