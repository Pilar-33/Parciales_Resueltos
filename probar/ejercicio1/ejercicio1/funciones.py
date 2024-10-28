from ejercicio1.auxiliares import *

def calcular_totales(existencias: list) ->  list:
    """
    Calcula los totales de las existencias de cada 
    depósito.
    Devuelve la lista de los totales de las existencias.
    """
    total = []
    
    for i in range(len(existencias)):
        suma = 0
        for j in range(len(existencias[0])):
            suma += existencias[i][j]
        total += [suma]
    return total
def reponer(
    existencias: list, depositos: list, 
    articulos: list, menos: int = 3000) -> None:
    """
    Busca los artículos que faltan reponer en cada depósito.
    Args:
    existencias (list): Matriz con las existencias de cada depósito.
    depositos (list): Lista con los nombres de los depósitos.
    
    Returns:
    list: Lista con los artículos que faltan reponer en cada depósito.
    """
    for i in range(len(existencias)):
        print(f"\t\tReponer del depósito {depositos[i]}:")
        for j in range(len(existencias[i])):
            if existencias[i][j] < menos:
                print(f"\t\t* {articulos[j]}")
        print()
        
#5. Generar una función que permita corregir un error de carga 
# mediante carga aleatoria o distribuida de matrices.
def corregir_error(existencias: list, depositos: list, articulos: list) -> None:
    """
    Corrige un error de carga en las matrices existencias.
    No devuelve nada, pero corrige el error en las matricez de cantidades.
    """
    ejecutar = True
    while ejecutar == True:
        corregir = input("\t\tNombre del depósito que va modificar?: ")
        deposito_encontrado = False
        for i  in range(len(depositos)):
                if corregir == depositos[i]:
                    deposito_encontrado = True
                    indice_deposito = i
                    break
        if not deposito_encontrado:
            print("\t\tError. Depósito no válido")
            continue
        
        articulo_encontrado = False
        nueva_articulo = input("\t\tNombre del artículo a modificar: ")
        for j in range(len(articulos)):
            if nueva_articulo == articulos[j]:
                articulo_encontrado = True
                indice_articulo = j
                break
        if not articulo_encontrado:
            print("\t\tError. Artículo no válido")
            continue
        
        cantidad = validar_numero("\t\tNueva cantidad del artículo: ")
        existencias[indice_deposito][indice_articulo] = cantidad
        print(
            f"\t\t{depositos[indice_deposito]} se modificó la cantidad del" 
            f"{articulos[indice_articulo]}: " 
            f"{ existencias[indice_deposito][indice_articulo]}"
        )
                    
        continuar = input("\t\tDesea modificar otro dato?(s/n): ")
        while continuar not in ["S", "s", "N", "n"]:
            print("\t\tError. Opción no válida.")
            continuar = input("\t\tDesea modificar otro dato?(s/n): ")
            
        if continuar == "N" or continuar == "n":
            print("\t\tCorregido el error en las existencias.")
            ejecutar = False

def calcular_porcentajes(existencias: list, articulos: list) -> None:
    """
    Calcular de los porcentajes de los existencias.
    Muestra los porcentajes de los existencias."""
    suma_total = 0
    total = []
    for i in range(len(existencias[0])):
        suma = 0
        for j in range(len(existencias)):
            suma += existencias[j][i]
            suma_total += existencias[j][i]
        total += [suma]
    print(total)
    print(suma_total)
    
    print(f"""
                PORCENTAJES DE CADA ARTÍCULO
            ===================================""")
    for i in range(len(total)):
        porcentaje = (total[i] / suma_total) * 100
        print(f"\t\t{articulos[i]}: {porcentaje:.2f}%")

def recaudar_deposito(
    ventas: list,  
    valor = [12, 25, 23, 45, 52, 10, 35]) -> list:
    recaudaciones = [0] * len(ventas)
    
    for i in range(len(ventas[0])):
        for j  in range(len(ventas)):
            recaudaciones[j] += ventas[j][i] * valor[i]
    return recaudaciones

def informar_deposito(ventas: list, depositos: list) -> list:
    """
    Ordena las recaudaciones de mayor a menor.
    Devuelve las recaudaciones ordenadas de mayor a menor.
    """
    recaudacion = recaudar_deposito(ventas)
    print(recaudacion)
    informe = []
    n = len(recaudacion)
    for i in range(n):
        for j in range(0, n - i - 1):
            if recaudacion[j] < recaudacion[j + 1]:
                mayor_recauda = recaudacion[j + 1]
                recaudacion[j + 1] = recaudacion[j]
                recaudacion[j] = mayor_recauda
                
                mayor_deposito = depositos[j + 1]
                depositos[j + 1] = depositos[j]
                depositos[j] = mayor_deposito
    informe += [depositos, recaudacion]
    return informe

def mayor_recaudacion(ventas: list, depositos: list) -> list:
    """
    Encuentra el dósito con mayor recaudación y su monto.
    Devuelve una lista con el nombre del depósito y su recaudación."""
    recaudacion = recaudar_deposito(ventas)
    
    print(recaudacion)
    mayor = []
    flag_mayor = True
    for i in range(len(recaudacion)):
        if flag_mayor == True:
            recaudacion_mayor = recaudacion[i]
            deposito_mayor = depositos[i]
            flag_mayor = False
        elif recaudacion[i] > recaudacion_mayor:
            recaudacion_mayor = recaudacion[i]
            deposito_mayor = depositos[i]
    mayor = [deposito_mayor, recaudacion_mayor]
    return(mayor)
    

                            