#Arquivo principal 
## banco > abstração do contro de banco de dados
## adicionar > adiciona as tarefas no banco de dados < este faz as verificações de duplicidade
#[x] Abstrair DB
#[x] Adicionar arquivo no DB com verificações
#[ ] Interface 
from crud import Banco
import flet
from flet import *

def main(page:Page):
    page.window_width = 600       # window's width is 200 px
    page.window_height = 800       # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    page.scroll = "always"
    sl_sprint = TextField(label="Digite a sprint")
    youid = Text("")
    crud = Banco
    tabela = DataTable(
        columns=[
            DataColumn(Text("id")),
            DataColumn(Text("Nome")),
            DataColumn(Text("Status")),
            DataColumn(Text("Sprint")),
            DataColumn(Text("Verificada")),
        ],
        rows=[]
    )

    def adicionar_tarefas(e):
        if len(tabela.rows) > 0:
            limpar(e)
        tarefas = crud.Puxar_tarefas(sl_sprint.value)
        for i in tarefas:
            if bt_veri.value and i[4] == 2:
                continue
            elif i[4] == 1:
                valor = Checkbox(value=False)
            elif i[4] == 2:
                valor = Checkbox(value=True)
            tabela.rows.append(
			DataRow(
			cells=[
				# THIS FOR ID THE YOU TABLE 
				DataCell(Text(i[0])),
				DataCell(Text(i[2])),
				DataCell(Text(i[3])),
				DataCell(Text(i[1])),
				DataCell(valor),
			], ))
        page.update()
    def limpar(e):
        while len(tabela.rows) != 0:
            del tabela.rows[0]
        page.update()

    def atualizardb(e):
        for i in tabela.rows:
            tid = i.cells[0].content.value
            sprint = i.cells[3].content.value
            status = i.cells[1].content.value
            if i.cells[4].content.value:
                verif = 2
            else:
                verif = 1
            crud.atualizar_tarefa(tid, sprint, status, verif)    
            #crud.atualizar_tarefa()
       
    addButton = ElevatedButton("Puxar tarefas", 
                               bgcolor="Blue",
                               color='white',
                               on_click=adicionar_tarefas
                               )
    bt_limpar = ElevatedButton("limpar tarefas",
                               bgcolor='yellow',
                               color='white',
                               on_click=limpar)

    Up_db = ElevatedButton("Mandar atualizar",
                           bgcolor="green",
                           color="black",
                           on_click=atualizardb)
    tx_veri = Text("Sem verificação")
    bt_veri = Checkbox()

    page.add(
        Column([
        Text("Organizador de Tarefas", size=30, weight="bold"),
        sl_sprint ,
        Row([addButton, bt_limpar, Up_db]),
        Row([tx_veri, bt_veri]),
        tabela
        ])
    )

flet.app(target=main)