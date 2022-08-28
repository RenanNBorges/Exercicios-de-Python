print("Lista de Exercícios - Estruturas de Controle")
print(" ")
print("Exercício 4")
n1, n2, n3, n4, n5  = [float(x) for x in input("Por favor insira cinco números separados por vírgula: ").split(",")]
s = (n1+n2+n3+n4+n5)
m = (s*n1)
print("A soma de todos os resultados é {} e resultado da soma multiplicado pelo primeiro número é {}".format(s,m))
