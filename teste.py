from crud import Banco

db = Banco
maxima = 26
conta = 1
while conta < maxima:
    st = "status" + str(conta)
    db.atualizar_tarefa(id=conta, sprint=1, status=st)
    conta += 1
