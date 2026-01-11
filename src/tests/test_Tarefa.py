from models.Tarefa import Tarefa
from datetime import date
import pytest

def test_criar_objeto_Tarefa():
    try:
        nova_tarefa = Tarefa(
            "Fazer Pipoca",
            "Fazer uma pipoca para assistir ao filme",
            date(2026, 4, 29),
            "em andamento",
            True
        )
        assert True
    except Exception as error:
        print(error)
        assert False

def test_valueerror_prazo_and_typeerror_prazo():
    with pytest.raises(ValueError):
        nova_tarefa = Tarefa(
            "Fazer Pipoca",
            "Fazer uma pipoca para assistir ao filme",
            date(2026, 1, 1),
            "em andamento",
            True
        )
    with pytest.raises(TypeError):
        nova_tarefa = Tarefa(
            "Fazer Pipoca",
            "Fazer uma pipoca para assistir ao filme",
            (2026, 1, 1),
            "em andamento",
            True
        )

def test_valueerror_status():
    with pytest.raises(ValueError):
        nova_tarefa = Tarefa(
                "Fazer Pipoca",
                "Fazer uma pipoca para assistir ao filme",
                date(2026, 1, 1),
                "fechado",
                True
            )


def test_typeerror_prioridade():
    with pytest.raises(TypeError):
        nova_tarefa = Tarefa(
                "Fazer Pipoca",
                "Fazer uma pipoca para assistir ao filme",
                date(2026, 12, 11),
                "concluida",
                1
            )