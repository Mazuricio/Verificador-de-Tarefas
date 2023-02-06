import sqlite3
tarefas = 'DB/tarefas.db'

## Verificado serve pra eu classificar:
## 0 -> Não é novidade
## 1 -> Não foi verificado (Valor Padrão)
## 2 -> Novidade
class Banco():
    def adicionar_tarefa(id, sprint, nome, status):
        verificado = 1
        conn = sqlite3.connect(tarefas)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tarefas (id, sprint, nome, status, verificado)
            VALUES (?, ?, ?, ?, ?)
        """, (id, sprint, nome, status, verificado))
        conn.commit()
        conn.close()
    
    def atualizar_tarefa(id, sprint, status, verificar=1):
        conn = sqlite3.connect(tarefas)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tarefas SET sprint = ?, status = ?, verificado = ? WHERE id = ?
            """,(sprint, status, verificar, id))
        conn.commit()
        conn.close()
    
    def verificar_tarefa(id, sprint, status):
        conn = sqlite3.connect(tarefas)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tarefas WHERE id = ?
        """, (id,))
        resposta = cursor.fetchall()
        if resposta:
            if sprint != resposta[0][1]:
                #print("precisa atualizar a sprint")
                cursor.execute("""
                    UPDATE tarefas SET sprint = ? WHERE id = ?
                    """,(sprint, id))
            if status != resposta[0][3]:
                #print("preicsa atualizar o status")
                cursor.execute("""
                    UPDATE tarefas SET status = ? WHERE id = ?
                    """,(status, id))
        else:
            return False
        conn.commit()
        conn.close()
        return True

    def Puxar_tarefas(sprint):
        conn = sqlite3.connect(tarefas)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tarefas WHERE sprint = ?
        """, (sprint,))
        reposta = cursor.fetchall()
        conn.close()
        return reposta
    def deletar(id):
        conn = sqlite3.connect(tarefas)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM tarefas WHERE id = ?
        """, (id,))
        conn.commit()
        conn.close()
       

if __name__ == "__main__":
    banco = Banco
    #banco.adicionar_tarefa(14837, 158, "tarefateste", "AGUARDANDO SPRINT")
    #banco.verificar_tarefa(14836, 158, 'AGUARDANDO SPRINT')
    banco.deletar(14837)
    tare = Banco.Puxar_tarefas(158)
    print(tare)