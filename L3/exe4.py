sal = float(input("Digite seu salario\n"))

if(sal>1250):
    sal = sal*1.1 
    print("Novo salario R$" + str(sal))
else:
    sal = sal*1.15 
    print("Novo salario R$" + str(sal))