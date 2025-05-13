def main():
    edificios = ["Aulas", "Biblioteca", "Administración", "Laboratorios", "Cafetería"]
    turnos = ["Mañana", "Tarde", "Noche"]
    dias = 7

    consumo_edificios = {edificio: 0 for edificio in edificios}

    for dia in range(1, dias + 1):
        print(f"\nDía {dia}")

        for turno in turnos:
            print(f" Turno: {turno}")

            for edificio in edificios:
                while True:
                    try:
                        consumo = float(input(f"  Consumo eléctrico (kWh) del edificio {edificio}: "))
                        if consumo < 0:
                            print("  Ingrese un valor positivo.")
                            continue
                        break
                    except ValueError:
                        print("  Por favor, ingrese un número válido.")
                consumo_edificios[edificio] += consumo

    print("\nConsumo total por edificio en la semana:")
    total_general = 0
    for edificio, consumo in consumo_edificios.items():
        print(f" {edificio}: {consumo:.2f} kWh")
        total_general += consumo

    print(f"\nConsumo eléctrico total general en la semana: {total_general:.2f} kWh")

if __name__ == "__main__":
    main()
