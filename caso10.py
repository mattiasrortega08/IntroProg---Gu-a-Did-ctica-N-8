
def main():
    categorias = ["Ingeniería", "Salud", "Derecho", "Literatura"]
    subcategorias = ["Subcategoría 1", "Subcategoría 2", "Subcategoría 3"]
    
    prestamos = {categoria: {sub: 0 for sub in subcategorias} for categoria in categorias}
    total_general = 0

    for categoria in categorias:
        print(f"\nRegistro de préstamos para la categoría {categoria}:")
        
        for subcategoria in subcategorias:
            print(f"  {subcategoria}:")
            
            for dia in range(1, 6):  
                cantidad = int(input(f"    Día {dia}, número de préstamos: "))
                prestamos[categoria][subcategoria] += cantidad
                total_general += cantidad

    
    print("\nResultados de los préstamos:")
    for categoria, sub_prestamos in prestamos.items():
        print(f"\nCategoría: {categoria}")
        total_categoria = 0
        for subcategoria, cantidad in sub_prestamos.items():
            print(f"  {subcategoria}: {cantidad}")
            total_categoria += cantidad
        print(f"  Total categoría: {total_categoria}")
    
    print(f"\nTotal general semanal: {total_general}")

if __name__ == "__main__":
    main()