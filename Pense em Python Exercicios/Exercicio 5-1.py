# Exercicio 5.1
import time
minutos_passados = time.time()//60
horas_passadas = minutos_passados//60
dias_passados = horas_passadas//24
print(dias_passados,'dias,', horas_passadas,"horas,", minutos_passados,'minutos e', time.time(), 'segundos passados desde 1 de janeiro de 1970')