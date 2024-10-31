from os import system
system("cls")

depositos = ["PBA", "Jujuy", "Neuquén"]

articulos = [
    "químicos", "trapos", "escobas",
    "cepillos", "papel higiénico", 
    "jabón", "pañuelos descartables"
]

existencias = [
    [1000, 500, 300, 20000, 150000, 8000, 600],   # PBA
    [700, 40550, 3500, 250, 12000, 6500, 500],    # Jujuy
    [500, 300, 25000, 150, 900, 500, 400000]      # Neuquén
]

def calcular_totales(existencias: list) ->  list:
    total = []
    
    for i in range(len(existencias[0])):
        suma = 0
        for j in range(len(existencias)):
            suma += existencias[j][i]
        total += [suma]
    return total
#total = calcular_totales(existencias)
#print(total)

def sumar_existencias(existencias: list) -> int:
    total_matriz = 0
    suma = 0
    for i in range(len(existencias)):
        for j  in range(len(existencias[0])):
            suma += existencias[i][j]
        total_matriz = suma
    return total_matriz
#totales = sumar_existencias(existencias)
#print(totales)

def calcular_total_totales(existencias: list) -> None:
    suma_total = 0
    total = []
    for i in range(len(existencias[0])):
        suma1 = 0
        for j in range(len(existencias)):
            suma1 += existencias[j][i]
            suma_total += existencias[j][i]
        total += [suma1]
    print(total)
    print(suma_total)
    
    print(f"""
                PORCENTAJES DE CADA ARTÍCULO
            ===================================""")
    for i in range(len(total)):
        porcentaje = (total[i] / suma_total) * 100
        print(f"\t\t{articulos[i]}: {porcentaje:.2f}%")
    
#calcular_total_totales(existencias)

def calcular_recaudacion(existencias: list, valor: int = [12, 30, 9, 20, 16, 26, 16]) -> list:
    recaudacion = []
    for i in range(len(existencias)):
        recauda = 0
        for j  in range(len(existencias[i])):
            recauda += existencias[j][i] * valor[j]
            recaudacion[i] += recauda
    return recaudacion

#recaudacion = calcular_recaudacion(existencias)
#print(recaudacion)


def calcular_recaudacion(matriz: list, 
                    lista_precios: list = [22, 33, 5, 77, 11, 67, 40])->list:

    """
    Esta función calcula recaudación.
    Recibe una matriz con las ventas y una lista con precios de productos.
    Devuelve una lista con recaudación por depósito.     
    """ 
    lista_retorno = [0] * len(matriz)
    
    for i in range(len(matriz)):
            recaudacion = 0 
            
            for j in range(len(matriz[i])):
                recaudacion += (matriz[i][j] * lista_precios[j])
            
            lista_retorno[i] = recaudacion

    return lista_retorno

recauda = calcular_recaudacion(existencias)
print(recauda)