def registrar_ventas():
    total_acumulado = 0 

    print("Registro de ventas de nacatamales en eventos de domingo en la UAM")
    print("---------------------------------------------------------------")

    for domingo in range(1, 5):
        print(f"\nDomingo {domingo}")
        clientes = solicitar_entero("Ingrese la cantidad de clientes: ")
        total_domingo = 0  

        for cliente in range(1, clientes + 1):
            nacatamales = solicitar_entero(f"  Nacatamales comprados por cliente {cliente}: ")
            total_domingo += nacatamales  

        print(f"Total vendido el domingo {domingo}: {total_domingo} nacatamales")
        total_acumulado += total_domingo  

    print("\n---------------------------------------------------------------")
    print(f"Total acumulado en los 4 domingos: {total_acumulado} nacatamales")
    print("---------------------------------------------------------------")


def solicitar_entero(mensaje):
    """Solicita un número entero positivo al usuario."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un número positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


registrar_ventas()