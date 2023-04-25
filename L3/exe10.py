q = float(input("Quantidade consumida\n"))
op = input("instalação:\nR para residencial\n I para industrial\n C para comércio\n\n")


if(op == "R"):
    if(q<=500):
        v = q*0.4
        print("Valor a pagar " + str(v))
    else:
        v = q*0.65
        print("Valor a pagar " + str(v))

if(op == "C"):
    if(q<=1000):
        v = q*0.55
        print("Valor a pagar " + str(v))
    else:
        v = q*0.60
        print("Valor a pagar " + str(v))


if(op == "I"):
    if(q<=5000):
        v = q*0.55
        print("Valor a pagar " + str(v))
    else:
        v = q*0.60
        print("Valor a pagar " + str(v))


else:
    print("Não existe")