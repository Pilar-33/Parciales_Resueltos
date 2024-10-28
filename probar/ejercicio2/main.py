from os import system
system("cls")

from ejercicio2.auxiliares import*
from ejercicio2.funciones import *

depositos = ["PBA", "CABA", "Chubut", 
            "Tucumán", "Mendoza"]

juguetes = [
    "autos", "muñecas", "trenes",
    "peluches", "spinners", "cartas"
]

"""existencias = [
    [1000, 20000, 800, 4000, 5000, 300],
    [150, 2500, 3500, 45000, 550, 1200],
    [2000, 3000, 600, 5000, 900, 12300],
    [250, 35000, 4500, 550, 6050, 4500],
    [1000, 4000, 50000, 600, 70, 20000]
]"""

ventas = [
    [1000, 200, 80, 40, 50, 30],
    [150, 2500, 350, 450, 55, 120],
    [200, 300, 60, 500, 90, 1230],
    [25, 350, 450, 55, 605, 450],
    [100, 400, 5000, 60, 70, 2000]
]

#valores_unidad = [10, 8, 15, 20, 30, 25]
ejecutar = True

while ejecutar == True:
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    opcion = input(f"""
                                MENÚ PRINCIPAL
        ============================================================
        1. Obtener existencias.
        2. Cantidad total de juguetes almacenados en cada depósito.
        3. Nombres de los juguetes que es necesario reponer en cada depósito.
        4. Máxima cantidad de artículos almacenados de cada tipo.
        5. Depósito con mayor recaudación.
        6. Cantidad de depósitos que hayan almacenado más de 50.000 unidades
        7. Porcentaje de artículos.
        8. Generar un informe con la recaudación de cada depósito.
        9. Corregir un error de carga
        10. Salir.
        Elija una opción (1 a 10): """)
    
    while opcion not in numeros:
        opcion = input("Opción no válida. Ingrese una opción (1 a 10): ")
    
    opcion = int(opcion)
    
    match opcion:
        case 1:
            existencias = inicializar_matriz(len(depositos), len(juguetes))
            mostrar_matriz(existencias, "existencias")
            
            #cargando existencias
            for i in range(len(depositos)):
                print(f"""
                    CARGANDO EXISTENCIAS DEL DEPÓSITO {depositos[i]}
                ===================================================""")
                for j in range(len(juguetes)):
                    cantidad = validar_numero(f"\t\t    Cantidad de {juguetes[j]}: ")
                    existencias[i][j] = cantidad
                    
            mostrar_matriz(existencias, "existencias")
        case 2:
            suma = 0
            total = []
            for i in range(len(depositos)):
                for j in range(len(existencias[i])):
                    suma += existencias[i][j]
                total += [suma]
            
            # mostar información
            print(f"""\n
                    TOTAL DE JUGUETES POR DEPÓSITO
                =========================================""")
            for i in range(len(depositos)):
                print(f"\t\tTotal de juguetes en {depositos[i]}: {total[i]} unidades.")
        case 3:
                print("""\n\t\tNOMBRES DE JUQUETES A REPONER POR DEPÓSITO 
            ====================================================""")
                reponer(existencias, depositos, juguetes, 500)
        case 4: 
            print("""
                        \n\t\tJUGUETES CON MAYOR CANTIDAD EN CADA DEPÓSITO
            =====================================================""")
            for i in range(len(existencias[0])):
                flag_maxima = True
                for j in range(len(existencias)):
                    if flag_maxima == True:
                        maximo = existencias[j][i]
                        deposito = depositos[j]
                        flag_maxima = False
                    elif existencias[j][i] > maximo:
                        maximo = existencias[j][i]
                        deposito = depositos[j]
                print(f"\t\tHay más {juguetes[i]} em el depósito {deposito}: {maximo}")
        case 5:
            #ventas = inicializar_matriz(len(depositos), len(juguetes))
            #mostrar_matriz(ventas, "ventas")
            
            #cargando ventas
            #for i in range(len(depositos)):
                #print(f"""
                    #CARGANDO VENTAS DEL DEPÓSITO {depositos[i]}
                #===================================================""")
                #for j in range(len(juguetes)):
                    #cantidad1 = validar_numero(f"    \t\tVentas de {juguetes[j]}: ")
                    #ventas[i][j] = cantidad1
            #mostrar matriz cargada de ventas
            #mostrar_matriz(ventas, "ventas")
            
            # Usando matriz cargada para no cargar en todas las pruebas
            recauda = recaudacion(ventas)
            print(f"\t reacaudaciones: {recauda}")
            flag_maxima = True
            for i in range(len(recauda)):
                if flag_maxima == True:
                    deposito_maximo = recauda[i]
                    deposito = depositos[i]
                    flag_maxima = False
                elif recauda[i] > deposito_maximo:
                    deposito_maximo = recauda[i]
                    deposito = depositos[i]
            print(
                f"\n                    DEPÓSITO CON MAYOR RECAUDACIÓN\n"
                f"  ================================================================\n"
                f"  \tÉl déposito {deposito} con mayor recaudación: ${deposito_maximo}"
                )
        case 6:
            total = calcular_totales(existencias)
            print(f"""
                    \n\t\tDEPÓSITOS QUE HAN ALMACENADO MÁS DE 50.000 UNIDADES
                =====================================================""")
            mayor = 50000
            flag_50000 = False
            for i in range(len(total)):
                if total[i] > mayor:
                    print(f"\t\t{depositos[i]}: {total[i]} unidades")
                    flag_50000 = True
            
            if flag_50000 == False:
                print("\t\tNo hay depósitos que hayan almacenado más de 50.000 unidades")
        case 7: 
            calcular_porcentajes(existencias, juguetes)
        case 8:
            informar = ordenar_recaudacion(ventas, depositos)
            print("\nINFORME CON LA RECAUDACIÓN DE CADA DEPÓSITO\n" + "=" * 45)
            for i in range(len(informar[0])):
                print(f"{informar[0][i]} recaudó: {informar[1][i]}")
        case 9:
            print("""\n\t\t\tMODIFICAR ERROR DE CARGA 
            ====================================================""")
            corregir_error(existencias, depositos, juguetes)
            mostrar_matriz(existencias, "existencias_corregida")
        case 10:
            ejecutar = False
            print("\tSaliendo del programa...")
            print("\tGracias por su preferencia.")
            break

