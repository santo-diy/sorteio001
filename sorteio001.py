from random import randint
import os
lista = []
def adiciona_mais(lista):
    lista.append(adicionar)



while True:
 quantos_indice = len(lista)
 os.system('cls' if os.name == 'nt' else 'clear' )
 print("o numero 1 iniciara a lista")
 resposta = input("responda com o numero 0 para adicinar um item a lista: >")
 #if de adicionar lista
 if resposta == '0':
    adicionar = input("nome do item: >")
    adiciona_mais(lista)
    #if para sortear a lista
 if resposta == '1':
    if quantos_indice >= 1:
     indice = randint(0, quantos_indice)
     break
    else:
      print("sua lista não tem itens para ser sorteados")

      input("se responder com qualquer letra o programa fecha")
      break


print(lista[indice])
input("fechar: >")

