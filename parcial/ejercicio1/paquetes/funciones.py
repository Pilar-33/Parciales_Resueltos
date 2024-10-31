
def validar_numero(mensaje) -> int:
    while True:
        es_valido = True
        entrada = input(mensaje)
        
        if len(entrada) == 0:
            es_valido = False
            
        for i in entrada:
            if i < '0' or i > '9':
                es_valido = False
                break
        
        if es_valido and entrada != 0:
            return int(entrada)
        
        print("Error!!!. Solo se permiten números enteros: ")
        
def sumar_cantidad_articulos(existencias: list, tipo_depositos: list) -> list:
    cantidad_PBA = 0
    cantidad_Jujuy = 0
    cantidad_Neuquen = 0
    totales_depositos =[]
    for cantidad in existencias:
        if cantidad[0] == tipo_depositos[0]:
            cantidad_PBA += cantidad[2]
        elif cantidad[0] == tipo_depositos[1]:
            cantidad_Jujuy += cantidad[2]
        elif cantidad[0] == tipo_depositos[2]:
            cantidad_Neuquen += cantidad[2]
    totales_depositos = [cantidad_PBA, cantidad_Jujuy, cantidad_Neuquen]
    return totales_depositos

def reponer_cada_deposito(existencias: list, tipo_depositos: list) -> list:
    reponer = []
    for existencia in existencias:
        if existencia[0] == tipo_depositos[0]:
            if existencia[2] < 3000:
                reponer += [[tipo_depositos[0], existencia[1], existencia[2]]]
        elif existencia[0] == tipo_depositos[1]:
            if existencia[2] < 3000:
                reponer += [[tipo_depositos[1], existencia[1], existencia[2]]]
        elif existencia[0] == tipo_depositos[2]:
            if existencia[2] < 3000:
                reponer += [[tipo_depositos[2], existencia[1], existencia[2]]]
    return reponer
            
def articulos_por_deposito(existencias: list, tipo_articulos: list) -> list:
    resultados = []
    
    for tipo in tipo_articulos:
        max_cantidad = 0
        provincia_max = ""
        
        for existencia in existencias:
            if existencia[1] == tipo:
                if existencia[2] > max_cantidad:
                    max_cantidad = existencia[2]
                    provincia_max = existencia[0]
        
        # Guardar el resultado en la lista
        resultados += [[provincia_max, tipo, max_cantidad]]
    return resultados

def contar_depositos_con_mas_de_3_millones(existencias: list, depositos: list):
    total_unidades = [0] * len(depositos)  # Inicializamos un contador para cada depósito

        
    # Sumar las unidades de cada depósito
    for i in range(len(existencias)):
        for j in range(len(depositos)):
            if existencias[i][0] == depositos[j]:
                total_unidades[j] += existencias[i][2]
        
    # Contar depósitos con más de 3.000.000 de unidades
    provincias = []
    for j in range(len(depositos)):
        if total_unidades[j] > 3000000:
            provincias += [depositos[j]]
        
    return provincias