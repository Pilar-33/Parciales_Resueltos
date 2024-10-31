# Carga de datos
def cargar_datos() -> list:
    # Ciclo para seguir pidiendo el dato hasta que sea un entero positivo mayor que cero
    n = input("Cuántos datos desea cargar: ")
    while True:
        es_valido = True  # Bandera para saber si es un número válido
        
        # Verifica si la entrada no está vacía
        if len(n) == 0:
            es_valido = False
        
        # Verifica cada carácter
        for caracter in n:
            if caracter < '0' or caracter > '9':  # Si hay una letra o símbolo
                es_valido = False
                break
        
        # Verifica si el número es mayor que cero
        if es_valido and n != "0":
            break  # Si es válido y mayor que 0, sale del ciclo
        
        # Si no es válido, pide nuevamente la entrada
        n = input("Error!!! Cuántos datos desea cargar (debe ser número positivo mayor que cero): ")
    n = int(n)  # Convierte el valor a entero después de validar
    
    inventario = []
    #Carga de datos secuencial
    print("      CARGA DE DATOS\n" + "=" * 30)
    for i in range(n):
        nombre = input(f"Nombre del producto no{i+1}: ")
        
        precio = float(input(f"Precio del producto no{i+1}: "))
        while precio < 0:
            precio = float(input(f"Error!!. Precio del producto no{i+1}: "))
        
        cantidad = int(input(f"Cantidad del producto no{i+1}: "))
        while cantidad < 0:
            cantidad = int(input(f"Error!!. Cantidad del producto no{i+1}: "))
        inventario += [[nombre, precio, cantidad]]
    return inventario

# Función buscar pruducto       
def buscar_producto(carga_datos) -> list:
    encontrado = []
    producto_buscar = input("Ingrese el nombre del producto a buscar: ")
    for producto in carga_datos:
        if producto[0] == producto_buscar:
            encontrado = [producto[0], producto[1], producto[2]]
            break
    if encontrado:
        return encontrado
    else:
        print("Producto no encontrado.")
        return None

# Función Ordenar
def ordenar_datos(carga_datos: list) -> list:
    n = len(carga_datos)
    for i in range(n):
        for j in range(n - i - 1):
            if carga_datos[j][1] > carga_datos[j + 1][1]:
                menor = carga_datos[j + 1][1]
                carga_datos[j + 1][1] = carga_datos[j][1]
                carga_datos[j][1] = menor
    lista_ordenada = carga_datos
    return lista_ordenada

def mostrar_producto_caro_barato(carga_datos: list) -> list:
    producto_caro = carga_datos[0]
    producto_barato = carga_datos[0]
    caro_barato = []
    for producto in carga_datos:
        if producto[1] > producto_caro[1]:
            producto_caro = producto
            
        if producto[1] < producto_barato[1]:
            producto_barato = producto
    caro_barato = [producto_caro, producto_barato]
    
    return caro_barato

def evaluar_precios_altos(carga_datos: list) -> list:
    precio_alto = [] 
    for precio in carga_datos:
        if precio[1] > 15000:
            precio_alto += [precio]
    return precio_alto
            
        

        
            
        