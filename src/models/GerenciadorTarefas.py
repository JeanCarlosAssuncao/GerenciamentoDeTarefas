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
            print(f"{'ID:':<20} {tarefa.ID:>45}")
            print(f"{'Titulo:':<20} {tarefa.titulo:>45}")
            print(f"{'Descrição:':<20} {tarefa.descricao:>45}")
            print(f"{'Prazo:':<20} {str(tarefa.prazo):>45}")
            print(f"{'Status:':<20} {tarefa.status:>45}")
            print(f"{'Prioridade:':<20} {tarefa.prioridade:>45}")
            print("-="*60)
            print()
    
    def coletar_tarefas_database(self):
        banco = BancoDeDados()
        self._tarefas = banco.listar_tarefas()
    
    @property
    def tarefas(self) -> list:
        return self._tarefas