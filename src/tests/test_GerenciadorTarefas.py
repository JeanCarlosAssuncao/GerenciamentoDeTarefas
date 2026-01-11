from models.GerenciadorTarefas import GerenciadorTarefas
from models.Tarefa import Tarefa
from datetime import date


def test_adicionar_tarefa():
    nova_tarefa = Tarefa(
            "Fazer Pipoca",
            "Fazer uma pipoca para assistir ao filme",
            date(2026, 4, 29),
            "em andamento",
            True
        )

    gerenciador = GerenciadorTarefas()
    result = gerenciador.adicionar_tarefa(nova_tarefa)
    print(result[1])
    assert result[0]
