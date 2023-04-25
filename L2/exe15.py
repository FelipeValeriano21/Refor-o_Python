nc = float(input("Quantos cigarros por dia\n"))
af = float(input("Quantos anos fumando\n"))

f = nc*365*af 

t = (f*10)/(60*24)

print(str(t) + "dias perdidos")
