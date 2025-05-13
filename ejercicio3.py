#Elabore un programa que procese las calificaciones de varios estudiantes de la carrera de
#Ingeniería en Sistemas de la Información en la UAM. Por cada estudiante, se ingresarán las
#calificaciones de tres asignaturas, y cada asignatura incluirá tres tareas y un examen. El
#programa debe calcular el promedio por asignatura y el promedio general del estudiante. Utilice
#estructuras cíclicas anidadas para manejar estudiantes, asignaturas y evaluaciones.

def promedio():
    estudiantes = 3
    asignaturas = 3
    tareas = 3
    examen = 1  
    total_calificaciones = 0
    for estudiante in range(estudiantes):
        print(f"A continuacion te preguntare las calificaciones del estudiante {estudiante+1}")
        for asignatura in range(asignaturas):
            print(f"A continuacion te preguntare las calificaciones de la asignatura {asignatura+1}")
            for tarea in range(tareas):
                calificacion = float(input(f"Dime la calificacion de la tarea {tarea+1}: "))
                total_calificaciones += calificacion
            for exa in range(examen):
                calificacion = float(input(f"Dime la calificacion del examen: "))
                total_calificaciones += calificacion
            promedio_asignatura = total_calificaciones / (tareas + examen)
            print(f"El promedio de la asignatura {asignatura+1} es: {promedio_asignatura}")
            total_calificaciones = 0
        promedio_general = total_calificaciones / (asignaturas * (tareas + examen))
        print(f"El promedio general del estudiante {estudiante+1} es: {promedio_general}")
        total_calificaciones = 0
promedio()


 
    

    
    
    
         