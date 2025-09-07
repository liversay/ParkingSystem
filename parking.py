import datetime
import random

CAPACIDAD_MAXIMA = 100
TARIFA_POR_HORA = 2.50

espacios_ocupados = 0
placas_estacionadas = []
eventos_parqueo = []
historial_autos = []

""" funciones principales """

def calcular_porcentaje_ocupacion():
    return (espacios_ocupados / CAPACIDAD_MAXIMA) * 100

def obtener_estado_parqueo():
    porcentaje = calcular_porcentaje_ocupacion()

    if porcentaje >= 90:
        return "lleno"
    elif porcentaje >= 50:
        return "medio ocupado"
    else:
        return "disponible"
    
def mostrar_estado_parqueo():
    espacios_libres = CAPACIDAD_MAXIMA - espacios_ocupados
    porcentaje = calcular_porcentaje_ocupacion()
    estado = obtener_estado_parqueo()

    print(f"⁄n--- ESTADO DEL PARKING ---")
    print(f"Espacios ocupados: {espacios_ocupados}/{CAPACIDAD_MAXIMA}")
    print(f"Espacios libres: {espacios_libres}")
    print(f"Estado: {estado.upper()}")