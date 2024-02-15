#Inicialize o interpretador do Python e use-o como uma calculadora.

#Quantos segundos há em 42 minutos e 42 segundos?

#Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.

#Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo 
# médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média 
# em milhas por hora?

# #1

minutos = 42
segundos = 42
print(f"Em 42m e 42s temos {minutos*60 + segundos}s")

# #2
km = 10/1.60934
print (f"Em 10km temos {km:.2f} milhas")

# #3
hora = ((minutos*60 + segundos)/60)/60 #0,71
pace = (minutos*60 + segundos) / km
print(f"{pace/60:.2f}") #minutos
print(f"{km/hora:.2f}") #horas


