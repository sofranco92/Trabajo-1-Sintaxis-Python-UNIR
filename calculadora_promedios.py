def ingresar_calificaciones():
    
    asignaturas = []
    calificaciones = []
    
    print("=== REGISTRO DE CALIFICACIONES ===")
    print("Ingrese las asignaturas y sus calificaciones (0-10)")
    print("Presione Enter sin escribir nada en 'asignatura' para terminar\n")

    while True:
        # Solicitar nombre de la asignatura
        asignatura = input("Nombre de la asignatura: ").strip()

        # Si no ingresa nada, terminar el ciclo
        if not asignatura:
            break
            
        # Solicitar calificación con validación
        while True:
            try:
                calificacion = float(input(f"Calificación de {asignatura} (0-10): "))

                # Validar que esté en el rango correcto
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10")
                    
            except ValueError:
                print("Error: Ingrese un número válido")
        
        # Agregar a los arrays
        asignaturas.append(asignatura)
        calificaciones.append(calificacion)

        print(f"{asignatura}: {calificacion}")

        # Preguntar si desea continuar
        continuar = input("\n¿Desea agregar otra asignatura? (s/n): ").lower().strip()
        if continuar not in ['s', 'si', 'sí', 'y', 'yes']:
            break
        print()
    
    return asignaturas, calificaciones

def calcular_promedio(calificaciones):
    
    if not calificaciones:
        return 0
    
    suma_total = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = suma_total / cantidad
    
    return promedio

def determinar_estado(calificaciones, umbral=5.0):
    
    aprobadas = []
    reprobadas = []
    
    for i, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
    
    indice_maxima = 0
    indice_minima = 0
    
    for i, calificacion in enumerate(calificaciones):
        if calificacion > calificaciones[indice_maxima]:
            indice_maxima = i
        if calificacion < calificaciones[indice_minima]:
            indice_minima = i
    
    return indice_maxima, indice_minima

def mostrar_resumen(asignaturas, calificaciones):
    
    print("\n" + "==================================================")
    print("           RESUMEN DE CALIFICACIONES")
    print("==================================================")

    # Verificar si hay datos
    if not asignaturas or not calificaciones:
        print("No se ingresaron asignaturas para procesar.")
        return
    
    # Mostrar todas las asignaturas con sus calificaciones
    print("\n ASIGNATURAS Y CALIFICACIONES:")
    print("-" * 30)
    for i, (asignatura, calificacion) in enumerate(zip(asignaturas, calificaciones), 1):
        print(f"{i:2d}. {asignatura:<20} : {calificacion:>5.1f}")
    
    # Calcular y mostrar promedio general
    promedio = calcular_promedio(calificaciones)
    print(f"\n PROMEDIO GENERAL: {promedio:.2f}")
    
    # Determinar estado de las asignaturas
    aprobadas, reprobadas = determinar_estado(calificaciones)

    print(f"\n ASIGNATURAS APROBADAS ({len(aprobadas)}):")
    if aprobadas:
        for indice in aprobadas:
            print(f"   • {asignaturas[indice]} - {calificaciones[indice]:.1f}")
    else:
        print("   Ninguna asignatura aprobada")

    print(f"\n ASIGNATURAS REPROBADAS ({len(reprobadas)}):")
    if reprobadas:
        for indice in reprobadas:
            print(f"   • {asignaturas[indice]} - {calificaciones[indice]:.1f}")
    else:
        print("   Ninguna asignatura reprobada")

    # Encontrar calificaciones mas altas y bajas
    indice_max, indice_min = encontrar_extremos(calificaciones)
    
    if indice_max is not None and indice_min is not None:
        print(f"\n MEJOR CALIFICACIÓN:")
        print(f"   {asignaturas[indice_max]} - {calificaciones[indice_max]:.1f}")

        print(f"\n PEOR CALIFICACIÓN:")
        print(f"   {asignaturas[indice_min]} - {calificaciones[indice_min]:.1f}")

    # Estadísticas adicionales
    print(f"\n ESTADÍSTICAS:")
    print(f"   Total de asignaturas: {len(asignaturas)}")
    print(f"   Porcentaje de aprobación: {(len(aprobadas)/len(asignaturas)*100):.1f}%")

    # Mensaje motivacional basado en el promedio
    if promedio >= 8.5:
        print(f"\n ¡Excelente rendimiento!")
    elif promedio >= 7.0:
        print(f"\n ¡Buen rendimiento!")
    elif promedio >= 6.0:
        print(f"\n ¡Rendimiento aceptable!")
    else:
        print(f"\n ¡Mal rendimiento!")

def main():
    
    print("CALCULADORA DE PROMEDIOS ESCOLARES")
    print("=============================================")
    
    try:
        # Ingresar calificaciones
        materias, calificaciones = ingresar_calificaciones()
        
        # Verificar si se ingresaron datos
        if not materias:
            print("\n  No se ingresaron materias.")
            print("El programa finalizará sin procesar datos.")
        else:
            # Mostrar resumen completo
            mostrar_resumen(materias, calificaciones)
        
    except KeyboardInterrupt:
        print("\n\n  Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"\n Error inesperado: {e}")
    
    finally:
        print("\n" + "=============================================")
        print("¡Gracias por usar la Calculadora de Promedios!")
        print("=============================================")

# Punto de entrada del programa
if __name__ == "__main__":
    main()