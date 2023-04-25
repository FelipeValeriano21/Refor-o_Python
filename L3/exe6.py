dis = float(input("Qual a distancia\n"))

if(dis<=200):
    dis = dis*0.5 
    print("Valor da corrida R$" + str(dis))
else:
    dis = dis*0.45 
    print("Valor da corrida R$" + str(dis))