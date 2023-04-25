n1 = float(input("Digite o numero 1\n"))
n2 = float(input("Digite o numero 2\n"))
n3 = float(input("Digite o numero 3\n"))

menor = n1 
maior = n1 


if(n2>n1):
    maior = n2
    if(n3>n2):
        maior = n3
elif(n3>n1):
    maior = n3

if(n2<n1):
    menor = n2
    if(n3<n2):
        menor = n3
elif(n3<n1):
    menor = n3


print(menor)
print(maior)
