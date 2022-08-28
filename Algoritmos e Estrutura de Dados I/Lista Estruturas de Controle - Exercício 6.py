print("Lista de Exercícios - Estruturas de Controle")
print(" ")
print("Exercício 6")
d1, d2 = [float(x) for x in input("Por favor insira dois números separados por vírgula: ").split(",")]
if (d1>d2):
	print("O número {} é o maior entre os dois números inseridos".format(d1))
elif (d1==d2):
	print("Os dois números são iguais")
else:
	print("O número {} é o maior entre os dois números inseridos".format(d2))
