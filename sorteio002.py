from random import randint
import sys
import os

lista = []

def adiciona_mais(lista, adicionar):
    lista.append(adicionar)



while True:
 #pega as posição dos itens
 quantos_indice = len(lista)

 #limpa o terminal
 os.system('cls' if os.name == 'nt' else 'clear' )

 print("o numero 1 iniciara o sorteio da lista")

 resposta = input("responda com o numero 0 para adicinar um item a lista: >")
 #if de adicionar lista
 if resposta == '0':
    adicionar = input("nome do item: >")
    adiciona_mais(lista, adicionar)
 elif resposta == "1":
   break 

if resposta == '1':
  if quantos_indice >= 1:
     indice = randint(0, quantos_indice)
     print(lista[indice])
else:
    print("sua lista não tem itens para ser sorteados \n")

    input("respoder qualquer coisa ira sair do progama")
    exit(sys)

input("fechar: >")

