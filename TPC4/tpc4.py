# Aplicação para gerir um cinema

def existeCinema(listac, nomec):
    for c in listac:
        if c[2] == nomec:
            return True
    return False

def inserirCinema(listac, lugares, nome):
    c = [lugares, [], nome]
    if not existeCinema(listac, nome):
        listac.append(c)
    return listac

def listarC(cinema, nomec=None):
    if nomec is None:
        print(cinema)
    else:
        for c in cinema:
            if c[2] == nomec:
                print(f"O cinema {c[2]} tem {c[0]} lugares e {c[1]} estão ocupados.")
    return

def disponivel(listac, nomec, lugar):
    for c in listac:
        if c[2] == nomec:
            if lugar in c[1] or lugar > c[0] or lugar < 1:
                return False
    return True

def vendabilhetes(listac, nomec, lugar):
    novalista = []
    for c in listac:
        if c[2] == nomec:
            if disponivel(listac, nomec, lugar):
                novalista.append([c[0], c[1] + [lugar], c[2]])
            else:
                novalista.append([c[0], c[1], c[2]])
        else:
            novalista.append([c[0], c[1], c[2]])
    return novalista

def listardisponibilidades(listac):
    for c in listac:
        disp = c[0] - len(c[1])
        print(f"{c[2]} tem {c[1]} lugares ocupados.")
        print(f"{c[2]} tem {disp} lugares disponíveis.")
    return

def libertaLugar(listac, nomec, lugar):
    novalista = []
    for c in listac:
        if c[2] == nomec:
            if lugar in c[1]:
                nova_ocupacao = c[1].copy()
                nova_ocupacao.remove(lugar)
                novalista.append([c[0], nova_ocupacao, c[2]])
            else:
                novalista.append([c[0], c[1], c[2]])
        else:
            novalista.append([c[0], c[1], c[2]])
    return novalista

def criaCinema(listac, nomec, lugares):
    if lugares > 0:
        c = [lugares, [], nomec]
        if not existeCinema(listac, nomec):
            listac.append(c)
    return listac

def removeCinema(listac, nomec):
    for c in listac:
        if c[2] == nomec and c[1] == []:
            listac.remove(c)
    return listac

menu = -1
cinema1 = []

while menu != 0:
    modo = int(input("""Qual operação deseja executar: 
                   (1) Inserir novo cinema; 
                   (2) Listar cinemas; 
                   (3) Verificar disponibilidade de lugares; 
                   (4) Comprar bilhetes;
                   (5) Apresentar lugares disponíveis;
                   (6) Listar lugares ocupados;
                   (7) Retirar lugar de um cinema;
                   (8) Criar novo cinema;
                   (9) Eliminar cinemas vazios;
                   (0) Sair\n"""))
    
    if modo == 0:
        print("Terminou")
        menu = 0
    elif modo == 1:
        nome = input("Nome do cinema: ")
        lugares = int(input("Número de lugares: "))
        cinema1 = inserirCinema(cinema1, lugares, nome)
    elif modo == 2:
        nome = input("Nome do cinema (Enter para listar todos): ")
        if nome.strip() == "":
            listarC(cinema1)
        else:
            listarC(cinema1, nome)
    elif modo == 3:
        nome = input("Nome do cinema: ")
        lugar = int(input("Lugar: "))
        if disponivel(cinema1, nome, lugar):
            print("Lugar disponível!")
        else:
            print("Lugar não disponível!")
    elif modo == 4:
        nome = input("Nome do cinema: ")
        lugar = int(input("Lugar: "))
        cinema1 = vendabilhetes(cinema1, nome, lugar)
    elif modo == 5:
        listardisponibilidades(cinema1)
    elif modo == 6:
        nome = input("Nome do cinema: ")
        listarC(cinema1, nome)
    elif modo == 7:
        nome = input("Nome do cinema: ")
        lugar = int(input("Lugar: "))
        cinema1 = libertaLugar(cinema1, nome, lugar)
    elif modo == 8:
        nome = input("Nome do cinema: ")
        lugares = int(input("Número de lugares: "))
        cinema1 = criaCinema(cinema1, nome, lugares)
    elif modo == 9:
        nome = input("Nome do cinema: ")
        cinema1 = removeCinema(cinema1, nome)