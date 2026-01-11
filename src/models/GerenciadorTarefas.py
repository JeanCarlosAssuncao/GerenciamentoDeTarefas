from models.BancoDeDados import BancoDeDados

class GerenciadorTarefas:
    def __init__(self):
        self._tarefas = []
    
    def adicionar_tarefa(self, tarefa: object) -> tuple:
        try:
            banco = BancoDeDados()
            resultado = banco.inserir_tarefa(tarefa.titulo, tarefa.descricao, tarefa.prazo, tarefa.status, tarefa.prioridade)
            self._tarefas = banco.listar_tarefas()
            return resultado
        except Exception as error:
            return False, error
