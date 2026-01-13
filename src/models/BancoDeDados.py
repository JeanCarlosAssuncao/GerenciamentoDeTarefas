import sqlite3
import os
from datetime import date
from models.Tarefa import Tarefa

class BancoDeDados:
    def __init__(self):
        base_dir = os.path.join("src", "databases")
        os.makedirs(base_dir, exist_ok=True)  # cria a pasta se não existir
        database_address = os.path.join(base_dir, "gerenciador_tarefas.db")
        
        self._conexao = sqlite3.connect(database_address)
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
        cursor = cursor.fetchall()

        lista_de_tarefas = []
        for item in cursor:
            #Transforma os dados em objeto Tarefa
            tarefa_atual = Tarefa(
                item[1],
                item[2],
                date(int(item[3][0:4]), int(item[3][5:7]), int(item[3][8:10])),
                item[4],
                True if item[5] == 1 else False)
            
            tarefa_atual.ID = item[0]
            lista_de_tarefas.append(tarefa_atual)
        
        return lista_de_tarefas
    
    def atualizar_tarefa(self, tarefa_atualizada: object) -> tuple:
        """
        Atualiza os dados da tarefa no banco de dados
        
        :param tarefa_atualizada: Objeto Tarefa atualizado
        :type tarefa_atualizada: object
        :return: Boolean mais mensagem informativa
        :rtype: tuple
        """
        try:
            self._cursor.execute("""
                UPDATE tarefas
                SET status = ?, prioridade = ?, titulo = ?, descricao = ?, prazo = ?
                WHERE id = ?
                """, (tarefa_atualizada.status,
                      tarefa_atualizada.prioridade,
                      tarefa_atualizada.titulo,
                      tarefa_atualizada.descricao,
                      tarefa_atualizada.prazo.isoformat(),
                      tarefa_atualizada.ID))
            self._conexao.commit()
            
            return True, "Tarefa atualizada!"
        except:
            return False, "Dados inválidos"
    
    def remover_tarefa(self, id:int) -> tuple:
        """
        Remove uma tarefa do banco de dados
        
        :param id: ID da tarefa
        :type id: int
        :return: retorna bollean e a mensagem informativa
        :rtype: tuple
        """
        try:
            self._cursor.execute(
                """DELETE FROM tarefas
                WHERE id = ?""",
                (id, )
            )
            self._conexao.commit()
            return True, "Tarefa deletada!"
        except sqlite3.Error as error:
            return False, error
        except Exception as error:
            return False, error