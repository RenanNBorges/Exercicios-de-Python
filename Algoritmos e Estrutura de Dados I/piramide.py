def piramide(tijolinho, andares):
	space = " "
	cont = 1
	cont_space = andares - 1
	while cont <= andares * 2:
		simbolo = tijolinho * cont
		print(space * cont_space + simbolo)		
		cont = cont + 2
		cont_space = cont_space - 1 

print("Olá montará uma piramide para você!")
a = input("Digite o tipo de símbolo que será seu tijolinho: ")
b = int(input("Digite o número de andares: "))
piramide(a,b)

