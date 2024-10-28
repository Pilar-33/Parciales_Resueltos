
def mostrar_matriz(matrices: list, tipo: str) -> None:
    """
    Muestra la matriz en el formato especificado
    """
    print(f"{tipo} = [")
    for matriz in matrices:
        print(f"    {matriz}")
    print("]")
        
def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any = 0) -> list:
    """
    Inicilaiza una lista de matrices con ceros segun sea la 
    dimensión específicada.
    list: devuleve una lista.
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def carga_secuencial(matriz: list, tipo: str, lista_1: list, lista2: list) -> list:
    """
    Realiza la cragas de datos
    Devuelve la matriz con los datos cargados.
    """
    for i in range(len(matriz)):
        print(f"\nEXISTENCIAS DEL DEPÓSITO {lista_1[i]}\n" + "=" * 30)
        for j  in range(len(matriz[i])): # tipo: cantidad, ventas
            cantidad = validar_numero(f"{tipo} de {lista2[j]}: ")
            matriz[i][j] = cantidad
    return matriz

def validar_numero(mensaje: str) -> int:
    """
    Valida si el dato ingresado es un número entero.
    Devuelve el número entero ingresado por el usuario.
    """
    valida = True
    while valida == True:
        es_valido = True
        entrada = input(mensaje)
        
        for caracter in entrada:
            if caracter < '0' or caracter > '9':
                es_valido = False
                break
            
        if es_valido and len(entrada) > 0:
            return int(entrada)
        else:
            print("Error!!. Ingresar un número entero!!!.")
            


    

