"""
Atividade: Controle de Níveis de Água
Descrição: Simulação de monitoramento de reservatório de água utilizando
           a biblioteca colorama para destacar níveis de alerta.
"""

from colorama import Fore, Style, init

# Inicializa o colorama (compatibilidade garantida em todos os SOs)
init(autoreset=True)


def obter_cor_e_alerta(nivel):
    """
    Função responsável por retornar a cor (Colorama) e a descrição do alerta
    de acordo com o nível informado do reservatório.
    """
    if nivel == 1:
        return Fore.RED, "Muito baixo (crítico)"
    elif nivel == 2:
        return Fore.YELLOW, "Baixo"
    elif nivel == 3:
        return Fore.GREEN, "Médio"
    elif nivel == 4:
        return Fore.CYAN, "Alto"
    elif nivel == 5:
        return Fore.BLUE, "Muito alto (alerta)"
    else:
        return Fore.WHITE, "Nível desconhecido"


def monitorar_reservatorio():
    """
    Função principal que simula a leitura e exibição dos níveis do reservatório.
    """
    # Lista contendo os níveis a serem simulados (Nível 1 até Nível 5)
    niveis_reservatorio = [1, 2, 3, 4, 5]

    print("=== SISTEMA DE MONITORAMENTO DE RESERVATÓRIO DE ÁGUA ===\n")

    for nivel in niveis_reservatorio:
        cor, mensagem = obter_cor_e_alerta(nivel)
        
        # Exibe a situação atual com a cor correspondente
        # Style.RESET_ALL garante a restauração do estilo padrão
        print(f"{cor}Nível {nivel}: Situação {mensagem}{Style.RESET_ALL}")

    print("\n=======================================================")


if __name__ == "__main__":
    monitorar_reservatorio()
