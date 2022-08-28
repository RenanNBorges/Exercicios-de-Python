while True:
	num = int(input("Digite o número que você quer ver a tabuada: "))
	multi = 0
	while multi <= 10:
		res = (num*multi)
		print(num,"x",multi,"=",res)
		multi = multi + 1
	loop = str(input("Deseja continuar? [S/N] "))
	if (loop == "N") or (loop == "n") or (loop == "Não") or (loop == "não"):
		break
	elif (loop != "N") and (loop != "n") and (loop != "Não") and (loop != "não") and (loop != "S") and (loop != "s") and (loop != "Sim") and (loop != "sim"):
		print("Inválido")
		break
