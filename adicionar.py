import pandas as pd
from crud import Banco

## pra não carregar o pandas, da pra fazer diferente, mas futuramente

def adicionar(file, sprint):
    banco = Banco
    df = pd.read_csv(file)
    index = 0
    for i in df['id']:
        if index < 0:
            pass
        else:
            if banco.verificar_tarefa(int(df['id'][index]), sprint, df['status'][index]):
                # verifica se já existe a entrada no DB
                # se já existe a funcão verificar tarefa atualiza automaticamente o status dela 
                pass
            else: # se não existe adiciona no banco
                banco.adicionar_tarefa(int(df['id'][index]), sprint, df['titulo'][index], df['status'][index])
                #print('add', int(df['id'][index]))
        index += 1


if __name__ == "__main__":
    arquivo = 'teste_tarefas.csv'
    adicionar(arquivo, 1)