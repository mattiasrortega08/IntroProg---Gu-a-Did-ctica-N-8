edificios = ["Aulas", "Biblioteca", "Administración", "Laboratorios", "Cafetería"]
turnos = ["Mañana", "Tarde", "Noche"]
total_general = 0

print("Por favor, ingrese el consumo eléctrico en kWh (asegúrese de ingresar números):")

for i in range(len(edificios)):
    total_edificio = 0
    print(f"\nEdificio: {edificios[i]}")
    for j in range(len(turnos)):
        total_turno = 0
        print(f" Turno: {turnos[j]}")
        for k in range(7):
            consumo = float(input(f"Consumo del día {k+1}: "))
            total_turno += consumo
        print(f"  Total para el turno {turnos[j]}: {total_turno:.2f} kWh")
        total_edificio += total_turno
    print(f"  Total semanal para {edificios[i]}: {total_edificio:.2f} kWh")
    total_general += total_edificio

print(f"\nTotal general de consumo eléctrico semanal: {total_general:.2f} kWh")