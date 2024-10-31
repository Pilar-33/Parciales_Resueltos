from os import system
system("cls")

from funciones.funcion import *
from funciones.menu import *

# Carga de datos
pacientes = [
    [109, "Juan Pérez", 30, "Gripe", 5],
    [108, "María López", 25, "Fractura de brazo", 10],
    [103, "Carlos García", 40, "Diabetes", 15],
    [104, "Ana Fernández", 35, "Asma", 3],
    [105, "Pedro Martínez", 50, "Hipertensión", 8],
    [110, "Laura Sánchez", 28, "COVID-19", 20],
    [107, "Jorge Rodríguez", 45, "Neumonía", 12],
    [102, "Lucía Gómez", 22, "Migraña", 7],
    [101, "Roberto Díaz", 33, "Cáncer", 25],
    [106, "Claudia Morales", 38, "Anemia", 4]
]

"""nro_pacientes = validar_numero_entero("Cantidad de pacientes: ")
pacientes = []
for i in range(nro_pacientes):
    nro_historia = validar_numero_entero(f"Número de historia clínica nro{i + 1}: ")
    nombre_paciente = validar_texto(f"Nombre del paciente nro{i + 1}: ")
    edad_paciente = validar_numero_entero(f"Edad del paciente nro{i + 1}: ")
    diagnostico = validar_texto(f"Diagnostico nro{i + 1}: ")
    dias_internacion = validar_numero_entero(f"Cantidad de días de internación nro{i + 1}: ")
    pacientes += [[nro_historia, nombre_paciente, edad_paciente, diagnostico, dias_internacion]]"""

menu(pacientes)