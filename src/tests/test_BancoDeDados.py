from models import BancoDeDados
import pytest
from datetime import date

def test_criar_tabela():
    """
    Test que valida se a tabela esta sendo criada.
    """
    database = BancoDeDados.BancoDeDados()
    resultado = database.criar_tabela()
    print(resultado)
    assert resultado[0]

def test_inserir_tarefa():
    """
    Testa se a tarefa está sendo inserida corretamente
    """
    database = BancoDeDados.BancoDeDados()
    resultado = database.inserir_tarefa("Fazer arroz", "Arroz soltinho", date(2026, 3, 12), "em andamento", 1)
    print(resultado)
    assert resultado

def test_listar_tarefas():
    """
    Testa se está listando todas as tarefas
    """
    database = BancoDeDados.BancoDeDados()
    resultado = database.listar_tarefas()
    assert type(resultado) == list
    