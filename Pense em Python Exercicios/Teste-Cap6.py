# Teste Cap 6
def compare(x,y):
  if (x > y):
    return 1
  elif (x == y):
    return 0
  elif (x < y):
    return -1

def comp():
  x = int(input("Digite o valor de x \n"))
  y = int(input("Digite o valor de y \n"))
  print(compare(x,y))

comp()
