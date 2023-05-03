#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.
numeros = input("Digite uma lista de numeros: " ).split(',')

maximo = numeros[0]
minimo = numeros[0]
for n in numeros:
       if n > maximo:
           maximo = n
       if n < minimo:
            minimo = n 
           
print("maior numero", maximo)
print("menor numero", minimo)