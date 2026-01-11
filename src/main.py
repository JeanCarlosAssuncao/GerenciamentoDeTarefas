from utils import gerar_titulo, coleta_data, coletar_status, coletar_prioridade
from models.GerenciadorTarefas import GerenciadorTarefas
from models.Tarefa import Tarefa
from time import sleep

LISTA_TAREFAS = GerenciadorTarefas()

parar = False
while not parar:
    gerar_titulo("Gerenciador de Tarefas")
    print(
        "[1] - Cadastrar nova tarefa.\n"
        "[2] - Listar tarefas.\n"
        "[5] - Sair"
    )

    escolha_usuario = input("Número de sua escolha: ").strip()

    if escolha_usuario == "5": #---------------- sair --------------------#
        parar = True

    elif escolha_usuario == "1": #-------------- cadastrar nova tarefa -----------------#
        gerar_titulo("Cadastro de Tarefas")
        titulo = input("Titulo: ")
        descricao = input("Descrição: ")
        prazo = coleta_data()
        status = coletar_status()
        prioridade = coletar_prioridade()

        if prazo[0] == True and status[0] == True and prioridade[0] == True:
            prazo = prazo[1]
            status = status[1]
            prioridade = prioridade[1]

            nova_tarefa = Tarefa(titulo, descricao, prazo, status, prioridade)
            LISTA_TAREFAS.adicionar_tarefa(nova_tarefa)
            print("Tarefa cadastrada com sucesso!")
            sleep(2)
        else:
            print("Dados inválidos!")
            sleep(2)
    
    elif escolha_usuario == "2": #-----------------Listar tarefas----------------#
        gerar_titulo("Lista de Tarefas")
        LISTA_TAREFAS.listar_tarefas()
