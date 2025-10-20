# Aplicação para gestão de alunos

# aluno = (nome, id, [notaTPC, notaProj, notaTeste])
# turma = [aluno]

def criarTurma():
    turma = []
    return turma

def inserirAluno(listaturma):
    a=input("Escreva o nome do aluno:")
    i=int(input("Escreva o id do aluno:"))
    n1=int(input("Escreva a nota dos TPCs:"))
    n2=int(input("Escreva a nota do Projeto:"))
    n3=int(input("Escreva a nota do Teste:"))
    notas=[n1,n2,n3]
    aluno=(a,i,notas)
    listaturma.append(aluno)
    print("Aluno inserido com sucesso!")
    return listaturma

def listarTurma(listaturma):
    print(f"Lista de alunos na turma {listaturma}:")
    for t in listaturma:
        print(f"O aluno {t[0]}, com o id {t[1]}, teve a nota {t[2][0]} no TPC, {t[2][1]} no projeto e {t[2][2]} no teste.")
    return

def idAluno(listat,id):
    encontrado = False
    for t in listat:
        if id == t[1]:
            print(f"O aluno cujo id é {id} é o/a {t[0]}.")
            encontrado = True
            break
    if not encontrado:
        print("Aluno não encontrado.")
    return

def guardarTurma(listaturma, fnome):
    file = open(fnome,"w")
    res=""
    for a in listaturma:
        aluno, id, notas = a
        res += str(aluno) + ";" + str(id) + ";" + str(notas[0]) + "::" + str(notas[1]) + "::" + str(notas[2])
        res+="\n"
    file.write(res)
    file.close()

def carregarTurma(fnome):
    listaturma = []
    file = open(fnome,"r")
    text=file.read()
    turma_text=text.split("\n")

    for p_text in turma_text[:-1]:
        t=[]
        t_text=p_text.split("|")

        for t_text in t_text[:-1]:
            al, i, notas = t_text.split(";")

            notas_lista=[]
            for n in notas.split("::"):
                notas_lista.append(float(n))
            alu=(str(al),int(i),list(notas_lista))
            t.append(alu)
        listaturma.append(t)
    file.close()
    return listaturma

def menu():
    print("\nMENU")
    print("1: Criar uma turma")
    print("2: Inserir um aluno na turma")
    print("3: Listar a turma")
    print("4: Consultar um aluno por id")
    print("5: Guardar a turma em ficheiro")
    print("6: Carregar a turma dum ficheiro")
    print("0: Sair")


turma = []
modo=-1
menu()
while modo!=0:
    modo=int(input("\nQue ação deseja realizar? "))
    if modo==0:
        print("Terminou.")
    elif modo==1:
        turma=criarTurma()
        print("Turma criada com sucesso!")
    elif modo==2:
        inserirAluno(turma)
    elif modo==3:
        if len(turma) == 0:
            print("A turma está vazia.")
        else:
            listarTurma(turma)
    elif modo==4:
        identificacao=int(input("Qual id deseja procurar: "))
        idAluno(turma,identificacao)
    elif modo==5:
        guardarTurma(turma,"turma.txt")
        print("A sua turma foi guardada no ficheiro: turma.txt")
    elif modo==6:
        turma = carregarTurma("turma.txt")
        print("Turma carregada com sucesso!")
    else:
        print("Opção inválida")