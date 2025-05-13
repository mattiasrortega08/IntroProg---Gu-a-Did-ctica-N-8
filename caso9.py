
def main():
    carreras = ["Ingeniería", "Medicina", "Derecho"]
    tipos_acceso = ["Estable", "Intermitente", "Sin acceso"]
    
    resultados = {carrera: {tipo: 0 for tipo in tipos_acceso} for carrera in carreras}

    for carrera in carreras:
        print(f"\nEncuesta para la carrera de {carrera}:")
        
        for grupo in range(1, 4):  
            print(f"  Grupo {grupo}:")
            
            
            for estudiante in range(1, 6):  
                print(f"    Estudiante {estudiante}:")
                opcion = int(input("      Tipo de acceso (1: Estable, 2: Intermitente, 3: Sin acceso): "))
                tipo_acceso = tipos_acceso[opcion - 1]
                resultados[carrera][tipo_acceso] += 1

   
    print("\nResultados de la encuesta:")
    for carrera, conteo in resultados.items():
        print(f"\nCarrera: {carrera}")
        for tipo, cantidad in conteo.items():
            print(f"  {tipo}: {cantidad}")

if __name__ == "__main__":
    main()