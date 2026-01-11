from datetime import date

class Tarefa:
    def __init__(self, titulo:str, descricao: str, prazo: date, status: str, prioridade: bool):
        self._ID = None
        self.titulo = titulo
        self.descricao = descricao
        self._prazo = prazo
        self._status = status
        self._prioridade = prioridade
    
    @property
    def ID(self) -> int:
        return self._ID
    @ID.setter
    def ID(self, id:int):
        if isinstance(id, int):
            self._ID = id
        else:
            raise TypeError("Tipo inválido do id!")
        
    @property
    def prazo(self) -> date:
        return self._prazo
    @prazo.setter
    def prazo(self, data: date):
        """
        Definição do prazo da tarefa
        
        :param data: deve ser do tipo date
        :type data: datetime.date
        """
        if isinstance(data, date):
            if data >= date.today():
                self._prazo = data
            else:
                raise ValueError("Valor inválido da data! deve ser maior ou igual a atual.")
        else:
            raise TypeError("Tipo inválido da data!")
    
    @property
    def status(self) -> str:
        return self._status
    @status.setter
    def status(self, status: str):
        """
        Definição do status do projeto
        
        :param status: Valores aceitos -> concluida, em andamento, pendente
        :type status: str
        """
        if status.lower() == "concluida" or status.lower() == "em andamento" or status.lower() == "pendente":
            self._status = status.lower()
        else:
            raise ValueError("Valor de status inválido! valores aceitos (concluida, em andamento ou pendente)")
    
    @property
    def prioridade(self) -> int:
        """
        Retorna a prioridade 1 para True (tem prioridade) 0 para False (não tem prioridade)
        
        :return: valor inteiro (1 True) (0 False)
        :rtype: int
        """
        if self._prioridade == True:
            return 1
        elif self._prioridade == False:
            return 0
    
    @prioridade.setter
    def prioridade(self, prioridade: bool):
        """
        Define a prioridade
        
        :param prioridade: True -> tem prioridae | False -> não tem prioridade
        :type prioridade: bool
        """
        if isinstance(prioridade, bool):
            self._prioridade = prioridade
        else:
            raise TypeError("prioridade deve conter valor boolean!")
