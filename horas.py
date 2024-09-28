horas = int(input("Ingresa horas: "))
minutos = int(input("Ingresa minutos: "))
segundos = int(input("Ingresa segundos: "))

horas_f = 23 -horas
minutos_f = 59 - minutos
segundos_f = 60 - segundos

print(f"Faltan {horas_f} horas, {minutos_f} minutos y {segundos_f} segundos.")