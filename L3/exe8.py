n1 = float(input("Digite o numero 1\n"))
n2 = float(input("Digite o numero 2\n"))

op = input("Qual operação?\nsoma(+)\nsubtração (-)\nmultiplicação(*)\ndivisão(/)\n\n USE OS SIMBOLOS\n\n")



if(op == "+"):
    r = n1+n2
    print("Resultado da soma é " + str(r))
if(op == "-"):
    r = n1-n2
    print("Resultado da subtração é " + str(r))
if(op == "*"):
    r = n1*n2
    print("Resultado da multiplicação é " + str(r))
if(op == "/"):
    r = n1/n2
