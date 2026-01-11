import os
from datetime import date

def gerar_titulo(titulo: str):
    limpar_tela()
    print("-=" * 60)
    print(f"{titulo:^120}")
    print("-=" * 60)
    print()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def coleta_data() -> tuple:
    """
    Coleta os dados para formar uma data

    :return: tupla com boolean + data ou boolean + mensagem de erro
    :rtype: tuple
    """
    print("\nPrazo para finalizar:")
    dia = input("Dia: ")
    mes = input("Mês: ")
    ano = input("Ano: ")
    try:
        data = date(int(ano), int(mes), int(dia))
        return True, data
    except:
        return False, "Dados inválidos!"

def coletar_status() -> tuple:
    """Coleta o status que o usuario deseja
    
    :return: tupla com Booblean + mensagem ou resultado
    :rtype: tuple
    """
    print("\nStatus da Tarefa:")
    print(
        "[1] - pendente\n"
        "[2] - em andamento\n"
        "[3] - concluida"
    )
    escolha_usuario = input("Número de sua escolha: ").strip()
    if escolha_usuario == "1":
        return True, "pendente"
    elif escolha_usuario == "2":
        return True, "em andamento"
    elif escolha_usuario == "3":
        return True, "concluida"
    else:
        return False, "Opção inválida!"

def coletar_prioridade() -> tuple:
    """
    Coleta a prioridade do usuário

    :return: boolean + mensagem caso de erro ou boolean se comfirmado.
    :rtype: tuple
    """
    print("\nDefinindo prioridade:")
    print("[1] - Tarefa com prioridade \n[2] - Tarefa sem prioridade")
    escolha_usuario = input("Número de sua escolha: ").strip()
    
    if escolha_usuario == "1":
        return True, True
    elif escolha_usuario == "2":
        return True, False
    else:
        return False, "Escolha inválida!"