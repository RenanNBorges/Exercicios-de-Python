def Escadinha(tijolinho, andares):
	n_andares = andares
	simbolo = tijolinho
	cont = 0
	while cont <= n_andares:
		cont = cont + 1
		print(simbolo*cont)

print("Olá montará uma escada para você!")
a = input("Digite o tipo de símbolo que será seu tijolinho: ")
b = int(input("Digite o número de andares: "))
Escadinha(a,b)
