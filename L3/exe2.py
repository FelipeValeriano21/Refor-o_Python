#Escreva um programa no qual leia dois valores numéricos e imprima o maior deles. Caso ambos os números forem iguais, imprima na tela “números iguais”.7

v = float(input("Qual a velocidade\n"))

if(v>80):
    m = v - 80
    m = m*5
    print("Você estava a " + str(v) + "km/h e sua multa é de R$ " + str(m))
else: 
    print("Ta tranquilo")
