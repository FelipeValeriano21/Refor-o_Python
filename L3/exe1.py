#Escreva um programa no qual leia dois valores numéricos e imprima o maior deles. Caso ambos os números forem iguais, imprima na tela “números iguais”.7

n1 = float(input("Digite o numero 1\n"))
n2 = float(input("Digite o numero 2\n"))

if(n1>n2):
    print(n1)
elif (n2>n1):
    print(n2)
else: 
    print("números iguais")
