import math 
x = float(input("insira o valor de x:"))
y = float(input("insira o valor de y:"))
x2 = float(input("insira o valor de x2:"))
y2 = float(input("insira o valor de y2:"))
distância = math.sqrt((x - x2)**2 + (y - y2)**2)
if distância >= 10:
	print("longe")
else: 
        print("perto")

