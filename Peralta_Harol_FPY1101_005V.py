import math
import random
import csv
import time

trabajadores = [
    {"nombre": "Juan Pérez     ",},
    {"nombre": "María García   ",},
    {"nombre": "Carlos López   ",},
    {"nombre": "Ana Martínez   ",},
    {"nombre": "Pedro Rodríguez",},
    {"nombre": "Laura Hernández",},
    {"nombre": "Miguel Sánchez ",},
    {"nombre": "Isabel Gómez   ",},
    {"nombre": "Francisco Díaz ",},
    {"nombre": "Elena Fernández",}
]

def SueldoRandon(trabajadores):
    for Empleado in trabajadores:
        Empleado["sueldo"] = random.randint(300000, 2500000)

def ClasificarSueldo(trabajadores):
    S_800k = []
    S_800k_2M = []
    S_2_5M = []
    
    for empleado in trabajadores:
        sueldo = empleado["sueldo"]
        if sueldo < 800000:
            S_800k.append(empleado)
        elif 800000 <= sueldo <= 2000000:
            S_800k_2M.append(empleado)
        else:
            S_2_5M.append(empleado)
    
    print(f"\nSueldos de 800.000: {len(S_800k)}")
    for empleado in S_800k:
        print(f"{empleado['nombre']}:\t${empleado['sueldo']}")
        
    print(f"\nSueldos de 800.000 a 2M: {len(S_800k_2M)}")
    for empleado in S_800k_2M:
        print(f"{empleado['nombre']}:\t${empleado['sueldo']}")
        
    print(f"\nSueldos de mas de 2M: {len(S_2_5M)}")
    for empleado in S_2_5M:
        print(f"{empleado['nombre']}:\t${empleado['sueldo']}")
    
   
    S_Total = sum(empleado["sueldo"] for empleado in trabajadores)
    print(f"Total de todos los sueldos: ${S_Total}")

def Salir():
    Mensaje = "Finalizando programa..."
    Nombre = "Harol Peralta"
    Rut = "25.451.483-7"
    
    print(Mensaje)
    time.sleep(1)
    print(Nombre)
    print(Rut)
    
def ver_estadisticas(trabajadores):
    sueldos = [empleado["sueldo"] for empleado in trabajadores]
    
    S_Mx = max(sueldos)
    S_Mn = min(sueldos)
    S_Pro = sum(sueldos) / len(sueldos)

    print("\nEstadísticas de sueldos:\n")
    print(f"Sueldo mas alto es: ${S_Mx}")
    print(f"Sueldo mas bajo es: ${S_Mn}")
    print(f"Promedio de los sueldo es de: ${S_Pro}")
    

def ReportesSueldos(trabajadores):
    with open('Reportee.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])

        print("\nNombre:\tSueldo Base:\tDesc. Salud:\tDesc. AFP:\tSueldo Liquido:")
        for empleado in trabajadores:
            sueldo = empleado["sueldo"]
            Desc_Salud = sueldo * 0.07
            DescAFP = sueldo * 0.12
            S_Liquido = sueldo - Desc_Salud - DescAFP
            writer.writerow([empleado["nombre"], sueldo, Desc_Salud, DescAFP, S_Liquido])
    print("Se genero el reporte de sueldos")


def Menu():
    while True:
        try:
            print("-----------------------------------------")
            print("Reportes")
            print("-----------------------------------------")
            print("1. Asignar sueldos aleatorios")
            print("2. Clasificar sueldos")
            print("3. Ver estadísticas.")
            print("4. Reporte de sueldos")
            print("5. Salir del programa")
            print("-----------------------------------------")
            op = int(input())
            
            if op == 1:
                SueldoRandon(trabajadores)
                print("Sueldo asociado")
            elif op == 2:
                ClasificarSueldo(trabajadores)
            elif op == 3:
                ver_estadisticas(trabajadores)
            elif op == 4:
                ReportesSueldos(trabajadores)
            elif op == 5:
                Salir()
                break
        except Exception as e:
            print(f"Se produjo el siguente error: {e}")            
            
Menu()