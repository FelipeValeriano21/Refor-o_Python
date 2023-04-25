vc = float(input("Digite o valor da casa\n"))
s = float(input("Digite seu salario\n"))
qta = float(input("Digite a quantidade de anos\n"))

p = vc/(qta*12)

if(p>0.3*s):
    print("Não")
else:
    print("Sim")


print("Prestação " + str(p))
print("Salario " + str(0.3*s))

