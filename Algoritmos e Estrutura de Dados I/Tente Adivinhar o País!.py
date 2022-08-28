print("Bom dia, tente acertar o país em 5 tentativas") 
cont = 1
dica = 0
while cont <= 5:
	chute = str(input("Digite o país que você acha que é tentativas (digite tudo minusculo): "))
	pais = "angola"
	if (chute != pais):
		cont = cont + 1
		dica = dica + 1
		print('Erroooou boboca ainda faltam', 6 - cont,'tentativas')
		if (cont == 2):
			print("Dica: É um país do ocidente\n")
		elif (cont == 3):
			print("Dica: Começa com A\n")
		elif (cont == 4):
			print("Dica: É onde fica o mestre do kuduro\n")
		elif (cont == 5):
			print("Dica: É um país da África\n")
		elif (cont == 6):
			print("Dica: Você fracassou bonito, gastou todas suas chances\n")
	elif (chute == pais):
		print("Parabéns, você acertou em", cont, "tentativas") 
		break

	 			
