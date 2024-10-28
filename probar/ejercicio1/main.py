from os import system
system("cls")

from ejercicio1.auxiliares import *
from ejercicio1.funciones import *

depositos = ["PBA", "Jujuy", "Neuquén"]

articulos = [
    "químicos", "trapos", "escobas",
    "cepillos", "papel higiénico", 
    "jabón", "pañuelos descartables"
]

existencias = [
    [1000, 500, 300, 20000, 5570000, 8000, 600],   # PBA
    [700, 40550, 35800, 250, 12000, 6500, 500],    # Jujuy
    [500, 300, 25000, 150, 900, 500, 4800000]      # Neuquén
]
#[12, 25, 23, 45, 52, 10, 35]
ventas = [
    [100, 200, 150, 50, 80, 40, 60],  # PBA
    [150, 250, 100, 100, 50, 100, 50], # Jujuy
    [200, 300, 120, 150, 100, 100, 80]  # Neuquén
]
ejecutar = True
carga = False

while ejecutar == True:
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    opcion = input(f"""
                                MENÚ PRINCIPAL
        ===========================================================
        1. Obtener existencias
        2. Cantidad total de artículos almacenados en cada depósito.
        3. Obtener nombres de artículos a reponer en cada depósito.
        4. Máxima cantidad de artículos almacenados de cada tipo.
        5. Corregir un error de carga.
        6. Cantidad de depósitos que tenga más de 3.000.000 de unidades
        7. Porcentaje de artículos.
        8. Informe con la recaudación de cada depósito.
        9. Depósito con mayor recaudación.
        10. Salir
        Ingrese una opción (1 al 10): """)
    
    while opcion not in  numeros:
        opcion = input("\t\tError!!. Ingrese una opción (1 al 10): ")
    opcion = int(opcion)
    
    match opcion:
        case 1:
            existencias = inicializar_matriz(len(depositos), len(articulos), 0)
            mostrar_matriz(existencias, "existencias")
                
            carga_cantidades = carga_secuencial(existencias, "Cantidad", depositos, articulos)
            mostrar_matriz(existencias, "existencias")
        case 2:
            total = calcular_totales(existencias)
            print(f"\nCANTIDAD TOTAL DE ARTÍCULOS EN CADA DEPÓSITO:\n" + "=" * 40)
            
            for i in range(len(total)):
                print(f"Total de artículos en {depositos[i]}: {total[i]}")
        case 3:
            print("""\n\t\tNOMBRES DE ARTÍCULOS A REPONER POR DEPÓSITO 
            \t=========================================""")
            reponer(existencias, depositos, articulos, 3000)
        case 4: 
            print("""
                        \n\t\tARTÍCULO CON MAYOR CANTIDAD EN CADA DEPÓSITO
            =====================================================""")
            for i in range(len(existencias[0])):
                flag_maximo = True
                for j in range(len(existencias)):
                    if flag_maximo == True:
                        maximo = existencias[j][i]
                        deposito = depositos[j]
                        flag_maximo = False
                    elif existencias[j][i] > maximo:
                        maximo = existencias[j][i]
                        deposito = depositos[j]
                print(f"\t\tArtículo {articulos[i]} hay más en {deposito}: {maximo}")
        case 5:
            print("""\n\t\t\tMODIFICAR ERROR DE CARGA 
            ====================================================""")
            corregir_error(existencias, depositos, articulos)
            mostrar_matriz(existencias, "existencias_modifcada")
        case 6:
            print("""
                        \n\t\tCANTIDAD DE DEPÓSTO(S) QUE TENGAN MÁS DE 3.000.000
                ===================================================""")
            total = calcular_totales(existencias)
            mayor = 3000000
            flag_deposito_mayor = False
            
            for i in range(len(total)):
                if total[i] > mayor:
                    print(f"\t\t {depositos[i]}: {total[i]}")
                    flag_deposito_mayor = True
                    
            if flag_deposito_mayor == False:
                print("\t\tNo hay depósitos con más de 3.000.000 unidades")
        case 7:
            porcentajes = calcular_porcentajes(existencias, articulos)
        case 8:
            """ventas = inicializar_matriz(len(depositos), len(articulos))
            mostrar_matriz(existencias, "ventas")
            #carga de ventas
            carga_ventas = carga_secuencial(ventas, "Ventas", depositos, articulos)
            mostrar_matriz(existencias, "ventas")"""
            
            informar = informar_deposito(ventas, depositos)
            print(f"\t INFORME DE LAS RECAUDACIONES POR DEPÓSITO\n\t" + "=" * 45)
            for i in range(len(informar[0])):
                print(f"\t\t{informar[0][i]}: ${informar[1][i]}")  
        case 9:
            recauda_mas = mayor_recaudacion(ventas, depositos)
            print(f"\n\tDEPÓSITO CON MAYOR RECAUDACIÓN\n\t" + "=" * 30)
            print(f"\t\t{recauda_mas[0]}: ${recauda_mas[1]}") 
        case 10:
            print("\tGracias por usar nuestro sistema.")
            ejecutar = False

            
    
    