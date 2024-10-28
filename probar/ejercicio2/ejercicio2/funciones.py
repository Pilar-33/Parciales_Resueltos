
from ejercicio2.auxiliares import *

def reponer(existencias: list, depositos: list, 
        juguetes: list, minimo: int = 500) -> None:
    """
    Obtiene los juguetes que tienen menos de 500 unidades.
    """
    for i  in range(len(existencias)):
        print(f"\t\tReponer del depósito {depositos[i]}:")
        for j  in range(len(existencias[0])):
            if existencias[i][j] <  minimo:
                print(f"\t\t* {juguetes[j]}")
        print()
        
def recaudacion(ventas: list,
        valores: list = [10, 8, 15, 20, 30, 25]) -> list:
    """
    Calcula las recudaciones de cada deposito.
    Devuelve lista con las recaudaciones de cada depósito.
    """
    recaudacion = [0] * len(ventas)
    for i in range(len(ventas)):
        calcula = 0
        for j  in range(len(ventas[i])):
            calcula += (ventas[i][j] * valores[j])
        recaudacion[i] = calcula
    return recaudacion

def calcular_totales(existencias: list) -> list:
    """
    Calcula la cantidad total de existencias por depósito.
    Devuelve la lista con los totales de cada depósito.
    """
    total = []
    for i in range(len(existencias)):
        suma = 0
        for j in range(len(existencias[0])):
            suma += existencias[i][j]
        total += [suma]
    return total

def calcular_porcentajes(existencias: list, juguetes: list) -> None:
    """
    Calcula los porcentajes de los juguetes por tipo.
    Imprime los porcentajes de cada juguete."""
    suma_total = 0
    total = []
    for i in range(len(existencias[0])):
        suma = 0
        for j in range(len(existencias)):
            suma += existencias[j][i]
            suma_total += existencias[j][i]
        total += [suma]
    
    print(f"""
                PORCENTAJES DE CADA JUGUETE
                ============================""")
    for i in range(len(total)):
        porcentaje = (total[i] / suma_total) * 100
        print(f"\t\t* {juguetes[i]}: {porcentaje:.2f}%")

#Insertsort    
def ordenar_recaudacion(ventas: list, depositos: list) -> list:
    """
    Ordena las recaudaciones de mayor a menor.
    Devuelve una lista con los depositos y las recaudaciones ordenadas.
    """
    
    recauda = recaudacion(ventas)
    informe = []
    #print(recaudacion)
    #[15850, 40400, 48750, 40300, 132500]
    for i in range(1, len(recauda)):
        aux_recaudacion = recauda[i]
        aux_deposito = depositos[i]
        j = i - 1
        while j >= 0 and aux_recaudacion > recauda[j]:
            recauda[j + 1] = recauda[j]
            depositos[j + 1] = depositos[j]
            j -= 1
        recauda[j + 1] = aux_recaudacion
        depositos[j + 1] = aux_deposito
    informe += [depositos, recauda]
    return informe

def corregir_error(
    existencias: list, depositos: list, juguetes: list) -> None:
    """
    Permite hacer modificaciones en la mátriz existencias.
    Imprime mensaje cuando ya se hizo la modificación en 
    la mátriz existencias.
    """
    ejecutar = True
    while ejecutar == True:
        deposito = input(f"\t\tNombre del depósito: ")
        deposito_encontrado = False
        for i  in range(len(depositos)):
            if deposito == depositos[i]:
                deposito_encontrado = True
                indice_deposito = i
                break
        if deposito_encontrado == False:
            print("\t\tError. Depósito no encontrado.")
            continue
        
        juguete = input(f"\t\tNombre del juguete: ")
        juguete_encontrado = False
        for j in range(len(juguetes)):
            if juguete == juguetes[j]:
                juguete_encontrado = True
                indice_juguete = j
                break
        if juguete_encontrado == False:
            print("\tError. Juguete no válido.")
            continue
        
        cantidad_corregir = validar_numero(f"\t\tNueva cantidad del juguete: ")
        existencias[indice_deposito][indice_juguete] = cantidad_corregir
        
        print(
            f"\t\t{depositos[indice_deposito]} se modificó de "
            f"{juguetes[indice_juguete]}: " 
            f"{existencias[indice_deposito][indice_juguete]}")
        
        continuar = input("\t\tDesea corregir otro dato?(s/n): ")
        while continuar not in ["N", "n", "s", "S"]:
            print("\t\tError. Opción no válida.")
            continuar = input("\t\tDesea corregir otro dato?(s/n): ")
        
        if continuar in ["n", "N"]:
            print("\t\tCorregido el error en las existencias.")
            ejecutar = False
            
    