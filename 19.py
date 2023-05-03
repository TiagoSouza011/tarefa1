#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por um número fornecido pelo usuário.


numeros = input('Digite uma lista de 5 números aleatórios, separados por vírgulas: ')
numeros = numeros.split(",")
divisor = float(input("Digite o número pelo qual deseja dividir os números da lista: "))


divisiveis = []

for num in numeros:
    if num % divisiveis == 0:
        divisiveis.append(num)
        
print("Os números divisíveis por: ", divisor,"na lista são: ")
print(divisiveis)