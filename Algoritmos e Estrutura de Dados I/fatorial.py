def Fatorial(numero):
	cont = numero
	num = numero
	while cont > 1 :
		num = num - 1	
		numero = numero * num
		cont = cont - 1
	print(numero)

a = int(input("Fatotial, escolha um número: "))
Fatorial(a)
