#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, imprima apenas as palavras que começam com a letra "a".

palavras = input("digite uma lista de palavras: ")

a = []

for palavras in palavras.split(','):
    if palavras[0] == 'a':
        a.append(palavras)
      
print("palavras começadas com a", a)