# Exercicio 5.4
def recurse(n, s):
  if n == 0:
    print(s)

  else:
    recurse(n-1, s+1)

recurse(3,0)