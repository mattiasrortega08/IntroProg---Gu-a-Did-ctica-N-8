#Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de
#primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,
#ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total
#gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer
#semanas y días.

def gastos():
    Semanas = 4
    total_gasto_sem1 = 0
    total_gasto_sem2 = 0
    total_gasto_sem3 = 0
    total_gasto_sem4 = 0
    total_gasto_mes = 0 
    print("A continuacion calculare cuanto gastaron un grupo de estudiantes de la UAM en cada una de las semanas de un mes inlcuyendo el mes")
    for semana in range(Semanas):
        print(f"a continuacion te preguntare cuanto gastaron en los 7 dias de la semana {semana+1}")
        Dias = 7
        for dia in range(Dias):
            gastos = float(input(f"Dime cuanto gastaron en el dia {dia+1}: "))
            if semana == 0:
                total_gasto_sem1 += gastos
            if semana == 1:
                total_gasto_sem2 += gastos
            if semana == 2:
                total_gasto_sem3 += gastos
            if semana == 3:
                total_gasto_sem4 += gastos 
            total_gasto_mes = total_gasto_sem1 + total_gasto_sem2 + total_gasto_sem3 + total_gasto_sem4
            
            
    print(f"El grupo gasto en la semana 1 {total_gasto_sem1} Cordobas")     
    print(f"El grupo gasto en la semana 2 {total_gasto_sem2} Cordobas")    
    print(f"El grupo gasto en la semana 3 {total_gasto_sem3} Cordobas")    
    print(f"El grupo gasto en la semana 4 {total_gasto_sem4} Cordobas")    
    print(f"En el mes el grupo de estudiantes gasto: {total_gasto_mes} Cordobas")
    
        
gastos()
    
        
    
                                                