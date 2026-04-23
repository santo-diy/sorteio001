from random  import randint

lista = []

for i in range(5):
    print("escreva as coisas que você quer")
    itens = input("escreva aqui >")
    lista.append(itens)

resultado = randint(0, 5)
print(lista[resultado])