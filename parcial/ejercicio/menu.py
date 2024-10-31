from funciones import *

def menu(existencias, depositos, tipo_articulos) -> None:
    while True:
        numeros = ["1", "2", "3", "4", "5", 
                "6", "7", "8", "9", "10",]
        opcion = input("""
                                MENÚ PRINCIPAL
        ==============================================================
        1. Mostrar existencias.
        2. Cantidad de artículos almacenados entre todos 
            los tipos(cada depósito).
        3. Obtener nombres de artículos a reponer menos 
            de 3000 unidades.
        4. Máxima cantidad de artículos almacenados por cada tipo
            en cada provincia.
        5. Corregir un error de cargs.
        6. Cantidad de depósitos que hayan almacenado más de 3000000
            de unidades entre los 7 artículos. Mostrar por provincias.
        7. Porcentaje de articulos de cada tipo
        8. Generara informe con la recaudación de cada depósito.
        9. Depósito con mayor recaudación.
        10. Salir.
        Ingrese una opción(1 al 10): """)
        while opcion not in numeros:
            opcion = input("Error!!!. Ingrese número válido(1 al 10): ")
        
        opcion =  int(opcion)
        
        match opcion:
            case 1: 
                print("\nCANTIDADES DE LOS PRODUCTOS\n" + "=" * 30)
                print("existencias = [")
                for existencia in existencias:
                    print(f"    {existencia},")
                print("]")
            case 2:
                cantidades = calcular_cantidad_total(existencias, depositos)
                print("\n\tCANTIDAD TOTAL DE ARTÍCULOS POR DEPÓSITO\n" + "=" * 55)
                for i in range(len(cantidades)):
                    print(f"Cantidad total del depósito {depositos[i]}: {cantidades[i]}")
            case 3:
                repone = reponer_x_deposito(existencias, depositos, tipo_articulos)
                #mostrar 1
                print("reponer = [")
                for cantidad in repone:
                    print(f"    {cantidad},")
                print("]")
                
                # mostrar 2
                for deposito in depositos:
                    print(f"\nArtículos a reponer del depósito {deposito}\n" + "=" * 40)
                    for item in repone:
                        if item[0] == deposito:
                            print(f"Artículo: {item[1]}, Cantidad: {item[2]}")
            case 4:
                cantidad_maxima = encontrar_maxima_cantidad(existencias, depositos, tipo_articulos)
                for deposito in depositos:
                    print(f"\nCantidad máxima de artículos de {deposito}\n" + "=" * 40)
                    for item in cantidad_maxima:
                        if item[0] == deposito:
                            print(f"Tipo: {item[1]}, Cantidad: {item[2]}")
            case 5:
                corregir_carga(existencias, depositos, tipo_articulos)
                
        rpta = ["S", "s", "N", "n"]
        continuar = input("Desea continuar?(s/n): ")
        while continuar not in rpta:
            continuar = input("Error!!!. Desea continuar? (s/n): ")
            
        if continuar in ["N", "n"]:
            print("Gracias por usar nuestro sistema!!!")
            break
        
        
        
        
        