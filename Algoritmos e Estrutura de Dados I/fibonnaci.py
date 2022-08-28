def friboi(limite):
	contador = 0
	num = 0
	num2 = 1
	while contador <= limite:
		if (num == 1) or (num == 0):
			print(num)
			num = num + num2
		else:
			print(num)
			num = num + num2
		contador = contador + 1

a = int(input("Escolhe um número aí: "))
friboi(a)



