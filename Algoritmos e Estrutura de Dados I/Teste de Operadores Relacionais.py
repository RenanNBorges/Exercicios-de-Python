a , b, c = [float(x) for x in input("Insira três valores separados por vírgula: ").split(",")]
if (a>c) and (a<b):
	print(a)
elif (b<c):
	print(b)
else:
	print(c)
