from utils import gerar_titulo, coleta_data, coletar_status, coletar_prioridade
from models.GerenciadorTarefas import GerenciadorTarefas
from models.Tarefa import Tarefa
from models.BancoDeDados import BancoDeDados
from time import sleep

LISTA_TAREFAS = GerenciadorTarefas()

parar = False
while not parar:
    gerar_titulo("Gerenciador de Tarefas")
    print(
        "[1] - Cadastrar nova tarefa. \n"
        "[2] - Listar tarefas. \n"
        "[3] - Atualizar Status de uma tarefa. \n"
        "[4] - Atualizar dados de uma tarefa. \n"
        "[5] - Remover uma tarefa. \n"
        "[6] - Listar tarefas por Status. \n"
        "[7] - Listar por Titulo ou Descrição. \n"
        "[8] - Ordenar tarefas por prazo. \n"
        "[12] - Sair"
    )

    escolha_usuario = input("Número de sua escolha: ").strip()

    if escolha_usuario == "12": #---------------- sair --------------------#
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
        input('Pressione "Enter" para voltar.')
    
    elif escolha_usuario == "3": #------------------ Atualizar Status -------------------- #
        gerar_titulo("Atualizar Status")
        LISTA_TAREFAS.listar_tarefas()
        id_tarefa = input("ID da tarefa: ")

        for tarefa in LISTA_TAREFAS.tarefas:
            if int(id_tarefa) == tarefa.ID:
                novo_status = coletar_status()
                if novo_status:
                    tarefa.status = novo_status[1]

                    # Atualiza o banco de dados e a lista de tarefas.
                    banco = BancoDeDados()
                    resultado = banco.atualizar_tarefa(tarefa)
                    LISTA_TAREFAS.coletar_tarefas_database()

                    print(resultado[1])
                    sleep(2)
                else:
                    print(novo_status[1])
                    sleep(2)
                break
    
    elif escolha_usuario == "4": #---------------------- editar tarefa ----------------------- #
        gerar_titulo("Editar Tarefa")
        LISTA_TAREFAS.listar_tarefas()
        id_tarefa = input("ID da tarefa: ")

        for tarefa in LISTA_TAREFAS.tarefas:
            if int(id_tarefa) == tarefa.ID:

                novo_titulo = input("Novo titulo: ")
                nova_descricao = input("Nova descrição: ")
                novo_prazo = coleta_data()

                if novo_prazo[0]:
                    tarefa.titulo = novo_titulo
                    tarefa.descricao = nova_descricao
                    tarefa.prazo = novo_prazo[1]

                    # Atualiza o banco de dados e a lista de tarefas.
                    banco = BancoDeDados()
                    resultado = banco.atualizar_tarefa(tarefa)
                    LISTA_TAREFAS.coletar_tarefas_database()

                    print(resultado[1])
                    sleep(2)

                else:
                    print(novo_prazo[1])
                    sleep(2)
                break
    elif escolha_usuario == "5": #------------------------ remover tarefa --------------------------#
        gerar_titulo("Remover Tarefa")
        LISTA_TAREFAS.listar_tarefas()
        id_tarefa = input("ID da tarefa: ")

        for tarefa in LISTA_TAREFAS.tarefas:
            if int(id_tarefa) == tarefa.ID:
                resultado = LISTA_TAREFAS.remover_tarefa(tarefa)
                print(resultado[1])
                sleep(2)
                break
        try:
            print(resultado[1])
            sleep(2)
        except NameError:
            print("ID inválido! ")
            sleep(2)
    
    elif escolha_usuario == "6": #----------------------Listar por Status ----------------------- #
        gerar_titulo("Lista por Status")
        status = coletar_status()
        if status:
            LISTA_TAREFAS.listar_por_status(status[1])
            input("Pressione 'Enter' para continuar.")
        else:
            print(status[1])
    
    elif escolha_usuario == "7": #---------------Listar por titulo ou descricao ----------------- #
        gerar_titulo("Listar por Titulo ou Descrição")
        frase = input("Palavra ou Frase que deseja procurar: ")
        resultado = LISTA_TAREFAS.listar_por_titulo_descricao(frase)
        print(resultado[1])
        input("Pressione 'Enter' para continuar...")

    elif escolha_usuario == "8": #-------------------------- ordenar por prazo ------------------------- #
        print("[1] - Ordem Crescente. \n[2] - Ordem Decrescente.")
        ordem = input("Número de escolha: ")
        if ordem == "1":
            mensagem = LISTA_TAREFAS.ordenar_por_prazo(True)
        elif ordem == "2":
            mensagem = LISTA_TAREFAS.ordenar_por_prazo(False)
        else:
            mensagem = "Opção inválida!"
        print(mensagem)
        sleep(2)