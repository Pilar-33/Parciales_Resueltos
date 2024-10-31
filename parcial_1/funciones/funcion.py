
def validar_numero_entero(mensaje):
    while True:
        entrada = input(mensaje) 
        es_valido = True
        if len(entrada) == 0:
            es_valido = False
            
        for i in entrada:
            if i < '0' or i > '9':
                es_valido = False
                break
        
        if es_valido and entrada != 0:
            return int(entrada)
        
        print("Error!!!. Número entero positivo")

def validar_texto(mensaje):
    while True:
        entrada = input(mensaje)
        es_valido = True
        if len(entrada) == 0:
            es_valido = False
            
        for caracter in entrada:
            if (caracter < 'A' or caracter > 'Z') and (caracter < 'a' or caracter > 'z') and caracter != " ":
                es_valido = False
                break
        
        if es_valido and entrada != 0:
            return entrada
        
        print("Error!!!. Solo se permiten letras: ")
        
# Buscar paciente por número de Historia Clinica.
def buscar_paciente(pacientes: list) -> None:
    while True:
        nro_clinica = validar_numero_entero("Nro de Historia Clínica a buscar: ")
        paciente_encontrado = False
        
        for paciente in pacientes:
            if paciente[0] == nro_clinica:
                print(f"""
                            PACIENTE ENCONTRADO
                    ==============================
                    Nro de Historia Clínica: {paciente[0]}
                    Nombre: {paciente[1]}
                    Edad: {paciente[2]}
                    Diagnóstico: {paciente[3]}
                    Días de hospitalización: {paciente[4]}""")
                paciente_encontrado = True
                break
        
        if not paciente_encontrado:
            print("No hay paciente registrado para la operción solicitada.")
            
        consulta = input("Desea hacer otra busqueda (s/n)?: ")
        while consulta not in ["N", "n", "S", "s"]:
            consulta = input("Debe ingresar (s/n). Desea hacer otra busqueda?: ")
        
        if consulta in ["N", "n"]:
            break
        
def oredenar_x_historia_clinica(pacientes: list) -> list:
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pacientes[j][0] > pacientes[j + 1][0]:
                paciente_aux = pacientes[j + 1]
                pacientes[j + 1] = pacientes[j]
                pacientes[j] = paciente_aux
    paciente_ordenado = pacientes
    return paciente_ordenado

def internar_mas_dias(pacientes: list) -> None:
    mas_dias = pacientes[0][4]
    paciente_mas_dias = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > mas_dias:
            mas_dias = paciente[4]
            paciente_mas_dias = paciente
    print(f"""
            PACIENTE CON MAYOR DÍAS DE HOSPITALIZACIÓN
    ========================================================
        Nro de Historia Clínica: {paciente_mas_dias[0]}
        Nombre: {paciente_mas_dias[1]}
        Edad: {paciente_mas_dias[2]}
        Diagnóstico: {paciente_mas_dias[3]}
        Días de hospitalización: {paciente_mas_dias[4]}""")
    
def internar_menos_dias(pacientes: list) -> None:
    menos_dias = pacientes[0][4]
    paciente_pocos_dias = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < menos_dias:
            menos_dias = paciente[4]
            paciente_pocos_dias = paciente
    print(f"""
            PACIENTE CON MENOS DÍAS DE HOSPITALIZACIÓN
    ========================================================
        Nro de Historia Clínica: {paciente_pocos_dias[0]}
        Nombre: {paciente_pocos_dias[1]}
        Edad: {paciente_pocos_dias[2]}
        Diagnóstico: {paciente_pocos_dias[3]}
        Días de hospitalización: {paciente_pocos_dias[4]}""")

def listar_pacientes_mayor_5dias(pacientes: list) -> list:
    lista_mayor_5dias = []
    for paciente in pacientes:
        if paciente[4] > 5:
            lista_mayor_5dias += [paciente]
    return lista_mayor_5dias

def promedio_dias_internacion(pacientes: list) -> int:
    total_dias = 0
    for i in pacientes:
        total_dias += i[4]
    promedio = total_dias / len(pacientes)
    return promedio
    
            

            
    
        
                
                
                
        