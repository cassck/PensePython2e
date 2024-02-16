from datetime import timedelta

hora_inicial = timedelta(hours=6, minutes=52, seconds=0)
pace_1 = timedelta(hours=0, minutes=8, seconds=15)
pace_2 = timedelta(hours=0, minutes=7, seconds=12)*3
pace_3 = pace_1
pace_total = pace_1 + pace_2 + pace_3

print(f"hora de chegada em casa {pace_total + hora_inicial}")