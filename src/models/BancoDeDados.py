import sqlite3
import os
from datetime import date

class BancoDeDados:
    def __init__(self):
        database_adress = f"src{os.sep}databases{os.sep}gerenciador_tarefas.db"
        self._conexao = sqlite3.connect(database_adress)
        self._cursor = self._conexao.cursor()

        self.criar_tabela()
    
    def criar_tabela(self) -> tuple:
        """
        Cria a tabela no banco de dados
        
        :return: tupla com (boolean, mensagem)
        :rtype: tuple
        """
        try:
            self._cursor.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, descricao TEXT, prazo DATE, status TEXT NOT NULL, prioridade BOOLEAN DEFAULT 0)")
            return True, "Tabela criada com sucesso!"
        except Exception as error:
            return False, error
    
    def inserir_tarefa(self, titulo: str, descricao: str, prazo: date, status: str, prioridade: int) -> tuple:
        """
        Insere os dados na tabela
        
        :param titulo: Título da tarefa
        :type titulo: str
        :param descricao: Descrição da tarefa
        :type descricao: str
        :param prazo: Prazo da tarefa tipo datetime.date
        :type prazo: date
        :param status: deve conter uma das seguintes descrições: pendente, em andamento, concluída
        :type status: str
        :param prioridade: 0 para False 1 para True
        :type prioridade: int
        :return: uma tupla contendo (boolean, Mensagem)
        :rtype: tuple
        """
        try:
            self._cursor.execute("INSERT INTO tarefas (titulo, descricao, prazo, status, prioridade) VALUES (?, ?, ?, ?, ?)", (titulo, descricao, prazo.isoformat(), status, prioridade, ))
            self._conexao.commit()
            return True, "Tarefa cadastrada com sucesso!"
        except:
            return False, "Erro ao cadastrar tarefa!"
    
    def listar_tarefas(self) -> list:
        """
        lista todas as tarefas da tabela

        :return: lista com todas as tarefas
        :rtype: list
        """
        cursor = self._cursor.execute("SELECT * FROM tarefas")
        return cursor.fetchall()
        
