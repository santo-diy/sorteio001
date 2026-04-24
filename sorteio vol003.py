from random import randint
from tqdm import tqdm
import time
import sys
import os

lista = ['__________________não apague o indice 0__________________']

def adiciona_mais(lista, adicionar):
    lista.append(adicionar)




while True:
 #pega as posição dos itens
 quantos_indice = len(lista)

 #limpa o terminal
 os.system('cls' if os.name == 'nt' else 'clear' )
 print("")
 print("o numero 1 iniciara o sorteio da lista \n " \
 "se você respoder com o numero 2 você podera retirar algo da lista")
 print("")

 resposta = input("responda com o numero 0 para adicinar um item a lista: >")
 #if de adicionar lista
 if resposta == '0':
    print("")
    adicionar = input("nome do item: >")
    adiciona_mais(lista, adicionar)
    print("")
  #verifica se numero é 2
 elif resposta == '2':
   #vai printar oq tem na lista
   for valor_dos_itens, nome_dos_itens in enumerate(lista):
        print("")
        print(f"{nome_dos_itens}: {valor_dos_itens}")
        print("")

    #vai pega a indice que o usuario quer retirar
   print("")
   retirar_itens = int(input("fale o numero da sua lista para ser retirada: >"))
   print("")

    #verificando se o numero que o usuario colocou é maior ou igual que 0 e verificando se a indice que colocou é igual ou menor doq as idices que tem dentro da lista
   if retirar_itens <= quantos_indice and retirar_itens >= 0 :
      #pegando a indice e apagando o item
      lista.pop(retirar_itens)
      print('')
      #printando o resultado depois que apagou a indice indicada
      for valor_dos_itens, nome_dos_itens in enumerate(lista):
           print(f"{nome_dos_itens} : {valor_dos_itens}")
      print("")

   else:
      #auto explicativo, se as condições não for atendida ela ira executar o else
      print('')
      print("você colocou um numero de item que não existe na lista")
      print('')

    #um  time para conseguitr ver as listas
   print("o menu principal vai retorna em 5 segundos")
   time.sleep(5)

 #verificando de a respota do usuario foi igual 1
 elif resposta == "1":
   #e ira fechar o loop
   break 
 #verificando se o numero escrito do usuario foi 1
if resposta == '1':
  #verificando se tem algo dentro da lista
  if quantos_indice >= 1:
     #fazendo um carregamento de suspense
     for i in tqdm(range(5)):
      time.sleep(1)
     #sorteando e printando o resultado
     indice = randint(0, quantos_indice)
     print(lista[indice])

else:
    #se as condições não for verdadeira ira executar esse else
    print("sua lista não tem itens para ser sorteados \n")
     #verificando se o usuario realmente quer fecha
input("respoder qualquer coisa ira sair do progama")
exit(sys)

