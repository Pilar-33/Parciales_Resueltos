def inicializar_matriz(
    cantidad_filas: int, cantidad_columnas: int, 
    valor_inicial: any = 0) -> list:
    
    """
    Crea una matriz de filas y columnas con el valor inicial especificado
    Devuelve una matriz de listas.
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz


def validar_numero(mensaje: str) -> int:
    """
    Pide al usuario un número entero y valida que sea mayor que cero.
    Devuelve el número entero introducido.
    """
    valida = True
    while valida == True:
        es_valido = True
        entrada = input(mensaje)

        for caracter in entrada:
            if caracter < "0" or caracter > "9":
                es_valido = False
                break

        if es_valido == True and len(entrada) > 0:
            return int(entrada)
        else:
            print("Error!!. Debe ingresar un número entero.")

def mostrar_matriz(matrices: list, tipo: str) -> None:
    """
    Muestra la matriz
    Devuelve None"""
    
    print(f"{tipo} = [")
    for matriz in matrices:
        print(f"    {matriz},")
    print("]")
