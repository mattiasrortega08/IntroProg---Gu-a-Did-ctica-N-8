carreras = ["Sistemas", "Marketing", "Derecho"]

total_general = 0  


for i in range(len(carreras)):
    print(f"\nCarrera: {carreras[i]}")
    total_carrera = 0

  
    for j in range(1, 4):
       
        for k in range(1, 3):
            participantes = int(input(f"  Ingrese participantes en {carreras[i]} - Año {j} - Sección {k}: "))
            total_carrera += participantes
            total_general += participantes

    print(f"  Total en {carreras[i]}: {total_carrera}")


print("\nTotal general de participantes:", total_general)