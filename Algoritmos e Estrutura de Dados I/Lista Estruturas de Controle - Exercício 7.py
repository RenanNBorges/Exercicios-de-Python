print('Lista de Exercícios - Estruturas de Controle\nExercício 7\n')
print("Olá, este é um programa para testar qual de três números é o maior")
a = float(input("Por favor digite o primeiro número: "))
b = float(input("Por favor digite o segundo número que seja diferente do anterior: "))
c = float(input('Por favor digite o terceiro número que seja diferente dos anteriores: '))
if (a==b) or (b==c) or (a==c):
  print("Digite outros números, estes são iguais entre si")
else:
  if (a > b) and (a > c):
    print("{} é o maior número entre os três".format(a))
  elif (a < b) and (b > c):
    print("{} é o maior número entre os três".format(b))
  elif (c>a) and (c>b):
    print("{} é o maior número entre os três".format(c))s