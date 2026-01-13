from models.BancoDeDados import BancoDeDados

class GerenciadorTarefas:
    def __init__(self):
        self._tarefas = []
        self.coletar_tarefas_database()
    
    def adicionar_tarefa(self, tarefa: object) -> tuple:
        try:
            banco = BancoDeDados()
            resultado = banco.inserir_tarefa(tarefa.titulo, tarefa.descricao, tarefa.prazo, tarefa.status, tarefa.prioridade)
            self._tarefas = banco.listar_tarefas()
            return resultado
        except Exception as error:
            return False, error

    def listar_tarefas(self):
        """
        Lista todas as tarefas de forma ordenada e detalhada
        """
        for tarefa in self._tarefas:
            print(tarefa)
    
    def coletar_tarefas_database(self):
        banco = BancoDeDados()
        self._tarefas = banco.listar_tarefas()
    
    @property
    def tarefas(self) -> list:
        return self._tarefas
    
    def remover_tarefa(self, end_tarefa) -> tuple:
        """
        remove uma tarefa.
        
        :param end_tarefa: Objeto Tarefa que deseja remover.
        :return: tupla com boolean e mensagem
        :rtype: tuple
        """

        banco = BancoDeDados()
        resultado = banco.remover_tarefa(end_tarefa.ID)
        
        self.coletar_tarefas_database()
        return resultado

    def listar_por_status(self, status: str) -> tuple:
        for tarefa in self._tarefas:
            if tarefa.status == status:
                print(tarefa)
