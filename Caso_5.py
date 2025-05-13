def main():
    print("=== Encuesta sobre Transporte Estudiantil - UAM ===")
    print("===================================================")

    facultades = {
        "Facultad de Ingeniería": ["Sistemas", "Electrónica"],
        "Facultad de Ciencias Sociales": ["Psicología", "Sociología"],
        "Facultad de Derecho": ["Derecho", "Criminología"]
    }

    transporte_totales = {
        "Bus": 0,
        "Moto": 0,
        "Taxi": 0,
        "Carro": 0,
        "Camina": 0
    }

    for facultad, carreras in facultades.items():
        print(f"\n--- {facultad} ---")
        transporte_facultad = {transporte: 0 for transporte in transporte_totales}

        for carrera in carreras:
            print(f"\nCarrera: {carrera}")

            for estudiante in range(1, 6):  
                while True:
                    transporte = input(f"  Estudiante #{estudiante}, ingrese su medio de transporte (Bus, Moto, Carro, Taxi, Camina): ").strip().capitalize()
                    if transporte in transporte_totales:
                        transporte_facultad[transporte] += 1
                        transporte_totales[transporte] += 1
                        break
                    else:
                        print("  Entrada inválida. Por favor, ingrese un medio de transporte válido.")

        print("\nTotales por medio de transporte en la facultad:")
        for medio, total in transporte_facultad.items():
            print(f"  {medio}: {total}")

    print("\n===================================================")
    print("Total general de participantes por medio de transporte:")
    for medio, total in transporte_totales.items():
        print(f"  {medio}: {total}")

if __name__ == "__main__":
    main()
