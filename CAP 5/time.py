import time

# Obter a hora atual em segundos desde a época
tempo_atual_segundos = time.time()

# Converter para uma estrutura de tempo
tempo_atual = time.localtime()

# Extrair horas, minutos e segundos
horas = tempo_atual.tm_hour
minutos = tempo_atual.tm_min
segundos = tempo_atual.tm_sec

# Calcular o número de dias desde a 1° data do calendario time 
# utilizar o int para deixar o numero  inteiro e não com decimais 
dias_desde_epoca = int(tempo_atual_segundos / (24 * 3600)) # 3600 = 1h então 24*3600 pois time me da o tempo em segundos


# Exibir os resultados
print(f"Hora atual: {horas} horas, {minutos} minutos, {segundos} segundos.")
print(f"Número de dias desde a época: {dias_desde_epoca} dias.")
