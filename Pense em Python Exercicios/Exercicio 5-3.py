#Exercicio 5.3 Pense em Python
def is_triangle(a,b,c):
  if (a+b) < c:
    print('No')
  elif (a+c) < b:
    print('No')
  elif (b+c) < a:
    print('No')
  else:
    print('Yes')

def test_triangle():
  print("Vamos testar se é possível formar um triângulo com os números digitados!")
  a = int(input('Por favor digite o primeiro valor: '))
  b = int(input('Por favor digite o segundo valor: '))
  c = int(input('Por favor digite o terceiro valor: '))
  print('É possível?')
  is_triangle(a,b,c)

test_triangle()