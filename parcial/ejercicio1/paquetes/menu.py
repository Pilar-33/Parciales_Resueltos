from paquetes.funciones import *
def menu_opciones(existencias, depositos, tipo_articulos) -> None:
    """Funcion de menu de opciones.
    Devuelve un str.
    """
    while True:
        numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        opcion = input(f"""
                                    MENÚ PRINCIPAL
            =============================================================
            1. Carga de datos
            2. Calcular por cada deposito la cantidad total de artículos.
            3. Obtener los nombres de los artículos menores de 3000 unidades.
            4. Máxima cantidad de artículos almacenados de cada tipo.
            5. Corregir un error de carga.
            6. Cantidad de depósitos mas de  3.000.000.
            7. Porcentaje de artículos de cada tipo.
            8. Generar informe con la recaudación de cada depósito.
            9. Depósito con mayor recaudación.
            Ingrese una opción(1 al 9): """)
        while opcion not in numeros:
            opcion = input("Opción no válida. Ingrese una opción (1 a 9): ")
        opcion =int(opcion)
        
        match opcion:
            case 1:
                print("existencias = [")
                for existencia in existencias:
                    print(f"    {existencia},")
                print("]")
            case 2:
                cantidad = sumar_cantidad_articulos(existencias, depositos)
                print(f"""
                    CANTIDAD TOTAL DE ARTÍCULOS DE CADA DEPÓSITO
                    ============================================
                    1. Total de articulos de PBA: {cantidad[0]}
                    2. Total de artículos de Jujuy: {cantidad[1]}
                    3. Total de artículos de Neuquen: {cantidad[2]}""")  
            case 3:
                repone = reponer_cada_deposito(existencias, depositos)
                print("reponer_depositos = [")
                for falta in repone:
                    print(f"    {falta},")
                print("]")
            case 4:
                resultados = articulos_por_deposito(existencias, tipo_articulos)
                informacion_a_mostrar = ""
                for resultado in resultados:
                    informacion_a_mostrar += f"Provincia: {resultado[0]}, Tipo: {resultado[1]}, Máxima cantidad: {resultado[2]}\n" 
                print(informacion_a_mostrar)
            case 5:
                pass
            case 6:
                provincias_con_mas_de_3_millones = contar_depositos_con_mas_de_3_millones(existencias, depositos)
                # Imprimir la información
                if len(provincias_con_mas_de_3_millones) > 0:
                    print("Provincia(s) que han almacenado más de 3.000.000 de unidades: ", end = "")
                    for i in range(len(provincias_con_mas_de_3_millones)):
                        if i < len(provincias_con_mas_de_3_millones) - 1:
                            print(provincias_con_mas_de_3_millones[i], end=", ")
                        else:
                            print(provincias_con_mas_de_3_millones[i])
                else:
                    print("No hay provincias que hayan almacenado más de 3.000.000 de unidades.")
            case 7:
                pass
            case 8:
                pass
            case 9:
                print("Gracias por usar nuestro sistema!!!.")
                break
        rpta = ["N", "n", "S", "s"]
        continuar = input("Desea continuar en el programa? (s/n): ")
        while continuar not in rpta:
            continuar = input("Debe ingresar (s/n). Desea continuar?: ")
        
        if continuar in ["N", "n"]:
            print("Gracias por elejirnos!!!")
            break