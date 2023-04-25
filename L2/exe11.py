s = float(input("Qual o valor da mercadoria\n"))
p = float(input("Quantos porcento de desconto\n"))


ns = s - s*p/100

d = s - ns


print("O produto agora custa " + str(ns) + " e o desconto foi de " + str(d))
