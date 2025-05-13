def control_ventas():
    kioscos = 3
    productos = 5
    dias = 4

    # Inicializa las ventas por kiosco y producto
    ventas = [[[0 for _ in range(productos)] for _ in range(kioscos)] for _ in range(dias)]

    print("Control de ventas en kioscos estudiantiles de la UAM")
    print("----------------------------------------------------")

    # Registro de ventas
    for dia in range(dias):
        print(f"\nDía {dia + 1}")
        for kiosco in range(kioscos):
            print(f"  Kiosco {kiosco + 1}")
            for producto in range(productos):
                mensaje = f"    Ventas del producto {producto + 1}: "
                ventas[dia][kiosco][producto] = solicitar_entero(mensaje)

    # Cálculo y muestra de resultados
    for dia in range(dias):
        print(f"\nResultados del Día {dia + 1}")
        total_dia = 0
        for kiosco in range(kioscos):
            print(f"  Kiosco {kiosco + 1}")
            total_kiosco = 0
            for producto in range(productos):
                total_kiosco += ventas[dia][kiosco][producto]
                print(f"    Total vendido del producto {producto + 1}: {ventas[dia][kiosco][producto]}")
            print(f"    Total vendido en el kiosco {kiosco + 1}: {total_kiosco}")
            total_dia += total_kiosco
        print(f"  Total general del día {dia + 1}: {total_dia}")

    # Cálculo del total vendido por producto en cada kiosco
    print("\nResumen total por kiosco y producto:")
    for kiosco in range(kioscos):
        print(f"\nKiosco {kiosco + 1}")
        for producto in range(productos):
            total_producto = sum(ventas[dia][kiosco][producto] for dia in range(dias))
            print(f"  Total vendido del producto {producto + 1}: {total_producto}")


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


# Llamada directa a la función principal
control_ventas()    