#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista
numeros = input("digite uma lista de números: ")
numeros = numeros.split(",")
pares = []

for numero in numeros:
     numero = int(numero)
     if numero % 2 == 0:
          pares.append(numero)
        
print("números pares: ", pares)