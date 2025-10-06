# Aplicação para manipulação de listas de inteiros

import random

Lista = []

def criaLista(N):
	global Lista
	Lista = []
	for n in range(N):
		Lista.append(random.randrange(1,101))
	return Lista

def leLista(N):
	global Lista
	Lista = []
	for k in range(N):
		Lista.append(int(input("Introduza um número.")))
	return Lista

def somaLista(N):
	soma = 0
	for n in N:
		soma = soma + n
	return soma

def mediaLista(N):
	if len(N) == 0:
		return 0
	soma = somaLista(N)
	return soma/len(N)

def maiorLista(N):
	if len(N) == 0:
		return None
	maior = N[0]
	for m in N:
		if m > maior:
			maior = m
	return maior

def menorLista(N):
	if len(N) == 0:
		return None
	menor = N[0]
	for m in N:
		if m < menor:
			menor = m
	return menor

def estaOrdenadaCrescente(N):
	for i in range(len(N) - 1):
		if N[i] > N[i + 1]:
			return "Não"
	return "Sim"

def estaOrdenadaDecrescente(N):
	for i in range(len(N) - 1):
		if N[i] < N[i + 1]:
			return "Não"
	return "Sim"

def indice(N, elem):
	cond = -1
	if elem in N:
		cond = N.index(elem) + 1
	return cond

modo = 1

while modo != 0:
	modo = int(input("Menu: (1) Criar Lista; (2) Ler Lista; (3) Soma; (4) Média; (5) Maior; (6) Menor; (7) estaOrdenada por ordem crescente; (8) estaOrdenada por ordem decrescente; (9) Procura um elemento; (0) Sair"))
	if modo == 1:
		print(criaLista(int(input("Introduza o número de elementos que quer na sua lista"))))
	elif modo == 2:
		print(leLista(int(input("Introduza o número de elementos que quer na sua lista"))))
	elif modo == 3:
		print(somaLista(Lista))
	elif modo == 4:
		print(mediaLista(Lista))
	elif modo == 5:
		print(maiorLista(Lista))
	elif modo == 6:
		print(menorLista(Lista))
	elif modo == 7:
		resultado = estaOrdenadaCrescente(Lista)
		print(resultado)
	elif modo == 8:
		resultado = estaOrdenadaDecrescente(Lista)
		print(resultado)
	elif modo == 9:
		print(Lista)
		print(indice(Lista,int(input("Procura um elemento"))))